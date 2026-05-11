"use client";
// components/ConfidenceMeter.tsx — All logic unchanged; only styling updated.

import { useEffect, useState } from "react";
import { formatLandmarkName } from "@/lib/api";

interface ConfidenceMeterProps {
  confidence: number;
  allScores: Record<string, number>;
}

export default function ConfidenceMeter({ confidence, allScores }: ConfidenceMeterProps) {
  const [animated, setAnimated] = useState(false);

  // ── All original logic unchanged ──────────────────────────────────────────
  useEffect(() => {
    const timer = setTimeout(() => setAnimated(true), 100);
    return () => clearTimeout(timer);
  }, []);

  const getConfidenceLabel = (score: number) => {
    if (score >= 90) return { label: "Exceptional", color: "#4ade80" };
    if (score >= 80) return { label: "Very High",   color: "#86efac" };
    if (score >= 70) return { label: "High",        color: "#F0C040" };
    if (score >= 65) return { label: "Confident",   color: "#C9A843" };
    return              { label: "Low",         color: "#f87171" };
  };

  const { label, color } = getConfidenceLabel(confidence);
  const sortedScores = Object.entries(allScores).sort(([, a], [, b]) => b - a).slice(0, 6);

  return (
    <section
      style={{
        background: "#110D07",
        border: "1px solid rgba(201,168,67,0.22)",
        borderRadius: "4px",
        padding: "1.75rem 2rem",
      }}
    >
      <div className="section-label">AI CONFIDENCE ANALYSIS</div>

      {/* ── Big score number ──────────────────────────────────────────────── */}
      <div style={{ display: "flex", alignItems: "flex-end", gap: "0.75rem", marginBottom: "1.2rem" }}>
        <span
          className="font-cinzel"
          style={{ fontSize: "clamp(3rem,8vw,5rem)", fontWeight: 900, lineHeight: 1, color }}
        >
          {confidence.toFixed(0)}
        </span>
        <div style={{ paddingBottom: "0.4rem" }}>
          <span className="font-cinzel" style={{ fontSize: "1.4rem", color: "rgba(234,216,168,0.4)" }}>%</span>
          <p className="font-lato" style={{ fontSize: "0.78rem", marginTop: "2px", color }}>{label} Confidence</p>
        </div>
      </div>

      {/* ── Animated bar ─────────────────────────────────────────────────── */}
      <div style={{ marginBottom: "2.5rem" }}>
        <div
          style={{
            height: "5px",
            background: "rgba(255,255,255,0.07)",
            borderRadius: "3px",
            overflow: "hidden",
          }}
        >
          <div
            style={{
              height: "100%",
              width: animated ? `${confidence}%` : "0%",
              background: `linear-gradient(90deg, ${color}70, ${color})`,
              boxShadow: `0 0 10px ${color}40`,
              borderRadius: "3px",
              transition: "width 1.1s cubic-bezier(0.22,1,0.36,1)",
            }}
          />
        </div>

        {/* Threshold marker */}
        <div style={{ position: "relative", marginTop: "4px" }}>
          <div
            style={{
              position: "absolute",
              left: "65%",
              top: "-9px",
              width: "1px",
              height: "10px",
              background: "rgba(201,168,67,0.4)",
            }}
          />
          <p
            className="font-lato"
            style={{
              position: "absolute",
              left: "65%",
              transform: "translateX(-50%)",
              top: "3px",
              fontSize: "0.68rem",
              color: "#7A6030",
              whiteSpace: "nowrap",
            }}
          >
            threshold (65%)
          </p>
        </div>
      </div>

      {/* ── All scores ───────────────────────────────────────────────────── */}
      <div>
        <p
          className="font-cinzel"
          style={{ fontSize: "0.65rem", letterSpacing: "0.18em", color: "#7A6030", textTransform: "uppercase", marginBottom: "0.85rem" }}
        >
          All Landmark Scores
        </p>
        <div style={{ display: "flex", flexDirection: "column", gap: "0.65rem" }}>
          {sortedScores.map(([landmark, score], i) => (
            <div key={landmark}>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "4px" }}>
                <span
                  className="font-lato"
                  style={{
                    fontSize: "0.85rem",
                    color: i === 0 ? "#EAD8A8" : "rgba(234,216,168,0.5)",
                  }}
                >
                  {i === 0 && <span style={{ color: "#C9A843" }}>★ </span>}
                  {formatLandmarkName(landmark)}
                </span>
                <span
                  className="font-cinzel"
                  style={{
                    fontSize: "0.78rem",
                    fontWeight: 600,
                    color: score >= 65 ? "#F0C040" : "rgba(201,168,67,0.35)",
                  }}
                >
                  {score.toFixed(1)}%
                </span>
              </div>
              <div style={{ height: "3px", background: "rgba(201,168,67,0.1)", borderRadius: "2px", overflow: "hidden" }}>
                <div
                  style={{
                    height: "100%",
                    borderRadius: "2px",
                    width: animated ? `${score}%` : "0%",
                    transition: `width 0.8s cubic-bezier(0.22,1,0.36,1) ${i * 80}ms`,
                    background: i === 0
                      ? "linear-gradient(90deg, #8B6B20, #F0C040)"
                      : "rgba(201,168,67,0.22)",
                  }}
                />
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
