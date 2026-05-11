"""
ai/pipeline.py
==============
PURPOSE: Orchestrate the full end-to-end recognition pipeline.

PIPELINE FLOW:
  
  User Image
      │
      ▼
  [1] Load & Validate Image
      │  - Check format (JPEG, PNG, WebP, HEIC)
      │  - Resize if too large (memory management)
      │
      ▼
  [2] Feature Extraction (CLIP model)
      │  - Preprocess: resize to 224×224, normalize
      │  - Forward pass through Vision Transformer
      │  - Output: 512-dimensional embedding vector
      │
      ▼
  [3] Embedding Retrieval
      │  - Load stored reference embeddings from disk
      │  - Shape: (N, 512) for N reference images
      │
      ▼
  [4] Cosine Similarity Matching
      │  - Compute similarity: query × stored^T
      │  - Aggregate per landmark (take MAX)
      │  - Find best-scoring landmark
      │
      ▼
  [5] Threshold Decision
      │  - score ≥ threshold → RECOGNIZED
      │  - score < threshold → NOT RECOGNIZED
      │
      ▼
  [6] Fetch Landmark Data (MongoDB)
      │  - Get description, history, gallery images
      │
      ▼
  Final Result (JSON)
"""

import logging
import time
import io
from PIL import Image
from typing import Optional
from dataclasses import dataclass, field

from ai.model import CLIPFeatureExtractor
from ai.embeddings import get_embedding_store
from ai.similarity import get_matcher, MatchResult

logger = logging.getLogger(__name__)


@dataclass
class RecognitionResult:
    """
    The final structured result returned to the frontend.
    """
    # Core recognition output
    recognized: bool
    landmark_name: Optional[str]
    confidence: float                    # 0–100 percentage
    raw_similarity: float                # 0.0–1.0
    
    # Landmark details (from database, populated after recognition)
    description: str = ""
    historical_facts: list[str] = field(default_factory=list)
    location: str = ""
    built_year: Optional[str] = None
    gallery_images: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    
    # Debug / transparency info
    all_scores: dict = field(default_factory=dict)  # All landmark scores
    processing_time_ms: float = 0.0
    model_used: str = "CLIP ViT-B-32"
    
    def to_dict(self) -> dict:
        return {
            "recognized": self.recognized,
            "landmark_name": self.landmark_name,
            "confidence": self.confidence,
            "raw_similarity": self.raw_similarity,
            "description": self.description,
            "historical_facts": self.historical_facts,
            "location": self.location,
            "built_year": self.built_year,
            "gallery_images": self.gallery_images,
            "tags": self.tags,
            "all_scores": self.all_scores,
            "processing_time_ms": self.processing_time_ms,
            "model_used": self.model_used,
        }


class RecognitionPipeline:
    """
    Main pipeline: orchestrates model, embeddings, similarity, and database.
    
    Usage:
        pipeline = RecognitionPipeline()
        result = await pipeline.recognize(image_bytes)
    """
    
    def __init__(self):
        # Load the CLIP model (singleton — loaded once, shared across requests)
        self.extractor = CLIPFeatureExtractor.get_instance()
        
        # Load the embedding store (precomputed reference embeddings)
        self.embedding_store = get_embedding_store()
        
        # Initialize the similarity matcher
        self.matcher = get_matcher()
        
        logger.info("🚀 Recognition pipeline initialized and ready")
    
    async def recognize(self, image_data: bytes) -> RecognitionResult:
        """
        Main entry point: takes raw image bytes, returns recognition result.
        
        Args:
            image_data: Raw bytes of the uploaded image file
        
        Returns:
            RecognitionResult with landmark info or "not recognized"
        """
        start_time = time.time()
        
        # ── Step 1: Validate & load image ──────────────────────────────────
        image = self._load_and_validate_image(image_data)
        
        # ── Step 2: Check if embeddings are loaded ──────────────────────────
        if not self.embedding_store.is_loaded:
            loaded = self.embedding_store.load()
            if not loaded:
                return RecognitionResult(
                    recognized=False,
                    landmark_name=None,
                    confidence=0.0,
                    raw_similarity=0.0,
                    description="Embedding database not found. Please run build_embeddings.py first.",
                    processing_time_ms=0.0
                )
        
        # ── Step 3: Extract embedding from uploaded image ───────────────────
        logger.info("🔍 Extracting image features with CLIP...")
        query_embedding = self.extractor.extract_embedding(image)
        # query_embedding shape: (512,) — the image's AI fingerprint
        
        # ── Step 4: Get stored reference embeddings ─────────────────────────
        stored_embeddings, stored_labels = self.embedding_store.get_all()
        logger.info(f"📚 Comparing against {len(stored_labels)} reference images...")
        
        # ── Step 5: Run cosine similarity matching ──────────────────────────
        match: MatchResult = self.matcher.match(
            query_embedding,
            stored_embeddings,
            stored_labels
        )
        
        # ── Step 6: Calculate processing time ──────────────────────────────
        elapsed_ms = (time.time() - start_time) * 1000
        
        # ── Step 7: Build result ────────────────────────────────────────────
        if match.is_recognized:
            # Fetch landmark details from database
            landmark_data = await self._fetch_landmark_info(match.landmark_name)
            
            return RecognitionResult(
                recognized=True,
                landmark_name=match.landmark_name,
                confidence=match.confidence,
                raw_similarity=match.raw_score,
                description=landmark_data.get("description", ""),
                historical_facts=landmark_data.get("historical_facts", []),
                location=landmark_data.get("location", "Egypt"),
                built_year=landmark_data.get("built_year"),
                gallery_images=landmark_data.get("gallery_images", []),
                tags=landmark_data.get("tags", []),
                all_scores=match.all_scores,
                processing_time_ms=round(elapsed_ms, 1),
                model_used=f"CLIP {self.extractor.model_name}"
            )
        else:
            return RecognitionResult(
                recognized=False,
                landmark_name=None,
                confidence=match.confidence,  # Show how close it got
                raw_similarity=match.raw_score,
                description="",
                all_scores=match.all_scores,
                processing_time_ms=round(elapsed_ms, 1),
                model_used=f"CLIP {self.extractor.model_name}"
            )
    
    def _load_and_validate_image(self, image_data: bytes) -> Image.Image:
        """
        Load image from bytes and perform basic validation.
        
        - Converts to RGB (handles RGBA, grayscale, CMYK)
        - Resizes very large images to save memory
        """
        try:
            image = Image.open(io.BytesIO(image_data))
        except Exception as e:
            raise ValueError(f"Invalid image file: {e}")
        
        # Convert to RGB (CLIP expects 3-channel images)
        image = image.convert("RGB")
        
        # Resize if larger than 1024px on any side (saves memory, no quality loss for AI)
        max_dim = 1024
        if max(image.size) > max_dim:
            image.thumbnail((max_dim, max_dim), Image.LANCZOS)
            logger.debug(f"Resized large image to {image.size}")
        
        return image
    
    async def _fetch_landmark_info(self, landmark_name: str) -> dict:
        """
        Fetch landmark details from MongoDB.
        Falls back to empty dict if DB not available.
        """
        try:
            from database.db import get_database
            db = await get_database()
            
            # Query by landmark_id (normalized name)
            landmark_id = landmark_name.lower().replace(" ", "_")
            doc = await db.landmarks.find_one({"landmark_id": landmark_id})
            
            if doc:
                doc.pop("_id", None)  # Remove MongoDB ObjectId
                return doc
            else:
                logger.warning(f"No DB entry for landmark: {landmark_name}")
                return {}
                
        except Exception as e:
            logger.error(f"DB fetch failed for {landmark_name}: {e}")
            return {}


# ─────────────────────────────────────────────
# Module-level singleton pipeline
# ─────────────────────────────────────────────
_pipeline: Optional[RecognitionPipeline] = None


def get_pipeline() -> RecognitionPipeline:
    """Get or create the global pipeline instance."""
    global _pipeline
    if _pipeline is None:
        _pipeline = RecognitionPipeline()
    return _pipeline
