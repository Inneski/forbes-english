# -*- coding: utf-8 -*-
"""Prepositions Double Lesson (B1) — the 27 scored items.

Lifted from the scrolling `b1_prepositions_double_lesson.html`, a four-section quiz
page with no teaching content at all: every rule lived only in the per-answer
feedback, which is the defect already recorded against the Lego and Twin Peaks
preposition decks in `docs/HANDOFF.md`. All 27 items survive unchanged in
substance and in count, so the deck scores exactly what the page scored.

**The options are rotated, and that is not cosmetic.** On the source page the
correct answer was written first in 15 of the 27 — and never written fourth at all. Engine shuffling
hides this at runtime, but `check-lesson.js` gates on the source order anyway,
and it is right to: the PDF export prints source order, so a printed hand-out
was an answer key with the column already filled in. Each item is now
left-rotated so the key lands at position `n % 4`, which preserves the option
set exactly and only moves where it sits.

Every `why` is a UI_I18N key rather than inline text — the deck ships English,
German and Spanish, and a key travels with the rest of the chrome instead of
leaving the explanation stuck in English. See HOUSE-STYLE.md §7 and §8.

One item was corrected rather than copied. `time` #2 read "We usually visit my
grandparents ______ the weekend" with the key `on`, and its explanation said
that "on the weekend" is British English. It is the American form; British
English is "at the weekend" — and `at` was sitting right there in the option
list, so a learner taught British English picked it, was marked wrong, and was
then told the inverse of the rule. The sentence now tests a named day, which
is the point the explanation was always claiming to make.

**Seven stems were rewritten because a distractor was also correct.** Innes
found three of them on the live deck; the other four came out of auditing the
rest for the same fault. This is the defect class to check for in any lesson
whose preposition is chosen by *meaning* rather than fixed by collocation —
place, time and movement. It does not reach the `dependent` section here, or
either B2 lesson, because a fixed pair admits no second answer by definition.

  `crack ______ the wall` → **a large map on the wall.** The worst of them: the
  key was `on`, but "a crack IN the wall" is the natural collocation, because a
  crack goes into the material rather than sitting on its face. The lesson was
  marking the right answer wrong. A map is unarguably on a surface.

  `sitting ______ strangers` → **lost among a crowd of strangers.** On a
  crowded train you can perfectly well sit *between* two strangers or
  *opposite* them; nothing forced the "three or more, no clear edges" reading
  the explanation depends on. "Lost among a crowd" forces it.

  `jogged ______ the river` → **jogged along the riverbank for three miles.**
  You can jog *across* a river — there are bridges. The riverbank plus a
  distance forces the following-the-length reading.

  `directly ______ the supermarket, so you cannot miss it` → **on the other
  side of the road.** `under` was live: cinemas sit under supermarkets in malls.

  `Please stay quiet ______ the presentation` → **Two people fell asleep.**
  "Stay quiet FOR the presentation" is ordinary English, and `for` was on the
  list. You cannot fall asleep "for" a presentation.

  `swim ______ the lake` → **to the far shore.** You can swim *along* a lake.

  `placed the tray ______ the table` → **lifted the tray.** Natural English is
  "placed it ON the table", and `on` was not offered — so the key `onto` was
  the least-bad answer to a question with no good one. "Lifted" needs the
  motion that `onto` carries.
"""


# ── PLACE ─────────────────────────────────────────────────────────────
PLACE = [
    dict(stem="The keys are ______ the drawer, under the old letters.",
         options=["in", "on", "at", "among"], correct=0, why="q1why"),
    dict(stem="There is a large map ______ the wall, just above the light switch.",
         options=["in", "on", "at", "between"], correct=1, why="q2why"),
    dict(stem="Meet me ______ the entrance to the stadium at six.",
         options=["in", "on", "at", "among"], correct=2, why="q3why"),
    dict(stem="The bank is ______ the bakery and the pharmacy.",
         options=["among", "opposite", "behind", "between"], correct=3, why="q4why"),
    dict(stem="She felt nervous, lost ______ a crowd of strangers at the station.",
         options=["among", "opposite", "behind", "between"], correct=0, why="q5why"),
    dict(stem="The cinema is directly ______ the supermarket, on the other side of the road.",
         options=["among", "opposite", "under", "between"], correct=1, why="q6why"),
    dict(stem="The cat is hiding ______ the sofa again.",
         options=["at", "onto", "behind", "between"], correct=2, why="q7why"),
]

# ── TIME ──────────────────────────────────────────────────────────────
TIME = [
    dict(stem="The meeting starts ______ 9 a.m. sharp, so don't be late.",
         options=["during", "in", "on", "at"], correct=3, why="q8why"),
    dict(stem="We usually visit my grandparents ______ Saturday mornings, when the traffic is light.",
         options=["on", "at", "for", "in"], correct=0, why="q9why"),
    dict(stem="The factory was closed ______ 1998, before the new owners took over.",
         options=["since", "in", "on", "at"], correct=1, why="q10why"),
    dict(stem="I have lived in this city ______ seven years now.",
         options=["during", "by", "for", "since"], correct=2, why="q11why"),
    dict(stem="He has felt much more confident ______ the promotion in March.",
         options=["during", "until", "for", "since"], correct=3, why="q12why"),
    dict(stem="Two people fell asleep ______ the presentation.",
         options=["during", "by", "for", "since"], correct=0, why="q13why"),
    dict(stem="You need to submit the report ______ Friday at the latest.",
         options=["until", "by", "during", "for"], correct=1, why="q14why"),
]

# ── MOVEMENT ──────────────────────────────────────────────────────────
MOVEMENT = [
    dict(stem="She walked straight ______ the office without knocking.",
         options=["across", "along", "into", "onto"], correct=2, why="q15why"),
    dict(stem="The waiter lifted the tray ______ the table carefully.",
         options=["through", "along", "into", "onto"], correct=3, why="q16why"),
    dict(stem="We drove ______ the tunnel and came out near the coast.",
         options=["through", "across", "into", "onto"], correct=0, why="q17why"),
    dict(stem="It took twenty minutes to swim ______ the lake to the far shore.",
         options=["along", "across", "onto", "through"], correct=1, why="q18why"),
    dict(stem="They jogged ______ the riverbank for three miles every morning.",
         options=["onto", "across", "along", "into"], correct=2, why="q19why"),
    dict(stem="He handed the documents ______ his manager before the deadline.",
         options=["into", "onto", "through", "to"], correct=3, why="q20why"),
]

# ── DEPENDENT ─────────────────────────────────────────────────────────
DEPENDENT = [
    dict(stem="I'm really looking forward ______ the concert next week.",
         options=["to", "for", "at", "about"], correct=0, why="q21why"),
    dict(stem="He apologised ______ being late to the interview.",
         options=["to", "for", "about", "of"], correct=1, why="q22why"),
    dict(stem="She's not very interested ______ politics.",
         options=["at", "for", "in", "on"], correct=2, why="q23why"),
    dict(stem="The results depend entirely ______ how much effort you put in.",
         options=["of", "for", "with", "on"], correct=3, why="q24why"),
    dict(stem="I'm worried ______ the exam results.",
         options=["about", "for", "of", "on"], correct=0, why="q25why"),
    dict(stem="The manager insisted ______ checking every figure herself.",
         options=["about", "on", "in", "for"], correct=1, why="q26why"),
    dict(stem="He's good ______ solving problems under pressure.",
         options=["on", "for", "at", "in"], correct=2, why="q27why"),
]

ALL = PLACE + TIME + MOVEMENT + DEPENDENT
assert len(ALL) == 27
