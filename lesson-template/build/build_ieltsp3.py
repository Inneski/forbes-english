# -*- coding: utf-8 -*-
"""IELTS Speaking Part 3 — the discussion (C1), built as a 16:9 deck.

The second of the two lessons `ielts-speaking.html` had been promising from a
disabled card. There was no source page to rebuild: the hero copy on the route
said "Part 3 is the abstract discussion and it needs the other two working
before it is worth attempting. It is next in the route," and behind that
sentence was nothing at all. This is the lesson it was promising.

It teaches the three moves that make Part 3 a different test from Part 1,
rather than the same test with harder topics:

  1. **The person changes.** Part 1 asks about your kitchen; Part 3 asks why
     fewer people cook. An answer that is still about you has answered the
     wrong question, however fluent it is.
  2. **The examiner is trained to disagree**, whatever you say — so pushback
     is the task rather than a verdict, and the skill is conceding what is
     fair while keeping the rest.
  3. **Certainty is graded once, on purpose.** Hedging is Lexical Resource,
     not filler; hedging every clause reads as evasion and leaves no position
     on the table at all.

Six pictures, one per section, none shared with Part 1 &amp; 2: the room from a
wider angle for the cover, a window onto a skyline for the move from the
personal to the general, two chairs set at an angle for the pushback, an
unmarked dial for degrees of certainty, five doors for the question run, and
the room with a clock for the activation stage. The palette derives from the
hero and lands close to the route's existing one, which is what keeps the two
decks reading as one course while sharing no image.

Spanish and German both ship complete. Note for whoever picks up the route:
`forbes-english-ielts-speaking-part1-2.html` is hand-written HTML with no
builder anywhere in the repo, and it still carries `es:{}` — English and German
only, against the standing minimum. It is recorded in docs/HANDOFF.md.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ielts_langs import LANGS
from ieltsp3_data import GENERAL, PUSHBACK, HEDGE, ALL, ORDER, ORDER_WHY
import i18n_ieltsp3 as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-speaking-part3.html'
F = 'ielts-speaking-part3'

# python3 lesson-template/extract-palette.py ielts-speaking-part3/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0a0f0e;
  --surface       : #141d1a;
  --surface2      : #1c2925;
  --border        : #a06851;
  --text          : #f5f3f2;
  --text-dim      : #bfaba3;
  --accent        : #e09677;
  --accent-bright : #f0c2ae;
  --accent-dim    : #c66035;
  --secondary     : #151e1b;
  --contrast      : #1dedc6;''' % F

# The target language, and the chips on the activation stage. English in every
# gloss: these are the phrases the learner has to produce in the room.
CHIPS = ['tend to', 'on the whole', 'by and large', 'a case in point',
         'true up to a point', 'it is often argued', 'broadly speaking',
         'on reflection']

# One picture per section (HOUSE-STYLE §5b), and its own for the activation
# stage. bg05 — five closed doors with one ajar — sits behind the ordering
# task because that slide is the one where the learner picks the way in.
BG_GENERAL, BG_PUSH, BG_HEDGE, BG_ORDER = ('bg02.jpg', 'bg03.jpg',
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
    D.assert_no_key_is_longest(ALL, 'IELTSP3')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']),
                 ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])])

        + D.teach('t1Eyebrow', E['t1Eyebrow'], 't1Title', E['t1Title'],
                  [card('t1a'), card('t1b'), card('t1c')],
                  folder=F, bg=BG_GENERAL)

        + "".join(D.mc(i + 1, len(GENERAL), q, 'mcaEyebrow', E['mcaEyebrow'],
                       'mcaTitle', E['mcaTitle'], folder=F, bg=BG_GENERAL,
                       ctx=q.get('ctx'))
                  for i, q in enumerate(GENERAL))

        + D.teach('t2Eyebrow', E['t2Eyebrow'], 't2Title', E['t2Title'],
                  [card('t2a'), card('t2b'), card('t2c')],
                  folder=F, bg=BG_PUSH)

        + "".join(D.mc(i + 1, len(PUSHBACK), q, 'mcbEyebrow', E['mcbEyebrow'],
                       'mcbTitle', E['mcbTitle'], folder=F, bg=BG_PUSH,
                       ctx=q.get('ctx'))
                  for i, q in enumerate(PUSHBACK))

        + D.teach('t3Eyebrow', E['t3Eyebrow'], 't3Title', E['t3Title'],
                  [card('t3a'), card('t3b'), card('t3c')],
                  folder=F, bg=BG_HEDGE)

        + "".join(D.mc(i + 1, len(HEDGE), q, 'mccEyebrow', E['mccEyebrow'],
                       'mccTitle', E['mccTitle'], folder=F, bg=BG_HEDGE,
                       ctx=q.get('ctx'))
                  for i, q in enumerate(HEDGE))

        + D.order(ORDER, 'ordEyebrow', E['ordEyebrow'],
                  'ordTitle', E['ordTitle'],
                  'ordHint', E['ordHint'],
                  'orderWhy', folder=F, bg=BG_ORDER)

        + D.results('resNext', 'You can spot it. Now use it &rarr;', folder=F)

        + D.activate(E['actTitle'], E['actUse'], CHIPS,
                     'Discussion &middot; in pairs',
                     E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'],
                     E['actPlaceholder'],
                     folder=F, bg=BG_ACT)
    )
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Speaking Part 3: The Discussion (C1) | Forbes English',
                   I, langs=LANGS)
    print('wrote %s — %d slides, %d questions, %d bytes'
          % (OUT, s.count('<section class="slide'), len(ALL) + 1, len(s)))


if __name__ == '__main__':
    build()
