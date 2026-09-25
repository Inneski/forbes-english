"""A seamless topographic contour tile, as SVG.

The Sherpa route map's background, `Sherpa Tensing/topo-tile.svg`, is:

    py tools/topo_tile.py "Sherpa Tensing/topo-tile.svg" --seed 7 --opacity .06 --index-opacity .10

Same arguments, same file: the seed fixes the terrain. If the colour or
opacity changes, re-run `py tools/check_route_map.py`: it measures the
page's small text against the darkest point a contour line makes.

    py tools/topo_tile.py <out.svg> [--size 640] [--seed 7] [--levels 16]
                    [--colour #AD5470] [--opacity .08] [--index-opacity .14]

The height field is a sum of sinusoids with integer wave numbers over the
tile, so it is periodic: the contours leaving one edge are the ones entering
the opposite edge, and the tile repeats without a seam. Contours are traced
with marching squares, stitched into polylines, smoothed (Chaikin) and
written as SVG paths. Every fifth level is an index contour, drawn heavier,
as on a survey map.
"""
import argparse
import math
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('out')
ap.add_argument('--size', type=int, default=640)
ap.add_argument('--step', type=float, default=4.0)
ap.add_argument('--seed', type=int, default=7)
ap.add_argument('--levels', type=int, default=16)
ap.add_argument('--colour', default='#AD5470')
ap.add_argument('--opacity', type=float, default=.08)
ap.add_argument('--index-opacity', type=float, default=.14)
ap.add_argument('--width', type=float, default=1.0)
a = ap.parse_args()

S = a.size
N = int(round(S / a.step))                  # cells per side
rng = np.random.default_rng(a.seed)

# periodic field: integer wave vectors, amplitude falling with frequency
xs = np.arange(N + 1) / N                    # 0..1 inclusive: last column == first
X, Y = np.meshgrid(xs, xs)
H = np.zeros_like(X)
for kx in range(-5, 6):
    for ky in range(0, 6):
        if (kx, ky) == (0, 0) or (ky == 0 and kx < 0):
            continue
        k = math.hypot(kx, ky)
        amp = rng.normal() / k ** 1.9
        ph = rng.uniform(0, 2 * math.pi)
        H += amp * np.cos(2 * math.pi * (kx * X + ky * Y) + ph)
H = (H - H.min()) / (H.max() - H.min())

levels = np.linspace(0, 1, a.levels + 2)[1:-1]
# marching squares edge table: which cell edges a level crosses
# corners: 0=(i,j) tl, 1=(i,j+1) tr, 2=(i+1,j+1) br, 3=(i+1,j) bl ; edges 0 top,1 right,2 bottom,3 left
CASES = {1: [(3, 0)], 2: [(0, 1)], 3: [(3, 1)], 4: [(1, 2)], 5: [(3, 0), (1, 2)], 6: [(0, 2)],
         7: [(3, 2)], 8: [(2, 3)], 9: [(0, 2)], 10: [(0, 1), (2, 3)], 11: [(1, 2)], 12: [(1, 3)],
         13: [(0, 1)], 14: [(3, 0)]}


def edge_point(i, j, e, lv):
    def lerp(p, q, vp, vq):
        t = (lv - vp) / (vq - vp) if vq != vp else .5
        return (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))
    tl, tr, br, bl = (j, i), (j + 1, i), (j + 1, i + 1), (j, i + 1)
    v = {tl: H[i, j], tr: H[i, j + 1], br: H[i + 1, j + 1], bl: H[i + 1, j]}
    return lerp(*{0: (tl, tr), 1: (tr, br), 2: (br, bl), 3: (bl, tl)}[e],
                *{0: (v[tl], v[tr]), 1: (v[tr], v[br]), 2: (v[br], v[bl]), 3: (v[bl], v[tl])}[e])


def trace(lv):
    segs = []
    for i in range(N):
        for j in range(N):
            c = ((H[i, j] > lv) << 0 | (H[i, j + 1] > lv) << 1 |
                 (H[i + 1, j + 1] > lv) << 2 | (H[i + 1, j] > lv) << 3)
            for e1, e2 in CASES.get(c, []):
                segs.append((edge_point(i, j, e1, lv), edge_point(i, j, e2, lv)))
    # stitch segments into polylines
    key = lambda p: (round(p[0], 4), round(p[1], 4))
    ends = {}
    for k, (p, q) in enumerate(segs):
        ends.setdefault(key(p), []).append((k, 0))
        ends.setdefault(key(q), []).append((k, 1))
    used = [False] * len(segs)
    lines = []
    for k in range(len(segs)):
        if used[k]:
            continue
        used[k] = True
        line = [segs[k][0], segs[k][1]]
        for grow_end in (1, 0):
            while True:
                tip = line[-1] if grow_end else line[0]
                nxt = None
                for (m, side) in ends.get(key(tip), []):
                    if not used[m]:
                        nxt = (m, side)
                        break
                if not nxt:
                    break
                m, side = nxt
                used[m] = True
                other = segs[m][1 - side]
                if grow_end:
                    line.append(other)
                else:
                    line.insert(0, other)
        lines.append(line)
    return lines


def chaikin(pts, closed, n=2):
    for _ in range(n):
        out = [] if closed else [pts[0]]
        rng_ = range(len(pts)) if closed else range(len(pts) - 1)
        for k in rng_:
            p, q = pts[k], pts[(k + 1) % len(pts)]
            out += [(.75 * p[0] + .25 * q[0], .75 * p[1] + .25 * q[1]),
                    (.25 * p[0] + .75 * q[0], .25 * p[1] + .75 * q[1])]
        if not closed:
            out.append(pts[-1])
        pts = out
    return pts


scale = S / N
paths_minor, paths_index = [], []
for li, lv in enumerate(levels):
    for line in trace(lv):
        if len(line) < 3:
            continue
        closed = abs(line[0][0] - line[-1][0]) < 1e-6 and abs(line[0][1] - line[-1][1]) < 1e-6
        pts = chaikin(line[:-1] if closed else line, closed)
        pts = [(x * scale, y * scale) for x, y in pts]
        # thin the points: drop ones closer than 2px to the last kept
        kept = [pts[0]]
        for p in pts[1:]:
            if math.hypot(p[0] - kept[-1][0], p[1] - kept[-1][1]) >= 3.5:
                kept.append(p)
        if not closed:
            kept.append(pts[-1])
        d = 'M' + ' '.join('%.0f %.0f' % p for p in kept) + ('Z' if closed else '')
        (paths_index if (li + 1) % 5 == 0 else paths_minor).append(d)

svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">'
       '<g fill="none" stroke="%s" stroke-linejoin="round" stroke-linecap="round">'
       '<path stroke-opacity="%s" stroke-width="%s" d="%s"/>'
       '<path stroke-opacity="%s" stroke-width="%s" d="%s"/>'
       '</g></svg>\n' % (S, S, S, S, a.colour, a.opacity, a.width, ''.join(paths_minor),
                         a.index_opacity, round(a.width * 1.5, 2), ''.join(paths_index)))
open(a.out, 'w', encoding='utf-8', newline='\n').write(svg)
print('%s: %d minor, %d index paths, %.1f KB' % (a.out, len(paths_minor), len(paths_index), len(svg) / 1024))
