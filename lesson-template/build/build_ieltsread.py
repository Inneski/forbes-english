# -*- coding: utf-8 -*-
"""IELTS Reading: True / False / Not Given (C1), built as a 16:9 deck.

The Reading card on `ielts.html` had been disabled since the route was split,
and its own copy chose this lesson: "True/False/Not Given first, because that
is where the most marks are lost — and it is technique, not vocabulary, that
recovers them." So this is technique, and the deck is built on one distinction:

  **FALSE means the passage contradicts the statement. NOT GIVEN means the
  passage is silent.** The test is whether you can put your finger on a line.
  If you are reasoning — "well, it must be" — the answer is Not Given, and
  reasoning feels like understanding, which is exactly why it costs so much.

Four teaching sections, twelve items and a sort:

  1. the shape of the paper, including the trap that Reading has **no**
     transfer time where Listening has ten minutes;
  2. FALSE against NOT GIVEN;
  3. answering from the passage rather than from what you know;
  4. the qualifier that decides it — absolutes, hedges, comparatives.

The sorting slide does not sort verdicts, which would be four more items. It
sorts the SIGNALS: three things that point to FALSE against three that point
to NOT GIVEN, and every one on the right is a way of reaching a verdict
without a line to point at.

Six pictures, one per section. The three stacks of paper are the three
passages; two doorways, one shut and one opening onto flat darkness, are False
and Not Given; a book in a pool of light with everything beyond it unlit is
the passage against the world; a balance almost but not quite level is the
qualifier; and the clock over a bare desk closes it.

Ten languages, all complete (`ielts_langs.LANGS`).
"""
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ielts_langs import LANGS
from ieltsread_data import (VERDICT, WORLD, QUALIFY, ALL, VERDICTS,
                            SORT_BINS, SORT_ITEMS)

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-reading-tfng.html'
F = 'ielts-reading'

# python3 lesson-template/extract-palette.py ielts-reading/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0c0c0b;
  --surface       : #191915;
  --surface2      : #24241e;
  --border        : #ac7766;
  --text          : #f5f3f2;
  --text-dim      : #bfaaa3;
  --accent        : #e4a794;
  --accent-bright : #efb19d;
  --accent-dim    : #cc6e50;
  --secondary     : #87a1aa;
  --contrast      : #1decba;''' % F

# The target language of this deck is a set of moves, not a set of phrases —
# which is why the chips read as instructions. English in every gloss: they are
# what the learner says to themselves in the exam room.
CHIPS = ['point at the line', 'contradicts = FALSE', 'silent = NOT GIVEN',
         'most &ne; all', 'may excludes nothing', 'paraphrase, not words']

BG_SHAPE, BG_VERDICT, BG_WORLD, BG_QUALIFY = ('bg02.jpg', 'bg03.jpg',
                                              'bg04.jpg', 'bg05.jpg')
BG_ACT = 'bg06.jpg'


def check_verdicts(I):
    """The ANSWERS rule in every language the deck offers. The checker reads
    the English markup; the glosses translate, and each verdict is the key on
    four items, so one that is the only longest by four characters in German
    would hand German learners a third of the answers."""
    for code in I.T:
        L = [len(html.unescape(re.sub(r'<[^>]+>', '', I.T[code][k])))
             for k, _ in VERDICTS]
        top = sorted(L)
        assert not (L.count(top[-1]) == 1 and top[-1] - top[-2] >= 4), (
            '%s: the verdict glosses run %s characters. One is the only '
            'longest by 4+, which gives away every item it is the key for.'
            % (code, L))


def build():
    import i18n_ieltsread as I
    D.assert_no_key_is_longest(ALL, 'IELTSREAD')
    check_verdicts(I)
    logo = D.logo_from(TPL)

    # Every English string on the slides is read from the i18n module, so the
    # HTML and UI_I18N.en cannot drift apart. Until 2026-09-24 they were
    # written out twice, and a correction to one copy would have missed the
    # other.
    E = I.T['en']

    def card(p):
        return (p + 'h', E[p + 'h'], p + 'b', E[p + 'b'], p + 'n', E[p + 'n'])

    slides = (
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']),
                 ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])])

        + D.teach('t1Eyebrow', E['t1Eyebrow'], 't1Title', E['t1Title'],
                  [card('t1a'), card('t1b'), card('t1c')],
                  folder=F, bg=BG_SHAPE)

        + D.teach('t2Eyebrow', E['t2Eyebrow'], 't2Title', E['t2Title'],
                  [card('t2a'), card('t2b'), card('t2c')],
                  folder=F, bg=BG_VERDICT)

        + "".join(D.mc(i + 1, len(VERDICT), q, 'mcaEyebrow', E['mcaEyebrow'],
                       'mcaTitle', E['mcaTitle'],
                       folder=F, bg=BG_VERDICT, ctx=q.get('ctx'))
                  for i, q in enumerate(VERDICT))

        + D.teach('t3Eyebrow', E['t3Eyebrow'], 't3Title', E['t3Title'],
                  [card('t3a'), card('t3b'), card('t3c')],
                  folder=F, bg=BG_WORLD)

        + "".join(D.mc(i + 1, len(WORLD), q, 'mcbEyebrow', E['mcbEyebrow'],
                       'mcbTitle', E['mcbTitle'],
                       folder=F, bg=BG_WORLD, ctx=q.get('ctx'))
                  for i, q in enumerate(WORLD))

        + D.teach('t4Eyebrow', E['t4Eyebrow'], 't4Title', E['t4Title'],
                  [card('t4a'), card('t4b'), card('t4c')],
                  folder=F, bg=BG_QUALIFY)

        + "".join(D.mc(i + 1, len(QUALIFY), q, 'mccEyebrow', E['mccEyebrow'],
                       'mccTitle', E['mccTitle'],
                       folder=F, bg=BG_QUALIFY, ctx=q.get('ctx'))
                  for i, q in enumerate(QUALIFY))

        + D.sort_slide(SORT_BINS, SORT_ITEMS,
                       'sortEyebrow', E['sortEyebrow'],
                       'sortTitle', E['sortTitle'],
                       'sortHint', E['sortHint'],
                       'sortWhy', folder=F, bg=BG_QUALIFY,
                       bin_keys=['sortBin1', 'sortBin2'])

        + D.results('resNext', 'You can call it. Now prove it &rarr;', folder=F)

        + D.activate(E['actTitle'], E['actUse'], CHIPS,
                     'Discussion &middot; in pairs',
                     E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'],
                     E['actPlaceholder'],
                     folder=F, bg=BG_ACT)
    )

    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Reading: True, False, Not Given (C1) | Forbes English',
                   I, langs=LANGS)
    # Twelve items plus the six signals on the sorting slide: the engine scores
    # a sort per chip, so the cover chip has to say 18, not 13.
    print('wrote %s — %d slides, %d scored points, %d bytes'
          % (OUT, s.count('<section class="slide'),
             len(ALL) + len(SORT_ITEMS), len(s)))


if __name__ == '__main__':
    build()
