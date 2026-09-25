#!/usr/bin/env python3
"""recolour_family.py — move one tense's whole colour family along a
defined OKLCh path, on every Sherpa page that carries it and on the route
map, then measure every contrast floor the pages rely on.

soften_family.py can only do one move (lighter and greyer, hue held). The
2026-09-26 request needed two others:

    Innes: "make the present perfect continuous colour a bit more towards
    baby blue-ish turquoise and make the oranges more tasteful"

  TURN   camp 8   hue +20°, lightness +0.06, chroma x0.85   #46B0AB -> #6DBECD
  MUTE   camps 7, 9   chroma x0.72, lightness held           #F0723F -> #DB815F
                                                              #F0A500 -> #E1AB5A

Three candidate sets were rendered side by side on the camp rows (hue turn
20/24/30; oranges muted, pastel via soften(), muted and deeper). Pastel
oranges went candy-bright (#FF8E63) and the deeper ones drifted towards
past simple's brown; the set above kept every row distinct.

Not measured here: text drawn on the accent inside a page's SVG diagrams.
Camp 8's "THE EVIDENCE" tag was white on the fill (2.6:1 before the turn,
2.1:1 after) and now uses the page's --on-accent ink, #12282C (7.3:1).
Check the diagrams by eye after any move.

The family on each page is found by hue, as in soften_family.py: every hex
within HUE_TOL of the page's accent and above a chroma floor moves with it,
and the page's --ink, --ink-soft, --paper, --card, --good and --bad are
never touched. The route map gets exact replacements only, because it also
carries every other tense's colour.

After the move, each stop is checked against the floor its role needs, and
a small-text stop that fails is walked back in lightness (never picked):
--accent on --paper 3.0 (large text and UI), --accent-dark on --paper 4.5,
--on-accent on --accent 4.5. The route map's row inks are re-chosen as the
better of white and #1A1206, and tools/check_route_map.py re-measures them.

    python3 lesson-template/recolour_family.py --dry-run
    python3 lesson-template/recolour_family.py

Scope: the Sherpa family only. Block Camp and the lessons that load
lesson-template/tense-palette.css keep the old values; they are a separate
family with their own colour gates. The stopped Sherpa deck builder's
content/*.json palettes are not touched either.
"""
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from soften import to_lch, from_lch, contrast        # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = '--dry-run' in sys.argv
CHROMA_FLOOR = 0.020
SKIP_DECL = re.compile(r'--(ink|ink-soft|paper|card|good|bad)[a-z-]*\s*:\s*$')
DARK_INK = '#1A1206'


def turn(dh, dl=0.0, kc=1.0):
    def f(h):
        L, C, H = to_lch(h)
        return from_lch(L + dl, C * kc, H + math.radians(dh))
    return f


def mute(kc, dl=0.0):
    def f(h):
        L, C, H = to_lch(h)
        return from_lch(L + dl, C * kc, H)
    return f


# name, the route map's canonical hex, the move, hue tolerance, the pages
FAMILIES = [
    ('8 present perfect continuous', '#46B0AB', turn(20, .06, .85), 14, [
        'sherpa-tensing-camp-eight-present-perfect-continuous.html']),
    ('7 future simple', '#F0723F', mute(.72), 12, [
        'sherpa-tensing-camp-seven-future-simple.html',
        'sherpa-tensing-descent-seven-future-simple-passive.html']),
    # 10 degrees, not 14: past simple's brown sits 14 degrees away
    ('9 future continuous', '#F0A500', mute(.72), 10, [
        'sherpa-tensing-camp-nine-future-continuous.html']),
]
MAP = 'sherpa-tensing-route-map.html'


def in_family(h, hue, tol):
    L, C, H = to_lch(h)
    if C < CHROMA_FLOOR:
        return False
    return abs((H - hue + math.pi) % (2 * math.pi) - math.pi) <= math.radians(tol)


def collect(src, accent, move, tol):
    hue = to_lch(accent)[2]
    out = {}
    for m in re.finditer(r'#([0-9A-Fa-f]{6})\b', src):
        h = '#' + m.group(1).upper()
        if h in out or not in_family(h, hue, tol):
            continue
        if SKIP_DECL.search(src[max(0, m.start() - 24):m.start()]):
            continue
        out[h] = move(h)
    return out


def rewrite(src, mapping):
    def sub(m):
        h = '#' + m.group(1).upper()
        if h not in mapping or SKIP_DECL.search(src[max(0, m.start() - 24):m.start()]):
            return m.group(0)
        return mapping[h]
    return re.sub(r'#([0-9A-Fa-f]{6})\b', sub, src)


def tokens(src):
    return {k: v.upper() for k, v in re.findall(r'(--[a-z-]+)\s*:\s*(#[0-9A-Fa-f]{6})', src)}


def walk(h, against, floor, darker):
    """Move h's lightness in small steps until it clears floor against `against`."""
    L, C, H = to_lch(h)
    step = -0.004 if darker else 0.004
    for _ in range(200):
        if contrast(h, against) >= floor:
            return h
        L += step
        h = from_lch(L, C, H)
    return h


def floors(src, name):
    """Measure the stops; walk back any that fail. Returns (src, report lines, failures)."""
    t = tokens(src)
    lines, bad = [], 0
    paper, acc = t.get('--paper'), t.get('--accent')
    if not paper or not acc:
        return src, ['      (no --paper/--accent tokens)'], 0
    dark_page = to_lch(paper)[0] < 0.5
    checks = [('--accent', paper, 3.0), ('--accent-dark', paper, 4.5)]
    for tok, against, floor in checks:
        v = t.get(tok)
        if not v:
            continue
        r = contrast(v, against)
        if r < floor:
            nv = walk(v, against, floor, darker=not dark_page)
            src = src.replace('%s:%s' % (tok, v), '%s:%s' % (tok, nv)).replace(
                '%s: %s' % (tok, v), '%s: %s' % (tok, nv))
            lines.append('      %-14s %s %.2f < %.1f -> walked to %s (%.2f)' % (tok, v, r, floor, nv, contrast(nv, against)))
            if contrast(nv, against) < floor:
                bad += 1
        else:
            lines.append('      %-14s %s %.2f >= %.1f' % (tok, v, r, floor))
    t = tokens(src)
    oa = t.get('--on-accent')
    if oa:
        r = contrast(oa, t['--accent'])
        ok = r >= 4.5
        bad += not ok
        lines.append('      --on-accent    %s on %s %.2f %s' % (oa, t['--accent'], r, '>= 4.5' if ok else 'FAIL'))
    return src, lines, bad


def main():
    print('\n  recolour the Sherpa family%s\n' % ('   [dry run]' if DRY else ''))
    fails = 0
    canon = {}
    for name, accent, move, tol, files in FAMILIES:
        canon[accent] = move(accent)
        print('  %s   %s -> %s' % (name, accent, canon[accent]))
        for f in files:
            path = os.path.join(ROOT, f)
            src = open(path, encoding='utf-8').read()
            mapping = collect(src, accent, move, tol)
            for old, new in sorted(mapping.items()):
                print('      %-50s %s -> %s' % (os.path.basename(f), old, new))
            new_src = rewrite(src, mapping)
            new_src, lines, bad = floors(new_src, f)
            fails += bad
            print('\n'.join(lines))
            if not DRY and new_src != src:
                open(path, 'w', encoding='utf-8', newline='\n').write(new_src)
        print('')
    # the route map: exact values only, and each row's ink re-chosen
    path = os.path.join(ROOT, MAP)
    src = open(path, encoding='utf-8').read()
    new = rewrite(src, canon)
    for old, c in canon.items():
        ink = '#FFFFFF' if contrast(c, '#FFFFFF') >= contrast(c, DARK_INK) else DARK_INK
        new = re.sub(r'(style="background:%s;color:)(#[0-9A-Fa-f]{6})' % re.escape(c),
                     lambda m: m.group(1) + ink, new)
        print('  %s row: %s on %s %.2f' % (MAP, ink, c, contrast(c, ink)))
        fails += contrast(c, ink) < 4.5
    n = sum(src.upper().count(o.upper()) for o in canon)
    print('  %s: %d replacement(s)' % (MAP, n))
    if not DRY and new != src:
        open(path, 'w', encoding='utf-8', newline='\n').write(new)
    if fails:
        sys.exit('\n  ! %d floor(s) still fail' % fails)
    print('\n  every floor passes')


if __name__ == '__main__':
    main()
