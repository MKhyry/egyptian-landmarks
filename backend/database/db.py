"""
database/db.py
==============
PURPOSE: MongoDB connection management using Motor (async driver).

Motor is the async version of PyMongo — it works with FastAPI's async nature.
"""

import os
import logging
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "egyptian_landmarks")

# Module-level client (one connection pool for entire app)
_client: Optional[AsyncIOMotorClient] = None
_database: Optional[AsyncIOMotorDatabase] = None


async def connect_to_mongo():
    """Initialize MongoDB connection. Called on app startup."""
    global _client, _database
    try:
        _client = AsyncIOMotorClient(MONGODB_URL, serverSelectionTimeoutMS=5000)
        _database = _client[DATABASE_NAME]
        
        # Test the connection
        await _client.admin.command("ping")
        logger.info(f"✅ Connected to MongoDB: {MONGODB_URL}/{DATABASE_NAME}")
        
    except Exception as e:
        logger.warning(f"⚠️  MongoDB connection failed: {e}")
        logger.warning("   Running without database (landmark info won't be available)")
        _client = None
        _database = None


async def close_mongo_connection():
    """Close connection on app shutdown."""
    global _client
    if _client:
        _client.close()
        logger.info("MongoDB connection closed")


async def get_database() -> AsyncIOMotorDatabase:
    """Return the database instance."""
    if _database is None:
        raise RuntimeError("Database not connected. Call connect_to_mongo() first.")
    return _database
