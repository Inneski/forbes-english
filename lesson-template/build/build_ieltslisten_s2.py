# -*- coding: utf-8 -*-
"""IELTS Listening Section 2 — the monologue and the map, as a 16:9 deck.

The second of the five Listening lessons. Section 1 was a conversation; this is
one speaker talking to a group, and the two things that change both make it
harder: nobody asks a clarifying question, so nothing is ever repeated for
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
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ieltslisten_s2_data import (TURNS, AUDIO, PLACES, PLACES_WHY,
                                 NOTES, NOTES_BANK, MC)

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

CHIPS = ['fix the entrance first', 'on your left', 'behind = across',
         'beyond = past it', 'two things, one landmark', 'a repeat is a flag']

BG_BRIEF, BG_AUDIO, BG_MAP, BG_DETAIL = ('bg02.jpg', 'bg03.jpg',
                                         'bg04.jpg', 'bg05.jpg')
BG_ACT = 'bg06.jpg'


# Each note's explanation goes out as an i18n key, n1why..n3why, so it
# translates; the English is registered from NOTES by i18n_ieltslisten_s2.
KEYED = [(s, a, 'n%dwhy' % (i + 1)) for i, (s, a, _) in enumerate(NOTES)]
NOTE_SLIDES = [KEYED[:2], KEYED[2:]]


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
        D.cover(logo, 'Section 2 &mdash; <em>the monologue and the map</em>',
                'One speaker, nobody to ask, and a plan you have to hold in '
                'your head',
                [('Level', 'B2&ndash;C1'),
                 ('Focus', 'Listening &middot; Section 2'),
                 ('Count', '12 questions')])

        + D.teach('t1Eyebrow', 'Before you listen',
                  't1Title', 'One voice, and no second chance at anything',
                  [('t1ah', 'Nobody asks a question', 't1ab',
                    'In Section 1 the other speaker keeps checking &mdash; '
                    '<em>sorry, forty-two?</em> &mdash; and every check is a '
                    'free repeat. A monologue never does that. A detail you '
                    'miss is simply gone.', 't1an',
                    'Which is why the preparation time matters more here than '
                    'anywhere else on the paper.'),
                   ('t1bh', 'The map task is not about English', 't1bb',
                    'Labelling a plan tests whether you can hold an '
                    'orientation while somebody walks you through a space in '
                    'words. The vocabulary is small; the difficulty is that '
                    'everything is relative to something else.', 't1bn',
                    'In the real paper you get a drawn plan with letters on '
                    'it. Here the places and positions are matched instead '
                    '&mdash; the same work, one step before the letters.'),
                   ('t1ch', 'Fix your starting point first', 't1cb',
                    '<em>On your left as you come through the gate</em> means '
                    'nothing until you know where the gate is and which way '
                    'you are facing. Find the entrance on the plan before the '
                    'recording starts, and mark which way is "ahead".',
                    't1cn',
                    'Half the marks on a map task are lost by candidates who '
                    'never established where they were standing.')],
                  folder=F, bg=BG_BRIEF)

        + D.audio('audEyebrow', 'The recording',
                  'audTitle', 'You will hear it once',
                  'audNote',
                  'A guide talking to a group of visitors at a public garden. '
                  'Read the questions on the next slides first, then press '
                  'play &mdash; here, or in the bar at the foot of any question '
                  'slide. The recording keeps playing while you answer, and you '
                  'hear it once.',
                  AUDIO, label, folder=F, bg=BG_AUDIO)

        + D.match(PLACES, 'matchEyebrow',
                  'Questions 1&ndash;5 &middot; The layout',
                  'matchTitle', 'Put each place where the guide put it',
                  'matchHint',
                  'Click a place, then its position. Everything is given '
                  'relative to something else.',
                  'placesWhy', folder=F, bg=BG_MAP)

        # Two slides, two notes and one. All three on one slide fit in
        # English and ran 12px off the canvas in Spanish once the
        # explanations translated: three two-line explanations and the hint
        # leave no room for the Check button. HOUSE-STYLE §6.
        + "".join(D.gap(n + 1, len(NOTE_SLIDES), rows, NOTES_BANK,
                        'notesEyebrow',
                        'Questions 6&ndash;8 &middot; Complete the notes',
                        'notesTitle',
                        'Write ONE WORD AND/OR A NUMBER in each gap',
                        folder=F, bg=BG_MAP,
                        hint_key='notesHint',
                        hint='Two numbers arrive in the same sentence more '
                             'than once. Write the one the gap asks for.',
                        width=210, size=19)
                  for n, rows in enumerate(NOTE_SLIDES))

        + "".join(D.mc(i + 1, len(MC), q, 'mcEyebrow',
                       'Questions 9&ndash;12 &middot; Detail', 'mcTitle',
                       'What exactly did the guide say?',
                       folder=F, bg=BG_DETAIL, ctx=q.get('ctx'))
                  for i, q in enumerate(MC))

        + D.teach('t2Eyebrow', 'After the recording',
                  't2Title', 'How a map task hides its answers',
                  [('t2ah', 'The shared landmark', 't2ab',
                    'Two things are put beside the same feature &mdash; the '
                    'play area <em>and</em> the bicycle racks are both next to '
                    'the car park. Naming the landmark does not identify '
                    'either of them, so the sentence has to be held whole.',
                    't2an',
                    'Whenever a speaker says <em>two things</em> or <em>in '
                    'fact</em>, a second item is about to share a position.'),
                   ('t2bh', 'The thing that moved', 't2bb',
                    'Something is described in its old place and then '
                    'corrected to its new one. The plant stall "used to stand '
                    'by the lake". Anyone answering from the first mention '
                    'puts it in the wrong place.', 't2bn',
                    'The guide repeats the new position deliberately. A repeat in a '
                    'monologue is never decoration.'),
                   ('t2ch', 'The direction that depends on you', 't2cb',
                    '<em>On your left</em>, <em>directly ahead</em>, '
                    '<em>behind the lake</em>, <em>on the far side from where '
                    'we are standing</em>. Every one of these is relative to '
                    'the speaker&rsquo;s position, not to the page.', 't2cn',
                    '<em>Behind</em> and <em>beyond</em> are the two that '
                    'catch people: behind the lake is across it, beyond the '
                    'greenhouse is past it.')],
                  folder=F, bg=BG_DETAIL)

        + D.results('resNext', 'You held the plan. Now draw one &rarr;',
                    folder=F)

        + D.activate('Give the tour', 'Use at least three:', CHIPS,
                     'Discussion &middot; in pairs',
                     'In pairs, with a simple plan each &mdash; draw the room '
                     'you are in, or a building you both know. One of you '
                     'describes where five things are, without pointing and '
                     'without naming a compass direction. The other marks '
                     'them on their own copy and then compares.',
                     ['Describer: fix the starting point out loud first. "You '
                      'come in through the door on the north side." Then '
                      'everything is relative to that.',
                      'Put two of your five things beside the same landmark, '
                      'and see whether your partner separates them.',
                      'Move one thing halfway through: "the printer used to '
                      'be by the window &mdash; it is now&hellip;" Say the '
                      'new place twice, as a real guide does.'],
                     'Writing &middot; 100&ndash;150 words',
                     'Write the opening ninety seconds of a tour of somewhere '
                     'you know well, describing where five things are. Use no '
                     'compass directions at all &mdash; only positions '
                     'relative to the entrance and to each other &mdash; and '
                     'put two of them beside the same landmark.',
                     'As you come through the main door, on your left…',
                     folder=F, bg=BG_ACT)
    )

    import i18n_ieltslisten_s2 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Listening Section 2: The Monologue and the Map | Forbes English',
                   I, langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d scored points, %d:%02d of audio, %d bytes'
          % (OUT, s.count('<section class="slide'),
             len(PLACES) + sum(r[0].count('______') for r in NOTES) + len(MC),
             secs // 60, secs % 60, len(s)))


if __name__ == '__main__':
    build(make_audio='--audio' in sys.argv)
