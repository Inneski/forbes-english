#!/usr/bin/env python3
"""The Block Camp RPG engine — `assemble(spec, out)` writes one self-contained
page in the house standard set by Innes's Blocula rebuild of 2026-09-04:

  * every scene is a full-bleed 3:2 picture with ONE glowing object on it;
    clicking the object (or Enter) pops the text panel out of that spot, and
    ✕ / Esc / a click on the picture folds it away again;
  * the panel is dark glass, the type is Monocraft (the Block Camp face) at a
    size that reads from the back of a classroom — see the type scale in CSS;
  * HUD across the top (points · tiles · chances), a translate menu built
    from whatever gloss languages the spec actually ships, and a fullscreen
    button; keys 1–3 answer, L cycles the language, F toggles fullscreen.

Nothing here is lesson-specific. A builder (`build_<name>.py` one level up)
supplies a SPEC dict and calls `assemble()`; read README.md in this
directory for the spec shape, the hotspot convention and the full pipeline.

Every string that reaches the learner is a dict keyed by language — `en`
always, then one key per gloss language — so a page shows English with the
gloss beneath it, never a translation instead of the English. Options are
glossed too (Innes's Blocula does the same); the English stays on top.
"""
import base64, html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
FONT_DIR = os.path.join(HERE, 'fonts')

LANG_NAMES = {'es': 'Español', 'de': 'Deutsch', 'fr': 'Français', 'it': 'Italiano',
              'pt': 'Português', 'pl': 'Polski', 'zh': '中文', 'ja': '日本語',
              'tr': 'Türkçe', 'ar': 'العربية', 'ru': 'Русский'}

# Chrome strings every RPG needs. A spec may override any key (and must add
# every gloss language it ships — assemble() refuses a half-translated set).
LABELS = {
    'read':       {'en': 'CLICK TO READ', 'es': 'PULSA PARA LEER', 'de': 'KLICKEN ZUM LESEN'},
    'hide':       {'en': 'HIDE', 'es': 'OCULTAR', 'de': 'AUSBLENDEN'},
    'continue':   {'en': 'CONTINUE', 'es': 'CONTINUAR', 'de': 'WEITER'},
    'begin':      {'en': 'BEGIN', 'es': 'EMPEZAR', 'de': 'LOSLEGEN'},
    'restart':    {'en': 'PLAY AGAIN', 'es': 'JUGAR OTRA VEZ', 'de': 'NOCH EINMAL SPIELEN'},
    'fullscreen': {'en': 'FULLSCREEN', 'es': 'PANTALLA COMPLETA', 'de': 'VOLLBILD'},
    'translate':  {'en': 'TRANSLATE', 'es': 'TRADUCIR', 'de': 'ÜBERSETZEN'},
    'off':        {'en': 'English only', 'es': 'Solo inglés', 'de': 'Nur Englisch'},
    'visual':     {'en': 'VISUAL CLUE', 'es': 'PISTA VISUAL', 'de': 'BILDHINWEIS'},
    'points':     {'en': 'POINTS', 'es': 'PUNTOS', 'de': 'PUNKTE'},
    'tiles':      {'en': 'TILES', 'es': 'BALDOSAS', 'de': 'PLATTEN'},
    'chances':    {'en': 'CHANCES', 'es': 'OPORTUNIDADES', 'de': 'CHANCEN'},
    'correct':    {'en': 'CORRECT · +{p} POINTS', 'es': 'CORRECTO · +{p} PUNTOS', 'de': 'RICHTIG · +{p} PUNKTE'},
    'relic':      {'en': 'TILE RECOVERED · +{p} POINTS', 'es': 'BALDOSA RECUPERADA · +{p} PUNTOS', 'de': 'PLATTE GEBORGEN · +{p} PUNKTE'},
    'wrong':      {'en': 'NO POINTS · −1 CHANCE', 'es': 'SIN PUNTOS · −1 OPORTUNIDAD', 'de': 'KEINE PUNKTE · −1 CHANCE'},
    'answerWas':  {'en': 'Correct answer:', 'es': 'Respuesta correcta:', 'de': 'Richtige Antwort:'},
    'finalScore': {'en': 'FINAL SCORE', 'es': 'PUNTUACIÓN FINAL', 'de': 'ENDPUNKTZAHL'},
    'route':      {'en': 'ROUTE', 'es': 'RUTA', 'de': 'ROUTE'},
    'progress':   {'en': 'SPELLS', 'es': 'HECHIZOS', 'de': 'ZAUBER'},
    'soundOn':    {'en': 'SOUND ON', 'es': 'SONIDO SÍ', 'de': 'TON AN'},
    'soundOff':   {'en': 'SOUND OFF', 'es': 'SONIDO NO', 'de': 'TON AUS'},
    'repaired':   {'en': 'SPELL REPAIRED', 'es': 'HECHIZO REPARADO', 'de': 'ZAUBER REPARIERT'},
    'tryAgain':   {'en': 'NOT YET · TRY ANOTHER', 'es': 'TODAVÍA NO · PRUEBA OTRA', 'de': 'NOCH NICHT · VERSUCH ES ANDERS'},
    'firstTry':   {'en': 'first try', 'es': 'a la primera', 'de': 'beim ersten Versuch'},
    'review':     {'en': 'REVIEW THE REPAIRED SPELLS', 'es': 'REPASA LOS HECHIZOS REPARADOS', 'de': 'DIE REPARIERTEN ZAUBER ANSEHEN'},
    'perfect':    {'en': 'Perfect first-try grammar. Every spell held.', 'es': 'Gramática perfecta a la primera. Todos los hechizos aguantaron.', 'de': 'Perfekte Grammatik beim ersten Versuch. Jeder Zauber hat gehalten.'},
    'help':       {'en': 'click the glowing object or ENTER to read · ESC hide · 1–3 choose · L language · S sound · F fullscreen',
                   'es': 'pulsa el objeto que brilla o ENTER para leer · ESC ocultar · 1–3 elegir · L idioma · S sonido · F pantalla completa',
                   'de': 'klicke das leuchtende Objekt oder ENTER zum Lesen · ESC ausblenden · 1–3 wählen · L Sprache · S Ton · F Vollbild'},
}

TEXT_KEYS = ('k', 'title', 'story', 'clue', 'prompt', 'fb', 'note', 'small', 'start')


def font_css():
    out = []
    for weight, name in ((400, 'Regular'), (700, 'Bold')):
        p = os.path.join(FONT_DIR, 'Monocraft-%s.woff2' % name)
        b64 = base64.b64encode(open(p, 'rb').read()).decode('ascii')
        out.append("@font-face{font-family:'Monocraft';font-style:normal;font-weight:%d;"
                   "font-display:block;src:url(data:font/woff2;base64,%s) format('woff2')}"
                   % (weight, b64))
    return '\n'.join(out)


CSS = r"""
:root{--accent:{{ACCENT}};--accent-ink:{{ACCENT_INK}};--deep:{{DEEP}};--panel:{{PANEL}};--bone:#fff6d9;--muted:#d9ccb0;--soft:#efe2c0;--good:#77efb4;--bad:#ff6f82;--shadow:rgba(0,0,0,.55)}
*{box-sizing:border-box}
html,body{width:100%;height:100%;margin:0;overflow:hidden;background:#0a0703;color:var(--bone);font-family:"Courier New",Courier,monospace}
/* Monocraft is the display face — titles, kickers, HUD, buttons, labels. The
   reading text (story, clue, prompt, options, feedback, glosses) stays in
   Courier New, as Blocula has it: a pixel face at paragraph length is hard
   work, and Innes asked for the split on 2026-09-06. */
.title,.kicker,.badge,.lang-btn,.utility,.lang-item b,.hot-label,.hide-btn,.option .key,.continue,.start,.restart,.rules-chips span,.rule-card b,.route b,.final-score,.feedback strong,.corner-help,.option .half small,.clue b{font-family:'Monocraft',"Courier New",Courier,monospace}
button{font:inherit}
.game{position:fixed;inset:0;background:#0a0703}
.frame{position:absolute;inset:0;overflow:hidden;container-type:inline-size}
.scene-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center;filter:saturate(1.04) contrast(1.03)}
/* ── HUD ── */
.hud{position:absolute;z-index:5;top:1.3cqw;left:1.5cqw;right:1.5cqw;display:flex;align-items:center;justify-content:space-between;gap:1cqw;pointer-events:none}
.hud-group{display:flex;gap:.55cqw;align-items:center;flex-wrap:wrap}
.badge{background:var(--panel);border:1px solid rgba(255,246,217,.34);box-shadow:0 0 1.3cqw var(--shadow);padding:.5cqw .8cqw;font-size:1.15cqw;letter-spacing:.04em;white-space:nowrap}
.badge b{color:var(--accent);font-weight:700}
.langs{display:flex;gap:.35cqw;pointer-events:auto;position:relative}
.lang-btn,.utility{border:1px solid rgba(255,246,217,.35);color:var(--bone);background:var(--panel);padding:.5cqw .75cqw;cursor:pointer;font-size:1.1cqw;pointer-events:auto}
.lang-btn{display:flex;align-items:center;gap:.3cqw;white-space:nowrap}.lang-btn b{color:var(--accent)}
.utility:hover,.lang-btn:hover{border-color:var(--bone)}
.utility.fs{display:flex;align-items:center;gap:.35cqw;color:var(--accent-ink);background:linear-gradient(180deg,#fff0b8,var(--accent));border:1px solid #fff8dc;font-weight:700;letter-spacing:.06em;animation:fsglow 2.4s ease-in-out infinite}
.utility.fs:hover{filter:brightness(1.08)}
.lang-menu[hidden]{display:none}
.lang-menu{position:absolute;right:0;top:calc(100% + .4cqw);z-index:20;display:grid;grid-template-columns:1fr;gap:.25cqw;min-width:18cqw;padding:.45cqw;background:rgba(14,9,2,.97);border:1px solid rgba(255,246,217,.4);box-shadow:0 1cqw 3cqw rgba(0,0,0,.7)}
.lang-item{display:grid;grid-template-columns:3cqw 1fr;align-items:center;gap:.4cqw;border:1px solid transparent;background:none;color:var(--bone);padding:.45cqw .55cqw;text-align:left;cursor:pointer;font-size:1.05cqw}
.lang-item b{color:var(--accent);font-size:.95cqw}.lang-item:hover{border-color:rgba(255,246,217,.5);background:rgba(60,40,5,.9)}
.lang-item.active{background:var(--accent);color:var(--accent-ink)}.lang-item.active b{color:var(--accent-ink)}
/* ── the panel ── */
.zone{position:absolute;z-index:4;top:8%;bottom:3.5%;left:2.2%;right:2.2%;display:flex;pointer-events:none}
.content{pointer-events:auto;display:flex;flex-direction:column;gap:.8cqw;width:46%;max-height:100%;overflow:auto;scrollbar-width:thin;padding:1.2cqw 1.4cqw;background:var(--panel);border:1px solid rgba(255,246,217,.22);box-shadow:0 1.4cqw 4cqw var(--shadow);backdrop-filter:blur(6px);transition:transform .38s cubic-bezier(.2,.9,.3,1.15),opacity .22s ease;transform-origin:50% 50%}
.frame:not(.open) .content{opacity:0;transform:scale(.12);pointer-events:none;transition:transform .26s ease-in,opacity .18s ease-in}
.left .zone{justify-content:flex-start}.left .content{text-align:left}
.right .zone{justify-content:flex-end}.right .content{text-align:right}
.center .zone{justify-content:center}.center .content{width:64%;text-align:center}
.v-top .zone{align-items:flex-start}.v-center .zone{align-items:center}.v-bottom .zone{align-items:flex-end}
.hide-btn{align-self:flex-end;order:-1;margin:-.4cqw -.5cqw -.3cqw 0;border:0;background:none;color:var(--soft);font-size:.95cqw;letter-spacing:.08em;cursor:pointer;padding:.25cqw .4cqw}
.hide-btn:hover{color:#fff}.right .hide-btn{align-self:flex-start}
/* ── the glowing object ── */
.hot{position:absolute;z-index:6;left:50%;top:50%;width:10%;height:14%;transform:translate(-50%,-50%);border:0;background:none;padding:0;cursor:pointer;transition:opacity .25s;min-width:3.6cqw;min-height:3.6cqw}
.hot i{position:absolute;inset:-.4cqw;border-radius:38%;background:linear-gradient(115deg,transparent 28%,rgba(255,250,220,.3) 42%,rgba(255,255,240,.7) 50%,rgba(255,250,220,.3) 58%,transparent 72%);background-size:260% 260%;mix-blend-mode:screen;box-shadow:0 0 0 .16cqw #fff,0 0 0 .36cqw rgba(70,45,0,.55),0 0 1.6cqw .4cqw rgba(255,240,170,.85),inset 0 0 1.4cqw rgba(255,255,220,.45);animation:shimmer 2.2s linear infinite,pulse 1.8s ease-in-out infinite}
.hot::before{content:"";position:absolute;inset:-.4cqw;border-radius:38%;border:.18cqw solid #fff;opacity:0;animation:ring 1.8s ease-out infinite}
.hot:hover i{animation-duration:1s,1.8s;box-shadow:0 0 0 .2cqw #fff,0 0 0 .4cqw rgba(70,45,0,.6),0 0 2.4cqw .6cqw rgba(255,240,170,1),inset 0 0 1.8cqw rgba(255,255,220,.6)}
.hot-label{position:absolute;left:50%;top:calc(100% + .8cqw);transform:translateX(-50%);white-space:nowrap;color:#fff;font-weight:700;font-size:1.3cqw;letter-spacing:.04em;text-shadow:-.09em -.09em 0 var(--deep),0 -.09em 0 var(--deep),.09em -.09em 0 var(--deep),-.09em 0 0 var(--deep),.09em 0 0 var(--deep),-.09em .09em 0 var(--deep),0 .09em 0 var(--deep),.09em .09em 0 var(--deep),0 .14em .5em rgba(0,0,0,.9);pointer-events:none}
.hot.above .hot-label{top:auto;bottom:calc(100% + .8cqw)}
.frame.open .hot{opacity:0;pointer-events:none}
@keyframes shimmer{0%{background-position:110% 110%}100%{background-position:-10% -10%}}
@keyframes pulse{0%,100%{opacity:.8}50%{opacity:1}}
@keyframes ring{0%{transform:scale(1);opacity:.9}100%{transform:scale(1.5);opacity:0}}
@keyframes fsglow{0%,100%{box-shadow:0 0 .6cqw rgba(255,240,170,.4)}50%{box-shadow:0 0 1.6cqw rgba(255,240,170,.9)}}
/* ── type scale: Monocraft is monospace and wide, so the scale is set by what
   fits 46% of a 16:9 frame, and it is deliberately a step up from Blocula
   (story 1.36cqw there, 1.65 here) — "text should be bigger", 2026-09-05 ── */
.kicker{color:var(--accent);font-weight:700;font-size:1.2cqw;letter-spacing:.1em;text-transform:uppercase}
.title{margin:0;color:var(--accent);font-weight:700;font-size:3cqw;line-height:1.08;letter-spacing:0;text-shadow:-.05em 0 0 var(--deep),.05em 0 0 var(--deep),0 -.05em 0 var(--deep),0 .05em 0 var(--deep),-.05em -.05em 0 var(--deep),.05em -.05em 0 var(--deep),-.05em .05em 0 var(--deep),.05em .05em 0 var(--deep),0 0 .6em rgba(0,0,0,.6)}
.story{font-size:1.65cqw;line-height:1.36}
.clue{border-left:.3cqw solid var(--accent);padding:.7cqw .9cqw;background:rgba(255,235,160,.14);font-size:1.4cqw;line-height:1.3}
.clue b{color:var(--accent)}
.right .clue{border-left:0;border-right:.3cqw solid var(--accent)}.center .clue{border-right:.3cqw solid var(--accent)}
.prompt{color:#fff;font-weight:700;font-size:1.65cqw;line-height:1.28}
.translation{display:block;color:var(--muted);font-size:1.1cqw;line-height:1.28;margin-top:.22cqw;font-weight:400;font-style:italic;unicode-bidi:plaintext}
.rtl .translation{direction:rtl;text-align:right}
.title .translation,.kicker .translation{font-family:"Courier New",Courier,monospace}.title .translation{font-size:1.25cqw;letter-spacing:0;color:var(--soft);margin-top:.4cqw;text-shadow:none}
.kicker .translation{font-size:.9cqw;letter-spacing:.05em}
.options{display:grid;gap:.55cqw;margin-top:.15cqw}
.option{display:grid;grid-template-columns:2.6cqw 1fr;align-items:center;gap:.65cqw;width:100%;border:1px solid rgba(255,246,217,.36);background:rgba(20,14,4,.8);color:var(--bone);padding:.7cqw .8cqw;text-align:left;cursor:pointer;font-size:1.4cqw;line-height:1.26;transition:.16s}
.option:hover{transform:translateY(-1px);border-color:#fff;background:rgba(70,48,8,.9)}
.option .key{display:grid;place-items:center;width:2.4cqw;height:2.4cqw;border:1px solid var(--accent);color:var(--accent);font-weight:700}
.option.correct{background:rgba(25,102,69,.9);border-color:var(--good)}.option.wrong{background:rgba(131,12,34,.93);border-color:var(--bad)}
.option:disabled{cursor:default;transform:none}.option .translation{font-size:1.05cqw}
.option.split{grid-template-columns:2.6cqw 1fr 1fr;gap:.5cqw}.option .half{display:flex;flex-direction:column;gap:.15cqw;padding:.45cqw .6cqw;border:1px solid rgba(255,246,217,.25)}
.option .half small{font-size:.8cqw;letter-spacing:.08em;opacity:.85}.option .half b{font-size:1.35cqw}
.option .half.a{background:rgba(207,52,125,.55)}.option .half.b{background:rgba(36,121,173,.55)}
.badge[hidden]{display:none}
.review{display:grid;gap:.45cqw;text-align:left}.review div{border-left:.25cqw solid var(--accent);padding:.4cqw .7cqw;background:rgba(255,235,160,.1);font-size:1.15cqw;line-height:1.3}.review b{color:var(--accent)}
.option.wrong:disabled{opacity:.7}
.right .option{text-align:right;grid-template-columns:1fr 2.6cqw}.right .option .key{order:2}.right .option.split{grid-template-columns:1fr 1fr 2.6cqw}.right .option.split .key{order:3}.option .half{text-align:left}
.feedback{display:none;padding:.8cqw .9cqw;border:1px solid rgba(255,246,217,.3);background:rgba(20,14,4,.85);font-size:1.35cqw;line-height:1.32}
.feedback.show{display:block}.feedback.good{border-color:var(--good)}.feedback.bad{border-color:var(--bad)}
.feedback strong{color:var(--accent)}.feedback .translation{font-size:1.05cqw}
.continue,.start,.restart{align-self:flex-start;border:1px solid #fff8dc;background:linear-gradient(180deg,#fff0b8,var(--accent));color:var(--accent-ink);font-weight:700;letter-spacing:.07em;padding:.8cqw 1.2cqw;cursor:pointer;font-size:1.2cqw;box-shadow:0 .5cqw 1.5cqw rgba(0,0,0,.48)}
.right .continue,.right .start,.right .restart{align-self:flex-end}.center .continue,.center .start,.center .restart{align-self:center}
.continue:hover,.start:hover,.restart:hover{filter:brightness(1.08)}
.rules-chips{display:flex;flex-wrap:wrap;gap:.5cqw}.right .rules-chips{justify-content:flex-end}.center .rules-chips{justify-content:center}
.rules-chips span{border:1px solid var(--accent);color:var(--accent);padding:.4cqw .65cqw;font-size:1cqw;font-weight:700;letter-spacing:.06em}
.route-options{display:grid;grid-template-columns:1fr 1fr;gap:.8cqw}
.route{border:1px solid rgba(255,246,217,.43);background:rgba(20,14,4,.82);color:#fff;padding:1cqw;cursor:pointer;text-align:left;min-height:7cqw;font-size:1.25cqw;line-height:1.3}
.route:hover{border-color:var(--accent);background:rgba(70,48,8,.92)}
.route b{display:block;color:var(--accent);font-size:1.3cqw;margin-bottom:.4cqw}.route .translation{font-size:1cqw}
.rules-intro{display:grid;grid-template-columns:1fr 1fr;gap:.5cqw}.rule-card:last-child{grid-column:1/-1}
.rule-card{border:1px solid rgba(255,246,217,.3);background:rgba(20,14,4,.8);padding:.55cqw .7cqw;font-size:1.08cqw;line-height:1.26;text-align:left}
.rule-card b{display:block;color:var(--accent);font-size:1.2cqw;margin-bottom:.15cqw}.rule-card .translation{font-size:.95cqw}
.rule-note{color:#fff;font-size:1.25cqw;line-height:1.3;border-left:.3cqw solid var(--accent);padding:.55cqw .75cqw;background:rgba(255,235,160,.14);text-align:left}
.cover-title{font-size:3.2cqw;line-height:1}
.cover-title .big{display:block;font-size:1.7em;line-height:.95}
.final-score{font-size:2.1cqw;color:var(--accent);font-weight:700}
.small{font-size:1cqw;color:var(--muted)}
.corner-help{position:absolute;z-index:5;right:1.5cqw;bottom:1.2cqw;color:var(--soft);font-size:.85cqw;background:rgba(14,9,2,.7);padding:.4cqw .55cqw;pointer-events:none}
/* translation on: a little tighter, a little wider */
.tr-on .content{gap:.55cqw;padding:1cqw 1.2cqw}.tr-on .option{padding:.5cqw .7cqw}.tr-on .options{gap:.4cqw}.tr-on .title{font-size:2.6cqw}
/* portrait / square-ish windows */
@media(max-aspect-ratio:4/3){.content{width:60%}.center .content{width:84%}.hot-label{font-size:1.8cqw}.lang-menu{min-width:30cqw}.lang-item{font-size:1.4cqw}.lang-item b{font-size:1.3cqw}.title{font-size:4.4cqw}.story,.prompt{font-size:2.1cqw}.option,.feedback{font-size:1.75cqw}.translation{font-size:1.35cqw}.badge{font-size:1.5cqw}.lang-btn,.utility{font-size:1.4cqw}.clue{font-size:1.7cqw}}
/* phones: the panel is a sheet across the bottom, sizes in px */
@media(max-width:700px){.hud{top:8px;left:8px;right:8px}.badge{font-size:11px;padding:5px 6px}.lang-btn,.utility{font-size:11px;padding:5px 6px}.zone{top:58px;bottom:10px;left:3%;right:3%;align-items:flex-end!important;justify-content:center!important}.content,.center .content,.tr-on .content{width:100%!important;margin:0!important;max-height:100%;text-align:left;padding:14px;gap:9px}.right .content{text-align:left}.right .clue{border-right:0;border-left:4px solid var(--accent)}.right .option{text-align:left;grid-template-columns:24px 1fr}.right .option .key{order:0}.right .continue,.right .start,.right .restart,.center .continue,.center .start,.center .restart{align-self:flex-start}.right .hide-btn{align-self:flex-end}.hot{min-width:44px;min-height:44px}.hot i,.hot::before{inset:-4px}.hot i{box-shadow:0 0 0 2px #fff,0 0 0 4px rgba(70,45,0,.55),0 0 14px 3px rgba(255,240,170,.85)}.hot::before{border-width:2px}.hot-label{font-size:13px}.lang-menu{min-width:200px;padding:6px;gap:3px}.lang-item{font-size:13px;padding:6px 8px;grid-template-columns:32px 1fr}.lang-item b{font-size:12px}.hide-btn{font-size:12px}.title,.tr-on .title{font-size:26px}.cover-title{font-size:22px}.kicker{font-size:12px}.story,.prompt{font-size:17px}.clue{font-size:15px;padding:8px 10px;border-left-width:4px}.translation,.title .translation{font-size:13px}.option,.feedback{font-size:15px;padding:9px 10px}.option{grid-template-columns:24px 1fr;gap:8px}.option .key{width:22px;height:22px}.option .translation,.route .translation,.rule-card .translation,.feedback .translation{font-size:12px}.option.split{grid-template-columns:24px 1fr 1fr;gap:6px}.option .half{padding:6px 8px}.option .half small{font-size:10px}.option .half b{font-size:14px}.review div{font-size:13px;padding:6px 8px}.route-options,.rules-intro{grid-template-columns:1fr}.rule-card:last-child{grid-column:auto}.rule-card,.rule-note,.route{font-size:14px;padding:9px}.rule-card b,.route b{font-size:14px}.rules-chips span{font-size:11px;padding:4px 7px}.final-score{font-size:19px}.small{font-size:12px}.continue,.start,.restart{font-size:14px;padding:11px 16px}.corner-help{display:none}}
"""

BODY = r"""
<main class="game" aria-live="polite">
  <section id="frame" class="frame left v-center">
    <img id="sceneImage" class="scene-img" alt="">
    <button id="hot" class="hot" aria-label="Show the text"><i></i><span id="hotLabel" class="hot-label">CLICK TO READ</span></button>
    <header class="hud">
      <div class="hud-group">
        <div class="badge"><span id="lblPoints">POINTS</span> <b id="score">0</b>/{{MAX}}</div>
        <div class="badge"><span id="lblTiles">TILES</span> <b id="tiles"></b></div>
        <div class="badge" id="chancesBadge"><span id="lblChances">CHANCES</span> <b id="chances"></b></div>
        <div class="badge" id="progressBadge" hidden><span id="lblProgress">SPELLS</span> <b id="progress"></b></div>
      </div>
      <div class="hud-group">
        <div class="langs">
          <button id="langBtn" class="lang-btn" aria-haspopup="true" aria-expanded="false">🌐 <span id="langWord">TRANSLATE</span> · <b id="langCur">OFF</b> ▾</button>
          <div id="langMenu" class="lang-menu" hidden></div>
        </div>
        <button id="sound" class="utility" title="S" aria-pressed="false">🔈 <span id="soundLabel">SOUND OFF</span></button>
        <button id="fullscreen" class="utility fs" title="F">⛶ <span id="fsLabel">FULLSCREEN</span></button>
      </div>
    </header>
    <div id="zone" class="zone"><article id="content" class="content"></article></div>
    <div id="help" class="corner-help"></div>
  </section>
</main>
"""

JS = r"""
const G = {{GAME}};
const LANGS = G.langs, RTL = ['ar'];
let state = fresh('off');
let sound=false;try{sound=localStorage.getItem('rpg-sound')==='1'}catch(_){}
/* two short tones, right and wrong — the Wonderland export's, kept */
function beep(ok){if(!sound)return;try{const c=new (window.AudioContext||window.webkitAudioContext)();const o=c.createOscillator(),g=c.createGain();o.type=ok?'square':'sawtooth';o.frequency.value=ok?620:180;g.gain.value=.03;o.connect(g);g.connect(c.destination);o.start();g.gain.exponentialRampToValueAtTime(.001,c.currentTime+.16);o.stop(c.currentTime+.18);o.onended=()=>c.close()}catch(_){}}
function setSound(on){sound=!!on;try{localStorage.setItem('rpg-sound',sound?'1':'0')}catch(_){}const b=document.getElementById('sound');b.setAttribute('aria-pressed',String(sound));b.firstChild.textContent=(sound?'🔊':'🔈')+' ';document.getElementById('soundLabel').textContent=ui(sound?'soundOn':'soundOff')}
function fresh(lang){return {scene:G.start,score:0,chances:G.chances,tiles:0,lang,open:false,route:[],results:{},attempts:{},mistakes:[],answered:0,finalCorrect:null}}
const frame=document.getElementById('frame'), content=document.getElementById('content'), sceneImage=document.getElementById('sceneImage');
const hot=document.getElementById('hot'), hotLabel=document.getElementById('hotLabel'), zone=document.getElementById('zone');
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const tx=(o,l)=>o?(l&&o[l]?o[l]:o.en):'';
function ui(key,vars){let s=tx(G.labels[key],state.lang==='off'?null:state.lang);if(vars)for(const k in vars)s=s.replace('{'+k+'}',vars[k]);return s}
function line(obj,cls=''){if(!obj)return '';const en=esc(obj.en);if(state.lang==='off'||!obj[state.lang])return `<span class="${cls}">${en}</span>`;return `<span class="${cls}">${en}<span class="translation">${esc(obj[state.lang])}</span></span>`}
function label(obj){if(!obj)return '';return state.lang==='off'||!obj[state.lang]?esc(obj.en):`${esc(obj.en)}<span class="translation">${esc(obj[state.lang])}</span>`}
/* an option is {en,…} or, for a two-blank item, {parts:[a,b], kinds:['a'|'b',…], tags:[{en,…},{en,…}]} — two coloured halves */
function optText(o){return o.parts?o.parts.join(' / '):o.en}
function optMarkup(o){if(!o.parts)return `<span>${label(o)}</span>`;return o.parts.map((p,i)=>`<span class="half ${o.kinds[i]}"><small>${label(G.tags[o.kinds[i]])}</small><b>${esc(p)}</b></span>`).join('')}
function updateHUD(){document.getElementById('score').textContent=state.score;document.getElementById('tiles').textContent='◆'.repeat(state.tiles)+'◇'.repeat(Math.max(0,G.tiles-state.tiles));document.getElementById('chances').textContent='♥'.repeat(state.chances)+'♡'.repeat(Math.max(0,G.chances-state.chances));document.getElementById('lblPoints').textContent=ui('points');document.getElementById('lblTiles').textContent=ui('tiles');document.getElementById('lblChances').textContent=ui('chances');document.getElementById('chancesBadge').hidden=!G.chances;document.getElementById('progressBadge').hidden=!G.total;if(G.total){document.getElementById('lblProgress').textContent=ui('progress');document.getElementById('progress').textContent=`${state.answered}/${G.total}`}document.getElementById('help').textContent=ui('help')}
function head(s){const t=s.kind==='intro'?`<span class="big">${label(s.title)}</span>`:label(s.title);return `${line(s.k,'kicker')}<h1 class="title ${s.kind==='intro'?'cover-title':''}">${t}</h1>${line(s.story,'story')}`}
/* HOT = [cx, cy, w, h] as % of the PICTURE (3:2). The picture is object-fit:cover in the frame, so convert picture space to frame pixels; a phone shows a narrow central slice and the object stays on it. */
function placeHot(h){const W=frame.clientWidth,H=frame.clientHeight,sc=Math.max(W/G.imgW,H/G.imgH),dw=G.imgW*sc,dh=G.imgH*sc;
  /* cover crops the picture; slide it so the object stays on screen (a portrait phone shows a third of the width) */
  const clamp=(v,a,b)=>Math.min(b,Math.max(a,v));const ox=dw>W?clamp(W/2-h[0]/100*dw,W-dw,0):(W-dw)/2,oy=dh>H?clamp(H/2-h[1]/100*dh,H-dh,0):(H-dh)/2;
  sceneImage.style.objectPosition=`${dw>W?ox/(W-dw)*100:50}% ${dh>H?oy/(H-dh)*100:50}%`;
  const cx=ox+h[0]/100*dw,cy=oy+h[1]/100*dh,w=h[2]/100*dw,hh=h[3]/100*dh;hot.style.left=cx+'px';hot.style.top=cy+'px';hot.style.width=w+'px';hot.style.height=hh+'px';hot.classList.toggle('above',cy+hh/2>H*.84);hotLabel.textContent=ui('read');
  document.getElementById('fsLabel').textContent=ui('fullscreen');document.getElementById('soundLabel').textContent=ui(sound?'soundOn':'soundOff');document.getElementById('langWord').textContent=ui('translate');document.getElementById('langCur').textContent=state.lang==='off'?'OFF':G.names[state.lang];
  document.querySelectorAll('.lang-item').forEach(b=>b.classList.toggle('active',b.dataset.lang===state.lang))}
function setOpen(on){state.open=!!on;if(on){const hr=hot.getBoundingClientRect(),zr=zone.getBoundingClientRect();const cl=zr.left+content.offsetLeft,ct=zr.top+content.offsetTop;content.style.transformOrigin=`${hr.left+hr.width/2-cl}px ${hr.top+hr.height/2-ct}px`}frame.classList.toggle('open',state.open)}
function openPanel(){if(!state.open)setOpen(true)}
function closePanel(){if(state.open)setOpen(false)}
function render(){const s=G.scenes[state.scene];frame.className=`frame ${s.pos||'left'} v-${s.v||'center'}${RTL.includes(state.lang)?' rtl':''}`;sceneImage.src=G.dir+s.img;sceneImage.alt=s.title.en;placeHot(s.hot);const tr=state.lang!=='off';frame.classList.toggle('tr-on',tr);content.style.width=((s.width||(s.pos==='center'?64:46))+(tr?8:0))+'%';content.style.marginLeft=s.pos==='left'&&s.inset?s.inset+'%':'';content.style.marginRight=s.pos==='right'&&s.inset?s.inset+'%':'';
  let html=`<button class="hide-btn" onclick="closePanel()" title="Esc">✕ ${ui('hide')}</button>`+head(s);
  if(s.kind==='intro'){html+=`${s.rules?`<div class="rules-chips">${s.rules.map(r=>`<span>${label(r)}</span>`).join('')}</div>`:''}<button class="start" onclick="go('${s.next}')">${label(s.start)}</button>${s.small?`<div class="small">${label(s.small)}</div>`:''}`}
  else if(s.kind==='rules'){html+=`<div class="rules-intro">${s.rules.map(r=>`<div class="rule-card"><b>${label(r.name)}</b>${label(r.form)}</div>`).join('')}</div>${s.note?`<div class="rule-note">${label(s.note)}</div>`:''}<button class="continue" onclick="go('${s.next}')">${s.button?label(s.button):ui('begin')}</button>`}
  else if(s.kind==='story'){html+=`${s.rules?`<div class="rules-intro">${s.rules.map(r=>`<div class="rule-card"><b>${label(r.name)}</b>${label(r.form)}</div>`).join('')}</div>`:''}${s.note?`<div class="rule-note">${label(s.note)}</div>`:''}<button class="continue" onclick="go('${s.next}')">${s.button?label(s.button):ui('continue')}</button>`}
  else if(s.kind==='question'){html+=`${s.clue?`<div class="clue"><b>${ui('visual')}</b><br>${label(s.clue)}</div>`:''}<div class="prompt">${label(s.prompt)}</div><div class="options">${s.opts.map((o,i)=>`<button class="option${o.parts?' split':''}" data-i="${i}" onclick="answer(${i})"><span class="key">${i+1}</span>${optMarkup(o)}</button>`).join('')}</div><div id="feedback" class="feedback"></div><button id="continue" class="continue" hidden onclick="advance()">${ui('continue')}</button>`}
  else if(s.kind==='choice'){html+=`<div class="route-options">${s.routes.map((r,i)=>`<button class="route" onclick="chooseRoute(${i})"><b>${i+1} · ${label(r.name)}</b>${label(r.desc)}</button>`).join('')}</div>`}
  else if(s.kind==='ending'){const rev=G.repair?(state.mistakes.length?`<div class="review">${state.mistakes.map(id=>{const m=G.scenes[id];return `<div>${esc(m.prompt.en)}<br><b>${esc(optText(m.opts[m.answer]))}</b> — ${label(m.fb)}</div>`}).join('')}</div>`:`<div class="small">${ui('perfect')}</div>`):'';const ft=G.repair?` · ${state.score/(G.points||1)}/${G.total} ${ui('firstTry')}`:'';html+=`<div class="final-score">${ui('finalScore')} ${state.score}/${G.max}${ft} · ${'◆'.repeat(state.tiles)}${'◇'.repeat(Math.max(0,G.tiles-state.tiles))}</div>${rev}${state.route.length?`<div class="small">${ui('route')}: ${esc(state.route.join(' · ').toUpperCase())}</div>`:''}<button class="restart" onclick="restart()">${ui('restart')}</button>`}
  content.innerHTML=html;content.scrollTop=0;updateHUD();setOpen(s.kind==='intro'||s.kind==='ending');
  if(s.kind==='question'&&Object.prototype.hasOwnProperty.call(state.results,state.scene))setTimeout(()=>displayAnswer(state.results[state.scene],false),0)}
hot.addEventListener('click',e=>{e.stopPropagation();openPanel()});
sceneImage.addEventListener('click',()=>{closeMenu();closePanel()});
window.addEventListener('resize',()=>placeHot(G.scenes[state.scene].hot));
const langMenu=document.getElementById('langMenu'), langBtn=document.getElementById('langBtn');
function closeMenu(){langMenu.hidden=true;langBtn.setAttribute('aria-expanded','false')}
function toggleMenu(){langMenu.hidden=!langMenu.hidden;langBtn.setAttribute('aria-expanded',String(!langMenu.hidden))}
function go(id){state.scene=id;render()}
function displayAnswer(i,apply){const s=G.scenes[state.scene];const buttons=[...document.querySelectorAll('.option')];const ok=i===s.answer;const p=s.points||G.points;const fb=document.getElementById('feedback');const expl=s.fb?`<br>${label(s.fb)}`:'';
  if(apply)beep(ok);
  if(G.repair&&!ok){/* repair mode: mark it, explain, let them try again */buttons[i].classList.add('wrong');buttons[i].disabled=true;fb.innerHTML=`<strong>${ui('tryAgain')}</strong>${expl}`;fb.className='feedback show bad';if(apply)requestAnimationFrame(()=>content.scrollTo({top:content.scrollHeight,behavior:'smooth'}));return}
  buttons.forEach(b=>b.disabled=true);buttons[i]?.classList.add(ok?'correct':'wrong');buttons[s.answer]?.classList.add('correct');
  const retried=G.repair&&(state.attempts[state.scene]||0)>0;
  if(apply){if(ok&&!retried){state.score+=p}if(ok&&s.relic)state.tiles=Math.min(G.tiles,state.tiles+1);if(!ok)state.chances=Math.max(0,state.chances-1);if(s.final)state.finalCorrect=ok;if(G.repair)state.answered++}
  const head=ok?(retried?ui('repaired'):ui(s.relic?'relic':'correct',{p})):ui('wrong');const was=ok?'':`<br>${ui('answerWas')} ${esc(optText(s.opts[s.answer]))}`;
  fb.innerHTML=`<strong>${head}</strong>${was}${expl}`;fb.className=`feedback show ${ok?'good':'bad'}`;document.getElementById('continue').hidden=false;updateHUD();if(apply)requestAnimationFrame(()=>content.scrollTo({top:content.scrollHeight,behavior:'smooth'}))}
function answer(i){if(Object.prototype.hasOwnProperty.call(state.results,state.scene))return;const s=G.scenes[state.scene];if(G.repair&&i!==s.answer){if(!(state.attempts[state.scene]||0))state.mistakes.push(state.scene);state.attempts[state.scene]=(state.attempts[state.scene]||0)+1;displayAnswer(i,true);return}state.results[state.scene]=i;displayAnswer(i,true)}
function resolve(){const full=state.tiles>=G.tiles&&state.chances>0;if(state.finalCorrect&&full&&state.score>=G.max)return G.endings.master;if(state.finalCorrect&&full&&state.score>=G.completeScore)return G.endings.complete;if(state.finalCorrect&&state.tiles<G.tiles)return G.endings.missing;return G.endings.failed}
function advance(){const s=G.scenes[state.scene];if(state.chances<=0&&state.results[state.scene]!==s.answer){go(G.endings.failed);return}if(s.next==='resolve'){go(resolve());return}go(s.next)}
function chooseRoute(i){const r=G.scenes[state.scene].routes[i];if(r.route)state.route.push(r.route);go(r.min!=null&&state.score<r.min?r.else:r.target)}
function restart(){state=fresh(state.lang);render()}
(function(){['off',...LANGS].forEach(l=>{const b=document.createElement('button');b.className='lang-item';b.dataset.lang=l;b.innerHTML=l==='off'?`<b>OFF</b><span>${esc(G.labels.off.en)}</span>`:`<b>${l.toUpperCase()}</b><span>${esc(G.names[l])}</span>`;b.addEventListener('click',()=>{state.lang=l;closeMenu();setLang()});langMenu.appendChild(b)});langBtn.addEventListener('click',e=>{e.stopPropagation();toggleMenu()});document.addEventListener('click',e=>{if(!langMenu.hidden&&!langMenu.contains(e.target))closeMenu()})})();
function setLang(){const wasOpen=state.open;render();if(wasOpen)setOpen(true)}
document.getElementById('sound').addEventListener('click',()=>{setSound(!sound);beep(true)});
document.getElementById('fullscreen').addEventListener('click',()=>{if(!document.fullscreenElement)document.documentElement.requestFullscreen?.();else document.exitFullscreen?.()});
document.addEventListener('keydown',e=>{const k=e.key;if(k.toLowerCase()==='l'){const all=['off',...LANGS];state.lang=all[(all.indexOf(state.lang)+1)%all.length];setLang();return}if(k==='Escape'){if(!langMenu.hidden){closeMenu();return}closePanel();return}if(k.toLowerCase()==='f'){document.getElementById('fullscreen').click();return}if(k.toLowerCase()==='s'){document.getElementById('sound').click();return}if(!state.open&&(k==='Enter'||['1','2','3'].includes(k))){openPanel();return}const s=G.scenes[state.scene];if(['1','2','3'].includes(k)){const i=Number(k)-1;if(s.kind==='question')document.querySelector(`.option[data-i="${i}"]`)?.click();if(s.kind==='choice')document.querySelectorAll('.route')[i]?.click();return}if(k==='Enter')document.querySelector('.continue:not([hidden]),.start,.restart')?.click()});
setSound(sound);render();
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<!-- SEO:start -->
<meta name="description" content="{{DESC}}">
<link rel="canonical" href="https://forbesenglish.com/{{FILE}}">
<!-- SEO:end -->
<title>{{TITLE}}</title>
<style>
{{FONTS}}
{{CSS}}
</style>
</head>
<body class="paywalled">
{{BODY}}
<script>
{{JS}}
</script>
</body>
</html>
"""


def _check_langs(obj, langs, path):
    """Every learner-facing string must carry `en` and every gloss language —
    a menu entry that falls back to English halfway down the panel is the
    half-finished screen HOUSE-STYLE §8 exists to prevent."""
    if isinstance(obj, dict) and 'en' in obj:
        missing = [l for l in langs if not obj.get(l)]
        if missing:
            raise SystemExit('%s: missing %s for %r' % (path, ','.join(missing), obj['en'][:50]))
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            _check_langs(v, langs, '%s.%s' % (path, k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _check_langs(v, langs, '%s[%d]' % (path, i))


def validate(spec):
    langs = spec['langs']
    scenes = spec['scenes']
    for sid, s in scenes.items():
        if 'hot' not in s or len(s['hot']) != 4:
            raise SystemExit('scene %s: needs hot=[cx,cy,w,h] in picture %%' % sid)
        cx, cy, w, h = s['hot']
        if not (0 < cx < 100 and 0 < cy < 100 and 0 < w <= 60 and 0 < h <= 60):
            raise SystemExit('scene %s: hot %r is off the picture' % (sid, s['hot']))
        img = os.path.join(REPO, spec['img_dir'], s['img'])
        if not os.path.exists(img):
            raise SystemExit('scene %s: no picture at %s' % (sid, img))
        if s['kind'] == 'question':
            for o in s['opts']:
                if not (('en' in o) or ('parts' in o and 'kinds' in o)):
                    raise SystemExit('scene %s: option %r needs en or parts+kinds' % (sid, o))
            if not (0 <= s['answer'] < len(s['opts'])):
                raise SystemExit('scene %s: answer index out of range' % sid)
            nxt = s['next']
            if nxt != 'resolve' and nxt not in scenes:
                raise SystemExit('scene %s: next %r does not exist' % (sid, nxt))
        elif s['kind'] == 'choice':
            for r in s['routes']:
                if r['target'] not in scenes or ('else' in r and r['else'] not in scenes):
                    raise SystemExit('scene %s: route target %r missing' % (sid, r['target']))
        elif s['kind'] in ('intro', 'rules', 'story'):
            if s['next'] not in scenes:
                raise SystemExit('scene %s: next %r missing' % (sid, s['next']))
    for key, sid in spec['endings'].items():
        if scenes.get(sid, {}).get('kind') != 'ending':
            raise SystemExit('ending %s -> %s is not an ending scene' % (key, sid))
    labels = dict(LABELS, **spec.get('labels', {}))
    _check_langs(labels, langs, 'labels')
    # `opts` are left out on purpose: they are the English being taught, and
    # a gloss under an option is optional (HOUSE-STYLE §8 — never translate the
    # target language; Blocula glosses, the Wonderland export does not).
    _check_langs({k: {kk: vv for kk, vv in s.items() if kk in TEXT_KEYS or kk in ('rules', 'routes', 'button')}
                  for k, s in scenes.items()}, langs, 'scenes')
    _check_langs(spec.get('tags', {}), langs, 'tags')
    return labels


def assemble(spec, out=None):
    """spec keys — see README.md. Writes the page and returns its path."""
    labels = validate(spec)
    langs = spec['langs']
    game = {
        'dir': spec['img_dir'].rstrip('/').split('/')[-1] + '/',
        'imgW': spec.get('img_w', 1536), 'imgH': spec.get('img_h', 1024),
        'langs': langs, 'names': {l: LANG_NAMES.get(l, l.upper()) for l in langs},
        'labels': labels,
        'start': spec['start'], 'scenes': spec['scenes'], 'endings': spec['endings'],
        'max': spec['max'], 'points': spec.get('points', 5), 'tiles': spec['tiles'],
        'chances': spec['chances'], 'completeScore': spec.get('complete_score', spec['max']),
        'repair': bool(spec.get('repair')), 'total': spec.get('total', 0),
        'tags': spec.get('tags', {'a': {'en': 'NOW'}, 'b': {'en': 'USUALLY'}}),
    }
    css = (CSS.replace('{{ACCENT}}', spec['accent']).replace('{{ACCENT_INK}}', spec.get('accent_ink', '#1a1200'))
              .replace('{{DEEP}}', spec.get('deep', '#1a1200')).replace('{{PANEL}}', spec.get('panel', 'rgba(20,14,4,.88)')))
    body = BODY.replace('{{MAX}}', str(spec['max']))
    js = JS.replace('{{GAME}}', json.dumps(game, ensure_ascii=False, separators=(',', ':')))
    page = (PAGE.replace('{{FONTS}}', font_css()).replace('{{CSS}}', css.strip())
                .replace('{{BODY}}', body.strip()).replace('{{JS}}', js.strip())
                .replace('{{TITLE}}', html.escape(spec['title'])).replace('{{DESC}}', html.escape(spec['description']))
                .replace('{{FILE}}', spec['file']))
    out = out or os.path.join(REPO, spec['file'])
    # tools/seo.py fills the fenced block once the lesson has a catalogue row.
    # Keep that block across rebuilds so a builder re-run without seo.py
    # (a cloud session with a stale cache, say) does not strip the page's
    # metadata; seo.py still runs last and still wins when it does.
    if os.path.exists(out):
        prev = open(out, encoding='utf-8').read()
        m = re.search(r'<!-- SEO:start -->.*?<!-- SEO:end -->', prev, re.S)
        if m:
            page = re.sub(r'<!-- SEO:start -->.*?<!-- SEO:end -->', lambda _: m.group(0), page, count=1, flags=re.S)
    open(out, 'w', encoding='utf-8', newline='\n').write(page)
    n_q = sum(1 for s in spec['scenes'].values() if s['kind'] == 'question')
    print('wrote %s — %d scenes, %d questions, %d KB, langs %s' % (
        os.path.relpath(out, REPO), len(spec['scenes']), n_q, os.path.getsize(out) // 1024, '+'.join(['en'] + langs)))
    return out
