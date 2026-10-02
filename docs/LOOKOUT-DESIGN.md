<!-- Generated 2026-10-02 by a design workflow (4 concepts: Raise the Lookout 22.5,
Beacon Peak 21.5, Lookout Town 17, the Flagship airship 14.5; judged on fun,
art feasibility and fit), for Innes: "think of a way to make this more fun like
you are building or trying to reach something". Not built yet. The art brief is
docs/ARTWORK-lookout.md; the code-drawn mockup lives in the session scratchpad. -->

# Raise the Lookout: final design

**In one line.** The 9 climb flags raise your lookout tower one storey per tense. The 9 descent flags light a lamp on each storey and feed the beacon on the roof. At 18/18 the beacon fires.

The goal already exists in the world: the Quest's Passport says *"Clear the lot and the lookout tower is yours"* (quest template line 312), and the tower stands on `BlockCamp/hub-hero.jpg`, at the end of the village walk and in climb-map scene 09. This design keeps that promise one flag at a time.

---

## 1. What changed from the shortlisted concept

Every flaw the three judges raised has a fix:

| Flaw (judge) | Fix in this design |
|---|---|
| Storeys 2–6 were five identical trestle bays, so the middle of the climb went flat (fun) | Each storey carries its own object, taken from its camp's climb-map scene (scenes 01–09), painted into the master. No two storeys look alike. |
| Gold on a climb flag was two near-invisible caps (fun) | A gold flag brings that storey's object to life at once (nine different effects, §4). **Trim tiers** at 3 / 9 / 18 golds turn every ring-beam cap iron, then brass, then gold (from WILD). A near-miss "4% to gold" line on Results and a "Closest to gold" chip (from REACH). |
| Descent banners were small decoration, and the beacon was held back until the end (fun) | The descent hangs **lamps**: light reads at phone size where a 20×40px banner does not. Each lamp makes the beacon flame one step bigger, so the passive half builds visibly toward the finale. The scene's dusk deepens a notch per lamp so the lamps glow. This is REACH's light reveal turned round: a free learner never sees a dark mountain. |
| The "Halfway up" toast at storey 4 was false (fun) | Milestones use true counts. 9/18 is "Halfway"; storey 4 says "Four storeys up". |
| Out-of-order states were fiddly, and the HUD had five counters (fun) | No crates. An early lamp hangs lit on its ghost storey, and a storey built early stands on the ghost of the storeys below. The HUD shows Lookout k/18, Gold and Stars only. Adventures sit on the bunting sign. |
| The build-in played one tap away from the Results slide (fun) | The Results card shows the tower with the new piece building in: a pixel meter in Phase A, a window onto your painted tower in Phase B. It also shows a caption in the deck's own tense (from WORLD). |
| Nine countable levels was the hardest image ask (art, fit) | The nine levels hold different objects, so they can be counted and checked by eye. The posts are vertical. Rods, sockets and flags are dropped from the ask because code draws them. The Phase A code tower ships first and is the fallback, so a failed art round costs nothing. |
| The summit brief contradicted its own scale (art) | The summit is portrait 1024×1536, the same as the tower. The pad is 45% of the plate's width, with its front edge 88% of the way down. The builder scales the tower to the measured pad and refuses a tower whose top sits less than 6% of the plate height below the plate's top edge. |
| Tower and summit came from separate generations and would disagree at the base (art) | The summit is made in the same ChatGPT chat with the chosen tower attached: same camera height, low sun from the right. A **foreground lip**, cut from the summit's own pixels, is drawn over the tower foot. A code contact shadow is added. |
| 14 trophies were illegible on a phone (art), and Phase C was scope creep (fit) | The trophies and their sheet are cut. Adventures become 14 code pennants on a bunting line with one tap target. Phase C shrinks to an optional beam on the climb map and village, plus a postcard. |
| The hub beam is invisible on phones, and the Quest sky drifts (art) | No hub beam on phones. On desktop it is drawn only when the computed cover crop contains the tower. No beam on the Quest. |
| ChatGPT alpha is not clean (fit, art) | The builder sets alpha below 16 to 0 and above 240 to 255, erodes 1px and decontaminates the edges, and only then applies the tiling gate. There is a green-screen fallback. |
| The tall 9-storey tower is not the short painted one (fit) | It uses the same design language (spruce X-braced legs, railed cabin, stepped green roof), drawn close up and taller. The link between them is the beam on the painted tower at 18/18. This is open question 2. |
| Lookout Keeper semantics (fit) | The rank is unchanged (everything cleared, score-blind). The Lookout is score-based. The Passport line keeps its promise and its "Your flags" button becomes "Your Lookout". |

---

## 2. The loop

1. **Play a deck.** On its Results slide, the flag card that `camp-end.js` already injects gains the tower beside the flag, with the new piece building in. It also gains one sentence in the deck's tense, e.g. *"You STACKED the logs this morning. PAST SIMPLE · STACKED"*, and one translated progress line: *"Storey 3 raised · Lookout 3/18"*, *"6% to go: 50% raises storey 4"* or *"4% to gold"*.
2. **"See it built →"** opens Your Lookout (`block-camp/flags.html#lookout`). Each piece earned since the last visit builds itself in, one after another.
3. **The Next chip** names one deck and one score, e.g. *"Next: Camp 5 · Going To Part 1 · 50% raises storey 5"* (with a padlock on Pro). A second chip shows *"Closest to gold: Camp 3 · 71% → 75%"*.
4. Tap the chip, play the deck, come back.

The **Next order** is: the lowest unbuilt storey; then the lowest unlit lamp; then a missing star; then an unfinished adventure. The Closest-to-gold chip is separate and always present while any planted piece is below 75%.

---

## 3. What feeds it

Everything is computed from data that already exists: the `'flags'` key in CampSave (through `CampFlags.state` and `summary`), `s.rpg` (the Quest's own `advState`) and `s.name`. **No save-format change and no new CampSave key.** The only new storage is one per-device localStorage marker, `'forbes-camp-lookout-seen'`, on the pattern of flags.html's `'forbes-camp-flags-seen'`. It decides what to animate.

| Source | Count | Becomes |
|---|---|---|
| **Planted**, climb (Part 1 ≥ 50%) | 9 | Storey N is raised: its painted pixels are revealed, and flag N (the existing `CampFlags.sprite`) is planted on the storey's right corner. |
| **Planted**, descent (station ≥ 50%) | 9 | A lamp in that station's TABLE colour hangs on the left corner of storey S−8, with a light pool. Station 9 goes on storey 1, … station 15 on storey 7. The Trial (16, gold) goes on storey 8, because camp 8 has no passive station. Station 17 hangs under the roof eave of storey 9. Each lamp is +1 step on the beacon flame and +0.04 on the dusk layer. |
| **Gold** (≥ 75%) | 18 | **Climb:** that storey's object comes to life (§4). **Descent:** the lamp gets a gold frame (outlined in INK; see the contrast check) and a 1.3× pool. **Running count:** the trim goes oak (0–2), iron (3–8), brass (9–17), then gold at 18, the **Golden Lookout**. The climb flag's existing gold finial and base cap still show. |
| **Star** (Part 2 ≥ 50%, camps 1–8) | 8 | A star on that storey's flag (the existing 7×6 sprite star) and one lit star of the constellation **The Summit Flag**: 8 pixel stars in the twilight sky, 3 for the pole and 5 for the pennant. At 8/8 lines join them. A Part 2 passed before its Part 1 shows a dim gold "waiting" star (the existing `starSaved`). |
| **Adventures** (every part in `s.rpg` cleared) | 14 | One pennant on the summit bunting, a line from the roof eave to a post at the summit's edge. Each pennant is in its adventure's camp colour from the Quest's mapping, and gold where there is no camp. A master ending (`parts.every(p => p.master)`) gives a gold-tipped pennant. Adventures never count toward the 18. |

The rules inherited from `camp-flags.js` still hold: **latched** (nothing ever comes down) and **order-free**.

---

## 4. The nine storeys

Each object comes from the matching scene on the climb map, `block-camp-map.html` (01 tents, 02 tent being pitched, 03 old fire pit, 04 campfire burning, 05 signpost and map, 06 sunset with the tower ahead, 07 summit cairn and boots, 08 night tent with lantern, 09 view from the tower). Colours are the hub's CAMP and INK. The captions are drafts and must pass the house tense check before shipping (see the memories "Stative is not the test" and "Grammar tokens in CAPS"). They stay in English on purpose, because they are the English being practised. The FORM line is the tense name plus the verb group in CAPS.

| # | Tense · colour | Painted object | Gold effect (code, at measured anchors) | Caption when raised | Lamp: station · caption when lit |
|---|---|---|---|---|---|
| 1 | Present Simple · #7A93B5 | Cobblestone footings, arched door, cream canvas awning, iron lantern | The lantern lights: a warm pool and a 2-frame flicker | The lantern LIGHTS the door every evening. | St 9 · The lamps ARE LIT every evening. |
| 2 | Present Continuous · #E66085 | Rope-and-pulley hoist lifting a canvas bundle | The pulley wheel turns gold (2-frame turn) | The hoist IS LIFTING the canvas. | St 10 · Storey 2's lamp IS BEING LIT. |
| 3 | Past Simple · #B08968 | Stacked logs and an empty iron fire basket | The basket catches: a 3-frame pixel flame | You STACKED the logs this morning. | St 11 · Storey 3's lamp WAS LIT at sunset. |
| 4 | Past Continuous · #F1D779 | Small stone hearth with a chimney pipe | The hearth mouth glows and 3 smoke puffs rise (cloud colour sampled from the plate) | The fire WAS BURNING when you finished the hearth. | St 12 · Storey 4's lamp WAS BEING LIT when the wind dropped. |
| 5 | Going To · #70A43A | Signpost with two arrows pointing up, a rolled map on a crate | A small lamp on the post lights | Look at the sign: you ARE GOING TO REACH the top! | St 13 · Look at the lamps: the beacon IS GOING TO BE LIT! |
| 6 | Future Simple · #F0723F | Brass telescope on a tripod | A glint at the lens every 6 s | One day you WILL SEE the far side from here. | St 14 · The beacon WILL BE SEEN from the valley. |
| 7 | Present Perfect · #2E7D65 | Wrap-around deck and railing, a small cairn and a pair of boots | A gold capstone on the cairn | You HAVE BUILT the deck. | St 15 · Storey 7's lamp HAS BEEN LIT. |
| 8 | Present Perfect Continuous · #46B0AB | Cabin with glass windows and a hanging lantern | The windows glow warm, as the village already lights the hub tower's windows | You HAVE BEEN BUILDING since breakfast. | St 16, The Trial (gold #e8c04a) · The Trial HAS BEEN PASSED: the gold lamp is yours. |
| 9 | Past Perfect · #d66d77 | Stepped green roof with a stone beacon cradle | The cradle stones turn gold | The sun HAD SET by the time the roof went on. | St 17 · The roof lamp HAD BEEN HUNG before dark. |

Every effect starts subtle (house memory "Effects start subtle"). Each newly gilded storey also gets one faint light sweep on the visit when it arrives. Under `prefers-reduced-motion` every effect freezes on its first frame.

---

## 5. Stages: flag count → what appears

This is the in-order path (climb first, then descent). Any other order uses the order-free rules below the table.

| Flags | What appears | Toast |
|---|---|---|
| **0** | The summit at golden hour. The whole Lookout stands as a **blueprint ghost**: the same pixels, washed toward the sky colour, with edge lines. A cold ghost cradle on top. Eight dim star outlines. An empty bunting line. A plaque reading YOUR LOOKOUT · 0/18. Next chip: *"Camp 1 Part 1 (free): 50% lays the footings"*. | none |
| 1 | Storey 1 builds in. Flag 1 is planted on its right corner, number tag 1 takes the camp colour, and the plaque takes the learner's save name if there is one. | Your Lookout has begun |
| 2–3 | The hoist storey, then the woodpile storey. | none |
| 4 | The hearth storey. This is everything a free learner can raise. The Next chip now shows Camp 5 with a padlock, and the Closest-to-gold chip keeps a free target. | Four storeys up |
| 5–8 | The signpost, the telescope, the deck, the cabin. | none |
| **9** | The roof and cradle go on. The door becomes a **"Climb to the top"** button that opens `BlockCampDescent/watchtower-far-side.jpg` with *"Now come down the far side →"* linking to the descent map. | THE LOOKOUT STANDS · Halfway: 9/18 |
| 10 | Lamp 1 (Station 9, slate) on storey 1. Beacon flame step 1 (embers). Dusk 0.04. | Lamp 1 lit |
| 11–17 | Lamps 2–8; lamp 8 is the Trial's gold. The flame grows at 4 lamps (small flame) and at 7 (big flame). The dusk deepens to 0.32 and the tower becomes a column of coloured light. | Lamp n lit |
| **18** | Lamp 9 hangs under the eave and the **BEACON IS LIT** (§7). | Every lamp is lit · BEACON LIT |
| Gold 3 / 9 / 18 | Every built storey's ring-beam caps, the plaque frame and the roof finial turn iron, then brass, then gold. At 18 the beam gains a solid gold core and the plaque turns gold: the **Golden Lookout**. | Iron trim · Brass trim · GOLDEN LOOKOUT |
| Stars 8 | Lines join the 8 stars and **The Summit Flag** constellation twinkles. | The Summit Flag |
| Adventures 14 | The bunting is full. | A full summit |

**Order-free rules (no crates, no special states):**
- A storey raised early stands solid on the ghost of the storeys below it. The ghost reads as the blueprint it is.
- A lamp lit early hangs lit on its ghost storey.
- The beacon flame grows with lamps whether or not the roof stands, burning on the ghost cradle if needed.
- The beam needs all 9 storeys and all 9 lamps.

**Free path today** (camps 1–4 Part 1 are free, per `lesson-meta.json`): 4 storeys, 4 gold effects and the iron trim at 3 golds. That is a real, finished-looking first stage. How the padlocked Next chip reads is open question 1.

---

## 6. Reward moments, surface by surface

**The Results slide**, `block-camp/camp-end.js`. Every deck already loads it, so no deck file changes.
- **Phase A.** The art slot holds the flag (64px; 48px on `html.bc-phone`) and the pixel meter beside it. The meter is the same 21×52-cell code tower at 2px per cell (42×104). On `html.bc-phone` it is clipped to a 40-row window scrolled to the new piece. The new piece flashes in `steps(6)`.
- **Phase B.** The meter is replaced by a 104×104 window (80×80 on phones) onto the painted Lookout, centred on the piece, which builds in. It uses `lookout-sm.webp` and `summit-sm.webp`, about 50 KB together, loaded only when Results becomes active. If anything fails to load, the card falls back to the meter, and from there to today's card.
- **Text.** Lines are the translated title (*"Storey 4 raised!"*, *"Lamp 2 lit!"*, *"Storey 3 is gold!"*, *"The Lookout stands!"*, *"Beacon lit!"*) and, on a win only, the English caption with its FORM line. Then comes the translated progress line: near miss (*"6% to go: 50% raises storey 4"*, *"…lights lamp 4"*), *"4% to gold"*, or *"Lookout 7/18"*. The link becomes *"See it built →"*.
- **Languages.** New chrome strings go in all ten of the card's languages (en, de, es, fr, it, pt, ru, ar, zh, ja). The house minimum is EN, DE and ES.
- **Cache.** `camp-end.js` bumps its own `camp-flags.js?v=1` to `?v=2`, because the decks request `camp-end.js?v=2` and cannot be re-tagged now.

**Your Lookout**, `block-camp/flags.html`. Same URL, so every "Your flags" link still works.
- **Stage.** On a phone the stage is the portrait plate. A 2:3 plate fits a 375px-wide stage of about 560px almost exactly, and taller screens use a cover crop of at most 15% at the sides. A compact HUD bar sits under it.
- **Desktop.** The stage is a column of `min(88vh, 1000px)`, with the HUD on its left as on the Quest.
- **HUD.** LOOKOUT k/18 · Gold k/18 · Stars k/8, plus the Next chip and the Closest-to-gold chip.
- **Tapping.** Tapping a storey (a 44px target) opens a bottom sheet in the style of the climb map's stop sheet: tense, the storey's flag and lamp, best scores, Part 1 / Part 2 / station links (padlock on Pro, read from the catalogue through the hub builder's `access()`), and what the next upgrade needs. Tapping the bunting sign opens the adventure list.
- **Below the stage**, the existing 18 tiles stay as "The parts list", relabelled "Storey 3 · Past Simple" and "Lamp 3 · Past Simple Passive".
- **Build-in.** Pieces new since `'forbes-camp-lookout-seen'` build in on arrival, in order. Each storey fills from the bottom up in 6 block-row steps over 0.9s, with dust in colours sampled from that storey. Its flag then drops with the existing `cf-drop`, and its caption shows. A lamp swings in and its pool fades up over 0.6s. More than 3 new pieces play as a quick montage at 0.3s each. Under reduced motion each piece appears with a static NEW tag.

**The route maps**: `CampFlags.decorateMap`, which both maps already load, so no map file changes. The chip becomes *"Flags 4/9 · Lookout 7/18 →"*.

**The hub**, via the hub builder. The "Your flags" entry becomes "Your Lookout" with the meter at 2px per cell. This needs `camp-save.js` and `camp-flags.js` loaded on the hub, which they are not today.

**The Quest**, via the quest builder. The HUD gets a "Lookout k/18" stat linking to the page. The Passport line's "Your flags →" button becomes "Your Lookout →" with the sub-line *"Light its beacon"*. The Lookout Keeper rank and its toast are untouched.

**The village**: Phase C, optional. The tower stop ("THE LOOKOUT · the far side") reports "Your Lookout 12/18" and links to the page. Once the beacon is lit, the canvas draws the beam at the tower apex in SCENE coordinates, next to the window glow it already draws at (1131, 441).

---

## 7. The finale: BEACON LIT (18/18)

1. The view eases to the whole tower.
2. The Quest's two-frame hiker (`FRAMES`), tagged with the save name, climbs the storey anchors to the roof, about 2.5s in all.
3. The beam rises in 6 steps from the cradle to the top of the stage, as nine 3px stripes in CAMP 1→9 with a gentle pulse. At 18 golds it gains a solid gold core.
4. The Quest's `fireworks()` fire, and the plaque becomes **<NAME>'S LOOKOUT · 18/18**.

From then on the beam stays lit on the page, the Results meter and the hub button. Phase C adds it to the climb-map hero (its `.canvas` already maps image pixels to stage percentages) and to the village, plus a "Save a postcard" button: `canvas.toBlob`, a 1024×1536 PNG saved on the learner's own device.

Under reduced motion the finale shows its final frame at once.

---

## 8. What is painted, what is code

| Item | Made by |
|---|---|
| `lookout.png`: the finished tower with its nine objects, transparent, frozen once traced | **ChatGPT** (1 image) |
| `summit.png`: the empty summit pad at golden hour, portrait, made in the same chat with the tower attached | **ChatGPT** (1 image) |
| The 18 flags | **Existing**: `CampFlags.sprite`, unchanged, at 32px (2px per cell) |
| The hiker, `toast()`, `fireworks()` | **Existing**: the Quest template |
| The view from the top | **Existing**: `BlockCampDescent/watchtower-far-side.jpg` |
| The painted tower for the Phase C beam | **Existing**: `BlockCamp/hub-hero.jpg` |
| Blueprint ghost (`lookout-ghost.webp`), from the master's own pixels | Code (builder) |
| Storey bands, anchors, lip polygon, sampled colours (`storeys.json`) | Code (builder, then a proof check) |
| Lamps (a 3×4-cell lantern plus a 2px iron hook) and their light pools | Code |
| The nine gold effects, trim caps, number tags (Monocraft), plaque | Code |
| Beacon flame steps, beam, dusk layer, constellation, bunting and pennants | Code |
| Contact shadow (in the plate's darkest ground tone) | Code |
| Phase A code tower and the meter: 21×52 cells, the fallback for everything | Code |
| HUD, sheets, chips, Results window, postcard | Code |

All code colours come from CAMP/INK, the sprite palette already in `camp-flags.js` (WOOD, CLAMP, STONE, GOLD, GHOST) or samples the builder takes from the plates (sky top and horizon, dusk = sky top at HLS L 0.12, cloud, darkest ground). None are hand-picked. New code uses no hardcoded `rgba(0,0,0,…)` or `rgba(255,255,255,…)`; tints come from those tokens.

---

## 9. Alignment technique

The rule: **never ask the image model for two versions of anything that has to line up.**

1. **The tower is one isolated, frozen image.** Every one of the 2^9 storey states is a subset of its pixels, chosen by 9 horizontal bands cut at the painted ring beams. The builder proposes the cuts from the row profile (wide, dark timber rows) and `--proof` confirms them. Storeys cannot be out of register with each other because they are one picture, and a cut along a block row reads as voxel construction.
2. **"Not built yet" is the same pixels, not a removal edit.** The ghost is computed from the master: desaturated, washed toward the sky colour the summit has at that height, with Sobel edge lines. It sits on the identical grid. Because the tower is transparent and separate, nothing ever has to be inpainted behind a hidden storey.
3. **The backdrop meets the tower at one anchor.** That anchor is the pad centre and width, measured once on `summit.png`. The summit is generated with the chosen tower attached, so camera height and light agree. A strip of the summit's own pixels (the bushes along the pad's front edge, stored as a polygon) is drawn again over the tower foot, which hides the join. A code contact shadow seats the tower.
4. **Everything that changes per learner is code at measured anchors**, in the master's pixel coordinates (`storeys.json`): flag foot, lamp hook, effect points, cap points, tag y, window rectangles, cradle, beacon origin and eave point for each storey. A state only switches overlays on or off.
5. **No ChatGPT edits after tracing.** `storeys.json` stores the sha1 of both plates, and `build.py --check` fails if either changes without a re-trace.
6. **The beam on existing art is a measurement, not new art.** For Phase C, the apex is measured once on `hub-hero.jpg` and drawn in each surface's own frame. On the hub it appears on desktop only, and only when the computed cover crop contains the tower.
7. **Measured, not eyeballed.**
   - `--check` fails if the bands don't tile the cleaned alpha (at least 99.5% covered, no overlaps), if any storey is under 6% of the tower's height, or if any anchor is outside the tower's bounding box.
   - It also fails if any adjacent pair of code colours (tag digit on its tag, lamp frame on its glass, gold frame on the Trial's gold glass) is below 3:1. The gold frame is outlined in INK, because GOLD_DK measured only 1.2–1.6:1 against the cloths.
   - `--proof` renders a PIL contact sheet of 20 canonical states at 375×812 and 1440×900, which is reviewed before shipping and then reviewed independently (house memory "Verify visual work before done").
   - `?lookout=0|4|9|12|18|ooo|gold|stars` forces a state without saving, so the proof and a browser check use the same inputs.

**Fallbacks.**
- The bays come out wrong but the structure is right: edit the image before it is frozen.
- The art fails after five rolls: Phase A's code tower stays as the stage. It is already a complete, shippable version.

---

## 10. Implementation plan by file

**Phase A, no art (about half a session).**
- `lesson-template/build/block-camp-flags/build.py`
  - New tables: STOREYS (object, gold effect, caption, FORM) and LAMPS (station → storey).
  - TIERS = (3, 9, 18), plus the milestones.
  - Each part stamped free or pro from the hub builder's `access()`.
  - Sky, dusk and cloud tokens sampled from `watchtower-far-side.jpg`.
  - Injected into the templates as `{{LOOKOUT}}`.
  - `--check` grows the caption check: every caption has a CAPS verb group and a FORM line.
- `template.js` → `block-camp/camp-flags.js`, all inside the IIFE:
  - `lookout(flags, save)`, returning per-piece states, golds, tier, stars, adventures, flame step, dusk, milestones, `next()` and `closestGold()`;
  - `meter(state, opts)`, the 21×52 tower as crispEdges SVG rect runs;
  - `lampSprite()`;
  - the `decorateMap` chip text.
- `block-camp/camp-end.js`:
  - the meter beside the flag;
  - the caption and progress line;
  - new strings in all 10 languages;
  - the "See it built" link;
  - `camp-flags.js?v=2`.
  - Everything stays inside the existing IIFE, guarded with try/catch, and falls back to today's card.
- `template.html` → `flags.html`: the `#lookout` stage drawn as the code tower on a canvas at an integer cell size (`floor(0.9·stageH/52)`), the HUD, the chips, the storey sheet, the build-in queue with `'forbes-camp-lookout-seen'`, and the relabelled parts list.
- Hub builder: load `camp-save.js` and `camp-flags.js`; the "Your Lookout" entry with the meter.
- Quest template: the HUD stat and the Passport button and sub-line.

**Phase B, after `lookout.png` and `summit.png` (one session).**
- `build.py` gains `--ingest`, `--trace`, `--proof`.
  - Clean the alpha (or chroma-key `#00FF00`).
  - Write `BlockCamp/lookout/lookout.webp` (768×1152), `lookout-ghost.webp`, `lookout-sm.webp`, `summit.webp` (1024w and 768w) and `summit-sm.webp`.
  - Write `lesson-template/build/block-camp-flags/storeys.json`.
  - `tools/prep-artwork.py` is not used here: it writes 16:9 JPEG and would drop the alpha. Raw PNGs stay in the gitignored `incoming/`.
- New `template-lookout.js` → `block-camp/camp-lookout.js`, the canvas renderer (about 350–450 lines):
  - Path2D band clips, ghost, lip, shadow;
  - lamps, pools and dusk (`destination-out` holes, then `screen`);
  - gold effects, trim, tags, plaque, stars, bunting;
  - build-in queue, storey sheet, "Climb to the top", finale.
  - It is loaded by `flags.html`, and lazily by `camp-end.js` for the Results window.
- `docs/ARTWORK-lookout.md`: the brief, written with `mkdir -p incoming/lookout` in the same step.

**Phase C, optional and small.**
- Beam on the climb-map hero via `decorateMap` (the apex measured on hub-hero, about (1152, 413) of 1600×900; re-measure), so the hand-kept map file is not edited.
- The village template: stop label and beam.
- The postcard.
- No beam on the Quest; the hub beam on desktop only.

**After every build** run `py lesson-template/build/block-camp-flags/build.py`, then `--check`, then the other builders, then `py tools/seo.py`, always last. Before starting, check that none of these files is modified in `git status`; at the time of writing none was. Commit with `git commit -o <files>` and write a `docs/HANDOFF.md` entry.

---

## 11. Tests

- **Node test** `test-lookout.js`:
  - all 2^18 planted combinations, plus 5,000 random gold/star/adventure states, including out-of-order ones;
  - counts must equal `CampFlags.summary()`;
  - `next()` never points at an earned piece;
  - tiers flip at exactly 3, 9 and 18;
  - every string exists in all 10 languages.
- **`build.py --check`**: stale output, bands, anchors, hashes, contrast, captions.
- **Results card fit.** In a real deck at 375×667 with `html.bc-phone`, read the card's bottom against the slide's bottom with a synchronous DOM read, not a pane screenshot (house memory). Repeat with storage blocked: no errors, and today's card.
- **Contact sheets** of the 20 states (Phase A and Phase B) at phone and desktop sizes, then an independent review.

## 12. Risks that remain

- **The tower art.** ChatGPT may still miscount the levels or paint flags or glow. Mitigations: acceptance checks by eye, edits before freezing, and the code tower as fallback.
- **The tower looks pasted onto the summit.** Mitigations: the same chat, the lip occluder, the shadow, and judging at phone size.
- **Phone crowding.** Flags 32px, lamps 9×12px plus pools, tags on a rail off the tower. Check the contact sheet at 375px.
- **localStorage only.** A cleared browser or an iPhone Home Screen app shows an empty summit. The page repeats the Quest's save-code note and links to `quest.html#save`.
- **`camp-end.js` runs inside 26 decks** owned by another session. Additions declare nothing at the top level and fail silently.
- **Captions** need the house tense check before shipping.