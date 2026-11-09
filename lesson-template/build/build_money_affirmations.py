# -*- coding: utf-8 -*-
"""Money Affirmations: Mindset or Magic? (B1). House style 1.

Innes, 2026-11-06: after a chat about financial manifestation, he pasted a
listicle of ninety-nine money affirmations ("I am worthy of …", "Money
flows to me …") and said *"Well lets make a class on it anyway"*.

The general manifestation deck already exists (forbes-manifestation-b2.html,
B2: reporting a claim without endorsing it — IT IS SAID THAT, SUPPOSEDLY,
hedging). This one does not repeat it. It takes the money angle and the
language the affirmations themselves are made of:

  1 Money words     — income stream, hourly rate, savings, debt, financial
                      freedom, scarcity mindset; a collocation match
                      (PAY OFF a loan, SET a budget …); MC ×3
  2 Verb patterns   — DESERVE TO, AFFORD TO, WORTHY OF + -ING, ATTRACT + object,
                      SPEND ON / SAVE FOR / INVEST IN; MC ×3, gap ×3
  3 Wish or plan?   — an affirmation is PRESENT SIMPLE/CONTINUOUS as if
                      already true; a plan is GOING TO / WILL + BY + date,
                      so it can be checked; sort, MC ×3, order ×2, gap ×3
then Let's talk with the target forms, results and the activation stage.

None of the article's affirmations is used: every sentence on the slides is
written for the lesson (the listicle is copyrighted, and its sentences are
not graded for B1). The deck takes no position the evidence cannot carry:
it never says affirmations make money, and its critique is a language
point — a sentence with no action and no date cannot be checked.

Keys checked by hand while writing:
  * "pay back his student loan" is also correct, so PAY BACK is not an
    option in Q2.
  * GOING TO vs WILL is not tested as a contrast: both are accepted in the
    gaps, and no MC hangs on the difference, because in speech either is
    usually fine for these sentences.
  * Order 1's decoy "until July." is wrong in every position (PAY OFF is a
    finished action); order 2's "taking" can only build "deserve taking".

Art: seven Midjourney plates (2026-11-08), one per slot, every prompt with
--sref to the manifestation deck's cover so the two lessons read as a set;
Innes picked each from its grid. They replace the stand-ins by name
(deck.plate() prefers <slot>.jpg) and the palette was re-derived from
hero.jpg. The warm-up plate carries the words WISH LIST on purpose: Innes
re-rolled it to make them clearer, since the slide asks what is on the
students' own wish lists.

Run from the repo root:  py lesson-template/build/build_money_affirmations.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
import deck as D
import i18n_money_affirmations as I
import hs1

TPL = 'lesson-template/lesson-template.html'
F = 'MoneyAffirmations'
OUT = 'forbes-money-affirmations-b1.html'
TITLE = 'Money Affirmations: Mindset or Magic? (B1)'
E = I.T['en']

ART = {
    'hero':  ('money', 'a small green seedling growing out of the coin slot of a piggy bank'),
    'warm':  ('quiz', 'an open wallet with a folded wish list sticking out of it instead of banknotes'),
    'talk':  ('talk', 'two coffee cups on a cafe table, the steam from one curling into a coin, from the other into a question mark'),
    'words': ('money', 'a piggy bank with three thin streams of coins flowing into it from different directions'),
    'verbs': ('words', 'a large horseshoe magnet pulling a trail of coins towards it'),
    'plan':  ('write', 'a wall calendar with one date circled and a single coin pinned beside it'),
    'act':   ('pair', 'two chairs facing each other across a small round table, a glass jar of coins and an open notebook between them'),
}
# House style 1 (HOUSE-STYLE §000, 2026-11-09): the seven plates above stay,
# and these nine Midjourney renders (his style images, --stylize 200) give
# every slide its own plate, none twice in a stage.
NEW = {
    'm-a2': 'a young man stuffing a letter about his student loan into a drawer, car keys on the desk',
    'm-a3': 'a worried woman counting coins at a kitchen table, bills paid and pinned on the wall',
    'm-b2': 'a woman in an office receiving a bigger pay envelope from her boss',
    'm-b3': 'a man at a laptop buying an online course, a pile of course boxes beside him',
    'm-c2': 'a calendar page for December with a debt paid stamp across it',
    'm-c3': 'a person sitting cross-legged repeating a phrase with eyes closed, coins floating around',
    'o1': 'a hand cutting up a credit card with scissors beside a calendar showing July',
    'o2': 'a tired office worker leaving the office for a holiday with a suitcase',
    'talk2': 'two friends talking about money over coffee, a notebook of figures between them',
}
POP = {'hero': (None, 'square'), 'talk2': (None, 'blob')}
K = hs1.Deck(F, pop=POP, title_px=50, cover_w=46)

# py lesson-template/extract-palette.py MoneyAffirmations/hero.jpg --paper
# (2026-11-08, from the Midjourney hero; every row PASS).
PALETTE_BODY = """
  --void          : #fcfcf9;
  --surface       : #f2f0e5;
  --surface2      : #f7f6f0;
  --border        : #d0c895;
  --text          : #231613;
  --text-dim      : #594540;
  --accent        : #d02900;
  --accent-bright : #a82100;
  --accent-dim    : #f0b6a8;
  --secondary     : #0e251a;
  --contrast      : #096d50;"""


def palette(hero_ref):
    return "  --hero: url('%s');\n%s" % (hero_ref, PALETTE_BODY)


# ── content ────────────────────────────────────────────────────────────
APOS = lambda a: '|'.join(sorted({a, a.replace('’', "'"), a.replace("'", '’')}))

SURVEY = [('buy a home', 1), ('travel', 2), ('pay off debts', 3),
          ('help their family', 4), ('stop working', 5)]

TALK_1 = [
    'Do you talk about money with your friends, or is it private?',
    'Have you ever seen a vision board or a list of affirmations?',
    'Can positive thinking change your bank balance?',
    'What is the difference between a dream and a goal?',
    'Who taught you about money when you were young?',
    'Is it better to save money or to enjoy it now?',
]

VOCAB_A = [
    ('an income stream', [('vA1', E['vA1'])],
     'She has three <strong>income streams</strong>: a job, a flat she rents out and an online shop.'),
    ('an hourly rate', [('vA2', E['vA2'])],
     'As a freelancer, his <strong>hourly rate</strong> is £40.'),
    ('savings', [('vA3', E['vA3'])],
     'We used our <strong>savings</strong> to pay for the wedding.'),
]
VOCAB_B = [
    ('debt', [('vB1', E['vB1'])],
     'After university, she was £30,000 in <strong>debt</strong>.'),
    ('financial freedom', [('vB2', E['vB2'])],
     'For him, <strong>financial freedom</strong> means never checking prices in the supermarket.'),
    ('a scarcity mindset', [('vB3', E['vB3'])],
     'Even with money in the bank, his <strong>scarcity mindset</strong> makes him worry.'),
]

MATCH = [('pay off', 'a loan'), ('set', 'a budget'), ('open', 'a savings account'),
         ('charge', 'a fee'), ('get', 'a pay rise'), ('go into', 'debt')]

MC_A = [
    dict(stem='She has three ___: her job, rent from a small flat and an online shop.',
         options=['income streams', 'hourly rates', 'savings accounts', 'pay rises'], correct=0, why='q1w'),
    dict(stem='He wants to ___ his student loan before he buys a car.',
         options=['pay off', 'go into', 'set up', 'charge for'], correct=0, why='q2w'),
    dict(stem='My bills are paid, but I always feel there is never enough money. I think I have a ___.',
         options=['scarcity mindset', 'savings account', 'generous budget', 'abundance mindset'],
         correct=0, why='q3w'),
]
MC_B = [
    dict(stem='I can’t ___ a new car this year — maybe next year.',
         options=['afford to buy', 'afford buying', 'afford for buying', 'afford buy'], correct=0, why='q4w'),
    dict(stem='After ten years of hard work, she feels worthy ___ a higher salary.',
         options=['of earning', 'to earning', 'for earn', 'of earn'], correct=0, why='q5w'),
    dict(stem='He spends most of his money ___ online courses about manifesting.',
         options=['on', 'for', 'in', 'at'], correct=0, why='q6w'),
]
MC_C = [
    dict(stem='I’ve decided. I ___ £100 a month until Christmas.',
         options=['am going to save', 'was going to save', 'have been saving', 'would have saved'],
         correct=0, why='q7w'),
    dict(stem='I’ll pay off the whole loan ___ the end of the year.',
         options=['by', 'until', 'since', 'for'], correct=0, why='q8w'),
    dict(stem=E['s9'],
         options=['I’m going to save £600 by June.', 'I am rich in every area of my life.',
                  'Money is flowing into my account right now.',
                  'I deserve every good thing that comes to me.'], correct=0, why='q9w'),
]
# Written key-first for readability; dealt across the positions here so the
# source does not give the key away (check-lesson.js KEYS).
for n, q in enumerate(MC_A + MC_B + MC_C):
    q['stem'] = q['stem'].replace('___', '____')
    k = q['options'].pop(q['correct'])
    q['correct'] = (n * 3 + 1) % 4
    q['options'].insert(q['correct'], k)
D.assert_no_key_is_longest(MC_A + MC_B + MC_C)

GAP_B = [
    ('We are saving ______ a new kitchen.', ['for|up for'], 'g1w'),
    ('You work so hard. You deserve ______ (have) a holiday.', ['to have'], 'g2w'),
    ('Never invest ______ something you don’t understand.', ['in'], 'g3w'),
]
GAP_C = [
    ('“Money flows to me.” → I ______ (ask) my boss for a pay rise next week.',
     [APOS('’m going to ask') + '|am going to ask|will ask|' + APOS('’ll ask')], 'g4w'),
    ('“I am debt-free.” → I’ll pay off my credit card ______ December.', ['by'], 'g5w'),
    ('“I attract opportunities.” → I ______ (apply) for three new jobs this month.',
     [APOS('’m going to apply') + '|am going to apply|will apply|' + APOS('’ll apply')
      + '|' + APOS('’m applying') + '|am applying'], 'g6w'),
]

SORT = [('Money comes to me easily.', 0), ('I am a magnet for success.', 0),
        ('My bank balance is growing every day.', 0), ('Abundance is all around me.', 0),
        ('I’m going to ask for a pay rise in March.', 1), ('I’ll pay off my credit card by July.', 1),
        ('I’m meeting a financial adviser on Friday.', 1), ('I’m going to put £20 a week into savings.', 1)]

ORDERS = [
    (['I’m going to', 'pay off', 'my credit card', 'by July.'], ['until July.'], 'o1w'),
    (['You', 'deserve', 'to take', 'a break', 'from work.'], ['taking'], 'o2w'),
]

TALK_2 = [
    'Do people <strong>deserve to</strong> be rich if they work hard?',
    'What <strong>can’t</strong> you <strong>afford to</strong> do right now that you would love to do?',
    'What <strong>are you going to</strong> save <strong>for</strong> this year?',
    'Would you <strong>spend</strong> money <strong>on</strong> a course about manifesting? Why or why not?',
    'Is it healthy to say “I am rich” when your bank account says something different?',
    'How many <strong>income streams</strong> does a typical person have? Is one enough?',
    'Is a <strong>scarcity mindset</strong> a problem, or is it just being careful?',
    'What <strong>will</strong> you do differently with money <strong>by</strong> the end of this year?',
]


# ── slide helpers ──────────────────────────────────────────────────────
def mcs(qs, start, total, ek, slots, stem_keys=None):
    out = []
    for n, (q, slot) in enumerate(zip(qs, slots)):
        sk = (stem_keys or {}).get(n)
        out.append(K.frame(D.mc(start + n, total, q, ek, E[ek], 'mcT', E['mcT'], stem_key=sk),
                           slot, text=(q['stem'], q['options'])))
    return out


def gap(rows, ek, hint_key):
    # Full width, no picture: each row grows an explanation once answered
    # (HOUSE-STYLE §16.2).
    return D.gap(1, 1, rows, None, ek, E[ek], 'gapT', E['gapT'],
                 hint=E[hint_key], hint_key=hint_key, size=21)


def b(keys):
    return [(k, E[k]) for k in keys]


def slides():
    s = [K.cover(E, [('Level', E['chipLevel']), ('Focus', E['chipFocus']), ('Count', E['chipCount'])])]

    # ── warm-up ────────────────────────────────────────────────────────
    s.append(K.frame(D.survey('eW', E['eW'], 'svT', E['svT'], 'svQ', E['svQ'], SURVEY,
                              hint=('svHint', E['svHint'])), 'warm'))
    s.append(K.frame(K.talk('eT', 'tk1T', TALK_1, E, cols=1), 'talk'))
    K.stage()

    # ── stage 1 · money words ──────────────────────────────────────────
    s.append(D.rules('eV', E['eV'], 'vAt', E['vAt'], VOCAB_A))
    s.append(D.rules('eV', E['eV'], 'vBt', E['vBt'], VOCAB_B))
    # the match's two columns take the full width
    s.append(D.match(MATCH, 'e1', E['e1'], 'matchT', E['matchT'], 'matchHint',
                     E['matchHint'], 'matchW'))
    s += mcs(MC_A, 1, 3, 'e1', ['words', 'm-a2', 'm-a3'])
    K.stage()

    # ── stage 2 · verb patterns ────────────────────────────────────────
    s.append(D.rules('eR', E['eR'], 'rBt', E['rBt'], [
        ('deserve / afford + to + verb', b(['rB1', 'rB2']),
         'You <strong>deserve to rest</strong>. I <strong>can’t afford to stop</strong>.'),
        ('worthy of + noun / -ing', b(['rB3', 'rB4']),
         'I am <strong>worthy of earning</strong> more.'),
        ('attract + noun · spend on', b(['rB5', 'rB6']),
         'Hard work <strong>attracts</strong> clients. Don’t <strong>spend</strong> it all <strong>on</strong> shoes.'),
    ]))
    s += mcs(MC_B, 1, 3, 'e2', ['verbs', 'm-b2', 'm-b3'])
    K.stage()
    s.append(gap(GAP_B, 'e2', 'gHintB'))

    # ── stage 3 · wish or plan ─────────────────────────────────────────
    s.append(K.frame(D.rules('eR', E['eR'], 'rCt', E['rCt'], [
        ('Affirmation: present simple / continuous', b(['rC1', 'rC2', 'rC3']),
         'Money <strong>flows</strong> to me. Money <strong>is pouring</strong> into my life.'),
        ('Plan: going to / will + by', b(['rC4', 'rC5', 'rC6']),
         'I<strong>’m going to save</strong> £600 <strong>by</strong> June. I<strong>’ll check</strong> my account every Friday.'),
    ]), None))
    s.append(D.sort_slide([E['binA'], E['binP']], SORT, 'e3', E['e3'], 'sortT', E['sortT'],
                          'sortHint', E['sortHint'], 'sortW', bin_keys=['binA', 'binP']))
    s += mcs(MC_C, 1, 3, 'e3', ['plan', 'm-c2', 'm-c3'], stem_keys={2: 's9'})
    for n, (items, dec, why) in enumerate(ORDERS):
        s.append(K.frame(D.order(items, 'e3', E['e3'], 'orderT', E['orderT'], 'orderHint',
                                 E['orderHint'], why, decoys=dec), ['o1', 'o2'][n]))
    s.append(gap(GAP_C, 'e3', 'gHintC'))

    # ── speaking, results, activation ──────────────────────────────────
    K.stage()
    # eight prompts need three columns: the talk plate goes to the results
    s.append(K.talk('eT', 'tk2T', TALK_2, E))
    s.append(K.frame(D.results(), 'talk2'))
    chips = ['deserve to', 'can’t afford to', 'worthy of', 'save for', 'spend on',
             'I’m going to', 'I’ll', 'by + date', 'an income stream', 'pay off']
    s.append(D.activate(E['actTitle'], E['actUse'], chips, 'Speaking', E['actSpeakBrief'],
                        [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                        E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder']))
    return "".join(s)


def build():
    if PALETTE_BODY is None:
        sys.exit('derive the palette first:\n  py lesson-template/extract-palette.py '
                 '%s/hero.jpg --paper' % F)
    K.assemble(OUT, slides(), TITLE, I, ('en', 'de', 'es'))


if __name__ == '__main__':
    build()
