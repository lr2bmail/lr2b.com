/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./script.js"],
  theme: {
    extend: {
      colors: {
        ink: "#17233f",
        muted: "#5f6f89",
        line: "#cfe0f5",
        paper: "#ffffff",
        panel: "#f2f8ff",
        accent: "#007ee5"
      },
      fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui", "sans-serif"]
      }
    }
  },
  plugins: []
};
