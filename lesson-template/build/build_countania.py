# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: Countania & Uncountania, countable and
uncountable nouns as a sea chart and a ship. The third chart in the series.

    py lesson-template/build/countania_clean.py      # only if the clean draft changes
    py lesson-template/build/build_countania.py
    py tools/build_hubs.py && py tools/seo.py

Built on the same machinery as build_regularia.py (and build_sailing.py
before it): the Sherpa camp shell, the clickable chart, the fourteen-question
crossing, the nine-language example reveal. Read build_sailing.py's
docstring for why the shell is borrowed and the mountain's progression
stripped.

THE TEACHING IDEA. Two shores face each other across a strait. Countania
holds the things you count (a chair, three chairs, many chairs); Uncountania
holds the stuff you measure (furniture, much furniture, no -s, ever). Every
uncountable harbour faces its countable partner at the same latitude with the
same surname (Furniture Crag / Chair Crag): the trap is on the east shore and
the way out is straight across. The piece-of ferry is the only way to count
something from Uncountania; Double Isle holds the nouns that live on both
shores with two meanings (a coffee / coffee); the Shallows hold the words that
work on either (some, any, a lot of); the False Cape flies an -S it has no
right to (the news is).

THE SHIP. Innes, 2026-09-30, wanted "two pictures of rooms full of one or the
other with an interim space where they share stuff", in a ship, in this
lesson. The store cabin (room-count) and the cargo hold (room-bulk) are his
ChatGPT paintings; the words are pinned on by the page. The third room, the
galley (the single thing beside the stuff: a coffee by a sack of coffee), was
never painted (brief: docs/CHATGPT-SEA-CHARTS-BRIEF.md part 1, `room-galley`).
Until it is, the galley is a written card in the same place. When the
picture arrives: drop it in incoming/sea-charts/room-galley.png, copy it to
sailing-the-seas-countania/room-galley.jpg, and set GALLEY_IMG below.

THE ART. hero.jpg is Codex's labelled repaint (2026-10-04) and
chart-clean.jpg the same chart with every word removed, two stray dots
painted out by countania_clean.py. The clean one is labelled live by
countania_map.py from coordinates measured by countania_measure.py.

PALETTE. Derived from hero.jpg by extract-palette.py --light (every row
PASS; block below). The page accent is that block's `contrast`, the sea teal,
as on the first two charts, so the series reads as one.
"""
import os, re, sys, glob, json
sys.path.insert(0, 'lesson-template')
sys.path.insert(0, 'lesson-template/build')
sys.path.insert(0, 'lesson-template/build/sherpa/legacy')
import regularia_map as R
import countania_map as M

_SNAP = {f: open(f, 'rb').read() for f in glob.glob('sherpa-tensing-camp-*.html')}
from build_c10 import assemble, hero, rule_grid, MARK_FLAG, MARK_TABLE, MARK_FORK, MARK_CLOCK, MARK_PANES
from build_c11_12_13 import chart, fork, signals, questions, palette
for _f, _b in _SNAP.items():
    if open(_f, 'rb').read() != _b:
        open(_f, 'wb').write(_b)
        print('restored', _f)

OUT = 'sailing-the-seas-countania.html'
ART = 'sailing-the-seas-countania'
GALLEY_IMG = None              # 'sailing-the-seas-countania/room-galley.jpg' once it is painted

# ── the ship's rooms: web copies of Innes's paintings ─────────────────
from PIL import Image
for _src, _dst in (('incoming/sea-charts/room-count.png', ART + '/room-count.jpg'),
                   ('incoming/sea-charts/room-bulk.png', ART + '/room-bulk.jpg')):
    if not os.path.exists(_dst):
        if not os.path.exists(_src):
            sys.exit('! %s is missing and %s is not there to make it from' % (_dst, _src))
        Image.open(_src).convert('RGB').save(_dst, 'JPEG', quality=84, optimize=True, progressive=True)
        print('made', _dst)
    assert Image.open(_dst).size == (1536, 1024), _dst

# ── palette ───────────────────────────────────────────────────────────
# py lesson-template/extract-palette.py sailing-the-seas-countania/hero.jpg --light
EXTRACTED = {
    'void': '#bacabc', 'surface': '#ced7d0', 'surface2': '#c4d0c5', 'border': '#96714a',
    'text': '#2a1e11', 'text-dim': '#5e472e', 'accent': '#824505', 'accent-bright': '#63380b',
    'accent-dim': '#e4831e', 'secondary': '#a7c9d0', 'contrast': '#075355',
}
ACCENT = EXTRACTED['contrast']
PAPER = R.mix(EXTRACTED['secondary'], '#FFFFFF', .82)
DARK = R.mix(ACCENT, '#000000', .3)
LIGHT = R.mix(ACCENT, '#FFFFFF', .7)
LIGHTER = R.mix(ACCENT, '#FFFFFF', .9)
for fg, bg, need, what in [(EXTRACTED['text'], PAPER, 7, 'ink on paper'),
                           (EXTRACTED['text-dim'], PAPER, 4.5, 'soft ink on paper'),
                           (ACCENT, PAPER, 4.5, 'accent on paper'),
                           ('#FFFFFF', ACCENT, 4.5, 'white on accent'),
                           (DARK, LIGHTER, 4.5, 'dark on lighter')]:
    r = R.ratio(fg, bg)
    assert r >= need, 'palette: %s is %.2f:1, needs %s' % (what, r, need)
PALETTE = palette(EXTRACTED['text'], EXTRACTED['text-dim'], PAPER, ACCENT, DARK, LIGHT, LIGHTER)


def panel_css(cls, paint):
    bg = R.mix(paint, '#FFFFFF', .84)
    return ('  .diagram-panel.%s{background:%s;border-color:%s;}\n'
            '  .diagram-panel.%s h4{color:%s;}\n'
            % (cls, bg, R.mix(paint, '#FFFFFF', .45), cls, R.ink_for(bg, 7)))


# tags pinned to the rooms take their land's colours: the cabin is Countania,
# the hold Uncountania
def tag_css(cls, paint):
    bg = R.mix(paint, '#FFFFFF', .72)
    ink = R.ink_for(bg, 7)
    assert R.ratio(ink, bg) >= 7
    return '  .room-tag.%s{background:%s;color:%s;border-color:%s;}\n' % (cls, bg, ink, R.mix(paint, '#000000', .25))


# ── the examples that carry a translation, in page order ──────────────
EX = []


def ex(html):
    EX.append(html)
    return '\x01%d\x01%s' % (len(EX) - 1, html)


def exi(html):
    EX.append(html)
    return ('<p class="ex" data-tr="%d" style="margin:14px 0 0">%s</p>' % (len(EX) - 1, html))


HERO_MAP_ALT = (
    'An illustrated sea chart. On the west, an orange land called Countania, with harbours named after '
    'countable nouns: Job Harbour, Fact Point, Tip Head, Suitcase Sands, Chair Crag and others. On the east, '
    'a golden land called Uncountania, whose harbours face them at the same latitude: Work Harbour, '
    'Information Point, Advice Head, Luggage Sands, Furniture Crag. In the strait lies a lilac island, Double '
    'Isle (both shores, two meanings: Coffee Cove, Chicken Crag, Paper Point). A ferry runs west, labelled '
    'a piece of advice, a bottle of water, a slice of bread. A spur of Uncountania flies an -S flag: the False '
    'Cape, the news is, maths is. A sandbank in the south, the Shallows, holds some, any, a lot of, plenty of.')

HERO = hero(
    'Sailing the Seas of Grammar &middot; nouns',
    'Countania &amp; Uncountania',
    'Two shores face each other across a strait. On the west live the things you count: a chair, three chairs, '
    'many chairs. On the east lives the stuff you measure: furniture, much furniture, and never an <em>-s</em>. '
    'Every harbour on the east shore has a partner directly across the water, so when a word catches you out, '
    'the way back is straight ahead. Start below deck, in the ship.',
    '<button type="button" class="hero-diagram-btn" id="hero-map-btn" aria-label="Expand the map">'
    '<img class="hero-diagram" src="%s/hero.jpg" alt="%s" width="1536" height="1024" loading="eager">'
    '</button>'
    '<div class="img-lightbox" id="hero-lightbox">'
    '<button type="button" class="lightbox-close" aria-label="Close">&times;</button>'
    '<img src="%s/hero.jpg" alt="%s">'
    '</div>' % (ART, HERO_MAP_ALT, ART, HERO_MAP_ALT))

# ═════════════════════════════════════════════════════════════════════
# THE SHIP: the store cabin, the cargo hold, the galley between them.
# Tag positions are the centre of each tag in the painting's own pixels
# (1536 x 1024), each set beside the thing it names, never on a face of it.
CABIN_TAGS = [
    (300, 290, 'three chairs'), (715, 182, 'three loaves'), (1090, 122, 'four tools'),
    (1355, 68, 'six books'), (1355, 262, 'four bottles'), (1290, 528, 'three letters'),
    (560, 778, 'three suitcases'), (770, 842, 'nine coins'), (1390, 582, 'six apples'),
]
HOLD_TAGS = [
    (330, 432, 'grain'), (190, 640, 'sand'), (820, 520, 'coffee'), (1262, 700, 'rice'),
    (700, 715, 'water'), (610, 165, 'furniture'), (960, 232, 'luggage'), (1140, 392, 'money'),
    (1330, 330, 'mail'),
]


def room(img, alt, tags, cls, title, ask, sub):
    pins = ''.join('<span class="room-tag %s" style="left:%.2f%%;top:%.2f%%">%s</span>'
                   % (cls, x / 15.36, y / 10.24, t) for x, y, t in tags)
    return '''<figure class="room" data-map-zoom data-mz-target=".room-wrap" data-mz-ratio="1.5" data-mz-min="1000">
          <figcaption><span class="room-ask %s">%s</span> <b>%s</b> %s</figcaption>
          <div class="room-stage" data-mz-scroll>
            <div class="room-wrap">
              <img src="%s" alt="%s" width="1536" height="1024" loading="lazy">
              %s
            </div>
          </div>
        </figure>''' % (cls, ask, title, sub, img, alt, pins)


GALLEY_PAIRS = [('a coffee', 'coffee'), ('a chicken', 'chicken'), ('a paper', 'paper'),
                ('a glass', 'glass'), ('a cake', 'cake'), ('a light', 'light')]
if GALLEY_IMG:
    GALLEY = room(GALLEY_IMG, 'The ship&#39;s galley: single things beside the stuff they are made of.', [],
                  'is-both', 'The galley', 'BOTH', 'where the two meet')
else:
    GALLEY = '''<div class="galley">
          <p class="galley-h"><span class="room-ask is-both">BOTH</span> <b>The galley</b> where the two meet</p>
          <p>Between the cabin and the hold is the galley, and here every word has two lives. On the table stands one thing; beside it, the stuff it is made of.</p>
          <ul>%s</ul>
          <p class="galley-foot">The single thing counts; the stuff does not. These are the words of Double Isle, on the chart below.</p>
        </div>''' % ''.join('<li><b>%s</b> <span>beside</span> <i>%s</i></li>' % p for p in GALLEY_PAIRS)

SHIP = '''<div class="camp" id="ship">
      ''' + MARK_PANES + '''
      <div class="camp-label">Below deck</div>
      <h2>Two rooms in one ship</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Before the chart, the cargo. In the store cabin everything stands apart, and you can count it. In the hold everything is poured, piled or spilled, and you can only measure it. Look at what the two rooms share: chairs in one are furniture in the other, suitcases are luggage, coins are money, letters are mail. <strong>The same cargo, a different word.</strong></p>
      <div class="rooms">
        ''' + room(ART + '/room-count.jpg',
                   'The ship&#39;s store cabin: three wooden chairs, three loaves on a shelf, tools on hooks, books, bottles, '
                   'three letters on a desk, three suitcases, nine coins in a row on a table and a crate of apples.',
                   CABIN_TAGS, 'is-count', 'The store cabin', 'HOW MANY?', 'everything apart') + '''
        ''' + room(ART + '/room-bulk.jpg',
                   'The ship&#39;s cargo hold: grain pouring from a chute, heaps of sand, coffee beans and rice, water across '
                   'the floor, chairs and tables piled up, a stack of trunks, coins heaped on a chest and a sack spilling letters.',
                   HOLD_TAGS, 'is-bulk', 'The cargo hold', 'HOW MUCH?', 'everything heaped') + '''
      </div>
      ''' + chart(
    'The same cargo, a different word',
    'The cabin&#39;s word is the thing; the hold&#39;s word is the whole lot of it. Only the left-hand word takes <em>a</em> and <em>-s</em>.',
    ['In the cabin: count it', 'In the hold: measure it'],
    [['three chairs', 'furniture'], ['three suitcases', 'luggage'], ['nine coins', 'money'],
     ['three letters', 'mail']]) + '''
      ''' + exi('There are three <em>chairs</em> in the cabin, and a lot of <em>furniture</em> in the hold.') + '''
      ''' + GALLEY + '''
    </div>

    '''

# ═════════════════════════════════════════════════════════════════════
WEST = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">The west shore</div>
      <h2>Countania: count it</h2>
      <p class="chart-note" style="margin:-6px 0 18px">A countable noun names a thing with edges: you can point at one, and put a number in front of it. That gives it four habits, and once you know them you can spot a Countania word anywhere.</p>
      ''' + rule_grid([
    ('<em>A</em> or <em>an</em> for one',
     'One of anything here takes <em>a</em> or <em>an</em>: <em>a chair, a job, an apple, an idea</em>.',
     ex('We found <em>a coin</em> under <em>a chair</em>.')),
    ('One alone is never bare',
     'A singular countable noun needs a word in front: <em>a, the, my, this, every</em>. <em>I need chair</em> is not English; <em>I need a chair</em> is.',
     ex('Is there <em>a chair</em> for me? <em>The chair</em> by the window is free.')),
    ('Add <em>-s</em> for more than one',
     'Most nouns add <em>-s</em> or <em>-es</em>: <em>chairs, boxes</em>. A few change inside: <em>man &rarr; men, child &rarr; children, foot &rarr; feet, person &rarr; people</em>.',
     ex('Three <em>suitcases</em> and two <em>boxes</em> came aboard.')),
    ('Numbers go straight in',
     '<em>two trips, ten tools, a hundred steps</em>. Nothing in between: never <em>two pieces of trip</em>.',
     ex('It took us <em>three trips</em> to load the ship.')),
    ('<em>Many</em>, <em>a few</em>, <em>few</em>',
     '<em>How many?</em> asks for a number. <em>A few</em> means some; <em>few</em> means not enough.',
     ex('How <em>many</em> coins are left? Only <em>a few</em>.')),
    ('<em>Fewer</em>, not <em>less</em>',
     'For fewer things, careful English says <em>fewer</em>: <em>fewer storms, fewer mistakes</em>. <em>Less</em> is common in speech, but exams mark it down.',
     ex('There were <em>fewer storms</em> this year than last.')),
]) + chart(
    'Twelve pairs, straight across the water',
    'On the chart every harbour on the east shore faces its partner on the west, with the same surname. When a word from the right-hand column will not take <em>a</em> or <em>-s</em>, its partner on the left will.',
    ['Countania: count it', 'Uncountania: measure it', 'The mistake'],
    [['a job &middot; two jobs', 'work', 'a work, works (but <em>a work of art</em> is a painting)'],
     ['a fact &middot; facts', 'information', 'an information, informations'],
     ['a tip &middot; tips', 'advice', 'an advice, advices'],
     ['a suitcase &middot; suitcases', 'luggage', 'a luggage, luggages'],
     ['a chair &middot; chairs', 'furniture', 'a furniture, furnitures'],
     ['a trip &middot; trips', 'travel', 'a travel (but <em>his travels</em>, his journeys)'],
     ['a coin &middot; coins', 'money', 'a money, moneys'],
     ['a song &middot; songs', 'music', 'a music, musics'],
     ['a tool &middot; tools', 'equipment', 'an equipment, equipments'],
     ['a storm &middot; storms', 'weather', 'a weather, a bad weather'],
     ['a task &middot; tasks', 'homework', 'a homework, homeworks'],
     ['a step &middot; steps', 'progress', 'a progress, progresses']]) + '''
    </div>

    '''

# ═════════════════════════════════════════════════════════════════════
EAST = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The east shore</div>
      <h2>Uncountania: measure it</h2>
      <p class="chart-note" style="margin:-6px 0 18px">An uncountable noun names stuff with no edges: a liquid, a material, an idea, or a whole category of things under one name. You cannot put a number in front of it, so it has none of Countania&#39;s habits, and four of its own.</p>
      ''' + rule_grid([
    ('No <em>a</em>, no <em>an</em>',
     'Never <em>an advice</em>, never <em>a furniture</em>. Use it bare, or with <em>some</em>, <em>the</em>, <em>my</em>.',
     ex('She gave me <em>some advice</em>, and it was <em>good advice</em>.')),
    ('No <em>-s</em>, ever',
     '<em>Informations, advices, luggages, furnitures, equipments</em> are some of the commonest mistakes in English. In many languages these words do have a plural; in English they do not.',
     ex('We need <em>more information</em> about the tides.')),
    ('The verb is singular',
     'The noun is one mass, so the verb is <em>is</em>, <em>was</em>, <em>has</em>: <em>the luggage is</em>, <em>the money was</em>.',
     ex('<em>The furniture is</em> old, but <em>the equipment is</em> new.')),
    ('<em>Much</em>, <em>a little</em>, <em>little</em>',
     '<em>How much?</em> asks for an amount. <em>Much</em> belongs in questions and negatives; in a plain statement say <em>a lot of</em>: <em>a lot of money</em>, not <em>much money</em>.',
     ex('How <em>much</em> money is left? Only <em>a little</em>.')),
    ('What lives here: stuff, not things',
     'Liquids and gases (<em>water, air</em>), materials (<em>wood, glass, sand</em>), grains (<em>rice, flour</em>), ideas (<em>advice, fun, luck</em>), activities (<em>work, travel, research</em>) and whole categories (<em>furniture, luggage, money</em>).',
     ex('<em>Rice</em>, <em>sand</em> and <em>water</em> filled the hold.')),
    ('Take the ferry to count it',
     'To count stuff, count a container or a unit of it: <em>a piece of advice, two pieces of furniture, a bottle of water, a slice of bread</em>. The unit takes the <em>-s</em>; the stuff never does.',
     ex('Can I give you <em>a piece of advice</em>? Pack <em>two bottles of water</em>.')),
]) + chart(
    'The piece-of ferry: one crossing, west only',
    'The ferry carries a word from Uncountania into Countania by putting a countable unit in front of it. <em>A piece of</em> is the all-purpose ticket; the others fit their cargo.',
    ['The unit', 'The stuff it carries'],
    [['a piece of', 'advice, information, news, furniture, luggage, equipment, music, work'],
     ['a bottle of &middot; a glass of', 'water, milk, wine, juice'],
     ['a cup of &middot; a mug of', 'coffee, tea, hot chocolate'],
     ['a slice of &middot; a loaf of', 'bread, cake, cheese, ham'],
     ['a bar of', 'chocolate, soap, gold'],
     ['a bag of &middot; a sack of', 'rice, flour, sand, coal'],
     ['a grain of', 'rice, sand, salt, truth'],
     ['a bit of', 'luck, help, time, fun: the informal ticket']]) + '''
    </div>

    '''

# ═════════════════════════════════════════════════════════════════════
DIAGRAM = '''<div class="camp" id="order">
      ''' + MARK_PANES + '''
      <div class="camp-label">Interactive</div>
      <h2>Read the chart</h2>
      <div class="diagram-card" data-map-zoom data-mz-target=".chart-toggle-wrap" data-mz-btn=".name-bar" data-mz-ratio="1.5" data-mz-min="1100">
        <p class="diagram-intro">Click a land and its list lights up below. Every harbour is named after a noun. Switch the chart to <em>just the nouns</em> to see them bare, then to <em>counted</em> to see how each shore counts: a number on the west, the ferry&#39;s <em>piece of</em> on the east. Read straight across: each pair shares a surname.</p>
        <div class="name-bar" id="name-bar">
          <span class="name-label">Read the chart as</span>
          <button type="button" data-mode="place" class="on" aria-pressed="true">Place names</button>
          <button type="button" data-mode="verb" aria-pressed="false">Just the nouns</button>
          <button type="button" data-mode="past" aria-pressed="false">Counted</button>
        </div>
        <div class="diagram-stage" data-mz-scroll>
          <div class="chart-toggle-wrap">
            <img class="chart-photo" src="''' + ART + '''/chart-clean.jpg" alt="" width="1536" height="1024" loading="lazy">
            ''' + M.chart_overlay('cnt') + '''
          </div>
        </div>
        <p class="chart-scroll-hint">Drag the chart sideways to reach the east shore.</p>
        <div class="diagram-panels three">
          <div class="diagram-panel is-west" id="panel-west">
            <h4>Countania &middot; count it</h4>
            <ul id="panel-west-list"></ul>
          </div>
          <div class="diagram-panel is-isle" id="panel-strait">
            <h4>The strait &middot; both, or neither</h4>
            <ul id="panel-strait-list"></ul>
          </div>
          <div class="diagram-panel is-east" id="panel-east">
            <h4>Uncountania &middot; measure it</h4>
            <ul id="panel-east-list"></ul>
          </div>
        </div>
      </div>
    </div>

    '''

# ═════════════════════════════════════════════════════════════════════
ISLE = fork(
    'Double Isle: both shores, two meanings',
    'The lilac island in the strait belongs to both shores. Its nouns are countable with one meaning and uncountable with '
    'another, and the <em>a</em> or the <em>-s</em> tells the listener which one you mean.',
    ['Noun', 'Countable: a thing', 'Uncountable: the stuff'],
    [['coffee', '<em>a coffee</em>: a cup of it<br><em>Two coffees, please.</em>',
      '<em>coffee</em>: the drink, the beans<br><em>Coffee keeps me awake.</em>'],
     ['chicken', '<em>a chicken</em>: the living bird<br><em>We keep six chickens.</em>',
      '<em>chicken</em>: the meat<br><em>We had chicken for dinner.</em>'],
     ['paper', '<em>a paper</em>: a newspaper, or an essay<br><em>She reads a paper every day.</em>',
      '<em>paper</em>: the material<br><em>Wrap it in paper.</em>'],
     ['room', '<em>a room</em>: a space with walls<br><em>The ship has ten rooms.</em>',
      '<em>room</em>: space<br><em>Is there room for one more?</em>'],
     ['glass', '<em>a glass</em>: you drink from it<br><em>Two glasses of water.</em>',
      '<em>glass</em>: the material<br><em>The porthole is made of glass.</em>'],
     ['hair', '<em>a hair</em>: one single strand<br><em>There&#39;s a hair in my soup.</em>',
      '<em>hair</em>: all of it on your head<br><em>She has long hair.</em>'],
     ['time', '<em>a time</em>: an occasion<br><em>I&#39;ve been there three times.</em>',
      '<em>time</em>: minutes and hours<br><em>We don&#39;t have much time.</em>']],
    'The test is the same everywhere on the island: if you could put a number in front of it in this sentence, it is '
    'countable here. <em>Three coffees</em> works in a café; <em>three coffees</em> does not work for the beans in the hold.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-regularia.html', 'Regularia: regular and irregular verbs')])

SHALLOWS = '''<div class="camp" id="shallows">
      ''' + MARK_FORK + '''
      <div class="camp-label">The Shallows</div>
      <h2>Words that work on either shore</h2>
      <p class="chart-note" style="margin:-6px 0 18px">South of Double Isle the water shoals. The words in the Shallows sail both ways: <em>some chairs</em> and <em>some furniture</em>, <em>a lot of coins</em> and <em>a lot of money</em>. Learn these first, and you have a safe word for every noun. The words on the two shores are the ones that only fit one kind.</p>
      ''' + chart(
    'Quantity words, shore by shore',
    'The middle column is the Shallows. The outer columns only fit their own shore.',
    ['Countania only', 'Either shore', 'Uncountania only'],
    [['many', 'a lot of &middot; lots of', 'much'],
     ['a few', 'some', 'a little'],
     ['few', 'any', 'little'],
     ['fewer', 'more &middot; most', 'less'],
     ['several', 'enough', 'a great deal of'],
     ['a number of', 'plenty of &middot; no', 'an amount of']]) + '''
      ''' + exi('<em>Some</em> chairs, <em>some</em> furniture; <em>a lot of</em> coins, <em>a lot of</em> money.') + '''
      <p class="chart-note" style="margin-top:22px"><strong>The False Cape.</strong> A spur of the east shore flies an <em>-S</em> flag it has no right to. These words end in <em>-s</em> and look plural, but they are uncountable and take a singular verb. Across the water stand a few words that do the opposite.</p>
      ''' + chart(
    'Looks plural, is not (and the other way round)',
    'The flag is a trick: read the verb, not the last letter.',
    ['Word', 'Is', 'Say'],
    [['news', 'uncountable, singular', 'The news <em>is</em> good. Never <em>a news</em>: <em>a piece of news</em>.'],
     ['maths &middot; physics &middot; economics', 'singular subjects', 'Maths <em>is</em> my best subject.'],
     ['athletics &middot; gymnastics', 'singular sports', 'Athletics <em>is</em> on tonight.'],
     ['people &middot; police &middot; cattle', 'plural, with no <em>-s</em>', 'The police <em>are</em> here. People <em>are</em> kind.'],
     ['clothes &middot; scissors &middot; trousers', 'plural only', 'My clothes <em>are</em> wet. <em>A pair of</em> scissors.']]) + '''
      ''' + exi('The news <em>is</em> good: the police <em>are</em> on their way.') + '''
    </div>

    '''

# ═════════════════════════════════════════════════════════════════════
SIGNALS = signals(
    'Count it &mdash; sail west',
    ['single objects with a shape: <em>a chair, a coin, a bottle</em>',
     'people and animals: <em>a sailor, a gull</em>',
     'events: <em>a trip, a storm, a meeting</em>',
     'units and containers: <em>a slice, a piece, a cup</em>',
     'jobs you can number: <em>a task, a job, a step</em>',
     'the members of a category: <em>a chair</em> of furniture, <em>a suitcase</em> of luggage'],
    'Measure it &mdash; sail east',
    ['liquids and gases: <em>water, milk, air</em>',
     'materials: <em>wood, glass, paper</em>',
     'grains and powders: <em>rice, sand, flour</em>',
     'ideas and feelings: <em>advice, fun, luck, love</em>',
     'activities: <em>work, travel, research, homework</em>',
     'whole categories: <em>furniture, luggage, money, equipment</em>'],
    'The one test to keep: can you put a number in front? <em>Three chairs</em>, yes, so sail west. '
    '<em>Three furnitures</em>, no, so it lives in Uncountania, and the ferry is how you count it: '
    '<em>three pieces of furniture</em>.')

# ═════════════════════════════════════════════════════════════════════
QUIZ = [
    ('Can you give me some ___ about the crossing?',
     'Uncountania: no <em>a</em>, no <em>-s</em>.', 'advice',
     ['advice', 'advices', 'an advice', 'advise'],
     'Advice is uncountable: some advice, a piece of advice, never advices. Advise is the verb.'),
    ('We carried six ___ up the gangway.',
     'A number in front: which shore?', 'suitcases',
     ['suitcases', 'luggages', 'luggage', 'suitcase'],
     'Six needs a countable noun with -s: six suitcases. Luggage is its partner across the water, and has no plural.'),
    ('How ___ money did the voyage cost?',
     'Money lives in Uncountania.', 'much',
     ['much', 'many', 'few', 'a few'],
     'Money is uncountable, so the question is how much. How many is for things you count: how many coins.'),
    ('There were only ___ chairs left on deck.',
     'Countania, and a small number.', 'a few',
     ['a few', 'a little', 'much', 'little'],
     'Chairs are countable, so a few. A little and little go with uncountable nouns: a little furniture.'),
    ('The news ___ good this morning.',
     'The False Cape flies a false flag.', 'is',
     ['is', 'are', 'were', 'have been'],
     'News ends in -s but is uncountable, so its verb is singular: the news is good.'),
    ('Two ___, please: one with milk, one without.',
     'Double Isle: a cup, or the drink?', 'coffees',
     ['coffees', 'coffee', 'coffee cup', 'much coffee'],
     'In a café, a coffee is a cup of coffee, so it counts: two coffees. Coffee as the drink or the beans has no plural.'),
    ('She has long dark ___.',
     'Double Isle: one strand, or all of it?', 'hair',
     ['hair', 'hairs', 'a hair', 'the hairs'],
     'All the hair on your head is uncountable: long hair. A hair is one single strand, as in a hair in the soup.'),
    ('We need two ___ of bread for the voyage.',
     'Take the ferry: which unit?', 'loaves',
     ['loaves', 'breads', 'loafs', 'bread'],
     'Bread is uncountable, so we count a unit of it: a loaf, two loaves (f becomes v). Breads is wrong in everyday English.'),
    ('Which sentence is correct?',
     'Equipment lives in Uncountania.', 'The equipment is in the hold.',
     ['The equipment is in the hold.', 'The equipments are in the hold.',
      'An equipment is in the hold.', 'The equipment are in the hold.'],
     'Equipment is uncountable: no a, no -s, and a singular verb. One item is a piece of equipment.'),
    ('Is there ___ for one more person in the cabin?',
     'Double Isle: space, or a space with walls?', 'room',
     ['room', 'a room', 'rooms', 'many room'],
     'Room meaning space is uncountable: is there room for one more? A room is a space with walls.'),
    ('There&#39;s ___ milk in the hold, but not much.',
     'Uncountania, a small amount.', 'a little',
     ['a little', 'a few', 'few', 'many'],
     'Milk is uncountable, so a little. A few and few are for countable nouns: a few bottles of milk.'),
    ('I don&#39;t have ___ homework tonight.',
     'A word from the Shallows, in a negative.', 'any',
     ['any', 'a', 'many', 'few'],
     'Any sails both ways and fits negatives: any homework, any tasks. Homework is uncountable, so never a homework or many homework.'),
    ('We had ___ storms this winter than last.',
     'Storms are counted.', 'fewer',
     ['fewer', 'less', 'little', 'much'],
     'Storms are countable, so careful English says fewer storms. Less is for uncountable nouns: less rain.'),
    ('Which of these is NOT correct?',
     'One phrase has sailed to the wrong shore.', 'three informations',
     ['three informations', 'three facts', 'some information', 'a piece of information'],
     'Information is uncountable and never takes -s or a number. Three facts, or three pieces of information.'),
]
for q in QUIZ:
    for part in (q[0], q[1], q[2], q[4]) + tuple(q[3]):
        assert '"' not in part, 'a quiz string would break its JS: ' + part
    assert q[2] in q[3], 'the answer is not among the options: ' + q[0]

# ═════════════════════════════════════════════════════════════════════
PANEL_WEST = [
    '<b>a / an</b> a job &middot; a fact &middot; a tip &middot; an apple',
    '<b>-s</b> jobs &middot; facts &middot; tips &middot; suitcases &middot; chairs &middot; trips',
    '<b>many &middot; a few &middot; few &middot; fewer</b>',
    'A number goes straight in: <em>three tools, two storms</em>.',
]
PANEL_STRAIT = [
    ('double', '<b>Double Isle</b> a coffee &middot; coffee &middot; a chicken &middot; chicken &middot; a paper &middot; paper'),
    ('double', 'a room &middot; room &middot; a glass &middot; glass &middot; a hair &middot; hair &middot; a time &middot; time'),
    ('shallows', '<b>The Shallows</b> some &middot; any &middot; a lot of &middot; plenty of &middot; no &middot; enough &middot; more &middot; most'),
    ('cape', '<b>The False Cape</b> the news is &middot; maths is &middot; physics is'),
    ('ferry', '<b>The ferry</b> a piece of advice &middot; a bottle of water &middot; a slice of bread'),
]
PANEL_EAST = [
    '<b>no a, no -s</b> work &middot; information &middot; advice &middot; luggage &middot; furniture',
    'travel &middot; money &middot; music &middot; equipment &middot; weather &middot; homework &middot; progress',
    '<b>much &middot; a little &middot; little &middot; less</b>',
    'A singular verb: <em>the luggage is</em>. To count it, take the ferry.',
]
for _rows in (PANEL_WEST, [t for _, t in PANEL_STRAIT], PANEL_EAST):
    for _t in _rows:
        assert '"' not in _t, 'a panel line would break its JS string: ' + _t

# land -> (panel, row key, outline colour)
TARGETS = {
    'countania': ('panel-west', '', M.INK['countania']),
    'uncountania': ('panel-east', '', M.INK['uncountania']),
    'double': ('panel-strait', 'double', M.INK['double']),
    'shallows': ('panel-strait', 'shallows', M.INK['shallows']),
    'cape': ('panel-strait', 'cape', M.INK['cape']),
    'ferry': ('panel-strait', 'ferry', M.SEA_INK),
}

DIAGRAM_JS = '''var panelWest = [
  %s
];
var panelStrait = [
  %s
];
var panelEast = [
  %s
];

function renderList(id, items){
  var ul = document.getElementById(id);
  if (!ul) return;
  ul.innerHTML = "";
  items.forEach(function(it){
    var li = document.createElement("li");
    if (typeof it === "string"){ li.innerHTML = it; }
    else { li.innerHTML = it[1]; li.setAttribute("data-key", it[0]); }
    ul.appendChild(li);
  });
}
renderList("panel-west-list", panelWest);
renderList("panel-strait-list", panelStrait);
renderList("panel-east-list", panelEast);

function pulseShape(el){
  el.animate([{ opacity: 1 }, { opacity: 0.55 }, { opacity: 1 }], { duration: 380, easing: "ease-out" });
}

// the chart reads three ways: place names, the bare noun, or the noun
// counted (three jobs / a piece of work). All three live on the same text
// node and swap content. A long counted form, or Double Isle's two forms
// ("a coffee · coffee"), is set a size smaller.
var NAME_ATTR = { place: "data-place", verb: "data-verb", past: "data-past" };
function cntNames(mode){
  document.querySelectorAll(".sail-chart text.place-name").forEach(function(t){
    var v = t.getAttribute(NAME_ATTR[mode]);
    t.textContent = v;
    t.setAttribute("font-size", (v.indexOf("·") >= 0 || v.length > %d) ? %d : t.getAttribute("data-size"));
    t.style.fontStyle = mode === "place" ? "normal" : "italic";
  });
  document.querySelectorAll("#name-bar button").forEach(function(b){
    var on = b.getAttribute("data-mode") === mode;
    b.classList.toggle("on", on);
    b.setAttribute("aria-pressed", on ? "true" : "false");
  });
}
document.querySelectorAll("#name-bar button[data-mode]").forEach(function(b){
  b.addEventListener("click", function(){ cntNames(b.getAttribute("data-mode")); });
});

// clicking a land lights its panel, and the feature's own line in it
var TARGETS = %s;
Object.keys(TARGETS).forEach(function(key){
  var el = document.getElementById("cnt-" + key);
  if (!el) return;
  var t = TARGETS[key];
  var activate = function(){
    pulseShape(el);
    document.querySelectorAll(".diagram-panel").forEach(function(p){ p.style.outline = "none"; });
    document.querySelectorAll(".diagram-panel li.is-lit").forEach(function(li){ li.classList.remove("is-lit"); });
    var panel = document.getElementById(t[0]);
    if (!panel) return;
    panel.style.outline = "2px solid " + t[2];
    if (t[1]){
      panel.querySelectorAll('li[data-key="' + t[1] + '"]').forEach(function(li){ li.classList.add("is-lit"); });
    }
    panel.scrollIntoView({ block: "nearest", behavior: "smooth" });
  };
  el.addEventListener("click", activate);
  el.addEventListener("keydown", function(e){
    if (e.key === "Enter" || e.key === " "){ e.preventDefault(); activate(); }
  });
});

''' % (",\n  ".join('"%s"' % e for e in PANEL_WEST),
       ",\n  ".join('["%s", "%s"]' % kt for kt in PANEL_STRAIT),
       ",\n  ".join('"%s"' % e for e in PANEL_EAST),
       M.LONG, M.SMALL, json.dumps(TARGETS))

_reg = open('lesson-template/build/build_regularia.py', encoding='utf-8').read()
LIGHTBOX_JS = _reg[_reg.index("LIGHTBOX_JS = '''") + 17:_reg.index("'''", _reg.index("LIGHTBOX_JS = '''") + 17)]
assert 'hero-lightbox' in LIGHTBOX_JS

# the gulls cross the sky layer only, never the hero: this chart has words in
# every channel, and a gull must not cross a teaching label
GULLS_JS = open('lesson-template/build/gulls.js', encoding='utf-8').read() + '''
skyGulls(document.getElementById("gull-sky"), {
  px: function (w) { return w < 560 ? 26 : 34; }, seed: 13,
  flocks: [
    {from: [108, 64], to: [-8, 24], flight: 17, cycle: 46, at: 5,
     birds: [[0, 0, 1], [-1.5, 1.1, .95], [-1.1, -1.3, 1.05]]},
    {from: [-8, 18], to: [108, 50], flight: 15, cycle: 46, at: 28,
     birds: [[0, 0, 1], [-1.4, -1, .92]]}
  ]
});
'''

sys.path.insert(0, 'tools')
import sherpa_sky, sherpa_topo
_music = json.load(open('sailing-the-seas-of-grammar/music.json', encoding='utf-8'))
MUSIC_TAG = ('<script src="block-camp/camp-music.js" data-track="sailing-the-seas-of-grammar/music.m4a" '
             'data-loop="%g %g" defer></script>\n' % tuple(_music['loop']))
SKY_CSS = ('  /* ── the sky: clouds and gulls (see build_sailing.py) ── */\n'
           '  .gull-sky{position:fixed;inset:0;z-index:-1;pointer-events:none;overflow:hidden;}\n'
           '  @media print{.gull-sky{display:none;}}\n'
           '  ' + ','.join(sherpa_topo.HALO_ON) + '{text-shadow:' + sherpa_topo.HALO + ';}\n')
SKY_EL = '<div class="gull-sky" id="gull-sky" aria-hidden="true"></div>\n' + sherpa_sky.ELEMENT

# the waterlined background and the hero lightbox / chart CSS are the series'
# own, shared verbatim from the earlier charts so the three read as one
_sail = open('lesson-template/build/build_sailing.py', encoding='utf-8').read()
_a = _sail.index('/* Waterlining:')
_b = _sail.index('  /* ── the sea chart ── */')
WATERLINES = _sail[_a:_b]
assert WATERLINES.count('@supports') == 1 and WATERLINES.rstrip().endswith('}'), 'waterline block moved in build_sailing.py'
_a = _reg.index("EXTRA_CSS = '''") + 15
_b = _reg.index("''' + WATERLINES + '''")
HEAD_CSS = _reg[_a:_b]
_a = _reg.index("  .diagram-panel li{padding:3px 6px;")
_b = _reg.index("'''\n\n# the result messages")
CHART_CSS = _reg[_a:_b]
assert '.chart-toggle-wrap' in CHART_CSS and '#order .diagram-card' in CHART_CSS, 'chart CSS moved in build_regularia.py'

ROOM_CSS = '''
  /* ── the ship's rooms: Innes's paintings, the words pinned on ── */
  /* one room to a row: side by side, in a 740px column, each painting was
     370px wide and its tags ran into each other */
  .rooms{display:grid;grid-template-columns:minmax(0,1fr);gap:18px;margin:0 0 6px;}
  .room{min-width:0;}   /* or the phone's 720px painting widens the track and the page */
  .room{margin:0;background:var(--card);border:1px solid var(--accent-light);border-radius:var(--radius);padding:14px;}
  .room figcaption{font-family:'Inter',sans-serif;font-size:13px;color:var(--ink-soft);margin:0 112px 10px 0;line-height:1.35;}
  .room figcaption b{color:var(--ink);font-size:15px;margin-right:4px;}
  .room-ask{display:inline-block;font-weight:700;font-size:11px;letter-spacing:.08em;padding:3px 8px;border-radius:999px;
            border:1px solid;margin-right:6px;vertical-align:1px;}
  .room-wrap{position:relative;}
  .room-wrap img{display:block;width:100%;height:auto;border-radius:10px;}
  .room-tag{position:absolute;transform:translate(-50%,-50%);white-space:nowrap;pointer-events:none;
            font-family:'Inter',sans-serif;font-weight:700;font-size:12.5px;line-height:1;
            padding:5px 9px;border-radius:999px;border:1px solid;
            box-shadow:0 2px 6px color-mix(in srgb,var(--ink) 30%,transparent);}
  .mz-max .room-tag{font-size:15px;}
  /* a painting this busy shrunk to a phone hides its tags: it scrolls at a
     width where they still sit beside their things */
  @media (max-width:760px){
    .room-stage{overflow-x:auto;-webkit-overflow-scrolling:touch;}
    .room-stage .room-wrap{width:720px;max-width:none;}
    .room-tag{font-size:11px;}
  }
  @media (max-width:600px){ #ship .rooms{margin-left:-56px;} #ship .room{padding:10px;} }
  .galley{margin-top:20px;background:var(--card);border:1px dashed var(--accent);border-radius:var(--radius);padding:20px 22px;}
  .galley-h{font-family:'Inter',sans-serif;font-size:13px;color:var(--ink-soft);margin:0 0 8px;}
  .galley-h b{color:var(--ink);font-size:15px;margin-right:4px;}
  .galley ul{list-style:none;padding:0;margin:14px 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:8px;}
  .galley li{padding:9px 12px;border-radius:10px;background:var(--accent-lighter);font-size:15px;}
  .galley li span{color:var(--ink-soft);font-size:13px;margin:0 4px;}
  .galley li i{font-style:normal;font-weight:600;}
  .galley-foot{font-size:14px;color:var(--ink-soft);margin:0;}
'''

EXTRA_CSS = HEAD_CSS + WATERLINES + '''
  /* ── the sea chart ── */
  .diagram-panels.three{grid-template-columns:repeat(3,1fr);}
  @media (max-width:820px){.diagram-panels.three{grid-template-columns:1fr;}}
''' + panel_css('is-west', M.PAINT['countania']) + panel_css('is-isle', M.PAINT['double']) \
    + panel_css('is-east', M.PAINT['uncountania']) + CHART_CSS + ROOM_CSS \
    + tag_css('is-count', M.PAINT['countania']) + tag_css('is-bulk', M.PAINT['uncountania']) \
    + tag_css('is-both', M.PAINT['double'])

REPLACEMENTS = [
    ('Start below deck, in the ship.</p>\n    </div>',
     'Start below deck, in the ship.</p>\n      '
     '<a class="hero-cta" href="#ship">Go below deck <span aria-hidden="true">&rarr;</span></a>\n    </div>'),
    ('<div class="brand">Sherpa <span>Tensing</span></div>',
     '<div class="brand">Sailing the <span>Seas of Grammar</span></div>'),
    ('<div class="sub">Forbes English &middot; a route up the tenses</div>',
     '<div class="sub">Forbes English &middot; countable and uncountable nouns</div>'),
    ('<a class="up-link" href="sherpa-tensing-route-map.html"><span class="arw" aria-hidden="true">&larr;</span>Route map</a>',
     '<a class="up-link" href="grammar.html#maps"><span class="arw" aria-hidden="true">&larr;</span>Grammar maps</a>'),
    ('<div class="camp-label">Summit log</div>', '<div class="camp-label">Ship&#39;s log</div>'),
    ('<button class="retry-btn" id="retry-btn">Climb again</button>',
     '<button class="retry-btn" id="retry-btn">Sail it again</button>'),
    ('<a class="base-camp" href="sherpa-tensing-route-map.html">&larr; Return to base camp</a>',
     '<a class="base-camp" href="grammar.html#maps">&larr; Back to the grammar maps</a>'),
    ('<a class="next-camp" href="sherpa-tensing-route-map.html">Choose your next camp &rarr;</a>',
     '<a class="next-camp" href="sailing-the-seas-regularia.html">Next chart: regular and irregular verbs &rarr;</a>'),
    ('"Clean run. You can tell a decision from a plan, and a belief from a forecast."',
     '"Clean run. You can tell a chair from furniture on any shore."'),
    ('"Solid progress. Worth a look back at camp five before camp eight."',
     '"Solid progress. Read the twelve pairs straight across, then sail it again."'),
    ('"Good first attempt. The will/going to fork is the part to read again."',
     '"Good first attempt. Go back below deck: count the cabin, measure the hold."'),
    ('/* ── NOW vs WILL DIAGRAM CAMP ── */', '/* ── THE SEA CHART ── */'),
    ('// ── NOW vs WILL diagram interactivity ──', '// ── the chart, made clickable ──'),
    ('\n</style>', EXTRA_CSS + SKY_CSS + '</style>'),
    ('<div class="camp-label">The fork in the path</div>', '<div class="camp-label">The island</div>'),
    ('<div class="camp-label">Trail markers</div>', '<div class="camp-label">Tide tables</div>'),
    ('<div class="camp-label">The climb</div>', '<div class="camp-label">The crossing</div>'),
    ('"Reach the summit"', '"Make landfall"'),
]

TITLE = '<title>Countania &amp; Uncountania &mdash; Countable and Uncountable Nouns</title>'

s = assemble(
    HERO,
    SHIP + WEST + EAST + DIAGRAM + ISLE + SHALLOWS + SIGNALS,
    DIAGRAM_JS + LIGHTBOX_JS + GULLS_JS,
    questions(QUIZ),
    PALETTE,
    TITLE,
    REPLACEMENTS,
    OUT,
    own_tail=False)

for a, b in REPLACEMENTS:
    if a != '\n</style>':            # that one is meant to recur: the insert ends with it
        assert a not in s, 'replacement did not land: %r' % a[:70]
assert 'countable and uncountable nouns</div>' in s and 'Make landfall' in s, 'the shell text was not replaced'

# ── strip the mountain's machinery: there is no camp here to earn ──
s = open(OUT, encoding='utf-8').read()
a = s.index('\n// ── progression:')
b = a + re.search(r'\nsherpaBar\(\);\n', s[a:]).end()
s = s[:a] + '\n' + s[b:]
s = re.sub(r'\n  /\* ── progression: the voice toggle and its lock ── \*/.*?\n(?=  /\*|\})',
           '\n', s, count=1, flags=re.S)

# ── lift the data-tr onto the wrapper rule_grid already drew ──
s = re.sub(r'<div class="ex">\x01(\d+)\x01', r'<div class="ex" data-tr="\1">', s)
assert '\x01' not in s, 'an example marker escaped'

# ── our own examples, our own translations ──
import ex_tr_countania as T
rows = []
for i in range(len(EX)):
    r = T.T.get(i)
    assert r and len(r) == 9, 'missing or short translation for example %d: %s' % (i, EX[i])
    rows.append('"%d": %s' % (i, json.dumps(r, ensure_ascii=False)))
assert len(T.T) == len(EX), 'ex_tr_countania has %d rows for %d examples' % (len(T.T), len(EX))
s = re.sub(r'var EX_TR = \{.*?\};\n', lambda m: 'var EX_TR = {%s};\n' % ", ".join(rows), s, count=1, flags=re.S)

# ── the sky and the music ──
_sizes = {k: Image.open('Sherpa Tensing/cloud-%d.webp' % k).size for k in range(1, sherpa_sky.IMAGES + 1)}
assert s.count('</head>') == 1
s = s.replace('</head>', sherpa_sky.block(_sizes) + '</head>', 1)
s, n = re.subn(r'(<body\b[^>]*>\n?)', lambda m: m.group(1) + SKY_EL, s, count=1)
assert n == 1, 'no <body> to hang the sky on'
assert s.count('</body>') == 1
# every map can be enlarged (Innes, 2026-11-08: "maps need to be expandable always")
s = s.replace('</body>', MUSIC_TAG + '<script src="map-zoom.js" defer></script>\n</body>', 1)

# the shell's SEO block describes the camp it was cloned from; tools/seo.py
# writes this page's own from the catalogue row, so leave the block empty
s, n = re.subn(r'(<!-- SEO:start -->).*?(<!-- SEO:end -->)', r'\1\n\2', s, count=1, flags=re.S)
assert n == 1, 'no SEO block in the shell'
s, n = re.subn(r'<title>.*?</title>', TITLE, s, count=1, flags=re.S)
assert n == 1, 'no <title> in the shell'

# nothing of the camp this shell was cloned from, or of the chart this
# builder was copied from, may leak through
for leak in ('Camp Seven', 'camp seven', 'will/going to', 'willExamples', 'Regularia &amp;', 'panel-reg', 'reg-'):
    assert leak not in s, 'a leak from the shell or the Regularia builder: %s' % leak

open(OUT, 'w', encoding='utf-8', newline='').write(s)
print('wrote %s: %d examples, %d questions, %d bytes' % (OUT, len(EX), len(QUIZ), len(s)))
