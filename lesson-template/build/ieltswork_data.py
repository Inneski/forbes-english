# -*- coding: utf-8 -*-
"""IELTS Vocabulary: Work, Automation and Cities — the twelve items and the sort.

The second topic bank on the IELTS Vocabulary route. The first deck, Lexical
Resource, ends by teaching a method: build the bank BY IDEA, so that each
idea arrives with two or three collocations and an argument already attached.
This deck is that method carried out on the three topics that between them
carry the most Part 3 questions and the most Task 2 prompts — work,
automation, cities.

So the unit here is never a word. Every item tests one of two things:

  1. **the pairing** — the verb or adjective the noun happens to take
     (`take on staff`, `suffer burnout`, `productivity gains`, `invest in`),
     against three near-misses a learner builds one word at a time from a
     dictionary;
  2. **the precise word** — the plain pairing English uses, against a rarer
     word that reaches past it (`augment career trajectories`, `a protracted
     transit`) or a real word that is precise about something else
     (`work safety`, `evict`, `dislocate`).

Three sections, four items each, one idea per picture. Keys sit at `i % 4`
across all twelve. **Every distractor was checked for the reading that makes
it right**: `low-cost housing`, `urban expansion`, `mechanise a process` and
`bring on staff` were all first drafts and all defensible English, so none of
them is here. Nothing reuses a sentence from a teach card — see
`check-teach-leak.js`; the cards NAME the pairings, emphasised, which that
gate exempts, and the item sentences are different sentences.
"""

# ── Activity 1 · work ──────────────────────────────────────────────────
WORK = [
    dict(stem='Which sentence uses the pairing English has for working away '
              'from the office?',
         options=['Half the team now works remotely three days a week.',
                  'Half the team now works distantly three days a week.',
                  'Half the team now works at distance three days a week.',
                  'Half the team now works from distance three days a week.'],
         correct=0, why='v1why'),

    dict(ctx='A candidate wants to say that a job is unlikely to disappear.',
         stem='Which sentence says it precisely?',
         options=['The post gives its holder work safety for years to come.',
                  'The post gives its holder job security for years to come.',
                  'The post gives its holder job assurance for years to come.',
                  'The post gives its holder career insurance for years to come.'],
         correct=1, why='v2why'),

    dict(stem='Nurses on double shifts are exhausted. Which sentence uses '
              'the pairing for it?',
         options=['Many of them get into burnout by the second winter.',
                  'Many of them fall in burnout by the second winter.',
                  'Many of them suffer burnout by the second winter.',
                  'Many of them make a burnout by the second winter.'],
         correct=2, why='v3why'),

    dict(ctx='Part 3: <em>Will people change jobs more often in the '
             'future?</em>',
         stem='Which answer uses the bank precisely?',
         options=["Yes &mdash; the gig economy will augment people's career trajectories.",
                  "Yes &mdash; the gig economy will enlarge people's career futures.",
                  "Yes &mdash; the gig economy will amplify people's career chances.",
                  "Yes &mdash; the gig economy will improve people's career prospects."],
         correct=3, why='v4why'),
]

# ── Activity 2 · automation ────────────────────────────────────────────
AUTOMATION = [
    dict(ctx='A candidate wants to say that machines have pushed workers out '
             'of their jobs.',
         stem='Which verb is the precise one?',
         options=['Automation has displaced thousands of factory workers.',
                  'Automation has dislocated thousands of factory workers.',
                  'Automation has misplaced thousands of factory workers.',
                  'Automation has evicted thousands of factory workers.'],
         correct=0, why='v5why'),

    dict(stem='Which pairing does English use for the benefit a new machine '
              'brings?',
         options=['The report predicts large productivity profits from the new line.',
                  'The report predicts large productivity gains from the new line.',
                  'The report predicts large productivity growths from the new line.',
                  'The report predicts large productivity winnings from the new line.'],
         correct=1, why='v6why'),

    dict(stem='The plant is closing. Which sentence uses the pairing for what '
              'should happen to its workers?',
         options=['The council should re-form the workforce for the new trades.',
                  'The council should re-teach the workforce for the new trades.',
                  'The council should retrain the workforce for the new trades.',
                  'The council should re-school the workforce for the new trades.'],
         correct=2, why='v7why'),

    dict(ctx='Part 3: <em>Should the state support people whose jobs are '
             'automated?</em>',
         stem='Which answer names the policy precisely?',
         options=['Some argue for a universal basic wage given to every adult.',
                  'Some argue for a universal basic salary given to every adult.',
                  'Some argue for a universal basic payment given to every adult.',
                  'Some argue for a universal basic income given to every adult.'],
         correct=3, why='v8why'),
]

# ── Activity 3 · cities ────────────────────────────────────────────────
CITIES = [
    dict(stem='Which is the English pairing for a city spreading outwards '
              'into the countryside?',
         options=['Urban sprawl has swallowed three villages since 1990.',
                  'Urban spread has swallowed three villages since 1990.',
                  'Urban stretch has swallowed three villages since 1990.',
                  'Urban widening has swallowed three villages since 1990.'],
         correct=0, why='v9why'),

    dict(ctx='Task 2: <em>Should governments control rents in large '
             'cities?</em>',
         stem='Which sentence uses the policy term precisely?',
         options=['Cities need more economical housing near the centre.',
                  'Cities need more affordable housing near the centre.',
                  'Cities need more cheap-priced housing near the centre.',
                  'Cities need more reasonable housing near the centre.'],
         correct=1, why='v10why'),

    dict(stem='Which sentence has the pairing right?',
         options=['The mayor promised to invest on infrastructure before the vote.',
                  'The mayor promised to invest for infrastructure before the vote.',
                  'The mayor promised to invest in infrastructure before the vote.',
                  'The mayor promised to invest into infrastructure before the vote.'],
         correct=2, why='v11why'),

    dict(stem='Which sentence says how far the journey to work is, the way '
              'English says it?',
         options=['Most residents face a protracted transit every morning.',
                  'Most residents face a prolonged journeying every morning.',
                  'Most residents face an extended travelling every morning.',
                  'Most residents face a long commute every morning.'],
         correct=3, why='v12why'),
]

ALL = WORK + AUTOMATION + CITIES

# ── The sorting task ───────────────────────────────────────────────────
# Six pairings, two columns. The three on the right are not random errors:
# they are what a learner produces when the phrase was learnt as a word plus
# a translation — a verb from the dictionary, an adjective from their own
# language, a suffix that looks like it should work.
SORT_BINS = ['English says this', 'English does not']
SORT_ITEMS = [
    ('ease congestion', 0),
    ('take on staff', 0),
    ('the gig economy', 0),
    ('make a commute', 1),
    ('strong traffic', 1),
    ('automatise tasks', 1),
]

# A UI_I18N key, not a sentence, so the explanation translates with the deck.
SORT_WHY = 'sortWhy'
