# lr2b.com: agent guide

Static site for LR2B (product studio). Read `README.md` for which file does what.

## Rules
1. List only the products already on the site unless the owner adds one. The owner's global CLAUDE.md names a project
   that must never appear here; check it before adding anything.
2. Real numbers only. No download counts, no invented stats, testimonials or clients.
3. Pushing to `main` deploys the live site (Cloudflare). Commit locally; push only with the owner's go-ahead.
   After a push: check the live pages, run `pwsh E:\tools\snapshot.ps1`, add a dated line to `E:\CHANGELOG.md`.

## How to change things
- Home page: edit `index.html` by hand.
- Product pages (`work/<slug>/`), `privacy/`, `terms/`, `404.html`: edit `tools/build_pages.py`, run `python tools/build_pages.py`.
  Never hand-edit those generated files.
- Styles: `assets/home.css` only. Bump `?v=` in `index.html` and `CSS_VERSION` in `tools/build_pages.py` after a change.
- New product: add it to `PRODUCTS` in the build script, a card and a "Running now" row in `index.html`, a line in
  `sitemap.xml`, and screenshots (`assets/work/<slug>.webp` 800×500 crop, `assets/work/full/<slug>.webp` 1200×758,
  `assets/og/<slug>.jpg` 1200×630).
- No external requests: fonts are self-hosted, and `_headers` sets a strict Content-Security-Policy (`'self'` only).
  Anything loaded from another domain will be blocked unless the policy is changed.

## Known open items (owner's Cloudflare dashboard, not files)
- `www.lr2b.com` has no DNS record.
- "Always Use HTTPS" is off (plain http is not redirected).
- Unknown URLs return an empty 404 instead of `404.html` (likely a Worker with not-found handling off).
