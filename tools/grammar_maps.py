# -*- coding: utf-8 -*-
"""The grammar maps: geographical charts of the language, shown as the
"Sailing the seas of grammar" section straight under the hero of
`grammar.html`.

Innes, 2026-11-08: *"The grammar area should have 'sailing the seas of
grammar' section at the top of the page and we are going to add extra
similar geographical grammar charts later."* Then, the same day, after a
first version put the section above the hero: *"keep the original hero we
had before ... push that section up"*. So the hero stays first, unchanged,
and this section comes directly after it, before the tense code.

TO ADD A CHART, add one dict below and run

    py tools/build_hubs.py
    py tools/seo.py

No markup changes. The first entry is the large featured card; the rest
follow it, picture beside words, as many to a row as fit (one alone fills
the row). Fields:

    href     the chart's page, a root .html file (must exist, or the build stops)
    title    the lesson's name; it leads the card's kicker line
    heading  the card's big line: what the chart teaches (falls back to title)
    image    site-relative picture; a web-sized copy is made in grammar-hub/
    alt      what the picture shows
    blurb    one or two sentences, learner-facing
    go       the link's call to action (optional)
    full     the picture the zoom view opens (optional; defaults to image).
             Every chart picture on the page opens full size on a click:
             Innes, 2026-11-08, "all the charts should be expandable here".

SOON is the same shape, for a chart whose art is painted but whose lesson
is not built: no href, a `level` typed by hand, and a `note` saying what is
still missing. Its card has no link, only the picture to open. When the
lesson ships, move the entry up into MAPS (with its href) and delete it here.

PLANNED is the chart table: charts from docs/GRAMMAR-MAPS-PLAN.md with no
art yet, one line each. Delete a line when its chart moves to SOON or MAPS.

Level and "Free" are NOT typed here: tools/build_grammar_hub.py reads them
off the catalogue row for `href`, like every other claim on the page.

Blurbs: write the -ING of a grammar token with a non-breaking hyphen
(U+2011) and keep "TO + verb" together with no-break spaces (U+00A0), or
they split across lines on a phone. The Seas blurb below has both.

The Sherpa Tensing route map is here because it is the same kind of thing:
the tenses drawn as a place (a mountain with a camp per tense) rather than
a list. It also appears in the "two routes" section further down, as a
course; here it is a map.
"""

MAPS = [
    dict(href='sailing-the-seas-of-grammar.html',
         title='Sailing the Seas of Grammar',
         heading='Gerunds or infinitives, coast by coast',
         image='sailing-the-seas-of-grammar/hero.jpg',
         alt=('A hand-drawn sea chart: the orange coast of Gerundia, the green '
              'coast of Infinitivia, and Twofold Isle in the channel between them'),
         blurb=('Every harbour on the west coast takes ‑ING, every harbour on '
                'the east takes TO + verb, and the island in the middle '
                'takes both, with a change of meaning. Learn the coastline and you '
                'know which form follows the verb.'),
         go='Set sail'),
    dict(href='sailing-the-seas-regularia.html',
         title='Regularia & Irregularia',
         heading='Regular and irregular verbs, island by island',
         image='sailing-the-seas-regularia/hero.jpg',
         alt=('A hand-painted sea chart: the green continent of Regularia on the west, '
              'and an archipelago of irregular-verb islands on the east'),
         blurb=('Almost every verb lives on one tidy continent and takes ‑ed, in one of '
                'three sounds. The rest live on islands, one family to an island, named '
                'after the sound they share: ring rang rung, keep kept, speak spoke spoken.'),
         go='Set sail'),
    dict(href='sailing-the-seas-countania.html',
         title='Countania & Uncountania',
         heading='Countable and uncountable nouns, shore by shore',
         image='sailing-the-seas-countania/hero.jpg',
         alt=('A hand-painted sea chart: the orange coast of Countania on the west, '
              'the gold coast of Uncountania on the east, Double Isle and the Shallows '
              'in the strait between them'),
         blurb=('A chair, two chairs, many chairs live on the west coast; furniture, '
                'much furniture, a piece of furniture live on the east. Below deck, the '
                'ship’s store cabin and cargo hold show the same cargo with two different words.'),
         go='Set sail'),
    dict(href='sailing-the-seas-adjective-canal.html',
         title='The Adjective Canal',
         heading='Adjective order, lock by lock',
         image='sailing-the-seas-adjective-canal/hero.jpg',
         alt=('A painted chart of a canal through green meadows, with eight lock gates labelled opinion, '
              'size, age, shape, colour, origin, material and purpose, ending in Noun Harbour'),
         blurb=('A noun travels with its adjectives like a barge down a canal: through eight locks, '
                'in one order, never backwards. Opinion first; purpose right next to the noun.'),
         go='Set sail'),
    dict(href='sailing-the-seas-prefixes.html',
         title='The Prefix Archipelago',
         heading='Negative prefixes, island by island',
         image='sailing-the-seas-prefixes/hero.jpg',
         alt=('A painted sea chart: an orange mainland marked UN- and six islands, IM-, IL-, IR-, IN-, '
              'DIS- and MIS-, each with its own landmark'),
         blurb=('Most words sail to the mainland and take un-. The rest live on islands with their own '
                'rules: im- before p and m, il- before l, ir- before r, dis- for the opposite, mis- for wrongly.'),
         go='Set sail'),
    dict(href='sailing-the-seas-soundings.html',
         title='Soundings of Frequency',
         heading='Adverbs of frequency, by the depth of the sea',
         image='sailing-the-seas-soundings/hero.jpg',
         alt=('A painted depth chart: a sandy shore at Never Point, then the sea deepening in bands from '
              'hardly ever to always, with a red anchor buoy'),
         blurb=('How often is how deep: never on the shore, always in the deepest water. The red buoy '
                'shows where the word drops anchor in a sentence.'),
         go='Set sail'),
    dict(href='sherpa-tensing-route-map.html',
         title='Sherpa Tensing route map',
         heading='Every tense, camp by camp',
         image='Sherpa Tensing/thumb-route-map.png',
         alt=('A mountain with a camp for each tense, from the present simple at '
              'the foot to the future perfect at the top'),
         blurb=('Each tense is a camp on the mountain, in its own colour: the active '
                'voice on the way up, the passive on the way down.'),
         go='Open the map'),
]

SOON = []

PLANNED = [
    ('The Atlas of THE', 'articles with place names', 'B1–B2'),
    ('Finished Time & Open Time', 'present perfect or past simple', 'A2–B2'),
    ('The Conditional Quadrants', 'real and unreal, now and past', 'B1–C1'),
    ('The Harbour of Scale', 'in, on and at', 'A2–B1'),
    ('The Voyage', 'prepositions of movement', 'A2–B1'),
    ('The ‑ER Coast & the MORE Coast', 'comparatives', 'A2–B1'),
    ('Statia & Actia', 'state and action verbs', 'B1–B2'),
    ('Makeland & Doland', 'make or do', 'A2–B2'),
    ('Soundings of Certainty', 'must, might, can’t', 'B2–C1'),
    ('The Passive Ferry', 'the passive', 'B1–B2'),
    ('The Backshift Current', 'reported speech', 'B1–B2'),
    ('The Bridges', 'linking words', 'B2–C1'),
]
