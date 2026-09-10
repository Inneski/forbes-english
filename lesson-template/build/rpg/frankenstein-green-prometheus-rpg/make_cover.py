#!/usr/bin/env python3
"""Composite Innes's title lockups onto the two cover plates.

    py lesson-template/build/rpg/frankenstein-green-prometheus-rpg/make_cover.py

Innes drew two lockups — *Part I: Ambitions* and *Part II: Consequences* — each
a complete title treatment: iced FRANKENSTEIN wordmark, THE GREEN PROMETHEUS
underneath, a compass-rose rule, the part line, and a closing flourish. Both
arrive as WebP with a real alpha channel, so there is nothing to matte: the
white behind them in a picture viewer is the viewer's own backdrop. Paste them
as they are and the flourishes keep their glow.

    part I   -> the original hero, Victor at the green apparatus   01_cover.webp
    part II  -> the Arctic, Walton's ship and the bearded stranger 01_cover_part2.webp

Round 2 had replaced the hero with the Arctic plate and the composite carried
only the bare wordmark; "Put this layer over the original hero. And part two
goes over the arctic beard boat one" puts each picture back where it belongs.

WHERE THE LOCKUP GOES is not a matter of taste, and eyeballing it on the plate
put the last one half behind the score badges. Three things decide the band,
and none of them is visible in the plate itself:

  * the HUD is drawn over the picture and owns the top of the viewport;
  * a 3:2 plate on a 16:9 viewport is cropped top and bottom, so plate y and
    viewport y are not the same number;
  * the glass panel rises to meet the lockup, and it rises furthest in the
    language whose text is longest.

So the numbers below are read off the rendered page in all ten languages, not
guessed. Measured 2026-09-10 at 1536x864, cover panel anchored `v-bottom`:

    HUD bottom          plate y 0.142
    panel top, worst    plate y 0.404   (Arabic; English gets 0.474)

The lockup is fitted to that band by HEIGHT and centred, which is why WIDTH is
derived rather than set: the two lockups have different aspect ratios, and
pinning a width would push the taller one under the HUD. Re-measure with
scratchpad/band.js if the cover panel's text ever changes length.
"""
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
ART = os.path.join(REPO, 'block-camp', 'frankenstein-green-prometheus-rpg')

TOP = 0.150       # of the plate's height — clear of the HUD at 0.142
BOTTOM = 0.392    # clear of the panel at its tallest, 0.404
MAX_W = 0.62      # never wider than this share of the plate

COVERS = [
    ('01_cover_part1_plain.webp', 'lockup_part1.webp', '01_cover.webp'),
    ('01_cover_plain.webp',       'lockup_part2.webp', '01_cover_part2.webp'),
]


def compose(plain, lockup, out):
    plate = Image.open(os.path.join(ART, plain)).convert('RGB')
    lock = Image.open(os.path.join(HERE, lockup)).convert('RGBA')
    lock = lock.crop(lock.getbbox())          # trim the transparent margin
    w, h = plate.size
    th = int(h * (BOTTOM - TOP))
    tw = round(lock.width * th / lock.height)
    if tw > w * MAX_W:                        # width-bound instead
        tw = int(w * MAX_W)
        th = round(lock.height * tw / lock.width)
    lock = lock.resize((tw, th), Image.LANCZOS)
    img = plate.copy()
    img.paste(lock, ((w - tw) // 2, int(h * TOP)), lock)
    # The plates are already close to the 200 KB the batch spec sets, and the
    # wordmark's icicle detail is expensive. Search for the quality that fits
    # rather than pinning a number, which goes stale on the next redraw.
    dst = os.path.join(ART, out)
    for q in range(88, 40, -2):
        img.save(dst, 'WEBP', quality=q, method=6)
        if os.path.getsize(dst) < 199000:
            break
    print('%-22s %d x %d lockup, %d KB at quality %d'
          % (out, tw, th, os.path.getsize(dst) // 1024, q))


def main():
    for plain, lockup, out in COVERS:
        compose(plain, lockup, out)


if __name__ == '__main__':
    main()
