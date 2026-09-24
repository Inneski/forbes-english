# -*- coding: utf-8 -*-
"""IELTS Reading: Summary and Sentence Completion — the twelve items and the sort.

Written fresh, against the card on `ielts-reading.html`: "Where the word limit
does the damage. Answers come straight from the passage, spelling counts, and
'no more than two words' means a three-word answer scores nothing however
right it is." That sentence is the whole lesson, in three parts:

  1. **Read the limit first.** The instruction line decides what a word is
     (hyphenated = one, a number = one, "the" counts) and how many you get.
     Activity 1 tests the instruction alone — no passage, no summary — so
     that counting words is learnt before it has to be done under time.
  2. **Copy, do not paraphrase.** The summary paraphrases AROUND the gap so
     the learner finds the place by meaning and then lifts the word exactly
     as printed. Activity 2 gives a passage excerpt in `ctx` and a gapped
     summary sentence in the stem; the key is the passage word(s) within the
     limit, and the three distractors are the three ways a right idea scores
     nothing — a paraphrase, the passage words plus one too many, the passage
     word in the wrong form.
  3. **The gap has a shape.** Predict the word class before looking; the
     answer must read as a grammatical sentence. Activity 3 offers four
     forms of the same passage word and only one fits the grammar of the gap.

**The key cycles i % 4 across the twelve** — index 0, 1, 2, 3 in each
activity — so the position carries nothing and the spread is exactly even.

**The key is never the longest option, and the distractor set makes that
easy**: "the passage words plus one too many" is longer than the key by
construction, and a paraphrase usually runs longer too. `check-lesson.js`'s
short-key gate (1.5× and ten characters) is watched as well: the wrong-form
distractor is always within a few characters of the key.

**The limit travels in `ctx`, not in the stem.** `check-teach-leak.js` reads
the stem for verbatim runs reproduced on a teach card, and the teach cards
have to print "NO MORE THAN TWO WORDS AND/OR A NUMBER" — that is the
instruction being taught. Kept out of the stem, the instruction is cited on
the teach slide and repeated on the item without tripping the gate; the stem
carries only the gapped summary sentence.

**Every item was checked for the second defensible reading.** Item 2 first
offered `iron` alongside `well-known` under ONE WORD ONLY, and both are one
word; the option set is now two two-word phrases, a hyphenated word and a
two-word compound. Item 12 first turned on "four hundred" against "400",
which real papers accept either way; it now turns on plural after a number,
which they do not.
"""

# ── Activity 1 · read the instruction ──────────────────────────────────
# No passage. The instruction line is the whole context, and the question is
# what it allows. "The" is a word; a number is a number; a hyphen joins.
INSTRUCT = [
    dict(ctx='<strong>Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each '
             'answer.</strong>',
         stem='Which of these answers is allowed by that limit?',
         options=['1997 survey results',
                  'the 1997 survey results',
                  'results of the survey',
                  'survey results from 1997'],
         correct=0, why='r1why'),

    dict(ctx='<strong>Write ONE WORD ONLY for each answer.</strong>',
         stem='Which of these counts as one word?',
         options=['arched bridge',
                  'well-known',
                  'iron arches',
                  'cast iron'],
         correct=1, why='r2why'),

    dict(ctx='<strong>Write NO MORE THAN THREE WORDS AND/OR A NUMBER for '
             'each answer.</strong>',
         stem='Which of these answers breaks the limit?',
         options=['in 1846',
                  'nearly 200 tonnes',
                  'a fall of 200 tonnes',
                  'some 200 tonnes each'],
         correct=2, why='r3why'),

    dict(ctx='<strong>Complete the summary using the list of words, A&ndash;H, '
             'below.</strong>',
         stem='What does that instruction change?',
         options=['Each word in the list is used exactly once',
                  'The summary covers the whole passage, start to end',
                  'The limit now counts letters instead of words',
                  'The answers might not appear in the passage at all'],
         correct=3, why='r4why'),
]

# ── Activity 2 · copy, do not paraphrase ───────────────────────────────
# A passage excerpt, a limit, and a summary sentence with one gap. The key is
# the passage word(s); the distractors are a paraphrase, the passage words
# plus one too many, and the passage word in the wrong form.
COPY = [
    dict(ctx='<em>The reef lost almost half its coral cover in a single '
             'decade, largely because warmer water triggers a process known '
             'as bleaching.</em><br><strong>NO MORE THAN TWO WORDS</strong>',
         stem='Rising sea temperatures cause ______, which stripped the reef '
              'of much of its coral.',
         options=['bleaching',
                  'coral whitening',
                  'bleached',
                  'known as bleaching'],
         correct=0, why='r5why'),

    dict(ctx='<em>Most of the town&rsquo;s drinking water is drawn from a '
             'limestone aquifer, and the council fears it cannot sustain '
             'further housing.</em><br><strong>NO MORE THAN TWO WORDS</strong>',
         stem='The town depends on a ______ for most of its supply.',
         options=['underground reservoir',
                  'limestone aquifer',
                  'a limestone aquifer',
                  'limestone aquifers'],
         correct=1, why='r6why'),

    dict(ctx='<em>The instrument was calibrated twice a year by a visiting '
             'engineer, a routine the observatory kept up until 1962.</em>'
             '<br><strong>NO MORE THAN TWO WORDS AND/OR A NUMBER</strong>',
         stem='A ______ checked the instrument every six months until 1962.',
         options=['travelling technician',
                  'visiting engineers',
                  'visiting engineer',
                  'a visiting engineer'],
         correct=2, why='r7why'),

    dict(ctx='<em>Farmers in the valley abandoned wheat after three failed '
             'harvests and planted olives, which tolerate the thin soil far '
             'better.</em><br><strong>ONE WORD ONLY</strong>',
         stem='After repeated crop failures, the valley&rsquo;s farmers '
              'switched to growing ______.',
         options=['olive groves',
                  'olive',
                  'planted olives',
                  'olives'],
         correct=3, why='r8why'),
]

# ── Activity 3 · the gap has a shape ───────────────────────────────────
# Four forms, one passage, one grammatical fit. The learner who predicts the
# word class before reading the options has already thrown three away.
SHAPE = [
    dict(ctx='<em>The lighthouse keeper recorded the weather in a '
             'leather-bound ledger, and his entries grow noticeably briefer '
             'after the automation of 1911.</em><br><strong>ONE WORD '
             'ONLY</strong>',
         stem='The keeper&rsquo;s ______ became shorter after 1911.',
         options=['entries',
                  'recorded',
                  'briefer',
                  'noticeably'],
         correct=0, why='r9why'),

    dict(ctx='<em>Although the dam was widely expected to fail, the engineers '
             'reinforced its base with granite and it has held for a '
             'century.</em><br><strong>NO MORE THAN TWO WORDS</strong>',
         stem='The engineers ______ the base of the dam with granite.',
         options=['reinforcement',
                  'reinforced',
                  'reinforcing',
                  'reinforces'],
         correct=1, why='r10why'),

    dict(ctx='<em>The species was first described in 1834 by a naturalist who '
             'mistook its fossil for a large bird; only in 1923 were the '
             'bones correctly identified.</em><br><strong>NO MORE THAN TWO '
             'WORDS AND/OR A NUMBER</strong>',
         stem='The fossil was not ______ until 1923.',
         options=['correctly identify',
                  'correct identification',
                  'correctly identified',
                  'identifying correctly'],
         correct=2, why='r11why'),

    dict(ctx='<em>The tunnel took eleven years to bore, and the crews met '
             'beneath the mountain within a few centimetres of the surveyed '
             'line.</em><br><strong>NO MORE THAN TWO WORDS AND/OR A '
             'NUMBER</strong>',
         stem='Boring the tunnel took ______.',
         options=['eleven year',
                  'eleventh years',
                  'an eleven years',
                  'eleven years'],
         correct=3, why='r12why'),
]

ALL = INSTRUCT + COPY + SHAPE

# ── The sorting task ───────────────────────────────────────────────────
# Six answers a candidate might write, sorted by what the marker does with
# them. Three score; three score nothing, and every one of the three is a way
# of being right and getting no mark for it.
SORT_BINS = ['Scores', 'Scores nothing']
SORT_ITEMS = [
    ('Two words copied exactly from the passage', 0),
    ('A number written as digits', 0),
    ('A hyphenated word under a one-word limit', 0),
    ('Three words when the limit is two', 1),
    ('The right idea in your own words', 1),
    ('The passage word with a spelling mistake', 1),
]

SORT_WHY = ('Everything in the left column is <strong>the passage, within '
            'the limit, spelt as printed</strong> &mdash; a number is one item, '
            'a hyphenated word is one word. The right column holds three ways of '
            'understanding the text and scoring nothing for it: one word over '
            'the limit, a correct idea in different words, a copied word with '
            'a letter wrong. The marker does not read for meaning. The marker '
            'compares your answer with the key.')
