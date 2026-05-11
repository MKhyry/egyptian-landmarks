"""
scripts/seed_landmarks.py
=========================
PURPOSE: Read landmark data from data/landmarks_data.py and insert into MongoDB.

This file contains ONLY the seeding logic — no landmark data.
All landmark content lives in data/landmarks_data.py.

USAGE:
  cd backend
  python scripts/seed_landmarks.py

  # Preview without inserting:
  python scripts/seed_landmarks.py --dry-run

  # Clear all landmarks and re-seed from scratch:
  python scripts/seed_landmarks.py --reset

WHAT IT DOES:
  - For each landmark in LANDMARKS list, it does an "upsert":
    → If landmark_id already exists in MongoDB → UPDATE it
    → If landmark_id does not exist           → INSERT it
  - This makes the script safe to run multiple times
"""

import sys
import asyncio
import argparse
import logging
from pathlib import Path

# Add parent directory to sys.path so imports work
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
load_dotenv()

from database.models import LandmarkDocument

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


async def seed(dry_run: bool = False, reset: bool = False):
    """
    Main seeding function.

    Args:
        dry_run: If True, validate data but do NOT write to database
        reset:   If True, delete all existing landmarks before seeding
    """
    # Import landmark data
    try:
        from data.landmarks_data import LANDMARKS
    except ImportError as e:
        logger.error(f"Could not import landmark data: {e}")
        sys.exit(1)

    if not LANDMARKS:
        logger.warning("LANDMARKS list is empty in data/landmarks_data.py")
        return

    logger.info("=" * 60)
    logger.info("Egyptian Landmark Database Seeder")
    logger.info("=" * 60)
    logger.info(f"   Landmarks to seed: {len(LANDMARKS)}")
    if dry_run:
        logger.info("   Mode: DRY RUN (no database writes)")
    if reset:
        logger.info("   Mode: RESET (will delete existing data)")

    # Validate all entries first
    logger.info("\nValidating landmark data...")
    valid_landmarks = []
    has_errors = False

    for i, raw in enumerate(LANDMARKS):
        landmark_id = raw.get("landmark_id", f"[entry #{i}]")
        try:
            validated = LandmarkDocument(**raw)
            valid_landmarks.append(validated)
            logger.info(f"   OK  {landmark_id}")
        except Exception as e:
            logger.error(f"   FAIL  {landmark_id}: {e}")
            has_errors = True

    if has_errors:
        logger.error("\nValidation failed. Fix errors above before seeding.")
        sys.exit(1)

    logger.info(f"\nAll {len(valid_landmarks)} entries validated")

    if dry_run:
        logger.info("\nDry run complete - no data written.")
        return

    # Connect to MongoDB
    try:
        from database.db import connect_to_mongo, get_database
        await connect_to_mongo()
        db = await get_database()
        collection = db.landmarks
    except Exception as e:
        logger.error(f"Could not connect to MongoDB: {e}")
        sys.exit(1)

    # Optionally reset
    if reset:
        deleted = await collection.delete_many({})
        logger.info(f"\nDeleted {deleted.deleted_count} existing landmark documents")

    # Upsert each landmark
    logger.info("\nWriting to MongoDB...")
    inserted = 0
    updated = 0
    failed = 0

    for landmark in valid_landmarks:
        try:
            data = landmark.model_dump(exclude_none=False)
            result = await collection.update_one(
                {"landmark_id": landmark.landmark_id},
                {"$set": data},
                upsert=True
            )
            if result.upserted_id:
                logger.info(f"   Inserted: {landmark.name}")
                inserted += 1
            else:
                logger.info(f"   Updated:  {landmark.name}")
                updated += 1
        except Exception as e:
            logger.error(f"   Failed:   {landmark.landmark_id} - {e}")
            failed += 1

    # Create indexes
    await collection.create_index("landmark_id", unique=True)
    await collection.create_index("tags")
    await collection.create_index("landmark_type")
    logger.info("\nDatabase indexes created")

    # Summary
    logger.info("\n" + "=" * 60)
    logger.info("SEEDING COMPLETE")
    logger.info("=" * 60)
    logger.info(f"   Inserted: {inserted} | Updated: {updated} | Failed: {failed}")

    logger.info("\n   Landmarks in database:")
    async for doc in collection.find({}, {"landmark_id": 1, "name": 1, "_id": 0}):
        logger.info(f"     - {doc['landmark_id']}  ->  {doc['name']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seed Egyptian landmark data into MongoDB")
    parser.add_argument("--dry-run", action="store_true", help="Validate without writing")
    parser.add_argument("--reset", action="store_true", help="Delete existing before seeding")
    args = parser.parse_args()
    asyncio.run(seed(dry_run=args.dry_run, reset=args.reset))