"""
scripts/upload_dataset_to_cloudinary.py
========================================
PURPOSE: Upload your entire local dataset folder to Cloudinary.
         Run this ONCE from your local machine before deploying.

WHAT IT DOES:
  - Scans every subfolder in dataset/
  - Uploads each image to Cloudinary under:
      folder: egyptian_landmarks/{landmark_id}/{filename}
  - Saves a JSON file: cloudinary_manifest.json
    This file maps each landmark_id → list of Cloudinary image URLs
  - You commit cloudinary_manifest.json to your repo
  - build_embeddings.py reads from this manifest instead of local files

USAGE:
  pip install cloudinary
  python scripts/upload_dataset_to_cloudinary.py

  # With a custom dataset path:
  python scripts/upload_dataset_to_cloudinary.py --dataset ./my_dataset
"""

import os
import sys
import json
import argparse
import logging
from pathlib import Path

import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

# ── Supported image formats (same as build_embeddings.py) ────────────────────
IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".webp", ".bmp",
    ".jfif", ".gif", ".tiff", ".avif", ".heic"
}

# ── Cloudinary folder where all images will live ─────────────────────────────
CLOUDINARY_BASE_FOLDER = "egyptian_landmarks"

# ── Output manifest path ──────────────────────────────────────────────────────
MANIFEST_PATH = Path("cloudinary_manifest.json")


def configure_cloudinary():
    """
    Read Cloudinary credentials from .env and configure the SDK.
    Raises a clear error if credentials are missing.
    """
    cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME")
    api_key    = os.getenv("CLOUDINARY_API_KEY")
    api_secret = os.getenv("CLOUDINARY_API_SECRET")

    if not all([cloud_name, api_key, api_secret]):
        logger.error("❌ Cloudinary credentials missing from .env!")
        logger.error("   Add these to your backend/.env file:")
        logger.error("   CLOUDINARY_CLOUD_NAME=your_cloud_name")
        logger.error("   CLOUDINARY_API_KEY=your_api_key")
        logger.error("   CLOUDINARY_API_SECRET=your_api_secret")
        logger.error("   Get them at: https://console.cloudinary.com")
        sys.exit(1)

    cloudinary.config(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret=api_secret,
        secure=True,   # Always use HTTPS URLs
    )
    logger.info(f"✅ Cloudinary configured — cloud: {cloud_name}")


def upload_dataset(dataset_path: Path) -> dict[str, list[str]]:
    """
    Upload all images in dataset_path to Cloudinary.

    Returns a manifest dict:
    {
        "pyramids_of_giza": [
            "https://res.cloudinary.com/.../pyramids_of_giza/img1.jpg",
            "https://res.cloudinary.com/.../pyramids_of_giza/img2.jpg",
        ],
        "great_sphinx": [...],
        ...
    }
    """
    if not dataset_path.exists():
        logger.error(f"❌ Dataset path not found: {dataset_path}")
        sys.exit(1)

    # Collect all landmark folders
    landmark_dirs = sorted([
        d for d in dataset_path.iterdir() if d.is_dir()
    ])

    if not landmark_dirs:
        logger.error("❌ No landmark folders found in dataset/")
        sys.exit(1)

    logger.info(f"📂 Found {len(landmark_dirs)} landmark folders")

    manifest = {}
    total_uploaded = 0
    total_skipped  = 0
    total_failed   = 0

    for landmark_dir in landmark_dirs:
        landmark_id = landmark_dir.name

        # Collect image files
        image_files = sorted([
            f for f in landmark_dir.rglob("*")
            if f.suffix.lower() in IMAGE_EXTENSIONS
        ])

        if not image_files:
            logger.warning(f"⚠️  No images in {landmark_id}/ — skipping")
            continue

        logger.info(f"\n🏛️  {landmark_id} — {len(image_files)} images")
        landmark_urls = []

        for img_path in tqdm(image_files, desc=f"  {landmark_id}", unit="img"):
            # Cloudinary public_id = folder path without extension
            # e.g. "egyptian_landmarks/pyramids_of_giza/img001"
            public_id = f"{CLOUDINARY_BASE_FOLDER}/{landmark_id}/{img_path.stem}"

            try:
                result = cloudinary.uploader.upload(
                    str(img_path),
                    public_id=public_id,
                    overwrite=False,        # Skip if already uploaded
                    resource_type="image",
                    quality="auto:good",    # Cloudinary auto-optimizes quality
                    fetch_format="auto",    # Serve WebP to modern browsers
                )
                landmark_urls.append(result["secure_url"])
                total_uploaded += 1

            except cloudinary.exceptions.Error as e:
                # If the image already exists, Cloudinary raises an error
                # when overwrite=False — we fetch the existing URL instead
                if "already exists" in str(e).lower():
                    existing_url = (
                        f"https://res.cloudinary.com/"
                        f"{os.getenv('CLOUDINARY_CLOUD_NAME')}"
                        f"/image/upload/{public_id}"
                    )
                    landmark_urls.append(existing_url)
                    total_skipped += 1
                else:
                    logger.warning(f"   ❌ Failed: {img_path.name} — {e}")
                    total_failed += 1

        if landmark_urls:
            manifest[landmark_id] = landmark_urls
            logger.info(f"   ✅ {len(landmark_urls)} URLs collected")

    return manifest, total_uploaded, total_skipped, total_failed


def save_manifest(manifest: dict, output_path: Path):
    """Save the manifest JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    logger.info(f"\n💾 Manifest saved → {output_path}")
    logger.info(f"   {len(manifest)} landmarks, "
                f"{sum(len(v) for v in manifest.values())} total URLs")


def main():
    parser = argparse.ArgumentParser(
        description="Upload landmark dataset to Cloudinary"
    )
    parser.add_argument(
        "--dataset",
        default=os.getenv("DATASET_PATH", "./dataset"),
        help="Path to your local dataset folder (default: ./dataset)",
    )
    parser.add_argument(
        "--output",
        default=str(MANIFEST_PATH),
        help="Output path for the manifest JSON (default: cloudinary_manifest.json)",
    )
    args = parser.parse_args()

    logger.info("=" * 60)
    logger.info("☁️  Cloudinary Dataset Uploader")
    logger.info("=" * 60)

    # 1. Configure Cloudinary
    configure_cloudinary()

    # 2. Upload everything
    manifest, uploaded, skipped, failed = upload_dataset(Path(args.dataset))

    # 3. Save manifest
    save_manifest(manifest, Path(args.output))

    # 4. Summary
    logger.info("\n" + "=" * 60)
    logger.info("✅ UPLOAD COMPLETE")
    logger.info("=" * 60)
    logger.info(f"   Uploaded : {uploaded}")
    logger.info(f"   Skipped  : {skipped} (already existed)")
    logger.info(f"   Failed   : {failed}")
    logger.info(f"\n📋 NEXT STEPS:")
    logger.info(f"   1. Commit cloudinary_manifest.json to your repo")
    logger.info(f"   2. Run: python scripts/build_embeddings.py --source cloudinary")
    logger.info(f"   3. Commit the generated embeddings_store/ folder too")


if __name__ == "__main__":
    main()
