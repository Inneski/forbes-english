#!/usr/bin/env python3
"""Every side-pinned slide of a deck on one page, with its text column shaded.

WHY THIS EXISTS. check-negative-space.py measures whether the text half is
further off the plate's colour grade than the free half, and it catches the
loud cases - it found seventeen. It cannot catch three whole classes, all of
which Innes has now found by eye on shipped decks:

  1. A BUSY BACKGROUND WITH NOBODY IN IT. The Trial's slide 7 has Steve on the
     right and a wall of bookshelves on the left. Wooden shelves and coloured
     book spines are as far off a teal grade as a person is, so the metric
     scored the two halves level (1.03) and passed a slide sitting on his face.

  2. A CHARACTER WEARING THE PLATE'S OWN GRADE. Slide 12's witch is teal on a
     teal plate - robe, hat and all, with only her face off-grade - while the
     free half holds glass bottles with warm corks. The metric said the half
     WITH the witch on it was the quieter one, at 0.84. It is not a small
     miss; it is backwards.

  3. A SMALL SUBJECT IN A BIG COLUMN. Slide 16's climber is maybe a twelfth of
     the column. A top-decile mean over the whole half averages her away.

No per-half colour statistic fixes those, because in each case the colour
statistics genuinely do not separate. What separates them is a person looking,
so this makes looking cheap: one image per deck instead of twenty.

    python3 lesson-template/checker/contact-sheet.py <deck.html> [out.png]

Shaded band = where the text goes. Ask one question per tile: is anybody
under the shading who could have been left alone?
"""
import glob, os, re, sys

try:
    from PIL import Image, ImageDraw
except ImportError:
    sys.exit('needs Pillow:  pip install pillow')

CANVAS_W, CANVAS_H = 1280, 720
PAD, COL = 64, 0.52
TILE_W = 420
COLS = 4
BAR = 22


def slides(src):
    body = src[src.find('<section class="slide'):src.find('const UI_I18N')]
    out, n = [], 0
    for m in re.finditer(r'<section class="slide[^>]*>', body):
        tag = m.group(0)
        if 'data-type=' not in tag:
            continue
        n += 1
        bg = re.search(r'data-bg="([^"]+)"', tag)
        side = re.search(r'data-side="(\w+)"', tag)
        vpos = re.search(r'data-vpos="(\w+)"', tag)
        kind = re.search(r'data-type="(\w+)"', tag)
        if not bg or not side:
            continue
        out.append((n, bg.group(1), side.group(1),
                    vpos.group(1) if vpos else 'center',
                    kind.group(1) if kind else ''))
    return out


def tile(path, side, vpos, label):
    im = Image.open(path).convert('RGB').resize((CANVAS_W, CANVAS_H))
    d = ImageDraw.Draw(im, 'RGBA')
    w = int(CANVAS_W * COL)
    x0 = PAD if side == 'left' else CANVAS_W - PAD - w
    # the band the text actually occupies, vertically as well as across
    y0, y1 = {'top': (60, 470), 'center': (150, 560), 'bottom': (230, 640)}[vpos]
    d.rectangle([x0, y0, x0 + w, y1], fill=(255, 0, 90, 70), outline=(255, 0, 90, 220), width=4)
    d.rectangle([0, 644, CANVAS_W, CANVAS_H], fill=(0, 0, 0, 130))
    h = int(TILE_W * CANVAS_H / CANVAS_W)
    im = im.resize((TILE_W, h))
    out = Image.new('RGB', (TILE_W, h + BAR), (18, 18, 20))
    out.paste(im, (0, BAR))
    ImageDraw.Draw(out).text((6, 5), label, fill=(240, 240, 240))
    return out


def main(argv):
    deck = argv[0]
    out_path = argv[1] if len(argv) > 1 else os.path.splitext(os.path.basename(deck))[0] + '-sheet.png'
    root = os.path.dirname(os.path.abspath(deck))
    src = open(deck, encoding='utf-8').read()
    tiles = []
    for n, bg, side, vpos, kind in slides(src):
        p = os.path.join(root, bg)
        if not os.path.exists(p):
            continue
        tiles.append(tile(p, side, vpos, '%2d  %-8s %-5s %-6s  %s'
                          % (n, kind, side, vpos, os.path.basename(bg))))
    if not tiles:
        sys.exit('no side-pinned slides with a plate')
    rows = (len(tiles) + COLS - 1) // COLS
    th = tiles[0].height
    sheet = Image.new('RGB', (COLS * TILE_W, rows * th), (18, 18, 20))
    for i, t in enumerate(tiles):
        sheet.paste(t, ((i % COLS) * TILE_W, (i // COLS) * th))
    sheet.save(out_path)
    print('%s  %d slide(s)' % (out_path, len(tiles)))


if __name__ == '__main__':
    if not sys.argv[1:]:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1:]))
