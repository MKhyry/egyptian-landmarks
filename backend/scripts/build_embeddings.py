"""
scripts/build_embeddings.py
===========================
PURPOSE: ⭐ INDEX YOUR DATASET — Run this ONCE before deploying (or after adding images).

SUPPORTS TWO SOURCES:
  --source local      (default) Read images from local dataset/ folder
  --source cloudinary           Read images from URLs in cloudinary_manifest.json

USAGE:

  # Local (original behavior — works exactly as before):
  python scripts/build_embeddings.py

  # Cloudinary (for deployment — reads from cloudinary_manifest.json):
  python scripts/build_embeddings.py --source cloudinary

  # Cloudinary with a custom manifest path:
  python scripts/build_embeddings.py --source cloudinary --manifest ./cloudinary_manifest.json

OUTPUT (same either way):
  embeddings_store/
    embeddings.npy   (float32 matrix, shape: N×512)
    labels.npy       (string array, shape: N)
    metadata.json    (statistics per landmark)
"""

import sys
import os
import argparse
import json
import time
import logging
import io
from pathlib import Path
from typing import Optional

# Add parent directory to path so we can import ai modules
sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
import requests
from PIL import Image
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff", ".heic"}

# ─────────────────────────────────────────────────────────────────────────────
# SOURCE: LOCAL (original behavior — unchanged)
# ─────────────────────────────────────────────────────────────────────────────

def scan_local_dataset(dataset_path: Path) -> dict[str, list]:
    """
    Scan the local dataset directory and group image PATHS by landmark folder.

    Returns:
        {"pyramids_of_giza": [Path("dataset/pyramids_of_giza/img1.jpg"), ...], ...}
    """
    landmark_images = {}

    if not dataset_path.exists():
        logger.error(f"❌ Dataset path not found: {dataset_path}")
        sys.exit(1)

    for landmark_dir in sorted(dataset_path.iterdir()):
        if not landmark_dir.is_dir():
            continue

        landmark_name = landmark_dir.name
        images = [
            f for f in landmark_dir.rglob("*")
            if f.suffix.lower() in IMAGE_EXTENSIONS
        ]

        if not images:
            logger.warning(f"⚠️  No images found in: {landmark_name}/")
            continue

        landmark_images[landmark_name] = sorted(images)
        logger.info(f"   📁 {landmark_name}: {len(images)} images")

    return landmark_images


def load_local_image(path: Path) -> Optional[Image.Image]:
    """Load a single image from a local file path."""
    try:
        return Image.open(path).convert("RGB")
    except Exception as e:
        logger.warning(f"   ⚠️  Failed to load {path.name}: {e}")
        return None


# ─────────────────────────────────────────────────────────────────────────────
# SOURCE: CLOUDINARY (new behavior — reads URLs from manifest JSON)
# ─────────────────────────────────────────────────────────────────────────────

def load_cloudinary_manifest(manifest_path: Path) -> dict[str, list[str]]:
    """
    Load the cloudinary_manifest.json file produced by upload_dataset_to_cloudinary.py.

    Returns:
        {"pyramids_of_giza": ["https://res.cloudinary.com/...", ...], ...}
    """
    if not manifest_path.exists():
        logger.error(f"❌ Manifest not found: {manifest_path}")
        logger.error("   Run upload_dataset_to_cloudinary.py first.")
        sys.exit(1)

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    total_urls = sum(len(v) for v in manifest.values())
    logger.info(f"   📋 Manifest loaded: {len(manifest)} landmarks, {total_urls} URLs")
    return manifest


def download_image_from_url(url: str) -> Optional[Image.Image]:
    """
    Download a single image from a URL and return a PIL Image.

    Cloudinary URLs are fast and reliable — this adds a small download
    overhead (~0.1–0.3s per image) but is necessary for cloud deployment.
    For speed, Cloudinary URLs are served from a global CDN.
    """
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        img = Image.open(io.BytesIO(response.content)).convert("RGB")
        return img
    except requests.exceptions.RequestException as e:
        logger.warning(f"   ⚠️  Download failed: {url[-50:]}... — {e}")
        return None
    except Exception as e:
        logger.warning(f"   ⚠️  Image decode failed: {e}")
        return None


# ─────────────────────────────────────────────────────────────────────────────
# CORE: EMBEDDING BUILDER (same logic regardless of source)
# ─────────────────────────────────────────────────────────────────────────────

def build_embeddings(
    source: str,
    dataset_path: Path,
    manifest_path: Path,
    output_path: Path,
    batch_size: int = 16,
    max_images_per_landmark: Optional[int] = None,
):
    """
    Main function: process all images and save embeddings.

    Args:
        source                  : "local" or "cloudinary"
        dataset_path            : Path to local dataset/ folder (used when source=local)
        manifest_path           : Path to cloudinary_manifest.json (used when source=cloudinary)
        output_path             : Where to save embeddings_store/
        batch_size              : Images processed at once (reduce if you hit memory errors)
        max_images_per_landmark : Cap per landmark (None = use all)
    """
    logger.info("=" * 60)
    logger.info("🏛️  Egyptian Landmark Embedding Builder")
    logger.info(f"   Source: {source.upper()}")
    logger.info("=" * 60)

    # ── Step 1: Collect image sources ────────────────────────────────────────
    if source == "local":
        logger.info(f"\n📂 Scanning local dataset: {dataset_path}")
        landmark_sources = scan_local_dataset(dataset_path)
        # landmark_sources = {"name": [Path, Path, ...]}

    elif source == "cloudinary":
        logger.info(f"\n☁️  Loading Cloudinary manifest: {manifest_path}")
        landmark_sources = load_cloudinary_manifest(manifest_path)
        # landmark_sources = {"name": ["https://...", "https://...", ...]}
        for name, urls in landmark_sources.items():
            logger.info(f"   📁 {name}: {len(urls)} URLs")

    else:
        logger.error(f"❌ Unknown source: {source}. Use 'local' or 'cloudinary'.")
        sys.exit(1)

    if not landmark_sources:
        logger.error("❌ No landmarks found!")
        sys.exit(1)

    total_landmarks = len(landmark_sources)
    total_images    = sum(len(v) for v in landmark_sources.values())
    logger.info(f"\n✅ Found {total_landmarks} landmarks, {total_images} total images")

    # ── Step 2: Load CLIP model ───────────────────────────────────────────────
    logger.info("\n🤖 Loading CLIP model...")
    from ai.model import CLIPFeatureExtractor
    extractor = CLIPFeatureExtractor.get_instance()
    logger.info(f"   Model: {extractor.model_name} on {extractor.device}")
    logger.info(f"   Embedding dimension: {extractor.embedding_dim}")

    # ── Step 3: Process each landmark ────────────────────────────────────────
    all_embeddings = []
    all_labels     = []
    metadata       = {}
    start_time     = time.time()

    for landmark_name, image_sources in landmark_sources.items():
        logger.info(f"\n🔍 Processing: {landmark_name}")

        # Optionally cap images per landmark
        if max_images_per_landmark:
            image_sources = image_sources[:max_images_per_landmark]

        landmark_embeddings = []
        failed_count = 0

        # Process images in batches with progress bar
        for i in tqdm(range(0, len(image_sources), batch_size),
                      desc=f"  {landmark_name}", unit="batch"):

            batch_sources = image_sources[i : i + batch_size]
            batch_images  = []

            # ── Load images: local path OR cloudinary URL ─────────────────
            for src in batch_sources:
                if source == "local":
                    img = load_local_image(src)          # src is a Path
                else:
                    img = download_image_from_url(src)   # src is a URL string

                if img is not None:
                    batch_images.append(img)
                else:
                    failed_count += 1

            if not batch_images:
                continue

            # ── Extract embeddings for this batch ─────────────────────────
            try:
                batch_embeddings = extractor.extract_batch_embeddings(
                    batch_images, batch_size=len(batch_images)
                )
                landmark_embeddings.append(batch_embeddings)
            except Exception as e:
                logger.error(f"   ❌ Batch failed: {e}")
                failed_count += len(batch_images)

        if not landmark_embeddings:
            logger.warning(f"   ⚠️  No valid embeddings for {landmark_name}")
            continue

        # Stack all embeddings for this landmark
        landmark_emb_matrix = np.vstack(landmark_embeddings)   # (n_imgs, 512)
        successful = len(landmark_emb_matrix)

        # Add to global arrays
        all_embeddings.append(landmark_emb_matrix)
        all_labels.extend([landmark_name] * successful)

        # Metadata for each landmark
        metadata[landmark_name] = {
            "image_count": successful,
            "failed_count": failed_count,
            "embedding_shape": list(landmark_emb_matrix.shape),
            "source": source,
        }

        # Log intra-class similarity (quality check)
        if successful > 1:
            sample     = landmark_emb_matrix[:min(10, successful)]
            intra_sim  = sample @ sample.T
            np.fill_diagonal(intra_sim, 0)
            avg_intra  = float(intra_sim.max(axis=1).mean())
            logger.info(f"   ✅ {successful} embeddings | avg intra-similarity: {avg_intra:.3f}")

    # ── Step 4: Stack all embeddings ─────────────────────────────────────────
    logger.info("\n💾 Saving embeddings...")
    final_embeddings = np.vstack(all_embeddings)
    final_labels     = np.array(all_labels)
    logger.info(f"   Final matrix shape: {final_embeddings.shape}")
    logger.info(f"   Total labeled images: {len(final_labels)}")

    # ── Step 5: Save to disk ─────────────────────────────────────────────────
    from ai.embeddings import EmbeddingStore
    store = EmbeddingStore()
    store.save(final_embeddings, final_labels.tolist(), metadata)

    # ── Step 6: Summary ───────────────────────────────────────────────────────
    elapsed = time.time() - start_time
    logger.info("\n" + "=" * 60)
    logger.info("✅ EMBEDDING BUILD COMPLETE")
    logger.info("=" * 60)
    logger.info(f"   Total time:    {elapsed:.1f} seconds")
    logger.info(f"   Landmarks:     {len(metadata)}")
    logger.info(f"   Total images:  {len(final_labels)}")
    logger.info(f"   Matrix shape:  {final_embeddings.shape}")
    logger.info(f"   Saved to:      {output_path}")
    logger.info("\n   Per-landmark breakdown:")
    for name, info in metadata.items():
        logger.info(f"     - {name}: {info['image_count']} images")

    logger.info("\n🚀 You can now start the server: uvicorn main:app --reload")


# ─────────────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build landmark embeddings")
    parser.add_argument(
        "--source",
        choices=["local", "cloudinary"],
        default="local",
        help="Image source: 'local' (default) or 'cloudinary'",
    )
    parser.add_argument(
        "--dataset",
        default=os.getenv("DATASET_PATH", "./dataset"),
        help="Path to local dataset folder (used when --source local)",
    )
    parser.add_argument(
        "--manifest",
        default="./cloudinary_manifest.json",
        help="Path to cloudinary_manifest.json (used when --source cloudinary)",
    )
    parser.add_argument(
        "--output",
        default=os.getenv("EMBEDDINGS_PATH", "./embeddings_store"),
        help="Output path for embeddings (default: ./embeddings_store)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=16,
        help="Batch size for processing (reduce if memory errors)",
    )
    parser.add_argument(
        "--max-per-landmark",
        type=int,
        default=None,
        help="Max images per landmark (default: use all)",
    )

    args = parser.parse_args()

    build_embeddings(
        source=args.source,
        dataset_path=Path(args.dataset),
        manifest_path=Path(args.manifest),
        output_path=Path(args.output),
        batch_size=args.batch_size,
        max_images_per_landmark=args.max_per_landmark,
    )