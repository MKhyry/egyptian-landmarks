"use client";
// app/page.tsx — Home page (upload). All logic unchanged; only styling updated.

import { useState, useCallback } from "react";
import { useRouter } from "next/navigation";
import { recognizeLandmark, RecognitionResult } from "@/lib/api";
import UploadZone from "@/components/UploadZone";

export default function HomePage() {
  const router = useRouter();
  const [isProcessing, setIsProcessing] = useState(false);
  const [processingStage, setProcessingStage] = useState("");
  const [error, setError] = useState<string | null>(null);

  // ── All original logic unchanged ──────────────────────────────────────────
  const handleImageUpload = useCallback(
    async (file: File) => {
      setError(null);
      setIsProcessing(true);

      try {
        const stages = [
          "Loading image...",
          "Extracting visual features with CLIP...",
          "Generating embedding fingerprint...",
          "Comparing against landmark database...",
          "Computing cosine similarity...",
          "Analyzing results...",
        ];

        let stageIndex = 0;
        setProcessingStage(stages[0]);

        const stageTimer = setInterval(() => {
          stageIndex = Math.min(stageIndex + 1, stages.length - 1);
          setProcessingStage(stages[stageIndex]);
        }, 600);

        const result: RecognitionResult = await recognizeLandmark(file);
        clearInterval(stageTimer);

        sessionStorage.setItem("recognitionResult", JSON.stringify(result));
        sessionStorage.setItem("uploadedImageUrl", URL.createObjectURL(file));

        router.push("/result");
      } catch (err) {
        setError(
          err instanceof Error
            ? err.message
            : "Recognition failed. Please try again."
        );
        setIsProcessing(false);
        setProcessingStage("");
      }
    },
    [router]
  );

  return (
    <main className="bg-desert-gradient" style={{ minHeight: "100vh", display: "flex", flexDirection: "column" }}>

      {/* ── Header ──────────────────────────────────────────────────────────── */}
      <header style={{ textAlign: "center", paddingTop: "3.5rem", paddingBottom: "2rem", paddingLeft: "1rem", paddingRight: "1rem", borderBottom: "1px solid rgba(201,168,67,0.18)" }}>
        <div style={{ fontSize: "2.8rem", lineHeight: 1, marginBottom: "0.7rem", opacity: 0.8 }}>𓂀</div>

        <h1
          className="font-cinzel"
          style={{ fontSize: "clamp(2rem,5vw,3.2rem)", fontWeight: 700, color: "#F0C040", letterSpacing: "0.18em", textTransform: "uppercase", lineHeight: 1, margin: 0 }}
        >
          KEMET LENS
        </h1>

        <p
          className="font-cinzel"
          style={{ marginTop: "0.5rem", fontSize: "0.85rem", letterSpacing: "0.28em", color: "#7A6030", textTransform: "uppercase" }}
        >
          Egyptian Landmark Recognition
        </p>

        <div className="ornament-divider" style={{ maxWidth: "360px", margin: "1.4rem auto 0" }}>
          <span className="font-cinzel" style={{ fontSize: "0.68rem", letterSpacing: "0.22em", color: "#7A6030", whiteSpace: "nowrap" }}>
            AI · VISION · HISTORY
          </span>
        </div>
      </header>

      {/* ── Upload / Processing ──────────────────────────────────────────────── */}
      <div style={{ flex: 1, display: "flex", alignItems: "center", justifyContent: "center", padding: "2.5rem 1.5rem" }}>
        <div style={{ width: "100%", maxWidth: "680px" }}>
          {!isProcessing ? (
            <UploadZone onImageSelected={handleImageUpload} error={error} />
          ) : (
            <ProcessingDisplay stage={processingStage} />
          )}
        </div>
      </div>

      {/* ── How it Works ─────────────────────────────────────────────────────── */}
      <section style={{ maxWidth: "900px", margin: "0 auto", padding: "0 1.5rem 4rem" }}>
        <div className="ornament-divider" style={{ marginBottom: "2rem" }}>
          <span className="font-cinzel" style={{ fontSize: "0.68rem", letterSpacing: "0.22em", color: "#7A6030", whiteSpace: "nowrap" }}>
            HOW IT WORKS
          </span>
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))", gap: "0.75rem" }}>
          {PIPELINE_STEPS.map((step, i) => (
            <div
              key={i}
              style={{
                textAlign: "center",
                padding: "1.25rem 1rem",
                background: "#110D07",
                border: "1px solid rgba(201,168,67,0.18)",
                borderRadius: "4px",
              }}
            >
              <div style={{ fontSize: "1.8rem", marginBottom: "0.6rem" }}>{step.icon}</div>
              <div
                className="font-cinzel"
                style={{ fontSize: "0.7rem", fontWeight: 700, color: "#C9A843", letterSpacing: "0.12em", marginBottom: "0.4rem" }}
              >
                {String(i + 1).padStart(2, "0")}
              </div>
              <div
                className="font-lato"
                style={{ fontSize: "0.82rem", color: "#7A6030", lineHeight: 1.5 }}
              >
                {step.label}
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* ── Footer ───────────────────────────────────────────────────────────── */}
      <footer style={{ textAlign: "center", padding: "1.5rem", borderTop: "1px solid rgba(201,168,67,0.12)", color: "#7A6030", fontSize: "0.82rem", fontStyle: "italic" }}>
        Powered by CLIP · FAISS · Next.js &nbsp;·&nbsp; Uncovering the wonders of ancient Egypt
      </footer>

    </main>
  );
}

// ── Processing Display ────────────────────────────────────────────────────────
// All original logic is inline; only visual markup updated.
function ProcessingDisplay({ stage }: { stage: string }) {
  return (
    <div style={{ textAlign: "center", padding: "4rem 1rem" }}>
      {/* Scanning eye */}
      <div
        style={{
          position: "relative",
          width: "120px",
          height: "120px",
          margin: "0 auto 2rem",
          borderRadius: "50%",
          border: "1.5px solid #C9A843",
          overflow: "hidden",
          background: "rgba(17,13,7,0.8)",
        }}
      >
        <div
          style={{
            position: "absolute",
            inset: 0,
            background: "radial-gradient(circle, rgba(201,168,67,0.15), transparent)",
            borderRadius: "50%",
          }}
        />
        <div
          className="scan-line"
          style={{
            position: "absolute",
            left: 0,
            right: 0,
            height: "1px",
            background: "#F0C040",
            boxShadow: "0 0 10px #C9A843",
          }}
        />
        <div
          style={{
            position: "absolute",
            inset: 0,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            fontSize: "3rem",
          }}
        >
          𓂀
        </div>
      </div>

      <p
        className="font-cinzel"
        style={{ fontSize: "1.1rem", fontWeight: 600, color: "#F0C040", marginBottom: "0.5rem" }}
      >
        Analyzing Landmark...
      </p>

      <p
        className="font-lato"
        style={{ fontSize: "0.88rem", color: "#7A6030", minHeight: "1.4em", transition: "opacity 0.4s" }}
      >
        {stage}
      </p>

      {/* Animated dots */}
      <div style={{ display: "flex", justifyContent: "center", gap: "6px", marginTop: "1.5rem" }}>
        {[0, 1, 2].map((i) => (
          <div
            key={i}
            className="dot-bounce"
            style={{
              width: "7px",
              height: "7px",
              borderRadius: "50%",
              background: "#C9A843",
              animationDelay: `${i * 160}ms`,
            }}
          />
        ))}
      </div>
    </div>
  );
}

// ── Pipeline Steps ────────────────────────────────────────────────────────────
const PIPELINE_STEPS = [
  { icon: "📸", label: "Upload a photo of any Egyptian landmark" },
  { icon: "🧠", label: "CLIP model extracts visual features into a 512-dim embedding" },
  { icon: "🔍", label: "Cosine similarity matches against indexed landmarks" },
  { icon: "🏛️", label: "Return landmark info, confidence, and history" },
];
