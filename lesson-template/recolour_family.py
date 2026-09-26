#!/usr/bin/env python3
"""recolour_family.py — move a tense's whole colour family along a defined
OKLCh path, on every Sherpa page that carries it and on the route map, then
measure every contrast floor the pages rely on.

    python3 lesson-template/recolour_family.py <pass> --dry-run
    python3 lesson-template/recolour_family.py <pass>

soften_family.py can only do one move (lighter and greyer, hue held). Each
request since has been its own pass, kept here as a record; a pass refuses
to run once its starting colours are gone from the route map.

  2026-09-26a  Innes: "make the present perfect continuous colour a bit more
               towards baby blue-ish turquoise and make the oranges more
               tasteful"
      camp 8     hue +20°, L +0.06, C x0.85       #46B0AB -> #6DBECD
      camps 7, 9 C x0.72, L held                  #F0723F -> #DB815F
                                                  #F0A500 -> #E1AB5A
  2026-09-26b  Innes: "Make present continuous a baby pink, number 5 also
               softer green and 8 even more baby blue turquoise"
      camp 1     hue -4°, L +0.15, C x0.50        #E66085 -> #F2ADBF
      camp 5     L +0.09, C x0.62                 #70A43A -> #99BA7D
      camp 8     hue +12°, L +0.07, C x0.80       #6DBECD -> #97D0E5

Each pass was chosen from three candidate sets rendered side by side on all
thirteen rows (pastel oranges went candy-bright; deeper ones drifted towards
past simple's brown; the milder pinks stayed a saturated rose).

HOW A FAMILY MOVES. On each page the family is found by hue: every hex
within the tolerance of the page's accent and above a chroma floor moves,
and --ink, --ink-soft, --paper, --card, --good and --bad never do. The hue
turn and the chroma cut apply to every member; the lightness step applies
only to the light half of the ramp (L > 0.5), scaled by how far each colour
is from white, so the dark surfaces of a descent page and the dark
on-accent inks stay dark and the palest tints do not burn out. Then each token is held
to the floor its role needs, walking lightness back where it fails (never a
picked colour): --accent on --paper 3.0 (large text and UI), --accent-dark
on --paper 4.5, --on-accent on --accent 4.5.

THE ROUTE MAP carries every tense's colour and uses camp one's pink as its
own accent too, so only the colour-key uses change there: a row's
background (its ink re-chosen as the better of white and #1A1206), a dot's
or segment's data-color, and a list row's or chip's --c. The hub keeps its
pink. tools/check_route_map.py re-measures rows, twins and contrast.

NOT MEASURED HERE: text drawn on the family's fills inside a page's SVG
diagrams. Camp 8's "THE EVIDENCE" tag (pass a) and camp 1's ripple labels
(pass b) went white-on-light and were moved to the page's dark ink by hand.
Render the pages and look after any pass; then re-render the library cards
that are snapshots of those diagrams (docs/HANDOFF.md, 2026-09-26).

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
MAP = 'sherpa-tensing-route-map.html'


def move(dh=0.0, dl=0.0, kc=1.0, lift='ramp'):
    """Turn hue by dh degrees, cut chroma by kc, and lift lightness by dl.

    lift='ramp' (pass b on): only the light half of the ramp lifts, and in
    proportion to its distance from white, so the accent gets the full dl
    and a pale tint almost none instead of burning out to #FFFFFF.
    lift='flat' is what pass a did (every member +dl), kept as its record."""
    def f(h, acc_L):
        L, C, H = to_lch(h)
        if lift == 'flat':
            up = dl
        else:
            up = dl * (1 - L) / max(1e-6, 1 - acc_L) if L > 0.5 else 0.0
        return from_lch(L + up, C * kc, H + math.radians(dh))
    return f


# pass -> [(name, the route map's canonical hex, the move, hue tolerance, pages)]
PASSES = {
    '2026-09-26a': [
        ('8 present perfect continuous', '#46B0AB', move(20, .06, .85, 'flat'), 14, [
            'sherpa-tensing-camp-eight-present-perfect-continuous.html']),
        ('7 future simple', '#F0723F', move(0, 0, .72, 'flat'), 12, [
            'sherpa-tensing-camp-seven-future-simple.html',
            'sherpa-tensing-descent-seven-future-simple-passive.html']),
        # 10 degrees, not 14: past simple's brown sits 14 degrees away
        ('9 future continuous', '#F0A500', move(0, 0, .72, 'flat'), 10, [
            'sherpa-tensing-camp-nine-future-continuous.html']),
    ],
    '2026-09-26b': [
        ('1 present continuous', '#E66085', move(-4, .15, .50), 16, [
            'sherpa-tensing-camp-one-present-continuous.html',
            'sherpa-tensing-descent-one-present-continuous-passive.html']),
        ('5 going to', '#70A43A', move(0, .09, .62), 14, [
            'sherpa-tensing-camp-five-going-to.html',
            'sherpa-tensing-descent-nine-going-to-passive.html']),
        ('8 present perfect continuous', '#6DBECD', move(12, .07, .80), 14, [
            'sherpa-tensing-camp-eight-present-perfect-continuous.html']),
    ],
}


def in_family(h, hue, tol):
    L, C, H = to_lch(h)
    if C < CHROMA_FLOOR:
        return False
    return abs((H - hue + math.pi) % (2 * math.pi) - math.pi) <= math.radians(tol)


def collect(src, accent, fn, tol):
    acc_L, _, hue = to_lch(accent)
    out = {}
    for m in re.finditer(r'#([0-9A-Fa-f]{6})\b', src):
        h = '#' + m.group(1).upper()
        if h in out or not in_family(h, hue, tol):
            continue
        if SKIP_DECL.search(src[max(0, m.start() - 24):m.start()]):
            continue
        out[h] = fn(h, acc_L)
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
    for _ in range(250):
        if contrast(h, against) >= floor:
            return h
        L += step
        h = from_lch(L, C, H)
    return h


def floors(src):
    """Measure the stops; walk back any that fail. Returns (src, report lines, failures)."""
    t = tokens(src)
    lines, bad = [], 0
    paper, acc = t.get('--paper'), t.get('--accent')
    if not paper or not acc:
        return src, ['      (no --paper/--accent tokens)'], 0
    dark_page = to_lch(paper)[0] < 0.5
    for tok, floor in (('--accent', 3.0), ('--accent-dark', 4.5)):
        v = t.get(tok)
        if not v:
            continue
        r = contrast(v, paper)
        if r < floor:
            nv = walk(v, paper, floor, darker=not dark_page)
            src = re.sub(r'(%s\s*:\s*)%s' % (re.escape(tok), re.escape(v)), lambda m: m.group(1) + nv,
                         src, flags=re.I)
            lines.append('      %-14s %s %.2f < %.1f -> walked to %s (%.2f)' % (tok, v, r, floor, nv, contrast(nv, paper)))
            bad += contrast(nv, paper) < floor
        else:
            lines.append('      %-14s %s %.2f >= %.1f' % (tok, v, r, floor))
    t = tokens(src)
    oa = t.get('--on-accent')
    if oa:
        r = contrast(oa, t['--accent'])
        bad += r < 4.5
        lines.append('      --on-accent    %s on %s %.2f %s' % (oa, t['--accent'], r, '>= 4.5' if r >= 4.5 else 'FAIL'))
    return src, lines, bad


def recolour_map(src, canon):
    """Only the colour-key uses: row backgrounds (ink re-chosen), data-color, --c."""
    lines, bad = [], 0
    for old, new in canon.items():
        ink = '#FFFFFF' if contrast(new, '#FFFFFF') >= contrast(new, DARK_INK) else DARK_INK
        n0 = 0
        src, k = re.subn(r'(style="background:)%s(;color:)#[0-9A-Fa-f]{6}' % re.escape(old),
                         lambda m: m.group(1) + new + m.group(2) + ink, src, flags=re.I)
        n0 += k
        src, k = re.subn(r'(data-color=")%s(")' % re.escape(old), lambda m: m.group(1) + new + m.group(2), src, flags=re.I)
        n0 += k
        src, k = re.subn(r'(--c:)%s' % re.escape(old), lambda m: m.group(1) + new, src, flags=re.I)
        n0 += k
        # a chip carries its ink as --k next to --c; keep it the row's ink
        src = re.sub(r'(--c:%s;--k:)#[0-9A-Fa-f]{6}' % re.escape(new), lambda m: m.group(1) + ink, src, flags=re.I)
        lines.append('  %s  %s -> %s: %d key use(s); row text %s at %.2f' % (MAP, old, new, n0, ink, contrast(new, ink)))
        bad += contrast(new, ink) < 4.5
    return src, lines, bad


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if len(args) != 1 or args[0] not in PASSES:
        sys.exit('usage: recolour_family.py <pass> [--dry-run]; passes: %s' % ', '.join(PASSES))
    fams = PASSES[args[0]]
    map_path = os.path.join(ROOT, MAP)
    map_src = open(map_path, encoding='utf-8').read()
    gone = [a for _, a, _, _, _ in fams if a.upper() not in map_src.upper()]
    if gone:
        sys.exit('! %s: %s no longer on the route map; this pass has been applied'
                 % (args[0], ', '.join(gone)))
    print('\n  pass %s%s\n' % (args[0], '   [dry run]' if DRY else ''))
    fails, canon = 0, {}
    for name, accent, fn, tol, files in fams:
        canon[accent] = fn(accent, to_lch(accent)[0])
        print('  %s   %s -> %s' % (name, accent, canon[accent]))
        for f in files:
            path = os.path.join(ROOT, f)
            src = open(path, encoding='utf-8').read()
            mapping = collect(src, accent, fn, tol)
            for old, new in sorted(mapping.items()):
                print('      %-50s %s -> %s' % (os.path.basename(f), old, new))
            new_src, lines, bad = floors(rewrite(src, mapping))
            fails += bad
            print('\n'.join(lines))
            if not DRY and new_src != src:
                open(path, 'w', encoding='utf-8', newline='\n').write(new_src)
        print('')
    new_map, lines, bad = recolour_map(map_src, canon)
    fails += bad
    print('\n'.join(lines))
    if not DRY and new_map != map_src:
        open(map_path, 'w', encoding='utf-8', newline='\n').write(new_map)
    if fails:
        sys.exit('\n  ! %d floor(s) still fail' % fails)
    print('\n  every floor passes')


if __name__ == '__main__':
    main()
