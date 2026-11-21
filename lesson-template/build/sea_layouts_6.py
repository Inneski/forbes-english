# -*- coding: utf-8 -*-
"""Layout drafts for sea charts 25-28, for ChatGPT to repaint.

    PYTHONPATH=lesson-template/build py lesson-template/build/sea_layouts_6.py

The four grammar-page topics no chart taught (Innes, 2026-11-21: the topic
cards went back to pictures, each topic's own chart, "Yes, write it" to the
brief for the four that had none): the Past Continuous, the Present Perfect
Continuous, the Past Perfect and Used To. Same method as sea_layouts_5.py:
two shores, harbours with an example under each, the tense painted in its
Sherpa colour (sea_tense.T), every word written so the repaint can copy it.

Used To is not a tense on the route map, so its two harbours take the past
simple (then) and the present simple (now): it is a past habit set against
the present.
"""
import os
from sea_layouts_2 import W, H, OUT, INK, SEA, SEA_INK, base, text, dot, compass
from sea_layouts_5 import harbour, two_shores, LAND, SAND, GREEN, ROCK, ISLE
from sea_tense import T


def save(im, name):
    im.save(os.path.join(OUT, name + '.png'))


def current(d, x0, x1, y, fill, width=3, dash=34):
    """A dashed current running east, with its arrowhead."""
    for x in range(x0, x1 - 20, dash):
        d.line((x, y, x + dash // 2, y), fill=fill, width=width)
    d.polygon([(x1 - 16, y - 8), (x1, y), (x1 - 16, y + 8)], fill=fill)


def squall(d, x, y, fill):
    """A short sharp storm: a jagged bolt striking the current."""
    d.polygon([(x - 10, y - 46), (x + 12, y - 46), (x + 2, y - 14), (x + 16, y - 14),
               (x - 12, y + 22), (x - 2, y - 6), (x - 16, y - 6)], fill=fill, outline=INK)


# ── 25. the Long Passage: past continuous ──────────────────────────────
PASSAGES = [('I was sailing home', 'when the storm hit.'),
            ('She was reading in her cabin', 'when the bell rang.'),
            ('While we were eating,', 'the ship left the harbour.')]


def long_passage():
    im, d = base()
    two_shores(d, None, None, T['past-continuous'], T['past-simple'])
    text(d, (270, 172), 'THE LONG COAST', 26, 'b')
    text(d, (270, 202), 'WAS / WERE + -ING: in progress', 16, 'i')
    text(d, (1266, 172), 'THE SQUALL COAST', 26, 'b')
    text(d, (1266, 202), 'past simple: the short event', 16, 'i')
    for i, (a, b) in enumerate(PASSAGES):
        y = 290 + i * 120
        harbour(d, 270, y, a)
        harbour(d, 1266, y, b)
        d.rectangle((560, y - 9, 1000, y + 9), fill=T['past-continuous'], outline=INK)   # the long passage
        squall(d, 940, y, T['past-simple'])
    text(d, (768, 246), 'THE LONG PASSAGE', 19, 'b', SEA_INK)
    for k, y in enumerate((690, 726)):                                                  # two at once
        d.rectangle((560, y - 7, 1000, y + 7), fill=T['past-continuous'], outline=INK)
    text(d, (780, 662), 'THE TWIN CURRENTS: two actions at the same time', 17, 'b', SEA_INK)
    text(d, (780, 760), 'I was steering while she was cooking.', 15, 'i', SEA_INK)
    d.ellipse((700, 812, 836, 868), fill=SAND)                                          # the lighthouse rock
    d.rectangle((760, 790, 776, 840), fill=(240, 236, 226), outline=INK)
    text(d, (768, 892), 'EIGHT O’CLOCK LIGHT: a time in the middle of it', 16, 'b', SEA_INK)
    text(d, (768, 918), 'At eight o’clock I was cooking dinner.', 14, 'i', SEA_INK)
    compass(d, 1420, 900, 38)
    text(d, (W // 2, 62), 'THE LONG PASSAGE', 44, 'b', SEA_INK)
    text(d, (W // 2, 102), 'a long action in progress, cut by a short one', 21, 'i', SEA_INK)
    save(im, 'long-passage')


# ── 26. the Running Tide: present perfect continuous ───────────────────
def running_tide():
    im, d = base()
    two_shores(d, None, None, LAND, T['present-perfect-continuous'])
    text(d, (270, 172), 'THEN', 28, 'b')
    text(d, (270, 202), 'when it started', 16, 'i')
    text(d, (1266, 172), 'NOW', 28, 'b')
    text(d, (1266, 202), 'still going, or only just stopped', 16, 'i')
    rows = [('since nine o’clock', 'I’ve been sailing since nine o’clock.', 'SINCE: the start'),
            ('for three hours', 'I’ve been sailing for three hours.', 'FOR: how long'),
            ('How long …?', 'How long have you been waiting?', 'the question')]
    for i, (w, ex, note) in enumerate(rows):
        y = 290 + i * 120
        harbour(d, 270, y, w, note)
        d.rectangle((560, y - 9, 1000, y + 9), fill=T['present-perfect-continuous'], outline=INK)
        current(d, 1000, 1110, y, SEA_INK)                                              # the tide runs on past now
        text(d, (1266, y - 20), ex, 15, 'i')
        dot(d, 1266, y + 6)
    text(d, (780, 246), 'THE RUNNING TIDE: HAVE / HAS BEEN + -ING', 19, 'b', SEA_INK)
    d.ellipse((600, 640, 936, 760), fill=ISLE)                                          # what you can see
    text(d, (768, 676), 'WET DECKS ISLE', 19, 'b')
    text(d, (768, 704), 'the result you can see now', 14, 'i')
    text(d, (768, 730), 'Why are you wet? I’ve been swimming.', 14, 'i')
    d.rectangle((560, 808, 1000, 828), fill=T['present-perfect'], outline=INK)          # the finished reef
    text(d, (780, 854), 'THE FINISHED REEF: the activity, or the thing done?', 17, 'b', SEA_INK)
    text(d, (780, 880), 'I’ve been painting the boat (the activity)  ·  I’ve painted the boat (done)', 14, 'i', SEA_INK)
    compass(d, 1420, 900, 38)
    text(d, (W // 2, 62), 'THE RUNNING TIDE', 44, 'b', SEA_INK)
    text(d, (W // 2, 102), 'it started in the past and it is still running now', 21, 'i', SEA_INK)
    save(im, 'running-tide')


# ── 27. the Earlier Shore: past perfect ────────────────────────────────
PAIRS = [('The ship had left', 'when we arrived.'),
         ('She had eaten,', 'so she wasn’t hungry.'),
         ('I had never seen the sea', 'before I went to Spain.'),
         ('The shop had closed', 'by the time we got there.')]


def earlier_shore():
    im, d = base()
    two_shores(d, None, None, T['past-perfect'], T['past-simple'])
    text(d, (270, 172), 'THE EARLIER SHORE', 26, 'b', (245, 245, 240))
    text(d, (270, 202), 'HAD + past participle: first', 16, 'i', (245, 245, 240))
    text(d, (1266, 172), 'THE LATER SHORE', 26, 'b')
    text(d, (1266, 202), 'past simple: after it', 16, 'i')
    for i, (a, b) in enumerate(PAIRS):
        y = 290 + i * 104
        harbour(d, 270, y, a, fill=(245, 245, 240))
        harbour(d, 1266, y, b)
        current(d, 560, 1000, y, SEA_INK)                                               # first, then
    text(d, (768, 246), 'FIRST, THEN', 19, 'b', SEA_INK)
    for i, w in enumerate(('already', 'just', 'never … before', 'by the time', 'after')):
        x = 600 + i * 84
        d.ellipse((x - 16, 732, x + 16, 764), fill=(216, 90, 48), outline=INK)          # the buoys
    text(d, (768, 790), 'SIGNAL BUOYS', 15, 'b', SEA_INK)
    text(d, (768, 812), 'already · just · never … before · by the time · after', 14, 'i', SEA_INK)
    d.ellipse((660, 838, 876, 908), fill=SAND)                                          # the Shallows
    text(d, (768, 862), 'THE SHALLOWS', 17, 'b')
    text(d, (768, 886), 'After we ate, we left: AFTER shows the order, so either', 13, 'i')
    d.polygon([(1400, 800), (1450, 780), (1460, 840), (1410, 850)], fill=ROCK)          # now, far off
    text(d, (1380, 878), 'NOW is off the chart', 14, 'i')
    text(d, (W // 2, 62), 'THE EARLIER SHORE', 44, 'b', SEA_INK)
    text(d, (W // 2, 102), 'two pasts: the one that happened first takes HAD', 21, 'i', SEA_INK)
    save(im, 'earlier-shore')


# ── 28. the Old Harbour: used to ───────────────────────────────────────
HABITS = [('I used to live by the sea.', 'Now I live in the city.'),
          ('We used to sail every summer.', 'Now we fly.'),
          ('She didn’t use to like fish.', 'Now she loves it.')]


def old_harbour():
    im, d = base()
    two_shores(d, None, None, T['past-simple'], T['present-simple'])
    text(d, (270, 172), 'THE OLD HARBOUR', 26, 'b')
    text(d, (270, 202), 'USED TO + verb: true then', 16, 'i')
    text(d, (1266, 172), 'THE NEW HARBOUR', 26, 'b')
    text(d, (1266, 202), 'not any more', 16, 'i')
    for i, (a, b) in enumerate(HABITS):
        y = 290 + i * 110
        harbour(d, 270, y, a)
        harbour(d, 1266, y, b)
        current(d, 560, 1000, y, SEA_INK)
    text(d, (768, 246), 'THEN, NOW', 19, 'b', SEA_INK)
    d.rectangle((640, 610, 896, 640), fill=ROCK)                                        # did … use to
    text(d, (768, 664), 'DID ROCK: Did you use to sail? no -D after DID', 15, 'b', SEA_INK)
    d.ellipse((560, 700, 1000, 830), fill=ISLE)                                         # be / get used to
    text(d, (780, 734), 'FAMILIAR ISLE: BE / GET USED TO + noun or -ING', 17, 'b')
    text(d, (780, 762), 'I’m used to the cold.  ·  I’m getting used to the waves.', 14, 'i')
    text(d, (780, 788), 'a different meaning: it is normal for me now', 14, 'i')
    d.rectangle((560, 868, 1000, 884), fill=ROCK)                                       # would
    text(d, (780, 910), 'WOULD REEF: repeated actions only, never states', 15, 'b', SEA_INK)
    text(d, (780, 934), 'We would swim every day.  ·  not: We would live by the sea.', 14, 'i', SEA_INK)
    text(d, (W // 2, 62), 'THE OLD HARBOUR', 44, 'b', SEA_INK)
    text(d, (W // 2, 102), 'used to: what was true then and is not now', 21, 'i', SEA_INK)
    save(im, 'old-harbour')


if __name__ == '__main__':
    for f in (long_passage, running_tide, earlier_shore, old_harbour):
        f()
    print('wrote four layouts to', OUT)
