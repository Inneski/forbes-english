# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: The Particle Ferries, phrasal verbs as a
ferry network. The twelfth chart.

    py lesson-template/build/build_phrasal_verbs.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. Five coloured ferry lines cross the bay, one per particle
(UP, OUT, OFF, ON, DOWN). Every line runs the same way, west to east, from
the stop where the little word means exactly what it says to the stop where
it no longer helps: THE DIRECTION (stand up), THE IDEA (speed up: faster),
STRETCHED (fill up: to the top), LEARN IT WHOLE (give up). So the chart is a
guide to how far to trust the particle. Each line's label lists its three
senses in the order of its first three stops.

The first build (2026-11-09) crossed the particle lines with four verb lines
(GET, TAKE, PUT, TURN) and labelled each line with a sense its own stops did
not keep (put off on the "away, stop" line, turn out on "to the end").
Innes: "confusing af and doesn't act as a guide in any useful way". The verb
lines carried no meaning, so the columns are now the four zones and the grey
lines are the zone boundaries; the painting did not have to change.

THE ART. Layout by sea_layouts_3.py (docs/sea-charts/particle-ferries.png),
painted by ChatGPT on 2026-11-09 with Gerundia as the style. The stops are
WHITE quay markers, not black dots, so sea_measure.py finds none; they were
measured as white discs (a 4 x 5 grid at x 476 744 1020 1294, y 284 400 518
636 754) and stored as 'markers' in phrasal-verbs_chart.json. The painter
moved the compass to the top centre.

The painted hero carried the first build's words (GET, TAKE, PUT, TURN), so
hero.jpg is now the clean chart with this overlay rendered on it (The stops
mode) by tools/render_chart_hero.js. Re-run it after changing the overlay.
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE

OUT = 'sailing-the-seas-phrasal-verbs.html'
ART = 'sailing-the-seas-phrasal-verbs'
UID = 'pvb'

# py lesson-template/extract-palette.py sailing-the-seas-phrasal-verbs/hero.jpg --light
EXTRACTED = {'text': '#2a2011', 'text-dim': '#5e4c2e', 'secondary': '#b0ced6', 'contrast': '#095f6d'}

D = O.load('phrasal-verbs_chart.json')
MARKS = [tuple(p) for p in D['markers']]
XS = sorted({p[0] for p in MARKS})
YS = sorted({p[1] for p in MARKS})
assert len(MARKS) == 20 and len(XS) == 4 and len(YS) == 5, MARKS

ZONES = [('THE DIRECTION', 'it says what it means'), ('THE IDEA', 'the same sense, not a place'),
         ('STRETCHED', 'the sense, pulled further'), ('LEARN IT WHOLE', 'the little word no longer helps')]
# (particle, its three senses in zone order, line colour, four stops: (verb, meaning, sentence))
LINES = [
    ('up', 'up &#183; faster &#183; full', '#D85A30',
     [('stand up', 'rise to your feet', 'Everyone stood up.'), ('speed up', 'go faster', 'The ferry sped up.'),
      ('fill up', 'fill to the top', 'Fill up the water tank.'), ('give up', 'stop trying', 'Don&#8217;t give up now!')]),
    ('out', 'out &#183; gone &#183; into view', '#1D9E75',
     [('go out', 'leave, go outside', 'Let&#8217;s go out on deck.'), ('run out', 'have none left', 'We ran out of fuel.'),
      ('find out', 'discover', 'Find out when it leaves.'), ('turn out', 'end up, prove to be', 'It turned out fine.')]),
    ('off', 'off &#183; away &#183; disconnected', '#534AB7',
     [('get off', 'leave a boat or bus', 'Get off at the pier.'), ('set off', 'start a journey', 'We set off at dawn.'),
      ('switch off', 'stop a machine', 'Switch off the engine.'), ('put off', 'postpone', 'We put off the trip.')]),
    ('on', 'on &#183; on you &#183; keep going', '#BA7517',
     [('get on', 'board', 'Get on the ferry.'), ('put on', 'dress in', 'Put on a life jacket.'),
      ('carry on', 'continue', 'Carry on rowing!'), ('take on', 'accept work or staff', 'We took on a new crew.')]),
    ('down', 'down &#183; slower &#183; on paper', '#185FA5',
     [('sit down', 'take a seat', 'Please sit down.'), ('slow down', 'go slower', 'Slow down near the harbour.'),
      ('write down', 'put on paper', 'Write down the number.'), ('turn down', 'refuse', 'He turned it down.')]),
]
INK, SEA = '#14262C', '#C0D8DE'


def key(verb):
    return verb.replace(' ', '-')


def overlay():
    spots, names = [], []
    for (p, sense, col, stops), y in zip(LINES, YS):
        for x, (verb, meaning, sent) in zip(XS, stops):
            assert (x, y) in MARKS and verb.endswith(' ' + p), verb
            names.append(O.name(x, y, (verb, meaning, sent), INK, SEA, size=17, anchor='start', dx=20,
                                dy=-36, fit=False, halo=.45))
            spots.append(O.hotspot(UID, key(verb), O.circle_path(x, y, 30), '%s: %s' % (verb, meaning)))
        spots.append(O.hotspot(UID, 'line-' + p, O.rect_path(40, y - 44, 330, y + 28), 'The %s line: %s' % (p.upper(), sense)))
    caps = [O.cap(768, 58, 'THE PARTICLE FERRIES', '#2A1E0C', 36, face=O.SERIF, spacing='.04em', halo='#F0E3CE'),
            O.cap(768, 84, 'one line for each little word &#183; the further east, the less it tells you', '#2A1E0C', 17,
                  face=O.SERIF, weight=600, spacing='0', style='italic', halo='#F0E3CE')]
    for (zone, sub), x in zip(ZONES, XS):
        caps.append(O.cap(x, 192, zone, INK, 18, face=O.SERIF, spacing='.04em', halo=O.mix(SEA, '#FFFFFF', .4)))
        caps.append(O.cap(x, 212, sub, INK, 13, weight=600, spacing='0', style='italic', halo=O.mix(SEA, '#FFFFFF', .4)))
    for (p, sense, col, stops), y in zip(LINES, YS):
        dark = O.mix(col, '#000000', .3)
        assert O.ratio(dark, SEA) >= 3, 'the %s line label is too faint' % p
        caps.append(O.cap(56, y - 12, p.upper(), dark, 25, 'start', face=O.SERIF, spacing='.03em',
                          halo=O.mix(SEA, '#FFFFFF', .5)))
        caps.append(O.cap(56, y + 12, sense, INK, 13, 'start', weight=600, spacing='0', style='italic',
                          halo=O.mix(SEA, '#FFFFFF', .5)))
    caps.append(O.cap(768, 974, 'west: trust the little word &#183; east: learn the verb as one word',
                      '#2A1E0C', 17, face=O.SERIF, weight=600, spacing='0', style='italic', halo='#FAD9AA'))
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated chart of a busy bay with harbour towns on the north and south shores. Five coloured '
            'dashed ferry lines cross it west to east, one per little word: UP in red, OUT in green, OFF in purple, '
            'ON in ochre, DOWN in blue. Four zones run from west to east: the direction, the idea, stretched, and '
            'learn it whole. The UP line stops at stand up, speed up, fill up and give up; the OFF line at get off, '
            'set off, switch off and put off; the DOWN line at sit down, slow down, write down and turn down.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; phrasal verbs', 'The Particle Ferries',
    'A phrasal verb is a verb and a little word: <em>stand</em> + <em>up</em>, <em>switch</em> + <em>off</em>. Each '
    'little word is a ferry line here, and every line sails the same way. In the west the little word means exactly '
    'what it says; further east it keeps the idea but not the place; at the end of the line it no longer helps, and '
    'you learn the verb as one word. Find the line, then see how far east you are.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the network</div>
      <h2>How far can you trust the little word?</h2>
      <p class="chart-note" style="margin:-6px 0 18px">The little word, the <em>particle</em>, is the clue. Near the start of its line it tells you everything; by the end of the line it tells you nothing. Every line has the same four zones.</p>
      ''' + rule_grid([
    ('Zone 1, the direction: it says what it means',
     'UP is up, OUT is out, DOWN is down. You can guess these the first time you hear them.',
     ex('Everyone <em>stood up</em> when the captain came in.')),
    ('Zone 2, the idea: the same sense, not a place',
     'UP becomes <em>more</em> or <em>faster</em>, OUT becomes <em>until none is left</em>, DOWN becomes <em>less</em>. Still guessable.',
     ex('We <em>ran out</em> of fuel two miles from shore.')),
    ('Zone 3, stretched: the sense pulled further',
     'OFF is <em>disconnected</em>, DOWN is <em>on paper</em>, UP is <em>to the top</em>. Guessable once you know the line.',
     ex('<em>Switch off</em> the engine before you land.')),
    ('Zone 4, learn it whole',
     'The little word no longer helps: <em>put off</em> is postpone, <em>give up</em> is stop trying. Learn these as single words.',
     ex('We <em>put off</em> the trip until spring.')),
    ('Some can split around their object',
     'With a noun, either order works: <em>put on a jacket</em>, <em>put a jacket on</em>.',
     ex('<em>Put</em> your life jacket <em>on</em>.')),
    ('A pronoun always splits them',
     'With <em>it</em>, <em>them</em>, <em>her</em>, the pronoun goes in the middle: <em>put it on</em>, never <em>put on it</em>.',
     ex('It&#39;s cold: <em>put it on</em>.')),
]) + chart(
    'The twenty stops',
    'Read across a line: the meaning drifts further from the little word with every stop. Read down a column: every line drifts the same way.',
    ['', '1 &middot; the direction', '2 &middot; the idea', '3 &middot; stretched', '4 &middot; learn it whole'],
    [[p.upper()] + ['<b>%s</b> %s' % (v, m) for v, m, _s in stops] for p, _sense, _c, stops in LINES]) + '''
    </div>

    '''

SPLIT = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The timetable</div>
      <h2>Where does the object go?</h2>
      <p class="chart-note" style="margin:-6px 0 18px">This is the part of phrasal verbs that grammar tests love. Two kinds of ferry: one that lets the object board in the middle, one that does not.</p>
      ''' + chart(
    'Separable: the object can board in the middle',
    'With a noun, both orders. With a pronoun, the middle only.',
    ['Verb', 'With a noun', 'With a pronoun'],
    [['turn off', 'Turn off the engine. / Turn the engine off.', 'Turn it off.'],
     ['put on', 'Put on your jacket. / Put your jacket on.', 'Put it on.'],
     ['take down', 'Take down the number. / Take the number down.', 'Take it down.'],
     ['turn down', 'She turned down the job. / She turned the job down.', 'She turned it down.']]) + '''
      ''' + exi('Turn the radio <em>down</em>, please: turn it <em>down</em>.') + chart(
    'Inseparable: the object stays on the quay',
    'The object always comes after the whole verb, noun or pronoun.',
    ['Verb', 'With a noun', 'With a pronoun'],
    [['get on', 'Get on the ferry.', 'Get on it.'], ['get off', 'Get off the bus.', 'Get off it.'],
     ['get over', 'She got over the cold.', 'She got over it.'], ['look after', 'Look after the boat.', 'Look after it.']]) + '''
      ''' + exi('She&#39;s had a cold, but she&#39;s <em>getting over</em> it.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a stop and its line lights up below; click a coloured line&#39;s name for its senses. Switch the chart to '
    'see what each stop means, then a sentence. Read each line west to east: the meaning moves further from the '
    'little word at every stop.',
    ('The stops', 'The meaning', 'In a sentence'),
    [('The direction and the idea', 'is-west'), ('Stretched, or learn it whole', 'is-isle'), ('The five lines', 'is-east')],
    'Drag the chart sideways to reach the last zone.', min_zoom=1000)

TRAPS = fork(
    'Wrong platform',
    'Most mistakes put the pronoun on the wrong side, or take the wrong line.',
    ['Not this', 'This', 'Why'],
    [['Put on it.', 'Put it on.', 'a pronoun splits the verb'],
     ['Turn off them.', 'Turn them off.', 'a pronoun splits the verb'],
     ['Get the ferry on.', 'Get on the ferry.', '<em>get on</em> never splits'],
     ['The meeting was put down until Monday.', 'The meeting was put off until Monday.', '<em>put off</em> is postpone'],
     ['Speed down near the harbour.', 'Slow down near the harbour.', 'DOWN is less, but the verb is <em>slow</em>'],
     ['We ran off fuel.', 'We ran out of fuel.', 'OUT is until none is left']],
    'A good dictionary shows which kind a verb is: <em>turn sth off</em> splits; <em>get on sth</em> does not.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-register.html', 'The heights of register')])

SIGNALS = signals(
    'The object can sit in the middle',
    ['<em>turn on / off / up / down</em>', '<em>put on / off / down / up</em>', '<em>take off</em> (clothes), <em>take down</em>',
     '<em>pick up</em>, <em>throw away</em>, <em>fill in</em>', 'pronoun in the middle: <em>turn it off</em>'],
    'The object stays after',
    ['<em>get on / off</em> (a bus, a boat)', '<em>get over</em> (an illness)', '<em>look after</em>, <em>look for</em>',
     '<em>come across</em>, <em>run into</em>', 'pronoun after: <em>get on it</em>, <em>look after her</em>'],
    'One test: can a machine or a piece of clothing go in the middle? <em>Turn the engine off</em>: yes. Then it splits.')

QUIZ = [
    ('Everyone ___ when the captain walked in.', 'Zone 1: the direction.', 'stood up',
     ['stood up', 'sat down', 'got off', 'stood on'], 'Stand up: UP means exactly what it says.'),
    ('The wind dropped, so the ferry ___.', 'Went slower: DOWN is less.', 'slowed down',
     ['slowed down', 'sped up', 'set off', 'carried on'], 'Slow down: DOWN as less.'),
    ('We ___ fuel two miles from shore.', 'Until none was left.', 'ran out of',
     ['ran out of', 'ran off', 'ran on', 'ran down of'], 'Run out of: OUT as until gone.'),
    ('Please ___ the engine before you land.', 'Disconnect it.', 'switch off',
     ['switch off', 'switch on', 'switch up', 'switch out'], 'Switch off: OFF as disconnected.'),
    ('We ___ at dawn and reached the island by noon.', 'Start a journey: OFF is away.', 'set off',
     ['set off', 'set on', 'set down', 'set in'], 'Set off: OFF as away, starting a journey.'),
    ('___ rowing! We&#39;re nearly there.', 'Keep going.', 'Carry on',
     ['Carry on', 'Carry off', 'Carry out', 'Carry up'], 'Carry on: ON as keep going.'),
    ('___ the number before you forget it.', 'On paper.', 'Write down',
     ['Write down', 'Write on', 'Write off', 'Put off'], 'Write down: DOWN as on paper.'),
    ('Fill ___ the water tank before we leave.', 'To the top.', 'up',
     ['up', 'out', 'off', 'on'], 'Fill up: UP as to the top.'),
    ('Which stop must you learn whole?', 'The little word does not help.', 'put off (postpone)',
     ['put off (postpone)', 'get off (leave a boat)', 'set off (start a journey)', 'switch off (stop a machine)'],
     'Postpone has nothing to do with away or disconnected: learn put off as one word.'),
    ('It&#39;s cold. Put your jacket on: put ___.', 'A pronoun splits the verb.', 'it on',
     ['it on', 'on it', 'it', 'on'], 'Put it on: the pronoun goes in the middle.'),
    ('She was offered the job, but she ___.', 'Refuse.', 'turned it down',
     ['turned it down', 'turned down it', 'turned it off', 'turned it out'], 'Turn down: refuse. With it: turned it down.'),
    ('Which sentence is NOT correct?', 'One pronoun is on the wrong side.', 'Switch off it, please.',
     ['Switch off it, please.', 'Switch it off, please.', 'Switch the light off, please.', 'Switch off the light, please.'],
     'With a pronoun: switch it off.'),
]

PANELS = [
    [(key(st[i][0]), '<b>%s</b> %s &middot; %s' % st[i]) for i in (0, 1) for p, s_, c, st in LINES],
    [(key(st[i][0]), '<b>%s</b> %s &middot; %s' % st[i]) for i in (2, 3) for p, s_, c, st in LINES],
    [('line-' + p, '<b>%s</b> %s' % (p.upper(), s_)) for p, s_, c, st in LINES],
]
TARGETS = {}
for p, s_, c, st in LINES:
    for i, stop in enumerate(st):
        TARGETS[key(stop[0])] = (0 if i < 2 else 1, key(stop[0]), c)
    TARGETS['line-' + p] = (2, 'line-' + p, c)

import ex_tr_phrasal_verbs as T
L.build(OUT, ART, 'The Particle Ferries &mdash; Phrasal Verbs', 'phrasal verbs', EXTRACTED,
        HERO, 'Find the line, then see how far east you are.', ('order', 'Read the chart'),
        RULES + SPLIT + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        ['#C9C6C0', '#BFD7DE', '#E3CF9E'], T.T,
        ['Clean run. You know how far to trust the little word, and where to stop trusting it.',
         'Solid progress. Watch the pronoun: put it on, switch it off.',
         'Good first attempt. Ride one line, UP, from stand up to give up.'],
        ('sailing-the-seas-of-grammar.html', 'Back to the first chart: Gerundia and Infinitivia'), gull_seed=53,
        long_name=30)
