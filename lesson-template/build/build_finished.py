# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: Finished Time & Open Time, the present
perfect or the past simple as two shores. The twentieth chart.

    py lesson-template/build/build_finished.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. The choice is made by the TIME, not by the action. The
west shore, Finished Time, holds time words whose time is over (yesterday,
last week, in 2019, two days ago): they take the past simple. The east
shore, Open Time, holds words whose time reaches now (ever, never, yet,
already, so far, since 2019): they take the present perfect. Twofold Isle
holds the two that depend on the situation (for five years, this morning);
the Shallows hold just, already and yet, which American English often puts
with the past simple; the False Cape is WHEN, which always takes the past.

TENSE COLOURS. Innes, 2026-11-13: anything involving a tense uses its Sherpa
colour. Finished Time is the past simple and Open Time the present perfect;
the shores are painted in those colours and the page's panels take them
from sea_tense.T, never typed.

THE ART. Layout by sea_layouts_4.py, painted by Codex on 2026-11-14.
sea_measure.py found the 18 harbour dots and one stray in the scenery
(finished_chart.json); the stray is dropped by position below.
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE
from sea_tense import T as TENSE

OUT = 'sailing-the-seas-finished.html'
ART = 'sailing-the-seas-finished'
UID = 'fin'

# py lesson-template/extract-palette.py sailing-the-seas-finished/hero.jpg --light
EXTRACTED = {'text': '#2a1e11', 'text-dim': '#5e472e', 'secondary': '#abced8', 'contrast': '#175b5e'}


def hexof(rgb):
    return '#%02X%02X%02X' % rgb


PAST, PERFECT = hexof(TENSE['past-simple']), hexof(TENSE['present-perfect'])

D = O.load('finished_chart.json')
WEST = sorted((tuple(p) for p in D['dots'] if abs(p[0] - 274) < 10), key=lambda p: p[1])
EAST = sorted((tuple(p) for p in D['dots'] if abs(p[0] - 1260) < 10), key=lambda p: p[1])
ISLE = sorted((tuple(p) for p in D['dots'] if abs(p[0] - 765) < 10), key=lambda p: p[1])
assert (len(WEST), len(EAST), len(ISLE)) == (8, 8, 2), D['dots']

# (time word, sentence)
FINISHED = [('yesterday', 'I saw her yesterday.'), ('last week', 'We met last week.'),
            ('in 2019', 'They moved in 2019.'), ('two days ago', 'He called two days ago.'),
            ('when I was ten', 'I learned to sail when I was ten.'), ('on Monday', 'She arrived on Monday.'),
            ('at six', 'The ferry left at six.'), ('the other day', 'I saw him the other day.')]
OPEN = [('ever', 'Have you ever sailed?'), ('never', 'I have never been to Rome.'),
        ('yet', 'She hasn&#8217;t called yet.'), ('already', 'We have already eaten.'),
        ('so far', 'I have read two chapters so far.'), ('since 2019', 'They have lived here since 2019.'),
        ('recently', 'I have seen him recently.'), ('just', 'He has just left.')]
TWOFOLD = [('for five years', 'lived (and left) &#183; have lived (still do)'),
           ('this morning', 'over? past &#183; still morning? perfect')]
INK, WEST_LAND, EAST_LAND, SAND = '#20180A', '#C48351', '#5BA49F', '#EED395'


def k(side, w):
    return side + '-' + w.replace(' ', '-')


def overlay():
    spots, names = [], []
    for (f, o), (wx, wy), (ex_, ey) in zip(zip(FINISHED, OPEN), WEST, EAST):
        names.append(O.name(wx, wy, (f[0], 'the time is over', f[1]), INK, WEST_LAND, size=19, dy=-15, fit=False, halo=.3))
        names.append(O.name(ex_, ey, (o[0], 'the time reaches now', o[1]), INK, EAST_LAND, size=19, dy=-15, fit=False,
                            halo=.4))
        spots.append(O.hotspot(UID, k('f', f[0]), O.circle_path(wx, wy, 30), '%s: finished time, past simple' % f[0]))
        spots.append(O.hotspot(UID, k('o', o[0]), O.circle_path(ex_, ey, 30), '%s: open time, present perfect' % o[0]))
    for (w, note), (x, y) in zip(TWOFOLD, ISLE):
        names.append(O.name(x, y, (w, 'the situation decides', note), INK, SAND, size=18, dy=-15, fit=False, halo=.2))
        spots.append(O.hotspot(UID, k('t', w), O.circle_path(x, y, 32), '%s: the situation decides' % w))
    spots.append(O.hotspot(UID, 'shallows', O.rect_path(549, 583, 958, 713), 'The Shallows: just, already, yet'))
    spots.append(O.hotspot(UID, 'cape', O.rect_path(540, 728, 990, 960), 'The False Cape: when always takes the past'))
    sea_ink = '#0F2F3D'
    caps = [O.cap(768, 58, 'FINISHED TIME &amp; OPEN TIME', sea_ink, 38, face=O.SERIF, spacing='.04em'),
            O.cap(768, 94, 'is the time over? read the shore', sea_ink, 20, face=O.SERIF, weight=600, spacing='0',
                  style='italic'),
            O.cap(274, 168, 'FINISHED TIME', INK, 27, face=O.SERIF, spacing='.02em', halo=WEST_LAND),
            O.cap(274, 198, 'past simple: I saw her yesterday.', INK, 15, weight=600, spacing='0', style='italic',
                  halo=WEST_LAND),
            O.cap(1260, 168, 'OPEN TIME', '#FFFFFF', 27, face=O.SERIF, spacing='.02em', halo='#2F5F5C'),
            O.cap(1260, 198, 'present perfect: I have seen her.', '#FFFFFF', 15, weight=600, spacing='0', style='italic',
                  halo='#2F5F5C'),
            O.cap(762, 292, 'TWOFOLD ISLE', INK, 21, face=O.SERIF, spacing='.04em'),
            O.cap(762, 640, 'THE SHALLOWS', INK, 20, face=O.SERIF, spacing='.04em'),
            O.cap(762, 668, 'just &#183; already &#183; yet: US past simple', INK, 15, weight=600, spacing='0',
                  style='italic'),
            O.cap(762, 908, 'THE FALSE CAPE', sea_ink, 20, face=O.SERIF, spacing='.04em'),
            O.cap(762, 938, 'When&#8230;? always takes the past: When did you arrive?', sea_ink, 15, weight=600,
                  spacing='0', style='italic')]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated chart with two shores. On the brown west shore, Finished Time, eight harbours: yesterday, '
            'last week, in 2019, two days ago, when I was ten, on Monday, at six and the other day. On the teal east '
            'shore, Open Time, eight more: ever, never, yet, already, so far, since 2019, recently and just. In the '
            'channel, Twofold Isle holds for five years and this morning. Below it a sandbank, the Shallows, and a '
            'spit with a red flag, the False Cape: When always takes the past.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; Present perfect or past simple', 'Finished Time &amp; Open Time',
    '<em>I saw her yesterday</em>, but <em>I have seen her today</em>. The action is the same. What changes is the '
    'time: yesterday is over, and today is still open. Finished time takes the past simple; open time takes the '
    'present perfect. Read the time word, find its shore, and the tense is decided.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the two shores</div>
      <h2>Is the time over?</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Do not ask how long ago it happened. Ask whether the time you are talking about has finished. If it has, you are on the west shore.</p>
      ''' + rule_grid([
    ('Finished: a named past time',
     '<em>Yesterday</em>, <em>last week</em>, <em>in 2019</em>, <em>on Monday</em>, <em>at six</em>: the time is over.',
     ex('I <em>saw</em> her yesterday.')),
    ('Finished: ago',
     '<em>Ago</em> counts back from now to a finished point.',
     ex('He <em>called</em> two days ago.')),
    ('Finished: when + a past time',
     'A <em>when</em> clause about the past closes the time.',
     ex('I <em>learned</em> to sail when I was ten.')),
    ('Open: your life so far',
     '<em>Ever</em> and <em>never</em> mean at any time up to now.',
     ex('<em>Have</em> you ever <em>sailed</em>?')),
    ('Open: up to now',
     '<em>Yet</em>, <em>already</em>, <em>so far</em>, <em>recently</em>, <em>just</em>: the time reaches this moment.',
     ex('We <em>have</em> already <em>eaten</em>.')),
    ('Open: since + a starting point',
     '<em>Since</em> names where the time began; it runs to now.',
     ex('They <em>have lived</em> here since 2019.')),
]) + chart(
    'The sixteen harbours',
    'Read each row across the channel: a finished time on the left, an open time on the right.',
    ['Finished time', 'Past simple', 'Open time', 'Present perfect'],
    [[f[0], f[1], o[0], o[1].replace('&#8217;', '&#39;')] for f, o in zip(FINISHED, OPEN)]) + '''
    </div>

    '''

ISLE_HTML = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Twofold Isle, the Shallows and the False Cape</div>
      <h2>Where the situation decides</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Two time words can be finished or open. The answer is not in the word: it is in what is true now.</p>
      ''' + chart(
    'Twofold Isle',
    'Read each row as a pair.',
    ['Time word', 'Finished', 'Open'],
    [['for five years', 'I lived in Rome for five years. (I left)', 'I have lived in Rome for five years. (I still do)'],
     ['this morning', 'I saw her this morning. (it is now afternoon)', 'I have seen her this morning. (it is still morning)'],
     ['today', 'I called her today. (the working day is over)', 'I have called her today. (the day is still going)'],
     ['this week', 'We met this week. (and will not again)', 'We have met twice this week. (so far)']]) + '''
      ''' + exi('I <em>lived</em> in Rome for five years, and I <em>have lived</em> here for two.') + chart(
    'The Shallows and the False Cape',
    'Two places where the chart needs a note.',
    ['Where', 'What happens', 'Example'],
    [['The Shallows', 'American English often uses the past simple with <em>just</em>, <em>already</em>, <em>yet</em>',
      'Did you eat yet? (US) / Have you eaten yet? (UK)'],
     ['The False Cape', '<em>When&#8230;?</em> asks for a finished time, so it takes the past simple',
      'When did you arrive? (not: When have you arrived?)'],
     ['The False Cape', 'the answer to it is finished too', 'I arrived at six.'],
     ['The False Cape', '<em>How long&#8230;?</em> is open and takes the perfect', 'How long have you been here?']]) + '''
      ''' + exi('<em>When did</em> you <em>arrive</em>? I<em>&#39;ve been</em> here since six.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a harbour and its line lights up below: Finished Time on the left, Open Time in the middle. Switch '
    'the chart to see why each word is on its shore, then each one in a sentence.',
    ('The time words', 'Why this shore', 'In a sentence'),
    [('Finished Time: past simple', 'is-west'), ('Open Time: present perfect', 'is-isle'),
     ('Twofold Isle, the Shallows, the Cape', 'is-east')],
    'Drag the chart sideways to reach Open Time.', min_zoom=1000)

TRAPS = fork(
    'Wrong shore',
    'Each of these puts a tense with a time word from the other shore.',
    ['Not this', 'This', 'Why'],
    [['I have seen her yesterday.', 'I saw her yesterday.', 'yesterday is finished'],
     ['We have met last week.', 'We met last week.', 'last week is finished'],
     ['He has called two days ago.', 'He called two days ago.', '<em>ago</em> is finished'],
     ['I never went to Rome. (in my life, so far)', 'I have never been to Rome.', 'your life is open'],
     ['They live here since 2019.', 'They have lived here since 2019.', '<em>since</em> is open'],
     ['When have you arrived?', 'When did you arrive?', 'the False Cape']],
    'If the sentence has no time word, ask what matters: the moment it happened (past simple) or the result now (present perfect).',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-regularia.html', 'Regularia &amp; Irregularia: the third forms')])

SIGNALS = signals(
    'You are in Finished Time',
    ['<em>yesterday</em>, <em>last week</em>, <em>last year</em>', '<em>in 2019</em>, <em>on Monday</em>, <em>at six</em>',
     '<em>two days ago</em>', '<em>when I was ten</em>', '<em>When&#8230;?</em>', 'past simple'],
    'You are in Open Time',
    ['<em>ever</em>, <em>never</em>', '<em>yet</em>, <em>already</em>, <em>just</em>', '<em>so far</em>, <em>recently</em>',
     '<em>since 2019</em>', '<em>How long&#8230;?</em>', 'present perfect'],
    'One test: can you still add to it? You can still add to <em>this week</em>. You cannot add to <em>last week</em>.')

QUIZ = [
    ('I ___ her yesterday.', 'Yesterday is over.', 'saw',
     ['saw', 'have seen', 'see', 'have saw'], 'Finished time: past simple.'),
    ('___ you ever ___ to Scotland?', 'Your life so far.', 'Have / been',
     ['Have / been', 'Did / go', 'Have / went', 'Did / been'], 'Ever is open: Have you ever been?'),
    ('We ___ last week.', 'Last week is over.', 'met',
     ['met', 'have met', 'meet', 'have meet'], 'Finished time: past simple.'),
    ('She ___ yet.', 'Up to now.', 'hasn&#39;t called',
     ['hasn&#39;t called', 'didn&#39;t called', 'doesn&#39;t call', 'hasn&#39;t call'], 'Yet is open: hasn&#39;t called yet.'),
    ('He ___ two days ago.', 'Ago is finished.', 'called',
     ['called', 'has called', 'calls', 'has call'], 'Ago: past simple.'),
    ('They ___ here since 2019.', 'Since runs to now.', 'have lived',
     ['have lived', 'lived', 'live', 'are living'], 'Since is open: have lived.'),
    ('The ferry ___ at six.', 'A named past time.', 'left',
     ['left', 'has left', 'leaves', 'has leave'], 'At six is finished: left.'),
    ('I ___ two chapters so far.', 'So far reaches now.', 'have read',
     ['have read', 'read yesterday', 'did read', 'am read'], 'So far is open: have read.'),
    ('When ___ you ___?', 'The False Cape.', 'did / arrive',
     ['did / arrive', 'have / arrived', 'did / arrived', 'have / arrive'], 'When takes the past simple.'),
    ('I ___ in Rome for five years, but I left in 2020.', 'Twofold Isle: it is over.', 'lived',
     ['lived', 'have lived', 'live', 'am living'], 'You left: the time is finished.'),
    ('I ___ in this town for five years, and I love it.', 'Twofold Isle: it continues.', 'have lived',
     ['have lived', 'lived', 'was living', 'had live'], 'You still live there: the time is open.'),
    ('Which sentence is right?', 'Check each time word.', 'I have never been to Rome, but I went to Milan last year.',
     ['I have never been to Rome, but I went to Milan last year.', 'I never went to Rome, but I have been to Milan last year.',
      'I have never been to Rome, but I have been to Milan last year.', 'I did never go to Rome, but I went to Milan last year.'],
     'Never (open): present perfect. Last year (finished): past simple.'),
]

PANELS = [
    [(k('f', f[0]), '<b>%s</b> %s' % (f[0], f[1])) for f in FINISHED],
    [(k('o', o[0]), '<b>%s</b> %s' % (o[0], o[1])) for o in OPEN],
    [(k('t', w), '<b>%s</b> %s' % (w, note)) for w, note in TWOFOLD] +
    [('shallows', '<b>The Shallows</b> <em>just</em>, <em>already</em>, <em>yet</em>: US past simple'),
     ('cape', '<b>The False Cape</b> <em>When did you arrive?</em>')],
]
TARGETS = {}
for f in FINISHED:
    TARGETS[k('f', f[0])] = (0, k('f', f[0]), '#175b5e')
for o in OPEN:
    TARGETS[k('o', o[0])] = (1, k('o', o[0]), '#175b5e')
for w, _ in TWOFOLD:
    TARGETS[k('t', w)] = (2, k('t', w), '#175b5e')
TARGETS['shallows'] = (2, 'shallows', '#175b5e')
TARGETS['cape'] = (2, 'cape', '#B4441F')

import ex_tr_finished as T
L.build(OUT, ART, 'Finished Time &amp; Open Time &mdash; Present Perfect or Past Simple', 'Present perfect or past simple',
        EXTRACTED, HERO, 'and the tense is decided.', ('order', 'Read the chart'),
        RULES + ISLE_HTML + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        [PAST, PERFECT, SAND], T.T,
        ['Clean run. You read the time word and the tense follows.',
         'Solid progress. Go back to Twofold Isle: for five years, this morning.',
         'Good first attempt. Start with two harbours: yesterday and ever.'],
        ('sailing-the-seas-quadrants.html', 'Next chart: the Conditional Quadrants'), gull_seed=83, long_name=24)
