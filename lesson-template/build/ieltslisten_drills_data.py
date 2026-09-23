# -*- coding: utf-8 -*-
"""IELTS Listening: numbers, spelling and accents — the drills.

The last lesson on the Listening route, and the odd one out. The four section
lessons each teach a section; this one takes the three things that lose marks
in ALL of them and drills each on its own.

  1. **Numbers.** Not arithmetic — conventions. "Double oh", "oh" for zero,
     "and" in a British number, the difference between thirteen and thirty at
     speaking speed, and how a price, a date and a phone number are each said
     differently.
  2. **Spelling.** English letter names are not the problem; the pairs that
     collide are. A and R, E and I, G and J, M and N, S and F. A candidate who
     cannot separate those loses an answer per paper, every paper.
  3. **Accents.** The test uses British, Australian, New Zealand, North
     American and Irish speakers, and a learner who has only ever heard one of
     them is not ready for the other four.

**THE RECORDINGS ARE SHORT, AND THERE ARE TWO OF THEM**, not one long one.
Every other lesson on this route plays a single section once, because that is
the test. A drill is the opposite: a few seconds, again and again, until the
distinction is automatic — and the engine offers a replay control the moment a
clip ends, which on these two is the point rather than a concession.

Each clip is built from short takes in DIFFERENT ACCENTS, so the accent drill
is not a section at the end: it is the structure of the other two. A learner
meets six accents while doing nothing but writing down numbers and letters.
"""

# ── the clips ──────────────────────────────────────────────────────────
# TWO grouped recordings rather than seven separate ones. Each is built from
# short takes in DIFFERENT ACCENTS, so the accent drill is not a section at the
# end — it is the structure of the other two. A learner meets British,
# American, Australian, Canadian, Irish and New Zealand English while doing
# nothing but writing down numbers and letters.
NUMBER_TAKES = [
    ('gb_f', 'The reference is double oh four, seven one three.'),
    ('us_m', 'It costs thirteen fifty. Not thirty, thirteen.'),
    ('au_f', "We're open from the fourteenth of March until the thirtieth "
             'of April.'),
    ('ca_f', 'The class is on the eighth floor, room eight eighty.'),
    ('gb_m2', 'Twenty pounds a head, or eighteen if you book by Friday.'),
]

SPELLING_TAKES = [
    ('ie_m', 'The surname is Hargreaves. H, A, R, G, R, E, A, V, E, S.'),
    ('nz_f', "That's Ffion. Double F, I, O, N."),
]

CLIPS = [
    ('numbers.mp3', NUMBER_TAKES, 'Numbers &middot; five accents'),
    ('spelling.mp3', SPELLING_TAKES, 'Spelling &middot; two accents'),
]

# ── Drill 1 · the numbers ──────────────────────────────────────────────
NUMBERS_A = [
    ('Reference: ______', ['004713|00 47 13|0047 13'],
     '"Double oh" is two noughts: 004713. A candidate counting six separate '
     'digits never hears six.'),
    ('Price: £______', ['13.50|13,50'],
     'Thirteen fifty, then "not thirty, thirteen": the pair that costs more '
     'marks than any other number in English.'),
    ('Open from ______ March', ['14th|14|fourteenth'],
     'The fourteenth. Ordinals run together at speed &mdash; fourteenth and '
     'fortieth come out close, and only one of them is a real date.'),
]

NUMBERS_B = [
    ('Room ______', ['880'],
     'Eight eighty. English says a room number in pairs rather than as a whole '
     'number, which is why "eight hundred and eighty" is what a learner '
     'expects and never what they hear.'),
    ('Price if you book early: £______', ['18|eighteen'],
     'Eighteen. Twenty is the full price and it is said first; the gap asks '
     'for the early-booking price, so the figure tied to that condition is the '
     'one to write.'),
]

NUMBERS_BANK = []

# ── Drill 2 · the spelling ─────────────────────────────────────────────
SPELLING = [
    ('Surname: ______', ['Hargreaves|HARGREAVES'],
     'Hargreaves. The traps are the vowels &mdash; an A, then E and A '
     'together &mdash; which learners swap because their own alphabets name '
     'them differently, and the G, which is easily written as J.'),
    ('First name: ______', ['Ffion|FFION'],
     'Ffion, with a double F. When a speaker says "double" before a letter it '
     'is two of them &mdash; the same convention as "double oh" in a number, '
     'which is why the two drills belong in one lesson.'),
]

SPELLING_BANK = []

# ── Drill 3 · the pairs that collide ───────────────────────────────────
# Not audio. This is the reference the learner takes away, and it is a sort
# because grouping the pairs is what makes them memorable.
PAIRS_BINS = ['Sound alike', 'Rarely confused']
PAIRS_ITEMS = [
    ('A and E', 0),
    ('E and I', 0),
    ('G and J', 0),
    ('M and N', 0),
    ('W and Y', 1),
    ('K and Q', 1),
]

PAIRS_WHY = ('The four on the left are the ones that actually collide in '
             'English letter names, and between them they account for most '
             'misspelled Section 1 answers. English <strong>A</strong> sounds '
             'like the E of most European alphabets, and English '
             '<strong>E</strong> like their I, so A and E, and E and I, are '
             'swapped by anyone hearing with their own alphabet; '
             '<strong>G</strong> and <strong>J</strong> share their opening '
             'sound and differ only in the vowel; <strong>M</strong> and '
             '<strong>N</strong> differ only in the final nasal. W and Y, and '
             'K and Q, sound nothing alike once said in full &mdash; which is '
             'why nobody mishears them.')

# ── Drill 4 · multiple choice ──────────────────────────────────────────
MC = [
    dict(stem='A speaker says "double four". You write',
         options=['44, because "double" means two of that digit.',
                  '4, because "double" is only emphasis here.',
                  '8, because "double four" means four plus four.',
                  '24, because "double" multiplies the digit given.'],
         correct=0, why='d1why'),

    dict(stem='Which pair of numbers is most often confused in English?',
         options=['Four and fourteen, because of the shared root.',
                  'Thirteen and thirty, because the stress differs.',
                  'Twenty and twelve, because both begin with "tw".',
                  'Sixty and sixteen, which sound nothing alike.'],
         correct=1, why='d2why'),

    dict(stem='Why does the test use several different accents?',
         options=['To make the recordings sound more interesting.',
                  'Because the recordings are made in several places.',
                  'Because English is used worldwide and so is the test.',
                  'To make the Listening paper harder than the others.'],
         correct=2, why='d3why'),

    dict(stem='You hear a letter and cannot tell if it is M or N. What helps?',
         options=['Guess M, since it is the commoner of the two.',
                  'Write both and let the marker choose one of them.',
                  'Leave it blank, since a wrong letter loses the mark.',
                  'Use the rest of the word, which usually settles it.'],
         correct=3, why='d4why'),
]
