# -*- coding: utf-8 -*-
"""My Cat, Your Dog — possessive adjectives and THIS / THAT (A1, young learners).

House style 2 (the panel deck), 47 slides. Built 2026-10-07 from Innes's four-page
coursebook sheet for William ("possessive adjectives.pdf", in his student
notes): possessive adjectives with a key-language table, how to form them
(I → MY … THEY → THEIR), a picture match, a gap fill with the subject in
brackets, an error correction, THIS / THAT for near and far, a word-order
task, a listening and a speaking chart.

Every teaching point on the sheet is here; none of its sentences, names or
pictures are. The cast is new and built for young learners — Mia, her cat
Pepper, her brother Leo and his dog Biscuit, the family rabbit Snowy, Grandpa
Joe's parrot, the twins' tortoise, the teacher's goldfish — so the deck can be
one story (a school pet show) rather than a list of strangers' pets.

What changed against the sheet, and why:

  * **The sheet's error-correction task (5.5) tests AM / IS / ARE**, not
    possessives — "Duke am our dog". It is a different lesson and is not
    carried over; the matching slot is a HIS / HER sort that tests the one
    thing a German speaker gets wrong: the OWNER chooses HIS or HER, not the
    animal.
  * **Two points the sheet never makes, both for a German speaker**, are a
    teach slide of their own: MY never changes (MEIN Hund, MEINE Katze,
    MEINE Hunde → MY, MY, MY), and ITS is not IT'S.
  * **The listening task (5.10) has no audio** in this deck; there is no
    recording to rebuild it from. Its place is taken by the translation
    stage below.
  * **The sheet's speaking chart (5.11)** is the activation stage's
    speaking task, made about the learner's own family and pets.

**The translation stage — Innes's request:** "will be compared with
translated text — english or german toggle in the exercise e.g. you may be
asked to translate". `translate()` below writes an ordinary gap slide, so
the engine scores, reviews and prints it with no new code path. Each row
carries both directions; a switch at the top (Deutsch → English / English →
Deutsch) swaps the prompt and the answer set on every translate slide at
once, and locks on a slide once it is checked. The feedback under each row
prints the German and English sentences side by side, which is the
comparison. Accepted answers are expanded at build time: final punctuation
optional, THAT'S / IT'S contractions, and ä/ö/ü/ß typed as ae/oe/ue/ss for a
keyboard without them. "Das ist" is THIS or THAT, so both are accepted;
"Das hier" is THIS only and "das da drüben" THAT only, which is the point.

**Stage 4, camping at the lake — Innes, 2026-10-14, "include this vocab"**,
with a screenshot of his annotated cover of "A1 Our Small Traditions -
Possessive Adjectives" (William's folder): tent, lake (der SEE) against sea
(das MEER), trees, next to, behind, kid / child, son, daughter, jumper,
stripe, and his SUBJEKT / OBJEKT table (Er = HE, Sie = SHE / THEY / polite
YOU, ihm = HIM, sie = HER). The table became the "Sie, sie and ihr" slide,
because IHR / IHRE = HER, THEIR or YOUR is the possessive trap for a German
speaker. Six translation rows use the same words; "Sie ist ihre Tochter"
accepts HER and THEIR, since German cannot tell them apart there.

**Split into two parts — Innes, 2026-10-14, "split".** 47 slides was too
long for a nine-year-old. Part 1 (25 slides,
`forbes-english-possessive-adjectives-a1-part1.html`): MY … THEIR, HIS / HER /
ITS, the three tips, and the first two translate slides. Part 2 (27 slides,
`…-part2.html`): THIS / THAT, the camping words and Sie / ihr, the pet show and
the last three translate slides. Each has its own cover, results and
activation; the activation chips are shuffled so the BANK gate does not read
them as a word bank in gap order.

**Art.** Six Midjourney plates, briefed in docs/ARTWORK-possessive-adj.md
(ChatGPT version: docs/CHATGPT-POSSESSIVE-ART-BRIEF.md). Part 1 uses hero,
mia, leo; Part 2 uses near-far, lake (its cover), pet-show. Each part is
written live as soon as ITS three plates are in; until then it writes a
gitignored `_`-prefixed preview on placeholder plates the builder draws
(`PossessiveAdj/_ph-*.jpg`). The drop folder `incoming/possessive-adj/` is
created while any plate is missing.

When the plates land: `py tools/prep-artwork.py <the six files> --into
PossessiveAdj --names hero,mia,leo,near-far,lake,pet-show`, then
`py lesson-template/extract-palette.py PossessiveAdj/hero.jpg --light` (Part 1)
and `… PossessiveAdj/lake.jpg --light` (Part 2), and paste each block into
PALETTE_LIVE[1] / [2] below (every row must PASS).

Run from the repo root:  py lesson-template/build/build_possessive_adj.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_possessive_adj as I

TPL = 'lesson-template/lesson-template.html'
F = 'PossessiveAdj'

# Innes, 2026-10-14: "split". 47 slides was too long for a nine-year-old.
# Part 1: MY ... THEIR, HIS / HER / ITS, two translate slides.
# Part 2: THIS / THAT, the camping words and Sie / ihr, three translate slides.
# Each part is written live only when ITS OWN plates are in; the cover of
# each part is one of its plates (hero for Part 1, lake for Part 2).
PARTS = {
    1: dict(live='forbes-english-possessive-adjectives-a1-part1.html',
            slots=['hero', 'mia', 'leo'], cover='hero',
            title='My Cat, Your Dog — Possessive Adjectives, Part 1 (A1)'),
    2: dict(live='forbes-english-possessive-adjectives-a1-part2.html',
            slots=['near-far', 'lake', 'pet-show'], cover='lake',
            title='This Is Our Tent — Possessive Adjectives, Part 2 (A1)'),
}
SLOTS = PARTS[1]['slots'] + PARTS[2]['slots']


def ready(part):
    return all(os.path.exists('%s/%s.jpg' % (F, s)) for s in PARTS[part]['slots'])


PIC = {s: ('%s.jpg' % s) if os.path.exists('%s/%s.jpg' % (F, s)) else ('_ph-%s.jpg' % s)
       for s in SLOTS}

# Innes, 2026-09-30: "make sure the folder exists or you tell me to make it".
DROP = os.path.join('incoming', 'possessive-adj')
if not (ready(1) and ready(2)):
    os.makedirs(DROP, exist_ok=True)

E = I.T['en']

# Placeholder colours, one per slot: flat, pale, nothing to do with the
# finished art. The preview palette below is extract-palette.py --light run
# on _ph-hero.jpg, so it is derived, not picked — and it is thrown away when
# the real hero arrives.
# py lesson-template/extract-palette.py PossessiveAdj/_ph-hero.jpg --light
# (2026-10-07; every row PASS)
PH = {'hero': (247, 214, 170), 'mia': (205, 226, 240), 'leo': (214, 236, 200),
      'near-far': (240, 214, 226), 'lake': (200, 230, 228),
      'pet-show': (236, 230, 196)}

PALETTE_PREVIEW = """  --hero: url('%s/%%s');

  --void          : #d5d5b0;
  --surface       : #dfdfc7;
  --surface2      : #d9d9bb;
  --border        : #96764a;
  --text          : #2a1f11;
  --text-dim      : #5e4a2e;
  --accent        : #824b00;
  --accent-bright : #693d00;
  --accent-dim    : #eb8f12;
  --secondary     : #fdfdfb;
  --contrast      : #09636d;""" % F

# Paste extract-palette.py's block for each part's cover plate here
# (Part 1: PossessiveAdj/hero.jpg, Part 2: PossessiveAdj/lake.jpg).
# The preview uses PALETTE_PREVIEW for both parts; it is a stand-in.
PALETTE_LIVE = {1: None, 2: None}


def palette(part):
    cover = PARTS[part]['cover']
    if not ready(part):
        return PALETTE_PREVIEW % PIC[cover]
    if not PALETTE_LIVE[part]:
        sys.exit('Part %d: the plates are in, but PALETTE_LIVE[%d] is empty. Run\n'
                 '  py lesson-template/extract-palette.py %s/%s.jpg --light\n'
                 'and paste its block into this builder.' % (part, part, F, cover))
    return PALETTE_LIVE[part]


def placeholders():
    """Flat stand-ins so the preview passes the ART gate and shows where each
    picture's subject sits: a disc in the right third, the slot's name on it."""
    from PIL import Image, ImageDraw, ImageFont
    os.makedirs(F, exist_ok=True)
    try:
        font = ImageFont.truetype('arialbd.ttf', 64)
    except OSError:
        font = ImageFont.load_default()
    for s in SLOTS:
        path = '%s/_ph-%s.jpg' % (F, s)
        if os.path.exists(path):
            continue
        W, H = 1536, 1024
        bg = PH[s]
        im = Image.new('RGB', (W, H), bg)
        d = ImageDraw.Draw(im)
        dark = tuple(int(c * 0.72) for c in bg)
        cx, cy, r = int(W * 0.74), H // 2, 300
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=dark)
        label = 'ART: %s' % s
        w = d.textlength(label, font=font)
        d.text((cx - w / 2, cy - 36), label, font=font, fill=(255, 255, 255))
        im.save(path, quality=85)


# ── reading panels: English in every language ─────────────────────────
READ = {
    1: ['Hi! I’m <strong>Mia</strong>. I’m nine. This is <strong>my</strong> cat, '
        'Pepper. She is black and white, and she sleeps on <strong>my</strong> bed.',
        'Leo’s friend asks: <em>“Is that <strong>your</strong> cat, Mia?”</em> '
        '— <em>“Yes! She’s <strong>my</strong> cat.”</em>'],
    2: ['This is Leo, Mia’s brother. Biscuit is <strong>his</strong> dog. Biscuit is a '
        'puppy: <strong>its</strong> ball is red and <strong>its</strong> bed is blue.',
        'Pepper is <strong>her</strong> cat, because Mia is a girl. Biscuit is '
        '<strong>his</strong> dog, because Leo is a boy.'],
    3: ['Mia holds Snowy, the family rabbit. <em>“<strong>This</strong> is '
        '<strong>our</strong> rabbit!”</em> Snowy is close — here, in her arms.',
        'Leo points at a horse in the field. <em>“<strong>That</strong> is '
        'Grandpa’s horse!”</em> The horse is far away — over there.'],
    4: ['Today is the school pet show! Grandpa Joe brings <strong>his</strong> '
        'parrot, Rio. Ella and Sam bring <strong>their</strong> tortoise, Tank.',
        '<em>“Look! That’s <strong>our</strong> teacher, Mr Brown. And this is '
        '<strong>his</strong> goldfish!”</em>'],
    5: ['The family goes camping. <strong>Their</strong> tent is <strong>next to</strong> '
        'the lake, and tall <strong>trees</strong> stand <strong>behind</strong> it.',
        'Leo is the <strong>kid</strong> on the blanket. <strong>His</strong> jumper has '
        'a green <strong>stripe</strong>. Leo is Mum and Dad’s <strong>son</strong>, and '
        'Mia, reading in the tent, is <strong>their</strong> <strong>daughter</strong>.'],
}


def panel(n, eyebrow, pic, side='left', pos='78% 50%'):
    a, b = READ[n]
    return D.panel(eyebrow, E[eyebrow], 'p%dt' % n, E['p%dt' % n],
                   [(None, a), (None, b)], folder=F, pic=PIC[pic], side=side, pos=pos)


def divider(n, pic):
    return D.divider('d%dt' % n, E['d%dt' % n], 'd%dn' % n, E['d%dn' % n],
                     folder=F, pic=PIC[pic])


def teach(title_key, eyebrow_key, items, bg, cols=None):
    """items: (English head, body key, English example). The six-item form,
    so the rule translates and the head and example stay English."""
    return D.teach(eyebrow_key, E[eyebrow_key], title_key, E[title_key],
                   [(None, h, bk, E[bk], None, ex) for h, bk, ex in items],
                   cols=cols, folder=F, bg=PIC[bg])


TEACH_A = [('I → MY', 'tA1', '“This is MY cat.”'),
           ('YOU → YOUR', 'tA2', '“Is that YOUR dog?”'),
           ('WE → OUR', 'tA3', '“OUR rabbit is called Snowy.”'),
           ('THEY → THEIR', 'tA4', '“Ella and Sam love THEIR tortoise.”')]
TEACH_B = [('HE → HIS', 'tB1', '“Leo loves HIS dog.”'),
           ('SHE → HER', 'tB2', '“Mia loves HER cat.”'),
           ('IT → ITS', 'tB3', '“The puppy loves ITS ball.”')]
TEACH_C = [('MY dog · MY cat · MY dogs', 'tC1', '“MY dog, MY cat and MY two fish.”'),
           ('Look at the OWNER', 'tC2', '“Mia has a dog. It is HER dog.”'),
           ('ITS or IT’S?', 'tC3', '“IT’S a puppy. ITS ball is red.”')]
# William's camping-page vocabulary (Innes's notes on "Our Small Traditions",
# 2026-10-14): the words, and his Er / Sie / ihm table.
VOCAB_A = [('tent', 'vA1', '“Their tent is next to the lake.”'),
           ('lake', 'vA2', '“We swim in the lake.”'),
           ('sea', 'vA3', '“The sea is big and salty.”'),
           ('trees', 'vA4', '“There are tall trees behind the lake.”'),
           ('next to', 'vA5', '“The dog is next to Leo.”'),
           ('behind', 'vA6', '“The trees are behind the tent.”')]
VOCAB_B = [('kid / child', 'vB1', '“The kid on the blanket is Leo.”'),
           ('son', 'vB2', '“Leo is their son.”'),
           ('daughter', 'vB3', '“Mia is their daughter.”'),
           ('jumper', 'vB4', '“His jumper is white.”'),
           ('stripe', 'vB5', '“His jumper has a green stripe.”')]
TEACH_SIE = [('Er → HE · ihm → HIM', 'sT1', '“HE is Leo. Biscuit plays with HIM.”'),
             ('Sie → SHE, THEY or YOU', 'sT2', '“SHE is Mia. THEY are twins. Are YOU Mr Brown?”'),
             ('ihr / ihre → HER, THEIR or YOUR', 'sT3', '“It is HER tent. It is THEIR tent.”')]
TEACH_D = [('Deutsch → English', 'tD1', '“Das ist meine Katze.” → “This is my cat.”'),
           ('English → Deutsch', 'tD2', '“This is my cat.” → “Das ist meine Katze.”'),
           ('Check and compare', 'tD3', 'Little mistakes count: check the spelling!')]

# ── multiple choice ────────────────────────────────────────────────────
MC1 = [
    dict(stem='Mia says: “Pepper is ____ cat.”',
         options=['my', 'your', 'our', 'their'], correct=0, why='q1w'),
    dict(stem='Leo asks Mia: “Is Pepper ____ cat?”',
         options=['his', 'my', 'your', 'their'], correct=2, why='q2w'),
    dict(stem='Mum and Dad say: “Snowy is ____ rabbit.”',
         options=['our', 'their', 'my', 'your'], correct=0, why='q3w'),
    dict(stem='Ella and Sam have a tortoise. It is ____ tortoise.',
         options=['our', 'their', 'her', 'your'], correct=1, why='q4w'),
]
MC2 = [
    dict(stem='Leo has a dog. Biscuit is ____ dog.',
         options=['his', 'her', 'its', 'their'], correct=0, why='q5w'),
    dict(stem='Mum has a horse. It is ____ horse.',
         options=['his', 'her', 'its', 'their'], correct=1, why='q6w'),
    dict(stem='The house has a garden. ____ garden is very big.',
         options=['Its', 'It’s', 'His', 'Her'], correct=0, why='q7w'),
]
# THIS / THAT: the situation is in ctx (translated); the sentence stays English.
MC3 = [
    dict(ctx='c8', stem='“____ is our rabbit.”', options=['This', 'That'],
         correct=0, why='q8w'),
    dict(ctx='c9', stem='“____ is Grandpa’s horse.”', options=['This', 'That'],
         correct=1, why='q9w'),
    dict(ctx='c10', stem='“____ is my dog.”', options=['This', 'That'],
         correct=0, why='q10w'),
    dict(ctx='c11', stem='“____ is his goldfish.”', options=['This', 'That'],
         correct=1, why='q11w'),
]
MC4 = [
    dict(ctx='c12', stem='Their tent is ____ the lake.',
         options=['next to', 'behind', 'in', 'under'], correct=0, why='q12w'),
    dict(ctx='c13', stem='The trees are ____ the lake.',
         options=['behind', 'next to', 'in', 'on'], correct=0, why='q13w'),
    dict(stem='Mum and Dad have a girl, Mia. Mia is their ____.',
         options=['daughter', 'son', 'brother', 'cousin'], correct=0, why='q14w'),
]
for group in (MC1, MC2, MC3, MC4):
    D.assert_no_key_is_longest(group)

# ── gap fill, the owner in brackets as on the sheet ───────────────────
GAP1 = [('Hi! ______ name is Mia. <span class="dim">(I)</span>', ['My'], 'g1w'),
        ('Leo asks: “What is ______ name?” <span class="dim">(you)</span>', ['your'], 'g2w'),
        ('Mum says: “______ house has a big garden.” <span class="dim">(we)</span>',
         ['Our'], 'g3w')]
GAP2 = [('Leo loves ______ dog. <span class="dim">(he)</span>', ['his'], 'g4w'),
        ('Mia brushes ______ cat every day. <span class="dim">(she)</span>', ['her'], 'g5w'),
        ('The tree is old. ______ leaves are yellow. <span class="dim">(it)</span>',
         ['Its'], 'g6w')]

# ── sort: the owner decides, never the pet ────────────────────────────
SORT_ITEMS = [('Leo’s dog', 0), ('Mia’s cat', 1), ('Grandpa’s parrot', 0),
              ('Mum’s horse', 1), ('Dad’s fish', 0), ('Ella’s rabbit', 1),
              ('Mr Brown’s goldfish', 0), ('Grandma’s hamster', 1)]

# ── word order, each with a spare subject pronoun that fits nowhere ───
ORDERS = [(['This', 'is', 'our', 'rabbit.'], ['we'], 'o1w'),
          (['That', 'is', 'their', 'tortoise.'], ['they'], 'o2w'),
          (['Her', 'cat', 'is called', 'Pepper.'], ['She'], 'o3w')]

# ── translation: (German, English, more English, more German, why) ────
TR = [
    [('Das ist meine Katze.', 'This is my cat.',
      ['That is my cat.', 'It is my cat.'],
      ['Das hier ist meine Katze.', 'Dies ist meine Katze.'], 'tw1'),
     ('Ist das dein Hund?', 'Is this your dog?',
      ['Is that your dog?', 'Is it your dog?'],
      ['Ist das hier dein Hund?', 'Ist dies dein Hund?'], 'tw2'),
     ('Unser Kaninchen heißt Snowy.', 'Our rabbit is called Snowy.',
      ['Our rabbit’s name is Snowy.', 'Our bunny is called Snowy.'],
      ['Unser Hase heißt Snowy.', 'Unser Häschen heißt Snowy.'], 'tw3')],
    [('Leo liebt seinen Hund.', 'Leo loves his dog.', [],
      ['Leo hat seinen Hund lieb.'], 'tw4'),
     ('Mia spielt mit ihrer Katze.', 'Mia plays with her cat.',
      ['Mia is playing with her cat.'], [], 'tw5'),
     ('Der Hund mag seinen Ball.', 'The dog likes its ball.',
      ['The dog likes his ball.', 'The dog loves its ball.', 'The dog loves his ball.'],
      ['Der Hund liebt seinen Ball.'], 'tw6')],
    [('Ella und Sam lieben ihre Schildkröte.', 'Ella and Sam love their tortoise.',
      ['Ella and Sam love their turtle.'], [], 'tw7'),
     ('Das hier ist dein Fisch.', 'This is your fish.', [],
      ['Das ist dein Fisch.', 'Dies ist dein Fisch.'], 'tw8'),
     ('Das da drüben ist unser Pferd.', 'That is our horse.',
      ['That over there is our horse.', 'That is our horse over there.'],
      ['Das ist unser Pferd.', 'Das da ist unser Pferd.', 'Das dort ist unser Pferd.'],
      'tw9')],
    [('Unser Zelt ist neben dem See.', 'Our tent is next to the lake.',
      ['Our tent is by the lake.'], ['Unser Zelt steht neben dem See.'], 'tw10'),
     ('Der See ist hinter den Bäumen.', 'The lake is behind the trees.', [],
      ['Der See liegt hinter den Bäumen.'], 'tw11'),
     ('Sein Pullover hat einen grünen Streifen.', 'His jumper has a green stripe.',
      ['His sweater has a green stripe.', 'His pullover has a green stripe.'],
      ['Sein Pulli hat einen grünen Streifen.'], 'tw12')],
    # SIE IST can only be SHE (formal Sie takes SIND); IHRE is HER or THEIR.
    [('Sie ist ihre Tochter.', 'She is their daughter.', ['She is her daughter.'],
      [], 'tw13'),
     ('Biscuit spielt mit ihm.', 'Biscuit plays with him.',
      ['Biscuit is playing with him.'], [], 'tw14'),
     ('Ist das Ihr Zelt, Herr Brown?', 'Is this your tent, Mr Brown?',
      ['Is that your tent, Mr Brown?', 'Is it your tent, Mr Brown?'],
      ['Ist das Ihr Zelt, Mr Brown?', 'Ist dies Ihr Zelt, Herr Brown?'], 'tw15')],
]


def _expand(sentences, german):
    """Every spelling a right answer might be typed in. The engine already
    ignores case, spacing and curly-vs-straight apostrophes."""
    out = []

    def add(s):
        if s not in out:
            out.append(s)
    for s in sentences:
        forms = [s]
        if not german:
            for a, b in (('That is', 'That’s'), ('It is', 'It’s')):
                forms += [f.replace(a, b) for f in forms if a in f and b not in s]
        else:
            for a, b in (('ä', 'ae'), ('ö', 'oe'), ('ü', 'ue'), ('ß', 'ss')):
                forms += [f.replace(a, b) for f in forms if a in f]
        for f in forms:
            add(f)
            add(f.rstrip('.?!'))
    assert not any('|' in s for s in out)
    return '|'.join(D.esc(s) for s in out)


TR_TOTAL = sum(len(r) for r in TR)


def translate(n, rows, total, pic):
    body = []
    for de, en, more_en, more_de, why in rows:
        ans_en = _expand([en] + more_en, german=False)
        ans_de = _expand([de] + more_de, german=True)
        body.append('''<div class="card gap-row tr-row" data-src-de="%s" data-src-en="%s" style="padding:12px 18px">
          <p class="q-stem" style="margin-bottom:0;font-size:22px"><span class="tr-src">%s</span> <span class="tr-arrow" aria-hidden="true">→</span> <input class="gap tr-in" data-answer="%s" data-ans-en="%s" data-ans-de="%s" aria-label="translation" autocomplete="off" spellcheck="false"></p>
          <p class="feedback" data-explain="%s"></p>
        </div>''' % (D.esc(de), D.esc(en), de, ans_en, ans_en, ans_de, why))
    return '''
    <section class="slide" data-type="gap" data-translate%s>
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="e4">%s</span> &middot; %d / %d</div>
        <h2 class="slide-title" data-i18n="trT">%s</h2>
      </div>
        <div class="tr-toggle" role="group" aria-label="Translation direction">
          <button type="button" class="tr-dir is-on" data-dir="de-en" aria-pressed="true">Deutsch → English</button>
          <button type="button" class="tr-dir" data-dir="en-de" aria-pressed="false">English → Deutsch</button>
        </div>
      </div>
      <div class="slide-body">
        %s
        <div style="margin-top:10px">
          <button class="btn" data-action="check" data-i18n="btnCheck">Check</button>
        </div>
      </div>
    </section>
''' % (D._bg(F, PIC[pic]), E['e4'], n, total, E['trT'], "\n        ".join(body))


# One block for every translate slide: the switch is global, so a learner who
# picks English → Deutsch keeps it on the next slide. A checked slide is
# locked, because swapping the answer set after marking would rewrite history.
TRANSLATE_KIT = '''
    <style>
      .tr-toggle { display:inline-flex; flex:none; gap:0; margin:0; border:2px solid var(--accent);
                   border-radius:999px; overflow:hidden; }
      .tr-dir { font:700 17px/1 'DM Sans',sans-serif; padding:10px 20px; border:0; cursor:pointer;
                background:transparent; color:var(--accent); }
      .tr-dir.is-on { background:var(--accent); color:var(--void); }
      .tr-dir:disabled { cursor:default; opacity:.55; }
      .tr-row .tr-src { font-weight:700; }
      .tr-row .tr-arrow { color:var(--accent); font-weight:700; }
      .tr-row input.tr-in { width:470px; font-size:21px; }
    </style>
    <script>
    (function () {
      var dir = 'de-en';
      function apply(slide) {
        if (slide.querySelector('.tr-in:disabled')) return;   // already marked
        slide.querySelectorAll('.tr-dir').forEach(function (b) {
          var on = b.dataset.dir === dir;
          b.classList.toggle('is-on', on);
          b.setAttribute('aria-pressed', on ? 'true' : 'false');
        });
        slide.querySelectorAll('.tr-row').forEach(function (r) {
          var src = r.querySelector('.tr-src'), g = r.querySelector('.tr-in');
          var from = dir === 'de-en' ? 'de' : 'en', to = dir === 'de-en' ? 'en' : 'de';
          if (src.textContent !== r.getAttribute('data-src-' + from)) g.value = '';
          src.textContent = r.getAttribute('data-src-' + from);
          src.lang = from;
          g.lang = to;
          g.dataset.answer = g.getAttribute('data-ans-' + to);
        });
      }
      document.addEventListener('click', function (e) {
        var b = e.target.closest('.tr-dir');
        if (b && !b.disabled) {
          dir = b.dataset.dir;
          document.querySelectorAll('.slide[data-translate]').forEach(apply);
          return;
        }
        var c = e.target.closest('.slide[data-translate] [data-action="check"]');
        if (c) c.closest('.slide').querySelectorAll('.tr-dir')
                .forEach(function (x) { x.disabled = true; });
      }, true);
    })();
    </script>
'''


def cover(part):
    k = '' if part == 1 else '2'
    return D.cover(D.logo_from(TPL), E['coverTitle' + k], E['coverSub' + k],
                   [('Level', E['chipLevel']), ('Focus', E['chipFocus' + k]),
                    ('Count', E['chipCount' + k])])


def ending(part, pic):
    k = '' if part == 1 else '2'
    # Not in teaching order: the BANK gate reads activation chips as a word
    # bank, and teaching order is the gap order.
    chips = (['their', 'this', 'her', 'my', 'that', 'its', 'your', 'our', 'his']
             if part == 1 else
             ['behind', 'their', 'lake', 'that', 'tent', 'next to', 'this', 'our', 'his'])
    return [
        D.results(folder=F, bg=PIC[pic]),
        D.activate(E['actTitle'], E['actUse'], chips, 'Speaking', E['actSpeakBrief' + k],
                   [E['actSpeak1' + k], E['actSpeak2' + k], E['actSpeak3' + k]],
                   E['actWriteKind'], E['actWriteBrief' + k], E['actPlaceholder' + k],
                   folder=F, bg=PIC[pic]),
    ]


def part1():
    return [
        cover(1),

        # ── stage 1 · MY, YOUR, OUR, THEIR ─────────────────────────────
        divider(1, 'mia'),
        panel(1, 'e1', 'mia'),
        teach('tAt', 'eR', TEACH_A, 'mia', cols='1fr 1fr'),
    ] + [
        D.mc(i + 1, len(MC1), q, 'e1', E['e1'], 'mcT', E['mcT'], folder=F, bg=PIC['mia'])
        for i, q in enumerate(MC1)
    ] + [
        D.gap(1, 1, GAP1, None, 'e1', E['e1'], 'gapT', E['gapT'], folder=F,
              bg=PIC['mia'], hint=E['gapHint'], hint_key='gapHint', width=130, size=24),

        # ── stage 2 · HIS, HER, ITS ────────────────────────────────────
        divider(2, 'leo'),
        panel(2, 'e2', 'leo', side='right'),
        teach('tBt', 'eR', TEACH_B, 'leo'),
        teach('tCt', 'eR', TEACH_C, 'leo'),
        D.match([('I', 'my'), ('you', 'your'), ('he', 'his'), ('she', 'her'),
                 ('it', 'its'), ('we', 'our'), ('they', 'their')],
                'e2', E['e2'], 'matchT', E['matchT'], 'matchHint', E['matchHint'],
                'matchW', folder=F, bg=PIC['leo']),
        D.sort_slide([E['binA'], E['binB']], SORT_ITEMS, 'e2', E['e2'],
                     'sortT', E['sortT'], 'sortHint', E['sortHint'], 'sortWhy',
                     bin_keys=['binA', 'binB'], folder=F, bg=PIC['leo']),
    ] + [
        D.mc(i + 1, len(MC2), q, 'e2', E['e2'], 'mcT', E['mcT'], folder=F, bg=PIC['leo'])
        for i, q in enumerate(MC2)
    ] + [
        D.gap(1, 1, GAP2, None, 'e2', E['e2'], 'gapT', E['gapT'], folder=F,
              bg=PIC['leo'], hint=E['gapHint'], hint_key='gapHint', width=130, size=24),

        # ── stage 3 · translate: the first two sets of rows ────────────
        divider(6, 'hero'),
        teach('tDt', 'e4', TEACH_D, 'hero'),
        TRANSLATE_KIT,
    ] + [
        translate(i + 1, r, 2, 'hero') for i, r in enumerate(TR[:2])
    ] + ending(1, 'hero')


def part2():
    return [
        cover(2),

        # ── stage 1 · THIS and THAT ────────────────────────────────────
        divider(3, 'near-far'),
        panel(3, 'e3', 'near-far'),
    ] + [
        D.mc(i + 1, len(MC3), q, 'e3', E['e3'], 'mc3T', E['mc3T'],
             folder=F, bg=PIC['near-far'], ctx=E[q['ctx']], ctx_key=q['ctx'])
        for i, q in enumerate(MC3)
    ] + [
        D.order(items, 'e3', E['e3'], 'orderT', E['orderT'], 'orderHint',
                E['orderHint'], why, folder=F, bg=PIC['near-far'], decoys=dec)
        for items, dec, why in ORDERS
    ] + [
        # ── stage 2 · camping at the lake: William's vocabulary ────────
        divider(5, 'lake'),
        panel(5, 'e5', 'lake'),
        teach('vAt', 'eV', VOCAB_A, 'lake', cols='1fr 1fr 1fr'),
        teach('vBt', 'eV', VOCAB_B, 'lake', cols='1fr 1fr 1fr'),
        teach('sTt', 'eR', TEACH_SIE, 'lake'),
        D.match([('lake', 'der See'), ('sea', 'das Meer'), ('tent', 'das Zelt'),
                 ('trees', 'die Bäume'), ('jumper', 'der Pullover'),
                 ('stripe', 'der Streifen'), ('daughter', 'die Tochter')],
                'e5', E['e5'], 'vmatchT', E['vmatchT'], 'vmatchHint', E['vmatchHint'],
                'vmatchW', folder=F, bg=PIC['lake']),
    ] + [
        D.mc(i + 1, len(MC4), q, 'e5', E['e5'], 'mcT', E['mcT'], folder=F,
             bg=PIC['lake'], ctx=E[q['ctx']] if 'ctx' in q else None,
             ctx_key=q.get('ctx'))
        for i, q in enumerate(MC4)
    ] + [
        # ── stage 3 · the pet show, then translate ─────────────────────
        divider(4, 'pet-show'),
        panel(4, 'e4', 'pet-show', side='right'),
        teach('tDt', 'e4', TEACH_D, 'pet-show'),
        TRANSLATE_KIT,
    ] + [
        translate(i + 1, r, 3, 'pet-show') for i, r in enumerate(TR[2:])
    ] + ending(2, 'lake')


def build(part):
    P = PARTS[part]
    out = P['live'] if ready(part) else '_' + P['live']    # underscore = gitignored
    slides = "".join(part1() if part == 1 else part2())
    D.assemble(TPL, out, slides, palette(part), P['title'], I, langs=('en', 'de', 'es'))
    print('wrote %s — %d slides%s' % (
        out, slides.count('<section class="slide'),
        '' if ready(part) else '  (PREVIEW: plates missing, see docs/ARTWORK-possessive-adj.md)'))


if __name__ == '__main__':
    if not (ready(1) and ready(2)):
        placeholders()
    build(1)
    build(2)
