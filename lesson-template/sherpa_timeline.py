# -*- coding: utf-8 -*-
"""One timeline diagram, shared by every Sherpa Tensing camp that needs it.

The geometry is fixed so the camps read as one series: the same NOW column in
the same place at the same size, the same arrowed line through it, and PAST /
FUTURE sitting level with NOW on either side. Only the block and the colour
change from camp to camp — which is the whole point: you can see at a glance
where a tense lives relative to the moment you are speaking.
"""

VIEWBOX = "0 0 640 344"
BASE_Y = 299          # the ground line
TOP_Y = 38            # top of every standing block
NOW_X = 320           # centre of the NOW column
LABEL_Y = 26          # baseline shared by PAST, NOW and FUTURE
PAST_LABEL_X = 150
FUTURE_LABEL_X = 490
REVEAL_Y = 317        # the caption that fades in under the line

# The NOW column is camp three's, unchanged and unscaled — coral behind blue.
NOW_COL = (
    '<rect x="311.5" y="38" width="17.0" height="261" fill="#D98A72"/>\n'
    '      <rect x="314.0" y="40.5" width="12.0" height="256" fill="#5C7690"/>'
)

# Blocks sit centred under their label, so the eye pairs them automatically.
# Narrow, and set well clear of the NOW column: the gap is doing work — it is
# the distance between where you are standing and where the tense lives. A
# block that crowds NOW reads as "soon", which is not what any of these mean.
PAST_BLOCK = dict(x=102.5, width=95)
FUTURE_BLOCK = dict(x=442.5, width=95)


def gradient(gid, stops):
    rows = "\n".join(
        '          <stop offset="%s" stop-color="%s"/>' % (o, c) for o, c in stops
    )
    return (
        '        <linearGradient id="%s" x1="0" y1="0" x2="0" y2="1">\n%s\n'
        '        </linearGradient>' % (gid, rows)
    )


def ramp(accent, mid, deep, floor):
    return [("0", accent), ("0.42", mid), ("0.78", deep), ("1", floor)]


def radial_defs(gid, stops):
    rows = "\n".join(
        '          <stop offset="%s" stop-color="%s"/>' % (o, c) for o, c in stops
    )
    return ('        <radialGradient id="%s" cx="50%%" cy="50%%" r="50%%">\n%s\n'
            '        </radialGradient>' % (gid, rows))


def ripple(gid, cx, r, ring_colour, rings=7, dashed=False):
    """A ripple spreading from a point on the line — camp one's motif, reused
    here so the future arrangement is visibly the same event as the present
    one, just standing further along the line."""
    out = ['<circle cx="%g" cy="%d" r="%g" fill="url(#%s)"/>' % (cx, BASE_Y, r, gid)]
    for k in range(1, rings + 1):
        rr = r * k / rings
        dash = ' stroke-dasharray="4 5"' if dashed else ''
        out.append('<circle cx="%g" cy="%d" r="%g" fill="none" stroke="%s" '
                   'stroke-width="1"%s opacity="%.2f"/>'
                   % (cx, BASE_Y, rr, ring_colour, dash, 0.42 - 0.03 * k))
    return "\n      ".join(out)


def diagram(gid, stops, block, caption, reveal, reveal_for,
            block_side="future", label_ink="#8A8175", extra="",
            aria="", classes="hero-diagram", groups=False):
    """Return the whole <svg>. `groups` wraps the shapes for the clickable
    version used inside the interactive camp."""
    bx = FUTURE_BLOCK if block_side == "future" else PAST_BLOCK
    if block:
        bx = dict(bx, **block)
    cx = bx["x"] + bx["width"] / 2

    block_svg = ('<rect x="%g" y="%d" width="%g" height="%d" fill="url(#%s)"/>'
                 % (bx["x"], TOP_Y, bx["width"], BASE_Y - TOP_Y, gid))
    now_svg = NOW_COL

    if groups:
        block_svg = ('<g class="diagram-shape" id="shape-%s" tabindex="0" role="button" '
                     'aria-label="Show %s examples">\n      %s\n      </g>'
                     % (reveal_for, caption.lower(), block_svg))
        now_svg = ('<g class="diagram-shape" id="shape-now" tabindex="0" role="button" '
                   'aria-label="Show present simple examples">\n      %s\n      </g>' % NOW_COL)

    return '''<svg class="%s" viewBox="%s" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="%s">
      <defs>
%s
        <marker id="ah-%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
          <path d="M0,0 L10,5 L0,10 z" fill="#1c130c"/>
        </marker>
      </defs>
      <rect x="0" y="0" width="640" height="344" fill="var(--paper)"/>
      <line x1="24" y1="%d" x2="616" y2="%d" stroke="#1c130c" stroke-width="2"
            marker-start="url(#ah-%s)" marker-end="url(#ah-%s)"/>
      %s
      %s
      <text x="%d" y="%d" text-anchor="middle" class="diagram-caption" fill="%s" style="letter-spacing:.14em" pointer-events="none">PAST</text>
      <text x="%d" y="%d" text-anchor="middle" class="diagram-caption" fill="#3E6A85" pointer-events="none">NOW</text>
      <text x="%d" y="%d" text-anchor="middle" class="diagram-caption" fill="%s" style="letter-spacing:.14em" pointer-events="none">FUTURE</text>
      <text x="%g" y="288" text-anchor="middle" class="diagram-caption" fill="#F4F1E8" style="font-size:12.5px;letter-spacing:.03em" pointer-events="none">%s</text>
      <text x="%g" y="%d" text-anchor="middle" class="dg-reveal" data-for="shape-%s" font-family="Inter, sans-serif" font-size="11.5" fill="%s" pointer-events="none">%s</text>%s
    </svg>''' % (
        classes, VIEWBOX, aria,
        gradient(gid, stops), gid,
        BASE_Y, BASE_Y, gid, gid,
        now_svg, block_svg,
        PAST_LABEL_X, LABEL_Y, label_ink,
        NOW_X, LABEL_Y,
        FUTURE_LABEL_X, LABEL_Y, label_ink,
        cx, caption,
        cx, REVEAL_Y, reveal_for, "#CFC9BC", reveal,
        extra,
    )
