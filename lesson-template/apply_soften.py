#!/usr/bin/env python3
"""apply_soften.py — push the softened present-continuous pink and
present-simple navy through every file that hardcodes them.

Innes asked for those two colours to be "much softer/lighter". The amount
is not a taste call. soften.py walks a colour up an OKLCh path — raise
lightness, drop chroma faster, hold hue — and stops at the last step where
--accent still clears 3:1 against its own paper. That is t = 0.29 for the
pink and t = 0.49 for the navy.

Every other member of each family moves along the SAME path by the SAME t,
so the family stays a family instead of drifting one stop at a time.

Two roles, two rules — this is the part that matters:

  FILL   backgrounds, dots, route segments, gradient stops, the 52px
         score. Gets the full t. The WCAG floor for these is 3:1.
  TEXT   small copy: --accent-dark on the italic examples and the retry
         button, the 11.5px diagram captions. Gets t, then walks BACK
         along the same path until it clears 4.5:1 on its own paper.
         Softening these blind is how a caption ends up at 2.9:1.

Tokens that were never the pink or the blue — --ink, --ink-soft, --paper,
--card, --good, --bad — are skipped by declaration name. --ink on camp two
is #0C2340, which is also a stop in the diagram gradient; without that
guard the body text of the page would have been lightened to #7488A2.

Softened fills cannot carry white text (white on the new pink is 3.3:1),
so an --on-accent token is added and every accent fill's label repointed
at it.

    python3 lesson-template/apply_soften.py --dry-run
    python3 lesson-template/apply_soften.py
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from soften import soften, contrast, to_lch, from_lch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = '--dry-run' in sys.argv

T_PINK, T_NAVY = 0.29, 0.49
TEXT_FLOOR = 4.5

#           colour     paper it sits on
PAPER_LIGHT_PINK = '#FDF7F5'
PAPER_LIGHT_NAVY = '#F7FAFD'
PAPER_DARK_PINK  = '#1A0810'
PAPER_DARK_NAVY  = '#0E141F'

def clamp_text(base, t, paper, floor=TEXT_FLOOR):
    """Soften as far as t, then walk back toward the original until the
    result is legible as small text on `paper`."""
    while t > 0:
        c = soften(base, t)
        if contrast(c, paper) >= floor:
            return c
        t -= 0.01
    return base

def on_accent_for(accent):
    """Label colour for text sitting on an accent fill: whichever of white
    or a deep tint of the accent's own hue reads better."""
    L, C, H = to_lch(accent)
    ink = from_lch(L * 0.28, C * 0.5, H)
    return '#FFFFFF' if contrast(accent, '#FFFFFF') >= contrast(accent, ink) else ink

# ── families ────────────────────────────────────────────────────────
def fills(stops, t):   return {s: soften(s, t) for s in stops}
def texts(stops, t, p): return {s: clamp_text(s, t, p) for s in stops}

PINK = {
    **fills(['#C2185B',   # --accent, route segments, camp dots, camp-row fill
             '#F6CFE1',   # --accent-light
             '#FBEAF0',   # --accent-lighter, diagram ramp 100%
             '#E0568F',   # diagram ramp 42%
             '#F3B8CF'],  # diagram ramp 70%
            T_PINK),
    **texts(['#7A0F3E',   # --accent-dark: italic examples, retry btn, captions
             '#8A6070'],  # 11.5px diagram sub-captions
            T_PINK, PAPER_LIGHT_PINK),
}

NAVY = {
    **fills(['#16345C',   # --accent
             '#C7DFF5',   # --accent-light
             '#EAF3FC',   # --accent-lighter
             '#3E6EA6',   # diagram ramp, lightest
             '#1E4372'],  # diagram ramp, mid
            T_NAVY),
    **texts(['#0A1E38',   # --accent-dark
             '#7C8899'],  # diagram labels
            T_NAVY, PAPER_LIGHT_NAVY),
}
# #0C2340 and #050F1C are left alone: the first is camp two's --ink and the
# second is the bottom of its gradient. Lifting either lightens body text.

DESCENT = {
    **fills(['#D14C7E', '#F09BBB'], T_PINK),
    **texts(['#5E0B2C', '#33061A'], T_PINK, PAPER_DARK_PINK),
    **fills(['#7C99C4'], T_NAVY),
}

ON_ACCENT = {'pink': on_accent_for(PINK['#C2185B']),
             'navy': on_accent_for(NAVY['#16345C'])}

SKIP_DECL = re.compile(r'--(ink|ink-soft|paper|card|good|bad)[a-z-]*\s*:\s*$')

FILES = {
    'lesson-template/tense-palette.css':                          {**PINK, **NAVY},
    'sherpa-tensing-camp-one-present-continuous.html':             PINK,
    'sherpa-tensing-camp-two-present-simple.html':                 NAVY,
    'sherpa-tensing-route-map.html':                              {**PINK, **NAVY},
    'sherpa-tensing-descent-one-present-continuous-passive.html':  DESCENT,
    'sherpa-tensing-descent-two-present-simple-passive.html':      DESCENT,
    'lesson-template/build/build_c1_c2.py':                       {**PINK, **NAVY},
    'lesson-template/build/build_descent_a.py':                   {**PINK, **NAVY, **DESCENT},
    'lesson-template/build/build_pt.py':                          {**PINK, **NAVY},
    'present-simple-vs-continuous.html':                          {**PINK, **NAVY},
}
# library.html is handled by hand, not here. Its pink appears in two
# unrelated places: the .sherpa-banner gradient, which carries white text
# and so cannot take the full t, and the 'Speaking activity' category
# chip, which is not a tense colour at all and must not move.

def rewrite(path, mapping):
    full = os.path.join(ROOT, path)
    src = open(full, encoding='utf-8').read()
    n = [0]
    def sub(m):
        h = '#' + m.group(1).upper()
        if h not in mapping:
            return m.group(0)
        if SKIP_DECL.search(src[max(0, m.start() - 24):m.start()]):
            return m.group(0)            # a token that was never the accent
        n[0] += 1
        return mapping[h]
    out = re.sub(r'#([0-9A-Fa-f]{6})', sub, src)
    if out != src and not DRY:
        open(full, 'w', encoding='utf-8').write(out)
    return n[0]

if __name__ == '__main__':
    print('\n  pink t=%.2f  ->  %s        navy t=%.2f  ->  %s%s\n'
          % (T_PINK, PINK['#C2185B'], T_NAVY, NAVY['#16345C'],
             '   [dry run]' if DRY else ''))
    print('  label on a pink fill: %s      on a navy fill: %s\n'
          % (ON_ACCENT['pink'], ON_ACCENT['navy']))
    for old, new in sorted({**PINK, **NAVY, **DESCENT}.items()):
        print('    %s  ->  %s' % (old, new))
    print('')
    total = 0
    for path, mapping in FILES.items():
        k = rewrite(path, mapping)
        total += k
        print('    %-58s %3d' % (path, k))
    print('\n    %d replacements\n' % total)
