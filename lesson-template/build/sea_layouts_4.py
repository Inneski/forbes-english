# -*- coding: utf-8 -*-
"""Layout drafts for sea charts 13-18, for ChatGPT to repaint.

    PYTHONPATH=lesson-template/build py lesson-template/build/sea_layouts_4.py

Innes, 2026-11-13: "do you have another handoff for chat gpt? ... it says on
the webpage that more are coming". The grammar page's chart table
(tools/grammar_maps.py PLANNED) lists twelve charts; these are the first six
in docs/GRAMMAR-MAPS-PLAN.md's order: the Atlas of THE, Finished Time & Open
Time, the Conditional Quadrants, the Harbour of Scale (in/on/at), the Voyage
(prepositions of movement) and the -ER Coast & the MORE Coast. Same method
as sea_layouts_2.py and _3.py: an EDIT TARGET that fixes the geography,
every harbour dot and every word, painted by ChatGPT with the Gerundia chart
as the style reference. Every dot here is a stop the lesson will make
clickable, so the brief pins them.
"""
import os
from PIL import ImageDraw
from sea_layouts_2 import W, H, OUT, INK, SEA, SEA_INK, base, text, dot, compass, font
from sea_tense import T          # a tense is always painted in its Sherpa colour

LAND, SAND, GREEN, ROCK = (201, 176, 122), (217, 199, 154), (183, 207, 155), (150, 140, 125)
WHITE = (245, 245, 240)


def save(im, name):
    im.save(os.path.join(OUT, name + '.png'))


def harbour(d, x, y, name, note=None, anchor='mm'):
    """A dot, its name above, a small note below."""
    dot(d, x, y)
    text(d, (x, y - 20), name, 19, 'b', INK, anchor)
    if note:
        text(d, (x, y + 21), note, 15, 'i', INK, anchor)


# ── 13. the Atlas of THE ───────────────────────────────────────────────
THE_LAND = [('the Atlantic', 'ocean'), ('the Mediterranean', 'sea'), ('the Thames', 'river'),
            ('the Sahara', 'desert'), ('the Alps', 'mountain range'), ('the Canaries', 'island group'),
            ('the Netherlands', 'plural country'), ('the USA', 'union of states')]
NO_THE = [('Europe', 'continent'), ('France', 'country'), ('Paris', 'city'), ('Lake Como', 'lake'),
          ('Mount Everest', 'single mountain'), ('Malta', 'single island'), ('Oxford Street', 'street'),
          ('Trafalgar Square', 'square')]


def atlas():
    im, d = base()
    d.polygon([(24, 140), (560, 140), (600, 400), (540, 640), (590, H - 24), (24, H - 24)], fill=GREEN)
    d.polygon([(W - 24, 140), (976, 140), (936, 380), (1000, 620), (950, H - 24), (W - 24, H - 24)], fill=SAND)
    text(d, (290, 172), 'THE-LAND', 30, 'b')
    text(d, (1246, 172), 'NO-THE-LAND', 30, 'b')
    for i, ((n1, c1), (n2, c2)) in enumerate(zip(THE_LAND, NO_THE)):
        y = 250 + i * 92
        harbour(d, 290, y, n1, c1)
        harbour(d, 1246, y, n2, c2)
    d.ellipse((640, 300, 896, 450), fill=SAND)                              # the Shallows
    text(d, (768, 352), 'THE SHALLOWS', 20, 'b')
    text(d, (768, 380), 'older maps keep the', 15, 'i')
    text(d, (768, 404), '(the) Sudan · (the) Lebanon', 15, 'i')
    d.polygon([(660, 760), (860, 740), (890, 800), (680, 820)], fill=SAND)    # the False Cape
    d.line((690, 760, 690, 705), fill=INK, width=3)
    d.polygon([(690, 705), (740, 720), (690, 735)], fill=(216, 90, 48))
    text(d, (768, 862), 'THE FALSE CAPE', 20, 'b', SEA_INK)
    text(d, (768, 890), 'the Hague · the Gambia · the Matterhorn', 16, 'i', SEA_INK)
    text(d, (W // 2, 62), 'THE ATLAS OF THE', 44, 'b', SEA_INK)
    text(d, (W // 2, 102), 'does the place take THE? read the shore', 21, 'i', SEA_INK)
    compass(d, 768, 560, 40)
    save(im, 'atlas-of-the')


# ── 14. Finished Time & Open Time ──────────────────────────────────────
FINISHED = ['yesterday', 'last week', 'in 2019', 'two days ago', 'when I was ten', 'on Monday', 'at six', 'the other day']
OPEN = ['ever', 'never', 'yet', 'already', 'so far', 'since 2019', 'recently', 'just']


def finished_open():
    im, d = base()
    d.polygon([(24, 140), (520, 140), (560, 420), (500, 700), (540, H - 24), (24, H - 24)], fill=T['past-simple'])
    d.polygon([(W - 24, 140), (1016, 140), (976, 400), (1040, 680), (996, H - 24), (W - 24, H - 24)], fill=T['present-perfect'])
    text(d, (270, 172), 'FINISHED TIME', 28, 'b')
    text(d, (270, 202), 'past simple: I saw her yesterday.', 16, 'i')
    text(d, (1266, 172), 'OPEN TIME', 28, 'b')
    text(d, (1266, 202), 'present perfect: I have seen her.', 16, 'i')
    for i, (a, b) in enumerate(zip(FINISHED, OPEN)):
        y = 280 + i * 84
        harbour(d, 270, y, a)
        harbour(d, 1266, y, b)
    d.ellipse((618, 250, 918, 520), fill=(214, 190, 140))                  # Twofold Isle
    text(d, (768, 300), 'TWOFOLD ISLE', 20, 'b')
    harbour(d, 768, 380, 'for five years', 'lived (and left) · have lived (and still do)')
    harbour(d, 768, 470, 'this morning', 'over? past · still morning? perfect')
    d.ellipse((650, 600, 886, 700), fill=SAND)                              # the Shallows
    text(d, (768, 636), 'THE SHALLOWS', 19, 'b')
    text(d, (768, 664), 'just · already · yet: US past simple', 14, 'i')
    d.polygon([(650, 800), (850, 780), (880, 840), (670, 860)], fill=SAND)  # the False Cape
    d.line((680, 800, 680, 745), fill=INK, width=3)
    d.polygon([(680, 745), (730, 760), (680, 775)], fill=(216, 90, 48))
    text(d, (768, 900), 'THE FALSE CAPE', 19, 'b', SEA_INK)
    text(d, (768, 928), 'When…? always takes the past: When did you arrive?', 15, 'i', SEA_INK)
    text(d, (W // 2, 62), 'FINISHED TIME & OPEN TIME', 42, 'b', SEA_INK)
    text(d, (W // 2, 102), 'is the time over? read the shore', 21, 'i', SEA_INK)
    save(im, 'finished-open-time')


# ── 15. the Conditional Quadrants ──────────────────────────────────────
def quadrants():
    im, d = base()
    cx, cy = 768, 560
    d.rectangle((cx - 9, 168, cx + 9, H - 24), fill=ROCK)                   # the reality reef
    for x in range(40, W - 40, 34):                                        # the now/past current
        d.line((x, cy, x + 18, cy), fill=SEA_INK, width=3)
    text(d, (cx, 150), 'THE REALITY REEF', 18, 'b', SEA_INK)
    text(d, (390, 172), 'REAL · NOW OR LATER', 22, 'b', SEA_INK)
    text(d, (1146, 172), 'UNREAL · NOW', 22, 'b', SEA_INK)
    text(d, (390, 598), 'REAL · PAST', 22, 'b', SEA_INK)
    text(d, (1146, 598), 'UNREAL · PAST', 22, 'b', SEA_INK)
    harbour(d, 300, 270, 'ZERO', 'If you heat ice, it melts.')
    harbour(d, 470, 380, 'FIRST', 'If it rains, we’ll stay in.')
    harbour(d, 1146, 300, 'SECOND', 'If I had a boat, I’d sail.')
    harbour(d, 390, 700, 'REAL PAST', 'If he said that, he was wrong.')
    harbour(d, 1146, 700, 'THIRD', 'If we’d left, we’d have caught it.')
    # the mixed current, between the two unreal seas
    for y in range(400, 640, 26):
        d.line((1380, y, 1380, y + 14), fill=SEA_INK, width=3)
    d.polygon([(1370, 640), (1390, 640), (1380, 660)], fill=SEA_INK)
    text(d, (1380, 690), 'MIXED', 17, 'b', SEA_INK)
    text(d, (1380, 714), 'If I’d studied,', 14, 'i', SEA_INK)
    text(d, (1380, 734), 'I’d be a doctor now.', 14, 'i', SEA_INK)
    # Regret Reef, off the third conditional
    d.ellipse((1010, 820, 1290, 900), fill=ROCK)
    text(d, (1150, 846), 'REGRET REEF', 17, 'b', WHITE)
    text(d, (1150, 872), 'I wish I had… · If only…', 14, 'i', WHITE)
    # the linking isles
    for (word, x) in zip(('unless', 'provided that', 'as long as', 'in case'), (170, 330, 490, 650)):
        d.ellipse((x - 62, 840, x + 62, 900), fill=SAND)
        dot(d, x, 878)
        text(d, (x, 858), word, 16, 'b')
    text(d, (410, 930), 'THE LINKING ISLES', 17, 'b', SEA_INK)
    text(d, (W // 2, 62), 'THE CONDITIONAL QUADRANTS', 42, 'b', SEA_INK)
    text(d, (W // 2, 100), 'real or unreal? now or past? find your sea', 20, 'i', SEA_INK)
    compass(d, 1440, 900, 34)
    save(im, 'conditional-quadrants')


# ── 16. the Harbour of Scale (in, on, at) ──────────────────────────────
def harbour_of_scale():
    im, d = base()
    # one bay, closed on three sides, its mouth opening east at x 1000
    d.rectangle((24, 140, 1010, H - 24), fill=GREEN)
    d.polygon([(150, 330), (700, 290), (860, 470), (1010, 470), (1010, 650), (860, 650), (700, 830),
               (150, 800), (110, 560)], fill=SEA)                            # the bay
    d.line((300, 140, 320, 310), fill=SEA, width=22)                         # the river, into the bay
    d.rectangle((440, 690, 470, 812), fill=(140, 110, 70))                   # the pier, from the south shore
    d.rectangle((890, 380, 914, 440), fill=WHITE, outline=INK)               # the lighthouse, north of the mouth
    harbour(d, 420, 470, 'in the bay', 'an area: IN')
    harbour(d, 600, 760, 'in the harbour', 'an area: IN')
    harbour(d, 132, 600, 'on the coast', 'a line: ON')
    harbour(d, 312, 230, 'on the river', 'a line: ON')
    harbour(d, 455, 740, 'on the pier', 'a surface: ON')
    harbour(d, 720, 560, 'at the buoy', 'a point: AT')
    harbour(d, 902, 350, 'at the lighthouse', 'a point: AT', )
    harbour(d, 930, 560, 'at the harbour mouth', 'a point: AT')
    # the tide boards: time
    for i, (head, words) in enumerate((('AT', 'at six · at night · at Christmas'),
                                       ('ON', 'on Monday · on 4 July · on my birthday'),
                                       ('IN', 'in July · in 2026 · in the morning'))):
        y = 220 + i * 150
        d.rectangle((1080, y, 1500, y + 110), fill=(214, 190, 140), outline=INK, width=2)
        text(d, (1290, y + 34), head, 30, 'b')
        text(d, (1290, y + 76), words, 17, 'i')
    text(d, (1290, 180), 'THE TIDE BOARDS', 20, 'b', SEA_INK)
    d.ellipse((1120, 700, 1460, 830), fill=(214, 190, 140))                  # Twofold Isle
    text(d, (1290, 735), 'TWOFOLD ISLE', 18, 'b')
    text(d, (1290, 765), 'in time · on time', 15, 'i')
    text(d, (1290, 790), 'in the end · at the end', 15, 'i')
    d.ellipse((1160, 870, 1420, 950), fill=SAND)                             # the Shallows
    text(d, (1290, 900), 'THE SHALLOWS', 16, 'b')
    text(d, (1290, 924), 'at (UK) / on (US) the weekend', 14, 'i')
    text(d, (W // 2, 62), 'THE HARBOUR OF SCALE', 42, 'b', SEA_INK)
    text(d, (W // 2, 102), 'a point: AT · a line: ON · an area: IN', 21, 'i', SEA_INK)
    save(im, 'harbour-of-scale')


# ── 17. the Voyage (prepositions of movement) ──────────────────────────
LEGS = [('out of', 'the harbour', (170, 900)), ('past', 'the lighthouse', (300, 770)),
        ('along', 'the coast', (250, 590)), ('round', 'the cape', (360, 330)),
        ('across', 'the bay', (590, 420)), ('through', 'the strait', (800, 540)),
        ('under', 'the bridge', (960, 680)), ('over', 'the sandbar', (1110, 820)),
        ('up', 'the river', (1300, 690)), ('towards', 'the island', (1170, 530)),
        ('into', 'the cove', (1360, 280)), ('onto', 'the jetty', (1440, 180))]


def voyage():
    im, d = base()
    d.polygon([(24, 140), (140, 140), (160, 300), (420, 280), (430, 360), (170, 400), (150, 700), (220, 860),
               (110, 960), (24, H - 24)], fill=GREEN)                       # west coast, the cape
    d.ellipse((680, 380, 820, 520), fill=LAND)                               # the strait's islands
    d.ellipse((780, 560, 920, 700), fill=LAND)
    d.polygon([(1180, H - 24), (1260, 760), (1380, 600), (W - 24, 560), (W - 24, H - 24)], fill=GREEN)
    d.line((1320, 980, 1300, 690), fill=SEA, width=40)                       # the river
    d.rectangle((930, 655, 990, 705), fill=(140, 110, 70))                   # the bridge
    d.ellipse((1060, 790, 1170, 840), fill=SAND)                             # the sandbar
    d.ellipse((1140, 380, 1300, 480), fill=LAND)                             # the island
    d.polygon([(W - 24, 140), (1300, 140), (1330, 230), (1420, 300), (W - 24, 330)], fill=GREEN)  # the cove
    pts = [p for _, _, p in LEGS]
    for (a, b) in zip(pts, pts[1:]):
        n = 14
        for k in range(0, n, 2):
            x0 = a[0] + (b[0] - a[0]) * k / n
            y0 = a[1] + (b[1] - a[1]) * k / n
            x1 = a[0] + (b[0] - a[0]) * (k + 1) / n
            y1 = a[1] + (b[1] - a[1]) * (k + 1) / n
            d.line((x0, y0, x1, y1), fill=SEA_INK, width=3)
    # where each leg's words go, clear of the land it names: above, right or below
    side = {6: 'r', 7: 'b', 8: 'b', 9: 'r', 10: 'b'}
    for i, (prep, place, (x, y)) in enumerate(LEGS, 1):
        dot(d, x, y)
        s = side.get(i, 'a')
        if s == 'r':
            text(d, (x + 16, y - 10), '%d · %s' % (i, prep.upper()), 18, 'b', SEA_INK, 'lm')
            text(d, (x + 16, y + 10), place, 15, 'i', SEA_INK, 'lm')
        elif s == 'b':
            text(d, (x, y + 22), '%d · %s' % (i, prep.upper()), 18, 'b', SEA_INK)
            text(d, (x, y + 42), place, 15, 'i', SEA_INK)
        else:
            text(d, (x, y - 34), '%d · %s' % (i, prep.upper()), 18, 'b', SEA_INK)
            text(d, (x, y - 14), place, 15, 'i', SEA_INK)
    text(d, (W // 2, 62), 'THE VOYAGE', 44, 'b', SEA_INK)
    text(d, (W // 2, 102), 'twelve legs, twelve prepositions: sail it, then tell it back', 20, 'i', SEA_INK)
    compass(d, 640, 860, 38)
    save(im, 'the-voyage')


# ── 18. the -ER Coast & the MORE Coast ─────────────────────────────────
ER = [('cold', 'colder'), ('fast', 'faster'), ('big', 'bigger'), ('nice', 'nicer'), ('happy', 'happier'), ('easy', 'easier')]
MORE = [('expensive', 'more expensive'), ('careful', 'more careful'), ('modern', 'more modern'),
        ('famous', 'more famous'), ('beautiful', 'more beautiful'), ('interesting', 'more interesting')]


def er_more():
    im, d = base()
    d.polygon([(24, 140), (540, 140), (580, 420), (520, 700), (560, H - 24), (24, H - 24)], fill=LAND)
    d.polygon([(W - 24, 140), (996, 140), (956, 400), (1020, 680), (976, H - 24), (W - 24, H - 24)], fill=GREEN)
    text(d, (280, 172), 'THE -ER COAST', 28, 'b')
    text(d, (280, 202), 'one syllable, or two ending in -y', 16, 'i')
    text(d, (1256, 172), 'THE MORE COAST', 28, 'b')
    text(d, (1256, 202), 'two syllables or more', 16, 'i')
    notes = {'big': 'double the g', 'nice': 'just add -r', 'happy': 'y becomes i', 'easy': 'y becomes i'}
    for i, ((a, b), (c, e)) in enumerate(zip(ER, MORE)):
        y = 290 + i * 104
        harbour(d, 280, y, '%s – %s' % (a, b), notes.get(a))
        harbour(d, 1256, y, e)
    d.ellipse((618, 240, 918, 400), fill=SAND)                               # the Shallows
    text(d, (768, 280), 'THE SHALLOWS', 20, 'b')
    text(d, (768, 310), 'either way', 15, 'i')
    text(d, (768, 336), 'clever · narrow · quiet', 15, 'i')
    text(d, (768, 360), 'simple · gentle', 15, 'i')
    for i, (a, b) in enumerate((('good', 'better'), ('bad', 'worse'), ('far', 'further'))):
        x = 660 + i * 108
        d.rectangle((x - 22, 520, x + 22, 600), fill=ROCK)                    # the lone stacks
        dot(d, x, 620)
        text(d, (x, 650), a, 16, 'b', SEA_INK)
        text(d, (x, 672), b, 15, 'i', SEA_INK)
    text(d, (768, 490), 'THE LONE STACKS', 19, 'b', SEA_INK)
    d.polygon([(650, 800), (850, 780), (880, 840), (670, 860)], fill=SAND)   # the False Cape
    d.line((680, 800, 680, 745), fill=INK, width=3)
    d.polygon([(680, 745), (730, 760), (680, 775)], fill=(216, 90, 48))
    text(d, (768, 900), 'THE FALSE CAPE', 19, 'b', SEA_INK)
    text(d, (768, 928), 'fun · real · right · wrong: short, but MORE', 15, 'i', SEA_INK)
    text(d, (W // 2, 62), 'THE -ER COAST & THE MORE COAST', 40, 'b', SEA_INK)
    text(d, (W // 2, 102), 'short words sail west, long words sail east', 21, 'i', SEA_INK)
    save(im, 'er-more-coasts')


if __name__ == '__main__':
    for f in (atlas, finished_open, quadrants, harbour_of_scale, voyage, er_more):
        f()
    print('wrote six layouts to', OUT)
