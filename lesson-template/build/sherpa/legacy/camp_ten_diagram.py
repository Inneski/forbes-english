# -*- coding: utf-8 -*-
"""Camp ten's diagram: two blocks in the past, in the order they happened.

Every other camp puts one shape on the line, because every other tense needs
only one. The past perfect needs two, and the whole grammar point is which of
them comes first — so the picture is the ordinary past simple block with a
second, darker block standing *before* it, and a small arrow between them
saying which way the day ran.
"""
import sys
sys.path.insert(0, 'lesson-template')
import sherpa_timeline as T

PP_STOPS = T.ramp("#8E1730", "#6E0B24", "#3A0614", "#180208")   # past perfect
PS_STOPS = T.ramp("#B08968", "#6B4B33", "#241A12", "#100C08")   # camp three's brown

PP = dict(x=40, w=76, cx=78)
PS = dict(x=174, w=76, cx=212)


def _block(gid, b, uid, shape_id=None, aria=""):
    r = ('<rect x="%d" y="38" width="%d" height="261" fill="url(#%s%s)"/>'
         % (b["x"], b["w"], gid, uid))
    if shape_id:
        r = ('<g class="diagram-shape" id="%s" tabindex="0" role="button" aria-label="%s">\n'
             '        %s\n      </g>' % (shape_id, aria, r))
    return r


def camp_ten(uid='pp', groups=False):
    defs = "\n".join([
        T.gradient('ppFade' + uid, PP_STOPS),
        T.gradient('psFade' + uid, PS_STOPS),
    ])
    pp = _block('ppFade', PP, uid,
                'shape-earlier' if groups else None,
                'Show past perfect examples')
    ps = _block('psFade', PS, uid,
                'shape-later' if groups else None,
                'Show past simple examples')

    return '''<svg%s viewBox="0 0 640 344" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A timeline from past to future. Two blocks stand in past time: a dark red past perfect block first, then the brown past simple block, with an arrow between them showing the order. Now is a narrow column at the centre.">
      <defs>
%s
        <marker id="ah-%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
          <path d="M0,0 L10,5 L0,10 z" fill="#1c130c"/>
        </marker>
        <marker id="seq-%s" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M0,1 L9,5 L0,9 z" fill="#7A5A3E"/>
        </marker>
      </defs>
      <rect x="0" y="0" width="640" height="344" fill="var(--paper)"/>
      <line x1="24" y1="299" x2="616" y2="299" stroke="#1c130c" stroke-width="2"
            marker-start="url(#ah-%s)" marker-end="url(#ah-%s)"/>
      %s
      %s
      %s
      <line x1="122" y1="170" x2="166" y2="170" stroke="#7A5A3E" stroke-width="1.6" marker-end="url(#seq-%s)"/>
      <text x="144" y="160" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#7A5A3E" pointer-events="none">then</text>
      <text x="150" y="26" text-anchor="middle" class="diagram-caption" fill="#8A8175" style="letter-spacing:.14em" pointer-events="none">PAST</text>
      <text x="320" y="26" text-anchor="middle" class="diagram-caption" fill="#3E6A85" pointer-events="none">NOW</text>
      <text x="490" y="26" text-anchor="middle" class="diagram-caption" fill="#8A8175" style="letter-spacing:.14em" pointer-events="none">FUTURE</text>
      <text x="78" y="288" text-anchor="middle" class="diagram-caption" fill="#F4E4E8" style="font-size:12.5px;letter-spacing:.02em" pointer-events="none">HAD DONE</text>
      <text x="212" y="288" text-anchor="middle" class="diagram-caption" fill="#F1E6DC" style="font-size:12.5px;letter-spacing:.06em" pointer-events="none">DID</text>
      <text x="78" y="317" text-anchor="middle" font-family="Inter, sans-serif" font-size="11.5" fill="#A88089" pointer-events="none">the earlier one</text>
      <text x="212" y="317" text-anchor="middle" font-family="Inter, sans-serif" font-size="11.5" fill="#9C8570" pointer-events="none">the main event</text>
    </svg>''' % (
        ' class="hero-diagram"' if not groups else '',
        defs, uid, uid, uid, uid,
        T.NOW_COL, pp, ps, uid,
    )
