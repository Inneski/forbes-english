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


def contrast_ratio(a, b):
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
        if contrast_ratio(text, surface) < 8:
            text = (244, 240, 233)
        text_dim = shift(text, dl=-0.26, ds=+0.02)
        accent_bright = shift(accent, dl=+0.14, ds=+0.06)
        accent_dim = shift(accent, dl=-0.18, ds=-0.05)
    else:
        # ── LIGHT THEME ──────────────────────────────────────────────
        # Paper, not pure white: keep a whisper of the image's own hue so a
        # bright lesson still belongs to its picture. Cards then sit ABOVE
        # the paper in pure white, which is what gives a light deck depth.
        lh, _, ls_ = to_hls(lightest)
        void = from_hls(lh, 0.965, min(0.30, max(0.05, ls_ * 0.55)))
        surface = (255, 255, 255)
        surface2 = shift(void, dl=-0.035, ds=+0.01)

        # Ink carries a trace of the accent hue, like the dark theme's text.
        text = from_hls(ah, 0.135, 0.42)
        if contrast_ratio(text, surface) < 9:
            text = (22, 27, 34)
        text_dim = shift(text, dl=+0.30, ds=-0.10)

        # On white, an accent taken straight from a pastel image will not
        # carry text or a button. Deepen it — keeping its hue — until it does.
        accent = accent
        guard = 0
        while contrast_ratio(accent, surface) < 4.5 and guard < 24:
            hx, lx, sx = to_hls(accent)
            accent = from_hls(hx, lx - 0.035, min(1.0, sx + 0.03))
            guard += 1

        # "Bright" in a light theme means MORE emphatic, i.e. deeper still.
        accent_bright = shift(accent, dl=-0.10, ds=+0.10)
        guard = 0
        while contrast_ratio(accent_bright, surface) < 5.5 and guard < 14:
            hx, lx, sx = to_hls(accent_bright)
            accent_bright = from_hls(hx, lx - 0.035, sx)
            guard += 1

        accent_dim = shift(accent, dl=+0.34, ds=-0.18)   # pale fills
        # A hairline that is actually visible on paper.
        border = from_hls(to_hls(accent)[0], 0.68, 0.30)

    # --accent-bright must stay visibly distinct from --text, or <em>
    # emphasis and eyebrows vanish into the body copy. When the image's
    # dominant colour is already near-white, brightening is the wrong move:
    # deepen and saturate instead.
    guard = 0
    step_b = -0.05 if dark else +0.05
    while contrast_ratio(accent_bright, text) < 1.45 and guard < 12:
        hb, lb, sb = to_hls(accent_bright)
        accent_bright = from_hls(hb, lb + step_b, min(1.0, sb + 0.08))
        guard += 1

    # ── Contrast colour ───────────────────────────────────────────────
    # A deliberate counterpoint to the accent, for the Forbes mark, a
    # highlight, or anything that should read as "not part of the wash".
    # Rotated ~150 degrees so it reads as a different colour family rather
    # than a shade, then pushed until it is legible on --surface.
    ch = (ah + 0.42) % 1.0
    contrast = from_hls(ch, 0.52 if dark else 0.38, max(0.55, min(0.85, asat + 0.25)))
    step = 0.05 if dark else -0.05
    guard = 0
    while contrast_ratio(contrast, surface) < 5.0 and guard < 9:
        h_, l_, s_ = to_hls(contrast)
        contrast = from_hls(h_, l_ + step, s_)
        guard += 1

    return {
        "void": void, "surface": surface, "surface2": surface2,
        "border": border, "text": text, "text-dim": text_dim,
        "accent": accent, "accent-bright": accent_bright,
        "accent-dim": accent_dim, "secondary": secondary,
        "contrast": contrast,
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
             "accent", "accent-bright", "accent-dim", "secondary", "contrast"]
    width = max(len(k) for k in order)
    for key in order:
        print(f"  --{key.ljust(width)} : {hex_of(p[key])};")
    print("}")

    print("\n/* Contrast report */")
    # (label, fg, bg, minimum, why)
    checks = [
        ("text on surface",          p["text"],          p["surface"], 4.5, "body copy"),
        ("text on void",             p["text"],          p["void"],    4.5, "body copy"),
        ("text-dim on surface",      p["text-dim"],      p["surface"], 4.5, "secondary copy"),
        ("accent on surface",        p["accent"],        p["surface"], 4.5, "buttons, rules"),
        ("accent-bright on surface", p["accent-bright"], p["surface"], 4.5, "headings"),
        ("contrast on surface",      p["contrast"],      p["surface"], 4.5, "counterpoint"),
        ("border on surface",        p["border"],        p["surface"], 1.25, "hairlines must show"),
        # Not a readability check: emphasis must be VISIBLY different from body
        # text, or <em> and eyebrows disappear into the paragraph.
        ("accent-bright vs text",    p["accent-bright"], p["text"],    1.45, "emphasis must show"),
    ]
    failed = []
    for label, fg, bg, minimum, why in checks:
        c = contrast_ratio(fg, bg)
        mark = "PASS" if c >= minimum else "FAIL"
        if c < minimum:
            failed.append(label)
        print(f"   {label.ljust(26)} {c:5.2f}:1  (min {minimum})  {mark}   {why}")

    if failed:
        print("\n   !! Failing: " + ", ".join(failed))
        print("      Do NOT ship the lesson until every row reads PASS.")


if __name__ == "__main__":
    main()
