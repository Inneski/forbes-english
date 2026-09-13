# -*- coding: utf-8 -*-
"""IELTS Reading: Matching Headings — the twelve items and the sort.

The hub card on `ielts-reading.html` names the lesson: "The type that does
not run in passage order, so the technique is different: read for what the
paragraph is doing rather than what it is about, and leave the headings that
fit two paragraphs until last." Three activities, one per clause:

  1. MAIN IDEA — a short paragraph in `ctx`, four headings. The key covers
     the whole paragraph; the distractors name a detail the paragraph
     mentions, the topic of a neighbouring idea, or something so general it
     would fit any paragraph in the passage.
  2. FUNCTION — the same shape, but the key names what the paragraph is
     DOING (illustrating, defending, warning, comparing) and the distractors
     quote a detail, repeat a word from the text, or are too general.
  3. ORDER OF ATTACK — two strategy questions and two elimination cases,
     where a heading fits two paragraphs and the learner has to decide which
     paragraph it really covers.

**Every option is a heading, so they are all short, and the length gate bites
hard.** A heading three words longer than its neighbours is a tell a learner
can scan for. The distractors were lengthened, never the key shortened, until
`assert_no_key_is_longest` passed on all twelve.

**The key cycles `i % 4`** across the twelve, so it lands on each position
three times and the spread carries no information.

**Every distractor is wrong for a reason the deck teaches.** A heading that
fits only the first sentence, a heading built from a word in the paragraph, a
heading that would fit the passage rather than the paragraph — each one is a
named trap on a teach card, so a wrong answer can be explained by the rule
rather than by "read more carefully".
"""

# ── Activity 1 · the main idea ─────────────────────────────────────────
MAIN = [
    dict(ctx='<em>Coral reefs cover less than one per cent of the ocean '
             'floor, yet they shelter roughly a quarter of all marine '
             'species. Fish breed among the branches, and small crabs hide '
             'from predators in the crevices. Remove the reef and the fish '
             'do not simply move elsewhere; most of them disappear.</em>',
         stem='Which heading states the main idea?',
         options=['Reefs support far more life than their size suggests',
                  'Where small crabs hide from predators on a reef',
                  'The share of the ocean floor that coral reefs cover',
                  'The oceans of the world and the creatures living in them'],
         correct=0, why='r1why'),

    dict(ctx='<em>The town&rsquo;s first railway station opened in 1846 and '
             'was demolished within thirty years. Its replacement, built on '
             'the same site, still stands. Passengers today walk over the '
             'foundations of the original without knowing it.</em>',
         stem='Which heading states the main idea?',
         options=['The passengers who use the station every day',
                  'A station built where an earlier one had stood',
                  'Why the first station was pulled down',
                  'Railway building in the nineteenth century'],
         correct=1, why='r2why'),

    dict(ctx='<em>Early printed books were designed to look exactly like '
             'manuscripts. Printers copied the handwriting of scribes, left '
             'space for illuminated capitals, and even sold some copies as '
             'if they had been written by hand. It took two generations '
             'before a printed page dared to look printed.</em>',
         stem='Which heading states the main idea?',
         options=['How scribes decorated their capital letters',
                  'The history of printing in Europe',
                  'Printing spent its first years in disguise',
                  'Books that were sold as handwritten copies'],
         correct=2, why='r3why'),

    dict(ctx='<em>The city banned cars from its central streets in 1998. '
             'Shopkeepers predicted ruin, and for a year takings did fall. '
             'Then footfall rose, rents rose with it, and the shops that had '
             'complained loudest found themselves unable to afford the '
             'pedestrianised streets they had opposed.</em>',
         stem='Which heading states the main idea?',
         options=['The year cars were removed from the centre',
                  'How the shopkeepers reacted to the ban at first',
                  'Traffic policy in modern cities',
                  'A ban that succeeded too well for its opponents'],
         correct=3, why='r4why'),
]

# ── Activity 2 · what the paragraph is doing ───────────────────────────
FUNCTION = [
    dict(ctx='<em>Consider the humble shipping container. Before 1956 a '
             'cargo ship might sit in port for a week while dockers handled '
             'every sack and barrel by hand. The container cut that to a '
             'day, and it did so without a single new engine or a faster '
             'hull.</em>',
         stem='What is this paragraph doing?',
         options=['An example of a simple change with large effects',
                  'Why a cargo ship once spent a whole week in port',
                  'The engine and hull of a modern cargo ship',
                  'The history of world trade since the Second World War'],
         correct=0, why='r5why'),

    dict(ctx='<em>None of this means the scheme should be abandoned. The '
             'early results are weak, but early results usually are, and '
             'the cost of stopping now would be borne by the very families '
             'the scheme was designed to help. The sensible course is to '
             'give it another two years.</em>',
         stem='What is this paragraph doing?',
         options=['The families who took part in the scheme',
                  'A case for keeping the scheme running',
                  'Why the early results were so weak',
                  'Government policy and its results'],
         correct=1, why='r6why'),

    dict(ctx='<em>A word of caution before the figures are read too '
             'eagerly. The survey reached only households with a landline, '
             'which in 2023 means older and wealthier ones. Whatever it says '
             'about the population as a whole, it says it about a '
             'population that no longer exists.</em>',
         stem='What is this paragraph doing?',
         options=['Households that still have a landline telephone',
                  'The survey&rsquo;s figures, read in full',
                  'A warning about how the sample was chosen',
                  'Change in the population since 2023'],
         correct=2, why='r7why'),

    dict(ctx='<em>Supporters of the dam point to the electricity it will '
             'produce and the floods it will end. Its critics point to the '
             'valley it will drown and the twelve villages that stand '
             'there. Both sides quote numbers; neither side quotes the '
             'other&rsquo;s.</em>',
         stem='What is this paragraph doing?',
         options=['The twelve villages that stand in the valley',
                  'The electricity the new dam will generate',
                  'Dams and the environment',
                  'Two sides that do not answer each other'],
         correct=3, why='r8why'),
]

# ── Activity 3 · order of attack ───────────────────────────────────────
ATTACK = [
    dict(ctx='<em>Seven paragraphs, A to G. Ten headings, i to x. Sixty '
             'minutes for the whole paper and twenty of them already '
             'gone.</em>',
         stem='Which do you match first?',
         options=['The paragraph whose heading you are surest of',
                  'Paragraph A, because the passage starts there',
                  'The heading that appears first on the list',
                  'The paragraph with the most unfamiliar vocabulary'],
         correct=0, why='r9why'),

    dict(ctx='<em>Heading iv, &ldquo;The cost of doing nothing&rdquo;, seems '
             'to fit both paragraph C and paragraph E. Paragraph C describes '
             'what a delay would cost. Paragraph E also mentions the cost of '
             'delay, in one sentence, before moving on to a proposed '
             'timetable.</em>',
         stem='What do you do with heading iv?',
         options=['Give iv to C and to E, since it fits both of them',
                  'Give iv to C; E is really about the timetable',
                  'Give iv to E, because it comes later in the passage',
                  'Leave iv unused, since a heading that fits twice is a trap'],
         correct=1, why='r10why'),

    dict(ctx='<em>Paragraph F is four sentences long. It names three cities '
             'that have tried congestion charging, gives the result in each, '
             'and ends by noting that none of the three has repealed '
             'it.</em>',
         stem='Which heading covers paragraph F?',
         options=['Transport policy around the world',
                  'The result in the first of the three cities',
                  'Where the charge was tried, and what happened',
                  'Why no city has yet tried congestion charging'],
         correct=2, why='r11why'),

    dict(ctx='<em>You have matched five of the seven paragraphs and the '
             'clock is against you. The list still shows all ten '
             'headings.</em>',
         stem='What is the right move for the last two?',
         options=['Reread the whole passage from the beginning',
                  'Leave both blank rather than risk a wrong answer',
                  'Reread all five matched paragraphs to check them',
                  'Strike out the five used, choose from what is left'],
         correct=3, why='r12why'),
]

ALL = MAIN + FUNCTION + ATTACK

# ── The sorting task ───────────────────────────────────────────────────
# Not headings — the SIGNALS. Three things that mark the heading that fits
# the whole paragraph, against the three ways a decoy heading looks right:
# a shared word, a match with the opening line only, a fit that the next
# paragraph could claim just as well.
SORT_BINS = ['Points to the right heading', 'A trap']
SORT_ITEMS = [
    ('Is true of every sentence in the paragraph', 0),
    ('Says what the paragraph does, not what it names', 0),
    ('Would survive the loss of any one sentence', 0),
    ('Shares its key word with the paragraph', 1),
    ('Fits the opening sentence and no other', 1),
    ('Would sit just as well on the next paragraph', 1),
]

SORT_WHY = ('The left column all describe a heading that <strong>fits the '
            'paragraph as a whole</strong>: it names the job, it holds for '
            'every sentence, and it does not depend on any one of them. The '
            'right column are the three ways a heading looks right without '
            'being right &mdash; a shared word, a match with the opening line '
            'only, a fit that another paragraph could claim just as well. '
            'Each is a decoy doing exactly what it was written to do.')
