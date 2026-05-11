"use client";
// components/UploadZone.tsx — All logic unchanged; only styling updated.

import { useCallback, useState, useRef } from "react";

interface UploadZoneProps {
  onImageSelected: (file: File) => void;
  error?: string | null;
}

const ACCEPTED_TYPES = ["image/jpeg", "image/jpg", "image/png", "image/webp"];
const MAX_SIZE_MB = 10;

export default function UploadZone({ onImageSelected, error }: UploadZoneProps) {
  const [isDragging, setIsDragging] = useState(false);
  const [preview, setPreview] = useState<string | null>(null);
  const [validationError, setValidationError] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  // ── All original logic unchanged ──────────────────────────────────────────
  const validateAndProcess = useCallback(
    (file: File) => {
      setValidationError(null);

      if (!ACCEPTED_TYPES.includes(file.type)) {
        setValidationError("Please upload a JPEG, PNG, or WebP image.");
        return;
      }

      if (file.size > MAX_SIZE_MB * 1024 * 1024) {
        setValidationError(`Image must be under ${MAX_SIZE_MB}MB.`);
        return;
      }

      const url = URL.createObjectURL(file);
      setPreview(url);
      onImageSelected(file);
    },
    [onImageSelected]
  );

  const handleDragEnter = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = (e: React.DragEvent) => {
    e.preventDefault();
    if (!e.currentTarget.contains(e.relatedTarget as Node)) {
      setIsDragging(false);
    }
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    const file = e.dataTransfer.files[0];
    if (file) validateAndProcess(file);
  };

  const handleFileInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) validateAndProcess(file);
  };

  const currentError = validationError || error;

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>

      {/* ── Drop Zone ─────────────────────────────────────────────────────── */}
      <div
        onDragEnter={handleDragEnter}
        onDragOver={(e) => e.preventDefault()}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        onClick={() => fileInputRef.current?.click()}
        style={{
          position: "relative",
          cursor: "pointer",
          borderRadius: "4px",
          border: isDragging
            ? "1px solid #C9A843"
            : "1px dashed rgba(201,168,67,0.35)",
          background: isDragging
            ? "rgba(201,168,67,0.04)"
            : "#110D07",
          padding: "3.5rem 2rem",
          textAlign: "center",
          transition: "border-color 0.25s, background 0.25s",
          overflow: "hidden",
        }}
        onMouseEnter={e => {
          if (!isDragging) {
            e.currentTarget.style.borderColor = "rgba(201,168,67,0.6)";
          }
        }}
        onMouseLeave={e => {
          if (!isDragging) {
            e.currentTarget.style.borderColor = "rgba(201,168,67,0.35)";
          }
        }}
      >
        {/* Drag-over overlay */}
        {isDragging && (
          <div
            style={{
              position: "absolute",
              inset: 0,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              background: "rgba(201,168,67,0.04)",
              borderRadius: "4px",
            }}
          >
            <p className="font-cinzel" style={{ fontSize: "1.2rem", color: "#F0C040", letterSpacing: "0.1em" }}>
              Release to upload
            </p>
          </div>
        )}

        {/* Content */}
        <div style={{ opacity: isDragging ? 0 : 1, transition: "opacity 0.2s" }}>

          {/* Upload icon circle */}
          <div
            style={{
              width: "80px",
              height: "80px",
              margin: "0 auto 1.5rem",
              borderRadius: "50%",
              border: "1px solid #8B6B20",
              background: "rgba(201,168,67,0.05)",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <svg
              width="30"
              height="30"
              viewBox="0 0 24 24"
              fill="none"
              stroke="#C9A843"
              strokeWidth="1.5"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
              <polyline points="17 8 12 3 7 8" />
              <line x1="12" y1="3" x2="12" y2="15" />
            </svg>
          </div>

          <p
            className="font-cinzel"
            style={{ fontSize: "1.15rem", fontWeight: 600, color: "#F0C040", marginBottom: "0.4rem", letterSpacing: "0.06em" }}
          >
            Upload Landmark Photo
          </p>
          <p
            className="font-lato"
            style={{ fontSize: "0.9rem", color: "#7A6030", marginBottom: "0.3rem" }}
          >
            Drag & drop or click to browse
          </p>
          <p
            className="font-lato"
            style={{ fontSize: "0.78rem", color: "rgba(122,96,48,0.7)" }}
          >
            JPEG · PNG · WebP · Max {MAX_SIZE_MB}MB
          </p>

          {/* Decorative hieroglyphs */}
          <div style={{ marginTop: "2rem", display: "flex", justifyContent: "center", gap: "1rem", fontSize: "1.4rem", opacity: 0.18, userSelect: "none" }}>
            {["𓀀", "𓂀", "𓃭", "𓄿", "𓅓"].map((g, i) => (
              <span key={i}>{g}</span>
            ))}
          </div>
        </div>

        {/* Hidden file input */}
        <input
          ref={fileInputRef}
          type="file"
          accept="image/jpeg,image/jpg,image/png,image/webp"
          style={{ display: "none" }}
          onChange={handleFileInput}
        />
      </div>

      {/* ── Error Message ──────────────────────────────────────────────────── */}
      {currentError && (
        <div
          className="font-lato"
          style={{
            background: "rgba(200,50,30,0.08)",
            border: "1px solid rgba(200,80,50,0.3)",
            borderRadius: "3px",
            padding: "0.85rem 1.1rem",
            fontSize: "0.88rem",
            color: "#e08070",
          }}
        >
          ⚠ {currentError}
        </div>
      )}

      {/* ── Example hint ──────────────────────────────────────────────────── */}
      <p
        className="font-lato"
        style={{ textAlign: "center", fontSize: "0.78rem", color: "rgba(122,96,48,0.55)" }}
      >
        Try: Pyramids of Giza · Great Sphinx · Karnak Temple · Abu Simbel · Valley of the Kings
      </p>

    </div>
  );
}
