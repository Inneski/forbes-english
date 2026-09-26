#!/usr/bin/env python3
"""recolour_family.py — move a tense's whole colour family along a defined
OKLCh path, on every Sherpa page that carries it and on the route map, then
measure every contrast floor the pages rely on.

    python3 lesson-template/recolour_family.py <pass> --dry-run
    python3 lesson-template/recolour_family.py <pass>
    python3 lesson-template/recolour_family.py --replay <git-rev> <pass> [<pass>...]

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
# A hex colour, but not the digits of an HTML character reference such as
# &#128274; (the padlock) — the first run rewrote camp 8's into &#519EA3;.
HEX = r'(?<!&)#([0-9A-Fa-f]{6})\b'
SHARED_ON = 4        # a colour on this many Sherpa pages is shared diagram furniture


def move(dh=0.0, dl=0.0, kc=1.0):
    """Turn hue by dh degrees, cut chroma by kc, and lift lightness by dl.

    Only the light half of the ramp lifts, and in proportion to its distance
    from white, so the accent gets the full dl and a pale tint almost none
    instead of burning out to #FFFFFF. (Pass a first ran with a flat lift,
    which washed camp 8's time band to #E2FFFF; the review caught it and the
    pages were replayed from ff8173e with this one — see --replay.)"""
    def f(h, acc_L):
        L, C, H = to_lch(h)
        up = dl * (1 - L) / max(1e-6, 1 - acc_L) if L > 0.5 else 0.0
        return from_lch(L + up, C * kc, H + math.radians(dh))
    return f


# pass -> [(name, the route map's canonical hex, the move, hue tolerance, pages)]
PASSES = {
    '2026-09-26a': [
        ('8 present perfect continuous', '#46B0AB', move(20, .06, .85), 14, [
            'sherpa-tensing-camp-eight-present-perfect-continuous.html']),
        ('7 future simple', '#F0723F', move(0, 0, .72), 12, [
            'sherpa-tensing-camp-seven-future-simple.html',
            'sherpa-tensing-descent-seven-future-simple-passive.html']),
        # 10 degrees, not 14: past simple's brown sits 14 degrees away
        ('9 future continuous', '#F0A500', move(0, 0, .72), 10, [
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


def shared_colours(pages):
    """Colours used on SHARED_ON or more Sherpa pages: the NOW bar, its halo,
    the PAST/FUTURE captions. They belong to no tense and never move, even
    when their hue happens to sit inside a family's (the first run turned
    camp 7's NOW halo and camp 9's captions)."""
    count = {}
    for src in pages:
        for h in {'#' + x.upper() for x in re.findall(HEX, src)}:
            count[h] = count.get(h, 0) + 1
    return {h for h, n in count.items() if n >= SHARED_ON}


def collect(src, accent, fn, tol, shared=frozenset()):
    acc_L, _, hue = to_lch(accent)
    out = {}
    for m in re.finditer(HEX, src):
        h = '#' + m.group(1).upper()
        if h in out or h in shared or not in_family(h, hue, tol):
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
    return re.sub(HEX, sub, src)


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
    # the eyebrow chip and panel headings: --accent-dark on --accent-lighter
    t = tokens(src)
    ad, al = t.get('--accent-dark'), t.get('--accent-lighter')
    if ad and al and contrast(ad, al) < 4.5:
        nv = walk(ad, al, 4.5, darker=not dark_page)
        src = re.sub(r'(--accent-dark\s*:\s*)%s' % re.escape(ad), lambda m: m.group(1) + nv, src, flags=re.I)
        lines.append('      --accent-dark  %s on --accent-lighter %.2f < 4.5 -> walked to %s (%.2f)'
                     % (ad, contrast(ad, al), nv, contrast(nv, al)))
        bad += contrast(nv, al) < 4.5
    t = tokens(src)
    oa = t.get('--on-accent')
    if oa:
        r = contrast(oa, t['--accent'])
        bad += r < 4.5
        lines.append('      --on-accent    %s on %s %.2f %s' % (oa, t['--accent'], r, '>= 4.5' if r >= 4.5 else 'FAIL'))
    else:
        w = contrast('#FFFFFF', t['--accent'])
        ink = t.get('--ink', DARK_INK)
        lines.append('      no --on-accent: white on --accent %.2f, --ink on it %.2f%s'
                     % (w, contrast(ink, t['--accent']), '  (check buttons by eye)' if w < 4.5 else ''))
    return src, lines, bad


def keep_text(src, mapping, paper):
    """An SVG label in the family keeps at least the contrast it had (capped
    at 4.5): a caption meant to be faint stays faint, but no fainter."""
    lines = []
    for old, new in mapping.items():
        if not re.search(r'<text[^>]*fill="%s"' % re.escape(new), src, re.I):
            continue
        want = min(contrast(old, paper), 4.5)
        if contrast(new, paper) + 0.005 >= want:
            continue
        L, C, H = to_lch(new)
        dark = to_lch(paper)[0] > 0.5
        nv = new
        for _ in range(250):
            if contrast(nv, paper) >= want:
                break
            L += -0.004 if dark else 0.004
            nv = from_lch(L, C, H)
        src = re.sub(r'(<text[^>]*fill=")%s(")' % re.escape(new), lambda m: m.group(1) + nv + m.group(2), src, flags=re.I)
        lines.append('      label %s -> %s: %.2f, as it had %.2f' % (new, nv, contrast(nv, paper), contrast(old, paper)))
    return src, lines


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


def replay(rev, names):
    """Re-apply passes, in order, to each page's content at git revision rev.
    The route map is not touched: its key uses are already right, and it is
    the check that a pass has been applied."""
    import subprocess
    def at(path):
        return subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (rev, path)], capture_output=True,
                              text=True, encoding='utf-8', check=True).stdout
    listing = subprocess.run(['git', '-C', ROOT, 'ls-tree', '--name-only', rev], capture_output=True,
                             text=True, encoding='utf-8', check=True).stdout.split()
    sherpa = [p for p in listing if p.startswith('sherpa-tensing-') and p.endswith('.html') and p != MAP]
    shared = shared_colours(at(p) for p in sherpa)
    pages = []
    for n in names:
        for fam in PASSES[n]:
            pages += [f for f in fam[4] if f not in pages]
    fails = 0
    print('\n  replay %s from %s%s   (%d shared colours held)\n'
          % (' + '.join(names), rev, '   [dry run]' if DRY else '', len(shared)))
    for f in pages:
        src = at(f)
        paper = tokens(src).get('--paper', '#FFFFFF')
        print('  ' + f)
        for n in names:
            for name, accent, fn, tol, files in PASSES[n]:
                if f not in files:
                    continue
                mapping = collect(src, accent, fn, tol, shared)
                src = rewrite(src, mapping)
                src, lines, bad = floors(src)
                src, tl = keep_text(src, mapping, paper)
                fails += bad
                print('    %s %s: %d colours moved' % (n, name, len(mapping)))
                print('\n'.join(lines + tl))
        if not DRY:
            open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='\n').write(src)
    if fails:
        sys.exit('\n  ! %d floor(s) still fail' % fails)
    print('\n  every floor passes')


def main():
    if '--replay' in sys.argv:
        i = sys.argv.index('--replay')
        rest = [a for a in sys.argv[i + 1:] if not a.startswith('--')]
        return replay(rest[0], rest[1:])
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
