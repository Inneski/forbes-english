#!/usr/bin/env python3
"""
Forbes English — cover-image palette extractor.

Derives a lesson's colour theme FROM its hero/cover image, so every lesson is
"inspired by the colour palette of the cover image aesthetics" in a repeatable,
non-vibes way.

Usage:
    python3 lesson-template/extract-palette.py <path-to-hero-image> [--light]

Outputs a ready-to-paste CSS :root block plus a WCAG contrast report.
Default is a dark theme (dark canvas, light text). Pass --light for a
paper/light theme.

Requires: pillow  (pip install pillow --break-system-packages)
"""

import sys
import colorsys
from collections import Counter

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is required:  pip install pillow --break-system-packages")


# ─────────────────────────────────────────────────────────── helpers ──

def hex_of(rgb):
    return "#%02x%02x%02x" % tuple(int(round(c)) for c in rgb)


def rel_luminance(rgb):
    """WCAG relative luminance."""
    out = []
    for c in rgb:
        c = c / 255.0
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    r, g, b = out
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = rel_luminance(a), rel_luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def to_hls(rgb):
    r, g, b = [c / 255.0 for c in rgb]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h, l, s


def from_hls(h, l, s):
    r, g, b = colorsys.hls_to_rgb(h, max(0.0, min(1.0, l)), max(0.0, min(1.0, s)))
    return (r * 255, g * 255, b * 255)


def shift(rgb, dl=0.0, ds=0.0):
    h, l, s = to_hls(rgb)
    return from_hls(h, l + dl, s + ds)


def hue_distance(h1, h2):
    d = abs(h1 - h2) % 1.0
    return min(d, 1.0 - d)


# ────────────────────────────────────────────────────── extraction ──

def dominant_colours(path, k=14):
    """Quantise the image and return [(rgb, weight), ...] most-common first."""
    img = Image.open(path).convert("RGB")
    img.thumbnail((360, 360))
    q = img.quantize(colors=k, method=Image.Quantize.FASTOCTREE).convert("RGB")
    colours = q.getcolors(maxcolors=1 << 24) or []
    total = sum(n for n, _ in colours) or 1
    colours.sort(key=lambda x: -x[0])
    return [(rgb, n / total) for n, rgb in colours]


def build_palette(path, dark=True):
    pals = dominant_colours(path)

    # Accent = the most colourful thing with enough presence to read as "the"
    # colour of the image. Weight saturation by a little bit of coverage so a
    # single stray neon pixel cannot hijack the theme.
    def accent_score(item):
        rgb, w = item
        _, l, s = to_hls(rgb)
        mid = 1.0 - abs(l - 0.5) * 1.4          # prefer mid lightness
        return s * max(mid, 0.05) * (w ** 0.28)

    accent = max(pals, key=accent_score)[0]
    ah, al, asat = to_hls(accent)

    # Secondary = the most colourful thing far enough away in hue to contrast.
    def secondary_score(item):
        rgb, w = item
        h, l, s = to_hls(rgb)
        return s * hue_distance(h, ah) * (w ** 0.25)

    secondary = max(pals, key=secondary_score)[0]

    # Canvas + text anchors, pulled from the image's own extremes so the page
    # feels like it belongs to the picture rather than a generic dark theme.
    darkest = min(pals, key=lambda i: rel_luminance(i[0]))[0]
    lightest = max(pals, key=lambda i: rel_luminance(i[0]))[0]

    if dark:
        # Never a pure black canvas: keep a whisper of the image's own hue so
        # the page reads as "this picture, darkened" rather than generic dark mode.
        dh, _, ds_ = to_hls(darkest)
        void = from_hls(dh, max(0.045, min(0.075, to_hls(darkest)[1] * 0.5)),
                        min(0.22, max(0.06, ds_)))
        surface = shift(void, dl=+0.045, ds=+0.01)
        surface2 = shift(void, dl=+0.085, ds=+0.01)
        border = shift(accent, dl=-0.20, ds=-0.30)
        # Warm the text very slightly toward the accent hue for cohesion.
        text = from_hls(ah, 0.955, 0.16)
        if contrast(text, surface) < 8:
            text = (244, 240, 233)
        text_dim = shift(text, dl=-0.26, ds=+0.02)
        accent_bright = shift(accent, dl=+0.14, ds=+0.06)
        accent_dim = shift(accent, dl=-0.18, ds=-0.05)
    else:
        void = shift(lightest, dl=+0.22, ds=-0.45)
        surface = (255, 255, 255)
        surface2 = shift(void, dl=-0.035, ds=+0.01)
        border = shift(accent, dl=+0.28, ds=-0.35)
        text = shift(darkest, dl=-0.12, ds=-0.25)
        if contrast(text, surface) < 8:
            text = (26, 28, 32)
        text_dim = shift(text, dl=+0.30, ds=+0.02)
        accent_bright = shift(accent, dl=-0.10, ds=+0.08)
        accent_dim = shift(accent, dl=+0.24, ds=-0.20)

    return {
        "void": void, "surface": surface, "surface2": surface2,
        "border": border, "text": text, "text-dim": text_dim,
        "accent": accent, "accent-bright": accent_bright,
        "accent-dim": accent_dim, "secondary": secondary,
    }


# ──────────────────────────────────────────────────────────── output ──

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    dark = "--light" not in sys.argv
    path = args[0]
    p = build_palette(path, dark=dark)

    print(f"/* Palette derived from {path} ({'dark' if dark else 'light'} theme) */")
    print(":root {")
    order = ["void", "surface", "surface2", "border", "text", "text-dim",
             "accent", "accent-bright", "accent-dim", "secondary"]
    width = max(len(k) for k in order)
    for key in order:
        print(f"  --{key.ljust(width)} : {hex_of(p[key])};")
    print("}")

    print("\n/* Contrast report — body text must be >= 4.5, ideally >= 7 */")
    checks = [
        ("text on surface", p["text"], p["surface"]),
        ("text on void", p["text"], p["void"]),
        ("text-dim on surface", p["text-dim"], p["surface"]),
        ("accent on surface", p["accent"], p["surface"]),
        ("accent-bright on surface", p["accent-bright"], p["surface"]),
    ]
    worst_body = None
    for label, fg, bg in checks:
        c = contrast(fg, bg)
        mark = "PASS" if c >= 4.5 else "FAIL"
        if label.startswith("text"):
            worst_body = c if worst_body is None else min(worst_body, c)
        print(f"   {label.ljust(26)} {c:5.2f}:1  {mark}")

    if worst_body is not None and worst_body < 4.5:
        print("\n   !! Body text fails WCAG AA on this palette.")
        print("      Lighten --text (dark theme) or darken it (light theme) until it passes.")
        print("      Do NOT ship the lesson until every body-text row reads PASS.")


if __name__ == "__main__":
    main()
