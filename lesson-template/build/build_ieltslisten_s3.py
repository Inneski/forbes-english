# -*- coding: utf-8 -*-
"""IELTS Listening Section 3 — the academic discussion, as a 16:9 deck.

Where most candidates' Listening score falls off, and not because of
vocabulary. Section 3 is three speakers, and **the section tests who said
what**: the questions are keyed to a person, so an answer heard perfectly and
attributed to the wrong student scores nothing.

Which makes the casting part of the pedagogy rather than decoration. Three
accents that cannot be confused — an Irish tutor, a Canadian student, a
British student — because three voices of the same age, gender and accent
would turn this into an aural puzzle instead of a language test, which is the
opposite of what the real paper does.

The script carries the four moves this section actually uses:

  1. **the concession** — Maya says sixty is fine "in principle" and takes it
     straight back, so her final position is the opposite of her first;
  2. **the agreement that is not one** — Ravi says "exactly" to a point Maya
     never made, and she corrects him;
  3. **suggested against decided** — the tutor pushes interviews and the
     students keep the questionnaire;
  4. **the shared term** — both students say "response rate" about two
     different things, and the tutor separates them out loud.

Attribution first (five positions, three speakers), then the tutorial notes,
then the questions that need the whole thread rather than one caught word.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ieltslisten_s3_data import (TURNS, AUDIO, TOPIC, TOPIC_BANK, MC_A, WHO,
                                 WHO_WHY, MC_B, DECISIONS, DECISIONS_BANK,
                                 MC_C, MC)

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-listening-s3.html'
F = 'ielts-listen-s3'

# python3 lesson-template/extract-palette.py ielts-listen-s3/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0d0d0a;
  --surface       : #191a13;
  --surface2      : #25261c;
  --border        : #ae7762;
  --text          : #f5f3f2;
  --text-dim      : #bfaba3;
  --accent        : #e5a891;
  --accent-bright : #f0b29b;
  --accent-dim    : #ce704c;
  --secondary     : #93afb5;
  --contrast      : #1dedc2;''' % F

CHIPS = ['write the names down', 'where they end up', 'suggested &ne; decided',
         'exactly = check it', 'one phrase, two meanings', 'the number can survive']

BG_BRIEF, BG_AUDIO, BG_WHO, BG_DETAIL = ('bg02.jpg', 'bg03.jpg',
                                         'bg04.jpg', 'bg05.jpg')
def one(html):
    """A lone multiple-choice slide: drop the "1 / 1" counter from its eyebrow."""
    return html.replace(' &middot; 1 / 1</div>', '</div>')


BG_ACT = 'bg06.jpg'


def build(make_audio=False):
    D.assert_no_key_is_longest(MC, 'IELTSLISTEN3')
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
    label = 'Section 3 &middot; %d:%02d' % (secs // 60, secs % 60)

    slides = (
        D.cover(logo, 'Section 3 &mdash; <em>the academic discussion</em>',
                'Three speakers, two of whom change their minds, and every '
                'question keyed to a person',
                [('Level', 'C1'),
                 ('Focus', 'Listening &middot; Section 3'),
                 ('Count', '12 questions')])

        + D.teach('t1Eyebrow', 'Before you listen',
                  't1Title',
                  'The section is not about the topic. It is about who said it.',
                  [('t1ah', 'Three voices, and the questions name them', 't1ab',
                    'Two students and a tutor discussing a piece of work. The '
                    'questions ask what <em>Ravi</em> thinks, what they '
                    '<em>decided</em>, what the <em>tutor</em> suggested. An '
                    'answer heard perfectly and given to the wrong speaker '
                    'scores nothing.', 't1an',
                    'Write the names down in the preparation time. Then you '
                    'are tracking people, not sentences.'),
                   ('t1bh', 'Positions move', 't1bb',
                    'This is a discussion, so somebody will argue themselves '
                    'out of the view they opened with. What is marked is where '
                    'they <strong>end up</strong>, not the first thing they '
                    'said.', 't1bn',
                    '<em>Actually, no</em> &middot; <em>I was against that at '
                    'first</em> &middot; <em>but you&rsquo;re right</em>. Every one '
                    'of them says a position just changed.'),
                   ('t1ch', 'Suggested is not decided', 't1cb',
                    'A tutor proposes things the students do not do. Both go '
                    'in the recording and only one is the answer, so a '
                    'question about the <em>plan</em> is answered by the '
                    'students and a question about the <em>advice</em> by the '
                    'tutor.', 't1cn',
                    '<em>I&rsquo;d still push you towards&hellip; Fair enough, '
                    'your decision.</em> That is a suggestion being declined, '
                    'in two lines.')],
                  folder=F, bg=BG_BRIEF)

        + D.audio('audEyebrow', 'The recording',
                  'audTitle', 'You will hear it once',
                  'audNote',
                  'Two students, Maya and Ravi, discussing a research project '
                  'with their tutor. Three voices. Read the questions on the '
                  'next slides first, then press play &mdash; here, or in the '
                  'bar at the foot of any question slide. The recording keeps '
                  'playing while you answer, and you hear it once.',
                  AUDIO, label, folder=F, bg=BG_AUDIO)

        + one(D.gap(1, 1, TOPIC, TOPIC_BANK,
                'topicEyebrow', 'Question 1 &middot; The project',
                'notesTitle', 'Write ONE WORD AND/OR A NUMBER in each gap',
                folder=F, bg=BG_WHO,
                hint_key='topicHint',
                hint='It is given in the first few seconds, before anyone '
                     'disagrees about anything.',
                width=210, size=19))

        + one(D.mc(1, 1, MC_A[0], 'mcaEyebrow',
                   'Question 2 &middot; The method', 'mcTitle',
                   'What happened in the discussion?',
                   folder=F, bg=BG_WHO))

        + D.match(WHO, 'whoEyebrow',
                  'Questions 3&ndash;6 &middot; Who holds this view?',
                  'whoTitle',
                  'Match each position to the person who ends up holding it',
                  'whoHint',
                  'Click a position, then a person. What counts is where each '
                  'speaker finishes, not where they started.',
                  WHO_WHY, folder=F, bg=BG_WHO)

        + one(D.mc(1, 1, MC_B[0], 'mcbEyebrow',
                   'Question 7 &middot; The deadline', 'mcTitle',
                   'What happened in the discussion?',
                   folder=F, bg=BG_DETAIL))

        + one(D.gap(1, 1, DECISIONS, DECISIONS_BANK,
                'notesEyebrow',
                'Questions 8&ndash;10 &middot; The tutorial notes',
                'notesTitle', 'Write ONE WORD AND/OR A NUMBER in each gap',
                folder=F, bg=BG_DETAIL,
                hint_key='notesHint',
                hint='All three numbers are agreed out loud. One of them is '
                     'argued about at length and then kept unchanged.',
                width=210, size=19))

        + "".join(D.mc(i + 1, len(MC_C), q, 'mcEyebrow',
                       'Questions 11&ndash;12 &middot; The reading', 'mcTitle',
                       'What happened in the discussion?',
                       folder=F, bg=BG_DETAIL, ctx=q.get('ctx'))
                  for i, q in enumerate(MC_C))

        + D.teach('t2Eyebrow', 'After the recording',
                  't2Title', 'Three ways a discussion hides the answer',
                  [('t2ah', 'The agreement that is not one', 't2ab',
                    'Ravi says <em>exactly</em> &mdash; and then states '
                    'something Maya did not say. She corrects him: <em>that&rsquo;s '
                    'not quite what I meant</em>. Agreement words are not '
                    'evidence that two people agree.', 't2an',
                    'The tutor then separates them explicitly, which is the '
                    'recording handing you the answer if you are still '
                    'listening.'),
                   ('t2bh', 'The shared term', 't2bb',
                    'Both students say <em>response rate</em>. Ravi means how '
                    'many people reply; Maya means how quickly. One phrase, '
                    'two meanings, two different answers keyed to two '
                    'different people.', 't2bn',
                    'When a phrase is repeated by a second speaker, check they '
                    'are using it for the same thing.'),
                   ('t2ch', 'The number that survives the argument', 't2cb',
                    'Sixty is questioned, defended, doubted and kept. A '
                    'discussion that argues about a figure and then leaves it '
                    'alone is standard, and the length of the argument is not '
                    'a signal that the figure changed.', 't2cn',
                    'What changed was the plan around it: a pilot, and a '
                    'reminder.')],
                  folder=F, bg=BG_DETAIL)

        + D.results('resNext', 'You followed it. Now run one &rarr;', folder=F)

        + D.activate('Hold the thread', 'Use at least three:', CHIPS,
                     'Discussion &middot; in pairs',
                     'In threes: two of you argue a decision out &mdash; '
                     'where to hold an event, what to spend a budget on '
                     '&mdash; and one takes notes. Each arguer must change '
                     'their mind exactly once, out loud.',
                     ['Arguers: signal the change when you make it. '
                      '<em>Actually, no&hellip;</em> or <em>I was against that '
                      'at first, but&hellip;</em>',
                      'Use one phrase for two different things on purpose, and '
                      'see whether the note-taker separates them.',
                      'Note-taker: read your notes back naming who holds what. '
                      'Every wrong attribution is a lost mark.'],
                     'Writing &middot; 120&ndash;180 words',
                     'Write the minutes of a three-person meeting: what '
                     'was suggested, what was decided, and who ended up '
                     'holding which view. One person must be recorded as '
                     'having changed position, and one suggestion as '
                     'declined.',
                     'Suggested: … Decided: … Maya now holds that …',
                     folder=F, bg=BG_ACT)
    )

    import i18n_ieltslisten_s3 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Listening Section 3: The Academic Discussion | Forbes English',
                   I, langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d scored points, %d:%02d of audio, %d bytes'
          % (OUT, s.count('<section class="slide'),
             len(TOPIC) + len(WHO) + len(DECISIONS) + len(MC),
             secs // 60, secs % 60, len(s)))


if __name__ == '__main__':
    build(make_audio='--audio' in sys.argv)
