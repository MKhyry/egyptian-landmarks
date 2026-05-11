"""
ai/similarity.py
================
PURPOSE: Compute similarity between a query embedding and all stored embeddings.

THE MATH — COSINE SIMILARITY:
  Given two embedding vectors A and B:
  
    cosine_similarity(A, B) = (A · B) / (|A| × |B|)
    
  Since our embeddings are L2-normalized (unit vectors):
    |A| = |B| = 1.0
    
  Therefore:
    cosine_similarity(A, B) = A · B  (just a dot product!)
  
  Result range:
    1.0 → identical images (same landmark, same angle)
    0.8 → very similar (same landmark, different photo)
    0.6 → somewhat similar (possibly same landmark type)
    0.0 → completely unrelated
   -1.0 → opposite (theoretically impossible for real images)

MATCHING STRATEGY:
  We compare the query against ALL stored embeddings, then aggregate
  per-landmark scores by taking the MAXIMUM similarity across all reference
  images for that landmark.
  
  Why MAX instead of MEAN?
  - If even ONE reference image is a perfect match, that's strong evidence
  - Mean would dilute a perfect match with lower-scoring images
  - Max is more robust to having varied reference images
"""

import numpy as np
from sklearn.preprocessing import normalize
from dataclasses import dataclass
from typing import Optional
import logging
import os
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

# Below this threshold → "Landmark not recognized"
SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", "0.65"))


@dataclass
class MatchResult:
    """
    Structured result from a similarity matching operation.
    
    Attributes:
        landmark_name: Name of the best-matching landmark (None if not recognized)
        confidence: Similarity score as percentage (0–100)
        raw_score: Raw cosine similarity (0.0–1.0)
        is_recognized: True if score exceeds threshold
        all_scores: Dict of all landmark → score pairs (for debugging)
    """
    landmark_name: Optional[str]
    confidence: float          # 0–100 percentage
    raw_score: float           # 0.0–1.0 cosine similarity
    is_recognized: bool
    all_scores: dict[str, float]


class SimilarityMatcher:
    """
    Finds the best-matching landmark for a given query embedding.
    
    This is where the actual AI recognition happens:
    query embedding → compare against database → ranked results.
    """
    
    def __init__(self, threshold: float = SIMILARITY_THRESHOLD):
        self.threshold = threshold
    
    def match(
        self,
        query_embedding: np.ndarray,
        stored_embeddings: np.ndarray,
        stored_labels: np.ndarray
    ) -> MatchResult:
        """
        Find the best matching landmark via cosine similarity.
        
        ALGORITHM:
          1. Ensure query is unit-normalized
          2. Compute dot product with ALL stored embeddings (matrix multiply)
          3. Group similarity scores by landmark name
          4. Take MAX score per landmark
          5. Find the landmark with the highest MAX score
          6. Apply recognition threshold
        
        Args:
            query_embedding: (512,) float32 array — the uploaded image's fingerprint
            stored_embeddings: (N, 512) float32 array — all reference fingerprints
            stored_labels: (N,) string array — landmark name for each row
        
        Returns:
            MatchResult with landmark name, confidence, and all scores
        """
        # ── Step 1: Ensure query is normalized (should already be, but safety check) ──
        query_norm = query_embedding / (np.linalg.norm(query_embedding) + 1e-8)
        query_norm = query_norm.reshape(1, -1)  # Shape: (1, 512)
        
        # ── Step 2: Compute ALL cosine similarities in one matrix multiply ──
        # stored_embeddings: (N, 512) × query_norm.T: (512, 1) → similarities: (N, 1)
        # This is equivalent to scikit-learn's cosine_similarity but faster
        raw_similarities = (stored_embeddings @ query_norm.T).squeeze()  # Shape: (N,)
        
        # Clip to [0, 1] — negative similarities are meaningless for landmarks
        similarities = np.clip(raw_similarities, 0.0, 1.0)
        
        # ── Step 3: Aggregate per landmark using MAX strategy ──
        landmark_scores = self._aggregate_by_landmark(similarities, stored_labels)
        
        # ── Step 4: Find best match ──
        best_landmark = max(landmark_scores, key=landmark_scores.get)
        best_score = landmark_scores[best_landmark]
        
        # ── Step 5: Apply recognition threshold ──
        is_recognized = best_score >= self.threshold
        
        # Convert to percentage confidence
        confidence = round(best_score * 100, 2)
        
        if is_recognized:
            logger.info(
                f"✅ Recognized: {best_landmark} "
                f"(confidence: {confidence:.1f}%, threshold: {self.threshold * 100:.0f}%)"
            )
        else:
            logger.info(
                f"❌ Not recognized. Best score: {confidence:.1f}% "
                f"for '{best_landmark}' — below threshold {self.threshold * 100:.0f}%"
            )
        
        return MatchResult(
            landmark_name=best_landmark if is_recognized else None,
            confidence=confidence,
            raw_score=float(best_score),
            is_recognized=is_recognized,
            all_scores={k: round(v * 100, 2) for k, v in sorted(
                landmark_scores.items(), key=lambda x: x[1], reverse=True
            )}
        )
    
    def _aggregate_by_landmark(
        self,
        similarities: np.ndarray,
        labels: np.ndarray
    ) -> dict[str, float]:
        """
        Group per-image similarities by landmark name and take the MAX.
        
        Example:
          pyramids images: [0.92, 0.87, 0.83] → MAX = 0.92
          sphinx images:   [0.41, 0.38]        → MAX = 0.41
          karnak images:   [0.34, 0.29, 0.31]  → MAX = 0.34
          
          Best match: pyramids (0.92 > threshold 0.65) ✅
        """
        landmark_scores = {}
        unique_landmarks = np.unique(labels)
        
        for landmark in unique_landmarks:
            # Boolean mask: which rows belong to this landmark?
            mask = labels == landmark
            
            # Get all similarity scores for this landmark's reference images
            landmark_sims = similarities[mask]
            
            # Take the maximum similarity as the landmark's score
            # Alternative: try np.mean or np.percentile(landmark_sims, 90)
            landmark_scores[landmark] = float(np.max(landmark_sims))
        
        return landmark_scores
    
    def get_top_matches(
        self,
        query_embedding: np.ndarray,
        stored_embeddings: np.ndarray,
        stored_labels: np.ndarray,
        top_k: int = 5
    ) -> list[dict]:
        """
        Return the top-k matching landmarks with scores.
        Useful for showing "similar landmarks" or debugging.
        """
        query_norm = query_embedding / (np.linalg.norm(query_embedding) + 1e-8)
        query_norm = query_norm.reshape(1, -1)
        
        similarities = np.clip(
            (stored_embeddings @ query_norm.T).squeeze(), 0.0, 1.0
        )
        
        landmark_scores = self._aggregate_by_landmark(similarities, stored_labels)
        
        sorted_matches = sorted(
            landmark_scores.items(), key=lambda x: x[1], reverse=True
        )
        
        return [
            {
                "landmark": name,
                "confidence": round(score * 100, 2),
                "is_match": score >= self.threshold
            }
            for name, score in sorted_matches[:top_k]
        ]


# ─────────────────────────────────────────────
# Global matcher instance
# ─────────────────────────────────────────────
_matcher = SimilarityMatcher()


def get_matcher() -> SimilarityMatcher:
    return _matcher
