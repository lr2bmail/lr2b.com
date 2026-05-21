# LR2B

Minimal static landing page for LR2B.

## Files

- `index.html`
- `script.js`
- `assets/styles.css`
- `robots.txt`
- `sitemap.xml`
- `assets/`

## Cloudflare Pages

Use these settings:

- Framework preset: `None`
- Build command: `npm run build`
- Build output directory: `dist`

Do not use `/` or `.` as the output directory on Cloudflare Pages. That can upload `node_modules` and fail because dependency binaries are too large.

The compiled CSS is also committed at `assets/styles.css`, so direct static upload still works.

## Local Preview

Open `index.html` directly, or run:

```bash
python -m http.server 8080
```

## CSS

Install dependencies and rebuild the production stylesheet:

```bash
npm install
npm run build
```

For local root-file preview only:

```bash
npm run build:local
```
