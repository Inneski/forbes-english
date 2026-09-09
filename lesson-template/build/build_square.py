# -*- coding: utf-8 -*-
"""The Square — 44 words (A2), built as a 16:9 deck.

The source was a plain word list with a dictionary gloss under each entry —
44 items, mixed A1 and A2, of the kind that accumulates over a term. It is
grouped here into eleven four-card teach slides so that each screen is one
semantic set (a building, a bag, things to read, what hands do…) rather than
an alphabetical run, and every gloss is rewritten to the A2 register: the
supplied one for *window* alone was 38 words and carried "transparent
material in a frame".

Three of the supplied glosses pick a sense the learner would not guess, and
each is honoured rather than quietly swapped for the easy one:

  * **desert** is the verb, "abandon", not the sandy noun. Kept, with the
    stress pair (de-SERT / DE-sert) on the card, because that is the only
    thing that makes the two learnable together.
  * **turn** is "move on to a new point", not "rotate".
  * **bad boy** is the man, not the scolding.

The hero is the isometric town square supplied with the request. It is bright
and airy, so this is a **light** deck per HOUSE-STYLE §4a — every contrast row
PASSes at --void #d8c4ac.

All ten languages ship complete, which is the second deck in the repo to do so
after `forbes-c1-negotiation.html`. The strings are split across
`i18n_square.py` (en/de/es) and `i18n_square_extra.py` (the other seven) only
for length; the completeness check in the first module covers both.

The timed search needs eight objects that are all in this lesson, so eight
icons were added to the shared `icons.py`: window, door, coin, bag, rug,
newspaper, toast, magnifier.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import icons as ICO
import i18n_square as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-the-square-a2.html'
F = 'the-square'

E = I.T['en']          # one source for the English; see the i18n docstring

# py lesson-template/extract-palette.py the-square/hero.jpg --light
PALETTE = """  --hero: url('%s/hero.jpg');

  --void          : #d8c4ac;
  --surface       : #e1d4c4;
  --surface2      : #dccbb8;
  --border        : #4a7296;
  --text          : #111e2a;
  --text-dim      : #2e475e;
  --accent        : #035cac;
  --accent-bright : #00417c;
  --accent-dim    : #3d99ec;
  --secondary     : #f5ede4;
  --contrast      : #990f10;""" % F


# ── the 44 words, four to a slide ──────────────────────────────────────
# (slide, stage, [(headword, English example), ...]). The definition is not
# here: it lives in i18n_square under s<n><letter>b, because it translates
# and the headword and the example do not.
WORDS = [
    (1,  1, [('window', 'She opened the window.'),
             ('door', 'Please close the door.'),
             ('bathroom', 'The bathroom is upstairs.'),
             ('rug', 'A blue rug under the table.')]),
    (2,  1, [('bag', 'My books are in my bag.'),
             ('pocket', 'The coin is in his pocket.'),
             ('coin', 'a two-euro coin'),
             ('magnifying glass', 'He read the small print with a magnifying glass.')]),
    (3,  1, [('magazine', 'a football magazine'),
             ('newspaper', 'Dad reads the newspaper at breakfast.'),
             ('board games', 'We play board games on Sunday.'),
             ('homework', 'I have a lot of homework.')]),
    (4,  1, [('clothes', 'Put your clothes on.'),
             ('swim trunks', 'He forgot his swim trunks.'),
             ('toast', 'Two pieces of toast, please.'),
             ('friend', 'She is my best friend.')]),
    (5,  2, [('push', 'Push the door.'),
             ('pull', 'Pull the door.'),
             ('reach', 'She reached for the coin.'),
             ('hit', 'He hit the ball.')]),
    (6,  2, [('scratch', 'The cat scratched the door.'),
             ('build', 'They built a bridge.'),
             ('make', 'I made a cake.'),
             ('walk', 'We walked across the square.')]),
    (7,  2, [('whistle', 'He whistled for the dog.'),
             ('turn', 'Now let us turn to page ten.'),
             ('think', 'I think it is true.'),
             ('know', 'I know her name.')]),
    (8,  3, [('start', 'The event starts at seven.'),
             ('finish', 'Finish your homework.'),
             ('desert', 'He deserted his friends.'),
             ('event', 'The market is the big event of the week.')]),
    (9,  3, [('true', 'It is true that Tuesday follows Monday.'),
             ('false', 'That answer is false.'),
             ('bad', 'bad weather, a bad film'),
             ('bad boy', 'the bad boy of Formula One')]),
    (10, 3, [('angry', 'Dad was angry about the window.'),
             ('important', 'an important event'),
             ('very', 'very angry, very important'),
             ('sometimes', 'Sometimes I walk to school.')]),
    (11, 3, [('a', 'I saw a door. The door was blue.'),
             ('in', 'The coin is in my pocket.'),
             ('they', 'My friends came. They were late.'),
             ('ciao', 'Ciao! See you tomorrow.')]),
]


def cards(n, stage, entries):
    """Four vocabulary cards, 2x2.

    The heading is the headword and the note is an English example — neither
    takes an i18n key, so neither ever translates. Only the definition does.
    """
    letters = 'abcd'
    return D.teach(
        'e%d' % stage, E['e%d' % stage], 's%dt' % n, E['s%dt' % n],
        [(None, word, 's%d%sb' % (n, letters[i]), E['s%d%sb' % (n, letters[i])],
          None, '<em>%s</em>' % ex) for i, (word, ex) in enumerate(entries)],
        cols='1fr 1fr', folder=F)


# ── four multiple-choice items ─────────────────────────────────────────
# The key is at a different index each time and is never the only longest
# option — deck.py asserts it and check-lesson.js measures it again.
MC = [
    dict(stem='She put her arm out to take the coin from the table. She ____ for it.',
         options=['reached', 'scratched', 'whistled', 'deserted'],
         correct=0,
         why='<em>Reach</em> is putting your arm out towards something. '
             '<em>Scratch</em> marks a surface, <em>whistle</em> makes a sound, '
             'and <em>desert</em> means to leave someone behind.'),
    dict(stem='His friends still needed him, but he walked away and never came '
              'back. He ____ them.',
         options=['finished', 'started', 'deserted', 'reached'],
         correct=2,
         why='To <em>desert</em> people is to leave them when they still need '
             'you. Watch the stress: de-<em>SERT</em> is this verb; '
             '<em>DE</em>-sert is the dry, sandy place.'),
    dict(stem='Which sentence is correct English?',
         options=['I have a lot of homework tonight.',
                  'I have a lot of homeworks tonight.',
                  'I have got many homework tonight.',
                  'I have got two homeworks tonight.'],
         correct=0,
         why='<em>Homework</em> has no plural, so <em>homeworks</em> does not '
             'exist and <em>many</em> and <em>two</em> cannot go in front of it. '
             'Use <em>a lot of</em> or <em>much</em>.'),
    dict(stem='It comes out every day, on big sheets of paper, and it is full of '
              "today's news. It is a ____.",
         options=['newspaper', 'magazine', 'board game', 'homework'],
         correct=0,
         why='A <em>newspaper</em> is daily news on big sheets. A '
             '<em>magazine</em> is thinner, has far more pictures, and comes '
             'out every week or every month.'),
]

# ── two gap-fill slides ────────────────────────────────────────────────
# Every row explains itself; the bank is sorted so that it is not an answer
# key in gap order — deck.py asserts that too.
GAP = [
    ([('The sign on the door says PUSH, so do not ______ it — move it away from you.',
       ['pull'],
       '<em>Push</em> is away from you; <em>pull</em> is towards you. The sign '
       'tells you which one.'),
      ('He keeps his money in his ______, not in his bag.',
       ['pocket'],
       'A <em>pocket</em> is sewn into your clothes. A <em>bag</em> is a '
       'separate container you carry.'),
      ('The writing was tiny, so she looked at it through a ______ ______.',
       ['magnifying', 'glass'],
       'A <em>magnifying glass</em> is a lens with a handle that makes small '
       'things look big.')],
     ['glass', 'magnifying', 'pocket', 'pull']),
    ([('______ I walk to school, but not every day.',
       ['sometimes'],
       '<em>Sometimes</em> means occasionally — some days yes, some days no.'),
      ('My friends arrived late. ______ had missed the bus.',
       ['they'],
       '<em>They</em> stands for two or more people you have already named.'),
      ('That is not ______ — it is false.',
       ['true'],
       '<em>True</em> agrees with the facts; <em>false</em> does not.')],
     ['they', 'true', 'sometimes', 'false']),
]

MATCH = [
    ('whistle', 'make a high sound with your lips'),
    ('scratch', 'mark a surface with something sharp'),
    ('build', 'put parts together to make a house'),
    ('rug', 'a small, thick cloth on the floor'),
]

# Nouns and verbs only, and only words that cannot be read as both — a
# vocabulary sort whose items are ambiguous tests nerve, not knowledge.
SORT_ITEMS = [
    ('window', 0), ('coin', 0), ('rug', 0), ('bathroom', 0),
    ('walk', 1), ('think', 1), ('reach', 1), ('know', 1),
]

ORDER = ['Sometimes', 'I walk across the square', 'to buy a newspaper',
         'before I start my homework']

# Eight objects, all of them words this deck teaches. `whistle` is not among
# them on purpose: the lesson's sense of the word is the verb, and a drawing
# of the object teaches the wrong noun.
SEARCH = [('a window', 'window', False), ('a door', 'door', False),
          ('a coin', 'coin', False), ('a bag', 'bag', False),
          ('a rug', 'rug', False), ('a newspaper', 'newspaper', False),
          ('a piece of toast', 'toast', False),
          ('a magnifying glass', 'magnifier', True)]


def build():
    logo = D.logo_from(TPL)
    D.assert_no_key_is_longest(MC)
    n_mc, n_gap = len(MC), len(GAP)

    slides = "".join(
        [D.cover(logo, E['coverTitle'], E['coverSub'],
                 [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                  ('Count', E['chipCount'])])]

        + [cards(n, stage, entries) for n, stage, entries in WORDS]

        + [D.mc(i + 1, n_mc, q, 'e4', E['e4'], 'q%dt' % (i + 1),
                E['q%dt' % (i + 1)], folder=F)
           for i, q in enumerate(MC)]

        + [D.gap(i + 1, n_gap, rows, bank, 'e4', E['e4'],
                 'g%dt' % (i + 1), E['g%dt' % (i + 1)], folder=F,
                 hint=E['gapHint'], hint_key='gapHint', width=150)
           for i, (rows, bank) in enumerate(GAP)]

        + [D.match(MATCH, 'e4', E['e4'], 'matchT', E['matchT'],
                   'matchHint', E['matchHint'], E['matchWhy'], folder=F),

           D.sort_slide(['A thing', 'An action'], SORT_ITEMS,
                        'e4', E['e4'], 'sortT', E['sortT'],
                        'sortHint', E['sortHint'], E['sortWhy'], folder=F),

           D.order(ORDER, 'e4', E['e4'], 'orderT', E['orderT'],
                   'orderHint', E['orderHint'], E['orderWhy'], folder=F),

           D.search(1, 1, E['searchStem'],
                    [(name, ICO.icon(key), is_key) for name, key, is_key in SEARCH],
                    'e4', E['e4'], 'searchT', E['searchT'], E['searchWhy'],
                    limit=25, folder=F),

           D.results(folder=F),

           D.activate(E['actTitle'], E['actUse'],
                      ['push', 'pull', 'reach for', 'sometimes', 'very',
                       'important', 'true / false'],
                      'Speaking', E['actSpeakBrief'],
                      [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                      E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder'],
                      folder=F)])

    D.assemble(TPL, OUT, slides, PALETTE,
               'The Square — 44 Words (A2)', I,
               langs=('en', 'de', 'es', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja'))
    print('wrote %s — %d slides' % (OUT, slides.count('<section class="slide')))


if __name__ == '__main__':
    build()
