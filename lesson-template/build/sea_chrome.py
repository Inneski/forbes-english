# -*- coding: utf-8 -*-
"""Site chrome for the Sailing the Seas chart pages: the Forbes English logo,
and panels that let the sky show through.

Innes, 2026-11-09: "forbes english logo should be on all of these". The
pages borrow the Sherpa camp shell, whose header (.wordmark) carries the
series name and no logo. add() puts the standard lesson lockup (HOUSE-STYLE
§2: the Forbes trace with ENGLISH as <text textLength="1520">, copied from
fe_logo_lesson.svgfrag, which tools/check_logos.py accepts) at the head of
that header, linked home.

Innes, 2026-11-10: "dont want white panels at 100% opacity either ... on all
grammar map stuff". The shell's --card is #FFFFFF and the quiz options are
#fff; here both become the palette's own card colour (read off the page's
--card) at 74% over the page, with a light
blur so the text stays readable over the clouds. The shell is shared with
the Sherpa camps, so the change is made per page, not in the palette.

Called by build_sailing.py, build_regularia.py, build_countania.py and
sea_lesson.build() just before they write the page.
"""
import os

FRAG = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fe_logo_lesson.svgfrag'),
            encoding='utf-8').read().strip()
CSS = ('  /* the Forbes English logo at the head of the header (sea_chrome.py) */\n'
       '  .wordmark{gap:18px;}\n'
       '  .wordmark .fe-home{display:block;flex:none;line-height:0;}\n'
       '  .wordmark .fe-home svg{height:40px;width:auto;display:block;}\n'
       '  .wordmark .brand{flex:1;}\n'
       '  @media (max-width:560px){.wordmark{flex-wrap:wrap;row-gap:6px;}.wordmark .fe-home svg{height:32px;}'
       '.wordmark .sub{flex-basis:100%;}}\n'
       '  /* see-through panels: the sky shows behind every card (sea_chrome.py) */\n'
       '  :root{--card:color-mix(in srgb, CARD 74%, transparent);}\n'
       '  .chart-wrap,.rule-card,.diagram-card,.quiz-card,.diagram-panel{-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px);}\n'
       '  .opt-btn{background:var(--card);}\n')


def add(s):
    assert 'class="fe-home"' not in s, 'the logo is already on the page'
    assert s.count('<div class="wordmark">') == 1, 'no single .wordmark header to hang the logo on'
    s = s.replace('<div class="wordmark">',
                  '<div class="wordmark">\n  <a class="fe-home" href="index.html" aria-label="Forbes English home">%s</a>'
                  % FRAG, 1)
    import re
    card = re.search(r'--card:\s*(#[0-9A-Fa-f]{6})\s*;', s)
    assert card, 'no solid --card in the palette to make see-through'
    i = s.rindex('</style>', 0, s.index('</head>'))
    return s[:i] + CSS.replace('CARD', card.group(1)) + s[i:]
