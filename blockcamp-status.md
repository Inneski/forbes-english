---
name: blocksavvy-unit-status
description: Where the sixteen Block Camp decks actually stand - what is live, what is fixed but unpublished, what is still open, and the two things that must never happen again. Read this before touching any blockcamp-*.html.
sources: cowork
---

# Block Camp — state of the line

## The short version

Sixteen decks (eight tenses x two parts), a hub (`block-camp.html`) and a
one-screen route map (`block-camp-map.html`) are **live**. A large corrective
pass is **done locally and NOT published**. Nothing goes up until Innes has
looked at the proof sheet.

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

## Fixed locally, not yet published

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

`claude/blockcamp-visual-checker.md` holds the four scripts in full. It renders
each slide, measures where the ink actually lands, builds a local-detail map of
the plate, and scores all six placements the deck can express. It independently
found every wrong-side slide Innes had found by eye: Present Simple 12,
Past Simple 2 / 8 / 17 / 18, Past Continuous 6 / 20.

## Still open

- **Content, not layout**: VERB (not BASE VERB) in yellow across all sixteen;
  the verb-colour check on Present Simple pages 3, 4 and 6.
- **Part 2 is not reachable from the map** - only Part 1a is linked.
- Four slides sit just under the placement threshold (x1.31-x1.36) and were
  left alone: Present Perfect 6, Past Continuous 6, Past Simple 2 p14,
  Present Perfect Continuous 2 p10.
- Nudges the six-slot model cannot express. Innes on Present Simple 14 ("move
  left onto the wall") and Present Continuous 9 ("move right") is asking for a
  shift WITHIN a side, to sit on flat wall rather than straddle a window. The
  deck has no horizontal-offset knob. Adding one is the next real capability.
- Backlog: `tools/lessons.json` and `seo.py` not refreshed for the sixteen;
  eight guides missing from `library.html`'s static SEO index; `docs/HANDOFF.md`
  carries superseded wording.

## Two rules that came out of this

1. **A rule written for one slide never goes in the shared shell.** It goes
   behind an opt-in that the slide or the deck asks for by name.
2. **Anything built in the sandbox that is not published is not saved.**
   The checker is in this project as text for exactly that reason.
