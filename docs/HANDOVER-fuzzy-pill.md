# Handover — "SUBJECT + am/are/is is fuzzy" on Present Simple slide 4

**Status: unresolved.** One fix shipped on a strong hypothesis (`efca4c2`), not
confirmed. Innes still saw the problem before that fix went out; nobody has
checked since.

Read `CLAUDE.md` first — the pipeline and the publishing rules there still apply.

## The symptom

<https://forbesenglish.com/blockcamp-present-simple>, slide 4 ("Adverbs of
frequency"). The **second** formula pill —
`SUBJECT + am / are / is + ADVERB OF FREQUENCY` — reads fuzzy and washed out.
The first pill on the same slide (`SUBJECT + ADVERB OF FREQUENCY + VERB`)
looks fine to him. In his screenshot the second pill's plain text is mid-grey
and soft; `ADVERB OF FREQUENCY` next to it is crisp blue.

He has reported this repeatedly. It is **not** the "faint" problem — that was a
contrast issue, fixed in `168a3fe`, and he used a different word for it. He
described this one as *fuzzy*.

## Ruled out, with the evidence

Do not re-run these unless you have a reason to distrust them.

1. **Not contrast.** Computed values at his window size are correct:
   pill text `#CED4DD`, `.t-ps` aux `#A8B8CD`, background 0.84 alpha. The
   `168a3fe` lift is applied and measurable.
2. **Not the stage transform.** `fitStage()` scales the stage — 1.333× at
   1920 wide. Same pill captured at stage scale 1.0 / 1.5 / 2.0, each
   normalised back to CSS pixels, gives edge-steepness p99 of **100 / 96 / 96**.
   No meaningful softening from scaling.
3. **Not Windows display scaling.** Rendered at `deviceScaleFactor` 1, 1.25
   and 1.5 — crisp at all three.
4. **Not a stale page.** *Innes worked this out, not me.* His page was showing
   the extra languages pushed an hour earlier, so it could not be an old copy.
   I had claimed cache; I was wrong.
5. **Not `backdrop-filter` compositing.** Removing it from `.formula` and from
   the `.freq` card moved edge p99 from 97 to 100 — inside noise. Both changes
   were reverted rather than kept.

## The live hypothesis — `color-mix()` is not supported in his browser

This deck declares **every plate as a bare `color-mix()`** — 77 of them. A
browser that does not understand the function drops the whole declaration, so
the plate is never painted and the artwork shows straight through the text.

Reproduced by stripping `color-mix` declarations at runtime: the pill then
computes to `background: rgba(0, 0, 0, 0)` with text `#A3AEBF`. That is dim
grey type sitting directly on a bright dawn sky — which is exactly what his
screenshot looks like, including the "washed" quality of the whole card.

`color-mix()` needs **Chrome 111** (March 2023).

### What shipped

`efca4c2` — 42 declarations on `blockcamp-present-simple.html` now carry a
solid fallback *before* the `color-mix`, using theme primitives only (no
hardcoded rgba, per CLAUDE.md):

```css
background: var(--surface2);
background: color-mix(in srgb, var(--surface2) 84%, transparent);
```

Where `color-mix` works, nothing changes — verified, the pill still computes
0.84 alpha with identical text and aux colours. Where it does not, the plate is
solid instead of absent.

**Only present-simple was done.** The other 23 decks still have bare
`color-mix` throughout. If this hypothesis is confirmed, sweep them.

## The next step, and it is one question

Ask Innes for the first line of `chrome://version`.

- **Chrome ≥ 111** → the hypothesis is dead. Do not sweep the other decks.
  Go to "If it is not color-mix" below.
- **Chrome < 111** → confirmed. Sweep the remaining 23 decks with the same
  regex pass, and consider whether `lesson-template/` should stop emitting
  bare `color-mix` at all.

Also worth having: his screen resolution and whether the browser window is
maximised, and a screenshot taken *after* `efca4c2` reached the live site.

## If it is not color-mix

Two things never explained:

- **Why pill 2 looks different from pill 1** to him when both are `.formula`
  with the same computed style. The only structural difference is that pill 2
  wraps to a second line. Worth testing a forced non-wrapping pill 2.
- The offered-but-not-applied blunt fix: raise `.formula` from **14.5px to
  16.5px** and make the plate fully opaque. It is the smallest ink on the
  slide by some margin, and slide 4 has room — all ten languages clear the
  deck bar with 4px+ to spare after the spacing fix in `1f072ae`. This would
  very likely make the complaint go away without ever identifying the cause,
  which is worth doing if the diagnosis stalls.

## How to reproduce the investigation

```bash
export NODE_PATH=/opt/node22/lib/node_modules
# render slide 4 at his window size (NOT 1280 — the stage is unscaled there,
# which is why three passes at this bug missed it)
node lesson-template/checker/shots.js blockcamp-present-simple.html 4 /tmp/out
```

Render at **1920×960**, not 1280×720. Every render I made while chasing "faint"
was 1280 wide, where `fitStage()`'s scale is exactly 1.0.

## Unrelated things found while chasing this — do not lose them

- **German and Spanish overflow present-simple slide 7 by 22px.** Pre-existing,
  untouched, nothing to do with this bug.
- **The cross-language overflow checker is unreliable.** It did not flag de/es
  on slide 4 even though direct measurement put both at +10px, then later did
  flag them on slide 7. Cause unknown. Treat a clean run as suggestive; measure
  a specific slide directly when it matters. The script is in the scratch dir,
  not committed — rewrite it if you need it.

## What else is open on Block Camp

See `docs/HANDOFF.md` — in particular the 643 always-on `.sup` glosses and
1,735 `BW_TR` word-bank entries per language that are still English-only, and
the fact that the gloss CSS is hardcoded to `es`/`de`.
