# Artwork: Credit Where It's Due (C1)

Eight pictures. The deck is built, measured and clean in all four languages;
this is the only thing it is waiting for.

**The spec has not changed, so it is not repeated here.** Geometry, palette,
safe areas, the upscale, and the `prep-artwork.py` warning to ignore are all
in [`ARTWORK-holding-the-line.md`](ARTWORK-holding-the-line.md), above its
slot table. The three that matter most, because last time they were the ones
that slipped:

1. **`--ar 7:6` for the seven framed plates**, `--ar 16:9` for the hero alone.
   Every candidate in the last batch came back 16:9 and had to be cropped
   here, which threw away about a third of each picture. A native 7:6 keeps
   it.
2. **Give each plate its own ground** — one step off the page cream
   (`#f3ede0`, a pale slate, a sage wall). Cream-on-cream makes the frame
   vanish; the interim plates in `CreditWhereDue/` do exactly that and you can
   see the effect.
3. **Upscale before dropping them in**, or they land under the 1400px minimum
   and `prep-artwork.py` skips them.

---

## The style stem

Same family as Holding the Line — these two decks are a pair and should look
like one. Every prompt below is `<subject>, <stem>`.

```text
flat editorial illustration, two-tone slate blue and pale blush on a warm cream ground, one brick-red accent, heavy grain and stipple texture, hard single light source, long soft shadow, no people, no faces, no text, no logos, no brand marks, generous negative space, centred subject, --ar 7:6 --style raw
```

**No text in any of them**, and this deck tempts it: three subjects are
documents. A generator writes gibberish where the words go, and a picture with
legible words behind a question is a step towards an answer key. Ruled lines,
blocks and marks — never letters.

---

## The eight slots

`build_creditdue.py` has an `ART` map at the top, and that is the only place a
filename appears.

| slot | where it appears | prompt subject |
|---|---|---|
| `hero` | the cover, full bleed | `a microphone on a stand at the end of a long dark table, one sheet of paper lying in front of it, the microphone on the right, wide empty floor to the left` — **`--ar 16:9`** |
| `room` | the cleft teaching card; the first question | `a single microphone on a tall stand, alone on a bare floor` |
| `trail` | the active/passive teaching card | `four dated paper slips pinned in a row along a wire, one pin brick red` |
| `tally` | both number screens | `a wall chart of tally marks counted in fives, some groups struck through` |
| `nameplate` | the first reclaim screen; the sentence-order round | `a blank engraved desk nameplate, face up, nothing written on it` |
| `folder` | the second reclaim screen; the email question | `a crisp card folder with three identical sheets fanned out of it` |
| `spotlight` | two questions | `an empty circle of light on a bare floor, the lamp just visible above` |
| `cups` | the activation stage | `two cups on a small table, one pushed forward towards the other` |

Variants per slot are welcome — `prep-artwork.py --dry-run` names the
near-duplicates and the building session picks one.

---

## When they land

Copy the batch out of `incoming/` into a folder of its own first (that folder
is shared with every other session), numbered so sorted order matches
`--names`:

```bash
py tools\prep-artwork.py <batch-folder> --into CreditWhereDue --width 1600 --names room,trail,tally,nameplate,folder,spotlight,cups
```

The hero goes in its own run without `--width`: 16:9 at 2000px is right for a
full-bleed cover and lands near 220 KB anyway.

Then:

1. **Not `extract-palette.py`.** This deck's colours are fixed. Run
   `py tools\check-editorial-palette.py` — every row must PASS.
2. Change the eight values in `ART` from `.svg` to `.jpg`.
3. `py lesson-template\build\build_creditdue.py`
4. `node lesson-template\check-lesson.js forbes-english-credit-where-its-due-c1.html`
   and `node lesson-template\checker\overflow-langs.js` on the same file —
   the second one is what measures the other three languages and both
   activation panels.
5. Catalogue row, `LibraryCards/forbes-english-credit-where-its-due-c1.jpg`
   (1200 × 512, cut from the hero), the `library.html` line,
   `py tools\build_hubs.py`, then `py tools\seo.py` last.

The interim plates and `lesson-template/build/plates_creditdue.py` go in the
bin in the same commit. Two sets of plates in one folder is how a lesson ends
up built twice.
