# Brief for ChatGPT: the pictures for The Comeback Ride (B2–C1)

**Superseded 2026-11-08.** These six plates were replaced by Midjourney renders when the deck was rebuilt as a classic Forbes deck (see `docs/HANDOFF.md`). Kept as a record.

**How to use this file.** Start a new ChatGPT chat, paste everything between
the two rules, then type **next** after each picture. Six pictures.

Save them into **[C:\Users\black\Documents\FORBES\incoming\comeback-ride](../incoming/comeback-ride)**
(the folder exists on Innes's machine) as `hero.png`, `talk.png`, `a.png`,
`b.png`, `c.png`, `act.png`. Then tell a local Claude session: *"The comeback
pictures are in incoming/comeback-ride: put them in."*

What that session does:

```bash
py tools/prep-artwork.py incoming/comeback-ride/hero.png incoming/comeback-ride/talk.png incoming/comeback-ride/a.png incoming/comeback-ride/b.png incoming/comeback-ride/c.png incoming/comeback-ride/act.png --into ComebackRide --names hero,talk,a,b,c,act --min-width 1000
py lesson-template/build/build_comeback_ride.py     # real plates win over the stand-ins; palette re-derived from hero
node lesson-template/check-lesson.js the-comeback-ride.html
py tools/standins.py                                # drops the six slots from the shopping list
```

(`--min-width 1000` because ChatGPT's squares are 1024 wide; the default
floor is 1400.) Then `tools/build_hubs.py`, `tools/seo.py`, commit, push. The library card is
`LibraryCards/the-comeback-ride.jpg`, 1200×512, cut from the hero.

**Done 2026-11-06:** all six pictures landed and the deck runs on them.

**Where each picture goes (house style 2).** The hero sits on the right half
of the cover. Every other picture is cropped into a tall rounded card beside
the text. So the subject sits in the middle, with plain background all round
it, and nothing important goes near the edges.

---

I'm making the pictures for an English lesson for adults (upper-intermediate)
about why old-fashioned designs come back into fashion: classic motorbikes,
round dials, retro scooters. Make **six pictures**, one at a time. Make picture
1 now, and the next one each time I say "next". Keep the same style and the same
colours in all six.

**The style.** Flat vector illustration, like a modern editorial magazine
illustration: simple geometric shapes, solid flat colour, no outlines or
very thin ones, no gradients, no shading, no texture, no 3D, no photo realism.
One clear idea per picture, with plenty of empty space. A Noma Bar kind of
cleverness is welcome but never at the expense of clarity.

**The colours, in every picture:** a plain warm off-white background
(#F6F2E8), with cream (#E4DABA), terracotta orange (#AF502E), a brighter
orange accent (#FF9E69), deep bottle green (#213632), sage (#A4ACA1) and a
little mustard yellow. No other colours.

**Never:** text, letters, numbers, brand names, logos, badges, number plates,
signs or watermarks. The dials have tick marks but no numbers. No people's
faces; where a person is needed, leave them out or show only a hand.

**The frame.** Picture 1 is landscape, 1536 × 1024. Pictures 2 to 6 are
square, 1024 × 1024. In every picture the subject sits in the **centre**,
taking up about half the frame, with plain off-white background on every side.
Nothing important within the outer fifth of the frame: the pictures get cropped.

1. **The cover.** A classic motorbike in side view, parked: round headlamp,
   cream teardrop tank, one round dial, spoked wheels, standing on a plain
   floor line. Its shadow on the floor is the silhouette of a sleek modern
   sports bike, in bottle green. (The idea: the old shape and the new one are
   the same machine.) If the shadow makes the picture hard to read, drop it
   and keep the classic bike alone.

2. **Let's talk.** An open-face motorbike helmet in cream and terracotta with a
   pair of round goggles on it, and two simple empty speech bubbles floating
   above it, one orange and one green.

3. **The reading.** A rounded 1950s-style Italian scooter in cream, parked
   beside a small round café table with one coffee cup on it. No brand, no
   badge, no plate.

4. **The sound.** A single-cylinder motorbike engine drawn as simple flat
   shapes (cylinder with cooling fins, an exhaust pipe), with three curved
   lines coming out of the exhaust like a sound or a heartbeat.

5. **The sales figures.** A simple bar chart of five plain bars standing on a
   floor line, no axes, no numbers. The two tallest bars are almost exactly
   the same height, one a tiny bit taller than the other, and a small classic
   motorbike sits on top of the tallest one.

6. **The design meeting.** Two wooden stools at a workbench. On the bench: a
   motorbike dashboard that has one round dial (tick marks only) and one small
   blank screen side by side, a blank sketch pad and a pencil.
