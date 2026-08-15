# -*- coding: utf-8 -*-
"""Face & neck — profile view.

A profile is the right view for this set. Temple, chin and the line of
the throat are all ambiguous head-on, and the nostril and lip read
unmistakably from the side.

Proportions follow the standard artist's canon so the thing looks like a
head rather than a blob: eye line at the vertical midpoint of the skull,
nose base halfway from the eye line to the chin, mouth a third of the way
from the nose base to the chin, and the ear spanning eye line to nose
base. Head depth is about four-fifths of head height.
"""
W, H = 1280, 720
CREAM, NAVY, PINK, MUTE = '#f4eee2', '#1b2340', '#ef4b6b', '#3c4a72'

# canon
TOP, CHIN = 132, 470
EYE = (TOP + CHIN) / 2          # 301
NOSE = EYE + (CHIN - EYE) / 2   # 385.5
MOUTH = NOSE + (CHIN - NOSE) / 3

def leader(x1, y1, x2, y2, tx, ty, text, anchor='start'):
    return (f'  <polyline class="lead" points="{x1},{y1} {x2},{y2}"/>\n'
            f'  <circle class="dot" cx="{x1}" cy="{y1}" r="4.5"/>\n'
            f'  <text class="lbl" x="{tx}" y="{ty}" text-anchor="{anchor}">{text}</text>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Labelled profile of the head and neck">
<title>Face and neck</title>
<style>
  .bg   {{ fill: {CREAM}; }}
  .body {{ fill: {NAVY}; }}
  .cut  {{ fill: {PINK}; }}
  .soft {{ fill: {PINK}; opacity: .42; }}
  .mute {{ fill: {MUTE}; }}
  .lead {{ fill: none; stroke: {NAVY}; stroke-width: 1.6; opacity: .7; }}
  .dot  {{ fill: {PINK}; stroke: {CREAM}; stroke-width: 1.5; }}
  .lbl  {{ font-family: 'DM Sans', system-ui, sans-serif; font-size: 21px;
           font-weight: 600; fill: {NAVY}; }}
  .ttl  {{ font-family: 'Playfair Display', Georgia, serif; font-size: 34px;
           font-weight: 700; fill: {NAVY}; }}
  .sub  {{ font-family: 'DM Mono', ui-monospace, monospace; font-size: 12.5px;
           letter-spacing: .14em; fill: {PINK}; }}
</style>
<rect class="bg" x="0" y="0" width="{W}" height="{H}"/>
<text class="sub" x="64" y="64">FORBES ENGLISH · C1 BODY PARTS</text>
<text class="ttl" x="64" y="104">Face &amp; neck</text>

<!-- ── head and neck, profile, facing right ─────────────────────── -->
<path class="body" d="
  M 452 470
  C 414 430 400 372 402 316
  C 404 240 452 132 528 132
  C 578 132 606 176 610 226
  L 611 288
  C 612 296 616 300 622 304
  L 646 372
  C 650 380 646 386 638 388
  L 616 392
  C 612 400 614 406 620 410
  C 610 414 600 416 596 420
  C 604 424 612 428 616 434
  C 606 442 596 446 592 452
  L 596 462
  C 600 470 596 476 588 476
  L 566 480
  C 552 496 528 504 496 500
  L 500 566
  C 500 606 524 628 566 644
  L 640 668
  L 640 720 L 360 720 L 360 668
  L 424 646
  C 458 630 472 606 472 566
  L 472 496
  C 472 490 460 482 452 470 Z"/>

<!-- ear: spans eye line to nose base, set behind the jaw hinge -->
<ellipse class="mute" cx="458" cy="332" rx="18" ry="32"/>
<path class="bg" d="M 452 316 q 13 5 10 22 q -3 15 -13 17 l 0 -7 q 8 -3 10 -13 q 2 -12 -10 -13 Z" opacity=".35"/>

<!-- brow ridge and eyebrow -->
<path class="cut" d="M 552 {EYE-20:.0f} q 32 -10 52 3 l -3 10 q -22 -10 -47 -2 Z"/>
<!-- eye + lid -->
<ellipse class="mute" cx="572" cy="{EYE+6:.0f}" rx="22" ry="12"/>
<!-- eyelashes fringe the lid, angled forward -->
<g class="cut">
  <rect x="556" y="{EYE-2:.0f}" width="3" height="11" transform="rotate(-42 556 {EYE-2:.0f})"/>
  <rect x="568" y="{EYE-5:.0f}" width="3" height="12" transform="rotate(-30 568 {EYE-5:.0f})"/>
  <rect x="580" y="{EYE-6:.0f}" width="3" height="12" transform="rotate(-18 580 {EYE-6:.0f})"/>
  <rect x="592" y="{EYE-4:.0f}" width="3" height="11" transform="rotate(-6 592 {EYE-4:.0f})"/>
</g>
<!-- temple: the flat area behind the eye, in front of the ear -->
<circle class="soft" cx="512" cy="{EYE-10:.0f}" r="19"/>
<!-- nostril, on the underside of the nose -->
<path class="cut" d="M 620 {NOSE-2:.0f} q 16 -4 20 6 q -14 6 -20 -6 Z"/>
<!-- lips -->
<path class="cut" d="M 590 {MOUTH-8:.0f} q 22 -6 32 -2 l -2 7 q -12 -3 -30 3 Z"/>
<path class="cut" d="M 590 {MOUTH+4:.0f} q 20 6 30 0 l -4 9 q -12 4 -26 -2 Z"/>
<!-- throat: the internal passage down the front of the neck -->
<path class="cut" d="M 516 510 q 20 8 24 32 l 0 82 l -26 -9 l 0 -74 q -2 -19 2 -31 Z" opacity=".8"/>

{leader(500, 210, 300, 190, 288, 196, 'forehead', 'end')}
{leader(512, 291, 300, 268, 288, 274, 'temple', 'end')}
{leader(578, 287, 300, 346, 288, 352, 'eyebrow', 'end')}
{leader(578, 306, 300, 424, 288, 430, 'eyelash', 'end')}
{leader(630, 388, 900, 356, 916, 362, 'nostril')}
{leader(612, 424, 900, 440, 916, 446, 'lip')}
{leader(594, 464, 900, 524, 916, 530, 'chin')}
{leader(528, 582, 900, 608, 916, 614, 'throat')}
{leader(452, 600, 300, 600, 288, 606, 'neck', 'end')}
</svg>
'''
open('/home/claude/forbes-english/BodyParts/face-neck.svg','w',encoding='utf-8').write(svg)
print('wrote face-neck.svg')
