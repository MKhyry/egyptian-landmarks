"""
api/schemas.py
==============
PURPOSE: Define the exact shape of API requests and responses using Pydantic.

Pydantic validates data automatically and generates OpenAPI documentation.
"""

from pydantic import BaseModel, Field
from typing import Optional


class RecognitionResponse(BaseModel):
    """
    JSON response returned to the frontend after recognition.
    All fields typed and documented for the auto-generated API docs.
    """
    recognized: bool = Field(description="True if a landmark was identified")
    landmark_name: Optional[str] = Field(None, description="Identified landmark name")
    confidence: float = Field(description="Confidence percentage (0–100)")
    raw_similarity: float = Field(description="Raw cosine similarity score (0–1)")
    
    # Landmark details (empty strings if not recognized)
    description: str = Field("", description="Landmark description")
    historical_facts: list[str] = Field([], description="Historical facts list")
    location: str = Field("", description="Geographic location")
    built_year: Optional[str] = Field(None, description="Construction year/period")
    gallery_images: list[str] = Field([], description="Gallery image URLs/paths")
    tags: list[str] = Field([], description="Search tags")
    
    # Debug info
    all_scores: dict = Field({}, description="All landmark scores for transparency")
    processing_time_ms: float = Field(description="Inference time in milliseconds")
    model_used: str = Field(description="AI model name")

    class Config:
        json_schema_extra = {
            "example": {
                "recognized": True,
                "landmark_name": "pyramids_of_giza",
                "confidence": 87.4,
                "raw_similarity": 0.874,
                "description": "The Pyramids of Giza are ancient limestone structures...",
                "historical_facts": ["Built around 2560 BCE", "The only surviving wonder..."],
                "location": "Giza Plateau, Cairo, Egypt",
                "built_year": "~2560 BCE",
                "gallery_images": ["/gallery/pyramids/1.jpg"],
                "tags": ["ancient", "wonder", "UNESCO"],
                "all_scores": {"pyramids_of_giza": 87.4, "great_sphinx": 41.2},
                "processing_time_ms": 234.5,
                "model_used": "CLIP ViT-B-32"
            }
        }


class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
    embeddings_loaded: bool
    landmark_count: int
    total_reference_images: int
    model_name: str
    embedding_dim: int


class LandmarkListResponse(BaseModel):
    landmarks: list[str]
    total: int
