import { cp, mkdir, rm } from "node:fs/promises";

const files = ["index.html", "script.js", "robots.txt", "sitemap.xml"];

await rm("dist", { recursive: true, force: true });
await mkdir("dist/assets", { recursive: true });

for (const file of files) {
  await cp(file, `dist/${file}`);
}

await cp("assets/favicon.svg", "dist/assets/favicon.svg");
await cp("assets/apple-touch-icon.svg", "dist/assets/apple-touch-icon.svg");
await cp("assets/og-image.png", "dist/assets/og-image.png");
