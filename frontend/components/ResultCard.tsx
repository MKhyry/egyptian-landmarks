"use client";
// components/ResultCard.tsx — All logic unchanged; only styling updated.

import { RecognitionResult, formatLandmarkName } from "@/lib/api";

interface ResultCardProps {
  result: RecognitionResult;
  uploadedImageUrl: string | null;
}

export default function ResultCard({ result, uploadedImageUrl }: ResultCardProps) {
  if (result.recognized) {
    return <RecognizedCard result={result} uploadedImageUrl={uploadedImageUrl} />;
  }
  return <NotRecognizedCard result={result} uploadedImageUrl={uploadedImageUrl} />;
}

// ── Recognized ────────────────────────────────────────────────────────────────
function RecognizedCard({ result, uploadedImageUrl }: ResultCardProps) {
  return (
    <div
      style={{
        background: "#110D07",
        border: "1px solid rgba(201,168,67,0.3)",
        borderRadius: "4px",
        overflow: "hidden",
      }}
    >
      {/* Top status strip */}
      <div
        style={{
          padding: "0.75rem 1.5rem",
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          background: "linear-gradient(90deg, rgba(201,168,67,0.12), rgba(201,120,20,0.06))",
          borderBottom: "1px solid rgba(201,168,67,0.2)",
          flexWrap: "wrap",
          gap: "0.5rem",
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}>
          <div style={{ width: "7px", height: "7px", borderRadius: "50%", background: "#4ade80" }} />
          <span className="font-cinzel" style={{ fontSize: "0.68rem", letterSpacing: "0.18em", color: "#4ade80" }}>
            LANDMARK RECOGNIZED
          </span>
        </div>
        <span className="font-cinzel" style={{ fontSize: "0.88rem", fontWeight: 700, color: "#F0C040" }}>
          {result.confidence.toFixed(1)}% match
        </span>
      </div>

      {/* Main content — two columns */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))",
          gap: "1.5rem",
          padding: "1.75rem",
        }}
      >
        {/* Uploaded image column */}
        <div>
          <p
            className="font-cinzel"
            style={{ fontSize: "0.65rem", letterSpacing: "0.18em", color: "#7A6030", textTransform: "uppercase", marginBottom: "0.75rem" }}
          >
            Uploaded Image
          </p>
          {uploadedImageUrl && (
            <div
              style={{
                borderRadius: "3px",
                border: "1px solid rgba(201,168,67,0.2)",
                overflow: "hidden",
                aspectRatio: "16/9",
              }}
            >
              <img
                src={uploadedImageUrl}
                alt="Uploaded landmark"
                style={{ width: "100%", height: "100%", objectFit: "cover", display: "block" }}
              />
            </div>
          )}
        </div>

        {/* Landmark info column */}
        <div style={{ display: "flex", flexDirection: "column", gap: "1.1rem" }}>
          {/* Name */}
          <div>
            <p
              className="font-cinzel"
              style={{ fontSize: "0.65rem", letterSpacing: "0.18em", color: "#7A6030", textTransform: "uppercase", marginBottom: "0.3rem" }}
            >
              Identified Landmark
            </p>
            <h2
              className="font-cinzel"
              style={{ fontSize: "clamp(1.3rem,3vw,1.9rem)", fontWeight: 700, color: "#F0C040", lineHeight: 1.2, margin: 0 }}
            >
              {formatLandmarkName(result.landmark_name || "")}
            </h2>
          </div>

          {/* Meta badges */}
          <div style={{ display: "flex", flexWrap: "wrap", gap: "0.5rem" }}>
            {result.location && (
              <span
                className="font-lato"
                style={{
                  display: "inline-flex",
                  alignItems: "center",
                  gap: "5px",
                  fontSize: "0.78rem",
                  padding: "0.35rem 0.75rem",
                  borderRadius: "100px",
                  border: "1px solid rgba(201,168,67,0.22)",
                  color: "rgba(234,216,168,0.75)",
                  background: "rgba(201,168,67,0.05)",
                }}
              >
                📍 {result.location}
              </span>
            )}
            {result.built_year && (
              <span
                className="font-lato"
                style={{
                  display: "inline-flex",
                  alignItems: "center",
                  gap: "5px",
                  fontSize: "0.78rem",
                  padding: "0.35rem 0.75rem",
                  borderRadius: "100px",
                  border: "1px solid rgba(201,168,67,0.22)",
                  color: "rgba(234,216,168,0.75)",
                  background: "rgba(201,168,67,0.05)",
                }}
              >
                🏺 {result.built_year}
              </span>
            )}
          </div>

          {/* Description */}
          {result.description && (
            <p
              className="font-lato"
              style={{ fontSize: "0.9rem", color: "rgba(234,216,168,0.75)", lineHeight: 1.65, margin: 0 }}
            >
              {result.description}
            </p>
          )}

          {/* Tags */}
          {result.tags.length > 0 && (
            <div style={{ display: "flex", flexWrap: "wrap", gap: "0.4rem" }}>
              {result.tags.map((tag) => (
                <span
                  key={tag}
                  className="font-lato"
                  style={{
                    fontSize: "0.72rem",
                    padding: "0.25rem 0.6rem",
                    borderRadius: "2px",
                    background: "rgba(201,168,67,0.08)",
                    color: "#8B6B20",
                    border: "1px solid rgba(201,168,67,0.15)",
                  }}
                >
                  #{tag}
                </span>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

// ── Not Recognized ────────────────────────────────────────────────────────────
function NotRecognizedCard({ result, uploadedImageUrl }: ResultCardProps) {
  return (
    <div
      style={{
        background: "#110D07",
        border: "1px solid rgba(200,60,40,0.25)",
        borderRadius: "4px",
        overflow: "hidden",
      }}
    >
      {/* Top status strip */}
      <div
        style={{
          padding: "0.75rem 1.5rem",
          display: "flex",
          alignItems: "center",
          gap: "0.5rem",
          background: "rgba(200,60,40,0.05)",
          borderBottom: "1px solid rgba(200,60,40,0.15)",
        }}
      >
        <div style={{ width: "7px", height: "7px", borderRadius: "50%", background: "#f87171", flexShrink: 0 }} />
        <span className="font-cinzel" style={{ fontSize: "0.68rem", letterSpacing: "0.18em", color: "#f87171" }}>
          LANDMARK NOT RECOGNIZED
        </span>
      </div>

      {/* Main content */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))",
          gap: "1.5rem",
          padding: "1.75rem",
        }}
      >
        {uploadedImageUrl && (
          <div>
            <p
              className="font-cinzel"
              style={{ fontSize: "0.65rem", letterSpacing: "0.18em", color: "#7A6030", textTransform: "uppercase", marginBottom: "0.75rem" }}
            >
              Uploaded Image
            </p>
            <div
              style={{
                position: "relative",
                borderRadius: "3px",
                border: "1px solid rgba(200,60,40,0.2)",
                overflow: "hidden",
                aspectRatio: "16/9",
              }}
            >
              <img
                src={uploadedImageUrl}
                alt="Uploaded landmark"
                style={{ width: "100%", height: "100%", objectFit: "cover", opacity: 0.5, display: "block" }}
              />
              <div
                style={{
                  position: "absolute",
                  inset: 0,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  fontSize: "3rem",
                  opacity: 0.5,
                }}
              >
                𓃾
              </div>
            </div>
          </div>
        )}

        <div style={{ display: "flex", flexDirection: "column", justifyContent: "center", gap: "1rem" }}>
          <div style={{ fontSize: "2.5rem" }}>🔍</div>
          <h2
            className="font-cinzel"
            style={{ fontSize: "1.6rem", fontWeight: 700, color: "#f87171", margin: 0 }}
          >
            Not Recognized
          </h2>
          <p
            className="font-lato"
            style={{ fontSize: "0.9rem", color: "rgba(234,216,168,0.6)", lineHeight: 1.65, margin: 0 }}
          >
            The AI could not confidently identify this landmark. Best similarity score was{" "}
            <span style={{ color: "#C9A843" }}>{result.confidence.toFixed(1)}%</span>, below the recognition threshold.
          </p>

          <div style={{ fontSize: "0.82rem" }} className="font-lato">
            <p style={{ color: "#7A6030", marginBottom: "0.4rem" }}>Tips for better results:</p>
            <ul style={{ color: "rgba(122,96,48,0.8)", paddingLeft: "1.2rem", display: "flex", flexDirection: "column", gap: "0.25rem", margin: 0 }}>
              <li>Use a clear, well-lit photo</li>
              <li>Center the landmark in the frame</li>
              <li>Avoid extreme angles or cropping</li>
              <li>Make sure the landmark is in the dataset</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
