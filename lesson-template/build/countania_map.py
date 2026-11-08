# -*- coding: utf-8 -*-
"""The Countania chart's label layer: the third chart in Sailing the Seas
of Grammar (countable and uncountable nouns).

The picture is the painted chart with every word removed
(sailing-the-seas-countania/chart-clean.jpg: Codex's clean draft of
2026-10-04, with its two stray title dots painted out by countania_clean.py).
This SVG puts back what a picture cannot do on its own:
  * the words, as live text, so the chart reads three ways: place names,
    the bare nouns, or the nouns counted (three jobs / a piece of work)
  * a click target over each landmass, which lights the list it belongs to

Everything is in the picture's own pixels (viewBox 0 0 1536 1024).

WHERE THE NUMBERS COME FROM. The harbour coordinates are the painted dots,
blob-detected by countania_measure.py on chart-clean.jpg (never eyeballed;
two detections are not harbours: a rock at (1115,887) and a farm at
(425,748)). The landmass outlines and their paint colours are in
countania_chart.json, written by the same tool. Uncountania's outline
includes the False Cape, which joins it; the cape gets its own hotspot,
drawn on top. The captions sit where the labelled repaint
(sailing-the-seas-countania/hero.jpg) has them, so the page's two charts
agree. The label inks are worked out, not picked (regularia_map.ink_for).

THE PAIRS. Every uncountable harbour faces its countable partner at the same
latitude, with the same surname (Furniture Crag / Chair Crag): the trap is on
the east shore, and the way out is straight across the water.
"""
import json, os
from regularia_map import ratio, mix, ink_for, _poly_path, _hotspot, _rect, _cap, SERIF

W, H = 1536, 1024
HERE = os.path.dirname(os.path.abspath(__file__))
_DATA = json.load(open(os.path.join(HERE, 'countania_chart.json'), encoding='utf-8'))


def _shape_at(x, y):
    hits = [s for s in _DATA['shapes']
            if s['bbox'][0] <= x <= s['bbox'][2] and s['bbox'][1] <= y <= s['bbox'][3]]
    if not hits:
        raise SystemExit('countania_map: no landmass measured at (%d, %d)' % (x, y))
    return min(hits, key=lambda s: s['area'])


LANDS = {                      # a point on each landmass (its measured centre)
    'countania': (227, 523), 'uncountania': (1304, 536),
    'double': (768, 524), 'shallows': (767, 840),
}
SHAPE = {k: _shape_at(*p) for k, p in LANDS.items()}
PAINT = {k: s['colour'] for k, s in SHAPE.items()}
PAINT['cape'] = PAINT['uncountania']
INK = {k: ink_for(PAINT[k]) for k in PAINT}
SEA = '#A0C7D1'                # median of the open water (b > r + 18, b > 140), measured
SEA_INK = ink_for(SEA, 7.5)

# ── the harbours: (x, y) is the painted dot ───────────────────────────
# (dot, place name, bare noun, counted)
COUNTANIA = [
    ((143, 115), 'Job Harbour', 'job', 'three jobs'),
    ((290, 172), 'Fact Point', 'fact', 'two facts'),
    ((146, 240), 'Tip Head', 'tip', 'a few tips'),
    ((288, 309), 'Suitcase Sands', 'suitcase', 'two suitcases'),
    ((145, 370), 'Chair Crag', 'chair', 'six chairs'),
    ((299, 448), 'Trip Tarn', 'trip', 'many trips'),
    ((134, 498), 'Coin Cove', 'coin', 'nine coins'),
    ((287, 565), 'Song Sound', 'song', 'a few songs'),
    ((134, 607), 'Tool Ness', 'tool', 'four tools'),
    ((302, 681), 'Storm Rock', 'storm', 'two storms'),
    ((146, 737), 'Task Fell', 'task', 'three tasks'),
    ((298, 812), 'Step Ridge', 'step', 'a few steps'),
]
UNCOUNTANIA = [
    ((1379, 112), 'Work Harbour', 'work', 'a piece of work'),
    ((1248, 178), 'Information Point', 'information', 'a piece of information'),
    ((1379, 240), 'Advice Head', 'advice', 'a piece of advice'),
    ((1263, 304), 'Luggage Sands', 'luggage', 'a piece of luggage'),
    ((1410, 365), 'Furniture Crag', 'furniture', 'a piece of furniture'),
    ((1276, 431), 'Travel Tarn', 'travel', 'a lot of travel'),
    ((1413, 495), 'Money Cove', 'money', 'a sum of money'),
    ((1274, 556), 'Music Sound', 'music', 'a piece of music'),
    ((1408, 610), 'Equipment Ness', 'equipment', 'a piece of equipment'),
    ((1263, 689), 'Weather Rock', 'weather', 'bad weather'),
    ((1412, 739), 'Homework Fell', 'homework', 'a piece of homework'),
    ((1291, 821), 'Progress Ridge', 'progress', 'a bit of progress'),
]
DOUBLE = [
    ((772, 431), 'Coffee Cove', 'coffee', 'a coffee &#183; coffee'),
    ((672, 490), 'Chicken Crag', 'chicken', 'a chicken &#183; chicken'),
    ((876, 490), 'Paper Point', 'paper', 'a paper &#183; paper'),
    ((779, 541), 'Room Reach', 'room', 'a room &#183; room'),
    ((672, 585), 'Glass Gill', 'glass', 'a glass &#183; glass'),
    ((863, 586), 'Hair Head', 'hair', 'a hair &#183; hair'),
    ((769, 640), 'Time Tarn', 'time', 'a time &#183; time'),
]
assert len(COUNTANIA) == len(UNCOUNTANIA) == 12
for (c, u) in zip(COUNTANIA, UNCOUNTANIA):       # the pairs share a latitude and a surname
    assert abs(c[0][1] - u[0][1]) <= 20, 'pair off its latitude: %s / %s' % (c[1], u[1])
    assert c[1].split()[-1] == u[1].split()[-1], 'pair without a shared surname: %s / %s' % (c[1], u[1])

NAME_SIZE = 19
SMALL = 15                     # a counted form longer than this many letters is set smaller
LONG = 13


def _name(x, y, place, noun, counted, ink, paint, size=NAME_SIZE):
    """A harbour name, with a halo of its own land's paint lifted a quarter
    toward white: Countania's brick is too mid-toned for 7:1 even in black
    (6.1:1), and the painted terrain under a name is not flat."""
    halo = mix(paint, '#FFFFFF', .3)
    return ('<text class="place-name" x="%d" y="%d" text-anchor="middle" font-family="Inter,sans-serif" '
            'font-size="%s" font-weight="600" fill="%s" stroke="%s" stroke-width="4" stroke-linejoin="round" '
            'paint-order="stroke" data-size="%s" data-place="%s" data-verb="%s" data-past="%s">%s</text>'
            % (x, y - 14, size, ink, halo, size, place, noun, counted, place))


def captions():
    s = SEA_INK
    w, e, d, sh, cp = INK['countania'], INK['uncountania'], INK['double'], INK['shallows'], INK['cape']
    out = [
        # the compass banner, split either side of the needle, whose tip
        # stands at (768, 60) on this repaint
        _cap(738, 64, '&#9664; HOW MANY?', s, 17, 'end'),
        _cap(798, 64, 'HOW MUCH? &#9654;', s, 17, 'start'),
        # the ferry (the dashed line runs west, under the ship)
        _cap(770, 228, 'THE PIECE-OF FERRY RUNS WEST', s, 18, spacing='.1em'),
        _cap(770, 296, 'a piece of advice &#183; a bottle of water &#183; a slice of bread', s, 16,
             face=SERIF, weight=600, spacing='0', style='italic'),
        # Double Isle (in the water above it)
        _cap(770, 338, 'DOUBLE ISLE', d, 24, face=SERIF, spacing='.06em'),
        _cap(770, 361, 'both shores &#183; two meanings', s, 14.5, weight=600, spacing='0'),
        # the False Cape (on the cape itself)
        _cap(1066, 703, 'THE FALSE CAPE', cp, 18, face=SERIF, spacing='.06em'),
        _cap(1066, 725, 'the news is &#183; maths is', cp, 14.5, weight=600, spacing='0'),
        # the Shallows (on the sandbank)
        _cap(775, 817, 'THE SHALLOWS', sh, 20, face=SERIF, spacing='.06em'),
        _cap(775, 840, 'either shore, same word', sh, 14.5, weight=600, spacing='0'),
        _cap(775, 863, 'some &#183; any &#183; a lot of &#183; plenty of', sh, 14, weight=500, spacing='0'),
        _cap(775, 884, 'no &#183; enough &#183; more &#183; most', sh, 14, weight=500, spacing='0'),
        # the two lands
        _cap(40, 935, 'COUNTANIA', w, 40, 'start', SERIF, 700, '.04em'),
        _cap(42, 965, 'a / an &#183; many &#183; a few &#183; -s', w, 19, 'start', SERIF, 600, '0', 'italic'),
        _cap(1498, 935, 'UNCOUNTANIA', e, 40, 'end', SERIF, 700, '.04em'),
        _cap(1496, 965, 'much &#183; a little &#183; no a / an &#183; no -s', e, 19, 'end', SERIF, 600, '0', 'italic'),
    ]
    return '<g class="chart-captions">\n        ' + '\n        '.join(out) + '\n      </g>'


ARIA = {
    'countania': 'Countania, the land of countable nouns: a, an, many, a few, plural -s',
    'uncountania': 'Uncountania, the land of uncountable nouns: much, a little, no a or an, no -s',
    'double': 'Double Isle: nouns that are both, with two meanings',
    'shallows': 'The Shallows: words that work with either kind of noun',
    'cape': 'The False Cape: news and maths look plural but are uncountable',
    'ferry': 'The piece-of ferry: how to count an uncountable noun',
}
CAPE = (918, 650, 1178, 772)           # the spur's box, measured on the clean chart
FERRY = (520, 205, 1010, 310)


def chart_overlay(uid):
    spots = [_hotspot(uid, k, _poly_path(SHAPE[k]['poly']), ARIA[k]) for k in LANDS]
    spots.append(_hotspot(uid, 'cape', _rect(*CAPE), ARIA['cape']))
    spots.append(_hotspot(uid, 'ferry', _rect(*FERRY), ARIA['ferry']))
    names = []
    for key, rows in (('countania', COUNTANIA), ('uncountania', UNCOUNTANIA), ('double', DOUBLE)):
        names += [_name(x, y, p, n, c, INK[key], PAINT[key]) for (x, y), p, n, c in rows]
    return '''<svg class="sail-chart sail-chart-overlay" viewBox="0 0 %d %d">
        %s
        %s
        <g class="place-layer">
        %s
        </g>
      </svg>''' % (W, H, '\n        '.join(spots), captions(), '\n        '.join(names))


if __name__ == '__main__':
    for k in PAINT:
        print('%-12s paint %s ink %s  %.1f:1' % (k, PAINT[k], INK[k], ratio(INK[k], PAINT[k])))
    print('sea          paint %s ink %s  %.1f:1' % (SEA, SEA_INK, ratio(SEA_INK, SEA)))
