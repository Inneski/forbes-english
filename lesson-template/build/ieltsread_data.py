# -*- coding: utf-8 -*-
"""IELTS Reading: True / False / Not Given — the twelve items and the sort.

Written fresh. `ielts.html` had carried a disabled Reading card since the route
was split, and its own copy named the lesson: "True/False/Not Given first,
because that is where the most marks are lost — and it is technique, not
vocabulary, that recovers them."

**The three options are fixed and identical on every item**, which is not
laziness — it is the question type. What varies is the passage and the
statement. That has two consequences this file is built around:

1. **The options must be near-equal in length or the key gives itself away.**
   `Not Given` is inherently the longest label, so a bare `True / False / Not
   Given` set would fail `check-lesson.js`'s ANSWERS gate whenever the key was
   True — and it would fail it in the same direction on a third of the paper.
   Each option is therefore written as a full clause of comparable length.

2. **The key distribution is decided by the verdicts, not by shuffling.** The
   twelve items cycle True, False, Not Given, so the key lands at index
   `i % 3` and the spread is exactly even — four of each, which is also what a
   real paper does.

**Every item was checked for the second defensible reading.** The distinction
being taught — FALSE means the passage contradicts the statement, NOT GIVEN
means the passage is silent — collapses the moment a passage *implies*
something strongly, so no item here turns on an inference. `q6` is the one
that needed rewriting: the passage originally said the mill "employed most of
the village", and the statement "the village depended on the mill" is a fair
inference, which made NOT GIVEN and TRUE both arguable. The passage now states
the dependence outright and the statement tests a different fact.
"""

# The three verdicts, in one place. Written as clauses rather than as bare
# labels so that no verdict is the conspicuously short or long option: the
# type would otherwise leak the answer on every item where the key is True.
T = 'True &mdash; the passage clearly states this'
F = 'False &mdash; the passage clearly denies this'
N = 'Not Given &mdash; the passage does not say'
OPTS = [T, F, N]

# ── Activity 1 · False is not Not Given ────────────────────────────────
VERDICT = [
    dict(ctx='<em>The museum opened in 1897 and has never closed to the '
             'public, not even during the two wars.</em>',
         stem='Statement: the museum remained open throughout both wars.',
         options=OPTS, correct=0, why='r1why'),

    dict(ctx='<em>Ferries leave the harbour twice a day in summer and once a '
             'day for the rest of the year.</em>',
         stem='Statement: there are three summer sailings a day.',
         options=OPTS, correct=1, why='r2why'),

    dict(ctx='<em>The library holds forty thousand volumes, a quarter of them '
             'in Welsh.</em>',
         stem='Statement: the library intends to enlarge its Welsh holdings.',
         options=OPTS, correct=2, why='r3why'),

    dict(ctx='<em>Rebuilding began in 1954 and the tower was finished two '
             'years later, ahead of schedule.</em>',
         stem='Statement: the tower was completed in 1956.',
         options=OPTS, correct=0, why='r4why'),
]

# ── Activity 2 · the passage, not the world ────────────────────────────
WORLD = [
    dict(ctx='<em>Bees navigate largely by polarised light, which remains '
             'usable when the sun is behind cloud.</em>',
         stem='Statement: bees cannot navigate on an overcast day.',
         options=OPTS, correct=1, why='r5why'),

    dict(ctx='<em>The mill was the only employer for miles, and the village '
             'depended on it entirely.</em>',
         stem='Statement: the mill was sold to a competitor in 1902.',
         options=OPTS, correct=2, why='r6why'),

    dict(ctx='<em>Antarctica holds roughly seventy per cent of the world&rsquo;s '
             'fresh water, locked up as ice.</em>',
         stem='Statement: most of the planet&rsquo;s fresh water is in Antarctica.',
         options=OPTS, correct=0, why='r7why'),

    dict(ctx='<em>The survey covered eight hundred households across four '
             'coastal districts.</em>',
         stem='Statement: the survey was funded by the national government.',
         options=OPTS, correct=2, why='r8why'),
]

# ── Activity 3 · the word that decides it ──────────────────────────────
QUALIFY = [
    dict(ctx='<em>Most of the islanders speak both languages at home.</em>',
         stem='Statement: every islander speaks both languages at home.',
         options=OPTS, correct=1, why='r9why'),

    # This item said "the drug has been proven to shorten recovery" and was
    # keyed FALSE. It had two answers. A passage that hedges ("may", "the trial
    # was small") does not thereby DENY that a thing is proven — it simply does
    # not claim it — and real papers key that shape as NOT GIVEN about as often
    # as FALSE. The statement now tests a fact the passage is plainly silent
    # about, and the hedge stays in the passage where the teach card can point
    # at it.
    dict(ctx='<em>The drug may reduce recovery time in some patients, though '
             'the trial was small.</em>',
         stem='Statement: the drug has been approved for general use.',
         options=OPTS, correct=2, why='r10why'),

    dict(ctx='<em>Rainfall in the valley is lower than on the coast, and has '
             'been for a century.</em>',
         stem='Statement: the coast is wetter than the valley.',
         options=OPTS, correct=0, why='r11why'),

    dict(ctx='<em>The festival has run every summer since 1970, apart from '
             'two years in the 1980s.</em>',
         stem='Statement: the festival has never once been cancelled.',
         options=OPTS, correct=1, why='r12why'),
]

ALL = VERDICT + WORLD + QUALIFY

# ── The sorting task ───────────────────────────────────────────────────
# Not the verdicts themselves — the SIGNALS. Sorting True/False/Not Given
# statements would just be four more items; sorting what tips you towards each
# verdict is the decision the learner actually has to make under time.
SORT_BINS = ['Points to FALSE', 'Points to NOT GIVEN']
SORT_ITEMS = [
    ('A sentence in the passage contradicts it', 0),
    ('The passage gives a number that disagrees', 0),
    ('The passage says "most", the statement says "all"', 0),
    ('You are reasoning from what is likely', 1),
    ('The topic appears, but not this detail', 1),
    ('You know it is true from outside the text', 1),
]

SORT_WHY = ('The left column all name a <strong>sentence you could point '
            'at</strong>. The right column are all the ways a candidate '
            'reaches a verdict without one &mdash; inference, association, or '
            'general knowledge. That is the whole distinction: FALSE needs a '
            'line in the passage that says otherwise, and if you cannot put '
            'your finger on it, the answer is NOT GIVEN.')
