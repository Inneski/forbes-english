# -*- coding: utf-8 -*-
"""Two more charts for the Sailing the Seas of Grammar family, painted in code
(sea_paint.py does the engraving) in the same 1000x660 space as the Gerundia
chart. They can be upgraded later in ChatGPT the way that chart was:
docs/CHATGPT-SEA-CHARTS-BRIEF.md, part 2.

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

            Innes's other picture of the same point, "rooms full of one or the
            other with an interim space where they share stuff", is not drawn
            here. He means real rooms in a ship, painted as scenes, so they
            are ChatGPT's (CHATGPT-SEA-CHARTS-BRIEF.md, part 1). A coded
            cross-section of the ship was tried and dropped on 2026-10-04:
            "not what I had in mind, I imagined real rooms".

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
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from sailing_map import _roughen, _path, _offscreen, W, H   # noqa: E402
import sea_paint as P                                        # noqa: E402

OUT = os.path.join(ROOT, 'docs', 'sea-charts')

SEA_TOP, SEA_BOT = '#D8EAE8', '#B2D1D6'
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
    <pattern id="%(u)s-sand" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(20)">
      <rect width="7" height="7" fill="#F3E4C3"/>
      <circle cx="2" cy="2" r=".75" fill="#B08A45"/><circle cx="5.5" cy="5" r=".55" fill="#B08A45"/>
    </pattern>
    <pattern id="%(u)s-fields" width="26" height="26" patternUnits="userSpaceOnUse">
      <path d="M 0 0 H 26 M 0 0 V 26" stroke="#5E7A3E" stroke-width=".9" opacity=".35"/>
    </pattern>
    %(paint)s
  </defs>''' % {'u': uid, 't': SEA_TOP, 'b': SEA_BOT, 'c': TIDE, 'paint': P.DEFS}


def _wave(x, y, w=28):
    return P.swell(x, y, w / 28)


def _land(lid, pts, beach, fill, overlay=None, kind='hills', avoid=(), marks=(), seed=1):
    """A landmass: a pale beach band, the land shaded darker toward its coast,
    engraved cliffs, its terrain (kept clear of avoid, the label boxes), its
    landmarks, and an ink coastline. lid is the id the label check looks the
    fill up by."""
    coast = _path(pts)
    extra = ('<path d="%s" fill="%s"/>' % (coast, overlay)) if overlay else ''
    ground = P.terrain(pts, kind, list(avoid) + P.landmark_boxes(marks), seed) if kind else ''
    return ('<g class="land"><path d="%s" fill="none" stroke="%s" stroke-width="10" '
            'stroke-linejoin="round" opacity=".9"/><path id="%s" class="fill" d="%s" fill="%s" '
            'filter="url(#sc-relief)"/>%s%s%s%s<path d="%s" fill="none" stroke="%s" '
            'stroke-width="1.5" stroke-linejoin="round"/></g>'
            % (coast, beach, lid, coast, fill, extra, P.hatch(pts, seed), ground,
               P.landmarks(marks), coast, P.INK))


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


def _compass(hint, cx=500, cy=94):
    return P.compass_rose(cx, cy, 34) + _sea_text(cx, cy - 56, hint, TIDE_INK, spacing='.06em')


def _ship(x, y, scale=1.0):
    return P.galleon(x, y, scale)


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
            '<title>%s</title>\n<style>@import url(\'%s\');</style>\n  %s\n  %s\n  %s\n  %s\n</svg>\n'
            % (W, H, W, H, title, FONTS.replace('&', '&amp;'), _defs(uid), P.sheet_open(), body,
               P.sheet_close()))


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


COUNT_TITLES = [
    (56, 592, 'COUNTANIA', 'a / an &#183; many &#183; a few &#183; -s', 'start'),
    (946, 592, 'UNCOUNTANIA', 'much &#183; a little &#183; no a / an &#183; no -s', 'end'),
]


def _title_boxes(x, y, name, sub, anchor):
    return [P.text_box(x, y, name, 22, anchor, k=.78), P.text_box(x, y + 19, sub, 11, anchor)]


def countable_chart(uid='cu'):
    west_pts = _roughen(COUNT_OUTLINE, seed=11, hold=_offscreen)
    east_pts = _roughen(UNCOUNT_OUTLINE, seed=29, hold=_offscreen)
    isle_pts = _roughen(DOUBLE_OUTLINE, seed=47, ratio=0.11)
    cape_pts = _roughen(COUNT_CAPE, seed=61, levels=2, ratio=0.10)
    west, east = _pair_places()
    (wx, wy, wn, ws, wa), (ex, ey, en, es, ea) = COUNT_TITLES
    body = '\n  '.join([
        _sea(uid, [(344, 214), (618, 206), (342, 330), (620, 440), (352, 600),
                   (606, 628), (420, 470), (330, 140), (650, 130)]),
        P.rings([_path(p) for p in (west_pts, east_pts, isle_pts, cape_pts)]),
        _shallows(uid, COUNT_SHALLOWS, 59, 512, 540, 'THE SHALLOWS',
                  'either shore, same word',
                  ['some &#183; any &#183; a lot of &#183; plenty of',
                   'no &#183; enough &#183; more &#183; most']),
        _land(uid + '-west', west_pts, C_BEACH, C_LAND, kind='orchard', seed=11,
              avoid=P.place_boxes(west) + _title_boxes(wx, wy, wn, ws, wa),
              marks=[('crates', 236, 452), ('crates', 226, 118)]),
        _land(uid + '-east', east_pts, U_BEACH, U_LAND, kind='wheat', seed=29,
              avoid=P.place_boxes(east) + _title_boxes(ex, ey, en, es, ea),
              marks=[('mill', 952, 140), ('mill', 962, 402)]),
        _land(uid + '-isle', isle_pts, LILAC_BEACH, LILAC, kind='hills', seed=47,
              avoid=P.place_boxes(DOUBLE_PLACES, 10.5), marks=[('lighthouse', 572, 292)]),
        _land(uid + '-cape', cape_pts, U_BEACH, U_LAND, kind='wheat', seed=61,
              avoid=[P.text_box(682, 482, 'THE FALSE CAPE', 10.5, k=.72),
                     P.text_box(680, 497, 'the news is &#183; maths is', 9)]),
        _flag(606, 480, 408, '-S', C_LAND, '#3A1004', point=1),
        _land_text(uid + '-cape', 682, 482, 'THE FALSE CAPE', U_INK),
        _land_text(uid + '-cape', 680, 497, 'the news is &#183; maths is', U_INK, size=9,
                   weight=600, spacing='0'),
        _current(uid, 174, 618, 352, 'THE PIECE-OF FERRY RUNS WEST',
                 'a piece of advice &#183; a bottle of water &#183; a slice of bread'),
        _ship(412, 160, 0.3),
        _compass('&#9664; HOW MANY? &#183; HOW MUCH? &#9654;'),
        _ship(334, 566, 0.78),
        P.serpent(600, 636, .8),
        _island_title(500, 224, 'DOUBLE ISLE', 'both shores &#183; two meanings', LILAC_INK),
        _title(wx, wy, wn, ws, C_INK, land=uid + '-west'),
        _title(ex, ey, en, es, U_INK, anchor=ea, land=uid + '-east'),
        _places(west, C_INK, uid + '-west'),
        _places(east, U_INK, uid + '-east'),
        _places(DOUBLE_PLACES, LILAC_INK, uid + '-isle', 10.5),
    ])
    return _svg(uid, 'Countania and Uncountania: countable and uncountable nouns', body)


# ─────────────────────────────────────────────────────────────────────
# 2. REGULARIA and the irregular archipelago
# ─────────────────────────────────────────────────────────────────────

R_LAND, R_BEACH, R_INK = '#9DB86E', '#E3EDC9', '#223A10'     # Regularia, tidy fields

# one continent, a smooth coast: the ratio is half the others', on purpose.
# It is the biggest land on the chart because nearly every verb lives here.
REGULAR_OUTLINE = [
    (214, 30), (292, 60), (326, 108), (330, 166), (342, 220), (350, 272),
    (340, 326), (328, 378), (338, 430), (348, 478), (330, 526), (314, 566),
    (282, 600), (210, 628), (110, 646),
    (-30, 654), (-30, 18),
]
PROVINCES = [(30, 212, '-ED SAYS /t/'), (212, 414, '-ED SAYS /d/'), (414, 596, '-ED SAYS /&#618;d/')]
# six per sound, in three staggered columns. The spelling rules ride along:
# stopped (double), liked / lived / decided (just -d), studied (y to i),
# travelled (British double l), opened (no double: the stress is on op-)
_L, _M, _R = 60, 156, 252
REGULAR_PLACES = [
    (_L, 84, 'Stop Harbour'), (_R, 84, 'Walk Ridge'), (_M, 118, 'Watch Head'),
    (_L, 152, 'Cook Cove'), (_R, 152, 'Like Mere'), (_M, 186, 'Laugh Rock'),
    (_L, 266, 'Play Bay'), (_R, 266, 'Study Sands'), (_M, 300, 'Travel Tarn'),
    (_L, 334, 'Call Crag'), (_R, 334, 'Live Ness'), (_M, 368, 'Open Sound'),
    (_L, 462, 'Start Point'), (_R, 462, 'Wait Moor'), (_M, 492, 'Visit Fell'),
    (_L, 522, 'Need Haven'), (_R, 522, 'Decide Head'), (_M, 552, 'Land&#8217;s End'),
]
REGULAR_TITLE = (56, 584, 'REGULARIA', 'verb + <tspan font-style="italic">-ed</tspan>')
REGULAR_EVERY = 'and almost every other verb'

# Each island is named after the sound its family shares, the way Ought
# Island always was. (The first names were puns, Bell Island for ring rang
# rung, and only made sense once you already knew the family.)

# (id, outline, seed, land, beach, ink, title x, name, pattern, places); the
# title sits a fixed height above the island's own top, clear of its beach
ISLANDS = [
    ('bell', [(724, 60), (774, 64), (812, 84), (822, 114), (806, 146), (770, 164),
              (722, 168), (678, 158), (650, 134), (652, 100), (676, 72)], 71,
     '#DC9A6A', '#F5DCC6', '#4A200A', 736, 'I &#183; A &#183; U ISLAND', 'ring &#183; rang &#183; rung',
     [(698, 104, 'Sing Sound'), (774, 108, 'Drink Cove'), (700, 142, 'Swim Bay'),
      (772, 146, 'Begin Point')]),
    ('ought', [(900, 110), (948, 118), (984, 146), (992, 190), (984, 238), (958, 272),
               (916, 286), (874, 272), (848, 238), (842, 190), (858, 146)], 73,
     '#CFAE5A', '#F2E3B8', '#46340A', 918, 'OUGHT ISLAND', 'buy &#183; bought &#183; bought',
     [(916, 158, 'Bring Head'), (906, 192, 'Think Tarn'), (918, 226, 'Catch Crag'),
      (910, 260, 'Teach Ness')]),
    ('wind', [(712, 232), (760, 236), (796, 258), (806, 294), (792, 330), (756, 350),
              (708, 352), (668, 336), (648, 302), (656, 264), (680, 242)], 79,
     '#A7B8C8', '#E1E9F0', '#1E2E3E', 728, '-EW ISLAND', 'blow &#183; blew &#183; blown',
     [(694, 280, 'Grow Fell'), (768, 284, 'Know Mere'), (698, 322, 'Throw Rock'),
      (762, 326, 'Fly Pike')]),
    ('keep', [(900, 338), (948, 346), (982, 372), (990, 412), (978, 452), (944, 476),
              (898, 482), (856, 466), (834, 430), (840, 390), (864, 356)], 89,
     '#C7899A', '#F0DCE2', '#431A26', 912, '-T ISLAND', 'keep &#183; kept &#183; kept',
     [(904, 382, 'Sleep Sands'), (908, 412, 'Feel Moor'), (906, 442, 'Leave Harbour'),
      (910, 472, 'Build Peak')]),
    ('broke', [(716, 432), (764, 436), (800, 458), (810, 494), (796, 530), (760, 550),
               (712, 552), (670, 536), (650, 502), (658, 464), (682, 442)], 97,
     '#DDB08C', '#F6E4D2', '#482A12', 730, '-EN ISLAND', 'speak &#183; spoke &#183; spoken',
     [(696, 478, 'Break Point'), (768, 482, 'Take Head'), (700, 520, 'Give Cove'),
      (766, 524, 'Write Bay')]),
]
TITLE_LIFT = 31
FORKED_OUTLINE = [
    (492, 272), (536, 278), (566, 300), (574, 334), (558, 366), (524, 384),
    (480, 384), (446, 366), (432, 332), (442, 298), (464, 280),
]
FORKED_PLACES = [(502, 312, 'Lie Harbour'), (470, 346, 'Hang Head'), (532, 356, 'Shine Ness')]
VERB_SHALLOWS = [
    (488, 512), (548, 521), (590, 538), (610, 562), (590, 590), (546, 606),
    (488, 614), (430, 606), (386, 590), (366, 562), (386, 538), (428, 521),
]
# the verbs that never change, as a scatter of low rocks, and the four that
# follow no family at all, as sea stacks
STILL_ROCKS = [(646, 592, 9), (664, 602, 6), (630, 608, 7), (678, 588, 5)]
LONE_STACKS = [(830, 548, 'go'), (870, 540, 'be'), (910, 550, 'do'), (950, 542, 'see')]


def _rock(x, y, r, fill='#9A8C7A'):
    return ('<path d="M %d %d L %d %d L %d %d L %d %d Z" fill="%s" stroke="%s" stroke-width="1.2"/>'
            % (x - r, y + r * .6, x - r * .4, y - r * .8, x + r * .5, y - r * .6, x + r, y + r * .6,
               fill, LINE))


# landmarks on the islands, placed clear of their four labels
ISLAND_MARKS = {'bell': [('bell', 736, 82)], 'wind': [('windmill', 732, 250)],
                'keep': [('keep', 960, 402)], 'broke': [('wreck', 732, 548)], 'ought': []}


def verbs_chart(uid='rv'):
    west_pts = _roughen(REGULAR_OUTLINE, seed=17, ratio=0.06, hold=_offscreen)
    forked_pts = _roughen(FORKED_OUTLINE, seed=37, ratio=0.11)
    island_pts = {iid: _roughen(outline, seed=seed, ratio=0.16)
                  for iid, outline, seed, *_ in ISLANDS}
    province_boxes = [P.text_box(20, top + 24, label, 9.5, 'start', k=.75) for top, _b, label in PROVINCES]
    parts = [
        _sea(uid, [(340, 216), (560, 222), (352, 420), (600, 400), (330, 620),
                   (560, 470), (820, 300), (330, 140), (610, 160)]),
        P.rings([_path(p) for p in [west_pts, forked_pts] + list(island_pts.values())]),
        _shallows(uid, VERB_SHALLOWS, 43, 488, 550, 'THE SHALLOWS',
                  'either form, same meaning',
                  ['learnt / learned &#183; dreamt / dreamed',
                   'burnt / burned &#183; spelt / spelled']),
        _land(uid + '-west', west_pts, R_BEACH, R_LAND, overlay='url(#%s-fields)' % uid,
              kind='fields', seed=17,
              avoid=P.place_boxes(REGULAR_PLACES) + province_boxes
              + _title_boxes(REGULAR_TITLE[0], REGULAR_TITLE[1], 'REGULARIA', 'verb + -ed', 'start')
              + [P.text_box(REGULAR_TITLE[0] + 2, REGULAR_TITLE[1] + 34, REGULAR_EVERY, 10, 'start')]),
    ]
    # province borders: dashed county lines from the back of the land to the coast
    for y in (PROVINCES[1][0], PROVINCES[2][0]):
        parts.append('<path d="M 0 %d L 300 %d" stroke="%s" stroke-width="1.4" '
                     'stroke-dasharray="3 4" opacity=".7"/>' % (y, y + 4, R_INK))
    for top, _bottom, label in PROVINCES:
        parts.append('<text class="place" data-land="%s-west" x="20" y="%d" %s font-size="9.5" '
                     'font-weight="700" letter-spacing=".12em" font-style="italic" fill="%s" '
                     'opacity=".85">%s</text>' % (uid, top + 24, SANS, R_INK, label))
    for iid, outline, seed, land, beach, ink, tx, name, pattern, places in ISLANDS:
        ty = min(y for _x, y in outline) - TITLE_LIFT
        parts.append(_land('%s-%s' % (uid, iid), island_pts[iid], beach, land, kind='hills',
                           seed=seed, avoid=P.place_boxes(places, 10), marks=ISLAND_MARKS[iid]))
        parts.append(_island_title(tx, ty, name, pattern, ink, size=12.5))
        parts.append(_places(places, ink, '%s-%s' % (uid, iid), 10))
    for x, y, r in STILL_ROCKS:
        parts.append(P.rock(x, y, r))
    parts.append(_sea_text(682, 628, 'THE STILL ROCKS', '#3E3528', size=10, spacing='.08em'))
    parts.append(_sea_text(682, 641, 'cut &#183; put &#183; hit &#183; let &#183; cost: no change',
                           '#3E3528', size=9, weight=600, spacing='0'))
    for x, y, verb in LONE_STACKS:
        parts.append('<path d="M %d %d L %d %d L %d %d L %d %d Z" fill="#8A7E70" stroke="%s" '
                     'stroke-width="1.2"/>' % (x - 7, y + 10, x - 5, y - 12, x + 4, y - 14, x + 7, y + 10,
                                               LINE))
        parts.append(_sea_text(x, y + 23, verb, '#3E3528', size=10, weight=700, spacing='0'))
    parts.append(_sea_text(890, 520, 'THE LONE STACKS', '#3E3528', size=10, spacing='.08em'))
    parts += [
        _land(uid + '-forked', forked_pts, LILAC_BEACH, LILAC, kind='hills', seed=37,
              avoid=P.place_boxes(FORKED_PLACES, 10.5)),
        _island_title(502, FORKED_OUTLINE[0][1] - TITLE_LIFT, 'FORKED ISLE', 'one verb &#183; two meanings &#183; two pasts',
                      LILAC_INK, size=14),
        _places(FORKED_PLACES, LILAC_INK, uid + '-forked', 10.5),
        _current(uid, 190, 616, 376, 'NEW VERBS SAIL WEST', 'texted &#183; emailed &#183; googled'),
        _current(uid, 450, 626, 386, 'SOME OLD ONES ARE DRIFTING WEST'),
        _compass('&#9664; WALKED &#183; WENT &#9654;', cx=494),
        _ship(612, 296, 0.42),
        _title(REGULAR_TITLE[0], REGULAR_TITLE[1], REGULAR_TITLE[2], REGULAR_TITLE[3], R_INK,
               land=uid + '-west'),
        _land_text(uid + '-west', REGULAR_TITLE[0] + 2, REGULAR_TITLE[1] + 34, REGULAR_EVERY, R_INK,
                   size=10, weight=600, spacing='0').replace('text-anchor="middle"',
                                                             'text-anchor="start" font-style="italic"'),
        _title(986, 614, 'IRREGULARIA', 'no one rule &#183; but families', '#3E3528', anchor='end'),
        _places(REGULAR_PLACES, R_INK, uid + '-west'),
    ]
    return _svg(uid, 'Regularia and the irregular archipelago: regular and irregular verbs',
                '\n  '.join(p for p in parts if p))


CHARTS = [
    ('countable-chart', countable_chart),
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
      // nothing may run under the ruled border (sea_paint.FRAME) or off the sheet
      const edge = texts.filter(t => { const b = box(t);
        return b.x < 11 || b.y < 11 || b.x + b.width > 989 || b.y + b.height > 649; })
        .map(t => t.textContent);
      const bs = texts.map(t => [t.textContent, box(t)]);
      for (let i = 0; i < bs.length; i++) for (let j = i + 1; j < bs.length; j++) {
        const [a, A] = bs[i], [c, C] = bs[j];
        if (A.x < C.x + C.width - 1 && C.x < A.x + A.width - 1 &&
            A.y < C.y + C.height - 3 && C.y < A.y + A.height - 3) clash.push(a + ' | ' + c);
      }
      return { fonts: [...new Set(fonts)], off_land: off, on_land: wet, overlaps: clash, off_sheet: edge };
    });
    await p.screenshot({ path: out });
    await p.close();
  }
  await b.close();
  console.log(JSON.stringify(report));
})();
"""


def plain(svg):
    """The same drawing with nothing written on it and no harbour dots: the
    composition reference Midjourney gets, since any lettering in an image
    prompt comes back as pseudo-writing."""
    svg = re.sub(r'<text\b.*?</text>', '', svg, flags=re.S)
    svg = re.sub(r'<circle cx="\d+" cy="\d+" r="2\.8"[^>]*/>', '', svg)
    return svg.replace('<title>', '<title>Unlabelled: ')


def main():
    os.makedirs(OUT, exist_ok=True)
    jobs = []
    for name, fn in CHARTS:
        src = fn()
        for suffix, body in (('', src), ('-plain', plain(src))):
            svg = os.path.join(OUT, name + suffix + '.svg')
            open(svg, 'w', encoding='utf-8', newline='\n').write(body)
            jobs.append((svg, os.path.join(OUT, name + suffix + '.png')))
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
        faults = [(k, r[k]) for k in ('off_land', 'on_land', 'overlaps', 'off_sheet') if r[k]]
        # a plain copy has no words, so it loads no fonts; that is not a fault
        missing = set() if '-plain' in name else {'Inter', 'Fraunces'} - set(r['fonts'])
        print('%-22s %s%s' % (name, 'OK' if not faults and not missing else 'FAIL',
                              '  (fonts missing: %s)' % ', '.join(sorted(missing)) if missing else ''))
        for k, v in faults:
            print('    %-9s %s' % (k, '; '.join(v)))
        bad = bad or bool(faults) or bool(missing)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
