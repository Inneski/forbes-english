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

    HUD bottom          viewport y  57
    marker top          viewport y 413
    panel top, worst    viewport y 502  (Arabic; English gets 581)

**Plate y and viewport y are not related by a constant.** `placeHot` slides the
picture to keep the hotspot on screen — `oy = clamp(H/2 - cy/100*dh, H-dh, 0)`
— so the crop offset is a function of the cover hotspot's cy. Moving the marker
DOWN moves the picture UP. That is how a lockup that was measured to clear the
HUD ended up with its top flourish cut off at y 0: the marker moved from cy 52
to cy 66, which took oy from -100 to its -160 limit and dragged the whole plate
up 60px with it. At 1536x864 with the cover hotspot at cy 66 the picture is
bottom-aligned, oy = -160, so

    viewport y = plate y * 1024 - 160

and the top 16% of the plate is never on screen at all. Re-derive this if the
cover hotspot moves.

The panel sits that low because the cover has no `title` of its own any more:
the lockup already reads FRANKENSTEIN: THE GREEN PROMETHEUS, so a typeset h1
underneath said it twice and ate the height the lockup wanted. Dropping it
moved the panel from 0.404 to 0.568 and bought the title half as much size
again. MAX_W, not the band, is what bounds the width now — a lockup wide
enough to fill 0.15-0.555 would put its left flourish on the Creature.

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

TOP = 0.225       # of the plate's height — viewport y 70, clear of the HUD at 57
BOTTOM = 0.548    # viewport y 401, twelve pixels above the marker at 413
MAX_W = 0.39      # a guard; the band binds first at this hotspot

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
