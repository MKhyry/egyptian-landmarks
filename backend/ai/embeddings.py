"""
ai/embeddings.py
================
PURPOSE: Manage the embedding database — store, load, and search computed embeddings.

CONCEPT:
  After running build_embeddings.py, we have a matrix of embeddings:
  
    embeddings_matrix shape: (N, 512)
      N = total number of images across all landmarks
      512 = dimensions per embedding (for ViT-B-32)
  
  We also have a parallel list of labels:
    labels: ["pyramids", "pyramids", "sphinx", "sphinx", "karnak", ...]
  
  Each row i in embeddings_matrix corresponds to labels[i].
  
  When a user uploads an image, we:
    1. Compute its embedding (512-dim vector)
    2. Compare against ALL stored embeddings (matrix multiply)
    3. Find the highest similarity score
    4. Return the corresponding landmark name

STORAGE FORMAT:
  embeddings_store/
    embeddings.npy    → float32 matrix (N, 512)
    labels.npy        → string array (N,)
    metadata.json     → per-landmark index info
"""

import numpy as np
import json
import logging
import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

EMBEDDINGS_PATH = Path(os.getenv("EMBEDDINGS_PATH", "./embeddings_store"))


class EmbeddingStore:
    """
    In-memory embedding database loaded from disk.
    
    Loaded once at startup, kept in RAM for millisecond-speed lookups.
    For large datasets (>100k images), consider FAISS for approximate
    nearest neighbor search.
    """
    
    def __init__(self):
        self.embeddings: Optional[np.ndarray] = None  # Shape: (N, 512)
        self.labels: Optional[np.ndarray] = None      # Shape: (N,) - landmark names
        self.metadata: dict = {}                       # Landmark → image count mapping
        self.is_loaded = False
    
    def load(self) -> bool:
        """
        Load precomputed embeddings from disk into memory.
        
        Returns True if successful, False if embeddings don't exist yet
        (user needs to run build_embeddings.py first).
        """
        embeddings_file = EMBEDDINGS_PATH / "embeddings.npy"
        labels_file = EMBEDDINGS_PATH / "labels.npy"
        metadata_file = EMBEDDINGS_PATH / "metadata.json"
        
        if not embeddings_file.exists():
            logger.warning(
                "⚠️  No embeddings found. Run: python scripts/build_embeddings.py"
            )
            return False
        
        try:
            # Load the embedding matrix (N × 512 float32)
            self.embeddings = np.load(embeddings_file)
            
            # Load corresponding landmark labels
            self.labels = np.load(labels_file, allow_pickle=True)
            
            # Load metadata (image counts per landmark)
            if metadata_file.exists():
                with open(metadata_file, "r") as f:
                    self.metadata = json.load(f)
            
            self.is_loaded = True
            
            unique_landmarks = len(set(self.labels))
            total_images = len(self.labels)
            logger.info(
                f"✅ Embeddings loaded: {total_images} images across "
                f"{unique_landmarks} landmarks"
            )
            logger.info(f"   Embedding matrix shape: {self.embeddings.shape}")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to load embeddings: {e}")
            return False
    
    def save(
        self,
        embeddings: np.ndarray,
        labels: list[str],
        metadata: dict
    ):
        """
        Save computed embeddings to disk.
        Called by build_embeddings.py after processing all dataset images.
        
        Args:
            embeddings: float32 array of shape (N, 512)
            labels: list of landmark names, parallel to embeddings
            metadata: dict with per-landmark statistics
        """
        EMBEDDINGS_PATH.mkdir(parents=True, exist_ok=True)
        
        # Save the main embedding matrix
        np.save(EMBEDDINGS_PATH / "embeddings.npy", embeddings.astype(np.float32))
        
        # Save labels as object array to handle strings
        np.save(EMBEDDINGS_PATH / "labels.npy", np.array(labels, dtype=object))
        
        # Save metadata as human-readable JSON
        with open(EMBEDDINGS_PATH / "metadata.json", "w") as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        logger.info(f"💾 Saved {len(labels)} embeddings to {EMBEDDINGS_PATH}")
        logger.info(f"   Landmarks indexed: {list(metadata.keys())}")
    
    def get_all(self) -> tuple[np.ndarray, np.ndarray]:
        """
        Return the full embedding matrix and label array.
        Used by the similarity engine for matching.
        """
        if not self.is_loaded:
            raise RuntimeError("Embeddings not loaded. Call load() first.")
        return self.embeddings, self.labels
    
    def get_landmark_names(self) -> list[str]:
        """Return list of all unique indexed landmark names."""
        if not self.is_loaded:
            return []
        return sorted(set(self.labels.tolist()))
    
    def get_image_count(self, landmark_name: str) -> int:
        """Return how many reference images are stored for a landmark."""
        return self.metadata.get(landmark_name, {}).get("image_count", 0)


# ─────────────────────────────────────────────
# Global singleton instance
# ─────────────────────────────────────────────
_store = EmbeddingStore()


def get_embedding_store() -> EmbeddingStore:
    """Return the global embedding store (load if needed)."""
    if not _store.is_loaded:
        _store.load()
    return _store
