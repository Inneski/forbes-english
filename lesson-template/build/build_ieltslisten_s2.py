# -*- coding: utf-8 -*-
"""IELTS Listening Section 2 — the monologue and the map, as a 16:9 deck.

The second of the five Listening lessons. Section 1 was a conversation; this is
one speaker talking to a group, and the two things that change both make it
harder: nobody asks a clarifying question, so almost nothing is repeated for
free, and the map task arrives.

**The map task is matched here rather than labelled, and that is a deliberate
limit rather than a shortcut.** A real paper hands you a drawn plan with
letters on it. The artwork for this lesson is illustration, not a diagram, so
instead of faking a map the deck tests the same skill in the form it can
honestly support: five places, five positions, matched from the description —
which is precisely the work a candidate does before they ever look at the
letters. The teach card says so in as many words.

The recording carries the three traps a map task really uses: a direction that
depends on where the speaker is standing, a feature described in its old place
and then moved, and two things sharing one landmark so that naming the landmark
identifies neither.

A New Zealand voice, different from Section 1's British-and-Australian pairing
on purpose — the route should give a learner the spread of accents the real
test uses rather than the same two voices five times over.

REVISED 2026-09-25: every English string on the slides is now read from the
i18n module, as in Section 1 (they were written out twice). The review of
2026-09-24 corrected overclaims ("no second chance at anything", "the map task
is not about English", "half the marks", "a repeat is never decoration"), a
multiple-choice distractor that was close to true (the stream path, which the
guide says is closed), a second one that was defensible (anticlockwise from
the main gate, where the group is standing next to the glasshouse), the
"behind = across" chip, and the entry-price note, which printed the "free under
16" that its own explanation called the trap.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ieltslisten_s2_data import (TURNS, AUDIO, PLACES, NOTES, NOTES_BANK, MC)
import i18n_ieltslisten_s2 as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-listening-s2.html'
F = 'ielts-listen-s2'

# python3 lesson-template/extract-palette.py ielts-listen-s2/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0c0d0a;
  --surface       : #181914;
  --surface2      : #22251e;
  --border        : #cd9b7d;
  --text          : #f5f3f2;
  --text-dim      : #bfaea3;
  --accent        : #f5d1bb;
  --accent-bright : #fbbd97;
  --accent-dim    : #e59c6f;
  --secondary     : #98b7ba;
  --contrast      : #1dedd8;''' % F

CHIPS = ['fix the entrance first', 'on your left', 'behind = far side',
         'beyond = past it', 'two things, one landmark', 'a repeat is a flag']

BG_BRIEF, BG_AUDIO, BG_MAP, BG_DETAIL = ('bg02.jpg', 'bg03.jpg',
                                         'bg04.jpg', 'bg05.jpg')
BG_ACT = 'bg06.jpg'


# Each note's explanation goes out as an i18n key, n1why..n3why, so it
# translates; the English is registered from NOTES by i18n_ieltslisten_s2.
KEYED = [(s, a, 'n%dwhy' % (i + 1)) for i, (s, a, _) in enumerate(NOTES)]
NOTE_SLIDES = [KEYED[:2], KEYED[2:]]


# Every English string on the slides is read from the i18n module, so the
# HTML and UI_I18N.en cannot drift apart.
E = I.T['en']


def card(p):
    """The six-item teach card for prefix p ('t1a', 't1b', …), from E."""
    return (p + 'h', E[p + 'h'], p + 'b', E[p + 'b'], p + 'n', E[p + 'n'])


def build(make_audio=False):
    D.assert_no_key_is_longest(MC, 'IELTSLISTEN2')
    logo = D.logo_from(TPL)

    if make_audio:
        import tts
        tts.render(TURNS, os.path.join(F, AUDIO))

    audio_path = os.path.join(F, AUDIO)
    assert os.path.exists(audio_path), (
        '%s is missing. Run this builder once with --audio; a deck whose '
        'recording is absent ships a player that never starts, and '
        'check-lesson.js has no gate for that.' % audio_path)
    import tts
    secs = tts.duration(audio_path)
    label = 'Section 2 &middot; %d:%02d' % (secs // 60, secs % 60)

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

        + D.match(PLACES, 'matchEyebrow', E['matchEyebrow'],
                  'matchTitle', E['matchTitle'],
                  'matchHint', E['matchHint'],
                  'placesWhy', folder=F, bg=BG_MAP)

        # Two slides, two notes and one. All three on one slide fit in
        # English and ran 12px off the canvas in Spanish once the
        # explanations translated: three two-line explanations and the hint
        # leave no room for the Check button. HOUSE-STYLE §6.
        + "".join(D.gap(n + 1, len(NOTE_SLIDES), rows, NOTES_BANK,
                        'notesEyebrow', E['notesEyebrow'],
                        'notesTitle', E['notesTitle'],
                        folder=F, bg=BG_MAP,
                        hint_key='notesHint', hint=E['notesHint'],
                        width=210, size=19)
                  for n, rows in enumerate(NOTE_SLIDES))

        + "".join(D.mc(i + 1, len(MC), q, 'mcEyebrow', E['mcEyebrow'],
                       'mcTitle', E['mcTitle'],
                       folder=F, bg=BG_DETAIL, ctx=q.get('ctx'))
                  for i, q in enumerate(MC))

        + D.teach('t2Eyebrow', E['t2Eyebrow'], 't2Title', E['t2Title'],
                  [card('t2a'), card('t2b'), card('t2c')],
                  folder=F, bg=BG_DETAIL)

        + D.results('resNext', 'You held the plan. Now draw one &rarr;',
                    folder=F)

        + D.activate(E['actTitle'], E['actUse'], CHIPS,
                     'Discussion &middot; in pairs',
                     E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'],
                     E['actPlaceholder'],
                     folder=F, bg=BG_ACT)
    )

    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Listening Section 2: The Monologue and the Map | Forbes English',
                   I, langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d scored points, %d:%02d of audio, %d bytes'
          % (OUT, s.count('<section class="slide'),
             len(PLACES) + sum(r[0].count('______') for r in NOTES) + len(MC),
             secs // 60, secs % 60, len(s)))


if __name__ == '__main__':
    build(make_audio='--audio' in sys.argv)
