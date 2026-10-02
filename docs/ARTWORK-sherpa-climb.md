# Artwork brief: The Climb (Sherpa Tensing's tense game)

Innes, 2026-10-02, after the first build: *"Your characters will be getting
replaced and a lot of those landscapes gonna be people."*

So this brief pins each picture to its moment in the story, says who is in
the frame, and gives the file name the game picks up. **Drop the renders in
`incoming/sherpa-climb/`** (the folder exists on Innes's machine; it is
gitignored, so a cloud session has to say "make it").

Nothing in the game's code needs to change when a picture arrives:

- **Characters:** `SherpaClimb/cast-<who>.jpg` replaces that character's drawn
  figure everywhere (the team cards, the speaker beside every line).
  `build.py` looks for the file; if it is absent, the figure stays.
- **Camp scenes:** `SherpaClimb/camp-01.jpg` … `camp-13.jpg` and `summit.jpg`
  (the summit push) replace the landscapes now in place. Each needs its
  `-sm.jpg` phone copy at 960 px. The card sits on the quieter half of the
  picture: `build.py` measures it (`quiet_side()`), or a camp in `content.py`
  can say `'side': 'left'`.
- **The summit screen:** `SherpaClimb/summit-top.jpg` replaces the course's
  sherpa render (`Sherpa Tensing/sherpa-day.jpg`) once it exists.

After dropping files: `py tools/prep-artwork.py incoming/sherpa-climb/<file>
--into SherpaClimb --names <name> --width 1600 --quality 82` (scenes) or
`--width 800` (portraits), make the `-sm` copy for a scene:

```bash
py -c "from PIL import Image; im=Image.open('SherpaClimb/camp-06.jpg'); im.resize((960, round(im.height*960/im.width)), Image.LANCZOS).save('SherpaClimb/camp-06-sm.jpg', quality=80, optimize=True, progressive=True)"
```

then
`py lesson-template/build/sherpa-climb/build.py`, then
`node lesson-template/build/sherpa-climb/test_climb.js`.

## The look

Match the course: the flat matte gouache of the route map and the sherpa
render (`Sherpa Tensing/sherpa-day.jpg`): pink and slate blue, soft paper
grain, quiet skies. The style stem the Sherpa heroes used:

```text
flat matte gouache mountain landscape, soft paper grain, muted natural tones, wide empty sky
```

**Faces.** The Sherpa art so far has no faces: the sherpa is drawn from
behind, and `docs/ARTWORK-sherpa-tensing.md` rules "No faces". The prompts
below keep people **seen from behind or far off**, so the game matches the
course. If you want faces, delete "seen from behind" from a prompt; nothing
in the game depends on it.

**One half quiet.** On a laptop the question card covers about 40% of the
picture, on whichever side is calmer. Keep the people and the action to one
side.

## The cast: portraits, 4:5, at least 800 × 1000

Head and shoulders to waist, one person, plain background, the same light in
every portrait so they read as one team. File names are the game's keys.

| File | Who | What the lines say about them |
|---|---|---|
| `cast-tensing.jpg` | **Tensing**, the guide | Calm, has never got lost in twenty years, watches the sky before waking the team, gets the locked hut door open. (Optional: the course's own sherpa render is already used.) |
| `cast-ana.jpg` | **Ana**, the planner | Brisk; the schedule, the forecast, the map; decides "we leave at six". |
| `cast-otto.jpg` | **Otto**, the old hand | Climbing since 1987, first up this mountain in 1998 with his brother; snores, sings the same song for an hour, loses glasses that are on his head; once rescued after two days in the snow. Older. |
| `cast-sam.jpg` | **Sam**, first big climb | Young, keen, keeps a diary, sore legs, the same socks for two weeks; meeting his sister in Kathmandu after the climb. |
| `cast-doris.jpg` | **Doris**, base camp radio | At base camp with a radio handset and a coffee; has known Otto twenty years. |
| (no file) | **Momo**, the yak | Never speaks, so he has no portrait. He can appear in Doris's base-camp scenes. |

Prompt pattern:

```text
portrait of <who: e.g. a brisk woman mountaineer holding a folded map>, seen from behind and slightly turned, head and shoulders, plain pale background, flat matte gouache, soft paper grain, muted pink and slate blue --ar 4:5 --style raw
```

## The camps: one scene each, 16:9, at least 2000 px wide

Each scene is the moment the camp's own lines describe, so the picture and
the questions tell the same story. The current landscape is listed so you
can keep it where a camp needs no people.

| File | Camp · tense | The moment (from the lines) | In the frame | Now |
|---|---|---|---|---|
| `camp-01.jpg` | 1 · present continuous | Dawn by the lake, day one. The sun **is coming** up; Otto and Ana **are cooking** breakfast; Sam **is tying** his boots. | The team packing up at the water's edge, small, to one side | the tarn with rings |
| `camp-02.jpg` | 2 · present simple | The foot of the granite rock. Every morning Tensing **watches** the sky first, then wakes the team. | Tensing alone on a rock, looking up; tents behind | the granite foot |
| `camp-03.jpg` | 3 · past simple | Evening at the struck campsite after fourteen kilometres. An eagle **flew** over them. | Sam writing his diary on a rock; an eagle overhead | the struck campsite |
| `camp-04.jpg` | 4 · present perfect | They **have climbed** twelve hundred metres. Otto **has gone** to look at the ice; a rope runs up from the small lower camp. | Two small figures on a rope up the slope | the rope from the camp |
| `camp-05.jpg` | 5 · going to | The plan: the meadow tomorrow, then the ridge. Clouds say it **is going to** rain tonight. | Ana pointing ahead with a map, the ridge and the weather beyond | the meadow and the ridge |
| `camp-06.jpg` | 6 · past continuous | The storm on the ridge: they **were crossing** when it hit; hail; a rock fell past Sam. | The team roped together on a narrow ridge in slanting hail | clouds massing on the ridge |
| `camp-07.jpg` | 7 · will | Weather building that nobody can read yet; Otto **will carry** Sam's bag. | Otto taking a pack from Sam, a wall of cloud behind | the bank of weather |
| `camp-08.jpg` | 8 · present perfect continuous | They **have been climbing** since dawn; wet snow, sore feet; Otto **has been singing** for an hour. | Boot tracks in wet snow with the tired team far along them | the boot tracks |
| `camp-09.jpg` | 9 · future continuous | A small tent on a rock ledge; tomorrow they **will be crossing** the glacier, visible beyond. | One lit tent on a ledge at dusk, the glacier behind | the tent on the ledge |
| `camp-10.jpg` | 10 · past perfect | Another team **had** already **cut** steps in the ice; the hut ahead **had been locked**. | Steps cut in an ice slope, the team looking at them; a hut far off | the empty snowy ledge |
| `camp-11.jpg` | 11 · past perfect continuous | They **had been shivering** outside the hut for an hour when Tensing got the door open. | Footprints to a small hut at twilight, light in the doorway, the team going in | the hut and the footprints |
| `camp-12.jpg` | 12 · future perfect | By ten the day after tomorrow they **will have reached** the top: the cairn below the summit. | The cairn with the team small beside it | the cairn |
| `camp-13.jpg` | 13 · future perfect continuous | The last camp; the summit push starts at four; by sunrise they **will have been walking** for two hours. | A line of head torches climbing the final snowfield before dawn | the final snowfield |
| `summit.jpg` | the summit push | The last pitch to the top at sunrise. | The team on the final ridge, the sun coming up | a second cairn render |
| `summit-top.jpg` | the summit screen | "We've made it. Look down: every camp is behind us." | The whole team on the top, seen from behind, the camps far below | the sherpa render (`sherpa-day.jpg`) |

Doris and Momo stay at base camp, so they are never on the mountain in a
camp scene. If you want them in a picture, the arrival line of camp one
("I'm watching you through the telescope. Wave!") is the moment.
