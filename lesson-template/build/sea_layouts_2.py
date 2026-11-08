# -*- coding: utf-8 -*-
"""Layout drafts for the next three grammar sea charts, for ChatGPT to repaint.

    py lesson-template/build/sea_layouts_2.py

Writes docs/sea-charts/adjective-canal.png, prefix-archipelago.png and
frequency-soundings.png (1536 x 1024). They are EDIT TARGETS, not art: they
fix the geography, the harbour dots and every word, so the painter cannot
invent places or misspell them. The painting comes back from ChatGPT with
the Gerundia chart (sailing-the-seas-of-grammar/hero.jpg) as its style
reference, the way Countania and Regularia were made (docs/GRAMMAR-MAPS-PLAN.md
section 5). The prompts were given to Innes in chat on 2026-11-08 and are
recorded in docs/HANDOFF.md.

Innes, 2026-11-08, on whether my own high-end art is still "shoddy": it is a
layout, not a painting. That is its job here.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1536, 1024
OUT = 'docs/sea-charts'
os.makedirs(OUT, exist_ok=True)
F = 'C:/Windows/Fonts/'
PARCH, SEA, INK = (239, 227, 198), (169, 203, 214), (40, 30, 18)
SEA_INK = (20, 52, 61)


def font(kind, size):
    return ImageFont.truetype(F + {'r': 'georgia.ttf', 'b': 'georgiab.ttf', 'i': 'georgiai.ttf'}[kind], size)


def base():
    im = Image.new('RGB', (W, H), SEA)
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W - 1, H - 1), outline=PARCH, width=22)
    d.rectangle((22, 22, W - 23, H - 23), outline=INK, width=2)
    return im, d


def text(d, xy, s, size=20, kind='r', fill=INK, anchor='mm'):
    d.text(xy, s, font=font(kind, size), fill=fill, anchor=anchor)


def dot(d, x, y, name=None, fill=INK, below=False):
    d.ellipse((x - 6, y - 6, x + 6, y + 6), fill=(25, 20, 15))
    if name:
        text(d, (x, y + 22 if below else y - 20), name, 19, 'b', fill)


def compass(d, x, y, r=46):
    d.ellipse((x - r, y - r, x + r, y + r), outline=INK, width=2)
    d.polygon([(x, y - r - 14), (x + 9, y), (x, y + r + 14), (x - 9, y)], outline=INK, fill=(214, 190, 140))
    d.polygon([(x - r - 14, y), (x, y - 9), (x + r + 14, y), (x, y + 9)], outline=INK, fill=(120, 150, 170))


# ── 1. the adjective canal ─────────────────────────────────────────────
LOCKS = [('OPINION', 'lovely'), ('SIZE', 'little'), ('AGE', 'old'), ('SHAPE', 'round'),
         ('COLOUR', 'red'), ('ORIGIN', 'French'), ('MATERIAL', 'wooden'), ('PURPOSE', 'fishing')]


def adjective_canal():
    im, d = base()
    green = (183, 207, 155)
    d.rectangle((150, 24, W - 24, H - 24), fill=green)                 # the meadows
    d.polygon([(24, 24), (210, 24), (170, 300), (200, 520), (160, 760), (215, H - 24), (24, H - 24)], fill=SEA)
    d.rectangle((150, 470, 1330, 560), fill=SEA)                       # the canal
    d.ellipse((1300, 380, 1500, 650), fill=SEA)                        # Noun Harbour basin
    d.polygon([(330, 470), (370, 470), (420, 300), (520, 250), (520, 290), (440, 330)], fill=SEA)   # the comma cut
    xs = [250 + i * 140 for i in range(8)]
    for (cat, word), x in zip(LOCKS, xs):
        d.rectangle((x - 6, 462, x + 6, 568), fill=(91, 58, 30))       # the lock gates
        text(d, (x, 420), cat, 19, 'b')
        dot(d, x, 600)
        text(d, (x, 632), word, 22, 'i')
    dot(d, 1400, 515, 'NOUN HARBOUR')
    text(d, (1400, 560), 'boat', 24, 'i')
    text(d, (W // 2, 90), 'THE ADJECTIVE CANAL', 46, 'b')
    text(d, (W // 2, 140), 'eight locks · one way only', 26, 'i')
    text(d, (560, 225), 'THE COMMA CUT', 22, 'b')
    text(d, (560, 255), 'two from one lock: a lovely, quiet evening', 19, 'i')
    text(d, (W // 2, 760), 'a lovely little old round red French wooden fishing boat', 30, 'i')
    text(d, (W // 2, 805), 'opinion before fact · the purpose sits right next to the noun', 21)
    compass(d, 1380, 180)
    im.save(os.path.join(OUT, 'adjective-canal.png'))


# ── 2. the prefix archipelago ──────────────────────────────────────────
MAINLAND = [('Happy Harbour', 240, 200), ('Kind Cove', 330, 330), ('Fair Point', 210, 460),
            ('Able Head', 320, 590), ('Usual Sands', 220, 720)]
ISLES = [
    ('IM- ISLE', 'before p and m', (720, 250), [('Possible Point', -70, -30), ('Patient Cove', 60, 10), ('Mature Head', -40, 55)]),
    ('IL- ISLE', 'before l', (1100, 250), [('Legal Point', -50, -10), ('Logical Cove', 50, 40)]),
    ('IR- ISLE', 'before r', (1360, 440), [('Regular Rock', -40, -20), ('Responsible Head', 0, 45)]),
    ('IN- ISLE', 'for the rest', (960, 500), [('Correct Cove', -90, -15), ('Visible Point', 70, -5), ('Expensive Ness', 0, 50)]),
    ('DIS- ISLE', 'not, or the opposite', (700, 770), [('Like Harbour', -70, -20), ('Agree Point', 70, 0), ('Honest Head', -10, 50)]),
    ('MIS- ISLE', 'wrongly', (1250, 770), [('Understand Sound', -40, -25), ('Spell Point', 60, 25), ('Lead Head', -60, 50)]),
]


def prefix_archipelago():
    im, d = base()
    sand, land = (217, 199, 154), (201, 176, 122)
    d.polygon([(24, 24), (470, 24), (430, 200), (480, 380), (420, 560), (470, 760), (400, 900), (24, H - 24)], fill=land)
    text(d, (180, 880), 'UN-', 64, 'b')
    text(d, (190, 935), 'the mainland · most words', 24, 'i')
    for name, x, y in MAINLAND:
        dot(d, x, y, name)
    for title, sub, (cx, cy), harbours in ISLES:
        d.ellipse((cx - 150, cy - 85, cx + 150, cy + 95), fill=sand)
        text(d, (cx, cy - 112), title, 26, 'b', SEA_INK)
        text(d, (cx, cy - 88), sub, 18, 'i', SEA_INK)
        for name, dx, dy in harbours:
            dot(d, cx + dx, cy + dy + 12, name)
    d.polygon([(900, 905), (1060, 890), (1090, 945), (930, 965)], fill=land)        # the False Cape
    d.line((925, 905, 925, 850), fill=INK, width=3)
    d.polygon([(925, 850), (975, 865), (925, 880)], fill=(216, 90, 48))
    text(d, (1290, 920), 'THE FALSE CAPE', 24, 'b', SEA_INK)
    text(d, (1290, 950), 'inflammable means flammable', 19, 'i', SEA_INK)
    text(d, (980, 75), 'THE PREFIX ARCHIPELAGO', 42, 'b', SEA_INK)
    text(d, (980, 112), 'not, the opposite, or wrongly: which island?', 22, 'i', SEA_INK)
    compass(d, 580, 940, 40)
    im.save(os.path.join(OUT, 'prefix-archipelago.png'))


# ── 3. soundings of frequency ──────────────────────────────────────────
BANDS = [('never', 0), ('hardly ever', 5), ('rarely', 10), ('occasionally', 30),
         ('sometimes', 50), ('often', 70), ('usually', 80), ('always', 100)]


def frequency_soundings():
    im, d = base()
    shore = (217, 199, 154)
    d.polygon([(24, 24), (W - 24, 24), (W - 24, 150), (1100, 175), (700, 150), (300, 185), (24, 160)], fill=shore)
    top, step = 200, 96
    for i in range(len(BANDS) - 1):
        shade = tuple(int(c * (1 - .075 * i)) for c in SEA)
        d.rectangle((24, top + i * step, W - 24, top + (i + 1) * step), fill=shade)
    word, depth = BANDS[0]
    dot(d, 260, 120)
    text(d, (260, 92), 'Never Point', 21, 'b')
    text(d, (420, 120), '0', 24, 'b', anchor='lm')
    for i, (word, depth) in enumerate(BANDS[1:]):
        y = top + i * step + step // 2
        ink = INK if i < 4 else (245, 245, 240)
        dot(d, 260, y)
        text(d, (290, y), word, 26, 'b', ink, 'lm')
        text(d, (620, y), str(depth), 24, 'i', ink, 'lm')
    text(d, (W // 2, 60), 'SOUNDINGS OF FREQUENCY', 42, 'b')
    text(d, (W // 2, 100), 'how often? read the depth', 22, 'i')
    text(d, (230, 990), 'depths are rough percentages', 18, 'i', (245, 245, 240), 'lm')
    # the anchor buoy: where the adverb goes
    d.ellipse((960, 320, 1020, 380), fill=(216, 90, 48))
    text(d, (1260, 300), 'THE ANCHOR', 26, 'b')
    text(d, (1260, 340), 'before the main verb: we often sail', 20, 'i')
    text(d, (1260, 370), 'after be: she is often late', 20, 'i')
    # the current: sometimes / usually / often can move to the front
    d.line((1400, 640, 1000, 640), fill=SEA_INK, width=3)
    d.polygon([(1000, 630), (980, 640), (1000, 650)], fill=SEA_INK)
    text(d, (1200, 610), 'SOMETIMES SAILS TO THE FRONT', 21, 'b', (245, 245, 240))
    text(d, (1200, 675), 'Sometimes we sail at night.', 20, 'i', (245, 245, 240))
    compass(d, 1380, 900, 40)
    im.save(os.path.join(OUT, 'frequency-soundings.png'))


if __name__ == '__main__':
    adjective_canal()
    prefix_archipelago()
    frequency_soundings()
    print('wrote', ', '.join(os.path.join(OUT, n) for n in
                             ('adjective-canal.png', 'prefix-archipelago.png', 'frequency-soundings.png')))
