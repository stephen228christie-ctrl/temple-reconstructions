# Temple Reconstructions

Walkable 3D reconstructions of Israel's sanctuaries, built with Three.js from the measurements given in the biblical text.

| Page | Source texts |
|------|--------------|
| [`/tabernacle/`](tabernacle/index.html) | Exodus 25–30 (with 35–40) |
| [`/solomons-temple/`](solomons-temple/index.html) | 1 Kings 6–8; 2 Chronicles 3–4 |

Each page is a single self-contained HTML file (Three.js r128 from cdnjs); the site itself needs no build step.
Solomon's Temple quotes the King James Version (public domain) verbatim and flags every
element as **explicit in the text** or **interpreted / reconstructed**.
Its surroundings (Solomon's palace complex, the city of David, the wall of Jerusalem, Millo,
Gihon, the Kidron and the Mount of Olives) are placed from the text and can be seen but not entered.
Cross-references come from a search of the whole KJV Bible.

## Playing on a laptop, a phone or a gamepad

Solomon's Temple adapts to the device:

- **Laptop:** `W A S D` to walk, the mouse to look, `E` to read, `O` for settings, `U` to hide the interface. A gamepad (standard mapping) also works.
- **Phone:** a thumb-stick appears wherever the left thumb lands, the right thumb looks, and a tap reads the object. The verses open in a bottom sheet in portrait and a side sheet in landscape. The menu is a slide-in drawer.
- **Graphics:** Auto / Low / Medium / High. Static parts are batched by material, the sun's shadow map is redrawn only when something changes (people get soft contact shadows below High), and resolution scales with the frame rate.
- **Progress:** your place, views and settings are saved in the browser (`localStorage`), and the landing page offers "Continue".

The landing page images in `img/` are rendered from the models themselves.

## Editing Solomon's Temple

Edit `src/solomons-temple.src.html` (verses live in `src/kjv.json`), then run `python3 src/build.py` from the repo root.
It writes `solomons-temple/index.html` and a body-only `solomons-temple.artifact.html` for the claude.ai artifact.

## Run locally

```bash
python3 -m http.server 8000
```

## Deploy

Static site, deployed on Vercel with no framework preset.
