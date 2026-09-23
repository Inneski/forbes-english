# -*- coding: utf-8 -*-
"""IELTS Listening Section 3 — the academic discussion.

Three speakers: two students and a tutor, talking about a piece of work. This
is where most candidates' score falls off, and the reason is not vocabulary.

**The section tests who said what.** Two students agreeing, disagreeing and
half-changing their minds, with a tutor steering. The questions are then keyed
to a person — *what does Ravi think about…* — so an answer heard perfectly and
attributed to the wrong speaker scores nothing.

So the casting matters more here than anywhere else on the route, and it is
deliberate: **three accents that cannot be confused.** An Irish male tutor, a
Canadian female student, a British male student. Three voices of the same age,
gender and accent would make this an aural puzzle rather than a language test,
which is the opposite of what the real paper does.

The traps in the script are the ones this section really uses:

  1. **The concession.** Maya says the sample size is fine "in principle" and
     then takes it back. Her final position is the opposite of her first.
  2. **The agreement that is not one.** Ravi says "exactly" to a point Maya
     did not make, and then states his own.
  3. **The tutor's suggestion versus the students' plan.** The tutor proposes
     interviews; the students settle on a questionnaire. A question about what
     they *decided* is answered by the students, not the tutor.
  4. **A shared word.** Both students say "response rate", about different
     things — one means how many replied, the other how fast.

`WHO` is the attribution task: five opinions, three speakers. `DECISIONS`
completes the tutorial notes. The multiple choice then asks the questions that
depend on holding the thread rather than on catching a single word.

REVISED 2026-09-23 (IELTS audit): the deck now plays the recording while the
learner answers, so the twelve questions run in the order they are heard, in
two halves either side of a reading pause, as the real Section 3 does (the
old order put the first multiple-choice answer in the opening seconds). The
match lost its Harrison item, which belonged to the tutor as much as to Ravi
("use the framework"), and its two identical "Ravi" chips; the project topic
is Question 1. Speakers contract; the narrator does not.
"""

# ── the recording ──────────────────────────────────────────────────────
# ie_m tutor, ca_f student, gb_m2 student. Three accents, two genders — no two
# voices in this recording can be mistaken for one another.
TURNS = [
    ('narrator',
     'Section three. You will hear two students, Maya and Ravi, discussing '
     'their research project with their tutor. First, you have some time to '
     'look at questions one to six.'),
    ('pause', 15),
    ('narrator', 'Now listen carefully and answer questions one to six.'),

    ('ie_m', "Right, come in, both of you. How's the project going?"),
    ('ca_f', "Well, we've got the design more or less settled. We're looking at "
             "how first-year students use the library after ten at night."),
    ('ie_m', 'Good topic. And how are you collecting the data?'),
    ('gb_m2', 'A questionnaire. We were going to interview people, but there '
              'are only the two of us.'),
    ('ie_m', "I'd still push you towards interviews, you know. You get the "
             "reasons, not just the numbers."),
    ('ca_f', 'We did think about it. But with sixty respondents, interviews '
             'would take us the whole term.'),
    ('ie_m', 'Fair enough. Your decision. So, questionnaire it is.'),

    ('ie_m', 'And how big is the sample?'),
    ('ca_f', "Sixty. Which in principle is fine for this kind of study — "
             "actually, no, I keep saying that and I don't believe it. Sixty "
             "is thin. If a dozen people don't reply we're down to forty-eight "
             "and the whole thing wobbles."),
    ('gb_m2', "Exactly, and that's my worry too — the response rate. If we "
              "only get half of them back the sample's meaningless."),
    ('ca_f', "That's not quite what I meant. I was worried about how fast "
             "they come back. We've got three weeks, and last time people "
             "answered in the final two days."),
    ('ie_m', "Two different problems, and you both need to solve them. Ravi's "
             "talking about how many; Maya's talking about how quickly."),

    ('narrator',
     'Before you hear the rest of the discussion, you have some time to look '
     'at questions seven to twelve.'),
    ('pause', 20),
    ('narrator', 'Now listen and answer questions seven to twelve.'),

    ('gb_m2', "Couldn't we just extend the deadline?"),
    ('ie_m', "You could, but then you lose the analysis time. I'd rather you "
             "sent one reminder, three days before the close."),
    ('ca_f', "A reminder. Yes, that's simple enough."),
    ('gb_m2', 'And I still think we should pilot it. Ten people, before we '
              'send it to everyone.'),
    ('ca_f', "I was against that at first, because of the time. But you're "
             "right. Better ten wasted responses than sixty useless ones."),
    ('ie_m', 'Good. So: pilot with ten, one reminder at three days, and keep '
             'the sample at sixty. Now, the literature review. Maya, you were '
             'reading Harrison?'),
    ('ca_f', "I was, but honestly I found her chapter on study spaces thin. "
             "It's all American universities."),
    ('gb_m2', "I liked it. The framework's useful even if the data isn't "
              "ours."),
    ('ie_m', "Use the framework, then, and say plainly that the context "
             "differs. That's a strength in a write-up, not a weakness."),

    ('narrator',
     'That is the end of section three. You now have half a minute to check '
     'your answers.'),
]

AUDIO = 'section3.mp3'

# The deck plays the recording while the learner answers, so the questions
# run in the order they are heard, in two halves either side of the reading
# pause, as the real Section 3 does:
#   1       the project           (gap)
#   2       the method            (MC)
#   3-6     who holds which view  (match)
#   ── pause ──
#   7       the deadline          (MC)
#   8-10    the decisions         (gaps)
#   11-12   the reading           (MC)

# ── Question 1 · the project ───────────────────────────────────────────
TOPIC = [
    ('How first-year students use the library after ______ at night',
     ['10|ten|10pm|10 pm'],
     'Ten, in Maya&rsquo;s first sentence. A Section 3 recording names its '
     'topic in the opening seconds, before anyone disagrees about anything.'),
]
TOPIC_BANK = []

# ── Question 2 · multiple choice ───────────────────────────────────────
MC_A = [
    dict(stem='Why did the students choose a questionnaire?',
         options=['There are only two of them to do the interviews.',
                  'Their tutor recommended it over doing interviews.',
                  'Interviews would not have given them the reasons.',
                  'The library would not allow them to interview.'],
         correct=0, why='n1why'),
]

# ── Questions 3-6 · who holds this view ────────────────────────────────
# Every position is someone's by the END of the first half, which is not the
# same as what they said first. The chips name the move each speaker makes,
# so no two of them read the same: two chips both saying "Ravi" made the
# right answer shake as a miss whenever the learner picked the other one.
WHO = [
    ('Interviews would be better than a questionnaire',
     'The tutor, whose advice is declined'),
    ('Sixty is too small a sample', 'Maya, after changing her mind'),
    ('The worry is how MANY reply', 'Ravi, who thinks he is agreeing'),
    ('The worry is how FAST they reply', 'Maya, correcting Ravi'),
]

WHO_WHY = ('Each person is named with the move they make, because the move is '
           'how you catch the view. The tutor&rsquo;s advice is heard and '
           'declined; Maya calls sixty fine <em>in principle</em> and takes it '
           'straight back; and "response rate" is said by both students about '
           'two different things, which the tutor then separates for you: '
           '"Ravi&rsquo;s talking about how many; Maya&rsquo;s talking about '
           'how quickly."')

# ── Question 7 · multiple choice ───────────────────────────────────────
MC_B = [
    dict(stem='What does the tutor say about extending the deadline?',
         options=['It is the simplest way to raise the response rate.',
                  'It would cost them the time they need to analyse.',
                  'It would be unfair on the students who replied.',
                  'It is not permitted this late in the term.'],
         correct=1, why='n2why'),
]

# ── Questions 8-10 · the tutorial notes ────────────────────────────────
DECISIONS = [
    ('Send one reminder ______ days before the close',
     ['3|three'],
     'Three days. The tutor gives the number and the students never repeat '
     'it &mdash; though the tutor does, once, in the summary at the end.'),
    ('Pilot the questionnaire with ______ people first',
     ['10|ten'],
     'Ten. Ravi proposes it and Maya agrees. She says she was against it at '
     'first, but the answer is where she ends up.'),
    ('Final sample size: ______ respondents',
     ['60|sixty'],
     'Sixty, unchanged. It is questioned at length and then kept &mdash; a '
     'discussion that argues about a number and does not change it is a '
     'standard Section 3 move.'),
]

DECISIONS_BANK = []

# ── Questions 11-12 · multiple choice ──────────────────────────────────
MC_C = [
    dict(stem='What do the students disagree about?',
         options=['Whether the sample of sixty is going to be enough.',
                  'Whether a reminder should be sent to respondents.',
                  'Whether the Harrison chapter is of any use to them.',
                  'Whether the project should be about the library.'],
         correct=2, why='n3why'),

    dict(stem='What does the tutor advise about the American data?',
         options=['Leave Harrison out, since the context is different.',
                  'Find a British study that reaches the same result.',
                  'Treat the difference in context as a real problem.',
                  'Use the framework and say the context is different.'],
         correct=3, why='n4why'),
]

MC = MC_A + MC_B + MC_C
