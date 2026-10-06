# -*- coding: utf-8 -*-
"""Plates for Have Your Say 3 — Key Topics (writing-a-comment-south-africa-key-topics.html).

The four pictures came inside Innes's Word sheet "Key topics for your comment
in your class test" (2026-10-06): a flag heart, a giraffe, a patterned map of
Africa — three portrait flat-vector pieces on white — and a landscape
infographic of the five topics. They were run through tools/prep-artwork.py
into CommentSouthAfrica/kt-*.jpg unchanged; this script makes the plates the
deck actually shows.

**Why the white has to go.** A light deck's canvas is a mid tone (HOUSE-STYLE
§4a), never white. A white-ground hero washed behind the question slides
bleaches them, and a white panel beside a tan text column reads as a pasted
rectangle. So the three vector pieces are lifted off their white with
colour-to-alpha — the GIMP method: alpha is how far the darkest channel sits
from white, and the colour is un-mixed from white by that alpha — and set on
PAPER instead. Opaque colour is untouched, the anti-aliased edges keep their
softness, and only the ground changes.

PAPER is the --void extract-palette.py --light derived from this hero
composed on its ORIGINAL white, so the pictures sit on the page rather than on
a card. It is taken once and not fed back: run on the paper version, the
extractor moves --void a few levels, and feeding that back walks the hue
further every pass (tried 2026-10-06: #cababa, #cac0ba, #cac5ba, #cacaba…).
The builder's palette is the extractor's reading of the finished hero, which
lands within a few levels of PAPER.

The infographic is NOT lifted: its panels are pastel, and colour-to-alpha
would turn them semi-transparent and muddy. It stays a white sheet, set on
paper with a margin, which is what it is.

  kt-hero.jpg            cover + the wash behind non-panel slides: the heart
                         left, the map right, the middle left for the title
  kt-<name>-paper.jpg    portrait, for panels (a 548x720 slice is 0.76; these
                         are 0.71, so almost nothing is cropped)
  kt-<name>-wide.jpg     16:9, for dividers: the picture whole, above the
                         caption band
  kt-<name>-quiz.jpg     16:9, behind the question slides: the picture on
                         the right, the left (where the options sit) clear
  kt-overview-wide.jpg   the infographic whole, above the caption band
  LibraryCards/writing-a-comment-south-africa-key-topics.jpg   the card

Run from the repo root:  py lesson-template/build/comment_sa_kt_art.py
"""
from PIL import Image
import numpy as np
from scipy import ndimage
from scipy.spatial import ConvexHull

F = 'CommentSouthAfrica/'
PAPER = (0xca, 0xba, 0xba)
W, H = 2400, 1350


def flag_heart(a):
    """The heart's own outline, so the flag's white stripes survive the lift.

    Lifting white everywhere took the stripes out of the flag (they are the
    same white as the ground and touch it at the heart's edge), and a
    morphological closing left round bites where each stripe meets the edge.
    A heart is two convex halves either side of the line from its cleft to
    its tip, so the outline is exact as the union of two convex hulls of the
    flag's coloured and black pixels. The grey pen line is neither, so it
    stays outside and lifts like the rest of the ground."""
    from scipy.spatial import Delaunay
    mx, mn = a.max(axis=2), a.min(axis=2)
    flag = ((mx - mn) > 60 / 255) | (mx < 30 / 255)
    flag = ndimage.binary_opening(flag, np.ones((7, 7)))
    ys, xs = np.nonzero(flag)
    tip = (xs[ys.argmax()], ys.max())
    # The cleft. The pen line crosses it, so the lowest top edge is the
    # stroke's, not the heart's (it put the cleft 46px low and kept a white
    # wedge of ground). Fit a line to each lobe's inner slope, 30-90px either
    # side of that low point, and take where they meet.
    x0, x1 = xs.min(), xs.max()
    tops = {x: ys[xs == x].min() for x in range(x0, x1 + 1) if (xs == x).any()}
    low = max((x for x in tops if x0 + (x1 - x0) / 3 < x < x1 - (x1 - x0) / 3),
              key=lambda x: tops[x])
    fit = lambda r: np.polyfit(list(r), [tops[x] for x in r], 1)
    (ml, cl), (mr, cr) = fit(range(low - 90, low - 30)), fit(range(low + 30, low + 90))
    cx = (cr - cl) / (ml - mr)
    cleft = (cx, ml * cx + cl)
    # side of the cleft-tip line each pixel is on
    side = lambda X, Y: (tip[0] - cleft[0]) * (Y - cleft[1]) - (tip[1] - cleft[1]) * (X - cleft[0])
    H_, W_ = flag.shape
    gy, gx = np.mgrid[0:H_, 0:W_]
    keep = np.zeros_like(flag)
    for sel in (side(xs, ys) >= 0, side(xs, ys) <= 0):
        pts = np.c_[xs[sel], ys[sel]]
        hull = Delaunay(pts[ConvexHull(pts).vertices])
        keep |= (hull.find_simplex(np.c_[gx.ravel(), gy.ravel()]) >= 0).reshape(flag.shape)
    return keep


def lift(name):
    """RGBA, full frame: the white ground lifted, the picture untouched.

    Alpha ramps from 0 at 8 levels off white to 1 at 40, and edge pixels are
    un-mixed from white by that alpha. Plain colour-to-alpha (alpha = how far
    the darkest channel is from white) made every pale colour translucent —
    the giraffe's cream patches went pink on the paper — and a ramp keeps
    them solid while the anti-aliased edges stay soft."""
    a = np.asarray(Image.open(F + name + '.jpg').convert('RGB')).astype(np.float64) / 255
    d = (1 - a).max(axis=2)
    alpha = np.clip((d - 8 / 255) / (32 / 255), 0, 1)
    rgb = np.clip((a - (1 - d[..., None])) / np.where(d > 0, d, 1)[..., None], 0, 1)
    rgb = np.where((alpha >= 1)[..., None], a, rgb)
    if name == 'kt-heart':
        keep = flag_heart(a)
        alpha = np.where(keep, 1, alpha)
        rgb = np.where(keep[..., None], a, rgb)
    out = np.dstack([rgb, alpha]) * 255
    return Image.fromarray(out.round().astype(np.uint8), 'RGBA')


def on_paper(size):
    return Image.new('RGB', size, PAPER)


def place(canvas, art, box):
    """Fit art inside box=(x, y, w, h), centred, keeping aspect."""
    x, y, w, h = box
    art = art.crop(art.getbbox())
    s = min(w / art.width, h / art.height)
    a = art.resize((round(art.width * s), round(art.height * s)), Image.LANCZOS)
    canvas.paste(a, (x + (w - a.width) // 2, y + (h - a.height) // 2), a)


def save(im, name):
    im.save(F + name + '.jpg', 'JPEG', quality=85, optimize=True)
    print('wrote', F + name + '.jpg', im.size)


def main():
    art = {n: lift('kt-' + n) for n in ('heart', 'giraffe', 'africa')}

    # Cover. The title is set on two lines and the subtitle kept short, so
    # the text stack is ~470px of the 1280 stage (760-1640 here) and each
    # side keeps a band of its own. First pass had them under the title.
    hero = on_paper((W, H))
    place(hero, art['heart'], (40, 330, 660, 690))
    place(hero, art['africa'], (1720, 140, 640, 1070))
    save(hero, 'kt-hero')

    # Behind the question slides: one picture per stage, on the right. The
    # cover's two-sided hero put the heart behind every answer button, since
    # options sit on the left; with nothing on the left the options are clear.
    for n, a in art.items():
        c = on_paper((W, H))
        place(c, a, (1700, 150, 620, 1050))
        save(c, 'kt-%s-quiz' % n)

    # Panels: the portrait frame, with a margin all round. Placed edge to
    # edge, the map touched the panel's outer edge and the giraffe lost its
    # hooves to the cover crop.
    for n, a in art.items():
        c = on_paper(a.size)
        place(c, a, (150, 200, a.width - 300, a.height - 400))
        save(c, 'kt-%s-paper' % n)

    # Dividers: the caption band takes the bottom ~22%, so the picture sits
    # in the top 76%.
    for n, a in art.items():
        c = on_paper((W, H))
        place(c, a, (300, 80, W - 600, 940))
        save(c, 'kt-%s-wide' % n)

    # Library card, 1200x512: all three pieces side by side. The cover's
    # empty middle (it is there for the title) reads as nothing at card size.
    c = on_paper((2400, 1024))
    place(c, art['heart'], (90, 170, 700, 690))
    place(c, art['giraffe'], (900, 50, 600, 924))
    place(c, art['africa'], (1600, 50, 720, 924))
    c.resize((1200, 512), Image.LANCZOS).save(
        'LibraryCards/writing-a-comment-south-africa-key-topics.jpg',
        'JPEG', quality=85, optimize=True)
    print('wrote LibraryCards/writing-a-comment-south-africa-key-topics.jpg')

    ov = Image.open(F + 'kt-overview.jpg').convert('RGB')
    c = on_paper((W, H))
    s = 960 / ov.height
    ov = ov.resize((round(ov.width * s), 960), Image.LANCZOS)
    c.paste(ov, ((W - ov.width) // 2, 70))
    save(c, 'kt-overview-wide')


if __name__ == '__main__':
    main()
