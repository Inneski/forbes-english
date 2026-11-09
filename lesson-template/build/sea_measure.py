# -*- coding: utf-8 -*-
"""Measure a painted sea chart so a label layer can sit on the art.

    py lesson-template/build/sea_measure.py <clean.png|jpg> <out.json> [--dark]

The general form of regularia_measure.py / countania_measure.py, for the
charts that came after them. Writes the harbour dots (blob detection: a dark,
round, ~11px disc) and every landmass (sea = the painter's pale blue) with
its median paint colour, and prints both. --dark relaxes the light-ring test
round each dot, for dots painted on deep water (the frequency soundings).
"""
import sys, json
import numpy as np
from PIL import Image
from scipy import ndimage as nd
import cv2


def load(src):
    return np.asarray(Image.open(src).convert('RGB')).astype(int)


def dots(a, maxv=70, ring_min=110, dark=False):
    L = a.mean(axis=2)
    m = a.max(axis=2) < maxv
    lab, _ = nd.label(m)
    out = []
    for i, sl in enumerate(nd.find_objects(lab), 1):
        h = sl[0].stop - sl[0].start
        w = sl[1].stop - sl[1].start
        area = (lab[sl] == i).sum()
        if not (7 <= h <= 18 and 7 <= w <= 18 and abs(h - w) <= 3 and area >= 0.68 * h * w):
            continue
        cy = (sl[0].start + sl[0].stop - 1) / 2
        cx = (sl[1].start + sl[1].stop - 1) / 2
        y0, y1 = max(0, int(cy - h)), int(cy + h + 1)
        x0, x1 = max(0, int(cx - w)), int(cx + w + 1)
        sub = lab[y0:y1, x0:x1] == i
        ring = L[y0:y1, x0:x1][~sub].mean()
        if ring > (ring_min if not dark else L[y0:y1, x0:x1][sub].mean() + 25):
            out.append((round(cx), round(cy)))
    return out


def outlines(a, min_area=1500, border=22):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    sea = nd.binary_opening((b > r + 18) & (b > 140), iterations=2)
    land = ~sea
    land[:border, :] = land[-border:, :] = False
    land[:, :border] = land[:, -border:] = False
    land = nd.binary_fill_holes(nd.binary_closing(land, iterations=3))
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
    return sorted(shapes, key=lambda s: -s['area'])


def sea_colour(a):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    return '#%02X%02X%02X' % tuple(np.median(a[(b > r + 18) & (b > 140)], axis=0).astype(int))


if __name__ == '__main__':
    src, out = sys.argv[1], sys.argv[2]
    a = load(src)
    d = dots(a, dark='--dark' in sys.argv)
    shapes = outlines(a)
    print('# %d dots' % len(d))
    print('DOTS = %s' % json.dumps(sorted(d, key=lambda p: (p[1], p[0]))))
    for s in shapes:
        print('# area %(area)d centre (%(cx)d,%(cy)d) bbox %(bbox)s colour %(colour)s' % s)
    print('# sea', sea_colour(a))
    json.dump({'source': src, 'size': [a.shape[1], a.shape[0]], 'sea': sea_colour(a), 'dots': d, 'shapes': shapes},
              open(out, 'w'), separators=(',', ':'))
    print('wrote', out)
