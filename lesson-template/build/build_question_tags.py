# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: The Return Voyage, question tags as a round
trip across a reef. The tenth chart.

    py lesson-template/build/build_question_tags.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. A reef splits the sea: positive water to the north,
negative to the south. Every question tag is a return voyage. Set out on a
positive (It's cold,) and you come home on a negative (isn't it?); set out
on a negative (It isn't far,) and you come home on a positive (is it?). The
four lone stacks in the south-east are the tags that do not follow the
route: I am late, aren't I? Let's go, shall we? Close the hatch, will you?
Nobody came, did they?

THE ART. Layout by sea_layouts_3.py (docs/sea-charts/return-voyage.png),
painted by ChatGPT on 2026-11-09 with Gerundia as the style; the brief
pinned the 14 dots, and sea_measure.py found all 14
(question-tags_chart.json). The painted routes cross the reef rather than
loop round its end; the teaching does not depend on which.
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE

OUT = 'sailing-the-seas-question-tags.html'
ART = 'sailing-the-seas-question-tags'
UID = 'qtg'

# py lesson-template/extract-palette.py sailing-the-seas-question-tags/hero.jpg --light
EXTRACTED = {'text': '#11252a', 'text-dim': '#2e555e', 'secondary': '#eaca9c', 'contrast': '#992849'}

D = O.load('question-tags_chart.json')
DOTS = [tuple(p) for p in D['dots']]
assert len(DOTS) == 14, DOTS


def near(x, y):
    p = min(DOTS, key=lambda q: abs(q[0] - x) + abs(q[1] - y))
    assert abs(p[0] - x) + abs(p[1] - y) < 14, (x, y, p)
    return p


# (key, statement, tag, the helper at the start, the helper at the end, the answer,
#  statement dot, tag dot, positive start?)
ROUTES = [
    ('cold', 'It&#8217;s cold,', 'isn&#8217;t it?', 'it IS cold', 'is &#8594; isn&#8217;t', 'Yes, it is.',
     (186, 320), (187, 691), True),
    ('swim', 'You can swim,', 'can&#8217;t you?', 'you CAN swim', 'can &#8594; can&#8217;t', 'Yes, I can.',
     (388, 319), (388, 691), True),
    ('home', 'She went home,', 'didn&#8217;t she?', 'went = DID go', 'did &#8594; didn&#8217;t', 'Yes, she did.',
     (588, 320), (588, 692), True),
    ('far', 'It isn&#8217;t far,', 'is it?', 'IS + not', 'isn&#8217;t &#8594; is', 'No, it isn&#8217;t.',
     (792, 688), (794, 340), False),
    ('left', 'They haven&#8217;t left,', 'have they?', 'HAVE + not', 'haven&#8217;t &#8594; have', 'No, they haven&#8217;t.',
     (987, 691), (992, 340), False),
]
ROUTES = [r[:6] + (near(*r[6]), near(*r[7]), r[8]) for r in ROUTES]
# (key, the whole question, the helper, the answer, dot)
STACKS = [
    ('late', 'I am late, aren&#8217;t I?', 'I am &#8594; aren&#8217;t I (never amn&#8217;t)', 'Yes, you are.', (1228, 698)),
    ('lets', 'Let&#8217;s go, shall we?', 'let&#8217;s &#8594; shall we', 'Yes, let&#8217;s.', (1228, 764)),
    ('hatch', 'Close the hatch, will you?', 'an order &#8594; will you', 'OK, I will.', (1228, 834)),
    ('nobody', 'Nobody came, did they?', 'nobody is negative &#8594; did they', 'No, nobody did.', (1228, 903)),
]
STACKS = [s[:4] + (near(*s[4]),) for s in STACKS]
assert len({r[6] for r in ROUTES} | {r[7] for r in ROUTES} | {s[4] for s in STACKS}) == 14
INK, NORTH, SOUTH = '#0E2A33', '#B1D5DF', '#7DB2C3'


def overlay():
    spots, names = [], []
    for k, said, tag, h1, h2, ans, (sx, sy), (tx, ty), pos in ROUTES:
        # the north dot's words sit above it, the south dot's below
        for (x, y), words, end in (((sx, sy), (said, h1, said), 's'), ((tx, ty), (tag, h2, ans), 't')):
            north = y < 512
            names.append(O.name(x, y, words, INK, NORTH if north else SOUTH, size=19, dy=-16 if north else 32,
                                fit=False, halo=.55 if north else .6))
        spots.append(O.hotspot(UID, k + '-s', O.circle_path(sx, sy, 30), 'Out: %s' % said))
        spots.append(O.hotspot(UID, k + '-t', O.circle_path(tx, ty, 30), 'Home: %s' % tag))
    for k, q, helper, ans, (x, y) in STACKS:
        names.append(O.name(x, y, (q, helper, ans), INK, SOUTH, size=17, anchor='start', dx=16, dy=6, fit=False,
                            halo=.65))
        spots.append(O.hotspot(UID, k, O.rect_path(x - 24, y - 26, 1500, y + 26), 'A lone stack: %s' % q))
    spots.append(O.hotspot(UID, 'reef', O.rect_path(1180, 478, 1500, 530), 'The turning reef'))
    caps = [O.cap(768, 62, 'THE RETURN VOYAGE', '#0E2A33', 38, face=O.SERIF, spacing='.05em'),
            O.cap(768, 90, 'out on a positive, home on a negative, and back again', '#0E2A33', 19, face=O.SERIF,
                  weight=600, spacing='0', style='italic'),
            O.cap(44, 462, 'POSITIVE WATERS', INK, 18, 'start', face=O.SERIF, spacing='.04em', halo=O.mix(NORTH, '#FFFFFF', .5)),
            O.cap(44, 590, 'NEGATIVE WATERS', INK, 18, 'start', face=O.SERIF, spacing='.04em', halo=O.mix(SOUTH, '#FFFFFF', .6)),
            O.cap(1336, 512, 'THE TURNING REEF', '#3A2408', 18, face=O.SERIF, spacing='.04em', halo='#F5CD9C'),
            O.cap(1350, 646, 'THE LONE STACKS', INK, 19, face=O.SERIF, spacing='.04em', halo=O.mix(SOUTH, '#FFFFFF', .6))]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated sea chart cut in two by a long rocky reef: calm pale water to the north, choppier dark '
            'water to the south. Five dashed routes, each with a little ship, cross between the waters: It&#8217;s '
            'cold, isn&#8217;t it? You can swim, can&#8217;t you? She went home, didn&#8217;t she? It isn&#8217;t '
            'far, is it? They haven&#8217;t left, have they? In the south-east four sea stacks: I am late, '
            'aren&#8217;t I? Let&#8217;s go, shall we? Close the hatch, will you? Nobody came, did they?')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; question tags', 'The Return Voyage',
    'A question tag is the little question on the end of a sentence: <em>It&#39;s cold, isn&#39;t it?</em> On this '
    'chart every tag is a round trip across the reef. Sail out on a positive and you come home on a negative; '
    'sail out on a negative and you come home on a positive. Four lone stacks keep their own rules.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the voyage</div>
      <h2>Out on one, home on the other</h2>
      <p class="chart-note" style="margin:-6px 0 18px">A tag turns a statement into a check: you think you know, and you want the other person to agree. Three things decide it: the direction, the helper and the pronoun.</p>
      ''' + rule_grid([
    ('Positive out, negative home',
     'A positive statement takes a negative tag.',
     ex('It&#39;s cold, <em>isn&#39;t it</em>?')),
    ('Negative out, positive home',
     'A negative statement takes a positive tag.',
     ex('It isn&#39;t far, <em>is it</em>?')),
    ('Sail home in the same boat',
     'The tag uses the same helper as the statement: <em>be</em>, <em>have</em>, <em>can</em>, <em>will</em>, <em>should</em>&#8230;',
     ex('You can swim, <em>can&#39;t you</em>?')),
    ('No helper? <em>do</em> rows you home',
     'In the present simple and past simple, the tag uses <em>do, does</em> or <em>did</em>.',
     ex('She went home, <em>didn&#39;t she</em>?')),
    ('A pronoun, never the noun',
     'The tag repeats the subject as a pronoun: <em>the ferry</em> becomes <em>it</em>, <em>the crew</em> becomes <em>they</em>.',
     ex('The ferry leaves at six, <em>doesn&#39;t it</em>?')),
    ('The tune tells the reader',
     'Voice falls at the end: you are sure, you want agreement. Voice rises: it is a real question.',
     ex('You haven&#39;t seen my keys, <em>have you</em>?')),
]) + chart(
    'The five routes',
    'Read each row left to right: out, home, and how the other person usually answers.',
    ['Out', 'Home', 'The answer'],
    [['It&#39;s cold,', 'isn&#39;t it?', 'Yes, it is.'], ['You can swim,', 'can&#39;t you?', 'Yes, I can.'],
     ['She went home,', 'didn&#39;t she?', 'Yes, she did.'], ['It isn&#39;t far,', 'is it?', 'No, it isn&#39;t.'],
     ['They haven&#39;t left,', 'have they?', 'No, they haven&#39;t.']]) + '''
    </div>

    '''

STACK_HTML = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The lone stacks</div>
      <h2>Four tags with their own rules</h2>
      <p class="chart-note" style="margin:-6px 0 18px">These stand apart from the routes. Learn them as they are.</p>
      ''' + chart(
    'The four stacks',
    'Each one breaks the pattern in its own way.',
    ['Question', 'Why'],
    [['I am late, aren&#39;t I?', 'there is no <em>amn&#39;t I</em>; <em>aren&#39;t I</em> takes its place'],
     ['Let&#39;s go, shall we?', '<em>let&#39;s</em> is a suggestion, so the tag is <em>shall we</em>'],
     ['Close the hatch, will you?', 'after an order, <em>will you</em> or <em>would you</em> makes it polite'],
     ['Nobody came, did they?', '<em>nobody</em>, <em>nothing</em>, <em>never</em> are negative, so the tag is positive; <em>nobody</em> becomes <em>they</em>']]) + '''
      ''' + exi('I&#39;m late, <em>aren&#39;t I</em>?') + chart(
    'More from the stacks',
    'The same rules reach a little further.',
    ['Statement', 'Tag', 'Why'],
    [['Nothing happened,', 'did it?', '<em>nothing</em> is negative; it becomes <em>it</em>'],
     ['You never swim,', 'do you?', '<em>never</em> is negative'], ['Everyone was there,', 'weren&#39;t they?', '<em>everyone</em> becomes <em>they</em>'],
     ['There&#39;s a café on board,', 'isn&#39;t there?', '<em>there</em> stays <em>there</em>'],
     ['I&#39;d better go,', 'hadn&#39;t I?', '<em>&#39;d better</em> is <em>had better</em>']]) + '''
      ''' + exi('Let&#39;s go, <em>shall we</em>?') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a harbour and its line lights up below. Switch the chart to see the helper hiding in each statement and '
    'the one that sails home, then how the other person answers: the helper crosses the reef and changes sign.',
    ('The voyage', 'The helper', 'The answer'),
    [('Positive out, negative home', 'is-west'), ('Negative out, positive home', 'is-isle'),
     ('The lone stacks', 'is-east')],
    'Drag the chart sideways to reach the stacks.', min_zoom=1000)

TRAPS = fork(
    'Run aground',
    'Most mistakes come home in the wrong boat, or forget to cross the reef.',
    ['Not this', 'This', 'Why'],
    [['It&#39;s cold, is it?', 'It&#39;s cold, isn&#39;t it?', 'positive out, negative home'],
     ['You can swim, don&#39;t you?', 'You can swim, can&#39;t you?', 'same helper: <em>can</em>'],
     ['She went home, wasn&#39;t she?', 'She went home, didn&#39;t she?', 'past simple: <em>did</em>'],
     ['I&#39;m late, amn&#39;t I?', 'I&#39;m late, aren&#39;t I?', 'a lone stack'],
     ['Nobody came, didn&#39;t they?', 'Nobody came, did they?', '<em>nobody</em> is already negative'],
     ['The ferry is late, isn&#39;t the ferry?', 'The ferry is late, isn&#39;t it?', 'a pronoun in the tag']],
    'Many speakers use <em>right?</em> or <em>yeah?</em> instead of a tag. That is fine in chat, but it is not a question tag, '
    'and an exam wants the real one.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-atlantic.html', 'The Atlantic')])

SIGNALS = signals(
    'The statement is negative',
    ['<em>not</em>: <em>isn&#39;t</em>, <em>can&#39;t</em>, <em>didn&#39;t</em>', '<em>never</em>, <em>no</em>',
     '<em>nobody</em>, <em>no one</em>, <em>nothing</em>', '<em>hardly</em>, <em>rarely</em>, <em>seldom</em>',
     'so the tag is positive: <em>is it?</em>, <em>do you?</em>'],
    'The statement is positive',
    ['no <em>not</em> anywhere', '<em>always</em>, <em>everyone</em>, <em>something</em>',
     '<em>I am</em> &#8594; <em>aren&#39;t I?</em>', 'an order &#8594; <em>will you?</em>',
     'so the tag is negative: <em>isn&#39;t it?</em>, <em>don&#39;t you?</em>'],
    'One test: say the tag as a full question. <em>Isn&#39;t it cold?</em> If it sounds right, the boat is right.')

QUIZ = [
    ('It&#39;s cold, ___?', 'Positive out.', 'isn&#39;t it',
     ['isn&#39;t it', 'is it', 'doesn&#39;t it', 'isn&#39;t that'], 'Positive out, negative home: isn&#39;t it?'),
    ('You can swim, ___?', 'Same helper.', 'can&#39;t you',
     ['can&#39;t you', 'don&#39;t you', 'aren&#39;t you', 'can you'], 'The statement has can, so the tag has can: can&#39;t you?'),
    ('She went home, ___?', 'Past simple: no helper.', 'didn&#39;t she',
     ['didn&#39;t she', 'wasn&#39;t she', 'went she', 'doesn&#39;t she'], 'Past simple: did. She went home, didn&#39;t she?'),
    ('It isn&#39;t far, ___?', 'Negative out.', 'is it',
     ['is it', 'isn&#39;t it', 'does it', 'it is'], 'Negative out, positive home: is it?'),
    ('They haven&#39;t left, ___?', 'Negative out, same helper.', 'have they',
     ['have they', 'haven&#39;t they', 'did they', 'do they'], 'They haven&#39;t left, have they?'),
    ('I&#39;m late, ___?', 'A lone stack.', 'aren&#39;t I',
     ['aren&#39;t I', 'amn&#39;t I', 'am I not', 'isn&#39;t I'], 'I am takes aren&#39;t I.'),
    ('Let&#39;s go, ___?', 'A suggestion.', 'shall we',
     ['shall we', 'don&#39;t we', 'let we', 'will we'], 'Let&#39;s ... shall we?'),
    ('Nobody came, ___?', 'Nobody is already negative.', 'did they',
     ['did they', 'didn&#39;t they', 'did nobody', 'didn&#39;t he'], 'Nobody is negative, so the tag is positive, and nobody becomes they.'),
    ('The ferry leaves at six, ___?', 'A pronoun, not the noun.', 'doesn&#39;t it',
     ['doesn&#39;t it', 'doesn&#39;t the ferry', 'isn&#39;t it', 'leaves it'], 'Present simple with -s: does. The ferry becomes it.'),
    ('Close the hatch, ___?', 'After an order.', 'will you',
     ['will you', 'do you', 'don&#39;t you', 'are you'], 'An order takes will you to sound polite.'),
    ('You never swim in the sea, ___?', 'Never is negative.', 'do you',
     ['do you', 'don&#39;t you', 'never you', 'are you'], 'Never makes the statement negative, so the tag is positive: do you?'),
    ('Which tag is NOT correct?', 'One came home in the wrong boat.', 'He&#39;s been here, isn&#39;t he?',
     ['He&#39;s been here, isn&#39;t he?', 'He&#39;s tired, isn&#39;t he?', 'He&#39;s got a boat, hasn&#39;t he?',
      'He has been here, hasn&#39;t he?'], 'He&#39;s been = he has been, so the tag is hasn&#39;t he?'),
]

PANELS = [
    [(r[0] + '-s', '<b>%s</b> %s &middot; %s' % (r[1], r[2], r[5])) for r in ROUTES if r[8]],
    [(r[0] + '-s', '<b>%s</b> %s &middot; %s' % (r[1], r[2], r[5])) for r in ROUTES if not r[8]]
    + [('reef', '<b>The reef</b> every tag crosses it: positive and negative swap')],
    [(s[0], '<b>%s</b> %s' % (s[1], s[2])) for s in STACKS],
]
TARGETS = {}
for r in ROUTES:
    for end in ('-s', '-t'):
        TARGETS[r[0] + end] = (0 if r[8] else 1, r[0] + '-s', '#992849')
for s in STACKS:
    TARGETS[s[0]] = (2, s[0], '#992849')
TARGETS['reef'] = (1, 'reef', '#992849')

import ex_tr_question_tags as T
L.build(OUT, ART, 'The Return Voyage &mdash; Question Tags', 'question tags', EXTRACTED,
        HERO, 'Four lone stacks keep their own rules.', ('order', 'Read the chart'),
        RULES + STACK_HTML + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        ['#B1D5DF', '#7DB2C3', '#C9B9A0'], T.T,
        ['Clean run. Every voyage came home in the right boat.',
         'Solid progress. Find the helper first, then cross the reef.',
         'Good first attempt. Start with the five routes: positive out, negative home.'],
        ('sailing-the-seas-forecast.html', 'Next chart: the grammar forecast'), gull_seed=43, long_name=24)
