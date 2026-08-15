import json, re

with open('/tmp/sections_i18n.json', encoding='utf-8') as f:
    SECTION_GLOSS = json.load(f)
with open('/tmp/all_questions_i18n.json', encoding='utf-8') as f:
    QUESTION_I18N = json.load(f)
with open('/tmp/ui_i18n.json', encoding='utf-8') as f:
    UI_I18N = json.load(f)

LANGS = [
 {"code":"de","flag":"\U0001F1E9\U0001F1EA","name":"Deutsch"},
 {"code":"it","flag":"\U0001F1EE\U0001F1F9","name":"Italiano"},
 {"code":"es","flag":"\U0001F1EA\U0001F1F8","name":"Español"},
 {"code":"fr","flag":"\U0001F1EB\U0001F1F7","name":"Français"},
 {"code":"ja","flag":"\U0001F1EF\U0001F1F5","name":"日本語"},
 {"code":"zh","flag":"\U0001F1E8\U0001F1F3","name":"中文"},
 {"code":"ar","flag":"\U0001F1F8\U0001F1E6","name":"العربية"},
 {"code":"ru","flag":"\U0001F1F7\U0001F1FA","name":"Русский"},
 {"code":"pt","flag":"\U0001F1F5\U0001F1F9","name":"Português"},
]

def js_str(s):
    return json.dumps(s, ensure_ascii=False)

def build_source(path, default_lang):
    with open(path, encoding='utf-8') as f:
        src = f.read()

    # ── 1. CSS additions before </style> ──
    css_add = """
/* ── LOGO / HERO (house style) ── */
.logo-wrap { display:flex; justify-content:center; margin: 4px 0 14px; }
.logo-wrap svg { width: 190px; height: auto; }
.hero-wrap { margin: 0 0 20px; border-radius: 10px; overflow: hidden; box-shadow: 0 8px 22px rgba(15,50,63,0.18); }
.hero-wrap img { width: 100%; height: auto; display: block; }

/* ── LANGUAGE SWITCHER ── */
.lang-switcher { margin: 0 0 22px; }
.lang-switcher-label { font-family: 'Space Mono', monospace; font-size: 10px; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); margin-bottom: 8px; }
.lang-grid { display: flex; flex-wrap: wrap; gap: 6px; }
.lang-btn { display: flex; align-items: center; gap: 6px; border: 1.5px solid var(--line); border-radius: 20px; padding: 6px 12px 6px 8px; background: var(--bg); cursor: pointer; font-family: 'Karla', sans-serif; font-size: 12.5px; font-weight: 600; color: var(--ink); transition: border-color .15s, background .15s; }
.lang-btn .flag { font-size: 15px; }
.lang-btn:hover { border-color: var(--ink); }
.lang-btn.active { border-color: var(--ink); background: var(--ink); color: #fff; }
"""
    src = src.replace("</style>", css_add + "</style>")

    # ── 2. body background gradient (house style item 3, from hero palette) ──
    src = src.replace(
        "body {\n  background: var(--bg);",
        "body {\n  background: linear-gradient(180deg, rgba(207,107,78,0.07) 0%, rgba(42,96,132,0.06) 45%, var(--bg) 100%);"
    )

    # ── 3. Insert logo + hero + lang switcher inside .intro, before intro-eye ──
    logo_svg = '''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(117.25,14.15) scale(0.040349)"><g transform="translate(0,1504) scale(0.1,-0.1)" fill="var(--ink)" stroke="none"><path d="M14940 11379 c-58 -10 -226 -34 -375 -54 -148 -20 -305 -41 -348 -47 l-78 -10 3 -146 3 -146 76 -12 c42 -6 85 -17 97 -23 27 -15 66 -67 82 -111 21 -57 27 -487 25 -1635 -2 -832 -6 -1120 -18 -1295 -8 -124 -14 -226 -13 -227 9 -9 462 -54 473 -47 7 5 40 61 72 124 32 63 63 116 68 117 6 2 43 -24 84 -58 105 -89 177 -133 272 -167 125 -45 205 -57 372 -57 316 1 518 82 725 294 141 144 224 297 285 521 74 276 91 648 42 925 -32 176 -68 310 -113 418 -164 392 -526 609 -944 565 -204 -21 -372 -97 -522 -237 l-48 -44 0 656 0 655 -31 31 c-35 36 -40 36 -189 10z m788 -1611 c112 -42 190 -158 236 -353 43 -182 55 -299 51 -525 -6 -382 -71 -618 -205 -744 -76 -71 -126 -91 -235 -91 -57 0 -110 6 -145 17 -71 22 -169 81 -225 135 l-45 43 0 669 0 669 54 49 c84 77 226 144 331 156 51 6 127 -4 183 -25z"/><path d="M6896 11053 c-4 -71 -3 -141 2 -158 8 -28 13 -31 89 -46 44 -9 95 -21 112 -29 43 -17 88 -72 98 -117 11 -50 10 -2471 0 -2545 -5 -31 -18 -72 -30 -89 -26 -39 -95 -76 -157 -84 -25 -3 -62 -8 -82 -11 l-38 -6 0 -159 0 -159 755 0 755 0 -2 163 -3 162 -87 7 c-175 13 -250 55 -284 158 -16 49 -18 108 -22 558 l-3 502 236 0 c344 0 346 -1 410 -267 l18 -73 168 0 169 0 -2 553 -3 552 -167 3 c-167 2 -168 2 -172 -20 -2 -13 -9 -54 -16 -93 -21 -126 -70 -206 -139 -225 -20 -5 -141 -10 -268 -10 l-233 0 0 555 0 556 428 -3 c473 -3 469 -3 540 -71 46 -44 78 -108 132 -267 l46 -135 203 -3 203 -2 -6 67 c-3 38 -15 205 -26 373 -11 168 -22 347 -26 398 l-6 92 -1293 0 -1292 0 -7 -127z"/><path d="M10520 10306 c-503 -73 -861 -361 -1014 -817 -51 -153 -68 -261 -73 -477 -6 -224 4 -336 43 -502 62 -263 143 -419 296 -569 255 -249 547 -361 939 -361 298 0 517 60 724 198 282 187 439 437 517 823 20 100 23 142 23 339 -1 205 -3 236 -27 350 -76 353 -203 581 -425 759 -147 119 -353 211 -551 247 -120 22 -335 26 -452 10z m325 -436 c141 -69 239 -258 297 -571 20 -108 22 -158 23 -384 0 -288 -10 -379 -57 -540 -52 -176 -121 -278 -224 -330 -47 -24 -73 -30 -145 -33 -171 -8 -285 53 -372 199 -95 161 -150 473 -142 809 10 449 121 745 315 845 58 30 81 34 170 32 67 -2 96 -7 135 -27z"/><path d="M18255 10313 c-141 -16 -204 -29 -292 -58 -271 -90 -467 -237 -611 -458 -182 -280 -257 -619 -223 -1007 37 -415 159 -696 387 -893 253 -218 538 -317 914 -317 341 1 615 84 815 247 60 49 185 177 191 195 4 14 -19 57 -77 144 -45 69 -86 127 -91 130 -5 3 -43 -17 -86 -44 -164 -106 -284 -154 -430 -173 -168 -22 -350 5 -497 76 -134 64 -216 161 -275 323 -33 90 -77 320 -67 347 6 13 94 15 776 15 l769 0 7 113 c7 120 -6 307 -31 447 -62 340 -198 580 -413 723 -95 64 -242 133 -334 156 -127 33 -318 48 -432 34z m221 -427 c132 -62 228 -270 241 -528 l6 -118 -408 0 -408 0 7 68 c25 246 110 453 221 538 87 66 245 85 341 40z"/><path d="M20656 10309 c-301 -29 -581 -166 -723 -354 -56 -73 -116 -197 -140 -285 -13 -48 -17 -103 -17 -210 0 -129 3 -155 28 -235 35 -114 68 -174 134 -246 129 -140 318 -226 797 -364 192 -55 255 -84 317 -146 106 -107 103 -287 -8 -389 -84 -78 -192 -107 -357 -97 -209 13 -353 92 -403 223 -10 27 -32 101 -49 164 l-30 115 -219 3 -219 2 6 -256 c4 -142 7 -304 7 -360 0 -122 -15 -107 173 -170 263 -88 487 -124 781 -124 205 0 315 10 436 41 164 41 281 102 392 207 155 146 233 326 245 562 12 245 -69 470 -218 604 -123 111 -266 178 -599 281 -385 119 -458 152 -515 234 -28 40 -30 49 -29 124 1 125 43 190 154 241 111 51 254 56 389 14 121 -37 177 -121 236 -353 l20 -80 205 0 205 0 3 346 2 347 -112 40 c-318 112 -594 149 -892 121z"/><path d="M12620 10249 c-223 -32 -411 -61 -417 -64 -10 -3 -13 -42 -13 -149 l0 -144 58 -7 c111 -13 183 -65 199 -143 4 -20 8 -397 8 -837 0 -787 0 -801 -21 -840 -26 -52 -87 -83 -177 -92 l-67 -6 0 -41 c0 -23 -3 -94 -7 -158 l-6 -118 702 0 701 0 0 159 0 158 -83 6 c-146 12 -214 43 -253 119 -27 51 -37 294 -30 722 7 428 12 470 69 579 82 157 210 228 407 226 76 0 166 -18 278 -54 12 -4 22 -3 22 1 0 5 20 167 44 359 25 193 41 353 38 356 -14 14 -115 29 -188 29 -112 0 -217 -25 -319 -75 -170 -83 -273 -193 -362 -382 -26 -56 -51 -103 -55 -103 -5 0 -8 15 -8 33 0 18 -7 134 -15 258 -15 218 -16 225 -41 247 -14 12 -33 22 -42 21 -9 0 -199 -27 -422 -60z"/></g></g>
      <text x="150" y="80" text-anchor="middle" font-family="Arial, sans-serif" font-weight="700" font-size="38.40" letter-spacing="3" fill="var(--ink)">ENGLISH</text>
    </svg>'''

    lang_buttons = "\n".join(
        f'''      <button class="lang-btn" data-lang="{l['code']}"><span class="flag">{l['flag']}</span>{l['name']}</button>'''
        for l in LANGS
    )

    # Extract this file's actual current literal strings (language-specific) via regex
    m = re.search(
        r'<div class="intro" id="intro">\s*'
        r'<div class="intro-eye">([^<]*)</div>\s*'
        r'<h1>([^<]*)</h1>\s*'
        r'<p class="sub">([^<]*)</p>',
        src
    )
    assert m, "could not locate intro block"
    cur_introEye, cur_h1, cur_sub = m.group(1), m.group(2), m.group(3)

    intro_prefix_old = f'''<!-- INTRO -->
<div class="intro" id="intro">
  <div class="intro-eye">{cur_introEye}</div>
  <h1>{cur_h1}</h1>
  <p class="sub">{cur_sub}</p>'''

    intro_prefix_new = f'''<!-- INTRO -->
<div class="intro" id="intro">
  <div class="logo-wrap">
    {logo_svg}
  </div>
  <div class="hero-wrap">
    <img src="grammarjail/jail-test-room.jpg" alt="A stylised test room with pastel blue and coral walls, a hanging lamp, a small desk with a glass of water and papers, seen through vertical bars">
  </div>
  <div class="lang-switcher">
    <div class="lang-switcher-label" id="langSwitcherLabel">{cur_introEye}</div>
    <div class="lang-grid" id="langGrid">
{lang_buttons}
    </div>
  </div>
  <div class="intro-eye" id="introEye">{cur_introEye}</div>
  <h1 id="introH1">{cur_h1}</h1>
  <p class="sub" id="introSub">{cur_sub}</p>'''

    assert intro_prefix_old in src, "intro prefix not found"
    src = src.replace(intro_prefix_old, intro_prefix_new)

    # give type-legend spans + start button ids for JS updates
    m2 = re.search(
        r'<div class="type-legend">\s*'
        r'<span class="type-tag">([^<]*)</span>\s*'
        r'<span class="type-tag">([^<]*)</span>\s*'
        r'<span class="type-tag">([^<]*)</span>\s*'
        r'</div>\s*'
        r'<button class="start-btn" id="startBtn">([^<]*)</button>',
        src
    )
    assert m2, "could not locate type-legend block"
    t1, t2, t3, cur_startBtn = m2.groups()

    old_legend = f'''  <div class="type-legend">
    <span class="type-tag">{t1}</span>
    <span class="type-tag">{t2}</span>
    <span class="type-tag">{t3}</span>
  </div>

  <button class="start-btn" id="startBtn">{cur_startBtn}</button>'''
    new_legend = f'''  <div class="type-legend" id="typeLegend">
    <span class="type-tag">{t1}</span>
    <span class="type-tag">{t2}</span>
    <span class="type-tag">{t3}</span>
  </div>

  <button class="start-btn" id="startBtn">{cur_startBtn}</button>'''
    assert old_legend in src
    src = src.replace(old_legend, new_legend)

    # results section: add ids
    m3 = re.search(r'<div class="results" id="results">\s*<div class="res-eye">([^<]*)</div>', src)
    assert m3, "could not locate res-eye"
    cur_resEye = m3.group(1)
    old_results = f'''<div class="results" id="results">
  <div class="res-eye">{cur_resEye}</div>'''
    new_results = f'''<div class="results" id="results">
  <div class="res-eye" id="resEye">{cur_resEye}</div>'''
    assert old_results in src
    src = src.replace(old_results, new_results)

    # ── 4. Replace SECTIONS array (strip de field) ──
    sec_start = src.index('const SECTIONS')
    sec_end = src.index('];', sec_start) + 2
    old_sections_block = src[sec_start:sec_end]
    # parse ids/labels/colors/qs via regex from original block
    sec_rows = re.findall(
        r'\{\s*id:"([^"]+)",\s*label:"((?:[^"\\]|\\.)+)",\s*de:"(?:[^"\\]|\\.)*",\s*color:"(var\(--[a-z\-]+\))",\s*qs:\[([^\]]+)\]\s*\}',
        old_sections_block
    )
    assert len(sec_rows) == 15, f"expected 15 sections, got {len(sec_rows)}"
    new_sections_lines = ["const SECTIONS = ["]
    for sid, label, color, qs in sec_rows:
        label_unescaped = label.replace('\\"', '"').replace("\\'", "'")
        new_sections_lines.append(f'  {{ id:"{sid}", label:{js_str(label_unescaped)}, color:"{color}", qs:[{qs}] }},')
    new_sections_lines.append("];")
    new_sections_block = "\n".join(new_sections_lines)
    src = src[:sec_start] + new_sections_block + src[sec_end:]

    # ── 5. Replace QUESTIONS array (strip de/feedbackDe fields) ──
    q_start = src.index('const QUESTIONS')
    q_end = src.index('\n];', q_start) + 3
    old_questions_block = src[q_start:q_end]

    # Remove the `de:"..."` and `feedbackDe:"..."` lines (they are always on their own lines in this file)
    # de line pattern:      de:"....",\n   (value may contain escaped quotes \")
    def strip_field(block, field, trailing_comma=True):
        suffix = r',' if trailing_comma else ''
        pattern = re.compile(r'\n\s*' + field + r':"(?:[^"\\]|\\.)*"' + suffix)
        return pattern.sub('', block)

    new_questions_block = old_questions_block
    new_questions_block = strip_field(new_questions_block, 'de', trailing_comma=True)
    new_questions_block = strip_field(new_questions_block, 'feedbackDe', trailing_comma=False)

    src = src[:q_start] + new_questions_block + src[q_end:]

    # ── 6. Insert i18n data blocks right after QUESTIONS array ──
    insert_marker = new_questions_block[-3:]  # "\n];"
    q_end2 = src.index('const QUESTIONS')
    q_end2 = src.index('\n];', q_end2) + 3

    i18n_block = f'''

/* ══ I18N DATA ══ */
const LANGS = {json.dumps(LANGS, ensure_ascii=False)};
let currentLang = "{default_lang}";
const UI_I18N = {json.dumps(UI_I18N, ensure_ascii=False)};
const SECTION_GLOSS = {json.dumps(SECTION_GLOSS, ensure_ascii=False)};
const QUESTION_I18N = {json.dumps(QUESTION_I18N, ensure_ascii=False)};

function ui(){{ return UI_I18N[currentLang]; }}

function updateStaticUI(){{
  const u = ui();
  document.getElementById('langSwitcherLabel').textContent = u.langLabel;
  document.getElementById('introEye').textContent = u.introEye;
  document.getElementById('introH1').textContent = u.h1;
  document.getElementById('introSub').textContent = u.sub;
  const tags = document.querySelectorAll('#typeLegend .type-tag');
  tags.forEach((el,i)=>{{ el.textContent = u.typeTags[i]; }});
  document.getElementById('startBtn').textContent = u.startBtn;
  document.getElementById('resEye').textContent = u.resEye;
  document.getElementById('retryBtn').textContent = u.retryBtn;
  document.querySelectorAll('.lang-btn').forEach(btn=>{{
    btn.classList.toggle('active', btn.dataset.lang===currentLang);
  }});
}}

document.getElementById('langGrid').addEventListener('click', (e)=>{{
  const btn = e.target.closest('.lang-btn');
  if(!btn) return;
  currentLang = btn.dataset.lang;
  updateStaticUI();
}});
'''
    src = src[:q_end2] + i18n_block + src[q_end2:]

    # ── 7. renderAll(): sec-banner + qtext blocks ──
    m4 = re.search(
        r'<div class="sec-qrange">([A-Za-zÀ-ÿ]*) \$\{sec\.qs\[0\]\+1\}',
        src
    )
    assert m4, "could not locate sec-qrange word"
    qrange_word = m4.group(1)

    old_banner_html = '''bn.innerHTML=`<div class="sec-icon" style="background:${sec.color}">${sec.qs[0]+1}–${sec.qs[2]+1}</div>
      <div><div class="sec-title">${sec.label}</div><div class="sec-de">${sec.de}</div></div>
      <div class="sec-qrange">''' + qrange_word + ''' ${sec.qs[0]+1}–${sec.qs[2]+1}</div>`;'''
    new_banner_html = '''bn.innerHTML=`<div class="sec-icon" style="background:${sec.color}">${sec.qs[0]+1}–${sec.qs[2]+1}</div>
      <div><div class="sec-title">${sec.label}</div><div class="sec-de">${SECTION_GLOSS[currentLang][si]}</div></div>
      <div class="sec-qrange">${sec.qs[0]+1}–${sec.qs[2]+1}</div>`;'''
    assert old_banner_html in src, "banner html mismatch"
    src = src.replace(old_banner_html, new_banner_html)

    src = src.replace("SECTIONS.forEach(sec=>{\n    // Banner", "SECTIONS.forEach((sec,si)=>{\n    // Banner")

    m5 = re.search(r'<span class="qnum">([A-Za-zÀ-ÿ]*) \$\{qi\+1\}', src)
    assert m5, "could not locate qnum word"
    question_word = m5.group(1)

    old_qtext = '''      let inner=`<div class="qmeta">
        <span class="qnum">''' + question_word + ''' ${qi+1} · ${typeLabel}</span>
        <span class="qtype-tag">${typeLabel}</span>
      </div>
      <div class="qtext">${q.en}</div>
      <div class="qde">${q.de}</div>`;'''
    new_qtext = '''      let inner=`<div class="qmeta">
        <span class="qnum">${ui().questionWord} ${qi+1} · ${typeLabel}</span>
        <span class="qtype-tag">${typeLabel}</span>
      </div>
      <div class="qtext">${q.en}</div>
      <div class="qde">${QUESTION_I18N[currentLang][qi][0]}</div>`;'''
    assert old_qtext in src, "qtext mismatch"
    src = src.replace(old_qtext, new_qtext)

    m6 = re.search(r'<div class="gap-hint">([A-Za-zÀ-ÿ]*:) \$\{q\.hint\}</div>\s*</div>\s*<button class="submit-gap" id="gs\$\{qi\}">([^<]*)</button>', src)
    assert m6, "could not locate gap-hint/submit-gap words"
    hint_word, check_word = m6.groups()

    old_gap = '''        inner+=`<div class="gap-wrap">
          <input class="gap-input" id="gi${qi}" type="text" placeholder="…" autocomplete="off" autocorrect="off" spellcheck="false"/>
          <div class="gap-hint">''' + hint_word + ''' ${q.hint}</div>
        </div>
        <button class="submit-gap" id="gs${qi}">''' + check_word + '''</button>`;'''
    new_gap = '''        inner+=`<div class="gap-wrap">
          <input class="gap-input" id="gi${qi}" type="text" placeholder="…" autocomplete="off" autocorrect="off" spellcheck="false"/>
          <div class="gap-hint">${ui().hintLabel} ${q.hint}</div>
        </div>
        <button class="submit-gap" id="gs${qi}">${ui().checkBtn}</button>`;'''
    assert old_gap in src, "gap mismatch"
    src = src.replace(old_gap, new_gap)

    m7 = re.search(r"qi===44\?'([^']*)':'([^']*)'", src)
    assert m7, "could not locate next-btn labels"
    results_word, next_word = m7.groups()

    old_next = '''      inner+=`<div class="feedback" id="fb${qi}"></div>
        <button class="next-btn" id="nb${qi}">${qi===44?\'''' + results_word + '''\':\'''' + next_word + '''\'}</button>`;'''
    new_next = '''      inner+=`<div class="feedback" id="fb${qi}"></div>
        <button class="next-btn" id="nb${qi}">${qi===44?ui().resultsBtn:ui().nextBtn}</button>`;'''
    assert old_next in src, "next-btn mismatch"
    src = src.replace(old_next, new_next)

    # ── 8. showFeedback ──
    m9 = re.search(r'<span class="(fb-[a-z]+)">\$\{q\.feedbackDe\}', src)
    assert m9, "could not locate fb class"
    fb_class = m9.group(1)
    old_fb = '  fb.innerHTML=`${q.feedbackEn}<span class="' + fb_class + '">${q.feedbackDe}</span>`;'
    new_fb = '  fb.innerHTML=`${q.feedbackEn}<span class="' + fb_class + '">${QUESTION_I18N[currentLang][qi][1]}</span>`;'
    assert old_fb in src, "feedback mismatch"
    src = src.replace(old_fb, new_fb)

    # ── 9. showResults verdicts ──
    m8 = re.search(
        r'if\(pct>=0\.89\)\{v="([^"]*)";vd="([^"]*)";\}\s*'
        r'else if\(pct>=0\.75\)\{v="([^"]*)";vd="([^"]*)";\}\s*'
        r'else if\(pct>=0\.6\)\{v="([^"]*)";vd="([^"]*)";\}\s*'
        r'else\{v="([^"]*)";vd="([^"]*)";\}',
        src
    )
    assert m8, "could not locate verdict block"
    v1,vd1,v2,vd2,v3,vd3,v4,vd4 = m8.groups()

    old_verdicts = f'''  const pct=score/45;
  let v,vd;
  if(pct>=0.89){{v="{v1}";vd="{vd1}";}}
  else if(pct>=0.75){{v="{v2}";vd="{vd2}";}}
  else if(pct>=0.6){{v="{v3}";vd="{vd3}";}}
  else{{v="{v4}";vd="{vd4}";}}
  document.getElementById('verdict').textContent=v;
  document.getElementById('verdictDe').textContent=vd;'''
    new_verdicts = '''  const pct=score/45;
  const vs=ui().verdicts;
  let tier = pct>=0.89?0 : pct>=0.75?1 : pct>=0.6?2 : 3;
  document.getElementById('verdict').textContent=vs[tier][0];
  document.getElementById('verdictDe').textContent=vs[tier][1];'''
    assert old_verdicts in src, "verdicts mismatch"
    src = src.replace(old_verdicts, new_verdicts)

    # ── 10. startBtn handler: call updateStaticUI() once more defensively + keep lang locked ──
    old_start = '''document.getElementById('startBtn').addEventListener('click',()=>{
  document.getElementById('intro').style.display='none';
  prepareQuestions();
  renderAll();'''
    new_start = '''document.getElementById('startBtn').addEventListener('click',()=>{
  document.getElementById('intro').style.display='none';
  prepareQuestions();
  renderAll();
  updateStaticUI();'''
    assert old_start in src
    src = src.replace(old_start, new_start)

    # call updateStaticUI() on load
    src = src.replace(
        "document.getElementById('retryBtn').addEventListener('click',reset);",
        "document.getElementById('retryBtn').addEventListener('click',reset);\nupdateStaticUI();"
    )

    return src

en_out = build_source('/home/claude/forbes-english/full_grammar_test.html', 'de')
with open('/home/claude/forbes-english/full_grammar_test.html', 'w', encoding='utf-8') as f:
    f.write(en_out)
print("full_grammar_test.html written, length", len(en_out))

it_out = build_source('/home/claude/forbes-english/full_grammar_test_italian.html', 'it')
with open('/home/claude/forbes-english/full_grammar_test_italian.html', 'w', encoding='utf-8') as f:
    f.write(it_out)
print("full_grammar_test_italian.html written, length", len(it_out))
