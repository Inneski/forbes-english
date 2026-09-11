# -*- coding: utf-8 -*-
"""Advanced Prepositions (B2) — the 28 scored items.

Lifted from the scrolling `b2_prepositions_advanced_lesson.html`, a four-section quiz
page with no teaching content at all: every rule lived only in the per-answer
feedback, which is the defect already recorded against the Lego and Twin Peaks
preposition decks in `docs/HANDOFF.md`. All 28 items survive unchanged in
substance and in count, so the deck scores exactly what the page scored.

**The options are rotated, and that is not cosmetic.** On the source page the
correct answer was written first in 25 of the 28 — and second in the other three. Engine shuffling
hides this at runtime, but `check-lesson.js` gates on the source order anyway,
and it is right to: the PDF export prints source order, so a printed hand-out
was an answer key with the column already filled in. Each item is now
left-rotated so the key lands at position `n % 4`, which preserves the option
set exactly and only moves where it sits.

Every `why` is a UI_I18N key rather than inline text — the deck ships English,
German and Spanish, and a key travels with the rest of the chrome instead of
leaving the explanation stuck in English. See HOUSE-STYLE.md §7 and §8.
"""


# ── PURPOSE ───────────────────────────────────────────────────────────
PURPOSE = [
    dict(stem="These boots were made ______ walking, according to the old song.",
         options=["for", "to", "in", "at"], correct=0, why="q1why"),
    dict(stem="I go to the gym every morning ______ get fit before work.",
         options=["for", "to", "in", "at"], correct=1, why="q2why"),
    dict(stem="She opened a separate account ______ paying university fees.",
         options=["with", "in", "for", "to"], correct=2, why="q3why"),
    dict(stem="He works two jobs ______ support his family back home.",
         options=["with", "by", "for", "to"], correct=3, why="q4why"),
    dict(stem="This attachment is designed ______ trimming hedges quickly.",
         options=["for", "to", "with", "at"], correct=0, why="q5why"),
    dict(stem="They arrived two hours early ______ get good seats at the front.",
         options=["for", "to", "with", "by"], correct=1, why="q6why"),
    dict(stem="I bought this cream specifically ______ reducing fine lines.",
         options=["with", "in", "for", "to"], correct=2, why="q7why"),
]

# ── IDIOM ─────────────────────────────────────────────────────────────
IDIOM = [
    dict(stem="Whether the picnic goes ahead depends ______ the weather forecast.",
         options=["of", "for", "at", "on"], correct=3, why="q8why"),
    dict(stem="In terms ______ salary, this offer is far better than my last job.",
         options=["of", "for", "with", "in"], correct=0, why="q9why"),
    dict(stem="I would like to say a few words ______ behalf of the whole team.",
         options=["at", "on", "in", "for"], correct=1, why="q10why"),
    dict(stem="______ spite of the heavy rain, the match continued as planned.",
         options=["At", "For", "In", "On"], correct=2, why="q11why"),
    dict(stem="After months of losses, the company is now ______ the verge of bankruptcy.",
         options=["in", "at", "of", "on"], correct=3, why="q12why"),
    dict(stem="He got the promotion ______ the expense of a colleague who had worked there longer.",
         options=["at", "on", "for", "with"], correct=0, why="q13why"),
    dict(stem="They stayed together for years ______ the sake of their children.",
         options=["at", "for", "of", "on"], correct=1, why="q14why"),
]

# ── DEPENDENT ─────────────────────────────────────────────────────────
DEPENDENT = [
    dict(stem="The manager accused the intern ______ leaking the confidential report.",
         options=["with", "about", "of", "for"], correct=2, why="q15why"),
    dict(stem="You can't blame the whole team ______ one person's mistake.",
         options=["of", "with", "on", "for"], correct=3, why="q16why"),
    dict(stem="After three attempts, she finally succeeded ______ passing her driving test.",
         options=["in", "at", "on", "with"], correct=0, why="q17why"),
    dict(stem="The heavy snowfall prevented the plane ______ taking off on time.",
         options=["with", "from", "of", "for"], correct=1, why="q18why"),
    dict(stem="Everyone congratulated her ______ her well-deserved promotion.",
         options=["of", "about", "on", "with"], correct=2, why="q19why"),
    dict(stem="This particular law firm specialises ______ corporate mergers and acquisitions.",
         options=["on", "at", "with", "in"], correct=3, why="q20why"),
    dict(stem="The advisory committee consists ______ five independent experts.",
         options=["of", "in", "with", "from"], correct=0, why="q21why"),
]

# ── PHRASAL ───────────────────────────────────────────────────────────
PHRASAL = [
    dict(stem="She has always looked up ______ her older sister as a role model.",
         options=["for", "to", "at", "on"], correct=1, why="q22why"),
    dict(stem="Honestly, I don't know how she puts up ______ her noisy neighbours every night.",
         options=["at", "on", "with", "for"], correct=2, why="q23why"),
    dict(stem="He never seems to get away ______ anything at school, unlike his classmates.",
         options=["for", "on", "at", "with"], correct=3, why="q24why"),
    dict(stem="We really need to come up ______ a better solution before Friday.",
         options=["with", "for", "on", "at"], correct=0, why="q25why"),
    dict(stem="He has a habit of looking down ______ people who did not go to university.",
         options=["with", "on", "at", "for"], correct=1, why="q26why"),
    dict(stem="It takes courage to stand up ______ what you believe in, even under pressure.",
         options=["on", "at", "for", "with"], correct=2, why="q27why"),
    dict(stem="My doctor has advised me to cut down ______ sugar and processed food.",
         options=["of", "for", "with", "on"], correct=3, why="q28why"),
]

ALL = PURPOSE + IDIOM + DEPENDENT + PHRASAL
assert len(ALL) == 28
