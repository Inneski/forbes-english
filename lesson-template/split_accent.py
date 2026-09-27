#!/usr/bin/env python3
"""Give a Sherpa page with a pale key colour its real colour back.

    py lesson-template/split_accent.py <page.html> <key-hex> [--dry-run]

Innes, 2026-09-26, on camp six: "this should be yellow to distinguish it
from past simple". The route map calls camp six a soft yellow (#F1D779), but
the page wore a mustard (#A8860B): the recolour tools walk --accent down
until TEXT in it clears 3:1 on the paper, and a yellow dark enough for text
is mustard, which beside past simple's tan reads as the same brown.

Almost every use of --accent is a FILL (section markers, the trail line,
buttons, the translation chip, the progress bar, borders); only a few are
text (the "Tensing" in the wordmark, the results score). So:

- a light page gets a split: --accent becomes the fill, derived from the key
  in OKLCh (hue kept, L -0.02, chroma x1.25, so it holds its own on the cream
  paper), with the page ink on it (--on-accent); the old 3:1 shade becomes
  --accent-text, and every `color:var(--accent)` points at it;
- a dark page needs no split (a yellow is legible on it): --accent is the fill;
- --accent-light and --accent-lighter are re-derived at the key hue with
  enough chroma to read as a tint of it, not as beige;
- in the diagrams, every fill, stroke or gradient stop in the accent's hue
  family darker than L 0.74 is lifted to it, at the key hue (a deep yellow,
  not a gold-brown); on a dark page only the mid-tones, since its dark
  family colours are grounds. Text colours are left alone: they need the dark.

recolour_family.floors() knows the split: on a page with --accent-text, the
3:1 floor is measured on it, and --accent is held only as a fill.
"""
import io
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from soften import to_lch, from_lch, contrast        # noqa: E402

HEX = r'(?<!&)#([0-9A-Fa-f]{6})\b'
FAMILY_DH = 10          # degrees either side of the key hue
FAMILY_MIN_C = 0.08     # below this a colour is a grey or an ink, not the family
DEEP_L = 0.74           # the darkest a diagram fill may be and still read as the key colour


def tokens(src):
    return {k: v.upper() for k, v in re.findall(r'(--[a-z-]+)\s*:\s*(#[0-9A-Fa-f]{6})', src)}


def set_token(src, tok, val):
    new, n = re.subn(r'(%s\s*:\s*)#[0-9A-Fa-f]{6}' % re.escape(tok), lambda m: m.group(1) + val, src, count=1)
    return new, n


def in_family(h, key_H):
    L, C, H = to_lch(h)
    d = abs((math.degrees(H) - math.degrees(key_H) + 180) % 360 - 180)
    return C >= FAMILY_MIN_C and d <= FAMILY_DH


def split(src, key):
    t = tokens(src)
    kL, kC, kH = to_lch(key)
    fill = from_lch(kL - 0.02, kC * 1.25, kH)
    paper, ink = t['--paper'], t['--ink']
    dark = to_lch(paper)[0] < 0.5
    log = []
    old = t['--accent']
    if not dark:
        if '--accent-text' not in t:
            src = src.replace('--accent:%s;' % old, '--accent:%s; --accent-text:%s;' % (old, old), 1) \
                if '--accent:%s;' % old in src else re.sub(
                    r'(--accent\s*:\s*%s\s*;)' % re.escape(old), r'\1 --accent-text:%s;' % old, src, count=1, flags=re.I)
            n = len(re.findall(r'(?<![-a-z])color\s*:\s*var\(--accent\)', src))
            src = re.sub(r'((?<![-a-z])color\s*:\s*)var\(--accent\)', r'\1var(--accent-text)', src)
            log.append('--accent-text %s (%.2f on the paper); %d text use(s) of --accent moved to it'
                       % (old, contrast(old, paper), n))
    src, _ = set_token(src, '--accent', fill)
    oa = t.get('--on-accent')
    best = max([ink, paper, '#FFFFFF'], key=lambda c: contrast(c, fill))
    if oa:
        src, _ = set_token(src, '--on-accent', best)
    log.append('--accent %s -> %s (fill; %.2f on the paper), --on-accent %s at %.2f'
               % (old, fill, contrast(fill, paper), best, contrast(best, fill)))
    if not dark:
        for tok, (L, C) in (('--accent-light', (0.925, kC * 0.85)), ('--accent-lighter', (0.972, kC * 0.42))):
            if tok in t:
                v = from_lch(L, C, kH)
                src, _ = set_token(src, tok, v)
                log.append('%s %s -> %s' % (tok, t[tok], v))
        ad, al = tokens(src).get('--accent-dark'), tokens(src).get('--accent-lighter')
        if ad and al:
            log.append('--accent-dark %s on --accent-lighter %.2f' % (ad, contrast(ad, al)))
    # the diagrams: lift dark family fills, strokes and stops; leave text alone
    moved = {}
    t2 = tokens(src)
    keep = {t2.get(k) for k in ('--accent-text', '--accent-dark', '--ink', '--ink-soft')}

    def lift(h):
        h = h.upper()
        if h in moved:
            return moved[h]
        L, C, H = to_lch(h)
        nv = h
        # on a dark page the dark family colours are grounds, not golds: only mid-tones lift
        if in_family(h, kH) and L < DEEP_L and (not dark or L >= 0.5) and h not in keep:
            nv = from_lch(DEEP_L, max(C, kC * 1.3), kH)
        moved[h] = nv
        return nv

    def attr(m):
        tag = m.group(0)
        if re.match(r'<text\b|<tspan\b', tag):
            return tag
        return re.sub(r'((?:fill|stroke|stop-color)=")#([0-9A-Fa-f]{6})(")', lambda a: a.group(1) + lift('#' + a.group(2)) + a.group(3), tag)
    src = re.sub(r'<(?:circle|rect|path|line|polyline|polygon|ellipse|stop|g)\b[^>]*>', attr, src)
    # colours handed to the diagram script as data (["shape-long", "panel-long", "#C79A00"])
    src = re.sub(r'(\["[a-z-]+",\s*"[a-z-]+",\s*")#([0-9A-Fa-f]{6})("\])', lambda a: a.group(1) + lift('#' + a.group(2)) + a.group(3), src)
    for a, b in sorted(moved.items()):
        if a != b:
            log.append('diagram %s -> %s' % (a, b))
    return src, log


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if len(args) != 2:
        sys.exit(__doc__.split('\n\n')[1])
    page, key = args
    src = io.open(page, encoding='utf-8').read()
    new, log = split(src, key.upper())
    print('\n'.join('  ' + l for l in log))
    if '--dry-run' not in sys.argv and new != src:
        io.open(page, 'w', encoding='utf-8', newline='\n').write(new)


if __name__ == '__main__':
    main()
