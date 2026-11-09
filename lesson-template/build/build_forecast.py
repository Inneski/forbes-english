# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: The Grammar Forecast, how sure a prediction
is, read off six sea areas. The eleventh chart.

    py lesson-template/build/build_forecast.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. A weather chart split into six sea areas, the weather in
each matching how sure the speaker is: BOUND (is bound to, about 100%) under
a downpour, WILL under dark cloud, LIKELY under gathering cloud, MAYBE (may,
might, could) in sun and cloud, UNLIKELY mostly fair, WON'T under a clear
sky. The page teaches the patterns (is likely to / it is likely that) and
the word order the forecasts trip on: will probably, but probably won't.

THE ART. Layout by sea_layouts_3.py (docs/sea-charts/grammar-forecast.png),
painted by ChatGPT on 2026-11-09 with Gerundia as the style; six dots,
measured by sea_measure.py into forecast_chart.json. The sea-area grid was
measured off the clean chart (dashed lines at x 345, 725, 1100, 1492 and
y 146, 523, 918).
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE

OUT = 'sailing-the-seas-forecast.html'
ART = 'sailing-the-seas-forecast'
UID = 'fct'

# py lesson-template/extract-palette.py sailing-the-seas-forecast/hero.jpg --light
EXTRACTED = {'text': '#2a2211', 'text-dim': '#5e4f2e', 'secondary': '#b1ccd3', 'contrast': '#0b586b'}

D = O.load('forecast_chart.json')
DOTS = sorted((tuple(p) for p in D['dots']), key=lambda p: (p[1] // 100, p[0]))
assert len(DOTS) == 6, DOTS
XS, YS = (345, 725, 1100, 1492), (146, 523, 918)

# (area, the words, about, the forecast)
AREAS = [
    ('BOUND', 'is bound to', '100%', 'It is bound to rain.'),
    ('WILL', 'will &#183; is sure to', '95%', 'It will rain tonight.'),
    ('LIKELY', 'is likely to &#183; will probably', '75%', 'It will probably rain.'),
    ('MAYBE', 'may &#183; might &#183; could', '50%', 'It might rain later.'),
    ('UNLIKELY', 'is unlikely to &#183; probably won&#8217;t', '25%', 'It probably won&#8217;t rain.'),
    ('WON&#8217;T', 'won&#8217;t &#183; definitely won&#8217;t', '0%', 'It definitely won&#8217;t rain.'),
]
INK, SEA = '#10303C', '#BED7DE'


def key(a):
    return a.lower().replace('&#8217;', '')


def overlay():
    spots, names = [], []
    for i, ((x, y), (area, words, pc, sent)) in enumerate(zip(DOTS, AREAS)):
        col, row = i % 3, i // 3
        assert XS[col] < x < XS[col + 1] and YS[row] < y < YS[row + 1], 'dot %d is out of its sea area' % i
        names.append(O.name(x, y, (area, 'about ' + pc, area), INK, SEA, size=27, dy=-20, fit=False, weight=700,
                            halo=.4))
        names.append(O.name(x, y, (words, words, sent), INK, SEA, size=19, dy=38, fit=False, halo=.4))
        spots.append(O.hotspot(UID, key(area), O.rect_path(XS[col] + 6, YS[row] + 6, XS[col + 1] - 6, YS[row + 1] - 6),
                               '%s: %s, about %s' % (area, words, pc)))
    spots.append(O.hotspot(UID, 'coast', O.rect_path(28, 150, 300, 1000), 'The coast: the forecast'))
    caps = [O.cap(907, 60, 'THE GRAMMAR FORECAST', INK, 38, face=O.SERIF, spacing='.04em'),
            O.cap(907, 92, 'how sure are we? read the sea area', INK, 19, face=O.SERIF, weight=600, spacing='0',
                  style='italic'),
            O.cap(156, 950, 'THE COAST', '#20180A', 26, face=O.SERIF, spacing='.04em', halo='#E6E2C4'),
            O.cap(918, 960, 'Rain is likely to reach the coast by evening.', INK, 19, face=O.SERIF, weight=600,
                  spacing='0', style='italic')]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated weather chart: a green coast with a lighthouse and harbour on the west, and the sea split '
            'into six areas. BOUND, is bound to, about 100%, under heavy rain; WILL, will or is sure to, 95%, under '
            'dark cloud; LIKELY, is likely to or will probably, 75%, under gathering cloud; MAYBE, may, might or '
            'could, 50%, in sun and cloud; UNLIKELY, is unlikely to or probably won&#8217;t, 25%, mostly fair; '
            'WON&#8217;T, won&#8217;t or definitely won&#8217;t, 0%, under a clear sky. Below: Rain is likely to '
            'reach the coast by evening.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; probability and prediction', 'The Grammar Forecast',
    'A forecast is a guess with a number on it. English has a word for every number: <em>is bound to</em> when '
    'you are certain, <em>might</em> when it could go either way, <em>won&#39;t</em> when you would bet against it. '
    'On this chart the weather in each sea area shows how sure you are. Read the sky, then pick the words.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the forecast</div>
      <h2>How sure are you?</h2>
      <p class="chart-note" style="margin:-6px 0 18px">These are all ways of talking about the future, or about something you cannot see. The percentages are rough; what matters is the order.</p>
      ''' + rule_grid([
    ('<em>Bound to</em>, <em>sure to</em>: almost certain',
     'Use them when you have good reasons. They often sound like a warning or a joke.',
     ex('The ferry is <em>bound to</em> be late in this wind.')),
    ('<em>Will</em> and <em>won&#39;t</em>: a confident forecast',
     'The plain prediction: you are sure, but you are not promising.',
     ex('It <em>will</em> rain tonight.')),
    ('<em>Probably</em>: after <em>will</em>, before <em>won&#39;t</em>',
     'The word order is the commonest mistake on this chart: <em>will probably</em>, but <em>probably won&#39;t</em>.',
     ex('She&#39;ll <em>probably</em> call later, but she <em>probably won&#39;t</em> come.')),
    ('<em>Likely</em> is an adjective',
     'It follows <em>be</em>: <em>is likely to</em>, <em>is unlikely to</em>. <em>Likely</em> on its own does not replace <em>probably</em>.',
     ex('The wind <em>is unlikely to</em> drop before Friday.')),
    ('<em>May</em>, <em>might</em>, <em>could</em>: either way',
     'All three mean about 50%. <em>Might</em> is the most common in speech.',
     ex('We <em>might</em> sail tomorrow.')),
    ('<em>Definitely</em> makes it 100% or 0%',
     '<em>Definitely</em> and <em>certainly</em> go in the same place as <em>probably</em>: after <em>will</em>, before <em>won&#39;t</em>.',
     ex('It <em>definitely won&#39;t</em> snow in July.')),
]) + chart(
    'The six sea areas',
    'From certain to impossible. Every row is a way of saying how likely rain is.',
    ['Sea area', 'About', 'The forecast'],
    [['BOUND', '100%', 'It is bound to rain.'], ['WILL', '95%', 'It will rain. / It is sure to rain.'],
     ['LIKELY', '75%', 'It is likely to rain. / It will probably rain.'],
     ['MAYBE', '50%', 'It may rain. / It might rain. / It could rain.'],
     ['UNLIKELY', '25%', 'It is unlikely to rain. / It probably won&#39;t rain.'],
     ['WON&#39;T', '0%', 'It won&#39;t rain. / It definitely won&#39;t rain.']]) + '''
    </div>

    '''

PATTERNS = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The shipping forecast</div>
      <h2>Three ways to say <em>likely</em></h2>
      <p class="chart-note" style="margin:-6px 0 18px">A weather forecaster rarely says <em>maybe</em>. These patterns sound more precise, and they turn up in reports, news and exam essays.</p>
      ''' + chart(
    'Likely, chance, possible',
    'Each pattern has its own shape. Learn the shape with the word.',
    ['Pattern', 'Example'],
    [['something <em>is likely to</em> + verb', 'Rain is likely to reach the coast by evening.'],
     ['<em>It is likely that</em> + clause', 'It is likely that the ferry will be cancelled.'],
     ['<em>There is a good chance of</em> + noun', 'There is a good chance of fog.'],
     ['<em>There is a good chance (that)</em> + clause', 'There is a good chance we will be late.'],
     ['<em>It is possible that</em> + clause', 'It is possible that the storm will turn north.']]) + '''
      ''' + exi('There&#39;s a <em>good chance of</em> rain this afternoon.') + chart(
    'Not only the weather',
    'The same words forecast anything you cannot see yet.',
    ['Certainty', 'Example'],
    [['bound to', 'He&#39;s bound to forget his keys.'], ['will', 'You&#39;ll love the island.'],
     ['likely to', 'Prices are likely to rise.'], ['might', 'I might be a bit late.'],
     ['unlikely to', 'The ship is unlikely to arrive before noon.'], ['won&#39;t', 'She won&#39;t mind.']]) + '''
      ''' + exi('The storm <em>is likely to</em> hit the coast tonight.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a sea area and its line lights up below. Switch the chart to see each area as a rough percentage, then '
    'as a forecast: the sky clears as the words grow less certain.',
    ('The sea areas', 'How sure', 'The forecast'),
    [('Likely to happen', 'is-west'), ('Less and less likely', 'is-isle'), ('The coast', 'is-east')],
    'Drag the chart sideways to reach the eastern areas.', min_zoom=1000)

TRAPS = fork(
    'Storm warnings',
    'The commonest mistakes are about word order and about <em>likely</em>.',
    ['Not this', 'This', 'Why'],
    [['It probably will rain.', 'It will probably rain.', '<em>probably</em> after <em>will</em>'],
     ['It won&#39;t probably rain.', 'It probably won&#39;t rain.', '<em>probably</em> before <em>won&#39;t</em>'],
     ['It will likely to rain.', 'It is likely to rain.', '<em>likely</em> follows <em>be</em>'],
     ['Rain is likely reach the coast.', 'Rain is likely to reach the coast.', '<em>likely to</em> + verb'],
     ['It is bound rain.', 'It is bound to rain.', '<em>bound to</em> + verb'],
     ['Maybe it might rain.', 'It might rain. / Maybe it will rain.', 'one <em>maybe</em> is enough']],
    'American English often says <em>It will likely rain</em>. British English prefers <em>It is likely to rain</em> or '
    '<em>It will probably rain</em>.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-question-tags.html', 'The return voyage')])

SIGNALS = signals(
    'You are sure',
    ['<em>is bound to</em>, <em>is sure to</em>', '<em>will</em>, <em>won&#39;t</em>',
     '<em>definitely</em>, <em>certainly</em>', '<em>There&#39;s no doubt that&#8230;</em>',
     '<em>I&#39;m sure (that)&#8230;</em>'],
    'You are not sure',
    ['<em>may</em>, <em>might</em>, <em>could</em>', '<em>is likely to</em>, <em>is unlikely to</em>',
     '<em>probably</em>, <em>possibly</em>, <em>perhaps</em>', '<em>There&#39;s a good chance of&#8230;</em>',
     '<em>I doubt (that)&#8230;</em>'],
    'One test: put a number on it. Over 90%, the left column; between 10% and 90%, the right.')

QUIZ = [
    ('The sky is black. It ___ rain any minute.', 'Almost certain.', 'is bound to',
     ['is bound to', 'might', 'is unlikely to', 'won&#39;t'], 'Black sky: is bound to, about 100%.'),
    ('It will ___ rain this evening.', 'Probably, with will.', 'probably',
     ['probably', 'likely', 'probable', 'be probably'], 'Will probably: probably goes after will.'),
    ('It ___ rain: the sky is clear.', 'Probably not, with won&#39;t.', 'probably won&#39;t',
     ['probably won&#39;t', 'won&#39;t probably', 'will probably not to', 'probably not will'], 'Probably goes before won&#39;t.'),
    ('Rain ___ reach the coast by evening.', 'About 75%.', 'is likely to',
     ['is likely to', 'is likely', 'likely to', 'will likely to'], 'Is likely to + verb.'),
    ('We ___ sail tomorrow: it depends on the wind.', 'Either way.', 'might',
     ['might', 'are bound to', 'definitely won&#39;t', 'will certainly'], 'It depends: about 50%, might.'),
    ('The wind is ___ to drop before Friday.', 'About 25%.', 'unlikely',
     ['unlikely', 'not likely to', 'unlikely to to', 'impossible'], 'Is unlikely to: the opposite of is likely to.'),
    ('There is a good chance ___ fog tonight.', 'Chance + a noun.', 'of',
     ['of', 'to', 'for', 'that'], 'A good chance of + noun: a good chance of fog.'),
    ('It ___ snow in July: it never does.', 'About 0%.', 'definitely won&#39;t',
     ['definitely won&#39;t', 'won&#39;t definitely', 'might', 'is likely to'], 'Definitely goes before won&#39;t.'),
    ('Which is about 50%?', 'Read the sky.', 'It may rain.',
     ['It may rain.', 'It is bound to rain.', 'It won&#39;t rain.', 'It is sure to rain.'], 'May, might and could are about 50%.'),
    ('It is likely ___ the ferry will be cancelled.', 'It is likely + a clause.', 'that',
     ['that', 'to', 'of', 'for'], 'It is likely that + a full clause.'),
    ('Which sentence is correct?', 'Watch likely.', 'Prices are likely to rise.',
     ['Prices are likely to rise.', 'Prices will likely to rise.', 'Prices likely rise.', 'Prices are likely rise.'],
     'Be + likely to + verb.'),
    ('Which is the MOST certain?', 'The darkest sky.', 'He&#39;s bound to be late.',
     ['He&#39;s bound to be late.', 'He&#39;ll probably be late.', 'He might be late.', 'He&#39;s unlikely to be late.'],
     'Bound to is about 100%.'),
]

PANELS = [
    [(key(a[0]), '<b>%s</b> %s &middot; about %s' % (a[0], a[1], a[2])) for a in AREAS[:3]],
    [(key(a[0]), '<b>%s</b> %s &middot; about %s' % (a[0], a[1], a[2])) for a in AREAS[3:]],
    [('coast', '<b>The forecast</b> <em>Rain is likely to reach the coast by evening.</em>'),
     ('coast', '<b>Word order</b> <em>will probably</em>, but <em>probably won&#39;t</em>'),
     ('coast', '<b>Likely</b> follows <em>be</em>: <em>is likely to</em>, <em>is unlikely to</em>')],
]
TARGETS = {}
for i, a in enumerate(AREAS):
    TARGETS[key(a[0])] = (0 if i < 3 else 1, key(a[0]), '#0b586b')
TARGETS['coast'] = (2, 'coast', '#0b586b')

import ex_tr_forecast as T
L.build(OUT, ART, 'The Grammar Forecast &mdash; Probability and Prediction', 'probability and prediction', EXTRACTED,
        HERO, 'Read the sky, then pick the words.', ('order', 'Read the chart'),
        RULES + PATTERNS + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        ['#8E9AA8', '#E9D9A0', '#B9CC92'], T.T,
        ['Clean run. You can read the sky and put the right words on it.',
         'Solid progress. Remember the order: will probably, probably won&#8217;t.',
         'Good first attempt. Start with the six sea areas, from bound to won&#8217;t.'],
        ('sailing-the-seas-phrasal-verbs.html', 'Next chart: the particle ferries'), gull_seed=47, long_name=30)
