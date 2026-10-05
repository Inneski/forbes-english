# Brief for ChatGPT — the pictures for The Descent (the storm and the yak)

**How to use this file.** Open the ChatGPT chat that made The Climb's pictures
(it already knows the team, Momo and the style), or start a new one and attach
the character deck and Momo's portrait (`SherpaClimb/cast-momo.jpg`). Paste
everything between the two rules, then type **next** for each scene. Twelve
scenes.

Save them into **[C:\Users\black\Documents\FORBES\incoming\sherpa-descent](../incoming/sherpa-descent)** (the folder exists on Innes's
machine) as `summit-night.png`, `camp-12.png`, `camp-10.png`, `camp-07.png`,
`camp-06.png`, `camp-05.png`, `camp-04.png`, `camp-03.png`, `camp-02.png`,
`camp-01.png`, `finale.png` and `base-camp.png`. Then tell a local Claude
session: *"The Descent pictures are in incoming/sherpa-descent — put them
in."* Until a picture exists, the game shows that camp's picture from The
Climb, so nothing is ever blank.

The scenes come from the game's own lines
(`lesson-template/build/sherpa-climb/content_descent.py`). The story runs as
follows:

1. Coming down from the summit, a severe storm closes in.
2. The hut has been wrecked.
3. On the ice wall the rope jams and Otto hurts his ankle.
4. Navya sends Momo the yak up from base camp.
5. Momo finds the team in a whiteout by the smell of Sam's two-week-old socks.
6. Momo carries Otto down.

---

I'm making the pictures for the second half of the same English-learning
game: **The Descent**. The same team comes down the mountain, and a severe
storm hits on the way. Use exactly the same people, clothes and drawing
style as before (the attached sheet and portraits), and the same Momo the
yak: big, shaggy, dark brown, with a woven red halter and a small bell.
Make **twelve scenes**, one at a time. Make scene 1 now, and the next one each
time I say "next".

**The team:**
- **Tensing:** the guide, calm, always at the front.
- **Myra:** the planner, with the map and the radio.
- **Otto:** the oldest. He hurts his ankle at scene 5 and is carried from then on.
- **Sam:** young, on his first big climb.
- **Navya:** runs the base-camp radio, with her mug of coffee. She stays at base camp, so she appears only in scenes 10, 11 and 12.
- **Momo:** the yak. He lives at base camp and climbs up to rescue them. He appears from scene 7 on.

**The style.** Match the earlier scenes: crisp angular matte colour planes,
fine print grain, and the same coral, slate and pale-blue clothing. This half
is darker. It is lit by dusk, snow-light, head torches and the glow of a tent,
with deep slate-blue and night-blue skies, and the familiar soft pink only where
the light comes back near the end. Keep the storm dramatic but never gloomy
or frightening for children: people are always safe in the end. No text,
no letters, no logos and no watermark.

**The frame for every scene: landscape, 1536 × 1024.**
- **Put the people and the action in ONE half**, the half each scene names.
  Keep the other half calmer (sky, snow, cloud), because the question card
  covers it.
- **Keep faces and the important action away from the bottom sixth.** On
  wide screens the game trims the bottom, never the top.
- People should read clearly at phone size.

**The twelve scenes:**

1. **The top, late afternoon.** The team stands on the summit. Far away, a
   black wall of storm cloud is massing on the horizon, and Tensing points
   down the route. People on the LEFT; the storm on the right.
2. **Camp twelve, the race.** Packing in a hurry by the summit cairn, wind
   rising, spindrift blowing. Myra checks her watch while Sam and Otto coil
   ropes. People on the RIGHT.
3. **Camp ten, the wrecked hut, at dusk.** A small stone hut with its door
   kicked in and part of the roof gone. Birds fly up from spilled food. Sam
   stands in the doorway staring; Otto looks at the roof. People on the
   LEFT.
4. **Camp seven, the radio, in the morning.** Snow is starting. Myra crouches
   with the radio to her ear; Tensing and Sam stack heavy bags under an
   overhanging rock to leave them behind. The pass beyond is lost in cloud.
   People on the RIGHT.
5. **Camp six, the ice wall, in a blizzard.** Otto is being lowered down a
   steep ice wall on a rope, which has jammed halfway. Sam, at the top,
   holds a head torch on him while Tensing braces the rope. The most
   dramatic scene: driving snow, but everyone's face is still clear. The
   action on the LEFT.
6. **Camp five, night in the tent.** Inside a small tent battered by snow,
   lit by one lamp. Otto lies with his ankle strapped up, making a joke;
   Myra talks into the radio. Warm light inside, blue storm outside. People
   on the RIGHT.
7. **Camp four, the whiteout: Momo arrives.** Almost white with blowing
   snow. A huge shaggy shape with horns and a red halter looms out of the
   whiteout on the ridge above the tents. It is Momo, with one of Sam's old
   grey socks hanging from his mouth. Sam points up, open-mouthed. Momo on
   the LEFT, big and heroic.
8. **Camp three, the rescue.** Momo leads the team down through the
   whiteout. Otto rides on Momo's back, wrapped in jackets, holding the
   halter; the others follow on a rope behind. Momo on the RIGHT, walking
   towards the viewer.
9. **Camp two, the storm breaking.** Evening; the clouds are tearing open and
   the first pink light comes back. The team rests by a small fire; Sam
   feeds Momo hay from his hands. People on the LEFT.
10. **Camp one, base camp in sight.** Below the lake, base camp's tents and
    prayer flags are visible. Porters carry a stretcher up the path towards
    the team, and far below, Navya waves both arms. Action on the RIGHT.
11. **Base camp, home.** Otto sits on a stretcher while a doctor checks his
    ankle. Momo is being brushed by two porters and cheered by everyone.
    Navya carries a cake. People on the LEFT.
12. **The end: Momo the hero.** Sunset at base camp, the mountain clear and
    pink behind. Momo wears a medal on a ribbon, half chewed. The whole team
    stands round him, Otto on crutches and Navya with her mug. Everyone on
    the RIGHT; the mountain on the left.

---

## For the Claude session that receives the pictures

1. **Sort and check.** Look at every file in `incoming/sherpa-descent/`.
   Name each one by its scene above and check it against the deck: is Otto
   carried from scene 5 on, is Momo in 7–12, and is Navya only in 10–12?
2. **Prep.** `py tools/prep-artwork.py incoming/sherpa-descent/<file> --into
   SherpaDescent --names camp-06 --width 1536 --quality 82` (scene 1 is
   `summit-night`, 11 is `finale`, 12 is `base-camp`). Then make each `-sm`
   copy at 960 px with the PIL one-liner in `docs/ARTWORK-sherpa-climb.md`.
3. **Build and check.** `py lesson-template/build/sherpa-climb/build.py
   --game descent`, then `node lesson-template/build/sherpa-climb/test_climb.js
   --game descent`. Look at every stop at phone and desktop size: tops are
   never cut, and the card must not cover a face.
4. **Commit** `SherpaDescent/` and the page together.
