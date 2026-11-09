# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: The Atlantic, British and American English
as the two shores of one ocean. The ninth chart.

    py lesson-template/build/build_atlantic.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. Eight harbours face each other across the water, paired
by latitude: Elevator Harbour in America looks straight across at Lift
Harbour in Britain. The Shallows in mid-ocean hold what both shores say (do
you have, learned, toward/towards); the False Cape holds the words that sail
across and change meaning (pants, chips, first floor). The page teaches the
grammar differences too: gotten, the present perfect, at/on the weekend,
collective nouns, spelling.

THE ART. Layout by sea_layouts_3.py (docs/sea-charts/the-atlantic.png),
painted by ChatGPT on 2026-11-09 with Gerundia as the style; the brief pinned
the 16 dot centres, and sea_measure.py found all 16 within 10px of them
(atlantic_chart.json). No national flags, by the brief.
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE

OUT = 'sailing-the-seas-atlantic.html'
ART = 'sailing-the-seas-atlantic'
UID = 'atl'

# py lesson-template/extract-palette.py sailing-the-seas-atlantic/hero.jpg --light
EXTRACTED = {'text': '#2a2411', 'text-dim': '#5e522e', 'secondary': '#abcad3', 'contrast': '#0c506a'}

D = O.load('atlantic_chart.json')
WEST = sorted((tuple(p) for p in D['dots'] if p[0] < 768), key=lambda p: p[1])
EAST = sorted((tuple(p) for p in D['dots'] if p[0] > 768), key=lambda p: p[1])
assert len(WEST) == len(EAST) == 8, D['dots']
for w, e in zip(WEST, EAST):
    assert abs(w[1] - e[1]) <= 8, 'a pair is off its latitude: %s %s' % (w, e)

# (American, British, American sentence, British sentence)
PAIRS = [
    ('elevator', 'lift', 'Take the elevator.', 'Take the lift.'),
    ('apartment', 'flat', 'We rent an apartment.', 'We rent a flat.'),
    ('fall', 'autumn', 'See you in the fall.', 'See you in the autumn.'),
    ('vacation', 'holiday', 'We&#8217;re on vacation.', 'We&#8217;re on holiday.'),
    ('truck', 'lorry', 'A truck blocked the road.', 'A lorry blocked the road.'),
    ('cookie', 'biscuit', 'Have a cookie.', 'Have a biscuit.'),
    ('the movies', 'the cinema', 'Let&#8217;s go to the movies.', 'Let&#8217;s go to the cinema.'),
    ('gotten', 'got', 'She&#8217;s gotten taller.', 'She&#8217;s got taller.'),
]
INK, WEST_LAND, EAST_LAND = '#20180A', '#E4E8C8', '#EAE6CC'


def harbour(w):
    return ' '.join(p[:1].upper() + p[1:] for p in w.split()) + ' Harbour'


def key(side, w):
    return side + '-' + w.replace('the ', '').replace(' ', '-')


def overlay():
    spots, names = [], []
    for (us, uk, s_us, s_uk), (wx, wy), (ex_, ey) in zip(PAIRS, WEST, EAST):
        names.append(O.name(wx, wy, (harbour(us), s_us, '%s &#183; UK: %s' % (us, uk)), INK, WEST_LAND, size=18,
                            dy=-16, fit=False, halo=.1))
        names.append(O.name(ex_, ey, (harbour(uk), s_uk, '%s &#183; US: %s' % (uk, us)), INK, EAST_LAND, size=18,
                            dy=-16, fit=False, halo=.1))
        spots.append(O.hotspot(UID, key('us', us), O.circle_path(wx, wy, 30), '%s, American: British %s' % (us, uk)))
        spots.append(O.hotspot(UID, key('uk', uk), O.circle_path(ex_, ey, 30), '%s, British: American %s' % (uk, us)))
    spots.append(O.hotspot(UID, 'shallows', O.rect_path(610, 430, 930, 600), 'The Shallows: both shores say it'))
    spots.append(O.hotspot(UID, 'cape', O.rect_path(470, 700, 820, 830), 'The False Cape: same word, other meaning'))
    sea_ink = '#0F2F3D'
    caps = [O.cap(768, 62, 'THE ATLANTIC', sea_ink, 38, face=O.SERIF, spacing='.05em'),
            O.cap(768, 90, 'two shores, one language', sea_ink, 19, face=O.SERIF, weight=600, spacing='0', style='italic'),
            O.cap(150, 965, 'AMERICA', INK, 32, face=O.SERIF, spacing='.04em', halo=WEST_LAND),
            O.cap(1392, 965, 'BRITAIN', INK, 32, face=O.SERIF, spacing='.04em', halo=EAST_LAND),
            O.cap(756, 490, 'THE SHALLOWS', INK, 21, face=O.SERIF, spacing='.04em'),
            O.cap(756, 518, 'both shores say it', INK, 16, weight=600, spacing='0', style='italic'),
            O.cap(756, 546, 'do you have &#183; learned &#183; toward(s)', INK, 16, weight=600, spacing='0', style='italic'),
            O.cap(768, 858, 'THE FALSE CAPE', sea_ink, 21, face=O.SERIF, spacing='.04em'),
            O.cap(768, 888, 'same word, other meaning: pants &#183; chips &#183; first floor', sea_ink, 16, weight=600,
                  spacing='0', style='italic')]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated chart of the Atlantic. On the west, the forested coast of America with eight harbours: '
            'Elevator, Apartment, Fall, Vacation, Truck, Cookie, The Movies and Gotten. Facing each across the water on '
            'the east, the white cliffs of Britain: Lift, Flat, Autumn, Holiday, Lorry, Biscuit, The Cinema and Got. '
            'In mid-ocean a sandbank, the Shallows, says: both shores say it. To the south a spit with a red flag is '
            'the False Cape: same word, other meaning.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; British and American English', 'The Atlantic',
    'One language, two shores. Most of English is the same on both sides of the ocean, but some harbours face '
    'each other with different names: an American takes the <em>elevator</em>, a Brit takes the <em>lift</em>. '
    'Read the chart across, harbour to harbour, then pick a shore and stay on it.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the crossing</div>
      <h2>Same ocean, two shores</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Neither shore is right or wrong. Both understand each other perfectly. The skill is choosing one shore and not switching in the middle of a text.</p>
      ''' + rule_grid([
    ('Different words, same thing',
     'Everyday objects often have two names. Learn them in pairs, harbour to harbour.',
     ex('We&#39;re going on <em>holiday</em> in August. / We&#39;re going on <em>vacation</em> in August.')),
    ('Different spelling',
     'Britain keeps <em>-our</em>, <em>-re</em> and a double <em>l</em>; America drops them: <em>colour / color</em>, <em>centre / center</em>, <em>travelled / traveled</em>.',
     ex('What <em>colour</em> is the boat? / What <em>color</em> is the boat?')),
    ('<em>Gotten</em> sails west only',
     'Americans say <em>has gotten</em> for a change; Britain says <em>has got</em>. Both say <em>have got</em> for having.',
     ex('She&#39;s <em>got</em> much taller this year. / She&#39;s <em>gotten</em> much taller this year.')),
    ('The present perfect is busier in Britain',
     'With <em>just</em>, <em>already</em> and <em>yet</em>, Britain uses the present perfect; America often uses the past simple.',
     ex('<em>Have you eaten</em> yet? / <em>Did you eat</em> yet?')),
    ('Small words differ',
     '<em>At</em> the weekend in Britain, <em>on</em> the weekend in America. Britain also says <em>different to</em>; America also says <em>different than</em>.',
     ex('What are you doing <em>at the weekend</em>? / What are you doing <em>on the weekend</em>?')),
    ('A crew can be one thing or many',
     'In Britain a group noun can take a plural verb (the crew <em>are</em>); in America it is almost always singular.',
     ex('The crew <em>are</em> tired. / The crew <em>is</em> tired.')),
]) + chart(
    'The eight crossings',
    'Read each row across the ocean. Every word on the left is understood in Britain, and every word on the right in America.',
    ['America', 'Britain', 'Also'],
    [['elevator', 'lift', 'subway / underground'], ['apartment', 'flat', 'first floor / ground floor'],
     ['fall', 'autumn', 'diaper / nappy'], ['vacation', 'holiday', 'line / queue'], ['truck', 'lorry', 'gas / petrol'],
     ['cookie', 'biscuit', 'candy / sweets'], ['the movies', 'the cinema', 'check / bill'], ['gotten', 'got', 'mail / post']]) + '''
    </div>

    '''

CAPE = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The Shallows and the False Cape</div>
      <h2>Shared words, and words that change at sea</h2>
      <p class="chart-note" style="margin:-6px 0 18px">In the Shallows, both shores are at home. At the False Cape a word lands on the other shore and means something else, which is where the jokes, and the embarrassments, come from.</p>
      ''' + chart(
    'The Shallows: both shores say it',
    'These are often taught as one shore&#39;s, but both sides use both.',
    ['Both say', 'Both say', 'Note'],
    [['Do you have a pen?', 'Have you got a pen?', '<em>have got</em> is more common in Britain'],
     ['learned', 'learnt', '<em>learnt</em> is British only'], ['toward', 'towards', '<em>towards</em> is more common in Britain'],
     ['dreamed', 'dreamt', 'both, on both shores']]) + '''
      ''' + exi('I live in a <em>flat</em> near the harbour.') + chart(
    'The False Cape: same word, other meaning',
    'Check the shore before you use these.',
    ['Word', 'In America', 'In Britain'],
    [['pants', 'trousers', 'underwear'], ['chips', 'crisps (thin, in a bag)', 'fries (thick, hot)'],
     ['first floor', 'the floor at street level', 'one floor up'], ['purse', 'a handbag', 'a small wallet for coins'],
     ['football', 'American football', 'soccer']]) + '''
      ''' + exi('Can I have some <em>chips</em> with my fish?') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a harbour and its line lights up below: America on the left, Britain in the middle. Switch the chart '
    'to see each word in a sentence, then with its twin from the far shore: the sentence is the same, only the '
    'harbour changes.',
    ('The harbours', 'In a sentence', 'Across the sea'),
    [('America', 'is-west'), ('Britain', 'is-isle'), ('The Shallows and the False Cape', 'is-east')],
    'Drag the chart sideways to reach Britain.', min_zoom=1000)

TRAPS = fork(
    'Mixed cargo',
    'The usual problem is not choosing a shore: one text with both.',
    ['Not this', 'This', 'Why'],
    [['I took the elevator to my flat.', 'I took the lift to my flat. / the elevator to my apartment.', 'one shore per text'],
     ['She&#39;s gotten a new car. (meaning: she has one)', 'She&#39;s got a new car.', '<em>have got</em> for having, on both shores'],
     ['My favourite color is blue.', 'My favourite colour is blue. / My favorite color is blue.', 'spelling, one shore'],
     ['I&#39;ve put my pants on. (to a British listener, meaning trousers)', 'I&#39;ve put my trousers on.', 'the False Cape'],
     ['We live on the first floor, so no stairs. (in Britain)', 'We live on the ground floor.', 'the False Cape']],
    'Exams accept either shore. What they mark down is a mixture: pick one, and keep its spelling too.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-inversion.html', 'The inversion maelstrom')])

SIGNALS = signals(
    'You are in America',
    ['<em>elevator</em>, <em>apartment</em>, <em>fall</em>', '<em>color</em>, <em>center</em>, <em>traveled</em>',
     '<em>-ize</em> only: <em>organize</em>', '<em>has gotten</em> for a change', '<em>on the weekend</em>',
     '<em>Did you eat yet?</em>'],
    'You are in Britain',
    ['<em>lift</em>, <em>flat</em>, <em>autumn</em>', '<em>colour</em>, <em>centre</em>, <em>travelled</em>',
     '<em>-ise</em> or <em>-ize</em>: <em>organise</em>', '<em>has got</em> for a change', '<em>at the weekend</em>',
     '<em>Have you eaten yet?</em>'],
    'One test: look at the spelling. A text with <em>colour</em> and <em>centre</em> wants <em>lift</em> and <em>flat</em> too.')

QUIZ = [
    ('In Britain: We live in a small ___ above a shop.', 'The British harbour.', 'flat',
     ['flat', 'apartment', 'condo', 'unit'], 'Flat is British; apartment is American.'),
    ('In America: The leaves turn red in the ___.', 'The American harbour.', 'fall',
     ['fall', 'autumn', 'harvest', 'leafing'], 'Fall is American; autumn is British (and understood everywhere).'),
    ('Which is the British twin of truck?', 'Read across the ocean.', 'lorry',
     ['lorry', 'van', 'trolley', 'wagon'], 'Truck in America, lorry in Britain.'),
    ('British spelling: My favourite ___ is green.', 'Britain keeps -our.', 'colour',
     ['colour', 'color', 'colur', 'coulor'], 'Colour in Britain, color in America.'),
    ('American: She has ___ much taller this year.', 'A change, in America.', 'gotten',
     ['gotten', 'got', 'getted', 'gets'], 'Has gotten taller in America; has got taller in Britain.'),
    ('British: What are you doing ___ the weekend?', 'Britain&#39;s preposition.', 'at',
     ['at', 'on', 'in', 'by'], 'At the weekend in Britain; on the weekend in America.'),
    ('British: ___ finished your homework yet?', 'Britain uses the present perfect with yet.', 'Have you',
     ['Have you', 'Did you', 'Do you', 'Are you'], 'Have you finished yet? is the British form.'),
    ('In Britain, chips are ...', 'The False Cape.', 'thick, hot fried potatoes',
     ['thick, hot fried potatoes', 'thin potato slices in a bag', 'biscuits', 'small coins'],
     'British chips are American fries; American chips are British crisps.'),
    ('In America, the first floor is ...', 'The False Cape.', 'the floor at street level',
     ['the floor at street level', 'one floor up', 'the basement', 'the top floor'], 'The American first floor is the British ground floor.'),
    ('Which word do BOTH shores use?', 'The Shallows.', 'learned',
     ['learned', 'gotten', 'lorry', 'flat'], 'Learned is used in Britain and America; learnt is British only.'),
    ('Which sentence mixes the two shores?', 'One text, two shores.', 'I took the elevator up to my flat.',
     ['I took the elevator up to my flat.', 'I took the lift up to my flat.', 'I took the elevator up to my apartment.',
      'We took the lift to the cinema.'], 'Elevator is American, flat is British: pick one shore.'),
    ('In Britain, the crew ___ all very tired.', 'A group can be many people in Britain.', 'are',
     ['are', 'is being', 'be', 'were being'], 'The crew are tired: Britain lets a group noun take a plural verb.'),
]

PANELS = [
    [(key('us', p[0]), '<b>%s</b> %s' % (p[0], p[2])) for p in PAIRS],
    [(key('uk', p[1]), '<b>%s</b> %s' % (p[1], p[3])) for p in PAIRS],
    [('shallows', '<b>The Shallows</b> both say <em>Do you have&#8230;?</em>, <em>learned</em>, <em>toward(s)</em>'),
     ('cape', '<b>The False Cape</b> <em>pants</em>: US trousers, UK underwear'),
     ('cape', '<em>chips</em>: US crisps, UK fries &middot; <em>first floor</em>: US ground floor, UK one up')],
]
TARGETS = {}
for p in PAIRS:
    TARGETS[key('us', p[0])] = (0, key('us', p[0]), '#0c506a')
    TARGETS[key('uk', p[1])] = (1, key('uk', p[1]), '#0c506a')
TARGETS['shallows'] = (2, 'shallows', '#0c506a')
TARGETS['cape'] = (2, 'cape', '#B4441F')

import ex_tr_atlantic as T
L.build(OUT, ART, 'The Atlantic &mdash; British and American English', 'British and American English', EXTRACTED,
        HERO, 'then pick a shore and stay on it.', ('order', 'Read the chart'),
        RULES + CAPE + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        ['#B9CC92', '#D8D2A8', '#E3CF9E'], T.T,
        ['Clean run. You can read the chart across the ocean, harbour to harbour.',
         'Solid progress. Pick one shore per text, spelling included.',
         'Good first attempt. Start with the eight crossings: elevator, lift.'],
        ('sailing-the-seas-question-tags.html', 'Next chart: the return voyage'), gull_seed=41, long_name=22)
