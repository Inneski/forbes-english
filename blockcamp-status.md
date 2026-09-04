---
name: blocksavvy-unit-status
description: Where the sixteen Block Camp decks actually stand - what is live, what is fixed but unpublished, what is still open, and the two things that must never happen again. Read this before touching any blockcamp-*.html.
sources: cowork
---

# Block Camp — state of the line

## The short version

**2026-09-04: a ninth camp.** `blockcamp-past-perfect.html` (9. Past Perfect —
Part 1) and `blockcamp-passive-past-perfect.html` (17. Past Perfect Passive)
are built, gated and in the `past-perfect-camp` bundle, not yet pushed. They
came from a NEW generator, `lesson-template/camp/build_camp.py` — the climb has
a builder again, chassis-based like the descent's — and the descent builder
learned `t-ppf`, per-station `tr` tables and a synthetic SEO row. Details in
`docs/HANDOFF.md`, 2026-09-04. "Sixteen decks" below is now eighteen.

Sixteen decks (eight tenses x two parts), a hub (`block-camp.html`) and a
one-screen route map (`block-camp-map.html`) are **live**. The large corrective
pass **shipped** in `fb2e25a` - this file used to say it was pending, and that
was stale. Verified: `data-equal` is opt-in (8 uses), the `min-width:200px`
answer-box floor is gone, `.sort-bins` is fixed-width.

## What was lost, and why it does not matter now

The deck generator (`lesson-template/build/bc_*.py`) lived only inside a
sandbox. Publishing goes through the GitHub web uploader, not `git push`, so
the scripts were never in the repo. The sandbox was recycled; they are gone.

The decks themselves survived, because they were published. **The published
HTML is now the source of truth for this line.** Do not rebuild a generator -
edit the deck files, and let the checker measure the result. That removes the
layer that caused the worst regression in the project's history (below).

## The regression that caused most of the complaints

Commit `109d47f` put an equal-box-width rule in the SHARED shell to satisfy
**one slide of Future Simple 1b**. Measured effect on Past Continuous page 6:
**599px wide with the rule, 411px without**. Every box in all sixteen decks
widened by ~188px, and the line was republished without re-checking. That one
edit is the source of "boxes too long", "text box too long", "make boxes
narrower" and "black boxes narrower" across four different decks - and of
Innes's *"We have DEFINITELY proof read these documents before and now we are
having to do them again."*

**The rule now has to be asked for**, per deck (`<div class="stage"
data-equal>`) or per slide (`<section class="slide" ... data-equal>`). Future
Simple 1 and 2 ask for it. Three other slides ask for it because they cannot
afford the height without it: Present Simple 8, Present Continuous 7,
Future Simple 8.

## Fixed and published in `fb2e25a`

| | |
|---|---|
| Equal-box regression | opt-in; Past Continuous 6 measured back to 411px |
| Answer boxes | `.opt` had `width:fit-content; min-width:200px` - each answer sized alone against a 200px floor, so four answers had four edges and the word "Do" sat in a 200px box. Now one grid column, sized by the longest answer, shared by all. Fixes Present Continuous 11 and 13. |
| Drop targets | `.sort-bins` ran the width of the line. Now a fixed 210px pair - big enough for the longest chip, not sized by the word WAS. |
| Example lists | `.exlist` was a wrapping flex row, so a card's intrinsic width was every example end to end and the card ran to the column edge however short its longest line. Now one example per row, so the card hugs what it holds. |
| Placement | 32 slides moved to the quieter side of their own artwork, by measurement. |
| Overflow | 0 slides paint outside the canvas across all sixteen. |

Proof sheet of all 173 changed slides, published beside current:
the `Block Camp Proof Sheet` artifact.

## The checker

`lesson-template/checker/` holds all seven scripts, in the repo - the project
doc is a transcription of them, not a design. The checker renders each slide,
measures where the ink actually lands, builds a local-detail map of the plate,
and scores all six placements the deck can express.

**It did NOT find every wrong-side slide Innes named, and this file used to say
it did.** It found Present Simple 12, Past Simple 2 / 8 / 17 / 18, Past
Continuous 6 / 20. It **missed Past Simple 7, 16 and 19**, which scored x1.12,
x1.02 and x1.11 - all under the x1.30 threshold - so `apply-placement` left them
and they sat exactly where he had objected to them. `check-placement` reported
**zero** placement findings on that deck, before and after. The tooling agreed
with itself while three of his instructions fell through the gap.

They are now pinned (7 -> right/top, 16 -> right/top, 19 -> right/bottom) and
applied. On 7 and 19 the measurement had actually picked the same side and was
merely too timid to act; on 16 it genuinely prefers left, and his call outranks
it - the detail map cannot see that the sunset road it likes is the subject of
the picture.

### `pins.json`: an absent entry means NEVER REVIEWED

Not "reviewed and clean". Five decks have no entry: `past-simple-2`,
`present-simple-2`, `present-continuous-2`, `future-simple-2` and - until now -
`past-simple`. **Do not let `apply-placement.py` run unsupervised on those.**

The rule that lost the three slides was: pin only where Innes OVERRULED the
measurement. That is the wrong rule, because it records the disagreement and
not the instruction. The rule now is: **pin every slide he names, whichever way
the measurement falls.**

## Still open

- **Content, not layout**: VERB (not BASE VERB) in yellow across all sixteen;
  the verb-colour check on Present Simple pages 3, 4 and 6.
- **Part 2 is not reachable from the map** - only Part 1a is linked.
- Four slides sit just under the placement threshold (x1.31-x1.36) and were
  left alone: Present Perfect 6, Past Continuous 6, Past Simple 2 p14,
  Present Perfect Continuous 2 p10.
- ~~Nudges the six-slot model cannot express~~ - **built and shipped.**
  `data-nudge="fine"` with `--nx` / `--ny` offsets, solved per slide by
  `solve-nudge.py` and written by `apply-pins.py`. Live on four decks, e.g.
  Present Simple 14 at -152px and Present Continuous 11 at +133px. This entry
  described it as "the next real capability" long after it existed.
- Backlog: `tools/lessons.json` and `seo.py` not refreshed for the sixteen;
  eight guides missing from `library.html`'s static SEO index; `docs/HANDOFF.md`
  carries superseded wording.

## Nobody has ever assessed whether these decks can be ANSWERED

Every pass over this line has measured **geometry**: where ink lands, box
widths, overflow, placement. Innes's own defect lists were layout too. The
checker scores pixels and has no notion of whether a question is answerable.

The cost surfaced on the live Past Simple deck, reported by Innes: gap slide 2,
"Choose a time signal", cannot be answered. Nothing in any sentence selects a
signal, the bank carries 4-5 chips against 3 gaps, and the hint says "Each is
used once", which is false. **The identical slide with the identical three
faults is in all sixteen decks - 48 unanswerable scored items.**
`blockcamp-past-simple.html` is fixed and is the worked example; see
`docs/HANDOFF.md`.

**Assume this is not the only one.** Answerability has never been in scope for
any deck in this line, so the time-signal slide is an unexamined defect rather
than a design decision - confirmed, not assumed.

## Two rules that came out of this

1. **A rule written for one slide never goes in the shared shell.** It goes
   behind an opt-in that the slide or the deck asks for by name.
2. **Anything built in the sandbox that is not published is not saved.**
   The checker is in this project as text for exactly that reason.
