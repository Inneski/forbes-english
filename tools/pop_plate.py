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


def cache_path(plate):
    """Masks are keyed by folder, name and byte size: keyed by name alone,
    Venezuela's hero.jpg was cut with The Comeback Ride's hero mask
    (2026-11-09), and a plate replaced under the same name reused its old
    mask. Run from the repo root; the cache is in incoming/ (gitignored)."""
    stem = os.path.basename(plate).rsplit('.', 1)[0]
    folder = os.path.basename(os.path.dirname(os.path.abspath(plate)))
    cache = os.path.join('incoming', 'pop-masks', '%s__%s__%d.mask.png' % (folder, stem, os.path.getsize(plate)))
    os.makedirs(os.path.dirname(cache), exist_ok=True)
    return cache


def subject(m, span=None, keep=0.15):
    """The subject's mask: the biggest connected piece and any piece at least
    `keep` of its size (a rider and his bike, two men and a bike); `span`
    (x0, x1 as fractions of the width) keeps only pieces centred inside it."""
    import cv2
    a = (np.asarray(m) > 128).astype(np.uint8)
    n, lab, st, cen = cv2.connectedComponentsWithStats(a, 8)
    w = a.shape[1]
    ok = [k for k in range(1, n) if span is None or span[0] * w <= cen[k][0] <= span[1] * w]
    if not ok:
        return a.astype(bool)
    big = max(st[k][4] for k in ok)
    return np.isin(lab, [k for k in ok if st[k][4] >= keep * big])


def blob(box, seed, n=240):
    """An organic blob filling `box` (x0, y0, x1, y1): an ellipse whose radius
    wobbles on three slow waves, the soft shape ENGHUB stands its figures on."""
    import math
    import random
    r = random.Random(seed)
    x0, y0, x1, y1 = box
    cx, cy, rx, ry = (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) / 2, (y1 - y0) / 2
    waves = [(k, r.uniform(0.03, 0.07), r.uniform(0, 6.28)) for k in (2, 3, 5)]
    rot = r.uniform(-0.25, 0.25)
    pts = []
    for i in range(n):
        t = 2 * math.pi * i / n
        f = 1 + sum(a * math.sin(k * t + ph) for k, a, ph in waves)
        x, y = rx * f * math.cos(t), ry * f * math.sin(t)
        pts.append((cx + x * math.cos(rot) - y * math.sin(rot), cy + x * math.sin(rot) + y * math.cos(rot)))
    return pts


def build(plate, out, narrow=False, span=None, mode='square', box=None, zone=None):
    """The subject is the star, the frame only a backdrop (Innes, 2026-11-08,
    after a 64px peek over the frame's top: "nothing pops out"; then
    "sometimes its cool to cut out the characters from the image and
    sometimes extend bits beyond the frame", with two ENGHUB pages).

    mode 'square': the subject spills over a smaller rounded square of its
                   own scene;
         'blob':   the same over an organic blob of its scene;
         'free':   the subject cut out whole, on a pale blob of colour taken
                   from the plate (its background, lifted towards cream).
    Everything stays inside the picture zone (frame width x frame height +
    POP_UP), so nothing can reach the text."""
    im = Image.open(plate).convert('RGB')
    pw, ph = im.size
    # the cache lives in incoming/ (gitignored): a mask is a working file,
    # not something the site serves
    # Keyed by folder, name and byte size: keyed by name alone, Venezuela's
    # hero.jpg was cut with The Comeback Ride's hero mask (2026-11-09), and a
    # plate replaced under the same name reused its old mask.
    m = mask_for(plate, cache_path(plate))
    a = subject(m, span)
    rows, cols = np.where(a.any(1))[0], np.where(a.any(0))[0]
    sy0, sy1, sx0, sx1 = rows[0], rows[-1], cols[0], cols[-1]
    if box:
        # the object's real extent, where the cut-out misses thin parts (the
        # scales' chains and pans): lay out on this, and the blob of scene
        # behind shows what the cut-out lost
        sx0, sy0, sx1, sy1 = box[0] * pw, box[1] * ph, box[2] * pw, box[3] * ph
    zw, zh = zone or (frame_w(narrow), FRAME_H + POP_UP)
    # the subject fills the zone: as wide as it, or as tall, whichever binds
    s = min(zw * 0.98 / (sx1 - sx0 + 1), zh * 0.97 / (sy1 - sy0 + 1))
    ox = zw / 2 - (sx0 + sx1) / 2 * s
    oy = (zh - 4) - sy1 * s                  # subject's base 4px off the bottom
    if (sy1 - sy0) * s < zh * 0.75:          # a wide, low subject: centre it
        oy = zh * 0.56 - (sy0 + sy1) / 2 * s
    # the backdrop square: inset, its foot above the subject's base
    q0x, q1x = zw * 0.13, zw * 0.87
    q0y, q1y = POP_UP + FRAME_H * 0.10, zh - 22
    # never past the plate's own edges
    q0x, q1x = max(q0x, ox), min(q1x, ox + pw * s)
    q0y, q1y = max(q0y, oy), min(q1y, oy + ph * s)
    S = SCALE
    cw, ch = int(round(zw * S)), int(round(zh * S))
    big = im.resize((int(round(pw * s * S)), int(round(ph * s * S))), Image.LANCZOS)
    am = Image.fromarray((a * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2)).resize(big.size, Image.LANCZOS)
    at = (int(round(ox * S)), int(round(oy * S)))
    full = Image.new('RGBA', (cw, ch), (0, 0, 0, 0))
    full.paste(big.convert('RGBA'), at)
    sq = Image.new('L', (cw, ch), 0)
    seed = os.path.basename(plate)
    canvas = Image.new('RGBA', (cw, ch), (0, 0, 0, 0))
    if mode == 'square':
        ImageDraw.Draw(sq).rounded_rectangle([q0x * S, q0y * S, q1x * S, q1y * S], RADIUS * S, fill=255)
        canvas.paste(full, (0, 0), sq)
    else:
        # the blob sits behind the subject's own box, a little larger
        bx0, bx1 = ox + sx0 * s, ox + sx1 * s
        by0, by1 = oy + sy0 * s, oy + sy1 * s
        padx, pady = (bx1 - bx0) * 0.06, (by1 - by0) * 0.10
        box = (max(4, bx0 - padx), max(4, by0 + (by1 - by0) * 0.12 - pady),
               min(zw - 4, bx1 + padx), min(zh - 4, by1 + pady * 0.4))
        ImageDraw.Draw(sq).polygon([(x * S, y * S) for x, y in blob(box, seed)], fill=255)
        sq = sq.filter(ImageFilter.GaussianBlur(0.8 * S))
        if mode == 'blob':
            canvas.paste(full, (0, 0), sq)
        else:
            px = np.asarray(im)[~a]
            bg = px.mean(0) if len(px) else np.array([200, 200, 200])
            tint = tuple(int(round(0.35 * c + 0.65 * v)) for c, v in zip(bg, (255, 249, 237)))
            canvas.paste(Image.new('RGBA', (cw, ch), tint + (255,)), (0, 0), sq)
    sub = big.convert('RGBA')
    sub.putalpha(am)
    layer = Image.new('RGBA', (cw, ch), (0, 0, 0, 0))
    layer.paste(sub, at)
    canvas = Image.alpha_composite(canvas, layer)
    canvas.save(out, 'WEBP', quality=88, method=6)
    return {'scale': round(s, 3), 'square': [round(q0x), round(q0y), round(q1x), round(q1y)],
            'bytes': os.path.getsize(out)}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('plate')
    ap.add_argument('out')
    ap.add_argument('--narrow', action='store_true')
    ap.add_argument('--span', type=float, nargs=2)
    ap.add_argument('--mode', default='square', choices=('square', 'blob', 'free'))
    a = ap.parse_args()
    print(build(a.plate, a.out, a.narrow, a.span, a.mode))
