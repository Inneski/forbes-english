# -*- coding: utf-8 -*-
"""IELTS Vocabulary: Lexical Resource (C1), built as a 16:9 deck.

The last disabled card on `ielts.html`, and its own copy set the brief: "Topic
banks that feed Speaking and Task 2 at once, since Lexical Resource is a
quarter of the marks in both. Words you have to use, not words you have to
read."

So the deck is built against the belief that costs candidates the most here —
that this criterion rewards rare words. It does not. The public descriptors ask
for less common lexis used with PRECISION and FLEXIBILITY, and they penalise
inaccuracy by name, which means a reach-and-miss scores below a plain word that
lands. What actually moves the band is three things, and they are the three
sections:

  1. **precision** — the near-miss costs more than the plain word, and a
     memorised "band 9 phrase" is audible because it sits apart from the
     English around it;
  2. **collocation** — the unit that gets scored is the pairing. You *conduct*
     research and *reach* a decision; there is *heavy traffic* and *heavy
     fighting* but never *heavy sunshine*, and no rule predicts it, which is
     why a notebook entry has to be a phrase and not a word;
  3. **paraphrase** — the one skill Speaking Part 3 and Task 2 both pay for,
     and the reason a topic bank is built by idea rather than alphabetically:
     a word filed under an idea arrives with an argument attached.

The sorting slide is the lesson in one screen. Six habits, two columns, and
the impressive-feeling ones — memorising phrase lists, reaching for a thesaurus
word, echoing the question — are all in the column that pays nothing.

Six pictures, one per section: a card-index cabinet for the cover, gauge blocks
for precision, interlocking blocks for collocation, two differently shaped
vessels holding the same volume for paraphrase, a wall of labelled drawers for
the bank, and a desk with an open notebook to close.

Ten languages, all complete (`ielts_langs.LANGS`).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ielts_langs import LANGS
from ieltsvocab_data import (PRECISION, COLLOCATION, PARAPHRASE, ALL,
                             SORT_BINS, SORT_ITEMS, SORT_WHY)
import i18n_ieltsvocab as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-lexical-resource.html'
F = 'ielts-vocabulary'

# python3 lesson-template/extract-palette.py ielts-vocabulary/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #10110f;
  --surface       : #1c1e19;
  --surface2      : #262922;
  --border        : #a18a7e;
  --text          : #f5f3f2;
  --text-dim      : #bfaca3;
  --accent        : #deb9a7;
  --accent-bright : #eac3b0;
  --accent-dim    : #c0866a;
  --secondary     : #a4bab6;
  --contrast      : #2edbc0;

  /* This deck's backgrounds are the brightest and busiest on the IELTS route —
     a wall of pale drawers behind the sorting slide. At the house default of
     0.68 the order hint measured 4.33:1 against the lightest patch under it,
     which is below AA. Raised per deck, exactly as the template's note says to
     do, and re-measured in the page rather than by eye. */
  --plate: 0.82;''' % F

# Collocations, not single words — which is the deck's own argument. English in
# every gloss: the pairing is the thing being learnt.
CHIPS = ['conduct research', 'reach a decision', 'draw a conclusion',
         'heavy traffic', 'tackle congestion', 'ease the pressure']

BG_PRECISION, BG_COLLOC, BG_PARA, BG_BANK = ('bg02.jpg', 'bg03.jpg',
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
    D.assert_no_key_is_longest(ALL, 'IELTSVOCAB')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']),
                 ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])])

        + D.teach('t1Eyebrow', E['t1Eyebrow'], 't1Title', E['t1Title'],
                  [card('t1a'), card('t1b'), card('t1c')],
                  folder=F, bg=BG_PRECISION)

        + "".join(D.mc(i + 1, len(PRECISION), q, 'mcaEyebrow', E['mcaEyebrow'],
                       'mcaTitle', E['mcaTitle'],
                       folder=F, bg=BG_PRECISION, ctx=q.get('ctx'))
                  for i, q in enumerate(PRECISION))

        + D.teach('t2Eyebrow', E['t2Eyebrow'], 't2Title', E['t2Title'],
                  [card('t2a'), card('t2b'), card('t2c')],
                  folder=F, bg=BG_COLLOC)

        + "".join(D.mc(i + 1, len(COLLOCATION), q, 'mcbEyebrow', E['mcbEyebrow'],
                       'mcbTitle', E['mcbTitle'],
                       folder=F, bg=BG_COLLOC, ctx=q.get('ctx'))
                  for i, q in enumerate(COLLOCATION))

        + D.teach('t3Eyebrow', E['t3Eyebrow'], 't3Title', E['t3Title'],
                  [card('t3a'), card('t3b'), card('t3c')],
                  folder=F, bg=BG_PARA)

        + "".join(D.mc(i + 1, len(PARAPHRASE), q, 'mccEyebrow', E['mccEyebrow'],
                       'mccTitle', E['mccTitle'],
                       folder=F, bg=BG_PARA, ctx=q.get('ctx'))
                  for i, q in enumerate(PARAPHRASE))

        + D.sort_slide(SORT_BINS, SORT_ITEMS,
                       'sortEyebrow', E['sortEyebrow'],
                       'sortTitle', E['sortTitle'],
                       'sortHint', E['sortHint'],
                       'sortWhy', folder=F, bg=BG_BANK,
                       bin_keys=['sortBin1', 'sortBin2'])

        + D.results('resNext', 'You can spot it. Now build it &rarr;', folder=F)

        + D.activate(E['actTitle'], E['actUse'], CHIPS,
                     'Discussion &middot; in pairs',
                     E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'],
                     E['actPlaceholder'],
                     folder=F, bg=BG_ACT)
    )
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Lexical Resource: Vocabulary That Scores (C1) | Forbes English',
                   I, langs=LANGS)
    print('wrote %s — %d slides, %d scored points, %d bytes'
          % (OUT, s.count('<section class="slide'),
             len(ALL) + len(SORT_ITEMS), len(s)))


if __name__ == '__main__':
    build()
