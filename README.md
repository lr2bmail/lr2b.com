# LR2B

Static website for lr2b.com, hosted on Cloudflare Pages (deploys on every push to `main`).

## Files

| Path | What it is | How to change it |
|---|---|---|
| `index.html` | Home page | Edit by hand |
| `work/<slug>/`, `privacy/`, `terms/`, `404.html` | Product pages, legal pages, not-found page | Generated: edit `tools/build_pages.py`, then run `python tools/build_pages.py` |
| `assets/home.css` | The one stylesheet (fonts included) | Edit, then bump `?v=` in `index.html` and `CSS_VERSION` in `tools/build_pages.py` |
| `assets/fonts/` | IBM Plex, self-hosted (SIL OFL 1.1) | - |
| `assets/work/*.webp` | Cropped screenshots on the home page (800×500); `firevpn-phone.webp` is the app screen | Replace the file |
| `assets/work/full/*.webp` | Full screenshots on product pages (1200×758) | Replace the file |
| `assets/og/*.jpg`, `assets/og-image.png` | Share images (1200×630) for product pages and the home page | Replace the file |
| `script.js` | Copy-email button and the enquiry form (opens the visitor's email app; there is no server) | Edit |
| `_headers` | Security headers and font caching (Cloudflare Pages) | Edit |
| `sitemap.xml`, `robots.txt` | SEO | Add a line when you add a page |

Rules: list only the products shown here unless the owner says otherwise. Show only real numbers; no download counts.

## Cloudflare Pages

- Framework preset: `None`
- Build command: leave empty
- Build output directory: `/`

## Local preview

```bash
python -m http.server 8080
```
