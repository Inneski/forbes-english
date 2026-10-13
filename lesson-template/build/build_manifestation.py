# -*- coding: utf-8 -*-
"""Manifestation: Can You Think It Into Being? (B2) — a new 16:9 panel deck
("house style 2").

Innes, 2026-10-13: *"make forbes lesson on manifestation - give me artwork
shopping list"*. The topic is the trend (vision boards, affirmations, the
law of attraction, "lucky girl syndrome"); the language is the English of
reporting a claim without endorsing it, which is what a learner needs to
talk about a trend like this at all:

  1 The trend         — vocabulary cards ×2, MC ×2, match
  2 The claims        — passive reporting (It is said that / X is said to /
                        X is said to have done), distancing adverbs; gap ×2,
                        order ×2 (the second with a decoy), MC ×2
  3 The evidence      — hedging (there is little evidence that, it would
                        seem, tends to), confirmation bias, placebo,
                        correlation; sort (fact / distance), MC ×3
  4 Your view         — the balanced view (there's something to be said
                        for, where it falls down is, I'd stop short of);
                        cards, gap ×2, MC ×2
then results and the activation stage. 35 slides, EN/DE/ES.

Facts the panels rest on, all reported with the lesson's own hedges: The
Secret (Rhonda Byrne, 2006); Cambridge Dictionary's Word of the Year 2024
was "manifest"; Gabriele Oettingen's research on positive fantasies and
her WOOP method (Rethinking Positive Thinking, 2014).

**Style 2.** Art: six slot plates briefed in docs/ARTWORK-manifestation.md.
Until all six exist in `manifestation/` this writes the gitignored preview
`_forbes-manifestation-b2.html` on stand-ins copied from the Alan Watts
plates (the style reference for the set) to `manifestation/_ph-*.jpg`,
also gitignored; the live page is not written at all. The palette below is
the stand-in's and is replaced from plate-cover once it lands.

MC keys are checked against the longest-option rule at build time; the two
word banks are checked against gap order. Order slide 2 carries a decoy
("that help") that is wrong in every position.
"""
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_manifestation as I

TPL = 'lesson-template/lesson-template.html'
LIVE = 'forbes-manifestation-b2.html'
PREVIEW = '_forbes-manifestation-b2.html'   # gitignored (leading underscore)
F = 'manifestation'

SLOTS = ('plate-cover', 'plate-trend', 'plate-claims', 'plate-evidence',
         'plate-view', 'plate-act')
# Stand-ins from the style reference, so the preview looks like the family
# it is joining rather than like grey boxes.
STAND_IN = {'plate-cover': 'hero.jpg', 'plate-trend': 'plate-h.jpg',
            'plate-claims': 'plate-e.jpg', 'plate-evidence': 'plate-f.jpg',
            'plate-view': 'plate-i.jpg', 'plate-act': 'plate-g.jpg'}
READY = all(os.path.exists(os.path.join(F, s + '.jpg')) for s in SLOTS)
OUT = LIVE if READY else PREVIEW

# The drop folder the brief names. Innes, 2026-09-30: "make sure the folder
# exists or you tell me to make it in future, hard wire that".
DROP = os.path.join('incoming', 'manifestation')
if not READY:
    os.makedirs(DROP, exist_ok=True)
    os.makedirs(F, exist_ok=True)
    for s in SLOTS:
        dst = os.path.join(F, '_ph-%s.jpg' % s)
        if not os.path.exists(dst):
            shutil.copyfile(os.path.join('alan-watts', STAND_IN[s]), dst)
PIC = {s: (s + '.jpg') if READY else ('_ph-%s.jpg' % s) for s in SLOTS}
HERO, TREND, CLAIMS, EVIDENCE, VIEW, ACT = (PIC[s] for s in SLOTS)

E = I.T['en']

# The live page must not ship on the stand-in's colours. Once plate-cover is
# in, run the command below and paste its ten tokens here as a string in the
# same form as PALETTE; until then a READY build stops and says so (the
# possessive-adjectives precedent).
# py lesson-template/extract-palette.py manifestation/plate-cover.jpg --light
# (2026-10-13, the dandelion; every row PASS)
PALETTE_LIVE = """  --hero: url('%s/%s');

  --void          : #d8c3ac;
  --surface       : #e1d3c4;
  --surface2      : #dccbb8;
  --border        : #966a4a;
  --text          : #2a1b11;
  --text-dim      : #5e422e;
  --accent        : #8f3d00;
  --accent-bright : #723204;
  --accent-dim    : #ee751c;
  --secondary     : #93b3b1;
  --contrast      : #075550;""" % (F, HERO)
if READY and PALETTE_LIVE is None:
    sys.exit('plates are in: run\n  py lesson-template/extract-palette.py '
             '%s/plate-cover.jpg --light\nand paste it into PALETTE_LIVE in %s'
             % (F, os.path.basename(__file__)))

# STAND-IN: py lesson-template/extract-palette.py alan-watts/plate-a.jpg --light
# (2026-10-13, every row PASS). Re-derive from manifestation/plate-cover.jpg
# when it lands, and paste over this block.
PALETTE = """  --hero: url('%s/%s');

  --void          : #d8bdac;
  --surface       : #e1cfc4;
  --surface2      : #dcc5b8;
  --border        : #96674a;
  --text          : #2a1a11;
  --text-dim      : #5e402e;
  --accent        : #9b3b00;
  --accent-bright : #682700;
  --accent-dim    : #ef7227;
  --secondary     : #a0b5b3;
  --contrast      : #07554d;""" % (F, HERO)
if PALETTE_LIVE:
    PALETTE = PALETTE_LIVE

# (headword, body key, example) — the headword and the example stay in English
CARDS = {
    1: [('manifest (verb)', 'c1', '“She says she manifested her new flat.”'),
        ('a vision board', 'c2',
         '“Her vision board has a beach house, a dog and a promotion on it.”'),
        ('an affirmation', 'c3',
         '“Every morning he repeats the affirmation ‘I am calm and confident.’”')],
    2: [('wishful thinking', 'c4',
         '“Expecting a pay rise without asking for one is wishful thinking.”'),
        ('the law of attraction', 'c5',
         '“According to the law of attraction, worrying about debt brings more debt.”'),
        ('a self-fulfilling prophecy', 'c6',
         '“Expecting to fail the interview became a self-fulfilling prophecy.”')],
    3: [('It is said that + clause', 'c7',
         '“It is said that writing a goal down makes you more likely to reach it.”'),
        ('X is said to + infinitive', 'c8',
         '“Manifesting is said to work best if you feel grateful in advance.”'),
        ('X is said to have + past participle', 'c9',
         '“The Secret is said to have sold over thirty million copies.”')],
    4: [('supposedly', 'c10',
         '“Supposedly, a glass of water can be ‘charged’ with your intentions.”'),
        ('apparently', 'c11', '“Apparently, half her office has a vision board now.”'),
        ('allegedly', 'c12',
         '“The coach allegedly charged £5,000 for a weekend retreat that never happened.”')],
    5: [('There is little evidence that', 'c13',
         '“There is little evidence that thoughts alone change events.”'),
        ('It would seem that', 'c14',
         '“It would seem that the planning, not the wishing, makes the difference.”'),
        ('tends to', 'c15', '“Fantasising about success tends to reduce effort.”')],
    6: [('confirmation bias', 'c16',
         '“She remembers the parking space she manifested, not the ten she didn’t.”'),
        ('the placebo effect', 'c17', '“Part of the calm may be the placebo effect.”'),
        ('correlation is not causation', 'c18',
         '“Successful people keep journals, but correlation is not causation.”')],
    7: [('There’s something to be said for', 'c19',
         '“There’s something to be said for writing your goals down.”'),
        ('Where it falls down is', 'c20',
         '“Where it falls down is the idea that wanting is enough.”'),
        ('I’d stop short of saying', 'c21',
         '“I’d stop short of saying it’s a scam, but it is oversold.”')],
}
CARD_TITLE = {n: 'vt%d' % n for n in CARDS}
CARD_PART = {1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4}

# (ctx key, stem key or None, stem, options, correct, why key). A stem with
# a blank stays in English (HOUSE-STYLE §8), so it has no key.
MC = [
    ('x1', 's1', None,
     ['an affirmation', 'a vision board', 'a prophecy', 'a manifesto'], 0, 'q1w'),
    ('x2', 's2', None,
     ['a self-fulfilling prophecy', 'a case of wishful thinking',
      'the law of attraction at work', 'a negative affirmation'], 0, 'q2w'),
    ('x3', 's3', None,
     ['Manifesting is claimed to reduce stress in under a week.',
      'Manifesting reduces stress in under a week, as we all know.',
      'Manifesting is claiming to reduce stress in under a week.',
      'Manifesting has reduced stress in under a week for everyone.'], 0, 'q3w'),
    ('x4', None, 'Lucky girl syndrome is believed ______ on TikTok in late 2022.',
     ['to have started', 'that it has started', 'to be starting off',
      'having been started'], 0, 'q4w'),
    ('x5', 's5', None,
     ['It would seem that fantasising about success can reduce effort.',
      'This proves that positive thinking always makes people lazier.',
      'Apparently, fantasising about success is the secret to a great week.',
      'Fantasising about success definitely ruins your energy for the week.'], 0, 'q5w'),
    ('x6', 's6', None,
     ['“Congratulations! Though it would seem the forty applications helped too.”',
      '“That’s nonsense. Manifesting has been proved not to work, not even once.”',
      '“Amazing! So the universe really gave you the job because you wrote it down.”',
      '“Allegedly you got the job, but I don’t really believe in journals.”'], 0, 'q6w'),
    ('x7', 's7', None,
     ['confirmation bias', 'the placebo effect', 'a self-fulfilling prophecy',
      'the law of attraction'], 0, 'q7w'),
    ('x8', 's8', None,
     ['“There’s something to be said for it, but where it falls down is the money.”',
      '“It’s completely true, and anyone who disagrees just hasn’t tried it properly.”',
      '“It’s a total scam, and I’d stop short of saying anything good about it at all.”',
      '“Supposedly it works, so I suppose it must work for most people, more or less.”'],
     0, 'q8w'),
    ('x9', 's9', None,
     ['The course is claimed to bring money in thirty days.',
      'The course brings money in thirty days, the coach knows.',
      'The course is claiming to bring you money in thirty days.',
      'The course was proved to have brought money in thirty days.'], 0, 'q9w'),
]
MC_PART = [1, 1, 2, 2, 3, 3, 3, 4, 4]
assert len(MC) == len(MC_PART)
# Keys are written first above for readability and dealt across the letters
# here: the engine shuffles at runtime, but KEYS reads the source order.
SLOT = [1, 2, 0, 3, 2, 1, 3, 0, 2]
for _i, (_x, _s, _t, _o, _c, _w) in enumerate(MC):
    _o = list(_o)
    _o.insert(SLOT[_i], _o.pop(_c))
    MC[_i] = (_x, _s, _t, _o, SLOT[_i], _w)

# rows: (sentence, [answer], why key); bank must not be in gap order
GAP1 = [
    ('Manifesting is said ______ work best last thing at night.', ['to'], 'gw1'),
    ('The Secret is thought to ______ sold over thirty million copies.', ['have'], 'gw2'),
    ('It ______ claimed that gratitude attracts money.', ['is'], 'gw3'),
    ('The book is reported to have ______ translated into fifty languages.',
     ['been'], 'gw4'),
]
BANK1 = ['been', 'is', 'to', 'have']
GAP2 = [
    ('There’s something to be ______ for keeping a gratitude journal.', ['said'], 'gw5'),
    ('Where it ______ down is the promise that you don’t need a plan.', ['falls'], 'gw6'),
    ('I’d stop ______ of calling it a scam, but it is oversold.', ['short'], 'gw7'),
    ('It would ______ that the people who succeed also work the hardest.', ['seem'], 'gw8'),
]
BANK2 = ['seem', 'short', 'said', 'falls']

ORDER1 = ['The Secret', 'is thought', 'to have sold', 'more than thirty million copies']
ORDER2 = ['Vision boards', 'are widely believed', 'to help', 'people stay focused']
ORDER2_DECOY = ['that help']

MATCH = [
    ('manifest', 'bring something about by believing in it'),
    ('a vision board', 'pictures of the life you want'),
    ('wishful thinking', 'believing what you would like to be true'),
    ('an affirmation', 'a positive sentence repeated every day'),
    ('a self-fulfilling prophecy', 'a prediction that makes itself come true'),
]

SORT_BINS = ['States it as fact', 'Keeps its distance']
SORT_ITEMS = [
    ('“Vision boards change your future.”', 0),
    ('“Vision boards are said to change your future.”', 1),
    ('“Gratitude attracts money.”', 0),
    ('“Supposedly, gratitude attracts money.”', 1),
    ('“The universe answers your thoughts.”', 0),
    ('“There is little evidence that thoughts change events.”', 1),
    ('“Affirmations always work.”', 0),
    ('“Affirmations tend to help some people relax.”', 1),
    ('“It would seem that the plan matters most.”', 1),
]


def divider(n, pic, pos=None):
    return D.divider('d%dt' % n, E['d%dt' % n], 'd%dn' % n, E['d%dn' % n],
                     folder=F, pic=pic, pos=pos)


def intro(n, pic, side, pos):
    return D.panel('e%d' % n, E['e%d' % n], 'p%dt' % n, E['p%dt' % n],
                   [('p%da' % n, E['p%da' % n]), ('p%db' % n, E['p%db' % n], 'dim')],
                   folder=F, pic=pic, side=side, pos=pos)


def cards(n):
    part, tk = CARD_PART[n], CARD_TITLE[n]
    return D.teach('e%d' % part, E['e%d' % part], tk, E[tk],
                   [(None, w, k, E[k], None, ex) for w, k, ex in CARDS[n]],
                   cols='1fr 1fr 1fr')


def mc(i):
    xk, sk, stem, opts, c, why = MC[i]
    part = MC_PART[i]
    return D.mc(i + 1, len(MC), dict(stem=E[sk] if sk else stem, options=opts,
                                     correct=c, why=why),
                'e%d' % part, E['e%d' % part], 'mt%d' % part, E['mt%d' % part],
                ctx=E[xk], ctx_key=xk, stem_key=sk)


def gap(i, rows, bank, part, tk):
    return D.gap(i, 4, rows, bank, 'e%d' % part, E['e%d' % part],
                 tk, E[tk], hint=E['gh'], hint_key='gh', width=150, size=20)


def build():
    logo = D.logo_from(TPL)
    D.assert_no_key_is_longest([dict(options=m[3], correct=m[4]) for m in MC])
    D.assert_bank_is_not_a_key(BANK1, [r[1][0] for r in GAP1])
    D.assert_bank_is_not_a_key(BANK2, [r[1][0] for r in GAP2])

    slides = "".join([
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])]),

        divider(1, TREND),
        intro(1, TREND, 'left', '74% 50%'),
        cards(1), cards(2),
        mc(0), mc(1),
        D.match(MATCH, 'e1', E['e1'], 'mtt', E['mtt'], 'matchHint', E['matchHint'],
                'matchWhy'),

        divider(2, CLAIMS),
        intro(2, CLAIMS, 'right', '32% 50%'),
        cards(3), cards(4),
        gap(1, GAP1[:2], BANK1, 2, 'gt1'), gap(2, GAP1[2:], BANK1, 2, 'gt1'),
        D.order(ORDER1, 'e2', E['e2'], 'ot1', E['ot1'], 'oh1', E['oh1'], 'ow1'),
        D.order(ORDER2, 'e2', E['e2'], 'ot2', E['ot2'], 'oh2', E['oh2'], 'ow2',
                decoys=ORDER2_DECOY),
        mc(2), mc(3),

        divider(3, EVIDENCE),
        intro(3, EVIDENCE, 'left', '38% 50%'),
        cards(5), cards(6),
        D.sort_slide(SORT_BINS, SORT_ITEMS, 'e3', E['e3'], 'st', E['st'], 'sh', E['sh'],
                     'sw', bin_keys=['sb1', 'sb2']),
        mc(4), mc(5), mc(6),

        divider(4, VIEW),
        # The scale fills the frame edge to edge, and any portrait slice of
        # it loses either the feather or the stone, which is the picture's
        # whole point. So the panel gets its own copy, padded rather than
        # cropped: the scale at 4–94% of the width with the plate's own sky
        # and table mirrored above and below (the Watts river-stone fix).
        # The divider still shows the plate whole.
        intro(4, 'plate-view-panel.jpg' if READY else VIEW, 'right', '50% 50%'),
        cards(7),
        gap(3, GAP2[:2], BANK2, 4, 'gt2'), gap(4, GAP2[2:], BANK2, 4, 'gt2'),
        mc(7), mc(8),

        D.results(),
        D.activate(E['actTitle'], E['actUse'],
                   ['It is said that', 'is believed to have', 'supposedly',
                    'There is little evidence that', 'It would seem that',
                    'There’s something to be said for', 'Where it falls down is',
                    'I’d stop short of saying'],
                   'Speaking', E['actSpeakBrief'],
                   [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                   E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder'],
                   folder=F, bg=ACT),
    ])

    n = slides.count('<section class="slide')
    assert ('%d slides' % n) == E['chipCount'], (n, E['chipCount'])
    langs = tuple(c for c in I.LANGS if c in I.T)
    D.assemble(TPL, OUT, slides, PALETTE,
               'Manifestation: Can You Think It Into Being? (B2) | Forbes English',
               I, langs=langs)
    print('wrote %s — %d slides, %s%s' % (OUT, n, ','.join(langs),
          '' if READY else ' (PREVIEW: plates missing, see docs/ARTWORK-manifestation.md)'))


if __name__ == '__main__':
    build()
