# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: The Atlas of THE, articles with place names
as two shores. The thirteenth chart.

    py lesson-template/build/build_atlas.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. Whether a place name takes THE depends on the KIND of
place, so the chart sorts kinds, one harbour each. The west shore, THE-LAND,
holds the kinds that take it: oceans, seas, rivers, deserts, mountain
ranges, island groups, plural countries, unions. The east shore,
NO-THE-LAND, holds the kinds that do not: continents, countries, cities,
lakes, single mountains, single islands, streets, squares. The pairs face
each other on purpose: a range against one mountain, a group of islands
against one island, a plural country against a country. The Shallows hold
the names older maps still write with THE (the Sudan, the Lebanon); the
False Cape holds the names that break their kind's rule (the Hague, the
Gambia, the Matterhorn).

THE ART. Layout by sea_layouts_4.py (docs/sea-charts/atlas-of-the.png),
painted on 2026-11-13 with Gerundia as the style. sea_measure.py found all
16 dots (atlas_chart.json). No tense on this chart, so no Sherpa colours.
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE

OUT = 'sailing-the-seas-atlas.html'
ART = 'sailing-the-seas-atlas'
UID = 'atlas'

# py lesson-template/extract-palette.py sailing-the-seas-atlas/hero.jpg --light
EXTRACTED = {'text': '#2a2411', 'text-dim': '#5e532e', 'secondary': '#b0d0d9', 'contrast': '#0d4e68'}

D = O.load('atlas_chart.json')
WEST = sorted((tuple(p) for p in D['dots'] if p[0] < 768), key=lambda p: p[1])
EAST = sorted((tuple(p) for p in D['dots'] if p[0] > 768), key=lambda p: p[1])
assert len(WEST) == len(EAST) == 8, D['dots']

# (name, kind, the kind as a rule, a sentence)
THE = [
    ('the Atlantic', 'ocean', 'oceans: THE', 'We crossed the Atlantic.'),
    ('the Mediterranean', 'sea', 'seas: THE', 'We swam in the Mediterranean.'),
    ('the Thames', 'river', 'rivers: THE', 'The Thames runs through London.'),
    ('the Sahara', 'desert', 'deserts: THE', 'Nothing grows in the Sahara.'),
    ('the Alps', 'mountain range', 'mountain ranges: THE', 'We ski in the Alps.'),
    ('the Canaries', 'island group', 'island groups: THE', 'They flew to the Canaries.'),
    ('the Netherlands', 'plural country', 'plural countries: THE', 'She works in the Netherlands.'),
    ('the USA', 'union of states', 'unions and republics: THE', 'He studied in the USA.'),
]
NO = [
    ('Europe', 'continent', 'continents: no THE', 'We travelled round Europe.'),
    ('France', 'country', 'countries: no THE', 'They moved to France.'),
    ('Paris', 'city', 'cities: no THE', 'I love Paris in spring.'),
    ('Lake Como', 'lake', 'lakes: no THE', 'We stayed at Lake Como.'),
    ('Mount Everest', 'single mountain', 'one mountain: no THE', 'She climbed Mount Everest.'),
    ('Malta', 'single island', 'one island: no THE', 'Malta is tiny.'),
    ('Oxford Street', 'street', 'streets: no THE', 'We shopped in Oxford Street.'),
    ('Trafalgar Square', 'square', 'squares: no THE', 'Meet me in Trafalgar Square.'),
]
INK, WEST_LAND, EAST_LAND, SAND = '#20180A', '#C5C88A', '#EFCA90', '#FBDDA7'


def key(side, name):
    return side + '-' + name.replace('the ', '').replace(' ', '-').lower()


def overlay():
    spots, names = [], []
    for (t, n), (wx, wy), (ex_, ey) in zip(zip(THE, NO), WEST, EAST):
        names.append(O.name(wx, wy, (t[0], t[2], t[3]), INK, WEST_LAND, size=19, dy=-17, fit=False, halo=.1))
        names.append(O.name(ex_, ey, (n[0], n[2], n[3]), INK, EAST_LAND, size=19, dy=-17, fit=False, halo=.1))
        spots.append(O.hotspot(UID, key('the', t[0]), O.circle_path(wx, wy, 32), '%s: %s' % (t[0], t[2])))
        spots.append(O.hotspot(UID, key('no', n[0]), O.circle_path(ex_, ey, 32), '%s: %s' % (n[0], n[2])))
    spots.append(O.hotspot(UID, 'shallows', O.rect_path(594, 286, 916, 458), 'The Shallows: older maps keep THE'))
    spots.append(O.hotspot(UID, 'cape', O.rect_path(590, 692, 940, 920), 'The False Cape: names that break the rule'))
    sea_ink = '#0F2F3D'
    caps = [O.cap(768, 62, 'THE ATLAS OF THE', sea_ink, 40, face=O.SERIF, spacing='.05em'),
            O.cap(768, 98, 'does the place take THE? read the shore', sea_ink, 20, face=O.SERIF, weight=600, spacing='0',
                  style='italic'),
            O.cap(291, 180, 'THE-LAND', INK, 31, face=O.SERIF, spacing='.03em', halo=WEST_LAND),
            O.cap(1246, 180, 'NO-THE-LAND', INK, 31, face=O.SERIF, spacing='.03em', halo=EAST_LAND),
            O.cap(757, 352, 'THE SHALLOWS', INK, 22, face=O.SERIF, spacing='.04em'),
            O.cap(757, 382, 'older maps keep the', INK, 17, weight=600, spacing='0', style='italic'),
            O.cap(757, 408, '(the) Sudan &#183; (the) Lebanon', INK, 17, weight=600, spacing='0', style='italic'),
            O.cap(765, 872, 'THE FALSE CAPE', sea_ink, 22, face=O.SERIF, spacing='.04em'),
            O.cap(765, 902, 'the Hague &#183; the Gambia &#183; the Matterhorn', sea_ink, 17, weight=600, spacing='0',
                  style='italic')]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated chart with two shores. On the green west shore, THE-LAND, eight harbours: the Atlantic, '
            'the Mediterranean, the Thames, the Sahara, the Alps, the Canaries, the Netherlands and the USA. On the '
            'sandy east shore, NO-THE-LAND, eight more: Europe, France, Paris, Lake Como, Mount Everest, Malta, Oxford '
            'Street and Trafalgar Square. In the channel a sandbank, the Shallows, says older maps keep the: (the) '
            'Sudan, (the) Lebanon. To the south a spit with a red flag is the False Cape: the Hague, the Gambia, the '
            'Matterhorn.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; Articles with place names', 'The Atlas of THE',
    'Why <em>the</em> Alps but Mount Everest? Why <em>the</em> Netherlands but France? The answer is the kind of '
    'place, not the place. Every kind has its harbour: the west shore takes THE, the east shore does not. '
    'Read the chart across, kind against kind, then name the world correctly.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the atlas</div>
      <h2>Ask what kind of place it is</h2>
      <p class="chart-note" style="margin:-6px 0 18px">You do not have to learn every name. Learn the sixteen kinds, and a new name goes to the right shore by itself.</p>
      ''' + rule_grid([
    ('Water you sail on takes THE',
     'Oceans, seas and rivers all take THE. So do canals and channels.',
     ex('We crossed <em>the Atlantic</em> and sailed up <em>the Thames</em>.')),
    ('A lake does not',
     'A lake is the one piece of water with no THE. The word <em>Lake</em> usually comes first.',
     ex('We stayed at <em>Lake Como</em> for a week.')),
    ('Many take THE, one does not',
     'A range of mountains or a group of islands takes THE. One mountain or one island does not.',
     ex('We ski in <em>the Alps</em>, but she climbed <em>Mount Everest</em>.')),
    ('Countries: plural or a union takes THE',
     'Most countries have no THE. A plural name, or a name with <em>States</em>, <em>Kingdom</em> or <em>Republic</em>, takes it.',
     ex('She lives in <em>the Netherlands</em>, but she works in <em>France</em>.')),
    ('Continents and cities do not',
     'A continent, a city, a town or a village stands alone.',
     ex('I love <em>Paris</em>. It is my favourite city in <em>Europe</em>.')),
    ('Streets and squares do not',
     'Streets, roads, squares and parks have no THE. Deserts do.',
     ex('Meet me in <em>Trafalgar Square</em>, not in <em>the Sahara</em>.')),
]) + chart(
    'The sixteen kinds',
    'Read each row across the channel. The two kinds on a row are easy to confuse, which is why they face each other.',
    ['THE-LAND', 'NO-THE-LAND', 'More of the same'],
    [['the Atlantic (ocean)', 'Europe (continent)', 'the Pacific / Asia'],
     ['the Mediterranean (sea)', 'France (country)', 'the Baltic / Japan'],
     ['the Thames (river)', 'Paris (city)', 'the Nile / Cairo'],
     ['the Sahara (desert)', 'Lake Como (lake)', 'the Gobi / Lake Geneva'],
     ['the Alps (mountain range)', 'Mount Everest (one mountain)', 'the Andes / Mount Fuji'],
     ['the Canaries (island group)', 'Malta (one island)', 'the Bahamas / Sicily'],
     ['the Netherlands (plural country)', 'Oxford Street (street)', 'the Philippines / Fifth Avenue'],
     ['the USA (union of states)', 'Trafalgar Square (square)', 'the UK / Times Square']]) + '''
    </div>

    '''

CAPE = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The Shallows and the False Cape</div>
      <h2>Names in between, and names that break the rule</h2>
      <p class="chart-note" style="margin:-6px 0 18px">In the Shallows the old maps and the new maps disagree. At the False Cape a name looks like one kind and behaves like the other, so these few are learned by heart.</p>
      ''' + chart(
    'The Shallows: older maps keep THE',
    'These countries once took THE. Modern English usually drops it, and you will still meet both.',
    ['Older', 'Now', 'Note'],
    [['the Sudan', 'Sudan', 'no THE is the safe choice'],
     ['the Lebanon', 'Lebanon', 'no THE is the safe choice'],
     ['the Ukraine', 'Ukraine', 'always without THE now'],
     ['the Argentine', 'Argentina', 'the old form is very rare']]) + '''
      ''' + exi('My grandfather always said <em>the Lebanon</em>. I say <em>Lebanon</em>.') + chart(
    'The False Cape: names that break the rule',
    'Each of these sits on the wrong shore for its kind.',
    ['Name', 'Its kind', 'So you expect', 'But it is'],
    [['the Hague', 'city', 'no THE', '<em>the</em> Hague'],
     ['the Gambia', 'country', 'no THE', '<em>the</em> Gambia'],
     ['the Matterhorn', 'one mountain', 'no THE', '<em>the</em> Matterhorn'],
     ['the High Street', 'street', 'no THE', '<em>the</em> High Street (in Britain)']]) + '''
      ''' + exi('The court sits in <em>the Hague</em>, a city in <em>the Netherlands</em>.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a harbour and its line lights up below: THE-LAND on the left, NO-THE-LAND in the middle. Switch the '
    'chart to see what kind of place each harbour stands for, then each name in a sentence.',
    ('The places', 'The kind of place', 'In a sentence'),
    [('THE-LAND', 'is-west'), ('NO-THE-LAND', 'is-isle'), ('The Shallows and the False Cape', 'is-east')],
    'Drag the chart sideways to reach NO-THE-LAND.', min_zoom=1000)

TRAPS = fork(
    'Wrong shore',
    'Each of these lands a name on the wrong side of the channel.',
    ['Not this', 'This', 'Why'],
    [['We went skiing in Alps.', 'We went skiing in the Alps.', 'a mountain range: THE'],
     ['She climbed the Mount Everest.', 'She climbed Mount Everest.', 'one mountain: no THE'],
     ['He lives in the France.', 'He lives in France.', 'a country: no THE'],
     ['I come from Netherlands.', 'I come from the Netherlands.', 'a plural country: THE'],
     ['We stayed at the Lake Como.', 'We stayed at Lake Como.', 'a lake: no THE'],
     ['The shop is in the Oxford Street.', 'The shop is in Oxford Street.', 'a street: no THE']],
    'One test before you write a name: is it one thing, or many? Is it water you sail on? That decides most of them.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-atlantic.html', 'The Atlantic')])

SIGNALS = signals(
    'You are in THE-LAND',
    ['an ocean, a sea, a river', 'a desert', 'a plural name: <em>the Alps</em>, <em>the Canaries</em>',
     'a plural country: <em>the Netherlands</em>', '<em>States</em>, <em>Kingdom</em>, <em>Republic</em> in the name',
     '<em>of</em> in the name: <em>the Isle of Wight</em>'],
    'You are in NO-THE-LAND',
    ['a continent, a country, a city', 'a lake: <em>Lake Como</em>', '<em>Mount</em> + one mountain',
     'one island: <em>Malta</em>, <em>Sicily</em>', 'a street, a road, a square', 'a park or a station: <em>Hyde Park</em>'],
    'One test: a plural name almost always takes THE. <em>The Alps</em>, <em>the Canaries</em>, <em>the Netherlands</em>, <em>the Philippines</em>.')

QUIZ = [
    ('We sailed across ___ last summer.', 'An ocean.', 'the Atlantic',
     ['the Atlantic', 'Atlantic', 'an Atlantic', 'the Atlantics'], 'An ocean takes THE: the Atlantic.'),
    ('They have a house near ___.', 'A lake.', 'Lake Como',
     ['Lake Como', 'the Lake Como', 'the Como Lake', 'a Lake Como'], 'A lake has no THE: Lake Como.'),
    ('We go skiing in ___ every winter.', 'A mountain range.', 'the Alps',
     ['the Alps', 'Alps', 'the Alp', 'an Alps'], 'A mountain range takes THE: the Alps.'),
    ('She was the first woman to climb ___.', 'One mountain.', 'Mount Everest',
     ['Mount Everest', 'the Mount Everest', 'the Everest Mount', 'a Mount Everest'], 'One mountain has no THE: Mount Everest.'),
    ('My sister works in ___.', 'A plural country.', 'the Netherlands',
     ['the Netherlands', 'Netherlands', 'the Netherland', 'a Netherlands'], 'A plural country takes THE: the Netherlands.'),
    ('They moved to ___ in 2019.', 'A country.', 'France',
     ['France', 'the France', 'a France', 'the Frances'], 'Most countries have no THE: France.'),
    ('___ runs through the middle of London.', 'A river.', 'The Thames',
     ['The Thames', 'Thames', 'A Thames', 'The Thame'], 'A river takes THE: the Thames.'),
    ('We spent a week in ___.', 'A group of islands.', 'the Canaries',
     ['the Canaries', 'Canaries', 'the Canary', 'a Canaries'], 'A group of islands takes THE: the Canaries.'),
    ('___ is a small island south of Sicily.', 'One island.', 'Malta',
     ['Malta', 'The Malta', 'A Malta', 'The Maltas'], 'One island has no THE: Malta.'),
    ('The best shops are in ___.', 'A street.', 'Oxford Street',
     ['Oxford Street', 'the Oxford Street', 'the Street Oxford', 'an Oxford Street'], 'A street has no THE: Oxford Street.'),
    ('Which city breaks the rule and takes THE?', 'The False Cape.', 'the Hague',
     ['the Hague', 'the Paris', 'the Rome', 'the Madrid'], 'Cities have no THE, but the Hague keeps it.'),
    ('Which sentence is right?', 'Check each shore.', 'He studied in the USA and now lives in Europe.',
     ['He studied in the USA and now lives in Europe.', 'He studied in USA and now lives in the Europe.',
      'He studied in the USA and now lives in the Europe.', 'He studied in USA and now lives in Europe.'],
     'A union of states takes THE; a continent does not.'),
]

PANELS = [
    [(key('the', t[0]), '<b>%s</b> %s' % (t[0], t[2].split(':')[0])) for t in THE],
    [(key('no', n[0]), '<b>%s</b> %s' % (n[0], n[2].split(':')[0])) for n in NO],
    [('shallows', '<b>The Shallows</b> older maps keep THE: <em>(the) Sudan</em>, <em>(the) Lebanon</em>'),
     ('cape', '<b>The False Cape</b> <em>the Hague</em>: a city, but THE'),
     ('cape', '<em>the Gambia</em>: a country, but THE &middot; <em>the Matterhorn</em>: one mountain, but THE')],
]
TARGETS = {}
for t in THE:
    TARGETS[key('the', t[0])] = (0, key('the', t[0]), '#0d4e68')
for n in NO:
    TARGETS[key('no', n[0])] = (1, key('no', n[0]), '#0d4e68')
TARGETS['shallows'] = (2, 'shallows', '#0d4e68')
TARGETS['cape'] = (2, 'cape', '#B4441F')

import ex_tr_atlas as T
L.build(OUT, ART, 'The Atlas of THE &mdash; Articles with Place Names', 'Articles with place names', EXTRACTED,
        HERO, 'then name the world correctly.', ('order', 'Read the chart'),
        RULES + CAPE + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        [WEST_LAND, EAST_LAND, SAND], T.T,
        ['Clean run. You can read the atlas: the kind of place tells you the article.',
         'Solid progress. Check the pairs again: a range against one mountain, a group against one island.',
         'Good first attempt. Start with water: oceans, seas and rivers take THE, a lake does not.'],
        ('sailing-the-seas-atlantic.html', 'Next chart: the Atlantic'), gull_seed=53, long_name=22)
