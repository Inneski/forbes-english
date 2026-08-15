# -*- coding: utf-8 -*-
"""The chart: two shores, an island in the strait, and a current that only
runs one way.

The whole grammar point is geographical. Verbs that take -ing are one landmass
and verbs that take to + infinitive are another, and no amount of wanting will
get you a harbour on the wrong shore. The island in the middle is the part
students actually get wrong: the same verb, two meanings, depending on which
channel you take. And the current is the rule nobody teaches explicitly --
every preposition drags you west to the -ing shore, including the prepositions
that happen to be spelled *to*.

The coastlines are drawn the way real coastlines are drawn: a rough outline,
then midpoint displacement applied three times, so bays grow smaller bays and
headlands grow smaller headlands. The seed is fixed, so the chart is the same
chart every time it is built.
"""
import math, random

W, H = 1000, 660

SEA_TOP, SEA_BOT = '#DEEFF6', '#B2D5E4'
G_LAND, G_BEACH, G_INK = '#D89257', '#F3DCBB', '#4A2409'      # Gerundia
I_LAND, I_BEACH, I_INK = '#7FA870', '#DCEBC9', '#1C3A17'      # Infinitivia
T_LAND, T_BEACH, T_INK = '#AE87BE', '#E7DAEF', '#341A40'      # Twofold Isle
S_SAND, S_INK = '#C09A55', '#6B5320'                          # The Shallows
LINE = '#2B4A57'

# ─────────────────────────────────────────────────────────────────────
# coastlines: a rough outline, then roughened
# ─────────────────────────────────────────────────────────────────────

def _roughen(points, closed=True, levels=3, ratio=0.13, seed=1, hold=None):
    """Midpoint displacement. Each edge grows a midpoint pushed sideways by a
    fraction of its own length, so the detail gets finer as the edges do —
    which is what makes a coastline look like a coastline rather than a wobble.

    hold(a, b) returns True for an edge that must stay dead straight: the
    off-canvas backs of the two landmasses, which nobody ever sees.
    """
    rng = random.Random(seed)
    pts = [tuple(p) for p in points]
    for _ in range(levels):
        out = []
        n = len(pts)
        last = n if closed else n - 1
        for i in range(last):
            a, b = pts[i], pts[(i + 1) % n]
            out.append(a)
            if hold and hold(a, b):
                continue
            dx, dy = b[0] - a[0], b[1] - a[1]
            length = math.hypot(dx, dy)
            if length < 6:
                continue
            d = rng.uniform(-1, 1) * length * ratio
            out.append(((a[0] + b[0]) / 2 - dy / length * d,
                        (a[1] + b[1]) / 2 + dx / length * d))
        if not closed:
            out.append(pts[-1])
        pts = out
    return pts


def _path(points, closed=True):
    head = 'M %.1f %.1f' % points[0]
    body = ' '.join('L %.1f %.1f' % p for p in points[1:])
    return '%s %s%s' % (head, body, ' Z' if closed else '')


def _offscreen(a, b):
    """Both ends outside the canvas: the back of a landmass, left straight."""
    return (a[0] < -10 and b[0] < -10) or (a[0] > 1010 and b[0] > 1010)


# Gerundia: sea-facing coast from north to south, then straight off-canvas
GERUND_OUTLINE = [
    (120, 34), (198, 62), (236, 112), (230, 160), (264, 202), (300, 256),
    (286, 302), (258, 350), (252, 402), (288, 448), (266, 492), (242, 532),
    (258, 566), (234, 594), (178, 622), (100, 642),
    (-30, 654), (-30, 18),
]
# Infinitivia: the mirror of it
INFIN_OUTLINE = [
    (892, 28), (802, 58), (748, 110), (754, 158), (722, 204), (700, 252),
    (702, 302), (722, 342), (736, 392), (720, 432), (704, 470), (700, 512),
    (714, 556), (700, 586), (742, 618), (862, 648),
    (1030, 656), (1030, 12),
]
# Twofold Isle: a ring, roughened into a proper island
ISLAND_OUTLINE = [
    (500, 224), (546, 232), (578, 254), (596, 284), (592, 318), (574, 352),
    (546, 382), (508, 402), (470, 390), (438, 366), (414, 336), (404, 302),
    (414, 268), (442, 240),
]
# The Shallows: a sandbank, not a landmass — flatter, and drawn dashed
SHALLOWS_OUTLINE = [
    (512, 498), (578, 507), (624, 523), (648, 546), (624, 572), (576, 589),
    (512, 596), (448, 589), (400, 572), (376, 546), (400, 523), (446, 507),
]
# A spur off the -ing shore flying a flag that says TO, because the to here is
# a preposition and a preposition always lands you on this side
CAPE_OUTLINE = [
    (258, 450), (296, 440), (340, 446), (378, 464), (390, 476),
    (362, 494), (312, 500), (270, 486),
]

GERUND_COAST = _path(_roughen(GERUND_OUTLINE, seed=7, hold=_offscreen))
INFIN_COAST = _path(_roughen(INFIN_OUTLINE, seed=23, hold=_offscreen))
ISLAND_COAST = _path(_roughen(ISLAND_OUTLINE, seed=41, ratio=0.11))
SHALLOWS_COAST = _path(_roughen(SHALLOWS_OUTLINE, seed=59, ratio=0.10))
FALSE_CAPE = _path(_roughen(CAPE_OUTLINE, seed=83, levels=2, ratio=0.10))

# ─────────────────────────────────────────────────────────────────────
# Every place name is a verb. That is the whole joke and the whole lesson.
# ─────────────────────────────────────────────────────────────────────
GERUND_PLACES = [
    (140, 92, 'Cape Avoid', 'avoid'),
    (78, 132, 'Enjoy Bay', 'enjoy'),
    (172, 152, 'Finish Point', 'finish'),
    (100, 196, 'Mind Head', 'mind'),
    (78, 250, 'Suggest Sound', 'suggest'),
    (190, 244, 'Admit Cove', 'admit'),
    (96, 300, 'Deny Rock', 'deny'),
    (206, 312, 'Practise Sands', 'practise'),
    (86, 356, 'Postpone Marsh', 'postpone'),
    (196, 372, 'Risk Reef', 'risk'),
    (96, 412, 'Consider Ness', 'consider'),
    (196, 448, 'Miss Mere', 'miss'),
    (86, 494, 'Imagine Fell', 'imagine'),
    (146, 534, "Can&#39;t-Stand Crag", "can&#39;t stand"),
    (86, 572, 'Keep Gill', 'keep'),
]
INFINITIVE_PLACES = [
    (840, 86, 'Want Harbour', 'want'),
    (806, 132, 'Decide Head', 'decide'),
    (900, 158, 'Hope Point', 'hope'),
    (782, 208, 'Refuse Rock', 'refuse'),
    (906, 236, 'Promise Bay', 'promise'),
    (760, 268, 'Agree Sands', 'agree'),
    (866, 306, 'Manage Moor', 'manage'),
    (790, 352, 'Offer Ness', 'offer'),
    (902, 386, 'Learn Ridge', 'learn'),
    (778, 428, 'Afford Fell', 'afford'),
    (886, 466, 'Pretend Pike', 'pretend'),
    (762, 496, 'Expect Tarn', 'expect'),
    (868, 536, 'Fail Force', 'fail'),
    (752, 582, 'Plan Peak', 'plan'),
]
ISLAND_PLACES = [
    (500, 262, 'Stop Harbour', 'stop'),
    (458, 296, 'Remember Rock', 'remember'),
    (552, 300, 'Forget Ness', 'forget'),
    (466, 336, 'Try Tarn', 'try'),
    (548, 340, 'Regret Reach', 'regret'),
    (500, 374, 'Go-On Gill', 'go on'),
]


def _places(items, ink, size=11):
    """Each harbour carries its map name and the bare verb underneath it, so the
    chart can be read either as a place or as a word list without redrawing."""
    out = []
    for x, y, name, verb in items:
        out.append(
            '<g class="place"><circle cx="%d" cy="%d" r="2.8" fill="%s"/>'
            '<text class="place-name" x="%d" y="%d" text-anchor="middle" '
            'font-family="Inter,sans-serif" font-size="%s" font-weight="600" fill="%s" '
            'data-place="%s" data-verb="%s">%s</text></g>'
            % (x, y, ink, x, y - 8, size, ink, name, verb, name))
    return "\n        ".join(out)


def _wave(x, y, w=28):
    return ('<path d="M %d %d q %d -5 %d 0 q %d 5 %d 0" fill="none" stroke="#84B4C9" '
            'stroke-width="1.6" stroke-linecap="round" opacity=".6"/>'
            % (x, y, w // 4, w // 2, w // 4, w // 2))


def _current(y, x_from, x_to, label, label_dy=-22):
    """A preposition current. It only ever runs west, toward the -ing shore."""
    mid = (x_from + x_to) / 2
    return '''<g class="current">
          <path d="M %d %d C %d %d, %d %d, %d %d" fill="none" stroke="#22707F"
                stroke-width="2.6" stroke-dasharray="10 7" stroke-linecap="round"
                marker-end="url(#SAILUID-tide)" opacity=".9"/>
          <text x="%d" y="%d" text-anchor="middle" font-family="Inter,sans-serif"
                font-size="10.5" font-weight="700" letter-spacing=".1em"
                fill="#1A5A66">%s</text>
        </g>''' % (x_from, y, x_from - 46, y - 15, x_to + 52, y + 15, x_to, y,
                   mid, y + label_dy, label)


COMPASS = '''<g class="compass">
          <circle cx="500" cy="92" r="36" fill="#FFFFFF" opacity=".6"/>
          <circle cx="500" cy="92" r="36" fill="none" stroke="#22707F" stroke-width="1.4"/>
          <path d="M 500 60 L 507 88 L 500 124 L 493 88 Z" fill="#D89257" stroke="#2B4A57" stroke-width="1"/>
          <path d="M 468 92 L 496 85 L 532 92 L 496 99 Z" fill="#2B4A57" opacity=".72"/>
          <text x="500" y="48" text-anchor="middle" font-family="Inter,sans-serif"
                font-size="10.5" font-weight="700" letter-spacing=".06em" fill="#1A5A66">&#9664; -ING &#183; TO &#9654;</text>
        </g>'''

SHIP = '''<g class="ship">
          <path d="M 274 616 L 330 616 L 321 630 L 283 630 Z" fill="#3B2A1E"/>
          <path d="M 302 578 L 302 616" stroke="#3B2A1E" stroke-width="2.4"/>
          <path d="M 304 582 L 330 611 L 304 611 Z" fill="#FBF6EC" stroke="#3B2A1E" stroke-width="1.3"/>
          <path d="M 298 588 L 275 611 L 298 611 Z" fill="#FBF6EC" stroke="#3B2A1E" stroke-width="1.3"/>
        </g>'''


def _land(uid, suffix, coast, beach, fill, aria, clickable):
    tag = ('tabindex="0" role="button" aria-label="%s" style="cursor:pointer"' % aria
           if clickable else 'aria-hidden="true"')
    return '''<g id="%s-%s" class="land" %s>
          <path d="%s" fill="none" stroke="%s" stroke-width="16" stroke-linejoin="round"/>
          <path d="%s" fill="%s" stroke="%s" stroke-width="2.2" stroke-linejoin="round"/>
        </g>''' % (uid, suffix, tag, coast, beach, coast, fill, LINE)


def chart(uid, clickable=False):
    """The whole map. uid keeps the ids unique when it appears twice on a page."""
    waves = "\n        ".join(
        _wave(x, y) for x, y in
        [(348, 210), (614, 200), (346, 330), (612, 340), (352, 596), (604, 500),
         (424, 470), (556, 468), (452, 626), (348, 130)])

    def cur(*a, **k):
        return _current(*a, **k).replace('SAILUID', uid)

    return '''<svg class="sail-chart" viewBox="0 0 %d %d" role="img"
       aria-label="A sea chart with two ragged coastlines. The western shore, Gerundia, has harbours named after verbs that take the -ing form: Cape Avoid, Enjoy Bay, Finish Point and others. The eastern shore, Infinitivia, has harbours named after verbs that take to plus infinitive: Want Harbour, Decide Head, Hope Point and others. Between them lies Twofold Isle, whose harbours take either form with a change of meaning. South of the island is a shoal marked The Shallows, where either channel is safe. Dashed currents run west across the strait, labelled prepositions. A spur off the western shore flies a flag reading TO and is marked the False Cape.">
        <defs>
          <linearGradient id="%s-sea" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%%" stop-color="%s"/><stop offset="100%%" stop-color="%s"/>
          </linearGradient>
          <marker id="%s-tide" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6"
                  markerHeight="6" orient="auto">
            <path d="M 0 1 L 9 5 L 0 9 z" fill="#22707F"/>
          </marker>
          <pattern id="%s-sand" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(35)">
            <rect width="10" height="10" fill="#F7EBD2"/>
            <line x1="0" y1="0" x2="0" y2="10" stroke="#E3C88F" stroke-width="3.4"/>
          </pattern>
        </defs>

        <rect x="0" y="0" width="%d" height="%d" fill="url(#%s-sea)"/>
        %s

        <g class="shallows" aria-hidden="true">
          <path d="%s" fill="url(#%s-sand)" opacity=".92"/>
          <path d="%s" fill="none" stroke="%s" stroke-width="1.8" stroke-dasharray="7 5"/>
          <rect x="424" y="526" width="176" height="50" rx="9" fill="#FFFCF4" opacity=".78"/>
          <text x="512" y="540" text-anchor="middle" font-family="Fraunces,Georgia,serif"
                font-size="13" font-weight="700" letter-spacing=".05em" fill="%s">THE SHALLOWS</text>
          <text x="512" y="555" text-anchor="middle" font-family="Inter,sans-serif"
                font-size="9.5" font-weight="600" fill="%s">either channel, same meaning</text>
          <text x="512" y="569" text-anchor="middle" font-family="Inter,sans-serif"
                font-size="9" fill="%s">begin &#183; start &#183; continue &#183; like &#183; hate</text>
        </g>

        %s
        %s
        %s

        <g id="%s-shape-false" class="land-false" %s>
          <path d="%s" fill="none" stroke="%s" stroke-width="12" stroke-linejoin="round"/>
          <path d="%s" fill="%s" stroke="%s" stroke-width="2" stroke-linejoin="round"/>
          <path d="M 388 470 L 388 412" stroke="%s" stroke-width="2.4"/>
          <path d="M 388 414 L 434 425 L 388 436 Z" fill="#D89257" stroke="%s" stroke-width="1.5"/>
          <text x="408" y="430" text-anchor="middle" font-family="Inter,sans-serif"
                font-size="11.5" font-weight="700" fill="#3A1D04">TO</text>
          <text x="316" y="516" text-anchor="middle" font-family="Inter,sans-serif"
                font-size="10.5" font-weight="700" letter-spacing=".06em" fill="%s">THE FALSE CAPE</text>
        </g>

        %s
        %s
        %s
        %s

        <g class="labels" aria-hidden="true">
          <text x="56" y="608" font-family="Fraunces,Georgia,serif" font-size="22"
                font-weight="700" letter-spacing=".05em" fill="%s">GERUNDIA</text>
          <text x="58" y="627" font-family="Inter,sans-serif" font-size="11"
                font-weight="600" fill="%s">verb + <tspan font-style="italic">-ing</tspan></text>
          <text x="946" y="608" text-anchor="end" font-family="Fraunces,Georgia,serif" font-size="22"
                font-weight="700" letter-spacing=".05em" fill="%s">INFINITIVIA</text>
          <text x="944" y="627" text-anchor="end" font-family="Inter,sans-serif" font-size="11"
                font-weight="600" fill="%s">verb + <tspan font-style="italic">to</tspan> + infinitive</text>
          <text x="500" y="204" text-anchor="middle" font-family="Fraunces,Georgia,serif"
                font-size="15.5" font-weight="700" letter-spacing=".05em" fill="%s">TWOFOLD ISLE</text>
          <text x="500" y="219" text-anchor="middle" font-family="Inter,sans-serif"
                font-size="9.5" font-weight="600" fill="%s">both channels &#183; two meanings</text>
        </g>

        <g class="place-layer" aria-hidden="true">
        %s
        %s
        %s
        </g>
      </svg>''' % (
        W, H,
        uid, SEA_TOP, SEA_BOT,
        uid,
        uid,
        W, H, uid,
        waves,
        SHALLOWS_COAST, uid, SHALLOWS_COAST, S_SAND, S_INK, S_INK, S_INK,
        _land(uid, 'shape-gerund', GERUND_COAST, G_BEACH, G_LAND,
              'Gerundia, the shore of verbs followed by the -ing form', clickable),
        _land(uid, 'shape-infin', INFIN_COAST, I_BEACH, I_LAND,
              'Infinitivia, the shore of verbs followed by to plus infinitive', clickable),
        _land(uid, 'shape-isle', ISLAND_COAST, T_BEACH, T_LAND,
              'Twofold Isle, verbs that take both forms with a change of meaning', clickable),
        uid,
        ('tabindex="0" role="button" aria-label="The False Cape, where to is a preposition and takes the -ing form" style="cursor:pointer"'
         if clickable else 'aria-hidden="true"'),
        FALSE_CAPE, G_BEACH, FALSE_CAPE, G_LAND, LINE, LINE, LINE, G_INK,
        cur(176, 618, 352, 'PREPOSITIONS RUN WEST'),
        cur(462, 616, 442, 'EVEN THE ONES SPELLED &#8220;TO&#8221;', -20),
        COMPASS,
        SHIP,
        G_INK, G_INK, I_INK, I_INK, T_INK, T_INK,
        _places(GERUND_PLACES, G_INK),
        _places(INFINITIVE_PLACES, I_INK),
        _places(ISLAND_PLACES, T_INK, 10.5))


if __name__ == '__main__':
    open('/tmp/sail_preview.svg', 'w', encoding='utf-8').write(chart('p', True))
    print('wrote /tmp/sail_preview.svg')
