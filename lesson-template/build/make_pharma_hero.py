# -*- coding: utf-8 -*-
"""Artwork for the pharma-sales interview deck.

Innes supplied five illustrations with the request — flat two-colour
silhouettes of two people facing each other across a desk, coral sky against
slate blue, heavy print grain. They arrived as images in the conversation and
never reached the container's filesystem, so this script reproduces that
composition and palette rather than leaving the deck with no hero at all.

It is a stand-in, and it is meant to be replaced. Everything downstream keys
off one path:

    PharmaInterview/hero.jpg

Drop the real JPEG there, re-run

    python3 lesson-template/extract-palette.py PharmaInterview/hero.jpg
    python3 lesson-template/build/build_pharma.py

and paste the emitted block over PALETTE in the builder. Nothing else in the
lesson refers to the artwork.

Three backgrounds come out, matching three of the supplied frames:

    hero.jpg    the wide window scene — two figures, sun low behind the desk
    panel.jpg   the flat interior — big coral disc, slate wall
    offer.jpg   the diagonal — coral wedge cutting across slate

Usage:  python3 lesson-template/build/make_pharma_hero.py
"""
import os
from PIL import Image, ImageDraw, ImageChops, ImageFilter

W, H = 2000, 1125
OUT = 'PharmaInterview'

# Lifted off the supplied frames by eye, then held fixed: every drawing
# function below takes its colours from here so the three backgrounds stay
# one family and the extracted palette is stable.
CORAL      = (233, 138, 115)
CORAL_DEEP = (223, 116,  92)
CORAL_PALE = (240, 165, 143)
SLATE      = (143, 168, 184)
SLATE_DEEP = (104, 132, 152)
SLATE_DARK = (62, 82, 98)
INK        = (16, 18, 24)
CREAM      = (246, 234, 216)

DESK_Y = 690          # top of the desk slab
FLOOR_Y = 962         # where the wall meets the floor


# ── helpers ────────────────────────────────────────────────────────────
def vgrad(size, top, bottom):
    """Vertical two-stop gradient. Built one row at a time on a 1px column
    and resized, which is ~600x faster than per-pixel and visually identical
    once the grain goes on."""
    w, h = size
    col = Image.new('RGB', (1, h))
    px = col.load()
    for y in range(h):
        t = y / max(1, h - 1)
        px[0, y] = tuple(int(round(top[i] + (bottom[i] - top[i]) * t)) for i in range(3))
    return col.resize((w, h), Image.BILINEAR)


def norm(box):
    """Sort a box so x0<=x1 and y0<=y1. The figures are drawn once and
    mirrored by negating an x offset, which flips every box the figure
    contains; Pillow rejects those rather than drawing them."""
    x0, y0, x1, y1 = box
    return [min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)]


def rect(d, box, **kw):
    d.rectangle(norm(box), **kw)


def rrect(d, box, **kw):
    d.rounded_rectangle(norm(box), **kw)


def ell(d, box, **kw):
    d.ellipse(norm(box), **kw)


def thick_line(d, pts, width, fill):
    """A polyline with round joints — arms and legs are drawn this way so a
    limb bends without a notch at the elbow."""
    d.line(pts, fill=fill, width=width, joint='curve')
    r = width // 2
    for x, y in pts:
        d.ellipse([x - r, y - r, x + r, y + r], fill=fill)


def grain(img, sigma=26, strength=0.30):
    """Screen-print stipple. Overlay blend, so it bites in the bright coral
    and stays quiet in the ink — which is how the supplied frames read."""
    n = Image.effect_noise((img.width, img.height), sigma).convert('RGB')
    return Image.blend(img, ImageChops.overlay(img, n), strength)


# ── the two figures ────────────────────────────────────────────────────
def man(d, cx, face=1, fill=INK):
    """Seated profile, forward lean, elbow on the desk and hand to the chin.
    `face` is +1 looking right, -1 looking left; every x is written as an
    offset from cx so the mirror is free."""
    def X(v):
        return cx + face * v

    # chair back, behind him
    rrect(d, [X(-105), 430, X(-38), 706], radius=16, fill=fill)
    # chair pedestal and base, under the desk
    rect(d, [X(-84), 700, X(-64), 856], fill=fill)
    d.polygon([(X(-134), 892), (X(-14), 892), (X(-30), 862), (X(-118), 862)], fill=fill)

    # thigh, shin, shoe
    thick_line(d, [(X(-8), 646), (X(168), 660)], 58, fill)
    thick_line(d, [(X(168), 660), (X(156), 878)], 44, fill)
    d.polygon([(X(122), 878), (X(224), 884), (X(228), 908), (X(118), 908)], fill=fill)

    # torso — front edge slopes out at the chest, back edge is the lean
    d.polygon([
        (X(8), 386), (X(88), 400), (X(104), 486), (X(96), 590),
        (X(78), 660), (X(-38), 664), (X(-46), 560), (X(-34), 452), (X(-16), 396),
    ], fill=fill)

    # neck and head
    d.polygon([(X(16), 336), (X(58), 340), (X(54), 396), (X(12), 392)], fill=fill)
    ell(d, [X(-6), 246, X(94), 356], fill=fill)
    ell(d, [X(-24), 240, X(56), 322], fill=fill)          # hair mass at the back

    # arm: shoulder → elbow planted on the desk → back up to the chin
    thick_line(d, [(X(74), 420), (X(196), 668), (X(78), 372)], 34, fill)


def woman(d, cx, face=-1, fill=INK):
    """Seated upright, hands forward on the desk, legs crossed."""
    def X(v):
        return cx + face * v

    rrect(d, [X(-108), 424, X(-40), 706], radius=16, fill=fill)
    rect(d, [X(-86), 700, X(-66), 856], fill=fill)
    d.polygon([(X(-136), 892), (X(-16), 892), (X(-32), 862), (X(-120), 862)], fill=fill)

    # crossed legs — the far one first so the near one reads on top
    thick_line(d, [(X(-6), 656), (X(150), 682)], 46, fill)
    thick_line(d, [(X(150), 682), (X(128), 872)], 34, fill)
    thick_line(d, [(X(-6), 640), (X(166), 654)], 48, fill)
    thick_line(d, [(X(166), 654), (X(196), 838)], 34, fill)
    # a heel, which is what makes the crossed pose read at this scale
    d.polygon([(X(180), 838), (X(226), 846), (X(214), 884), (X(200), 884),
               (X(196), 862), (X(176), 858)], fill=fill)

    d.polygon([
        (X(4), 390), (X(76), 398), (X(92), 480), (X(86), 574),
        (X(72), 656), (X(-40), 658), (X(-46), 556), (X(-32), 456), (X(-14), 398),
    ], fill=fill)

    d.polygon([(X(14), 340), (X(54), 344), (X(50), 398), (X(10), 394)], fill=fill)
    ell(d, [X(-4), 252, X(90), 356], fill=fill)
    ell(d, [X(-28), 246, X(48), 320], fill=fill)          # hair
    ell(d, [X(-72), 254, X(-16), 310], fill=fill)         # bun at the back

    thick_line(d, [(X(66), 424), (X(152), 606), (X(206), 668)], 32, fill)


def desk(d, x0, x1, top=DESK_Y, legs=True):
    rect(d, [x0, top, x1, top + 26], fill=INK)
    if legs:
        rect(d, [x0 + 26, top + 26, x0 + 44, FLOOR_Y], fill=INK)
        rect(d, [x1 - 44, top + 26, x1 - 26, FLOOR_Y], fill=INK)
    # the things on it: glass, mug, a closed laptop, a small monitor
    mid = (x0 + x1) // 2
    rect(d, [mid - 210, top - 54, mid - 176, top], fill=INK)
    rect(d, [mid - 108, top - 44, mid - 62, top], fill=INK)
    rect(d, [mid - 116, top - 50, mid - 54, top - 42], fill=INK)
    rect(d, [mid + 26, top - 16, mid + 190, top], fill=INK)
    rect(d, [mid + 240, top - 46, mid + 282, top], fill=INK)


# ── the three backgrounds ──────────────────────────────────────────────
def hero():
    """The window scene: coral sky over a slate skyline, sun low behind the
    desk, mullions splitting the glass into three bays."""
    img = vgrad((W, H), CORAL_PALE, CORAL_DEEP)
    d = ImageDraw.Draw(img)

    # the sun, high in the centre bay and clear of both figures — behind
    # the desk it was almost entirely occluded, which is not what the
    # supplied frames do with it
    d.ellipse([1092, 296, 1292, 496], fill=CREAM)

    # skyline behind the glass
    d.rectangle([0, 856, W, FLOOR_Y], fill=SLATE)
    for x, w, h in [(60, 150, 96), (250, 96, 150), (420, 190, 70), (700, 130, 118),
                    (900, 170, 86), (1140, 110, 140), (1310, 200, 64),
                    (1560, 140, 126), (1760, 190, 92)]:
        d.rectangle([x, 856 - h, x + w, 872], fill=SLATE_DEEP)

    # floor
    d.rectangle([0, FLOOR_Y, W, H], fill=INK)

    # mullions
    for x in (252, 984, 1748):
        d.rectangle([x, 0, x + 18, FLOOR_Y], fill=SLATE_DARK)

    man(d, 500, +1)
    woman(d, 1512, -1)
    desk(d, 336, 1700)
    return grain(img)


def panel():
    """The flat interior: a big coral disc on a slate wall, and the shadow
    the desk throws across it."""
    img = Image.new('RGB', (W, H), SLATE)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 300, H], fill=CORAL)
    d.rectangle([300, 0, 320, H], fill=CORAL_DEEP)
    d.ellipse([400, 40, 900, 540], fill=CORAL_PALE)
    d.rectangle([0, FLOOR_Y, W, H], fill=SLATE_DEEP)
    man(d, 560, +1)
    woman(d, 1560, -1)
    desk(d, 400, 1760, legs=False)
    # the cast shadow, drawn last and soft
    sh = Image.new('RGB', (W, H), (0, 0, 0))
    sd = ImageDraw.Draw(sh)
    sd.polygon([(700, 716), (1760, 716), (1900, H), (560, H)], fill=(255, 255, 255))
    sh = sh.filter(ImageFilter.GaussianBlur(18))
    img = Image.composite(ImageChops.multiply(img, Image.new('RGB', (W, H), SLATE_DEEP)), img,
                          sh.convert('L'))
    return grain(img, strength=0.26)


def offer():
    """The diagonal: a coral wedge cutting down across slate, which is the
    one of the five with the most air in it."""
    img = Image.new('RGB', (W, H), SLATE)
    d = ImageDraw.Draw(img)
    d.polygon([(300, 0), (W, 0), (W, 470), (300, 250)], fill=CORAL)
    d.rectangle([0, 700, W, H], fill=CORAL_PALE)
    d.rectangle([0, FLOOR_Y, W, H], fill=(228, 150, 128))
    for x in (250, 1500):
        d.rectangle([x, 0, x + 16, 700], fill=SLATE_DEEP)
    man(d, 620, +1)
    woman(d, 1480, -1)
    desk(d, 460, 1660)
    return grain(img, strength=0.24)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for name, fn in (('hero', hero), ('panel', panel), ('offer', offer)):
        p = os.path.join(OUT, name + '.jpg')
        fn().save(p, 'JPEG', quality=86, optimize=True)
        print('wrote %s  %d bytes' % (p, os.path.getsize(p)))
