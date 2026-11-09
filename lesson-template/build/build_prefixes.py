# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: The Prefix Archipelago, negative prefixes as
a mainland and six islands. The fifth chart.

    py lesson-template/build/build_prefixes.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. UN- is the mainland: most everyday adjectives sail there
(unhappy, unkind, unusual), and it also reverses actions (unlock). Out to sea
lie the islands, each with its own rule: IN- for the rest of the Latin words,
whose spelling bends to the next sound (IM- before p and m, IL- before l,
IR- before r), DIS- for not / the opposite, MIS- for wrongly. The False Cape
flies a flag for the trap: inflammable means flammable.

THE ART. Layout by sea_layouts_2.py (docs/sea-charts/prefix-archipelago.png),
painted by Codex on 2026-11-09 with Gerundia as the style. Dots measured by
sea_measure.py into prefixes_chart.json: 24 blobs, of which three are not
harbours (a cliff at (376,88) and (424,452), the lighthouse at (1126,196));
the 21 below were matched to the painting by eye on a marked copy.
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE

OUT = 'sailing-the-seas-prefixes.html'
ART = 'sailing-the-seas-prefixes'
UID = 'pfx'

# py lesson-template/extract-palette.py sailing-the-seas-prefixes/hero.jpg --light
EXTRACTED = {'text': '#2a1e11', 'text-dim': '#5e482e', 'secondary': '#adccd4', 'contrast': '#075155'}

D = O.load('prefixes_chart.json')
NOT_HARBOURS = {(376, 88), (424, 452), (1126, 196)}
assert {tuple(p) for p in D['dots']} >= NOT_HARBOURS
LANDS = {'un': (207, 504), 'im': (670, 242), 'il': (1078, 237), 'in': (893, 483),
         'ir': (1337, 432), 'dis': (654, 710), 'mis': (1237, 713), 'cape': (972, 908)}
SHAPE = {k: O.shape_at(D, *p) for k, p in LANDS.items()}
PAINT = {k: s['colour'] for k, s in SHAPE.items()}
INK = {k: O.ink_for(p, 7) for k, p in PAINT.items()}
SEA_INK = O.ink_for(D['sea'], 7.5)

# (dot, land, place name, the word, with its prefix)
HARBOURS = [
    ((222, 180), 'un', 'Happy Harbour', 'happy', 'unhappy'),
    ((291, 314), 'un', 'Kind Cove', 'kind', 'unkind'),
    ((174, 452), 'un', 'Fair Point', 'fair', 'unfair'),
    ((289, 566), 'un', 'Able Head', 'able', 'unable'),
    ((215, 692), 'un', 'Usual Sands', 'usual', 'unusual'),
    ((616, 214), 'im', 'Possible Point', 'possible', 'impossible'),
    ((744, 252), 'im', 'Patient Cove', 'patient', 'impatient'),
    ((648, 298), 'im', 'Mature Head', 'mature', 'immature'),
    ((1010, 227), 'il', 'Legal Point', 'legal', 'illegal'),
    ((1100, 274), 'il', 'Logical Cove', 'logical', 'illogical'),
    ((1279, 416), 'ir', 'Regular Rock', 'regular', 'irregular'),
    ((1347, 479), 'ir', 'Responsible Head', 'responsible', 'irresponsible'),
    ((779, 455), 'in', 'Correct Cove', 'correct', 'incorrect'),
    ((1010, 483), 'in', 'Visible Point', 'visible', 'invisible'),
    ((906, 536), 'in', 'Expensive Ness', 'expensive', 'inexpensive'),
    ((570, 680), 'dis', 'Like Harbour', 'like', 'dislike'),
    ((740, 708), 'dis', 'Agree Point', 'agree', 'disagree'),
    ((649, 762), 'dis', 'Honest Head', 'honest', 'dishonest'),
    ((1138, 680), 'mis', 'Understand Sound', 'understand', 'misunderstand'),
    ((1320, 714), 'mis', 'Spell Point', 'spell', 'misspell'),
    ((1158, 758), 'mis', 'Lead Head', 'lead', 'mislead'),
]
assert len(HARBOURS) == 21
assert {h[0] for h in HARBOURS} | NOT_HARBOURS == {tuple(p) for p in D['dots']}, 'a measured dot is unaccounted for'

ARIA = {'un': 'The mainland, UN-: not, or reversing an action', 'im': 'IM- Isle: before p and m',
        'il': 'IL- Isle: before l', 'ir': 'IR- Isle: before r', 'in': 'IN- Isle: for the rest',
        'dis': 'DIS- Isle: not, or the opposite', 'mis': 'MIS- Isle: wrongly',
        'cape': 'The False Cape: inflammable means flammable'}


def overlay():
    spots = [O.hotspot(UID, k, O.poly_path(SHAPE[k]['poly']), ARIA[k]) for k in LANDS]
    names = [O.name(x, y, (p, w, pw), INK[k], PAINT[k]) for (x, y), k, p, w, pw in HARBOURS]
    s = SEA_INK
    caps = [O.cap(768, 60, 'THE PREFIX ARCHIPELAGO', s, 34, face=O.SERIF, spacing='.04em'),
            O.cap(768, 86, 'not, the opposite, or wrongly: which island?', s, 17, face=O.SERIF, weight=600, spacing='0', style='italic')]
    for x, y, t, sub in [(650, 114, 'IM- ISLE', 'before p and m'), (1058, 114, 'IL- ISLE', 'before l'),
                         (1342, 280, 'IR- ISLE', 'before r'), (906, 336, 'IN- ISLE', 'for the rest'),
                         (634, 574, 'DIS- ISLE', 'not, or the opposite'), (1214, 576, 'MIS- ISLE', 'wrongly')]:
        caps += [O.cap(x, y, t, s, 21, face=O.SERIF, spacing='.05em'),
                 O.cap(x, y + 22, sub, s, 14.5, weight=600, spacing='0', style='italic')]
    caps += [O.cap(46, 880, 'UN-', INK['un'], 56, 'start', O.SERIF, 700, '.02em'),
             O.cap(48, 912, 'the mainland &#183; most words', INK['un'], 18, 'start', O.SERIF, 600, '0', 'italic'),
             O.cap(1250, 893, 'THE FALSE CAPE', s, 20, face=O.SERIF, spacing='.05em'),
             O.cap(1250, 917, 'inflammable means flammable', s, 15, weight=600, spacing='0', style='italic')]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated sea chart. On the west, a large orange mainland marked UN-, with Happy Harbour, Kind Cove, '
            'Fair Point, Able Head and Usual Sands. Out to sea, six islands: IM- Isle with a windmill (before p and m), '
            'IL- Isle with a lighthouse (before l), IR- Isle with a castle (before r), IN- Isle with a harbour town, '
            'DIS- Isle with a ruined tower (not, or the opposite) and MIS- Isle with a shipwreck (wrongly). A small '
            'islet flies a red flag: the False Cape, inflammable means flammable.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; negative prefixes', 'The Prefix Archipelago',
    'To say <em>not</em> in front of a word, English has one big mainland and six islands. Most everyday words sail to '
    'the mainland and take <em>un-</em>. The rest live on islands, and each island has its own rule: one for words '
    'starting with p and m, one for l, one for r, one for <em>the opposite</em>, one for <em>wrongly</em>. '
    'Learn which island a word belongs to, and its spelling follows.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">The mainland and the islands</div>
      <h2>Which prefix makes the opposite?</h2>
      <p class="chart-note" style="margin:-6px 0 18px">A prefix never changes the word it sits on: you add it whole, even when that doubles a letter (<em>un + necessary = unnecessary</em>, <em>mis + spell = misspell</em>). What changes is which prefix the word takes.</p>
      ''' + rule_grid([
    ('UN- means <em>not</em>',
     'The mainland, and the safest guess for an everyday adjective: <em>unhappy, unkind, unusual, unfair, unable</em>.',
     ex('The crew were <em>unhappy</em> with the food.')),
    ('UN- also reverses an action',
     'With verbs, <em>un-</em> undoes what was done: <em>unlock, unpack, untie, undo</em>.',
     ex('We <em>unpacked</em> the boxes and <em>untied</em> the boat.')),
    ('IN- for the Latin words',
     'Many longer words from Latin take <em>in-</em>: <em>incorrect, invisible, inexpensive, informal, incomplete</em>.',
     ex('The second answer was <em>incorrect</em>.')),
    ('IN- bends before p, m, l, r',
     '<em>im-</em> before p and m (<em>impossible, immature</em>), <em>il-</em> before l (<em>illegal</em>), <em>ir-</em> before r (<em>irregular</em>).',
     ex('It is <em>illegal</em> to fish here, and <em>impossible</em> to hide.')),
    ('DIS- means <em>not</em>, or the opposite',
     'With feelings, actions and qualities: <em>dislike, disagree, dishonest, disappear, disconnect</em>.',
     ex('I <em>disagree</em>: the map is wrong.')),
    ('MIS- means <em>wrongly</em>',
     'Not the opposite, but done badly: <em>misunderstand, misspell, mislead, misplace</em>.',
     ex('Sorry, I <em>misunderstood</em> the question.')),
]) + chart(
    'Island by island',
    'The rule each island keeps, and words that live there. The im-, il- and ir- rules are strong habits, with a few exceptions on the mainland (<em>unpopular, unlucky, unreal</em>).',
    ['Where', 'Rule', 'Words'],
    [['UN- (mainland)', 'most everyday words; reverses verbs', 'unhappy, unkind, unusual, unlock, untie'],
     ['IM- Isle', 'before p and m', 'impossible, impatient, impolite, immature, immoral'],
     ['IL- Isle', 'before l', 'illegal, illogical, illiterate'],
     ['IR- Isle', 'before r', 'irregular, irresponsible, irrelevant'],
     ['IN- Isle', 'other Latin words', 'incorrect, invisible, inexpensive, informal'],
     ['DIS- Isle', 'not, or the opposite', 'dislike, disagree, dishonest, disappear'],
     ['MIS- Isle', 'wrongly', 'misunderstand, misspell, mislead, misplace']]) + '''
    </div>

    '''

PAIRS = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Two islands, two meanings</div>
      <h2>When a word can take two prefixes</h2>
      <p class="chart-note" style="margin:-6px 0 18px">A few words can land on two islands, and the meaning changes with the island. Most learners only need the first column; the second is where B2 and C1 writing gains precision.</p>
      ''' + chart(
    'Same word, two prefixes',
    'Read across: the prefix carries the difference.',
    ['Word', 'One island', 'The other'],
    [['satisfied', '<em>dissatisfied</em>: not pleased with something', '<em>unsatisfied</em>: not yet met (an unsatisfied need)'],
     ['organised', '<em>disorganised</em>: messy, badly run', '<em>unorganised</em>: not organised yet'],
     ['informed', '<em>misinformed</em>: told the wrong thing', '<em>uninformed</em>: not told anything'],
     ['interested', '<em>disinterested</em>: neutral, with nothing to gain', '<em>uninterested</em>: bored']]) + '''
      ''' + exi('I&#39;m <em>dissatisfied</em> with the service: the staff were <em>disorganised</em>.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click an island and its line lights up below. Switch the chart to <em>just the words</em> to see them bare, then to '
    '<em>with their prefix</em> to see each one sail home. Notice how every word on IM- Isle starts with p or m.',
    ('Place names', 'Just the words', 'With their prefix'),
    [('The mainland &middot; UN-', 'is-west'), ('IN- and its spellings', 'is-isle'), ('DIS- and MIS-', 'is-east')],
    'Drag the chart sideways to reach the islands.')

TRAPS = fork(
    'The False Cape: prefixes that are not what they seem',
    'These look as if a prefix turns them negative. It does not.',
    ['Word', 'Looks like', 'Really means'],
    [['inflammable', 'cannot burn', 'burns easily: the same as <em>flammable</em>'],
     ['invaluable', 'worth nothing', 'extremely valuable'],
     ['infamous', 'not famous', 'famous for something bad'],
     ['unravel', 'the opposite of <em>ravel</em>', 'come apart; <em>ravel</em> means nearly the same']],
    'On a warning sign, <em>inflammable</em> and <em>flammable</em> mean the same thing. The safe opposite is '
    '<em>non-flammable</em>.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-adjective-canal.html', 'The adjective canal')])

SIGNALS = signals(
    'Sail to the mainland &mdash; UN-',
    ['everyday adjectives: <em>happy, kind, fair, usual</em>', '<em>-ed</em> and <em>-ing</em> forms: <em>unexpected, unconvincing</em>',
     '<em>-able</em> words from English verbs: <em>unbreakable, unbelievable</em>', 'reversing an action: <em>unlock, unpack</em>',
     'a word you are unsure about: it is the commonest prefix', 'even before p, l, r: <em>unpopular, unlucky, unreal</em>'],
    'Sail to the islands',
    ['longer Latin words: <em>in-</em>', 'starting with p or m: <em>im-</em>', 'starting with l: <em>il-</em>', 'starting with r: <em>ir-</em>',
     'the opposite of a feeling or action: <em>dis-</em>', 'done wrongly: <em>mis-</em>'],
    'If you are not sure, <em>un-</em> is the best bet. The islands are smaller, and their words are mostly longer and more formal.')

QUIZ = [
    ('The story was hard to believe: it was ___.', 'An everyday adjective.', 'unlikely',
     ['unlikely', 'inlikely', 'dislikely', 'mislikely'], 'Likely is an everyday English word, so it takes un-: unlikely.'),
    ('It is ___ to park here.', 'Before l.', 'illegal',
     ['illegal', 'unlegal', 'inlegal', 'dislegal'], 'In- becomes il- before l: illegal.'),
    ('Learning every word is ___.', 'Before p.', 'impossible',
     ['impossible', 'inpossible', 'unpossible', 'dispossible'], 'In- becomes im- before p: impossible.'),
    ('Please ___ the hatch.', 'Reversing an action.', 'unlock',
     ['unlock', 'dislock', 'inlock', 'mislock'], 'Un- reverses an action: lock, unlock.'),
    ('Many English verbs are ___.', 'Before r.', 'irregular',
     ['irregular', 'unregular', 'inregular', 'disregular'], 'In- becomes ir- before r: irregular.'),
    ('I ___ with you: the map is wrong.', 'Not, or the opposite.', 'disagree',
     ['disagree', 'unagree', 'misagree', 'inagree'], 'Dis- makes the opposite of agree: disagree.'),
    ('Sorry, I ___ the question.', 'Done wrongly.', 'misunderstood',
     ['misunderstood', 'disunderstood', 'ununderstood', 'inunderstood'], 'Mis- means wrongly: misunderstood.'),
    ('The second answer is ___.', 'A Latin word, with no spelling change.', 'incorrect',
     ['incorrect', 'uncorrect', 'discorrect', 'imcorrect'], 'Correct comes from Latin and starts with c, so in- stays in-: incorrect.'),
    ('He is too young and ___ to be captain.', 'Before m.', 'immature',
     ['immature', 'unmature', 'inmature', 'dismature'], 'In- becomes im- before m: immature, with a double m.'),
    ('Inflammable means…', 'The False Cape.', 'it burns easily',
     ['it burns easily', 'it cannot burn', 'it is made of flame', 'it burns slowly'],
     'Inflammable means the same as flammable. The opposite is non-flammable.'),
    ('Which word is spelled correctly?', 'Add the prefix whole: no letters lost.', 'unnecessary',
     ['unnecessary', 'unecessary', 'unnecesary', 'innecessary'], 'Un + necessary keeps every letter, so the n doubles: unnecessary.'),
    ('Which is NOT a real word?', 'One word sailed to the wrong island.', 'unpossible',
     ['unpossible', 'unhappy', 'impolite', 'dishonest'], 'Possible starts with p, so it lives on IM- Isle: impossible.'),
]

PANELS = [
    [('un', '<b>UN-</b> unhappy &middot; unkind &middot; unfair &middot; unable &middot; unusual'),
     ('un', 'It also reverses actions: unlock, unpack, untie.')],
    [('im', '<b>IM-</b> before p and m: impossible &middot; impatient &middot; immature'),
     ('il', '<b>IL-</b> before l: illegal &middot; illogical'),
     ('ir', '<b>IR-</b> before r: irregular &middot; irresponsible'),
     ('in', '<b>IN-</b> the rest: incorrect &middot; invisible &middot; inexpensive')],
    [('dis', '<b>DIS-</b> not, or the opposite: dislike &middot; disagree &middot; dishonest'),
     ('mis', '<b>MIS-</b> wrongly: misunderstand &middot; misspell &middot; mislead'),
     ('cape', '<b>The False Cape</b> inflammable means flammable')],
]
TARGETS = {'un': (0, 'un', INK['un']), 'im': (1, 'im', INK['im']), 'il': (1, 'il', INK['il']),
           'ir': (1, 'ir', INK['ir']), 'in': (1, 'in', INK['in']), 'dis': (2, 'dis', INK['dis']),
           'mis': (2, 'mis', INK['mis']), 'cape': (2, 'cape', SEA_INK)}

import ex_tr_prefixes as T
L.build(OUT, ART, 'The Prefix Archipelago &mdash; Negative Prefixes', 'negative prefixes', EXTRACTED,
        HERO, 'Learn which island a word belongs to, and its spelling follows.', ('order', 'Read the chart'),
        RULES + PAIRS + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        [PAINT['un'], PAINT['in'], PAINT['dis']], T.T,
        ['Clean run. Every word landed on the right island.',
         'Solid progress. Say the island rules aloud: p and m, l, r, then the rest.',
         'Good first attempt. When in doubt, un- is the mainland.'],
        ('sailing-the-seas-soundings.html', 'Next chart: soundings of frequency'), gull_seed=23, long_name=13)
