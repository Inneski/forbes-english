# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: Soundings of Certainty, modals of deduction
as the depth of the sea. The sixteenth chart.

    py lesson-template/build/build_certainty.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. How sure are you that it is true? MUST is the deep water
(95%), SHOULD a little shallower (80%), MAY, MIGHT and COULD lie in the fog
bank (50%), and CAN'T is on the rocks (0%). The west column is now; the east
column is the past, the same modal + HAVE + past participle. The pairing
that matters is at the two ends: the opposite of MUST is CAN'T, not MUSTN'T.

Modals are not tenses, so no Sherpa colours on this chart.

THE ART. Layout by sea_layouts_5.py, painted by Codex on 2026-11-14.
sea_measure.py --dark found all 7 dots (certainty_chart.json).
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE

OUT = 'sailing-the-seas-certainty.html'
ART = 'sailing-the-seas-certainty'
UID = 'cert'

# py lesson-template/extract-palette.py sailing-the-seas-certainty/hero.jpg --light
EXTRACTED = {'text': '#111f2a', 'text-dim': '#2e495e', 'secondary': '#ebd0a8', 'contrast': '#9c0d12'}

D = O.load('certainty_chart.json')
WEST = sorted((tuple(p) for p in D['dots'] if p[0] < 768), key=lambda p: p[1])
EAST = sorted((tuple(p) for p in D['dots'] if p[0] > 768), key=lambda p: p[1])
assert (len(WEST), len(EAST)) == (4, 3), D['dots']

# (key, modal, how sure, sentence)
NOW = [('must', 'must', '95% sure it is true', 'It must be the ferry: it&#8217;s six o&#8217;clock.'),
       ('should', 'should', '80%: I expect it', 'It should be calm by noon.'),
       ('might', 'may &#183; might &#183; could', '50%: perhaps', 'It might be a whale. It could be a log.'),
       ('cant', 'can&#8217;t &#183; couldn&#8217;t', '0%: sure it is not true', 'It can&#8217;t be Tom: he&#8217;s in Rome.')]
PAST = [('must-have', 'must have', '95%, about the past', 'She must have left.'),
        ('might-have', 'might have', '50%, about the past', 'He might have missed it.'),
        ('cant-have', 'can&#8217;t have', '0%, about the past', 'They can&#8217;t have seen us.')]
WHITE, INK = '#FFFFFF', '#101820'
DEEP, MID, FOG, ROCK = '#1D5C8B', '#4E86A8', '#DCE3E8', '#717A7E'
# ink and paint by depth: the four rows of the west column, the three of the east
W_LOOK = [(WHITE, DEEP), (WHITE, MID), (INK, FOG), (WHITE, ROCK)]
E_LOOK = [(WHITE, DEEP), (INK, FOG), (WHITE, ROCK)]


def overlay():
    spots, names = [], []
    for (key, modal, sure, sent), (x, y), (ink, paint) in zip(NOW, WEST, W_LOOK):
        names.append(O.name(x, y, (modal, sure, sent), ink, paint, size=20, dy=-17, fit=False,
                            halo=.25 if ink == INK else -.35))
        spots.append(O.hotspot(UID, key, O.circle_path(x, y, 34), '%s: %s' % (modal.replace('&#183;', ','), sure)))
    for (key, modal, sure, sent), (x, y), (ink, paint) in zip(PAST, EAST, E_LOOK):
        names.append(O.name(x, y, (modal, sure, sent), ink, paint, size=20, dy=-17, fit=False,
                            halo=.25 if ink == INK else -.35))
        spots.append(O.hotspot(UID, key, O.circle_path(x, y, 34), '%s: %s' % (modal, sure)))
    spots.append(O.hotspot(UID, 'fog', O.rect_path(560, 470, 980, 560), 'The fog bank: perhaps'))
    spots.append(O.hotspot(UID, 'rocks', O.rect_path(560, 680, 980, 760), 'The rocks: sure it is not true'))
    sea_ink = '#0F2F3D'
    caps = [O.cap(768, 62, 'SOUNDINGS OF CERTAINTY', sea_ink, 40, face=O.SERIF, spacing='.05em'),
            O.cap(768, 98, 'how sure are you that it&#8217;s true? read the depth', sea_ink, 20, face=O.SERIF, weight=600,
                  spacing='0', style='italic'),
            O.cap(333, 172, 'NOW', WHITE, 26, face=O.SERIF, spacing='.05em', halo=DEEP),
            O.cap(1177, 172, 'THE PAST: + have + past participle', WHITE, 21, face=O.SERIF, spacing='.02em', halo=DEEP),
            O.cap(768, 524, 'THE FOG BANK', sea_ink, 21, face=O.SERIF, spacing='.05em', halo=FOG),
            O.cap(768, 724, 'THE ROCKS', WHITE, 21, face=O.SERIF, spacing='.05em', halo=ROCK)]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated depth chart. Deep blue water at the top, a white fog bank across the middle, grey rocks and '
            'breaking waves at the foot. A left column, NOW, runs down through must (95%), should (80%), may, might, '
            'could (50%) in the fog, and can&#39;t, couldn&#39;t (0%) on the rocks. A right column, THE PAST, has must '
            'have, might have and can&#39;t have at the same depths.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; Must, might, can&#8217;t', 'Soundings of Certainty',
    'You see a shape on the water. Is it the ferry? You do not know, but you can say how sure you are. '
    '<em>Must</em> is deep water: you are almost certain. <em>Might</em> is the fog: perhaps. <em>Can&#8217;t</em> is '
    'the rocks: you are sure it is not. Read the depth, then do the same for the past.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the depth</div>
      <h2>How sure are you?</h2>
      <p class="chart-note" style="margin:-6px 0 18px">None of these states a fact. Each says what you work out from what you can see. The deeper the water, the surer you are.</p>
      ''' + rule_grid([
    ('Must: almost certain it is true',
     'You have a reason, so you are nearly sure.',
     ex('It <em>must</em> be the ferry: it&#39;s six o&#39;clock.')),
    ('Should: what you expect',
     'Things are normal, so this is what ought to happen.',
     ex('The sea <em>should</em> be calm by noon.')),
    ('May, might, could: perhaps',
     'All three mean it is possible. In the fog you cannot tell.',
     ex('It <em>might</em> be a whale. It <em>could</em> be a log.')),
    ('Can&#39;t: almost certain it is not true',
     'The opposite of this <em>must</em> is <em>can&#39;t</em>, not <em>mustn&#39;t</em>.',
     ex('It <em>can&#39;t</em> be Tom: he&#39;s in Rome.')),
    ('The past: modal + have + past participle',
     'Keep the modal and add <em>have</em> + the third form. The depth stays the same.',
     ex('She <em>must have left</em>: her coat is gone.')),
    ('Might not is not can&#39;t',
     '<em>Might not</em> is still the fog: perhaps not. <em>Can&#39;t</em> is the rocks: surely not.',
     ex('He <em>might not</em> know. He <em>can&#39;t</em> know.')),
]) + chart(
    'The soundings',
    'Read down the chart, deep to shallow, then across to the past.',
    ['How sure', 'Now', 'The past'],
    [['95%: surely true', 'must be', 'must have been'], ['80%: I expect so', 'should be', 'should have been'],
     ['50%: perhaps', 'may / might / could be', 'may / might / could have been'],
     ['50%: perhaps not', 'may not / might not be', 'may not / might not have been'],
     ['0%: surely not true', 'can&#39;t / couldn&#39;t be', 'can&#39;t / couldn&#39;t have been']]) + '''
    </div>

    '''

BANKS = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The fog bank and the rocks</div>
      <h2>Where learners run aground</h2>
      <p class="chart-note" style="margin:-6px 0 18px">The fog holds three words with one meaning. The rocks hold the form that most languages get wrong: the negative of a sure guess.</p>
      ''' + chart(
    'The fog bank: three words, one depth',
    'For a guess, these are the same strength. <em>Can</em> is not among them.',
    ['Say', 'Not', 'Note'],
    [['It may be true.', 'It can be true.', '<em>can</em> is ability, not a guess'],
     ['It might rain.', 'It can rain later.', 'for one guess about now or later'],
     ['It could be Ana.', 'It can be Ana.', 'the same'],
     ['It might not be true.', 'It couldn&#39;t be true. (if you mean perhaps not)', '<em>couldn&#39;t</em> is the rocks']]) + '''
      ''' + exi('That <em>might</em> be Ana at the door, or it <em>could</em> be the postman.') + chart(
    'The rocks: surely not',
    'When you are sure something is not true, use <em>can&#39;t</em>.',
    ['Not this', 'This', 'Why'],
    [['It mustn&#39;t be Tom.', 'It can&#39;t be Tom.', '<em>mustn&#39;t</em> means it is forbidden'],
     ['She mustn&#39;t have seen us.', 'She can&#39;t have seen us.', 'the same, in the past'],
     ['He must not be at home. (as a guess)', 'He can&#39;t be at home.', 'the usual form, in British English'],
     ['It can&#39;t to be true.', 'It can&#39;t be true.', 'no <em>to</em> after a modal']]) + '''
      ''' + exi('They <em>can&#39;t have seen</em> us: it was dark.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a sounding and its line lights up below: now on the left, the past in the middle. Switch the chart to '
    'see how sure each one is, then each in a sentence.',
    ('The modals', 'How sure', 'In a sentence'),
    [('Now', 'is-west'), ('The past', 'is-isle'), ('The fog bank and the rocks', 'is-east')],
    'Drag the chart sideways to reach the past.', min_zoom=1000)

TRAPS = fork(
    'Wrong depth',
    'Each of these says something a little different from what was meant.',
    ['Not this', 'This', 'Why'],
    [['It mustn&#39;t be true.', 'It can&#39;t be true.', 'the opposite of <em>must</em> here is <em>can&#39;t</em>'],
     ['It can be Ana at the door.', 'It could be Ana at the door.', 'a guess: could, may, might'],
     ['She must left.', 'She must have left.', 'the past needs <em>have</em>'],
     ['He might has missed it.', 'He might have missed it.', '<em>have</em> never changes after a modal'],
     ['They can&#39;t saw us.', 'They can&#39;t have seen us.', '<em>have</em> + the third form'],
     ['It must to be late.', 'It must be late.', 'no <em>to</em>']],
    'Two checks: no <em>to</em> after the modal, and for the past it is always <em>have</em> + the third form.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-forecast.html', 'The Grammar Forecast')])

SIGNALS = signals(
    'You are in deep water',
    ['you have a reason: <em>it&#39;s six o&#39;clock</em>', '<em>I&#39;m sure</em>, <em>certainly</em>', '<em>must be</em>',
     '<em>must have been</em>', '<em>can&#39;t be</em> for the opposite', 'you would bet on it'],
    'You are in the fog',
    ['<em>perhaps</em>, <em>maybe</em>, <em>possibly</em>', '<em>I&#39;m not sure</em>', '<em>may</em>, <em>might</em>, <em>could</em>',
     '<em>might have been</em>', '<em>might not</em> for perhaps not', 'you would not bet on it'],
    'One test: can you say <em>I&#39;m sure</em>? Then it is <em>must</em> or <em>can&#39;t</em>. If you would say <em>perhaps</em>, it is the fog.')

QUIZ = [
    ('The lights are on. They ___ be at home.', 'You have a reason: almost sure.', 'must',
     ['must', 'might', 'can&#39;t', 'should to'], 'A sure guess: they must be at home.'),
    ('I&#39;m not sure. It ___ rain later.', 'Perhaps.', 'might',
     ['might', 'must', 'can&#39;t', 'can'], 'Perhaps: it might rain.'),
    ('That ___ be Tom. He&#39;s in Rome this week.', 'Sure it is not true.', 'can&#39;t',
     ['can&#39;t', 'mustn&#39;t', 'might', 'should'], 'Sure it is not: can&#39;t, never mustn&#39;t.'),
    ('The ferry left at five, so it ___ arrive by six.', 'What you expect.', 'should',
     ['should', 'can&#39;t', 'might not', 'must to'], 'What you expect: it should arrive by six.'),
    ('Her coat is gone. She ___ left.', 'Sure, about the past.', 'must have',
     ['must have', 'must', 'must has', 'must had'], 'Must + have + the third form.'),
    ('He isn&#39;t here. He ___ missed the boat.', 'Perhaps, about the past.', 'might have',
     ['might have', 'might has', 'might', 'can have'], 'Might + have + the third form.'),
    ('It was dark. They ___ seen us.', 'Sure it did not happen.', 'can&#39;t have',
     ['can&#39;t have', 'mustn&#39;t have', 'can&#39;t', 'might'], 'Can&#39;t have seen: sure it did not happen.'),
    ('Which word does NOT fit? It ___ be a whale.', 'One of these is not a guess.', 'can',
     ['can', 'may', 'might', 'could'], 'For a guess: may, might or could. Can is ability.'),
    ('Which is the opposite of &#8220;It must be true&#8221;?', 'The rocks.', 'It can&#39;t be true.',
     ['It can&#39;t be true.', 'It mustn&#39;t be true.', 'It doesn&#39;t must be true.', 'It not must be true.'],
     'The opposite of a sure guess is can&#39;t.'),
    ('Which sentence means &#8220;perhaps not&#8221;?', 'Fog, not rocks.', 'He might not know.',
     ['He might not know.', 'He can&#39;t know.', 'He must know.', 'He should know.'], 'Might not: perhaps not. Can&#39;t: surely not.'),
    ('Which sentence is right?', 'No to, and have + third form.', 'She must have forgotten.',
     ['She must have forgotten.', 'She must to have forgotten.', 'She must has forgotten.', 'She must have forgot it yesterday to.'],
     'Must have forgotten.'),
    ('You are 50% sure. Which do you say?', 'Read the depth.', 'It could be the ferry.',
     ['It could be the ferry.', 'It must be the ferry.', 'It can&#39;t be the ferry.', 'It is the ferry.'],
     'Fifty per cent is the fog: could, may or might.'),
]

PANELS = [
    [(key, '<b>%s</b> %s' % (modal, sent)) for key, modal, _, sent in NOW],
    [(key, '<b>%s</b> %s' % (modal, sent)) for key, modal, _, sent in PAST],
    [('fog', '<b>The fog bank</b> <em>may</em>, <em>might</em>, <em>could</em>: perhaps'),
     ('rocks', '<b>The rocks</b> <em>can&#39;t</em>: sure it is not true'),
     ('rocks', 'not <em>mustn&#39;t</em>: that means it is forbidden')],
]
TARGETS = {}
for key, _, _, _ in NOW:
    TARGETS[key] = (0, key, '#0c506a')
for key, _, _, _ in PAST:
    TARGETS[key] = (1, key, '#0c506a')
TARGETS['fog'] = (2, 'fog', '#0c506a')
TARGETS['rocks'] = (2, 'rocks', '#9c0d12')

import ex_tr_certainty as T
L.build(OUT, ART, 'Soundings of Certainty &mdash; Must, Might, Can&#8217;t', 'Must, might, can&#8217;t', EXTRACTED,
        HERO, 'then do the same for the past.', ('order', 'Read the chart'),
        RULES + BANKS + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        ['#8FB2C8', '#B9CBD6', '#C9CED1'], T.T,
        ['Clean run. You can read the depth, now and in the past.',
         'Solid progress. Check the rocks again: can’t, not mustn’t.',
         'Good first attempt. Start with the two ends: must and can’t.'],
        ('sailing-the-seas-passive.html', 'Next chart: the Passive Ferry'), gull_seed=67, long_name=22)
