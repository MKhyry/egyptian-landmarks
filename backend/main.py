"""
main.py
=======
PURPOSE: FastAPI application entry point.

This file:
  - Creates the FastAPI app
  - Configures CORS (so the Next.js frontend can call the API)
  - Registers all routes
  - Loads AI model + embeddings on startup
  - Connects to MongoDB

STARTUP SEQUENCE:
  1. Connect to MongoDB
  2. Load CLIP model (takes 5–30 seconds first time, cached after)
  3. Load precomputed embeddings from disk
  4. App is ready to serve requests

RUN:
  uvicorn main:app --reload --host 0.0.0.0 --port 8000
"""

import logging
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan events.
    Everything before `yield` runs on startup.
    Everything after `yield` runs on shutdown.
    """
    logger.info("=" * 60)
    logger.info("🏛️  Egyptian Landmark Recognition System")
    logger.info("=" * 60)
    
    # ── Startup ────────────────────────────────────────────────────────────
    
    # 1. Connect to MongoDB (non-fatal if not available)
    try:
        from database.db import connect_to_mongo
        await connect_to_mongo()
    except Exception as e:
        logger.warning(f"MongoDB unavailable: {e}")
    
    # 2. Preload the CLIP model (avoid cold start on first request)
    logger.info("🤖 Preloading AI model...")
    try:
        from ai.model import CLIPFeatureExtractor
        CLIPFeatureExtractor.get_instance()
    except Exception as e:
        logger.error(f"❌ Failed to load CLIP model: {e}")
    
    # 3. Load precomputed embeddings
    logger.info("📚 Loading landmark embeddings...")
    try:
        from ai.embeddings import get_embedding_store
        store = get_embedding_store()
        if store.is_loaded:
            logger.info(f"✅ Ready: {len(store.get_landmark_names())} landmarks indexed")
        else:
            logger.warning("⚠️  Run 'python scripts/build_embeddings.py' to index your dataset")
    except Exception as e:
        logger.error(f"❌ Failed to load embeddings: {e}")
    
    logger.info("🚀 Server ready — API at http://localhost:8000")
    logger.info("📖 API docs at http://localhost:8000/docs")
    
    yield
    
    # ── Shutdown ───────────────────────────────────────────────────────────
    from database.db import close_mongo_connection
    await close_mongo_connection()
    logger.info("👋 Server shut down")


# Create FastAPI application
app = FastAPI(
    title="🏛️ Egyptian Landmark Recognition API",
    description=(
        "AI-powered Egyptian landmark recognition using CLIP embeddings "
        "and cosine similarity matching."
    ),
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",   # Swagger UI at /docs
    redoc_url="/redoc"  # ReDoc at /redoc
)

# ── CORS Middleware ──────────────────────────────────────────────────────────
# Allows the Next.js frontend (localhost:3000) to call this API
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Static Files (landmark gallery images) ───────────────────────────────────
gallery_path = Path("./gallery")
gallery_path.mkdir(exist_ok=True)
app.mount("/gallery", StaticFiles(directory="gallery"), name="gallery")

# ── API Routes ───────────────────────────────────────────────────────────────
from api.routes import router as api_router
app.include_router(api_router, prefix="/api", tags=["Recognition"])

# ── Root endpoint ─────────────────────────────────────────────────────────────
@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Egyptian Landmark Recognition API",
        "docs": "/docs",
        "health": "/api/health",
        "recognize": "POST /api/recognize"
    }


# ── Direct run (for development without uvicorn command) ──────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=True
    )