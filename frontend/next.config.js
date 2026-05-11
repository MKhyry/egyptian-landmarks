// frontend/next.config.js
// ========================
// Updated for deployment:
//   - Allows images from Cloudinary (gallery images on result page)
//   - Allows images from your Render backend URL (if serving local gallery)
//   - Keeps localhost working for local development
//
// IMPORTANT: Replace YOUR_RENDER_APP with your actual Render service name.
// Example: if your Render URL is https://egyptian-landmarks-api.onrender.com
//          then hostname = "egyptian-landmarks-api.onrender.com"

/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      // ── Local development ──────────────────────────────────────────────
      {
        protocol: "http",
        hostname: "localhost",
        port: "8000",
        pathname: "/gallery/**",
      },

      // ── Render backend (production) ────────────────────────────────────
      // Replace YOUR_RENDER_APP with your actual Render service name
      {
        protocol: "https",
        hostname: "YOUR_RENDER_APP.onrender.com",
        pathname: "/gallery/**",
      },

      // ── Cloudinary (production gallery images) ─────────────────────────
      // Your gallery_images in MongoDB point to Cloudinary URLs
      {
        protocol: "https",
        hostname: "res.cloudinary.com",
        pathname: "/**",
      },
    ],
  },

  // ── Environment variable exposed to the browser ────────────────────────────
  // NEXT_PUBLIC_API_URL is set in Vercel dashboard → points to your Render URL
  // Locally it reads from frontend/.env.local
  env: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL,
  },
};

module.exports = nextConfig;