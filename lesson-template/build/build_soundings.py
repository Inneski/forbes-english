# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: Soundings of Frequency, adverbs of frequency
as the depth of the sea. The sixth chart.

    py lesson-template/build/build_soundings.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. How often is how deep: never on the shore, hardly ever in
the shallows, always in the deep water. The anchor buoy is the word-order
rule (before the main verb, after be, after the first of two verbs), and the
current shows the adverbs that can sail to the front (Sometimes we...).

THE ART. Layout by sea_layouts_2.py (docs/sea-charts/frequency-soundings.png),
painted by Codex on 2026-11-09 with Gerundia as the style. Dots measured by
sea_measure.py --dark into soundings_chart.json: the usual ring test fails on
the dark bands (a dark dot on dark water), so --dark compares the ring with
the dot instead. Each band's paint is sampled beside its dot, so the label
ink flips from dark to light as the water deepens.
"""
import sys
import numpy as np
from PIL import Image
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE

OUT = 'sailing-the-seas-soundings.html'
ART = 'sailing-the-seas-soundings'
UID = 'snd'

# py lesson-template/extract-palette.py sailing-the-seas-soundings/hero.jpg --light
EXTRACTED = {'text': '#2a2011', 'text-dim': '#5e4b2e', 'secondary': '#2d546a', 'contrast': '#074c55'}

D = O.load('soundings_chart.json')
DOTS = sorted((tuple(p) for p in D['dots']), key=lambda p: p[1])
assert len(DOTS) == 8, DOTS
_px = np.asarray(Image.open(ART + '/chart-clean.jpg').convert('RGB')).astype(int)


def paint_at(x, y):
    return '#%02X%02X%02X' % tuple(np.median(_px[y - 20:y + 20, x:x + 260].reshape(-1, 3), axis=0).astype(int))


def ink_on(paint):
    """Dark ink on the pale water, light on the deep: whichever reads better."""
    dark, light = O.ink_for(paint, 7), '#FBF8F0'
    return (dark, .3) if O.ratio(dark, paint) >= O.ratio(light, paint) and O.ratio(dark, paint) >= 4.5 else (light, -.35)


# (adverb, about how often, a sentence)
SOUNDINGS = [
    ('never', '0%', 'I never swim at night.'),
    ('hardly ever', '5%', 'I hardly ever swim at night.'),
    ('rarely', '10%', 'I rarely swim at night.'),
    ('occasionally', '30%', 'I occasionally swim at night.'),
    ('sometimes', '50%', 'I sometimes swim at night.'),
    ('often', '70%', 'I often swim at night.'),
    ('usually', '80%', 'I usually swim at night.'),
    ('always', '100%', 'I always swim at night.'),
]
BANDS = []
for (x, y), (adv, pc, sent) in zip(DOTS, SOUNDINGS):
    paint = paint_at(x + 30, y)
    BANDS.append((x, y, adv, pc, sent, paint, ink_on(paint)))
SEA_DEEP = paint_at(1000, 600)
CAP_INK = ink_on(paint_at(1000, 300))[0]


def overlay():
    spots, names = [], []
    for i, (x, y, adv, pc, sent, paint, (ink, halo)) in enumerate(BANDS):
        names.append(O.name(x, y, (adv, '%s &#183; about %s' % (adv, pc), sent), ink, paint, size=24,
                            anchor='start', dx=28, dy=8, fit=False, halo=halo))
        top = 24 if i == 0 else y - 48
        spots.append(O.hotspot(UID, adv.replace(' ', '-'), O.rect_path(24, top, 900, y + 48),
                               '%s: about %s of the time' % (adv, pc)))
    spots.append(O.hotspot(UID, 'anchor', O.circle_path(976, 336, 62), 'The anchor: where the adverb goes'))
    spots.append(O.hotspot(UID, 'front', O.rect_path(960, 590, 1430, 700), 'The current: sometimes sails to the front'))
    dark_ink = ink_on(paint_at(1100, 640))[0]
    caps = [O.cap(768, 60, 'SOUNDINGS OF FREQUENCY', '#2A2011', 38, face=O.SERIF, spacing='.04em'),
            O.cap(768, 92, 'how often? read the depth', '#2A2011', 19, face=O.SERIF, weight=600, spacing='0', style='italic'),
            O.cap(1256, 298, 'THE ANCHOR', CAP_INK, 22, face=O.SERIF, spacing='.05em'),
            O.cap(1256, 330, 'before the main verb: we often sail', CAP_INK, 16, weight=600, spacing='0', style='italic'),
            O.cap(1256, 356, 'after be: she is often late', CAP_INK, 16, weight=600, spacing='0', style='italic'),
            O.cap(1200, 610, 'SOMETIMES SAILS TO THE FRONT', dark_ink, 18, spacing='.06em'),
            O.cap(1200, 670, 'Sometimes we sail at night.', dark_ink, 16, weight=600, spacing='0', style='italic'),
            O.cap(60, 980, 'depths are rough percentages', '#FBF8F0', 14.5, 'start', weight=500, spacing='0', style='italic')]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated depth chart. A sandy shore with a harbour village runs along the top, at Never Point, 0. '
            'Below it the sea deepens in bands: hardly ever 5, rarely 10, occasionally 30, sometimes 50, often 70, '
            'usually 80, always 100, from pale blue to deep navy. A red anchor buoy marks the rule: before the main '
            'verb, we often sail; after be, she is often late. A current flows west: sometimes sails to the front.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; adverbs of frequency', 'Soundings of Frequency',
    'Old sea charts mark the depth of the water in numbers called soundings. Here the depth is how often something '
    'happens: <em>never</em> on the dry shore, <em>sometimes</em> halfway out, <em>always</em> in the deepest water. '
    'The red buoy marks where the word drops anchor in a sentence. Read the depth, then drop the anchor.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the depth</div>
      <h2>How often, and where it goes</h2>
      <p class="chart-note" style="margin:-6px 0 18px">An adverb of frequency answers <em>How often?</em> Choosing the word is half the job; the other half is the anchor, its place in the sentence.</p>
      ''' + rule_grid([
    ('<em>Always</em> and <em>never</em> are the ends',
     'One is the deepest water, the other dry land. Everything else lies between.',
     ex('The lighthouse is <em>always</em> on, but the ferry <em>never</em> runs at night.')),
    ('<em>Usually</em>, <em>often</em>, <em>sometimes</em>',
     'The middle depths: most of the time, a lot of the time, some of the time.',
     ex('We <em>usually</em> sail on Saturdays, and <em>sometimes</em> on Sundays.')),
    ('<em>Rarely</em> and <em>hardly ever</em> are already negative',
     'They mean <em>almost never</em>, so they never take <em>not</em>: <em>I hardly ever swim</em>, not <em>I don&#39;t hardly ever swim</em>.',
     ex('I <em>hardly ever</em> get seasick.')),
    ('Before the main verb',
     'With an ordinary verb, the adverb drops anchor just in front of it.',
     ex('She <em>often</em> swims before breakfast.')),
    ('After <em>be</em>',
     'With <em>am, is, are, was, were</em>, it comes after the verb instead.',
     ex('The sea is <em>usually</em> calm in July.')),
    ('With two verbs: after the first',
     'After <em>have, can, will, must</em> and the other helpers: <em>I have never seen</em>, <em>you can always ask</em>.',
     ex('I have <em>never</em> seen a whale.')),
]) + chart(
    'The eight soundings',
    'The numbers are rough: <em>often</em> to one speaker is <em>usually</em> to another. What matters is the order.',
    ['Adverb', 'About', 'At sea'],
    [['always', '100%', 'The lighthouse is always on.'], ['usually', '80%', 'We usually eat on deck.'],
     ['often', '70%', 'It often rains in the afternoon.'], ['sometimes', '50%', 'We sometimes see dolphins.'],
     ['occasionally', '30%', 'I occasionally fish from the pier.'], ['rarely', '10%', 'The harbour rarely freezes.'],
     ['hardly ever', '5%', 'We hardly ever sail in winter.'], ['never', '0%', 'The ferry never runs at night.']]) + '''
    </div>

    '''

CURRENT = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The current</div>
      <h2>Front, middle and end</h2>
      <p class="chart-note" style="margin:-6px 0 18px">The middle of the sentence is always safe. A few adverbs can also ride the current to the front, for emphasis or contrast. <em>Always</em> and <em>never</em> stay anchored.</p>
      ''' + chart(
    'Where each one can go',
    'A dash means the position sounds wrong.',
    ['Adverb', 'Middle (always safe)', 'Front', 'End'],
    [['sometimes', 'We sometimes sail at night.', 'Sometimes we sail at night.', 'We sail at night sometimes.'],
     ['usually', 'We usually eat on deck.', 'Usually we eat on deck.', '&mdash;'],
     ['occasionally', 'I occasionally fish.', 'Occasionally I fish.', 'I fish occasionally.'],
     ['often', 'She often swims.', '&mdash;', 'She swims quite often.'],
     ['always', 'He always waves.', '&mdash;', '&mdash;'],
     ['never', 'They never stop.', '&mdash;', '&mdash;']]) + '''
      ''' + exi('<em>Sometimes</em> we sail at night.') + chart(
    'Longer answers go at the end',
    'Phrases like these do not drop anchor in the middle: they go at the end, or at the very front.',
    ['How often do you sail?', 'In a sentence'],
    [['every day', 'We sail every day.'], ['twice a week', 'We sail twice a week.'],
     ['once a month', 'Once a month we sail to the island.'], ['three times a year', 'They visit three times a year.']]) + '''
      ''' + exi('We sail <em>twice a week</em>.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a depth and its line lights up below; click the red buoy for the word-order rule. Switch the chart to see '
    'each adverb with its rough percentage, then in a sentence: only the adverb changes, and it always drops anchor '
    'in the same place.',
    ('The adverbs', 'How often', 'In a sentence'),
    [('Shallow water &middot; not often', 'is-west'), ('Deep water &middot; often', 'is-isle'),
     ('Where to drop anchor', 'is-east')],
    'Drag the chart sideways to reach the buoy.', min_zoom=1000)

TRAPS = fork(
    'Anchors in the wrong place',
    'The commonest mistakes with adverbs of frequency are about position, not meaning.',
    ['Not this', 'This', 'Why'],
    [['I go always to the beach.', 'I always go to the beach.', 'before the main verb'],
     ['She often is late.', 'She is often late.', 'after <em>be</em>'],
     ['I never have seen a whale.', 'I have never seen a whale.', 'after the first of two verbs'],
     ['I don&#39;t hardly ever swim.', 'I hardly ever swim.', '<em>hardly ever</em> is already negative'],
     ['Always I wake up early.', 'I always wake up early.', '<em>always</em> does not go to the front']],
    'In a question the adverb still comes before the main verb: <em>Do you often swim?</em> '
    '<em>Are you always this early?</em>',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-adjective-canal.html', 'The adjective canal')])

SIGNALS = signals(
    'Before the main verb',
    ['ordinary verbs: <em>I often swim</em>', '<em>he always waves</em>', '<em>they never stop</em>',
     'in questions: <em>Do you often swim?</em>', 'in negatives: <em>I don&#39;t often swim</em>',
     'with <em>do / does / did</em> doing the work'],
    'After the first verb',
    ['<em>be</em>: <em>she is often late</em>', '<em>have</em>: <em>I have never seen</em>',
     '<em>can</em>: <em>you can always ask</em>', '<em>will</em>: <em>it will usually rain</em>',
     '<em>must, should, could</em>', 'the first verb carries the tense; the adverb follows it'],
    'One test: find the verb that carries the tense. If it is <em>be</em> or a helper, the adverb comes after it; '
    'otherwise, before the main verb.')

QUIZ = [
    ('I ___ to the beach on Sundays.', 'Before the main verb.', 'always go',
     ['always go', 'go always', 'always going', 'am always go'], 'An ordinary verb: the adverb goes in front of it. I always go.'),
    ('She ___ late for work.', 'After be.', 'is never',
     ['is never', 'never is', 'never be', 'is not never'], 'With be, the adverb comes after it: she is never late.'),
    ('I ___ seen a dolphin.', 'Two verbs: after the first.', 'have never',
     ['have never', 'never have', 'have not never', 'never had'], 'After the first verb, have: I have never seen.'),
    ('Which means about 10% of the time?', 'Shallow water.', 'rarely',
     ['rarely', 'usually', 'often', 'sometimes'], 'Rarely sits in the shallows, at about 10%.'),
    ('We ___ get seasick: it happens once or twice a year.', 'Almost never.', 'hardly ever',
     ['hardly ever', 'don&#39;t hardly ever', 'usually', 'always'], 'Hardly ever means almost never, and it is already negative: no don&#39;t.'),
    ('Which sentence is correct?', 'Sometimes can ride the current to the front.', 'Sometimes we sail at night.',
     ['Sometimes we sail at night.', 'Always we sail at night.', 'Never we sail at night.', 'Hardly ever we sail at night.'],
     'Sometimes can go first. Always, never and hardly ever stay in the middle.'),
    ('Do you ___ swim in the sea?', 'In a question, still before the main verb.', 'often',
     ['often', 'oftenly', 'ever often', 'are often'], 'Do you often swim? The adverb comes before the main verb, swim.'),
    ('The harbour ___ busy in August.', 'After be.', 'is usually',
     ['is usually', 'usually is', 'usually be', 'is usual'], 'With be, the adverb comes after it: the harbour is usually busy.'),
    ('Which is the deepest water: the most often?', 'Read the depth.', 'usually',
     ['usually', 'sometimes', 'occasionally', 'rarely'], 'Of these four, usually (about 80%) is the deepest.'),
    ('He ___ fishing at the weekend.', 'Present simple: he takes -s.', 'often goes',
     ['often goes', 'goes often to', 'often go', 'often going'], 'He often goes: the adverb before the verb, and the verb keeps its -s.'),
    ('How often do you sail? — ___', 'A longer answer goes at the end.', 'Twice a week.',
     ['Twice a week.', 'Two times week.', 'Twice in week.', 'Weekly twice.'], 'Twice a week: once, twice, then three times, four times.'),
    ('Which is NOT correct?', 'One adverb dropped anchor in the wrong place.', 'I go never sailing.',
     ['I go never sailing.', 'I never go sailing.', 'I am never bored at sea.', 'I have never sailed alone.'],
     'Never goes before the main verb: I never go sailing.'),
]

PANELS = [
    [('never', '<b>never</b> 0% &middot; dry land'), ('hardly-ever', '<b>hardly ever</b> about 5%'),
     ('rarely', '<b>rarely</b> about 10%'), ('occasionally', '<b>occasionally</b> about 30%')],
    [('sometimes', '<b>sometimes</b> about 50%'), ('often', '<b>often</b> about 70%'),
     ('usually', '<b>usually</b> about 80%'), ('always', '<b>always</b> 100% &middot; the deepest water')],
    [('anchor', '<b>The anchor</b> before the main verb: <em>we often sail</em>'),
     ('anchor', 'after <em>be</em>: <em>she is often late</em> &middot; after the first verb: <em>I have never seen</em>'),
     ('front', '<b>The current</b> sometimes, usually, occasionally can go first: <em>Sometimes we sail at night.</em>')],
]
TARGETS = {}
for i, (x, y, adv, pc, sent, paint, (ink, halo)) in enumerate(BANDS):
    key = adv.replace(' ', '-')
    TARGETS[key] = (0 if i < 4 else 1, key, '#074c55')
TARGETS['anchor'] = (2, 'anchor', '#B4441F')
TARGETS['front'] = (2, 'front', '#074c55')

import ex_tr_soundings as T
L.build(OUT, ART, 'Soundings of Frequency &mdash; Adverbs of Frequency', 'adverbs of frequency', EXTRACTED,
        HERO, 'Read the depth, then drop the anchor.', ('order', 'Read the chart'),
        RULES + CURRENT + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        [paint_at(300, 300), paint_at(300, 650), '#D8C79A'], T.T,
        ['Clean run. You can read the depth and drop the anchor in the right place.',
         'Solid progress. Say the rule aloud: before the main verb, after be.',
         'Good first attempt. Start with the anchor: before the main verb.'],
        ('sailing-the-seas-adjective-canal.html', 'Next chart: the adjective canal'), gull_seed=29)
