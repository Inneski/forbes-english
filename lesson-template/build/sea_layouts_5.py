# -*- coding: utf-8 -*-
"""Layout drafts for sea charts 19-24, for ChatGPT to repaint.

    PYTHONPATH=lesson-template/build py lesson-template/build/sea_layouts_5.py

The rest of the grammar page's chart table (tools/grammar_maps.py PLANNED):
Statia & Actia, Makeland & Doland, Soundings of Certainty, the Passive
Ferry, the Backshift Current and the Bridges. Innes, 2026-11-13, on the
first six: "Why is it only making 6?" There was no reason, so all twelve go
to ChatGPT at once. Same method as sea_layouts_4.py.

Statia & Actia follows the memory "Stative is not the test": the chart asks
whether IS/ARE + -ING works in THAT sentence, so the shores say "usually"
and Twofold Isle carries the verbs whose answer depends on the sentence.
"""
import os
from PIL import ImageDraw
from sea_layouts_2 import W, H, OUT, INK, SEA, SEA_INK, base, text, dot, compass

LAND, SAND, GREEN, ROCK = (201, 176, 122), (217, 199, 154), (183, 207, 155), (150, 140, 125)
WHITE, ISLE, FOG = (245, 245, 240), (214, 190, 140), (222, 226, 228)


def save(im, name):
    im.save(os.path.join(OUT, name + '.png'))


def harbour(d, x, y, name, note=None, fill=INK):
    dot(d, x, y)
    text(d, (x, y - 20), name, 19, 'b', fill)
    if note:
        text(d, (x, y + 21), note, 15, 'i', fill)


def two_shores(d, west, east, wfill, efill):
    d.polygon([(24, 140), (520, 140), (560, 420), (500, 700), (540, H - 24), (24, H - 24)], fill=wfill)
    d.polygon([(W - 24, 140), (1016, 140), (976, 400), (1040, 680), (996, H - 24), (W - 24, H - 24)], fill=efill)


def false_cape(d, y, title, line):
    d.polygon([(650, y), (850, y - 20), (880, y + 40), (670, y + 60)], fill=SAND)
    d.line((680, y, 680, y - 55), fill=INK, width=3)
    d.polygon([(680, y - 55), (730, y - 40), (680, y - 25)], fill=(216, 90, 48))
    text(d, (768, y + 100), title, 19, 'b', SEA_INK)
    text(d, (768, y + 128), line, 15, 'i', SEA_INK)


# ── 19. Statia & Actia ─────────────────────────────────────────────────
STATIA = ['know', 'believe', 'want', 'belong', 'need', 'understand', 'prefer', 'own']
ACTIA = ['run', 'cook', 'read', 'build', 'swim', 'write', 'sail', 'eat']


def statia_actia():
    im, d = base()
    two_shores(d, None, None, LAND, GREEN)
    text(d, (270, 172), 'STATIA', 28, 'b')
    text(d, (270, 202), 'usually no -ING: I know the way.', 16, 'i')
    text(d, (1266, 172), 'ACTIA', 28, 'b')
    text(d, (1266, 202), '-ING for now: I’m sailing.', 16, 'i')
    for i, (a, b) in enumerate(zip(STATIA, ACTIA)):
        y = 280 + i * 84
        harbour(d, 270, y, a)
        harbour(d, 1266, y, b)
    d.ellipse((598, 230, 938, 640), fill=ISLE)                                # Twofold Isle
    text(d, (768, 268), 'TWOFOLD ISLE', 20, 'b')
    text(d, (768, 292), 'the sentence decides', 14, 'i')
    for (w, a, b), y in zip((('think', 'I think so.', 'I’m thinking about it.'),
                             ('have', 'I have a boat.', 'I’m having lunch.'),
                             ('see', 'I see what you mean.', 'I’m seeing Ana tonight.'),
                             ('be', 'He is silly.', 'He’s being silly today.')), (350, 420, 490, 560)):
        dot(d, 768, y)
        text(d, (768, y - 18), w, 18, 'b')
        text(d, (768, y + 20), '%s · %s' % (a, b), 13, 'i')
    d.ellipse((660, 680, 876, 770), fill=SAND)                                # the Shallows
    text(d, (768, 712), 'THE SHALLOWS', 18, 'b')
    text(d, (768, 740), 'feel · hurt: either, same meaning', 13, 'i')
    false_cape(d, 830, 'THE TEST', 'does IS/ARE + -ING work in THIS sentence?')
    text(d, (W // 2, 62), 'STATIA & ACTIA', 44, 'b', SEA_INK)
    text(d, (W // 2, 102), 'a state or an action? ask the sentence, not the verb', 21, 'i', SEA_INK)
    save(im, 'statia-actia')


# ── 20. Makeland & Doland ──────────────────────────────────────────────
MAKE = ['a decision', 'a mistake', 'money', 'a plan', 'progress', 'friends', 'a noise', 'an effort']
DO = ['homework', 'the dishes', 'business', 'a favour', 'your best', 'research', 'damage', 'the shopping']


def make_do():
    im, d = base()
    two_shores(d, None, None, LAND, GREEN)
    text(d, (270, 172), 'MAKELAND', 28, 'b')
    text(d, (270, 202), 'you create it', 16, 'i')
    text(d, (1266, 172), 'DOLAND', 28, 'b')
    text(d, (1266, 202), 'it is a task, a job, an activity', 16, 'i')
    for i, (a, b) in enumerate(zip(MAKE, DO)):
        y = 280 + i * 84
        harbour(d, 270, y, 'make ' + a)
        harbour(d, 1266, y, 'do ' + b)
    d.ellipse((618, 300, 918, 560), fill=ISLE)                                # Take Island
    text(d, (768, 338), 'TAKE ISLAND', 20, 'b')
    for w, y in (('take a photo', 410), ('take a break', 470), ('take a seat', 530)):
        dot(d, 768, y)
        text(d, (768, y - 18), w, 17, 'b')
    false_cape(d, 760, 'THE FALSE CAPE', 'not make a photo but take a photo (German: machen)')
    text(d, (W // 2, 62), 'MAKELAND & DOLAND', 44, 'b', SEA_INK)
    text(d, (W // 2, 102), 'make it or do it? read the shore', 21, 'i', SEA_INK)
    save(im, 'make-do')


# ── 21. Soundings of Certainty ─────────────────────────────────────────
def certainty():
    im, d = base()
    # depth bands, deep at the top, the rocks at the foot
    bands = [((140, 330), (120, 160, 190)), ((330, 480), (150, 185, 205)), ((480, 700), FOG), ((700, H - 24), ROCK)]
    for (y0, y1), c in bands:
        d.rectangle((24, y0, W - 24, y1), fill=c)
    rows = [('must', '95%', 'It must be the ferry: it’s six o’clock.', 'must have', 'She must have left.', 235),
            ('should', '80%', 'It should be calm by noon.', None, None, 405),
            ('may · might · could', '50%', 'It might be a whale. It could be a log.', 'might have', 'He might have missed it.', 590),
            ('can’t · couldn’t', '0%', 'It can’t be Tom: he’s in Rome.', 'can’t have', 'They can’t have seen us.', 830)]
    for word, pc, ex, past, pex, y in rows:
        fill = WHITE if y > 700 else INK
        harbour(d, 330, y, word, '%s · %s' % (pc, ex), fill)
        if past:
            harbour(d, 1180, y, past, pex, fill)
    text(d, (330, 172), 'NOW', 24, 'b', WHITE)
    text(d, (1180, 172), 'THE PAST: + have + past participle', 20, 'b', WHITE)
    text(d, (768, 520), 'THE FOG BANK', 18, 'b', SEA_INK)
    text(d, (768, 742), 'THE ROCKS', 18, 'b', WHITE)
    text(d, (W // 2, 62), 'SOUNDINGS OF CERTAINTY', 42, 'b', SEA_INK)
    text(d, (W // 2, 102), 'how sure are you that it’s true? read the depth', 21, 'i', SEA_INK)
    compass(d, 768, 330, 34)
    save(im, 'certainty')


# ── 22. the Passive Ferry ──────────────────────────────────────────────
PAIRS = [('They build it.', 'It is built.', 'present'), ('They built it.', 'It was built.', 'past'),
         ('They have built it.', 'It has been built.', 'perfect'), ('They will build it.', 'It will be built.', 'future'),
         ('They are building it.', 'It is being built.', 'continuous'), ('They can build it.', 'It can be built.', 'modal')]


def passive_ferry():
    im, d = base()
    two_shores(d, None, None, GREEN, LAND)
    text(d, (270, 172), 'ACTIVIA', 28, 'b')
    text(d, (270, 202), 'who does it comes first', 16, 'i')
    text(d, (1266, 172), 'PASSIVIA', 28, 'b')
    text(d, (1266, 202), 'what it happens to comes first', 16, 'i')
    for i, (a, p, tense) in enumerate(PAIRS):
        y = 290 + i * 96
        harbour(d, 270, y, a, tense)
        harbour(d, 1266, y, p)
        for x in range(300, 1236, 30):                                          # the ferry lane
            d.line((x, y, x + 14, y), fill=SEA_INK, width=2)
    d.ellipse((700, 150, 836, 220), fill=SAND)                                  # the by-buoy
    text(d, (768, 178), 'BY-BUOY', 16, 'b')
    text(d, (768, 200), 'by … : only if it matters', 12, 'i')
    d.ellipse((90, 860, 450, 960), fill=SEA)                                    # the land-locked lake
    text(d, (270, 896), 'THE LAND-LOCKED LAKE', 16, 'b', SEA_INK)
    text(d, (270, 922), 'happen · arrive · die · seem: no passive', 13, 'i', SEA_INK)
    d.ellipse((640, 870, 896, 960), fill=SAND)                                  # the Shallows
    text(d, (768, 900), 'THE SHALLOWS', 16, 'b')
    text(d, (768, 924), 'I was given a book. A book was given to me.', 12, 'i')
    d.polygon([(1080, 880), (1260, 860), (1290, 920), (1100, 940)], fill=SAND)  # the False Cape
    d.line((1110, 880, 1110, 830), fill=INK, width=3)
    d.polygon([(1110, 830), (1160, 845), (1110, 860)], fill=(216, 90, 48))
    text(d, (1266, 966), 'THE FALSE CAPE: I was born in Lima.', 15, 'b')
    text(d, (W // 2, 62), 'THE PASSIVE FERRY', 44, 'b', SEA_INK)
    text(d, (W // 2, 102), 'the object sails to the front: be + past participle', 21, 'i', SEA_INK)
    save(im, 'passive-ferry')


# ── 23. the Backshift Current ──────────────────────────────────────────
SHIFTS = [('“I am tired.”', 'she was tired'), ('“I work here.”', 'he worked there'),
          ('“I’m leaving.”', 'she was leaving'), ('“I’ve finished.”', 'he had finished'),
          ('“I saw it.”', 'she had seen it'), ('“I’ll help.”', 'he would help'), ('“I can swim.”', 'she could swim')]


def backshift():
    im, d = base()
    two_shores(d, None, None, GREEN, LAND)
    text(d, (270, 172), 'DIRECT HARBOUR', 26, 'b')
    text(d, (270, 202), 'the words as they were said', 16, 'i')
    text(d, (1266, 172), 'REPORTED HARBOUR', 26, 'b')
    text(d, (1266, 202), 'she said (that) …', 16, 'i')
    for i, (a, b) in enumerate(SHIFTS):
        y = 280 + i * 88
        harbour(d, 270, y, a)
        harbour(d, 1266, y, b)
        for x in range(300, 1220, 34):                                          # the current, west to east
            d.line((x, y, x + 18, y), fill=SEA_INK, width=2)
        d.polygon([(1222, y - 7), (1236, y), (1222, y + 7)], fill=SEA_INK)
    text(d, (768, 238), 'THE BACKSHIFT CURRENT', 19, 'b', SEA_INK)
    text(d, (768, 872), 'DRIFTING BUOYS: today becomes that day · tomorrow, the next day · here, there', 15, 'i', SEA_INK)
    for i, w in enumerate(('had done', 'would', 'could', 'should', 'might')):
        x = 600 + i * 84
        d.rectangle((x - 18, 892, x + 18, 936), fill=ROCK)
    text(d, (768, 962), 'THE STILL ROCKS: had done · would · could · should · might never move', 14, 'b', SEA_INK)
    text(d, (W // 2, 62), 'THE BACKSHIFT CURRENT', 42, 'b', SEA_INK)
    text(d, (W // 2, 102), 'report it later and the tense drifts one step back', 21, 'i', SEA_INK)
    save(im, 'backshift-current')


# ── 24. the Bridges ────────────────────────────────────────────────────
def bridges():
    im, d = base()
    two_shores(d, None, None, GREEN, LAND)
    text(d, (270, 180), 'IT WAS STORMY', 26, 'b')
    text(d, (270, 210), 'the first idea', 16, 'i')
    text(d, (1266, 180), 'WE SAILED', 26, 'b')
    text(d, (1266, 210), 'the second idea', 16, 'i')
    groups = [('BRIDGES', 'one sentence: because · although · but · so · while',
               [('although', 'Although it was stormy, we sailed.'), ('but', 'It was stormy, but we sailed.')], 300),
              ('FERRIES', 'a new sentence first: . However, … Therefore, …',
               [('However,', 'It was stormy. However, we sailed.'), ('Nevertheless,', 'It was stormy. Nevertheless, we sailed.')], 540),
              ('PIERS', 'a noun or -ING after them',
               [('despite', 'Despite the storm, we sailed.'), ('in spite of', 'In spite of the storm, we sailed.')], 780)]
    for title, rule, stops, y in groups:
        text(d, (768, y - 40), title, 22, 'b', SEA_INK)
        text(d, (768, y - 14), rule, 14, 'i', SEA_INK)
        for k, (w, ex) in enumerate(stops):
            yy = y + 40 + k * 80
            d.rectangle((500, yy - 8, 1036, yy + 8), fill=(140, 110, 70) if title != 'FERRIES' else SEA)
            if title == 'FERRIES':
                for x in range(500, 1036, 30):
                    d.line((x, yy, x + 14, yy), fill=SEA_INK, width=3)
            dot(d, 768, yy)
            text(d, (768, yy - 22), w, 18, 'b', SEA_INK)
            text(d, (768, yy + 24), ex, 14, 'i', SEA_INK)
    text(d, (W // 2, 62), 'THE BRIDGES', 44, 'b', SEA_INK)
    text(d, (W // 2, 102), 'join two ideas: a bridge, a ferry or a pier?', 21, 'i', SEA_INK)
    save(im, 'the-bridges')


if __name__ == '__main__':
    for f in (statia_actia, make_do, certainty, passive_ferry, backshift, bridges):
        f()
    print('wrote six layouts to', OUT)
