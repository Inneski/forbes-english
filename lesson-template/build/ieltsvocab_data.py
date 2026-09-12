# -*- coding: utf-8 -*-
"""IELTS Vocabulary: Lexical Resource — the twelve items and the sort.

Written fresh. `ielts.html` had carried a disabled Vocabulary card with its own
brief on it: "Topic banks that feed Speaking and Task 2 at once, since Lexical
Resource is a quarter of the marks in both. Words you have to use, not words
you have to read."

**The lesson is built against the belief that costs candidates the most here:
that Lexical Resource rewards rare words.** It does not. The public descriptors
ask for *less common* lexis used with *precision* and *flexibility*, and they
penalise inaccuracy explicitly — so a band 6 candidate reaching for
"plethora" and missing costs themselves more than one who writes "a lot of"
and is right. What actually moves the band is collocation, paraphrase and
topic range.

Three sections, four items each:

  1. **Precision** — the descriptor is accuracy, not rarity; a near-miss word
     is worse than a plain one.
  2. **Collocation** — the unit that gets scored is the pairing, not the word.
     "Make research", "do a decision", "heavy traffic" but not "heavy rain
     shower" — the noun chooses the verb and the adjective.
  3. **Paraphrase** — the one skill both Speaking Part 3 and Task 2 pay for,
     and the reason a topic bank is built around ideas rather than words.

**Every distractor was checked for the reading that makes it right.** `v7` is
the one that needed rewriting: the first version asked which sentence showed
"flexibility" and offered a synonym swap against a register shift, and both are
flexibility under the descriptors. It now asks what the examiner does with a
memorised phrase, which has one answer.

Keys sit at `i % 4` across all twelve. Nothing here reuses a sentence from a
teach card — see `check-teach-leak.js`.
"""

# ── Activity 1 · precision beats rarity ────────────────────────────────
PRECISION = [
    dict(stem='What do the Lexical Resource descriptors actually reward?',
         options=['Less common words used accurately and flexibly.',
                  'The largest number of rare words in the answer.',
                  'Vocabulary drawn from academic subject lists.',
                  'Long words in place of short everyday ones.'],
         correct=0, why='v1why'),

    dict(ctx='A candidate writes: <em>The government should ameliorate the '
             'traffic.</em>',
         stem='What has this cost them?',
         options=['Nothing &mdash; a rare verb always raises the band.',
                  'Marks, because the word does not fit the object.',
                  'Marks, but only under Grammatical Range instead.',
                  'Nothing, provided the rest of the essay is plain.'],
         correct=1, why='v2why'),

    dict(stem='Which is the stronger choice in an essay about congestion?',
         options=['A rare noun the writer has not used before.',
                  'A long synonym taken from a thesaurus entry.',
                  'A plain word that is exactly right in context.',
                  'A word repeated from the essay question itself.'],
         correct=2, why='v3why'),

    dict(stem='Why do memorised "band 9 phrases" often lower the score?',
         options=['They are too formal for the Speaking test alone.',
                  'They are banned outright by the marking scheme.',
                  'They take up words the examiner wanted spent.',
                  'They sit apart from the answer and sound learnt.'],
         correct=3, why='v4why'),
]

# ── Activity 2 · the unit is the pairing ───────────────────────────────
COLLOCATION = [
    # "Do research" was one of the distractors here and it is perfectly good
    # English — two defensible answers, which is the defect class this file is
    # written against. The three wrong verbs are now ones English never takes
    # with `research`.
    dict(stem='Which pairing is the natural English one?',
         options=['Conduct research into the causes of congestion.',
                  'Make research into the causes of congestion.',
                  'Take research into the causes of congestion.',
                  'Build research into the causes of congestion.'],
         correct=0, why='v5why'),

    # A different adjective from the one on the teach card, on purpose. The
    # card teaches `heavy` and check-teach-leak.js allows a card to name the
    # collocation it is teaching — but a learner who has just read the card
    # could answer a `heavy` item without thinking. Testing `strong` makes the
    # item about the rule rather than about the card.
    dict(stem='English says <em>strong coffee</em> and <em>strong accent</em>. What does it not say?',
         options=['Strong evidence emerged during the second inquiry.',
                  'Strong rain fell across the county for three days.',
                  'Strong opinions were expressed on both of the sides.',
                  'Strong smells were coming from the kitchen window.'],
         correct=1, why='v6why'),

    dict(stem='Which part of a collocation does a learner usually get wrong?',
         options=['The noun, which is the part that carries meaning.',
                  'The word order, which English fixes very loosely.',
                  'The verb or adjective the noun happens to take.',
                  'The article, which changes with every single noun.'],
         correct=2, why='v7why'),

    dict(stem='How should a new word go into your notebook?',
         options=['On its own in a list, with a translation beside it.',
                  'With its part of speech and nothing else at all.',
                  'With every meaning the dictionary lists for it.',
                  'In a phrase, with the words it normally travels with.'],
         correct=3, why='v8why'),
]

# ── Activity 3 · paraphrase, and the topic bank ────────────────────────
PARAPHRASE = [
    dict(ctx='Question: <em>Some people think museums should be free. Do you '
             'agree?</em>',
         stem='Which opening paraphrases rather than copies?',
         options=['Whether entry to museums should cost anything is disputed.',
                  'Some people think museums should be free, and I agree.',
                  'Museums should be free, some people think. I agree also.',
                  'People think that museums ought to be free. I agree too.'],
         correct=0, why='v9why'),

    dict(stem='Why does paraphrase pay twice in this exam?',
         options=['It is faster to write than an original sentence.',
                  'Speaking Part 3 and Task 2 both score the same skill.',
                  'It lets you reuse the question wording in full.',
                  'Examiners are told to reward any repeated phrasing.'],
         correct=1, why='v10why'),

    dict(stem='A topic bank is most useful when it is organised by what?',
         options=['The alphabet, so that any word is quick to find.',
                  'Difficulty, so the rarest words are studied last.',
                  'Idea, so a word arrives with an argument attached.',
                  'Part of speech, so the grammar is never in doubt.'],
         correct=2, why='v11why'),

    dict(stem='You do not know the word for something in the test. What works?',
         options=['Say the word in your own language and move on.',
                  'Stop and ask the examiner what the word is.',
                  'Use the nearest rare word and hope it lands.',
                  'Describe what the thing does, in plain English.'],
         correct=3, why='v12why'),
]

ALL = PRECISION + COLLOCATION + PARAPHRASE

# ── The sorting task ───────────────────────────────────────────────────
# Six habits, two columns. The point candidates get backwards: the effortful,
# impressive-feeling habits are mostly on the right.
SORT_BINS = ['Raises the band', 'Does nothing, or costs you']
SORT_ITEMS = [
    ('Learning words in the phrases they live in', 0),
    ('Saying exactly what you mean in plain words', 0),
    ('Rewording the question in your own terms', 0),
    ('Memorising a list of impressive phrases', 1),
    ('Swapping in a thesaurus word you have not used', 1),
    ('Repeating the question wording word for word', 1),
]

SORT_WHY = ('Everything on the left is about <strong>using</strong> language; '
            'everything on the right is about <strong>displaying</strong> it. '
            'The descriptors ask whether you can say what you mean, precisely '
            'and flexibly &mdash; so a plain word that lands beats a rare one '
            'that misses, and a phrase learnt whole beats a word learnt alone. '
            'The right-hand column is where most of the revision time goes.')
