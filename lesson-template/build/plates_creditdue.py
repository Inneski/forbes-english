# -*- coding: utf-8 -*-
"""Interim plates for Credit Where It's Due (C1).

NOT the lesson's artwork. The brief for the real set is
`docs/ARTWORK-credit-where-its-due.md`; these exist so the deck can be built
and measured before it arrives, and they go in the bin with this file when it
does. Same arrangement as Holding the Line, and the same two reasons it is
safe: the builder's ART map is the only place a filename appears, and the
hexes are the editorial palette's own tokens, which that style fixes rather
than derives (HOUSE-STYLE §15).

Geometry is the editorial frame's: 7:6 for the seven framed plates, 16:9 for
the hero, because the cover is the one full-bleed slide.

    python lesson-template/build/plates_creditdue.py
"""
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))), 'CreditWhereDue')

CREAM, SHELF, LINE = '#fff9ed', '#f3ede0', '#d8dfd8'
INK, SLATE, DEEP = '#123a3e', '#1c5789', '#16456b'
BLUSH, BRICK, DIM = '#f8dcd1', '#a33b12', '#4a6265'

W, H = 1400, 1200
HW, HH = 2000, 1125


def svg(name, w, h, body):
    """One plate, no text: a labelled picture behind a question is a key."""
    doc = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
           'width="%d" height="%d" role="img" aria-label="%s">\n'
           '  <rect width="%d" height="%d" fill="%s"/>\n%s</svg>\n'
           % (w, h, w, h, name, w, h, CREAM, body))
    open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8',
         newline='').write(doc)


def floor(w, y):
    return ('  <rect x="0" y="%d" width="%d" height="4000" fill="%s"/>\n'
            '  <rect x="0" y="%d" width="%d" height="3" fill="%s"/>\n'
            % (y, w, SHELF, y, w, LINE))


def shadow(cx, cy, rx):
    return ('  <ellipse cx="%d" cy="%d" rx="%d" ry="%d" fill="%s"/>\n'
            % (cx, cy, rx, round(rx * 0.15), SHELF))


def mic(x, y, s, stand=True):
    """A microphone on a stand — the room, and who is holding the floor."""
    out = ('  <rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" rx="%.0f" fill="%s"/>\n'
           % (x, y, 92 * s, 150 * s, 46 * s, DEEP))
    for i in range(4):
        out += ('  <rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" rx="%.0f" fill="%s"/>\n'
                % (x + 18 * s, y + (26 + i * 28) * s, 56 * s, 9 * s, 5 * s, CREAM))
    if stand:
        out += ('  <rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" fill="%s"/>\n'
                '  <rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" rx="%.0f" fill="%s"/>\n'
                % (x + 34 * s, y + 150 * s, 24 * s, 330 * s, SLATE,
                   x - 56 * s, y + 470 * s, 204 * s, 26 * s, 13 * s, SLATE))
    return out


# -- hero ---------------------------------------------------------------
# The cover lockup owns the left 58%, so the subject sits right: the floor,
# and one sheet of paper on the table in front of it.
svg('hero', HW, HH,
    floor(HW, 900)
    + shadow(1430, 905, 300)
    + mic(1380, 250, 1.25)
    + '  <rect x="1060" y="690" width="700" height="20" rx="8" fill="%s"/>\n' % INK
    + '  <g transform="rotate(-4 1180 660)">\n'
      '    <rect x="1090" y="596" width="180" height="96" rx="6" fill="#ffffff" '
      'stroke="%s" stroke-width="5"/>\n'
      '    <rect x="1112" y="622" width="120" height="10" rx="5" fill="%s"/>\n'
      '    <rect x="1112" y="646" width="86" height="10" rx="5" fill="%s"/>\n'
      '  </g>\n' % (SLATE, SLATE, BLUSH))

# -- room ---------------------------------------------------------------
svg('room', W, H, floor(W, 980) + shadow(700, 985, 260) + mic(650, 230, 1.55))

# -- trail --------------------------------------------------------------
# Dated slips pinned in a row: the record that beats a good memory.
svg('trail', W, H,
    '  <rect x="120" y="300" width="1160" height="6" rx="3" fill="%s"/>\n' % LINE
    + ''.join(
        '  <g transform="rotate(%d %d 560)">\n'
        '    <rect x="%d" y="330" width="230" height="330" rx="10" fill="#ffffff" '
        'stroke="%s" stroke-width="6"/>\n'
        '    <rect x="%d" y="372" width="150" height="16" rx="8" fill="%s"/>\n'
        '    <rect x="%d" y="416" width="176" height="12" rx="6" fill="%s"/>\n'
        '    <rect x="%d" y="446" width="140" height="12" rx="6" fill="%s"/>\n'
        '    <circle cx="%d" cy="330" r="15" fill="%s"/>\n'
        '  </g>\n' % ((-4, 3, -2, 5)[i], 220 + i * 300,
                      160 + i * 300, SLATE,
                      186 + i * 300, DEEP,
                      186 + i * 300, LINE,
                      186 + i * 300, LINE,
                      275 + i * 300, BRICK if i == 1 else SLATE)
        for i in range(4)))

# -- tally --------------------------------------------------------------
# Counted marks: the number that ends the argument.
svg('tally', W, H,
    shadow(700, 1040, 420)
    + '  <rect x="250" y="220" width="900" height="760" rx="20" fill="#ffffff" '
      'stroke="%s" stroke-width="10"/>\n' % SLATE
    + ''.join(
        ''.join('  <rect x="%d" y="%d" width="18" height="110" rx="9" fill="%s"/>\n'
                % (330 + g * 210 + m * 34, 330 + r * 210, SLATE)
                for m in range(4))
        + '  <rect x="%d" y="%d" width="150" height="18" rx="9" fill="%s" '
          'transform="rotate(-24 %d %d)"/>\n'
          % (322 + g * 210, 385 + r * 210, BRICK, 397 + g * 210, 394 + r * 210)
        for r in range(3) for g in range(3) if not (r == 2 and g == 2)))

# -- nameplate ----------------------------------------------------------
# A blank desk plate: the name that is missing from it is the lesson.
svg('nameplate', W, H,
    floor(W, 880) + shadow(700, 890, 380)
    + '  <path d="M330 880 L1070 880 L1010 600 L390 600 Z" fill="%s"/>\n' % DEEP
    + '  <path d="M390 600 L1010 600 L1010 586 L390 586 Z" fill="%s"/>\n' % SLATE
    + '  <rect x="470" y="660" width="460" height="24" rx="12" fill="%s"/>\n' % CREAM
    + '  <rect x="540" y="716" width="320" height="18" rx="9" fill="%s"/>\n' % BLUSH
    + '  <rect x="600" y="500" width="200" height="86" rx="10" fill="%s"/>\n' % BRICK)

# -- folder -------------------------------------------------------------
# The crisp folder, copies fanned: a timestamp you can hand round.
svg('folder', W, H,
    shadow(700, 1030, 400)
    + ''.join('  <g transform="rotate(%d 700 700)">\n'
              '    <rect x="420" y="330" width="540" height="640" rx="12" '
              'fill="#ffffff" stroke="%s" stroke-width="6"/>\n  </g>\n'
              % ((-11, -5, 2)[i], LINE) for i in range(3))
    + '  <rect x="380" y="430" width="620" height="560" rx="16" fill="%s"/>\n' % SLATE
    + '  <path d="M380 430 L660 430 L700 500 L1000 500 L1000 460 L380 460 Z" fill="%s"/>\n' % DEEP
    + '  <rect x="700" y="560" width="200" height="120" rx="12" fill="%s"/>\n' % BLUSH
    + '  <rect x="740" y="596" width="120" height="14" rx="7" fill="%s"/>\n' % BRICK)

# -- spotlight ----------------------------------------------------------
# A circle of light on an empty floor: the moment, and nobody standing in it.
svg('spotlight', W, H,
    floor(W, 700)
    + '  <path d="M640 0 L760 0 L1120 1200 L280 1200 Z" fill="%s" opacity="0.5"/>\n' % BLUSH
    + '  <ellipse cx="700" cy="980" rx="380" ry="120" fill="%s"/>\n' % CREAM
    + '  <ellipse cx="700" cy="980" rx="380" ry="120" fill="none" stroke="%s" '
      'stroke-width="8"/>\n' % BRICK
    + '  <rect x="660" y="0" width="80" height="120" rx="12" fill="%s"/>\n' % DEEP)

# -- cups ---------------------------------------------------------------
# Two cups, one pushed forward: the check-in where the record gets corrected.
svg('cups', W, H,
    floor(W, 820) + shadow(480, 830, 200) + shadow(960, 830, 200)
    + '  <rect x="180" y="770" width="1040" height="22" rx="11" fill="%s"/>\n' % INK
    + ''.join(
        '  <g>\n'
        '    <path d="M%d 560 L%d 560 L%d 760 L%d 760 Z" fill="%s"/>\n'
        '    <path d="M%d 600 q70 46 0 92" fill="none" stroke="%s" stroke-width="20"/>\n'
        '    <ellipse cx="%d" cy="560" rx="100" ry="26" fill="%s"/>\n'
        '  </g>\n' % (cx - 100, cx + 100, cx + 70, cx - 70, col,
                      cx + 96, col, cx, CREAM)
        for cx, col in ((480, SLATE), (960, BLUSH))))

print('wrote 8 plates to %s' % OUT)
