# -*- coding: utf-8 -*-
"""Are You a Boltzmann Brain? (C1) — a new 16:9 panel deck ("house style 2").

Innes, 2026-10-15: *"make a class on this"*, with the narration of a short
animated science explainer on the Boltzmann brain paradox pasted in chat
(not in the repo). The script is copyrighted, so no slide reproduces it:
the four reading panels retell it in new words, and the language points are
the ones the script itself leans on.

  1 The paradox        — the story; idioms it uses (keep somebody up at
                         night, claim to fame, put forward, take for granted,
                         over and done with, something is amiss); MC ×3
  2 Entropy            — entropy, a closed system, tend towards, pristine,
                         ephemeral, spontaneously; match (fluctuation, blip,
                         namesake, precede, decay); MC ×2
  3 The odds           — comparing likelihood (vastly more likely than, by
                         far the most likely, not impossible just so unlikely
                         that) and talking about the odds (the odds are, a
                         slim chance, a near certainty); sort, gap ×2 (bank),
                         order, MC
  4 What came before?  — speculative modals, past (MUST / MIGHT / CAN'T
                         HAVE + past participle) and present (MUST / MIGHT /
                         CAN'T BE); gap ×2, order with a decoy, MC ×2
then results and the activation stage. 35 slides, EN/DE/ES.

Facts the panels rest on: Ludwig Boltzmann (1844–1906) gave entropy its
statistical interpretation; the brains themselves were introduced by later
cosmologists (the term dates from the early 2000s); the Big Bang is the
standard resolution, and the question is open again because nobody knows
what preceded it.

**Art — Innes, 2026-10-16: "files in".** Thirteen Midjourney renders, all
used, in `boltzmann/` (briefed in chat with --sref to the live Harari
plate). No plate-odds was rendered; Part 3's reading is about universes
forming by chance, so the two galaxy-swirl variants from the plate-before
batch are `plate-odds` / `-2`, and the two bursts stay with Part 4. Each part
rotates its own pool slide by slide (the Manifestation rule: no two
neighbouring slides share a picture). The divider takes the plate whose
subject reads whole; the panel the one whose subject survives a column crop.
Results get the empty chairs, the activation the man at the table.

MC keys are checked against the longest-option rule at build time; the
word banks are checked against gap order. The second order slide carries a
decoy ("must had") that is wrong in every position.

Run from the repo root:  py lesson-template/build/build_boltzmann.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_boltzmann as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-boltzmann-brain-c1.html'
F = 'boltzmann'
TITLE = 'Are You a Boltzmann Brain? (C1) | Forbes English'

HERO = 'plate-cover.jpg'
# part: (divider, panel, [rotation for cards and questions])
ART = {1: ('plate-paradox-4', 'plate-paradox', ['plate-paradox-2', 'plate-paradox-3']),
       2: ('plate-entropy-2', 'plate-entropy', ['plate-entropy-2', 'plate-entropy']),
       3: ('plate-odds', 'plate-odds-2', ['plate-odds', 'plate-odds-2']),
       4: ('plate-before', 'plate-before-2', ['plate-before', 'plate-before-2'])}
RESULTS, ACT = 'plate-results.jpg', 'plate-act.jpg'
for _d, _p, _pool in ART.values():
    for _f in [_d, _p] + _pool:
        assert os.path.exists(os.path.join(F, _f + '.jpg')), _f
_turn = {1: 0, 2: 0, 3: 0, 4: 0}


def qbg(part):
    """The next picture in this part's rotation."""
    pool = ART[part][2]
    f = pool[_turn[part] % len(pool)]
    _turn[part] += 1
    return f + '.jpg'


E = I.T['en']

# py lesson-template/extract-palette.py boltzmann/plate-cover.jpg
# (2026-10-16, dark, every row PASS)
PALETTE = """  --hero: url('%s/%s');

  --void          : #090e0e;
  --surface       : #121c1b;
  --surface2      : #1a2927;
  --border        : #ad4942;
  --text          : #f5f2f2;
  --text-dim      : #bfa5a3;
  --accent        : #ea746b;
  --accent-bright : #f6aca7;
  --accent-dim    : #d43225;
  --secondary     : #101b1a;
  --contrast      : #1ded98;
  /* The cover brain is the accent's own coral, so the mark vanished into
     it in --accent. HOUSE-STYLE §2: --text is the safe fallback. */
  --logo-mark     : var(--text);""" % (F, HERO)

# ── reading panels: English in every language (the reading IS the material)
READ = {
    1: ['How do you know that you have really lived your life? You might be a brain '
        'that formed <strong>a moment ago</strong> out of drifting particles, complete '
        'with false memories, imagining a world that is not there. It sounds absurd, but '
        'the idea has <strong>kept cosmologists up at night</strong> for generations. '
        'They call it the <strong>Boltzmann brain paradox</strong>.',
        'Ludwig Boltzmann (1844–1906) never imagined the brains himself. His '
        '<strong>claim to fame</strong> was a new way of understanding entropy. Later '
        'cosmologists <strong>put forward</strong> the brains, building on his work.'],
    2: ['<strong>Entropy</strong> measures how disordered a system is. A glass on a '
        'table is ordered; the same glass in pieces on the floor is disordered. The '
        'second law of thermodynamics says that a <strong>closed system tends '
        'towards</strong> disorder: the pieces will never jump back into a '
        '<strong>pristine</strong> glass.',
        'Boltzmann’s insight was statistical. Disorder wins because there are vastly '
        'more ways to be messy than to be neat. A glass mending itself is not '
        'impossible, just so unlikely that nobody will ever see it.'],
    3: ['Now give the universe infinite time. Sooner or later, random particles will '
        'form anything: a statue made of pasta, a single brain full of false memories, '
        'even a whole new universe. Which is <strong>more likely</strong>? The brain, '
        '<strong>by far</strong>. Next to a universe it is a blip, so for every universe '
        'that forms by chance, <strong>vastly more</strong> lonely brains do.',
        'So if time is infinite, <strong>the odds are</strong> that you are one of those '
        'brains. The way out was the Big Bang: the universe has not existed forever.'],
    4: ['The evidence for the Big Bang is everywhere we look, so it <strong>must have '
        'happened</strong>. But nobody knows what came before it. Something <strong>might '
        'have caused</strong> it. Our universe <strong>could be</strong> one turn of an '
        'endless cycle, or one bubble in a multiverse.',
        'Some cosmologists say today’s models still predict more Boltzmann brains than '
        'real ones, so something in them <strong>must be</strong> wrong. Others say such '
        'brains <strong>can’t</strong> actually form. Unless, of course, you are the one '
        'who is wrong.'],
}

# (headword, body key, example) — the headword and the example stay in English
CARDS = {
    1: [('keep somebody up at night', 'c1',
         '“The paradox has kept cosmologists up at night for decades.”'),
        ('somebody’s claim to fame', 'c2',
         '“Boltzmann’s claim to fame was a new theory of entropy.”'),
        ('put forward (an idea)', 'c3',
         '“He put forward a statistical explanation of disorder.”')],
    2: [('take something for granted', 'c4',
         '“Today most of us take the Big Bang for granted.”'),
        ('over and done with', 'c5',
         '“I thought the problem was over and done with. It wasn’t.”'),
        ('something is amiss', 'c6',
         '“If a model predicts more fake brains than real ones, something is amiss.”')],
    3: [('entropy', 'c7', '“The entropy of my desk rises every week.”'),
        ('a closed system', 'c8', '“The universe as a whole may be a closed system.”'),
        ('tend towards', 'c9', '“Closed systems tend towards disorder.”')],
    4: [('pristine', 'c10', '“The glass was pristine a second before it fell.”'),
        ('ephemeral', 'c11',
         '“A Boltzmann brain is ephemeral: it thinks one thought and decays.”'),
        ('spontaneously', 'c12',
         '“Could a universe burst into existence spontaneously?”')],
    5: [('VASTLY / FAR / MUCH more likely than', 'c13',
         '“A brain is vastly more likely than a universe.”'),
        ('BY FAR the most likely', 'c14', '“The brain is by far the most likely outcome.”'),
        ('NOT IMPOSSIBLE, JUST SO unlikely THAT…', 'c15',
         '“It isn’t impossible, just so unlikely that nobody will ever see it.”')],
    6: [('THE ODDS ARE (THAT)…', 'c16',
         '“The odds are that you are a perfectly ordinary person.”'),
        ('THERE’S A SLIM CHANCE (THAT)…', 'c17',
         '“There’s a slim chance that the theory is wrong.”'),
        ('IT’S A NEAR CERTAINTY (THAT)…', 'c18',
         '“It’s a near certainty that the Big Bang happened.”')],
    7: [('MUST HAVE + past participle', 'c19',
         '“The Big Bang must have happened: the evidence is everywhere.”'),
        ('MIGHT / COULD HAVE + past participle', 'c20',
         '“Something might have caused it.”'),
        ('CAN’T HAVE + past participle', 'c21',
         '“Boltzmann can’t have used the term: it came later.”')],
    8: [('MUST BE', 'c22',
         '“If a model predicts more fake brains than real ones, it must be wrong.”'),
        ('MIGHT / COULD BE', 'c23', '“We might be in one of many universes.”'),
        ('CAN’T BE', 'c24', '“That can’t be right: the numbers don’t add up.”')],
}
CARD_PART = {1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}

# (ctx key, stem key or None, stem, options, correct, why key, part). A stem
# with a blank stays in English (HOUSE-STYLE §8), so it has no key.
MC = [
    ('x1', 's1', None,
     ['The deadline is keeping her up at night.',
      'The deadline is putting her forward at night.',
      'The deadline has become her claim to fame.',
      'She takes the deadline for granted every night.'], 0, 'q1w', 1),
    ('x2', 's2', None,
     ['later cosmologists, building on his work',
      'Boltzmann himself, in the nineteenth century',
      'the scientists who found the Big Bang',
      'a physicist who argued with Boltzmann in Vienna'], 0, 'q2w', 1),
    ('x3', 's3', None,
     ['“Great, it’s over and done with.”', '“Great, it’s taken for granted.”',
      '“Great, there’s something amiss.”', '“Great, it’s keeping us up at night.”'],
     0, 'q3w', 1),
    ('x4', 's4', None,
     ['Sand on a beach tends towards disorder.',
      'Sand on a beach tends towards a pristine order.',
      'The sandcastle is a closed system that cannot decay.',
      'The tide spontaneously makes the sand more ordered.'], 0, 'q4w', 2),
    ('x5', None, 'The display was beautiful but ______: gone in two seconds.',
     ['ephemeral', 'pristine', 'spontaneous', 'disordered'], 0, 'q5w', 2),
    ('x6', 's6', None,
     ['“There’s a slim chance of rain.”', '“The odds are that it will rain.”',
      '“Rain is by far the most likely.”', '“It’s a near certainty it’ll rain.”'],
     0, 'q6w', 3),
    ('x7', None, 'My flatmate ______ them.',
     ['must have moved', 'can’t have moved', 'must have to move', 'should had moved'],
     0, 'q7w', 4),
    ('x8', None, 'Boltzmann ______ the term himself.',
     ['can’t have used', 'must have used', 'might have used', 'mustn’t have used'],
     0, 'q8w', 4),
]
# Keys are written first above for readability and dealt across the letters
# here: the engine shuffles at runtime, but KEYS reads the source order.
SLOT = [2, 0, 3, 1, 2, 3, 1, 0]
assert len(SLOT) == len(MC)
for _i, (_x, _s, _t, _o, _c, _w, _p) in enumerate(MC):
    _o = list(_o)
    _o.insert(SLOT[_i], _o.pop(_c))
    MC[_i] = (_x, _s, _t, _o, SLOT[_i], _w, _p)
MC_TOTAL = len(MC)

# rows: (sentence, [answer], why key); bank must not be in gap order
GAP1 = [('A single brain is ______ more likely than a whole universe.',
         ['vastly|far|much'], 'gw1'),
        ('Of the three, the brain is by ______ the most likely.', ['far'], 'gw2'),
        ('The ______ are that you are a perfectly real person.', ['odds'], 'gw3')]
BANK1 = ['far', 'odds', 'vastly']
GAP2 = [('There’s a ______ chance that the model is right after all.', ['slim'], 'gw4'),
        ('It’s a ______ certainty that the universe is expanding.', ['near'], 'gw5'),
        ('It isn’t impossible, ______ so unlikely that we’ll never see it.',
         ['just'], 'gw6')]
BANK2 = ['near', 'just', 'slim']
CANT = 'can’t|cannot|couldn’t|could not'
GAP3 = [('The evidence is everywhere: the Big Bang ______ have happened.',
         ['must'], 'gw7'),
        ('Boltzmann died in 1906, so he ______ have heard the term “Boltzmann brain”.',
         [CANT], 'gw8'),
        ('Nobody knows for sure. Something ______ have caused it, or nothing did.',
         ['might|could|may'], 'gw9')]
GAP4 = [('If a model predicts more fake brains than real ones, it ______ be wrong.',
         ['must'], 'gw10'),
        ('Our universe ______ be one of many in a multiverse. Nobody knows yet.',
         ['might|could|may'], 'gw11'),
        ('A pasta statue ______ form by chance in one afternoon: the odds are far too low.',
         [CANT], 'gw12')]

ORDER1 = ['A glass mending itself', 'isn’t impossible,', 'just', 'so unlikely',
          'that nobody will ever see it']
ORDER2 = ['Something', 'must have', 'caused', 'the Big Bang']
ORDER2_DECOY = ['must had']

MATCH = [
    ('a fluctuation', 'a small, random change up or down'),
    ('a blip', 'something brief and unimportant on a large scale'),
    ('a namesake', 'a person or thing named after someone'),
    ('precede', 'come before something in time'),
    ('decay', 'break down slowly and disappear'),
]

SORT_BINS = ['Probably true', 'Probably not true']
SORT_ITEMS = [
    ('“The odds are that it will rain.”', 0),
    ('“There’s a slim chance that it will rain.”', 1),
    ('“It’s a near certainty that it will rain.”', 0),
    ('“Rain isn’t impossible, just very unlikely.”', 1),
    ('“Rain is by far the most likely outcome.”', 0),
    ('“Rain is far less likely than sun.”', 1),
    ('“Rain is slightly more likely than not.”', 0),
    ('“I wouldn’t bet on rain.”', 1),
]


def divider(n, pic, pos=None):
    return D.divider('d%dt' % n, E['d%dt' % n], 'd%dn' % n, E['d%dn' % n],
                     folder=F, pic=pic, pos=pos)


def panel(n, side, pos):
    a, b = READ[n]
    return D.panel('e%d' % n, E['e%d' % n], 'p%dt' % n, E['p%dt' % n],
                   [(None, a), (None, b, 'dim')],
                   folder=F, pic=ART[n][1] + '.jpg', side=side, pos=pos)


def cards(n):
    part, tk = CARD_PART[n], 'vt%d' % n
    return D.teach('e%d' % part, E['e%d' % part], tk, E[tk],
                   [(None, w, k, E[k], None, ex) for w, k, ex in CARDS[n]],
                   cols='1fr 1fr 1fr', folder=F, bg=qbg(part))


_mc_n = [0]


def mc(i):
    xk, sk, stem, opts, c, why, part = MC[i]
    return D.mc(i + 1, MC_TOTAL, dict(stem=E[sk] if sk else stem, options=opts,
                                      correct=c, why=why),
                'e%d' % part, E['e%d' % part], 'mt%d' % part, E['mt%d' % part],
                ctx=E[xk], ctx_key=xk, stem_key=sk, folder=F, bg=qbg(part))


def gap(i, rows, bank, part, tk, hk):
    return D.gap(i, 4, rows, bank, 'e%d' % part, E['e%d' % part],
                 tk, E[tk], hint=E[hk], hint_key=hk, size=20,
                 folder=F, bg=qbg(part))


def build():
    logo = D.logo_from(TPL)
    D.assert_no_key_is_longest([dict(options=m[3], correct=m[4]) for m in MC])
    D.assert_bank_is_not_a_key(BANK1, [r[1][0] for r in GAP1])
    D.assert_bank_is_not_a_key(BANK2, [r[1][0] for r in GAP2])

    slides = "".join([
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])]),

        divider(1, ART[1][0] + '.jpg'),
        panel(1, 'left', '80% 50%'),
        cards(1), cards(2),
        mc(0), mc(1), mc(2),

        divider(2, ART[2][0] + '.jpg'),
        panel(2, 'right', '58% 50%'),
        cards(3), cards(4),
        D.match(MATCH, 'e2', E['e2'], 'mtt', E['mtt'], 'matchHint', E['matchHint'],
                'matchWhy', folder=F, bg=qbg(2)),
        mc(3), mc(4),

        divider(3, ART[3][0] + '.jpg'),
        panel(3, 'left', '40% 50%'),
        cards(5), cards(6),
        D.sort_slide(SORT_BINS, SORT_ITEMS, 'e3', E['e3'], 'st', E['st'], 'sh', E['sh'],
                     'sw', bin_keys=['sb1', 'sb2'], folder=F, bg=qbg(3)),
        gap(1, GAP1, BANK1, 3, 'gt1', 'gh1'), gap(2, GAP2, BANK2, 3, 'gt1', 'gh1'),
        D.order(ORDER1, 'e3', E['e3'], 'ot1', E['ot1'], 'oh1', E['oh1'], 'ow1',
                folder=F, bg=qbg(3)),
        mc(5),

        divider(4, ART[4][0] + '.jpg'),
        panel(4, 'right', '70% 50%'),
        cards(7), cards(8),
        gap(3, GAP3, None, 4, 'gt2', 'gh2'), gap(4, GAP4, None, 4, 'gt2', 'gh2'),
        D.order(ORDER2, 'e4', E['e4'], 'ot1', E['ot1'], 'oh2', E['oh2'], 'ow2',
                decoys=ORDER2_DECOY, folder=F, bg=qbg(4)),
        mc(6), mc(7),

        D.results(folder=F, bg=RESULTS),
        # Not in teaching order: the BANK gate reads activation chips as a
        # word bank, and teaching order is the gap order.
        D.activate(E['actTitle'], E['actUse'],
                   ['must have', 'The odds are that', 'something is amiss',
                    'vastly more likely than', 'can’t have', 'There’s a slim chance that',
                    'take it for granted', 'not impossible, just so unlikely that',
                    'might have', 'by far the most likely'],
                   'Speaking', E['actSpeakBrief'],
                   [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                   E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder'],
                   folder=F, bg=ACT),
    ])

    n = slides.count('<section class="slide')
    assert ('%d slides' % n) == E['chipCount'], (n, E['chipCount'])
    langs = tuple(c for c in I.LANGS if c in I.T)
    D.assemble(TPL, OUT, slides, PALETTE, TITLE, I, langs=langs)
    print('wrote %s — %d slides, %s' % (OUT, n, ','.join(langs)))


if __name__ == '__main__':
    build()
