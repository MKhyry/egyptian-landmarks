"""
database/models.py
==================
PURPOSE: Define the data structure (schema) for landmark documents in MongoDB.

These Pydantic models serve two purposes:
  1. Validate data before inserting into the database
  2. Serialize/deserialize MongoDB documents to Python objects

DOCUMENT STRUCTURE IN MONGODB:
  Collection: landmarks
  One document per landmark, identified by landmark_id
  
  Example document:
  {
    "landmark_id": "pyramids_of_giza",       ← matches dataset folder name
    "name": "Pyramids of Giza",              ← display name in UI
    "arabic_name": "أهرامات الجيزة",
    "location": "Giza Plateau, Cairo, Egypt",
    "coordinates": {"lat": 29.9792, "lng": 31.1342},
    "built_year": "~2560 BCE",
    "dynasty": "4th Dynasty",
    "pharaoh": "Khufu",
    "description": "...",
    "historical_facts": ["fact1", "fact2", ...],
    "gallery_images": ["/gallery/pyramids/1.jpg", ...],
    "visitor_info": { "open_hours": "...", "entry_fee_egp": 160 },
    "tags": ["ancient", "wonder", "UNESCO"],
  }
"""

from pydantic import BaseModel, Field
from typing import Optional


class Coordinates(BaseModel):
    """GPS coordinates of the landmark."""
    lat: float
    lng: float


class VisitorInfo(BaseModel):
    """Practical visitor information."""
    open_hours: Optional[str] = None
    entry_fee_egp: Optional[int] = None       # Entry fee in Egyptian Pounds
    entry_fee_usd_approx: Optional[float] = None
    best_time: Optional[str] = None
    nearest_city: Optional[str] = None
    tips: Optional[str] = None


class LandmarkDocument(BaseModel):
    """
    Full landmark document — the shape of a MongoDB landmarks document.
    
    landmark_id MUST match the folder name in your dataset directory.
    Example: if dataset/karnak_temple/ → landmark_id = "karnak_temple"
    """
    
    # ── Identity ──────────────────────────────────────────────────────────
    landmark_id: str = Field(
        description="Unique ID — must match dataset folder name exactly"
    )
    name: str = Field(
        description="Display name shown in the UI"
    )
    arabic_name: Optional[str] = Field(
        None, description="Name in Arabic script"
    )
    
    # ── Location ──────────────────────────────────────────────────────────
    location: str = Field(
        description="Human-readable location string"
    )
    coordinates: Optional[Coordinates] = Field(
        None, description="GPS coordinates for map display"
    )
    governorate: Optional[str] = Field(
        None, description="Egyptian governorate (محافظة)"
    )
    
    # ── Historical context ────────────────────────────────────────────────
    built_year: Optional[str] = Field(
        None, description="Construction year or approximate period"
    )
    dynasty: Optional[str] = Field(
        None, description="Egyptian dynasty period"
    )
    pharaoh: Optional[str] = Field(
        None, description="Pharaoh who commissioned or is associated with it"
    )
    period: Optional[str] = Field(
        None, description="Historical period (e.g. 'New Kingdom', 'Islamic')"
    )
    
    # ── Content ───────────────────────────────────────────────────────────
    description: str = Field(
        description="Main descriptive paragraph shown on result page"
    )
    historical_facts: list[str] = Field(
        default_factory=list,
        description="List of interesting historical facts (shown as numbered list)"
    )
    '''
    # ── Media ─────────────────────────────────────────────────────────────
    gallery_images: list[str] = Field(
        default_factory=list,
        description="List of image paths or URLs for the gallery"
    )
    thumbnail: Optional[str] = Field(
        None, description="Single representative thumbnail image"
    )
    '''
    # ── Metadata ──────────────────────────────────────────────────────────
    tags: list[str] = Field(
        default_factory=list,
        description="Keywords for search/filtering"
    )
    visitor_info: Optional[VisitorInfo] = Field(
        None, description="Practical visitor information"
    )
    unesco_listed: bool = Field(
        False, description="Whether it is a UNESCO World Heritage Site"
    )
    landmark_type: Optional[str] = Field(
        None,
        description="Category: pyramid, temple, tomb, mosque, fortress, museum, etc."
    )

    class Config:
        # Allow extra fields (MongoDB _id won't cause validation errors)
        extra = "allow"


class LandmarkSummary(BaseModel):
    """
    Lightweight version of LandmarkDocument for list views.
    Only the fields needed for cards/previews.
    """
    landmark_id: str
    name: str
    arabic_name: Optional[str] = None
    location: str
    built_year: Optional[str] = None
    thumbnail: Optional[str] = None
    tags: list[str] = []
    landmark_type: Optional[str] = None
    unesco_listed: bool = False