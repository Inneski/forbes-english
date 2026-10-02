# Artwork brief: Your Lookout (2 pictures)

**Drop folder: `incoming/lookout/`. It exists (made 2026-10-02).** `incoming/` is gitignored, so nothing you drop there reaches git.

## Why only two pictures, and why the order matters

ChatGPT cannot draw the same scene twice so that it lines up. So we never ask it for "the tower with 4 storeys" and then "the tower with 5". You make the **finished** tower once, on a transparent background. The site then cuts every build stage out of that one picture: hidden storeys show as a blueprint made from the same pixels. The summit is a separate backdrop, which the tower stands on at one measured point. Flags, lamps, gold, stars, the beacon and the bunting are all drawn by the site's code. So:

1. Make **picture 1, the tower**, first, and pick the best one.
2. Make **picture 2, the summit**, **in the same chat**, with the chosen tower attached, so the camera and light match.
3. Once Claude has traced the tower, **don't replace either file**. The builder checks a fingerprint of each one and stops if it changes.

Both pictures are **1024 × 1536 portrait**, which is one of ChatGPT's own sizes.

---

## Picture 1: the tower → save as `incoming/lookout/lookout.png`

Open a **new** ChatGPT chat. Attach **two** files from the repo, in this order:
1. `BlockCamp/hub-hero.jpg`
2. `BlockCampDescent/trial-gate.png`

Then paste:

```
Make ONE image, 1024 x 1536 pixels, portrait, PNG with a TRANSPARENT background.

Subject: one tall wooden fire-lookout tower, in exactly the style of the first attached picture (the tower on the hill there): a blocky voxel world built from visible cubes, soft painterly light, dark spruce timber, grey cobblestone, a stepped dark-green roof. Use the second attached picture only as an example of one object cut out cleanly on a transparent background.

Camera: a front view, turned only slightly (about 15 degrees) so a little of the right side shows. Camera level with the middle of the tower. Every post perfectly vertical, every floor perfectly level, no perspective lean, no fisheye. Low warm evening sun from the RIGHT.

The tower has exactly NINE levels stacked from bottom to top. A thick horizontal timber beam runs right across the front between every two levels, so the levels are easy to count. Four straight vertical corner posts run up through levels 2 to 6; they do NOT lean inwards. On levels 2 to 6 the FRONT face is open (only a small brace in each top corner) so we can see what stands on that level's floor; the side face has an X brace. A zig-zag stair climbs inside at the back.

Level by level, from the BOTTOM:
1. A cobblestone base with an arched wooden door, a small cream canvas awning over the door, and an unlit iron lantern on the wall beside it.
2. On this level's floor: a rope-and-pulley hoist hanging from the beam above, lifting a rolled bundle of cream canvas.
3. On this level's floor: a neat stack of logs and an empty iron fire basket.
4. On this level's floor: a small stone hearth with a short chimney pipe.
5. On this level's floor: a wooden signpost with two arrow boards pointing up, and a rolled map lying on a crate.
6. On this level's floor: a brass telescope on a wooden tripod, pointing out to the left.
7. A wrap-around plank deck with a fence railing, a little wider than the levels below; on its left end a small pile of stones and a pair of walking boots.
8. The lookout cabin: corner posts, big glass windows, a small unlit lantern hanging on the right.
9. A stepped dark-green roof with a small flat square stone platform on its very top.

Nothing else: no flags, banners, lamps or lights hanging anywhere, no fire, no smoke, no glow (both lanterns are dark), no people, no animals, no ground, no grass, no sky, no text, no logo. The whole tower in frame with clear empty space on every side; the tower about 85% of the picture's height.
```

### Check it by eye before saving

- [ ] **Count the thick beams. There should be nine levels**, bottom to top: stone base, five open levels, deck, cabin, roof. Eight or ten means reroll.
- [ ] **The posts are vertical.** Hold a window edge or a ruler against the screen: they don't lean in toward the top.
- [ ] **You can see the right object on levels 2–6**: hoist, logs and basket, hearth, signpost, telescope. If only one is missing or wrong and everything else is good, ask in the same chat: *"Same picture, but on level N put …"*. Edits are fine now, before the picture is frozen.
- [ ] **No flags, no banners, no fire or glow, no people.** The lanterns are dark.
- [ ] **Nothing is cut off** at the top, bottom or sides.
- [ ] **The background is really transparent.** If the chequerboard is painted *into* the picture (you can see grey and white squares in a normal image viewer), ask: *"Same picture on a flat plain pure green #00FF00 background instead, no shadow on the background."* The builder keys the green out. Save that one under the same name.

Up to about 5 rolls is normal. If none passes, tell Claude: the code-drawn tower ships anyway and nothing is lost.

---

## Picture 2: the summit → save as `incoming/lookout/summit.png`

Stay **in the same chat**. Attach **three** files, in this order:
1. the `lookout.png` you just chose
2. `BlockCamp/hub-hero.jpg`
3. `BlockCampDescent/watchtower-far-side.jpg`

Then paste:

```
Make ONE image, 1024 x 1536 pixels, portrait, in exactly the same blocky voxel style as these pictures.

This is the top of the hill where the tower in the first picture will stand. Do NOT draw the tower: draw the empty place for it.

Camera at the same height and angle as the first picture (level with the middle of a tall tower), so the ground is seen almost edge-on. Light: low warm evening sun from the RIGHT, the same light as on the tower.

- Ground: the flat grassy hilltop fills the bottom 15% of the picture. In the exact centre, an EMPTY, level, square build pad of packed earth and gravel edged with grey stone blocks. Its front edge is about 88% of the way down the picture, and it is about 45% of the picture's width.
- Right along the front edge of the pad, a low row of grass blocks and small bushes, only one or two blocks high.
- Sky: deep twilight blue at the very top, fading to warm gold at the horizon, like the third picture. A few small blocky clouds only near the left and right edges.
- Keep a tall empty column of clear sky above the pad, the middle half of the picture's width, from the pad all the way to the top: no trees, no clouds, nothing.
- A trail comes up to the pad from the bottom left; another trail goes down over the far side on the right. Low bushes and a few rocks round the hilltop, pine and birch treetops below the edge, distant blue ridges on the horizon.
- No tower, no building, no people, no animals, no flags, no text, no logo, no sun disc in the sky.
```

### Check it by eye before saving

- [ ] **Nothing stands on the pad**, and there is no tower anywhere.
- [ ] The pad is **in the middle**, with its front edge **low**, about seven-eighths of the way down.
- [ ] The **middle half of the sky is empty** from the pad to the top edge.
- [ ] The **top is deep blue and the horizon warm gold**, with the light coming from the right, the same side as on the tower.
- [ ] A low line of bushes runs along the front of the pad (it hides the join).

---

## Only if Claude asks for it: a repair picture

If the tower passes everything except one or two objects on levels 2–6, Claude may ask for a small sheet of just those objects. **Don't make it unless asked.**

## When both are in the folder

Tell Claude: *"lookout art is in incoming/lookout/"*. The session then:
- cleans the transparency;
- traces the nine levels;
- makes the blueprint ghost from the same pixels;
- places the tower on the pad;
- sends you a contact sheet of the build stages at phone size **before** anything goes live.