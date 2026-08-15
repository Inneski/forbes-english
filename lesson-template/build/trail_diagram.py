# -*- coding: utf-8 -*-
"""The continuous-perfect family: a trail of movement between two pegs, with a
separate zone above for what the activity leaves behind.

Every one of these tenses says the same two things at once — *this went on for
a while*, and *here is what that means at the moment I am measuring from*. So
every diagram is built the same way:

  · a pale band of time, carrying a trail of the same chevron repeated —
    faint behind, solid at the head, the way a moving thing smears in a still
    photograph. That is the activity: not one event, but one going on and on.
  · a brown peg where it starts, because the start is always a past simple
    event — "since I arrived", "since 2019".
  · a second peg where you are measuring to: the NOW column for camp eight,
    another brown past-simple event for camp eleven, a dashed appointment for
    camp thirteen.
  · a separate zone above, holding the result you can point at when you get
    there. Camp four stacks its zones the same way.

Each camp uses exactly two tones, both its own route-map colour: a pale tint
for the band, the colour itself for the marks. Nothing borrows from a
neighbour.
"""
import sys
sys.path.insert(0, 'lesson-template')
import sherpa_timeline as T

BASE = 299
BAND_TOP = 196
UPPER_TOP = 118
UPPER_BOT = 182
MID = 247
ARM, RISE = 6.5, 17
PEG_TOP = 118

BROWN_DARK = "#7A5A3E"
BROWN = "#B08968"

ARROW = ('        <marker id="ah-%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
         'markerHeight="7" orient="auto-start-reverse">\n'
         '          <path d="M0,0 L10,5 L0,10 z" fill="#1c130c"/>\n        </marker>')


def chevron(cx, colour, opacity, width=5.5, cy=MID, rise=RISE):
    return ('<path d="M%g,%g L%g,%g L%g,%g" fill="none" stroke="%s" stroke-width="%g" '
            'stroke-linecap="round" stroke-linejoin="round" opacity="%.2f"/>'
            % (cx - ARM, cy - rise, cx + ARM, cy, cx - ARM, cy + rise, colour, width, opacity))


def trail(x0, x1, step, colour, o0=0.20, o1=1.0, width=5.5):
    xs, x = [], x0
    while x <= x1 + 0.01:
        xs.append(x)
        x += step
    n = max(len(xs) - 1, 1)
    return "\n        ".join(
        chevron(cx, colour, o0 + i * (o1 - o0) / n, width) for i, cx in enumerate(xs))


def peg(x, label, ink=BROWN_DARK, top=PEG_TOP):
    """A past-simple event, in camp three's brown, pinning one end of the run."""
    return ('<rect x="%g" y="%g" width="13" height="%g" fill="%s"/>\n'
            '      <rect x="%g" y="%g" width="8" height="%g" fill="%s"/>\n'
            '      <text x="%g" y="%g" text-anchor="middle" font-family="Inter, sans-serif" '
            'font-size="10.5" font-weight="700" fill="%s" letter-spacing="1.4" '
            'pointer-events="none">%s</text>'
            % (x - 6.5, top, BASE - top, BROWN_DARK,
               x - 4, top + 2.5, BASE - top - 5, BROWN,
               x, top - 8, ink, label))


def upper_zone(x0, x1, fill, label, sub="", label_ink="#FFFFFF", sub_ink="#EAF6F5"):
    cx = (x0 + x1) / 2
    out = ['<rect x="%g" y="%g" width="%g" height="%g" rx="3" fill="%s"/>'
           % (x0, UPPER_TOP, x1 - x0, UPPER_BOT - UPPER_TOP, fill)]
    out.append('<text x="%g" y="%g" text-anchor="middle" class="diagram-caption" fill="%s" '
               'style="font-size:12.5px;letter-spacing:.04em" pointer-events="none">%s</text>'
               % (cx, 146 if sub else 155, label_ink, label))
    if sub:
        out.append('<text x="%g" y="168" text-anchor="middle" font-family="Inter, sans-serif" '
                   'font-size="10.5" fill="%s" pointer-events="none">%s</text>' % (cx, sub_ink, sub))
    return "\n      ".join(out)


def band(x0, x1, pale, shape_id=None, aria=""):
    r = ('<rect x="%g" y="%g" width="%g" height="%g" fill="%s"/>'
         % (x0, BAND_TOP, x1 - x0, BASE - BAND_TOP, pale))
    if shape_id:
        r = ('<g class="diagram-shape" id="%s" tabindex="0" role="button" aria-label="%s">\n'
             '        %s\n      </g>' % (shape_id, aria, r))
    return r


def cap(x, text, fill, y=317, size=11.5, weight=400, anchor="middle"):
    return ('<text x="%g" y="%g" text-anchor="%s" font-family="Inter, sans-serif" font-size="%g" '
            'font-weight="%d" fill="%s" pointer-events="none">%s</text>'
            % (x, y, anchor, size, weight, fill, text))


def shell(uid, defs, body, aria, cls='hero-diagram', labels=True):
    lab = ''
    if labels:
        lab = (
            '\n      <text x="150" y="26" text-anchor="middle" class="diagram-caption" fill="#8A8175" style="letter-spacing:.14em" pointer-events="none">PAST</text>'
            '\n      <text x="320" y="26" text-anchor="middle" class="diagram-caption" fill="#3E6A85" pointer-events="none">NOW</text>'
            '\n      <text x="490" y="26" text-anchor="middle" class="diagram-caption" fill="#8A8175" style="letter-spacing:.14em" pointer-events="none">FUTURE</text>')
    return ('<svg%s viewBox="0 0 640 344" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="%s">\n'
            '      <defs>\n%s\n%s\n      </defs>\n'
            '      <rect x="0" y="0" width="640" height="344" fill="var(--paper)"/>\n%s%s\n    </svg>'
            % ((' class="%s"' % cls) if cls else '', aria, defs, ARROW % uid, body, lab))


def baseline(uid):
    return ('<line x1="24" y1="299" x2="616" y2="299" stroke="#1c130c" stroke-width="2"\n'
            '            marker-start="url(#ah-%s)" marker-end="url(#ah-%s)"/>' % (uid, uid))


def fade_defs(gid, colour):
    return ('        <linearGradient id="%s" x1="0" y1="0" x2="1" y2="0">\n'
            '          <stop offset="0" stop-color="%s" stop-opacity="0.85"/>\n'
            '          <stop offset="0.55" stop-color="%s" stop-opacity="0.40"/>\n'
            '          <stop offset="1" stop-color="%s" stop-opacity="0"/>\n'
            '        </linearGradient>' % (gid, colour, colour, colour))


# ── camp eight · present perfect continuous ──────────────────────────
E_PALE, E_MARK, E_INK = "#C6ECEA", "#2FA6A1", "#0E5F5C"


def camp_eight(uid='ppc', groups=False):
    defs = fade_defs('ppcGhost' + uid, E_PALE)
    zone = upper_zone(200, 311.5, E_MARK, 'THE EVIDENCE', 'you can see it now')
    if groups:
        zone = ('<g class="diagram-shape" id="shape-evidence" tabindex="0" role="button" '
                'aria-label="Show the evidence examples">\n        %s\n      </g>' % zone)
    body = '''      %s
      %s
      <rect x="336.5" y="196" width="208" height="103" fill="url(#ppcGhost%s)"/>
      %s
      %s
      %s
      %s
      %s
      %s
      %s''' % (
        band(96, 328.5, E_PALE, 'shape-run' if groups else None, 'Show the duration examples'),
        trail(126, 294, 24, E_MARK),
        uid,
        trail(352, 424, 24, E_MARK, 0.46, 0.10, 5.0),
        baseline(uid),
        zone,
        peg(96, 'SINCE'),
        T.NOW_COL,
        cap(200, 'unbroken, right up to now', '#4C7C7A'),
        cap(440, 'and very likely still going', '#8FB6B4'),
    )
    return shell(uid, defs, body,
                 'A timeline from past to future. A pale turquoise band of time carries a trail of '
                 'chevrons that grow solid as they arrive at the NOW column, with a brown past simple '
                 'peg marking where it started. A separate turquoise zone above holds the evidence you '
                 'can see in the present. Past NOW the band and trail carry on, fading.',
                 cls='hero-diagram' if not groups else '')


# ── camp eleven · past perfect continuous ────────────────────────────
L_PALE, L_MARK, L_INK = "#E0D5F1", "#4B1A7A", "#3A1460"


def camp_eleven(uid='ppcx', groups=False):
    zone = upper_zone(124, 248, L_MARK, 'THE EVIDENCE', 'how things stood', sub_ink='#DCCBF0')
    if groups:
        zone = ('<g class="diagram-shape" id="shape-evidence" tabindex="0" role="button" '
                'aria-label="Show the evidence examples">\n        %s\n      </g>' % zone)
    body = '''      %s
      %s
      %s
      %s
      %s
      %s
      %s
      %s
      %s''' % (
        band(76, 252, L_PALE, 'shape-run' if groups else None, 'Show the duration examples'),
        trail(104, 224, 24, L_MARK),
        baseline(uid),
        zone,
        peg(76, 'SINCE'),
        peg(252, 'WHEN'),
        T.NOW_COL,
        cap(150, 'it had been running for a while', '#6E5A8A'),
        cap(420, 'and you are telling it now', '#5F7C90'),
    )
    return shell(uid, '', body,
                 'A timeline from past to future. A pale purple band of time carries a trail of chevrons '
                 'between two brown past simple pegs, the second marking the past moment you are '
                 'measuring to. A purple zone above holds the evidence visible at that moment. Now is a '
                 'narrow column further right.',
                 cls='hero-diagram' if not groups else '')


# ── camp thirteen · future perfect continuous ────────────────────────
F_PALE, F_MARK, F_INK = "#E4E4E4", "#7C7C7C", "#4A4A4A"


def camp_thirteen(uid='fpc', groups=False):
    zone = upper_zone(418, 522, F_MARK, 'THE TOTAL', 'the hours add up', sub_ink='#EFEFEF')
    if groups:
        zone = ('<g class="diagram-shape" id="shape-evidence" tabindex="0" role="button" '
                'aria-label="Show the total examples">\n        %s\n      </g>' % zone)
    body = '''      %s
      %s
      %s
      %s
      %s
      <line x1="522" y1="118" x2="522" y2="299" stroke="%s" stroke-width="1.8" stroke-dasharray="5 4"/>
      <circle cx="522" cy="299" r="4.5" fill="%s"/>
      <text x="522" y="110" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" font-weight="700" fill="%s" letter-spacing="1.4" pointer-events="none">BY THEN</text>
      %s
      %s
      %s''' % (
        band(96, 522, F_PALE, 'shape-run' if groups else None, 'Show the duration examples'),
        trail(124, 496, 26, F_MARK),
        baseline(uid),
        T.NOW_COL,
        peg(96, 'SINCE'),
        F_INK, F_INK, F_INK,
        zone,
        cap(200, 'already running, and it keeps going', '#7A7A7A'),
        cap(471, 'how long, by the time you arrive', '#8A8A8A'),
    )
    return shell(uid, '', body,
                 'A timeline from past to future. A pale grey band of time carries a trail of chevrons '
                 'from a brown past simple peg, straight through the NOW column and on to a dashed '
                 'future appointment. A grey zone above holds the total the activity will have reached '
                 'by then.',
                 cls='hero-diagram' if not groups else '')


# ── camp twelve · future perfect ─────────────────────────────────────
W_LIGHT, W_MARK, W_INK = "#8A8A8A", "#454545", "#3A3A3A"


def camp_twelve(uid='fp', groups=False):
    block = ('<rect x="400" y="38" width="48" height="261" fill="url(#fpFade%s)"/>' % uid)
    if groups:
        block = ('<g class="diagram-shape" id="shape-done" tabindex="0" role="button" '
                 'aria-label="Show future perfect examples">\n        %s\n      </g>' % block)
    now = T.NOW_COL
    if groups:
        now = ('<g class="diagram-shape" id="shape-now" tabindex="0" role="button" '
               'aria-label="Show present simple examples">\n        %s\n      </g>' % T.NOW_COL)
    defs = ('        <linearGradient id="fpFade%s" x1="0" y1="0" x2="0" y2="1">\n'
            '          <stop offset="0" stop-color="#8A8A8A"/>\n'
            '          <stop offset="0.42" stop-color="#5A5A5A"/>\n'
            '          <stop offset="0.78" stop-color="#333333"/>\n'
            '          <stop offset="1" stop-color="#1C1C1C"/>\n'
            '        </linearGradient>\n'
            '        <marker id="seq-%s" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" '
            'markerHeight="6" orient="auto">\n'
            '          <path d="M0,1 L9,5 L0,9 z" fill="%s"/>\n        </marker>' % (uid, uid, W_INK))
    body = '''      %s
      %s
      %s
      <line x1="458" y1="170" x2="540" y2="170" stroke="%s" stroke-width="1.6" marker-end="url(#seq-%s)"/>
      <text x="499" y="160" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="%s" pointer-events="none">before</text>
      <line x1="552" y1="80" x2="552" y2="299" stroke="%s" stroke-width="1.8" stroke-dasharray="5 4"/>
      <circle cx="552" cy="299" r="4.5" fill="%s"/>
      <text x="552" y="72" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" font-weight="700" fill="%s" letter-spacing="1.4" pointer-events="none">BY THEN</text>
      <text x="424" y="254" text-anchor="middle" class="diagram-caption" fill="#EDEDED" style="font-size:11px;letter-spacing:.02em" pointer-events="none">WILL</text>
      <text x="424" y="270" text-anchor="middle" class="diagram-caption" fill="#EDEDED" style="font-size:11px;letter-spacing:.02em" pointer-events="none">HAVE</text>
      <text x="424" y="286" text-anchor="middle" class="diagram-caption" fill="#EDEDED" style="font-size:11px;letter-spacing:.02em" pointer-events="none">DONE</text>
      %s''' % (
        baseline(uid),
        now,
        block,
        W_INK, uid, W_INK,
        W_INK, W_INK, W_INK,
        cap(424, 'already done', '#8A8A8A'),
    )
    return shell(uid, defs, body,
                 'A timeline from past to future. A dark grey block stands in future time and ends '
                 'before a dashed appointment further along the line, with an arrow between them '
                 'reading before. Now is a narrow column at the centre.',
                 cls='hero-diagram' if not groups else '')
