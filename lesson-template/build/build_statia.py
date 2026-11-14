# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: Statia & Actia, state and action verbs as
two shores. The fourteenth chart.

    py lesson-template/build/build_statia.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. The west shore, Statia, holds verbs that usually stay in
the present simple (know, believe, want). The east shore, Actia, holds verbs
that take IS/ARE + -ING for now (run, cook, read). Twofold Isle holds the
verbs whose answer depends on the sentence (think, have, see, be), which is
the real lesson: THE TEST is whether IS/ARE + -ING works in THIS sentence,
not whether the verb is on a list. The Shallows hold feel and hurt, which
take either form with the same meaning.

TENSE COLOURS. Innes, 2026-11-13: anything involving a tense uses its Sherpa
colour. Statia is the present simple and Actia the present continuous; the
shores are painted in those colours and the page's panels take them from
sea_tense.T, never typed.

THE ART. Layout by sea_layouts_5.py, painted by Codex on 2026-11-14.
sea_measure.py found the 20 harbour dots and one stray in the scenery
(statia_chart.json); the stray is dropped by position below.
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE
from sea_tense import T as TENSE

OUT = 'sailing-the-seas-statia.html'
ART = 'sailing-the-seas-statia'
UID = 'statia'

# py lesson-template/extract-palette.py sailing-the-seas-statia/hero.jpg --light
EXTRACTED = {'text': '#2a2111', 'text-dim': '#5e4d2e', 'secondary': '#aecbd4', 'contrast': '#095c6d'}


def hexof(rgb):
    return '#%02X%02X%02X' % rgb


SIMPLE, CONT = hexof(TENSE['present-simple']), hexof(TENSE['present-continuous'])

D = O.load('statia_chart.json')
WEST = sorted((tuple(p) for p in D['dots'] if abs(p[0] - 278) < 12), key=lambda p: p[1])
EAST = sorted((tuple(p) for p in D['dots'] if abs(p[0] - 1260) < 12), key=lambda p: p[1])
ISLE = sorted((tuple(p) for p in D['dots'] if abs(p[0] - 768) < 12), key=lambda p: p[1])
assert (len(WEST), len(EAST), len(ISLE)) == (8, 8, 4), D['dots']

# (verb, sentence)
STATIA = [('know', 'I know the way.'), ('believe', 'I believe you.'), ('want', 'She wants a coffee.'),
          ('belong', 'This bag belongs to me.'), ('need', 'We need more time.'),
          ('understand', 'I understand the problem.'), ('prefer', 'He prefers tea.'), ('own', 'They own a boat.')]
ACTIA = [('run', 'He is running for the bus.'), ('cook', 'She is cooking dinner.'), ('read', 'I am reading a novel.'),
         ('build', 'They are building a shed.'), ('swim', 'The children are swimming.'),
         ('write', 'I am writing an email.'), ('sail', 'We are sailing home.'), ('eat', 'They are eating lunch.')]
# (verb, the state sentence, the action sentence)
TWOFOLD = [('think', 'I think so.', 'I&#8217;m thinking about it.'),
           ('have', 'I have a boat.', 'I&#8217;m having lunch.'),
           ('see', 'I see what you mean.', 'I&#8217;m seeing Ana tonight.'),
           ('be', 'He is silly.', 'He&#8217;s being silly today.')]
INK, WEST_LAND, EAST_LAND, SAND = '#20180A', '#A0ADB3', '#E5B1AF', '#F9CF89'


def overlay():
    spots, names = [], []
    for (s, a), (wx, wy), (ex_, ey) in zip(zip(STATIA, ACTIA), WEST, EAST):
        names.append(O.name(wx, wy, (s[0], 'no -ING', s[1]), INK, WEST_LAND, size=19, dy=-15, fit=False, halo=.25))
        names.append(O.name(ex_, ey, (a[0], '-ING for now', a[1]), INK, EAST_LAND, size=19, dy=-15, fit=False, halo=.25))
        spots.append(O.hotspot(UID, 's-' + s[0], O.circle_path(wx, wy, 30), '%s: usually no -ING' % s[0]))
        spots.append(O.hotspot(UID, 'a-' + a[0], O.circle_path(ex_, ey, 30), '%s: -ING for now' % a[0]))
    for (v, st, ac), (x, y) in zip(TWOFOLD, ISLE):
        names.append(O.name(x, y, (v, 'the sentence decides', '%s &#183; %s' % (st, ac)), INK, SAND, size=18, dy=-14,
                            fit=False, halo=.2))
        spots.append(O.hotspot(UID, 't-' + v, O.circle_path(x, y, 30), '%s: the sentence decides' % v))
    spots.append(O.hotspot(UID, 'shallows', O.rect_path(590, 670, 940, 750), 'The Shallows: either form, same meaning'))
    spots.append(O.hotspot(UID, 'test', O.rect_path(560, 760, 960, 980), 'The test: does IS/ARE + -ING work in this sentence?'))
    sea_ink = '#0F2F3D'
    caps = [O.cap(768, 58, 'STATIA &amp; ACTIA', sea_ink, 40, face=O.SERIF, spacing='.05em'),
            O.cap(768, 92, 'a state or an action? ask the sentence, not the verb', sea_ink, 19, face=O.SERIF, weight=600,
                  spacing='0', style='italic'),
            O.cap(278, 162, 'STATIA', INK, 30, face=O.SERIF, spacing='.03em', halo=WEST_LAND),
            O.cap(278, 190, 'usually no -ING: I know the way.', INK, 15, weight=600, spacing='0', style='italic',
                  halo=WEST_LAND),
            O.cap(1260, 162, 'ACTIA', INK, 30, face=O.SERIF, spacing='.03em', halo=EAST_LAND),
            O.cap(1260, 190, '-ING for now: I&#8217;m sailing.', INK, 15, weight=600, spacing='0', style='italic',
                  halo=EAST_LAND),
            O.cap(768, 250, 'TWOFOLD ISLE', INK, 21, face=O.SERIF, spacing='.04em'),
            O.cap(768, 274, 'the sentence decides', INK, 15, weight=600, spacing='0', style='italic'),
            O.cap(768, 702, 'THE SHALLOWS', INK, 20, face=O.SERIF, spacing='.04em'),
            O.cap(768, 728, 'feel &#183; hurt: either, same meaning', INK, 15, weight=600, spacing='0', style='italic'),
            O.cap(768, 936, 'THE TEST', sea_ink, 21, face=O.SERIF, spacing='.04em'),
            O.cap(768, 964, 'does IS/ARE + -ING work in THIS sentence?', sea_ink, 16, weight=600, spacing='0',
                  style='italic')]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated chart with two shores. On the blue-grey west shore, Statia, eight harbours: know, believe, '
            'want, belong, need, understand, prefer and own. On the pink east shore, Actia, eight more: run, cook, '
            'read, build, swim, write, sail and eat. In the channel, Twofold Isle holds think, have, see and be, each '
            'with two sentences. Below it a sandbank, the Shallows, says feel and hurt take either form. A spit with '
            'a red flag carries the test: does IS/ARE + -ING work in this sentence?')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; State and action verbs', 'Statia &amp; Actia',
    'Some verbs name a state: you <em>know</em>, you <em>want</em>, you <em>own</em>. Others name an action: you '
    '<em>run</em>, you <em>cook</em>, you <em>sail</em>. States usually stay in the present simple; actions take '
    'IS/ARE + -ING for now. Read the two shores, then cross to Twofold Isle, where the sentence decides.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the two shores</div>
      <h2>A state stays, an action happens</h2>
      <p class="chart-note" style="margin:-6px 0 18px">The shores are a guide, not a law. The test at the bottom of the chart is what decides: does IS/ARE + -ING work in <em>this</em> sentence?</p>
      ''' + rule_grid([
    ('Statia: knowing and believing',
     'Verbs of the mind name a state, not something you do. They usually take the present simple, even for now.',
     ex('I <em>know</em> the way. (not: I am knowing)')),
    ('Statia: wanting and needing',
     'So do verbs of wanting, liking and needing.',
     ex('She <em>wants</em> a coffee right now.')),
    ('Statia: owning and belonging',
     'Possession is a state too.',
     ex('This bag <em>belongs</em> to me.')),
    ('Actia: things you do',
     'An action in progress now takes IS/ARE + -ING.',
     ex('We <em>are sailing</em> home at the moment.')),
    ('Actia: the same verb, as a habit',
     'An action verb takes the present simple for a habit, like any verb.',
     ex('We <em>sail</em> every weekend.')),
    ('The test',
     'Do not ask &#8220;is this verb on the list?&#8221; Ask whether IS/ARE + -ING works in this sentence.',
     ex('I <em>am thinking</em> about it. (an action: it works)')),
]) + chart(
    'The sixteen harbours',
    'Read each row across the channel: a state on the left, an action on the right.',
    ['Statia', 'Now', 'Actia', 'Now'],
    [[s[0], s[1], a[0], a[1]] for s, a in zip(STATIA, ACTIA)]) + '''
    </div>

    '''

ISLE_HTML = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Twofold Isle and the Shallows</div>
      <h2>Where the sentence decides</h2>
      <p class="chart-note" style="margin:-6px 0 18px">These verbs live on both shores. As a state they stay simple; as an action they take -ING, and the meaning changes with the form.</p>
      ''' + chart(
    'Twofold Isle: one verb, two meanings',
    'Read each row as a pair. The verb is the same; the meaning is not.',
    ['Verb', 'A state', 'An action'],
    [['think', 'I think so. (my opinion)', 'I&#39;m thinking about it. (I am considering it)'],
     ['have', 'I have a boat. (I own it)', 'I&#39;m having lunch. (I am eating)'],
     ['see', 'I see what you mean. (I understand)', 'I&#39;m seeing Ana tonight. (I am meeting her)'],
     ['be', 'He is silly. (always)', 'He&#39;s being silly today. (he is acting that way)'],
     ['taste', 'The soup tastes good.', 'I&#39;m tasting the soup.'],
     ['weigh', 'The bag weighs ten kilos.', 'She&#39;s weighing the bag.']]) + '''
      ''' + exi('I <em>have</em> a boat, and today I<em>&#39;m having</em> lunch on it.') + chart(
    'The Shallows: either form, same meaning',
    'With these two, both forms are right and the meaning does not change.',
    ['Simple', 'Continuous', 'Note'],
    [['I feel tired.', 'I&#39;m feeling tired.', 'both are natural'],
     ['My leg hurts.', 'My leg is hurting.', 'both are natural'],
     ['You look well.', 'You&#39;re looking well.', 'both are natural']]) + '''
      ''' + exi('How <em>do you feel</em>? How <em>are you feeling</em>? Both are fine.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a harbour and its line lights up below: Statia on the left, Actia in the middle, Twofold Isle on the '
    'right. Switch the chart to see what each shore does, then every verb in a sentence.',
    ('The verbs', 'What the shore does', 'In a sentence'),
    [('Statia: present simple', 'is-west'), ('Actia: present continuous', 'is-isle'),
     ('Twofold Isle and the Shallows', 'is-east')],
    'Drag the chart sideways to reach Actia.', min_zoom=1000)

TRAPS = fork(
    'Wrong shore',
    'Each of these puts -ING on a state, or leaves it off an action.',
    ['Not this', 'This', 'Why'],
    [['I am knowing the answer.', 'I know the answer.', 'a state of mind'],
     ['She is wanting a coffee.', 'She wants a coffee.', 'a state: wanting'],
     ['This bag is belonging to me.', 'This bag belongs to me.', 'a state: possession'],
     ['Look! He runs for the bus.', 'Look! He is running for the bus.', 'an action, now'],
     ['I am having a boat.', 'I have a boat.', 'have = own is a state'],
     ['I have lunch right now.', 'I&#39;m having lunch right now.', 'have = eat is an action']],
    'When you are not sure, try the sentence with IS/ARE + -ING. If it sounds like something happening, it is Actia.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-atlas.html', 'The Atlas of THE')])

SIGNALS = signals(
    'You are in Statia',
    ['the mind: <em>know</em>, <em>believe</em>, <em>understand</em>', 'wanting: <em>want</em>, <em>need</em>, <em>prefer</em>',
     'owning: <em>own</em>, <em>belong</em>', 'no end and no start you can watch', 'present simple, even for now',
     '<em>I think so</em>, <em>I have a boat</em>'],
    'You are in Actia',
    ['something you can watch happening', '<em>now</em>, <em>at the moment</em>, <em>Look!</em>', 'IS/ARE + -ING',
     'it starts and it stops', '<em>I&#39;m thinking about it</em>', '<em>I&#39;m having lunch</em>'],
    'One test: can you watch it happening? You can watch someone <em>run</em>. You cannot watch someone <em>know</em>.')

QUIZ = [
    ('I ___ the way to the harbour.', 'A state of mind.', 'know',
     ['know', 'am knowing', 'knowing', 'am know'], 'Know is a state: I know the way.'),
    ('Look! The children ___ in the sea.', 'An action, now.', 'are swimming',
     ['are swimming', 'swim', 'swims', 'is swim'], 'An action happening now: are swimming.'),
    ('She ___ a coffee right now.', 'Wanting is a state.', 'wants',
     ['wants', 'is wanting', 'wanting', 'are wanting'], 'Want is a state: she wants a coffee.'),
    ('This boat ___ to my uncle.', 'Possession.', 'belongs',
     ['belongs', 'is belonging', 'belonging', 'are belonging'], 'Belong is a state: it belongs to him.'),
    ('Be quiet. I ___ an email.', 'An action, now.', 'am writing',
     ['am writing', 'write', 'writes', 'am write'], 'An action in progress: I am writing.'),
    ('We ___ more time, I am afraid.', 'Needing is a state.', 'need',
     ['need', 'are needing', 'needing', 'is needing'], 'Need is a state: we need more time.'),
    ('I ___ about your offer. Give me a day.', 'Twofold Isle: an action.', 'am thinking',
     ['am thinking', 'think', 'thinks', 'am think'], 'Think = consider is an action: I am thinking about it.'),
    ('I ___ you are right.', 'Twofold Isle: an opinion.', 'think',
     ['think', 'am thinking', 'thinking', 'am think'], 'Think = have an opinion is a state: I think you are right.'),
    ('They ___ lunch on the deck at the moment.', 'Twofold Isle: have = eat.', 'are having',
     ['are having', 'have', 'has', 'are have'], 'Have = eat is an action: they are having lunch.'),
    ('They ___ a small boat.', 'Twofold Isle: have = own.', 'have',
     ['have', 'are having', 'having', 'is having'], 'Have = own is a state: they have a boat.'),
    ('He is usually sensible, but today he ___ silly.', 'Twofold Isle: be, for now.', 'is being',
     ['is being', 'is', 'be', 'are being'], 'Is being silly: acting that way today, not always.'),
    ('Which sentence is right?', 'The test.', 'I understand the problem now.',
     ['I understand the problem now.', 'I am understanding the problem now.', 'I understanding the problem now.',
      'I am understand the problem now.'], 'Understand is a state, even with now.'),
]

PANELS = [
    [('s-' + s[0], '<b>%s</b> %s' % (s[0], s[1])) for s in STATIA],
    [('a-' + a[0], '<b>%s</b> %s' % (a[0], a[1])) for a in ACTIA],
    [('t-' + v, '<b>%s</b> %s &middot; %s' % (v, st, ac)) for v, st, ac in TWOFOLD] +
    [('shallows', '<b>The Shallows</b> <em>feel</em>, <em>hurt</em>: either form, same meaning'),
     ('test', '<b>The test</b> does IS/ARE + -ING work in THIS sentence?')],
]
TARGETS = {}
for s in STATIA:
    TARGETS['s-' + s[0]] = (0, 's-' + s[0], '#095c6d')
for a in ACTIA:
    TARGETS['a-' + a[0]] = (1, 'a-' + a[0], '#095c6d')
for v, _, _ in TWOFOLD:
    TARGETS['t-' + v] = (2, 't-' + v, '#095c6d')
TARGETS['shallows'] = (2, 'shallows', '#095c6d')
TARGETS['test'] = (2, 'test', '#B4441F')

import ex_tr_statia as T
L.build(OUT, ART, 'Statia &amp; Actia &mdash; State and Action Verbs', 'State and action verbs', EXTRACTED,
        HERO, 'where the sentence decides.', ('order', 'Read the chart'),
        RULES + ISLE_HTML + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        [SIMPLE, CONT, SAND], T.T,
        ['Clean run. You ask the sentence, not the verb.',
         'Solid progress. Go back to Twofold Isle: think, have, see and be.',
         'Good first attempt. Start with the test: can you watch it happening?'],
        ('sailing-the-seas-make-do.html', 'Next chart: Makeland &amp; Doland'), gull_seed=59, long_name=22)
