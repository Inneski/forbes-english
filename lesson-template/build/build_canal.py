# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: The Adjective Canal, adjective order as a
canal with eight locks that only open one way. The fourth chart.

    py lesson-template/build/build_canal.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. Adjective order is a fixed series, so it is drawn as one:
a barge carrying a noun passes through eight locks (opinion, size, age,
shape, colour, origin, material, purpose) and cannot go back. The purpose
lock is the last before Noun Harbour because a purpose word is almost part
of the noun (a fishing boat). The Comma Cut is the side channel for two
adjectives from the same lock (a friendly, helpful crew). Real English rarely
loads more than three; the eight-word barge exists to show the order.

THE ART. Layout by sea_layouts_2.py (docs/sea-charts/adjective-canal.png),
painted by Codex on 2026-11-09 with Gerundia as the style: hero.jpg is the
labelled painting, chart-clean.jpg the same with every word removed. Dots
measured by sea_measure.py into canal_chart.json (9: eight locks and the
harbour). The page and its machinery: sea_lesson.py.
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE

OUT = 'sailing-the-seas-adjective-canal.html'
ART = 'sailing-the-seas-adjective-canal'
UID = 'cnl'

# py lesson-template/extract-palette.py sailing-the-seas-adjective-canal/hero.jpg --light
EXTRACTED = {'text': '#2a2211', 'text-dim': '#5e4f2e', 'secondary': '#6f93a0', 'contrast': '#09596d'}

# ── the label layer ───────────────────────────────────────────────────
D = O.load('canal_chart.json')
DOTS = sorted(D['dots'], key=lambda p: (p[1], p[0]))
HARBOUR = DOTS[0]                      # (1404, 520): the one dot off the lock row
LOCK_DOTS = sorted(DOTS[1:])
assert len(LOCK_DOTS) == 8 and HARBOUR[0] > 1300, 'canal dots: %s' % DOTS
MEADOW = D['shapes'][0]['colour']
INK = O.ink_for(MEADOW, 7)
WATER_INK = O.ink_for(D['sea'], 7)
LOCKS = ['OPINION', 'SIZE', 'AGE', 'SHAPE', 'COLOUR', 'ORIGIN', 'MATERIAL', 'PURPOSE']
BOAT = ['lovely', 'little', 'old', 'round', 'red', 'French', 'wooden', 'fishing']
BAG = ['beautiful', 'big', 'new', 'flat', 'green', 'Spanish', 'leather', 'travel']
LAMP = ['nice', 'small', 'modern', 'square', 'white', 'Japanese', 'paper', 'reading']
NOUNS = ('boat', 'bag', 'lamp')
for row in (BOAT, BAG, LAMP):
    assert len(row) == 8


def overlay():
    names, caps, spots = [], [], []
    for (x, y), lock, a, b, c in zip(LOCK_DOTS, LOCKS, BOAT, BAG, LAMP):
        caps.append(O.cap(x, 428, lock, INK, 17))
        names.append(O.name(x, y, (a, b, c), INK, MEADOW, size=22, dy=34, fit=False, weight=500))
        spots.append(O.hotspot(UID, lock.lower(), O.rect_path(x - 64, 440, x + 64, 650), 'The %s lock' % lock.lower()))
    hx, hy = HARBOUR
    caps.append(O.cap(hx, hy - 30, 'NOUN HARBOUR', INK, 18))
    names.append(O.name(hx, hy, NOUNS, WATER_INK, D['sea'], size=24, dy=44, fit=False, weight=500))
    spots.append(O.hotspot(UID, 'noun', O.circle_path(hx, hy, 115), 'Noun Harbour'))
    spots.append(O.hotspot(UID, 'comma', O.rect_path(290, 250, 480, 410), 'The Comma Cut: two from one lock'))
    caps += [O.cap(768, 92, 'THE ADJECTIVE CANAL', INK, 40, face=O.SERIF, spacing='.04em'),
             O.cap(768, 132, 'eight locks &#183; one way only', INK, 22, face=O.SERIF, weight=600, spacing='0', style='italic'),
             O.cap(528, 224, 'THE COMMA CUT', INK, 18, face=O.SERIF, spacing='.05em'),
             O.cap(528, 250, 'two from one lock: a lovely, quiet evening', INK, 15, weight=600, spacing='0', style='italic')]
    sentence = tuple('a %s %s' % (' '.join(r), n) for r, n in zip((BOAT, BAG, LAMP), NOUNS))
    names.append(O.name(768, 776, sentence, INK, MEADOW, size=26, dy=0, fit=False, weight=600))
    caps.append(O.cap(768, 820, 'opinion before fact &#183; the purpose sits right next to the noun', INK, 17, weight=600, spacing='0'))
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated chart of a canal running west to east through green meadows. Eight wooden lock gates '
            'cross it, labelled opinion, size, age, shape, colour, origin, material and purpose, with the words '
            'lovely, little, old, round, red, French, wooden and fishing beneath them, and it ends in a round basin '
            'called Noun Harbour. A side channel, the Comma Cut, branches off near the first lock.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; adjective order', 'The Adjective Canal',
    'A noun travels with its adjectives the way a barge travels down a canal: through a row of locks, in one order, '
    'and never backwards. Opinion opens first; the purpose lock is the last before the harbour, because a purpose '
    'word is almost part of the noun. Learn the eight locks once and every adjective has its place.',
    HERO_ALT)

WEST = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">The locks</div>
      <h2>Eight locks, one way</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Each lock asks one question about the noun, and they always ask in the same order. You will rarely need more than two or three in one sentence; the full barge is there to show where each one goes.</p>
      ''' + rule_grid([
    ('Opinion before fact',
     'What you think (<em>lovely, ugly, boring, delicious</em>) comes before anything anyone could check.',
     ex('It was a <em>lovely old</em> boat.')),
    ('Size, then age, then shape',
     '<em>big, little, long</em> &rarr; <em>old, new, young</em> &rarr; <em>round, square, flat</em>.',
     ex('We sat at a <em>big old round</em> table.')),
    ('Colour, origin, material',
     'What colour, where from, and what it is made of: <em>red, Italian, leather</em>.',
     ex('She carried a <em>red Italian leather</em> bag.')),
    ('Purpose sits next to the noun',
     'The purpose word is almost part of the noun: <em>a fishing boat, a sleeping bag, running shoes</em>. Nothing comes between them.',
     ex('He bought some <em>new running</em> shoes.')),
    ('Two or three is normal',
     'Real English seldom stacks more than three adjectives. Choose the ones that matter, and keep their order.',
     ex('We stayed in a <em>lovely little</em> cottage by the sea.')),
    ('Nouns can be adjectives too',
     'A noun in front of a noun works like a material or purpose word, and goes last: <em>a stone wall, a summer dress, a glass bottle</em>.',
     ex('She found a <em>small glass</em> bottle on the beach.')),
]) + chart(
    'The eight locks',
    'Read down the column: that is the order. Each lock asks its own question.',
    ['Lock', 'It asks', 'Words that pass through'],
    [['1 &middot; opinion', 'what do you think of it?', 'lovely, nice, ugly, boring, delicious, strange'],
     ['2 &middot; size', 'how big?', 'big, small, tiny, huge, long, short'],
     ['3 &middot; age', 'how old?', 'old, new, young, ancient, modern'],
     ['4 &middot; shape', 'what shape?', 'round, square, flat, narrow, wide'],
     ['5 &middot; colour', 'what colour?', 'red, green, pale blue, dark'],
     ['6 &middot; origin', 'where from?', 'French, Chinese, Scottish, northern'],
     ['7 &middot; material', 'made of what?', 'wooden, metal, cotton, glass, paper'],
     ['8 &middot; purpose', 'what is it for?', 'fishing, sleeping, running, reading, travel']]) + '''
    </div>

    '''

COMMA = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The Comma Cut</div>
      <h2>When two come from the same lock</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Adjectives from different locks sail straight through: <em>a big old boat</em>, no comma. Two from the <em>same</em> lock cannot queue, so they take the side channel: a comma, or <em>and</em>.</p>
      ''' + chart(
    'Comma, <em>and</em>, or nothing',
    'Ask whether the two words answer the same question.',
    ['The adjectives', 'Write', 'Example'],
    [['from different locks', 'nothing between them', 'a beautiful old ship'],
     ['two opinions', 'a comma', 'a friendly, helpful crew'],
     ['two colours', '<em>and</em>', 'a blue and white flag'],
     ['two materials', '<em>and</em>', 'a wood and glass door'],
     ['after <em>be</em>, <em>look</em>, <em>seem</em>', 'commas and <em>and</em>', 'The cabin was small, dark and cold.']]) + '''
      ''' + exi('a friendly, helpful crew &nbsp;&middot;&nbsp; a blue and white flag') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a lock and its line lights up below. Switch the cargo to send a different noun down the canal: the words '
    'change, the locks never do. Read the bottom line each time; it is the whole barge in order.',
    ('A fishing boat', 'A travel bag', 'A reading lamp'),
    [('Opinion first', 'is-west'), ('Then the facts', 'is-isle'), ('Next to the noun', 'is-east')],
    'Drag the chart sideways to reach Noun Harbour.')

TRAPS = fork(
    'Wrong-way barges',
    'These are the orders learners most often send down the canal backwards. Each one has a lock that should have opened first.',
    ['Not this', 'This', 'The lock that comes first'],
    [['a French old car', 'an old French car', 'age before origin'],
     ['a wooden big table', 'a big wooden table', 'size before material'],
     ['a red beautiful dress', 'a beautiful red dress', 'opinion before colour'],
     ['a leather new jacket', 'a new leather jacket', 'age before material'],
     ['a running new pair of shoes', 'a new pair of running shoes', 'purpose stays next to its noun']],
    'The order is a strong habit, not a law, and a speaker will break it for emphasis now and then. But a learner who '
    'keeps to it never sounds wrong, and one who breaks it by accident always does.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-of-grammar.html', 'The first chart: gerunds and infinitives')])

SIGNALS = signals(
    'Opinion locks &mdash; words that judge',
    ['<em>lovely, nice, beautiful, ugly</em>', '<em>boring, interesting, strange</em>',
     '<em>delicious, awful, perfect</em>', '<em>friendly, helpful, rude</em>',
     'anything another person might disagree with', 'they always open first'],
    'Fact locks &mdash; words you can check',
    ['size: <em>big, tiny, long</em>', 'age: <em>old, new, modern</em>', 'shape: <em>round, flat</em>',
     'colour: <em>red, dark blue</em>', 'origin and material: <em>Italian, wooden</em>',
     'purpose, last of all: <em>fishing, sleeping</em>'],
    'One question settles most orders: could someone disagree with this word? If yes, it is an opinion, and it goes first.')

QUIZ = [
    ('She lives in a ___ house by the harbour.', 'Size before age.', 'big old',
     ['big old', 'old big', 'big, old', 'old and big'],
     'Size comes before age: a big old house. No comma, because big and old come from different locks.'),
    ('He bought a ___ bag.', 'Colour, origin, material.', 'red Italian leather',
     ['red Italian leather', 'Italian red leather', 'leather red Italian', 'red leather Italian'],
     'Colour, then where it is from, then what it is made of: a red Italian leather bag.'),
    ('They live in a ___ cottage.', 'Opinion opens first.', 'beautiful old',
     ['beautiful old', 'old beautiful', 'old a beautiful', 'beautiful a old'],
     'Opinion before fact: a beautiful old cottage.'),
    ('I need some ___ shoes.', 'Purpose sits next to the noun.', 'new running',
     ['new running', 'running new', 'new runned', 'runner new'],
     'Running says what the shoes are for, so it goes right next to shoes: new running shoes.'),
    ('The captain wore a ___ coat.', 'Size, colour, material.', 'long black wool',
     ['long black wool', 'black long wool', 'wool long black', 'long wool black'],
     'Size, then colour, then material: a long black wool coat.'),
    ('It was a ___ table.', 'Shape before material.', 'round wooden',
     ['round wooden', 'wooden round', 'round wood made', 'wooden, round'],
     'Shape comes before material: a round wooden table.'),
    ('Which one needs a comma?', 'Two words from the same lock.', 'a friendly helpful crew',
     ['a friendly helpful crew', 'a big old ship', 'a small French car', 'a new leather bag'],
     'Friendly and helpful are both opinions, from the same lock, so they take a comma: a friendly, helpful crew.'),
    ('They flew a ___ flag.', 'Two colours.', 'blue and white',
     ['blue and white', 'blue white', 'and blue white', 'white blue and'],
     'Two colours are joined with and: a blue and white flag.'),
    ('Which order is correct?', 'Opinion, size, age.', 'a lovely little old boat',
     ['a lovely little old boat', 'a little lovely old boat', 'an old lovely little boat', 'a little old lovely boat'],
     'Opinion, then size, then age: a lovely little old boat.'),
    ('She found an ___ coin on the beach.', 'Age, origin, material.', 'old Spanish silver',
     ['old Spanish silver', 'Spanish old silver', 'silver old Spanish', 'old silver Spanish'],
     'Age, then origin, then material: an old Spanish silver coin.'),
    ('The cabin was ___.', 'After be, the adjectives are a list.', 'small, dark and cold',
     ['small, dark and cold', 'small dark cold', 'dark small cold', 'small and dark cold'],
     'After be, adjectives form a list: commas, and and before the last one.'),
    ('Which is NOT correct?', 'One barge went the wrong way.', 'a French old car',
     ['a French old car', 'an old French car', 'a small blue car', 'a nice red car'],
     'Age comes before origin: an old French car.'),
]

PANELS = [
    [('opinion', '<b>Opinion</b> lovely &middot; beautiful &middot; nice &middot; boring &middot; delicious'),
     ('', 'It opens first, whatever follows.')],
    [('size', '<b>Size</b> big &middot; little &middot; long'), ('age', '<b>Age</b> old &middot; new &middot; modern'),
     ('shape', '<b>Shape</b> round &middot; flat &middot; square'), ('colour', '<b>Colour</b> red &middot; green &middot; white'),
     ('origin', '<b>Origin</b> French &middot; Spanish &middot; Japanese'), ('material', '<b>Material</b> wooden &middot; leather &middot; paper')],
    [('purpose', '<b>Purpose</b> fishing &middot; travel &middot; reading: right next to the noun'),
     ('noun', '<b>Noun Harbour</b> where the barge ties up: boat, bag, lamp'),
     ('comma', '<b>The Comma Cut</b> two from one lock: a friendly, helpful crew')],
]
TARGETS = {'opinion': (0, 'opinion', INK)}
for k in ('size', 'age', 'shape', 'colour', 'origin', 'material'):
    TARGETS[k] = (1, k, INK)
for k in ('purpose', 'noun', 'comma'):
    TARGETS[k] = (2, k, INK)

import ex_tr_canal as T
L.build(OUT, ART, 'The Adjective Canal &mdash; Adjective Order', 'adjective order', EXTRACTED,
        HERO, 'Learn the eight locks once and every adjective has its place.', ('order', 'Read the chart'),
        WEST + COMMA + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        ['#d7a96b', MEADOW, '#9ec0cc'], T.T,
        ['Clean run. Every barge reached Noun Harbour the right way round.',
         'Solid progress. Say the eight locks aloud, then sail it again.',
         'Good first attempt. Start with one rule: opinion before fact.'],
        ('sailing-the-seas-prefixes.html', 'Next chart: the prefix archipelago'), gull_seed=21)
