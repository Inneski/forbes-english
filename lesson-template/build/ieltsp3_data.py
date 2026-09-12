# -*- coding: utf-8 -*-
"""IELTS Speaking Part 3 — the twelve scored items and the ordering task.

Written fresh. There was no source page: `ielts-speaking.html` promised Part 3
in its hero copy ("It is next in the route") and carried a disabled card for
it, and nothing existed behind either.

The items test the three moves that separate Part 3 from Part 1, which is the
only thing that makes it a lesson rather than a topic list:

  1. the answer is about the CATEGORY, not about you;
  2. the examiner's disagreement is an invitation to defend or revise;
  3. certainty is graded on purpose, once, not sprayed across every clause.

**Two right answers is the defect class this file is written against.** The
multi-agent audit of 2026-09-11 found four items across the preposition decks
with a second defensible key, so every distractor here was checked for the
reading that makes it true. The one that needed the most work is `q12`: the
first draft offered "Fluency, because hedges fill the silence while you
think" against the key "Lexical Resource" — and filled silence IS scored under
Fluency and Coherence, so the item had two answers. The distractor now claims
the examiner counts hedges, which no descriptor does.

**Keys sit at `i % 4` across all twelve**, so the printed PDF is not an answer
key with the column already filled in, and `check-lesson.js`'s KEYS gate sees
a uniform spread.

Nothing here reuses a sentence from a teach card — see
`check-teach-leak.js`. The rule travels; the sentence does not.
"""

# ── Activity 1 · from your own life to the general case ────────────────
GENERAL = [
    dict(ctx='Examiner: &ldquo;Do people read as much as they used to?&rdquo;',
         stem='Which opening belongs in Part 3?',
         options=['On the whole they read less, though more of it is on a screen.',
                  'I read two books last month, and both were thrillers.',
                  'No. Reading has finished as a daily habit, completely.',
                  'That is hard to say, and I have never once thought about it.'],
         correct=0, why='q1why'),

    dict(stem='Which phrase turns a personal habit into a general claim?',
         options=['In my own case,', 'By and large,', 'As far as I go,',
                  'Speaking personally,'],
         correct=1, why='q2why'),

    dict(ctx='Examiner: &ldquo;Why do so many people move to cities?&rdquo;',
         stem='Which opening is strongest?',
         options=['My cousin moved to Madrid last year to find work.',
                  'Because cities are better than villages in every way.',
                  'Work, mainly &mdash; the jobs sit in a few large places.',
                  'I have never lived in a city, so I could not tell you.'],
         correct=2, why='q3why'),

    dict(stem='Where does a personal example belong in a Part 3 answer?',
         options=['It stands in place of the general claim entirely.',
                  'It opens the answer, before any general claim.',
                  'It has no place in Part 3 at any point at all.',
                  'It follows the general claim, as one illustration.'],
         correct=3, why='q4why'),
]

# ── Activity 2 · when the examiner pushes back ─────────────────────────
PUSHBACK = [
    dict(ctx='Examiner: &ldquo;But surely that is only true of rich '
             'countries?&rdquo;',
         stem='Which reply keeps the conversation going?',
         options=['That holds where wages are high, though it is spreading.',
                  'No, you are wrong, and I do not accept that at all.',
                  'Yes, you are completely right, so I withdraw my point.',
                  'Sorry, I am afraid I do not understand your question.'],
         correct=0, why='q5why'),

    dict(stem='Which phrase concedes a point and still keeps your position?',
         options=['I disagree with that completely.',
                  'That is true up to a point, though',
                  'Yes, exactly, I agree entirely.',
                  'I am not at all sure what you mean.'],
         correct=1, why='q6why'),

    dict(stem='You change your mind halfway through an answer. Is that a problem?',
         options=['Yes &mdash; it costs marks under Fluency and Coherence.',
                  'Yes &mdash; the examiner writes it down as an error.',
                  'No &mdash; said aloud, it reads as thinking, not as weakness.',
                  'No &mdash; provided you never signal that you have done it.'],
         correct=2, why='q7why'),

    dict(stem='The examiner disagrees with you. What is being tested?',
         options=['Whether your opinion matches the examiner&rsquo;s own view.',
                  'Whether you know the facts of the topic in real detail.',
                  'Whether you will drop any claim as soon as it is pushed.',
                  'Whether you can defend or revise a claim in English.'],
         correct=3, why='q8why'),
]

# ── Activity 3 · saying how sure you are ───────────────────────────────
HEDGE = [
    dict(stem='Which answer commits to a view and then limits it once?',
         options=['Broadly speaking it works, though not for every subject.',
                  'It might possibly perhaps work in some cases, maybe.',
                  'It works. It always works. There is no doubt at all.',
                  'It is arguably possible that it could conceivably work.'],
         correct=0, why='q9why'),

    dict(stem='What does hedging every single clause cost you?',
         options=['Nothing at all &mdash; hedging is rewarded in Part 3.',
                  'The answer stops carrying a position of any kind.',
                  'The examiner has to stop you and ask again.',
                  'The mark moves from Grammar to Lexical Resource.'],
         correct=1, why='q10why'),

    dict(stem='Which phrase puts the claim on other people rather than on you?',
         options=['In my honest opinion,', 'What I believe is that',
                  'It is often argued that', 'I am quite convinced that'],
         correct=2, why='q11why'),

    dict(stem='Which criterion does well-judged hedging feed most directly?',
         options=['Pronunciation, because every hedge carries heavy stress.',
                  'Fluency, because the examiner counts how many you use.',
                  'Grammar, because each hedge is a conditional structure.',
                  'Lexical Resource, because it is precise word choice.'],
         correct=3, why='q12why'),
]

ALL = GENERAL + PUSHBACK + HEDGE

# ── The ordering task ──────────────────────────────────────────────────
# The four moves of a Part 3 answer. The example sits third on purpose: lead
# with it and the examiner hears an anecdote rather than an argument.
ORDER = ['State your position in one sentence',
         'Give the reason behind it',
         'Add one case that illustrates it',
         'Name what the other side gets right']

ORDER_WHY = ('Position, reason, example, concession. The example comes third '
             'because it illustrates a claim that has already been made &mdash; '
             'lead with it and the examiner hears an anecdote rather than an '
             'argument. The concession comes last because it is the move that '
             'survives pushback: you have already named the limit yourself, so '
             'there is nothing left to catch you with.')
