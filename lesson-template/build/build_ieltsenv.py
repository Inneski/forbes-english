# -*- coding: utf-8 -*-
"""IELTS Vocabulary: Environment and Energy (C1), built as a 16:9 deck.

The first topic bank on the IELTS Vocabulary route. The Lexical Resource deck
ends by telling the learner to build the bank by idea rather than
alphabetically, so that each word arrives with an argument attached; this deck
is that method carried out on one topic. The hub card on `ielts-vocabulary.html`
set the brief: "emissions, renewables, consumption and waste, each arriving
with two phrases and an argument already attached."

So the deck is three IDEAS, one per picture, and each teach slide is three
cards: the verb-noun pairings, the adjective-noun pairings and the precise
word, then the argument the idea usually carries in Part 3 and Task 2:

  1. **emissions** — cut emissions, burn fossil fuels, greenhouse gases, air
     quality, a carbon footprint, a carbon tax; who pays, targets against
     enforcement;
  2. **renewables** — generate electricity, solar panels, a wind farm, the
     national grid, an intermittent supply, subsidise, phase out coal, energy
     security; reliability against cost, subsidy against the market;
  3. **consumption and waste** — sent to landfill, recycling rates, cut down
     on, excess packaging, single-use plastic, a throwaway culture, a deposit
     scheme, consumer habits; individual against producer, convenience
     against cost.

The items test the pairing or the precise word, never a bare word — which is
the previous deck's own rule — and one item per section asks which argument a
Part 3 answer is making. The sorting slide files six pairings under two of the
ideas, and its explanation says why filing by idea gives you an argument.

Six pictures: a card index for the cover, a factory chimney for emissions, a
roof of solar panels for renewables, an overflowing street bin for waste, a
pegboard with tools hung by kind for the filing, and a bare bulb switched on
to close.

Ten languages, all complete (`ielts_langs.LANGS`).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ielts_langs import LANGS
from ieltsenv_data import (EMISSIONS, RENEWABLES, WASTE, ALL,
                           SORT_BINS, SORT_ITEMS, SORT_WHY)
import i18n_ieltsenv as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-vocabulary-environment.html'
F = 'ielts-vocabulary-environment'

# python3 lesson-template/extract-palette.py ielts-vocabulary-environment/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #090c0e;
  --surface       : #13191b;
  --surface2      : #1b2427;
  --border        : #a8948a;
  --text          : #f5f3f2;
  --text-dim      : #bfada3;
  --accent        : #e3c5b5;
  --accent-bright : #eac0a9;
  --accent-dim    : #c59277;
  --secondary     : #a0b7b8;
  --contrast      : #2fdac4;''' % F

# Pairings, not words — the deck's own rule. English in every gloss: the
# pairing is the thing being learnt.
CHIPS = ['cut emissions', 'a carbon footprint', 'generate electricity',
         'phase out coal', 'single-use plastic', 'a deposit scheme']

BG_EMISSIONS, BG_RENEW, BG_WASTE, BG_FILE = ('bg02.jpg', 'bg03.jpg',
                                             'bg04.jpg', 'bg05.jpg')
BG_ACT = 'bg06.jpg'

# Every English string on the slides is read from the i18n module, so the
# HTML and UI_I18N.en cannot drift apart. Until 2026-09-24 they were written
# out twice, and a correction to one copy would have missed the other.
E = I.T['en']


def card(p):
    """The six-item teach card for prefix p ('t1a', 't1b', …), from E."""
    return (p + 'h', E[p + 'h'], p + 'b', E[p + 'b'], p + 'n', E[p + 'n'])


def build():
    D.assert_no_key_is_longest(ALL, 'IELTSENV')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']),
                 ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])])

        + D.teach('t1Eyebrow', E['t1Eyebrow'], 't1Title', E['t1Title'],
                  [card('t1a'), card('t1b'), card('t1c')],
                  folder=F, bg=BG_EMISSIONS)

        + "".join(D.mc(i + 1, len(EMISSIONS), q, 'mcaEyebrow', E['mcaEyebrow'],
                       'mcaTitle', E['mcaTitle'],
                       folder=F, bg=BG_EMISSIONS, ctx=q.get('ctx'))
                  for i, q in enumerate(EMISSIONS))

        + D.teach('t2Eyebrow', E['t2Eyebrow'], 't2Title', E['t2Title'],
                  [card('t2a'), card('t2b'), card('t2c')],
                  folder=F, bg=BG_RENEW)

        + "".join(D.mc(i + 1, len(RENEWABLES), q, 'mcbEyebrow', E['mcbEyebrow'],
                       'mcbTitle', E['mcbTitle'],
                       folder=F, bg=BG_RENEW, ctx=q.get('ctx'))
                  for i, q in enumerate(RENEWABLES))

        + D.teach('t3Eyebrow', E['t3Eyebrow'], 't3Title', E['t3Title'],
                  [card('t3a'), card('t3b'), card('t3c')],
                  folder=F, bg=BG_WASTE)

        + "".join(D.mc(i + 1, len(WASTE), q, 'mccEyebrow', E['mccEyebrow'],
                       'mccTitle', E['mccTitle'],
                       folder=F, bg=BG_WASTE, ctx=q.get('ctx'))
                  for i, q in enumerate(WASTE))

        + D.sort_slide(SORT_BINS, SORT_ITEMS,
                       'sortEyebrow', E['sortEyebrow'],
                       'sortTitle', E['sortTitle'],
                       'sortHint', E['sortHint'],
                       SORT_WHY, folder=F, bg=BG_FILE,
                       bin_keys=['sortBin1', 'sortBin2'])

        + D.results('resNext', 'You can file it. Now argue with it &rarr;',
                    folder=F)

        + D.activate(E['actTitle'], E['actUse'], CHIPS,
                     'Discussion &middot; in pairs',
                     E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'],
                     E['actPlaceholder'],
                     folder=F, bg=BG_ACT)
    )
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Vocabulary: Environment and Energy (C1) | Forbes English',
                   I, langs=LANGS)
    print('wrote %s — %d slides, %d scored points, %d bytes'
          % (OUT, s.count('<section class="slide'),
             len(ALL) + len(SORT_ITEMS), len(s)))


if __name__ == '__main__':
    build()
