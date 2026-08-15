# -*- coding: utf-8 -*-
"""Torso & organs — front view.

Seen from the front, so the figure's right is the viewer's LEFT. That one
fact decides most of this drawing, and it is what diagrams usually get
wrong:

  liver     figure's RIGHT upper abdomen, tucked under the ribs
  stomach   figure's LEFT — the two are not interchangeable
  kidneys   behind everything, either side of the spine at about T12-L3,
            and the figure's RIGHT one sits lower, because the liver is
            sitting on top of it
  lungs     the left is the smaller: the heart notches its inner edge
  ribs      twelve pairs, sweeping down and forward from the spine.
            1-7 reach the sternum, 8-10 stop on the costal margin, and
            11-12 reach nothing at all — hence floating
  colon     up the figure's right, across, down the left, framing the
            small intestine

Drawn back to front — spine, kidneys, lungs, liver and stomach, gut, then
the ribcage over the top of all of it, so the cage reads as being in
front of the organs rather than painted out by them.

Tone carries meaning: pink is a labelled organ, muted blue is bone, teal
is vein. Nothing on the page is decoration.
"""
W, H = 1280, 720
CREAM, NAVY, PINK, MUTE, TEAL = '#f4eee2', '#1b2340', '#ef4b6b', '#46557f', '#2b8f9e'
CX = 620

def leader(x1, y1, x2, y2, tx, ty, text, anchor='start'):
    return (f'  <polyline class="lead" points="{x1},{y1} {x2},{y2}"/>\n'
            f'  <circle class="dot" cx="{x1}" cy="{y1}" r="4.5"/>\n'
            f'  <text class="lbl" x="{tx}" y="{ty}" text-anchor="{anchor}">{text}</text>')

# ── ribs ────────────────────────────────────────────────────────────
# Only the front half of each rib is drawn: from the widest point of the
# cage, curving down and inward to the sternum. The back half runs to the
# spine and a front view does not show it. Drawing the whole hoop is what
# turns a ribcage into a coiled spring.
ribs = []
for i in range(12):
    y = 208 + i * 15.0
    w = 42 + 66 * max(0.0, 1 - ((i - 6.5) / 7.4) ** 2) ** .5
    drop = 26 + i * 3.2
    for s_ in (-1, 1):
        if i < 7:
            ex = CX + s_ * 15                      # true ribs reach the sternum
        elif i < 10:
            ex = CX + s_ * (26 + (i - 6) * 12)     # false ribs: costal margin
        else:
            ex = CX + s_ * (w - 34)                # floating: nowhere
        ribs.append(
            f'  <path class="rib" d="M {CX + s_*w:.0f} {y:.0f} '
            f'Q {CX + s_*w*0.92:.0f} {y + drop*0.82:.0f} {ex:.0f} {y + drop:.0f}"/>')
RIBS = "\n".join(ribs)

# ── spine: only where a front view would actually show it — above the
# sternum and below the ribcage. Behind the cage it is hidden. ──
verts = []
for i in range(5):                       # lumbar, below the cage, where a
    # front view genuinely shows it — behind the ribs it is hidden, and
    # drawing it there would only compete with the sternum.
    verts.append(f'  <rect class="bone" x="{CX-17}" y="{432 + i*17}" width="34" height="12" rx="4"/>')
SPINE = "\n".join(verts)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Labelled front view of the torso and internal organs">
<title>Torso and organs</title>
<style>
  .bg    {{ fill: {CREAM}; }}
  .skin  {{ fill: {NAVY}; opacity: .10; }}
  .bone  {{ fill: {MUTE}; }}
  .rib   {{ fill: none; stroke: {MUTE}; stroke-width: 6; stroke-linecap: round; opacity: .85; }}
  .pelv  {{ fill: none; stroke: {MUTE}; stroke-width: 8; stroke-linecap: round; }}
  .organ {{ fill: {PINK}; stroke: {NAVY}; stroke-width: 2.5; stroke-opacity: .5; }}
  .lungs {{ fill: {PINK}; opacity: .42; stroke: {NAVY}; stroke-width: 2.5; stroke-opacity: .4; }}
  .vein  {{ fill: none; stroke: {TEAL}; stroke-linecap: round; }}
  .lead  {{ fill: none; stroke: {NAVY}; stroke-width: 1.6; opacity: .7; }}
  .dot   {{ fill: {PINK}; stroke: {CREAM}; stroke-width: 1.5; }}
  .lbl   {{ font-family: 'DM Sans', system-ui, sans-serif; font-size: 20px;
            font-weight: 600; fill: {NAVY}; }}
  .ttl   {{ font-family: 'Playfair Display', Georgia, serif; font-size: 34px;
            font-weight: 700; fill: {NAVY}; }}
  .sub   {{ font-family: 'DM Mono', ui-monospace, monospace; font-size: 12.5px;
            letter-spacing: .14em; fill: {PINK}; }}
  .note  {{ font-family: 'DM Mono', ui-monospace, monospace; font-size: 11px;
            letter-spacing: .1em; fill: {MUTE}; }}
</style>
<rect class="bg" x="0" y="0" width="{W}" height="{H}"/>
<text class="sub" x="64" y="64">FORBES ENGLISH · C1 BODY PARTS</text>
<text class="ttl" x="64" y="104">Torso &amp; organs</text>
<text class="note" x="64" y="132">FROM THE FRONT — THE FIGURE'S RIGHT IS ON YOUR LEFT</text>

<!-- 1. the body -->
<path class="skin" d="
  M {CX-52} 146 L {CX+52} 146
  C {CX+84} 146 {CX+134} 172 {CX+142} 218
  C {CX+150} 262 {CX+142} 336 {CX+130} 378
  C {CX+118} 418 {CX+104} 436 {CX+102} 462
  C {CX+100} 500 {CX+122} 540 {CX+126} 584
  L {CX+120} 656 L {CX-120} 656 L {CX-126} 584
  C {CX-122} 540 {CX-100} 500 {CX-102} 462
  C {CX-104} 436 {CX-118} 418 {CX-130} 378
  C {CX-142} 336 {CX-150} 262 {CX-142} 218
  C {CX-134} 172 {CX-84} 146 {CX-52} 146 Z"/>

<!-- 2. spine, where a front view would show it -->
{SPINE}

<!-- 3. kidneys: behind everything. Figure's RIGHT (your left) sits lower. -->
<path class="organ" d="M {CX-56} 440 c -20 -3 -33 10 -33 29 c 0 20 14 33 31 29
  c 7 -2 5 -11 -2 -16 c -9 -6 -9 -20 0 -26 c 7 -5 9 -14 4 -16 Z"/>
<path class="organ" d="M {CX+56} 420 c 20 -3 33 10 33 29 c 0 20 -14 33 -31 29
  c -7 -2 -5 -11 2 -16 c 9 -6 9 -20 0 -26 c -7 -5 -9 -14 -4 -16 Z"/>

<!-- 4. lungs. The figure's LEFT (your right) is the narrower one — the
     heart takes a bite out of its inner edge. -->
<path class="lungs" d="M {CX-26} 212 C {CX-92} 220 {CX-118} 274 {CX-112} 326
  C {CX-108} 358 {CX-84} 366 {CX-54} 352 C {CX-32} 342 {CX-24} 306 {CX-26} 254 Z"/>
<path class="lungs" d="M {CX+26} 212 C {CX+92} 220 {CX+118} 274 {CX+112} 326
  C {CX+108} 358 {CX+84} 366 {CX+54} 352
  C {CX+38} 344 {CX+44} 322 {CX+32} 304
  C {CX+44} 292 {CX+32} 266 {CX+26} 254 Z"/>

<!-- 5. liver on the figure's right, stomach on the figure's left -->
<path class="organ" d="M {CX-108} 336 C {CX-64} 322 {CX-18} 332 {CX-4} 350
  C {CX-2} 372 {CX-22} 388 {CX-50} 390 C {CX-86} 392 {CX-106} 368 {CX-108} 336 Z"/>
<path class="organ" d="M {CX+24} 340 C {CX+52} 330 {CX+88} 342 {CX+96} 370
  C {CX+102} 400 {CX+80} 418 {CX+56} 412 C {CX+38} 408 {CX+30} 392 {CX+38} 378
  C {CX+50} 384 {CX+64} 382 {CX+68} 372 C {CX+62} 358 {CX+42} 354 {CX+24} 356 Z"/>

<!-- 6. gut: colon up the figure's right, across, down the left -->
<g class="vein" style="stroke:{PINK};stroke-width:16;opacity:.95">
  <path d="M {CX-84} 574 L {CX-84} 512 Q {CX-84} 496 {CX-66} 496
           L {CX+66} 496 Q {CX+84} 496 {CX+84} 512 L {CX+84} 578"/>
</g>
<g class="vein" style="stroke:{PINK};stroke-width:11;opacity:.6">
  <path d="M {CX-56} 528 q 28 15 56 0 q 28 -15 42 6"/>
  <path d="M {CX-58} 552 q 32 17 62 0 q 25 -13 38 8"/>
  
</g>

<!-- 7. the cage, over the organs -->
{RIBS}
  <rect class="bone" x="{CX-12}" y="206" width="24" height="132" rx="9"/>

<!-- 8. pelvis -->
<path class="pelv" d="
  M {CX-100} 556 C {CX-108} 598 {CX-86} 622 {CX-58} 628
  M {CX+100} 556 C {CX+108} 598 {CX+86} 622 {CX+58} 628
  M {CX-100} 556 C {CX-62} 540 {CX+62} 540 {CX+100} 556"/>
<circle class="pelv" cx="{CX-96}" cy="598" r="16" style="stroke-width:7"/>
<circle class="pelv" cx="{CX+96}" cy="598" r="16" style="stroke-width:7"/>

<!-- 9. veins: the return line beside the spine, and the neck vessels -->
<path class="vein" style="stroke-width:7" d="M {CX+38} 222 C {CX+46} 290 {CX+34} 350 {CX+30} 412"/>
<path class="vein" style="stroke-width:4.5" d="M {CX+42} 250 L {CX+80} 240 M {CX+44} 284 L {CX+84} 276"/>

{leader(CX-92, 236, 300, 206, 288, 212, 'chest', 'end')}
{leader(CX-88, 288, 300, 254, 288, 260, 'lung', 'end')}
{leader(CX-116, 322, 300, 302, 288, 308, 'rib', 'end')}
{leader(CX-68, 360, 300, 350, 288, 356, 'liver', 'end')}
{leader(CX-76, 462, 300, 404, 288, 410, 'kidney', 'end')}
{leader(CX-104, 462, 300, 446, 288, 452, 'waist', 'end')}
{leader(CX-96, 598, 300, 494, 288, 500, 'hip', 'end')}
{leader(CX-36, 616, 300, 542, 288, 548, 'pelvis', 'end')}
{leader(CX+74, 376, 980, 300, 996, 306, 'stomach')}
{leader(CX, 444, 980, 348, 996, 354, 'spine')}
{leader(CX+44, 268, 980, 396, 996, 402, 'veins')}
{leader(CX+50, 552, 980, 444, 996, 450, 'intestines')}
</svg>
'''
open('/home/claude/forbes-english/BodyParts/torso-organs.svg','w',encoding='utf-8').write(svg)
print('wrote torso-organs.svg')
