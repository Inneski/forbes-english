#!/usr/bin/env python3
"""Find the horizontal offset that puts a block in the negative space.

Innes: "place in the negative space and don't overlap if possible". A named
step (one nudge, two nudges) is a guess. This scans every offset the canvas
allows and scores two things at each one:

  overlap  the share of the block's area sitting over BUSY artwork - the
           subject. This is the thing to drive to zero.
  mean     the average detail under the block, as the tie-breaker when a
           whole range of offsets reaches zero overlap: the middle of that
           range is the calmest place to stand, not its edge.

Usage: python3 solve-nudge.py <deck.html> <slide> [side] [vpos]
"""
import importlib.util, json, os, subprocess, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('cp', os.path.join(HERE, 'check-placement.py'))
cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)

BUSY   = 0.34    # a cell above this is subject, not backdrop
PAD    = 0.035   # keep this much clear of the canvas edge
STEP   = 8       # px


def cells(sd, b):
    G = cp.GRID
    x0 = max(0, min(G - 1, int(b['x'] * G)))
    x1 = max(x0 + 1, min(G, int(round((b['x'] + b['w']) * G))))
    y0 = max(0, min(G - 1, int(b['y'] * G)))
    y1 = max(y0 + 1, min(G, int(round((b['y'] + b['h']) * G))))
    return sd[y0:y1, x0:x1]


def main():
    deck, idx = sys.argv[1], int(sys.argv[2])
    data = json.loads(subprocess.run(['node', os.path.join(HERE, 'dump-rects.js'), deck],
                                     capture_output=True, text=True).stdout)
    s = data['slides'][idx - 1]
    side = sys.argv[3] if len(sys.argv) > 3 else s['side']
    vpos = sys.argv[4] if len(sys.argv) > 4 else (s['vpos'] or 'center')
    boxes = s['slots'][f'{side}/{vpos}']
    sd = cp.detail_map(os.path.join(os.path.dirname(os.path.abspath(deck)), s['bg']))

    lo = min(b['x'] for b in boxes.values())
    hi = max(b['x'] + b['w'] for b in boxes.values())
    dmin = int((PAD - lo) * 1280)
    dmax = int((1 - PAD - hi) * 1280)

    rows = []
    for d in range(dmin, dmax + 1, STEP):
        ov = mn = area = 0.0
        for b in boxes.values():
            r = cells(sd, dict(b, x=b['x'] + d / 1280))
            a = r.size
            ov += float((r > BUSY).sum()); mn += float(r.sum()); area += a
        rows.append((d, ov / area, mn / area))

    best_ov = min(r[1] for r in rows)
    clear = [r for r in rows if r[1] <= best_ov + 1e-9]
    best = min(clear, key=lambda r: r[2])
    print(f'{os.path.basename(deck)} slide {idx}  {side}/{vpos}   range {dmin}..{dmax}px')
    print(f'  block spans {lo:.2f}..{hi:.2f} of the frame')
    for d, ov, mn in rows:
        if rows.index((d, ov, mn)) % max(1, len(rows) // 24) and d != best[0]:
            continue
        bar = '#' * int(ov * 90)
        print(f'   {d:+5d}px  overlap {ov*100:5.1f}%  mean {mn:.3f}  {bar}'
              + ('   <- best' if d == best[0] else ''))
    print(f'\n  BEST {best[0]:+d}px   overlap {best[1]*100:.1f}%   mean {best[2]:.3f}')
    print(f'  zero-overlap window: '
          + (f'{min(r[0] for r in clear):+d} .. {max(r[0] for r in clear):+d}px'
             if best_ov == 0 else 'none - some overlap is unavoidable'))


if __name__ == '__main__':
    main()
