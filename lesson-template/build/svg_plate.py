# -*- coding: utf-8 -*-
"""Body parts C1 — one anatomical plate, laid out the way a normal wall
chart is: a head in profile for the face terms, a full figure with the
trunk opened for the organs, and detail views of the hand and foot.

Figure proportions follow the standard canon so it reads as a body:
seven and a half heads tall, shoulders three heads wide, the hip joint at
the halfway point of total height, knee halfway again from hip to floor.
"""
W, H = 1600, 1000
CREAM, NAVY, CORAL, MUTE, DEEP = '#f4eee2', '#1b2340', '#ef4b6b', '#5a6890', '#0f1526'

def lead(x1, y1, x2, y2, text, anchor='start', dy=6):
    tx = x2 + (14 if anchor == 'start' else -14)
    return (f'<polyline class="ld" points="{x1},{y1} {x2},{y2}"/>'
            f'<circle class="dt" cx="{x1}" cy="{y1}" r="4"/>'
            f'<text class="lb" x="{tx}" y="{y2+dy}" text-anchor="{anchor}">{text}</text>')

# ── ribs for the opened trunk ───────────────────────────────────────
FX = 950                      # figure centre line
ribs = []
for i in range(12):
    y = 232 + i * 14.6
    w = 40 + 62 * max(0.0, 1 - ((i - 6.4) / 7.3) ** 2) ** .5
    drop = 24 + i * 3.4
    for s in (-1, 1):
        ex = FX + s * (14 if i < 7 else (24 + (i-6)*11 if i < 10 else w - 32))
        ribs.append(f'<path class="rb" d="M {FX+s*w:.0f} {y:.0f} '
                    f'Q {FX+s*w*0.94:.0f} {y+drop*0.8:.0f} {ex:.0f} {y+drop:.0f}"/>')
RIBS = "".join(ribs)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Anatomical chart of the human body with labelled parts">
<title>Anatomy of the human body — C1 vocabulary</title>
<style>
  .bg {{ fill: {CREAM}; }}
  .fig {{ fill: {NAVY}; }}
  .fig2 {{ fill: {DEEP}; }}
  .org {{ fill: {CORAL}; stroke: {DEEP}; stroke-width: 2; }}
  .org-l {{ fill: {CORAL}; opacity: .45; stroke: {DEEP}; stroke-width: 2; }}
  .rb {{ fill: none; stroke: {MUTE}; stroke-width: 5; stroke-linecap: round; }}
  .bn {{ fill: {MUTE}; }}
  .bnl {{ fill: none; stroke: {MUTE}; stroke-width: 6.5; stroke-linecap: round; }}
  .mk {{ fill: {CORAL}; }}
  .mk-s {{ fill: {CORAL}; opacity: .5; }}
  .ld {{ fill: none; stroke: {NAVY}; stroke-width: 1.4; opacity: .6; }}
  .dt {{ fill: {CORAL}; stroke: {CREAM}; stroke-width: 1.4; }}
  .lb {{ font-family: 'DM Sans', system-ui, sans-serif; font-size: 19px;
         font-weight: 600; fill: {NAVY}; }}
  .hd {{ font-family: 'DM Mono', ui-monospace, monospace; font-size: 12px;
         letter-spacing: .16em; fill: {CORAL}; }}
  .ttl {{ font-family: 'Playfair Display', Georgia, serif; font-size: 40px;
          font-weight: 700; fill: {NAVY}; }}
  .nt {{ font-family: 'DM Mono', ui-monospace, monospace; font-size: 11px;
         letter-spacing: .1em; fill: {MUTE}; }}
  .rule {{ stroke: {MUTE}; stroke-width: 1; opacity: .35; }}
</style>
<rect class="bg" x="0" y="0" width="{W}" height="{H}"/>
<text class="hd" x="56" y="54">FORBES ENGLISH · C1</text>
<text class="ttl" x="56" y="98">Anatomy of the human body</text>
<text class="nt" x="56" y="124">SEEN FROM THE FRONT — THE FIGURE'S RIGHT IS ON YOUR LEFT</text>
<line class="rule" x1="56" y1="146" x2="{W-56}" y2="146"/>

<!-- ══════════ PANEL 1 — head in profile ══════════ -->
<text class="hd" x="56" y="190">FACE &amp; NECK</text>
<g transform="translate(-52,44) scale(0.72)">
  <path class="fig" d="
    M 372 620 C 330 576 314 512 316 452 C 318 368 372 250 456 250
    C 512 250 542 298 546 352 L 547 420 C 548 430 552 434 558 438
    L 584 512 C 588 520 584 526 576 528 L 552 532 C 548 540 550 546 556 550
    C 546 554 536 558 532 562 C 540 566 548 570 552 576 C 542 584 532 588 528 594
    L 532 604 C 536 612 532 618 524 618 L 500 622 C 486 640 460 648 426 644
    L 426 706 C 426 750 452 774 496 792 L 576 820 L 576 900 L 300 900 L 300 820
    L 372 792 C 410 774 426 750 426 706 L 426 640 C 408 636 386 632 372 620 Z"/>
  <ellipse class="fig2" cx="392" cy="418" rx="19" ry="34"/>
  <ellipse class="fig2" cx="508" cy="392" rx="23" ry="12"/>
  <path class="mk" d="M 480 358 q 34 -11 56 3 l -3 11 q -28 -11 -50 -2 Z"/>
  <g class="mk">
    <rect x="490" y="382" width="3" height="12" transform="rotate(-40 490 382)"/>
    <rect x="502" y="379" width="3" height="13" transform="rotate(-28 502 379)"/>
    <rect x="514" y="378" width="3" height="13" transform="rotate(-16 514 378)"/>
    <rect x="526" y="380" width="3" height="12" transform="rotate(-4 526 380)"/>
  </g>
  <circle class="mk-s" cx="446" cy="366" r="20"/>
  <path class="mk" d="M 556 522 q 17 -5 21 6 q -15 6 -21 -6 Z"/>
  <path class="mk" d="M 524 556 q 23 -6 34 -2 l -2 7 q -13 -3 -32 3 Z"/>
  <path class="mk" d="M 524 572 q 21 6 32 0 l -4 9 q -13 4 -27 -2 Z"/>
  <path class="mk" d="M 442 650 q 21 8 25 33 l 0 86 l -27 -10 l 0 -77 q -2 -20 2 -32 Z" opacity=".8"/>
</g>
{lead(272, 220, 130, 200, 'forehead', 'end')}
{lead(269, 308, 130, 246, 'temple', 'end')}
{lead(313, 302, 130, 292, 'eyebrow', 'end')}
{lead(316, 320, 130, 338, 'eyelash', 'end')}
{lead(352, 420, 470, 400, 'nostril')}
{lead(332, 456, 470, 452, 'lip')}
{lead(325, 490, 470, 504, 'chin')}
{lead(325, 588, 470, 592, 'throat')}
{lead(272, 610, 130, 610, 'neck', 'end')}
<line class="rule" x1="56" y1="700" x2="560" y2="700"/>

<!-- ══════════ PANEL 3 — hand and foot ══════════ -->
<text class="hd" x="56" y="742">HAND &amp; FOOT, IN DETAIL</text>
<!-- hand, palm towards you -->
<g transform="translate(150,748) scale(0.8)">
  <path class="fig" d="M 20 60 L 128 60 C 144 60 152 72 152 88 L 152 150
    C 152 184 134 202 102 204 L 46 204 C 16 202 0 184 0 150 L 0 88 C 0 72 6 60 20 60 Z"/>
  <g class="fig">
    <rect x="12" y="188" width="28" height="76" rx="14"/>
    <rect x="48" y="188" width="28" height="86" rx="14"/>
    <rect x="84" y="188" width="28" height="82" rx="14"/>
    <rect x="120" y="188" width="26" height="70" rx="13"/>
  </g>
  <path class="fig" d="M 0 100 C -26 104 -42 126 -40 152 C -38 178 -20 190 -2 184
    C 8 180 8 156 6 136 Z"/>
  <rect class="fig" x="14" y="24" width="124" height="34" rx="14"/>
  <ellipse class="mk-s" cx="76" cy="138" rx="52" ry="46"/>
  <g class="mk"><circle cx="26" cy="188" r="12"/><circle cx="62" cy="188" r="12"/>
    <circle cx="98" cy="188" r="12"/><circle cx="133" cy="188" r="11"/></g>
  <rect class="mk" x="14" y="26" width="124" height="30" rx="13" opacity=".85"/>
  <path class="mk-s" d="M -40 130 C -50 140 -50 168 -34 180 l 10 -10 c -12 -10 -12 -28 -2 -38 Z"/>
</g>
{lead(212, 852, 96, 800, 'palm', 'end')}
{lead(174, 898, 96, 846, 'knuckle', 'end')}
{lead(122, 884, 96, 892, 'thumb', 'end')}
{lead(212, 782, 96, 938, 'wrist', 'end')}
<!-- foot, from the side, facing right -->
<g transform="translate(360,776) scale(0.82)">
  <path class="fig" d="M 40 0 L 96 0 L 100 96 C 100 116 108 128 124 134
    L 236 140 C 254 142 262 152 262 166 L 262 186 L 24 186
    C 8 186 0 176 0 162 L 4 132 C 20 124 30 112 32 92 Z"/>
  <ellipse class="mk" cx="68" cy="96" rx="42" ry="15"/>
  <path class="mk" d="M 12 120 C -6 130 -6 158 8 172 l 34 0 C 24 158 24 136 40 124 Z"/>
  <rect class="mk-s" x="26" y="170" width="236" height="16" rx="7"/>
</g>
{lead(416, 862, 620, 802, 'ankle')}
{lead(372, 912, 620, 848, 'heel')}
{lead(510, 924, 620, 894, 'sole')}

<!-- ══════════ PANEL 2 — full figure, trunk opened ══════════ -->
<text class="hd" x="{FX-100}" y="190">THE TRUNK, OPENED</text>
<!-- body: shoulders at 3 heads wide, hip joint at mid-height -->
<path class="fig" opacity=".13" d="
  M {FX-26} 176 C {FX-70} 178 {FX-116} 194 {FX-124} 216
  C {FX-140} 236 {FX-168} 320 {FX-176} 380 L {FX-198} 470
  C {FX-202} 486 {FX-188} 494 {FX-180} 480 L {FX-152} 396
  C {FX-146} 428 {FX-140} 448 {FX-134} 470
  C {FX-124} 512 {FX-120} 548 {FX-118} 586
  C {FX-116} 622 {FX-112} 648 {FX-106} 668
  L {FX-96} 796 C {FX-94} 830 {FX-88} 856 {FX-84} 880
  L {FX-88} 928 L {FX-30} 928 L {FX-26} 880
  C {FX-22} 848 {FX-18} 812 {FX-14} 780 L {FX-6} 690 L {FX+6} 690
  L {FX+14} 780 C {FX+18} 812 {FX+22} 848 {FX+26} 880
  L {FX+30} 928 L {FX+88} 928 L {FX+84} 880
  C {FX+88} 856 {FX+94} 830 {FX+96} 796 L {FX+106} 668
  C {FX+112} 648 {FX+116} 622 {FX+118} 586
  C {FX+120} 548 {FX+124} 512 {FX+134} 470
  C {FX+140} 448 {FX+146} 428 {FX+152} 396 L {FX+180} 480
  C {FX+188} 494 {FX+202} 486 {FX+198} 470 L {FX+176} 380
  C {FX+168} 320 {FX+140} 236 {FX+124} 216
  C {FX+116} 194 {FX+70} 178 {FX+26} 176 Z"/>
<!-- head and neck of the figure -->
<ellipse class="fig" opacity=".13" cx="{FX}" cy="{'126'}" rx="40" ry="50"/>

<!-- organs, back to front -->
<g class="bn">
  <rect x="{FX-16}" y="452" width="32" height="14" rx="4"/>
  <rect x="{FX-17}" y="472" width="34" height="14" rx="4"/>
  <rect x="{FX-18}" y="492" width="36" height="14" rx="4"/>
  <rect x="{FX-19}" y="512" width="38" height="14" rx="4"/>
</g>
<path class="org" d="M {FX-56} 452 c -20 -3 -34 11 -34 30 c 0 21 15 34 32 30
  c 8 -2 5 -12 -2 -17 c -10 -7 -10 -21 0 -28 c 8 -5 9 -14 4 -15 Z"/>
<path class="org" d="M {FX+56} 432 c 20 -3 34 11 34 30 c 0 21 -15 34 -32 30
  c -8 -2 -5 -12 2 -17 c 10 -7 10 -21 0 -28 c -8 -5 -9 -14 -4 -15 Z"/>
<path class="org-l" d="M {FX-24} 238 C {FX-88} 246 {FX-112} 296 {FX-106} 346
  C {FX-102} 376 {FX-80} 384 {FX-52} 370 C {FX-30} 360 {FX-22} 326 {FX-24} 278 Z"/>
<path class="org-l" d="M {FX+24} 238 C {FX+88} 246 {FX+112} 296 {FX+106} 346
  C {FX+102} 376 {FX+80} 384 {FX+52} 370 C {FX+36} 362 {FX+42} 340 {FX+30} 322
  C {FX+42} 310 {FX+30} 286 {FX+24} 278 Z"/>
<path class="org" d="M {FX-104} 358 C {FX-60} 344 {FX-16} 354 {FX-2} 372
  C {FX} 394 {FX-20} 410 {FX-46} 412 C {FX-82} 414 {FX-102} 390 {FX-104} 358 Z"/>
<path class="org" d="M {FX+26} 362 C {FX+52} 352 {FX+86} 364 {FX+94} 392
  C {FX+100} 420 {FX+78} 438 {FX+54} 432 C {FX+36} 428 {FX+28} 412 {FX+36} 398
  C {FX+48} 404 {FX+62} 402 {FX+66} 392 C {FX+60} 378 {FX+42} 376 {FX+26} 378 Z"/>
<path class="bnl" style="stroke:{CORAL};stroke-width:15;opacity:.95;fill:none"
  d="M {FX-78} 596 L {FX-78} 542 Q {FX-78} 528 {FX-62} 528 L {FX+62} 528
     Q {FX+78} 528 {FX+78} 542 L {FX+78} 600"/>
<path class="bnl" style="stroke:{CORAL};stroke-width:10;opacity:.55;fill:none"
  d="M {FX-52} 556 q 26 14 52 0 q 26 -14 40 6 M {FX-54} 580 q 30 16 58 0 q 24 -12 36 8"/>
{RIBS}
<rect class="bn" x="{FX-11}" y="238" width="22" height="126" rx="8"/>
<path class="bnl" d="M {FX-96} 606 C {FX-104} 646 {FX-84} 668 {FX-58} 674
  M {FX+96} 606 C {FX+104} 646 {FX+84} 668 {FX+58} 674
  M {FX-96} 606 C {FX-60} 592 {FX+60} 592 {FX+96} 606"/>
<circle class="bnl" cx="{FX-92}" cy="646" r="15"/>
<circle class="bnl" cx="{FX+92}" cy="646" r="15"/>
<path style="fill:none;stroke:#2b8f9e;stroke-width:6;stroke-linecap:round"
  d="M {FX+36} 250 C {FX+44} 320 {FX+32} 380 {FX+28} 442"/>
<path style="fill:none;stroke:#2b8f9e;stroke-width:4;stroke-linecap:round"
  d="M {FX+39} 282 L {FX+78} 272 M {FX+33} 356 L {FX+74} 348"/>
<!-- surface landmarks on the figure -->
<ellipse class="mk" cx="{FX-176}" cy="392" rx="20" ry="11" transform="rotate(-18 {FX-176} 392)"/>
<ellipse class="mk" cx="{FX-196}" cy="474" rx="15" ry="9"/>
<path class="mk-s" d="M {FX-124} 214 c 20 12 30 26 32 46 c -22 -2 -36 -18 -32 -46 Z"/>
<ellipse class="mk" cx="{FX-52}" cy="742" rx="34" ry="14"/>
<path class="mk" d="M {FX-26} 800 C {FX-18} 830 {FX-16} 856 {FX-14} 878 l -16 2
  C {FX-32} 856 {FX-34} 830 {FX-42} 802 Z"/>
<path class="mk" d="M {FX-88} 800 C {FX-100} 830 {FX-100} 858 {FX-88} 880 l 16 -4
  C {FX-84} 856 {FX-84} 830 {FX-74} 802 Z"/>

{lead(FX-176, 392, FX-330, 300, 'elbow', 'end')}
{lead(FX-124, 236, FX-330, 246, 'armpit', 'end')}
{lead(FX-92, 262, FX-330, 200, 'chest', 'end')}
{lead(FX-84, 314, FX-330, 352, 'lung', 'end')}
{lead(FX-110, 336, FX-330, 398, 'rib', 'end')}
{lead(FX-66, 384, FX-330, 444, 'liver', 'end')}
{lead(FX-74, 474, FX-330, 490, 'kidney', 'end')}
{lead(FX-122, 500, FX-330, 536, 'waist', 'end')}
{lead(FX-92, 646, FX-330, 582, 'hip', 'end')}
{lead(FX-40, 664, FX-330, 628, 'pelvis', 'end')}
{lead(FX-52, 742, FX-330, 700, 'thigh', 'end')}
{lead(FX-84, 840, FX-330, 760, 'calf', 'end')}
{lead(FX+72, 404, FX+280, 300, 'stomach')}
{lead(FX, 500, FX+280, 350, 'spine')}
{lead(FX+30, 380, FX+280, 400, 'veins')}
{lead(FX+40, 566, FX+280, 450, 'intestines')}
{lead(FX+26, 840, FX+280, 520, 'shin')}
</svg>
'''
open('/home/claude/forbes-english/BodyParts/anatomy-chart.svg','w',encoding='utf-8').write(svg)
print('wrote anatomy-chart.svg')
