# -*- coding: utf-8 -*-
"""Descent diagrams that keep their tense's own shape.

The passive does not change when something happens, so the picture should not
change either. A continuous tense keeps its ripple, the perfect keeps its
layers, the past perfect keeps its two blocks. Only two things are different
on the descent: the paper is dark and the light comes from above, and inside
the shape there is a dashed box for the doer.
"""
import sys
sys.path.insert(0, 'lesson-template')
import sherpa_timeline as T

NOW_COL_DARK = ('<rect x="311.5" y="38" width="17.0" height="261" fill="#D98A72"/>\n'
                '      <rect x="314.0" y="40.5" width="12.0" height="256" fill="#4A6379"/>')
ARROW = ('        <marker id="ah-%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
         'markerHeight="7" orient="auto-start-reverse">\n'
         '          <path d="M0,0 L10,5 L0,10 z" fill="#C9BCAE"/>\n        </marker>')


def by_box(cx, ghost, top=196, w=88, h=92):
    """The doer, drawn inside whatever shape the tense has."""
    return ('<rect x="%g" y="%g" width="%g" height="%g" rx="4" fill="none" stroke="%s" '
            'stroke-width="1.5" stroke-dasharray="5 4" opacity="0.92"/>\n'
            '      <text x="%g" y="%g" text-anchor="middle" font-family="Inter, sans-serif" '
            'font-size="10.5" font-weight="700" fill="%s" letter-spacing="1.4" pointer-events="none">BY&#8230;</text>\n'
            '      <text x="%g" y="%g" text-anchor="middle" font-family="Inter, sans-serif" '
            'font-size="10" fill="%s" pointer-events="none">doer usually</text>\n'
            '      <text x="%g" y="%g" text-anchor="middle" font-family="Inter, sans-serif" '
            'font-size="10" fill="%s" pointer-events="none">left out</text>'
            % (cx - w / 2, top, w, h, ghost,
               cx, top + 26, ghost, cx, top + 55, ghost, cx, top + 71, ghost))


def radial(gid, stops):
    rows = "\n".join('          <stop offset="%s" stop-color="%s"/>' % s for s in stops)
    return ('        <radialGradient id="%s" cx="50%%" cy="50%%" r="50%%">\n%s\n'
            '        </radialGradient>' % (gid, rows))


def dome(gid, cx, r, ring, rings=8, dashed=False):
    out = ['<circle cx="%g" cy="299" r="%g" fill="url(#%s)"/>' % (cx, r, gid)]
    for k in range(1, rings + 1):
        d = ' stroke-dasharray="4 5"' if dashed else ''
        out.append('<circle cx="%g" cy="299" r="%.1f" fill="none" stroke="%s" stroke-width="1"%s '
                   'opacity="%.2f"/>' % (cx, r * k / rings, ring, d, 0.44 - 0.03 * k))
    return "\n      ".join(out)


def shell(uid, defs, body, aria, groups, caps):
    lab = ('\n      <text x="150" y="26" text-anchor="middle" class="diagram-caption" fill="#9C8E7F" style="letter-spacing:.14em" pointer-events="none">PAST</text>'
           '\n      <text x="320" y="26" text-anchor="middle" class="diagram-caption" fill="#8FB2C6" pointer-events="none">NOW</text>'
           '\n      <text x="490" y="26" text-anchor="middle" class="diagram-caption" fill="#9C8E7F" style="letter-spacing:.14em" pointer-events="none">FUTURE</text>')
    return ('<svg%s viewBox="0 0 640 344" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="%s">\n'
            '      <defs>\n%s\n%s\n        <clipPath id="above-%s"><rect x="0" y="0" width="640" height="299"/></clipPath>\n      </defs>\n'
            '      <rect x="0" y="0" width="640" height="344" fill="var(--paper)"/>\n%s%s\n%s\n    </svg>'
            % ('' if groups else ' class="hero-diagram"', aria, defs, ARROW % uid, uid, body, lab, caps))


def baseline(uid):
    return ('<line x1="24" y1="299" x2="616" y2="299" stroke="#C9BCAE" stroke-width="2"\n'
            '            marker-start="url(#ah-%s)" marker-end="url(#ah-%s)"/>' % (uid, uid))


def cap(x, text, fill, y=317, size=11.5, weight=400):
    return ('      <text x="%g" y="%g" text-anchor="middle" font-family="Inter, sans-serif" font-size="%g" '
            'font-weight="%d" fill="%s" pointer-events="none">%s</text>' % (x, y, size, weight, fill, text))


def wrap(sid, aria, inner):
    return ('<g class="diagram-shape" id="%s" tabindex="0" role="button" aria-label="%s">\n'
            '        %s\n      </g>' % (sid, aria, inner))


# ── present continuous passive: camp one's ripple, at NOW ────────────
def pc_passive(uid='pcp', groups=False):
    stops = [("0%", "#FBD9E5"), ("18%", "#F09BBB"), ("42%", "#D14C7E"),
             ("70%", "#7A1638"), ("100%", "#3A0A1C")]
    d = radial('pcpG' + uid, stops)
    shape = '<g clip-path="url(#above-%s)">\n      %s\n      </g>' % (uid, dome('pcpG' + uid, 320, 122, '#E07FA6'))
    ghost = by_box(255, '#F3C4D6')
    if groups:
        shape = wrap('shape-event', 'Show passive examples', shape)
        ghost = wrap('shape-agent', 'Show by-phrase examples', ghost)
    body = '''      %s
      %s
      %s
      %s
      <text x="320" y="120" text-anchor="middle" class="diagram-caption" fill="#FBD9E5" style="font-size:12.5px;letter-spacing:.03em" pointer-events="none">IS BEING DONE</text>''' % (
        shape, baseline(uid), NOW_COL_DARK, ghost)
    caps = cap(430, 'happening to it, right now', '#E58FB0')
    return shell(uid, d, body,
                 'A timeline on dark paper. A pink ripple spreads from the NOW column, with a dashed box '
                 'inside it marking the doer, usually left out.', groups, caps)


# ── past continuous passive: camp six's ripple, plus the interruption ─
def pct_passive(uid='pctp', groups=False):
    stops = [("0%", "#FFF3C0"), ("18%", "#FFE87A"), ("42%", "#D9AE00"),
             ("70%", "#6E5600"), ("100%", "#2E2400")]
    d = radial('pctpG' + uid, stops)
    shape = ('<g clip-path="url(#above-%s)">\n      %s\n'
             '      <rect x="196" y="118" width="13" height="150" fill="#5E4630"/>\n'
             '      <rect x="198.5" y="120.5" width="8" height="145" fill="#B08968"/>\n'
             '      </g>' % (uid, dome('pctpG' + uid, 150, 118, '#C79A00')))
    ghost = by_box(104, '#F5E6A8', top=196, w=84)
    if groups:
        shape = wrap('shape-event', 'Show passive examples', shape)
        ghost = wrap('shape-agent', 'Show by-phrase examples', ghost)
    body = '''      %s
      %s
      %s
      %s
      <text x="150" y="112" text-anchor="middle" class="diagram-caption" fill="#FFF3C0" style="font-size:12.5px;letter-spacing:.03em" pointer-events="none">WAS BEING DONE</text>
      <text x="262" y="86" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#C29A6E" pointer-events="none">then something cut in</text>''' % (
        shape, baseline(uid), NOW_COL_DARK, ghost)
    caps = cap(150, 'in progress, and it was happening to it', '#C7B36A')
    return shell(uid, d, body,
                 'A timeline on dark paper. A yellow ripple spreads through past time with a brown past '
                 'simple bar cutting into it, and a dashed box inside marking the doer.', groups, caps)


# ── present perfect passive: camp four's layers, arriving at now ──────
def pp_passive(uid='ppp', groups=False):
    d = ('        <linearGradient id="pppA%s" x1="0" y1="0" x2="1" y2="0">\n'
         '          <stop offset="0" stop-color="#0E2224"/>\n'
         '          <stop offset="0.34" stop-color="#12383B"/>\n'
         '          <stop offset="0.78" stop-color="#2E9198"/>\n'
         '          <stop offset="1" stop-color="#7FC8CC"/>\n        </linearGradient>' % uid)
    layers = ('<rect x="120" y="38" width="191.5" height="80" fill="#23787E"/>\n'
              '      <rect x="120" y="124" width="191.5" height="72" fill="#23787E"/>\n'
              '      <rect x="120" y="202" width="191.5" height="97" fill="url(#pppA%s)"/>' % uid)
    ghost = by_box(200, '#BFE4E6', top=210, w=88, h=80)
    if groups:
        layers = wrap('shape-event', 'Show passive examples', layers)
        ghost = wrap('shape-agent', 'Show by-phrase examples', ghost)
    body = '''      %s
      %s
      %s
      %s
      <text x="215.75" y="88" text-anchor="middle" class="diagram-caption" fill="#DFF3F4" style="font-size:12.5px;letter-spacing:.03em" pointer-events="none">HAS BEEN DONE</text>
      <text x="215.75" y="168" text-anchor="middle" font-family="Inter, sans-serif" font-size="11.5" fill="#BFE4E6" pointer-events="none">unspecified time &#183; still relevant</text>''' % (
        layers, baseline(uid), NOW_COL_DARK, ghost)
    caps = cap(215.75, 'finished, and it lands on now', '#8FD0D4')
    return shell(uid, d, body,
                 'A timeline on dark paper. Three turquoise layers run through past time and arrive at '
                 'the NOW column, with a dashed box in the lowest layer marking the doer.', groups, caps)


# ── past perfect passive: camp ten's two blocks, in order ────────────
def ppf_passive(uid='ppfp', groups=False):
    d = ('        <linearGradient id="ppfpA%s" x1="0" y1="0" x2="0" y2="1">\n'
         '          <stop offset="0" stop-color="#D48CA1"/><stop offset="0.42" stop-color="#8E1730"/>\n'
         '          <stop offset="0.78" stop-color="#3E0614"/><stop offset="1" stop-color="#20030A"/>\n'
         '        </linearGradient>\n'
         '        <linearGradient id="ppfpB%s" x1="0" y1="0" x2="0" y2="1">\n'
         '          <stop offset="0" stop-color="#E3C3A4"/><stop offset="0.42" stop-color="#B08968"/>\n'
         '          <stop offset="0.78" stop-color="#5E4632"/><stop offset="1" stop-color="#332619"/>\n'
         '        </linearGradient>\n'
         '        <marker id="seq-%s" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">\n'
         '          <path d="M0,1 L9,5 L0,9 z" fill="#C29A6E"/>\n        </marker>' % (uid, uid, uid))
    earlier = '<rect x="40" y="38" width="106" height="261" fill="url(#ppfpA%s)"/>' % uid
    later = '<rect x="190" y="38" width="76" height="261" fill="url(#ppfpB%s)"/>' % uid
    ghost = by_box(93, '#E9B8C4', top=196, w=88)
    if groups:
        earlier = wrap('shape-event', 'Show passive examples', earlier)
        ghost = wrap('shape-agent', 'Show by-phrase examples', ghost)
    body = '''      %s
      %s
      %s
      %s
      %s
      <line x1="152" y1="170" x2="184" y2="170" stroke="#C29A6E" stroke-width="1.6" marker-end="url(#seq-%s)"/>
      <text x="168" y="160" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#C29A6E" pointer-events="none">then</text>
      <text x="93" y="70" text-anchor="middle" class="diagram-caption" fill="#F6DCE3" style="font-size:12px;letter-spacing:.02em" pointer-events="none">HAD BEEN DONE</text>
      <text x="228" y="70" text-anchor="middle" class="diagram-caption" fill="#F5E7DA" style="font-size:12px;letter-spacing:.04em" pointer-events="none">DID</text>''' % (
        baseline(uid), earlier, later, NOW_COL_DARK, ghost, uid)
    caps = cap(93, 'over before you got there', '#D9899F') + '\n' + cap(228, 'then this', '#C7A184')
    return shell(uid, d, body,
                 'A timeline on dark paper. A dark red block stands early in past time with a dashed doer '
                 'box inside it, then a brown past simple block, with an arrow reading then between them.',
                 groups, caps)


# ── future perfect passive: camp twelve's block and its deadline ─────
def fpf_passive(uid='fpfp', groups=False):
    d = ('        <linearGradient id="fpfpA%s" x1="0" y1="0" x2="0" y2="1">\n'
         '          <stop offset="0" stop-color="#C4C4C4"/><stop offset="0.42" stop-color="#7A7A7A"/>\n'
         '          <stop offset="0.78" stop-color="#333333"/><stop offset="1" stop-color="#1C1C1C"/>\n'
         '        </linearGradient>\n'
         '        <marker id="seq-%s" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">\n'
         '          <path d="M0,1 L9,5 L0,9 z" fill="#B4B4B4"/>\n        </marker>' % (uid, uid))
    block = '<rect x="376" y="38" width="106" height="261" fill="url(#fpfpA%s)"/>' % uid
    ghost = by_box(429, '#DCDCDC', top=196, w=90)
    if groups:
        block = wrap('shape-event', 'Show passive examples', block)
        ghost = wrap('shape-agent', 'Show by-phrase examples', ghost)
    body = '''      %s
      %s
      %s
      %s
      <line x1="490" y1="150" x2="540" y2="150" stroke="#B4B4B4" stroke-width="1.6" marker-end="url(#seq-%s)"/>
      <text x="515" y="140" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#B4B4B4" pointer-events="none">before</text>
      <line x1="552" y1="80" x2="552" y2="299" stroke="#B4B4B4" stroke-width="1.8" stroke-dasharray="5 4"/>
      <circle cx="552" cy="299" r="4.5" fill="#B4B4B4"/>
      <text x="552" y="72" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" font-weight="700" fill="#B4B4B4" letter-spacing="1.4" pointer-events="none">BY THEN</text>
      <text x="429" y="72" text-anchor="middle" class="diagram-caption" fill="#EDEDED" style="font-size:11px;letter-spacing:0" pointer-events="none">WILL HAVE BEEN DONE</text>''' % (
        baseline(uid), NOW_COL_DARK, block, ghost, uid)
    caps = cap(429, 'already done when you arrive', '#B4B4B4')
    return shell(uid, d, body,
                 'A timeline on dark paper. A grey block stands in future time with a dashed doer box '
                 'inside it, ending before a dashed deadline further along the line.', groups, caps)
