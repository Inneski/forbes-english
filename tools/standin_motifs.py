# -*- coding: utf-8 -*-
"""Flat stand-in figures for house style 2 (2026-11-06).

Innes: "use stand in graphics to be replaced in shopping list". A deck is
built and shipped on these, and tools/standins.py lists every one still in
use, with its brief, as the artwork shopping list. The real plate replaces a
stand-in by being dropped into the lesson folder under the slot's name and
the builder being re-run (deck.plate() prefers it automatically).

What a stand-in has to be: honest (obviously a placeholder to anyone who
orders art, never mistaken for the finished picture) but not ugly in front
of a class. So: one flat object per slot, on a pale blob, in the benchmark's
idiom — ENGHUB's figures stand on white with a soft shape behind them. No
text, no faces, no gradients, no shadows: the same rules as the Midjourney
stem, so a stand-in and its replacement are the same KIND of picture.

Every motif is an SVG body on a 1000x1000 grid, filled from a scheme:
  ink   outlines and dark masses      a, b, c, d   four flat colours
  blob  the soft shape behind it      paper        white-ish highlights
"""

SCHEMES = {
    # ENGHUB's own family: mustard, terracotta, teal, navy on greige.
    'warm': dict(ink='#2b2d3a', a='#e08a3c', b='#f2c35c', c='#3f9e94', d='#c4553b',
                 blob='#efe5dc', paper='#fffdf9', skin='#e9b48f'),
    # The second benchmark deck: blue panels, coral and yellow.
    'cool': dict(ink='#1f2a44', a='#3f6fd6', b='#a7c4f2', c='#f08a5d', d='#f2c74f',
                 blob='#e6eef9', paper='#fdfeff', skin='#e9b48f'),
    # The revamp list's stem: cream, dusty pink, coral, slate blue.
    'rose': dict(ink='#2e2633', a='#d8636b', b='#f3b8a5', c='#4f7a8c', d='#f0c06b',
                 blob='#f4e5df', paper='#fffcfb', skin='#e9b48f'),
    # Outdoors and nature decks.
    'sage': dict(ink='#22302a', a='#4f8a6b', b='#a8cdb0', c='#e3a14d', d='#c2694a',
                 blob='#e7efe4', paper='#fdfefb', skin='#e9b48f'),
    # Business decks: slate and salmon (the revamp list's business family).
    'slate': dict(ink='#1e2733', a='#4b6a8a', b='#f0a58a', c='#93b3cf', d='#e8c36a',
                  blob='#e9edf2', paper='#fdfdfe', skin='#e9b48f'),
}

BLOBS = [
    'M500 120 C700 110 880 240 890 450 C900 680 760 880 520 890 C290 900 110 760 110 520 C110 300 300 130 500 120 Z',
    'M470 110 C690 90 900 260 880 500 C860 720 700 900 470 880 C250 860 100 700 120 470 C140 270 270 125 470 110 Z',
    'M530 130 C740 150 890 320 870 540 C850 760 650 900 440 870 C230 840 110 660 130 450 C150 250 330 110 530 130 Z',
]

M = {}

M['talk'] = '''
<path d="M190 250 h420 a150 150 0 0 1 150 150 v60 a150 150 0 0 1 -150 150 h-250 l-110 90 l20 -90 h-80 a150 150 0 0 1 -150 -150 v-60 a150 150 0 0 1 150 -150 z" fill="{a}"/>
<circle cx="300" cy="430" r="34" fill="{paper}"/><circle cx="410" cy="430" r="34" fill="{paper}"/><circle cx="520" cy="430" r="34" fill="{paper}"/>
<path d="M520 560 h250 a110 110 0 0 1 110 110 v20 a110 110 0 0 1 -110 110 h-20 l20 80 l-110 -80 h-140 a110 110 0 0 1 -110 -110 v-20 a110 110 0 0 1 110 -110 z" fill="{c}"/>
<rect x="500" y="640" width="250" height="26" rx="13" fill="{paper}"/><rect x="500" y="690" width="170" height="26" rx="13" fill="{paper}"/>
'''

M['people'] = '''
<circle cx="330" cy="330" r="80" fill="{skin}"/><path d="M330 300 a80 80 0 0 1 80 -10 a80 80 0 0 0 -160 40 z" fill="{ink}"/>
<path d="M200 820 v-230 a130 130 0 0 1 260 0 v230 z" fill="{a}"/>
<circle cx="670" cy="360" r="78" fill="{skin}"/><path d="M592 350 a78 78 0 0 1 156 0 c-30 -60 -126 -60 -156 0 z" fill="{d}"/>
<path d="M540 820 v-210 a130 130 0 0 1 260 0 v210 z" fill="{c}"/>
<path d="M430 170 h170 a50 50 0 0 1 50 50 v20 a50 50 0 0 1 -50 50 h-90 l-50 40 l10 -40 h-40 a50 50 0 0 1 -50 -50 v-20 a50 50 0 0 1 50 -50 z" fill="{b}"/>
'''

M['read'] = '''
<path d="M150 360 l350 70 l350 -70 v380 l-350 70 l-350 -70 z" fill="{d}"/>
<path d="M180 330 l320 70 v380 l-320 -70 z" fill="{paper}"/><path d="M820 330 l-320 70 v380 l320 -70 z" fill="{paper}"/>
<g fill="{blob}"><rect x="230" y="420" width="210" height="20" rx="10" transform="rotate(12 230 420)"/>
<rect x="230" y="480" width="210" height="20" rx="10" transform="rotate(12 230 480)"/>
<rect x="230" y="540" width="160" height="20" rx="10" transform="rotate(12 230 540)"/>
<rect x="560" y="463" width="210" height="20" rx="10" transform="rotate(-12 560 463)"/>
<rect x="560" y="523" width="210" height="20" rx="10" transform="rotate(-12 560 523)"/>
<rect x="560" y="583" width="160" height="20" rx="10" transform="rotate(-12 560 583)"/></g>
<rect x="490" y="400" width="20" height="390" fill="{ink}"/>
<path d="M600 300 v-110 l40 30 l40 -30 v110" fill="{a}"/>
'''

M['write'] = '''
<g transform="rotate(-7 470 520)"><rect x="230" y="180" width="440" height="600" rx="22" fill="{paper}"/>
<g fill="{blob}"><rect x="290" y="280" width="320" height="22" rx="11"/><rect x="290" y="350" width="320" height="22" rx="11"/>
<rect x="290" y="420" width="320" height="22" rx="11"/><rect x="290" y="490" width="220" height="22" rx="11"/></g></g>
<g transform="rotate(38 640 560)"><rect x="590" y="250" width="100" height="470" rx="10" fill="{b}"/>
<rect x="590" y="250" width="100" height="70" rx="10" fill="{d}"/><rect x="590" y="312" width="100" height="22" fill="{ink}"/>
<path d="M590 720 h100 l-50 110 z" fill="{skin}"/><path d="M622 790 h36 l-18 40 z" fill="{ink}"/></g>
'''

M['words'] = '''
<rect x="190" y="300" width="400" height="260" rx="26" fill="{c}" transform="rotate(-10 390 430)"/>
<rect x="250" y="340" width="400" height="260" rx="26" fill="{b}" transform="rotate(4 450 470)"/>
<rect x="300" y="400" width="400" height="260" rx="26" fill="{paper}" transform="rotate(-3 500 530)"/>
<g fill="{blob}" transform="rotate(-3 500 530)"><rect x="350" y="470" width="220" height="26" rx="13"/><rect x="350" y="530" width="300" height="20" rx="10"/><rect x="350" y="575" width="250" height="20" rx="10"/></g>
<circle cx="650" cy="640" r="120" fill="{paper}" fill-opacity="0.55" stroke="{ink}" stroke-width="34"/>
<rect x="725" y="740" width="48" height="170" rx="20" fill="{a}" transform="rotate(-45 749 825)"/>
'''

M['build'] = '''
<rect x="200" y="660" width="600" height="150" rx="24" fill="{a}"/>
<rect x="260" y="500" width="420" height="150" rx="24" fill="{c}"/>
<rect x="330" y="340" width="300" height="150" rx="24" fill="{b}"/>
<g fill="{paper}" fill-opacity="0.55"><circle cx="300" cy="735" r="22"/><circle cx="420" cy="735" r="22"/><circle cx="540" cy="735" r="22"/><circle cx="660" cy="735" r="22"/>
<circle cx="350" cy="575" r="22"/><circle cx="470" cy="575" r="22"/><circle cx="590" cy="575" r="22"/><circle cx="420" cy="415" r="22"/><circle cx="540" cy="415" r="22"/></g>
<rect x="600" y="150" width="240" height="130" rx="24" fill="{d}" transform="rotate(14 720 215)"/>
'''

M['quiz'] = '''
<path d="M250 640 a140 140 0 0 1 20 -278 a190 190 0 0 1 350 -60 a150 150 0 0 1 150 210 a120 120 0 0 1 -60 230 z" fill="{blob2}"/>
<circle cx="250" cy="780" r="44" fill="{blob2}"/><circle cx="180" cy="860" r="26" fill="{blob2}"/>
<path d="M420 420 a95 95 0 1 1 150 80 c-40 26 -55 46 -55 90 v20" fill="none" stroke="{a}" stroke-width="62" stroke-linecap="round"/>
<circle cx="515" cy="700" r="40" fill="{a}"/>
'''

M['time'] = '''
<circle cx="500" cy="500" r="290" fill="{paper}" stroke="{ink}" stroke-width="40"/>
<g fill="{ink}"><rect x="488" y="250" width="24" height="60" rx="12"/><rect x="488" y="690" width="24" height="60" rx="12"/>
<rect x="250" y="488" width="60" height="24" rx="12"/><rect x="690" y="488" width="60" height="24" rx="12"/></g>
<rect x="484" y="330" width="32" height="190" rx="16" fill="{ink}"/>
<rect x="484" y="484" width="32" height="150" rx="16" fill="{a}" transform="rotate(-55 500 500)"/>
<circle cx="500" cy="500" r="30" fill="{d}"/>
<path d="M150 360 a370 370 0 0 1 220 -200" fill="none" stroke="{c}" stroke-width="34" stroke-linecap="round"/>
<path d="M330 120 l70 40 l-70 60 z" fill="{c}"/>
'''

M['work'] = '''
<rect x="560" y="200" width="80" height="320" rx="12" fill="{c}"/><rect x="670" y="300" width="80" height="220" rx="12" fill="{b}"/><rect x="780" y="140" width="80" height="380" rx="12" fill="{a}"/>
<rect x="390" y="370" width="190" height="90" rx="40" fill="none" stroke="{ink}" stroke-width="34"/>
<rect x="170" y="440" width="560" height="380" rx="44" fill="{d}"/>
<rect x="170" y="560" width="560" height="34" fill="{ink}" fill-opacity="0.25"/>
<rect x="420" y="540" width="60" height="80" rx="14" fill="{b}"/>
'''

M['travel'] = '''
<circle cx="650" cy="360" r="210" fill="{b}"/>
<g fill="none" stroke="{paper}" stroke-width="16"><ellipse cx="650" cy="360" rx="90" ry="210"/><path d="M440 360 h420"/><path d="M470 260 h360"/><path d="M470 460 h360"/></g>
<rect x="330" y="420" width="140" height="90" rx="30" fill="none" stroke="{ink}" stroke-width="30"/>
<rect x="200" y="480" width="400" height="360" rx="44" fill="{c}"/>
<rect x="280" y="480" width="40" height="360" fill="{d}"/><rect x="480" y="480" width="40" height="360" fill="{d}"/>
<circle cx="260" cy="860" r="26" fill="{ink}"/><circle cx="540" cy="860" r="26" fill="{ink}"/>
'''

M['trophy'] = '''
<path d="M330 210 h340 v200 a170 170 0 0 1 -340 0 z" fill="{b}"/>
<path d="M330 260 h-80 a80 80 0 0 0 80 150" fill="none" stroke="{b}" stroke-width="36"/>
<path d="M670 260 h80 a80 80 0 0 1 -80 150" fill="none" stroke="{b}" stroke-width="36"/>
<rect x="460" y="570" width="80" height="110" fill="{d}"/><rect x="340" y="680" width="320" height="110" rx="22" fill="{ink}"/>
<path d="M500 280 l26 54 l58 6 l-44 40 l14 58 l-54 -30 l-54 30 l14 -58 l-44 -40 l58 -6 z" fill="{paper}"/>
<path d="M770 130 l14 34 l36 4 l-28 24 l9 36 l-31 -20 l-31 20 l9 -36 l-28 -24 l36 -4 z" fill="{a}"/>
'''

M['pair'] = '''
<rect x="300" y="470" width="400" height="44" rx="22" fill="{ink}"/><rect x="480" y="510" width="40" height="300" fill="{ink}"/><rect x="400" y="800" width="200" height="30" rx="15" fill="{ink}"/>
<path d="M370 430 h70 l-10 40 h-50 z" fill="{d}"/><path d="M560 430 h70 l-10 40 h-50 z" fill="{c}"/>
<path d="M140 520 v300 M140 640 h170 v180" fill="none" stroke="{a}" stroke-width="34" stroke-linecap="round"/><rect x="120" y="610" width="200" height="40" rx="20" fill="{a}"/>
<path d="M860 520 v300 M860 640 h-170 v180" fill="none" stroke="{c}" stroke-width="34" stroke-linecap="round"/><rect x="680" y="610" width="200" height="40" rx="20" fill="{c}"/>
<path d="M395 380 q15 -30 0 -60 M600 380 q15 -30 0 -60" fill="none" stroke="{blob2}" stroke-width="16" stroke-linecap="round"/>
'''

M['star'] = '''
<path d="M500 160 l90 190 l208 22 l-156 140 l46 204 l-188 -106 l-188 106 l46 -204 l-156 -140 l208 -22 z" fill="{b}"/>
<path d="M800 650 l22 48 l52 6 l-40 34 l12 52 l-46 -28 l-46 28 l12 -52 l-40 -34 l52 -6 z" fill="{a}"/>
<path d="M210 640 l16 34 l38 4 l-28 26 l8 36 l-34 -20 l-34 20 l8 -36 l-28 -26 l38 -4 z" fill="{c}"/>
<circle cx="500" cy="470" r="44" fill="{paper}" fill-opacity="0.6"/>
'''

M['idea'] = '''
<path d="M500 180 a210 210 0 0 1 130 375 c-20 16 -30 40 -30 70 v40 h-200 v-40 c0 -30 -10 -54 -30 -70 a210 210 0 0 1 130 -375 z" fill="{b}"/>
<rect x="400" y="680" width="200" height="40" rx="14" fill="{ink}"/><rect x="415" y="732" width="170" height="40" rx="14" fill="{ink}"/><rect x="450" y="784" width="100" height="40" rx="18" fill="{ink}"/>
<path d="M455 640 v-110 M545 640 v-110" stroke="{d}" stroke-width="16" stroke-linecap="round"/><g fill="none" stroke="{d}" stroke-width="12"><circle cx="473" cy="515" r="16"/><circle cx="500" cy="515" r="16"/><circle cx="527" cy="515" r="16"/></g>
<g stroke="{a}" stroke-width="30" stroke-linecap="round"><path d="M500 60 v50"/><path d="M220 180 l40 36"/><path d="M780 180 l-40 36"/><path d="M130 420 h56"/><path d="M870 420 h-56"/></g>
'''

M['home'] = '''
<path d="M180 470 l320 -270 l320 270 z" fill="{d}"/>
<rect x="230" y="460" width="540" height="380" fill="{paper}"/>
<rect x="440" y="620" width="120" height="220" rx="10" fill="{a}"/>
<rect x="290" y="530" width="110" height="110" rx="10" fill="{c}"/><rect x="600" y="530" width="110" height="110" rx="10" fill="{c}"/>
<rect x="640" y="250" width="70" height="140" fill="{ink}"/>
'''

M['food'] = '''
<circle cx="500" cy="540" r="270" fill="{paper}"/><circle cx="500" cy="540" r="190" fill="{blob2}"/>
<circle cx="440" cy="500" r="70" fill="{a}"/><circle cx="560" cy="580" r="60" fill="{c}"/><circle cx="560" cy="470" r="40" fill="{b}"/>
<g fill="{ink}"><rect x="140" y="300" width="34" height="500" rx="17"/><rect x="118" y="260" width="16" height="120" rx="8"/><rect x="149" y="260" width="16" height="120" rx="8"/><rect x="180" y="260" width="16" height="120" rx="8"/>
<path d="M830 260 c60 40 60 200 0 240 z"/><rect x="826" y="300" width="34" height="500" rx="17"/></g>
'''

M['nature'] = '''
<circle cx="680" cy="300" r="120" fill="{b}"/>
<path d="M90 820 c140 -220 300 -300 460 -170 c120 -110 260 -90 360 170 z" fill="{a}"/>
<path d="M60 820 c160 -140 330 -150 470 -40 c110 -60 240 -40 410 40 z" fill="{c}" fill-opacity="0.9"/>
<rect x="300" y="460" width="40" height="230" fill="{ink}"/><circle cx="320" cy="420" r="110" fill="{d}"/>
'''

M['city'] = '''
<rect x="150" y="380" width="180" height="440" rx="8" fill="{c}"/><rect x="350" y="220" width="200" height="600" rx="8" fill="{ink}"/>
<rect x="570" y="320" width="150" height="500" rx="8" fill="{a}"/><rect x="740" y="470" width="120" height="350" rx="8" fill="{d}"/>
<g fill="{paper}" fill-opacity="0.75"><rect x="190" y="430" width="40" height="40"/><rect x="250" y="430" width="40" height="40"/><rect x="190" y="510" width="40" height="40"/><rect x="250" y="510" width="40" height="40"/>
<rect x="390" y="270" width="44" height="44"/><rect x="466" y="270" width="44" height="44"/><rect x="390" y="350" width="44" height="44"/><rect x="466" y="350" width="44" height="44"/><rect x="390" y="430" width="44" height="44"/><rect x="466" y="430" width="44" height="44"/>
<rect x="600" y="370" width="36" height="36"/><rect x="656" y="370" width="36" height="36"/><rect x="600" y="440" width="36" height="36"/><rect x="656" y="440" width="36" height="36"/></g>
<rect x="100" y="815" width="800" height="30" rx="15" fill="{ink}"/>
'''

M['mail'] = '''
<rect x="140" y="320" width="520" height="360" rx="30" fill="{paper}"/>
<path d="M140 350 l260 190 l260 -190" fill="none" stroke="{a}" stroke-width="40" stroke-linejoin="round"/>
<rect x="600" y="300" width="250" height="460" rx="44" fill="{ink}"/><rect x="630" y="360" width="190" height="320" rx="16" fill="{c}"/>
<circle cx="725" cy="720" r="18" fill="{paper}"/>
<path d="M680 470 h90 M680 520 h60" stroke="{paper}" stroke-width="20" stroke-linecap="round"/>
'''

M['money'] = '''
<rect x="140" y="300" width="520" height="290" rx="24" fill="{c}" transform="rotate(-8 400 445)"/>
<circle cx="400" cy="445" r="80" fill="{paper}" fill-opacity="0.6" transform="rotate(-8 400 445)"/>
<g fill="{b}" stroke="{d}" stroke-width="14"><ellipse cx="650" cy="760" rx="170" ry="54"/><ellipse cx="650" cy="690" rx="170" ry="54"/><ellipse cx="650" cy="620" rx="170" ry="54"/><ellipse cx="650" cy="550" rx="170" ry="54"/></g>
'''

M['film'] = '''
<rect x="170" y="420" width="480" height="340" rx="24" fill="{ink}"/>
<g transform="rotate(-14 170 420)"><rect x="170" y="330" width="480" height="90" rx="14" fill="{ink}"/>
<g fill="{paper}"><path d="M220 330 h60 l-40 90 h-60 z"/><path d="M340 330 h60 l-40 90 h-60 z"/><path d="M460 330 h60 l-40 90 h-60 z"/><path d="M580 330 h60 l-40 90 h-60 z"/></g></g>
<rect x="220" y="490" width="380" height="20" rx="10" fill="{a}"/><rect x="220" y="550" width="260" height="20" rx="10" fill="{c}"/>
<circle cx="760" cy="330" r="150" fill="{a}"/><g fill="{paper}"><circle cx="760" cy="250" r="34"/><circle cx="840" cy="330" r="34"/><circle cx="760" cy="410" r="34"/><circle cx="680" cy="330" r="34"/></g><circle cx="760" cy="330" r="22" fill="{ink}"/>
'''

M['health'] = '''
<path d="M500 820 c-260 -170 -360 -320 -330 -450 c30 -130 220 -170 330 -30 c110 -140 300 -100 330 30 c30 130 -70 280 -330 450 z" fill="{a}"/>
<path d="M200 540 h170 l50 -90 l70 190 l60 -130 h250" fill="none" stroke="{paper}" stroke-width="30" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M760 170 c120 0 140 100 120 170 c-110 0 -150 -80 -120 -170 z" fill="{c}"/>
'''

M['mountain'] = '''
<circle cx="740" cy="270" r="100" fill="{b}"/>
<path d="M80 820 l300 -470 l300 470 z" fill="{c}"/><path d="M380 820 l240 -360 l280 360 z" fill="{a}"/>
<path d="M300 475 l80 -125 l80 125 l-40 -20 l-40 30 l-40 -30 z" fill="{paper}"/>
<path d="M560 550 l60 -90 l66 90 l-34 -16 l-32 22 l-30 -22 z" fill="{paper}"/>
'''

M['sea'] = '''
<circle cx="740" cy="250" r="90" fill="{b}"/>
<path d="M300 620 h420 l-70 100 h-290 z" fill="{d}"/><rect x="495" y="220" width="18" height="400" fill="{ink}"/>
<path d="M480 240 l-200 340 h200 z" fill="{paper}"/><path d="M530 290 l150 290 h-150 z" fill="{a}"/>
<path d="M90 760 q60 -50 120 0 t120 0 t120 0 t120 0 t120 0 t120 0 t120 0 v80 h-840 z" fill="{c}"/>
'''

M['sport'] = '''
<circle cx="420" cy="560" r="250" fill="{paper}" stroke="{ink}" stroke-width="22"/>
<path d="M420 470 l86 62 l-33 101 h-106 l-33 -101 z" fill="{ink}"/>
<g stroke="{ink}" stroke-width="18" stroke-linecap="round"><path d="M420 470 v-150"/><path d="M506 532 l140 -46"/><path d="M473 633 l90 120"/><path d="M367 633 l-90 120"/><path d="M334 532 l-140 -46"/></g>
<rect x="700" y="160" width="22" height="520" fill="{ink}"/><path d="M722 170 h170 l-40 70 l40 70 h-170 z" fill="{a}"/>
'''

M['music'] = '''
<path d="M380 700 v-420 l380 -90 v420" fill="none" stroke="{ink}" stroke-width="40" stroke-linejoin="round"/>
<path d="M380 280 l380 -90 v90 l-380 90 z" fill="{ink}"/>
<ellipse cx="310" cy="710" rx="100" ry="76" fill="{a}"/><ellipse cx="690" cy="620" rx="100" ry="76" fill="{c}"/>
<path d="M170 300 q40 -60 80 0 t80 0" fill="none" stroke="{b}" stroke-width="22" stroke-linecap="round"/>
'''

M['shop'] = '''
<path d="M210 360 h580 l-50 460 h-480 z" fill="{a}"/>
<path d="M380 360 v-60 a120 120 0 0 1 240 0 v60" fill="none" stroke="{ink}" stroke-width="34"/>
<rect x="300" y="470" width="400" height="30" rx="15" fill="{paper}" fill-opacity="0.5"/>
<rect x="640" y="520" width="200" height="260" rx="20" fill="{c}" transform="rotate(8 740 650)"/>
'''

M['tech'] = '''
<rect x="200" y="250" width="600" height="390" rx="30" fill="{ink}"/><rect x="235" y="285" width="530" height="320" rx="12" fill="{c}"/>
<rect x="130" y="660" width="740" height="44" rx="22" fill="{ink}"/>
<rect x="290" y="350" width="200" height="26" rx="13" fill="{paper}"/><rect x="290" y="410" width="300" height="26" rx="13" fill="{paper}" fill-opacity="0.7"/>
<rect x="290" y="470" width="250" height="26" rx="13" fill="{paper}" fill-opacity="0.7"/>
<circle cx="660" cy="490" r="62" fill="{b}"/>
'''

M['law'] = '''
<rect x="485" y="210" width="30" height="560" fill="{ink}"/><rect x="340" y="760" width="320" height="50" rx="20" fill="{ink}"/>
<rect x="230" y="250" width="540" height="26" rx="13" fill="{ink}"/>
<path d="M260 270 l-90 220 h180 z M740 270 l-90 220 h180 z" fill="none" stroke="{ink}" stroke-width="10"/>
<path d="M150 490 a110 70 0 0 0 220 0 z" fill="{a}"/><path d="M630 490 a110 70 0 0 0 220 0 z" fill="{c}"/>
<circle cx="500" cy="200" r="40" fill="{b}"/>
'''

M['science'] = '''
<path d="M420 180 h160 M450 180 v220 l-210 340 a60 60 0 0 0 52 90 h416 a60 60 0 0 0 52 -90 l-210 -340 v-220" fill="none" stroke="{ink}" stroke-width="34" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M330 600 h340 l70 115 a35 35 0 0 1 -30 52 h-420 a35 35 0 0 1 -30 -52 z" fill="{c}"/>
<circle cx="470" cy="660" r="26" fill="{paper}"/><circle cx="560" cy="700" r="18" fill="{paper}"/><circle cx="600" cy="520" r="22" fill="{a}"/><circle cx="560" cy="430" r="14" fill="{a}"/>
'''

M['animal'] = '''
<ellipse cx="500" cy="600" rx="260" ry="190" fill="{a}"/>
<circle cx="700" cy="420" r="120" fill="{a}"/><path d="M640 330 l-10 -110 l80 70 z M760 330 l10 -110 l-80 70 z" fill="{a}"/>
<rect x="320" y="740" width="60" height="110" rx="26" fill="{a}"/><rect x="580" y="740" width="60" height="110" rx="26" fill="{a}"/>
<path d="M250 560 c-120 -40 -120 -200 -40 -230" fill="none" stroke="{a}" stroke-width="44" stroke-linecap="round"/>
<ellipse cx="500" cy="640" rx="140" ry="90" fill="{b}"/>
'''

M['game'] = '''
<path d="M260 380 h480 a160 160 0 0 1 150 210 l-50 140 a80 80 0 0 1 -140 20 l-60 -80 h-280 l-60 80 a80 80 0 0 1 -140 -20 l-50 -140 a160 160 0 0 1 150 -210 z" fill="{ink}"/>
<path d="M280 470 v120 M220 530 h120" stroke="{paper}" stroke-width="34" stroke-linecap="round"/>
<circle cx="680" cy="490" r="30" fill="{a}"/><circle cx="740" cy="550" r="30" fill="{b}"/><circle cx="620" cy="550" r="30" fill="{c}"/><circle cx="680" cy="610" r="30" fill="{d}"/>
'''


def _deeper(hexc, by):
    r, g, b = (int(hexc[i:i + 2], 16) for i in (1, 3, 5))
    return '#%02x%02x%02x' % tuple(max(0, int(v * (1 - by))) for v in (r, g, b))


def svg(motif, scheme='warm', blob=0, size=1000):
    """The full SVG for one stand-in: a pale blob and the motif on it."""
    c = dict(SCHEMES[scheme])
    # a second, slightly deeper blob tone for motifs that draw a cloud
    c['blob2'] = _deeper(c['blob'], 0.06)
    body = M[motif].format(**c)
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" '
            'width="%d" height="%d"><path d="%s" fill="%s"/>%s</svg>'
            % (size, size, BLOBS[blob % len(BLOBS)], c['blob'], body))
