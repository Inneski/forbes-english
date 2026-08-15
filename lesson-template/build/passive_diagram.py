# -*- coding: utf-8 -*-
"""The descent: the same timelines, inverted, with the doer let go.

Coming down the mountain the geometry does not change — same line, same NOW
column, same block in the same place — because the tense has not changed. Only
the light has: dark paper, and the block lit from above instead of fading into
the dark. What is added is the ghost: a dashed box for the agent, standing
where 'by somebody' would go, drawn as an outline because most of the time
nobody says it.
"""
import sys
sys.path.insert(0, 'lesson-template')
import sherpa_timeline as T

NOW_COL_DARK = ('<rect x="311.5" y="38" width="17.0" height="261" fill="#D98A72"/>\n'
                '      <rect x="314.0" y="40.5" width="12.0" height="256" fill="#4A6379"/>')


def gradient(gid, stops):
    rows = "\n".join('          <stop offset="%s" stop-color="%s"/>' % (o, c) for o, c in stops)
    return ('        <linearGradient id="%s" x1="0" y1="0" x2="0" y2="1">\n%s\n'
            '        </linearGradient>' % (gid, rows))


def descent(uid, gid_stops, block_x, caption, reveal, agent_label, ink, ghost_ink,
            groups=False, aria=""):
    bx, bw = block_x, 95
    cx = bx + bw / 2
    gx, gw = bx + 8, bw - 16           # the by-phrase, tucked inside the event itself

    block = '<rect x="%g" y="38" width="%g" height="261" fill="url(#dg%s)"/>' % (bx, bw, uid)
    ghost = ('<rect x="%g" y="190" width="%g" height="98" rx="4" fill="none" stroke="%s" '
             'stroke-width="1.5" stroke-dasharray="5 4" opacity="0.9"/>' % (gx, gw, ghost_ink))
    if groups:
        block = ('<g class="diagram-shape" id="shape-event" tabindex="0" role="button" '
                 'aria-label="Show passive examples">\n        %s\n      </g>' % block)
        ghost = ('<g class="diagram-shape" id="shape-agent" tabindex="0" role="button" '
                 'aria-label="Show by-phrase examples">\n        %s\n      </g>' % ghost)

    return '''<svg%s viewBox="0 0 640 344" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="%s">
      <defs>
%s
        <marker id="ah-%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
          <path d="M0,0 L10,5 L0,10 z" fill="#C9BCAE"/>
        </marker>
      </defs>
      <rect x="0" y="0" width="640" height="344" fill="var(--paper)"/>
      <line x1="24" y1="299" x2="616" y2="299" stroke="#C9BCAE" stroke-width="2"
            marker-start="url(#ah-%s)" marker-end="url(#ah-%s)"/>
      %s
      %s
      %s
      <text x="%g" y="216" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" font-weight="700" fill="%s" letter-spacing="1.4" pointer-events="none">%s</text>
      <text x="150" y="26" text-anchor="middle" class="diagram-caption" fill="#9C8E7F" style="letter-spacing:.14em" pointer-events="none">PAST</text>
      <text x="320" y="26" text-anchor="middle" class="diagram-caption" fill="#8FB2C6" pointer-events="none">NOW</text>
      <text x="490" y="26" text-anchor="middle" class="diagram-caption" fill="#9C8E7F" style="letter-spacing:.14em" pointer-events="none">FUTURE</text>
      <text x="%g" y="66" text-anchor="middle" class="diagram-caption" fill="#3A2A1C" style="font-size:12.5px;letter-spacing:.03em" pointer-events="none">%s</text>
      <text x="%g" y="317" text-anchor="middle" font-family="Inter, sans-serif" font-size="11.5" fill="%s" pointer-events="none">%s</text>
      <text x="%g" y="245" text-anchor="middle" font-family="Inter, sans-serif" font-size="10" fill="%s" pointer-events="none">doer usually</text>
      <text x="%g" y="261" text-anchor="middle" font-family="Inter, sans-serif" font-size="10" fill="%s" pointer-events="none">left out</text>
    </svg>''' % (
        '' if groups else ' class="hero-diagram"', aria,
        gradient('dg' + uid, gid_stops), uid, uid, uid,
        NOW_COL_DARK, block, ghost,
        cx, ghost_ink, agent_label,
        cx, caption,
        cx, ink, reveal,
        cx, ghost_ink,
        cx, ghost_ink,
    )


# ── descent three · past simple passive ──────────────────────────────
BROWN_UP = [("0", "#E3C3A4"), ("0.42", "#C79A72"), ("0.78", "#8A6A4C"), ("1", "#5E4632")]


def past_simple_passive(uid='psp', groups=False):
    return descent(uid, BROWN_UP, 102.5, 'WAS DONE', 'the event, still the subject',
                   'BY&#8230;', '#C9A882', '#EBD3B8', groups,
                   'A timeline on dark paper. A brown block stands in past time carrying the passive '
                   'event, with a dashed box inside it for the agent — the by-phrase that is '
                   'usually left out. Now is a narrow column to the right.')
