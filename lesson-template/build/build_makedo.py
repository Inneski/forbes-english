# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: Makeland & Doland, MAKE or DO as two shores.
The fifteenth chart.

    py lesson-template/build/build_makedo.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. Makeland is where you create something that was not
there before: a decision, a mistake, a plan, a noise. Doland is tasks, jobs
and activities: homework, the dishes, research, the shopping. Take Island
holds the nouns that take neither (take a photo, a break, a seat), and the
False Cape names the classic transfer error from German MACHEN and its
cousins: not "make a photo".

No tense on this chart, so no Sherpa colours.

THE ART. Layout by sea_layouts_5.py, painted by Codex on 2026-11-14.
sea_measure.py found the 19 harbour dots and one stray in the scenery
(make-do_chart.json); the stray is dropped by position below.
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE

OUT = 'sailing-the-seas-make-do.html'
ART = 'sailing-the-seas-make-do'
UID = 'makedo'

# py lesson-template/extract-palette.py sailing-the-seas-make-do/hero.jpg --light
EXTRACTED = {'text': '#2a1f11', 'text-dim': '#5e492e', 'secondary': '#add0dc', 'contrast': '#074e55'}

D = O.load('make-do_chart.json')
WEST = sorted((tuple(p) for p in D['dots'] if abs(p[0] - 292) < 12), key=lambda p: p[1])
EAST = sorted((tuple(p) for p in D['dots'] if abs(p[0] - 1249) < 14), key=lambda p: p[1])
ISLE = sorted((tuple(p) for p in D['dots'] if abs(p[0] - 756) < 12), key=lambda p: p[1])
assert (len(WEST), len(EAST), len(ISLE)) == (8, 8, 3), D['dots']

# (noun, sentence)
MAKE = [('a decision', 'We have to make a decision.'), ('a mistake', 'I made a mistake.'),
        ('money', 'They make money from tourists.'), ('a plan', 'Let&#8217;s make a plan.'),
        ('progress', 'She is making progress.'), ('friends', 'He makes friends easily.'),
        ('a noise', 'Don&#8217;t make a noise.'), ('an effort', 'Please make an effort.')]
DO = [('homework', 'I do my homework at six.'), ('the dishes', 'Who is doing the dishes?'),
      ('business', 'We do business with them.'), ('a favour', 'Can you do me a favour?'),
      ('your best', 'Just do your best.'), ('research', 'She does research on whales.'),
      ('damage', 'The storm did a lot of damage.'), ('the shopping', 'I do the shopping on Fridays.')]
TAKE = [('a photo', 'Can you take a photo of us?'), ('a break', 'Let&#8217;s take a break.'),
        ('a seat', 'Please take a seat.')]
INK, WEST_LAND, EAST_LAND, SAND = '#20180A', '#E4A863', '#C5BD74', '#EACA8C'


def k(side, noun):
    return side + '-' + noun.replace('the ', '').replace('an ', '').replace('a ', '').replace('your ', '').replace(' ', '-')


def overlay():
    spots, names = [], []
    for (m, d), (wx, wy), (ex_, ey) in zip(zip(MAKE, DO), WEST, EAST):
        names.append(O.name(wx, wy, ('make ' + m[0], 'you create it', m[1]), INK, WEST_LAND, size=18, dy=-15, fit=False,
                            halo=.2))
        names.append(O.name(ex_, ey, ('do ' + d[0], 'a task or activity', d[1]), INK, EAST_LAND, size=18, dy=-15,
                            fit=False, halo=.2))
        spots.append(O.hotspot(UID, k('m', m[0]), O.circle_path(wx, wy, 30), 'make %s' % m[0]))
        spots.append(O.hotspot(UID, k('d', d[0]), O.circle_path(ex_, ey, 30), 'do %s' % d[0]))
    for t, (x, y) in zip(TAKE, ISLE):
        names.append(O.name(x, y, ('take ' + t[0], 'neither: take', t[1]), INK, SAND, size=18, dy=-15, fit=False, halo=.2))
        spots.append(O.hotspot(UID, k('t', t[0]), O.circle_path(x, y, 30), 'take %s' % t[0]))
    spots.append(O.hotspot(UID, 'cape', O.rect_path(580, 660, 950, 880), 'The False Cape: not make a photo'))
    sea_ink = '#0F2F3D'
    caps = [O.cap(768, 62, 'MAKELAND &amp; DOLAND', sea_ink, 40, face=O.SERIF, spacing='.05em'),
            O.cap(768, 98, 'make it or do it? read the shore', sea_ink, 20, face=O.SERIF, weight=600, spacing='0',
                  style='italic'),
            O.cap(292, 158, 'MAKELAND', INK, 30, face=O.SERIF, spacing='.03em', halo=WEST_LAND),
            O.cap(292, 186, 'you create it', INK, 16, weight=600, spacing='0', style='italic', halo=WEST_LAND),
            O.cap(1249, 158, 'DOLAND', INK, 30, face=O.SERIF, spacing='.03em', halo=EAST_LAND),
            O.cap(1249, 186, 'it is a task, a job, an activity', INK, 16, weight=600, spacing='0', style='italic',
                  halo=EAST_LAND),
            O.cap(756, 306, 'TAKE ISLAND', INK, 21, face=O.SERIF, spacing='.04em'),
            O.cap(768, 826, 'THE FALSE CAPE', sea_ink, 21, face=O.SERIF, spacing='.04em'),
            O.cap(768, 856, 'not make a photo but take a photo (German: machen)', sea_ink, 16, weight=600, spacing='0',
                  style='italic')]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated chart with two shores. On the orange west shore, Makeland, eight harbours: make a decision, '
            'a mistake, money, a plan, progress, friends, a noise and an effort. On the green east shore, Doland, '
            'eight more: do homework, the dishes, business, a favour, your best, research, damage and the shopping. '
            'In the channel, Take Island holds take a photo, take a break and take a seat. A spit with a red flag is '
            'the False Cape: not make a photo but take a photo.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; Make or do', 'Makeland &amp; Doland',
    'You <em>make</em> a mistake but <em>do</em> your homework. Many languages have one verb for both, so English '
    'learners guess. There is a pattern: you make what you create, and you do a task or an activity. '
    'Read the two shores, then stop at Take Island before you make a photo.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the two shores</div>
      <h2>Create it, or carry it out?</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Ask what is there at the end. If something new exists, you made it. If a job is finished, you did it.</p>
      ''' + rule_grid([
    ('Make: something new exists',
     'A decision, a plan, a list, a cake: it was not there before.',
     ex('We have to <em>make a decision</em> today.')),
    ('Make: sounds, mistakes and money',
     'You also make what you produce or cause: a noise, a mistake, a mess, money, progress.',
     ex('I <em>made a mistake</em> in the first line.')),
    ('Make: with people',
     'Friends, a promise, a phone call, an effort: what you offer or build with others.',
     ex('He <em>makes friends</em> easily.')),
    ('Do: work and study',
     'Homework, research, business, a course, an exam, a job.',
     ex('She <em>does research</em> on whales.')),
    ('Do: jobs around the house',
     'The dishes, the shopping, the washing, the cleaning. Note <em>the</em>.',
     ex('Who is <em>doing the dishes</em> tonight?')),
    ('Do: with general words',
     'Something, nothing, anything, your best, a favour, well, badly.',
     ex('Can you <em>do me a favour</em>?')),
]) + chart(
    'The sixteen harbours',
    'Read each row across the channel.',
    ['Makeland', 'Doland', 'More of the same'],
    [['make ' + m[0], 'do ' + d[0], x] for m, d, x in zip(MAKE, DO, [
        'make a choice / do an exam', 'make a mess / do the washing', 'make a profit / do a job',
        'make a list / do a course', 'make a difference / do well', 'make a promise / do nothing',
        'make a phone call / do harm', 'make an excuse / do the cleaning'])]) + '''
    </div>

    '''

ISLE_HTML = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Take Island and the False Cape</div>
      <h2>Neither make nor do</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Some nouns belong to a third verb. If your own language says &#8220;make a photo&#8221; or &#8220;make a break&#8221;, this island is for you.</p>
      ''' + chart(
    'Take Island',
    'These take <em>take</em>. A few also take <em>have</em>.',
    ['Say', 'Not', 'Also'],
    [['take a photo', 'make a photo', 'take a picture'], ['take a break', 'make a break', 'have a break'],
     ['take a seat', 'make a seat', 'have a seat'], ['take a shower', 'make a shower', 'have a shower'],
     ['take an exam', 'make an exam', 'do an exam'], ['take notes', 'do notes', 'make notes']]) + '''
      ''' + exi('Let&#39;s <em>take a break</em> and <em>take a photo</em> of the harbour.') + chart(
    'The False Cape: the usual wrecks',
    'Each of these is a direct translation that does not work in English.',
    ['Not this', 'This', 'Why'],
    [['make a photo', 'take a photo', 'Take Island'], ['make a party', 'have a party', 'have, for events'],
     ['make sport', 'do sport', 'an activity: do'], ['do a mistake', 'make a mistake', 'you produce it: make'],
     ['make homework', 'do homework', 'a task: do']]) + '''
      ''' + exi('I <em>do sport</em> twice a week, and I always <em>make</em> the same <em>mistake</em>.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a harbour and its line lights up below: Makeland on the left, Doland in the middle, Take Island on the '
    'right. Switch the chart to see why each harbour is on its shore, then each phrase in a sentence.',
    ('The phrases', 'Why this shore', 'In a sentence'),
    [('Makeland', 'is-west'), ('Doland', 'is-isle'), ('Take Island and the False Cape', 'is-east')],
    'Drag the chart sideways to reach Doland.', min_zoom=1000)

TRAPS = fork(
    'Wrong shore',
    'Each of these lands on the wrong side.',
    ['Not this', 'This', 'Why'],
    [['I did a mistake.', 'I made a mistake.', 'you produce it'],
     ['She makes her homework.', 'She does her homework.', 'a task'],
     ['Can you make me a favour?', 'Can you do me a favour?', 'a general word: do'],
     ['We have to do a decision.', 'We have to make a decision.', 'something new exists'],
     ['Don&#39;t do a noise.', 'Don&#39;t make a noise.', 'you cause it'],
     ['He made a photo of the boat.', 'He took a photo of the boat.', 'Take Island']],
    'These are collocations: the noun chooses the verb. Learn the noun with its verb, as one phrase.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-statia.html', 'Statia &amp; Actia')])

SIGNALS = signals(
    'You are in Makeland',
    ['something new exists at the end', 'a decision, a plan, a list', 'a noise, a mess, a mistake', 'money, a profit, progress',
     'friends, a promise, a phone call', 'food and drink: <em>make dinner</em>'],
    'You are in Doland',
    ['a job is finished at the end', 'homework, research, an exam', 'the dishes, the shopping, the washing',
     'business, a job, a course', '<em>something</em>, <em>nothing</em>, <em>your best</em>', 'sport and exercise'],
    'One test: can you point at the result? You can point at a list or a mess. You cannot point at &#8220;the shopping&#8221;.')

QUIZ = [
    ('We need to ___ a decision before Friday.', 'Something new exists.', 'make',
     ['make', 'do', 'take', 'have'], 'You create a decision: make a decision.'),
    ('I always ___ my homework after dinner.', 'A task.', 'do',
     ['do', 'make', 'take', 'have'], 'Homework is a task: do homework.'),
    ('Sorry, I ___ a mistake in the bill.', 'You produce it.', 'made',
     ['made', 'did', 'took', 'had'], 'Make a mistake.'),
    ('Could you ___ me a favour?', 'A general word.', 'do',
     ['do', 'make', 'take', 'give'], 'Do someone a favour.'),
    ('The children are ___ too much noise.', 'You cause it.', 'making',
     ['making', 'doing', 'taking', 'having'], 'Make a noise.'),
    ('Who is ___ the dishes tonight?', 'A job in the house.', 'doing',
     ['doing', 'making', 'taking', 'having'], 'Do the dishes.'),
    ('She is ___ good progress with her English.', 'You produce it.', 'making',
     ['making', 'doing', 'taking', 'having'], 'Make progress.'),
    ('Just ___ your best. That is enough.', 'A general word.', 'do',
     ['do', 'make', 'take', 'have'], 'Do your best.'),
    ('Can you ___ a photo of us?', 'Take Island.', 'take',
     ['take', 'make', 'do', 'give'], 'Take a photo, not make a photo.'),
    ('The storm ___ a lot of damage.', 'Doland.', 'did',
     ['did', 'made', 'took', 'had'], 'Do damage.'),
    ('He ___ friends very quickly at his new school.', 'With people.', 'made',
     ['made', 'did', 'took', 'got'], 'Make friends.'),
    ('Which sentence is right?', 'Check both verbs.', 'I did the shopping and made a list for tomorrow.',
     ['I did the shopping and made a list for tomorrow.', 'I made the shopping and did a list for tomorrow.',
      'I did the shopping and did a list for tomorrow.', 'I made the shopping and made a list for tomorrow.'],
     'Do the shopping (a job); make a list (something new).'),
]

PANELS = [
    [(k('m', m[0]), '<b>make %s</b> %s' % (m[0], m[1])) for m in MAKE],
    [(k('d', d[0]), '<b>do %s</b> %s' % (d[0], d[1])) for d in DO],
    [(k('t', t[0]), '<b>take %s</b> %s' % (t[0], t[1])) for t in TAKE] +
    [('cape', '<b>The False Cape</b> not <em>make a photo</em> but <em>take a photo</em>')],
]
TARGETS = {}
for m in MAKE:
    TARGETS[k('m', m[0])] = (0, k('m', m[0]), '#074e55')
for d in DO:
    TARGETS[k('d', d[0])] = (1, k('d', d[0]), '#074e55')
for t in TAKE:
    TARGETS[k('t', t[0])] = (2, k('t', t[0]), '#074e55')
TARGETS['cape'] = (2, 'cape', '#B4441F')

import ex_tr_makedo as T
L.build(OUT, ART, 'Makeland &amp; Doland &mdash; Make or Do', 'Make or do', EXTRACTED,
        HERO, 'before you make a photo.', ('order', 'Read the chart'),
        RULES + ISLE_HTML + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        [WEST_LAND, EAST_LAND, SAND], T.T,
        ['Clean run. You know which shore each noun lives on.',
         'Solid progress. Ask what is there at the end: something new, or a finished job?',
         'Good first attempt. Start with Doland: homework, the dishes, the shopping.'],
        ('sailing-the-seas-certainty.html', 'Next chart: Soundings of Certainty'), gull_seed=61, long_name=22)
