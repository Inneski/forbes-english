# -*- coding: utf-8 -*-
"""IELTS Reading: Yes / No / Not Given — the twelve items and the sort.

Written fresh, as the sibling of `ieltsread_data.py` (True / False / Not
Given). Same three-way decision, a different question: TFNG asks what the
passage SAYS, YNNG asks what the writer THINKS. So every passage here is a
piece of argument, and every item turns on one of the three things that
decide a writer's view:

  1. **whose voice a sentence is in** — a view the writer only reports
     (critics argue, it is often claimed) is not the writer's until the
     writer judges it;
  2. **the concession and the turn** — both halves of "Admittedly … but"
     are the writer's; the turn outweighs the concession, it does not
     cancel it;
  3. **how strongly the writer means it** — degree (largely ≠ completely),
     hedges (may commits to nothing), evaluation words (surprisingly).

**The verdicts are one fixed set, written as clauses of near-equal
length**, for the reason `ieltsread_data.py` gives: a bare `Yes / No / Not
Given` makes Not Given the conspicuously long option on every item where it
is the key. The gloss after the dash translates, as it now does in that
deck too; the verdict word stays English, because it is what goes on the
answer sheet. `build_ieltsynng.py` checks the lengths in every language, not
only in English.

**The keys cycle YES, NO, NOT GIVEN**, so the key sits at `i % 3` and the
spread is exactly four of each.

**Every item was checked for a second defensible reading**, the house rule
from the TFNG deck. Three drafts failed it and were dropped, and the shapes
are worth avoiding in any item added later:

  * a NOT GIVEN on electric cars read "not yet cheaper to buy" against "will
    soon be cheaper": "not yet" implies the writer expects it, a YES by
    implicature.
  * a NOT GIVEN on scope ("the finest building the city has put up in fifty
    years" against "the finest in the city") carries the implicature that
    something older is finer, which argues for NO. Scope items all carry
    one; the hedge and the unstated reason (q9, q12) do not.
  * a NO on the teach card ("the trial proved the treatment works", against
    "Admittedly, the trial was small"): "small" arguably denies "proved",
    the same two-answer shape `ieltsread_data.py` q10 was rewritten for. The
    card makes its point with both halves held and no third statement.
"""

# The verdicts: (UI_I18N key, English). The key goes on an inner span, not on
# the button, because the engine prepends the A/B/C letter INTO the button at
# load and the language pass sets innerHTML — on the button it would wipe the
# letter off every option the moment a learner switched language.
VERDICTS = [('optYes', 'Yes &mdash; the writer agrees with this'),
            ('optNo', 'No &mdash; the writer disagrees with this'),
            ('optNG', 'Not Given &mdash; the writer does not say')]
OPTS = ['<span data-i18n="%s">%s</span>' % kv for kv in VERDICTS]

# ── Activity 1 · whose view is it? ─────────────────────────────────────
VOICE = [
    dict(ctx='<em>Supporters of the four-day week say that it raises '
             'productivity. On the evidence of the trials so far, they are '
             'right.</em>',
         stem='Statement: a four-day week makes staff more productive.',
         options=OPTS, correct=0, why='r1why'),

    dict(ctx='<em>Critics dismiss the new tram line as an expensive toy. They '
             'are wrong: it already carries twenty thousand passengers a '
             'day.</em>',
         stem='Statement: the tram line serves little real purpose.',
         options=OPTS, correct=1, why='r2why'),

    dict(ctx='<em>It is often claimed that parks lower crime in the streets '
             'around them. Whatever the truth of that, they certainly make '
             'those streets pleasanter to live in.</em>',
         stem='Statement: parks reduce crime in the streets nearby.',
         options=OPTS, correct=2, why='r3why'),

    dict(ctx='<em>Many parents assume, mistakenly, that children raised with '
             'two languages fall behind at school.</em>',
         stem='Statement: growing up with two languages does not hold '
              'children back at school.',
         options=OPTS, correct=0, why='r4why'),
]

# ── Activity 2 · the concession and the turn ───────────────────────────
# One item per move: the turn overrules the concession (q5); a statement
# that goes past both halves (q6); the concession is the writer's own view
# (q7, through a double negative); and contradicting a concession is NO even
# when the statement sounds like the writer's side (q8).
TURN = [
    dict(ctx='<em>The new library cost twice what was promised and opened a '
             'year late. Even so, I would build it again tomorrow.</em>',
         stem='Statement: building the library was a mistake.',
         options=OPTS, correct=1, why='r5why'),

    dict(ctx='<em>Admittedly, the new timetable has made some journeys longer. '
             'But the buses now arrive when they say they will, and that is '
             'what passengers asked for.</em>',
         stem='Statement: more people have used the buses since the '
              'timetable changed.',
         options=OPTS, correct=2, why='r6why'),

    dict(ctx='<em>Coursework tells us far more about a student than a '
             'three-hour exam can. This is not to say that exams have no '
             'place: for comparing students from different schools, nothing '
             'fairer has been found.</em>',
         stem='Statement: exams still have a useful part to play.',
         options=OPTS, correct=0, why='r7why'),

    dict(ctx='<em>Working from home has obvious benefits, and I do not '
             'dispute them. Yet for someone starting out, the cost is too '
             'high: you learn a job by watching other people do it.</em>',
         stem='Statement: working from home has few real benefits.',
         options=OPTS, correct=1, why='r8why'),
]

# ── Activity 3 · how strongly does the writer mean it? ─────────────────
DEGREE = [
    dict(ctx='<em>The ban on plastic bags may have reduced litter on the '
             'beaches, though other changes came in that same year.</em>',
         stem='Statement: the ban on plastic bags reduced litter on the '
              'beaches.',
         options=OPTS, correct=2, why='r9why'),

    dict(ctx='<em>Surprisingly, the smallest schools in the study produced '
             'the best results.</em>',
         stem='Statement: the smallest schools did unexpectedly well.',
         options=OPTS, correct=0, why='r10why'),

    dict(ctx='<em>The housing plan has largely succeeded: most of the '
             'promised homes were built, if a year late.</em>',
         stem='Statement: the housing plan achieved everything it set out '
              'to do.',
         options=OPTS, correct=1, why='r11why'),

    dict(ctx='<em>The council was right to close the old bridge, though it '
             'handled the announcement badly.</em>',
         stem='Statement: the old bridge was no longer safe to use.',
         options=OPTS, correct=2, why='r12why'),
]

ALL = VOICE + TURN + DEGREE

# ── The sorting task ───────────────────────────────────────────────────
# Six ways a sentence can open, all about the same plan. The two that catch
# people are on the left: "Supporters rightly point out" reads as reported
# until you see the adverb, and "Admittedly" reads as the other side until
# you remember the writer is the one admitting it. The sentences are the
# English under test, so they stay English in every gloss; the bins and the
# explanation translate.
SORT_BINS = ['The writer’s own view', 'A view the writer only reports']
SORT_ITEMS = [
    ('The truth, I think, is that the plan came too late.', 0),
    ('Supporters rightly point out that the plan is popular.', 0),
    ('Admittedly, the plan has had its problems.', 0),
    ('Critics have long argued that the plan costs too much.', 1),
    ('It is often claimed that the plan will pay for itself.', 1),
    ('According to the council, the plan is on schedule.', 1),
]
