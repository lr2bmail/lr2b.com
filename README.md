# LR2B

Minimal landing page for **lr2b.com**.

LR2B is a small dev team building digital products that work: websites, apps, bots, automation, AI/scraping systems, VPN/proxy tools, and trading systems.

## Live Site

- Domain: [lr2b.com](https://lr2b.com)
- Repository: [github.com/lr2bmail/lr2b.com](https://github.com/lr2bmail/lr2b.com)

## Stack

- Static HTML
- Tailwind CSS CDN
- Small vanilla JavaScript menu
- SEO metadata, Open Graph tags, sitemap, robots file, and JSON-LD structured data

## Project Structure

```text
.
├── index.html
├── script.js
├── robots.txt
├── sitemap.xml
├── CNAME
└── assets/
    ├── apple-touch-icon.svg
    ├── favicon.svg
    └── og-image.png
```

## Deploy

This repo is ready for GitHub Pages.

1. Push changes to `main`.
2. GitHub Actions deploys the static site.
3. Point the domain `lr2b.com` to GitHub Pages.

## Local Preview

Open `index.html` directly in a browser, or run a tiny static server:

```bash
python -m http.server 8080
```

Then open `http://localhost:8080`.

## Contact

[contact@lr2b.com](mailto:contact@lr2b.com)
