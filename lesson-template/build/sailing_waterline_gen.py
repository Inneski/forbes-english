"""Generate the final waterlining pattern.css (finalist: waterline).

Concept: each side of the page is a coast. A wandering shoreline hugs the
edge; waterlines run out from it into the open water of the margin, each one
smoother, wider-spaced and fainter than the last -- the antique-chart
convention the hero uses around its shores. A faint shallow-water tint hugs
the shore (optional, --no-tint to leave it out).

Changes from the first-round candidate (cand-waterline):
  * one pseudo-element (body::before). Both coasts are mask layers on it:
    the left tile at 0 0, and a right tile at 100% 0 that is GENERATED
    mirrored (x -> W-x) and turned end for end (y -> H-y), so no transform.
  * no dashed current, no arrowhead.
  * first gaps 10px and up (were 4.5-6.5px), so the lines never close up
    into a moire band when the page is scaled down for a screen-share.
  * 10 lines reaching ~190px from the edge instead of ~110px; one fade,
    computed from the viewport, takes them to exactly zero 4px outside the
    1000px column at every width.
  * @supports guard: without masks the page shows nothing.
  * the fill stops 2px short of the page bottom. At a fractional DPR (1440
    CSS at 133%) Chrome painted the fill's part-pixel last row outside the
    mask: a 4-level line right across the column at the foot of the page
    (the first-round candidate had it too, 1334 px at the quiz stop).
  * the shore never comes nearer the page edge than ~6px (it touched 0.7px),
    which is what the low-frequency peak of the downscaled page sat on.
The tile is periodic in y so it repeats without a seam.

usage: py gen.py [opacity=.05] [phone_opacity=.04] [out=pattern.css] [--no-tint] [--svg]
"""
import math, sys, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

W, H = 980, 1200             # tile size (px): each coast reaches the page's centre line
BASE = 34                    # mean shoreline distance from the page edge (never < 6)

# harmonics of the coast: (k, amplitude px, phase)
HARM = [(1, 7.0, 0.3), (2, 6.0, 1.9), (3, 5.0, 4.1), (5, 4.5, 2.6),
        (7, 3.6, 5.2), (11, 2.0, 0.9), (16, 1.3, 3.7), (21, 0.8, 2.2)]

# waterline distances from the shore (cumulative gaps) and relative alpha.
# Innes, 2026-09-30: "too subtle and doesn't cover enough". So past the ninth
# line the water keeps going, gaps widening to 40px, all the way to the
# page's centre line, where the other coast's lines take over.
GAPS = [10, 11, 12, 13.5, 15, 17, 19, 21.5, 24]
while sum(GAPS) < W - 30:
    GAPS.append(min(40, GAPS[-1] + 2))
DIST = [sum(GAPS[:i]) for i in range(len(GAPS) + 1)]
ALPHA = [1.0, .86, .78, .71, .65, .59, .54, .49, .45, .41]
ALPHA = [max(.5, a) for a in ALPHA]
ALPHA += [.5] * (len(DIST) - len(ALPHA))
assert len(ALPHA) == len(DIST)

def shore(y):
    x = BASE
    for k, a, p in HARM:
        x += a * math.sin(2 * math.pi * k * y / H + p)
    return x

RES = 4                                   # samples per px
_Y = np.arange(-H, 2 * H, 1 / RES)
_S = np.array([shore(y) for y in _Y])
_lines = {}

def iso(d):
    """The true iso-distance line at distance d from the land (everything
    left of the shore): the shore dilated by a disc. Headlands round off,
    bays fill in, and no two lines ever touch. A light moving average takes
    the cusps out of the bays."""
    if d in _lines:
        return _lines[d]
    if d == 0:
        out = _S.copy()
    else:
        n = int(d * RES)
        out = np.full_like(_S, -1e9)
        for j in range(-n, n + 1):
            dy = j / RES
            out = np.maximum(out, np.roll(_S, -j) + math.sqrt(max(d * d - dy * dy, 0)))
        win = max(1, int(d * 0.35 * RES))
        k = np.ones(2 * win + 1) / (2 * win + 1)
        out = np.convolve(np.pad(out, win, mode='wrap'), k, mode='valid')
    _lines[d] = out
    return out

def coast(y, d):
    return float(np.interp(y, _Y, iso(d)))

def fmt(v):
    s = ('%.1f' % v).rstrip('0').rstrip('.')
    if s in ('-0', ''):
        s = '0'
    if s.startswith('0.'):
        s = s[1:]
    elif s.startswith('-0.'):
        s = '-' + s[2:]
    return s

def fa(v):
    """alpha to two places, no leading zero"""
    return ('%.2f' % v).rstrip('0').rstrip('.').lstrip('0') or '0'

def join(vals):
    out = ''
    for v in vals:
        t = fmt(v)
        out += t if (not out or t[0] == '-') else ',' + t
    return out

def spline_path(f, y0, y1, step, nd=1):
    """Catmull-Rom through f(y) sampled every `step`, written as relative
    cubics measured from the ROUNDED current point (so rounding never drifts
    across the tile seam), 's' after the first segment. `step` is a multiple
    of 3 so the control points' y offsets are whole numbers; the smooth outer
    lines are written to whole pixels (nd=0)."""
    ys = [y0 + j * step for j in range(int(round((y1 - y0) / step)) + 1)]
    pts = [(f(y), y) for y in ys]
    cur = [round(pts[0][0], nd), pts[0][1]]
    out = 'M%s,%s' % (fmt(cur[0]), fmt(cur[1]))
    for j in range(len(pts) - 1):
        p0 = pts[j - 1] if j > 0 else (f(ys[0] - step), ys[0] - step)
        p1, p2 = pts[j], pts[j + 1]
        p3 = pts[j + 2] if j + 2 < len(pts) else (f(p2[1] + step), p2[1] + step)
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        vals = (c1[0], c1[1], c2[0], c2[1], p2[0], p2[1])
        rel = [round(v - cur[k % 2], nd) for k, v in enumerate(vals)]
        out += ('c' + join(rel)) if j == 0 else ('s' + join(rel[2:]))
        cur = [cur[0] + rel[4], cur[1] + rel[5]]
    return out

def step_for(d):
    """Sampling step (px) and decimals: the further out, the smoother the
    line, so the fewer points it needs. Whole pixels off the shore: the
    rounding moves a line by at most half a pixel and never drifts."""
    if d == 0:
        return 15, 1
    if d < 25:
        return 24, 0
    if d < 40:
        return 30, 0
    if d < 70:
        return 48, 0
    return 60, 0

ID = 'uvwxyz'                # <use> ids: no hex letters, so nothing reads as a colour

# shallow water: a wide, very faint stroke laid along one of the waterlines,
# so it costs no path data of its own. (line index, stroke width, alpha)
TINT = [(1, 20, .10), (2, 40, .09), (3, 62, .07)]

def svg_coast(mirror, tint=True):
    """mirror=True: the right-hand coast, x -> W-x and y -> H-y."""
    if mirror:
        g = lambda d: (lambda y: W - coast(H - y, d))
    else:
        g = lambda d: (lambda y: coast(y, d))
    tinted = {i: (w, a) for i, w, a in TINT} if tint else {}
    defs, parts, under = [], [], []
    for i, dist in enumerate(DIST):
        st, nd = step_for(dist)
        d = spline_path(g(dist), -st, H + st, st, nd)
        sw = fmt(1.25 if i == 0 else 1.05)
        swa = " stroke-width='1.25'" if i == 0 else ''
        if i in tinted:
            w, a = tinted[i]
            defs.append("<path id='%s' d='%s'/>" % (ID[i], d))
            under.append("<use href='#%s' stroke-width='%s' stroke-opacity='%s'/>" % (ID[i], fmt(w), fa(a)))
            parts.append("<use href='#%s' stroke-width='%s' stroke-opacity='%s'/>" % (ID[i], sw, fa(ALPHA[i])))
        else:
            op = '' if ALPHA[i] >= 1 else " stroke-opacity='%s'" % fa(ALPHA[i])
            parts.append("<path d='%s'%s%s/>" % (d, swa, op))
    body = (('<defs>%s</defs>' % ''.join(defs)) if defs else '') + ''.join(under) + ''.join(parts)
    return ("<svg xmlns='http://www.w3.org/2000/svg' width='%d' height='%d' "
            "fill='none' stroke='currentColor' stroke-width='1.05'>%s</svg>" % (W, H, body))

def encode(s):
    return (s.replace('%', '%25').replace('#', '%23').replace('<', '%3C')
             .replace('>', '%3E').replace('"', '%22'))

def css(opacity, phone_opacity, tint=True):
    left = encode(svg_coast(False, tint))
    right = encode(svg_coast(True, tint))
    # Each coast owns half the page: body::before the left half, body::after
    # the right, so the two sets of waterlines never cross. Full strength in
    # the margins; behind the 1000px column the lines carry on at COL of it.
    # The fill stops 2px short of the page bottom: at a fractional DPR Chrome
    # paints a part-pixel row unmasked.
    COL = 70
    colmix = f'color-mix(in srgb,var(--ink) {COL}%,transparent)'
    L = f"linear-gradient(to right,var(--ink) max(8px,calc(100% - 574px)),{colmix} max(24px,calc(100% - 504px)))"
    R = f"linear-gradient(to left,var(--ink) max(8px,calc(100% - 574px)),{colmix} max(24px,calc(100% - 504px)))"
    return f"""/* Waterlining: each side of the page is a coast; waterlines run out from
   it across the page, each smoother, wider-spaced and fainter than the last,
   over a faint shallow-water tint by the shore. Each coast owns half the page,
   so the two sets never cross; behind the reading column the lines carry on
   at {COL}% strength. Cards and the hero image are opaque and sit above;
   the sky (clouds and gulls, z-index -1) passes over the water. */
@supports ((mask-image:none) or (-webkit-mask-image:none)) and (color:color-mix(in srgb,red 50%,transparent)){{
body{{position:relative;}}
body::before,body::after{{
  content:"";position:absolute;top:0;bottom:0;
  z-index:-2;pointer-events:none;
  background:linear-gradient(var(--accent) calc(100% - 2px),transparent 0);opacity:{opacity};
  -webkit-mask-repeat:no-repeat,repeat-y;mask-repeat:no-repeat,repeat-y;
  -webkit-mask-size:100% 100%,{W}px {H}px;mask-size:100% 100%,{W}px {H}px;
  -webkit-mask-composite:source-in;mask-composite:intersect;
}}
body::before{{left:0;right:50%;
  -webkit-mask-image:{L},url("data:image/svg+xml,{left}");
  mask-image:{L},url("data:image/svg+xml,{left}");
  -webkit-mask-position:0 0,0 0;mask-position:0 0,0 0;}}
body::after{{left:50%;right:0;
  -webkit-mask-image:{R},url("data:image/svg+xml,{right}");
  mask-image:{R},url("data:image/svg+xml,{right}");
  -webkit-mask-position:0 0,100% 0;mask-position:0 0,100% 0;}}
@media (max-width:1060px){{
  body::before,body::after{{opacity:{phone_opacity};}}
}}
@media print{{body::before,body::after{{display:none;}}}}
}}
"""

if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    tint = '--no-tint' not in sys.argv
    op = args[0] if len(args) > 0 else '.22'
    pop = args[1] if len(args) > 1 else '.13'
    name = args[2] if len(args) > 2 else 'pattern.css'
    out = css(op, pop, tint)
    with open(os.path.join(HERE, name), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(out)
    if '--svg' in sys.argv:
        for nm, m in (('tile-left.svg', False), ('tile-right.svg', True)):
            with open(os.path.join(HERE, nm), 'w', encoding='utf-8', newline='\n') as fh:
                fh.write(svg_coast(m, tint))
    print(name, len(out.encode()), 'bytes')
