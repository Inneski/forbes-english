# -*- coding: utf-8 -*-
"""IELTS Listening Section 4 — the lecture, as a 16:9 deck.

The hardest section, and hard for a reason candidates usually misdiagnose. Not
the vocabulary and not the speed: **there is no break**. Sections 1 to 3 pause
halfway so you can read the next questions; Section 4 runs straight through,
one speaker, no second voice to interrupt and repeat. Lose your place and there
is nothing to grab hold of.

So the lesson teaches the only thing that helps — reading every question before
pressing play, and then navigating on the lecturer's own signposts rather than
on meaning. The four traps in the script are the four that this end of the
paper really uses: a term defined in passing, a number corrected inside one
sentence, a figure quoted and then qualified, and a twenty-second aside with no
answers in it, placed exactly where a tiring candidate starts writing down
whatever they hear.

Six note-completion gaps across two slides, then four questions on the
argument. A British male lecturer — the fourth distinct voice across the four
sections, so a learner working the route in order has met a spread rather than
the same speaker four times.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ieltslisten_s4_data import (TURNS, AUDIO, NOTES, NOTES_BANK,
                                 NOTES_SLIDES)

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-listening-s4.html'
F = 'ielts-listen-s4'

# python3 lesson-template/extract-palette.py ielts-listen-s4/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0d0c0a;
  --surface       : #1a1814;
  --surface2      : #26231d;
  --border        : #ac7462;
  --text          : #f5f3f2;
  --text-dim      : #bfaaa3;
  --accent        : #e4a490;
  --accent-bright : #f1c0b1;
  --accent-dim    : #cc6a4c;
  --secondary     : #98b9ba;
  --contrast      : #1dedba;''' % F

CHIPS = ['read every question first', 'first &middot; second &middot; finally',
         'the technical term is', 'a corrected number wins',
         'a qualified figure loses', 'an aside still counts']

BG_BRIEF, BG_AUDIO, BG_NOTES, BG_DETAIL = ('bg02.jpg', 'bg03.jpg',
                                           'bg04.jpg', 'bg05.jpg')
BG_ACT = 'bg06.jpg'


# Each note's explanation goes out as an i18n key, n1why..n10why, so it
# translates; the English is registered from NOTES by i18n_ieltslisten_s4.
WHY_KEY = {r[0]: 'n%dwhy' % (i + 1) for i, r in enumerate(NOTES)}


def keyed(rows):
    return [(s, a, WHY_KEY[s]) for s, a, _ in rows]


def build(make_audio=False):
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
    label = 'Section 4 &middot; %d:%02d' % (secs // 60, secs % 60)

    slides = (
        D.cover(logo, 'Section 4 &mdash; <em>the lecture</em>',
                'One speaker, one long run, and the only section with no '
                'break in the middle',
                [('Level', 'C1'),
                 ('Focus', 'Listening &middot; Section 4'),
                 ('Count', '10 questions')])

        + D.teach('t1Eyebrow', 'Before you listen',
                  't1Title',
                  'It is hard for one reason, and it is not the vocabulary',
                  [('t1ah', 'There is no pause', 't1ab',
                    'Sections 1 to 3 stop halfway so you can read the next '
                    'questions. Section 4 runs straight through. One speaker, '
                    'no second voice to interrupt and repeat &mdash; so if you '
                    'lose your place there is nothing to grab hold of.',
                    't1an',
                    'Read all the questions before you press play. There will '
                    'be no moment later in which to do it.'),
                   ('t1bh', 'Follow the signposts, not the sentences', 't1bb',
                    '<em>First</em> &middot; <em>the second factor</em> '
                    '&middot; <em>the third function</em> &middot; '
                    '<em>finally</em>. A lecturer tells you where you are '
                    'roughly once a minute, and those words are the only '
                    'handholds in a long run of continuous speech.', 't1bn',
                    'If you have drifted, stop trying to catch up on meaning '
                    'and wait for the next signpost. It is coming.'),
                   ('t1ch', 'The word limit is the marker', 't1cb',
                    'Note completion takes the words from the recording, so '
                    'the answer is rarely hard to hear. What loses the mark is '
                    'writing three words where two were allowed, or adding a '
                    'word the gap already has beside it.', 't1cn',
                    'Read what is printed either side of the gap. Half the '
                    'over-long answers repeat a word that was already there.')],
                  folder=F, bg=BG_BRIEF)

        + D.audio('audEyebrow', 'The recording',
                  'audTitle', 'You will hear it once, straight through',
                  'audNote',
                  'Part of a lecture on the role of trees in cities, with no '
                  'break in the middle. Read all ten questions on the next '
                  'slides first, then press play &mdash; here, or in the bar at '
                  'the foot of any question slide. It keeps playing while you '
                  'answer.',
                  AUDIO, label, folder=F, bg=BG_AUDIO)

        + "".join(D.gap(n + 1, len(NOTES_SLIDES), keyed(rows), NOTES_BANK,
                        'notesEyebrow',
                        'Questions 1&ndash;10 &middot; Complete the notes',
                        'notesTitle',
                        'Write ONE WORD AND/OR A NUMBER in each gap',
                        folder=F, bg=BG_NOTES,
                        hint_key='notesHint',
                        hint='Every answer is said aloud, in order. Two come '
                             'with a second number beside them, and only one '
                             'of each pair counts.',
                        width=210, size=19)
                  for n, rows in enumerate(NOTES_SLIDES))

        + D.teach('t2Eyebrow', 'After the recording',
                  't2Title', 'The four places a lecture takes its marks',
                  [('t2ah', 'The term defined in passing', 't2ab',
                    '<em>The technical term is interception loss</em> &mdash; '
                    'and then an explanation. When a lecturer says <em>the '
                    'technical term is</em> or <em>that is</em>, a markable '
                    'word has just gone past.', 't2an',
                    'The definition is help, not the answer. The answer is '
                    'usually the term itself.'),
                   ('t2bh', 'The number that is corrected', 't2bb',
                    'Eight hundred pounds, then <em>no, I should be '
                    'accurate</em>, then twelve hundred. The Section 1 '
                    'correction trap, arriving at Section 4 speed where there '
                    'is no second speaker to confirm it.', 't2bn',
                    'And two degrees is the answer while four is quoted and '
                    'then called "an upper bound" &mdash; a figure that gets '
                    'qualified is not the figure they want.'),
                   ('t2ch', 'The aside that still counts', 't2cb',
                    'Twenty seconds about roots and pavements, which the '
                    'lecturer flags as a digression. It is off the main '
                    'argument &mdash; and it still holds an answer, Question '
                    '6.', 't2cn',
                    '<em>An aside</em> &middot; <em>somebody always asks</em> '
                    '&middot; <em>that&rsquo;s a different lecture</em>. A '
                    'digression is a change of subject, not a rest.')],
                  folder=F, bg=BG_DETAIL)

        + D.results('resNext', 'You stayed with it. Now give one &rarr;',
                    folder=F)

        + D.activate('Give the three-minute lecture', 'Use at least three:',
                     CHIPS, 'Discussion &middot; in pairs',
                     'In pairs. Take something you know well and talk for '
                     'three minutes without stopping, with three numbered '
                     'points. Your partner takes notes and is not allowed to '
                     'ask anything. Then compare their notes with what you '
                     'meant to say.',
                     ['Speaker: signpost every point out loud &mdash; '
                      '<em>first</em>, <em>the second reason</em>, '
                      '<em>finally</em>. Count them as you go.',
                      'Correct one number halfway through, the way a real '
                      'lecturer does, and see whether it reaches the notes.',
                      'Take one twenty-second digression and announce it as '
                      'one. Your partner notes its one point, in three words '
                      'or fewer.'],
                     'Writing &middot; 120&ndash;180 words',
                     'Write the notes a listener should have ended up with: '
                     'your three points, the numbers, and the one term you '
                     'defined. Set a word limit at the top &mdash; ONE WORD '
                     'AND/OR A NUMBER is the strictest the test uses &mdash; and '
                     'keep every line inside it.',
                     'Point 1: … / cooled by: …',
                     folder=F, bg=BG_ACT)
    )

    import i18n_ieltslisten_s4 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Listening Section 4: The Lecture | Forbes English',
                   I, langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d scored points, %d:%02d of audio, %d bytes'
          % (OUT, s.count('<section class="slide'),
             sum(r[0].count('______') for r in NOTES),
             secs // 60, secs % 60, len(s)))


if __name__ == '__main__':
    build(make_audio='--audio' in sys.argv)
