"""
ai/model.py
===========
PURPOSE: Load the CLIP model and extract visual embeddings from images.

WHAT IS CLIP?
  CLIP (Contrastive Language-Image Pretraining) by OpenAI is a neural network
  trained on 400 million image-text pairs. It understands images semantically,
  not just pixel patterns. This makes it excellent for landmark recognition
  because it captures high-level visual concepts.

HOW IT WORKS:
  Image → Preprocessing → CLIP Vision Encoder → 512-dim embedding vector
  
  The embedding is a "fingerprint" of the image — similar images produce
  similar vectors in embedding space.

WHY CLIP OVER ResNet50?
  - Zero-shot capability (works on unseen images)
  - Better semantic understanding
  - Robust to lighting, angle, and crop variations
  - State-of-the-art visual features
"""

import torch
import open_clip
import numpy as np
from PIL import Image
import logging
from pathlib import Path
from typing import Union
import os
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)


class CLIPFeatureExtractor:
    """
    Wraps the CLIP model to extract normalized image embeddings.
    
    Singleton pattern: load once, reuse across all requests.
    The model stays in memory for fast inference.
    """
    
    _instance = None  # Singleton instance
    
    def __init__(self):
        self.device = self._get_device()
        self.model = None
        self.preprocess = None
        self.model_name = os.getenv("CLIP_MODEL_NAME", "ViT-B-32")
        self.pretrained = os.getenv("CLIP_PRETRAINED", "openai")
        self._load_model()
    
    @classmethod
    def get_instance(cls) -> "CLIPFeatureExtractor":
        """Return the singleton model instance (load only once)."""
        if cls._instance is None:
            logger.info("🤖 Loading CLIP model for the first time...")
            cls._instance = cls()
        return cls._instance
    
    def _get_device(self) -> torch.device:
        """
        Automatically select the best compute device.
        GPU (CUDA) is ~10x faster than CPU for inference.
        """
        if torch.cuda.is_available():
            logger.info("✅ GPU detected — using CUDA for fast inference")
            return torch.device("cuda")
        else:
            logger.info("⚠️  No GPU found — using CPU (slower but works)")
            return torch.device("cpu")
    
    def _load_model(self):
        """
        Load CLIP model and its preprocessing pipeline.
        
        open_clip.create_model_and_transforms() returns:
          - model: the neural network
          - train_preprocess: augmented preprocessing (for training)
          - val_preprocess: clean preprocessing (for inference) ← we use this
        """
        try:
            logger.info(f"📦 Loading {self.model_name} pretrained on {self.pretrained}...")
            
            self.model, _, self.preprocess = open_clip.create_model_and_transforms(
                self.model_name,
                pretrained=self.pretrained,
                device=self.device
            )
            
            # Set to evaluation mode (disables dropout, batch norm in train mode)
            # CRITICAL: always do this before inference
            self.model.eval()
            
            logger.info(f"✅ CLIP model loaded successfully on {self.device}")
            
        except Exception as e:
            logger.error(f"❌ Failed to load CLIP model: {e}")
            raise
    
    def extract_embedding(self, image: Union[Image.Image, str, Path]) -> np.ndarray:
        """
        Extract a feature embedding from a single image.
        
        THE CORE AI FUNCTION:
          Image → Preprocess → CLIP Encoder → L2 Normalize → Embedding
        
        Args:
            image: PIL Image, file path string, or Path object
        
        Returns:
            embedding: numpy array of shape (512,) for ViT-B-32
                       normalized to unit length (L2 norm = 1.0)
                       so cosine similarity = dot product
        """
        # Step 1: Load image if path was given
        if isinstance(image, (str, Path)):
            image = Image.open(image).convert("RGB")
        elif isinstance(image, Image.Image):
            image = image.convert("RGB")  # Ensure RGB (not RGBA or grayscale)
        
        # Step 2: Preprocess — resize, center crop, normalize pixel values
        # CLIP expects: 224×224 pixels, normalized with ImageNet stats
        image_tensor = self.preprocess(image).unsqueeze(0)  # Add batch dim → (1, 3, 224, 224)
        image_tensor = image_tensor.to(self.device)
        
        # Step 3: Forward pass through CLIP vision encoder
        # torch.no_grad() disables gradient computation (saves memory, speeds up)
        with torch.no_grad():
            # encode_image() runs the visual transformer (ViT) backbone
            embedding = self.model.encode_image(image_tensor)
        
        # Step 4: Normalize to unit vector
        # This makes cosine_similarity = dot_product, which is much faster
        # Two similar images will have a high dot product (close to 1.0)
        embedding = embedding / embedding.norm(dim=-1, keepdim=True)
        
        # Step 5: Convert to numpy for storage and similarity computation
        embedding_np = embedding.cpu().numpy().squeeze()  # Shape: (512,)
        
        return embedding_np
    
    def extract_batch_embeddings(self, images: list, batch_size: int = 32) -> np.ndarray:
        """
        Extract embeddings for multiple images efficiently using batching.
        
        Used by build_embeddings.py to process your entire dataset.
        Processing in batches is much faster than one-by-one.
        
        Args:
            images: List of PIL Images
            batch_size: Number of images per GPU/CPU batch
        
        Returns:
            embeddings: numpy array of shape (N, 512)
        """
        all_embeddings = []
        
        for i in range(0, len(images), batch_size):
            batch = images[i:i + batch_size]
            
            # Preprocess entire batch
            tensors = torch.stack([
                self.preprocess(img.convert("RGB")) for img in batch
            ]).to(self.device)
            
            with torch.no_grad():
                batch_embeddings = self.model.encode_image(tensors)
                batch_embeddings = batch_embeddings / batch_embeddings.norm(dim=-1, keepdim=True)
            
            all_embeddings.append(batch_embeddings.cpu().numpy())
        
        return np.vstack(all_embeddings)  # Shape: (N, 512)
    
    @property
    def embedding_dim(self) -> int:
        """Return the dimensionality of the embedding vector."""
        dims = {"ViT-B-32": 512, "ViT-L-14": 768, "RN50": 1024}
        return dims.get(self.model_name, 512)
