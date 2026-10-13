"""Build the installable web app in docs/ from src/docket.html.

src/docket.html is written as page content (no <html>/<head>), so it can be
published as a Claude artifact unchanged. This script wraps it in a full
document with the home-screen metadata iPad needs, and draws the app icon.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "docket.html"
OUT = ROOT / "docs"

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Docket">
<meta name="theme-color" content="#000000">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="icon" type="image/png" href="icon-192.png">
<style>
:root { padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); color-scheme: light; }
body { margin: 0; font: 14px system-ui, sans-serif; }
img { max-width: 100%; }
[hidden] { display: none !important; }
</style>
</head>
<body>
"""

MANIFEST = """{
  "name": "Docket Planner",
  "short_name": "Docket",
  "start_url": "./",
  "display": "standalone",
  "orientation": "any",
  "background_color": "#f3f3f3",
  "theme_color": "#000000",
  "icons": [
    { "src": "icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable" }
  ]
}
"""


def icon(size: int) -> Image.Image:
    img = Image.new("RGB", (size, size), "#000000")
    d = ImageDraw.Draw(img)
    s = size / 512
    # three ledger lines with a tick on the first
    for i, y in enumerate((170, 256, 342)):
        d.rounded_rectangle([200 * s, (y - 14) * s, 400 * s, (y + 14) * s], radius=14 * s,
                            fill="#ffffff" if i == 0 else "#8a8a8a")
        d.rounded_rectangle([108 * s, (y - 30) * s, 168 * s, (y + 30) * s], radius=14 * s,
                            fill="#ffffff" if i == 0 else None, outline="#ffffff", width=max(1, int(10 * s)))
    d.line([(122 * s, 170 * s), (134 * s, 184 * s), (156 * s, 154 * s)], fill="#000000", width=max(2, int(12 * s)), joint="curve")
    return img


def main() -> None:
    OUT.mkdir(exist_ok=True)
    (OUT / "index.html").write_text(HEAD + SRC.read_text() + "\n</body>\n</html>\n")
    (OUT / "manifest.webmanifest").write_text(MANIFEST)
    for n in (180, 192, 512):
        icon(n).save(OUT / f"icon-{n}.png")
    print("built", OUT)


if __name__ == "__main__":
    main()
