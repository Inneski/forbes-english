# -*- coding: utf-8 -*-
"""IELTS Reading: Matching Headings (C1), built as a 16:9 deck.

The second Reading lesson on the route, after True / False / Not Given. The
hub card on `ielts-reading.html` set the brief: "The type that does not run
in passage order, so the technique is different: read for what the paragraph
is doing rather than what it is about, and leave the headings that fit two
paragraphs until last." The deck is those three clauses in order:

  1. THE SHAPE OF THE TASK — more headings than paragraphs, the one type
     that jumps, and the trap of reading the list before the paragraph.
  2. FUNCTION OVER TOPIC — a heading names what the paragraph is DOING; the
     topic sentence moves around; a repeated word is bait.
  3. ORDER OF ATTACK — sure ones first, cross it out once used, a heading
     that fits two paragraphs goes last and is decided by elimination.

Twelve items in three activities, four options each — every option a
heading, so they are all short and the length gate had to be satisfied by
lengthening distractors word by word. A sort of six SIGNALS closes the
scored part: three marks of the heading that fits the whole paragraph
against the three ways a decoy looks right.

Six pictures, one per idea. A long row of numbered mailboxes under an empty
sky is the list of headings waiting for paragraphs; an empty frame on a wall
with the picture leaning below it is function against topic — the frame is
what the paragraph does, the picture is what it is about; a box of index
cards knocked over is the passage with no order to lean on; a jigsaw with
one gap and two nearly identical pieces is the heading that fits twice; and
a single coat on a long row of hooks closes it on the activation stage.

Ten languages, all complete (`ielts_langs.LANGS`).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ielts_langs import LANGS
from ieltshead_data import (MAIN, FUNCTION, ATTACK, ALL,
                            SORT_BINS, SORT_ITEMS, SORT_WHY)
import i18n_ieltshead as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-reading-headings.html'
F = 'ielts-reading-headings'

# python3 lesson-template/extract-palette.py ielts-reading-headings/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #090e09;
  --surface       : #121c12;
  --surface2      : #1a281a;
  --border        : #d4a77f;
  --text          : #f5f3f2;
  --text-dim      : #bfb0a3;
  --accent        : #f8dbc1;
  --accent-bright : #d2c6c6;
  --accent-dim    : #ebab73;
  --secondary     : #9db6b3;
  --contrast      : #1dedeb;''' % F

# The target language of this deck is a set of moves, not a set of phrases —
# which is why the chips read as instructions. English in every gloss: they are
# what the learner says to themselves in the exam room.
CHIPS = ['function, not topic', 'a detail is not a heading', 'sure ones first',
         'two-fit goes last', 'cross it out', 'too general fails']

BG_SHAPE, BG_FUNCTION, BG_ORDER, BG_TWOFIT = ('bg02.jpg', 'bg03.jpg',
                                              'bg04.jpg', 'bg05.jpg')

# A passage paragraph, a stem and four headings fit the canvas at rest, but
# once a learner answers, the explanation and the "Answer:" line push the
# slide 23-24px past the bottom edge (measured 2026-09-23, every language).
# check-lesson only measures slides unanswered, so it never saw it. Two
# options a row buys back two rows.
def two_up(html):
    return html.replace('<div class="opts">', '<div class="opts two-up">')


BG_ACT = 'bg06.jpg'

# Every English string on the slides is read from the i18n module, so the
# HTML and UI_I18N.en cannot drift apart. Until 2026-09-24 they were written
# out twice, and a correction to one copy would have missed the other.
E = I.T['en']


def card(p):
    """The six-item teach card for prefix p ('t1a', 't1b', …), from E."""
    return (p + 'h', E[p + 'h'], p + 'b', E[p + 'b'], p + 'n', E[p + 'n'])


def build():
    D.assert_no_key_is_longest(ALL, 'IELTSHEAD')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']),
                 ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])])

        + D.teach('t1Eyebrow', E['t1Eyebrow'], 't1Title', E['t1Title'],
                  [card('t1a'), card('t1b'), card('t1c')],
                  folder=F, bg=BG_SHAPE)

        + "".join(two_up(D.mc(i + 1, len(MAIN), q, 'mcaEyebrow', E['mcaEyebrow'],
                              'mcaTitle', E['mcaTitle'],
                              folder=F, bg=BG_SHAPE, ctx=q.get('ctx')))
                  for i, q in enumerate(MAIN))

        + D.teach('t2Eyebrow', E['t2Eyebrow'], 't2Title', E['t2Title'],
                  [card('t2a'), card('t2b'), card('t2c')],
                  folder=F, bg=BG_FUNCTION)

        + "".join(two_up(D.mc(i + 1, len(FUNCTION), q, 'mcbEyebrow',
                              E['mcbEyebrow'], 'mcbTitle', E['mcbTitle'],
                              folder=F, bg=BG_FUNCTION, ctx=q.get('ctx')))
                  for i, q in enumerate(FUNCTION))

        + D.teach('t3Eyebrow', E['t3Eyebrow'], 't3Title', E['t3Title'],
                  [card('t3a'), card('t3b'), card('t3c')],
                  folder=F, bg=BG_ORDER)

        + "".join(D.mc(i + 1, len(ATTACK), q, 'mccEyebrow', E['mccEyebrow'],
                       'mccTitle', E['mccTitle'],
                       folder=F, bg=BG_TWOFIT, ctx=q.get('ctx'))
                  for i, q in enumerate(ATTACK))

        # The explanation goes through its i18n key so it translates with
        # the rest of the slide; SORT_WHY in the data module is the English
        # of that key, kept there so the data file reads whole.
        + D.sort_slide(SORT_BINS, SORT_ITEMS,
                       'sortEyebrow', E['sortEyebrow'],
                       'sortTitle', E['sortTitle'],
                       'sortHint', E['sortHint'],
                       'sortWhy', folder=F, bg=BG_TWOFIT,
                       bin_keys=['sortBin1', 'sortBin2'])

        + D.results('resNext', 'You can match them. Now write them &rarr;',
                    folder=F)

        + D.activate(E['actTitle'], E['actUse'], CHIPS,
                     'Discussion &middot; in pairs',
                     E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'],
                     E['actPlaceholder'],
                     folder=F, bg=BG_ACT)
    )
    assert I.T['en']['sortWhy'] == SORT_WHY, 'sortWhy drifted from SORT_WHY'
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Reading: Matching Headings (C1) | Forbes English',
                   I, langs=LANGS)
    # Twelve items plus the six signals on the sorting slide: the engine scores
    # a sort per chip, so the cover chip has to say 18, not 13.
    print('wrote %s — %d slides, %d scored points, %d bytes'
          % (OUT, s.count('<section class="slide'),
             len(ALL) + len(SORT_ITEMS), len(s)))


if __name__ == '__main__':
    build()
