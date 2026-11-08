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
