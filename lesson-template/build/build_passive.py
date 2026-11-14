# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: The Passive Ferry, the passive as a crossing.
The seventeenth chart.

    py lesson-template/build/build_passive.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. Activia is the shore where the doer comes first (They
build it). The ferry carries the object across to Passivia, where it comes
first (It is built). Six lanes, one per form: the verb BE takes the tense
and the main verb is always the past participle. The By-Buoy marks BY + the
doer, used only when it matters; the Land-locked Lake holds the verbs with
no object, which cannot cross (happen, arrive, die, seem); the Shallows hold
verbs with two objects, which have two passives.

TENSE COLOURS. Innes, 2026-11-13: anything involving a tense uses its Sherpa
colour. Each of the five tense lanes is painted in its colour on the chart,
and the page's panel rows carry the same colour as a disc, read from
sea_tense.T. The modal lane is not a tense and has none.

THE ART. Layout by sea_layouts_5.py, painted by Codex on 2026-11-14.
sea_measure.py found the 12 harbour dots and one stray on the By-Buoy
(passive_chart.json); the stray is dropped by position below.
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE
from sea_tense import T as TENSE

OUT = 'sailing-the-seas-passive.html'
ART = 'sailing-the-seas-passive'
UID = 'pass'

# py lesson-template/extract-palette.py sailing-the-seas-passive/hero.jpg --light
EXTRACTED = {'text': '#2a2311', 'text-dim': '#5e522e', 'secondary': '#a9cddc', 'contrast': '#09526d'}

D = O.load('passive_chart.json')
WEST = sorted((tuple(p) for p in D['dots'] if abs(p[0] - 269) < 12), key=lambda p: p[1])
EAST = sorted((tuple(p) for p in D['dots'] if abs(p[0] - 1266) < 12), key=lambda p: p[1])
assert (len(WEST), len(EAST)) == (6, 6), D['dots']

# (key, active, passive, the lane's name, its Sherpa tense or None, BE in that form)
PAIRS = [('present', 'They build it.', 'It is built.', 'present simple', 'present-simple', 'is / are'),
         ('past', 'They built it.', 'It was built.', 'past simple', 'past-simple', 'was / were'),
         ('perfect', 'They have built it.', 'It has been built.', 'present perfect', 'present-perfect', 'has / have been'),
         ('future', 'They will build it.', 'It will be built.', 'future simple', 'future-simple', 'will be'),
         ('continuous', 'They are building it.', 'It is being built.', 'present continuous', 'present-continuous',
          'is / are being'),
         ('modal', 'They can build it.', 'It can be built.', 'a modal', None, 'can be')]
INK, WEST_LAND, EAST_LAND, SAND = '#20180A', '#C2C27C', '#F4C885', '#FCD89D'


def disc(tense):
    """The lane's Sherpa colour as a small disc in a panel row."""
    if not tense:
        return ''
    # no double quotes: sea_lesson puts panel lines in a JS string, so the
    # attribute is unquoted (valid HTML while it holds no space)
    return '<i style=color:#%02X%02X%02X;font-style:normal;margin-right:.35em>&#9679;</i>' % TENSE[tense]


def overlay():
    spots, names = [], []
    for (key, act, pas, lane, tense, be), (wx, wy), (ex_, ey) in zip(PAIRS, WEST, EAST):
        names.append(O.name(wx, wy, (act, lane, 'the doer first'), INK, WEST_LAND, size=18, dy=-19, fit=False, halo=.25))
        names.append(O.name(ex_, ey, (pas, 'BE: ' + be, be + ' + built'), INK, EAST_LAND, size=18, dy=-19, fit=False,
                            halo=.25))
        spots.append(O.hotspot(UID, 'a-' + key, O.circle_path(wx, wy, 32), '%s Active, %s' % (act, lane)))
        spots.append(O.hotspot(UID, 'p-' + key, O.circle_path(ex_, ey, 32), '%s Passive, %s' % (pas, lane)))
    spots.append(O.hotspot(UID, 'buoy', O.rect_path(592, 123, 937, 242), 'The By-Buoy: by, only if it matters'))
    spots.append(O.hotspot(UID, 'lake', O.rect_path(40, 840, 500, 980), 'The Land-locked Lake: verbs with no passive'))
    spots.append(O.hotspot(UID, 'shallows', O.rect_path(553, 828, 981, 985), 'The Shallows: two passives'))
    spots.append(O.hotspot(UID, 'cape', O.rect_path(1040, 830, 1500, 990), 'The False Cape: I was born'))
    sea_ink = '#0F2F3D'
    caps = [O.cap(768, 60, 'THE PASSIVE FERRY', sea_ink, 40, face=O.SERIF, spacing='.05em'),
            O.cap(768, 96, 'the object sails to the front: be + past participle', sea_ink, 19, face=O.SERIF, weight=600,
                  spacing='0', style='italic'),
            O.cap(269, 150, 'ACTIVIA', INK, 30, face=O.SERIF, spacing='.03em', halo=WEST_LAND),
            O.cap(269, 178, 'who does it comes first', INK, 15, weight=600, spacing='0', style='italic', halo=WEST_LAND),
            O.cap(1266, 150, 'PASSIVIA', INK, 30, face=O.SERIF, spacing='.03em', halo=EAST_LAND),
            O.cap(1266, 178, 'what it happens to comes first', INK, 15, weight=600, spacing='0', style='italic',
                  halo=EAST_LAND),
            O.cap(764, 172, 'BY-BUOY', INK, 17, face=O.SERIF, spacing='.04em'),
            O.cap(764, 194, 'by &#8230; : only if it matters', INK, 13, weight=600, spacing='0', style='italic'),
            O.cap(270, 908, 'THE LAND-LOCKED LAKE', sea_ink, 16, face=O.SERIF, spacing='.03em'),
            O.cap(270, 932, 'happen &#183; arrive &#183; die &#183; seem: no passive', sea_ink, 13, weight=600, spacing='0',
                  style='italic'),
            O.cap(768, 898, 'THE SHALLOWS', INK, 17, face=O.SERIF, spacing='.04em'),
            O.cap(768, 922, 'I was given a book. A book was given to me.', INK, 13, weight=600, spacing='0', style='italic'),
            O.cap(1270, 966, 'THE FALSE CAPE: I was born in Lima.', INK, 15, face=O.SERIF, weight=700, spacing='0',
                  halo=EAST_LAND)]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated chart with two shores and six ferry lanes between them. On the green west shore, Activia: They '
            'build it, They built it, They have built it, They will build it, They are building it, They can build it. '
            'On the sandy east shore, Passivia: It is built, It was built, It has been built, It will be built, It is '
            'being built, It can be built. Five of the lanes are coloured by tense. A small island at the top is the '
            'By-Buoy; a lake in the south-west holds verbs with no passive; a sandbank holds I was given a book; a '
            'spit with a red flag says I was born in Lima.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; The passive', 'The Passive Ferry',
    'In Activia the doer comes first: <em>They built the bridge</em>. Put the bridge on the ferry and it lands in '
    'Passivia at the front of the sentence: <em>The bridge was built</em>. The crossing is always the same: BE takes '
    'the tense, and the main verb becomes the past participle. Read each lane across, then learn what cannot cross.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the crossing</div>
      <h2>BE takes the tense, the verb stays the same</h2>
      <p class="chart-note" style="margin:-6px 0 18px">On every lane the last word is the same: <em>built</em>. Only BE changes. Find the tense of the active sentence, put BE in that tense, and add the past participle.</p>
      ''' + rule_grid([
    ('The present simple lane',
     '<em>is / are</em> + past participle.',
     ex('The boats <em>are built</em> in this yard.')),
    ('The past simple lane',
     '<em>was / were</em> + past participle.',
     ex('The bridge <em>was built</em> in 1890.')),
    ('The present perfect lane',
     '<em>has / have been</em> + past participle.',
     ex('A new harbour <em>has been built</em>.')),
    ('The future lane',
     '<em>will be</em> + past participle.',
     ex('The ferry <em>will be repaired</em> next week.')),
    ('The present continuous lane',
     '<em>is / are being</em> + past participle. Do not lose <em>being</em>.',
     ex('The road <em>is being repaired</em> at the moment.')),
    ('The modal lane',
     'modal + <em>be</em> + past participle.',
     ex('Tickets <em>can be bought</em> on board.')),
]) + chart(
    'The six lanes',
    'Read each row across the water.',
    ['Lane', 'Activia', 'Passivia', 'BE'],
    [[lane, act, pas, be] for _, act, pas, lane, _, be in PAIRS]) + '''
    </div>

    '''

EXTRAS = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The buoy, the lake, the Shallows and the Cape</div>
      <h2>Who did it, and what cannot cross</h2>
      <p class="chart-note" style="margin:-6px 0 18px">The passive is for when the doer is unknown, obvious or unimportant. That is why most passives have no <em>by</em> at all.</p>
      ''' + chart(
    'The By-Buoy: add the doer only if it matters',
    'Leave <em>by</em> out when the doer is people in general, or obvious.',
    ['Sentence', 'By?', 'Why'],
    [['My bike was stolen.', 'no', 'we do not know who'], ['English is spoken here.', 'no', 'people in general'],
     ['He was arrested.', 'no', 'obvious: the police'],
     ['The bridge was designed by Brunel.', 'yes', 'the doer is the news']]) + '''
      ''' + exi('The bridge <em>was designed by</em> Brunel.') + chart(
    'The Land-locked Lake, the Shallows and the False Cape',
    'Three things the ferry does differently.',
    ['Where', 'What happens', 'Example'],
    [['The Land-locked Lake', 'a verb with no object has no passive', 'It happened. (not: It was happened.)'],
     ['The Land-locked Lake', 'the same for <em>arrive</em>, <em>die</em>, <em>seem</em>', 'He died in 1950. (not: He was died.)'],
     ['The Shallows', 'a verb with two objects has two passives', 'I was given a book. / A book was given to me.'],
     ['The False Cape', '<em>be born</em> is always passive', 'I was born in Lima. (not: I born / I am born)']]) + '''
      ''' + exi('I <em>was born</em> in Lima, and I <em>was given</em> this name by my grandmother.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a harbour and its line lights up below: Activia on the left, Passivia in the middle. The disc beside '
    'each line is the lane&#8217;s tense colour. Switch the chart to see each lane&#8217;s name and its form of BE.',
    ('The sentences', 'The lane', 'The form'),
    [('Activia', 'is-west'), ('Passivia', 'is-isle'), ('The buoy, the lake, the Shallows, the Cape', 'is-east')],
    'Drag the chart sideways to reach Passivia.', min_zoom=1000)

TRAPS = fork(
    'Lost in the crossing',
    'Each of these loses a piece of the passive on the way.',
    ['Not this', 'This', 'Why'],
    [['The bridge built in 1890.', 'The bridge was built in 1890.', 'BE is missing'],
     ['The road is repairing.', 'The road is being repaired.', '<em>being</em> + past participle'],
     ['A new harbour has built.', 'A new harbour has been built.', '<em>been</em> is missing'],
     ['It was happened yesterday.', 'It happened yesterday.', 'the Land-locked Lake'],
     ['I am born in Lima.', 'I was born in Lima.', 'the False Cape: always past'],
     ['The letter was wrote by Ana.', 'The letter was written by Ana.', 'the third form, not the second']],
    'Count the words: every passive has a form of BE and a past participle. If one is missing, the ferry has sunk.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-regularia.html', 'Regularia &amp; Irregularia: the third forms')])

SIGNALS = signals(
    'Stay in Activia',
    ['the doer is the topic', 'you are telling a story', 'the verb has no object', '<em>happen</em>, <em>arrive</em>, <em>seem</em>',
     'short, direct sentences', '<em>Brunel designed the bridge.</em>'],
    'Take the ferry',
    ['the doer is unknown: <em>was stolen</em>', 'the doer is obvious: <em>was arrested</em>', 'the thing is the topic',
     'processes: <em>is made</em>, <em>are picked</em>', 'news and reports', '<em>The bridge was designed by Brunel.</em>'],
    'One test: what is the sentence about? If it is about the bridge, start with the bridge.')

QUIZ = [
    ('These boats ___ in Scotland.', 'Present simple lane.', 'are built',
     ['are built', 'is built', 'are build', 'built'], 'Are + past participle: are built.'),
    ('The bridge ___ in 1890.', 'Past simple lane.', 'was built',
     ['was built', 'is built', 'built', 'was build'], 'Was + past participle: was built.'),
    ('A new harbour ___ since my last visit.', 'Present perfect lane.', 'has been built',
     ['has been built', 'has built', 'was been built', 'has being built'], 'Has been + past participle.'),
    ('The ferry ___ next week.', 'Future lane.', 'will be repaired',
     ['will be repaired', 'will repaired', 'will be repair', 'will repairing'], 'Will be + past participle.'),
    ('Careful: the road ___ at the moment.', 'Present continuous lane.', 'is being repaired',
     ['is being repaired', 'is repairing', 'is been repaired', 'being repaired'], 'Is being + past participle.'),
    ('Tickets ___ on board.', 'Modal lane.', 'can be bought',
     ['can be bought', 'can bought', 'can be buy', 'can been bought'], 'Modal + be + past participle.'),
    ('The letter was ___ by Ana.', 'The third form.', 'written',
     ['written', 'wrote', 'write', 'writing'], 'The past participle: written.'),
    ('My bike ___ last night.', 'We do not know who did it.', 'was stolen',
     ['was stolen', 'stole', 'was stole', 'is stealing'], 'Was stolen: no by, because the thief is unknown.'),
    ('Which sentence is right?', 'The Land-locked Lake.', 'The accident happened at noon.',
     ['The accident happened at noon.', 'The accident was happened at noon.', 'The accident is happened at noon.',
      'The accident was happen at noon.'], 'Happen has no object, so it has no passive.'),
    ('I ___ in Lima.', 'The False Cape.', 'was born',
     ['was born', 'am born', 'born', 'have born'], 'Be born is always passive, and always past for your own birth.'),
    ('Which needs &#8220;by&#8221;?', 'The By-Buoy.', 'The bridge was designed ___ Brunel.',
     ['The bridge was designed ___ Brunel.', 'English is spoken ___ here.', 'My bike was stolen ___ last night.',
      'He was arrested ___ on Friday.'], 'Add by only when the doer matters: by Brunel.'),
    ('Which is also right? &#8220;They gave me a book.&#8221;', 'The Shallows.', 'I was given a book.',
     ['I was given a book.', 'I was gave a book.', 'I given a book.', 'I am give a book.'],
     'Two objects, two passives: I was given a book / A book was given to me.'),
]

PANELS = [
    [('a-' + key, '%s<b>%s</b> %s' % (disc(tense), lane, act)) for key, act, _, lane, tense, _ in PAIRS],
    [('p-' + key, '%s<b>%s</b> %s' % (disc(tense), be, pas)) for key, _, pas, _, tense, be in PAIRS],
    [('buoy', '<b>The By-Buoy</b> <em>by</em> + the doer, only if it matters'),
     ('lake', '<b>The Land-locked Lake</b> <em>happen</em>, <em>arrive</em>, <em>die</em>, <em>seem</em>: no passive'),
     ('shallows', '<b>The Shallows</b> <em>I was given a book. A book was given to me.</em>'),
     ('cape', '<b>The False Cape</b> <em>I was born in Lima.</em>')],
]
TARGETS = {}
for key, _, _, _, _, _ in PAIRS:
    TARGETS['a-' + key] = (0, 'a-' + key, '#09526d')
    TARGETS['p-' + key] = (1, 'p-' + key, '#09526d')
for key in ('buoy', 'lake', 'shallows'):
    TARGETS[key] = (2, key, '#09526d')
TARGETS['cape'] = (2, 'cape', '#B4441F')

import ex_tr_passive as T
L.build(OUT, ART, 'The Passive Ferry &mdash; The Passive', 'The passive', EXTRACTED,
        HERO, 'then learn what cannot cross.', ('order', 'Read the chart'),
        RULES + EXTRAS + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        [WEST_LAND, EAST_LAND, SAND], T.T,
        ['Clean run. Every lane crossed: BE in the right tense, and the past participle.',
         'Solid progress. Check the continuous and perfect lanes: being and been.',
         'Good first attempt. Start with two lanes: is built and was built.'],
        ('sailing-the-seas-backshift.html', 'Next chart: the Backshift Current'), gull_seed=71, long_name=24)
