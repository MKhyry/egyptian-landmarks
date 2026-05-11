"use client";
// app/result/page.tsx — All logic unchanged; only styling updated.

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { RecognitionResult, formatLandmarkName } from "@/lib/api";
import ResultCard from "@/components/ResultCard";
import ConfidenceMeter from "@/components/ConfidenceMeter";
import Link from "next/link";

export default function ResultPage() {
  const router = useRouter();
  const [result, setResult] = useState<RecognitionResult | null>(null);
  const [uploadedImageUrl, setUploadedImageUrl] = useState<string | null>(null);

  // ── All original logic unchanged ──────────────────────────────────────────
  useEffect(() => {
    const storedResult = sessionStorage.getItem("recognitionResult");
    const storedImage = sessionStorage.getItem("uploadedImageUrl");

    if (!storedResult) {
      router.replace("/");
      return;
    }

    setResult(JSON.parse(storedResult));
    setUploadedImageUrl(storedImage);
  }, [router]);

  if (!result) {
    return (
      <div
        className="bg-desert-gradient"
        style={{ minHeight: "100vh", display: "flex", alignItems: "center", justifyContent: "center" }}
      >
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: "1rem" }}>
          <div className="eye-pulse" style={{ fontSize: "3rem" }}>𓂀</div>
          <span className="font-cinzel" style={{ color: "#7A6030", fontSize: "0.85rem", letterSpacing: "0.2em" }}>
            LOADING...
          </span>
        </div>
      </div>
    );
  }

  return (
    <main className="bg-desert-gradient" style={{ minHeight: "100vh" }}>

      {/* ── Header ──────────────────────────────────────────────────────────── */}
      <header style={{ textAlign: "center", paddingTop: "2.5rem", paddingBottom: "1.5rem", paddingLeft: "1rem", paddingRight: "1rem", borderBottom: "1px solid rgba(201,168,67,0.18)" }}>
        <Link
          href="/"
          className="font-cinzel"
          style={{ display: "inline-block", fontSize: "0.7rem", letterSpacing: "0.2em", color: "#7A6030", textDecoration: "none", marginBottom: "1.2rem", transition: "color 0.2s" }}
          onMouseEnter={e => (e.currentTarget.style.color = "#C9A843")}
          onMouseLeave={e => (e.currentTarget.style.color = "#7A6030")}
        >
          ← NEW SEARCH
        </Link>

        <div style={{ fontSize: "2.2rem", lineHeight: 1, marginBottom: "0.6rem", opacity: 0.65 }}>𓂀</div>

        <h1
          className="font-cinzel"
          style={{ fontSize: "clamp(1.6rem,4vw,2.4rem)", fontWeight: 700, color: "#F0C040", letterSpacing: "0.16em", textTransform: "uppercase", lineHeight: 1, margin: 0 }}
        >
          RECOGNITION RESULT
        </h1>
      </header>

      {/* ── Content ─────────────────────────────────────────────────────────── */}
      <div style={{ maxWidth: "960px", margin: "0 auto", padding: "2.5rem 1.5rem 5rem" }}>

        {/* Result Card */}
        <div className="animate-fade-in-up" style={{ marginBottom: "1.5rem" }}>
          <ResultCard result={result} uploadedImageUrl={uploadedImageUrl} />
        </div>

        {/* Confidence Meter */}
        {result.recognized && (
          <div className="animate-fade-in-up delay-100" style={{ marginBottom: "1.5rem" }}>
            <ConfidenceMeter confidence={result.confidence} allScores={result.all_scores} />
          </div>
        )}

        {/* Historical Facts */}
        {result.recognized && result.historical_facts.length > 0 && (
          <div className="animate-fade-in-up delay-200" style={{ marginBottom: "1.5rem" }}>
            <HistoricalFacts facts={result.historical_facts} />
          </div>
        )}

        {/* AI Debug Panel */}
        <div className="animate-fade-in-up delay-400" style={{ marginBottom: "2rem" }}>
          <AIDebugPanel result={result} />
        </div>

        {/* Try Again */}
        <div style={{ textAlign: "center", paddingTop: "1rem" }}>
          <Link
            href="/"
            className="font-cinzel"
            style={{
              display: "inline-block",
              fontSize: "0.8rem",
              letterSpacing: "0.14em",
              textTransform: "uppercase",
              padding: "0.75rem 2rem",
              border: "1px solid #8B6B20",
              color: "#C9A843",
              textDecoration: "none",
              borderRadius: "2px",
              transition: "all 0.2s",
              background: "transparent",
            }}
            onMouseEnter={e => {
              e.currentTarget.style.background = "rgba(201,168,67,0.08)";
              e.currentTarget.style.borderColor = "#C9A843";
            }}
            onMouseLeave={e => {
              e.currentTarget.style.background = "transparent";
              e.currentTarget.style.borderColor = "#8B6B20";
            }}
          >
            RECOGNIZE ANOTHER LANDMARK
          </Link>
        </div>

      </div>
    </main>
  );
}

// ── Historical Facts ──────────────────────────────────────────────────────────
function HistoricalFacts({ facts }: { facts: string[] }) {
  return (
    <section
      style={{
        background: "#110D07",
        border: "1px solid rgba(201,168,67,0.22)",
        borderRadius: "4px",
        padding: "1.75rem 2rem",
      }}
    >
      <div className="section-label">HISTORICAL FACTS</div>

      <div style={{ display: "flex", flexDirection: "column", gap: "0.65rem" }}>
        {facts.map((fact, i) => (
          <div
            key={i}
            style={{
              display: "flex",
              gap: "0.9rem",
              background: "rgba(255,255,255,0.025)",
              border: "1px solid rgba(201,168,67,0.18)",
              borderLeft: "3px solid #8B6B20",
              padding: "0.75rem 1rem",
              borderRadius: "2px",
            }}
          >
            <span
              className="font-cinzel"
              style={{ fontSize: "0.68rem", color: "#C9A843", flexShrink: 0, marginTop: "2px", fontWeight: 600 }}
            >
              {String(i + 1).padStart(2, "0")}.
            </span>
            <span
              className="font-lato"
              style={{ fontSize: "0.92rem", color: "#EAD8A8", lineHeight: 1.6 }}
            >
              {fact}
            </span>
          </div>
        ))}
      </div>
    </section>
  );
}

// ── AI Debug Panel ────────────────────────────────────────────────────────────
// All original logic unchanged; only styling updated.
function AIDebugPanel({ result }: { result: RecognitionResult }) {
  const [isOpen, setIsOpen] = useState(false);
  const sortedScores = Object.entries(result.all_scores)
    .sort(([, a], [, b]) => b - a)
    .slice(0, 8);

  return (
    <section
      style={{
        background: "#110D07",
        border: "1px solid rgba(201,168,67,0.15)",
        borderRadius: "4px",
        overflow: "hidden",
      }}
    >
      <button
        onClick={() => setIsOpen(!isOpen)}
        style={{
          width: "100%",
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          padding: "1rem 1.5rem",
          background: "transparent",
          border: "none",
          cursor: "pointer",
          textAlign: "left",
          transition: "background 0.2s",
        }}
        onMouseEnter={e => (e.currentTarget.style.background = "rgba(201,168,67,0.05)")}
        onMouseLeave={e => (e.currentTarget.style.background = "transparent")}
      >
        <span className="font-cinzel" style={{ fontSize: "0.68rem", letterSpacing: "0.18em", color: "#7A6030" }}>
          🔬 AI REASONING — SIMILARITY SCORES
        </span>
        <span style={{ color: "#7A6030", fontSize: "0.75rem" }}>{isOpen ? "▲" : "▼"}</span>
      </button>

      {isOpen && (
        <div style={{ padding: "0 1.5rem 1.5rem", background: "rgba(7,5,3,0.4)" }}>
          <div style={{ display: "flex", gap: "2rem", marginBottom: "1rem", paddingBottom: "0.75rem", borderBottom: "1px solid rgba(201,168,67,0.1)" }}>
            <span className="font-lato" style={{ fontSize: "0.8rem", color: "#7A6030" }}>
              Model: {result.model_used}
            </span>
            <span className="font-lato" style={{ fontSize: "0.8rem", color: "#7A6030" }}>
              Time: {result.processing_time_ms}ms
            </span>
          </div>

          <div style={{ display: "flex", flexDirection: "column", gap: "0.6rem" }}>
            {sortedScores.map(([landmark, score]) => (
              <div key={landmark}>
                <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "3px" }}>
                  <span className="font-lato" style={{ fontSize: "0.82rem", color: "#EAD8A8", opacity: 0.75 }}>
                    {formatLandmarkName(landmark)}
                  </span>
                  <span
                    className="font-cinzel"
                    style={{ fontSize: "0.78rem", fontWeight: 600, color: score >= 65 ? "#F0C040" : "rgba(201,168,67,0.35)" }}
                  >
                    {score.toFixed(1)}%
                  </span>
                </div>
                <div style={{ height: "3px", background: "rgba(201,168,67,0.1)", borderRadius: "2px", overflow: "hidden" }}>
                  <div
                    style={{
                      height: "100%",
                      width: `${score}%`,
                      background: score >= 65 ? "#C9A843" : "rgba(201,168,67,0.25)",
                      borderRadius: "2px",
                      transition: "width 0.7s ease",
                    }}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </section>
  );
}
