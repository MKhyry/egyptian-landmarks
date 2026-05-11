// tailwind.config.ts
import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        cinzel: ["var(--font-cinzel)", "serif"],
        lato: ["var(--font-lato)", "sans-serif"],
      },
      colors: {
        gold: {
          DEFAULT: "#c8962e",
          light: "#e8b84b",
          dim: "#8a6520",
        },
      },
      animation: {
        "fade-in-up": "fadeInUp 0.6s ease forwards",
      },
    },
  },
  plugins: [],
};

export default config;