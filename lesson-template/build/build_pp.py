# -*- coding: utf-8 -*-
src = open('sherpa-tensing-camp-three-past-simple.html', encoding='utf-8').read()
s = src

# ── title ─────────────────────────────────────────────────────────────
s = s.replace('<title>Sherpa Tensing - Camp Three: The Camp Behind You (Past Simple)</title>',
              '<title>Sherpa Tensing - Camp Four: The Rope Still Attached (Present Perfect Simple)</title>')

# ── palette: the route map gives present perfect its green ────────────
for a, b in [
    ('--ink:#2B1B12;',        '--ink:#16251F;'),
    ('--ink-soft:#6B5644;',   '--ink-soft:#4E6A60;'),
    ('--accent:#B08968;',     '--accent:#0F6E56;'),
    ('--accent-dark:#7A5A3E;','--accent-dark:#0A4E3D;'),
    ('--accent-light:#E8D9C7;','--accent-light:#C8E0D6;'),
    ('--accent-lighter:#F5EDE3;','--accent-lighter:#E9F3EF;'),
]:
    assert a in s, a
    s = s.replace(a, b, 1)

# ══ THE DIAGRAM ═══════════════════════════════════════════════════════
DEFS = '''      <defs>
        <linearGradient id="ppArrive" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0"    stop-color="#FBF6F0"/>
          <stop offset="0.60" stop-color="#FBF6F0"/>
          <stop offset="0.75" stop-color="#8FCBB8"/>
          <stop offset="0.88" stop-color="#2E8E72"/>
          <stop offset="1"    stop-color="#0F6E56"/>
        </linearGradient>
        <filter id="{fid}" x="-8%" y="-8%" width="116%" height="116%">
          <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" stitchTiles="stitch" result="n"/>
          <feColorMatrix in="n" type="matrix"
            values="0 0 0 0 0.98  0 0 0 0 0.95  0 0 0 0 0.88  0 0 0 0.4 0" result="g"/>
          <feComposite in="g" in2="SourceGraphic" operator="in"/>
        </filter>
      </defs>'''

def grain(fid, shape):
    return f'{shape.replace("FILL", "#000")} filter="url(#{fid})" opacity="0.35"'

def diagram(fid, interactive):
    """The whole picture. interactive=True adds the clickable groups."""
    o = lambda tag: f'<g class="diagram-shape" id="{tag}" tabindex="0" role="button">' if interactive else ''
    c = '</g>' if interactive else ''

    past = f'''{o("shape-past")}
      <rect x="10" y="55" width="156" height="219" fill="#B08968"/>
      <rect x="10" y="55" width="156" height="219" fill="#000" filter="url(#{fid})" opacity="0.3"/>
      <text x="24" y="78" class="dg-cap" fill="#F6EBE0" opacity="0.9">PAST SIMPLE</text>
      <text x="24" y="152" class="dg-line" fill="#FDF8F3">I moved here</text>
      <text x="24" y="171" class="dg-line" fill="#FDF8F3">ten years ago</text>
      {c}'''

    unfinished = f'''{o("shape-unfinished")}
      <rect x="170" y="55" width="310" height="95" fill="#0F6E56"/>
      <rect x="170" y="55" width="310" height="95" fill="#000" filter="url(#{fid})" opacity="0.3"/>
      <text x="209" y="80" class="dg-cap" fill="#BFE3D6">UNFINISHED TIME PERIOD</text>
      <text x="209" y="116" class="dg-line" fill="#F2FAF7">I have lived here for ten years.</text>
      {c}'''

    unspecified = f'''{o("shape-unspecified")}
      <rect x="196" y="150" width="284" height="72" fill="#FBF6F0"/>
      <text x="209" y="167" class="dg-cap" fill="#0A4E3D">UNSPECIFIED TIME</text>
      <text x="209" y="197" class="dg-q" fill="#0F6E56">????????</text>
      <text x="209" y="216" class="dg-small" fill="#16251F">Have you ever been to Scotland?</text>
      {c}'''

    recent = f'''{o("shape-recent")}
      <rect x="196" y="222" width="284" height="73" fill="url(#ppArrive)"/>
      <text x="209" y="243" class="dg-cap" fill="#0A4E3D">JUST NOW &#183; RESULT IN THE PRESENT</text>
      <text x="209" y="268" class="dg-line" fill="#16251F">Doris has just made coffee.</text>
      {c}'''

    now = f'''{o("shape-now")}
      <text x="544" y="42" class="diagram-caption" fill="#3E6A85">NOW</text>
      <rect x="480" y="55" width="128" height="240" fill="#D98A72"/>
      <rect x="480" y="55" width="128" height="240" fill="#000" filter="url(#{fid})" opacity="0.22"/>
      <rect x="497" y="74" width="94" height="203" fill="#5C7690"/>
      <text x="544" y="160" text-anchor="middle" class="dg-line" fill="#F1F5F8">I live</text>
      <text x="544" y="179" text-anchor="middle" class="dg-line" fill="#F1F5F8">here</text>
      <text x="544" y="198" text-anchor="middle" class="dg-line" fill="#F1F5F8">now</text>
      {c}'''

    return f'''{DEFS.format(fid=fid)}
      <rect x="0" y="0" width="640" height="344" fill="var(--paper)"/>
      <!-- the ground the whole route stands on -->
      <line x1="196" y1="300" x2="632" y2="300" stroke="#241811" stroke-width="2.5"/>
      <!-- past simple: closed, and left behind -->
      {past}
      <path d="M10,274 L196,274 L196,300 L52,300 L10,281 Z" fill="#241811"/>
      <path d="M10,274 L196,274 L196,300 L52,300 L10,281 Z" fill="#000" filter="url(#{fid})" opacity="0.5"/>
      <!-- three ways the present perfect reaches forward to now -->
      {unfinished}
      <rect x="166" y="150" width="30" height="150" fill="#241811"/>
      <rect x="166" y="150" width="30" height="150" fill="#000" filter="url(#{fid})" opacity="0.5"/>
      {unspecified}
      {recent}
      <!-- now, and the one watching from it -->
      {now}
      <g fill="#241811">
        <path d="M614,300 L620,288 M626,300 L620,288 M620,300 L620,288" stroke="#241811" stroke-width="1.3"/>
        <rect x="611" y="278" width="15" height="9" rx="1"/>
        <rect x="607" y="280" width="4" height="5"/>
        <circle cx="631" cy="277" r="3.1"/>
        <path d="M631,280 L631,292 L627,300 M631,292 L635,300 M631,283 L625,281" stroke="#241811" stroke-width="1.6" fill="none" stroke-linecap="round"/>
      </g>'''

HERO_SVG = ('<svg class="hero-diagram" viewBox="0 0 640 344" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="A brown block labelled past simple, I moved here ten years ago; three green bands reaching '
            'across to a coral and blue block labelled now, I live here now; the bands show an unfinished time period, '
            'an unspecified time marked by question marks, and a very recent action arriving at the present">\n'
            + diagram('grainHero', False) + '\n    </svg>')

STAGE_SVG = ('<svg viewBox="0 0 640 344" xmlns="http://www.w3.org/2000/svg" role="img" '
             'aria-label="Interactive diagram of the three uses of the present perfect, between past simple and now">\n'
             + diagram('grainStage', True) + '\n          </svg>')

# ── swap the hero ─────────────────────────────────────────────────────
h0 = s.index('<svg class="hero-diagram"'); h1 = s.index('</svg>', h0) + 6
s = s[:h0] + HERO_SVG + s[h1:]
g0 = s.index('<svg viewBox="0 0 640 344"', h0 + len(HERO_SVG)); g1 = s.index('</svg>', g0) + 6
s = s[:g0] + STAGE_SVG + s[g1:]

# ── diagram type styles ───────────────────────────────────────────────
s = s.replace(".diagram-caption{font-family:'Inter',sans-serif;font-weight:700;font-size:15px;letter-spacing:.04em;}",
""".diagram-caption{font-family:'Inter',sans-serif;font-weight:700;font-size:15px;letter-spacing:.04em;}
  .dg-cap{font-family:'Inter',sans-serif;font-weight:700;font-size:9.5px;letter-spacing:.11em;}
  .dg-line{font-family:'Inter',sans-serif;font-weight:600;font-size:14px;}
  .dg-small{font-family:'Inter',sans-serif;font-weight:500;font-size:12px;}
  .dg-q{font-family:'Inter',sans-serif;font-weight:700;font-size:26px;letter-spacing:.32em;}""", 1)

open('/tmp/pp_stage1.html', 'w', encoding='utf-8').write(s)
print('diagram in')
