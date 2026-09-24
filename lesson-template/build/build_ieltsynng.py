# -*- coding: utf-8 -*-
"""IELTS Reading: Yes / No / Not Given (C1), built as a 16:9 deck.

    py lesson-template/build/build_ieltsynng.py              # live page, once
                                                             # the art is in
    py lesson-template/build/build_ieltsynng.py --stand-in   # preview only

The sibling of `build_ieltsread.py` (True / False / Not Given), and the first
item on the Reading expansion list in the 2026-09-23 IELTS audit. Same three
answers, a different question: TFNG asks what the passage SAYS; this asks what
the WRITER THINKS. The deck is built on the one skill that difference needs:

  **Find the sentence in which the writer speaks.** A passage that argues is
  full of other people's views — critics argue, it is often claimed — and
  those sentences state the claim in full, so word-matching finds them first.
  A reported view answers nothing until the writer judges it.

Four teaching sections, twelve items and a sort:

  1. what changes from TFNG, and the answer-sheet trap (YES on a TFNG
     question scores nothing);
  2. whose voice a sentence is in — reported, the writer's own, reported
     and then judged;
  3. the concession and the turn: both halves are the writer's, the turn
     outweighs the concession, and a statement past both halves is NOT GIVEN;
  4. how strongly the writer means it — degree, hedges, evaluation words.

The sorting slide sorts six sentence openings about one plan into the
writer's own view and a view the writer only reports. The two that catch
people are both on the writer's side: "Supporters rightly point out" and
"Admittedly".

**Six pictures, one per section**, commissioned from
`docs/ARTWORK-ielts-reading-ynng.md` in the style of the TFNG set so the two
decks read as a pair, and delivered 2026-09-24: a pen on a blank notebook
(the writer), reading glasses on a closed book (the same answers, read
another way), five microphones with a spotlight on one (whose voice), a
weathervane mid-turn (the turn), a lamp whose shade is half lit (how
strongly), a wax seal on a letter (on the record). If any of them goes
missing, or PALETTE is unset, this builder writes the gitignored preview
`_forbes-english-ielts-reading-ynng.html` on the TFNG pictures and palette
instead of the live page — HOUSE-STYLE §5c and §14. `--stand-in` forces the
preview even when the art is there.

Ten languages, all complete (`ielts_langs.LANGS`). The verdict glosses translate;
the checker only reads the English, so `check_verdicts()` applies the ANSWERS
rule to every language here.
"""
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_ieltsynng as I
from chrome_i18n import CHROME
from ielts_langs import LANGS
from ieltsynng_data import (VOICE, TURN, DEGREE, ALL, VERDICTS,
                            SORT_BINS, SORT_ITEMS)

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-reading-ynng.html'
F = 'ielts-reading-ynng'
ART = ('hero.jpg', 'bg02.jpg', 'bg03.jpg', 'bg04.jpg', 'bg05.jpg', 'bg06.jpg')

# python3 lesson-template/extract-palette.py ielts-reading-ynng/hero.jpg
# Every row PASSes. The accent is the cream of the notebook's pages, not the
# TFNG salmon: derived, never picked.
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0b0d0a;
  --surface       : #161a14;
  --surface2      : #20261d;
  --border        : #d5bb98;
  --text          : #f5f4f2;
  --text-dim      : #bfb3a3;
  --accent        : #f9ecda;
  --accent-bright : #d2c6c6;
  --accent-dim    : #e9c38e;
  --secondary     : #98acaa;
  --contrast      : #1dd8ed;''' % F

# The preview borrows the TFNG set: same file names, same kind of picture, so
# the layout it measures is the layout the real art will get.
STAND_IN = 'ielts-reading'

BG_SHAPE, BG_VOICE, BG_TURN, BG_DEGREE = ('bg02.jpg', 'bg03.jpg',
                                          'bg04.jpg', 'bg05.jpg')
BG_ACT = 'bg06.jpg'

# As in the TFNG deck, the target language is a set of moves, so the chips
# read as what the learner says to themselves in the exam room.
CHIPS = ['whose voice is it?', 'reported &ne; held', 'admittedly &hellip; but',
         'the turn outweighs', 'largely &ne; completely',
         'may &ne; did']

E = I.T['en']


def check_verdicts():
    """The ANSWERS rule, in every language the deck offers.

    `check-lesson.js` and `D.assert_no_key_is_longest` read the English
    markup. The glosses translate, and each verdict is the key on four items,
    so a verdict that is the only longest by four characters in German would
    hand German learners a third of the answers."""
    for code in I.T:
        L = [len(html.unescape(re.sub(r'<[^>]+>', '', I.T[code][k])))
             for k, _ in VERDICTS]
        top = sorted(L)
        assert not (L.count(top[-1]) == 1 and top[-1] - top[-2] >= 4), (
            '%s: the verdict glosses run %s characters. One is the only '
            'longest by 4+, which gives away every item it is the key for.'
            % (code, L))


def card(p, x):
    k = p + x
    return (k + 'h', E[k + 'h'], k + 'b', E[k + 'b'], k + 'n', E[k + 'n'])


def build(stand_in=False):
    have = {a: os.path.exists('%s/%s' % (F, a)) for a in ART}
    live = all(have.values()) and PALETTE is not None and not stand_in
    folder = F if live else STAND_IN
    if live:
        palette = PALETTE
    else:
        from build_ieltsread import PALETTE as palette

    D.assert_no_key_is_longest(ALL, 'IELTSYNNG')
    check_verdicts()
    assert SORT_BINS == [E['sortBin1'], E['sortBin2']], \
        'sort bins and their i18n keys have drifted apart'
    logo = D.logo_from(TPL)

    def teach(n, bg):
        return D.teach('t%dEyebrow' % n, E['t%dEyebrow' % n],
                       't%dTitle' % n, E['t%dTitle' % n],
                       [card('t%d' % n, x) for x in 'abc'],
                       folder=folder, bg=bg)

    def items(qs, p, bg):
        return "".join(D.mc(i + 1, len(qs), q, p + 'Eyebrow', E[p + 'Eyebrow'],
                            p + 'Title', E[p + 'Title'], folder=folder, bg=bg,
                            ctx=q['ctx'])
                       for i, q in enumerate(qs))

    slides = (
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])])
        + teach(1, BG_SHAPE)
        + teach(2, BG_VOICE)
        + items(VOICE, 'mca', BG_VOICE)
        + teach(3, BG_TURN)
        + items(TURN, 'mcb', BG_TURN)
        + teach(4, BG_DEGREE)
        + items(DEGREE, 'mcc', BG_DEGREE)
        + D.sort_slide(SORT_BINS, SORT_ITEMS,
                       'sortEyebrow', E['sortEyebrow'],
                       'sortTitle', E['sortTitle'],
                       'sortHint', E['sortHint'],
                       'sortWhy', folder=folder, bg=BG_DEGREE,
                       bin_keys=['sortBin1', 'sortBin2'])
        + D.results('resNext', CHROME['en']['resNext'].strip("'"),
                    folder=folder)
        + D.activate(E['actTitle'], E['actUse'], CHIPS,
                     CHROME['en']['actSpeakKind'].strip("'"),
                     E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'],
                     E['actPlaceholder'], folder=folder, bg=BG_ACT)
    )

    out = OUT if live else '_' + OUT
    s = D.assemble(TPL, out, slides, palette,
                   'IELTS Reading: Yes, No, Not Given (C1) | Forbes English',
                   I, langs=LANGS)
    # Twelve items plus six openings on the sorting slide, which the engine
    # scores one point each: the cover chip says 18, not 13.
    print('wrote %s — %d slides, %d scored points, %d bytes'
          % (out, s.count('<section class="slide'),
             len(ALL) + len(SORT_ITEMS), len(s)))
    if not live:
        missing = [a for a in ART if not have[a]]
        print('  PREVIEW ONLY, on the %s pictures and palette. %s' % (
            STAND_IN,
            'Not on disk: %s.' % ', '.join(missing) if missing else
            'PALETTE is unset: run extract-palette.py on the hero.'
            if PALETTE is None else '--stand-in was given.'))


if __name__ == '__main__':
    build('--stand-in' in sys.argv)
