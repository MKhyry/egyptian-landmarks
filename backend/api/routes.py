"""
api/routes.py
=============
PURPOSE: Define all HTTP API endpoints.

Endpoints:
  POST /api/recognize    → Upload image, get recognition result
  GET  /api/health       → Check system status
  GET  /api/landmarks    → List all indexed landmarks
  GET  /api/landmark/{id} → Get specific landmark details
"""

import logging
import os
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

from api.schemas import RecognitionResponse, HealthResponse, LandmarkListResponse
from ai.pipeline import get_pipeline
from ai.embeddings import get_embedding_store
from ai.model import CLIPFeatureExtractor

logger = logging.getLogger(__name__)
router = APIRouter()

# Max upload size in bytes
MAX_UPLOAD_BYTES = int(os.getenv("MAX_UPLOAD_SIZE_MB", "10")) * 1024 * 1024

# Allowed MIME types
ALLOWED_MIME_TYPES = {
    "image/jpeg", "image/jpg", "image/png",
    "image/webp", "image/bmp", "image/tiff"
}


@router.post("/recognize", response_model=RecognitionResponse)
async def recognize_landmark(
    file: UploadFile = File(..., description="Image file of an Egyptian landmark")
):
    """
    🎯 MAIN ENDPOINT — Recognize an Egyptian landmark from an uploaded image.
    
    Flow:
      1. Validate file type and size
      2. Read image bytes
      3. Run through AI recognition pipeline
      4. Return structured result
    """
    # ── Validate file type ──────────────────────────────────────────────────
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=415,
            detail=f"Unsupported file type: {file.content_type}. "
                   f"Allowed: JPEG, PNG, WebP, BMP"
        )
    
    # ── Read file data ──────────────────────────────────────────────────────
    image_data = await file.read()
    
    # ── Validate file size ──────────────────────────────────────────────────
    if len(image_data) > MAX_UPLOAD_BYTES:
        raise HTTPException(
            status_code=413,
            detail=f"File too large. Maximum size: {MAX_UPLOAD_BYTES // 1024 // 1024}MB"
        )
    
    if len(image_data) == 0:
        raise HTTPException(status_code=400, detail="Empty file uploaded")
    
    # ── Run AI recognition pipeline ─────────────────────────────────────────
    try:
        pipeline = get_pipeline()
        result = await pipeline.recognize(image_data)
        
        return RecognitionResponse(**result.to_dict())
        
    except ValueError as e:
        # Invalid image format
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logger.error(f"Recognition failed: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Recognition service error")


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Check system health: embeddings ready, landmark count.
    NOTE: Does NOT load the CLIP model — model loads on first /recognize call.
    """
    # Check if model is already loaded WITHOUT triggering the load
    # _instance is None until someone calls get_instance() from /recognize
    model_loaded = (
        CLIPFeatureExtractor._instance is not None
        and CLIPFeatureExtractor._instance.model is not None
    )

    store = get_embedding_store()
    landmark_names = store.get_landmark_names() if store.is_loaded else []
    total_refs = len(store.labels) if store.is_loaded and store.labels is not None else 0

    return HealthResponse(
        status="ok",  # Always ok — model loads lazily on first request
        model_loaded=model_loaded,
        embeddings_loaded=store.is_loaded,
        landmark_count=len(landmark_names),
        total_reference_images=total_refs,
        model_name=CLIPFeatureExtractor._instance.model_name if model_loaded else "ViT-B-32",
        embedding_dim=CLIPFeatureExtractor._instance.embedding_dim if model_loaded else 512
    )


@router.get("/landmarks", response_model=LandmarkListResponse)
async def list_landmarks():
    """Return all indexed landmark names."""
    store = get_embedding_store()
    landmarks = store.get_landmark_names()
    return LandmarkListResponse(landmarks=landmarks, total=len(landmarks))


@router.get("/landmark/{landmark_id}")
async def get_landmark_info(landmark_id: str):
    """Fetch full landmark info from MongoDB by landmark_id."""
    try:
        from database.db import get_database
        db = await get_database()
        doc = await db.landmarks.find_one({"landmark_id": landmark_id})
        
        if not doc:
            raise HTTPException(status_code=404, detail=f"Landmark '{landmark_id}' not found")
        
        doc.pop("_id", None)  # Remove non-serializable ObjectId
        return doc
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
