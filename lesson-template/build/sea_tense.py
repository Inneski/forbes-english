# -*- coding: utf-8 -*-
"""Tense colours for the sea charts.

Innes, 2026-11-13: *"Anything involving a tense must use colours in
sherpa."* So a chart that sets one tense against another paints each tense
in the colour the Sherpa Tensing route map publishes for it. The colours are
read off the route map (tools/build_grammar_hub.tense_colours), never typed
here, so a recolour of the map carries into the next layout run.

    from sea_tense import T
    T['past-simple']        # (176, 137, 104)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
import build_grammar_hub                     # noqa: E402

T = {k: tuple(int(fill[i:i + 2], 16) for i in (1, 3, 5))
     for k, (fill, _ink) in build_grammar_hub.tense_colours(quiet=True).items()}
