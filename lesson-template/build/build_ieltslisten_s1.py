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

Six pictures, one per section. English, German and Spanish all complete.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ielts_langs import LANGS
from ieltslisten_s1_data import (TURNS, AUDIO, FORM, FORM_SLIDES, FORM_BANK, MC)

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
         'take the correction', 'two prices, one label', 'spelling is marked']

BG_BRIEF, BG_AUDIO, BG_TRAPS, BG_DETAIL = ('bg02.jpg', 'bg03.jpg',
                                           'bg04.jpg', 'bg05.jpg')
BG_ACT = 'bg06.jpg'


# Each form row's explanation goes out as an i18n key, f1why..f7why, so it
# translates; the English is registered from FORM by i18n_ieltslisten_s1.
WHY_KEY = {r[0]: 'f%dwhy' % (i + 1) for i, r in enumerate(FORM)}


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
        D.cover(logo, 'Section 1 &mdash; <em>the everyday conversation</em>',
                'Two speakers, one form to fill in, and a recording that plays '
                'exactly once',
                [('Level', 'B2&ndash;C1'),
                 ('Focus', 'Listening &middot; Section 1'),
                 ('Count', '10 questions')])

        + D.teach('t1Eyebrow', 'Before you listen',
                  't1Title',
                  'The easiest section, and the one people throw marks away on',
                  [('t1ah', 'What Section 1 always is', 't1ab',
                    'Two speakers, an everyday situation, and a form or a set '
                    'of notes to complete. Enrolling, booking, reporting '
                    'something lost. It is the gentlest English on the paper.',
                    't1an',
                    'Which is why a lost mark here costs the same as a lost '
                    'mark in the lecture, and hurts more.'),
                   ('t1bh', 'It tests writing, not understanding', 't1bb',
                    'You will understand nearly every word. The marks go on '
                    'whether you can write a spelled surname, a phone number '
                    'and a price down accurately while someone keeps talking.',
                    't1bn',
                    'Spelling counts. A correctly heard word spelt wrong '
                    'scores nothing.'),
                   ('t1ch', 'Read the form first', 't1cb',
                    'You get time before the recording starts. Use it to see '
                    'what KIND of answer each gap wants &mdash; a day, a '
                    'number, a name &mdash; so you are waiting for the right '
                    'thing instead of listening to everything.', 't1cn',
                    'A gap after "£" wants a number. You can know that before '
                    'you hear a word.')],
                  folder=F, bg=BG_BRIEF)

        + D.audio('audEyebrow', 'The recording',
                  'audTitle', 'You will hear it once',
                  'audNote',
                  'A telephone conversation between a woman and the manager of '
                  'a community sports centre. Read the questions on the next '
                  'slides first, then press play &mdash; here, or in the bar '
                  'at the foot of any question slide. The recording keeps '
                  'playing while you answer, and you hear it once.',
                  AUDIO, label, folder=F, bg=BG_AUDIO)

        + "".join(D.gap(n + 1, len(FORM_SLIDES), keyed(rows), FORM_BANK,
                        'gapEyebrow', 'Questions 1&ndash;7 &middot; Complete the form',
                        'gapTitle',
                        'Write ONE WORD AND/OR A NUMBER in each gap',
                        folder=F, bg=BG_AUDIO,
                        hint_key='gapHint',
                        hint='Spelling is marked. Write what you actually '
                             'heard, not what you expected to hear.',
                        width=210, size=19)
                  for n, rows in enumerate(FORM_SLIDES))

        + "".join(D.mc(i + 1, len(MC), q, 'mcEyebrow',
                       'Questions 8&ndash;10 &middot; Detail', 'mcTitle',
                       'What exactly did they say?',
                       folder=F, bg=BG_DETAIL, ctx=q.get('ctx'))
                  for i, q in enumerate(MC))

        + D.teach('t2Eyebrow', 'After the recording',
                  't2Title', 'The four places this section takes its marks',
                  [('t2ah', 'The correction', 't2ab',
                    'A speaker says one thing and immediately changes it '
                    '&mdash; <em>Tuesday&hellip; sorry, that&rsquo;s the children, '
                    'the adult class is Thursday</em>. The answer is always '
                    'the second one. This is the commonest mistake on the '
                    'whole section.', 't2an',
                    'Listen for <em>sorry</em>, <em>actually</em>, <em>I '
                    'mean</em>, <em>I beg your pardon</em>. Every one of them '
                    'is a warning that the answer is about to change.'),
                   ('t2bh', 'The spelled word', 't2bb',
                    'When a speaker starts giving letters, an answer is being '
                    'dictated. In Section 1 it usually happens once, and it '
                    'is never repeated more than the speakers would naturally '
                    'repeat it.', 't2bn',
                    'Know the letters that sound alike in English: A, E and I; '
                    'G and J; M and N.'),
                   ('t2ch', 'The number and the distractor', 't2cb',
                    'British speakers say <em>double oh</em> for two noughts '
                    'and <em>oh</em> for one. And there are nearly always two '
                    'prices or two times &mdash; one of them labelled as the '
                    'wrong one, quickly.', 't2cn',
                    'Thirty-five was the monthly rate for non-members. She was '
                    'joining, so the answer was forty-two.')],
                  folder=F, bg=BG_TRAPS)

        + D.results('resNext', 'You heard it. Now run one &rarr;', folder=F)

        + D.activate('Take the call', 'Use at least three:', CHIPS,
                     'Discussion &middot; in pairs',
                     'In pairs, with a form each. One of you is the '
                     'receptionist at a centre, a hotel or a garage; the other '
                     'is enquiring. The receptionist must spell one name, give '
                     'one phone number, and correct themselves once. The '
                     'caller fills in the form and then reads it back.',
                     ['Speller: give the surname once, at speaking speed. Do '
                      'not slow down and do not repeat it unless you are '
                      'asked.',
                      'Caller: read the whole form back at the end. Every '
                      'wrong letter is a mark, so say the letters, not the '
                      'word.',
                      'Somewhere in the call, change one detail after you have '
                      'already given it. See whether your partner catches it.'],
                     'Writing &middot; 100&ndash;150 words',
                     'Write the six lines of a form for a booking of your own '
                     'choosing &mdash; a course, a delivery, a repair &mdash; '
                     'and beside each one write what KIND of answer it needs: '
                     'a name, a day, a number, a price. That is the thirty '
                     'seconds of preparation the test gives you, done in '
                     'advance.',
                     'Surname: … (a name, spelled)',
                     folder=F, bg=BG_ACT)
    )

    import i18n_ieltslisten_s1 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Listening Section 1: The Everyday Conversation | Forbes English',
                   I, langs=LANGS)
    print('wrote %s — %d slides, %d scored points, %d:%02d of audio, %d bytes'
          % (OUT, s.count('<section class="slide'),
             sum(r[0].count('______') for r in FORM) + len(MC),
             secs // 60, secs % 60, len(s)))


if __name__ == '__main__':
    build(make_audio='--audio' in sys.argv)
