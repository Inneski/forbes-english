#!/usr/bin/env python3
"""soften_family.py — nudge one tense's whole colour family by a given
amount, across the page, the route map and the canonical token.

Innes: "make 4, 5, 7, 8 about 10% softer."

"10% softer" is read as t=0.10 on the SAME scale the pink and the navy
used — 10% of the way along soften()'s OKLCh path toward white, chroma
falling faster than lightness rises. That keeps one meaning of "softer"
across every request in this series (pink 29%, navy 49%, these 10%).

Two readings were measured and rejected first, because "10%" is ambiguous
and the wrong reading produces a commit that changes nothing:

  A 10% CHROMA cut is invisible. dE 0.73 to 1.75 for these four — all
  below the ~2.0 just-noticeable threshold. Shipping it would have been a
  no-op the eye cannot find.

  Matching the yellow's approved perceptual step (dE 6.27) destroys them.
  The yellow could lose 35% of its chroma and stay yellow because it
  started at C=0.181. Present perfect starts at C=0.071, so the same
  perceptual distance means an 88% cut — #596060, which is grey, and
  collides with camps 12 and 13.

Rather than hand-list every hex per page, the family is found by HUE:
every colour in the file within HUE_TOL of the page's accent and above a
chroma floor belongs to that accent's ramp, and moves with it. Greys and
inks fall out automatically because their chroma is near zero. The
declaration guard from apply_soften.py still applies on top, so --ink,
--paper, --card, --good and --bad are never touched even if a hue matches.

    python3 lesson-template/soften_family.py --dry-run
    python3 lesson-template/soften_family.py
"""
import os, re, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from soften import soften, to_lch, contrast

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = '--dry-run' in sys.argv

T = 0.10
HUE_TOL = math.radians(14)
CHROMA_FLOOR = 0.020

SKIP_DECL = re.compile(r'--(ink|ink-soft|paper|card|good|bad)[a-z-]*\s*:\s*$')

# tense -> the accent that defines its family, and the files that carry it
FAMILIES = [
    ('4 present perfect', '#1F6A70', [
        'sherpa-tensing-camp-four-present-perfect.html',
        'sherpa-tensing-descent-four-present-perfect-passive.html']),
    ('5 going to', '#639922', [
        'sherpa-tensing-camp-five-going-to.html',
        'sherpa-tensing-descent-nine-going-to-passive.html']),
    ('7 future simple', '#E8632A', [
        'sherpa-tensing-camp-seven-future-simple.html',
        'sherpa-tensing-descent-seven-future-simple-passive.html']),
    ('8 present perfect continuous', '#2FA6A1', [
        'sherpa-tensing-camp-eight-present-perfect-continuous.html']),
]

# the route map and the master list carry all four; handled separately so
# one file is not rewritten four times over
SHARED = ['sherpa-tensing-route-map.html', 'lesson-template/tense-palette.css']

# Present perfect is forked: the route map and camp four use #1F6A70, while
# tense-palette.css and five standalone lessons use #0F6E56. Different hues,
# so the hue-matching above finds only the first. Soften BOTH by the same t
# — the fork stays exactly as unresolved as it was, and this change does not
# quietly widen it.
EXTRA = ['#0F6E56']

def hue_of(h):
    L, C, H = to_lch(h)
    return L, C, H

def in_family(h, accent_hue):
    L, C, H = hue_of(h)
    if C < CHROMA_FLOOR:
        return False                      # grey: not part of any hue family
    d = abs((H - accent_hue + math.pi) % (2 * math.pi) - math.pi)
    return d <= HUE_TOL

def collect(path, accent):
    """Every distinct hex in the file that belongs to the accent's family."""
    src = open(os.path.join(ROOT, path), encoding='utf-8').read()
    _, _, ah = hue_of(accent)
    out = {}
    for m in re.finditer(r'#([0-9A-Fa-f]{6})', src):
        h = '#' + m.group(1).upper()
        if h in out or not in_family(h, ah):
            continue
        if SKIP_DECL.search(src[max(0, m.start() - 24):m.start()]):
            continue
        out[h] = soften(h, T)
    return out

def rewrite(path, mapping):
    full = os.path.join(ROOT, path)
    src = open(full, encoding='utf-8').read()
    n = [0]
    def sub(m):
        h = '#' + m.group(1).upper()
        if h not in mapping:
            return m.group(0)
        if SKIP_DECL.search(src[max(0, m.start() - 24):m.start()]):
            return m.group(0)
        n[0] += 1
        return mapping[h]
    out = re.sub(r'#([0-9A-Fa-f]{6})', sub, src)
    if out != src and not DRY:
        open(full, 'w', encoding='utf-8').write(out)
    return n[0]

if __name__ == '__main__':
    print('\n  t = %.2f — 10%% along the same path the pink and navy used%s\n'
          % (T, '   [dry run]' if DRY else ''))
    shared_map = {}
    for name, accent, files in FAMILIES:
        print('  %s   %s -> %s' % (name, accent, soften(accent, T)))
        merged = {}
        for f in files:
            m = collect(f, accent)
            merged.update(m)
            for old, new in sorted(m.items()):
                print('      %-38s %s -> %s' % (os.path.basename(f), old, new))
        shared_map.update(merged)
        # the route map and the token file use the canonical value, which may
        # not appear on the camp page at all (camp eight runs a darker one)
        shared_map[accent] = soften(accent, T)
        for f in files:
            print('      %-38s %d replacement(s)' % (os.path.basename(f), rewrite(f, merged)))
        print('')
    for h in EXTRA:
        shared_map[h] = soften(h, T)
        print('  the forked present perfect     %s -> %s' % (h, shared_map[h]))
    print('')
    for f in SHARED:
        print('  %-44s %d replacement(s)' % (f, rewrite(f, shared_map)))
    print('')
