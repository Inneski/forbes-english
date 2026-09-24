# -*- coding: utf-8 -*-
"""IELTS Pronunciation & fluency (C1), built as a 16:9 deck.

The third step on `ielts-speaking.html`, and the second of the two cards that
route had been showing as disabled with nothing behind them. Its own copy made
the argument for the lesson: "A quarter of the marks sits on pronunciation and
most candidates never practise it deliberately."

The deck is built around the misconception that makes that practice not happen.
Candidates hear "pronunciation" and think "accent", decide the accent is not
going to change in the weeks before the test, and skip the criterion. But the
public descriptors score intelligibility, control of the features that carry
meaning, and the effort the listener has to make. An accent costs nothing. Flat
stress, a break in the middle of a noun phrase and a filler inside a phrase all
cost something, and all three are fixable in an afternoon.

Three sections — stress, thought groups, pausing and repair — then a sorting
task that puts the whole misconception on one slide: six habits, two columns,
"costs you marks" against "costs you nothing". The accent goes in the free
column. That slide is the lesson.

Six pictures, one per section: a microphone in an empty room for the cover,
pendant lamps at unequal heights for stress, a shelf of clustered objects for
thought groups, an empty chair and a glass set down for the pause, a tiled wall
for the drills, and two chairs with a stopwatch for the activation stage.

Ten languages, all complete (`ielts_langs.LANGS`).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ielts_langs import LANGS
from ieltspron_data import (STRESS, CHUNK, PAUSE, ALL,
                            SORT_BINS, SORT_ITEMS, SORT_WHY)
import i18n_ieltspron as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-pronunciation.html'
F = 'ielts-pronunciation'

# python3 lesson-template/extract-palette.py ielts-pronunciation/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0f1517;
  --surface       : #182125;
  --surface2      : #202c31;
  --border        : #b2aba0;
  --text          : #f5f4f2;
  --text-dim      : #bfb4a3;
  --accent        : #eadfce;
  --accent-bright : #d2c6c6;
  --accent-dim    : #cab492;
  --secondary     : #364851;
  --contrast      : #35c0d4;''' % F

# The chips are the moves, not phrases: this is the one deck on the route whose
# target language is a way of saying things rather than a set of expressions.
CHIPS = ['thought groups', 'content-word stress', 'pause at the joins',
         'no filler inside a phrase', 'paraphrase, do not stop',
         'RECord / reCORD']

BG_STRESS, BG_CHUNK, BG_PAUSE, BG_SORT = ('bg02.jpg', 'bg03.jpg',
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
    D.assert_no_key_is_longest(ALL, 'IELTSPRON')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']),
                 ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])])

        + D.teach('t1Eyebrow', E['t1Eyebrow'], 't1Title', E['t1Title'],
                  [card('t1a'), card('t1b'), card('t1c')],
                  folder=F, bg=BG_STRESS)

        + "".join(D.mc(i + 1, len(STRESS), q, 'mcaEyebrow', E['mcaEyebrow'],
                       'mcaTitle', E['mcaTitle'], folder=F, bg=BG_STRESS,
                       ctx=q.get('ctx'))
                  for i, q in enumerate(STRESS))

        + D.teach('t2Eyebrow', E['t2Eyebrow'], 't2Title', E['t2Title'],
                  [card('t2a'), card('t2b'), card('t2c')],
                  folder=F, bg=BG_CHUNK)

        + "".join(D.mc(i + 1, len(CHUNK), q, 'mcbEyebrow', E['mcbEyebrow'],
                       'mcbTitle', E['mcbTitle'], folder=F, bg=BG_CHUNK,
                       ctx=q.get('ctx'))
                  for i, q in enumerate(CHUNK))

        + D.teach('t3Eyebrow', E['t3Eyebrow'], 't3Title', E['t3Title'],
                  [card('t3a'), card('t3b'), card('t3c')],
                  folder=F, bg=BG_PAUSE)

        + "".join(D.mc(i + 1, len(PAUSE), q, 'mccEyebrow', E['mccEyebrow'],
                       'mccTitle', E['mccTitle'], folder=F, bg=BG_PAUSE,
                       ctx=q.get('ctx'))
                  for i, q in enumerate(PAUSE))

        + D.sort_slide(SORT_BINS, SORT_ITEMS,
                       'sortEyebrow', E['sortEyebrow'],
                       'sortTitle', E['sortTitle'],
                       'sortHint', E['sortHint'],
                       'sortWhy', folder=F, bg=BG_SORT,
                       bin_keys=['sortBin1', 'sortBin2'])

        + D.results('resNext', 'You can hear it. Now say it &rarr;', folder=F)

        + D.activate(E['actTitle'], E['actUse'], CHIPS,
                     'Discussion &middot; in pairs',
                     E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'],
                     E['actPlaceholder'],
                     folder=F, bg=BG_ACT)
    )
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Pronunciation & Fluency (C1) | Forbes English',
                   I, langs=LANGS)
    # The engine scores each sort chip separately, so the deck is out of
    # 18: twelve items plus the six habits on the sorting slide. The cover
    # chip has to match what the results slide prints, or the learner
    # arrives at a score out of a number the cover never mentioned.
    print('wrote %s — %d slides, %d scored points, %d bytes'
          % (OUT, s.count('<section class="slide'),
             len(ALL) + len(SORT_ITEMS), len(s)))


if __name__ == '__main__':
    build()
