# Artwork brief: Reddit × French Market — Getting in the Door (C1)

> **DONE 2026-09-30.** Innes rendered all six the same afternoon (nine
> files, two variants each of the door, the telephone and the chairs);
> they are `RedditFrench/plate-*.jpg` and the deck is live. Kept for the
> record and as the pattern for the next brief. The sources are in
> `incoming/_previous/forbes-reddit-french-door-c1/`.

Innes, 2026-09-30: *"Make a new one that would fit with the others and ask
for artwork etc, house style 2"*. **Six plates, one per slot.** The deck is
built and passes every gate against placeholders;
`build_redditdoor.py` writes the gitignored preview
`_forbes-reddit-french-door-c1.html` until all six files below exist in
`RedditFrench/`, then writes the live `forbes-reddit-french-door-c1.html`.
The builder also creates the drop folder `incoming/reddit-door/` whenever
it runs in preview mode, so the path this brief names always exists.

Two renders were attached to the request from the phone. **They did not
reach this machine**: a picture attached through Remote Control is not
written to the local transcript, so they could not be recovered the way a
desktop attachment can. The drop folder is what worked.

## Format: house style 2, the panel

Every plate is used twice, so it has to survive both crops:

1. **Full bleed** on its part divider: the whole 16:9 frame.
2. **Panel**: a 548×720 slice (aspect 0.76, portrait) out of the same file,
   chosen by `pos=` in the builder, at full opacity beside the text column.

So: **`--ar 16:9`, upscaled to at least 2400 px wide**, and **the one
subject inside a vertical band about a third of the frame wide**, with flat
ground either side. The slot table says which third; the builder's `pos=`
is already set to it. A wide composition with the idea spread across the
frame will not survive the panel.

## What the set matches

The family already has three site pictures, and they are the style
reference: `RedditFrench/cafe-hero.jpg` (the Paris café, cream walls, black
silhouettes, red stools and signage), `RedditFrench/office-silhouette-desk.jpg`
(a man's silhouette against a coral panel, slate-blue desk) and
`dnd-rpg/parisian-office-scene.jpg` (slate-blue office, salmon windows). All
three are flat editorial vector with light grain: cream, coral, slate blue,
solid black silhouettes. Give Midjourney `office-silhouette-desk.jpg` as
`--sref`; it holds the palette best. The café and the desk stay on disk as
placeholders and are not used by the finished deck.

## The style stem

Every prompt is `<subject>, <stem>`:

```text
flat editorial vector illustration in the style of Noma Bar, one idea in negative space, cream and warm salmon with slate blue and solid black silhouettes, light grain, Paris, business, calm, no text, no letters, no logos, no signage, no faces, subject contained in the <THIRD> of the frame with empty flat ground either side --ar 16:9 --style raw --sref <url of RedditFrench/office-silhouette-desk.jpg>
```

- **`no text, no signage`**: emails, phones and subject lines invite
  lettering. Midjourney lettering is garbage; ruled lines and blocks stand
  in for words.
- **`no faces`**: silhouettes are the family's idiom. The café hero has
  faces and it is the weakest thing in it.
- Replace `<THIRD>` with the slot's third.

## The shopping list — into `RedditFrench/`

| slot | where it appears | third / `pos=` | prompt subject |
|---|---|---|---|
| `plate-cover` | cover (washed under the title) and the default wash behind card and question slides | centre, calm in the middle | `a tall Haussmann double door on a Paris street, one leaf open a hand's width, warm light in the gap, the street empty` |
| `plate-door` | Part 1 divider + panel (the cold email: hook, credibility, soft ask) | left third / `20% 50%` | `a single envelope sliding under a closed door, seen from inside, a strip of daylight beneath the door` |
| `plate-gate` | Part 2 divider + panel (the gatekeeper call) | right third / `80% 50%` | `a desk telephone with a long coiled cord running to an inner door that stands ajar, an empty chair beside it` |
| `plate-room` | Part 3 divider + panel (the first meeting, French style) | centre / `50% 50%` | `a long boardroom table set for lunch at one end, two glasses of red wine, a folded document at the other end` |
| `plate-follow` | Part 4 divider + panel (the follow-up) | left-of-centre / `30% 50%` | `a wall calendar with one date circled in red, a paper aeroplane resting on the desk below it` |
| `plate-act` | activation stage background | centre, calm | `two café chairs facing each other at a small round table on a Paris pavement, two cups, nobody in either` |

Notes:

- **`plate-cover` is the lesson's idea** — the door, and it is not shut. If
  the Haussmann door will not resolve flat, the fallback is
  `a brass door handle in close-up with a hand's-width gap of light beside it`.
- **`plate-act` is a pair-speaking slide**, so two empty seats, as in every
  activation brief in this family. Do not swap it for a still life.
- **The café hero is the wrong cover for this deck**: it has faces, lettering
  and no single subject, and it belongs to the first lesson. It is a
  placeholder here only.

## Dropping the set in

```bash
py tools/prep-artwork.py incoming/reddit-door --into RedditFrench --dry-run
py tools/prep-artwork.py "incoming/reddit-door/<six files>" --into RedditFrench \
   --names plate-cover,plate-door,plate-gate,plate-room,plate-follow,plate-act
py lesson-template/extract-palette.py RedditFrench/plate-cover.jpg   # paste over PALETTE in the builder
py lesson-template/build/build_redditdoor.py      # writes the LIVE page once all 6 exist
py tools/build_hubs.py
py tools/seo.py                                   # restores the SEO block; read its diff
node lesson-template/check-lesson.js forbes-reddit-french-door-c1.html
node lesson-template/checker/answered-overflow.js forbes-reddit-french-door-c1.html en de es
```

Then look at every divider and panel once and tune `pos=` by eye: the
checker cannot see a subject cut in half. Add the row to `library.html`'s
`LESSON_IMAGES` (`"forbes-reddit-french-door-c1.html": "RedditFrench/plate-cover.jpg"`),
the `OVERRIDES` line in `tools/topics.py` (`['business-english']`, the title
names no grammar), and the catalogue row (SQL in HANDOFF).
