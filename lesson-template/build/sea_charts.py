# -*- coding: utf-8 -*-
"""Three more charts for the Sailing the Seas of Grammar family, drawn the
way the Gerundia chart was first drawn: as a coded schematic that ChatGPT then
repaints as an illustrated sea chart (the brief is docs/ARTWORK-sea-charts.md).

    py lesson-template/build/sea_charts.py

writes docs/sea-charts/<name>.svg and <name>.png for each chart, and exits
non-zero if any label spills off its land or collides with another label.
That check is measured in headless Chromium, against the real glyph boxes and
the real roughened coastlines, because the whole point of these files is that
the painter can copy their layout exactly.

The charts
----------
countable   COUNTANIA and UNCOUNTANIA. Every harbour on the uncountable
            shore faces its countable partner across the strait, under the
            same surname: Furniture Crag looks across at Chair Crag. Between
            them, Double Isle (coffee / a coffee: both shores, two meanings),
            the False Cape flying an -S that is not a plural (news, maths),
            the Shallows (quantifiers that work on either shore) and the
            piece-of ferry, the one way across: a piece of advice.

hold        Innes's other idea for the same point, 2026-09-30: "two pictures
            of rooms full of one or the other with an interim space where they
            share stuff". Kept nautical as a ship in cross-section: the
            counting hold (chairs, one by one, tagged), the bulk hold (the same
            cargo as heaps: furniture) and the galley between them, where a
            coffee and coffee sit on the same table.

verbs       REGULARIA, one tidy continent with one rule and three sounds, and
            the irregular verbs as an archipelago: no single rule, but
            families, each family an island. New verbs sail west (texted); a
            few old ones are drifting there (learnt, learned).

Place names are grammar, as on the first chart. Coordinates are the same
1000x660 space sailing_map.py uses, so a label layer for a lesson page can be
calibrated to the painted dots the same way (blob-detect them, as eb491249 did).
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from sailing_map import _roughen, _path, _offscreen, W, H   # noqa: E402

OUT = os.path.join(ROOT, 'docs', 'sea-charts')

SEA_TOP, SEA_BOT = '#DEEFF6', '#B2D5E4'
LINE = '#2B4A57'
TIDE, TIDE_INK = '#22707F', '#1A5A66'
S_SAND, S_INK = '#C09A55', '#6B5320'
LILAC, LILAC_BEACH, LILAC_INK = '#AE87BE', '#E7DAEF', '#341A40'  # the island that is both, on every chart

FONTS = ('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,700'
         '&family=Inter:ital,wght@0,400;0,600;0,700;1,600&display=swap')
SANS = 'font-family="Inter,sans-serif"'
SERIF = 'font-family="Fraunces,Georgia,serif"'


# ─────────────────────────────────────────────────────────────────────
# the pieces every chart shares
# ─────────────────────────────────────────────────────────────────────

def _defs(uid):
    return '''<defs>
    <linearGradient id="%(u)s-sea" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%%" stop-color="%(t)s"/><stop offset="100%%" stop-color="%(b)s"/>
    </linearGradient>
    <marker id="%(u)s-tide" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6"
            markerHeight="6" orient="auto"><path d="M 0 1 L 9 5 L 0 9 z" fill="%(c)s"/></marker>
    <pattern id="%(u)s-sand" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(35)">
      <rect width="10" height="10" fill="#F7EBD2"/>
      <line x1="0" y1="0" x2="0" y2="10" stroke="#E3C88F" stroke-width="3.4"/>
    </pattern>
    <pattern id="%(u)s-fields" width="26" height="26" patternUnits="userSpaceOnUse">
      <path d="M 0 0 H 26 M 0 0 V 26" stroke="#5E7A3E" stroke-width=".9" opacity=".35"/>
    </pattern>
  </defs>''' % {'u': uid, 't': SEA_TOP, 'b': SEA_BOT, 'c': TIDE}


def _wave(x, y, w=28):
    return ('<path d="M %d %d q %d -5 %d 0 q %d 5 %d 0" fill="none" stroke="#84B4C9" '
            'stroke-width="1.6" stroke-linecap="round" opacity=".6"/>'
            % (x, y, w // 4, w // 2, w // 4, w // 2))


def _land(lid, coast, beach, fill, overlay=None):
    """A landmass: a pale beach band, the land, a coastline. lid is the id the
    label check looks the fill up by."""
    extra = ('<path d="%s" fill="%s"/>' % (coast, overlay)) if overlay else ''
    return ('<g class="land"><path d="%s" fill="none" stroke="%s" stroke-width="16" '
            'stroke-linejoin="round"/><path id="%s" class="fill" d="%s" fill="%s" stroke="%s" '
            'stroke-width="2.2" stroke-linejoin="round"/>%s</g>'
            % (coast, beach, lid, coast, fill, LINE, extra))


def _places(items, ink, lid, size=11):
    """Dot and name. data-land ties each label to the fill it must sit inside."""
    out = []
    for x, y, name in items:
        out.append('<circle cx="%d" cy="%d" r="2.8" fill="%s"/>'
                   '<text class="place" data-land="%s" x="%d" y="%d" text-anchor="middle" %s '
                   'font-size="%s" font-weight="600" fill="%s">%s</text>'
                   % (x, y, ink, lid, x, y - 8, SANS, size, ink, name))
    return '\n  '.join(out)


def _sea_text(x, y, text, ink, size=10.5, weight=700, spacing='.1em', serif=False,
              anchor='middle', italic=False):
    """Writing that belongs on open water: the check fails it if it lands on
    any coast."""
    return ('<text class="sea" x="%s" y="%s" text-anchor="%s" %s font-size="%s" '
            'font-weight="%s" letter-spacing="%s" fill="%s"%s>%s</text>'
            % (x, y, anchor, SERIF if serif else SANS, size, weight, spacing, ink,
               ' font-style="italic"' if italic else '', text))


def _current(uid, y, x_from, x_to, label, sub=None, label_dy=-22):
    """A dashed current with a caption above it and, optionally, examples below."""
    mid = (x_from + x_to) / 2
    s = ('<path d="M %d %d C %d %d, %d %d, %d %d" fill="none" stroke="%s" stroke-width="2.6" '
         'stroke-dasharray="10 7" stroke-linecap="round" marker-end="url(#%s-tide)" opacity=".9"/>'
         % (x_from, y, x_from - 46, y - 15, x_to + 52, y + 15, x_to, y, TIDE, uid))
    s += _sea_text(mid, y + label_dy, label, TIDE_INK)
    if sub:
        s += _sea_text(mid, y + 24, sub, TIDE_INK, size=9.5, weight=600, spacing='0',
                       italic=True)
    return '<g class="current">%s</g>' % s


def _compass(hint, cx=500, cy=92):
    return '''<g class="compass">
    <circle cx="%(x)d" cy="%(y)d" r="36" fill="#FFFFFF" opacity=".6"/>
    <circle cx="%(x)d" cy="%(y)d" r="36" fill="none" stroke="%(t)s" stroke-width="1.4"/>
    <path d="M %(x)d %(n)d L %(e)d %(m)d L %(x)d %(s)d L %(w)d %(m)d Z" fill="#D89257" stroke="#2B4A57" stroke-width="1"/>
    <path d="M %(W)d %(y)d L %(a)d %(k)d L %(E)d %(y)d L %(a)d %(j)d Z" fill="#2B4A57" opacity=".72"/>
    %(hint)s
  </g>''' % {'x': cx, 'y': cy, 'n': cy - 32, 's': cy + 32, 'm': cy - 4, 'e': cx + 7,
             'w': cx - 7, 'W': cx - 32, 'E': cx + 32, 'a': cx - 4, 'k': cy - 7,
             'j': cy + 7, 't': TIDE,
             'hint': _sea_text(cx, cy - 44, hint, TIDE_INK, spacing='.06em')}


def _ship(x, y, scale=1.0):
    return '''<g class="ship" transform="translate(%s %s) scale(%s)">
    <path d="M -28 38 L 28 38 L 19 52 L -19 52 Z" fill="#3B2A1E"/>
    <path d="M 0 0 L 0 38" stroke="#3B2A1E" stroke-width="2.4"/>
    <path d="M 2 4 L 28 33 L 2 33 Z" fill="#FBF6EC" stroke="#3B2A1E" stroke-width="1.3"/>
    <path d="M -4 10 L -27 33 L -4 33 Z" fill="#FBF6EC" stroke="#3B2A1E" stroke-width="1.3"/>
  </g>''' % (x, y, scale)


def _flag(x, y_base, y_top, text, fill, ink, point=-1):
    """A flag on a pole; point=-1 flies it west, +1 east."""
    tip = x + 46 * point
    return ('<path d="M %d %d L %d %d" stroke="%s" stroke-width="2.4"/>'
            '<path d="M %d %d L %d %d L %d %d Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
            '<text class="sea" x="%d" y="%d" text-anchor="middle" %s font-size="11.5" '
            'font-weight="700" fill="%s">%s</text>'
            % (x, y_base, x, y_top, LINE,
               x, y_top + 2, tip, y_top + 13, x, y_top + 24, fill, LINE,
               x + 20 * point, y_top + 18, SANS, ink, text))


def _shallows(uid, outline, seed, cx, top, title, sub, words):
    coast = _path(_roughen(outline, seed=seed, ratio=0.10))
    lines = ''.join(_sea_text(cx, top + 29 + 13 * i, w, S_INK, size=9, weight=400, spacing='0')
                    for i, w in enumerate(words))
    height = 38 + 13 * len(words)
    return '''<g class="shallows">
    <path d="%s" fill="url(#%s-sand)" opacity=".92"/>
    <path d="%s" fill="none" stroke="%s" stroke-width="1.8" stroke-dasharray="7 5"/>
    <rect x="%d" y="%d" width="196" height="%d" rx="9" fill="#FFFCF4" opacity=".8"/>
    %s%s%s
  </g>''' % (coast, uid, coast, S_SAND, cx - 98, top - 14, height,
             _sea_text(cx, top, title, S_INK, size=13, spacing='.05em', serif=True),
             _sea_text(cx, top + 15, sub, S_INK, size=9.5, weight=600, spacing='0'),
             lines)


def _title(x, y, name, sub, ink, anchor='start', land=None):
    """A shore's name and its rule. land=<fill id> when it is written on the
    land itself, as GERUNDIA is; otherwise it must stay on open water."""
    where = 'class="place" data-land="%s"' % land if land else 'class="sea"'
    return ('<text %s x="%d" y="%d" text-anchor="%s" %s font-size="22" font-weight="700" '
            'letter-spacing=".05em" fill="%s">%s</text>'
            '<text %s x="%d" y="%d" text-anchor="%s" %s font-size="11" font-weight="600" '
            'fill="%s">%s</text>'
            % (where, x, y, anchor, SERIF, ink, name,
               where, x + (2 if anchor == 'start' else -2), y + 19, anchor, SANS, ink, sub))


def _land_text(lid, x, y, text, ink, size=10.5, weight=700, spacing='.06em'):
    """A caption written on a landmass, checked for staying on it."""
    return ('<text class="place" data-land="%s" x="%s" y="%s" text-anchor="middle" %s '
            'font-size="%s" font-weight="%s" letter-spacing="%s" fill="%s">%s</text>'
            % (lid, x, y, SANS, size, weight, spacing, ink, text))


def _island_title(x, y, name, sub, ink, size=15.5):
    return (_sea_text(x, y, name, ink, size=size, spacing='.05em', serif=True)
            + _sea_text(x, y + 15, sub, ink, size=9.5, weight=600, spacing='0'))


def _svg(uid, title, body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">'
            '<title>%s</title>\n<style>@import url(\'%s\');</style>\n  %s\n  %s\n</svg>\n'
            % (W, H, W, H, title, FONTS.replace('&', '&amp;'), _defs(uid), body))


def _sea(uid, waves):
    return ('<rect x="0" y="0" width="%d" height="%d" fill="url(#%s-sea)"/>\n  ' % (W, H, uid)
            + '\n  '.join(_wave(x, y) for x, y in waves))


# ─────────────────────────────────────────────────────────────────────
# 1. COUNTANIA and UNCOUNTANIA
# ─────────────────────────────────────────────────────────────────────

C_LAND, C_BEACH, C_INK = '#C9745A', '#F1D6C6', '#4A1A0C'     # Countania, brick
U_LAND, U_BEACH, U_INK = '#D8B866', '#F4E6BE', '#4A3608'     # Uncountania, wheat

COUNT_OUTLINE = [
    (132, 30), (206, 58), (246, 104), (238, 156), (272, 200), (298, 252),
    (284, 300), (262, 348), (270, 398), (294, 444), (272, 492), (252, 532),
    (264, 568), (238, 598), (180, 624), (100, 644),
    (-30, 654), (-30, 18),
]
UNCOUNT_OUTLINE = [
    (884, 26), (800, 56), (752, 106), (760, 158), (730, 204), (712, 252),
    (716, 302), (732, 346), (742, 394), (730, 434), (716, 472), (712, 514),
    (724, 556), (706, 588), (746, 620), (866, 648),
    (1030, 656), (1030, 12),
]
DOUBLE_OUTLINE = [
    (500, 252), (548, 260), (582, 282), (600, 314), (596, 350), (578, 384),
    (548, 414), (508, 432), (468, 420), (436, 396), (410, 364), (402, 328),
    (412, 292), (442, 266),
]
# a spur off the uncountable shore flying an -S, because news and maths look
# plural and are not: the news IS good
COUNT_CAPE = [
    (756, 450), (708, 440), (660, 444), (620, 458), (598, 474),
    (608, 496), (648, 512), (702, 516), (750, 504),
]
COUNT_SHALLOWS = [
    (512, 502), (582, 511), (630, 528), (654, 552), (630, 580), (580, 598),
    (512, 606), (444, 598), (394, 580), (370, 552), (394, 528), (442, 511),
]

# (countable, uncountable, surname). Each pair shares a latitude and a place
# type, so the chart can be read across as well as down.
PAIRS = [
    ('Job', 'Work', 'Harbour'),
    ('Fact', 'Information', 'Point'),
    ('Tip', 'Advice', 'Head'),
    ('Suitcase', 'Luggage', 'Sands'),
    ('Chair', 'Furniture', 'Crag'),
    ('Trip', 'Travel', 'Tarn'),
    ('Coin', 'Money', 'Cove'),
    ('Song', 'Music', 'Sound'),
    ('Tool', 'Equipment', 'Ness'),
    ('Storm', 'Weather', 'Rock'),
    ('Task', 'Homework', 'Fell'),
    ('Step', 'Progress', 'Ridge'),
]
PAIR_TOP, PAIR_STEP = 90, 42
# both shores step outer, inner, outer together, so every pair sits mirror-wise
# across the strait
COUNT_X = (96, 186)
UNCOUNT_X = (906, 816)

DOUBLE_PLACES = [
    (500, 288, 'Coffee Cove'),
    (456, 324, 'Chicken Crag'),
    (552, 326, 'Paper Point'),
    (500, 354, 'Room Reach'),
    (450, 384, 'Glass Gill'),
    (550, 386, 'Hair Head'),
    (500, 416, 'Time Tarn'),
]


def _pair_places():
    west, east = [], []
    for i, (c, u, kind) in enumerate(PAIRS):
        y = PAIR_TOP + PAIR_STEP * i
        west.append((COUNT_X[i % 2], y, '%s %s' % (c, kind)))
        east.append((UNCOUNT_X[i % 2], y, '%s %s' % (u, kind)))
    return west, east


def countable_chart(uid='cu'):
    west_coast = _path(_roughen(COUNT_OUTLINE, seed=11, hold=_offscreen))
    east_coast = _path(_roughen(UNCOUNT_OUTLINE, seed=29, hold=_offscreen))
    isle = _path(_roughen(DOUBLE_OUTLINE, seed=47, ratio=0.11))
    cape = _path(_roughen(COUNT_CAPE, seed=61, levels=2, ratio=0.10))
    west, east = _pair_places()
    body = '\n  '.join([
        _sea(uid, [(344, 214), (618, 206), (342, 330), (620, 440), (352, 600),
                   (606, 628), (420, 470), (330, 140), (650, 130)]),
        _shallows(uid, COUNT_SHALLOWS, 59, 512, 540, 'THE SHALLOWS',
                  'either shore, same word',
                  ['some &#183; any &#183; a lot of &#183; plenty of',
                   'no &#183; enough &#183; more &#183; most']),
        _land(uid + '-west', west_coast, C_BEACH, C_LAND),
        _land(uid + '-east', east_coast, U_BEACH, U_LAND),
        _land(uid + '-isle', isle, LILAC_BEACH, LILAC),
        _land(uid + '-cape', cape, U_BEACH, U_LAND),
        _flag(606, 480, 408, '-S', C_LAND, '#3A1004', point=1),
        _land_text(uid + '-cape', 682, 482, 'THE FALSE CAPE', U_INK),
        _land_text(uid + '-cape', 680, 497, 'the news is &#183; maths is', U_INK, size=9,
                   weight=600, spacing='0'),
        _current(uid, 174, 618, 352, 'THE PIECE-OF FERRY RUNS WEST',
                 'a piece of advice &#183; a bottle of water &#183; a slice of bread'),
        _ship(404, 157, 0.42),
        _compass('&#9664; HOW MANY? &#183; HOW MUCH? &#9654;'),
        _ship(302, 578),
        _island_title(500, 224, 'DOUBLE ISLE', 'both shores &#183; two meanings', LILAC_INK),
        _title(56, 592, 'COUNTANIA', 'a / an &#183; many &#183; a few &#183; -s', C_INK,
               land=uid + '-west'),
        _title(946, 592, 'UNCOUNTANIA', 'much &#183; a little &#183; no a / an &#183; no -s',
               U_INK, anchor='end', land=uid + '-east'),
        _places(west, C_INK, uid + '-west'),
        _places(east, U_INK, uid + '-east'),
        _places(DOUBLE_PLACES, LILAC_INK, uid + '-isle', 10.5),
    ])
    return _svg(uid, 'Countania and Uncountania: countable and uncountable nouns', body)


# ─────────────────────────────────────────────────────────────────────
# 2. The ship's hold: the same point as two rooms and the space between
# ─────────────────────────────────────────────────────────────────────

HULL_TOP, KEEL = 166, 566
WATERLINE = 424
BULKHEADS = (392, 608)
ROWS = [268, 318, 368, 418, 468, 518]

# (countable, how many, uncountable). The bulk hold carries the same cargo as
# the counting hold; only the word changes.
CARGO = [
    ('chair', 3, 'furniture'),
    ('suitcase', 4, 'luggage'),
    ('coin', 6, 'money'),
    ('loaf', 4, 'bread'),
    ('tool', 5, 'equipment'),
    ('letter', 6, 'mail'),
]
PLURAL = {'loaf': 'loaves'}
GALLEY = ['coffee', 'chicken', 'paper', 'glass', 'cake', 'hair']

WOOD, WOOD_DARK, WOOD_INK = '#E9D3AE', '#B98B55', '#3E2A12'


def _hull():
    """Stern to the west, square; bow to the east, curved; cut open lengthways."""
    return ('M 42 %d L 960 %d C 958 300, 930 470, 850 %d L 130 %d C 70 556, 44 500, 42 %d Z'
            % (HULL_TOP, HULL_TOP - 14, KEEL, KEEL, HULL_TOP))


def _counted(x0, y, n, ink, size=18, step=24):
    """n things, each one separate and numbered: the counting hold's idiom."""
    out = []
    for i in range(n):
        x = x0 + i * step
        out.append('<rect x="%d" y="%d" width="%d" height="%d" rx="3" fill="#FFFCF4" '
                   'stroke="%s" stroke-width="1.3"/>'
                   '<text class="tag" x="%d" y="%d" text-anchor="middle" %s font-size="9" '
                   'font-weight="700" fill="%s">%d</text>'
                   % (x, y - 15, size, size, ink, x + size / 2, y - 3, SANS, ink, i + 1))
    return ''.join(out)


def _heap(xc, y, w, h, fill, ink, word, size=11.5, caps=True):
    """One pile, one word: the bulk hold's idiom."""
    return ('<path d="M %d %d C %d %d, %d %d, %d %d Z" fill="%s" stroke="%s" stroke-width="1.3"/>'
            '<text class="tag" x="%d" y="%d" text-anchor="middle" %s font-size="%s" '
            'font-weight="700" letter-spacing="%s" fill="%s">%s</text>'
            % (xc - w / 2, y, xc - w / 3, y - h * 1.3, xc + w / 3, y - h * 1.3, xc + w / 2, y,
               fill, ink, xc, y - h * .28, SANS, size, '.08em' if caps else '0', ink,
               word.upper() if caps else word))


def _mast(x, top, label, fill, ink, point, width=132):
    """A mast flying a swallowtail with the question its hold answers."""
    tip = x + width * point
    return ('<path d="M %d %d L %d %d" stroke="%s" stroke-width="4"/>'
            '<path d="M %d %d L %d %d L %d %d L %d %d L %d %d Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
            '<text class="sea" x="%d" y="%d" text-anchor="middle" %s font-size="11.5" '
            'font-weight="700" letter-spacing=".06em" fill="%s">%s</text>'
            % (x, HULL_TOP, x, top, WOOD_INK,
               x, top, tip, top, tip - 14 * point, top + 16, tip, top + 32, x, top + 32, fill, LINE,
               x + (width - 14) / 2 * point, top + 20, SANS, ink, label))


def hold_chart(uid='hd'):
    x_l, x_r = BULKHEADS
    rows = []
    for (thing, n, stuff), y in zip(CARGO, ROWS):
        plural = PLURAL.get(thing, thing + 's')
        rows.append('<text class="tag" x="88" y="%d" %s font-size="11" font-weight="600" '
                    'fill="%s">%s</text>' % (y - 2, SANS, C_INK,
                                             'a %s &#183; %d %s' % (thing, n, plural)))
        rows.append(_counted(232, y, n, C_INK))
        rows.append(_heap(748, y + 2, 200, 24, U_LAND, U_INK, stuff))
    # the galley keeps one of each: a single counted thing and a small heap
    for word, y in zip(GALLEY, ROWS):
        rows.append(_counted(404, y, 1, LILAC_INK))
        rows.append('<text class="tag" x="428" y="%d" %s font-size="11" font-weight="600" '
                    'fill="%s">a %s</text>' % (y - 2, SANS, LILAC_INK, word))
        rows.append(_heap(556, y + 2, 84, 17, LILAC, LILAC_INK, word, size=10.5, caps=False))

    band = HULL_TOP + 12, KEEL - HULL_TOP - 12
    body = '\n  '.join([
        '<clipPath id="%s-hull"><path d="%s"/></clipPath>' % (uid, _hull()),
        '<rect x="0" y="0" width="%d" height="%d" fill="url(#%s-sea)"/>' % (W, H, uid),
        '<rect x="0" y="%d" width="%d" height="%d" fill="#8FC0D6"/>' % (WATERLINE, W, H - WATERLINE),
        '\n  '.join(_wave(x, WATERLINE + dy) for x, dy in
                    [(12, 30), (930, 40), (20, 150), (940, 170), (380, 204), (600, 196)]),
        '<path id="%s-inside" class="fill" d="%s" fill="%s"/>' % (uid, _hull(), WOOD),
        # the three compartments, tinted after the three regions of the chart
        '<g clip-path="url(#%s-hull)">' % uid
        + '<rect x="0" y="%d" width="%d" height="%d" fill="%s" opacity=".34"/>'
        % (band[0], x_l, band[1], C_LAND)
        + '<rect x="%d" y="%d" width="%d" height="%d" fill="%s" opacity=".3"/>'
        % (x_l, band[0], x_r - x_l, band[1], LILAC)
        + '<rect x="%d" y="%d" width="%d" height="%d" fill="%s" opacity=".38"/>'
        % (x_r, band[0], W - x_r, band[1], U_LAND) + '</g>',
        '<path d="M %d %d L %d %d M %d %d L %d %d" stroke="%s" stroke-width="5"/>'
        % (x_l, HULL_TOP - 3, x_l, KEEL, x_r, HULL_TOP - 9, x_r, KEEL, WOOD_DARK),
        '<path d="%s" fill="none" stroke="%s" stroke-width="3"/>' % (_hull(), WOOD_INK),
        _mast(216, 40, 'HOW MANY?', C_LAND, '#3A1004', 1),
        _mast(500, 22, 'BOTH', LILAC, LILAC_INK, 1, width=90),
        _mast(786, 40, 'HOW MUCH?', U_LAND, U_INK, -1),
        _sea_text(220, HULL_TOP + 36, 'THE COUNTING HOLD', C_INK, size=15, spacing='.05em', serif=True),
        _sea_text(220, HULL_TOP + 51, 'one by one &#183; a &#183; many &#183; a few', C_INK, size=9.5,
                  weight=600, spacing='0'),
        _sea_text(500, HULL_TOP + 36, 'THE GALLEY', LILAC_INK, size=15, spacing='.05em', serif=True),
        _sea_text(500, HULL_TOP + 51, 'both &#183; two meanings', LILAC_INK, size=9.5, weight=600,
                  spacing='0'),
        _sea_text(760, HULL_TOP + 36, 'THE BULK HOLD', U_INK, size=15, spacing='.05em', serif=True),
        _sea_text(760, HULL_TOP + 51, 'in heaps &#183; much &#183; a little &#183; no -s', U_INK,
                  size=9.5, weight=600, spacing='0'),
        '\n  '.join(rows),
        _sea_text(500, 606, 'THE SAME CARGO &#183; A DIFFERENT WORD', TIDE_INK, size=12, spacing='.1em'),
        _sea_text(500, 626, 'a chair is furniture &#183; a coin is money &#183; a letter is mail',
                  TIDE_INK, size=10, weight=600, spacing='0', italic=True),
    ])
    # everything written below deck has to stay inside the hull, and the check
    # holds it to that the same way it holds a harbour name to its coast
    inside = 'class="place" data-land="%s-inside"' % uid
    body = body.replace('class="tag"', inside)
    for title in ('THE COUNTING HOLD', 'THE GALLEY', 'THE BULK HOLD', 'one by one', 'both &#183; two',
                  'in heaps'):
        i = body.index('>' + title)
        j = body.rindex('class="sea"', 0, i)
        body = body[:j] + inside + body[j + len('class="sea"'):]
    return _svg(uid, 'The ship&#39;s hold: countable and uncountable nouns', body)


# ─────────────────────────────────────────────────────────────────────
# 3. REGULARIA and the irregular archipelago
# ─────────────────────────────────────────────────────────────────────

R_LAND, R_BEACH, R_INK = '#9DB86E', '#E3EDC9', '#223A10'     # Regularia, tidy fields

# one continent, a smooth coast: the ratio is half the others', on purpose
REGULAR_OUTLINE = [
    (150, 30), (222, 62), (258, 112), (262, 170), (286, 220), (300, 272),
    (292, 326), (280, 378), (290, 430), (302, 478), (284, 526), (270, 566),
    (238, 600), (180, 626), (100, 644),
    (-30, 654), (-30, 18),
]
PROVINCES = [(30, 212, '-ED SAYS /t/'), (212, 414, '-ED SAYS /d/'), (414, 596, '-ED SAYS /&#618;d/')]
REGULAR_PLACES = [
    (98, 80, 'Stop Harbour'), (196, 110, 'Walk Ridge'),
    (96, 150, 'Watch Head'), (206, 184, 'Cook Cove'),
    (98, 262, 'Play Bay'), (214, 290, 'Study Sands'),
    (100, 332, 'Travel Tarn'), (214, 372, 'Call Crag'),
    (98, 464, 'Start Point'), (214, 494, 'Wait Moor'),
    (100, 534, 'Visit Fell'), (206, 566, 'Land&#8217;s End'),
]

# (id, outline, seed, land, beach, ink, title x, name, pattern, places); the
# title sits a fixed height above the island's own top, clear of its beach
ISLANDS = [
    ('bell', [(724, 48), (774, 52), (812, 74), (822, 108), (806, 142), (770, 162),
              (722, 166), (678, 154), (650, 128), (652, 92), (676, 62)], 71,
     '#DC9A6A', '#F5DCC6', '#4A200A', 736, 'BELL ISLAND', 'ring &#183; rang &#183; rung',
     [(698, 96, 'Sing Sound'), (774, 100, 'Drink Cove'), (700, 136, 'Swim Bay'),
      (772, 140, 'Begin Point')]),
    ('ought', [(900, 110), (948, 118), (984, 146), (992, 190), (984, 238), (958, 272),
               (916, 286), (874, 272), (848, 238), (842, 190), (858, 146)], 73,
     '#CFAE5A', '#F2E3B8', '#46340A', 918, 'OUGHT ISLAND', 'buy &#183; bought &#183; bought',
     [(916, 158, 'Bring Head'), (906, 192, 'Think Tarn'), (918, 226, 'Catch Crag'),
      (910, 260, 'Teach Ness')]),
    ('wind', [(712, 232), (760, 236), (796, 258), (806, 294), (792, 330), (756, 350),
              (708, 352), (668, 336), (648, 302), (656, 264), (680, 242)], 79,
     '#A7B8C8', '#E1E9F0', '#1E2E3E', 728, 'WINDWARD ISLE', 'blow &#183; blew &#183; blown',
     [(694, 280, 'Grow Fell'), (768, 284, 'Know Mere'), (698, 322, 'Throw Rock'),
      (762, 326, 'Fly Pike')]),
    ('keep', [(900, 338), (948, 346), (982, 372), (990, 412), (978, 452), (944, 476),
              (898, 482), (856, 466), (834, 430), (840, 390), (864, 356)], 89,
     '#C7899A', '#F0DCE2', '#431A26', 912, 'KEEP ISLAND', 'keep &#183; kept &#183; kept',
     [(904, 382, 'Sleep Sands'), (908, 412, 'Feel Moor'), (906, 442, 'Leave Harbour'),
      (910, 472, 'Build Peak')]),
    ('broke', [(716, 432), (764, 436), (800, 458), (810, 494), (796, 530), (760, 550),
               (712, 552), (670, 536), (650, 502), (658, 464), (682, 442)], 97,
     '#DDB08C', '#F6E4D2', '#482A12', 730, 'BROKEN REEF', 'break &#183; broke &#183; broken',
     [(696, 478, 'Speak Point'), (768, 482, 'Steal Cove'), (700, 520, 'Wake Head'),
      (766, 524, 'Choose Bay')]),
]
TITLE_LIFT = 31
FORKED_OUTLINE = [
    (452, 272), (496, 278), (526, 300), (534, 334), (518, 366), (484, 384),
    (440, 384), (406, 366), (392, 332), (402, 298), (424, 280),
]
FORKED_PLACES = [(462, 312, 'Lie Harbour'), (430, 346, 'Hang Head'), (492, 356, 'Shine Ness')]
VERB_SHALLOWS = [
    (470, 510), (540, 519), (588, 536), (612, 560), (588, 588), (538, 606),
    (470, 614), (402, 606), (352, 588), (328, 560), (352, 536), (400, 519),
]
# the verbs that never change, as a scatter of low rocks, and the four that
# follow no family at all, as sea stacks
STILL_ROCKS = [(628, 590, 9), (646, 600, 6), (612, 606, 7), (660, 586, 5)]
LONE_STACKS = [(830, 548, 'go'), (870, 540, 'be'), (910, 550, 'do'), (950, 542, 'see')]


def _rock(x, y, r, fill='#9A8C7A'):
    return ('<path d="M %d %d L %d %d L %d %d L %d %d Z" fill="%s" stroke="%s" stroke-width="1.2"/>'
            % (x - r, y + r * .6, x - r * .4, y - r * .8, x + r * .5, y - r * .6, x + r, y + r * .6,
               fill, LINE))


def verbs_chart(uid='rv'):
    west_coast = _path(_roughen(REGULAR_OUTLINE, seed=17, ratio=0.06, hold=_offscreen))
    forked = _path(_roughen(FORKED_OUTLINE, seed=37, ratio=0.11))
    parts = [
        _sea(uid, [(340, 216), (560, 222), (352, 420), (600, 400), (330, 620),
                   (560, 470), (820, 300), (330, 140), (610, 160)]),
        _shallows(uid, VERB_SHALLOWS, 43, 470, 548, 'THE SHALLOWS',
                  'either form, same meaning',
                  ['learnt / learned &#183; dreamt / dreamed',
                   'burnt / burned &#183; spelt / spelled']),
        _land(uid + '-west', west_coast, R_BEACH, R_LAND, overlay='url(#%s-fields)' % uid),
    ]
    # province borders: dashed county lines from the back of the land to the coast
    for y in (PROVINCES[1][0], PROVINCES[2][0]):
        parts.append('<path d="M 0 %d L 272 %d" stroke="%s" stroke-width="1.4" '
                     'stroke-dasharray="3 4" opacity=".7"/>' % (y, y + 4, R_INK))
    for top, _bottom, label in PROVINCES:
        parts.append('<text class="place" data-land="%s-west" x="20" y="%d" %s font-size="9.5" '
                     'font-weight="700" letter-spacing=".12em" font-style="italic" fill="%s" '
                     'opacity=".85">%s</text>' % (uid, top + 24, SANS, R_INK, label))
    for iid, outline, seed, land, beach, ink, tx, name, pattern, places in ISLANDS:
        ty = min(y for _x, y in outline) - TITLE_LIFT
        coast = _path(_roughen(outline, seed=seed, ratio=0.16))
        parts.append(_land('%s-%s' % (uid, iid), coast, beach, land))
        parts.append(_island_title(tx, ty, name, pattern, ink, size=12.5))
        parts.append(_places(places, ink, '%s-%s' % (uid, iid), 10))
    for x, y, r in STILL_ROCKS:
        parts.append(_rock(x, y, r))
    parts.append(_sea_text(640, 628, 'THE STILL ROCKS', '#3E3528', size=10, spacing='.08em'))
    parts.append(_sea_text(640, 641, 'cut &#183; put &#183; hit &#183; let &#183; cost: no change',
                           '#3E3528', size=9, weight=600, spacing='0'))
    for x, y, verb in LONE_STACKS:
        parts.append('<path d="M %d %d L %d %d L %d %d L %d %d Z" fill="#8A7E70" stroke="%s" '
                     'stroke-width="1.2"/>' % (x - 7, y + 10, x - 5, y - 12, x + 4, y - 14, x + 7, y + 10,
                                               LINE))
        parts.append(_sea_text(x, y + 23, verb, '#3E3528', size=10, weight=700, spacing='0'))
    parts.append(_sea_text(890, 520, 'THE LONE STACKS', '#3E3528', size=10, spacing='.08em'))
    parts += [
        _land(uid + '-forked', forked, LILAC_BEACH, LILAC),
        _island_title(462, FORKED_OUTLINE[0][1] - TITLE_LIFT, 'FORKED ISLE', 'one verb &#183; two meanings &#183; two pasts',
                      LILAC_INK, size=14),
        _places(FORKED_PLACES, LILAC_INK, uid + '-forked', 10.5),
        _current(uid, 190, 610, 330, 'NEW VERBS SAIL WEST', 'texted &#183; emailed &#183; googled'),
        _current(uid, 450, 620, 340, 'SOME OLD ONES ARE DRIFTING WEST'),
        _compass('&#9664; WALKED &#183; WENT &#9654;', cx=470),
        _ship(588, 292, 0.8),
        _title(56, 600, 'REGULARIA', 'verb + <tspan font-style="italic">-ed</tspan>', R_INK,
               land=uid + '-west'),
        _title(986, 614, 'IRREGULARIA', 'no one rule &#183; but families', '#3E3528', anchor='end'),
        _places(REGULAR_PLACES, R_INK, uid + '-west'),
    ]
    return _svg(uid, 'Regularia and the irregular archipelago: regular and irregular verbs',
                '\n  '.join(p for p in parts if p))


CHARTS = [
    ('countable-chart', countable_chart),
    ('countable-hold', hold_chart),
    ('verbs-chart', verbs_chart),
]


# ─────────────────────────────────────────────────────────────────────
# rasterise and measure
# ─────────────────────────────────────────────────────────────────────

RASTER_JS = r"""const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const jobs = JSON.parse(process.argv[2]);
  const b = await chromium.launch();
  const report = {};
  for (const [src, out] of jobs) {
    const p = await b.newPage({ viewport: { width: 1000, height: 660 }, deviceScaleFactor: 2 });
    await p.goto(new URL('file://' + path.resolve(src)).href);
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(400);
    report[path.basename(src)] = await p.evaluate(() => {
      const svg = document.querySelector('svg');
      const fonts = [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family);
      const lands = [...svg.querySelectorAll('path.fill')];
      const texts = [...svg.querySelectorAll('text')];
      const box = t => t.getBBox();
      // m grows the box: sea writing has to clear the pale beach band too
      const corners = (b, m = 0) => [[b.x - m, b.y + 2 - m], [b.x + b.width + m, b.y + 2 - m],
                                     [b.x - m, b.y + b.height - 2 + m], [b.x + b.width + m, b.y + b.height - 2 + m],
                                     [b.x + b.width / 2, b.y - m], [b.x + b.width / 2, b.y + b.height + m]];
      const inFill = (el, [x, y]) => el.isPointInFill(new DOMPoint(x, y));
      const off = [], wet = [], clash = [];
      for (const t of svg.querySelectorAll('text[data-land]')) {
        const land = document.getElementById(t.dataset.land);
        if (corners(box(t)).some(c => !inFill(land, c))) off.push(t.textContent);
      }
      for (const t of svg.querySelectorAll('text.sea')) {
        const hit = lands.find(l => corners(box(t), 7).some(c => inFill(l, c)));
        if (hit) wet.push(t.textContent + ' (on ' + hit.id + ')');
      }
      const bs = texts.map(t => [t.textContent, box(t)]);
      for (let i = 0; i < bs.length; i++) for (let j = i + 1; j < bs.length; j++) {
        const [a, A] = bs[i], [c, C] = bs[j];
        if (A.x < C.x + C.width - 1 && C.x < A.x + A.width - 1 &&
            A.y < C.y + C.height - 3 && C.y < A.y + A.height - 3) clash.push(a + ' | ' + c);
      }
      return { fonts: [...new Set(fonts)], off_land: off, on_land: wet, overlaps: clash };
    });
    await p.screenshot({ path: out });
    await p.close();
  }
  await b.close();
  console.log(JSON.stringify(report));
})();
"""


def main():
    os.makedirs(OUT, exist_ok=True)
    jobs = []
    for name, fn in CHARTS:
        svg = os.path.join(OUT, name + '.svg')
        open(svg, 'w', encoding='utf-8', newline='\n').write(fn())
        jobs.append((svg, os.path.join(OUT, name + '.png')))
    script = os.path.join(HERE, '_raster_sea_charts.js')
    open(script, 'w', encoding='utf-8', newline='\n').write(RASTER_JS)
    try:
        env = dict(os.environ, NODE_PATH=os.path.join(ROOT, 'node_modules'))
        res = subprocess.run(['node', script, json.dumps(jobs)], cwd=ROOT, env=env,
                             capture_output=True, text=True)
    finally:
        os.remove(script)
    if res.returncode:
        sys.exit(res.stderr)
    report = json.loads(res.stdout.strip().splitlines()[-1])
    bad = False
    for name, r in report.items():
        faults = [(k, r[k]) for k in ('off_land', 'on_land', 'overlaps') if r[k]]
        missing = {'Inter', 'Fraunces'} - set(r['fonts'])
        print('%-22s %s%s' % (name, 'OK' if not faults and not missing else 'FAIL',
                              '  (fonts missing: %s)' % ', '.join(sorted(missing)) if missing else ''))
        for k, v in faults:
            print('    %-9s %s' % (k, '; '.join(v)))
        bad = bad or bool(faults) or bool(missing)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
