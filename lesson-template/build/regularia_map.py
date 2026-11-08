# -*- coding: utf-8 -*-
"""The Regularia chart's label layer: the second chart in Sailing the Seas
of Grammar (regular and irregular past forms).

The picture is the painted chart with every word removed
(sailing-the-seas-regularia/chart-clean.jpg, repainted by Codex on
2026-10-04 from sea_charts.py's coded layout, Gerundia as the style). This
SVG puts back what a picture cannot do on its own:
  * the words, as live text, so the chart reads three ways: place names,
    bare verbs, or past forms
  * a click target over each landmass, which lights the list it belongs to

Everything is in the picture's own pixels (viewBox 0 0 1536 1024).

WHERE THE NUMBERS COME FROM. The harbour coordinates are the painted dots,
blob-detected by regularia_measure.py (never eyeballed). The landmass
outlines and their paint colours are in regularia_chart.json, written by
the same tool. The captions sit where the labelled repaint
(sailing-the-seas-regularia/hero.jpg) has them, so the page's two charts
agree. The label inks are worked out, not picked: each landmass's median
paint, darkened along its own hue until it reaches 7:1 against that paint.
"""
import json, os

W, H = 1536, 1024
HERE = os.path.dirname(os.path.abspath(__file__))
_DATA = json.load(open(os.path.join(HERE, 'regularia_chart.json'), encoding='utf-8'))


# ── colour, measured ──────────────────────────────────────────────────
def _rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _hex(c):
    return '#%02X%02X%02X' % tuple(max(0, min(255, round(v))) for v in c)


def _lum(h):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= .03928 else ((v + .055) / 1.055) ** 2.4
    r, g, b = (ch(v) for v in _rgb(h))
    return .2126 * r + .7152 * g + .0722 * b


def ratio(a, b):
    la, lb = sorted((_lum(a), _lum(b)), reverse=True)
    return (la + .05) / (lb + .05)


def mix(a, b, t):
    """t of b into a."""
    return _hex(tuple(x + (y - x) * t for x, y in zip(_rgb(a), _rgb(b))))


def ink_for(paint, need=7.0):
    """The paint itself, darkened step by step toward black, until text in
    it reads at `need`:1 on that paint. Keeps the hue, so Regularia's
    words are a deep green and -T Island's a deep rose."""
    t = 0.0
    while t < 1:
        c = mix(paint, '#000000', t)
        if ratio(c, paint) >= need:
            return c
        t += .02
    return '#000000'


def _shape_at(x, y):
    """The measured landmass whose bounding box holds (x, y), smallest first
    (an island inside Regularia's box is still the island)."""
    hits = [s for s in _DATA['shapes']
            if s['bbox'][0] <= x <= s['bbox'][2] and s['bbox'][1] <= y <= s['bbox'][3]]
    if not hits:
        raise SystemExit('regularia_map: no landmass measured at (%d, %d)' % (x, y))
    return min(hits, key=lambda s: s['area'])


LANDS = {                      # a point on each landmass (its measured centre)
    'regularia': (256, 504), 'forked': (751, 508), 'shallows': (754, 834),
    'iau': (1113, 162), 'ought': (1392, 298), 'ew': (1112, 440),
    't': (1393, 632), 'en': (1125, 724),
}
SHAPE = {k: _shape_at(*p) for k, p in LANDS.items()}
PAINT = {k: s['colour'] for k, s in SHAPE.items()}
INK = {k: ink_for(PAINT[k]) for k in PAINT}
SEA = '#9DC9D6'                # median of the open water (b > r + 18, b > 140), measured
SEA_INK = ink_for(SEA, 7.5)

# ── the harbours: (x, y) is the painted dot ───────────────────────────
# (dot, place name, bare verb, past form[s])
REGULARIA = [
    # -ED says /t/
    ((141, 128), 'Stop Harbour', 'stop', 'stopped'),
    ((365, 128), 'Walk Ridge', 'walk', 'walked'),
    ((265, 184), 'Watch Head', 'watch', 'watched'),
    ((98, 231), 'Cook Cove', 'cook', 'cooked'),
    ((381, 248), 'Like Mere', 'like', 'liked'),
    ((262, 301), 'Laugh Rock', 'laugh', 'laughed'),
    # -ED says /d/
    ((110, 398), 'Play Bay', 'play', 'played'),
    ((390, 408), 'Study Sands', 'study', 'studied'),
    ((285, 459), 'Travel Tarn', 'travel', 'travelled'),
    ((144, 500), 'Call Crag', 'call', 'called'),
    ((427, 503), 'Live Ness', 'live', 'lived'),
    ((294, 547), 'Open Sound', 'open', 'opened'),
    # -ED says /ɪd/
    ((113, 652), 'Start Point', 'start', 'started'),
    ((382, 657), 'Wait Moor', 'wait', 'waited'),
    ((232, 718), 'Visit Fell', 'visit', 'visited'),
    ((393, 756), 'Decide Head', 'decide', 'decided'),
    ((116, 778), 'Need Haven', 'need', 'needed'),
    ((266, 820), 'Land&#8217;s End', 'land', 'landed'),
]
ISLANDS = {
    'iau': [((1056, 142), 'Sing Sound', 'sing', 'sang &#183; sung'),
            ((1191, 152), 'Drink Cove', 'drink', 'drank &#183; drunk'),
            ((1056, 201), 'Swim Bay', 'swim', 'swam &#183; swum'),
            ((1177, 210), 'Begin Point', 'begin', 'began &#183; begun')],
    'ought': [((1417, 212), 'Bring Head', 'bring', 'brought'),
              ((1402, 287), 'Think Tarn', 'think', 'thought'),
              ((1364, 353), 'Catch Crag', 'catch', 'caught'),
              ((1423, 410), 'Teach Ness', 'teach', 'taught')],
    'ew': [((1038, 414), 'Grow Fell', 'grow', 'grew &#183; grown'),
           ((1176, 409), 'Know Mere', 'know', 'knew &#183; known'),
           ((1061, 472), 'Throw Rock', 'throw', 'threw &#183; thrown'),
           ((1178, 488), 'Fly Pike', 'fly', 'flew &#183; flown')],
    't': [((1382, 576), 'Sleep Sands', 'sleep', 'slept'),
          ((1410, 622), 'Feel Moor', 'feel', 'felt'),
          ((1364, 669), 'Leave Harbour', 'leave', 'left'),
          ((1433, 715), 'Build Peak', 'build', 'built')],
    'en': [((1066, 698), 'Break Point', 'break', 'broke &#183; broken'),
           ((1184, 698), 'Take Head', 'take', 'took &#183; taken'),
           ((1083, 752), 'Give Cove', 'give', 'gave &#183; given'),
           ((1194, 762), 'Write Bay', 'write', 'wrote &#183; written')],
    'forked': [((766, 436), 'Lie Harbour', 'lie', 'lied &#183; lay'),
               ((692, 504), 'Hang Head', 'hang', 'hanged &#183; hung'),
               ((828, 527), 'Shine Ness', 'shine', 'shined &#183; shone')],
}
STILL_ROCKS = [(1090, 'cut'), (1150, 'put')]     # (only the caption names them)
# the stacks stand 60px apart, too close for 'went · gone' on one line, so
# their past form is two lines (the page script splits at '|')
LONE_STACKS = [(1290, 'go', 'went|gone'), (1350, 'be', 'was|been'),
               (1416, 'do', 'did|done'), (1471, 'see', 'saw|seen')]

NAME_SIZE = 19


def _name(x, y, place, verb, past, ink, size=NAME_SIZE):
    return ('<text class="place-name" x="%d" y="%d" text-anchor="middle" font-family="Inter,sans-serif" '
            'font-size="%s" font-weight="600" fill="%s" data-size="%s" data-place="%s" data-verb="%s" data-past="%s">%s</text>'
            % (x, y - 14, size, ink, size, place, verb, past, place))


def _cap(x, y, text, ink, size=16, anchor='middle', face='Inter,sans-serif', weight=700,
         spacing='.08em', style=''):
    return ('<text x="%d" y="%d" text-anchor="%s" font-family="%s" font-size="%s" font-weight="%s" '
            'letter-spacing="%s" fill="%s"%s>%s</text>'
            % (x, y, anchor, face, size, weight, spacing, ink, (' font-style="%s"' % style) if style else '', text))


SERIF = 'Fraunces,Georgia,serif'


def captions():
    g, s = INK['regularia'], SEA_INK
    out = [
        _cap(765, 50, '&#9664; WALKED &#183; WENT &#9654;', s, 16),
        # Regularia's three provinces, by the sound -ed makes
        _cap(34, 84, '-ED SAYS /t/', g, 15, 'start', style='italic'),
        _cap(34, 360, '-ED SAYS /d/', g, 15, 'start', style='italic'),
        _cap(34, 614, '-ED SAYS /&#618;d/', g, 15, 'start', style='italic'),
        _cap(34, 930, 'REGULARIA', g, 38, 'start', SERIF, 700, '.04em'),
        _cap(36, 958, 'verb + -ed', g, 19, 'start', SERIF, 600, '0', 'italic'),
        _cap(36, 982, 'and almost every other verb', g, 16, 'start', SERIF, 600, '0', 'italic'),
        # the currents
        _cap(762, 240, 'NEW VERBS SAIL WEST', s, 18, spacing='.1em'),
        _cap(757, 298, 'texted &#183; emailed &#183; googled', s, 16, face=SERIF, weight=600, spacing='0', style='italic'),
        _cap(772, 660, 'SOME OLD ONES ARE DRIFTING WEST', s, 17, spacing='.08em'),
        # Forked Isle
        _cap(760, 345, 'FORKED ISLE', INK['forked'], 22, face=SERIF, spacing='.06em'),
        _cap(760, 368, 'one verb &#183; two meanings &#183; two pasts', INK['forked'], 14, weight=600, spacing='0'),
        # the Shallows (on the sandbank itself)
        _cap(746, 815, 'THE SHALLOWS', INK['shallows'], 20, face=SERIF, spacing='.06em'),
        _cap(746, 838, 'either form, same meaning', INK['shallows'], 14.5, weight=600, spacing='0'),
        _cap(746, 862, 'learnt / learned &#183; dreamt / dreamed', INK['shallows'], 14, weight=500, spacing='0'),
        _cap(746, 884, 'burnt / burned &#183; spelt / spelled', INK['shallows'], 14, weight=500, spacing='0'),
        # the islands, each named after its sound
        _cap(1118, 42, 'I &#183; A &#183; U ISLAND', s, 19, face=SERIF, spacing='.06em'),
        _cap(1118, 64, 'ring &#183; rang &#183; rung', s, 14, weight=600, spacing='0'),
        _cap(1416, 108, 'OUGHT ISLAND', s, 19, face=SERIF, spacing='.06em'),
        _cap(1416, 128, 'buy &#183; bought &#183; bought', s, 14, weight=600, spacing='0'),
        _cap(1116, 300, '-EW ISLAND', s, 19, face=SERIF, spacing='.06em'),
        _cap(1116, 320, 'blow &#183; blew &#183; blown', s, 14, weight=600, spacing='0'),
        _cap(1404, 482, '-T ISLAND', s, 19, face=SERIF, spacing='.06em'),
        _cap(1404, 502, 'keep &#183; kept &#183; kept', s, 14, weight=600, spacing='0'),
        _cap(1120, 592, '-EN ISLAND', s, 19, face=SERIF, spacing='.06em'),
        _cap(1120, 612, 'speak &#183; spoke &#183; spoken', s, 14, weight=600, spacing='0'),
        # the rocks and stacks
        _cap(1380, 800, 'THE LONE STACKS', s, 15),
        _cap(1078, 946, 'THE STILL ROCKS', s, 15),
        _cap(1078, 968, 'cut &#183; put &#183; hit &#183; let &#183; cost: no change', s, 14, weight=600, spacing='0'),
        _cap(1500, 946, 'IRREGULARIA', s, 34, 'end', SERIF, 700, '.04em'),
        _cap(1500, 974, 'no one rule &#183; but families', s, 17, 'end', SERIF, 600, '0', 'italic'),
    ]
    for x, verb, past in LONE_STACKS:
        out.append('<text class="place-name" x="%d" y="884" text-anchor="middle" font-family="Inter,sans-serif" '
                   'font-size="%s" font-weight="600" fill="%s" data-size="%s" data-place="%s" data-verb="%s" data-past="%s">%s</text>'
                   % (x, NAME_SIZE, s, NAME_SIZE, verb, verb, past, verb))
    return '<g class="chart-captions">\n        ' + '\n        '.join(out) + '\n      </g>'


def _poly_path(poly):
    return 'M ' + ' L '.join('%d %d' % (x, y) for x, y in poly) + ' Z'


def _hotspot(uid, key, d, aria):
    return ('<path id="%s-%s" class="land" tabindex="0" role="button" aria-label="%s" '
            'style="cursor:pointer" d="%s" fill="transparent" stroke="transparent" stroke-width="14"/>'
            % (uid, key, aria, d))


def _rect(x0, y0, x1, y1):
    return 'M %d %d L %d %d L %d %d L %d %d Z' % (x0, y0, x1, y0, x1, y1, x0, y1)


ARIA = {
    'regularia': 'Regularia, the continent of regular verbs: verb plus -ed',
    'forked': 'Forked Isle: one verb, two meanings, two past forms',
    'shallows': 'The Shallows: either past form, same meaning',
    'iau': 'I A U Island: ring, rang, rung',
    'ought': 'Ought Island: buy, bought, bought',
    'ew': '-EW Island: blow, blew, blown',
    't': '-T Island: keep, kept, kept',
    'en': '-EN Island: speak, spoke, spoken',
    'still': 'The Still Rocks: verbs that never change',
    'lone': 'The Lone Stacks: go, be, do and see, which belong to no family',
}


def chart_overlay(uid):
    spots = [_hotspot(uid, k, _poly_path(SHAPE[k]['poly']), ARIA[k]) for k in LANDS]
    spots.append(_hotspot(uid, 'still', _rect(930, 850, 1160, 932), ARIA['still']))
    spots.append(_hotspot(uid, 'lone', _rect(1262, 806, 1500, 868), ARIA['lone']))
    names = [_name(x, y, p, v, pa, INK['regularia']) for (x, y), p, v, pa in REGULARIA]
    for k, rows in ISLANDS.items():
        names += [_name(x, y, p, v, pa, INK[k]) for (x, y), p, v, pa in rows]
    return '''<svg class="sail-chart sail-chart-overlay" viewBox="0 0 %d %d">
        %s
        %s
        <g class="place-layer">
        %s
        </g>
      </svg>''' % (W, H, '\n        '.join(spots), captions(), '\n        '.join(names))


if __name__ == '__main__':
    for k in PAINT:
        print('%-10s paint %s ink %s  %.1f:1' % (k, PAINT[k], INK[k], ratio(INK[k], PAINT[k])))
    print('sea        paint %s ink %s  %.1f:1' % (SEA, SEA_INK, ratio(SEA_INK, SEA)))
