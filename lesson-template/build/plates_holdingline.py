# -*- coding: utf-8 -*-
"""Interim plates for Holding the Line (C1).

These are NOT the lesson's artwork. Innes is commissioning that; the brief is
`docs/ARTWORK-holding-the-line.md`. They exist so the deck can be built,
measured and read today, and so the editorial frame has something in it that
is at least the right shape and the right colours.

Two things make them safe to throw away:

  * every plate is named by a SLOT, and the builder's ART map is the only
    place a filename appears. Swapping in `hero.jpg` is one line per slot;
  * the palette here is the editorial palette's own tokens, copied from
    `deck.EDITORIAL_PALETTE`. The editorial style does NOT derive its colours
    from the hero (HOUSE-STYLE §15), so the art has to match the palette
    rather than the other way round. That is the whole reason this file can
    hard-code hexes without breaking house rule 4.

Geometry is the editorial frame's, not 16:9: `.editorial-art` is 37% x 57% of
the 1280x720 stage, so 473.6 x 410.4 css px, which is 7:6. The hero is the one
16:9 plate, because the cover alone is full-bleed.

    python lesson-template/build/plates_holdingline.py
"""
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))), 'HoldingTheLine')

CREAM = '#fff9ed'
SHELF = '#f3ede0'
LINE = '#d8dfd8'
INK = '#123a3e'
SLATE = '#1c5789'
DEEP = '#16456b'
BLUSH = '#f8dcd1'
BRICK = '#a33b12'
DIM = '#4a6265'

W, H = 1400, 1200          # 7:6 - the editorial frame
HW, HH = 2000, 1125        # 16:9 - the cover only


def svg(name, w, h, body):
    """Write one plate. No text anywhere: a labelled picture behind a
    question is an answer key, and these sit behind questions."""
    doc = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
        'width="%d" height="%d" role="img" aria-label="%s">\n'
        '  <rect width="%d" height="%d" fill="%s"/>\n%s</svg>\n'
        % (w, h, w, h, name.replace('-', ' '), w, h, CREAM, body))
    open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8',
         newline='').write(doc)


def chair(x, y, s, back, seat, legs=SLATE, tall=1.0):
    """One chair, side-on. s scales it; tall stretches the back only, which
    is the whole visual argument of the cover."""
    bh = 300 * s * tall
    return (
        '  <g>\n'
        '    <rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" rx="%.0f" fill="%s"/>\n'
        '    <rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" rx="%.0f" fill="%s"/>\n'
        '    <rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" fill="%s"/>\n'
        '    <rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" fill="%s"/>\n'
        '  </g>\n' % (
            x, y - bh, 150 * s, bh, 34 * s, back,
            x - 40 * s, y, 300 * s, 46 * s, 14 * s, seat,
            x - 20 * s, y + 46 * s, 26 * s, 210 * s, legs,
            x + 210 * s, y + 46 * s, 26 * s, 210 * s, legs))


def shadow(cx, cy, rx, ry=None):
    return ('  <ellipse cx="%.0f" cy="%.0f" rx="%.0f" ry="%.0f" fill="%s"/>\n'
            % (cx, cy, rx, ry or rx * 0.16, SHELF))


def floor(w, y):
    return ('  <rect x="0" y="%d" width="%d" height="%d" fill="%s"/>\n'
            '  <rect x="0" y="%d" width="%d" height="3" fill="%s"/>\n'
            % (y, w, 4000, SHELF, y, w, LINE))


# -- hero ---------------------------------------------------------------
# The cover lockup is left-aligned and capped at 58%, so the subject sits
# right and the left is quiet. The argument is the two chairs: same table,
# nothing like the same chair.
svg('hero', HW, HH,
    floor(HW, 880)
    + shadow(1480, 900, 260) + shadow(1090, 900, 150)
    + chair(1400, 700, 1.15, DEEP, SLATE, tall=1.55)
    + chair(1020, 720, 0.72, BLUSH, BLUSH, legs=DIM)
    + '  <rect x="900" y="640" width="720" height="18" rx="9" fill="%s"/>\n' % INK
    + '  <rect x="1240" y="598" width="60" height="42" rx="6" fill="%s"/>\n' % BRICK)

# -- remit --------------------------------------------------------------
# A taped boundary with the work neatly inside it, and one file outside.
svg('remit', W, H,
    floor(W, 980)
    + '  <rect x="210" y="300" width="800" height="600" rx="10" fill="none" '
      'stroke="%s" stroke-width="16" stroke-dasharray="54 40"/>\n' % SLATE
    + ''.join('  <rect x="%d" y="%d" width="420" height="86" rx="10" fill="%s"/>\n'
              % (400, 420 + i * 120, SLATE if i != 1 else DEEP) for i in range(3))
    + '  <g transform="rotate(-13 1150 880)">\n'
      '    <rect x="960" y="820" width="420" height="86" rx="10" fill="%s"/>\n'
      '    <rect x="960" y="820" width="90" height="86" rx="10" fill="%s"/>\n'
      '  </g>\n' % (BLUSH, BRICK))

# -- ledger -------------------------------------------------------------
# Three done, dated. One row that was never issued.
svg('ledger', W, H,
    shadow(700, 1070, 420)
    + '  <rect x="300" y="170" width="800" height="880" rx="26" fill="#ffffff" '
      'stroke="%s" stroke-width="10"/>\n' % SLATE
    + '  <rect x="600" y="130" width="200" height="80" rx="20" fill="%s"/>\n' % DEEP
    + ''.join(
        '  <rect x="380" y="%d" width="520" height="30" rx="15" fill="%s"/>\n'
        '  <path d="M960 %d l34 38 66 -86" fill="none" stroke="%s" '
        'stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>\n'
        % (330 + i * 170, SLATE, 340 + i * 170, SLATE) for i in range(3))
    + '  <rect x="380" y="840" width="520" height="30" rx="15" fill="%s"/>\n' % LINE
    + '  <rect x="952" y="820" width="76" height="76" rx="14" fill="none" '
      'stroke="%s" stroke-width="16" stroke-dasharray="26 20"/>\n' % BRICK)

# -- facts --------------------------------------------------------------
# A clock you can read, and a record you can check.
svg('facts', W, H,
    shadow(520, 1030, 330)
    + '  <rect x="470" y="120" width="100" height="56" rx="16" fill="%s"/>\n' % DEEP
    + '  <circle cx="520" cy="620" r="330" fill="none" stroke="%s" stroke-width="34"/>\n' % SLATE
    + '  <circle cx="520" cy="620" r="256" fill="#ffffff"/>\n'
    + '  <rect x="504" y="400" width="32" height="240" rx="16" fill="%s"/>\n' % INK
    + '  <rect x="520" y="604" width="190" height="32" rx="16" fill="%s"/>\n' % BRICK
    + '  <circle cx="520" cy="620" r="26" fill="%s"/>\n' % INK
    + ''.join('  <rect x="%d" y="%d" width="380" height="110" rx="14" fill="#ffffff" '
              'stroke="%s" stroke-width="8"/>\n'
              '  <rect x="%d" y="%d" width="120" height="30" rx="15" fill="%s"/>\n'
              % (930 - i * 14, 560 + i * 150, SLATE,
                 970 - i * 14, 600 + i * 150, BLUSH) for i in range(3)))

# -- door ---------------------------------------------------------------
# A room with a door, which is where this conversation belongs.
svg('door', W, H,
    floor(W, 1010)
    + '  <path d="M980 1010 L1400 1010 L1400 1200 L840 1200 Z" fill="%s"/>\n' % SHELF
    + '  <rect x="420" y="150" width="560" height="860" rx="14" fill="%s"/>\n' % DEEP
    + '  <rect x="470" y="200" width="460" height="760" rx="8" fill="%s"/>\n' % SLATE
    + '  <rect x="560" y="300" width="280" height="150" rx="10" fill="%s"/>\n' % BLUSH
    + '  <circle cx="900" cy="620" r="30" fill="%s"/>\n' % BRICK)

# -- handover -----------------------------------------------------------
# The box, the lid off, and the tag that says whose it is now.
svg('handover', W, H,
    shadow(700, 1010, 420)
    + '  <rect x="330" y="520" width="740" height="450" rx="18" fill="%s"/>\n' % SLATE
    + '  <rect x="330" y="520" width="740" height="90" rx="18" fill="%s"/>\n' % DEEP
    + ''.join('  <rect x="%d" y="%d" width="170" height="240" rx="10" fill="%s"/>\n'
              % (410 + i * 200, 320 + (i % 2) * 40,
                 BLUSH if i % 2 else '#ffffff') for i in range(3))
    + '  <path d="M1070 600 q160 40 150 220" fill="none" stroke="%s" '
      'stroke-width="12" stroke-linecap="round"/>\n' % BRICK
    + '  <rect x="1130" y="820" width="200" height="120" rx="16" fill="%s"/>\n' % BRICK
    + '  <circle cx="1220" cy="838" r="16" fill="%s"/>\n' % CREAM)

# -- keys ---------------------------------------------------------------
# Access: the card, and the thing it has to open.
svg('keys', W, H,
    shadow(660, 1030, 380)
    + '  <rect x="820" y="230" width="330" height="620" rx="26" fill="%s"/>\n' % DEEP
    + '  <circle cx="985" cy="430" r="52" fill="%s"/>\n' % BRICK
    + '  <rect x="900" y="560" width="170" height="26" rx="13" fill="%s"/>\n' % SLATE
    + '  <rect x="900" y="630" width="170" height="26" rx="13" fill="%s"/>\n' % SLATE
    + '  <g transform="rotate(-9 480 640)">\n'
      '    <rect x="250" y="440" width="470" height="300" rx="28" fill="%s" '
      'stroke="%s" stroke-width="10"/>\n'
      '    <rect x="300" y="500" width="130" height="100" rx="12" fill="%s"/>\n'
      '    <rect x="300" y="650" width="320" height="26" rx="13" fill="#ffffff"/>\n'
      '  </g>\n' % (BLUSH, SLATE, SLATE))

# -- talk ---------------------------------------------------------------
# Two chairs, the same size, turned to face each other. The meeting you
# asked for rather than the corridor you were caught in.
svg('talk', W, H,
    floor(W, 960)
    + shadow(380, 980, 210) + shadow(1030, 980, 210)
    + chair(320, 800, 0.9, SLATE, SLATE)
    + '  <g transform="translate(1400 0) scale(-1 1)">\n'
    + chair(320, 800, 0.9, DEEP, DEEP)
    + '  </g>\n'
    + '  <rect x="600" y="700" width="200" height="22" rx="11" fill="%s"/>\n' % INK
    + '  <rect x="686" y="722" width="28" height="240" fill="%s"/>\n' % INK
    + '  <rect x="640" y="640" width="120" height="60" rx="14" fill="%s"/>\n' % BLUSH)

print('wrote 8 plates to %s' % OUT)
