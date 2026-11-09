# -*- coding: utf-8 -*-
"""Layout drafts for sea charts 7-12, for ChatGPT to repaint.

    py lesson-template/build/sea_layouts_3.py

The rest of the list Innes asked about on 2026-11-08 ("what would these look
like?"): register, inversion, British/American, question tags, probability
and phrasal verbs. Same method as sea_layouts_2.py: an edit target that fixes
every word and harbour dot, painted by ChatGPT with the Gerundia chart as the
style reference.
"""
import os
from PIL import ImageDraw
from sea_layouts_2 import W, H, OUT, INK, SEA, SEA_INK, base, text, dot, compass

LAND, SAND, GREEN, ROCK = (201, 176, 122), (217, 199, 154), (183, 207, 155), (150, 140, 125)
WHITE = (245, 245, 240)


def save(im, name):
    im.save(os.path.join(OUT, name + '.png'))


# ── 7. the heights of register ─────────────────────────────────────────
TRAILS = [('get', 'obtain'), ('buy', 'purchase'), ('need', 'require'), ('help', 'assist'),
          ('start', 'commence'), ('ask', 'enquire'), ('enough', 'sufficient'), ('find out', 'discover')]


def register():
    im, d = base()
    cx, cy = 768, 560
    for i, (rx, ry, c) in enumerate([(700, 420, (183, 207, 155)), (520, 310, (201, 190, 140)),
                                     (340, 205, (190, 160, 110)), (160, 100, (160, 130, 95))]):
        d.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=c, outline=INK, width=1)
    text(d, (cx, cy + 8), 'THE SUMMIT', 22, 'b', WHITE)
    for label, y in (('EVERYDAY · chat, texts', cy + 390), ('NEUTRAL · emails', cy + 282),
                     ('FORMAL · reports, letters', cy + 178)):
        text(d, (cx, y), label, 19, 'i')
    import math
    for i, (low, high) in enumerate(TRAILS):
        a = math.pi * (0.08 + 0.84 * i / (len(TRAILS) - 1))
        lx, ly = cx - 600 * math.cos(a), cy - 360 * math.sin(a) * (-1 if i % 2 else 1) * 0 + cy * 0
        # trails fan round the mountain: low dot near the shore, high dot near the top
        lx, ly = cx + 610 * math.cos(a + math.pi), cy + 360 * math.sin(a + math.pi) * (1 if i < 4 else -1)
        hx, hy = cx + 250 * math.cos(a + math.pi), cy + 140 * math.sin(a + math.pi) * (1 if i < 4 else -1)
        d.line((lx, ly, hx, hy), fill=(110, 80, 50), width=3)
        dot(d, lx, ly, low)
        dot(d, hx, hy, high)
    text(d, (cx, 62), 'THE HEIGHTS OF REGISTER', 42, 'b', SEA_INK)
    text(d, (cx, 100), 'the higher you climb, the more formal the word', 22, 'i', SEA_INK)
    text(d, (240, 985), 'phrasal verbs live in the valleys', 19, 'i', SEA_INK)
    compass(d, 1400, 900, 40)
    save(im, 'heights-of-register')


# ── 8. the inversion maelstrom ─────────────────────────────────────────
SIGNALS = ['Never', 'Rarely', 'Seldom', 'Not only', 'No sooner', 'Hardly', 'Little',
           'Only then', 'Under no circumstances']


def maelstrom():
    im, d = base()
    import math
    cx, cy = 768, 560
    for r in range(40, 300, 26):
        d.arc((cx - r, cy - r * .8, cx + r, cy + r * .8), 20, 330, fill=SEA_INK, width=2)
    for i, w in enumerate(SIGNALS):
        a = -math.pi / 2 + 2 * math.pi * i / len(SIGNALS)
        x, y = cx + 470 * math.cos(a), cy + 330 * math.sin(a)
        rx = max(70, d.textlength(w, font=__import__('sea_layouts_2').font('b', 19)) / 2 + 22)
        d.ellipse((x - rx, y - 32, x + rx, y + 32), fill=ROCK)
        dot(d, x, y + 6, w)
    text(d, (cx, 70), 'THE INVERSION MAELSTROM', 42, 'b', SEA_INK)
    text(d, (cx, 108), 'sail past these rocks and the auxiliary spins in front of the subject', 21, 'i', SEA_INK)
    text(d, (230, 930), 'IN: I have never seen', 21, 'b', SEA_INK, 'lm')
    text(d, (230, 960), 'OUT: Never have I seen', 21, 'b', SEA_INK, 'lm')
    text(d, (1300, 930), 'no auxiliary? do appears:', 19, 'i', SEA_INK)
    text(d, (1300, 960), 'Rarely do we sail at night.', 19, 'i', SEA_INK)
    compass(d, 1400, 190, 40)
    save(im, 'inversion-maelstrom')


# ── 9. the Atlantic ────────────────────────────────────────────────────
PAIRS = [('elevator', 'lift'), ('apartment', 'flat'), ('fall', 'autumn'), ('vacation', 'holiday'),
         ('truck', 'lorry'), ('cookie', 'biscuit'), ('the movies', 'the cinema'), ('gotten', 'got')]


def atlantic():
    im, d = base()
    d.polygon([(24, 24), (330, 24), (290, 260), (360, 520), (300, 800), (340, H - 24), (24, H - 24)], fill=GREEN)
    d.polygon([(W - 24, 24), (1200, 24), (1250, 300), (1180, 520), (1240, 760), (1200, H - 24), (W - 24, H - 24)], fill=SAND)
    text(d, (150, 960), 'AMERICA', 40, 'b')
    text(d, (1390, 960), 'BRITAIN', 40, 'b')
    for i, (us, uk) in enumerate(PAIRS):
        y = 150 + i * 92
        dot(d, 170, y, us.title() + ' Harbour' if ' ' not in us else us.title().replace('The ', 'The ') + ' Harbour')
        dot(d, 1370, y, uk.title() + ' Harbour' if ' ' not in uk else uk.title() + ' Harbour')
    d.ellipse((620, 440, 920, 600), fill=SAND)
    text(d, (770, 490), 'THE SHALLOWS', 22, 'b')
    text(d, (770, 520), 'both shores say it', 17, 'i')
    text(d, (770, 548), 'do you have · learned · toward(s)', 17, 'i')
    d.polygon([(560, 760), (760, 740), (800, 800), (590, 820)], fill=SAND)
    d.line((585, 760, 585, 705), fill=INK, width=3)
    d.polygon([(585, 705), (635, 720), (585, 735)], fill=(216, 90, 48))
    text(d, (770, 860), 'THE FALSE CAPE', 22, 'b', SEA_INK)
    text(d, (770, 888), 'same word, other meaning: pants · chips · first floor', 18, 'i', SEA_INK)
    text(d, (770, 70), 'THE ATLANTIC', 44, 'b', SEA_INK)
    text(d, (770, 108), 'two shores, one language', 22, 'i', SEA_INK)
    compass(d, 770, 260, 44)
    save(im, 'the-atlantic')


# ── 10. the return voyage (question tags) ──────────────────────────────
ROUTES = [('It’s cold,', 'isn’t it?', True), ('You can swim,', 'can’t you?', True),
          ('She went home,', 'didn’t she?', True), ('It isn’t far,', 'is it?', False),
          ('They haven’t left,', 'have they?', False)]
STACKS = [('I am late,', 'aren’t I?'), ('Let’s go,', 'shall we?'),
          ('Close the hatch,', 'will you?'), ('Nobody came,', 'did they?')]


def return_voyage():
    im, d = base()
    d.rectangle((24, 500, W - 24, 524), fill=ROCK)                     # the turning reef
    text(d, (130, 470), 'POSITIVE WATERS', 22, 'b', SEA_INK, 'lm')
    text(d, (130, 560), 'NEGATIVE WATERS', 22, 'b', SEA_INK, 'lm')
    text(d, (1250, 512), 'THE TURNING REEF', 19, 'b', WHITE)
    for i, (said, tag, pos) in enumerate(ROUTES):
        x = 200 + i * 200
        y1, y2 = (330, 690) if pos else (690, 330)
        d.arc((x - 60, 350, x + 60, 670), 280, 80, fill=SEA_INK, width=2)
        dot(d, x - 4, y1, said)
        dot(d, x - 4, y2, tag, below=True)
    d.rectangle((1180, 610, W - 40, 980), fill=(150, 175, 185))
    text(d, (1345, 640), 'THE LONE STACKS', 22, 'b', SEA_INK)
    for i, (said, tag) in enumerate(STACKS):
        y = 700 + i * 70
        dot(d, 1210, y)
        text(d, (1230, y), '%s %s' % (said, tag), 19, 'b', INK, 'lm')
    text(d, (W // 2, 70), 'THE RETURN VOYAGE', 44, 'b', SEA_INK)
    text(d, (W // 2, 108), 'out on a positive, home on a negative, and back again', 22, 'i', SEA_INK)
    compass(d, 1400, 220, 40)
    save(im, 'return-voyage')


# ── 11. the grammar forecast (probability) ─────────────────────────────
AREAS = [('BOUND', 'is bound to', '100'), ('WILL', 'will · is sure to', '95'),
         ('LIKELY', 'is likely to · will probably', '75'), ('MAYBE', 'may · might · could', '50'),
         ('UNLIKELY', 'is unlikely to · probably won’t', '25'), ('WON’T', 'won’t · definitely won’t', '0')]


def forecast():
    im, d = base()
    d.polygon([(24, 24), (300, 24), (260, 300), (320, 600), (250, H - 24), (24, H - 24)], fill=GREEN)
    text(d, (150, 960), 'THE COAST', 26, 'b')
    for i, (area, words, pc) in enumerate(AREAS):
        col, row = i % 3, i // 3
        x0, y0 = 360 + col * 380, 180 + row * 400
        d.rectangle((x0, y0, x0 + 360, y0 + 380), outline=SEA_INK, width=2)
        dot(d, x0 + 180, y0 + 170)
        text(d, (x0 + 180, y0 + 120), area, 28, 'b', SEA_INK)
        text(d, (x0 + 180, y0 + 215), words, 19, 'i', SEA_INK)
        text(d, (x0 + 180, y0 + 250), 'about %s%%' % pc, 18, 'r', SEA_INK)
    text(d, (W // 2 + 130, 70), 'THE GRAMMAR FORECAST', 42, 'b', SEA_INK)
    text(d, (W // 2 + 130, 108), 'how sure are we? read the sea area', 22, 'i', SEA_INK)
    text(d, (W // 2 + 130, 1000 - 12), 'Rain is likely to reach the coast by evening.', 19, 'i', SEA_INK)
    compass(d, 150, 140, 40)
    save(im, 'grammar-forecast')


# ── 12. the particle ferries (phrasal verbs) ───────────────────────────
LINES = [('UP', 'finish, or more', (216, 90, 48)), ('OUT', 'to the end, or outside', (29, 158, 117)),
         ('OFF', 'away, or stop', (83, 74, 183)), ('ON', 'continue, or connect', (186, 117, 23)),
         ('DOWN', 'less, or on paper', (24, 95, 165))]
HUBS = ['GET', 'TAKE', 'PUT', 'TURN']


def ferries():
    im, d = base()
    d.rectangle((24, 24, W - 24, 150), fill=SAND)
    d.rectangle((24, H - 120, W - 24, H - 24), fill=SAND)
    ys = [250 + i * 130 for i in range(5)]
    xs = [520 + i * 250 for i in range(4)]
    for x, hub in zip(xs, HUBS):
        d.line((x, 200, x, ys[-1] + 50), fill=(136, 135, 128), width=6)
        text(d, (x, 182), hub, 28, 'b', SEA_INK)
    for (p, sense, col), y in zip(LINES, ys):
        d.line((250, y, 1400, y), fill=col, width=9)
        text(d, (90, y - 14), p, 28, 'b', col, 'lm')
        text(d, (90, y + 16), sense, 16, 'i', SEA_INK, 'lm')
        for x, hub in zip(xs, HUBS):
            d.ellipse((x - 12, y - 12, x + 12, y + 12), fill=WHITE, outline=INK, width=3)
            text(d, (x + 18, y - 22), '%s %s' % (hub.lower(), p.lower()), 17, 'b', INK, 'lm')
    text(d, (W // 2, 70), 'THE PARTICLE FERRIES', 42, 'b')
    text(d, (W // 2, 108), 'one line for each particle · change at the big verbs', 22, 'i')
    text(d, (W // 2, H - 72), 'the same verb on a new line is a new meaning: take off · take on · take down', 20, 'i')
    compass(d, 1420, 900, 36)
    save(im, 'particle-ferries')


if __name__ == '__main__':
    for f in (register, maelstrom, atlantic, return_voyage, forecast, ferries):
        f()
    print('wrote six layouts to', OUT)
