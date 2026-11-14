# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: The Bridges, linking words as three ways to
cross. The nineteenth chart.

    py lesson-template/build/build_bridges.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. Two ideas stand on two shores: IT WAS STORMY and WE
SAILED. There are three ways to join them, and they differ in grammar, not
in meaning. A BRIDGE joins both clauses in one sentence (although, but,
because, so, while). A FERRY leaves the first shore as a finished sentence
and starts a new one (However, Nevertheless, Therefore), with a full stop
before it and a comma after. A PIER reaches out from one shore only: it is
followed by a noun or -ING, not a clause (despite, in spite of, because
of, due to).

No tense on this chart, so no Sherpa colours.

THE ART. Layout by sea_layouts_5.py, painted by Codex on 2026-11-14.
sea_measure.py found the 6 crossing dots, all at x=768, and four strays in
the scenery (bridges_chart.json); the strays are dropped by position below.
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE

OUT = 'sailing-the-seas-bridges.html'
ART = 'sailing-the-seas-bridges'
UID = 'brid'

# py lesson-template/extract-palette.py sailing-the-seas-bridges/hero.jpg --light
EXTRACTED = {'text': '#2a2311', 'text-dim': '#5e502e', 'secondary': '#accfdd', 'contrast': '#09556c'}

D = O.load('bridges_chart.json')
DOTS = sorted((tuple(p) for p in D['dots'] if abs(p[0] - 768) < 8), key=lambda p: p[1])
assert len(DOTS) == 6, D['dots']

# (key, linker, what kind of crossing, sentence)
STOPS = [('although', 'although', 'a bridge: one sentence', 'Although it was stormy, we sailed.'),
         ('but', 'but', 'a bridge: one sentence', 'It was stormy, but we sailed.'),
         ('however', 'However,', 'a ferry: a new sentence', 'It was stormy. However, we sailed.'),
         ('nevertheless', 'Nevertheless,', 'a ferry: a new sentence', 'It was stormy. Nevertheless, we sailed.'),
         ('despite', 'despite', 'a pier: + noun or -ING', 'Despite the storm, we sailed.'),
         ('in-spite-of', 'in spite of', 'a pier: + noun or -ING', 'In spite of the storm, we sailed.')]
INK, WEST_LAND, EAST_LAND, SEA = '#20180A', '#AEC18E', '#E9CF9A', '#B4D6E1'


def overlay():
    spots, names = [], []
    sea_ink = '#0F2F3D'
    for (key, word, kind, sent), (x, y) in zip(STOPS, DOTS):
        names.append(O.name(x, y, (word, kind, sent), sea_ink, SEA, size=19, dy=-18, fit=False, halo=.55))
        spots.append(O.hotspot(UID, key, O.rect_path(500, y - 30, 1036, y + 30), '%s: %s' % (word, kind)))
    caps = [O.cap(768, 62, 'THE BRIDGES', sea_ink, 42, face=O.SERIF, spacing='.05em'),
            O.cap(768, 98, 'join two ideas: a bridge, a ferry or a pier?', sea_ink, 20, face=O.SERIF, weight=600,
                  spacing='0', style='italic'),
            O.cap(268, 190, 'IT WAS STORMY', INK, 26, face=O.SERIF, spacing='.02em', halo=WEST_LAND),
            O.cap(268, 218, 'the first idea', INK, 16, weight=600, spacing='0', style='italic', halo=WEST_LAND),
            O.cap(1268, 190, 'WE SAILED', INK, 26, face=O.SERIF, spacing='.02em', halo=EAST_LAND),
            O.cap(1268, 218, 'the second idea', INK, 16, weight=600, spacing='0', style='italic', halo=EAST_LAND),
            O.cap(768, 252, 'BRIDGES', sea_ink, 22, face=O.SERIF, spacing='.05em', halo=SEA),
            O.cap(768, 276, 'one sentence: because &#183; although &#183; but &#183; so &#183; while', sea_ink, 14, weight=600,
                  spacing='0', style='italic', halo=SEA),
            O.cap(768, 496, 'FERRIES', sea_ink, 22, face=O.SERIF, spacing='.05em', halo=SEA),
            O.cap(768, 520, 'a new sentence first: . However, &#8230; Therefore, &#8230;', sea_ink, 14, weight=600,
                  spacing='0', style='italic', halo=SEA),
            O.cap(768, 730, 'PIERS', sea_ink, 22, face=O.SERIF, spacing='.05em', halo=SEA),
            O.cap(768, 754, 'a noun or -ING after them', sea_ink, 14, weight=600, spacing='0', style='italic', halo=SEA)]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated chart of a strait between two shores. The green west shore, under storm clouds, is IT WAS '
            'STORMY, the first idea. The sandy east shore, with ships setting sail, is WE SAILED, the second idea. '
            'Six crossings join them: two wooden bridges, although and but; two dashed ferry lanes, However and '
            'Nevertheless; and two piers, despite and in spite of.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; Linking words', 'The Bridges',
    '<em>It was stormy. We sailed.</em> Two ideas, and something surprising between them. English gives you three '
    'ways to cross: a bridge joins them in one sentence, a ferry starts a new sentence, and a pier takes a noun, '
    'not a clause. The meaning is the same. Read each crossing, then choose by the grammar around the gap.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the crossings</div>
      <h2>Same meaning, three kinds of grammar</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Look at what comes before and after the gap. A full stop before it? A ferry. A subject and a verb after it? A bridge. Only a noun or -ING after it? A pier.</p>
      ''' + rule_grid([
    ('A bridge: one sentence, two clauses',
     '<em>Although</em> goes at the start of its clause; a comma follows that clause if it comes first.',
     ex('<em>Although</em> it was stormy, we sailed.')),
    ('A bridge: but in the middle',
     '<em>But</em> stands between the two clauses, after a comma.',
     ex('It was stormy, <em>but</em> we sailed.')),
    ('A ferry: a new sentence',
     'Full stop, capital letter, comma. <em>However</em> cannot join two clauses with only a comma.',
     ex('It was stormy. <em>However,</em> we sailed.')),
    ('A ferry: the formal ones',
     '<em>Nevertheless</em> and <em>Nonetheless</em> work the same way, and are more formal.',
     ex('It was stormy. <em>Nevertheless,</em> we sailed.')),
    ('A pier: a noun after it',
     '<em>Despite</em> is followed by a noun, never by a subject and a verb.',
     ex('<em>Despite</em> the storm, we sailed.')),
    ('A pier: or -ING',
     '<em>In spite of</em> is the same, with <em>of</em>. Both also take -ING.',
     ex('<em>In spite of</em> feeling ill, she sailed.')),
]) + chart(
    'The six crossings',
    'One meaning, six sentences. Watch the punctuation.',
    ['Crossing', 'Word', 'Sentence'],
    [['bridge', 'although', 'Although it was stormy, we sailed.'], ['bridge', 'but', 'It was stormy, but we sailed.'],
     ['ferry', 'However,', 'It was stormy. However, we sailed.'],
     ['ferry', 'Nevertheless,', 'It was stormy. Nevertheless, we sailed.'],
     ['pier', 'despite', 'Despite the storm, we sailed.'], ['pier', 'in spite of', 'In spite of the storm, we sailed.']]) + '''
    </div>

    '''

EXTRAS = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Other cargo</div>
      <h2>The same three crossings carry reason and result</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Contrast is only one cargo. The words change, the three kinds of grammar do not.</p>
      ''' + chart(
    'Reason and result, by crossing',
    'Read down a column to stay on one kind of crossing.',
    ['Cargo', 'Bridge', 'Ferry', 'Pier'],
    [['contrast', 'although, but, while', 'However, Nevertheless,', 'despite, in spite of'],
     ['reason', 'because, as, since', '(none in common use)', 'because of, due to'],
     ['result', 'so', 'Therefore, As a result,', '(none in common use)'],
     ['addition', 'and', 'Moreover, In addition,', 'as well as, in addition to']]) + '''
      ''' + exi('We stayed in <em>because</em> it was raining. We stayed in <em>because of</em> the rain.') + chart(
    'One idea, three crossings',
    'The same reason, written three ways.',
    ['Crossing', 'Sentence'],
    [['bridge', 'The ferry was late because the sea was rough.'],
     ['ferry', 'The sea was rough. Therefore, the ferry was late.'],
     ['pier', 'The ferry was late because of the rough sea.']]) + '''
      ''' + exi('The sea was rough. <em>Therefore,</em> the ferry was late.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a crossing and its line lights up below: bridges on the left, ferries in the middle, piers on the '
    'right. Switch the chart to see what kind each crossing is, then its sentence.',
    ('The words', 'The crossing', 'The sentence'),
    [('Bridges: one sentence', 'is-west'), ('Ferries: a new sentence', 'is-isle'), ('Piers: + noun or -ING', 'is-east')],
    'Drag the chart sideways to see both shores.', min_zoom=1000)

TRAPS = fork(
    'Wrong crossing',
    'Each of these uses the right word with the wrong grammar.',
    ['Not this', 'This', 'Why'],
    [['Despite it was stormy, we sailed.', 'Although it was stormy, we sailed. / Despite the storm, we sailed.',
      'a pier takes a noun, not a clause'],
     ['It was stormy, however we sailed.', 'It was stormy. However, we sailed.', 'a ferry needs a full stop'],
     ['Although it was stormy, but we sailed.', 'Although it was stormy, we sailed.', 'one bridge is enough'],
     ['In spite the storm, we sailed.', 'In spite of the storm, we sailed.', '<em>of</em> is part of it'],
     ['Despite of the storm, we sailed.', 'Despite the storm, we sailed.', 'no <em>of</em> after despite'],
     ['We stayed in because of it was raining.', 'We stayed in because it was raining.', 'a clause follows: a bridge']],
    'In an exam gap, read the three words after the gap first. A subject and a verb? Although. A noun? Despite.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-backshift.html', 'The Backshift Current')])

SIGNALS = signals(
    'It is a bridge or a ferry',
    ['a subject and a verb follow the gap', 'a full stop before the gap: a ferry', 'a comma after the word: a ferry',
     'no full stop: a bridge', '<em>although</em>, <em>but</em>, <em>because</em>, <em>so</em>',
     '<em>However,</em> <em>Therefore,</em>'],
    'It is a pier',
    ['a noun follows the gap: <em>the storm</em>', 'or -ING: <em>feeling ill</em>', 'no subject and verb after it',
     '<em>despite</em>, <em>in spite of</em>', '<em>because of</em>, <em>due to</em>', '<em>the fact that</em> turns it back into a bridge'],
    'One test: can you find a subject and a verb after the gap? If not, you need a pier.')

QUIZ = [
    ('___ it was stormy, we sailed.', 'A subject and a verb follow.', 'Although',
     ['Although', 'Despite', 'However', 'In spite'], 'A clause follows, in one sentence: although.'),
    ('___ the storm, we sailed.', 'A noun follows.', 'Despite',
     ['Despite', 'Although', 'However', 'But'], 'A noun follows: despite.'),
    ('It was stormy. ___, we sailed.', 'A full stop before, a comma after.', 'However',
     ['However', 'Although', 'Despite', 'But'], 'A new sentence, with a comma: However,'),
    ('It was stormy, ___ we sailed.', 'One sentence, in the middle.', 'but',
     ['but', 'however', 'despite', 'nevertheless'], 'Between two clauses, after a comma: but.'),
    ('In spite ___ the storm, we sailed.', 'One small word.', 'of',
     ['of', 'from', 'to', 'for'], 'In spite of.'),
    ('___ feeling ill, she went to work.', '-ING follows.', 'Despite',
     ['Despite', 'Although', 'However', 'Because'], 'A pier takes -ING: despite feeling ill.'),
    ('We stayed in ___ the rain.', 'A noun follows.', 'because of',
     ['because of', 'because', 'although', 'so'], 'A noun follows: because of the rain.'),
    ('We stayed in ___ it was raining.', 'A clause follows.', 'because',
     ['because', 'because of', 'despite', 'due to'], 'A clause follows: because it was raining.'),
    ('The sea was rough. ___, the ferry was late.', 'A result, in a new sentence.', 'Therefore',
     ['Therefore', 'Because', 'So that', 'Despite'], 'A ferry for a result: Therefore,'),
    ('Which sentence is right?', 'Check the punctuation.', 'It was late. Nevertheless, we went out.',
     ['It was late. Nevertheless, we went out.', 'It was late, nevertheless we went out.',
      'Nevertheless it was late, we went out.', 'It was late nevertheless, we went out.'],
     'A ferry: full stop before, comma after.'),
    ('Which sentence is right?', 'One bridge is enough.', 'Although he was tired, he kept walking.',
     ['Although he was tired, he kept walking.', 'Although he was tired, but he kept walking.',
      'Despite he was tired, he kept walking.', 'Although of being tired, he kept walking.'],
     'Although on its own; never although with but.'),
    ('Which word can NOT fill the gap? ___ the bad weather, the race went ahead.', 'A noun follows.', 'Although',
     ['Although', 'Despite', 'In spite of', 'Because of'], 'Although needs a clause; the others take a noun.'),
]

PANELS = [
    [('although', '<b>although</b> Although it was stormy, we sailed.'),
     ('but', '<b>but</b> It was stormy, but we sailed.'),
     ('although', 'also: <em>because</em>, <em>so</em>, <em>while</em>')],
    [('however', '<b>However,</b> It was stormy. However, we sailed.'),
     ('nevertheless', '<b>Nevertheless,</b> It was stormy. Nevertheless, we sailed.'),
     ('however', 'also: <em>Therefore,</em> <em>Moreover,</em>')],
    [('despite', '<b>despite</b> Despite the storm, we sailed.'),
     ('in-spite-of', '<b>in spite of</b> In spite of the storm, we sailed.'),
     ('despite', 'also: <em>because of</em>, <em>due to</em>')],
]
TARGETS = {'although': (0, 'although', '#09556c'), 'but': (0, 'but', '#09556c'),
           'however': (1, 'however', '#09556c'), 'nevertheless': (1, 'nevertheless', '#09556c'),
           'despite': (2, 'despite', '#09556c'), 'in-spite-of': (2, 'in-spite-of', '#09556c')}

import ex_tr_bridges as T
L.build(OUT, ART, 'The Bridges &mdash; Linking Words', 'Linking words', EXTRACTED,
        HERO, 'then choose by the grammar around the gap.', ('order', 'Read the chart'),
        RULES + EXTRAS + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        ['#B89B6E', SEA, '#C9B48A'], T.T,
        ['Clean run. You choose the crossing by the grammar around the gap.',
         'Solid progress. Check the piers again: a noun or -ING, never a clause.',
         'Good first attempt. Start with one pair: although it was stormy, despite the storm.'],
        ('sailing-the-seas-of-grammar.html', 'Back to the first chart: Gerundia &amp; Infinitivia'), gull_seed=79,
        long_name=24)
