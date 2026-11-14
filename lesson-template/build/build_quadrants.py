# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: The Conditional Quadrants, the conditionals
as four seas. The twenty-first chart.

    py lesson-template/build/build_quadrants.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. Two questions place every conditional. Is it REAL or
UNREAL (west or east of the Reality Reef)? Is it about NOW or the PAST
(north or south of the dashed line)? Zero and first are real and now or
later; the second is unreal and now; the third is unreal and past; "real
past" is the one coursebooks skip (If he said that, he was wrong). MIXED
runs from the unreal past up to the unreal now: a past that did not happen,
a result that is not true today. The Linking Isles are the words that can
replace IF; Regret Reef is I WISH and IF ONLY.

TENSE COLOURS. Innes, 2026-11-13: anything involving a tense uses its Sherpa
colour, and on this chart WOULD is the outline of a half-disc in WILL's
orange: empty for WOULD + verb, filled present perfect for WOULD HAVE,
filled present simple for WOULD BE. The page's panel rows repeat that with a
disc for the if-clause and a ring (and a disc) for the result, from
sea_tense.T.

THE ART. Layout by sea_layouts_4.py, painted by Codex on 2026-11-14.
sea_measure.py found all 9 dots (quadrants_chart.json). MIXED has a disc and
no dot, by design.
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE
from sea_tense import T as TENSE

OUT = 'sailing-the-seas-quadrants.html'
ART = 'sailing-the-seas-quadrants'
UID = 'quad'

# py lesson-template/extract-palette.py sailing-the-seas-quadrants/hero.jpg --light
EXTRACTED = {'text': '#11252a', 'text-dim': '#2e545e', 'secondary': '#eccda1', 'contrast': '#962c49'}

D = O.load('quadrants_chart.json')
DOTS = [tuple(p) for p in D['dots']]


def near(x, y):
    hit = [p for p in DOTS if abs(p[0] - x) < 30 and abs(p[1] - y) < 30]
    assert len(hit) == 1, (x, y, DOTS)
    return hit[0]


# (key, name, the two verb forms, sentence, where its dot is, if-clause tense, result: tense / 'would' / ('would', tense))
CONDS = [('zero', 'ZERO', 'present + present', 'If you heat ice, it melts.', near(294, 272),
          'present-simple', 'present-simple'),
         ('first', 'FIRST', 'present + will', 'If it rains, we&#8217;ll stay in.', near(462, 385),
          'present-simple', 'future-simple'),
         ('second', 'SECOND', 'past + would', 'If I had a boat, I&#8217;d sail.', near(1121, 310),
          'past-simple', 'would'),
         ('real-past', 'REAL PAST', 'past + past', 'If he said that, he was wrong.', near(378, 696),
          'past-simple', 'past-simple'),
         ('third', 'THIRD', 'past perfect + would have', 'If we&#8217;d left, we&#8217;d have caught it.', near(1129, 696),
          'past-perfect', ('would', 'present-perfect'))]
ISLES = [('unless', near(156, 864)), ('provided that', near(320, 864)), ('as long as', near(484, 864)),
         ('in case', near(645, 864))]
assert len(DOTS) == 9
INK, SEA, SAND, ROCK = '#0F2F3D', '#B4D6E1', '#E5CA97', '#988E83'


def col(tense):
    return '#%02X%02X%02X' % TENSE[tense]


def disc(tense):
    return '<i style=color:%s;font-style:normal;margin-right:.2em>&#9679;</i>' % col(tense)


def ring():
    """WOULD: the outline only, in WILL's orange."""
    return '<i style=color:%s;font-style:normal;margin-right:.2em>&#9675;</i>' % col('future-simple')


def marks(a, b):
    """The discs for a conditional's two clauses, for a panel row (no
    double quotes: sea_lesson puts panel lines in a JS string)."""
    if b == 'would':
        res = ring()
    elif isinstance(b, tuple):
        res = ring() + disc(b[1])
    else:
        res = disc(b)
    return disc(a) + res + ' '


def overlay():
    spots, names = [], []
    for key, name, forms, sent, (x, y), _, _ in CONDS:
        names.append(O.name(x, y, (name, forms, sent), INK, SEA, size=20, dy=-34, fit=False, halo=.6))
        spots.append(O.hotspot(UID, key, O.circle_path(x, y, 44), '%s conditional: %s' % (name.lower(), forms)))
    for word, (x, y) in ISLES:
        names.append(O.name(x, y, (word, 'instead of if', word), '#20180A', SAND, size=16, dy=-14, fit=False, halo=.2))
        spots.append(O.hotspot(UID, 'isles', O.circle_path(x, y, 34), '%s: can replace if' % word))
    spots.append(O.hotspot(UID, 'mixed', O.rect_path(1290, 200, 1500, 360), 'Mixed: past perfect + would be'))
    spots.append(O.hotspot(UID, 'regret', O.rect_path(905, 781, 1353, 907), 'Regret Reef: I wish, if only'))
    caps = [O.cap(768, 52, 'THE CONDITIONAL QUADRANTS', INK, 38, face=O.SERIF, spacing='.04em'),
            O.cap(768, 88, 'real or unreal? now or past? find your sea', INK, 19, face=O.SERIF, weight=600, spacing='0',
                  style='italic'),
            O.cap(768, 140, 'THE REALITY REEF', INK, 17, face=O.SERIF, spacing='.04em', halo=SEA),
            O.cap(372, 172, 'REAL &#183; NOW OR LATER', INK, 21, face=O.SERIF, spacing='.03em'),
            O.cap(1150, 172, 'UNREAL &#183; NOW', INK, 21, face=O.SERIF, spacing='.03em'),
            O.cap(372, 602, 'REAL &#183; PAST', INK, 21, face=O.SERIF, spacing='.03em'),
            O.cap(1150, 602, 'UNREAL &#183; PAST', INK, 21, face=O.SERIF, spacing='.03em'),
            O.cap(1384, 300, 'MIXED', INK, 18, face=O.SERIF, spacing='.04em'),
            O.cap(1384, 324, 'If I&#8217;d studied,', INK, 14, weight=600, spacing='0', style='italic'),
            O.cap(1384, 344, 'I&#8217;d be a doctor now.', INK, 14, weight=600, spacing='0', style='italic'),
            O.cap(400, 928, 'THE LINKING ISLES', INK, 17, face=O.SERIF, spacing='.04em'),
            O.cap(1136, 832, 'REGRET REEF', '#FFFFFF', 18, face=O.SERIF, spacing='.04em', halo='#5E564E'),
            O.cap(1136, 860, 'I wish I had&#8230; &#183; If only&#8230;', '#FFFFFF', 14, weight=600, spacing='0',
                  style='italic', halo='#5E564E')]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated chart of open sea divided into four by a rocky reef running north to south, the Reality '
            'Reef, and a dashed line running east to west. North-west, real and now or later: Zero and First. '
            'North-east, unreal and now: Second. South-west, real and past: Real Past, with four small linking isles, '
            'unless, provided that, as long as and in case. South-east, unreal and past: Third, and Regret Reef. Each '
            'harbour has a two-colour disc for its two tenses. A dashed arrow runs north from the unreal past to '
            'Mixed.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; Conditionals', 'The Conditional Quadrants',
    'Forget the numbers for a moment. Every <em>if</em> sentence answers two questions: is it real or unreal, and is '
    'it about now or the past? Two questions make four seas, and each conditional has its own. '
    'Find the sea first, and the verb forms follow.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the four seas</div>
      <h2>Real or unreal? Now or past?</h2>
      <p class="chart-note" style="margin:-6px 0 18px">West of the reef, the speaker thinks it is possible or true. East of it, the speaker is imagining. North of the line is now or later; south of it is the past.</p>
      ''' + rule_grid([
    ('Zero: real, always true',
     'Present + present. It happens every time.',
     ex('If you <em>heat</em> ice, it <em>melts</em>.')),
    ('First: real, and it may happen',
     'Present + <em>will</em>. No <em>will</em> in the <em>if</em> half.',
     ex('If it <em>rains</em>, we<em>&#39;ll stay</em> in.')),
    ('Second: unreal, now',
     'Past + <em>would</em>. The past form does not mean past time here: it means not real.',
     ex('If I <em>had</em> a boat, I<em>&#39;d sail</em> every day.')),
    ('Third: unreal, past',
     'Past perfect + <em>would have</em> + past participle. It did not happen.',
     ex('If we<em>&#39;d left</em> earlier, we<em>&#39;d have caught</em> it.')),
    ('Real past: it may be true',
     'Past + past. You do not know whether it happened; if it did, something follows.',
     ex('If he <em>said</em> that, he <em>was</em> wrong.')),
    ('Mixed: an unreal past, a result now',
     'Past perfect + <em>would</em> + verb. The current runs from the past up to now.',
     ex('If I<em>&#39;d studied</em>, I<em>&#39;d be</em> a doctor now.')),
]) + chart(
    'The six conditionals',
    'Find the sea, then read the two halves.',
    ['Name', 'Sea', 'If half', 'Result half'],
    [['zero', 'real, now', 'present simple', 'present simple'], ['first', 'real, later', 'present simple', 'will + verb'],
     ['second', 'unreal, now', 'past simple', 'would + verb'],
     ['third', 'unreal, past', 'past perfect', 'would have + past participle'],
     ['real past', 'real, past', 'past simple', 'past simple'],
     ['mixed', 'unreal: past to now', 'past perfect', 'would + verb']]) + '''
    </div>

    '''

EXTRAS = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The Linking Isles and Regret Reef</div>
      <h2>Other words for if, and sentences with no result</h2>
      <p class="chart-note" style="margin:-6px 0 18px">The four isles sit in the real sea: they take the same verb forms as <em>if</em>. Regret Reef lies in the unreal past, and its sentences have only one half.</p>
      ''' + chart(
    'The Linking Isles',
    'Each can stand where <em>if</em> stands. Still no <em>will</em> after them.',
    ['Word', 'Means', 'Example'],
    [['unless', 'if &#8230; not', 'We&#39;ll sail unless it rains.'],
     ['provided that', 'only if', 'You can come provided that you help.'],
     ['as long as', 'only if', 'I&#39;ll lend it to you as long as you bring it back.'],
     ['in case', 'because it may happen', 'Take a coat in case it gets cold.']]) + '''
      ''' + exi('We<em>&#39;ll sail</em> tomorrow <em>unless</em> it <em>rains</em>.') + chart(
    'Regret Reef',
    '<em>I wish</em> and <em>If only</em> take the unreal forms, with no result half.',
    ['About', 'Form', 'Example'],
    [['now', 'wish + past simple', 'I wish I had a boat.'], ['now', 'if only + past simple', 'If only I knew the answer.'],
     ['the past', 'wish + past perfect', 'I wish I had studied harder.'],
     ['the past', 'if only + past perfect', 'If only we had left earlier.']]) + '''
      ''' + exi('<em>I wish</em> I <em>had studied</em> harder at school.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a harbour and its line lights up below: the real seas on the left, the unreal seas in the middle. The '
    'discs beside each line are its two tenses; a ring is WOULD. Switch the chart to see the verb forms, then a '
    'sentence.',
    ('The names', 'The verb forms', 'In a sentence'),
    [('Real: west of the reef', 'is-west'), ('Unreal: east of the reef', 'is-isle'),
     ('The Linking Isles and Regret Reef', 'is-east')],
    'Drag the chart sideways to cross the reef.', min_zoom=1000)

TRAPS = fork(
    'Wrong sea',
    'Each of these mixes the two halves of different conditionals, or puts will or would where it cannot go.',
    ['Not this', 'This', 'Why'],
    [['If it will rain, we&#39;ll stay in.', 'If it rains, we&#39;ll stay in.', 'no <em>will</em> in the if half'],
     ['If I would have a boat, I&#39;d sail.', 'If I had a boat, I&#39;d sail.', 'no <em>would</em> in the if half'],
     ['If I had a boat, I will sail.', 'If I had a boat, I&#39;d sail.', 'unreal: <em>would</em>'],
     ['If we left earlier, we&#39;d have caught it.', 'If we&#39;d left earlier, we&#39;d have caught it.', 'unreal past: past perfect'],
     ['If we&#39;d left earlier, we would caught it.', 'If we&#39;d left earlier, we&#39;d have caught it.', '<em>would have</em> + third form'],
     ['We&#39;ll sail unless it doesn&#39;t rain.', 'We&#39;ll sail unless it rains.', '<em>unless</em> already means not']],
    'In speech you will hear <em>If I would have known</em>. In an exam, keep <em>would</em> out of the <em>if</em> half.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-certainty.html', 'Soundings of Certainty')])

SIGNALS = signals(
    'You are west of the reef: real',
    ['it is true, or it may happen', 'facts and habits: zero', 'plans, promises, warnings: first',
     'present in the if half', '<em>will</em>, <em>can</em>, <em>may</em> in the result', '<em>unless</em>, <em>as long as</em>'],
    'You are east of the reef: unreal',
    ['you are imagining', 'it is not true now: second', 'it did not happen: third', 'past or past perfect in the if half',
     '<em>would</em>, <em>could</em>, <em>might</em> in the result', '<em>I wish</em>, <em>If only</em>'],
    'One test: is there a real chance? <em>If I win</em> (I may) is real. <em>If I won</em> (I do not expect to) is unreal.')

QUIZ = [
    ('If you heat ice, it ___.', 'Always true.', 'melts',
     ['melts', 'will melt', 'would melt', 'melted'], 'Zero: present + present.'),
    ('If it rains tomorrow, we ___ in.', 'Real, later.', 'will stay',
     ['will stay', 'would stay', 'stayed', 'would have stayed'], 'First: present + will.'),
    ('If I ___ a boat, I would sail every day.', 'Unreal, now.', 'had',
     ['had', 'have', 'would have', 'had had'], 'Second: past + would.'),
    ('If we had left earlier, we ___ the ferry.', 'Unreal, past.', 'would have caught',
     ['would have caught', 'would catch', 'will catch', 'caught'], 'Third: past perfect + would have.'),
    ('If it ___ tomorrow, we&#39;ll stay in.', 'No will in the if half.', 'rains',
     ['rains', 'will rain', 'would rain', 'rained'], 'Present in the if half.'),
    ('If I ___ you, I would take the job.', 'Unreal, now.', 'were',
     ['were', 'am', 'would be', 'will be'], 'Second: If I were you.'),
    ('If I had studied medicine, I ___ a doctor now.', 'Mixed: past to now.', 'would be',
     ['would be', 'would have been', 'will be', 'am'], 'Mixed: past perfect + would + verb.'),
    ('We&#39;ll sail ___ it rains.', 'A linking isle.', 'unless',
     ['unless', 'provided', 'in case of', 'if not'], 'Unless = if not.'),
    ('Take a coat ___ it gets cold.', 'A linking isle.', 'in case',
     ['in case', 'unless', 'as long', 'provided'], 'In case: because it may happen.'),
    ('I wish I ___ harder at school.', 'Regret Reef: the past.', 'had studied',
     ['had studied', 'studied', 'would study', 'have studied'], 'A past regret: wish + past perfect.'),
    ('Which sea? &#8220;If he said that, he was wrong.&#8221;', 'You do not know if he said it.', 'real, past',
     ['real, past', 'unreal, past', 'unreal, now', 'real, later'], 'It may be true: real past, past + past.'),
    ('Which sentence is right?', 'Keep would out of the if half.', 'If I had known, I would have told you.',
     ['If I had known, I would have told you.', 'If I would have known, I would have told you.',
      'If I knew, I would have told you yesterday already.', 'If I had known, I will tell you.'], 'Third: past perfect + would have.'),
]

ROW = {c[0]: c for c in CONDS}


def row(key):
    _, name, forms, sent, _, a, b = ROW[key]
    return (key, '%s<b>%s</b> %s' % (marks(a, b), name.title() if name != 'REAL PAST' else 'Real past', sent))


PANELS = [
    [row('zero'), row('first'), row('real-past')],
    [row('second'), row('third'),
     ('mixed', '%s<b>Mixed</b> If I&#8217;d studied, I&#8217;d be a doctor now.'
      % marks('past-perfect', ('would', 'present-simple')))],
    [('isles', '<b>The Linking Isles</b> <em>unless</em>, <em>provided that</em>'),
     ('isles', '<em>as long as</em>, <em>in case</em>'),
     ('regret', '<b>Regret Reef</b> <em>I wish I had&#8230;</em> &middot; <em>If only&#8230;</em>')],
]
TARGETS = {'zero': (0, 'zero', '#0c506a'), 'first': (0, 'first', '#0c506a'), 'real-past': (0, 'real-past', '#0c506a'),
           'second': (1, 'second', '#0c506a'), 'third': (1, 'third', '#0c506a'), 'mixed': (1, 'mixed', '#0c506a'),
           'isles': (2, 'isles', '#0c506a'), 'regret': (2, 'regret', '#962c49')}

import ex_tr_quadrants as T
L.build(OUT, ART, 'The Conditional Quadrants &mdash; Conditionals', 'Conditionals', EXTRACTED,
        HERO, 'and the verb forms follow.', ('order', 'Read the chart'),
        RULES + EXTRAS + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        ['#9CC3D2', '#C7B9C6', SAND], T.T,
        ['Clean run. You find the sea first, and the verb forms follow.',
         'Solid progress. Cross the reef again: second and third.',
         'Good first attempt. Start with one question: real or unreal?'],
        ('sailing-the-seas-scale.html', 'Next chart: the Harbour of Scale'), gull_seed=89, long_name=24)
