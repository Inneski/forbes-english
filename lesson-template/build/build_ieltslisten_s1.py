# -*- coding: utf-8 -*-
"""IELTS Listening Section 1 — the everyday conversation, as a 16:9 deck.

The first of the five Listening lessons `ielts-listening.html` has been
promising from disabled cards since 2026-09-11. Those cards were blocked on one
thing: a recording. Innes chose synthetic voices on 2026-09-13, so the audio is
now generated from a script the same way every other asset here is generated —
see `tts.py` and `ieltslisten_s1_data.py`. Change the script, re-run this, and
the recording and the answer key move together.

**This is the first deck in the repo to use the audio slide.** The engine has
supported `data-type="audio"` for a while — play once, no scrubbing, and (until
2026-09-23) Continue locked until the recording ended; it now keeps playing
while the learner answers, see `deck.audio` — but nothing had ever authored one, so
`deck.py` had no builder for it and `chrome_i18n.py` had none of the five
player strings. Both were added for this deck, which means every Listening
deck after it gets a translated player for free.

The lesson teaches the four things that actually lose marks in Section 1, and
every one of them is deliberately in the recording:

  1. **the self-correction** — Tuesday, then "sorry, that is the children",
     then Thursday. The commonest error on the section;
  2. **the spelled surname** — given once, letter by letter;
  3. **the British number** — "double oh" for two noughts;
  4. **the distractor price** — thirty-five said first and labelled as the
     rate she is not paying.

Form completion first, with **no word bank** — a real form task gives you
nothing to choose from — then four detail questions.

Six pictures, one per section. Ten languages, all complete.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ielts_langs import LANGS
from ieltslisten_s1_data import (TURNS, AUDIO, FORM, FORM_SLIDES, FORM_BANK, MC)
import i18n_ieltslisten_s1 as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-listening-s1.html'
F = 'ielts-listen-s1'

# python3 lesson-template/extract-palette.py ielts-listen-s1/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0e0c09;
  --surface       : #1c1812;
  --surface2      : #29221a;
  --border        : #a15f4e;
  --text          : #f5f2f2;
  --text-dim      : #bfa9a3;
  --accent        : #e18a74;
  --accent-bright : #f1baac;
  --accent-dim    : #c75032;
  --secondary     : #aeb7b6;
  --contrast      : #1dedb3;''' % F

# The moves, not phrases. This deck's target language is what a candidate says
# to themselves while writing.
CHIPS = ['read the form first', 'wait for the letters', 'double oh = 00',
         'take the correction', 'two prices, one ruled out',
         'spelling is marked']

BG_BRIEF, BG_AUDIO, BG_TRAPS, BG_DETAIL = ('bg02.jpg', 'bg03.jpg',
                                           'bg04.jpg', 'bg05.jpg')
BG_ACT = 'bg06.jpg'


# Each form row's explanation goes out as an i18n key, f1why..f7why, so it
# translates; the English is registered from FORM by i18n_ieltslisten_s1.
WHY_KEY = {r[0]: 'f%dwhy' % (i + 1) for i, r in enumerate(FORM)}


# Every English string on the slides is read from the i18n module, so the
# HTML and UI_I18N.en cannot drift apart. They were written out twice until
# 2026-09-24, and a fix made in one copy would have missed the other.
E = I.T['en']


def card(p):
    """The six-item teach card for prefix p ('t1a', 't1b', …), from E."""
    return (p + 'h', E[p + 'h'], p + 'b', E[p + 'b'], p + 'n', E[p + 'n'])


def keyed(rows):
    return [(s, a, WHY_KEY[s]) for s, a, _ in rows]


def build(make_audio=False):
    D.assert_no_key_is_longest(MC, 'IELTSLISTEN1')
    logo = D.logo_from(TPL)

    if make_audio:
        import tts
        tts.render(TURNS, os.path.join(F, AUDIO))

    audio_path = os.path.join(F, AUDIO)
    assert os.path.exists(audio_path), (
        '%s is missing. Run this builder once with --audio to generate it; a '
        'deck whose recording is absent ships a player that never starts, and '
        'check-lesson.js has no gate for that.' % audio_path)
    import tts
    secs = tts.duration(audio_path)
    label = 'Section 1 &middot; %d:%02d' % (secs // 60, secs % 60)

    slides = (
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']),
                 ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])])

        + D.teach('t1Eyebrow', E['t1Eyebrow'], 't1Title', E['t1Title'],
                  [card('t1a'), card('t1b'), card('t1c')],
                  folder=F, bg=BG_BRIEF)

        + D.audio('audEyebrow', E['audEyebrow'],
                  'audTitle', E['audTitle'],
                  'audNote', E['audNote'],
                  AUDIO, label, folder=F, bg=BG_AUDIO)

        + "".join(D.gap(n + 1, len(FORM_SLIDES), keyed(rows), FORM_BANK,
                        'gapEyebrow', E['gapEyebrow'],
                        'gapTitle', E['gapTitle'],
                        folder=F, bg=BG_AUDIO,
                        hint_key='gapHint', hint=E['gapHint'],
                        width=210, size=19)
                  for n, rows in enumerate(FORM_SLIDES))

        + "".join(D.mc(i + 1, len(MC), q, 'mcEyebrow', E['mcEyebrow'],
                       'mcTitle', E['mcTitle'],
                       folder=F, bg=BG_DETAIL, ctx=q.get('ctx'))
                  for i, q in enumerate(MC))

        + D.teach('t2Eyebrow', E['t2Eyebrow'], 't2Title', E['t2Title'],
                  [card('t2a'), card('t2b'), card('t2c')],
                  folder=F, bg=BG_TRAPS)

        + D.results('resNext', 'You heard it. Now run one &rarr;', folder=F)

        + D.activate(E['actTitle'], E['actUse'], CHIPS,
                     'Discussion &middot; in pairs',
                     E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'],
                     E['actPlaceholder'],
                     folder=F, bg=BG_ACT)
    )
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Listening Section 1: The Everyday Conversation | Forbes English',
                   I, langs=LANGS)
    print('wrote %s — %d slides, %d scored points, %d:%02d of audio, %d bytes'
          % (OUT, s.count('<section class="slide'),
             sum(r[0].count('______') for r in FORM) + len(MC),
             secs // 60, secs % 60, len(s)))


if __name__ == '__main__':
    build(make_audio='--audio' in sys.argv)
