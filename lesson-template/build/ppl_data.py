# -*- coding: utf-8 -*-
"""Present Perfect with Lego (B1) — the twenty-six scored items.

Lifted from the scrolling `forbes-english-present-perfect-lego-b1.html`, a
Lego-themed drill on Present Perfect Simple against Present Perfect
Continuous, colour-coded teal for Simple and pale teal for Continuous. Seven
multiple choice, seven gap-fills, six sentences to rebuild from word bricks
and six time expressions to match to a tense — the Polish glosses on the
matching column belong to the original and are kept. All twenty-six survive.

One item is rewritten. **Multiple choice question 1 was ungrammatical.** The
stem read "My nephew _____ this Lego castle three times this week" and the
key was "has built it", which builds "has built it this Lego castle" — the
object appears twice. Two of the three distractors carried the same fault, so
three of four options were unsayable and the one clean option was wrong. The
stem is kept and the four options are rebuilt around the bare participle
phrase: the key is now "has built", and the distractors are "built",
"has been building" and "was building". The item still does the job it was
written for — an unfinished-time marker ("this week") plus a countable
repetition ("three times") forces Present Perfect Simple over past simple and
over the continuous.

The gap answers are widened. The page compared the typed string against a
short list with `===` after lowercasing, so "'s been working" and "havent
found" were both marked wrong when a learner had the grammar exactly right.
Every answer below carries its contraction and its apostrophe-less spelling
pipe-separated inside one string. Gap seven also accepts "have completed":
this is en_GB and "our team have" is standard collective agreement, which the
original refused.

Multiple-choice keys sat at 1, 2, 0, 3, 0, 1, 1 — position 1 three times and
position 2 only once. Respread across all four below.
"""

# ── Activity 1: multiple choice ────────────────────────────────────────
# original key positions: [1, 2, 0, 3, 0, 1, 1]
MC_POS = [2, 0, 3, 1, 2, 3, 0]

_MC_RAW = [
    ("My nephew _____ this Lego castle three times this week &mdash; he loves "
     "rebuilding it.",
     ["has built", "built", "has been building", "was building"],
     "q1why"),

    ("Look at the table &mdash; pieces everywhere! She _____ all afternoon.",
     ["has been sorting", "has sorted them", "sorted them now",
      "sorts them here"],
     "q2why"),

    ("We _____ the new Falcon set yet &mdash; it only arrived this morning.",
     ["haven&rsquo;t opened", "didn&rsquo;t open it", "haven&rsquo;t been open",
      "don&rsquo;t open it"],
     "q3why"),

    ("Marek _____ Lego sets since he was six years old.",
     ["has been collecting", "was collecting them", "has collected them all",
      "is always collecting"],
     "q4why"),

    ("How many minifigures _____ in your whole collection?",
     ["have you got", "are you having", "do you having", "did you have"],
     "q5why"),

    ("The instructions _____ confusing, and I still can&rsquo;t find step 12.",
     ["have been", "have being so", "are being now", "were being so"],
     "q6why"),

    ("My hands hurt because I _____ tiny pieces for the last hour.",
     ["have been sorting", "have sorted out", "sort them now",
      "sorted them up"],
     "q7why"),
]


def _place(options, pos):
    key, rest = options[0], list(options[1:])
    return rest[:pos] + [key] + rest[pos:]


MC = [dict(stem=stem, options=_place(opts, pos), correct=pos, why=why)
      for (stem, opts, why), pos in zip(_MC_RAW, MC_POS)]

assert [q['options'][q['correct']] for q in MC] == [r[1][0] for r in _MC_RAW], \
    'reordering lost a key'


# ── Activity 2: the gaps ───────────────────────────────────────────────
FIB = [
    ("I ______ (finish) the Eiffel Tower set already, so we can start the next "
     "box tonight.",
     ["have finished|'ve finished|ve finished"], "g1why"),

    ("She ______ (work) on that Technic crane for two days &mdash; it&rsquo;s "
     "an enormous build.",
     ["has been working|'s been working|s been working"], "g2why"),

    ("They ______ (not find) the missing wheel piece yet, even after checking "
     "every box.",
     ["haven't found|havent found|have not found"], "g3why"),

    ("We ______ (build) Lego sets together every weekend since 2019.",
     ["have been building|'ve been building|ve been building"], "g4why"),

    ("This is the third time he ______ (drop) that minifigure on the floor "
     "today!",
     ["has dropped|'s dropped|s dropped"], "g5why"),

    ("My eyes are tired because I ______ (read) the instruction booklet under "
     "poor light for ages.",
     ["have been reading|'ve been reading|ve been reading"], "g6why"),

    ("Our team ______ (complete) all twelve modular buildings in the city "
     "collection.",
     ["has completed|'s completed|s completed|have completed|'ve completed|"
      "ve completed"], "g7why"),
]

# The page had no word bank for this activity and needs none: the verb sits in
# brackets after the gap, so the task is to inflect a given lemma, not to pick
# a word. A bank of the seven answers would just be the key laid out flat.
BANK = None


# ── Activity 3: sentence building ──────────────────────────────────────
# (chunks, why)
ORDER = [
    (["She", "has", "designed", "her", "own", "spaceship", "model"], "o1why"),

    (["He", "has", "been", "painting", "bricks", "all", "morning"], "o2why"),

    (["We", "have", "never", "seen", "such", "a", "huge", "set"], "o3why"),

    (["The", "twins", "have", "been", "arguing", "about", "the",
      "instructions"], "o4why"),

    (["I", "have", "already", "sorted", "the", "blue", "pieces"], "o5why"),

    (["She", "has", "been", "waiting", "for", "the", "new", "set", "for",
      "months"], "o6why"),
]


# ── Activity 4: matching ───────────────────────────────────────────────
# time expression (with the original's Polish gloss) → tense
# The original called this a matching activity, but its six right-hand cells
# held only two distinct values — Simple or Continuous — so it was a sort
# wearing a match's clothes, and `match()` cannot pair six terms to two
# definitions. It is a sort slide here, which is what it always was.
#
# Each cue also carried a Polish gloss ("just / właśnie"). Polish is not one of
# the site's nine languages and the deck's own switcher does not offer it, so a
# Polish-only crutch inside the English would have been the one language a
# learner could not turn off. The cues stand in English; the L1 support is the
# switcher.
SORT_BINS = ['Present Perfect Simple', 'Present Perfect Continuous']

SORT = [
    ('just', 0),
    ('ever', 0),
    ('how many times', 0),
    ('for the last few hours', 1),
    ('all day', 1),
    ('lately', 1),
]


# ORIGINAL EXPLANATIONS —
# q1: Use Present Perfect Simple (has built) because we count completed repetitions — 'three times' — not the ongoing activity itself.
# q2: Present Perfect Continuous (has been sorting) explains the visible mess now — it stresses the ongoing activity and its duration, not a finished result.
# q3: 'Yet' with a negative signals Present Perfect Simple (haven't opened) for an action expected but not completed.
# q4: 'Since' plus a long, unfinished period calls for Present Perfect Continuous (has been collecting) to highlight the duration of the habit.
# q5: 'Have' as a state verb (possession) doesn't normally take the continuous form, so Present Perfect Simple (have you got) is correct here.
# q6: A state (the instructions being confusing) that continues up to now uses Present Perfect Simple with 'been' — not a continuous form, since 'be' is a state verb.
# q7: The physical result (hurting hands) is explained by recent, continuous activity — 'for the last hour' confirms Present Perfect Continuous.
# g1: 'Already' with a completed task signals Present Perfect Simple: have/has + past participle (have finished).
# g2: 'For two days' measures duration of an ongoing task, so Present Perfect Continuous is needed: has been working.
# g3: 'Yet' in a negative sentence about a single expected outcome takes Present Perfect Simple: haven't found.
# g4: A repeated habit stretching from a point in the past ('since 2019') to now is expressed with Present Perfect Continuous: have been building.
# g5: Counting repeated single events ('the third time') uses Present Perfect Simple: has dropped, not the continuous form.
# g6: A present result (tired eyes) caused by an ongoing recent activity calls for Present Perfect Continuous: have been reading.
# g7: A finished total achievement with a clear result uses Present Perfect Simple: has completed.
# o1: A single completed achievement with a clear result takes Present Perfect Simple: has designed.
# o2: 'All morning' stresses duration of an ongoing activity, so Present Perfect Continuous fits: has been painting.
# o3: 'Never' describing life experience up to now is a classic Present Perfect Simple use: have never seen.
# o4: An ongoing, possibly unfinished activity (arguing) is expressed with Present Perfect Continuous: have been arguing.
# o5: 'Already' marks a completed action with a present result, so Present Perfect Simple is correct: have sorted.
# o6: 'For months' measures the length of an unfinished wait, calling for Present Perfect Continuous: has been waiting.
# m1: 'Just' refers to a very recently completed single action — Present Perfect Simple.
# m2: A measured recent duration signals Present Perfect Continuous.
# m3: 'Ever' asks about life experience as a whole — Present Perfect Simple.
# m4: 'All day' emphasises the ongoing span of an activity — Present Perfect Continuous.
# m5: Counting repetitions of a completed action uses Present Perfect Simple.
# m6: 'Lately' often points to a recent, possibly unfinished pattern of activity — Present Perfect Continuous.
