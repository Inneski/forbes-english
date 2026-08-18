#!/usr/bin/env python3
"""soften.py — lighten/desaturate a tense colour as far as the contrast
floor allows, and re-derive its whole ramp from the result.

Innes asked for the present-continuous pink and the present-simple navy to
be "much softer/lighter". The temptation is to eyeball a nicer hex. The
rule instead:

  Soften along a single OKLCh path — raise L, drop C, hold hue — and stop
  at the LAST step where accent-on-paper still clears 4.5:1.

That makes "as soft as possible" a measurement rather than a taste, and it
is reproducible: change FLOOR, re-run, get the next answer.

Every derived stop (dark / light / lighter / ink / ink-soft / paper) comes
off the same path, so the ramp stays internally consistent instead of
drifting one stop at a time.

    python3 lesson-template/soften.py            # report
    python3 lesson-template/soften.py --check    # non-zero if any row fails
"""
import sys, math

# --accent is never small body text on these pages. Grepping camp one, it
# carries: the 52px score, the wordmark, button fills, borders and dots.
# Small copy uses --ink and --accent-dark. So the honest floor for --accent
# is the WCAG large-text / non-text-contrast floor, not the body floor —
# and --accent-dark, which IS small text, keeps the strict one.
FLOOR = 3.0          # --accent vs its own paper (large text + UI)
DARK_FLOOR = 4.5     # --accent-dark vs paper (small italic examples, retry btn)

# ── colour maths ────────────────────────────────────────────────────
def hex2rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) / 255 for i in (0, 2, 4))

def rgb2hex(r):
    return '#' + ''.join('%02X' % max(0, min(255, round(c * 255))) for c in r)

def _lin(c):  return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
def _srgb(c): return c * 12.92 if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055

def luminance(h):
    r, g, b = (_lin(c) for c in hex2rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

def rgb2oklab(r, g, b):
    r, g, b = _lin(r), _lin(g), _lin(b)
    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    return (0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
            1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
            0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s)

def oklab2rgb(L, a, b):
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    return tuple(_srgb(max(0.0, min(1.0, v))) for v in (
        +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s))

def to_lch(h):
    L, a, b = rgb2oklab(*hex2rgb(h))
    return L, math.hypot(a, b), math.atan2(b, a)

def from_lch(L, C, H):
    return rgb2hex(oklab2rgb(max(0.0, min(1.0, L)), C * math.cos(H), C * math.sin(H)))

def soften(h, t, chroma_drop=0.55):
    """t=0 is the original; t=1 is white. Chroma falls faster than
    lightness rises, which is what makes it read as *soft* rather than
    merely pale."""
    L, C, H = to_lch(h)
    return from_lch(L + (1 - L) * t, C * (1 - chroma_drop * t), H)

# ── the two colours ─────────────────────────────────────────────────
TENSES = [
    ('present continuous', '#C2185B', '#FDF7F5'),   # accent, camp-one paper
    ('present simple',     '#16345C', '#F7FAFD'),   # accent, camp-two paper
]

def softest(base, floor=FLOOR):
    """Walk t upward in 1% steps and return the last value where the whole
    ramp still holds: --accent clears FLOOR against the paper derived from
    it, and --accent-dark clears DARK_FLOOR against that same paper.

    The paper is re-derived at every step rather than held fixed, because
    softening the accent softens the paper with it — checking against the
    old paper would flatter the result."""
    best, best_t = base, 0.0
    t = 0.0
    while t <= 1.0:
        cand = soften(base, t)
        r = ramp(cand)
        if (contrast(cand, r['paper']) < floor
                or contrast(r['accent-dark'], r['paper']) < DARK_FLOOR):
            break
        best, best_t = cand, t
        t += 0.01
    return best, best_t

def on_accent(accent):
    """Text sitting ON an accent fill. Pick whichever of white / the ramp's
    ink reads better — do not assume white, which is how a softened button
    ends up with 2:1 label text."""
    L, C, H = to_lch(accent)
    ink = from_lch(L * 0.30, C * 0.45, H)
    return ('#FFFFFF', contrast(accent, '#FFFFFF')) \
        if contrast(accent, '#FFFFFF') >= contrast(accent, ink) else (ink, contrast(accent, ink))

def ramp(accent):
    """Re-derive the six companion stops from the softened accent, along
    the same OKLCh path, so the ramp stays one family."""
    L, C, H = to_lch(accent)
    return {
        'accent':         accent,
        'accent-dark':    from_lch(L * 0.62, C * 1.05, H),   # hover / emphasis
        'accent-light':   from_lch(L + (1 - L) * 0.72, C * 0.42, H),
        'accent-lighter': from_lch(L + (1 - L) * 0.90, C * 0.28, H),
        'ink':            from_lch(L * 0.42, C * 0.55, H),
        'ink-soft':       from_lch(L * 0.78, C * 0.38, H),
        'paper':          from_lch(L + (1 - L) * 0.965, C * 0.20, H),
    }

def report():
    bad = 0
    out = {}
    for name, base, _old_paper in TENSES:
        new, t = softest(base)
        r = ramp(new)
        r['on-accent'], c_on = on_accent(new)
        out[name] = (base, t, r)
        print('\n  %s' % name.upper())
        print('  %-16s %s  ->  %s      (softened %d%% toward white)'
              % ('accent', base, new, round(t * 100)))
        for k in ('accent-dark', 'accent-light', 'accent-lighter',
                  'ink', 'ink-soft', 'paper', 'on-accent'):
            print('  %-16s %s' % (k, r[k]))
        rows = (('--accent on paper',      contrast(new, r['paper']),               FLOOR),
                ('--accent-dark on paper', contrast(r['accent-dark'], r['paper']),  DARK_FLOOR),
                ('--ink on paper',         contrast(r['ink'], r['paper']),          7.0),
                ('label on accent fill',   c_on,                                    4.5))
        for label, val, need in rows:
            ok = val >= need
            if not ok:
                bad += 1
            print('    %-24s %5.2f:1  (need %.1f)  %s'
                  % (label, val, need, 'PASS' if ok else 'FAIL'))
    print('')
    return out, bad

if __name__ == '__main__':
    _, bad = report()
    if '--check' in sys.argv and bad:
        sys.exit(1)


# ── softening a colour that is already at the top of its lightness range ──
#
# The path above (raise L, drop C) is wrong for yellow. #FFD400 sits at
# L=0.88 — there is almost no headroom, so raising lightness turns it to
# paper rather than softening it. Everything that reads as "too strong"
# about it is chroma.
#
# So for these, hold lightness and cut chroma. Two things were measured
# before trusting it, because neither is obvious:
#
#   The contrast floor does not bind. Cutting chroma at constant L leaves
#   the route segment at 3.8:1 against the mountain from 0% all the way to
#   -80%. There is no last-passing step, so contrast cannot pick the value
#   here the way it does for soften().
#
#   Separation IMPROVES. The nearest other tense colour to the yellow is
#   future continuous (#F0A500) at dE 12.0. Softening moves it further
#   away, not closer — dE 13.3 at -50% — because the amber is both darker
#   and more saturated. Dropping LIGHTNESS instead would close that gap to
#   dE 8.4, which is why this function does not touch L.
#
# With neither constraint binding, the amount is a judgement. Say so
# rather than inventing a floor to justify it. Render the candidates in
# situ and let Innes pick: he chose -35% over -45% on 2026-08-18.

def soften_light(h, chroma_drop):
    """Reduce chroma at constant lightness and hue. For colours near the
    top of the lightness range, where soften() would wash them out."""
    L, C, H = to_lch(h)
    return from_lch(L, C * (1 - chroma_drop), H)
