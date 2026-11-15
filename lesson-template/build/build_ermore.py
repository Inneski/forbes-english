# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: The -ER Coast & the MORE Coast, comparatives
as two shores. The twenty-fourth and last chart of the table.

    py lesson-template/build/build_ermore.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. Short words sail west and take -ER: one syllable, or two
ending in -Y (cold, colder; happy, happier). Long words sail east and take
MORE: two syllables or more (more expensive, more careful). The harbour
notes carry the spelling rules (double the g, just add -r, y becomes i).
The Shallows hold the two-syllable words that go either way (clever,
narrow, quiet); the Lone Stacks are the irregulars (good, bad, far); the
False Cape holds the short words that still take MORE (fun, real, right).

No tense on this chart, so no Sherpa colours.

THE ART. Layout by sea_layouts_4.py, painted by Codex on 2026-11-14.
sea_measure.py found all 15 dots (er-more_chart.json).
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE

OUT = 'sailing-the-seas-er-more.html'
ART = 'sailing-the-seas-er-more'
UID = 'ermore'

# py lesson-template/extract-palette.py sailing-the-seas-er-more/hero.jpg --light
EXTRACTED = {'text': '#2a2211', 'text-dim': '#5e4f2e', 'secondary': '#adcfd7', 'contrast': '#0c5669'}

D = O.load('er-more_chart.json')
WEST = sorted((tuple(p) for p in D['dots'] if abs(p[0] - 280) < 10), key=lambda p: p[1])
EAST = sorted((tuple(p) for p in D['dots'] if abs(p[0] - 1256) < 10), key=lambda p: p[1])
STACKS = sorted((tuple(p) for p in D['dots'] if 600 < p[0] < 930), key=lambda p: p[0])
assert (len(WEST), len(EAST), len(STACKS)) == (6, 6, 3), D['dots']

# (adjective, comparative, spelling note, sentence)
ER = [('cold', 'colder', 'add -er', 'Today is colder than yesterday.'),
      ('fast', 'faster', 'add -er', 'The ferry is faster than the old boat.'),
      ('big', 'bigger', 'double the g', 'Our boat is bigger than theirs.'),
      ('nice', 'nicer', 'just add -r', 'The new harbour is nicer.'),
      ('happy', 'happier', 'y becomes i', 'She seems happier at sea.'),
      ('easy', 'easier', 'y becomes i', 'The second route is easier.')]
MORE = [('expensive', 'more expensive', 'The cabin is more expensive than a seat.'),
        ('careful', 'more careful', 'Be more careful on deck.'),
        ('modern', 'more modern', 'The new ferry is more modern.'),
        ('famous', 'more famous', 'This beach is more famous than that one.'),
        ('beautiful', 'more beautiful', 'The north coast is more beautiful.'),
        ('interesting', 'more interesting', 'The second trip was more interesting.')]
LONE = [('good', 'better', 'The weather is better today.'), ('bad', 'worse', 'The storm was worse than we thought.'),
        ('far', 'farther', 'The island is farther than it looks.')]
INK, WEST_LAND, EAST_LAND, SEA = '#20180A', '#D8B268', '#B9C989', '#B4D6E1'
SEA_INK = '#0F2F3D'


def overlay():
    spots, names = [], []
    for (a, c, note, s), (x, y) in zip(ER, WEST):
        names.append(O.name(x, y, ('%s &#8211; %s' % (a, c), note, s), INK, WEST_LAND, size=19, dy=-15, fit=False, halo=.3))
        spots.append(O.hotspot(UID, 'er-' + a, O.circle_path(x, y, 30), '%s, %s: %s' % (a, c, note)))
    for (a, c, s), (x, y) in zip(MORE, EAST):
        names.append(O.name(x, y, (c, 'two syllables or more', s), INK, EAST_LAND, size=19, dy=-15, fit=False, halo=.3))
        spots.append(O.hotspot(UID, 'more-' + a, O.circle_path(x, y, 30), '%s: more %s' % (a, a)))
    for (a, c, s), (x, y) in zip(LONE, STACKS):
        # the stacks stand 128px apart, so on the chart each gets a short
        # phrase; the full sentence is in the panel
        short = {'good': 'better weather', 'bad': 'a worse storm', 'far': 'farther away'}[a]
        names.append(O.name(x, y, (a, c, short), SEA_INK, SEA, size=17, dy=26, fit=False, halo=.6))
        spots.append(O.hotspot(UID, 'lone-' + a, O.circle_path(x, y, 34), '%s, %s: irregular' % (a, c)))
    spots.append(O.hotspot(UID, 'shallows', O.rect_path(561, 204, 951, 411), 'The Shallows: either way'))
    spots.append(O.hotspot(UID, 'cape', O.rect_path(562, 728, 960, 960), 'The False Cape: short, but more'))
    caps = [O.cap(768, 56, 'THE -ER COAST &amp; THE MORE COAST', SEA_INK, 36, face=O.SERIF, spacing='.04em'),
            O.cap(768, 92, 'short words sail west, long words sail east', SEA_INK, 19, face=O.SERIF, weight=600,
                  spacing='0', style='italic'),
            O.cap(280, 172, 'THE -ER COAST', INK, 28, face=O.SERIF, spacing='.03em', halo=WEST_LAND),
            O.cap(280, 200, 'one syllable, or two ending in -y', INK, 15, weight=600, spacing='0', style='italic',
                  halo=WEST_LAND),
            O.cap(1256, 172, 'THE MORE COAST', INK, 28, face=O.SERIF, spacing='.03em', halo=EAST_LAND),
            O.cap(1256, 200, 'two syllables or more', INK, 15, weight=600, spacing='0', style='italic', halo=EAST_LAND),
            O.cap(758, 276, 'THE SHALLOWS', INK, 21, face=O.SERIF, spacing='.04em'),
            O.cap(758, 304, 'either way', INK, 15, weight=600, spacing='0', style='italic'),
            O.cap(758, 330, 'clever &#183; narrow &#183; quiet', INK, 15, weight=600, spacing='0', style='italic'),
            O.cap(758, 354, 'simple &#183; gentle', INK, 15, weight=600, spacing='0', style='italic'),
            O.cap(764, 494, 'THE LONE STACKS', SEA_INK, 19, face=O.SERIF, spacing='.04em'),
            O.cap(764, 900, 'THE FALSE CAPE', SEA_INK, 19, face=O.SERIF, spacing='.04em'),
            O.cap(764, 928, 'fun &#183; real &#183; right &#183; wrong: short, but MORE', SEA_INK, 15, weight=600,
                  spacing='0', style='italic')]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated chart with two shores. On the golden west shore, the -ER Coast, six harbours: cold, colder; '
            'fast, faster; big, bigger; nice, nicer; happy, happier; easy, easier. On the green east shore, the MORE '
            'Coast: more expensive, more careful, more modern, more famous, more beautiful and more interesting. In '
            'the channel, a sandbank, the Shallows; three sea stacks, the Lone Stacks: good, better; bad, worse; far, '
            'farther; and a spit with a red flag, the False Cape.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; Comparatives', 'The -ER Coast &amp; the MORE Coast',
    'Is the ferry <em>faster</em> or <em>more fast</em>? Is the cabin <em>expensiver</em> or <em>more expensive</em>? '
    'Count the syllables. Short words sail west and take -ER; long words sail east and take MORE. '
    'Then learn the three stacks that never follow the rule.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the two coasts</div>
      <h2>Count the syllables</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Say the word and count the beats. One beat: west. Three or more: east. Two beats: east, unless the word ends in -y.</p>
      ''' + rule_grid([
    ('One syllable: -er',
     'Add -er, and <em>than</em> before the thing you compare.',
     ex('Today is <em>colder</em> than yesterday.')),
    ('A short vowel and one consonant: double it',
     '<em>big</em>, <em>bigger</em>; <em>hot</em>, <em>hotter</em>; <em>thin</em>, <em>thinner</em>.',
     ex('Our boat is <em>bigger</em> than theirs.')),
    ('Ends in -e: just add -r',
     '<em>nice</em>, <em>nicer</em>; <em>safe</em>, <em>safer</em>; <em>wide</em>, <em>wider</em>.',
     ex('The new harbour is <em>nicer</em>.')),
    ('Two syllables ending in -y: -ier',
     'The <em>y</em> becomes <em>i</em>: <em>happy</em>, <em>happier</em>; <em>easy</em>, <em>easier</em>.',
     ex('She seems <em>happier</em> at sea.')),
    ('Two syllables or more: more',
     'Put <em>more</em> in front, and leave the word as it is.',
     ex('The cabin is <em>more expensive</em> than a seat.')),
    ('Less works for every word',
     'The opposite of both coasts is <em>less</em> + the word.',
     ex('The second route is <em>less</em> dangerous.')),
]) + chart(
    'The twelve harbours',
    'Read each row across the channel.',
    ['-ER Coast', 'Spelling', 'MORE Coast'],
    [['%s, %s' % (a, c), note, mc] for (a, c, note, _), (_, mc, _) in zip(ER, MORE)]) + '''
    </div>

    '''

EXTRAS = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The Shallows, the Lone Stacks and the False Cape</div>
      <h2>Where the syllable count is not enough</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Some two-syllable words go either way, three common words have their own forms, and a few short words take MORE anyway.</p>
      ''' + chart(
    'The Shallows and the Lone Stacks',
    'Learn these as they are.',
    ['Where', 'Word', 'Comparative'],
    [['The Shallows', 'clever', 'cleverer / more clever'], ['The Shallows', 'narrow', 'narrower / more narrow'],
     ['The Shallows', 'quiet', 'quieter / more quiet'], ['The Lone Stacks', 'good', 'better'],
     ['The Lone Stacks', 'bad', 'worse'], ['The Lone Stacks', 'far', 'farther / further']]) + '''
      ''' + exi('The weather is <em>better</em> today, but the sea is <em>worse</em>.') + chart(
    'The False Cape',
    'One syllable, but they sail east.',
    ['Word', 'Say', 'Not'],
    [['fun', 'more fun', 'funner'], ['real', 'more real', 'realer'], ['right', 'more right', 'righter'],
     ['wrong', 'more wrong', 'wronger'], ['tired', 'more tired', 'tireder']]) + '''
      ''' + exi('Sailing is <em>more fun</em> than I expected.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a harbour and its line lights up below: the -ER Coast on the left, the MORE Coast in the middle, the '
    'Lone Stacks on the right. Switch the chart to see the rule for each, then each one in a sentence.',
    ('The comparatives', 'The rule', 'In a sentence'),
    [('The -ER Coast', 'is-west'), ('The MORE Coast', 'is-isle'), ('The Lone Stacks and the Cape', 'is-east')],
    'Drag the chart sideways to reach the MORE Coast.', min_zoom=1000)

TRAPS = fork(
    'Wrong coast',
    'Each of these takes a word to the wrong shore, or to both at once.',
    ['Not this', 'This', 'Why'],
    [['The cabin is expensiver.', 'The cabin is more expensive.', 'three syllables: MORE'],
     ['The ferry is more fast.', 'The ferry is faster.', 'one syllable: -er'],
     ['She is more happier now.', 'She is happier now.', 'never both'],
     ['The weather is gooder today.', 'The weather is better today.', 'a Lone Stack'],
     ['Our boat is biger.', 'Our boat is bigger.', 'double the g'],
     ['This is more cold than that.', 'This is colder than that.', 'one syllable: -er']],
    'Never put <em>more</em> and <em>-er</em> on the same word. One coast at a time.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-adjective-canal.html', 'The Adjective Canal: adjective order')])

SIGNALS = signals(
    'You are on the -ER Coast',
    ['one syllable: <em>cold</em>, <em>fast</em>, <em>big</em>', 'two, ending in -y: <em>happy</em>, <em>easy</em>',
     'add -er: <em>colder</em>', 'short vowel + consonant: double it', 'ends in -e: add -r', '+ <em>than</em>'],
    'You are on the MORE Coast',
    ['two syllables, not -y: <em>careful</em>, <em>modern</em>', 'three or more: <em>expensive</em>',
     '<em>more</em> + the word', 'the word does not change', '<em>less</em> works the same', '+ <em>than</em>'],
    'One test: clap the syllables. One clap, -er. Three claps, more.')

QUIZ = [
    ('Today is ___ than yesterday.', 'One syllable.', 'colder',
     ['colder', 'more cold', 'more colder', 'coldier'], 'One syllable: colder.'),
    ('The cabin is ___ than a seat.', 'Three syllables.', 'more expensive',
     ['more expensive', 'expensiver', 'more expensiver', 'expensivier'], 'Three syllables: more expensive.'),
    ('Our boat is ___ than theirs.', 'Double the consonant.', 'bigger',
     ['bigger', 'biger', 'more big', 'biggger'], 'Short vowel + one consonant: bigger.'),
    ('She seems ___ at sea.', 'Two syllables ending in -y.', 'happier',
     ['happier', 'more happy', 'happyer', 'more happier'], 'Y becomes i: happier.'),
    ('Be ___ on deck in the rain.', 'Two syllables, not -y.', 'more careful',
     ['more careful', 'carefuller', 'more carefuller', 'carefulier'], 'Two syllables, not -y: more careful.'),
    ('The weather is ___ today.', 'A Lone Stack.', 'better',
     ['better', 'gooder', 'more good', 'more better'], 'Good, better.'),
    ('The storm was ___ than we expected.', 'A Lone Stack.', 'worse',
     ['worse', 'badder', 'more bad', 'worser'], 'Bad, worse.'),
    ('The new harbour is ___.', 'Ends in -e.', 'nicer',
     ['nicer', 'niceer', 'more nice', 'nicier'], 'Ends in -e: just add -r.'),
    ('Sailing is ___ than I thought.', 'The False Cape.', 'more fun',
     ['more fun', 'funner', 'funnier', 'more funner'], 'Fun is short, but it takes more.'),
    ('This route is ___ than the coast road.', 'Two syllables ending in -y.', 'easier',
     ['easier', 'more easy', 'easyer', 'more easier'], 'Easy, easier.'),
    ('The island is ___ than it looks.', 'A Lone Stack.', 'farther',
     ['farther', 'farer', 'more far', 'farrer'], 'Far, farther (or further).'),
    ('Which sentence is right?', 'One coast at a time.', 'The north coast is more beautiful and quieter.',
     ['The north coast is more beautiful and quieter.', 'The north coast is beautifuller and more quieter.',
      'The north coast is more beautifuller and quieter.', 'The north coast is beautifuller and quieter.'],
     'More beautiful (long); quieter (the Shallows, either way).'),
]

PANELS = [
    [('er-' + a, '<b>%s, %s</b> %s' % (a, c, s)) for a, c, _, s in ER],
    [('more-' + a, '<b>%s</b> %s' % (c, s)) for a, c, s in MORE],
    [('lone-' + a, '<b>%s, %s</b> %s' % (a, c, s)) for a, c, s in LONE] +
    [('shallows', '<b>The Shallows</b> <em>clever</em>, <em>narrow</em>, <em>quiet</em>: either way'),
     ('cape', '<b>The False Cape</b> <em>more fun</em>, <em>more real</em>, <em>more right</em>')],
]
TARGETS = {}
for a, _, _, _ in ER:
    TARGETS['er-' + a] = (0, 'er-' + a, '#0c5669')
for a, _, _ in MORE:
    TARGETS['more-' + a] = (1, 'more-' + a, '#0c5669')
for a, _, _ in LONE:
    TARGETS['lone-' + a] = (2, 'lone-' + a, '#0c5669')
TARGETS['shallows'] = (2, 'shallows', '#0c5669')
TARGETS['cape'] = (2, 'cape', '#B4441F')

import ex_tr_ermore as T
L.build(OUT, ART, 'The -ER Coast &amp; the MORE Coast &mdash; Comparatives', 'Comparatives', EXTRACTED,
        HERO, 'never follow the rule.', ('order', 'Read the chart'),
        RULES + EXTRAS + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        [WEST_LAND, EAST_LAND, SEA], T.T,
        ['Clean run. You count the syllables and the coast follows.',
         'Solid progress. Check the Lone Stacks again: better, worse, farther.',
         'Good first attempt. Start with one word from each coast: colder, more expensive.'],
        ('sailing-the-seas-of-grammar.html', 'Back to the first chart: Gerundia &amp; Infinitivia'), gull_seed=103,
        long_name=24)
