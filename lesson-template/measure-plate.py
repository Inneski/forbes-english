#!/usr/bin/env python3
"""How transparent can a text plate get before the text stops being readable?

The plates exist because of a measurement, not a preference: 52 of 60
on-canvas text blocks on the Ukraine deck sat below WCAG AA before the rule
in `lesson-template.html` §"Text that sits on the canvas" was added. So
lowering the plate opacity — which is a thing Innes asks for, because the
artwork is the point of the deck — has to be answered with the same
instrument rather than by eye.

WHAT IT COMPOSITES, in the order the browser does:

    void                                    the deck's --void
    + hero pixel      at --bg-opacity       .bg-layer::before
    + wash            at --wash-mid         .bg-layer::after
    = backdrop
    + plate (--surface at ALPHA)            the rule under test
    = ground behind the glyphs
    contrast(ground, --text)                must clear 4.5:1

It samples the real background images, not an average: a plate fails where
the picture is BRIGHTEST, so the figure that matters is the worst tile in the
frame, not the mean. Tiles are 64px, and the reported number is the worst
tile of the worst image.

Usage:
    python3 lesson-template/measure-plate.py <folder> [<folder>...]
    python3 lesson-template/measure-plate.py ielts-pronunciation --alpha 0.94,0.86,0.78
"""
import argparse
import os
import sys

from PIL import Image

BG_OPACITY = 0.74          # --bg-opacity, dark theme
WASH = 0.04                # --wash-mid, dark theme: --void at 4%
TILE = 64
AA = 4.5


def srgb(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def lum(rgb):
    r, g, b = (srgb(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = lum(a), lum(b)
    if la < lb:
        la, lb = lb, la
    return (la + 0.05) / (lb + 0.05)


def over(top, bottom, alpha):
    return tuple(t * alpha + b * (1 - alpha) for t, b in zip(top, bottom))


def hexrgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def palette_of(folder):
    """Read --void, --surface and --text out of the builder that owns it."""
    build = os.path.join('lesson-template', 'build')
    for name in os.listdir(build):
        if not name.startswith('build_') or not name.endswith('.py'):
            continue
        src = open(os.path.join(build, name), encoding='utf-8').read()
        if "F = '%s'" % folder not in src:
            continue
        got = {}
        for key in ('--void', '--surface', '--text'):
            for line in src.splitlines():
                if line.strip().startswith(key) and ':' in line:
                    val = line.split(':')[1].strip().strip("';,")
                    if val.startswith('#') and key not in got:
                        got[key] = hexrgb(val)
                    break
        if len(got) == 3:
            return got, name
    return None, None


def worst_tile(path, void):
    """The brightest TILE-sized patch of the composited backdrop."""
    im = Image.open(path).convert('RGB')
    im.thumbnail((1280, 720))
    w, h = im.size
    worst = None
    for y in range(0, h - TILE + 1, TILE):
        for x in range(0, w - TILE + 1, TILE):
            tile = im.crop((x, y, x + TILE, y + TILE))
            n = TILE * TILE
            px = tile.getdata()
            mean = tuple(sum(p[i] for p in px) / n for i in range(3))
            back = over(mean, void, BG_OPACITY)
            back = over(void, back, WASH)
            if worst is None or lum(back) > lum(worst):
                worst = back
    return worst


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('folders', nargs='+')
    ap.add_argument('--alpha', default='0.94,0.90,0.86,0.82,0.78,0.74,0.70')
    args = ap.parse_args()
    alphas = [float(a) for a in args.alpha.split(',')]

    bad = 0
    for folder in args.folders:
        pal, builder = palette_of(folder)
        if not pal:
            print('  %s — no builder declares this folder' % folder)
            bad = 1
            continue
        void, surface, text = pal['--void'], pal['--surface'], pal['--text']
        print('\n  %s  (%s)' % (folder, builder))
        print('    void %s  surface %s  text %s'
              % (tuple(map(int, void)), tuple(map(int, surface)),
                 tuple(map(int, text))))

        imgs = sorted(f for f in os.listdir(folder)
                      if f.lower().endswith(('.jpg', '.jpeg', '.png')))
        backs = {f: worst_tile(os.path.join(folder, f), void) for f in imgs}

        print('    %-10s %s' % ('alpha', '  '.join('%-6s' % f.split('.')[0]
                                                   for f in imgs)))
        for a in alphas:
            row, low = [], False
            for f in imgs:
                ground = over(surface, backs[f], a)
                c = contrast(ground, text)
                row.append('%-6.2f' % c)
                if c < AA:
                    low = True
            print('    %-10.2f %s   %s' % (a, '  '.join(row),
                                           'FAIL' if low else 'pass'))
            if low and a == alphas[0]:
                bad = 1

    print('\n  AA is %.1f:1. The lowest alpha whose row still says pass is the '
          'floor.' % AA)
    return bad


if __name__ == '__main__':
    sys.exit(main())
