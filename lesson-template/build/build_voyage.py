# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: The Voyage, prepositions of movement as one
route. The twenty-third chart.

    py lesson-template/build/build_voyage.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. Twelve legs, twelve prepositions, in the order a boat
would sail them: out of the harbour, past the lighthouse, along the coast,
round the cape, across the bay, through the strait, under the bridge, over
the sandbar, up the river, towards the island, into the cove, onto the
jetty. Each preposition is tied to the shape of the thing it passes, so the
picture carries the meaning; the learner sails it, then tells it back.

No tense on this chart, so no Sherpa colours.

THE ART. Layout by sea_layouts_4.py, painted by Codex on 2026-11-14.
sea_measure.py found the 12 leg dots and one stray in the scenery
(voyage_chart.json); each leg is matched by position below.
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE

OUT = 'sailing-the-seas-voyage.html'
ART = 'sailing-the-seas-voyage'
UID = 'voy'

# py lesson-template/extract-palette.py sailing-the-seas-voyage/hero.jpg --light
EXTRACTED = {'text': '#2a2111', 'text-dim': '#5e4e2e', 'secondary': '#b3cfd8', 'contrast': '#095a6d'}

D = O.load('voyage_chart.json')
DOTS = [tuple(p) for p in D['dots']]


def near(x, y):
    hit = [p for p in DOTS if abs(p[0] - x) < 30 and abs(p[1] - y) < 30]
    assert len(hit) == 1, (x, y, DOTS)
    return hit[0]


# (preposition, place, what the movement is, dot, where the words sit: a(bove), b(elow), r(ight))
LEGS = [('out of', 'the harbour', 'from inside to outside', near(170, 900), 'a'),
        ('past', 'the lighthouse', 'by it, and on', near(299, 769), 'a'),
        ('along', 'the coast', 'following a line', near(250, 587), 'a'),
        ('round', 'the cape', 'in a curve, to the other side', near(360, 330), 'a'),
        ('across', 'the bay', 'from one side to the other', near(586, 420), 'a'),
        ('through', 'the strait', 'in one end and out the other', near(800, 540), 'r'),
        ('under', 'the bridge', 'below it', near(960, 681), 'b'),
        ('over', 'the sandbar', 'above it, to the other side', near(1109, 818), 'b'),
        ('up', 'the river', 'against the flow', near(1298, 688), 'r'),
        ('towards', 'the island', 'in its direction', near(1168, 530), 'b'),
        ('into', 'the cove', 'from outside to inside', near(1348, 282), 'a'),
        ('onto', 'the jetty', 'to a surface', near(1425, 182), 'a')]
INK, SEA = '#0F2F3D', '#B4D6E1'


def key(prep):
    return prep.replace(' ', '-')


def overlay():
    spots, names = [], []
    for i, (prep, place, move, (x, y), side) in enumerate(LEGS, 1):
        anchor, dx, dy = 'middle', 0, -16
        if side == 'r':
            anchor, dx, dy = 'start', 18, 6
        elif side == 'b':
            dy = 32
        if x > 1380:                      # the jetty is hard against the border: read leftwards
            anchor, dx = 'end', 22
        names.append(O.name(x, y, ('%d &#183; %s' % (i, prep.upper()), place, '%s %s' % (prep, place)), INK, SEA,
                            size=18, anchor=anchor, dx=dx, dy=dy, fit=False, halo=.6, weight=700))
        spots.append(O.hotspot(UID, key(prep), O.circle_path(x, y, 34), 'Leg %d: %s %s' % (i, prep, place)))
    caps = [O.cap(768, 62, 'THE VOYAGE', INK, 44, face=O.SERIF, spacing='.05em'),
            O.cap(768, 100, 'twelve legs, twelve prepositions: sail it, then tell it back', INK, 20, face=O.SERIF,
                  weight=600, spacing='0', style='italic')]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated chart of a voyage in twelve numbered legs, joined by a dashed route. It leaves a harbour in '
            'the south-west, passes a lighthouse, follows the west coast north, rounds a cape, crosses a bay, goes '
            'through a strait between two islands, under a bridge, over a sandbar, up a river on the east coast, '
            'towards an island, into a cove and onto a jetty in the north-east.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; Prepositions of movement', 'The Voyage',
    'A preposition of movement is a small picture: <em>through</em> has an inside, <em>across</em> has two sides, '
    '<em>along</em> has a line to follow. So this chart is one voyage in twelve legs, each named by the word that '
    'draws it. Sail the route once with the chart, then tell it back without it.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the route</div>
      <h2>Each word has a shape</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Ask what the thing looks like. A strait has walls, so you go <em>through</em> it. A bay is open water with two shores, so you go <em>across</em> it.</p>
      ''' + rule_grid([
    ('In and out: into, out of',
     'From outside to inside, and back. <em>Out of</em> is two words.',
     ex('We sailed <em>out of</em> the harbour and, hours later, <em>into</em> the cove.')),
    ('Following a line: along, up, down',
     '<em>Along</em> a coast or a road; <em>up</em> a river against the flow, <em>down</em> it with the flow.',
     ex('We sailed <em>along</em> the coast and then <em>up</em> the river.')),
    ('To the other side: across, over',
     '<em>Across</em> a flat space; <em>over</em> something that is in the way below you.',
     ex('We sailed <em>across</em> the bay and <em>over</em> the sandbar.')),
    ('Between walls: through',
     'In at one end and out at the other, with something on both sides.',
     ex('We sailed <em>through</em> the strait.')),
    ('By and beyond: past, round, under',
     '<em>Past</em> it and on; <em>round</em> it in a curve; <em>under</em> it, below.',
     ex('We sailed <em>past</em> the lighthouse, <em>round</em> the cape and <em>under</em> the bridge.')),
    ('Direction and arrival: towards, onto',
     '<em>Towards</em> is the direction only: you may not arrive. <em>Onto</em> ends on a surface.',
     ex('We sailed <em>towards</em> the island, and I stepped <em>onto</em> the jetty.')),
]) + chart(
    'The twelve legs',
    'The whole voyage, in order.',
    ['Leg', 'Preposition', 'Place', 'The movement'],
    [[str(i), prep, place, move] for i, (prep, place, move, _, _) in enumerate(LEGS, 1)]) + '''
    </div>

    '''

EXTRAS = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Pairs to keep apart</div>
      <h2>Close in meaning, different in shape</h2>
      <p class="chart-note" style="margin:-6px 0 18px">These are the pairs learners swap. In each, look at what the thing is: a surface, a space, a line, an obstacle.</p>
      ''' + chart(
    'Six pairs',
    'Read each row as a contrast.',
    ['This', 'Not the same as', 'The difference'],
    [['across the bay', 'through the strait', 'open space / walls on both sides'],
     ['over the sandbar', 'across the bay', 'something below in the way / a flat space'],
     ['into the cove', 'in the cove', 'movement / position'],
     ['onto the jetty', 'on the jetty', 'movement / position'],
     ['towards the island', 'to the island', 'direction only / arrival'],
     ['past the lighthouse', 'round the cape', 'straight by / in a curve']]) + '''
      ''' + exi('We sailed <em>towards</em> the island, but we never got <em>to</em> it.') + chart(
    'The same words on land',
    'The shapes are the same away from the sea.',
    ['At sea', 'On land', 'Shape'],
    [['through the strait', 'through the tunnel, through the park', 'something on both sides'],
     ['across the bay', 'across the road, across the square', 'one side to the other'],
     ['along the coast', 'along the river, along the street', 'following a line'],
     ['round the cape', 'round the corner', 'a curve'],
     ['up the river', 'up the hill, up the stairs', 'to a higher point'],
     ['out of the harbour', 'out of the house, out of the car', 'from inside']]) + '''
      ''' + exi('Go <em>along</em> this street, <em>across</em> the square and <em>through</em> the park.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a leg and its line lights up below. Switch the chart to see the place each leg passes, then the two '
    'together. When you can, cover the lists and tell the voyage from the chart alone.',
    ('The prepositions', 'The places', 'Together'),
    [('Legs 1 to 4', 'is-west'), ('Legs 5 to 8', 'is-isle'), ('Legs 9 to 12', 'is-east')],
    'Drag the chart sideways to follow the route east.', min_zoom=1000)

TRAPS = fork(
    'Off course',
    'Each of these uses a preposition with the wrong shape.',
    ['Not this', 'This', 'Why'],
    [['We sailed through the bay.', 'We sailed across the bay.', 'open water, two shores'],
     ['We sailed across the strait. (along its length)', 'We sailed through the strait.', 'walls on both sides'],
     ['He jumped in the water.', 'He jumped into the water.', 'movement: <em>into</em>'],
     ['She stepped on the jetty. (from the boat)', 'She stepped onto the jetty.', 'movement to a surface'],
     ['We sailed out the harbour.', 'We sailed out of the harbour.', '<em>of</em> is needed in British English'],
     ['We went to the island but did not arrive.', 'We went towards the island but did not arrive.', 'direction only']],
    '<em>Round</em> is British; Americans say <em>around</em>. Both are understood everywhere.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-scale.html', 'The Harbour of Scale: in, on and at')])

SIGNALS = signals(
    'It is a position',
    ['no movement', '<em>be</em>, <em>stay</em>, <em>live</em>, <em>wait</em>', '<em>in</em> the cove', '<em>on</em> the jetty',
     '<em>at</em> the lighthouse', 'see the Harbour of Scale'],
    'It is a movement',
    ['a verb of motion: <em>sail</em>, <em>go</em>, <em>walk</em>, <em>run</em>', '<em>into</em> the cove',
     '<em>onto</em> the jetty', '<em>past</em> the lighthouse', 'a start and an end', 'this chart'],
    'One test: is anything moving? <em>The boat is in the cove</em> (position). <em>The boat sailed into the cove</em> (movement).')

QUIZ = [
    ('We sailed ___ the harbour at dawn.', 'From inside to outside.', 'out of',
     ['out of', 'into', 'through', 'onto'], 'From inside to outside: out of.'),
    ('The route goes ___ the coast for ten miles.', 'Following a line.', 'along',
     ['along', 'across', 'through', 'into'], 'Following a line: along.'),
    ('We sailed ___ the bay to the other shore.', 'One side to the other, open water.', 'across',
     ['across', 'through', 'along', 'under'], 'Open water with two sides: across.'),
    ('The strait is narrow. We sailed ___ it slowly.', 'Walls on both sides.', 'through',
     ['through', 'across', 'over', 'onto'], 'Something on both sides: through.'),
    ('The mast is low enough to go ___ the bridge.', 'Below it.', 'under',
     ['under', 'over', 'onto', 'along'], 'Below it: under.'),
    ('At high tide we can sail ___ the sandbar.', 'Above something in the way.', 'over',
     ['over', 'under', 'through', 'into'], 'Above it to the other side: over.'),
    ('We sailed ___ the river to the old mill.', 'Against the flow.', 'up',
     ['up', 'down', 'across', 'past'], 'Against the flow, inland: up the river.'),
    ('We turned ___ the island, but the wind stopped us.', 'Direction only.', 'towards',
     ['towards', 'to', 'into', 'onto'], 'Direction, without arriving: towards.'),
    ('The boat slipped ___ the cove and dropped anchor.', 'From outside to inside.', 'into',
     ['into', 'in', 'onto', 'out of'], 'Movement to the inside: into.'),
    ('She stepped from the boat ___ the jetty.', 'To a surface.', 'onto',
     ['onto', 'on', 'into', 'at'], 'Movement to a surface: onto.'),
    ('We sailed ___ the cape and saw the bay.', 'In a curve.', 'round',
     ['round', 'through', 'under', 'into'], 'In a curve to the other side: round.'),
    ('Which sentence is right?', 'Position or movement?', 'The boat sailed into the cove and stayed in it all night.',
     ['The boat sailed into the cove and stayed in it all night.', 'The boat sailed in the cove and stayed into it all night.',
      'The boat sailed onto the cove and stayed on it all night.', 'The boat sailed at the cove and stayed to it all night.'],
     'Into for the movement, in for the position.'),
]


def leg_row(i):
    prep, place, _, _, _ = LEGS[i]
    return (key(prep), '<b>%d &middot; %s</b> We sailed %s %s.' % (i + 1, prep, prep, place))


PANELS = [[leg_row(i) for i in range(0, 4)], [leg_row(i) for i in range(4, 8)], [leg_row(i) for i in range(8, 12)]]
TARGETS = {key(prep): (i // 4, key(prep), '#095a6d') for i, (prep, _, _, _, _) in enumerate(LEGS)}

import ex_tr_voyage as T
L.build(OUT, ART, 'The Voyage &mdash; Prepositions of Movement', 'Prepositions of movement', EXTRACTED,
        HERO, 'then tell it back without it.', ('order', 'Read the chart'),
        RULES + EXTRAS + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        ['#AFA169', '#E9BF80', '#A99F6B'], T.T,
        ['Clean run. You can tell the whole voyage back.',
         'Solid progress. Sail the middle again: across, through, under, over.',
         'Good first attempt. Start with the first four legs: out of, past, along, round.'],
        ('sailing-the-seas-er-more.html', 'Next chart: the -ER Coast &amp; the MORE Coast'), gull_seed=101, long_name=24)
