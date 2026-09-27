# -*- coding: utf-8 -*-
"""The Writer's Nightmare (B2), rebuilt as a 16:9 panel deck ("house style 2").

`forbes-english-writers-nightmare.html` was a scrolling page, English with
Spanish glosses, written for Spanish speakers. Everything it taught
survives: the story, the ten vocabulary items, the three grammar rules, the
eleven pronunciation words, the eight quiz items and the four discussion
prompts (now the activation stage). The negatives table's Spanish column is
replaced by rule text in each of eleven languages.

**Style 2.** The hero is flat-vector, so it owns a panel at full opacity
rather than sitting washed behind a card. It is the only picture the lesson
has, so each panel takes a different 548×720 slice of it with pos=. More
plates would be better (HOUSE-STYLE §5c); the handoff lists what to brief.

**Content fixed in the rebuild** (learner-facing text never mentions it):
- "Her process is different from other writers" compared a process with
  people. Now "different from that of the other writers she knows".
- "It has the opposite effect" had no referent for "it" in a lesson whose
  Rule A is about the dummy subject. Now "Forcing ideas has...".
- "Almost automatically, without forcing anything." was a fragment in a
  lesson teaching that every sentence needs a subject.
- "overwhelmingly good" did not use the taught word; "the feeling is
  overwhelming" does.
- Pronunciation: "experts" claimed the x is /ks/ "because it follows a short
  vowel" (it is the stress); "growth" put the tongue behind the teeth for
  /θ/; "auto" was taught though the word in the lesson is "automatically";
  IPA mixed British and American vowels. All now British, and the tips are
  written for every learner, not only Spanish speakers.
- Quiz: three keys were the longest option (nightmare, opposites attract,
  and the exhausting item, whose "Two: ex-HAUS-ting" distractor actually
  showed three syllables). Distractors lengthened, never the key shortened.
- Q2 asked which word is "ALWAYS correct" with "to" among the options,
  which is correct in British English; the gap fill now accepts it too.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_writersnightmare as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-writers-nightmare.html'
F = 'WritersNightmare'
HERO = 'writers-block-typewriter.jpg'

E = I.T['en']

# py lesson-template/extract-palette.py WritersNightmare/writers-block-typewriter.jpg
PALETTE = """  --hero: url('%s/%s');

  --void          : #0a0e0a;
  --surface       : #141b14;
  --surface2      : #1d261d;
  --border        : #b7665b;
  --text          : #f5f2f2;
  --text-dim      : #bfa7a3;
  --accent        : #ea998e;
  --accent-bright : #f5b9b1;
  --accent-dim    : #d65746;
  --secondary     : #4f6885;
  --contrast      : #1deda2;""" % (F, HERO)

# Slices of the one picture: ink spill, lever, nameplate, keys, cable.
POS = ['8% 50%', '30% 50%', '58% 50%', '80% 50%', '97% 50%']

STORY = [
    'It is true — writer\'s block is a <strong>nightmare</strong>. Maya stares at the '
    'blank page every morning. She doesn\'t write a single word for days. The cursor '
    'blinks, <strong>consistent</strong> and merciless.',
    'Forcing ideas has the opposite effect: the harder she tries, the less creative she '
    'feels. Some authors say it is <strong>exhausting</strong> to fight the block. '
    '<strong>Experts</strong> say that changes to a writer\'s routine need to be gradual.',
    'Her process is <strong>different from</strong> that of the other writers she knows. '
    'A <strong>fixed</strong> mindset doesn\'t help. Her <strong>choices</strong> matter: '
    'she can take a long walk, read something <strong>different to</strong> her usual '
    'genre, or let her mind wander without it feeling like failure.',
    'The idea comes on a quiet Tuesday. It arrives almost <strong>automatically</strong>, '
    'without any force. Her novel is about two characters who could not be more '
    'different. But, as they say, <strong>opposites attract</strong>. Their '
    '<strong>growth</strong> — painful, slow, real — is the story.',
    'When Maya finally reads the first chapter back, the feeling is '
    '<strong>overwhelming</strong>. It is good. It is really good. The nightmare is over.',
]

VOCAB = [  # (word, part of speech + IPA)
    ('nightmare', 'noun · /ˈnaɪt.meə/'),
    ('consistent', 'adjective · /kənˈsɪs.tənt/'),
    ('exhausting', 'adjective · /ɪɡˈzɔː.stɪŋ/'),
    ('experts', 'noun, plural · /ˈek.spɜːts/'),
    ('fixed', 'adjective · /fɪkst/'),
    ('choices', 'noun, plural · /ˈtʃɔɪ.sɪz/'),
    ('different from / to', 'adjective + preposition'),
    ('automatically', 'adverb · /ˌɔː.təˈmæt.ɪ.kli/'),
    ('opposites attract', 'expression · /ˈɒp.ə.zɪts əˈtrækt/'),
    ('growth', 'noun · /ɡrəʊθ/'),
    ('overwhelming', 'adjective · /ˌəʊ.vəˈwel.mɪŋ/'),
]
# the definition key for each vocabulary card; "different from" is Rule B,
# not a vocabulary item, so it has no card here
VKEY = {'nightmare': 'v1', 'opposites attract': 'v2', 'consistent': 'v3',
        'exhausting': 'v4', 'overwhelming': 'v5', 'fixed': 'v6', 'growth': 'v7',
        'automatically': 'v8', 'choices': 'v9', 'experts': 'v10'}
VSLIDES = [['nightmare', 'consistent', 'exhausting', 'experts'],
           ['fixed', 'choices', 'automatically'],
           ['opposites attract', 'growth', 'overwhelming']]
IPA = dict(VOCAB)

MATCH_A = [
    ('nightmare', 'a very difficult experience'),
    ('consistent', 'always the same'),
    ('exhausting', 'extremely tiring'),
    ('overwhelming', 'too great to manage'),
    ('fixed', 'not able to change'),
]
MATCH_B = [
    ('growth', 'the process of developing'),
    ('automatically', 'without thinking'),
    ('choices', 'decisions between options'),
    ('experts', 'people with deep knowledge'),
    ('opposites attract', 'different people are drawn together'),
]

PRON = [  # (word, stress pattern, IPA, key)
    [('nightmare', 'NIGHT-mare', '/ˈnaɪt.meə/', 'p1'),
     ('exhausting', 'ex-HAUST-ing', '/ɪɡˈzɔː.stɪŋ/', 'p2'),
     ('experts', 'EX-perts', '/ˈek.spɜːts/', 'p3'),
     ('overwhelmed', 'o-ver-WHELMED', '/ˌəʊ.vəˈwelmd/', 'p4')],
    [('automatically', 'au-to-MAT-ic-ally', '/ˌɔː.təˈmæt.ɪ.kli/', 'p5'),
     ('consistent', 'con-SIS-tent', '/kənˈsɪs.tənt/', 'p6'),
     ('it is true', 'it-iz-TRUE', '/ɪt ɪz truː/', 'p7'),
     ('changes', 'CHANGE-es', '/ˈtʃeɪn.dʒɪz/', 'p8')],
    [('growth', 'GROWTH', '/ɡrəʊθ/', 'p9'),
     ('fixed', 'FIXED', '/fɪkst/', 'p10'),
     ('choices', 'CHOI-ces', '/ˈtʃɔɪ.sɪz/', 'p11')],
]

# (stem, options, correct, why, ctx_key, stem_key)
MC = [
    ('Which sentence is correct English?',
     ["Doesn't help to force the ideas.", "She doesn't helps with the block.",
      "It doesn't help to force ideas.", 'It not helps to force the ideas.'],
     2, 'q1w', None, 'q1s'),
    ("Her approach is very different ____ her co-author's.",
     ['of', 'to', 'from', 'at'], 2, 'q2w', 'q2c', None),
    ('Meeting that deadline was a nightmare.',
     ['a frightening dream that you have at night', 'a very hard, unpleasant experience',
      'a creative block that stops you writing', 'a job that you do without thinking about it'],
     1, 'q3w', 'q3c', None),
    ('exhausting',
     ['two: ex-HAUSTING', 'three: ex-HAUST-ing', 'three: EX-haust-ing', 'four: ex-HAU-sti-ing'],
     1, 'q4w', 'q4c', None),
    ('The changes happen automatically.',
     ['The changes not happen automatically.', "The changes doesn't happen automatically.",
      "The changes don't happen automatically.", "The changes aren't happen automatically."],
     2, 'q5w', 'q5c', None),
    ('When do people say "opposites attract"?',
     ['when two people have exactly the same interests',
      'when a writer cannot find even one new idea to use',
      'when very different people are drawn together',
      'when inspiration comes without any effort at all'],
     2, 'q6w', None, 'q6s'),
    ('Which word ends in /θ/, the sound in "think"?',
     ['choices', 'changes', 'growth', 'fixed'], 2, 'q7w', None, 'q7s'),
    ("She doesn't write when she's overwhelmed.",
     ['Present Simple negative', 'Present Perfect negative', 'Past Simple negative',
      'Future Simple negative'],
     0, 'q8w', 'q8c', None),
]

GAP = [
    [('______ is exhausting to fight the block.', ['It'], 'ga1'),
     ("Maya stares at the page. ______ doesn't write a word.", ['She'], 'ga2')],
    [("She ______ write when she's overwhelmed.", ["doesn't|does not"], 'gb1'),
     ('Experts ______ always agree on the best solution.', ["don't|do not"], 'gb2')],
    [('A fixed mindset ______ ______ creativity. (help)', ["doesn't|does not", 'help'], 'gc1'),
     ('Her writing is very different ______ mine.', ['from|to'], 'gc2')],
]


def divider(n, pos=None):
    return D.divider('d%dt' % n, E['d%dt' % n], 'd%dn' % n, E['d%dn' % n],
                     folder=F, pic=HERO, pos=pos)


def story(n, side, pos):
    paras = [(None, STORY[n - 1])]
    if n == 1:
        paras.append(('storyNote', E['storyNote'], 'dim'))
    return D.panel('e1', E['e1'], 'st%d' % n, E['st%d' % n], paras,
                   folder=F, pic=HERO, side=side, pos=pos)


def rule(r, side, pos):
    return D.panel('e3', E['e3'], 'g%st' % r, E['g%st' % r],
                   [('g%sa' % r, E['g%sa' % r]), ('g%sb' % r, E['g%sb' % r], 'dim')],
                   folder=F, pic=HERO, side=side, pos=pos)


def cards(eb, tkey, items, cols=None):
    """items: (head, body_key, note)."""
    return D.teach(eb, E[eb], tkey, E[tkey],
                   [(None, h, k, E[k], None, n) for h, k, n in items], cols=cols)


def vocab_slide(n, words):
    return cards('e2', 'vt%d' % n,
                 [(w, VKEY[w], IPA[w]) for w in words],
                 cols='1fr 1fr' if len(words) == 4 else None)


def pron_slide(n, words):
    return cards('e4', 'pt%d' % n,
                 [('%s · <span style="font-weight:400">%s</span>' % (w, s), k, ipa)
                  for w, s, ipa, k in words],
                 cols='1fr 1fr' if len(words) == 4 else None)


def build():
    logo = D.logo_from(TPL)
    D.assert_no_key_is_longest([dict(options=o, correct=c) for _, o, c, *_ in MC])

    slides = "".join([
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])]),

        divider(1),
        story(1, 'left', POS[0]),
        story(2, 'right', POS[2]),
        story(3, 'left', POS[1]),
        story(4, 'right', POS[3]),
        story(5, 'left', POS[4]),

        divider(2, '58% 50%'),
    ] + [vocab_slide(i + 1, w) for i, w in enumerate(VSLIDES)] + [
        D.match(MATCH_A, 'e2', E['e2'], 'mt', E['mt'], 'matchHint', E['matchHint'],
                'matchWhy'),
        D.match(MATCH_B, 'e2', E['e2'], 'mt', E['mt'], 'matchHint', E['matchHint'],
                'matchWhy'),

        divider(3, '30% 50%'),
        rule('A', 'left', POS[0]),
        cards('e3', 'gAct', [
            ('✓ SHE writes every morning.', 'ca1', '✗ Writes every morning.'),
            ('✓ IT is exhausting to fight the block.', 'ca2',
             '✗ Is exhausting to fight the block.'),
            ("✓ IT doesn't help to force ideas.", 'ca3', "✗ Doesn't help to force ideas."),
        ]),
        rule('B', 'right', POS[3]),
        cards('e3', 'gBct', [
            ('DIFFERENT FROM', 'cb1', '"Her style is different from mine."'),
            ('DIFFERENT TO', 'cb2', '"This chapter is different to the last."'),
            ('DIFFERENT THAN', 'cb3', '"It\'s different than I expected."'),
        ]),
        rule('C', 'left', POS[2]),
        cards('e3', 'gCct', [
            ("She DOESN'T write when she's overwhelmed.", 'cc1', None),
            ("Experts DON'T always agree.", 'cc2', None),
            ("The changes DON'T happen automatically.", 'cc3', None),
            ("It DOESN'T help to force new ideas.", 'cc4', None),
        ], cols='1fr 1fr'),
    ] + [
        D.gap(i + 1, len(GAP), rows, None, 'e3', E['e3'],
              'gt%d' % (i + 1), E['gt%d' % (i + 1)],
              hint=E['gapHint'], hint_key='gapHint', width=150)
        for i, rows in enumerate(GAP)
    ] + [
        divider(4, '80% 50%'),
    ] + [pron_slide(i + 1, w) for i, w in enumerate(PRON)] + [
        divider(5, '8% 50%'),
    ] + [
        D.mc(i + 1, len(MC), dict(stem=stem, options=opts, correct=c, why=w),
             'e5', E['e5'], 'qt', E['qt'],
             ctx=E[ck] if ck else None, ctx_key=ck, stem_key=sk)
        for i, (stem, opts, c, w, ck, sk) in enumerate(MC)
    ] + [
        D.results(),
        D.activate(E['actTitle'], E['actUse'],
                   ['nightmare', 'exhausting', 'overwhelming', 'different from',
                    "doesn't + verb", 'opposites attract'],
                   'Speaking', E['actSpeakBrief'],
                   [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                   E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder'],
                   folder=F, bg=HERO),
    ])

    langs = tuple(c for c in I.LANGS if c in I.T)
    D.assemble(TPL, OUT, slides, PALETTE, "The Writer's Nightmare — B2", I, langs=langs)
    print('wrote %s — %d slides, %s' % (OUT, slides.count('<section class="slide'),
                                        ','.join(langs)))


if __name__ == '__main__':
    build()
