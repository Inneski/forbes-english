# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: The Harbour of Scale, IN, ON and AT by the
size of the thing. The twenty-second chart.

    py lesson-template/build/build_scale.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. One harbour, read at three scales. A POINT takes AT (the
buoy, the lighthouse, the harbour mouth). A LINE or a SURFACE takes ON (the
coast, the river, the pier). An AREA you are inside takes IN (the bay, the
harbour). The Tide Boards carry the same three scales into time: AT a clock
time, ON a day, IN a month, a year or a part of the day. Twofold Isle holds
the pairs that change meaning (in time / on time, in the end / at the end);
the Shallows hold the weekend, AT in Britain and ON in America.

No tense on this chart, so no Sherpa colours.

THE ART. Layout by sea_layouts_4.py, painted by Codex on 2026-11-14.
sea_measure.py found the 8 harbour dots and one stray in the scenery
(scale_chart.json); each harbour is matched by position below.
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE

OUT = 'sailing-the-seas-scale.html'
ART = 'sailing-the-seas-scale'
UID = 'scale'

# py lesson-template/extract-palette.py sailing-the-seas-scale/hero.jpg --light
EXTRACTED = {'text': '#2a2111', 'text-dim': '#5e4e2e', 'secondary': '#b1ccd3', 'contrast': '#095a6d'}

D = O.load('scale_chart.json')
DOTS = [tuple(p) for p in D['dots']]


def near(x, y):
    hit = [p for p in DOTS if abs(p[0] - x) < 30 and abs(p[1] - y) < 30]
    assert len(hit) == 1, (x, y, DOTS)
    return hit[0]


# (key, phrase, the scale, sentence, dot, is it on land?)
PLACES = [('buoy', 'at the buoy', 'a point: AT', 'Turn left at the buoy.', near(696, 559), False),
          ('lighthouse', 'at the lighthouse', 'a point: AT', 'Meet me at the lighthouse.', near(897, 350), True),
          ('mouth', 'at the harbour mouth', 'a point: AT', 'The pilot waits at the harbour mouth.', near(926, 559), False),
          ('coast', 'on the coast', 'a line: ON', 'The town is on the coast.', near(134, 600), True),
          ('river', 'on the river', 'a line: ON', 'There is a mill on the river.', near(312, 230), True),
          ('pier', 'on the pier', 'a surface: ON', 'We stood on the pier.', near(436, 730), False),
          ('bay', 'in the bay', 'an area: IN', 'Two ships lie in the bay.', near(422, 470), False),
          ('harbour', 'in the harbour', 'an area: IN', 'The boats are safe in the harbour.', near(608, 757), False)]
INK, LAND, SEA, BOARD = '#20180A', '#A8A067', '#B4D6E1', '#F6CD94'
SEA_INK = '#0F2F3D'
# the three tide boards as painted: (key, head, words, top, bottom)
BOARDS = [('t-at', 'AT', 'at six &#183; at night &#183; at Christmas', 211, 336),
          ('t-on', 'ON', 'on Monday &#183; on 4 July &#183; on my birthday', 367, 488),
          ('t-in', 'IN', 'in July &#183; in 2026 &#183; in the morning', 509, 631)]


def overlay():
    spots, names = [], []
    for key, phrase, scale, sent, (x, y), on_land in PLACES:
        ink, paint = (INK, LAND) if on_land else (SEA_INK, SEA)
        # the harbour mouth's words go under its dot: beside the buoy's they collide
        names.append(O.name(x, y, (phrase, scale, sent), ink, paint, size=18, dy=32 if key == 'mouth' else -16, fit=False,
                            halo=.3 if on_land else .55, anchor='start' if x < 200 else 'middle',
                            dx=-70 if x < 200 else 0))
        spots.append(O.hotspot(UID, key, O.circle_path(x, y, 32), '%s, %s' % (phrase, scale)))
    caps = [O.cap(768, 54, 'THE HARBOUR OF SCALE', SEA_INK, 40, face=O.SERIF, spacing='.05em'),
            O.cap(768, 90, 'a point: AT &#183; a line: ON &#183; an area: IN', SEA_INK, 20, face=O.SERIF, weight=600,
                  spacing='0', style='italic'),
            O.cap(1294, 180, 'THE TIDE BOARDS', SEA_INK, 20, face=O.SERIF, spacing='.04em')]
    for key, head, words, top, bottom in BOARDS:
        caps.append(O.cap(1294, top + 52, head, INK, 30, face=O.SERIF, spacing='.04em'))
        caps.append(O.cap(1294, top + 92, words, INK, 16, weight=600, spacing='0', style='italic'))
        spots.append(O.hotspot(UID, key, O.rect_path(1076, top, 1513, bottom), 'Tide board: %s for time' % head))
    caps += [O.cap(1276, 736, 'TWOFOLD ISLE', INK, 18, face=O.SERIF, spacing='.04em'),
             O.cap(1276, 764, 'in time &#183; on time', INK, 15, weight=600, spacing='0', style='italic'),
             O.cap(1276, 788, 'in the end &#183; at the end', INK, 15, weight=600, spacing='0', style='italic'),
             O.cap(1276, 896, 'THE SHALLOWS', INK, 16, face=O.SERIF, spacing='.04em'),
             O.cap(1276, 920, 'at (UK) / on (US) the weekend', INK, 14, weight=600, spacing='0', style='italic')]
    spots.append(O.hotspot(UID, 'twofold', O.rect_path(1057, 679, 1489, 840), 'Twofold Isle: in time, on time'))
    spots.append(O.hotspot(UID, 'shallows', O.rect_path(1080, 860, 1480, 950), 'The Shallows: at or on the weekend'))
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated chart of one harbour: a bay closed by green land on three sides, with its mouth to the east. '
            'Eight harbours are marked: on the river, at the lighthouse, in the bay, on the coast, at the buoy, at the '
            'harbour mouth, on the pier and in the harbour. On the right, three wooden tide boards read AT, ON and IN '
            'with times under each. Below them, Twofold Isle and a sandbank, the Shallows.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; In, on and at', 'The Harbour of Scale',
    'The same harbour takes three prepositions, and none of them is about the harbour. It is about how you see the '
    'thing: as a point, as a line, or as a space you are inside. A point takes <em>at</em>, a line or a surface '
    'takes <em>on</em>, an area takes <em>in</em>. Read the harbour first, then the tide boards, where time works the same way.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the harbour</div>
      <h2>A point, a line or an area?</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Zoom out and a town is a point on the map: <em>at</em> Dover. Zoom in and you are inside it: <em>in</em> Dover. The preposition tells the listener which scale you mean.</p>
      ''' + rule_grid([
    ('AT: a point',
     'A place you think of as a dot on the chart: where to meet, where to turn.',
     ex('Turn left <em>at</em> the buoy.')),
    ('ON: a line',
     'A coast, a river, a road, a border: something long and thin.',
     ex('The town is <em>on</em> the coast.')),
    ('ON: a surface',
     'Something you stand or lie on top of.',
     ex('We stood <em>on</em> the pier.')),
    ('IN: an area with edges',
     'A space you are inside: a bay, a harbour, a room, a country.',
     ex('Two ships lie <em>in</em> the bay.')),
    ('Time: AT a point, ON a day',
     'A clock time is a point. A day or a date is a surface you stand on.',
     ex('The ferry leaves <em>at</em> six <em>on</em> Monday.')),
    ('Time: IN a longer stretch',
     'A month, a season, a year, a part of the day: you are inside it.',
     ex('We sail <em>in</em> July, <em>in</em> the morning.')),
]) + chart(
    'The eight harbours',
    'One bay, three scales.',
    ['Phrase', 'Scale', 'Sentence'],
    [[p[1], p[2], p[3]] for p in PLACES]) + '''
    </div>

    '''

BOARDS_HTML = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The Tide Boards, Twofold Isle and the Shallows</div>
      <h2>The same three scales, for time</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Small, medium, large: a moment, a day, a longer period. The boards have the few that break the pattern, too.</p>
      ''' + chart(
    'The Tide Boards',
    'Read across: the smaller the time, the further left.',
    ['AT: a point', 'ON: a day', 'IN: a longer stretch'],
    [['at six', 'on Monday', 'in July'], ['at noon', 'on 4 July', 'in 2026'], ['at midnight', 'on my birthday', 'in summer'],
     ['at night', 'on Friday evening', 'in the morning'], ['at Christmas', 'on Christmas Day', 'in the 1990s'],
     ['at the moment', 'on the first day', 'in ten minutes']]) + '''
      ''' + exi('See you <em>at</em> six <em>on</em> Friday. We always meet <em>in</em> the evening.') + chart(
    'Twofold Isle and the Shallows',
    'The same noun, two prepositions, two meanings.',
    ['Phrase', 'Means', 'Example'],
    [['in time', 'early enough', 'We arrived in time to catch the ferry.'],
     ['on time', 'not late, at the planned moment', 'The ferry left on time.'],
     ['in the end', 'finally, after everything', 'In the end, we stayed at home.'],
     ['at the end', 'at the last point of something', 'There is a lighthouse at the end of the pier.'],
     ['at the weekend / on the weekend', 'the same', 'British <em>at</em>, American <em>on</em>']]) + '''
      ''' + exi('The ferry was <em>on time</em>, and we got there <em>in time</em> for dinner.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a harbour or a tide board and its line lights up below: AT on the left, ON in the middle, IN on the '
    'right. Switch the chart to see the scale of each place, then each one in a sentence.',
    ('The phrases', 'The scale', 'In a sentence'),
    [('AT: a point', 'is-west'), ('ON: a line or a surface', 'is-isle'), ('IN: an area', 'is-east')],
    'Drag the chart sideways to reach the tide boards.', min_zoom=1000)

TRAPS = fork(
    'Wrong scale',
    'Each of these reads the place or the time at the wrong size.',
    ['Not this', 'This', 'Why'],
    [['See you in Monday.', 'See you on Monday.', 'a day: ON'],
     ['The ferry leaves on six o&#39;clock.', 'The ferry leaves at six o&#39;clock.', 'a clock time: AT'],
     ['We sail at July.', 'We sail in July.', 'a month: IN'],
     ['The town is in the coast.', 'The town is on the coast.', 'a line: ON'],
     ['I&#39;ll wait in the bus stop.', 'I&#39;ll wait at the bus stop.', 'a point: AT'],
     ['in the night (as a general time)', 'at night', 'a fixed phrase: <em>at night</em>, but <em>in the morning</em>']],
    'Three fixed ones to learn whole: <em>at night</em>, <em>at the weekend</em>, <em>at Christmas</em> (the season) against <em>on Christmas Day</em>.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-voyage.html', 'The Voyage: prepositions of movement')])

SIGNALS = signals(
    'Small: AT',
    ['a dot on the map', 'a meeting point: <em>at the station</em>', 'an address: <em>at 10 Dock Road</em>',
     'a clock time: <em>at six</em>', '<em>at noon</em>, <em>at midnight</em>, <em>at night</em>', 'an event: <em>at a party</em>'],
    'Large: IN',
    ['you are inside it', 'a room, a building, a town', 'a country, a sea', 'a month, a season, a year',
     '<em>in the morning</em>, <em>in the evening</em>', 'a length of time ahead: <em>in ten minutes</em>'],
    'Between the two is ON: a line, a surface, a day. If it is neither a dot nor a space you can be inside, try ON.')

QUIZ = [
    ('Turn left ___ the buoy.', 'A point.', 'at',
     ['at', 'on', 'in', 'to'], 'A point on the chart: at the buoy.'),
    ('The town is ___ the coast.', 'A line.', 'on',
     ['on', 'in', 'at', 'by the'], 'A coast is a line: on the coast.'),
    ('Two ships are anchored ___ the bay.', 'An area.', 'in',
     ['in', 'on', 'at', 'to'], 'A bay is an area you are inside: in the bay.'),
    ('We stood ___ the pier and watched.', 'A surface.', 'on',
     ['on', 'in', 'at', 'into'], 'You stand on top of it: on the pier.'),
    ('The ferry leaves ___ six.', 'A clock time.', 'at',
     ['at', 'on', 'in', 'by the'], 'A clock time is a point: at six.'),
    ('See you ___ Monday.', 'A day.', 'on',
     ['on', 'in', 'at', 'the'], 'A day: on Monday.'),
    ('We always sail ___ July.', 'A month.', 'in',
     ['in', 'on', 'at', 'by'], 'A month: in July.'),
    ('I was born ___ 4 July.', 'A date.', 'on',
     ['on', 'in', 'at', 'the'], 'A date is a day: on 4 July.'),
    ('It is quiet here ___ night.', 'A fixed phrase.', 'at',
     ['at', 'in', 'on', 'by the'], 'At night, but in the morning.'),
    ('The ferry left exactly ___ time, at 6.00.', 'Twofold Isle.', 'on',
     ['on', 'in', 'at', 'by'], 'On time: at the planned moment.'),
    ('We ran, and we got there just ___ time.', 'Twofold Isle.', 'in',
     ['in', 'on', 'at', 'by'], 'In time: early enough.'),
    ('Which sentence is right?', 'Three scales in one sentence.', 'We met at six on Friday in the harbour.',
     ['We met at six on Friday in the harbour.', 'We met on six at Friday in the harbour.',
      'We met in six on Friday at the harbour.', 'We met at six in Friday on the harbour.'],
     'At a clock time, on a day, in an area.'),
]

PANELS = [
    [(p[0], '<b>%s</b> %s' % (p[1], p[3])) for p in PLACES[:3]] +
    [('t-at', '<b>time</b> at six &middot; at night &middot; at Christmas'),
     ('shallows', '<em>at</em> (UK) / <em>on</em> (US) the weekend')],
    [(p[0], '<b>%s</b> %s' % (p[1], p[3])) for p in PLACES[3:6]] +
    [('t-on', '<b>time</b> on Monday &middot; on 4 July &middot; on my birthday')],
    [(p[0], '<b>%s</b> %s' % (p[1], p[3])) for p in PLACES[6:]] +
    [('t-in', '<b>time</b> in July &middot; in 2026 &middot; in the morning'),
     ('twofold', '<b>Twofold Isle</b> <em>in time</em> / <em>on time</em> &middot; <em>in the end</em> / <em>at the end</em>')],
]
TARGETS = {}
for i, p in enumerate(PLACES):
    TARGETS[p[0]] = (i // 3 if i < 6 else 2, p[0], '#095a6d')
TARGETS['t-at'] = (0, 't-at', '#095a6d')
TARGETS['t-on'] = (1, 't-on', '#095a6d')
TARGETS['t-in'] = (2, 't-in', '#095a6d')
TARGETS['twofold'] = (2, 'twofold', '#B4441F')
TARGETS['shallows'] = (0, 'shallows', '#095a6d')

import ex_tr_scale as T
L.build(OUT, ART, 'The Harbour of Scale &mdash; In, On and At', 'In, on and at', EXTRACTED,
        HERO, 'where time works the same way.', ('order', 'Read the chart'),
        RULES + BOARDS_HTML + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        [BOARD, LAND, SEA], T.T,
        ['Clean run. You read the scale, and the preposition follows.',
         'Solid progress. Check the tide boards again: at six, on Monday, in July.',
         'Good first attempt. Start with one question: a point, a line or an area?'],
        ('sailing-the-seas-voyage.html', 'Next chart: the Voyage'), gull_seed=97, long_name=24)
