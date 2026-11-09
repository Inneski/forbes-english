# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: The Particle Ferries, phrasal verbs as a
ferry network. The twelfth chart.

    py lesson-template/build/build_phrasal_verbs.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. Five coloured ferry lines cross the bay, one per particle
(UP, OUT, OFF, ON, DOWN), each with its rough sense; four grey lines cross
them, one per big verb (GET, TAKE, PUT, TURN). Every crossing is a phrasal
verb, and the same verb on a new line is a new meaning: take off, take on,
take down. Twenty stops, read three ways: the verb, its meaning, a sentence.

THE ART. Layout by sea_layouts_3.py (docs/sea-charts/particle-ferries.png),
painted by ChatGPT on 2026-11-09 with Gerundia as the style. The stops are
WHITE quay markers, not black dots, so sea_measure.py finds none; they were
measured as white discs (a 4 x 5 grid at x 476 744 1020 1294, y 284 400 518
636 754) and stored as 'markers' in phrasal-verbs_chart.json. The painter
moved the compass to the top centre.
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

VERBS = ['get', 'take', 'put', 'turn']
# (particle, its rough sense, line colour, and per verb: (meaning, sentence))
LINES = [
    ('up', 'finish, or more', '#D85A30', [('leave your bed', 'I get up at six.'), ('start a hobby', 'She took up sailing.'),
                                         ('raise', 'Put up the sail.'), ('arrive', 'He turned up late.')]),
    ('out', 'to the end, or outside', '#1D9E75', [('leave', 'Get out of the water!'), ('remove', 'Take out the oars.'),
                                                 ('stop a fire', 'Put out the fire.'), ('end up', 'It turned out fine.')]),
    ('off', 'away, or stop', '#534AB7', [('leave a boat or bus', 'Get off at the pier.'), ('leave the ground', 'The plane took off.'),
                                        ('postpone', 'We put off the trip.'), ('stop a machine', 'Turn off the engine.')]),
    ('on', 'continue, or connect', '#BA7517', [('board', 'Get on the ferry.'), ('accept', 'We took on a new crew.'),
                                              ('dress in', 'Put on a life jacket.'), ('start a machine', 'Turn on the lights.')]),
    ('down', 'less, or on paper', '#185FA5', [('descend', 'Get down from the mast.'), ('write', 'Take down the number.'),
                                             ('place', 'Put down your bags.'), ('refuse', 'He turned it down.')]),
]
INK, SEA = '#14262C', '#C0D8DE'


def key(v, p):
    return '%s-%s' % (v, p)


def overlay():
    spots, names = [], []
    for (p, sense, col, stops), y in zip(LINES, YS):
        for v, x, (meaning, sent) in zip(VERBS, XS, stops):
            assert (x, y) in MARKS
            names.append(O.name(x, y, ('%s %s' % (v, p), meaning, sent), INK, SEA, size=17, anchor='start', dx=20,
                                dy=-36, fit=False, halo=.45))
            spots.append(O.hotspot(UID, key(v, p), O.circle_path(x, y, 30), '%s %s: %s' % (v, p, meaning)))
        dark = O.mix(col, '#000000', .3)
        spots.append(O.hotspot(UID, 'line-' + p, O.rect_path(40, y - 44, 330, y + 28), 'The %s line: %s' % (p.upper(), sense)))
    caps = [O.cap(768, 58, 'THE PARTICLE FERRIES', '#2A1E0C', 36, face=O.SERIF, spacing='.04em', halo='#F0E3CE'),
            O.cap(768, 84, 'one line for each particle &#183; change at the big verbs', '#2A1E0C', 17, face=O.SERIF,
                  weight=600, spacing='0', style='italic', halo='#F0E3CE')]
    for v, x in zip(VERBS, XS):
        caps.append(O.cap(x, 200, v.upper(), INK, 25, face=O.SERIF, spacing='.04em', halo=O.mix(SEA, '#FFFFFF', .4)))
    for (p, sense, col, stops), y in zip(LINES, YS):
        dark = O.mix(col, '#000000', .3)
        caps.append(O.cap(56, y - 12, p.upper(), dark, 25, 'start', face=O.SERIF, spacing='.03em',
                          halo=O.mix(SEA, '#FFFFFF', .5)))
        caps.append(O.cap(56, y + 12, sense, INK, 14, 'start', weight=600, spacing='0', style='italic',
                          halo=O.mix(SEA, '#FFFFFF', .5)))
    caps.append(O.cap(768, 974, 'the same verb on a new line is a new meaning: take off &#183; take on &#183; take down',
                      '#2A1E0C', 17, face=O.SERIF, weight=600, spacing='0', style='italic', halo='#FAD9AA'))
    for (p, sense, col, stops), y in zip(LINES, YS):
        assert O.ratio(O.mix(col, '#000000', .3), SEA) >= 3, 'the %s line label is too faint' % p
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated chart of a busy bay with harbour towns on the north and south shores. Five coloured '
            'dashed ferry lines cross it west to east: UP, finish or more, in red; OUT, to the end or outside, in '
            'green; OFF, away or stop, in purple; ON, continue or connect, in ochre; DOWN, less or on paper, in blue. '
            'Four grey lines cross them north to south: GET, TAKE, PUT and TURN. At each of the twenty crossings a '
            'small island harbour is named: get up, take up, put up, turn up, and so on down to turn down.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; phrasal verbs', 'The Particle Ferries',
    'A phrasal verb is a big verb and a little word: <em>get</em> + <em>up</em>, <em>take</em> + <em>off</em>. On this '
    'chart each little word is a ferry line with its own colour and its own rough direction, and each big verb is '
    'a line that crosses them. Change lines and the meaning changes. Pick a verb, then ride every line.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the network</div>
      <h2>Big verbs, little words</h2>
      <p class="chart-note" style="margin:-6px 0 18px">The little word, the <em>particle</em>, often keeps a rough direction (UP is more, DOWN is less, OFF is away). Often, not always: some stops have to be learned as they are.</p>
      ''' + rule_grid([
    ('Same verb, new line, new meaning',
     '<em>Take off</em>, <em>take on</em> and <em>take down</em> are three different verbs. Learn each stop on its own.',
     ex('The plane <em>took off</em> at six.')),
    ('Same line, a family of meanings',
     'OFF often means <em>stop</em> or <em>away</em>: <em>turn off</em> the engine, <em>get off</em> the boat, <em>put off</em> the trip.',
     ex('<em>Turn off</em> the engine before you land.')),
    ('Many have a one-word twin',
     'The one-word verb is more formal: <em>put off</em> / <em>postpone</em>, <em>find out</em> / <em>discover</em>.',
     ex('We <em>put off</em> the trip until spring.')),
    ('Some can split around their object',
     'With a noun, either order works: <em>put on a jacket</em>, <em>put a jacket on</em>.',
     ex('<em>Put</em> your life jacket <em>on</em>.')),
    ('A pronoun always splits them',
     'With <em>it</em>, <em>them</em>, <em>her</em>, the pronoun goes in the middle: <em>put it on</em>, never <em>put on it</em>.',
     ex('It&#39;s cold: <em>put it on</em>.')),
    ('Some never split',
     '<em>Get on</em> the ferry, <em>get off</em> the bus, <em>get over</em> a cold: the object always comes after.',
     ex('We <em>got on</em> the ferry just in time.')),
]) + chart(
    'The twenty stops',
    'Read across a line to see one particle on four verbs; read down a column to see one verb on five lines.',
    ['', 'get', 'take', 'put', 'turn'],
    [['UP', 'leave your bed', 'start a hobby', 'raise', 'arrive'],
     ['OUT', 'leave', 'remove', 'stop a fire', 'end up'],
     ['OFF', 'leave a boat or bus', 'leave the ground', 'postpone', 'stop a machine'],
     ['ON', 'board', 'accept', 'dress in', 'start a machine'],
     ['DOWN', 'descend', 'write', 'place', 'refuse']]) + '''
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
    'Click a stop and its line lights up below; click a coloured line&#39;s name for its sense. Switch the chart to '
    'see what each stop means, then a sentence: the verb stays on its grey line, and the coloured line changes '
    'the meaning.',
    ('The stops', 'The meaning', 'In a sentence'),
    [('GET and TAKE', 'is-west'), ('PUT and TURN', 'is-isle'), ('The five lines', 'is-east')],
    'Drag the chart sideways to reach the TURN line.', min_zoom=1000)

TRAPS = fork(
    'Wrong platform',
    'Most mistakes put the pronoun on the wrong side, or take the wrong line.',
    ['Not this', 'This', 'Why'],
    [['Put on it.', 'Put it on.', 'a pronoun splits the verb'],
     ['Turn off them.', 'Turn them off.', 'a pronoun splits the verb'],
     ['Get the ferry on.', 'Get on the ferry.', '<em>get on</em> never splits'],
     ['The meeting was put down until Monday.', 'The meeting was put off until Monday.', '<em>put off</em> is postpone'],
     ['Turn on the music, it&#39;s too loud!', 'Turn down the music, it&#39;s too loud!', 'DOWN is less'],
     ['He turned at the party late.', 'He turned up at the party late.', '<em>turn up</em> is arrive']],
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
    ('I usually ___ at six, before the ferry leaves.', 'Leave your bed.', 'get up',
     ['get up', 'get off', 'get on', 'get down'], 'Get up: leave your bed.'),
    ('The plane ___ at 9.15.', 'Leave the ground.', 'took off',
     ['took off', 'took on', 'took up', 'took out'], 'Take off: a plane leaves the ground.'),
    ('We ___ the trip until the storm passed.', 'Postpone.', 'put off',
     ['put off', 'put down', 'put out', 'put on'], 'Put off: postpone.'),
    ('Please ___ the engine before you go ashore.', 'Stop a machine.', 'turn off',
     ['turn off', 'turn up', 'turn out', 'turn down'], 'Turn off: stop a machine.'),
    ('It&#39;s cold. Put your jacket on: put ___.', 'A pronoun splits the verb.', 'it on',
     ['it on', 'on it', 'it', 'on'], 'Put it on: the pronoun goes in the middle.'),
    ('We ___ the ferry just in time.', 'Board.', 'got on',
     ['got on', 'got the ferry on', 'got up', 'got in'], 'Get on a ferry, bus or train. It never splits.'),
    ('She was offered the job, but she ___.', 'Refuse.', 'turned it down',
     ['turned it down', 'turned down it', 'turned it off', 'turned it out'], 'Turn down: refuse. With it: turned it down.'),
    ('The firefighters ___ the fire.', 'Stop a fire.', 'put out',
     ['put out', 'put off', 'put down', 'turned out'], 'Put out a fire.'),
    ('He ___ two hours late.', 'Arrive.', 'turned up',
     ['turned up', 'turned on', 'got off', 'took up'], 'Turn up: arrive, often late or unexpectedly.'),
    ('The weather was terrible, but the trip ___ fine.', 'End up.', 'turned out',
     ['turned out', 'took out', 'got out', 'put out'], 'Turn out: end up, be in the end.'),
    ('My grandfather ___ sailing when he retired.', 'Start a hobby.', 'took up',
     ['took up', 'took on', 'got up', 'turned up'], 'Take up a hobby.'),
    ('Which sentence is NOT correct?', 'One pronoun is on the wrong side.', 'Turn off it, please.',
     ['Turn off it, please.', 'Turn it off, please.', 'Turn the light off, please.', 'Turn off the light, please.'],
     'With a pronoun: turn it off.'),
]

PANELS = [
    [(key(v, p), '<b>%s %s</b> %s &middot; %s' % (v, p, st[i][0], st[i][1]))
     for v, i in (('get', 0), ('take', 1)) for p, s, c, st in LINES],
    [(key(v, p), '<b>%s %s</b> %s &middot; %s' % (v, p, st[i][0], st[i][1]))
     for v, i in (('put', 2), ('turn', 3)) for p, s, c, st in LINES],
    [('line-' + p, '<b>%s</b> %s' % (p.upper(), s)) for p, s, c, st in LINES],
]
TARGETS = {}
for p, s, c, st in LINES:
    for i, v in enumerate(VERBS):
        TARGETS[key(v, p)] = (0 if i < 2 else 1, key(v, p), c)
    TARGETS['line-' + p] = (2, 'line-' + p, c)

import ex_tr_phrasal_verbs as T
L.build(OUT, ART, 'The Particle Ferries &mdash; Phrasal Verbs', 'phrasal verbs', EXTRACTED,
        HERO, 'Pick a verb, then ride every line.', ('order', 'Read the chart'),
        RULES + SPLIT + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        ['#C9C6C0', '#BFD7DE', '#E3CF9E'], T.T,
        ['Clean run. You can ride every line and get off at the right stop.',
         'Solid progress. Watch the pronoun: put it on, turn it off.',
         'Good first attempt. Start with one verb, get, and ride all five lines.'],
        ('sailing-the-seas-of-grammar.html', 'Back to the first chart: Gerundia and Infinitivia'), gull_seed=53,
        long_name=30)
