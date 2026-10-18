"""Cut the front-page lady out of her sofa for the 3D landing page.

The landing page (index.html) stands her in a dusk landscape as a glowing
slab, cut to her own outline: hair, spread arms and the open book. This
script makes the two things that page needs from the flat artwork:

  home/lady-cutout.webp   the figure, cropped to her bounding box, with an
                          alpha channel; the pixels outside her are filled
                          with the nearest colour inside her, so the 3D
                          edge never shows a fringe of sofa red
  home/lady-outline.json  her outer contour, normalised to 0..1 in the
                          texture's own frame (y up), which the page
                          extrudes into the slab and draws as the loader

The figure is everything that is neither the mustard wall nor the red
sofa, kept as the largest connected piece; that drops the legs and shoes,
which only touch her across the sofa. Run it again if the artwork changes:

    py tools/make_home_cutout.py
"""
import json
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'HOUSE STYLE' / ('blackisler_cool_female_student_studying_at_home_with_books_No_'
                              'f252909d-c97d-494b-b5b6-596be1e11502_2.png')
OUT_IMG = ROOT / 'home' / 'lady-cutout.webp'
OUT_JSON = ROOT / 'home' / 'lady-outline.json'
TEX_W = 2048


def main():
    rgb = np.asarray(Image.open(SRC).convert('RGB'))
    r, g, b = (rgb[..., i].astype(int) for i in range(3))
    mustard = (r > 200) & (g > 150) & (g < 215) & (b < 130)
    sofa = (r > 120) & (g < 95) & (b < 100)
    fig = (~mustard & ~sofa).astype(np.uint8) * 255
    fig = cv2.morphologyEx(fig, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    n, lab, stats, _ = cv2.connectedComponentsWithStats(fig)
    k = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
    x, y, w, h = (int(v) for v in stats[k][:4])
    mask = (lab == k).astype(np.uint8) * 255
    # fill her interior (the lips and glasses read as sofa colours)
    cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    mask = np.zeros_like(mask)
    cv2.drawContours(mask, [max(cnts, key=cv2.contourArea)], -1, 255, cv2.FILLED)

    pad = 8
    x0, y0 = max(x - pad, 0), max(y - pad, 0)
    x1, y1 = min(x + w + pad, rgb.shape[1]), min(y + h + pad, rgb.shape[0])
    crop, m = rgb[y0:y1, x0:x1], mask[y0:y1, x0:x1]

    tex_h = round(TEX_W * crop.shape[0] / crop.shape[1])
    crop = cv2.resize(crop, (TEX_W, tex_h), interpolation=cv2.INTER_AREA)
    m = cv2.resize(m, (TEX_W, tex_h), interpolation=cv2.INTER_AREA)
    m = np.where(m > 127, 255, 0).astype(np.uint8)

    # bleed: every outside pixel takes the colour of the nearest inside one
    _, labels = cv2.distanceTransformWithLabels((m == 0).astype(np.uint8), cv2.DIST_L2, 5,
                                                labelType=cv2.DIST_LABEL_PIXEL)
    lut = np.zeros((labels.max() + 1, 3), np.uint8)
    lut[labels[m > 0]] = crop[m > 0]
    bled = np.where(m[..., None] > 0, crop, lut[labels])

    Image.fromarray(np.dstack([bled, m])).save(OUT_IMG, 'WEBP', quality=88, method=6)

    # the outline sits 2px inside the mask, so the slab's edge is all her
    edge = cv2.erode(m, np.ones((5, 5), np.uint8))
    cnts, _ = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    c = max(cnts, key=cv2.contourArea)
    c = cv2.approxPolyDP(c, 1.0, True)[:, 0, :]
    if cv2.contourArea(c.astype(np.float32), oriented=True) > 0:
        c = c[::-1]  # image y runs down; flipping y below makes it counter-clockwise
    pts = [[round(px / TEX_W, 4), round(1 - py / tex_h, 4)] for px, py in c]
    OUT_JSON.write_text(json.dumps({'aspect': round(TEX_W / tex_h, 4), 'points': pts}, separators=(',', ':')))
    print(f'{OUT_IMG.name}: {TEX_W}x{tex_h}, {OUT_IMG.stat().st_size // 1024} KB; outline: {len(pts)} points')


if __name__ == '__main__':
    main()
