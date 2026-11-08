# -*- coding: utf-8 -*-
"""Measure the painted Regularia chart, so the label layer sits on the art.

    py lesson-template/build/regularia_measure.py <clean-chart.png|jpg>

Prints three Python blocks to paste into regularia_map.py:

  DOTS      every harbour dot, found by blob detection (a dark, round,
            11-ish px disc with a lighter ring round it), in image pixels
  OUTLINES  each landmass as a simplified polygon (sea = the pale blue the
            painter used; everything else inside the border is land)
  LANDS     the median paint colour of each landmass, for the label inks

The painter moved every harbour when it repainted the coded chart, so
nothing from sea_charts.py's coordinates can be reused. HANDOFF's rule for
overlaying artwork: blob-detect the markers, never eyeball them.
"""
import sys, json
import numpy as np
from PIL import Image
from scipy import ndimage as nd
import cv2

src = sys.argv[1] if len(sys.argv) > 1 else 'sailing-the-seas-regularia/chart-clean.jpg'
im = Image.open(src).convert('RGB')
a = np.asarray(im).astype(int)
H, W = a.shape[:2]
L = a.mean(axis=2)


def dots(maxv=70, ring_min=110):
    m = a.max(axis=2) < maxv
    lab, _ = nd.label(m)
    out = []
    for i, sl in enumerate(nd.find_objects(lab), 1):
        h = sl[0].stop - sl[0].start
        w = sl[1].stop - sl[1].start
        area = (lab[sl] == i).sum()
        if not (7 <= h <= 16 and 7 <= w <= 16 and abs(h - w) <= 3 and area >= 0.68 * h * w):
            continue
        cy = (sl[0].start + sl[0].stop - 1) / 2
        cx = (sl[1].start + sl[1].stop - 1) / 2
        y0, y1 = max(0, int(cy - h)), int(cy + h + 1)
        x0, x1 = max(0, int(cx - w)), int(cx + w + 1)
        sub = lab[y0:y1, x0:x1] == i
        if L[y0:y1, x0:x1][~sub].mean() > ring_min:
            out.append((round(cx), round(cy)))
    return out


def sea_mask():
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    sea = (b > r + 18) & (b > 140)
    sea = nd.binary_opening(sea, iterations=2)
    return sea


def outlines(min_area=1500):
    sea = sea_mask()
    land = ~sea
    border = 22                                  # the ruled parchment frame
    land[:border, :] = land[-border:, :] = False
    land[:, :border] = land[:, -border:] = False
    land = nd.binary_closing(land, iterations=3)
    land = nd.binary_fill_holes(land)
    lab, n = nd.label(land)
    shapes = []
    for i in range(1, n + 1):
        m = (lab == i).astype(np.uint8)
        area = int(m.sum())
        if area < min_area:
            continue
        cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        c = max(cs, key=cv2.contourArea)
        poly = cv2.approxPolyDP(c, 3.0, True)[:, 0, :].tolist()
        ys, xs = np.nonzero(m)
        med = np.median(a[ys, xs], axis=0).astype(int).tolist()
        shapes.append(dict(area=area, cx=int(xs.mean()), cy=int(ys.mean()),
                           bbox=[int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())],
                           colour='#%02x%02x%02x' % tuple(med), poly=poly))
    return shapes


OUT = 'lesson-template/build/regularia_chart.json'

if __name__ == '__main__':
    d = dots()
    print('# %d dots (two are not harbours: a rock in the Still Rocks and a cliff edge on -T Island;'
          ' Think Tarn sits on a lake shore and needs the ring test relaxed)' % len(d))
    print('DOTS = %s' % json.dumps(d))
    shapes = sorted(outlines(), key=lambda s: -s['area'])
    for s in shapes:
        print('# area %(area)d centre (%(cx)d,%(cy)d) bbox %(bbox)s colour %(colour)s points %(n)d'
              % dict(s, n=len(s['poly'])))
    json.dump({'source': src, 'size': [W, H], 'shapes': shapes}, open(OUT, 'w'), separators=(',', ':'))
    print('wrote', OUT)
