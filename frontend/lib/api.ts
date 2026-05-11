// lib/api.ts
// ==========
// PURPOSE: Centralize all backend API calls. The frontend imports from here.

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export interface RecognitionResult {
  recognized: boolean;
  landmark_name: string | null;
  confidence: number;
  raw_similarity: number;
  description: string;
  historical_facts: string[];
  location: string;
  built_year: string | null;
  gallery_images: string[];
  tags: string[];
  all_scores: Record<string, number>;
  processing_time_ms: number;
  model_used: string;
}

export interface HealthStatus {
  status: string;
  model_loaded: boolean;
  embeddings_loaded: boolean;
  landmark_count: number;
  total_reference_images: number;
  model_name: string;
  embedding_dim: number;
}

/**
 * Send an image to the backend for landmark recognition.
 * Returns the full RecognitionResult.
 */
export async function recognizeLandmark(
  imageFile: File
): Promise<RecognitionResult> {
  const formData = new FormData();
  formData.append("file", imageFile);

  const response = await fetch(`${API_BASE}/api/recognize`, {
    method: "POST",
    body: formData,
    // Don't set Content-Type header — browser sets it automatically with boundary
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: "Unknown error" }));
    throw new Error(error.detail || `HTTP ${response.status}`);
  }

  return response.json();
}

/**
 * Fetch system health status (model loaded, embeddings ready, etc.)
 */
export async function getHealthStatus(): Promise<HealthStatus> {
  const response = await fetch(`${API_BASE}/api/health`);
  if (!response.ok) throw new Error("Health check failed");
  return response.json();
}

/**
 * Get list of all indexed landmark names
 */
export async function getLandmarkList(): Promise<string[]> {
  const response = await fetch(`${API_BASE}/api/landmarks`);
  if (!response.ok) throw new Error("Failed to fetch landmarks");
  const data = await response.json();
  return data.landmarks;
}

/**
 * Format landmark_id to display name
 * e.g. "pyramids_of_giza" → "Pyramids of Giza"
 */
export function formatLandmarkName(id: string): string {
  return id
    .split("_")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
}

/**
 * Get full gallery image URL (handles relative paths)
 */
export function getGalleryImageUrl(path: string): string {
  if (path.startsWith("http")) return path;
  return `${API_BASE}${path}`;
}