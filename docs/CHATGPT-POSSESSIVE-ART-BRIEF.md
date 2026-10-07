# Brief for ChatGPT — the pictures for My Cat, Your Dog (A1, young learners)

**How to use this file.** Start a new ChatGPT chat, paste everything between
the two rules, then type **next** for each picture. Five pictures.

Save them into **[C:\Users\black\Documents\FORBES\incoming\possessive-adj](../incoming/possessive-adj)**
(the folder exists on Innes's machine; the builder recreates it whenever it
runs without the art) as `hero.png`, `mia.png`, `leo.png`, `near-far.png`
and `pet-show.png`. Then tell a local Claude session: *"The possessive
pictures are in incoming/possessive-adj — put them in."*

What that session does (also in the builder's docstring,
`lesson-template/build/build_possessive_adj.py`):

```bash
py tools/prep-artwork.py incoming/possessive-adj --into PossessiveAdj --names hero,mia,leo,near-far,pet-show
py lesson-template/extract-palette.py PossessiveAdj/hero.jpg --light   # paste into PALETTE_LIVE
py lesson-template/build/build_possessive_adj.py                       # now writes the live page
node lesson-template/check-lesson.js forbes-english-possessive-adjectives-a1.html
```

then the catalogue row, `tools/build_hubs.py`, `tools/seo.py`, commit, push.
`--names` maps in the order the files are listed, so pass the five files
by name rather than the folder if the order is in doubt.

**Where each picture goes.** Every picture is used three ways: whole, on its
stage's opening slide; as a tall slice (about the middle-right half) beside
the reading text; and faintly behind the questions, where the answers sit on
the LEFT. So the people and animals go in the **right half**, and the left
third stays plain.

---

I'm making the pictures for an English lesson for children of about eight to
ten. It teaches "my, your, his, her, its, our, their" and "this / that",
through one family and their pets. Make **five pictures**, one at a time.
Make picture 1 now, and the next one each time I say "next". Keep the same
characters, clothes and drawing style in all five.

**The style.** Bright, friendly, flat picture-book illustration: simple
rounded shapes, clean flat colour, no outlines or only soft ones, a light
paper grain. Warm, cheerful pastels (butter yellow, peach, mint, sky blue)
with a few strong accents (tomato red, deep teal). Friendly cartoon faces
with simple dot eyes and small smiles — sweet, never scary, never realistic.
No text, no letters, no numbers, no logos, no signs, no watermark.

**The cast — the same in every picture:**
- **Mia**, a girl of nine: brown hair in a high ponytail, yellow T-shirt,
  denim dungarees, white trainers.
- **Pepper**, Mia's cat: black and white, with white paws and a white chest.
- **Leo**, Mia's little brother, seven: short sandy hair, red hoodie, green
  shorts.
- **Biscuit**, Leo's puppy: golden-brown, floppy ears, a red ball. His bed is
  bright blue.
- **Snowy**, the family rabbit: white, pink ears.
- **Grandpa Joe**: grey beard, flat cap, green cardigan. **Rio**, his
  parrot: blue and yellow.
- **Ella and Sam**, twin neighbours (a girl and a boy, about nine): matching
  red-and-white striped jumpers. **Tank**, their tortoise.
- **Mr Brown**, the teacher: round glasses, brown jacket. A goldfish in a
  round bowl.

**The frame for every picture: landscape, 1536 × 1024.**
- **Put all the people and animals in the RIGHT half** of the frame, centred
  about two-thirds of the way across. Keep the left third calm and plain
  (lawn, sky, a plain wall), because text goes there.
- Keep faces away from the very top and bottom edges.
- Characters must read clearly at phone size: big, simple, not too many
  small details.

**The five pictures:**

1. **The cover — the whole family in the garden.** Mia sits on the lawn
   hugging Pepper; Leo kneels beside her with Biscuit licking his face;
   Snowy the rabbit sits in front of them. A sunny afternoon, a low fence
   and a tree behind. Everyone on the RIGHT; plain lawn and sky on the left.

2. **Mia and her cat, in Mia's bedroom.** Mia sits on her bed holding
   Pepper up proudly, as if saying "This is my cat!". A soft cushion, a
   window with sky, a small cat bowl on the floor. Mia on the RIGHT; a
   plain pale wall on the left.

3. **Leo and his puppy, in the garden.** Leo has just thrown the red ball;
   Biscuit leaps after it, ears flying. Biscuit's bright blue bed is by the
   back door. Leo and Biscuit on the RIGHT; open lawn on the left.

4. **Near and far — "this" and "that".** Big, close to us: Mia holding
   Snowy in her arms. Behind her, Leo points far into the distance, where a
   SMALL brown horse stands in a field on a hill, clearly far away. The
   difference between close (the rabbit) and far (the horse) must be
   obvious at a glance. Mia slightly right of centre, Leo and the distant
   horse further right; open sky and grass on the left.

5. **The school pet show.** A sunny school playground with coloured
   bunting (no letters on it). Grandpa Joe with Rio the parrot on his
   shoulder; Ella and Sam proudly holding up Tank the tortoise; Mr Brown
   behind a small table with the goldfish bowl. Happy, busy, but not
   crowded. Everyone on the RIGHT; a plain stretch of playground and sky on
   the left.

---

## Notes for the session that puts them in

- ChatGPT renders 3:2; `prep-artwork.py` will flag "not 16:9". That is
  expected here: the panel takes a 0.76 slice and the divider and cover
  crop to fill, and the subject is already placed for both.
- Panels use `pos='78% 50%'` (in `panel()` in the builder). If a picture's
  subject sits further left, pass a `pos=` for that panel rather than
  recropping the file.
- The preview palette in the builder is derived from a placeholder and must
  be replaced by the extractor's reading of the real `hero.jpg`; the builder
  refuses to write the live page until `PALETTE_LIVE` is filled.
