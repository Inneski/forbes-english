# Artwork brief: IELTS Reading — Yes, No, Not Given

Six pictures for `forbes-english-ielts-reading-ynng.html`, asked for on
2026-09-23 ("build yes/no/not given reading lesson next and explain if you
need artwork"). **The deck is built and passes every check on stand-in art.**
It goes live when these six land. Until then `build_ieltsynng.py` writes only
the gitignored preview `_forbes-english-ielts-reading-ynng.html`, on the
True/False/Not Given pictures, and never the live page.

## What the set has to match

This deck is the sibling of **True, False, Not Given**, and the two should
look like a pair. Its six pictures (`ielts-reading/`) are the style reference:
flat editorial illustration, two tones — **dusty slate blue and warm salmon
pink** — with near-black shadows, heavy grain and a distressed, printed
texture, a hard single light, plain interiors, one object per picture, **no
people**. A reading-room table under a hanging lamp; three towers of paper;
two doors, one opening onto darkness; an open book; a balance; a clock over
an empty desk.

**Tip:** give Midjourney the TFNG hero as a style reference —
`--sref https://forbesenglish.com/ielts-reading/hero.jpg` — which holds the
palette and the grain across a batch better than any words in the prompt.

## The style stem

Every prompt below is `<subject>, <stem>`:

```text
flat editorial illustration, two-tone palette of dusty slate blue and warm salmon pink, near-black shadows, heavy grain and distressed print texture, hard single light source, plain interior, no people, no hands, no text, no lettering, generous empty space, subject right of centre, --ar 16:9 --style raw
```

- **`no people, no hands`**: the pen, the glasses and the letter are all
  things a hand would hold, and that is the prompt that grows one.
- **`no text, no lettering`**: the notebook, the book and the letter invite
  writing. It would sit behind a Reading lesson looking like a passage.
- **`subject right of centre`**: every question slide puts the passage and
  the answers over the left two-thirds, and the teaching slides cover the
  lower two-thirds with cards. An object on the right or high up stays
  visible; one bottom-left disappears.
- **16:9, at least 1400px wide** (HOUSE-STYLE §3). A 2× upscale of a base
  render is plenty; `prep-artwork.py` brings it down to 2000px.

## The shopping list

One picture per section (HOUSE-STYLE §5c), each chosen for what its section
teaches. File names are the slot names; drop the set into
`incoming/ielts-reading-ynng/` under any names and say which is which.

| slot | where it appears | prompt subject |
|---|---|---|
| `hero` | the cover, and the library card | `a fountain pen lying uncapped across an open blank notebook on a wide desk, a single pendant lamp above` |
| `bg02` | slide 2 — *Same three answers, a different question* | `a pair of folded reading glasses resting on a closed hardback book` |
| `bg03` | slides 3–7 — *Whose voice is it?* and Activity 1 | `a row of four old microphones on stands across a bare stage, only one of them lit by a spotlight` |
| `bg04` | slides 8–12 — *Admittedly … but*, Activity 2 | `a weathervane on a rooftop, its arrow caught halfway through a turn, against a flat sky` |
| `bg05` | slides 13–18 — *How strongly does the writer mean it?*, Activity 3, the sort | `a table lamp glowing at half brightness beside a round dimmer switch turned halfway on the wall` |
| `bg06` | slide 20 — the activation stage | `a folded letter sealed with a wax seal, the brass seal stamp lying beside it on a desk` |

Notes on the list:

- **The hero is the writer**, the one person the whole question type asks
  about, shown by the one thing they leave behind. Blank pages: nothing on
  them is for reading.
- **`bg03` is the lesson in one picture**: many voices on the stage, one of
  them the writer's. If four microphones come back cluttered, three will do;
  one lit and the rest dark is the part that matters.
- **`bg04` must be mid-turn.** A weathervane pointing firmly one way is a
  different idea. The turn after *Admittedly* is the point of the section.
- **`bg05` is degree**: half on. A lamp fully lit or fully off loses it.
  Fallback if the switch will not render as a flat tone: `a lamp with a
  heavy fabric shade, glowing dimly, in a dark room`.
- **`bg06` is putting a view on record**, which is what the activation asks
  the learner to do. Keep the seal plain: no crest, no initials.

## Dropping the set in

In a local session, with the six files in `incoming/ielts-reading-ynng/`:

```bash
py tools/prep-artwork.py incoming/ielts-reading-ynng/ --into ielts-reading-ynng --dry-run
py tools/prep-artwork.py "incoming/ielts-reading-ynng/<six files, in slot order>" \
   --into ielts-reading-ynng --names hero,bg02,bg03,bg04,bg05,bg06
py lesson-template/extract-palette.py ielts-reading-ynng/hero.jpg   # every row must PASS
```

Paste the palette block into `PALETTE` in
`lesson-template/build/build_ieltsynng.py` (the `--hero` line takes
`ielts-reading-ynng/hero.jpg`), then:

```bash
py lesson-template/build/build_ieltsynng.py        # now writes the LIVE page
node lesson-template/check-lesson.js forbes-english-ielts-reading-ynng.html
node lesson-template/checker/answered-overflow.js forbes-english-ielts-reading-ynng.html en de es
```

Then look at every slide once, in all three languages: the checker cannot
tell a picture with lettering in it, or one whose subject sits under the
cards.

To publish, in this order:

1. A `lessons` row in Supabase **and** in `tools/lessons.json`:
   `forbes-english-ielts-reading-ynng.html`, title `IELTS Reading: Yes, No,
   Not Given`, level `C1`, `deck = true`, access `pro` like Matching
   Headings and Summary Completion (TFNG is the free one).
2. `library.html`: `"forbes-english-ielts-reading-ynng.html":
   "ielts-reading-ynng/hero.jpg"` in `LESSON_IMAGES` — run
   `node lesson-template/check-library.js --vs-origin` first.
3. `ielts-reading.html`: a fourth card after True, False, Not Given, and
   the count on `ielts.html` if it names one.
4. `py tools/build_hubs.py`, then `py tools/seo.py` last. Read the diff on
   `library.html`, `sitemap.xml`, `lesson-meta.json` and `llms.txt`.
5. `git add` the new files by name, `git commit -o` them with the indexes,
   push.
