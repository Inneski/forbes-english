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


def build():
    D.assert_no_key_is_longest(ALL, 'IELTSENV')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Environment <em>and Energy</em>',
                'The first topic bank: three ideas, each with its pairings '
                'and its argument already attached',
                [('Level', 'C1 &middot; Advanced'),
                 ('Focus', 'Speaking &amp; Writing Task 2'),
                 ('Count', '18 points')])

        + D.teach('t1Eyebrow', 'Idea 1 of 3',
                  't1Title', 'Emissions: four pairings and two arguments',
                  [('t1ah', 'Cut them &mdash; the verb is fixed', 't1ab',
                    'Emissions are <em>cut</em> or <em>reduced</em>; a '
                    'country <em>burns fossil fuels</em> and releases '
                    '<em>greenhouse gases</em>; a city measures its <em>air '
                    'quality</em>. The verb is chosen by the noun, and none '
                    'of the four is rare.', 't1an',
                    'Four pairings, learnt whole. A bare <em>emissions</em> '
                    'in the notebook is worth none of them.'),
                   ('t1bh', 'The footprint and the tax', 't1bb',
                    'A person or a firm has a <em>carbon footprint</em>, and '
                    'shrinking it is what a <em>carbon tax</em> is for. '
                    'Both are fixed: the mark you leave is a '
                    '<em>footprint</em>, not a trace, and the charge is a '
                    '<em>tax</em>, not a fine.', 't1bn',
                    'File them together. The tax exists because of the '
                    'footprint.'),
                   ('t1ch', 'The argument it arrives with', 't1cb',
                    'Two shapes carry most Part 3 answers here. <strong>Who '
                    'pays</strong>: dirty air lands on people who did not '
                    'produce it. <strong>Targets against '
                    'enforcement</strong>: a country can promise to halve '
                    'its emissions and never fine a single factory.', 't1cn',
                    'File the idea, and the paragraph is half-written before '
                    'the question is read.')],
                  folder=F, bg=BG_EMISSIONS)

        + "".join(D.mc(i + 1, len(EMISSIONS), q, 'mcaEyebrow',
                       'Activity 1 &middot; Emissions', 'mcaTitle',
                       'Which pairing, and which word?',
                       folder=F, bg=BG_EMISSIONS, ctx=q.get('ctx'))
                  for i, q in enumerate(EMISSIONS))

        + D.teach('t2Eyebrow', 'Idea 2 of 3',
                  't2Title', 'Renewables: generate, subsidise, phase out',
                  [('t2ah', 'Generate, not make', 't2ab',
                    'A <em>wind farm</em> or a roof of <em>solar panels</em> '
                    '<em>generates electricity</em>, and what it generates '
                    'feeds the <em>national grid</em>. <em>Renewable '
                    'energy</em> is the umbrella term; <em>renewables</em> on '
                    'its own is the noun a Part 3 answer uses.', 't2an',
                    'Four pairings and one umbrella noun. All plain, all '
                    'fixed.'),
                   ('t2bh', 'The precise word for the weakness', 't2bb',
                    'The sun sets and the wind drops, so the supply is '
                    '<em>intermittent</em>: it comes and goes on its own '
                    'schedule. Several words sound close and mean something '
                    'else, and the examiner counts the one that means what '
                    'you meant.', 't2bn',
                    'A near-miss that sounds advanced scores below the plain '
                    'word that lands.'),
                   ('t2ch', 'The argument it arrives with', 't2cb',
                    'Governments <em>subsidise</em> renewables and <em>phase '
                    'out coal</em>, and every essay on the topic weighs the '
                    'same two pairs. <strong>Reliability against '
                    'cost</strong>: cheap to generate, dear to store. '
                    '<strong>Subsidy against the market</strong>: the panels '
                    'exist because someone paid, and may need someone to '
                    'keep paying.', 't2cn',
                    '<em>Energy security</em> is the third term: a country '
                    'that generates its own power cannot be cut off.')],
                  folder=F, bg=BG_RENEW)

        + "".join(D.mc(i + 1, len(RENEWABLES), q, 'mcbEyebrow',
                       'Activity 2 &middot; Renewables', 'mcbTitle',
                       'Which pairing, and which word?',
                       folder=F, bg=BG_RENEW, ctx=q.get('ctx'))
                  for i, q in enumerate(RENEWABLES))

        + D.teach('t3Eyebrow', 'Idea 3 of 3',
                  't3Title', 'Consumption and waste: the pairing includes the '
                             'preposition',
                  [('t3ah', 'Sent to landfill, cut down on', 't3ab',
                    'Rubbish is <em>sent to landfill</em>; a council reports '
                    'its <em>recycling rates</em>; a shopper <em>cuts down '
                    'on</em> <em>excess packaging</em>. The preposition '
                    'belongs to the pairing: <em>landfill</em> takes no '
                    'article, and the phrasal verb is two particles, not '
                    'one.', 't3an',
                    'Write the whole thing. Half a phrasal verb is a miss.'),
                   ('t3bh', 'Single-use, throwaway, deposit', 't3bb',
                    'A bottle used once is <em>single-use plastic</em>; a '
                    'society that expects to bin things has a <em>throwaway '
                    'culture</em>; a scheme that pays you to bring the '
                    'bottle back is a <em>deposit scheme</em>. Three '
                    'adjective-noun pairings, all C1, none rare.', 't3bn',
                    '<em>A throwaway culture</em> is worth more than '
                    '<em>consumerism</em> because it is precise.'),
                   ('t3ch', 'The argument it arrives with', 't3cb',
                    'Ask who should change and the answer is written. '
                    '<strong>Individual against producer '
                    'responsibility</strong>: a shopper can change '
                    '<em>consumer habits</em>, but the packaging was decided '
                    'before the shopper arrived. <strong>Convenience against '
                    'cost</strong>: single-use is cheap now and paid for '
                    'later.', 't3cn',
                    'Both arguments run either way round, which is what '
                    'makes them worth filing.')],
                  folder=F, bg=BG_WASTE)

        + "".join(D.mc(i + 1, len(WASTE), q, 'mccEyebrow',
                       'Activity 3 &middot; Consumption and waste', 'mccTitle',
                       'Which pairing, and which word?',
                       folder=F, bg=BG_WASTE, ctx=q.get('ctx'))
                  for i, q in enumerate(WASTE))

        + D.sort_slide(SORT_BINS, SORT_ITEMS,
                       'sortEyebrow', 'Activity 4 &middot; Filing by idea',
                       'sortTitle', 'File the six pairings',
                       'sortHint', 'Drag each one into a column &mdash; or '
                                   'click an item, then the column you want '
                                   'it in.',
                       SORT_WHY, folder=F, bg=BG_FILE,
                       bin_keys=['sortBin1', 'sortBin2'])

        + D.results('resNext', 'You can file it. Now argue with it &rarr;',
                    folder=F)

        + D.activate('Answer from the bank', 'Use at least three:', CHIPS,
                     'Discussion &middot; in pairs',
                     'In pairs. One of you is the examiner and asks three '
                     'Part 3 questions on the environment &mdash; whether '
                     'governments or individuals should act on emissions, '
                     'whether renewables can replace coal, whether recycling '
                     'is worth the effort. The other answers using only '
                     'pairings from the bank. Swap after three.',
                     ['Every answer carries at least one pairing from the '
                      'bank, said whole &mdash; the verb with its noun, or '
                      'the adjective with its noun.',
                      'The examiner asks <em>why</em> after every answer. The '
                      'follow-up has to use one of the arguments the idea '
                      'arrived with: who pays, reliability against cost, '
                      'individual against producer.',
                      'If the word is not in the bank, describe the thing in '
                      'plain English rather than reaching for a rare word.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Write one Task 2 body paragraph on one of the three '
                     'ideas &mdash; emissions, renewables, or consumption and '
                     'waste. Use at least five pairings from the bank and '
                     'underline each one. Then say which argument the '
                     'paragraph is making.',
                     'The most effective way to cut emissions is…',
                     folder=F, bg=BG_ACT)
    )

    import i18n_ieltsenv as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Vocabulary: Environment and Energy (C1) | Forbes English',
                   I, langs=LANGS)
    print('wrote %s — %d slides, %d scored points, %d bytes'
          % (OUT, s.count('<section class="slide'),
             len(ALL) + len(SORT_ITEMS), len(s)))


if __name__ == '__main__':
    build()
