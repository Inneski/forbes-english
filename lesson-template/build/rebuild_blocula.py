#!/usr/bin/env python3
"""Rebuild block-camp/dracula-castle-of-if.html as "Grammar Stoker's Blocula".

Three changes to the published file, done as string surgery on the shipped HTML
(this lesson was hand-built; it has no builder in lesson-template/build/):

1. Text lives behind a shimmering hotspot. Every scene opens on the full
   artwork with only the HUD and a pulsing gold marker on the story object.
   Clicking the marker (or ENTER) grows the text panel out of that point;
   ESC, the HIDE button, or a click on the picture folds it away again.
   The side gradients (.shade) that used to darken 70% of the frame are gone;
   the panel carries its own plate.
2. Title: "Grammar Stoker's" small, "BLOCULA" big, in the pixel font.
3. Translation glosses in nine languages: ES DE FR IT PT PL ZH JA TR.
"""
import json, re, sys, html

SRC = '/root/work/original.html'
OUT = sys.argv[1] if len(sys.argv) > 1 else '/root/repo/block-camp/dracula-castle-of-if.html'
WORK = '/root/work'
LANGS = ['es', 'de', 'fr', 'it', 'pt', 'pl', 'zh', 'ja', 'tr', 'ar', 'ru']

s = open(SRC, encoding='utf-8').read()

# ---------------------------------------------------------------- 1. strings
pat = re.compile(r"T\('((?:[^'\\]|\\.)*)','((?:[^'\\]|\\.)*)','((?:[^'\\]|\\.)*)'\)")
tr = {l: json.load(open(f'{WORK}/tr_{l}.json', encoding='utf-8')) for l in LANGS[2:]}

def jsq(t):
    return "'" + t.replace('\\', '\\\\').replace("'", "\\'") + "'"

counter = [0]
def sub(m):
    i = counter[0]; counter[0] += 1
    en, es, de = m.group(1), m.group(2), m.group(3)
    parts = [m.group(1), m.group(2), m.group(3)]  # keep original escaping for en/es/de
    out = "T(" + ",".join("'" + p + "'" for p in parts)
    for l in LANGS[2:]:
        out += "," + jsq(tr[l][str(i)])
    return out + ")"

head_i = s.index('<script>\nconst IMAGES')
page, js = s[:head_i], s[head_i:]
js = pat.sub(sub, js)
assert counter[0] == 274, counter[0]

js = js.replace("const T=(en,es,de)=>({en,es,de});",
    "const LANGS=['es','de','fr','it','pt','pl','zh','ja','tr','ar','ru'];\n"
    "const LANG_NAMES={es:'Español',de:'Deutsch',fr:'Français',it:'Italiano',pt:'Português',pl:'Polski',zh:'中文',ja:'日本語',tr:'Türkçe',ar:'العربية',ru:'Русский'};\n"
    "const T=(en,...r)=>{const o={en};LANGS.forEach((l,i)=>o[l]=r[i]);return o};")

# extra UI labels (9 languages) – the read hint and the hide button
js = js.replace("  subtitle:T(",
    "  read:T('CLICK TO READ','PULSA PARA LEER','KLICKEN ZUM LESEN','CLIQUE POUR LIRE','CLICCA PER LEGGERE','CLIQUE PARA LER','KLIKNIJ, ABY CZYTAĆ','点击阅读','クリックして読む','OKUMAK İÇİN TIKLA','انقر للقراءة','НАЖМИ, ЧТОБЫ ЧИТАТЬ'),\n"
    "  hide:T('HIDE','OCULTAR','AUSBLENDEN','MASQUER','NASCONDI','OCULTAR','UKRYJ','隐藏','隠す','GİZLE','إخفاء','СКРЫТЬ'),\n"
    "  fullscreen:T('FULLSCREEN','PANTALLA COMPLETA','VOLLBILD','PLEIN ÉCRAN','SCHERMO INTERO','ECRÃ INTEIRO','PEŁNY EKRAN','全屏','全画面','TAM EKRAN','ملء الشاشة','ВО ВЕСЬ ЭКРАН'),\n"
    "  translate:T('TRANSLATE','TRADUCIR','ÜBERSETZEN','TRADUIRE','TRADUCI','TRADUZIR','TŁUMACZ','翻译','翻訳','ÇEVİR','ترجمة','ПЕРЕВОД'),\n"
    "  subtitle:T(")
# ---------------------------------------------------------------- 2. title
old_title = re.search(r"title:T\('THE CASTLE OF IF'[^)]*\)", js).group(0)
js = js.replace(old_title, "title:T(" + ",".join(["'BLOCULA'"]*12) + ")", 1)

# ---------------------------------------------------------------- 3. hotspots
# [x%, y%] of the 16:9 frame – the story object the marker sits on – then the
# panel placement: side (left|right|center), vertical (top|center|bottom).
# Chosen from the contact sheets, per scene, so the panel opens over the
# emptiest part of the picture and never across the subject.
HOT = {
 'cover':            (84, 24, 10, 26, 'left',  'center'),          # Dracula on the stairs
 'rules':            (60, 74, 20, 18, 'left',  'center', 58),      # the open journal
 'train':            (62, 55, 10, 13, 'left',  'center'),          # the letter
 'inn':              (27, 48,  6, 10, 'right', 'center'),          # the crucifix
 'coach':            (72, 28, 10, 18, 'left',  'top', 36),         # the hooded driver
 'blue_fire':        (63, 68, 20, 26, 'left',  'top'),             # the blue fire
 'choice1':          (12, 11,  8, 13, 'left',  'top'),             # the moon
 'blue_treasure':    (80, 76, 15, 16, 'left',  'top', 34),         # the iron chest
 'blue_cross':       (30, 38,  7, 11, 'right', 'center'),          # the crucifix
 'wolves':           (85, 24, 12, 20, 'left',  'center'),          # the coachman's raised hand
 'coach_rescue':     (63, 52, 11, 30, 'left',  'top', 32),         # the coachman, no footprints
 'castle_gate':      (72, 58,  7, 15, 'left',  'top', 38),         # Dracula's candle
 'dinner':           (76, 44, 10, 24, 'left',  'center'),          # the host who does not eat
 'mirror':           (45, 30, 10, 15, 'left',  'center', 32),      # the mirror
 'locked_room':      (40, 75,  8, 12, 'right', 'center'),          # the keys
 'choice2':          (80, 22,  9, 15, 'left',  'top'),             # the shadow in the tower
 'forged_letters':   (43, 72, 24, 15, 'left',  'top'),             # the letters
 'stolen_key':       (46, 44,  7, 11, 'right', 'bottom'),          # the key
 'wall_crawl':       (77, 56, 14, 56, 'left',  'top', 38, 14),     # Dracula on the wall
 'vampire_brides':   (40, 27, 10, 17, 'right', 'top'),             # Dracula holding them back
 'shipping_plan':    (46, 72, 22, 15, 'left',  'center'),          # the shipping ledger
 'earth_boxes':      (72, 42,  9, 11, 'left',  'center'),          # Dracula's eyes in the box
 'stolen_clothes':   (86, 52,  7, 18, 'left',  'center'),          # the blood-smeared cuff
 'last_chance':      (17, 50, 11, 28, 'right', 'center'),          # the window
 'escape_plan':      (66, 55,  6, 34, 'left',  'bottom'),          # the sheet-rope
 'choice3':          (12, 45, 15, 32, 'center','top'),             # the crypt archway
 'crypt_tomb':       (70, 57, 24, 22, 'left',  'top'),             # the stone coffin
 'stake_decision':   (75, 63, 12, 13, 'left',  'center'),          # Dracula's face
 'courtyard_carts':  (62, 62, 20, 20, 'right', 'top'),             # the wagons
 'carriage_sabotage':(48, 62, 15, 22, 'left',  'top', 32),         # the wheel
 'final_escape':     (87, 14,  9, 13, 'left',  'center'),          # Dracula at the window
 'success':          (55, 58, 24, 28, 'right', 'top'),             # the monks
 'failure':          (56, 70, 12, 32, 'left',  'top'),             # Dracula at the gate
 'epilogue':         (75, 55, 32, 32, 'left',  'center'),          # the Demeter
}
hot_js = "const HOT=" + json.dumps({k: list(v) for k, v in HOT.items()}, ensure_ascii=False) + ";\n"
js = js.replace("let state={scene:'cover'", hot_js + "let state={scene:'cover'", 1)
js = js.replace("let state={scene:'cover',score:0,nerve:5,evidence:0,lang:'off',answered:false,",
                "let state={scene:'cover',score:0,nerve:5,evidence:0,lang:'off',open:false,answered:false,", 1)
js = js.replace("function restart(){state={scene:'cover',score:0,nerve:5,evidence:0,lang:state.lang,answered:false,",
                "function restart(){state={scene:'cover',score:0,nerve:5,evidence:0,lang:state.lang,open:false,answered:false,", 1)

# every scene id must have a hotspot
scene_ids = re.findall(r"^(\w+):\{img:", js, re.M)
missing = [x for x in scene_ids if x not in HOT]
assert not missing, missing

# ---------------------------------------------------------------- 4. render
old_render_head = "function render(){const s=scenes[state.scene];state.answered=false;frame.className=`frame ${s.pos}`;sceneImage.src=IMAGES[s.img];sceneImage.alt=s.title.en;let html=head(s,s.kind==='intro');"
assert old_render_head in js
new_render_head = ("function render(){const s=scenes[state.scene];state.answered=false;const h=HOT[state.scene];"
  "frame.className=`frame ${h[4]} v-${h[5]}${state.lang==='ar'?' rtl':''}`;sceneImage.src=IMAGES[s.img];sceneImage.alt=s.title.en;"
  "placeHot(h);const tr=state.lang!=='off';frame.classList.toggle('tr-on',tr);content.style.width=((h[6]||42)+(tr?10:0))+'%';content.style.marginLeft=h[4]==='left'&&h[7]?h[7]+'%':'';content.style.marginRight=h[4]==='right'&&h[7]?h[7]+'%':'';"
  "let html=`<button class=\"hide-btn\" onclick=\"closePanel()\" title=\"Esc\">✕ ${escapeHTML(state.lang==='off'?LABELS.hide.en:LABELS.hide[state.lang])}</button>`+head(s,s.kind==='intro');")
js = js.replace(old_render_head, new_render_head, 1)

# after the html is assembled: open the cover automatically, everything else closed
old_render_tail = "content.innerHTML=html;updateHUD();"
assert old_render_tail in js
js = js.replace(old_render_tail,
  "content.innerHTML=html;updateHUD();setOpen(s.kind==='intro');", 1)

# cover title: pre-line small, BLOCULA big
old_head = "function head(s,cover=false){return `${line(s.k,'kicker')}<h1 class=\"title ${cover?'cover-title':''}\">${label(s.title)}</h1>${line(s.story,'story')}`}"
assert old_head in js
new_head = ("function head(s,cover=false){const t=cover?`<span class=\"pre\">GRAMMAR STOKER’S</span><span class=\"big\">BLOCULA</span>`:label(s.title);"
  "return `${line(s.k,'kicker')}<h1 class=\"title ${cover?'cover-title':''}\">${t}</h1>${line(s.story,'story')}`}")
js = js.replace(old_head, new_head, 1)

# panel open / close machinery
panel_js = r"""
const hot=document.getElementById('hot'), hotLabel=document.getElementById('hotLabel'), zone=document.getElementById('zone');
function ui(key){return state.lang==='off'?LABELS[key].en:LABELS[key][state.lang]}
// HOT coordinates are % of the 16:9 frame at desktop; the picture is 3:2 and object-fit:cover, so convert to image space and back for the actual frame (a phone shows a narrow central slice)
function placeHot(h){const W=frame.clientWidth,H=frame.clientHeight,sc=Math.max(W/1536,H/1024),dw=1536*sc,dh=1024*sc,ox=(W-dw)/2,oy=(H-dh)/2;const ix=h[0]/100,iy=0.078+h[1]/100*0.844,iw=h[2]/100,ih=h[3]/100*0.844;hot.style.left=(ox+ix*dw)+'px';hot.style.top=(oy+iy*dh)+'px';hot.style.width=(iw*dw)+'px';hot.style.height=(ih*dh)+'px';const cy=oy+iy*dh,ch=ih*dh;hot.classList.toggle('above',cy+ch/2>H*0.84);hotLabel.textContent=ui('read');
  document.getElementById('fsLabel').textContent=ui('fullscreen');document.getElementById('langWord').textContent=ui('translate');document.getElementById('langCur').textContent=state.lang==='off'?'OFF':LANG_NAMES[state.lang];
  document.querySelectorAll('.lang-item').forEach(b=>b.classList.toggle('active',b.dataset.lang===state.lang))}
function setOpen(on){state.open=!!on;if(on){const hr=hot.getBoundingClientRect(),zr=zone.getBoundingClientRect();const cl=zr.left+content.offsetLeft,ct=zr.top+content.offsetTop;const ox=hr.left+hr.width/2-cl,oy=hr.top+hr.height/2-ct;content.style.transformOrigin=`${ox}px ${oy}px`}frame.classList.toggle('open',state.open)}
function openPanel(){if(!state.open)setOpen(true)}
function closePanel(){if(state.open)setOpen(false)}
hot.addEventListener('click',e=>{e.stopPropagation();openPanel()});
sceneImage.addEventListener('click',()=>{closeMenu();closePanel()});
window.addEventListener('resize',()=>{if(HOT[state.scene])placeHot(HOT[state.scene])});
const langMenu=document.getElementById('langMenu'), langBtn=document.getElementById('langBtn');
function closeMenu(){langMenu.hidden=true;langBtn.setAttribute('aria-expanded','false')}
function toggleMenu(){langMenu.hidden=!langMenu.hidden;langBtn.setAttribute('aria-expanded',String(!langMenu.hidden))}
"""
js = js.replace("function go(id){", panel_js + "function go(id){", 1)

# language dropdown: generated from LANGS; L cycles through all of them
js = js.replace("document.querySelectorAll('.lang-btn').forEach(b=>b.addEventListener('click',()=>{state.lang=b.dataset.lang;render()}));",
  "(function(){['off',...LANGS].forEach(l=>{const b=document.createElement('button');b.className='lang-item';b.dataset.lang=l;b.innerHTML=l==='off'?'<b>OFF</b><span>English only</span>':`<b>${l.toUpperCase()}</b><span>${LANG_NAMES[l]}</span>`;b.addEventListener('click',()=>{state.lang=l;closeMenu();setLang()});langMenu.appendChild(b)});"
  "langBtn.addEventListener('click',e=>{e.stopPropagation();toggleMenu()});document.addEventListener('click',e=>{if(!langMenu.hidden&&!langMenu.contains(e.target))closeMenu()})})();\n"
  "function setLang(){const wasOpen=state.open;render();if(wasOpen)setOpen(true)}", 1)

old_key = "document.addEventListener('keydown',e=>{if(e.key.toLowerCase()==='l'){state.lang=state.lang==='off'?'es':state.lang==='es'?'de':'off';render();return}"
assert old_key in js
new_key = ("document.addEventListener('keydown',e=>{if(e.key.toLowerCase()==='l'){const all=['off',...LANGS];state.lang=all[(all.indexOf(state.lang)+1)%all.length];setLang();return}"
  "if(e.key==='Escape'){if(!langMenu.hidden){closeMenu();return}closePanel();return}"
  "if(e.key==='Enter'&&!state.open){openPanel();return}"
  "if(['1','2','3'].includes(e.key)&&!state.open){openPanel();return}")
js = js.replace(old_key, new_key, 1)

# ---------------------------------------------------------------- 5. markup
old_markup = """    <img id="sceneImage" class="scene-img" alt="">
    <div class="shade"></div>"""
assert old_markup in page
new_markup = """    <img id="sceneImage" class="scene-img" alt="">
    <button id="hot" class="hot" aria-label="Show the text"><i></i><span id="hotLabel" class="hot-label">CLICK TO READ</span></button>"""
page = page.replace(old_markup, new_markup, 1)

old_content = '    <article id="content" class="content"></article>'
assert old_content in page
page = page.replace(old_content, '    <div id="zone" class="zone"><article id="content" class="content"></article></div>', 1)

old_langs = """        <div class="langs" aria-label="Translation language">
          <button class="lang-btn active" data-lang="off">OFF</button>
          <button class="lang-btn" data-lang="es">ES</button>
          <button class="lang-btn" data-lang="de">DE</button>
        </div>
        <button id="fullscreen" class="utility" title="Fullscreen">⛶</button>"""
assert old_langs in page
page = page.replace(old_langs, """        <div class="langs">
          <button id="langBtn" class="lang-btn" aria-haspopup="true" aria-expanded="false">🌐 <span id="langWord">TRANSLATE</span> · <b id="langCur">OFF</b> ▾</button>
          <div id="langMenu" class="lang-menu" hidden></div>
        </div>
        <button id="fullscreen" class="utility fs" title="F">⛶ <span id="fsLabel">FULLSCREEN</span></button>""", 1)

page = page.replace('<div class="corner-help">1–3 choose · ENTER continue · L language · F fullscreen</div>',
                    '<div class="corner-help">click the glowing object or ENTER to read · ESC hide · 1–3 choose · L language · F fullscreen</div>', 1)

# ---------------------------------------------------------------- 6. CSS
page = re.sub(r"\.shade\{position:absolute;inset:0;pointer-events:none\}.*?\n\.frame\.right \.shade\{.*?\n\.frame\.center \.shade\{.*?\n", "", page, count=1)
assert '.shade' not in page

# the content panel: replace the fixed top/bottom stretch with a zone + a fitted panel
css_old_content = re.search(r"\.content\{position:absolute;z-index:4;.*?\n", page).group(0)
css_old_pos = re.search(r"\.left \.content\{left:2\.2%;text-align:left\}.*?\n", page).group(0)
new_content_css = """.zone{position:absolute;z-index:4;top:8%;bottom:3.5%;left:2.2%;right:2.2%;display:flex;pointer-events:none}
.content{pointer-events:auto;display:flex;flex-direction:column;gap:.78cqw;width:42%;max-height:100%;overflow:auto;scrollbar-width:thin;padding:1.15cqw 1.3cqw;background:rgba(7,3,8,.86);border:1px solid rgba(245,234,215,.2);box-shadow:0 1.4cqw 4cqw rgba(0,0,0,.55);backdrop-filter:blur(6px);transition:transform .38s cubic-bezier(.2,.9,.3,1.15),opacity .22s ease;transform-origin:50% 50%}
.frame:not(.open) .content{opacity:0;transform:scale(.12);pointer-events:none;transition:transform .26s ease-in,opacity .18s ease-in}
.left .zone{justify-content:flex-start}.left .content{text-align:left}.right .zone{justify-content:flex-end}.right .content{text-align:right}.center .zone{justify-content:center}.center .content{width:60%;text-align:center}
.v-top .zone{align-items:flex-start}.v-center .zone{align-items:center}.v-bottom .zone{align-items:flex-end}
.hide-btn{align-self:flex-end;order:-1;margin:-.4cqw -.5cqw -.2cqw 0;border:0;background:none;color:#e5d3c6;font-size:.82cqw;letter-spacing:.08em;cursor:pointer;padding:.25cqw .4cqw}.hide-btn:hover{color:#fff}.left .hide-btn,.center .hide-btn{align-self:flex-end}.right .hide-btn{align-self:flex-start}
.hot{position:absolute;z-index:6;left:50%;top:50%;width:10%;height:14%;transform:translate(-50%,-50%);border:0;background:none;padding:0;cursor:pointer;transition:opacity .25s;min-width:3.6cqw;min-height:3.6cqw}
.hot i{position:absolute;inset:-.4cqw;border-radius:38%;background:linear-gradient(115deg,transparent 28%,rgba(255,240,190,.28) 42%,rgba(255,250,225,.62) 50%,rgba(255,240,190,.28) 58%,transparent 72%);background-size:260% 260%;mix-blend-mode:screen;box-shadow:0 0 0 .14cqw rgba(240,200,120,.9),0 0 1.4cqw .25cqw rgba(240,200,120,.55),inset 0 0 1.4cqw rgba(255,235,170,.35);animation:shimmer 2.2s linear infinite,pulse 1.8s ease-in-out infinite}
.hot::before{content:"";position:absolute;inset:-.4cqw;border-radius:38%;border:.16cqw solid rgba(255,240,190,.9);opacity:0;animation:ring 1.8s ease-out infinite}
.hot:hover i{animation-duration:1s,1.8s;box-shadow:0 0 0 .18cqw #fff3c4,0 0 2.2cqw .5cqw rgba(240,200,120,.85),inset 0 0 1.8cqw rgba(255,235,170,.5)}
.hot-label{position:absolute;left:50%;top:calc(100% + .7cqw);transform:translateX(-50%);white-space:nowrap;color:var(--gold);font-family:'Pixelify Sans','Courier New',monospace;font-size:1.15cqw;letter-spacing:.04em;text-shadow:-.09em -.09em 0 var(--deep),0 -.09em 0 var(--deep),.09em -.09em 0 var(--deep),-.09em 0 0 var(--deep),.09em 0 0 var(--deep),-.09em .09em 0 var(--deep),0 .09em 0 var(--deep),.09em .09em 0 var(--deep),0 .14em .5em rgba(5,3,7,.9);pointer-events:none}
.hot.above .hot-label{top:auto;bottom:calc(100% + .7cqw)}
.langs{position:relative}.lang-btn{display:flex;align-items:center;gap:.3cqw;white-space:nowrap}.lang-btn b{color:var(--gold)}
.lang-menu[hidden]{display:none}.lang-menu{position:absolute;right:0;top:calc(100% + .4cqw);z-index:20;display:grid;grid-template-columns:1fr 1fr;gap:.25cqw;min-width:22cqw;padding:.45cqw;background:rgba(8,4,9,.96);border:1px solid rgba(245,234,215,.4);box-shadow:0 1cqw 3cqw rgba(0,0,0,.7)}
.lang-item{display:grid;grid-template-columns:2.6cqw 1fr;align-items:center;gap:.4cqw;border:1px solid transparent;background:none;color:var(--bone);padding:.4cqw .5cqw;text-align:left;cursor:pointer;font-size:1cqw}.lang-item b{color:var(--gold);font-size:.9cqw}.lang-item span{font-size:.95cqw}.lang-item:hover{border-color:rgba(245,234,215,.5);background:rgba(60,9,21,.9)}.lang-item.active{background:var(--blood);color:#fff}.lang-item.active b{color:#fff}
.utility.fs{display:flex;align-items:center;gap:.35cqw;color:#1a0810;background:linear-gradient(180deg,#f7d98c,#d9a94a);border:1px solid #fff0c0;font-weight:700;letter-spacing:.06em;box-shadow:0 0 1cqw rgba(240,200,120,.55);animation:fsglow 2.4s ease-in-out infinite}.utility.fs:hover{filter:brightness(1.1)}
.translation{unicode-bidi:plaintext}.rtl .translation{direction:rtl;text-align:right}.utility{pointer-events:auto}
.frame.open .hot{opacity:0;pointer-events:none}
.tr-on .content{gap:.5cqw;padding:.9cqw 1.1cqw}.tr-on .translation{font-size:.86cqw;line-height:1.22;margin-top:.12cqw}.tr-on .option{padding:.42cqw .6cqw}.tr-on .options{gap:.36cqw}.tr-on .clue{padding:.45cqw .7cqw}.tr-on .feedback{padding:.5cqw .7cqw}.tr-on .story{font-size:1.25cqw;line-height:1.28}.rules-intro{grid-template-columns:1fr 1fr}.rule-card:last-child{grid-column:1/-1}.tr-on .rules-intro{gap:.32cqw}.tr-on .rule-card{padding:.36cqw .55cqw;font-size:.88cqw}.tr-on .rule-card .translation{font-size:.7cqw}.tr-on .rule-note{font-size:.88cqw}.tr-on .title{font-size:3cqw}
@keyframes shimmer{0%{background-position:110% 110%}100%{background-position:-10% -10%}}
@keyframes pulse{0%,100%{opacity:.8}50%{opacity:1}}
@keyframes ring{0%{transform:scale(1);opacity:.9}100%{transform:scale(1.5);opacity:0}}
@keyframes fsglow{0%,100%{box-shadow:0 0 .6cqw rgba(240,200,120,.4)}50%{box-shadow:0 0 1.6cqw rgba(240,200,120,.9)}}
"""
page = page.replace(css_old_content, new_content_css, 1)
page = page.replace(css_old_pos, "", 1)

# cover title
page = page.replace(".cover-title{font-size:5.3cqw}",
  ".cover-title{font-size:3.2cqw;line-height:1}.cover-title .pre{display:block;font-size:1em;letter-spacing:.04em;color:var(--bone);margin-bottom:.25em}.cover-title .big{display:block;font-size:2.5em;line-height:.92;color:var(--gold)}", 1)

# aspect / mobile rules
page = page.replace("@media(max-aspect-ratio:4/3){.content{width:58%}.center .content{width:82%}",
                    "@media(max-aspect-ratio:4/3){.content{width:58%}.center .content{width:82%}.hot-label{font-size:1.6cqw}.lang-menu{min-width:30cqw}.lang-item{font-size:1.3cqw}.lang-item b{font-size:1.2cqw}", 1)
old_mobile = ".content,.center .content{top:58px;bottom:14px;left:3%;right:3%;transform:none;width:94%;max-height:none;text-align:left;justify-content:flex-end;background:linear-gradient(180deg,transparent 0%,rgba(5,3,7,.91) 32%);border:0;padding:18px}"
assert old_mobile in page
page = page.replace(old_mobile,
  ".zone{top:58px;bottom:10px;left:3%;right:3%;align-items:flex-end!important;justify-content:center!important}.content,.center .content,.tr-on .content{width:100%!important;margin:0!important;max-height:100%;text-align:left;padding:14px;gap:8px}"
  ".hot{min-width:44px;min-height:44px}.hot i,.hot::before{inset:-4px}.hot i{box-shadow:0 0 0 2px rgba(240,200,120,.9),0 0 14px 3px rgba(240,200,120,.55)}.hot::before{border-width:2px}.hot-label{font-size:12px}.lang-menu{min-width:220px;padding:6px;gap:3px;grid-template-columns:1fr}.lang-item{font-size:12px;padding:5px 7px;grid-template-columns:30px 1fr}.lang-item b,.lang-item span{font-size:12px}.lang-btn{gap:4px}.hide-btn{font-size:11px}.title.cover-title{font-size:19px}.clue,.rule-card,.rule-note,.route,.rules-intro{font-size:13px;padding:8px}.rule-card b,.route b{font-size:13px}.final-score{font-size:18px}.small{font-size:11px}.continue,.start,.restart{font-size:13px;padding:10px 14px}.option{grid-template-columns:22px 1fr}.option .key{width:20px;height:20px}.option .translation,.route .translation,.rule-card .translation{font-size:11px}.rules-intro{grid-template-columns:1fr}.rule-card:last-child{grid-column:auto}", 1)
page = page.replace(".title,.cover-title{font-size:36px}", ".title{font-size:36px}", 1)

# ---------------------------------------------------------------- 7. SEO + title
NEW = "Grammar Stoker’s Blocula — Conditionals &amp; Passive Voice RPG (B2)"
page = page.replace("Dracula: The Castle of If — Conditionals &amp; Passive Voice RPG (B2)", NEW)
page = page.replace('"name":"Dracula: The Castle of If — Conditionals & Passive Voice RPG (B2)"', '"name":"Grammar Stoker’s Blocula — Conditionals & Passive Voice RPG (B2)"')
page = page.replace("An interactive B2 English lesson from Forbes English: Dracula: The Castle of If — Conditionals & Passive Voice RPG (B2).",
                    "An interactive B2 English lesson from Forbes English: Grammar Stoker’s Blocula — Conditionals & Passive Voice RPG (B2).")
assert 'Castle of If' not in page, [m.start() for m in re.finditer('Castle of If', page)]

out = page + js
open(OUT, 'w', encoding='utf-8').write(out)
print('wrote', OUT, len(out), 'bytes')
