# -*- coding: utf-8 -*-
"""IELTS Vocabulary: Work, Automation and Cities (C1), built as a 16:9 deck.

The second topic bank on the IELTS Vocabulary route, and the hub card on
`ielts-vocabulary.html` set the brief: "The topics that carry the most Part 3
questions and the most Task 2 prompts between them, and the collocations that
make an answer on either sound like someone who has thought about it before."

The first deck on the route, Lexical Resource, ends by teaching a method — a
bank built BY IDEA rather than alphabetically, so that each idea arrives with
two or three collocations and an argument attached. This deck is that method
carried out. Three ideas, one per picture, and each teach card is one
sub-idea: the pairings it needs (verb + noun or adjective + noun, never a bare
word) and the argument it is usually attached to in Part 3 or Task 2:

  1. **work** — flexibility against isolation, security against opportunity;
  2. **automation** — jobs lost against jobs created, who retrains whom;
  3. **cities** — density against space, the car against the bus.

The items test the pairing or the precise word, never the meaning of a word
on its own; the sort puts three real pairings against three a learner builds
one word at a time from a dictionary. The activation answers Part 3 questions
from the bank and nothing else, and writes a Task 2 body paragraph the same
way.

Six pictures, one per section: a departure board for the cover, an empty
office chair for work, a robotic arm holding one bolt for automation, a block
of flats with one window lit for cities, two interlocking cogs for the sort,
and a board mid-flip in an empty station to close.

Ten languages, all complete (`ielts_langs.LANGS`).
is read from `i18n_ieltswork.T['en']`, so the HTML and `UI_I18N.en` cannot
drift apart.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ielts_langs import LANGS
from ieltswork_data import (WORK, AUTOMATION, CITIES, ALL,
                            SORT_BINS, SORT_ITEMS, SORT_WHY)
import i18n_ieltswork as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-vocabulary-work.html'
F = 'ielts-vocabulary-work'

# python3 lesson-template/extract-palette.py ielts-vocabulary-work/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0e100e;
  --surface       : #181c18;
  --surface2      : #222722;
  --border        : #be937c;
  --text          : #f5f3f2;
  --text-dim      : #bfada3;
  --accent        : #eec7b2;
  --accent-bright : #f4b18e;
  --accent-dim    : #d9926b;
  --secondary     : #a7c3c6;
  --contrast      : #1dedd2;''' % F

# Six pairings from the bank, two per idea. English in every gloss: the
# pairing is the thing being learnt.
CHIPS = ['job security', 'take on staff', 'retrain the workforce',
         'productivity gains', 'affordable housing', 'ease congestion']

BG_WORK, BG_AUTO, BG_CITY, BG_SORT = ('bg02.jpg', 'bg03.jpg',
                                      'bg04.jpg', 'bg05.jpg')
BG_ACT = 'bg06.jpg'

E = I.T['en']


def card(p):
    """The six-item teach card for prefix p ('t1a', 't1b', …), from E."""
    return (p + 'h', E[p + 'h'], p + 'b', E[p + 'b'], p + 'n', E[p + 'n'])


def build():
    D.assert_no_key_is_longest(ALL, 'IELTSWORK')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']),
                 ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])])

        + D.teach('t1Eyebrow', E['t1Eyebrow'], 't1Title', E['t1Title'],
                  [card('t1a'), card('t1b'), card('t1c')],
                  folder=F, bg=BG_WORK)

        + "".join(D.mc(i + 1, len(WORK), q, 'mcaEyebrow', E['mcaEyebrow'],
                       'mcaTitle', E['mcaTitle'],
                       folder=F, bg=BG_WORK, ctx=q.get('ctx'))
                  for i, q in enumerate(WORK))

        + D.teach('t2Eyebrow', E['t2Eyebrow'], 't2Title', E['t2Title'],
                  [card('t2a'), card('t2b'), card('t2c')],
                  folder=F, bg=BG_AUTO)

        + "".join(D.mc(i + 1, len(AUTOMATION), q, 'mcbEyebrow', E['mcbEyebrow'],
                       'mcbTitle', E['mcbTitle'],
                       folder=F, bg=BG_AUTO, ctx=q.get('ctx'))
                  for i, q in enumerate(AUTOMATION))

        + D.teach('t3Eyebrow', E['t3Eyebrow'], 't3Title', E['t3Title'],
                  [card('t3a'), card('t3b'), card('t3c')],
                  folder=F, bg=BG_CITY)

        + "".join(D.mc(i + 1, len(CITIES), q, 'mccEyebrow', E['mccEyebrow'],
                       'mccTitle', E['mccTitle'],
                       folder=F, bg=BG_CITY, ctx=q.get('ctx'))
                  for i, q in enumerate(CITIES))

        + D.sort_slide(SORT_BINS, SORT_ITEMS,
                       'sortEyebrow', E['sortEyebrow'],
                       'sortTitle', E['sortTitle'],
                       'sortHint', E['sortHint'],
                       SORT_WHY, folder=F, bg=BG_SORT,
                       bin_keys=['sortBin1', 'sortBin2'])

        + D.results('resNext', 'You can spot it. Now say it &rarr;', folder=F)

        + D.activate(E['actTitle'], E['actUse'], CHIPS,
                     'Discussion &middot; in pairs',
                     E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'],
                     E['actPlaceholder'],
                     folder=F, bg=BG_ACT)
    )

    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Vocabulary: Work, Automation and Cities (C1) | Forbes English',
                   I, langs=LANGS)
    print('wrote %s — %d slides, %d scored points, %d bytes'
          % (OUT, s.count('<section class="slide'),
             len(ALL) + len(SORT_ITEMS), len(s)))


if __name__ == '__main__':
    build()
