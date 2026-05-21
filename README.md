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
- Build output directory: `/` or `.`

The compiled CSS is committed at `assets/styles.css`, so direct static upload also works.

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
