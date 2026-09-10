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

G_LAND, G_INK = '#D89257', '#4A2409'      # Gerundia
I_LAND, I_INK = '#7FA870', '#1C3A17'      # Infinitivia
T_LAND, T_INK = '#AE87BE', '#341A40'      # Twofold Isle
S_INK = '#6B5320'                         # The Shallows
CURRENT_INK = '#1A5A66'                   # compass hint + the two currents

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
# A spur off the -ing shore flying a flag that says TO, because the to here is
# a preposition and a preposition always lands you on this side
CAPE_OUTLINE = [
    (258, 450), (296, 440), (340, 446), (378, 464), (390, 476),
    (362, 494), (312, 500), (270, 486),
]

GERUND_COAST = _path(_roughen(GERUND_OUTLINE, seed=7, hold=_offscreen))
INFIN_COAST = _path(_roughen(INFIN_OUTLINE, seed=23, hold=_offscreen))
ISLAND_COAST = _path(_roughen(ISLAND_OUTLINE, seed=41, ratio=0.11))
FALSE_CAPE = _path(_roughen(CAPE_OUTLINE, seed=83, levels=2, ratio=0.10))

# ─────────────────────────────────────────────────────────────────────
# Every place name is a verb. That is the whole joke and the whole lesson.
# ─────────────────────────────────────────────────────────────────────
# Coordinates below are calibrated against the actual dots in the illustrated
# map (sailing-the-seas-of-grammar/chart-clean.jpg), not just the procedural
# coastline: matched by blob-detecting that artwork's own harbour markers and
# converting back into this 1000x660 space, so a label overlaid on the photo
# lands on the dot it names rather than somewhere nearby.
GERUND_PLACES = [
    (144, 85, 'Cape Avoid', 'avoid'),
    (85, 125, 'Enjoy Bay', 'enjoy'),
    (176, 142, 'Finish Point', 'finish'),
    (109, 186, 'Mind Head', 'mind'),
    (86, 229, 'Suggest Sound', 'suggest'),
    (202, 236, 'Admit Cove', 'admit'),
    (102, 282, 'Deny Rock', 'deny'),
    (203, 299, 'Practise Sands', 'practise'),
    (95, 341, 'Postpone Marsh', 'postpone'),
    (198, 353, 'Risk Reef', 'risk'),
    (93, 385, 'Consider Ness', 'consider'),
    (197, 419, 'Miss Mere', 'miss'),
    (98, 456, 'Imagine Fell', 'imagine'),
    (160, 502, "Can&#39;t-Stand Crag", "can&#39;t stand"),
    (85, 552, 'Keep Gill', 'keep'),
]
INFINITIVE_PLACES = [
    (845, 86, 'Want Harbour', 'want'),
    (813, 124, 'Decide Head', 'decide'),
    (894, 171, 'Hope Point', 'hope'),
    (802, 200, 'Refuse Rock', 'refuse'),
    (922, 221, 'Promise Bay', 'promise'),
    (772, 262, 'Agree Sands', 'agree'),
    (891, 295, 'Manage Moor', 'manage'),
    (800, 339, 'Offer Ness', 'offer'),
    (908, 376, 'Learn Ridge', 'learn'),
    (785, 416, 'Afford Fell', 'afford'),
    (907, 463, 'Pretend Pike', 'pretend'),
    (782, 485, 'Expect Tarn', 'expect'),
    (875, 568, 'Fail Force', 'fail'),
    (736, 610, 'Plan Peak', 'plan'),
]
ISLAND_PLACES = [
    (512, 256, 'Stop Harbour', 'stop'),
    (454, 296, 'Remember Rock', 'remember'),
    (569, 297, 'Forget Ness', 'forget'),
    (460, 340, 'Try Tarn', 'try'),
    (560, 343, 'Regret Reach', 'regret'),
    (503, 370, 'Go-On Gill', 'go on'),
]


def _places(items, ink, size=11):
    """Each harbour's label, positioned just above the dot the artwork itself
    already draws there — the coordinates are calibrated to that dot (see the
    PLACES lists above), so no marker of our own is needed underneath the
    text. Carries the bare verb too, so the chart can be read either as a
    place or as a word list without redrawing."""
    out = []
    for x, y, name, verb in items:
        out.append(
            '<text class="place-name" x="%d" y="%d" text-anchor="middle" '
            'font-family="Inter,sans-serif" font-size="%s" font-weight="600" fill="%s" '
            'data-place="%s" data-verb="%s">%s</text>'
            % (x, y - 8, size, ink, name, verb, name))
    return "\n        ".join(out)


# The captions the artwork itself no longer carries (it was generated with
# no text at all, so a label could be overlaid on it cleanly) — the compass
# hint, the two current arrows, the false cape's flag and name, the shallows
# box, and the two shore titles. Positions are the same viewBox coordinates
# the old hand-drawn chart used for these same elements, since the artwork
# was composed to match that layout.
CAPTIONS = '''<g class="chart-captions">
        <text x="500" y="48" text-anchor="middle" font-family="Inter,sans-serif"
              font-size="10.5" font-weight="700" letter-spacing=".06em" fill="%(cur)s">&#9664; -ING &#183; TO &#9654;</text>
        <text x="485" y="154" text-anchor="middle" font-family="Inter,sans-serif"
              font-size="10.5" font-weight="700" letter-spacing=".1em" fill="%(cur)s">PREPOSITIONS RUN WEST</text>
        <text x="529" y="442" text-anchor="middle" font-family="Inter,sans-serif"
              font-size="10.5" font-weight="700" letter-spacing=".1em" fill="%(cur)s">EVEN THE ONES SPELLED &#8220;TO&#8221;</text>
        <text x="408" y="430" text-anchor="middle" font-family="Inter,sans-serif"
              font-size="11.5" font-weight="700" fill="#3A1D04">TO</text>
        <text x="316" y="516" text-anchor="middle" font-family="Inter,sans-serif"
              font-size="10.5" font-weight="700" letter-spacing=".06em" fill="%(g)s">THE FALSE CAPE</text>
        <text x="512" y="540" text-anchor="middle" font-family="Fraunces,Georgia,serif"
              font-size="13" font-weight="700" letter-spacing=".05em" fill="%(s)s">THE SHALLOWS</text>
        <text x="512" y="555" text-anchor="middle" font-family="Inter,sans-serif"
              font-size="9.5" font-weight="600" fill="%(s)s">either channel, same meaning</text>
        <text x="512" y="569" text-anchor="middle" font-family="Inter,sans-serif"
              font-size="9" fill="%(s)s">begin &#183; start &#183; continue &#183; like &#183; hate</text>
        <text x="56" y="608" font-family="Fraunces,Georgia,serif" font-size="22"
              font-weight="700" letter-spacing=".05em" fill="%(g)s">GERUNDIA</text>
        <text x="58" y="627" font-family="Inter,sans-serif" font-size="11"
              font-weight="600" fill="%(g)s">verb + <tspan font-style="italic">-ing</tspan></text>
        <text x="946" y="608" text-anchor="end" font-family="Fraunces,Georgia,serif" font-size="22"
              font-weight="700" letter-spacing=".05em" fill="%(i)s">INFINITIVIA</text>
        <text x="944" y="627" text-anchor="end" font-family="Inter,sans-serif" font-size="11"
              font-weight="600" fill="%(i)s">verb + <tspan font-style="italic">to</tspan> + infinitive</text>
        <text x="500" y="204" text-anchor="middle" font-family="Fraunces,Georgia,serif"
              font-size="15.5" font-weight="700" letter-spacing=".05em" fill="%(t)s">TWOFOLD ISLE</text>
        <text x="500" y="219" text-anchor="middle" font-family="Inter,sans-serif"
              font-size="9.5" font-weight="600" fill="%(t)s">both channels &#183; two meanings</text>
      </g>''' % {'cur': CURRENT_INK, 'g': G_INK, 'i': I_INK, 't': T_INK, 's': S_INK}


def _hotspot(uid, suffix, coast, aria):
    """An invisible click/focus target shaped like a landmass, with no fill
    of its own — the illustrated map underneath supplies all the paint now."""
    return ('<path id="%s-%s" class="land" tabindex="0" role="button" aria-label="%s" '
            'style="cursor:pointer" d="%s" fill="transparent" stroke="transparent" stroke-width="14"/>'
            % (uid, suffix, aria, coast))


def chart_overlay(uid):
    """A hotspot-and-label layer for the illustrated chart
    (sailing-the-seas-of-grammar/chart-clean.jpg): the artwork already draws
    the sea, the shores, the island, the currents, the compass and the ship,
    so this SVG only adds what a picture can't do on its own — click targets
    over each landmass and text that switches between place names and bare
    verbs. uid keeps the ids unique if the chart ever appears twice on a page.
    """
    return '''<svg class="sail-chart sail-chart-overlay" viewBox="0 0 %d %d">
        %s
        %s
        %s
        %s
        %s
        <g class="place-layer">
        %s
        %s
        %s
        </g>
      </svg>''' % (
        W, H,
        _hotspot(uid, 'shape-gerund', GERUND_COAST,
                 'Gerundia, the shore of verbs followed by the -ing form'),
        _hotspot(uid, 'shape-infin', INFIN_COAST,
                 'Infinitivia, the shore of verbs followed by to plus infinitive'),
        _hotspot(uid, 'shape-isle', ISLAND_COAST,
                 'Twofold Isle, verbs that take both forms with a change of meaning'),
        _hotspot(uid, 'shape-false', FALSE_CAPE,
                 'The False Cape, where to is a preposition and takes the -ing form'),
        CAPTIONS,
        _places(GERUND_PLACES, G_INK),
        _places(INFINITIVE_PLACES, I_INK),
        _places(ISLAND_PLACES, T_INK, 10.5))


if __name__ == '__main__':
    open('/tmp/sail_preview.svg', 'w', encoding='utf-8').write(chart_overlay('p'))
    print('wrote /tmp/sail_preview.svg')
