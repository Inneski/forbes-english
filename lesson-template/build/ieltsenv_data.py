# -*- coding: utf-8 -*-
"""IELTS Vocabulary: Environment and Energy — the twelve items and the sort.

The first topic bank on the IELTS Vocabulary route, and the method the Lexical
Resource deck ends by teaching: a bank built BY IDEA rather than alphabetically,
each idea arriving with two or three collocations and the argument it is
usually attached to in Speaking Part 3 and Writing Task 2. The hub card on
`ielts-vocabulary.html` fixed the three ideas: emissions, renewables,
consumption and waste.

Three sections, four items each, and every item tests one of two things:

  1. **the pairing** — which verb or adjective the noun actually takes
     (*cut* emissions, *generate* electricity, *phase out* coal, *sent to*
     landfill, *cut down on*), against three pairings English does not use;
  2. **the precise word** — the plain right word against near-misses that
     sound close (*intermittent* against interrupted / infrequent /
     intermediate; *footprint* against step / trace / fingerprint).

One item per section asks the learner to name the ARGUMENT a Part 3 answer is
making — who pays, subsidy against the market, producer over individual — so
that the bank is filed the way the previous deck said to file it.

**Every distractor was checked for the reading that makes it right.** `phase
down coal` was a distractor and it is real English (the COP26 wording), so it
was replaced; `reduce emissions` and `produce electricity` are both fine and
are kept out of the option lists altogether. `inconsistent supply` was
defensible and became `intermediate`, which merely sounds close.

Keys sit at `i % 4` across all twelve. Nothing here reuses a sentence from a
teach card — see `check-teach-leak.js`.
"""

# ── Activity 1 · emissions ─────────────────────────────────────────────
EMISSIONS = [
    dict(stem='Which verb does English pair with <em>emissions</em>?',
         options=['Cut emissions by a third before 2035.',
                  'Lower down emissions by a third before 2035.',
                  'Descend emissions by a third before 2035.',
                  'Shrink off emissions by a third before 2035.'],
         correct=0, why='v1why'),

    dict(stem='Every flight, every car journey, every steak adds to a '
              'person\'s what?',
         options=['Their carbon step.',
                  'Their carbon footprint.',
                  'Their carbon trace.',
                  'Their carbon fingerprint.'],
         correct=1, why='v2why'),

    dict(ctx='A Part 3 answer: <em>The people who breathe the worst air are '
             'rarely the people who made it.</em>',
         stem='Which argument is this candidate making?',
         options=['That targets are more useful than enforcement.',
                  'That air quality has improved since the tax came in.',
                  'That the cost falls on those who did not cause it.',
                  'That greenhouse gases are a problem for governments.'],
         correct=2, why='v3why'),

    dict(stem='A government charges firms for every tonne of CO&#8322; they '
              'release. What is the charge called?',
         options=['A carbon fine.',
                  'A smoke tariff.',
                  'An emissions toll.',
                  'A carbon tax.'],
         correct=3, why='v4why'),
]

# ── Activity 2 · renewables ────────────────────────────────────────────
RENEWABLES = [
    dict(stem='Which pairing is the natural English one?',
         options=['Generate electricity from wind.',
                  'Fabricate electricity from wind.',
                  'Originate electricity from wind.',
                  'Manufacture electricity from wind.'],
         correct=0, why='v5why'),

    dict(stem='Solar gives nothing at night and wind gives nothing in still '
              'weather. What kind of supply is that?',
         options=['An interrupted supply.',
                  'An intermittent supply.',
                  'An infrequent supply.',
                  'An intermediate supply.'],
         correct=1, why='v6why'),

    dict(stem='A country stops using coal in stages over twenty years. Which '
              'verb?',
         options=['Fade out coal by 2045.',
                  'Phase off coal by 2045.',
                  'Phase out coal by 2045.',
                  'Phase away coal by 2045.'],
         correct=2, why='v7why'),

    dict(ctx='A Part 3 answer: <em>Without public money no turbine would have '
             'gone up; with it, the industry never learns to stand alone.</em>',
         stem='Which argument is the candidate weighing?',
         options=['Reliability against cost.',
                  'Energy security against imports.',
                  'Targets against enforcement.',
                  'Subsidy against the market.'],
         correct=3, why='v8why'),
]

# ── Activity 3 · consumption and waste ─────────────────────────────────
WASTE = [
    dict(stem='Where does rubbish that is not recycled go, in the phrase '
              'English uses?',
         options=['It is sent to landfill.',
                  'It is sent to the dumping.',
                  'It is sent to the burial ground.',
                  'It is sent to earth-fill.'],
         correct=0, why='v9why'),

    dict(stem='A bottle designed to be binned after one drink is made of '
              'what?',
         options=['One-time plastic.',
                  'Single-use plastic.',
                  'Disposable-only plastic.',
                  'Once-only plastic.'],
         correct=1, why='v10why'),

    dict(stem='Which sentence uses a phrasal verb English actually has?',
         options=['Shoppers could cut off on packaging.',
                  'Shoppers could cut away on packaging.',
                  'Shoppers could cut down on packaging.',
                  'Shoppers could cut back off packaging.'],
         correct=2, why='v11why'),

    dict(ctx='A Part 3 answer: <em>Telling shoppers to carry a bag changes '
             'nothing while the supermarket wraps every cucumber.</em>',
         stem='Which argument is this?',
         options=['Convenience against the cost of going without.',
                  'Recycling rates against landfill capacity.',
                  'A deposit scheme against a packaging tax.',
                  'Producer over individual responsibility.'],
         correct=3, why='v12why'),
]

ALL = EMISSIONS + RENEWABLES + WASTE

# ── The sorting task ───────────────────────────────────────────────────
# Six pairings, two ideas. The filing is the point: each one lands next to
# the argument it serves, which is what a bank built by idea is for.
SORT_BINS = ['Emissions and energy', 'Consumption and waste']
SORT_ITEMS = [
    ('burn fossil fuels', 0),
    ('phase out coal', 0),
    ('a carbon footprint', 0),
    ('send to landfill', 1),
    ('a throwaway culture', 1),
    ('excess packaging', 1),
]

# A UI_I18N key, not the sentence: the explanation translates with the deck.
SORT_WHY = 'sortWhy'
