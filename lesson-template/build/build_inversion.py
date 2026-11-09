# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: The Inversion Maelstrom, negative inversion
as a whirlpool that spins the auxiliary in front of the subject. The eighth
chart.

    py lesson-template/build/build_inversion.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. Nine rocks ring the whirlpool, one for each negative or
restrictive opening (Never, Rarely, Seldom, Hardly, No sooner, Little, Not
only, Only then, Under no circumstances). Sail past one at the start of a
sentence and the auxiliary spins round in front of the subject, as in a
question: I have never seen becomes Never have I seen. No auxiliary? do
appears: Rarely do we sail at night.

THE ART. Layout by sea_layouts_3.py (docs/sea-charts/inversion-maelstrom.png),
painted by ChatGPT on 2026-11-09 with Gerundia as the style. Nine dots
measured by sea_measure.py into inversion_chart.json, one per islet.
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE

OUT = 'sailing-the-seas-inversion.html'
ART = 'sailing-the-seas-inversion'
UID = 'inv'

# py lesson-template/extract-palette.py sailing-the-seas-inversion/hero.jpg --light
EXTRACTED = {'text': '#2a2211', 'text-dim': '#5e4f2e', 'secondary': '#24586f', 'contrast': '#0a586b'}

D = O.load('inversion_chart.json')
DOTS = [tuple(p) for p in D['dots']]
assert len(DOTS) == 9, DOTS


def near(x, y):
    p = min(DOTS, key=lambda q: abs(q[0] - x) + abs(q[1] - y))
    assert abs(p[0] - x) + abs(p[1] - y) < 12, (x, y, p)
    return p


# (signal, the spun opening, a sentence, dot, group: 0 one word, 1 a longer opening)
ROCKS = [
    ('Never', 'Never have I&#8230;', 'Never have I seen such a storm.', (768, 197), 0),
    ('Rarely', 'Rarely does it&#8230;', 'Rarely does the sea freeze here.', (1081, 270), 0),
    ('Seldom', 'Seldom has it&#8230;', 'Seldom has the port been so quiet.', (1258, 472), 0),
    ('Not only', 'Not only did it&#8230;', 'Not only did it rain, it snowed.', (1199, 680), 1),
    ('No sooner', 'No sooner had we&#8230;', 'No sooner had we left than it rained.', (944, 829), 1),
    ('Hardly', 'Hardly had we&#8230;', 'Hardly had we left when it rained.', (553, 830), 0),
    ('Little', 'Little did they&#8230;', 'Little did they know the danger.', (314, 674), 0),
    ('Only then', 'Only then did I&#8230;', 'Only then did I see the rocks.', (271, 472), 1),
    ('Under no circumstances', 'Under no circumstances should you&#8230;',
     'Under no circumstances should you swim.', (437, 278), 1),
]
ROCKS = [(a, b, c, near(*p), g) for a, b, c, p, g in ROCKS]
INK, ROCK_PAINT = '#21190C', '#E8DDB8'
SEA_INK = '#10303C'


def key(w):
    return w.lower().replace(' ', '-')


def overlay():
    spots, names = [], []
    for sig, spun, sent, (x, y), g in ROCKS:
        names.append(O.name(x, y, (sig, spun, sent), INK, ROCK_PAINT, size=20, dy=-16, fit=False, halo=.15))
        spots.append(O.hotspot(UID, key(sig), O.circle_path(x, y, 58), '%s: %s' % (sig, sent)))
    spots.append(O.hotspot(UID, 'maelstrom', O.circle_path(768, 500, 150), 'The maelstrom: the auxiliary spins round'))
    caps = [O.cap(768, 60, 'THE INVERSION MAELSTROM', SEA_INK, 38, face=O.SERIF, spacing='.04em'),
            O.cap(768, 90, 'sail past these rocks and the auxiliary spins in front of the subject', SEA_INK, 18,
                  face=O.SERIF, weight=600, spacing='0', style='italic'),
            O.cap(64, 930, 'IN: I have never seen', SEA_INK, 21, 'start', face=O.SERIF, spacing='0'),
            O.cap(64, 962, 'OUT: Never have I seen', SEA_INK, 21, 'start', face=O.SERIF, spacing='0'),
            O.cap(1290, 930, 'no auxiliary? do appears:', SEA_INK, 18, weight=600, spacing='0', style='italic'),
            O.cap(1290, 960, 'Rarely do we sail at night.', SEA_INK, 18, weight=600, spacing='0', style='italic')]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated sea chart of a great whirlpool, a small ship tipped on its side in the middle. Nine rocky '
            'islets ring it: Never, Rarely, Seldom, Not only, No sooner, Hardly, Little, Only then and Under no '
            'circumstances. Bottom left: in, I have never seen; out, Never have I seen. Bottom right: no auxiliary? '
            'do appears: Rarely do we sail at night.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; negative inversion', 'The Inversion Maelstrom',
    'Start a sentence with <em>never</em>, <em>rarely</em> or <em>not only</em> and something strange happens: the '
    'sentence turns round like a question. <em>I have never seen</em> becomes <em>Never have I seen</em>. On this '
    'chart the nine rocks that cause it ring a whirlpool. Sail past a rock, and the auxiliary spins round.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the whirlpool</div>
      <h2>Rock first, then the spin</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Inversion is formal and dramatic: speeches, stories, essays, news. The everyday sentence is always correct too; the spun one adds weight.</p>
      ''' + rule_grid([
    ('Swap the auxiliary and the subject',
     'After the rock, the word order is a question&#39;s: auxiliary, then subject, then the rest.',
     ex('<em>Never have I</em> seen such a storm.')),
    ('No auxiliary? <em>do</em> appears',
     'In the present simple and past simple there is nothing to spin, so <em>do, does</em> or <em>did</em> comes up from the deep.',
     ex('<em>Rarely do we</em> sail at night.')),
    ('<em>Be</em> spins on its own',
     'With <em>am, is, are, was, were</em> as the main verb, <em>be</em> itself moves.',
     ex('<em>Seldom is the harbour</em> this quiet.')),
    ('<em>No sooner &#8230; than</em>, <em>Hardly &#8230; when</em>',
     'One thing happened straight after another. Past perfect after the rock, then <em>than</em> or <em>when</em>.',
     ex('<em>No sooner had we</em> left <em>than</em> it began to rain.')),
    ('<em>Not only &#8230; but also</em>',
     'Spin the first half only. The second half keeps normal order.',
     ex('<em>Not only did the mast</em> break, but the engine also failed.')),
    ('Rules and warnings',
     '<em>Under no circumstances</em>, <em>On no account</em>, <em>At no time</em>: the formal way to say never.',
     ex('<em>Under no circumstances should you</em> leave the boat.')),
]) + chart(
    'The nine rocks',
    'Each everyday sentence on the left means the same as the spun one on the right.',
    ['Rock', 'Everyday order', 'After the maelstrom'],
    [['Never', 'I have never seen a whale.', 'Never have I seen a whale.'],
     ['Rarely', 'We rarely sail at night.', 'Rarely do we sail at night.'],
     ['Seldom', 'The port is seldom so quiet.', 'Seldom is the port so quiet.'],
     ['Hardly', 'We had hardly left when it rained.', 'Hardly had we left when it rained.'],
     ['No sooner', 'We had no sooner left than it rained.', 'No sooner had we left than it rained.'],
     ['Little', 'They didn&#39;t know the danger at all.', 'Little did they know the danger.'],
     ['Not only', 'It not only rained, it also snowed.', 'Not only did it rain, it also snowed.'],
     ['Only then', 'I only saw the rocks then.', 'Only then did I see the rocks.'],
     ['Under no circumstances', 'You must not swim, whatever happens.', 'Under no circumstances should you swim.']]) + '''
    </div>

    '''

ONLY = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The far side of the rock</div>
      <h2><em>Only</em> and <em>not until</em>: the spin comes later</h2>
      <p class="chart-note" style="margin:-6px 0 18px">With <em>Only when</em>, <em>Only after</em>, <em>Only if</em> and <em>Not until</em> the rock is a whole clause. The spin waits until that clause is finished, then happens in the main clause.</p>
      ''' + chart(
    'One clause, then the spin',
    'The first clause keeps normal order. The auxiliary spins in the second.',
    ['Rock', 'First clause (normal)', 'Main clause (spun)'],
    [['Only when', 'Only when the fog lifted', 'did we see the coast.'],
     ['Only after', 'Only after the storm passed', 'could we leave the harbour.'],
     ['Only if', 'Only if the wind drops', 'will the ferry sail.'],
     ['Not until', 'Not until we reached land', 'did we feel safe.']]) + '''
      ''' + exi('Only when the fog lifted <em>did we see</em> the coast.') + chart(
    'Spin or no spin?',
    'The rock has to be at the very start of the sentence, and it has to limit or deny the whole sentence.',
    ['Sentence', 'Spin?', 'Why'],
    [['Never have I been so cold.', 'yes', 'the rock opens the sentence'],
     ['I have never been so cold.', 'no', 'the rock is in the middle'],
     ['Only Tom knew the way.', 'no', '<em>only</em> limits the subject, Tom'],
     ['Only then did Tom know the way.', 'yes', '<em>only then</em> limits the whole sentence'],
     ['Hardly anyone came.', 'no', '<em>hardly</em> limits <em>anyone</em>, the subject']]) + '''
      ''' + exi('<em>Little did they know</em> what lay ahead.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a rock and its line lights up below; click the whirlpool for the rule. Switch the chart to see each '
    'rock spin the start of a sentence, then a whole sentence: the auxiliary always lands in front of the subject.',
    ('The rocks', 'The spin', 'In a sentence'),
    [('One-word rocks', 'is-west'), ('Longer rocks', 'is-isle'), ('The whirlpool', 'is-east')],
    'Drag the chart sideways to reach the eastern rocks.', min_zoom=1000)

TRAPS = fork(
    'Caught in the current',
    'Most mistakes forget the spin, forget <em>do</em>, or pair the wrong words.',
    ['Not this', 'This', 'Why'],
    [['Never I have seen such a storm.', 'Never have I seen such a storm.', 'spin the auxiliary'],
     ['Rarely we sail at night.', 'Rarely do we sail at night.', 'no auxiliary: <em>do</em> appears'],
     ['Not only she sings, but she also dances.', 'Not only does she sing, but she also dances.', '<em>does</em>, and <em>sing</em> without -s'],
     ['No sooner had we left when it rained.', 'No sooner had we left than it rained.', '<em>no sooner</em> takes <em>than</em>'],
     ['Hardly had we left than it rained.', 'Hardly had we left when it rained.', '<em>hardly</em> takes <em>when</em>'],
     ['Only when the fog lifted we saw the coast.', 'Only when the fog lifted did we see the coast.', 'spin the main clause']],
    'After <em>do, does, did</em> the main verb goes back to its base form: <em>did we see</em>, never <em>did we saw</em>.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-register.html', 'The heights of register')])

SIGNALS = signals(
    'These rocks spin',
    ['<em>Never</em>, <em>Rarely</em>, <em>Seldom</em>', '<em>Hardly &#8230; when</em>, <em>Scarcely &#8230; when</em>',
     '<em>No sooner &#8230; than</em>', '<em>Little</em> (meaning not at all)', '<em>Not only &#8230; but also</em>',
     '<em>Only then</em>, <em>Only when</em>, <em>Not until</em>', '<em>Under no circumstances</em>, <em>On no account</em>'],
    'These do not',
    ['the rock in the middle: <em>I have never seen</em>', '<em>Only</em> + the subject: <em>Only Tom knew</em>',
     '<em>Hardly anyone</em>, <em>Never mind</em>', 'everyday speech: <em>I&#39;ve never seen that!</em>',
     '<em>Not long ago</em>, <em>Not far away</em> (time and place, not denial)'],
    'One test: can you put the rock in front and make the rest a question (have I seen? do we sail?)? Then spin it.')

QUIZ = [
    ('Never ___ such a storm.', 'Spin the auxiliary.', 'have I seen',
     ['have I seen', 'I have seen', 'I saw', 'did I saw'], 'Never have I seen: auxiliary, then subject.'),
    ('Rarely ___ at night.', 'Present simple: no auxiliary to spin.', 'do we sail',
     ['do we sail', 'we sail', 'we do sail', 'sail we'], 'No auxiliary? do appears: Rarely do we sail.'),
    ('No sooner had we left ___ it began to rain.', 'Which word pairs with no sooner?', 'than',
     ['than', 'when', 'then', 'that'], 'No sooner ... than.'),
    ('Hardly had we left ___ it began to rain.', 'Which word pairs with hardly?', 'when',
     ['when', 'than', 'that', 'so'], 'Hardly ... when.'),
    ('Not only ___, but she also dances.', 'Spin, and the verb goes back to its base.', 'does she sing',
     ['does she sing', 'she sings', 'does she sings', 'sings she'], 'Not only does she sing: does carries the -s.'),
    ('Little ___ what lay ahead.', 'Past simple, spun.', 'did they know',
     ['did they know', 'they knew', 'did they knew', 'knew they'], 'Little did they know: did, then the base form.'),
    ('Seldom ___ so quiet.', 'Be spins on its own.', 'is the harbour',
     ['is the harbour', 'the harbour is', 'does the harbour be', 'the harbour does'], 'Be moves itself: Seldom is the harbour so quiet.'),
    ('Only when the fog lifted ___ the coast.', 'The spin waits for the main clause.', 'did we see',
     ['did we see', 'we saw', 'we did see', 'saw we'], 'Only when ... , then spin: did we see.'),
    ('Under no circumstances ___ the boat.', 'A warning: should, spun.', 'should you leave',
     ['should you leave', 'you should leave', 'you leave', 'should you to leave'], 'Under no circumstances should you leave.'),
    ('Which sentence is correct?', 'Only + the subject does not spin.', 'Only Tom knew the way.',
     ['Only Tom knew the way.', 'Only did Tom know the way.', 'Only knew Tom the way.', 'Only Tom did knew the way.'],
     'Only limits Tom, the subject, so the sentence keeps normal order.'),
    ('Which sentence is NOT correct?', 'One forgot to spin.', 'Never I have been so cold.',
     ['Never I have been so cold.', 'Never have I been so cold.', 'I have never been so cold.', 'Rarely have I been so cold.'],
     'After Never at the start: Never have I been.'),
    ('Which is the everyday version of Seldom do we see whales?', 'Unspin it.', 'We seldom see whales.',
     ['We seldom see whales.', 'We do seldom whales see.', 'Seldom we see whales.', 'We see seldom whales.'],
     'Move the rock back to the middle and do disappears: We seldom see whales.'),
]

PANELS = [
    [(key(r[0]), '<b>%s</b> %s' % (r[0], r[2])) for r in ROCKS if r[4] == 0],
    [(key(r[0]), '<b>%s</b> %s' % (r[0], r[2])) for r in ROCKS if r[4] == 1],
    [('maelstrom', '<b>The spin</b> auxiliary before subject, as in a question: <em>have I</em>, <em>had we</em>'),
     ('maelstrom', '<b>No auxiliary?</b> <em>do, does, did</em> appears: <em>Rarely do we sail</em>'),
     ('maelstrom', '<b>Be</b> spins on its own: <em>Seldom is the harbour so quiet</em>')],
]
TARGETS = {}
for r in ROCKS:
    TARGETS[key(r[0])] = (r[4], key(r[0]), '#0a586b')
TARGETS['maelstrom'] = (2, 'maelstrom', '#0a586b')

import ex_tr_inversion as T
L.build(OUT, ART, 'The Inversion Maelstrom &mdash; Negative Inversion', 'negative inversion', EXTRACTED,
        HERO, 'and the auxiliary spins round.', ('order', 'Read the chart'),
        RULES + ONLY + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        ['#C9B98A', '#B4A57A', '#7FA9BA'], T.T,
        ['Clean run. You can sail past every rock and spin the sentence round.',
         'Solid progress. Say it as a question first: have I seen? do we sail?',
         'Good first attempt. Start with Never have I seen, then add do: Rarely do we sail.'],
        ('sailing-the-seas-atlantic.html', 'Next chart: the Atlantic'), gull_seed=37, long_name=24)
