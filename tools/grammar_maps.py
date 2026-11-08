# -*- coding: utf-8 -*-
"""The grammar maps: geographical charts of the language, shown as the band
that opens `grammar.html` ("Sailing the seas of grammar").

Innes, 2026-11-08: *"The grammar area should have 'sailing the seas of
grammar' section at the top of the page and we are going to add extra
similar geographical grammar charts later."*

TO ADD A CHART, add one dict below and run

    py tools/build_hubs.py
    py tools/seo.py

No markup changes. The first entry is the large featured card; the rest
follow it in a row, in list order. Fields:

    href   the chart's page, a root .html file (must exist)
    title  the card's heading
    image  site-relative picture; a web-sized copy is made in grammar-hub/
    alt    what the picture shows (the card is a link, so say what it is)
    blurb  one or two sentences, learner-facing
    go     the link's call to action (optional)

Level and "free" are NOT typed here: tools/build_grammar_hub.py reads them
off the catalogue row for `href`, like every other claim on the page.

The Sherpa Tensing route map is here because it is the same kind of thing:
the tenses drawn as a place (a mountain with a camp per tense) rather than
a list. It also opens the "two routes" section further down, as a course;
here it is a map.
"""

MAPS = [
    dict(href='sailing-the-seas-of-grammar.html',
         title='Sailing the Seas of Grammar',
         image='sailing-the-seas-of-grammar/hero.jpg',
         alt=('A hand-drawn sea chart: the orange coast of Gerundia, the green '
              'coast of Infinitivia, and Twofold Isle in the channel between them'),
         # ‑ is a non-breaking hyphen and   a non-breaking space,
         # so "-ING" and "TO + verb" never split across lines on a phone
         blurb=('Gerunds or infinitives, as a sea chart. Every harbour on the west '
                'coast takes ‑ING, every harbour on the east takes TO + verb, and the '
                'island in the middle takes both, with a change of meaning.'),
         go='Set sail'),
    dict(href='sherpa-tensing-route-map.html',
         title='The Sherpa Tensing route map',
         image='Sherpa Tensing/thumb-route-map.png',
         alt='A mountain with a camp for each tense, from the present simple at the foot to the future perfect at the top',
         blurb=('Every tense as a camp on the mountain, in its own colour: active '
                'on the way up, passive on the way down.'),
         go='Open the map'),
]
