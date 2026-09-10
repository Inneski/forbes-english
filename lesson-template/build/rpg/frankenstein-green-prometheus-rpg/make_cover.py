#!/usr/bin/env python3
"""Composite the FRANKENSTEIN wordmark back onto the cover plate.

    python lesson-template/build/rpg/frankenstein-green-prometheus-rpg/make_cover.py

Round 2c told ChatGPT to deliver the cover with **no lettering**, because the
engine draws the cover title itself and glosses it into nine languages, and
lettering baked into a plate is English-only. That was right about the
subtitle and wrong about the name: Innes asked where the logo had gone, and
he was right to. *Frankenstein* is a proper noun — it does not translate, so
painting it costs no language anything.

So the plate carries the name and the panel carries the rest:

    plate   FRANKENSTEIN            painted, English-only, and that is fine
    kicker  BLOCK CAMP · GOING TO   glossed
    title   The Green Prometheus    glossed

The wordmark is lifted from the Part II export's cover, which is where Innes
saw it. It is matted out of that plate by luminance — the ice glyphs sit well
above the teal band behind them — rather than cut by hand, so this is
repeatable. `lockup.png` beside this file is that matte, kept so the composite
does not depend on the 64 MB export being present.

Re-run after any redraw of the plain plate; the result must stay under
200 KB like every other picture in the lesson.
"""
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
ART = os.path.join(REPO, 'block-camp', 'frankenstein-green-prometheus-rpg')
PLAIN = os.path.join(ART, '01_cover_plain.webp')     # as delivered, no lettering
OUT = os.path.join(ART, '01_cover.webp')

# Two things squeeze the band the wordmark can live in, and both are only
# visible in the browser, not in the plate:
#   * the HUD (points / sparks / chances, and the utilities) owns the top ~7%
#     of the VIEWPORT, and it is drawn over the picture;
#   * a 3:2 plate on a 16:9 viewport is cropped top and bottom — roughly 8% off
#     each — so plate y 0.06 lands under the HUD at viewport y 0.
# Placing it by eye on the plate put it half behind the score badges. These
# numbers are read off the rendered page instead: the wordmark clears the HUD
# and stops above the cover panel, which begins at viewport y ~0.28.
WIDTH = 0.44      # of the plate's width
TOP = 0.155       # of the plate's height


def main():
    plate = Image.open(PLAIN).convert('RGB')
    lock = Image.open(os.path.join(HERE, 'lockup.png')).convert('RGBA')
    w, h = plate.size
    tw = int(w * WIDTH)
    lock = lock.resize((tw, round(lock.height * tw / lock.width)), Image.LANCZOS)
    out = plate.copy()
    out.paste(lock, ((w - tw) // 2, int(h * TOP)), lock)
    # The delivered plate is already 190 KB, so the wordmark's icicle detail
    # cannot be added at the plate's own quality and still clear 200 KB. 66 is
    # the highest that fits, and on this dark, soft-focus sky it is invisible.
    out.save(OUT, 'WEBP', quality=66, method=6)
    print('%s — %d x %d, %d KB' % (os.path.relpath(OUT, REPO), *out.size,
                                   os.path.getsize(OUT) // 1024))


if __name__ == '__main__':
    main()
