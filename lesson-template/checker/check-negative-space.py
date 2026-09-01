#!/usr/bin/env python3
"""Is the text block sitting on the busy half of the plate, or the quiet one?

WHY THIS EXISTS. Innes, opening a freshly built deck: "slides 5-10 with text on
wrong side - like are you even scanning for negative space?!" No. Nothing was.
check-lesson.js measures whether text FITS - overflow, scroll height - and I
added a check for ink running into the bottom chrome and another for ink off
the sides. Every one of them passes a slide whose text sits squarely on a
character's face, because that slide fits perfectly.

Six rounds of "text on the wrong side" this week were all found by eye, one
slide at a time. This is the measurement that should have existed first.

HOW IT WORKS, and why it does not need to know what a character is. A Minecraft
plate is mostly flat sky, flat ground and flat wall - low local contrast - with
the subject carrying nearly all the fine detail. So: convert the plate to
luminance, take a Sobel-style gradient magnitude, and sum it over the exact
rectangle the text occupies, then over the mirrored rectangle on the other
side. If the text half is measurably busier than the half it could have used,
the text is on the subject and the empty side is going to waste.

That is a proxy, not a face detector, and it is deliberately a blunt one:
  - it reports a RATIO, so a deck author can see how bad each one is;
  - it only convicts past a margin, because a plate with detail everywhere has
    no good side and flagging it helps nobody;
  - a slide can legitimately sit on the busy side (a plate whose subject IS the
    background), so ALLOW takes named exceptions the same way the colour gate
    does.

    python3 lesson-template/checker/check-negative-space.py [deck.html ...]
"""
import glob, os, re, sys

try:
    from PIL import Image, ImageFilter, ImageOps
except ImportError:
    sys.exit('needs Pillow:  pip install pillow')

CANVAS_W, CANVAS_H = 1280, 720
# The column a data-side block occupies: 52% of the canvas, pinned to its edge
# with the stage's 64px padding. Measured from the shipped CSS, not guessed.
PAD, COL = 64, 0.52
# Ratio at which a slide is called wrong. 1.35 means the text half carries 35%
# more fine detail than the half it left empty.
MARGIN = 1.35

ALLOW = {
    # ('deck.html', slide_number): 'why this one is right anyway'
}


def busy(img):
    """Total gradient magnitude - a stand-in for 'how much is going on here'."""
    if img.width < 4 or img.height < 4:
        return 0.0
    g = img.convert('L').filter(ImageFilter.FIND_EDGES)
    h = g.histogram()
    return sum(i * n for i, n in enumerate(h)) / float(img.width * img.height)


def rects(side):
    """The text column, and the mirror of it on the other side."""
    w = int(CANVAS_W * COL)
    if side == 'left':
        text = (PAD, 0, PAD + w, CANVAS_H)
        other = (CANVAS_W - PAD - w, 0, CANVAS_W - PAD, CANVAS_H)
    elif side == 'right':
        text = (CANVAS_W - PAD - w, 0, CANVAS_W - PAD, CANVAS_H)
        other = (PAD, 0, PAD + w, CANVAS_H)
    else:
        return None
    return text, other


def slides(src):
    body = src[src.find('<section class="slide'):src.find('const UI_I18N')]
    out = []
    n = 0
    for m in re.finditer(r'<section class="slide[^>]*>', body):
        tag = m.group(0)
        if 'data-type=' not in tag:
            continue
        n += 1
        bg = re.search(r'data-bg="([^"]+)"', tag)
        side = re.search(r'data-side="(\w+)"', tag)
        kind = re.search(r'data-type="(\w+)"', tag)
        out.append((n, bg.group(1) if bg else None,
                    side.group(1) if side else None,
                    kind.group(1) if kind else ''))
    return out


RED, GRN, DIM = '\x1b[31m%s\x1b[0m', '\x1b[32m%s\x1b[0m', '\x1b[2m%s\x1b[0m'


def main(decks):
    findings, checked, allowed = [], 0, []
    for deck in decks:
        name = os.path.basename(deck)
        root = os.path.dirname(os.path.abspath(deck))
        src = open(deck, encoding='utf-8').read()
        for n, bg, side, kind in slides(src):
            # A cover or a centred slide has no other side to move to.
            if not bg or side not in ('left', 'right'):
                continue
            path = os.path.join(root, bg)
            if not os.path.exists(path):
                continue
            try:
                im = Image.open(path).convert('RGB').resize((CANVAS_W, CANVAS_H))
            except Exception:
                continue
            checked += 1
            text_r, other_r = rects(side)
            t, o = busy(im.crop(text_r)), busy(im.crop(other_r))
            if o <= 0:
                continue
            ratio = t / o
            if ratio >= MARGIN:
                if (name, n) in ALLOW:
                    allowed.append((name, n))
                    continue
                findings.append((name, n, kind, side, ratio))

    findings.sort(key=lambda f: -f[4])
    print('\n  TEXT ON THE BUSY SIDE          %d slide(s) measured, margin %.2fx\n'
          % (checked, MARGIN))
    if not findings:
        print('    ' + GRN % 'PASS', 'every side-pinned slide sits on the quieter half\n')
        return 0
    for name, n, kind, side, ratio in findings:
        print('    ' + RED % 'FAIL',
              '%-40s slide %2d  %-8s on the %-5s  %.2fx busier than the free side'
              % (name.replace('blockcamp-', '').replace('.html', ''), n, kind, side, ratio))
    print(DIM % '\n          Flip data-side, or add it to ALLOW with a reason.')
    print('\n  %d slide(s) to look at\n' % len(findings))
    return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or sorted(glob.glob('blockcamp-*.html'))))
