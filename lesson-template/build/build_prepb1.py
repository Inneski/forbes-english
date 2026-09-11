# -*- coding: utf-8 -*-
"""Prepositions Double Lesson (B1) — rebuilt as a 16:9 deck.

`b1_prepositions_double_lesson.html` was a scrolling four-section quiz with no
teaching content whatsoever. Every rule in the lesson lived only in the
per-answer feedback, so a learner met the rule for the first time *after*
getting the question wrong — the exact defect already recorded against both
Lego preposition decks and Twin Peaks in `docs/HANDOFF.md`. It also carried no
hero, which is why `comingSoon()` in `library.html` had it greyed out and
sorted behind every other lesson: `comingSoon(l)` is `!LESSON_IMAGES[l.file]`.

All 27 items survive in count, so the deck scores exactly what the page
scored. Nine stems were rewritten, every one of them because a distractor was
also a defensible answer — see `prepb1_data.py` for the list and the reasoning.
What is new beyond that:

- **Five teaching slides now exist. None did.** They cover precisely what the
  27 items test — in/on/at for place, the four neighbours (between, among,
  opposite, behind), in/on/at plus for/since/during/by for time, the movement
  set, and the fixed verb/adjective pairs.
- **One item was taught backwards and is corrected.** The `time` section said
  "on the weekend" is British English. It is the American form; British English
  is "at the weekend", and `at` was sitting in the same option list — so a
  learner taught British English picked it, was marked wrong, and was then
  handed the inverse of the rule. The sentence now tests a named day.
- **The teach slides no longer print the answers.** Every example on them was
  the item sentence verbatim — "The keys are in the drawer", "In 1998, on
  Saturday mornings, at 9 a.m." — which answered ten of the twenty-one
  place/time/movement items on the slide immediately before them. The rule
  travels; the sentence does not.
- **German and Spanish.** The page was English-only.

Artwork is `PrepositionsB1/hero.jpg` — a flat-shape town street with two
figures standing opposite each other across a gap, shopfronts behind them.
The picture is the grammar: between, opposite and behind are all in frame.
The palette is derived from it with `--light`; every contrast row PASSes.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from prepb1_data import PLACE, TIME, MOVEMENT, DEPENDENT, ALL

TPL = 'lesson-template/lesson-template.html'
OUT = 'b1_prepositions_double_lesson.html'
F = 'PrepositionsB1'

# python3 lesson-template/extract-palette.py PrepositionsB1/hero.jpg --light
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #bacac6;
  --surface       : #ced7d5;
  --surface2      : #c4d0cd;
  --border        : #96684a;
  --text          : #2a1b11;
  --text-dim      : #5e412e;
  --accent        : #9d3f03;
  --accent-bright : #6d2a00;
  --accent-dim    : #eb7930;
  --secondary     : #2c3a47;
  --contrast      : #0a524c;''' % F

CHIPS = ['between', 'among', 'opposite', 'behind', 'during', 'by',
         'along', 'look forward to', 'good at']

# One backdrop per activity, from the same four-up Midjourney grid as the hero,
# so every section is the same street at a different moment. The teach slide
# that opens a section carries its background too, which is what makes the
# change read as "new section" rather than "different picture". HOUSE-STYLE §5b:
# swap the pattern, never paste a box.
BG_PLACE, BG_TIME, BG_MOVE, BG_DEP = ('bg05.jpg', 'bg02.jpg',
                                      'bg03.jpg', 'bg04.jpg')

# The activation stage is the densest slide in the deck — two task cards, the
# chip strip and a textarea — and the last thing the learner sees, so it gets a
# picture of its own rather than falling back to the cover's. Chosen by measuring
# edge energy over the slide's own footprint, not by eye: 9.57 against 11.61 and
# 15.90 for the other two candidates.
BG_ACT = 'bg06.jpg'

ACTIVITIES = [
    (PLACE, 'a', 'Activity 1 &middot; Place', 'Where is it?'),
    (TIME, 'b', 'Activity 2 &middot; Time', 'When does it happen?'),
    (MOVEMENT, 'c', 'Activity 3 &middot; Movement', 'Which way does it go?'),
    (DEPENDENT, 'd', 'Activity 4 &middot; Fixed pairs',
     'Which preposition does the word demand?'),
]


def build():
    D.assert_no_key_is_longest(ALL, 'PrepB1')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Prepositions <em>Double Lesson</em>',
                'Place, time, movement, and the pairs that have to be '
                'learned whole',
                [('Level', 'B1 &middot; Intermediate'),
                 ('Focus', 'Prepositions'),
                 ('Count', '27 questions')])

        + D.teach('t1Eyebrow', 'Part 1 &middot; Before you start',
                  't1Title', 'In, on, at &mdash; the three that do most of the work',
                  [('t1ah', 'Inside a space', 't1ab',
                    '<strong>In</strong> means enclosed. A drawer, a box, a '
                    'room, a pocket &mdash; if it has sides and something '
                    'can sit inside them, it takes <em>in</em>.', 't1an',
                    'The spare batteries are <em>in</em> the box.'),
                   ('t1bh', 'On a surface', 't1bb',
                    '<strong>On</strong> means touching a surface. The '
                    'surface does not have to be flat or horizontal &mdash; '
                    'a wall and a ceiling both take <em>on</em>.', 't1bn',
                    'A notice goes <em>on</em> the door; a crack goes '
                    '<em>in</em> it. The surface takes <em>on</em>, the '
                    'material takes <em>in</em>.'),
                   ('t1ch', 'At a point', 't1cb',
                    '<strong>At</strong> marks one specific point rather '
                    'than an area &mdash; an entrance, a desk, a bus stop, '
                    'the traffic lights.', 't1cn',
                    '<em>At</em> fixes a spot on the map. <em>In</em> '
                    'fills it.')],
                  folder=F, bg=BG_PLACE)

        + D.teach('t2Eyebrow', 'Part 1 &middot; Before you start',
                  't2Title', 'Four more that describe a position',
                  [('t2ah', 'Two, or more than two', 't2ab',
                    '<strong>Between</strong> needs exactly two clear '
                    'points &mdash; the chemist sits between the two '
                    'cafés. <strong>Among</strong> puts you inside a '
                    'larger, vaguer group of three or more.', 't2an',
                    'Between two named places; among a forest of them.'),
                   ('t2bh', 'Facing it', 't2bb',
                    '<strong>Opposite</strong> means facing something, '
                    'usually across a street or a room. The two things look '
                    'at each other.', 't2bn',
                    'Not the same as <em>next to</em>, which is side '
                    'by side.'),
                   ('t2ch', 'Out of sight', 't2cb',
                    '<strong>Behind</strong> puts something at the back of '
                    'something else, often hidden by it &mdash; the ball '
                    'behind the curtain.', 't2cn',
                    'Its opposite is <em>in front of</em>, not '
                    '<em>before</em>, which is about time.')],
                  folder=F, bg=BG_PLACE)

        + "".join(D.mc(i + 1, len(PLACE), q, 'mcaEyebrow',
                       'Activity 1 &middot; Place', 'mcaTitle',
                       'Where is it?', folder=F, bg=BG_PLACE)
                  for i, q in enumerate(PLACE))

        + D.teach('t3Eyebrow', 'Part 1 &middot; Before you start',
                  't3Title', 'The same three words, now about time',
                  [('t3ah', 'Long, medium, exact', 't3ab',
                    '<strong>In</strong> takes the long periods &mdash; '
                    'years, months, seasons. <strong>On</strong> takes days '
                    'and dates. <strong>At</strong> takes clock times.',
                    't3an',
                    '<em>In</em> April, <em>on</em> 3 June, '
                    '<em>at</em> midnight.'),
                   ('t3bh', 'How long, or since when', 't3bb',
                    '<strong>For</strong> takes a length of time &mdash; '
                    'seven years, two hours. <strong>Since</strong> takes '
                    'the point it started from &mdash; a date, an event.',
                    't3bn',
                    '<em>For</em> ten minutes; <em>since</em> '
                    'Tuesday.'),
                   ('t3ch', 'Throughout, or no later than', 't3cb',
                    '<strong>During</strong> means throughout an event. '
                    '<strong>By</strong> marks a deadline &mdash; at that '
                    'time or before it, never after.', 't3cn',
                    '<em>By</em> noon is a deadline; <em>until</em> '
                    'noon is a period that ends there.')],
                  folder=F, bg=BG_TIME)

        + "".join(D.mc(i + 1, len(TIME), q, 'mcbEyebrow',
                       'Activity 2 &middot; Time', 'mcbTitle',
                       'When does it happen?', folder=F, bg=BG_TIME)
                  for i, q in enumerate(TIME))

        + D.teach('t4Eyebrow', 'Part 2 &middot; Before you start',
                  't4Title', 'Movement: the path matters, not the place',
                  [('t4ah', 'In, and onto', 't4ab',
                    '<strong>Into</strong> is movement from outside to '
                    'inside. <strong>Onto</strong> is movement that ends on '
                    'top of a surface. Both describe arriving, not sitting '
                    'still.', 't4an',
                    'She stepped <em>into</em> the lift; he lifted the '
                    'box <em>onto</em> the shelf.'),
                   ('t4bh', 'Enclosed, or open', 't4bb',
                    '<strong>Through</strong> goes in one side of an '
                    'enclosed space and out the other &mdash; a tunnel, a '
                    'forest. <strong>Across</strong> crosses an open area '
                    '&mdash; a lake, a square.', 't4bn',
                    '<em>Through</em> the forest; <em>across</em> '
                    'the square.'),
                   ('t4ch', 'Following a line', 't4cb',
                    '<strong>Along</strong> follows the length of something '
                    '&mdash; a river, a road. <strong>To</strong> is the '
                    'plain one: movement or transfer towards a destination '
                    'or a person.', 't4cn',
                    'They walked <em>along</em> the canal; she passed the '
                    'keys <em>to</em> her neighbour.')],
                  folder=F, bg=BG_MOVE)

        + "".join(D.mc(i + 1, len(MOVEMENT), q, 'mccEyebrow',
                       'Activity 3 &middot; Movement', 'mccTitle',
                       'Which way does it go?', folder=F, bg=BG_MOVE)
                  for i, q in enumerate(MOVEMENT))

        + D.teach('t5Eyebrow', 'Part 2 &middot; Before you start',
                  't5Title', 'Some prepositions are not a choice at all',
                  [('t5ah', 'The verb chooses for you', 't5ab',
                    'Certain verbs take one fixed preposition and no other. '
                    'You <em>depend on</em>, you <em>insist on</em>, you '
                    '<em>apologise for</em>. There is no logic to recover '
                    '&mdash; there is only the pair.',
                    't5an',
                    'Learn the verb and its preposition as one item, the '
                    'way you learn a word.'),
                   ('t5bh', 'So does the adjective', 't5bb',
                    'Adjectives behave the same way. <em>Interested '
                    'in</em>, <em>worried about</em>, <em>good at</em> '
                    '&mdash; swapping the preposition does not give you a '
                    'variant, it gives you an error.', 't5bn',
                    'Good <em>at</em> a skill. Good <em>for</em> your '
                    'health. Different pairs, different meanings.'),
                   ('t5ch', 'Why guessing fails', 't5cb',
                    'Your own language pairs these words differently, so '
                    'translating the preposition is the one strategy '
                    'guaranteed to be wrong. The pair has to be memorised '
                    'whole.', 't5cn',
                    'If a fixed phrase feels swappable, that feeling is '
                    'wrong.')],
                  folder=F, bg=BG_DEP)

        + "".join(D.mc(i + 1, len(DEPENDENT), q, 'mcdEyebrow',
                       'Activity 4 &middot; Fixed pairs', 'mcdTitle',
                       'Which preposition does the word demand?', folder=F, bg=BG_DEP)
                  for i, q in enumerate(DEPENDENT))

        + D.results('resNext', 'You can spot it. Now use it &rarr;', folder=F)

        + D.activate('Describe where, when and how',
                     'Use at least three:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you has just moved to the other’s town and '
                     'needs to find five places. One asks, one directs. '
                     'Four minutes each, then swap.',
                     ['Direct your partner to a shop that sits '
                      '<em>between</em> two others, and to one '
                      '<em>opposite</em> the station.',
                      'Say how long you have lived where you live, using '
                      '<em>for</em> and <em>since</em>, and what changed '
                      '<em>during</em> that time.',
                      'Tell your partner three things you are '
                      '<em>good at</em>, <em>interested in</em> or '
                      '<em>worried about</em>, and why.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Write directions for a friend arriving at your local '
                     'station for the first time: where to meet you, how to '
                     'get there, and what time to be there by. Use at least '
                     'three of the expressions above.',
                     'Meet me at…',
                     folder=F, bg=BG_ACT)
    )

    import i18n_prepb1 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Prepositions Double Lesson (B1) | Forbes English',
                   I, langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d questions, %d bytes'
          % (OUT, s.count('<section class="slide'), len(ALL), len(s)))


if __name__ == '__main__':
    build()
