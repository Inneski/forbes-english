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
"""

# ── the recording ──────────────────────────────────────────────────────
# ie_m tutor, ca_f student, gb_m2 student. Three accents, two genders — no two
# voices in this recording can be mistaken for one another.
TURNS = [
    ('narrator',
     'Section three. You will hear two students, Maya and Ravi, discussing '
     'their research project with their tutor. First, you have some time to '
     'look at questions one to twelve.'),
    ('narrator', 'Now listen carefully and answer questions one to twelve.'),

    ('ie_m', 'Right, come in, both of you. How is the project going?'),
    ('ca_f', 'Well, we have the design more or less settled. We are looking at '
             'how first-year students use the library after ten at night.'),
    ('ie_m', 'Good topic. And how are you collecting the data?'),
    ('gb_m2', 'A questionnaire. We were going to interview people, but there '
              'are only the two of us.'),
    ('ie_m', 'I would still push you towards interviews, you know. You get the '
             'reasons, not just the numbers.'),
    ('ca_f', 'We did think about it. But with sixty respondents, interviews '
             'would take us the whole term.'),
    ('ie_m', 'Fair enough. Your decision. So, questionnaire it is.'),

    ('ie_m', 'And how big is the sample?'),
    ('ca_f', 'Sixty. Which in principle is fine for this kind of study — '
             'actually, no, I keep saying that and I do not believe it. Sixty '
             'is thin. If a dozen people do not reply we are down to forty-'
             'eight and the whole thing wobbles.'),
    ('gb_m2', 'Exactly, and that is my worry too — the response rate. If we '
              'only get half of them back the sample is meaningless.'),
    ('ca_f', 'That is not quite what I meant. I was worried about how fast '
             'they come back. We have three weeks, and last time people '
             'answered in the final two days.'),
    ('ie_m', 'Two different problems, and you both need to solve them. Ravi is '
             'talking about how many; Maya is talking about how quickly.'),

    ('gb_m2', 'Could we not just extend the deadline?'),
    ('ie_m', 'You could, but then you lose the analysis time. I would rather '
             'you sent one reminder, three days before the close.'),
    ('ca_f', 'A reminder. Yes, that is simple enough.'),
    ('gb_m2', 'And I still think we should pilot it. Ten people, before we '
              'send it to everyone.'),
    ('ca_f', 'I was against that at first, because of the time. But you are '
             'right. Better ten wasted responses than sixty useless ones.'),
    ('ie_m', 'Good. So: pilot with ten, one reminder at three days, and keep '
             'the sample at sixty. Now, the literature review. Maya, you were '
             'reading Harrison?'),
    ('ca_f', 'I was, but honestly I found her chapter on study spaces thin. '
             'It is all American universities.'),
    ('gb_m2', 'I liked it. The framework is useful even if the data is not '
              'ours.'),
    ('ie_m', 'Use the framework, then, and say plainly that the context '
             'differs. That is a strength in a write-up, not a weakness.'),

    ('narrator',
     'That is the end of section three. You now have half a minute to check '
     'your answers.'),
]

AUDIO = 'section3.mp3'

# ── Questions 1-5 · who said it ────────────────────────────────────────
# The whole section in one task. Every one of these is a position somebody
# actually holds by the END of the discussion, which is not the same as what
# they said first.
WHO = [
    ('Sixty is too small a sample', 'Maya, after changing her mind'),
    ('The worry is how MANY reply', 'Ravi'),
    ('The worry is how FAST they reply', 'Maya'),
    ('Interviews would be better than a questionnaire', 'The tutor'),
    ('Harrison&rsquo;s chapter is worth using', 'Ravi'),
]

WHO_WHY = ('Four of these five are stated by someone who is disagreeing with '
           'someone else in the same breath, which is what makes attribution '
           'the skill. Maya says sixty is fine <em>in principle</em> and then '
           'takes it straight back &mdash; her final position is the opposite '
           'of her first. And "response rate" is said by both students about '
           'two different things, which the tutor then separates for you: '
           '"Ravi is talking about how many; Maya is talking about how '
           'quickly."')

# ── Questions 6-8 · the tutorial notes ─────────────────────────────────
DECISIONS = [
    ('Pilot the questionnaire with ______ people first',
     ['10|ten'],
     'Ten. Ravi proposes it and Maya, who was against it, agrees &mdash; so '
     'the decision stands even though the first thing she said about it was '
     'no.'),
    ('Send one reminder ______ days before the close',
     ['3|three'],
     'Three days. The tutor gives the number; the students accept it without '
     'restating it, which is why it has to be caught the first time.'),
    ('Final sample size: ______ respondents',
     ['60|sixty'],
     'Sixty, unchanged. It is questioned at length and then kept &mdash; a '
     'discussion that argues about a number and does not change it is a '
     'standard Section 3 move.'),
]

DECISIONS_BANK = []

# ── Questions 9-12 · multiple choice ───────────────────────────────────
MC = [
    dict(stem='Why did the students choose a questionnaire?',
         options=['There are only two of them to do the interviews.',
                  'Their tutor recommended it over doing interviews.',
                  'Interviews would not have given them the reasons.',
                  'The library would not allow them to interview.'],
         correct=0, why='n1why'),

    dict(stem='What does the tutor say about extending the deadline?',
         options=['It is the simplest way to raise the response rate.',
                  'It would cost them the time they need to analyse.',
                  'It would be unfair on the students who replied.',
                  'It is not permitted this late in the whole term.'],
         correct=1, why='n2why'),

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
