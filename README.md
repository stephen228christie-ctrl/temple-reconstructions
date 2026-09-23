# Temple Reconstructions

Walkable 3D reconstructions of Israel's sanctuaries, built with Three.js from the measurements given in the biblical text.

| Page | Source texts |
|------|--------------|
| [`/tabernacle/`](tabernacle/index.html) | Exodus 25–30 (with 35–40) |
| [`/solomons-temple/`](solomons-temple/index.html) | 1 Kings 6–8; 2 Chronicles 3–4 |

Each page is a single self-contained HTML file (Three.js r128 from cdnjs, no build step).
Solomon's Temple quotes the King James Version (public domain) verbatim and flags every
element as **explicit in the text** or **interpreted / reconstructed**.

## Run locally

```bash
python3 -m http.server 8000
```

## Deploy

Static site, deployed on Vercel with no framework preset.
