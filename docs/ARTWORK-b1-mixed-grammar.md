# Artwork brief: B1 Mixed Grammar Test, parts 1 and 2

The shopping list Innes asked for on 2026-09-23 ("house style 2 and ask for
shopping list images"). **Fourteen plates, seven per part. The heroes are
already on disk and stay.** Both decks are built and pass every check; they
ship when these land. `build_mixed_b1.py` writes an underscore preview until
every plate for a part exists, then writes the live page.

Read `ARTWORK-holding-the-line.md` for the general mechanics of an editorial
commission (the arch frame, the "middle 65%" rule, the `prep-artwork.py`
warnings to ignore). This brief only covers what is particular to these two.

---

## What the set has to match

The two heroes are the style reference. They are already flat editorial
vector art: a dusty slate-blue sky, coral and salmon clouds and ground, a pale
cream sun, grain, one lone silhouette. Part 1 is a low concrete building at
sunset. Part 2 is a roadside petrol station. **The set is an American desert
road at golden hour.** Every plate is one object from that world, chosen for
what its section tests.

| file | what it is |
|---|---|
| `MixedGrammarPart1/desert-building-sunset-clouds.jpg` | Part 1 hero, keep |
| `MixedGrammarPart2/desert-gas-station-sunset.jpg` | Part 2 hero, keep |

**Tip:** give Midjourney the hero of that part as a style reference
(`--sref <hero url>`). It holds the palette and the grain across a batch
better than any words in the prompt.

## The style stem

Every prompt below is `<subject>, <stem>`:

```text
flat editorial illustration, posterised into four flat tones, dusty slate blue and warm coral on a pale cream ground, one brick-red accent, heavy grain and halftone stipple, American desert roadside at golden hour, hard low sun, long soft shadow, no people, no faces, no hands, no text, no logos, no brand marks, generous negative space, centred subject, --ar 7:6 --style raw
```

- **`no people, no faces, no hands`**: the heroes have a silhouette each, but
  plates are objects. Several subjects below (the cot, the chairs, the
  suitcase) are things a person would be using, and that is the prompt that
  grows an arm in the corner.
- **`no text`**: the petrol pump, the signpost, the passport and the
  typewriter all invite lettering. Midjourney lettering is garbage and it
  would sit next to a grammar test.
- **`centred subject` with air above it**: every plate goes in the 190px
  arch, which cuts off the top corners.
- **`--ar 7:6`**, then **upscale 2×**. A base render is about 1232 × 1056,
  under the 1400px house minimum.

---

## The shopping list

### Part 1: the roadside building, into `MixedGrammarPart1/`

| slot | where it appears | prompt subject |
|---|---|---|
| `plate-mc-a` | Multiple choice 1–5 (*Listen! Someone is knocking at the door*) | `a closed wooden front door of a low desert house, a round brass door knocker, one wall lamp lit beside it` |
| `plate-mc-b` | Multiple choice 6–10 (*This bridge was built in 1889*) | `an old riveted iron truss bridge crossing a dry desert riverbed, seen from the bank` |
| `plate-story` | Elena's day, 3 slides (*she overslept because her alarm didn't ring*) | `a vintage twin-bell alarm clock on a bedside table, early light through a half-open blind, desert hills outside` |
| `plate-tf` | True or false, 6 slides, plus the results slide | `a wooden roadside signpost with two blank arrow boards pointing in opposite directions, open desert behind` |
| `plate-order` | Sentence building, 5 slides | `a vintage typewriter on a wooden desk with a blank sheet of paper in it, a desk lamp beside it` |
| `plate-fix` | Error correction, 3 slides | `an open red metal toolbox on a garage workbench, a spanner and a screwdriver laid out beside it` |
| `plate-act` | Activation (speaking in pairs) | `two folding chairs turned towards each other on a motel porch, a small table with two glasses between them, nobody in either` |

### Part 2: the petrol station, into `MixedGrammarPart2/`

| slot | where it appears | prompt subject |
|---|---|---|
| `plate-mc-a` | Multiple choice 1–5 (*Be quiet! The baby is sleeping*) | `a wooden baby's cot beside a window at dusk, a mobile of paper stars hanging still above it` |
| `plate-mc-b` | Multiple choice 6–10 (*The Mona Lisa was painted by Leonardo*) | `an empty wooden easel holding a blank canvas in a sunlit adobe room, a jar of brushes on a stool` |
| `plate-story` | Diego's trip, 3 slides (*while he was packing his suitcase*) | `an open half-packed suitcase on a motel bed, a folded map and a plain dark passport on top` |
| `plate-tf` | True or false, 6 slides, plus the results slide | `a straight desert highway splitting into two roads at a fork, seen from high above` |
| `plate-order` | Sentence building, 5 slides | `a small cairn of flat stones balanced one on another beside a desert road` |
| `plate-fix` | Error correction, 3 slides | `a car jack and a spare tyre leaning against an old petrol pump` |
| `plate-act` | Activation (speaking in pairs) | `two stools at an empty roadside diner counter, two coffee cups side by side` |

Notes on the list:

- **The two `plate-act` slots are doing a job.** The slide is a speaking task
  for pairs, and two seats with nobody in them says so without a word. Do
  not swap either for another still life.
- **`plate-mc-b` in Part 2 must stay blank.** A Mona Lisa that is nearly
  right is worse than none, and the question is about the passive, not the
  painting.
- **`plate-tf` in both parts is a choice between two directions.** That is
  the metaphor. If the fork will not resolve as a flat tone, the fallback is
  `two identical doors side by side in a whitewashed wall, one ajar`.
- **Nothing here needs a person or a place name.** Keep it that way on
  re-renders.

## Dropping the set in

```bash
py tools/prep-artwork.py incoming/ --into MixedGrammarPart1 --dry-run
py tools/prep-artwork.py "incoming/<seven files>" --into MixedGrammarPart1 \
   --names plate-mc-a,plate-mc-b,plate-story,plate-tf,plate-order,plate-fix,plate-act
# the same for MixedGrammarPart2
py lesson-template/build/build_mixed_b1.py          # writes the LIVE pages once all 7 exist
node lesson-template/check-lesson.js forbes-english-b1-mixed-grammar-test.html
node lesson-template/check-lesson.js forbes-english-b1-mixed-grammar-test-part2.html
```

`prep-artwork.py` will say `aspect 1.17, not 16:9` for every plate. **Ignore
it**: 7:6 is the frame's own shape under the editorial style.

Then look at every slide once. The checker cannot tell a plate with lettering
in it, or one that came back as a photograph. Set `deck = true` on both rows
in Supabase and `tools/lessons.json`, run `tools/build_hubs.py`, then
`tools/seo.py`, read the diff on the four index files, commit by name and
push.
