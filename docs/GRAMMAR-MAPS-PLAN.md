# Grammar maps: the plan for the series

Innes, 2026-11-08: *"make a plan of geographical & nautical based grammar
guides — what else could work?"* The grammar page now opens with a
"Sailing the seas of grammar" section (`tools/grammar_maps.py`). This file
is the queue for it: what the series is, which charts come next, and in
what order.

The test for every idea below: **the shape of the grammar has to be the
shape of the place.** A chart works when a learner can find the rule by
looking at the geography, before reading a word. If the map is only a
pretty frame round a list, it is not a chart. Leave it out.

---

## 1. The chart language (what every map in the series reuses)

Gerundia, Countania and Regularia already share a visual grammar. Keep it
identical across the series so that a learner who has read one chart can
read the next:

| On the chart | Means | Seen in |
|---|---|---|
| Two shores facing across a strait | a binary choice | Gerundia / Infinitivia, Countania / Uncountania |
| The island in the channel | both forms work, **with a change of meaning** | Twofold Isle, Double Isle, Forked Isle |
| The Shallows (sandbank) | both forms work, **same meaning** | begin / start / like; some / any; learnt / learned |
| The False Cape (with a flag) | looks as if it belongs to one shore but does not | -ING spelled "to"; *the news is* |
| A dashed current with an arrow | a conversion, or drift over time | "prepositions run west"; "new verbs sail west" |
| Big tidy continent + archipelago | one rule, plus exceptions that come in families | Regularia / Irregularia |
| Lone Stacks / Still Rocks | one-off exceptions / forms that never change | go be do see; cut put hit |
| Harbour dots | the example words, clickable, with a place-name / bare-word toggle | every chart |
| The compass banner | the question the chart answers | ◀ HOW MANY? · HOW MUCH? ▶ |

**New forms this plan adds** (each one is needed by at least one chart
below, and each is a real piece of geography):

| Form | Means | For |
|---|---|---|
| **Quadrant chart** (two axes: north/south and east/west) | two independent choices at once | conditionals (real/unreal × past/now) |
| **Soundings** (depth numbers, contour lines) | a scale from 100 % to 0 % | certainty modals, frequency adverbs |
| **Canal with locks** | a fixed order you must pass through | adjective order |
| **River delta** | one root splitting into forms | word formation |
| **Voyage route** (one ship's track round a chart) | movement and direction | prepositions of movement |
| **Bridges and ferries** between islands | linking structures, and how they attach | linkers / connectors |
| **Contour map** (altitude) | register: higher = more formal | formal vs informal vocabulary |
| **Maelstrom** (whirlpool) | word order that flips | inversion |
| **Land-locked lake** | forms that cannot make the crossing | intransitive verbs (no passive) |

**Anything involving a tense uses the Sherpa colour for that tense** (Innes,
2026-11-13). The colours come from `lesson-template/build/sea_tense.py`,
which reads them off the route map: the land, lane or harbour that stands for
a tense is painted in it, in the layout, the painting and the page.

Do not overlap Sherpa Tensing. Sherpa teaches one tense per camp. A chart
may set two tenses against each other, as in §3.2.

---

## 2. Ready now: art exists, the lesson does not

| Chart | Art | State |
|---|---|---|
| **Regularia & Irregularia** (regular / irregular past), A2–B1 | Painted repaint + clean copy, by Codex on 2026-10-04 | **Built 2026-11-08**: `sailing-the-seas-regularia.html`, builder `build_regularia.py`. Its catalogue row was still to be inserted (see HANDOFF). |
| **Countania & Uncountania** (countable / uncountable), A2–B1 | Painted repaint + clean copy, plus two ship's rooms (store cabin, cargo hold) | **Built 2026-11-08**: `sailing-the-seas-countania.html`, builder `build_countania.py`; the stray dots are painted out by `countania_clean.py`. The galley is a written card until its picture exists (`GALLEY_IMG`). Was: **The galley is missing:** the room *between* the two, where a coffee sits beside coffee. Brief: `docs/CHATGPT-SEA-CHARTS-BRIEF.md` part 1. The clean copy still has two stray dots where the titles were, at (145,956) and (1378,956) on the 1536×1024 canvas. Paint them out in code, not by re-asking ChatGPT. |

**Where the art is:** `C:\Users\black\Documents\Codex\2026-10-04\files-mentioned-by-the-user-artwork\outputs\`.
That folder is outside the repo and is not in `incoming/sea-charts/`
(which is empty). The prompts Codex used are in `generation-prompts.txt`
and `room-generation-prompts.txt` in the same folder. The repaints moved
the harbour dots, so **re-measure every hotspot by blob detection on the
repaint itself**; do not reuse `sea_charts.py`'s coordinates. Spelling was
checked on 2026-11-08: all 31 countable and 41 verbs place names and every
caption are correct.

---

## 3. What else could work, ranked

Ranked by fit (does the grammar really have this shape?), then demand
(how often it is taught and searched), then cost. "Hub" says which topic
page the lesson joins. **new** means it needs a new entry in `tools/topics.py`.

### Wave 1: the strongest fits

**3.1 The Atlas of THE: articles with place names.** B1–B2. Hub: **new**
(articles).
The content *is* geography, so this is the most natural chart in the series.
- **Two shores:** THE-land and No-the-land.
  - THE-land holds oceans, seas, rivers, canals, deserts, mountain ranges, island groups, plural or "union" countries (*the Netherlands, the UK, the USA*) and *the north of*.
  - No-the-land holds continents, most countries, cities, lakes (*Lake Como*), single mountains (*Mount Everest*) and single islands (*Malta*).
- **False Cape:** *the Hague, the Gambia, the Matterhorn*.
- **Shallows:** *(the) Sudan, (the) Lebanon*: older usage keeps the *the*. Leave out names where the *the* is politically loaded (*the Ukraine*).
- **Harbours:** real features, each labelled with its own name.
- A second sheet could carry the general article rules (first mention / known / unique).

**3.2 Present Perfect vs Past Simple.** A2–B2. Hub: present-perfect.
- **Two shores:**
  - Finished Time: *yesterday, last week, in 2019, ago, when I was a child*.
  - Open Time: *ever, never, yet, already, so far, since, this week, recently, just*.
- **Twofold Isle:**
  - *for*: *I lived here for five years* (and left) vs *I've lived here for five years* (and still do).
  - *this morning*: past simple if it is now afternoon, present perfect if it is still morning.
- **Shallows:** *just, already, yet* with the past simple in American English, same meaning.
- **False Cape:** *When…?* questions always take the past simple (*When have you arrived?* ✗).
- The most-requested contrast in ESL.

**3.3 The Conditional Quadrants.** B1–C1. Hub: conditionals.
This is the first quadrant chart.
- **The two axes:**
  - West ↔ East: REAL ↔ UNREAL, with a reef along the reality line.
  - North ↔ South: NOW/LATER ↔ PAST.
- **The four seas:**
  - Real-now: zero and first conditionals.
  - Unreal-now: second conditional.
  - Unreal-past: third conditional.
  - Real-past: *If he said that, he was wrong*, which every textbook skips.
- **Mixed conditionals** are the currents crossing between the unreal seas.
- **Harbours for the linking words:** *unless, provided that, as long as, in case*.
- **Regret Reef**, off the third-conditional sea: *I wish… / if only…*.

**3.4 In, On, At: the Harbour of Scale.** A2–B1. Hub: prepositions.
The size of the feature *is* the preposition.

| | Place | Time |
|---|---|---|
| AT | a point: a buoy, *at the harbour mouth* | *at six, at night* |
| ON | a line or surface: *on the coast, on the river, on deck* | *on Monday, on 4 July* |
| IN | an enclosed area: *in the bay, in the sea* | *in July, in 2026, in the morning* |

- **Twofold Isle:** *in time / on time*, *in the end / at the end*.
- **Shallows:** *at / on the weekend*, BrE / AmE.

**3.5 The Voyage: prepositions of movement.** A2–B1. Hub: prepositions.
- One ship's track round one chart, each leg a preposition:
  - *out of* the harbour, *past* the lighthouse, *along* the coast, *round* the cape, *across* the bay, *through* the strait, *under* the bridge, *over* the bar, *up* the river, *towards* the island, *into* the cove, *onto* the jetty.
- Built as a route like the Sherpa map, not a two-shore chart.
- **Speaking task:** describe the voyage back.

### Wave 2: good fits, solid demand

**3.6 The -ER Coast and the MORE Coast: comparatives.** A2–B1. Hub: **new**.
- **West:** one syllable plus *-er* (with the spelling harbours *bigger, nicer*), and two syllables ending in *-y* → *-ier* (*happier*).
- **East:** *more* for two-plus syllables.
- **Shallows:** *clever, narrow, quiet, simple, gentle*, either form.
- **Lone Stacks:** *good better, bad worse, far further*.
- **False Cape:** *fun, real, right, wrong*. They look like *-er* words but take *more*.

**3.7 Statia and Actia: state and action verbs.** B1–B2. Hub: present-continuous.
- **Twofold Isle:** *think, have, see, taste, smell, look, be* (*He's being silly*).
- **Shallows:** *feel, hurt* (*I feel / I'm feeling ill*).
- **Caution (memory: "Stative is not the test"):** the chart must ask whether IS/ARE + -ING works *in that sentence*, not label verbs as stative once and for all. The island is exactly that question. Good for German and Spanish speakers.

**3.8 Makeland and Doland (with Take Island).** A2–B2. Hub: **new**, or vocabulary.
- **Makeland:** *a decision, a mistake, money, a plan, progress, friends, a noise*.
- **Doland:** *homework, the dishes, business, a favour, your best, research, damage*.
- **Take Island**, offshore: *a photo, a break, a seat*. It catches the German *machen* false friend (*make a photo* ✗) as a False Cape.

**3.9 Soundings of Certainty: modals of deduction.** B2–C1. Hub: modal-verbs.
- Depth soundings and fog banks:
  - *must* = charted deep water, 95 %;
  - *should* = probably;
  - *may / might / could* = the fog;
  - *can't / couldn't* = the rocks.
- A second contour layer for the past: *must have, might have, can't have*.
- The same chart form serves frequency adverbs (§3.15).

**3.10 The Passive Ferry.** B1–B2. Hub: passive-voice.
- Activia and Passivia, with a ferry carrying the object across to the front of the sentence.
- **The by-agent** is a buoy the ferry may skip.
- **The land-locked lake:** *happen, arrive, die, seem* never reach the sea; there is no passive.
- **Shallows:** two-object verbs (*I was given a book / A book was given to me*).
- **False Cape:** *I was born*.

**3.11 The Backshift Current: reported speech.** B1–B2. Hub: **new**.
- Direct Harbour to Reported Harbour on one current: *am → was, have done → had done, will → would, can → could*.
- Time and place words drift with it: *today → that day, here → there*.
- **Still Rocks:** *had done, would, could, should, might* do not move.
- **Shallows:** backshift is optional when it is still true (*She said she likes / liked jazz*).

### Wave 3: C1, IELTS and exam

**3.12 The Bridges: linkers.** B2–C1. Hubs: ielts + **new**.
Islands of ideas joined three ways, and the way it joins *is* the grammar:
- **Conjunction bridges** join two clauses in one sentence: *although, because, while, whereas*.
- **Preposition bridges** need a noun or -ing on the far side: *despite, because of, due to, in spite of*.
- **Ferries** need a new sentence (full stop or semicolon): *However, Therefore, Nevertheless*.

The commonest IELTS Writing error, drawn as a map.

**3.13 The Word Delta: word formation.** B2–C1. Hubs: ielts + vocabulary.
- One root river splits into noun, verb, adjective and adverb channels, with a harbour per suffix: *-tion, -ment, -ness, -ity; -ful, -ous, -ive, -able; -ise, -ify, -en; -ly*.
- Built for the Cambridge/IELTS word-formation task.

**3.14 Comma Reef: relative clauses.** B1–B2. Hub: **new**.
- Defining waters on one side of a reef of commas, non-defining on the other.
- **Harbours:** *who, which, where, whose, when*.
- **False Cape:** *that* cannot follow a comma or a preposition.
- **Sunk buoy:** the object pronoun you can drop.

**3.15 Smaller charts, each one lesson**
- **The OSASCOMP Canal (adjective order), A2–B1.** A barge carrying a noun through eight locks in a fixed order: opinion, size, age, shape, colour, origin, material, purpose. Quick to build.
- **Soundings of Frequency (frequency adverbs), A2.** *always* → *never* as depth. The anchor mark shows the position: before the main verb, after *be*.
- **The Prefix Archipelago (negative prefixes), B1–B2.** Mainland *un-*, then the islands:
  - *im-* before p, m;
  - *il-* before l;
  - *ir-* before r;
  - *in-*;
  - *dis-*;
  - *mis-*.
- **The Atlantic (British vs American), B1–C1.** Two real shores:
  - Shallows: both fine (*have you got / do you have*).
  - False Cape: same word, different meaning (*pants, chips, first floor*).
  - Grammar harbours: *gotten*, collective nouns, *shall*.
- **The Contour Map of Register, C1.** Altitude = formality: *obtain* on the peaks, *get* in the valley. Pairs for emails and essays.
- **The Inversion Maelstrom, C1.** After *Never, Rarely, Not only, No sooner, Hardly, Under no circumstances*, the whirlpool spins the auxiliary in front of the subject.
- **The Return Voyage (question tags), B1.** Out positive, back negative. Lone Stacks for *I am → aren't I*, *Let's → shall we*, imperatives → *will you*.

### Not a chart, but the same world

- **The Departure Board (future forms), B1.** A harbour scene, not a map:
  - the timetabled ferry (*leaves at six*: present simple);
  - the booked crossing (*we're sailing on Friday*: present continuous);
  - the plan (*going to*);
  - the snap decision (*I'll take the next one*: will).
- **The Shipping Forecast (probability and prediction), B2.** The BBC genre as a listening and speaking lesson: *will, is likely to, may, could, is unlikely to, is bound to*. A strong British cultural hook. Must not imitate the BBC's branding.
- **The Particle Ferries (phrasal verbs), B1–B2.** A ferry network in the style of a transit map: one line per particle (UP: finish/increase, OUT, OFF, ON, DOWN). Interchange harbours for *get, take, put, turn*, which sit on every line.

---

## 4. Recommended order

1. ~~**Regularia lesson**~~: built 2026-11-08. Copy `build_regularia.py` + `regularia_map.py` + `regularia_measure.py` for the next chart: measure the clean chart, map dots to names, write the content.
2. ~~**Countania lesson**~~: built 2026-11-08, with the galley as a written card until it is painted.
   - ~~Charts 4-12~~ (adjective canal, prefixes, soundings; register, inversion, the Atlantic, question tags, the forecast, phrasal verbs): built 2026-11-09 on `sea_lesson.py`. See HANDOFF.
3. **3.1 Atlas of THE** and **3.2 Present Perfect vs Past Simple**: the two biggest gaps with the best fit.
4. **3.3 Conditional Quadrants**, which proves the quadrant form.
5. **3.4 In/On/At** and **3.5 The Voyage** as a pair for the Prepositions hub.
6. Then Wave 2 by demand, and Wave 3 alongside the IELTS track.

**Naming.** Keep the series name on every chart: *Sailing the Seas of
Grammar: Countania & Uncountania*. The existing one stays *Sailing the
Seas of Grammar* (gerunds and infinitives); it was first.

## 5. How one chart gets made (the pipeline that already exists)

1. **Layout in code:** `lesson-template/build/sea_charts.py` draws the
   chart in the 1000×660 space and fails the build if a label leaves its
   land, touches a beach, overlaps another or runs under the border.
   `sea_paint.py` gives the coded look.
2. **Painted repaint:** ChatGPT or Codex, with the Gerundia chart
   (`sailing-the-seas-of-grammar/hero.jpg`) as the style reference and the
   coded chart as the edit target. Prompt pattern:
   `docs/CHATGPT-SEA-CHARTS-BRIEF.md`; Codex's own prompts are in the outputs
   folder (§2). Then ask for a clean copy that keeps the harbour dots. Check
   every word on the labelled copy, and count the dots on the clean one.
3. **Lesson:** on the Sailing machinery. `lesson-template/build/build_sailing.py`
   is the model: the clickable chart, the place-name / bare-word toggle,
   `EX_TR` example reveals in nine languages, the activation stage. Ship
   EN + DE + ES at minimum.
4. **Grammar page:** one entry in `tools/grammar_maps.py`, then
   `py tools/build_hubs.py` and `py tools/seo.py`. A new topic needs its
   line in `tools/topics.py` first.
