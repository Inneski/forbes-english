"""Make an editorial picture whose subject breaks out of its frame.

Innes, 2026-11-08: "You don't have to confine the pictures into the squares
... a bike coming out of square. Cut out bike." and then "objects should pop
out including the scales and bikes where possible or looks good".

The editorial frame (HOUSE-STYLE §15) is 37% x 57% of the 1280x720 stage at
top 172px, or 30% wide with data-art-size="narrow". A pop picture is that
frame plus POP_UP px above it, drawn as ONE transparent image:

  * inside the frame: the plate, rounded to the frame's 22px corners;
  * above the frame: only the subject (rembg's cut-out), so the bike's
    mirrors, the rider's head or the scale's beam rise out of the frame.

It only ever rises upwards. The text column is beside the frame and the
title is above-left of it, so a pop to either side would land on words.
The plate is zoomed just enough for the subject's top to clear the frame by
POP_UP and stay centred in it; its bottom stays on the frame's bottom edge.

    py tools/pop_plate.py ComebackRide/h-scales.jpg ComebackRide/pop-h-scales.webp [--narrow]

The template draws it with data-art="pop" (the .editorial-art box grows
POP_UP upwards, no radius, a drop shadow that follows the outline).
Masks are cached in incoming/pop-masks/ (gitignored); delete one to redo it.
Run from the repo root.
"""
import argparse
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

STAGE_H = 720
FRAME_TOP = 172
FRAME_H = 0.57 * STAGE_H          # 410.4
POP_UP = 64                       # px the subject may rise above the frame
RADIUS = 22
SCALE = 2                          # render at 2x for sharp edges


def frame_w(narrow):
    return (0.30 if narrow else 0.37) * 1280


def mask_for(plate, cache):
    if os.path.exists(cache):
        return Image.open(cache).convert('L')
    from rembg import new_session, remove
    m = remove(Image.open(plate).convert('RGB'), session=new_session('isnet-general-use'), only_mask=True)
    # close small holes (chains, spokes) so the risen part is not lace
    m = m.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(5))
    m.save(cache)
    return m


def build(plate, out, narrow=False, cx=None):
    im = Image.open(plate).convert('RGB')
    pw, ph = im.size
    # the cache lives in incoming/ (gitignored): a mask is a working file,
    # not something the site serves
    cache = os.path.join('incoming', 'pop-masks', os.path.basename(os.path.splitext(out)[0]) + '.mask.png')
    os.makedirs(os.path.dirname(cache), exist_ok=True)
    m = mask_for(plate, cache)
    a = np.asarray(m) > 128
    rows, cols = np.where(a.any(1))[0], np.where(a.any(0))[0]
    top = rows[0] if len(rows) else 0
    sx0, sx1 = (cols[0], cols[-1]) if len(cols) else (0, pw)
    fw, fh = frame_w(narrow), FRAME_H
    # zoom so the subject's top sits POP_UP above the frame, plate bottom on
    # the frame's bottom; never smaller than 'cover'
    cfrac = cx if cx is not None else (sx0 + sx1) / 2 / pw
    s = max(fh / ph, fw / pw, (fh + POP_UP) / max(ph - top, 1))
    for _ in range(3):
        W, H = pw * s, ph * s
        # centre the subject (or a given centre, as a fraction of plate width)
        ox = min(0, max(fw - W, fw / 2 - cfrac * W))
        # the top that matters is the subject's top INSIDE the frame's columns:
        # a figure cropped out at the side cannot rise above the frame
        c0, c1 = int(max(0, -ox / s)), int(min(pw, (fw - ox) / s))
        r = np.where(a[:, c0:c1].any(1))[0]
        top = r[0] if len(r) else top
        s = max(fh / ph, fw / pw, min((fh + POP_UP) / max(ph - top, 1), 1.6 * max(fh / ph, fw / pw)))
    W, H = pw * s, ph * s
    ox = min(0, max(fw - W, fw / 2 - cfrac * W))
    oy = fh - H                      # plate bottom on frame bottom (frame coords)
    # output canvas: frame width x (POP_UP + frame height), frame at y=POP_UP
    cw, ch = int(round(fw * SCALE)), int(round((fh + POP_UP) * SCALE))
    big = im.resize((int(round(W * SCALE)), int(round(H * SCALE))), Image.LANCZOS)
    bm = m.resize(big.size, Image.LANCZOS)
    canvas = Image.new('RGBA', (cw, ch), (0, 0, 0, 0))
    px, py = int(round(ox * SCALE)), int(round((oy + POP_UP) * SCALE))
    layer = big.convert('RGBA')
    layer.putalpha(bm)
    # 1. subject everywhere (only the part above the frame will survive step 2's
    #    mask choice); 2. full plate inside the rounded frame
    sub = Image.new('RGBA', (cw, ch), (0, 0, 0, 0))
    sub.paste(layer, (px, py))
    full = Image.new('RGBA', (cw, ch), (0, 0, 0, 0))
    full.paste(big.convert('RGBA'), (px, py))
    fr = Image.new('L', (cw, ch), 0)
    ImageDraw.Draw(fr).rounded_rectangle([0, POP_UP * SCALE, cw - 1, ch - 1], RADIUS * SCALE, fill=255)
    canvas = Image.composite(full, sub, fr)
    canvas.save(out, 'WEBP', quality=88, method=6)
    risen = np.asarray(sub.split()[3])[:POP_UP * SCALE].max(1) > 128
    return {'zoom': round(s / max(fh / ph, fw / pw), 3), 'risen_px': int(risen.sum() / SCALE),
            'bytes': os.path.getsize(out)}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('plate')
    ap.add_argument('out')
    ap.add_argument('--narrow', action='store_true')
    ap.add_argument('--cx', type=float)
    a = ap.parse_args()
    print(build(a.plate, a.out, a.narrow, a.cx))
