# -*- coding: utf-8 -*-
"""The two continuous camps' diagrams.

Both are the camp-one ripple moved along the shared line, because that is what
a continuous tense is: something spread out around a moment rather than
occupying a block of it. Camp six puts the ripple behind NOW and drives a thin
past-simple bar into it — the interruption, which is the whole grammar point.
Camp nine puts the ripple ahead of NOW and marks the appointed moment inside
it, because the future continuous is always answering "at what time?".
"""
import sys
sys.path.insert(0, 'lesson-template')
import sherpa_timeline as T

ARROW = ('        <marker id="ah-%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
         'markerHeight="7" orient="auto-start-reverse">\n'
         '          <path d="M0,0 L10,5 L0,10 z" fill="#1c130c"/>\n        </marker>')


def dome(gid, cx, r, ring, rings=8, dashed=False):
    out = ['<circle cx="%d" cy="299" r="%d" fill="url(#%s)"/>' % (cx, r, gid)]
    for k in range(1, rings + 1):
        d = ' stroke-dasharray="4 5"' if dashed else ''
        out.append('<circle cx="%d" cy="299" r="%.1f" fill="none" stroke="%s" stroke-width="1"%s '
                   'opacity="%.2f"/>' % (cx, r * k / rings, ring, d, 0.42 - 0.03 * k))
    return "\n      ".join(out)


def shell(uid, defs, body, aria, cls='hero-diagram'):
    return '''<svg%s viewBox="0 0 640 344" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="%s">
      <defs>
%s
%s
        <clipPath id="above-%s"><rect x="0" y="0" width="640" height="299"/></clipPath>
      </defs>
      <rect x="0" y="0" width="640" height="344" fill="var(--paper)"/>
%s
      <text x="150" y="26" text-anchor="middle" class="diagram-caption" fill="#8A8175" style="letter-spacing:.14em" pointer-events="none">PAST</text>
      <text x="320" y="26" text-anchor="middle" class="diagram-caption" fill="#3E6A85" pointer-events="none">NOW</text>
      <text x="490" y="26" text-anchor="middle" class="diagram-caption" fill="#8A8175" style="letter-spacing:.14em" pointer-events="none">FUTURE</text>
    </svg>''' % ((' class="%s"' % cls) if cls else '', aria, defs, ARROW % uid, uid, body)


# ── camp six · past continuous ───────────────────────────────────────
YELLOW = [("0%", "#8A6A00"), ("16%", "#D9AE00"), ("38%", "#FFD400"),
          ("64%", "#FFE87A"), ("100%", "#FFF7D1")]

def camp_six(uid='pc'):
    defs = T.radial_defs('pcGlow' + uid, YELLOW)
    body = '''      <g clip-path="url(#above-%s)">
      %s
      <rect x="196" y="118" width="13" height="150" fill="#7A5A3E"/>
      <rect x="198.5" y="120.5" width="8" height="145" fill="#B08968"/>
      </g>
      <line x1="24" y1="299" x2="616" y2="299" stroke="#1c130c" stroke-width="2"
            marker-start="url(#ah-%s)" marker-end="url(#ah-%s)"/>
      %s
      <text x="112" y="188" text-anchor="middle" class="diagram-caption" fill="#6B5200" style="letter-spacing:.06em" pointer-events="none">WAS DOING</text>
      <text x="150" y="319" text-anchor="middle" font-family="Inter, sans-serif" font-size="11.5" fill="#8A7A4A" pointer-events="none">already running, no start and no end in view</text>
      <text x="253" y="112" text-anchor="middle" font-family="Inter, sans-serif" font-size="11.5" font-weight="700" fill="#7A5A3E" pointer-events="none">past simple &#8212; the interruption</text>
      <text x="320" y="319" text-anchor="middle" font-family="Inter, sans-serif" font-size="11.5" fill="#5F7C90" pointer-events="none">present simple</text>''' % (
        uid, dome('pcGlow' + uid, 150, 118, '#C79A00'), uid, uid, T.NOW_COL)
    return shell(uid, defs, body,
                 'A timeline from past to future. A yellow ripple spreads through past time, '
                 'and a thin brown bar drops into it partway down: the past simple interrupting '
                 'the past continuous. Now is a narrow column at the centre.')


# ── camp nine · future continuous ────────────────────────────────────
AMBER = [("0%", "#7A5200"), ("16%", "#C98A00"), ("38%", "#F0A500"),
         ("64%", "#FFD48A"), ("100%", "#FFF0D6")]

def camp_nine(uid='fc'):
    defs = T.radial_defs('fcGlow' + uid, AMBER)
    body = '''      <g clip-path="url(#above-%s)">
      %s
      </g>
      <line x1="24" y1="299" x2="616" y2="299" stroke="#1c130c" stroke-width="2"
            marker-start="url(#ah-%s)" marker-end="url(#ah-%s)"/>
      <line x1="490" y1="150" x2="490" y2="299" stroke="#5B4A2A" stroke-width="1.6" stroke-dasharray="5 4"/>
      <circle cx="490" cy="299" r="4.5" fill="#5B4A2A"/>
      %s
      <text x="490" y="188" text-anchor="middle" class="diagram-caption" fill="#6B4A00" style="letter-spacing:.06em" pointer-events="none">WILL BE DOING</text>
      <text x="490" y="142" text-anchor="middle" font-family="Inter, sans-serif" font-size="11.5" font-weight="700" fill="#5B4A2A" pointer-events="none">the appointed moment</text>
      <text x="490" y="319" text-anchor="middle" font-family="Inter, sans-serif" font-size="11.5" fill="#8A7A4A" pointer-events="none">already under way when you get there</text>
      <text x="320" y="319" text-anchor="middle" font-family="Inter, sans-serif" font-size="11.5" fill="#5F7C90" pointer-events="none">present simple</text>''' % (
        uid, dome('fcGlow' + uid, 490, 118, '#C98A00', dashed=True), uid, uid, T.NOW_COL)
    return shell(uid, defs, body,
                 'A timeline from past to future. An amber ripple spreads through future time '
                 'with a dashed line marking a single appointed moment inside it. Now is a '
                 'narrow column at the centre.')
