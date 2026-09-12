# -*- coding: utf-8 -*-
"""IELTS Pronunciation & fluency — the twelve scored items and the sorting task.

Written fresh; `ielts-speaking.html` carried a disabled card for it and nothing
behind that card. The route's own copy makes the case for the lesson: "A
quarter of the marks sits on pronunciation and most candidates never practise
it deliberately."

The deck is built on the one distinction candidates get wrong about this
criterion — that it is **not** about sounding British, American or anything
else. The public band descriptors score intelligibility, the features that
carry meaning (stress, grouping, intonation) and the strain on the listener.
An accent costs nothing. A sentence with every word stressed equally costs
plenty, because the listener cannot tell which word the speaker meant.

Three sections, four items each:

  1. **Stress** — where the beat falls, and what moves when it moves.
  2. **Chunking** — speech arrives in groups, and the group boundary is where
     the meaning is; the same words in different groups say different things.
  3. **Pausing** — the difference between a pause that reads as thinking and
     one that reads as stalling, and why filling it with "erm" is worse than
     leaving it silent.

**Checked for a second defensible key on every distractor.** `q7` needed the
most work: an early draft offered "Pause before the word you want to
highlight" against "Pause at the end of a thought group", and a pause before a
focus word is a real and taught technique — two answers. The distractor now
claims a pause belongs after every individual word, which nothing teaches.

Keys sit at `i % 4` across all twelve. Nothing here reuses a sentence from a
teach card: the rule travels, the sentence does not (`check-teach-leak.js`).
"""

# ── Activity 1 · where the beat falls ──────────────────────────────────
STRESS = [
    dict(stem='What does English sentence stress actually mark?',
         options=['The words that carry the meaning of the sentence.',
                  'Every word of more than one syllable in the line.',
                  'The last word before the speaker takes a breath.',
                  'The words the speaker has the most trouble saying.'],
         correct=0, why='p1why'),

    dict(ctx='&ldquo;I didn&rsquo;t say she stole the money.&rdquo;',
         stem='Stressing <em>she</em> rather than <em>stole</em> changes what?',
         options=['Nothing at all &mdash; the words are the same either way.',
                  'Which part of the claim is being denied by the speaker.',
                  'The grammar, because stress can shift the tense marking.',
                  'The politeness, since a stressed pronoun sounds ruder.'],
         correct=1, why='p2why'),

    dict(stem='A candidate stresses every word equally. What does it cost?',
         options=['Nothing, provided each individual word is clear.',
                  'Marks under Grammar, as the structure is flattened.',
                  'The listener cannot tell which word was the point.',
                  'Marks under Fluency, because equal stress is slower.'],
         correct=2, why='p3why'),

    dict(stem='Which pair of words changes stress when the part of speech changes?',
         options=['<em>Answer</em> and <em>answer</em>, noun and then verb.',
                  '<em>Open</em> and <em>open</em>, adjective and then verb.',
                  '<em>Travel</em> and <em>travel</em>, noun and then verb.',
                  '<em>Record</em> and <em>record</em>, noun and then verb.'],
         correct=3, why='p4why'),
]

# ── Activity 2 · speech arrives in groups ──────────────────────────────
CHUNK = [
    dict(stem='What is a thought group?',
         options=['A short run of words said as one unit of meaning.',
                  'Any four or five words, counted out as you speak.',
                  'The words between one breath and the next one taken.',
                  'A clause that has both a subject and a main verb.'],
         correct=0, why='p5why'),

    dict(ctx='&ldquo;My brother who lives in Rome is a chef.&rdquo;',
         stem='What do the group boundaries decide here?',
         options=['How formal the sentence sounds to the examiner.',
                  'Whether the speaker has one brother or several.',
                  'Whether the sentence is a statement or a question.',
                  'Which of the two nouns is heard as the subject.'],
         correct=1, why='p6why'),

    dict(stem='Where does a pause belong in connected speech?',
         options=['Before any word longer than three syllables.',
                  'After every single word, to keep each one clear.',
                  'At the end of a thought group, not inside one.',
                  'Only where the written sentence has a comma.'],
         correct=2, why='p7why'),

    dict(stem='Long turn, no pauses at all, all two minutes. How does that read?',
         options=['As fluency, and it is the strongest possible answer.',
                  'As accuracy, since no pause means no hesitation.',
                  'As confidence, which the examiner rewards directly.',
                  'As a rehearsed script, which the examiner listens for.'],
         correct=3, why='p8why'),
]

# ── Activity 3 · the pause, and what fills it ──────────────────────────
PAUSE = [
    dict(stem='Which pause reads as thinking rather than as stalling?',
         options=['A short silence taken between two thought groups.',
                  'A long <em>errrm</em> held in the middle of a phrase.',
                  'A silence that arrives halfway through a long noun.',
                  'A repeated first word, said three or four times over.'],
         correct=0, why='p9why'),

    dict(stem='You cannot find a word. What is the best repair?',
         options=['Stop the answer and ask the examiner for the word.',
                  'Say what the thing does, and keep the turn moving.',
                  'Use the word from your own language and carry on.',
                  'Go back and start the whole sentence again from zero.'],
         correct=1, why='p10why'),

    dict(stem='Does a strong first-language accent lower the Pronunciation band?',
         options=['Yes &mdash; the band is built around a native speaker model.',
                  'Yes &mdash; but only above band seven does the accent count.',
                  'No &mdash; what is scored is how easily you are followed.',
                  'No &mdash; pronunciation is only ever scored in Part 2.'],
         correct=2, why='p11why'),

    dict(stem='Which habit costs the most marks under this criterion?',
         options=['An accent the examiner can place immediately.',
                  'Occasional silence while you choose the next word.',
                  'Slower speech than a first-language speaker uses.',
                  'Mispronouncing the words the answer is built on.'],
         correct=3, why='p12why'),
]

ALL = STRESS + CHUNK + PAUSE

# ── The sorting task ───────────────────────────────────────────────────
# Two bins. The point is the one candidates get backwards: an accent is free,
# a flat or mis-placed stress pattern is not.
SORT_BINS = ['Costs you marks', 'Costs you nothing']
SORT_ITEMS = [
    ('Stressing every word in the sentence equally', 0),
    ('Pausing in the middle of a noun phrase', 0),
    ('Mispronouncing the key word of your answer', 0),
    ('An accent the examiner can place at once', 1),
    ('A short silence between two thought groups', 1),
    ('Speaking more slowly than a native speaker', 1),
]

SORT_WHY = ('The left column is about whether the listener can follow you; the '
            'right column is about whether you sound like someone else. Only '
            'the first is scored. A candidate who works on the accent and '
            'leaves the stress flat has spent the practice on the column that '
            'carries no marks.')
