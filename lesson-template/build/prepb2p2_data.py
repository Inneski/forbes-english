# -*- coding: utf-8 -*-
"""Advanced Prepositions (B2) — Part 2 — the 28 scored items.

Lifted from the scrolling `b2_prepositions_advanced_lesson_part2.html`, a four-section quiz
page with no teaching content at all: every rule lived only in the per-answer
feedback, which is the defect already recorded against the Lego and Twin Peaks
preposition decks in `docs/HANDOFF.md`. All 28 items survive unchanged in
substance and in count, so the deck scores exactly what the page scored.

**The options are rotated, and that is not cosmetic.** On the source page the
correct answer was written first in all 28 — without a single exception. Engine shuffling
hides this at runtime, but `check-lesson.js` gates on the source order anyway,
and it is right to: the PDF export prints source order, so a printed hand-out
was an answer key with the column already filled in. Each item is now
left-rotated so the key lands at position `n % 4`, which preserves the option
set exactly and only moves where it sits.

**One stem was rewritten because none of the four options was natural.** The
`dependent` section read "The hotel boasts ______ a rooftop pool", keyed to
`about` — but a hotel *boasts a rooftop pool* with no preposition at all. That
transitive `boast` (to have as a feature) is a different verb from `boast
about` (to brag), and the sentence had picked the wrong one, so every option
was wrong and the key was merely the least wrong. The subject is now a person
bragging, which is what `boast about` is for. Same fault class as the seven
rewritten in `prepb1_data.py`, arriving by a different route.

Every `why` is a UI_I18N key rather than inline text — the deck ships English,
German and Spanish, and a key travels with the rest of the chrome instead of
leaving the explanation stuck in English. See HOUSE-STYLE.md §7 and §8.
"""


# ── TRENDS ────────────────────────────────────────────────────────────
TRENDS = [
    dict(stem="There has been a steady rise ______ demand for electric cars over the past five years.",
         options=["in", "of", "by", "at"], correct=0, why="q1why"),
    dict(stem="The company reported an increase ______ eight percent in quarterly revenue.",
         options=["from", "of", "in", "by"], correct=1, why="q2why"),
    dict(stem="Costs fell sharply, dropping ______ almost a fifth in just one year.",
         options=["in", "from", "by", "of"], correct=2, why="q3why"),
    dict(stem="Membership rose ______ 500 to over 800 within two years.",
         options=["by", "of", "at", "from"], correct=3, why="q4why"),
    dict(stem="Compared ______ its main competitor, this airline offers far better value for money.",
         options=["to", "for", "of", "at"], correct=0, why="q5why"),
    dict(stem="There is currently a serious shortage ______ affordable housing in the city centre.",
         options=["with", "of", "in", "for"], correct=1, why="q6why"),
    dict(stem="Staff satisfaction has improved dramatically ______ regard to flexible working arrangements.",
         options=["by", "for", "with", "upon"], correct=2, why="q7why"),
]

# ── IDIOM ─────────────────────────────────────────────────────────────
IDIOM = [
    dict(stem="She has been ______ charge of the marketing department since January.",
         options=["on", "at", "of", "in"], correct=3, why="q8why"),
    dict(stem="Most residents are ______ favour of the new cycling lanes.",
         options=["in", "on", "for", "at"], correct=0, why="q9why"),
    dict(stem="He offered to fix my car ______ return for a home-cooked meal.",
         options=["at", "in", "for", "on"], correct=1, why="q10why"),
    dict(stem="Taking another day off this week is completely out ______ the question.",
         options=["in", "at", "of", "for"], correct=2, why="q11why"),
    dict(stem="Firefighters say the blaze is now ______ control after burning for six hours.",
         options=["in", "on", "at", "under"], correct=3, why="q12why"),
    dict(stem="Her talent is ______ doubt the best I have seen on this course.",
         options=["beyond", "around", "before", "under"], correct=0, why="q13why"),
    dict(stem="______ addition to her salary, she receives a generous pension.",
         options=["With", "In", "On", "At"], correct=1, why="q14why"),
]

# ── DEPENDENT ─────────────────────────────────────────────────────────
DEPENDENT = [
    dict(stem="You can always rely ______ him to be on time, whatever the weather.",
         options=["at", "for", "on", "in"], correct=2, why="q15why"),
    dict(stem="Many local residents objected ______ the new road being built through the park.",
         options=["for", "against", "of", "to"], correct=3, why="q16why"),
    dict(stem="Please excuse me ______ interrupting, but I have an urgent question.",
         options=["for", "of", "from", "about"], correct=0, why="q17why"),
    dict(stem="The owner never stops boasting ______ the rooftop pool and its views.",
         options=["with", "about", "on", "for"], correct=1, why="q18why"),
    dict(stem="He resigned ______ his position shortly after the scandal became public.",
         options=["at", "with", "from", "of"], correct=2, why="q19why"),
    dict(stem="In her speech, the CEO referred ______ the recent changes in company policy.",
         options=["at", "about", "for", "to"], correct=3, why="q20why"),
    dict(stem="Small businesses will benefit greatly ______ the new tax relief scheme.",
         options=["from", "of", "with", "for"], correct=0, why="q21why"),
]

# ── PHRASAL ───────────────────────────────────────────────────────────
PHRASAL = [
    dict(stem="Managers need to deal ______ conflicts quickly and fairly.",
         options=["at", "with", "in", "for"], correct=1, why="q22why"),
    dict(stem="It can be hard to cope ______ so much pressure at once.",
         options=["on", "for", "with", "against"], correct=2, why="q23why"),
    dict(stem="It took him a long time to get ______ the loss of his job.",
         options=["off", "back", "down", "over"], correct=3, why="q24why"),
    dict(stem="Stop putting ______ the decision &mdash; you need to choose today.",
         options=["off", "up", "down", "out"], correct=0, why="q25why"),
    dict(stem="I came ______ an old photo of my grandparents while cleaning the attic.",
         options=["through", "across", "into", "over"], correct=1, why="q26why"),
    dict(stem="I ran ______ my old teacher at the supermarket yesterday.",
         options=["down", "up", "into", "over"], correct=2, why="q27why"),
    dict(stem="If you don't submit the report today, we'll fall ______ schedule.",
         options=["back", "off", "under", "behind"], correct=3, why="q28why"),
]

ALL = TRENDS + IDIOM + DEPENDENT + PHRASAL
assert len(ALL) == 28
