# -*- coding: utf-8 -*-
"""The clouds: grammar that sits off the route rather than on it.

These are not tenses, so they do not get a tense colour. They get the sky —
the slate of the clouds already drawn on the route map — and each one is shaped
to the single idea that makes it hard:

  used to        a block that stops dead, with nothing at NOW. The whole
                 meaning is the gap between the block and the column.
  be used to     a band that runs straight through NOW, because it is a state,
                 not a habit — it describes how you are, right now.
"""
import sys
sys.path.insert(0, 'lesson-template')
import sherpa_timeline as T

ARROW = ('        <marker id="ah-%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
         'markerHeight="7" orient="auto-start-reverse">\n'
         '          <path d="M0,0 L10,5 L0,10 z" fill="#1c130c"/>\n        </marker>')

BROWN_DARK, BROWN = "#7A5A3E", "#B08968"


def peg(x, label, top=118):
    return ('<rect x="%g" y="%g" width="13" height="%g" fill="%s"/>\n'
            '      <rect x="%g" y="%g" width="8" height="%g" fill="%s"/>\n'
            '      <text x="%g" y="%g" text-anchor="middle" font-family="Inter, sans-serif" '
            'font-size="10.5" font-weight="700" fill="%s" letter-spacing="1.4" '
            'pointer-events="none">%s</text>'
            % (x - 6.5, top, 299 - top, BROWN_DARK, x - 4, top + 2.5, 299 - top - 5, BROWN,
               x, top - 8, BROWN_DARK, label))


def shell(uid, defs, body, aria, groups):
    return '''<svg%s viewBox="0 0 640 344" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="%s">
      <defs>
%s
%s
      </defs>
      <rect x="0" y="0" width="640" height="344" fill="var(--paper)"/>
%s
      <text x="150" y="26" text-anchor="middle" class="diagram-caption" fill="#8A8175" style="letter-spacing:.14em" pointer-events="none">PAST</text>
      <text x="320" y="26" text-anchor="middle" class="diagram-caption" fill="#3E6A85" pointer-events="none">NOW</text>
      <text x="490" y="26" text-anchor="middle" class="diagram-caption" fill="#8A8175" style="letter-spacing:.14em" pointer-events="none">FUTURE</text>
    </svg>''' % ('' if groups else ' class="hero-diagram"', aria, defs, ARROW % uid, body)


def baseline(uid):
    return ('<line x1="24" y1="299" x2="616" y2="299" stroke="#1c130c" stroke-width="2"\n'
            '            marker-start="url(#ah-%s)" marker-end="url(#ah-%s)"/>' % (uid, uid))


def cap(x, text, fill, y=317, size=11.5, weight=400):
    return ('<text x="%g" y="%g" text-anchor="middle" font-family="Inter, sans-serif" font-size="%g" '
            'font-weight="%d" fill="%s" pointer-events="none">%s</text>' % (x, y, size, weight, fill, text))


# ── used to ──────────────────────────────────────────────────────────
U_STOPS = [("0", "#7FA6B6"), ("0.42", "#4A6E80"), ("0.78", "#22323B"), ("1", "#131C21")]


def used_to(uid='ut', groups=False):
    grad = ('        <linearGradient id="ut%s" x1="0" y1="0" x2="0" y2="1">\n' % uid
            + "\n".join('          <stop offset="%s" stop-color="%s"/>' % s for s in U_STOPS)
            + '\n        </linearGradient>')
    block = '<rect x="72" y="38" width="126" height="261" fill="url(#ut%s)"/>' % uid
    gone = ('<rect x="230" y="38" width="82" height="261" rx="4" fill="none" stroke="#A8B6BD" '
            'stroke-width="1.6" stroke-dasharray="4 6"/>')
    if groups:
        block = ('<g class="diagram-shape" id="shape-then" tabindex="0" role="button" '
                 'aria-label="Show used to examples">\n        %s\n      </g>' % block)
        gone = ('<g class="diagram-shape" id="shape-gone" tabindex="0" role="button" '
                'aria-label="Show the not-any-more examples">\n        %s\n      </g>' % gone)
    body = '''      %s
      %s
      %s
      %s
      <line x1="198" y1="38" x2="198" y2="299" stroke="#C2412F" stroke-width="2.5"/>
      <text x="265" y="112" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#C2412F" pointer-events="none">it stopped</text>
      <text x="271" y="176" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" fill="#8496A0" pointer-events="none">not any more</text>
      <text x="135" y="66" text-anchor="middle" class="diagram-caption" fill="#EAF1F4" style="font-size:12.5px;letter-spacing:.04em" pointer-events="none">USED TO</text>
      %s
      %s''' % (
        baseline(uid), block, gone, T.NOW_COL,
        cap(135, 'a habit or a state, over and done', '#5E7683'),
        cap(460, 'nothing of it reaches now', '#9AAAB2'),
    )
    return shell(uid, grad, body,
                 'A timeline. A slate block fills past time and stops dead at a red line, with a dashed '
                 'empty box after it marking what is no longer true. Nothing reaches the NOW column.',
                 groups)


# ── be used to + -ing ────────────────────────────────────────────────
B_PALE, B_MARK, B_INK = "#DCD8EC", "#7A6E9B", "#4C4270"


def be_used_to(uid='but', groups=False):
    band = '<rect x="96" y="196" width="448" height="103" fill="%s"/>' % B_PALE
    dots = "\n        ".join(
        '<circle cx="%d" cy="247" r="5" fill="%s" opacity="%.2f"/>' % (x, B_MARK, o)
        for x, o in zip(range(126, 530, 26), [min(1.0, 0.22 + i * 0.055) for i in range(16)]))
    zone = ('<rect x="200" y="118" width="111.5" height="64" rx="3" fill="%s"/>\n'
            '      <text x="255.75" y="146" text-anchor="middle" class="diagram-caption" fill="#FFFFFF" '
            'style="font-size:12.5px;letter-spacing:.04em" pointer-events="none">NOT STRANGE</text>\n'
            '      <text x="255.75" y="168" text-anchor="middle" font-family="Inter, sans-serif" '
            'font-size="10.5" fill="#E4DFF3" pointer-events="none">how you are now</text>' % B_MARK)
    if groups:
        band = ('<g class="diagram-shape" id="shape-state" tabindex="0" role="button" '
                'aria-label="Show be used to examples">\n        %s\n      </g>' % band)
        zone = ('<g class="diagram-shape" id="shape-nowstate" tabindex="0" role="button" '
                'aria-label="Show the present state examples">\n        %s\n      </g>' % zone)
    body = '''      %s
        %s
      %s
      %s
      %s
      %s
      %s''' % (
        band, dots, baseline(uid), zone, peg(96, 'AT FIRST'), T.NOW_COL,
        cap(200, 'strange at first, then normal', '#6E6490') + '\n      '
        + cap(450, 'and it stays that way', '#9A92B4'),
    )
    return shell(uid, '', body,
                 'A timeline. A pale violet band of familiarity runs from a brown starting peg in the '
                 'past, straight through the NOW column and on into the future, with dots growing more '
                 'solid along it. A violet zone above marks the present state: not strange any more.',
                 groups)
