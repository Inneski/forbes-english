# -*- coding: utf-8 -*-
"""LEGO Prepositions & Phrasal Verbs — Part 2 (B2) — the 27 scored items.

Lifted from the scrolling `forbes-english-lego-lesson-part2.html`, a five-tab
quiz page with no pre-teaching at all — every rule lived only in the
per-answer feedback, the exact defect recorded against both Lego B2 decks in
`docs/HANDOFF.md`. All 27 items survive unchanged in substance:

  MC   — 6 multiple-choice items on prepositions and phrasal verbs
  FITB — 5 fill-in-the-blank items, one word bank shared by all five
  TF   — 6 true/false items on whether an underlined phrase is used correctly
  MATCH— 5 building/progress phrasal verbs matched to their definitions
  EC   — 5 error-correction items, each already a 4-option multiple choice

TF is built with the deck's own `mc()` as a two-option True/False question —
there is no dedicated true/false slide type, and a two-option MC is exactly
what the page already was. EC is likewise left as multiple choice: unlike the
Lego Car Building pair, this page's error-correction was already "pick the
correct replacement from four", not "type the correction", so there is
nothing to convert.

Every explanation is the page's own. Nothing is dropped; the shorter
distractors and the 4/6 true-skew on TF are the source content, not a
building error.
"""

# Every `why` below is a UI_I18N key, not inline text — the deck ships three
# languages, and a key translates with the rest of the chrome instead of
# leaving the explanation stuck in English. See HOUSE-STYLE.md §7 and §8.

# ── Activity 1: multiple choice ─────────────────────────────────────────
MC = [
    dict(stem='When the LEGO Technic crane tipped over, all the gear pieces '
              'fell ______ the table and scattered across the floor.',
         options=['off', 'out of', 'over', 'down from'], correct=0, why='q1why'),
    dict(stem='The instruction booklet says to connect the axle pin ______ '
              'the 3L beam before attaching it to the chassis.',
         options=['across from', 'inside of', 'through', 'next to'],
         correct=2, why='q2why'),
    dict(stem='The new LEGO set sold ______ within hours of being released '
              'on the official website.',
         options=['out', 'off', 'up', 'away'], correct=0, why='q3why'),
    dict(stem='He ______ assembling the castle at midnight and finally '
              'finished it at dawn.',
         options=['set off', 'got round to', 'turned up for', 'went down with'],
         correct=1, why='q4why'),
    dict(stem='The minifigures were arranged ______ the LEGO city street in '
              'a parade formation.',
         options=['alongside', 'in between', 'beyond', 'overhead'],
         correct=0, why='q5why'),
    dict(stem='She could not ______ why the instructions skipped from Step '
              '8 directly to Step 12.',
         options=['put up with', 'make out', 'look into', 'get away with'],
         correct=1, why='q6why'),
]

# ── Activity 2: fill in the blank ───────────────────────────────────────
# (sentence with ______, [answer(s)], why-key)
FITB = [
    ('The motorised LEGO train ______ halfway along the track because the '
     'battery had run out.',
     ['broke down'], 'f1why'),
    ('______ its complexity, the 9,000-piece LEGO Eiffel Tower took a full '
     'week to complete.',
     ['owing to'], 'f2why'),
    ('______ the main model, the set includes alternate building '
     'instructions for a smaller version.',
     ['in addition to'], 'f3why'),
    ('After the school holidays, the LEGO club met to ______ the building '
     'challenge they had missed.',
     ['catch up on'], 'f4why'),
    ('While sorting through an old box, she ______ a vintage 1980s LEGO '
     'Space set still in its original packaging.',
     ['stumbled upon|stumbled on'], 'f5why'),
]

# Bank order deliberately not the answer order — see assert_bank_is_not_a_key.
FITB_BANK = ['stumbled upon', 'pass on', 'catch up on', 'as a result of',
             'owing to', 'broke down', 'in addition to']

# ── Activity 3: true or false, as two-option MC ─────────────────────────
# (sentence with the tested phrase <u>underlined</u>, is_true, why-key)
TF = [
    ('The red 2&times;4 brick sits <u>on top of</u> the yellow base plate, '
     'forming the first layer of the wall.', True, 't1why'),
    ('She carefully took the Millennium Falcon <u>apart from</u> to sort '
     'the pieces by colour before rebuilding it.', False, 't2why'),
    ('The LEGO store was <u>run out of</u> the exclusive minifigure, so we '
     'had to order it online.', False, 't3why'),
    ('The builder was so absorbed in the project that she stayed up all '
     'night to finish it <u>on time</u>.', True, 't4why'),
    ('He looked the missing piece <u>up</u> on the LEGO parts website and '
     'ordered a replacement.', True, 't5why'),
    ('The new set comes <u>along with</u> a collector&rsquo;s booklet '
     'detailing the history of LEGO space sets.', True, 't6why'),
]

# ── Activity 4: terms and definitions ───────────────────────────────────
MATCH = [
    ('build up to', 'to prepare or develop towards something significant'),
    ('fall apart', 'to break into pieces or stop functioning completely'),
    ('piece together', 'to gradually assemble information or objects into a whole'),
    ('go through with', 'to complete something difficult that was planned'),
    ('branch out into', 'to start doing something new beyond your usual activity'),
]

# ── Activity 5: error correction, as multiple choice ────────────────────
EC = [
    dict(stem='The LEGO designer came <s>with up</s> a brilliant concept '
              'for a modular apartment building.',
         options=['up with', 'out of', 'about with', 'through on'],
         correct=0, why='e1why'),
    dict(stem='She was looking <s>forward for</s> the annual LEGO '
              'convention, which she had attended every year for a decade.',
         options=['forward to', 'forward about', 'forward into', 'ahead for'],
         correct=0, why='e2why'),
    dict(stem='The missing tile piece was hidden <s>in the bottom</s> of '
              'the box, underneath a pile of Technic connectors.',
         options=['at the bottom', 'on the bottom', 'by the bottom', 'to the bottom'],
         correct=0, why='e3why'),
    dict(stem='He finally managed to <s>sort away</s> all 3,000 pieces '
              'into labelled storage drawers after a full weekend of work.',
         options=['sort out', 'sort off', 'sort over', 'sort aside'],
         correct=0, why='e4why'),
    dict(stem='The new LEGO sustainability report focused on the '
              'environmental <s>impact in</s> using plant-based plastic '
              'materials.',
         options=['impact of', 'impact at', 'impact with', 'impact on'],
         correct=0, why='e5why'),
]
