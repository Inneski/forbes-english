# -*- coding: utf-8 -*-
"""The page machinery for a Sailing the Seas of Grammar chart lesson.

build_regularia.py and build_countania.py each carry this inline; from the
fourth chart on (2026-11-09: the adjective canal, the prefix archipelago,
the frequency soundings) a builder only writes its content and calls
build(). What it does, in order:

  * the Sherpa camp shell (assemble) with the series' own header, links and
    result messages, its mountain progression stripped, its SEO block emptied
    (tools/seo.py writes it from the catalogue row) and its <title> set
  * the palette from extract-palette.py's block, contrast asserted
  * the clickable chart's three reading modes and its three panels
  * nine-language example reveals (EX / ex() / exi() and a translations dict)
  * the waterlines, the sky, the gulls, the music, and map-zoom.js
    (Innes, 2026-11-08: "maps need to be expandable always")

Read build_sailing.py's docstring for why the Sherpa shell is borrowed.
"""
import glob, json, re, sys
sys.path.insert(0, 'lesson-template')
sys.path.insert(0, 'lesson-template/build')
sys.path.insert(0, 'lesson-template/build/sherpa/legacy')
sys.path.insert(0, 'tools')
import regularia_map as R

_SNAP = {f: open(f, 'rb').read() for f in glob.glob('sherpa-tensing-camp-*.html')}
from build_c10 import assemble, hero, rule_grid, MARK_FLAG, MARK_TABLE, MARK_FORK, MARK_CLOCK, MARK_PANES  # noqa
from build_c11_12_13 import chart, fork, signals, questions, palette  # noqa
for _f, _b in _SNAP.items():
    if open(_f, 'rb').read() != _b:
        open(_f, 'wb').write(_b)
        print('restored', _f)

# ── examples that carry a translation, in page order ──────────────────
EX = []


def ex(html):
    EX.append(html)
    return '\x01%d\x01%s' % (len(EX) - 1, html)


def exi(html):
    EX.append(html)
    return '<p class="ex" data-tr="%d" style="margin:14px 0 0">%s</p>' % (len(EX) - 1, html)


def hero_block(art, kicker, title, para, alt):
    return hero(kicker, title, para,
                '<button type="button" class="hero-diagram-btn" id="hero-map-btn" aria-label="Expand the map">'
                '<img class="hero-diagram" src="%s/hero.jpg" alt="%s" width="1536" height="1024" loading="eager">'
                '</button>'
                '<div class="img-lightbox" id="hero-lightbox">'
                '<button type="button" class="lightbox-close" aria-label="Close">&times;</button>'
                '<img src="%s/hero.jpg" alt="%s">'
                '</div>' % (art, alt, art, alt))


def palette_from(extracted):
    accent = extracted['contrast']
    paper = R.mix(extracted['secondary'], '#FFFFFF', .82)
    if R.ratio(extracted['text'], paper) < 7:           # a dark secondary (the soundings) makes a dim paper
        paper = R.mix(extracted['secondary'], '#FFFFFF', .9)
    dark, light, lighter = R.mix(accent, '#000000', .3), R.mix(accent, '#FFFFFF', .7), R.mix(accent, '#FFFFFF', .9)
    for fg, bg, need, what in [(extracted['text'], paper, 7, 'ink on paper'),
                               (extracted['text-dim'], paper, 4.5, 'soft ink on paper'),
                               (accent, paper, 4.5, 'accent on paper'),
                               ('#FFFFFF', accent, 4.5, 'white on accent'),
                               (dark, lighter, 4.5, 'dark on lighter')]:
        r = R.ratio(fg, bg)
        assert r >= need, 'palette: %s is %.2f:1, needs %s' % (what, r, need)
    return palette(extracted['text'], extracted['text-dim'], paper, accent, dark, light, lighter)


def panel_css(cls, paint):
    bg = R.mix(paint, '#FFFFFF', .84)
    return ('  .diagram-panel.%s{background:%s;border-color:%s;}\n'
            '  .diagram-panel.%s h4{color:%s;}\n'
            % (cls, bg, R.mix(paint, '#FFFFFF', .45), cls, R.ink_for(bg, 7)))


def diagram(art, uid, overlay, intro, modes, panels, scroll_hint, min_zoom=1100):
    """The interactive chart section. modes: three button labels; panels:
    three (title, cls) pairs (their lists come from build())."""
    btns = ''.join('\n          <button type="button" data-mode="%s"%s aria-pressed="%s">%s</button>'
                   % (m, ' class="on"' if i == 0 else '', 'true' if i == 0 else 'false', label)
                   for i, (m, label) in enumerate(zip(('place', 'verb', 'past'), modes)))
    pans = ''.join('''
          <div class="diagram-panel %s" id="%s-panel-%d">
            <h4>%s</h4>
            <ul id="%s-panel-%d-list"></ul>
          </div>''' % (cls, uid, i, title, uid, i) for i, (title, cls) in enumerate(panels))
    return '''<div class="camp" id="order">
      ''' + MARK_PANES + '''
      <div class="camp-label">Interactive</div>
      <h2>Read the chart</h2>
      <div class="diagram-card" data-map-zoom data-mz-target=".chart-toggle-wrap" data-mz-btn=".name-bar" data-mz-ratio="1.5" data-mz-min="%d">
        <p class="diagram-intro">%s</p>
        <div class="name-bar" id="name-bar">
          <span class="name-label">Read the chart as</span>%s
        </div>
        <div class="diagram-stage" data-mz-scroll>
          <div class="chart-toggle-wrap">
            <img class="chart-photo" src="%s/chart-clean.jpg" alt="" width="1536" height="1024" loading="lazy">
            %s
          </div>
        </div>
        <p class="chart-scroll-hint">%s</p>
        <div class="diagram-panels three">%s
        </div>
      </div>
    </div>

    ''' % (min_zoom, intro, btns, art, overlay, scroll_hint, pans)


NAMES_JS = '''
// the chart reads three ways; all three readings live on each text node
// and swap. A long reading (data-fit) is set a size smaller.
var NAME_ATTR = { place: "data-place", verb: "data-verb", past: "data-past" };
function seaNames(mode){
  document.querySelectorAll(".sail-chart text.place-name").forEach(function(t){
    var v = t.getAttribute(NAME_ATTR[mode]);
    t.textContent = v;
    var small = t.hasAttribute("data-fit") && (v.indexOf("·") >= 0 || v.length > %d);
    t.setAttribute("font-size", small ? Math.min(15, +t.getAttribute("data-size")) : t.getAttribute("data-size"));
    t.style.fontStyle = mode === "place" ? "normal" : "italic";
  });
  document.querySelectorAll("#name-bar button[data-mode]").forEach(function(b){
    var on = b.getAttribute("data-mode") === mode;
    b.classList.toggle("on", on);
    b.setAttribute("aria-pressed", on ? "true" : "false");
  });
}
document.querySelectorAll("#name-bar button[data-mode]").forEach(function(b){
  b.addEventListener("click", function(){ seaNames(b.getAttribute("data-mode")); });
});
'''

PANEL_JS = '''
function renderList(id, items){
  var ul = document.getElementById(id);
  if (!ul) return;
  ul.innerHTML = "";
  items.forEach(function(it){
    var li = document.createElement("li");
    li.innerHTML = it[1];
    if (it[0]) li.setAttribute("data-key", it[0]);
    ul.appendChild(li);
  });
}
var PANELS = %s;
PANELS.forEach(function(items, i){ renderList("%s-panel-" + i + "-list", items); });
function pulseShape(el){
  el.animate([{ opacity: 1 }, { opacity: 0.55 }, { opacity: 1 }], { duration: 380, easing: "ease-out" });
}
// clicking a place lights its panel, and its own line in it
var TARGETS = %s;
Object.keys(TARGETS).forEach(function(key){
  var el = document.getElementById("%s-" + key);
  if (!el) return;
  var t = TARGETS[key];
  var activate = function(){
    pulseShape(el);
    document.querySelectorAll(".diagram-panel").forEach(function(p){ p.style.outline = "none"; });
    document.querySelectorAll(".diagram-panel li.is-lit").forEach(function(li){ li.classList.remove("is-lit"); });
    var panel = document.getElementById("%s-panel-" + t[0]);
    if (!panel) return;
    panel.style.outline = "2px solid " + t[2];
    if (t[1]) panel.querySelectorAll('li[data-key="' + t[1] + '"]').forEach(function(li){ li.classList.add("is-lit"); });
    panel.scrollIntoView({ block: "nearest", behavior: "smooth" });
  };
  el.addEventListener("click", activate);
  el.addEventListener("keydown", function(e){
    if (e.key === "Enter" || e.key === " "){ e.preventDefault(); activate(); }
  });
});
'''


def build(out, art, title, sub, extracted, hero_html, hero_end, cta, body, quiz, uid, panel_items, targets,
          panel_paints, translations, results, next_link, gull_seed=17, long_name=13, extra_css=''):
    """Write the page. hero_end: the hero paragraph's last words (the CTA
    goes after them); cta: (anchor, label); panel_items: three lists of
    (key, html); targets: {hotspot key: (panel index, row key, colour)};
    results: the three result messages; next_link: (href, label)."""
    for items in panel_items:
        for _k, t in items:
            assert '"' not in t, 'a panel line would break its JS string: ' + t
    for q in quiz:
        for part in (q[0], q[1], q[2], q[4]) + tuple(q[3]):
            assert '"' not in part, 'a quiz string would break its JS: ' + part
        assert q[2] in q[3], 'the answer is not among the options: ' + q[0]

    _reg = open('lesson-template/build/build_regularia.py', encoding='utf-8').read()
    i = _reg.index("LIGHTBOX_JS = '''") + 17
    lightbox_js = _reg[i:_reg.index("'''", i)]
    i = _reg.index("EXTRA_CSS = '''") + 15
    head_css = _reg[i:_reg.index("''' + WATERLINES + '''")]
    i = _reg.index("  .diagram-panel li{padding:3px 6px;")
    chart_css = _reg[i:_reg.index("'''\n\n# the result messages")]
    _sail = open('lesson-template/build/build_sailing.py', encoding='utf-8').read()
    waterlines = _sail[_sail.index('/* Waterlining:'):_sail.index('  /* ── the sea chart ── */')]

    gulls_js = open('lesson-template/build/gulls.js', encoding='utf-8').read() + '''
skyGulls(document.getElementById("gull-sky"), {
  px: function (w) { return w < 560 ? 26 : 34; }, seed: %d,
  flocks: [
    {from: [108, 64], to: [-8, 24], flight: 17, cycle: 46, at: 5,
     birds: [[0, 0, 1], [-1.5, 1.1, .95], [-1.1, -1.3, 1.05]]},
    {from: [-8, 18], to: [108, 50], flight: 15, cycle: 46, at: 28,
     birds: [[0, 0, 1], [-1.4, -1, .92]]}
  ]
});
''' % gull_seed

    import sherpa_sky, sherpa_topo
    music = json.load(open('sailing-the-seas-of-grammar/music.json', encoding='utf-8'))
    music_tag = ('<script src="block-camp/camp-music.js" data-track="sailing-the-seas-of-grammar/music.m4a" '
                 'data-loop="%g %g" defer></script>\n' % tuple(music['loop']))
    sky_css = ('  /* ── the sky: clouds and gulls (see build_sailing.py) ── */\n'
               '  .gull-sky{position:fixed;inset:0;z-index:-1;pointer-events:none;overflow:hidden;}\n'
               '  @media print{.gull-sky{display:none;}}\n'
               '  ' + ','.join(sherpa_topo.HALO_ON) + '{text-shadow:' + sherpa_topo.HALO + ';}\n')
    sky_el = '<div class="gull-sky" id="gull-sky" aria-hidden="true"></div>\n' + sherpa_sky.ELEMENT

    extra = (head_css + waterlines + '''
  /* ── the sea chart ── */
  .hero-diagram{height:auto;}
  .diagram-panels.three{grid-template-columns:repeat(3,1fr);}
  @media (max-width:820px){.diagram-panels.three{grid-template-columns:1fr;}}
''' + panel_css('is-west', panel_paints[0]) + panel_css('is-isle', panel_paints[1])
             + panel_css('is-east', panel_paints[2]) + chart_css + extra_css)

    js = (PANEL_JS % (json.dumps(panel_items), uid, json.dumps(targets), uid, uid)
          + NAMES_JS % long_name + lightbox_js + gulls_js)

    shell_results = [
        '"Clean run. You can tell a decision from a plan, and a belief from a forecast."',
        '"Solid progress. Worth a look back at camp five before camp eight."',
        '"Good first attempt. The will/going to fork is the part to read again."']
    replacements = [
        (hero_end + '</p>\n    </div>',
         hero_end + '</p>\n      <a class="hero-cta" href="#%s">%s <span aria-hidden="true">&rarr;</span></a>\n    </div>' % cta),
        ('<div class="brand">Sherpa <span>Tensing</span></div>',
         '<div class="brand">Sailing the <span>Seas of Grammar</span></div>'),
        ('<div class="sub">Forbes English &middot; a route up the tenses</div>',
         '<div class="sub">Forbes English &middot; %s</div>' % sub),
        ('<a class="up-link" href="sherpa-tensing-route-map.html"><span class="arw" aria-hidden="true">&larr;</span>Route map</a>',
         '<a class="up-link" href="grammar.html#maps"><span class="arw" aria-hidden="true">&larr;</span>Grammar maps</a>'),
        ('<div class="camp-label">Summit log</div>', '<div class="camp-label">Ship&#39;s log</div>'),
        ('<button class="retry-btn" id="retry-btn">Climb again</button>',
         '<button class="retry-btn" id="retry-btn">Sail it again</button>'),
        ('<a class="base-camp" href="sherpa-tensing-route-map.html">&larr; Return to base camp</a>',
         '<a class="base-camp" href="grammar.html#maps">&larr; Back to the grammar maps</a>'),
        ('<a class="next-camp" href="sherpa-tensing-route-map.html">Choose your next camp &rarr;</a>',
         '<a class="next-camp" href="%s">%s &rarr;</a>' % next_link),
        ('/* ── NOW vs WILL DIAGRAM CAMP ── */', '/* ── THE SEA CHART ── */'),
        ('// ── NOW vs WILL diagram interactivity ──', '// ── the chart, made clickable ──'),
        ('\n</style>', extra + sky_css + '</style>'),
        ('<div class="camp-label">The fork in the path</div>', '<div class="camp-label">The traps</div>'),
        ('<div class="camp-label">Trail markers</div>', '<div class="camp-label">Tide tables</div>'),
        ('<div class="camp-label">The climb</div>', '<div class="camp-label">The crossing</div>'),
        ('"Reach the summit"', '"Make landfall"'),
    ] + [(a, '"%s"' % b) for a, b in zip(shell_results, results)]
    for r in results:
        assert '"' not in r and '&#39;' not in r, 'result messages are set as text: use ’'

    ttl = '<title>%s</title>' % title
    s = assemble(hero_html, body, js, questions(quiz), palette_from(extracted), ttl, replacements, out, own_tail=False)
    for a, _b in replacements:
        if a != '\n</style>':
            assert a not in s, 'replacement did not land: %r' % a[:70]

    s = open(out, encoding='utf-8').read()
    a = s.index('\n// ── progression:')
    b = a + re.search(r'\nsherpaBar\(\);\n', s[a:]).end()
    s = s[:a] + '\n' + s[b:]
    s = re.sub(r'\n  /\* ── progression: the voice toggle and its lock ── \*/.*?\n(?=  /\*|\})',
               '\n', s, count=1, flags=re.S)
    s = re.sub(r'<div class="ex">\x01(\d+)\x01', r'<div class="ex" data-tr="\1">', s)
    assert '\x01' not in s, 'an example marker escaped'

    rows = []
    for i in range(len(EX)):
        r = translations.get(i)
        assert r and len(r) == 9, 'missing or short translation for example %d: %s' % (i, EX[i])
        rows.append('"%d": %s' % (i, json.dumps(r, ensure_ascii=False)))
    assert len(translations) == len(EX), '%d translations for %d examples' % (len(translations), len(EX))
    s = re.sub(r'var EX_TR = \{.*?\};\n', lambda m: 'var EX_TR = {%s};\n' % ", ".join(rows), s, count=1, flags=re.S)

    from PIL import Image
    sizes = {k: Image.open('Sherpa Tensing/cloud-%d.webp' % k).size for k in range(1, sherpa_sky.IMAGES + 1)}
    assert s.count('</head>') == 1
    s = s.replace('</head>', sherpa_sky.block(sizes) + '</head>', 1)
    s, n = re.subn(r'(<body\b[^>]*>\n?)', lambda m: m.group(1) + sky_el, s, count=1)
    assert n == 1, 'no <body> to hang the sky on'
    assert s.count('</body>') == 1
    s = s.replace('</body>', music_tag + '<script src="map-zoom.js" defer></script>\n</body>', 1)
    s, n = re.subn(r'(<!-- SEO:start -->).*?(<!-- SEO:end -->)', r'\1\n\2', s, count=1, flags=re.S)
    assert n == 1, 'no SEO block in the shell'
    s, n = re.subn(r'<title>.*?</title>', ttl, s, count=1, flags=re.S)
    assert n == 1, 'no <title> in the shell'
    for leak in ('Camp Seven', 'camp seven', 'will/going to', 'willExamples'):
        assert leak not in s, 'the Sherpa shell leaked: %s' % leak
    open(out, 'w', encoding='utf-8', newline='').write(s)
    print('wrote %s: %d examples, %d questions, %d bytes' % (out, len(EX), len(quiz), len(s)))
