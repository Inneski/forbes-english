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
    'read':       {'en': 'CLICK TO READ', 'es': 'PULSA PARA LEER', 'de': 'KLICKEN ZUM LESEN', 'fr': 'CLIQUE POUR LIRE', 'it': 'CLICCA PER LEGGERE', 'pt': 'CLIQUE PARA LER', 'ru': 'НАЖМИ, ЧТОБЫ ЧИТАТЬ', 'ar': 'انقر للقراءة', 'zh': '点击阅读', 'ja': 'クリックして読む'},
    'hide':       {'en': 'HIDE', 'es': 'OCULTAR', 'de': 'AUSBLENDEN', 'fr': 'MASQUER', 'it': 'NASCONDI', 'pt': 'OCULTAR', 'ru': 'СКРЫТЬ', 'ar': 'إخفاء', 'zh': '隐藏', 'ja': '隠す'},
    'continue':   {'en': 'CONTINUE', 'es': 'CONTINUAR', 'de': 'WEITER', 'fr': 'CONTINUER', 'it': 'CONTINUA', 'pt': 'CONTINUAR', 'ru': 'ДАЛЕЕ', 'ar': 'متابعة', 'zh': '继续', 'ja': '続ける'},
    'begin':      {'en': 'BEGIN', 'es': 'EMPEZAR', 'de': 'LOSLEGEN', 'fr': 'COMMENCER', 'it': 'INIZIA', 'pt': 'COMEÇAR', 'ru': 'НАЧАТЬ', 'ar': 'ابدأ', 'zh': '开始', 'ja': '始める'},
    'restart':    {'en': 'PLAY AGAIN', 'es': 'JUGAR OTRA VEZ', 'de': 'NOCH EINMAL SPIELEN', 'fr': 'REJOUER', 'it': 'GIOCA ANCORA', 'pt': 'JOGAR DE NOVO', 'ru': 'ИГРАТЬ СНОВА', 'ar': 'العب مرة أخرى', 'zh': '再玩一次', 'ja': 'もう一度遊ぶ'},
    'fullscreen': {'en': 'FULLSCREEN', 'es': 'PANTALLA COMPLETA', 'de': 'VOLLBILD', 'fr': 'PLEIN ÉCRAN', 'it': 'SCHERMO INTERO', 'pt': 'ECRÃ INTEIRO', 'ru': 'ВО ВЕСЬ ЭКРАН', 'ar': 'ملء الشاشة', 'zh': '全屏', 'ja': '全画面'},
    'translate':  {'en': 'TRANSLATE', 'es': 'TRADUCIR', 'de': 'ÜBERSETZEN', 'fr': 'TRADUIRE', 'it': 'TRADUCI', 'pt': 'TRADUZIR', 'ru': 'ПЕРЕВОД', 'ar': 'ترجمة', 'zh': '翻译', 'ja': '翻訳'},
    'off':        {'en': 'English only', 'es': 'Solo inglés', 'de': 'Nur Englisch', 'fr': 'Anglais seulement', 'it': 'Solo inglese', 'pt': 'Só inglês', 'ru': 'Только английский', 'ar': 'الإنجليزية فقط', 'zh': '仅英语', 'ja': '英語のみ'},
    'visual':     {'en': 'VISUAL CLUE', 'es': 'PISTA VISUAL', 'de': 'BILDHINWEIS', 'fr': 'INDICE VISUEL', 'it': 'INDIZIO VISIVO', 'pt': 'PISTA VISUAL', 'ru': 'ВИЗУАЛЬНАЯ ПОДСКАЗКА', 'ar': 'دليل بصري', 'zh': '视觉线索', 'ja': '視覚ヒント'},
    'points':     {'en': 'POINTS', 'es': 'PUNTOS', 'de': 'PUNKTE', 'fr': 'POINTS', 'it': 'PUNTI', 'pt': 'PONTOS', 'ru': 'ОЧКИ', 'ar': 'نقاط', 'zh': '分数', 'ja': 'ポイント'},
    'tiles':      {'en': 'TILES', 'es': 'BALDOSAS', 'de': 'PLATTEN', 'fr': 'DALLES', 'it': 'PIASTRELLE', 'pt': 'LADRILHOS', 'ru': 'ПЛИТКИ', 'ar': 'بلاطات', 'zh': '砖块', 'ja': 'タイル'},
    'chances':    {'en': 'CHANCES', 'es': 'OPORTUNIDADES', 'de': 'CHANCEN', 'fr': 'CHANCES', 'it': 'TENTATIVI', 'pt': 'CHANCES', 'ru': 'ПОПЫТКИ', 'ar': 'فرص', 'zh': '机会', 'ja': 'チャンス'},
    'correct':    {'en': 'CORRECT · +{p} POINTS', 'es': 'CORRECTO · +{p} PUNTOS', 'de': 'RICHTIG · +{p} PUNKTE', 'fr': 'CORRECT · +{p} POINTS', 'it': 'CORRETTO · +{p} PUNTI', 'pt': 'CORRETO · +{p} PONTOS', 'ru': 'ВЕРНО · +{p} ОЧКОВ', 'ar': 'صحيح · +{p} نقاط', 'zh': '正确 · +{p} 分', 'ja': '正解 · +{p} ポイント'},
    'relic':      {'en': 'TILE RECOVERED · +{p} POINTS', 'es': 'BALDOSA RECUPERADA · +{p} PUNTOS', 'de': 'PLATTE GEBORGEN · +{p} PUNKTE', 'fr': 'DALLE RÉCUPÉRÉE · +{p} POINTS', 'it': 'PIASTRELLA RECUPERATA · +{p} PUNTI', 'pt': 'LADRILHO RECUPERADO · +{p} PONTOS', 'ru': 'ПЛИТКА НАЙДЕНА · +{p} ОЧКОВ', 'ar': 'استُعيدت البلاطة · +{p} نقاط', 'zh': '找回砖块 · +{p} 分', 'ja': 'タイル回収 · +{p} ポイント'},
    'wrong':      {'en': 'NO POINTS · −1 CHANCE', 'es': 'SIN PUNTOS · −1 OPORTUNIDAD', 'de': 'KEINE PUNKTE · −1 CHANCE', 'fr': 'AUCUN POINT · −1 CHANCE', 'it': 'NESSUN PUNTO · −1 TENTATIVO', 'pt': 'SEM PONTOS · −1 CHANCE', 'ru': 'НЕТ ОЧКОВ · −1 ПОПЫТКА', 'ar': 'لا نقاط · −1 فرصة', 'zh': '没有分数 · −1 机会', 'ja': 'ポイントなし · チャンス −1'},
    'answerWas':  {'en': 'Correct answer:', 'es': 'Respuesta correcta:', 'de': 'Richtige Antwort:', 'fr': 'Bonne réponse :', 'it': 'Risposta corretta:', 'pt': 'Resposta certa:', 'ru': 'Правильный ответ:', 'ar': 'الإجابة الصحيحة:', 'zh': '正确答案：', 'ja': '正解：'},
    'finalScore': {'en': 'FINAL SCORE', 'es': 'PUNTUACIÓN FINAL', 'de': 'ENDPUNKTZAHL', 'fr': 'SCORE FINAL', 'it': 'PUNTEGGIO FINALE', 'pt': 'PONTUAÇÃO FINAL', 'ru': 'ИТОГОВЫЙ СЧЁТ', 'ar': 'النتيجة النهائية', 'zh': '最终得分', 'ja': '最終スコア'},
    'route':      {'en': 'ROUTE', 'es': 'RUTA', 'de': 'ROUTE', 'fr': 'ROUTE', 'it': 'PERCORSO', 'pt': 'ROTA', 'ru': 'МАРШРУТ', 'ar': 'المسار', 'zh': '路线', 'ja': 'ルート'},
    'progress':   {'en': 'SPELLS', 'es': 'HECHIZOS', 'de': 'ZAUBER', 'fr': 'SORTS', 'it': 'INCANTESIMI', 'pt': 'FEITIÇOS', 'ru': 'ЗАКЛИНАНИЯ', 'ar': 'تعويذات', 'zh': '咒语', 'ja': '呪文'},
    'soundOn':    {'en': 'SOUND ON', 'es': 'SONIDO SÍ', 'de': 'TON AN', 'fr': 'SON ACTIVÉ', 'it': 'AUDIO ON', 'pt': 'SOM LIGADO', 'ru': 'ЗВУК ВКЛ', 'ar': 'الصوت مفعّل', 'zh': '声音开', 'ja': 'サウンドON'},
    'soundOff':   {'en': 'SOUND OFF', 'es': 'SONIDO NO', 'de': 'TON AUS', 'fr': 'SON COUPÉ', 'it': 'AUDIO OFF', 'pt': 'SOM DESLIGADO', 'ru': 'ЗВУК ВЫКЛ', 'ar': 'الصوت مغلق', 'zh': '声音关', 'ja': 'サウンドOFF'},
    'repaired':   {'en': 'SPELL REPAIRED', 'es': 'HECHIZO REPARADO', 'de': 'ZAUBER REPARIERT', 'fr': 'SORT RÉPARÉ', 'it': 'INCANTESIMO RIPARATO', 'pt': 'FEITIÇO REPARADO', 'ru': 'ЗАКЛИНАНИЕ ИСПРАВЛЕНО', 'ar': 'أُصلحت التعويذة', 'zh': '咒语已修复', 'ja': '呪文を修復した'},
    'tryAgain':   {'en': 'NOT YET · TRY ANOTHER', 'es': 'TODAVÍA NO · PRUEBA OTRA', 'de': 'NOCH NICHT · VERSUCH ES ANDERS', 'fr': 'PAS ENCORE · ESSAIE AUTRE CHOSE', 'it': 'NON ANCORA · PROVA UN\'ALTRA', 'pt': 'AINDA NÃO · TENTA OUTRA', 'ru': 'ПОКА НЕТ · ПОПРОБУЙ ДРУГОЙ', 'ar': 'ليس بعد · جرّب إجابة أخرى', 'zh': '还不对 · 再试一个', 'ja': 'まだ · 別の答えを試そう'},
    'firstTry':   {'en': 'first try', 'es': 'a la primera', 'de': 'beim ersten Versuch', 'fr': 'du premier coup', 'it': 'al primo tentativo', 'pt': 'à primeira', 'ru': 'с первой попытки', 'ar': 'من المحاولة الأولى', 'zh': '一次答对', 'ja': '一発正解'},
    'review':     {'en': 'REVIEW THE REPAIRED SPELLS', 'es': 'REPASA LOS HECHIZOS REPARADOS', 'de': 'DIE REPARIERTEN ZAUBER ANSEHEN', 'fr': 'REVOIR LES SORTS RÉPARÉS', 'it': 'RIVEDI GLI INCANTESIMI RIPARATI', 'pt': 'REVER OS FEITIÇOS REPARADOS', 'ru': 'ПОВТОРИТЬ ИСПРАВЛЕННЫЕ ЗАКЛИНАНИЯ', 'ar': 'راجع التعويذات المُصلحة', 'zh': '复习已修复的咒语', 'ja': '修復した呪文を復習'},
    'perfect':    {'en': 'Perfect first-try grammar. Every spell held.', 'es': 'Gramática perfecta a la primera. Todos los hechizos aguantaron.', 'de': 'Perfekte Grammatik beim ersten Versuch. Jeder Zauber hat gehalten.', 'fr': 'Grammaire parfaite du premier coup. Tous les sorts ont tenu.', 'it': 'Grammatica perfetta al primo tentativo. Ogni incantesimo ha retto.', 'pt': 'Gramática perfeita à primeira. Todos os feitiços aguentaram.', 'ru': 'Идеальная грамматика с первой попытки. Все заклинания выдержали.', 'ar': 'قواعد مثالية من المحاولة الأولى. صمدت كل التعويذات.', 'zh': '一次全对，语法完美。每个咒语都成功了。', 'ja': '一発で完璧な文法。すべての呪文が成功した。'},
    'readOn':     {'en': 'READ ON →', 'es': 'SIGUE LEYENDO →', 'de': 'WEITERLESEN →', 'fr': 'LIRE LA SUITE →', 'it': 'CONTINUA A LEGGERE →', 'pt': 'CONTINUAR A LER →', 'ru': 'ЧИТАТЬ ДАЛЬШЕ →', 'ar': '← تابع القراءة', 'zh': '继续阅读 →', 'ja': '読み進める →'},
    'nextChapter':{'en': 'CHAPTER {n} →', 'es': 'CAPÍTULO {n} →', 'de': 'KAPITEL {n} →', 'fr': 'CHAPITRE {n} →', 'it': 'CAPITOLO {n} →', 'pt': 'CAPÍTULO {n} →', 'ru': 'ГЛАВА {n} →', 'ar': '← الفصل {n}', 'zh': '第 {n} 章 →', 'ja': '第{n}章 →'},
    'chapters':   {'en': 'ALL CHAPTERS', 'es': 'TODOS LOS CAPÍTULOS', 'de': 'ALLE KAPITEL', 'fr': 'TOUS LES CHAPITRES', 'it': 'TUTTI I CAPITOLI', 'pt': 'TODOS OS CAPÍTULOS', 'ru': 'ВСЕ ГЛАВЫ', 'ar': 'كل الفصول', 'zh': '所有章节', 'ja': 'すべての章'},
    'help':       {'en': 'click the glowing object or ENTER to read · ESC hide · 1–3 choose · L language · S sound · F fullscreen',
                   'es': 'pulsa el objeto que brilla o ENTER para leer · ESC ocultar · 1–3 elegir · L idioma · S sonido · F pantalla completa',
                   'de': 'klicke das leuchtende Objekt oder ENTER zum Lesen · ESC ausblenden · 1–3 wählen · L Sprache · S Ton · F Vollbild',
                   'fr': 'clique sur l\'objet lumineux ou ENTRÉE pour lire · ÉCHAP masquer · 1–3 choisir · L langue · S son · F plein écran',
                   'it': 'clicca l\'oggetto luminoso o INVIO per leggere · ESC nascondi · 1–3 scegli · L lingua · S audio · F schermo intero',
                   'pt': 'clica no objeto brilhante ou ENTER para ler · ESC ocultar · 1–3 escolher · L idioma · S som · F ecrã inteiro',
                   'ru': 'нажми на светящийся предмет или ENTER, чтобы читать · ESC скрыть · 1–3 выбрать · L язык · S звук · F во весь экран',
                   'ar': 'انقر على الشيء المتوهج أو ENTER للقراءة · ESC إخفاء · 1–3 اختيار · L اللغة · S الصوت · F ملء الشاشة',
                   'zh': '点击发光物体或按 ENTER 阅读 · ESC 隐藏 · 1–3 选择 · L 语言 · S 声音 · F 全屏',
                   'ja': '光る物をクリックか ENTER で読む · ESC 隠す · 1–3 選ぶ · L 言語 · S サウンド · F 全画面'},
}

# `link` is a URL, not prose, so it is deliberately not in here; `linkLabel`
# is the words on it and must be glossed like anything else a learner reads.
TEXT_KEYS = ('k', 'title', 'story', 'clue', 'prompt', 'fb', 'note', 'small',
             'start', 'linkLabel')


NINE = ['es', 'de', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja']   # HOUSE-STYLE §8's full set


def apply_translations(spec, path):
    """Fill every learner-facing string from a translations file.

    The file maps language -> {English string: translation}. Keying by the
    English text keeps the file flat and lets one entry serve every place a
    line repeats ("Choose the correct question."). Strings the file lacks
    stay untouched, so validate() names them; a lesson ships the languages
    in spec['langs'] and nothing else."""
    if os.path.isdir(path):      # one <lang>.json per language
        table = {os.path.splitext(f)[0]: json.load(open(os.path.join(path, f), encoding='utf-8'))
                 for f in sorted(os.listdir(path)) if f.endswith('.json')}
    else:
        table = json.load(open(path, encoding='utf-8'))
    def walk(o):
        if isinstance(o, dict):
            if 'en' in o and isinstance(o['en'], str):
                for lang, m in table.items():
                    if lang in spec['langs'] and not o.get(lang) and o['en'] in m:
                        o[lang] = m[o['en']]
            else:
                for v in o.values():
                    walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(spec['scenes']); walk(spec.get('labels', {})); walk(spec.get('tags', {}))
    # a deck that folds a simpler text layer in keeps its chrome overrides
    # here; they need filling too, or they ship with English and nothing else.
    walk(spec.get('easy_labels', {})); walk(spec.get('easy_tags', {}))
    return spec


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
:root{--cake-a:rgba(207,52,125,.55);--cake-b:rgba(36,121,173,.55);
--cake-a-ink:#fff0f7;--cake-b-ink:#eef7ff;
--cake-a-edge:#ff8dc2;--cake-b-edge:#7cc4f2;
--cake-a-wash:rgba(207,52,125,.22);--cake-b-wash:rgba(36,121,173,.22);
--accent:{{ACCENT}};--accent-ink:{{ACCENT_INK}};--deep:{{DEEP}};--panel:{{PANEL}};--scrim:{{SCRIM}};--bone:#fff6d9;--muted:#d9ccb0;--soft:#efe2c0;--good:#77efb4;--bad:#ff6f82;--shadow:rgba(0,0,0,.55);
/* The scale unit. Every size below was authored as a fraction of a 16:9
   frame's width, so on a wider window the type outgrew the panel and the
   options fell below the fold. 1vw and 1.7778vh are equal at 16:9, so this
   changes nothing there and only ever caps, never enlarges. The frame is
   the viewport (.game is fixed inset:0), which is why vw/vh and not cqw. */
--u:min(1vw,1.7778vh)}
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
/* opt-in, per lesson: show the whole plate, letterboxed in the deep colour */
.fit-contain .scene-img{object-fit:contain}
.fit-contain{background:{{DEEP}}}
/* ── HUD ── */
.hud{position:absolute;z-index:5;top:calc(1.3 * var(--u));left:calc(1.5 * var(--u));right:calc(1.5 * var(--u));display:flex;align-items:center;justify-content:space-between;gap:calc(1 * var(--u));pointer-events:none}
.hud-group{display:flex;gap:calc(.55 * var(--u));align-items:center;flex-wrap:wrap}
.badge{background:var(--panel);backdrop-filter:blur(5px);border:1px solid rgba(255,246,217,.34);box-shadow:0 0 calc(1.3 * var(--u)) var(--shadow);padding:calc(.5 * var(--u)) calc(.8 * var(--u));font-size:calc(1.15 * var(--u));letter-spacing:.04em;white-space:nowrap}
.badge b{color:var(--accent);font-weight:700}
.langs{display:flex;gap:calc(.35 * var(--u));pointer-events:auto;position:relative}
.lang-btn,.utility{border:1px solid rgba(255,246,217,.35);color:var(--bone);background:var(--panel);padding:calc(.5 * var(--u)) calc(.75 * var(--u));cursor:pointer;font-size:calc(1.1 * var(--u));pointer-events:auto}
.lang-btn{display:flex;align-items:center;gap:calc(.3 * var(--u));white-space:nowrap}.lang-btn b{color:var(--accent)}
.utility:hover,.lang-btn:hover{border-color:var(--bone)}
.utility.fs{display:flex;align-items:center;gap:calc(.35 * var(--u));color:var(--accent-ink);background:linear-gradient(180deg,#fff0b8,var(--accent));border:1px solid #fff8dc;font-weight:700;letter-spacing:.06em;animation:fsglow 2.4s ease-in-out infinite}
.utility.fs:hover{filter:brightness(1.08)}
.lang-menu[hidden]{display:none}
.lang-menu{position:absolute;right:0;top:calc(100% + calc(.4 * var(--u)));z-index:20;display:grid;grid-template-columns:1fr;gap:calc(.25 * var(--u));min-width:calc(18 * var(--u));padding:calc(.45 * var(--u));background:rgba(14,9,2,.97);border:1px solid rgba(255,246,217,.4);box-shadow:0 calc(1 * var(--u)) calc(3 * var(--u)) rgba(0,0,0,.7)}
.lang-item{display:grid;grid-template-columns:calc(3 * var(--u)) 1fr;align-items:center;gap:calc(.4 * var(--u));border:1px solid transparent;background:none;color:var(--bone);padding:calc(.45 * var(--u)) calc(.55 * var(--u));text-align:left;cursor:pointer;font-size:calc(1.05 * var(--u))}
.lang-item b{color:var(--accent);font-size:calc(.95 * var(--u))}.lang-item:hover{border-color:rgba(255,246,217,.5);background:rgba(60,40,5,.9)}
.lang-item.active{background:var(--accent);color:var(--accent-ink)}.lang-item.active b{color:var(--accent-ink)}
/* ── the panel ── */
.zone{position:absolute;z-index:4;top:8%;bottom:3.5%;left:2.2%;right:2.2%;display:flex;pointer-events:none}
.content{pointer-events:auto;display:flex;flex-direction:column;gap:calc(.8 * var(--u));width:46%;max-height:100%;overflow:auto;scrollbar-width:thin;padding:calc(1.2 * var(--u)) calc(1.4 * var(--u));background:var(--panel);border:1px solid rgba(255,246,217,.22);box-shadow:0 calc(1.4 * var(--u)) calc(4 * var(--u)) var(--shadow);backdrop-filter:blur(6px);transition:transform .38s cubic-bezier(.2,.9,.3,1.15),opacity .22s ease;transform-origin:50% 50%}
.frame:not(.open) .content{opacity:0;transform:scale(.12);pointer-events:none;transition:transform .26s ease-in,opacity .18s ease-in}
/* A cover is a strip at the foot of the frame, with the panel fading up out of
   the picture instead of sitting on it as a box. The plate is the title
   screen; this is the caption under it.

   The foot is forced; the SIDE is not. Forcing both buried the cover marker on
   four of seven adventures — 43% on Frankenstein Part I, 37% on Sherlock —
   because a centred strip is ~64% of the zone and most cover objects sit near
   the middle. `pos` already carries each lesson's answer to that (Part I is
   `left`, Part II is `right`, both chosen against a measurement), so the
   strip honours it and centres only where the scene asks to be centred. */
.is-cover .zone{align-items:flex-end!important;bottom:16%}
.is-cover .content{width:auto!important;max-width:64%;margin:0!important;text-align:center;align-items:center;
  /* The scrim reaches full strength well above the first line of text. It used
     to start fading in at 42%, which put the kicker — accent colour, smallest
     type — on bare artwork: unreadable over snow on Part I and ice on Part II.
     The bottom padding clears the corner help bar, which the spec line used to
     sit on top of by 5-14px depending on how long that line is. */
  background:linear-gradient(180deg,rgba(0,0,0,0) 0%,var(--scrim) 30%);border:0;box-shadow:none;backdrop-filter:none;
  padding:calc(3.4 * var(--u)) calc(2.4 * var(--u)) calc(1.2 * var(--u));gap:calc(.5 * var(--u))}
.is-cover .kicker{text-shadow:0 .12em .5em rgba(0,0,0,.85),0 0 .3em rgba(0,0,0,.9)}
.is-cover .rules-chips{justify-content:center}
.is-cover .start{align-self:center;margin-top:calc(.35 * var(--u))}
.is-cover .hide-btn{display:none}
.is-cover .cover-title{font-size:calc(2.9 * var(--u))}
.is-cover .story{font-size:calc(1.5 * var(--u));max-width:calc(46 * var(--u))}
.left .zone{justify-content:flex-start}.left .content{text-align:left}
.right .zone{justify-content:flex-end}.right .content{text-align:right}
.center .zone{justify-content:center}.center .content{width:64%;text-align:center}
.v-top .zone{align-items:flex-start}.v-center .zone{align-items:center}.v-bottom .zone{align-items:flex-end}
/* ── `band`: a wide, shallow strip across the foot of the frame ──
   A side panel assumes the picture has an empty side. Wonderland's plates are
   crowd scenes — Alice stands in the middle and the supporting cast fills both
   edges — so 46% of the width buried a named character on eighteen of thirty-
   five screens, and on the pink/blue contrast plates it covered half of the
   very thing the question compares. A band reads across instead of down: the
   prose in one column, the options in the other, so it is roughly a third of
   the height a stacked panel needs and the upper two thirds of the picture
   stay visible. Innes asked for it on the first fork on 2026-09-16 ("bottom
   central and more streamlined or in two parts") and it answers the occlusion
   everywhere else too.

   It comes after the .v-* rules on purpose: same specificity, so the foot wins
   whatever `v` the scene carries. A band scene's hotspot must sit above ~60%
   of the picture — check-rpg-panels.js measures that. */
.band .zone{justify-content:center;align-items:flex-end}
.band .content{text-align:left;display:grid;grid-template-columns:1.12fr 1fr;align-items:end;
  column-gap:calc(2 * var(--u));row-gap:calc(.3 * var(--u));margin-bottom:calc(1.6 * var(--u));
  padding:calc(1 * var(--u)) calc(1.3 * var(--u))}
.band .hide-btn{grid-column:1/-1;justify-self:end;margin:calc(-.4 * var(--u)) calc(-.5 * var(--u)) 0 0}
.band-text,.band-act{display:flex;flex-direction:column;gap:calc(.6 * var(--u));min-width:0}
.band .continue,.band .start,.band .restart{align-self:flex-start}
/* The even split above is for a question, where the prompt and three options
   weigh about what the story does. The other kinds are lopsided.

   A story screen is prose and one button, so the button column shrinks to the
   button and the prose takes the whole strip: the same paragraph in a 64% column
   runs seven lines and in an 88% one runs five, and a band is only worth having
   while it stays shallow. The cap stops a long button label ("HELP ALICE STOP
   THE WARDEN") from taking a third of the strip back. */
.band.k-story:not(.has-rules) .content{grid-template-columns:1fr auto}.band.k-story:not(.has-rules) .band-act{max-width:calc(17 * var(--u))}
/* has-rules comes last: a story screen that carries a grammar table (the cake
   briefing) is a rules screen in everything but name, and the prose ratio
   squeezed the table into a column too narrow to read. */
.band.k-rules .content{grid-template-columns:1fr 2.4fr}
.band.has-rules:not(.k-rules) .content{grid-template-columns:1fr 1.6fr}
.band.k-choice .content{grid-template-columns:1.3fr 1fr}
.hide-btn{align-self:flex-end;order:-1;margin:calc(-.4 * var(--u)) calc(-.5 * var(--u)) calc(-.3 * var(--u)) 0;border:0;background:none;color:var(--soft);font-size:calc(.95 * var(--u));letter-spacing:.08em;cursor:pointer;padding:calc(.25 * var(--u)) calc(.4 * var(--u))}
.hide-btn:hover{color:#fff}.right .hide-btn{align-self:flex-start}
/* ── the glowing object ── */
.hot{position:absolute;z-index:6;left:50%;top:50%;width:10%;height:14%;transform:translate(-50%,-50%);border:0;background:none;padding:0;cursor:pointer;transition:opacity .25s;min-width:calc(3.6 * var(--u));min-height:calc(3.6 * var(--u))}
.hot i{position:absolute;inset:calc(-.4 * var(--u));border-radius:38%;background:linear-gradient(115deg,transparent 28%,rgba(255,250,220,.3) 42%,rgba(255,255,240,.7) 50%,rgba(255,250,220,.3) 58%,transparent 72%);background-size:260% 260%;mix-blend-mode:screen;box-shadow:0 0 0 calc(.16 * var(--u)) #fff,0 0 0 calc(.36 * var(--u)) rgba(70,45,0,.55),0 0 calc(1.6 * var(--u)) calc(.4 * var(--u)) rgba(255,240,170,.85),inset 0 0 calc(1.4 * var(--u)) rgba(255,255,220,.45);animation:shimmer 2.2s linear infinite,pulse 1.8s ease-in-out infinite}
.hot::before{content:"";position:absolute;inset:calc(-.4 * var(--u));border-radius:38%;border:calc(.18 * var(--u)) solid #fff;opacity:0;animation:ring 1.8s ease-out infinite}
.hot:hover i{animation-duration:1s,1.8s;box-shadow:0 0 0 calc(.2 * var(--u)) #fff,0 0 0 calc(.4 * var(--u)) rgba(70,45,0,.6),0 0 calc(2.4 * var(--u)) calc(.6 * var(--u)) rgba(255,240,170,1),inset 0 0 calc(1.8 * var(--u)) rgba(255,255,220,.6)}
.hot-label{position:absolute;left:50%;top:calc(100% + calc(.8 * var(--u)));transform:translateX(-50%);white-space:nowrap;color:#fff;font-weight:700;font-size:calc(1.3 * var(--u));letter-spacing:.04em;text-shadow:-.09em -.09em 0 var(--deep),0 -.09em 0 var(--deep),.09em -.09em 0 var(--deep),-.09em 0 0 var(--deep),.09em 0 0 var(--deep),-.09em .09em 0 var(--deep),0 .09em 0 var(--deep),.09em .09em 0 var(--deep),0 .14em .5em rgba(0,0,0,.9);pointer-events:none}
.hot.above .hot-label{top:auto;bottom:calc(100% + calc(.8 * var(--u)))}
.frame.open .hot{opacity:0;pointer-events:none}
@keyframes shimmer{0%{background-position:110% 110%}100%{background-position:-10% -10%}}
@keyframes pulse{0%,100%{opacity:.8}50%{opacity:1}}
@keyframes ring{0%{transform:scale(1);opacity:.9}100%{transform:scale(1.5);opacity:0}}
@keyframes fsglow{0%,100%{box-shadow:0 0 calc(.6 * var(--u)) rgba(255,240,170,.4)}50%{box-shadow:0 0 calc(1.6 * var(--u)) rgba(255,240,170,.9)}}
/* ── type scale: Monocraft is monospace and wide, so the scale is set by what
   fits 46% of a 16:9 frame, and it is deliberately a step up from Blocula
   (story calc(1.36 * var(--u)) there, 1.65 here) — "text should be bigger", 2026-09-05 ── */
.kicker{color:var(--accent);font-weight:700;font-size:calc(1.2 * var(--u));letter-spacing:.1em;text-transform:uppercase}
.title{margin:0;color:var(--accent);font-weight:700;font-size:calc(3 * var(--u));line-height:1.08;letter-spacing:0;text-shadow:-.05em 0 0 var(--deep),.05em 0 0 var(--deep),0 -.05em 0 var(--deep),0 .05em 0 var(--deep),-.05em -.05em 0 var(--deep),.05em -.05em 0 var(--deep),-.05em .05em 0 var(--deep),.05em .05em 0 var(--deep),0 0 .6em rgba(0,0,0,.6)}
.story{font-size:calc(1.65 * var(--u));line-height:1.36}
.clue{border-left:calc(.3 * var(--u)) solid var(--accent);padding:calc(.7 * var(--u)) calc(.9 * var(--u));background:rgba(255,235,160,.14);font-size:calc(1.4 * var(--u));line-height:1.3}
.clue b{color:var(--accent)}
.right .clue{border-left:0;border-right:calc(.3 * var(--u)) solid var(--accent)}.center .clue{border-right:calc(.3 * var(--u)) solid var(--accent)}
.prompt{color:#fff;font-weight:700;font-size:calc(1.65 * var(--u));line-height:1.28}
.translation{display:block;color:var(--muted);font-size:calc(1.1 * var(--u));line-height:1.28;margin-top:calc(.22 * var(--u));font-weight:400;font-style:italic;unicode-bidi:plaintext}
.rtl .translation{direction:rtl;text-align:right}
.title .translation,.kicker .translation{font-family:"Courier New",Courier,monospace}.title .translation{font-size:calc(1.25 * var(--u));letter-spacing:0;color:var(--soft);margin-top:calc(.4 * var(--u));text-shadow:none}
.kicker .translation{font-size:calc(.9 * var(--u));letter-spacing:.05em}
.options{display:grid;gap:calc(.55 * var(--u));margin-top:calc(.15 * var(--u))}
.option{display:grid;grid-template-columns:calc(2.6 * var(--u)) 1fr;align-items:center;gap:calc(.65 * var(--u));width:100%;border:1px solid rgba(255,246,217,.36);background:rgba(20,14,4,.8);color:var(--bone);padding:calc(.7 * var(--u)) calc(.8 * var(--u));text-align:left;cursor:pointer;font-size:calc(1.4 * var(--u));line-height:1.26;transition:.16s}
.option:hover{transform:translateY(-1px);border-color:#fff;background:rgba(70,48,8,.9)}
.option .key{display:grid;place-items:center;width:calc(2.4 * var(--u));height:calc(2.4 * var(--u));border:1px solid var(--accent);color:var(--accent);font-weight:700}
.option.correct{background:rgba(25,102,69,.9);border-color:var(--good)}.option.wrong{background:rgba(131,12,34,.93);border-color:var(--bad)}
.option:disabled{cursor:default;transform:none}.option .translation{font-size:calc(1.05 * var(--u))}
.option.split{grid-template-columns:calc(2.6 * var(--u)) 1fr 1fr;gap:calc(.5 * var(--u))}.option .half{display:flex;flex-direction:column;gap:calc(.15 * var(--u));padding:calc(.45 * var(--u)) calc(.6 * var(--u));border:1px solid rgba(255,246,217,.25)}
.option .half small{font-size:calc(.8 * var(--u));letter-spacing:.08em;opacity:.85}.option .half b{font-size:calc(1.35 * var(--u))}
.option .half.a{background:var(--cake-a)}.option .half.b{background:var(--cake-b)}
/* the two kinds of time this deck teaches. Everything that names them —
   the cake halves, the rule cards, the words inside a sentence — reads
   these two, so the pair can never drift apart in one place only. */
.tone-a,.tone-b{padding:0 .15em;border-radius:2px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.tone-a{background:var(--cake-a);color:var(--cake-a-ink)}
.tone-b{background:var(--cake-b);color:var(--cake-b-ink)}
.rule-card.tone{background:rgba(20,14,4,.8)}
.rule-card.tone-card-a{border-color:var(--cake-a-edge);background:var(--cake-a-wash)}
.rule-card.tone-card-b{border-color:var(--cake-b-edge);background:var(--cake-b-wash)}
.rule-card.tone-card-a>b{color:var(--cake-a-edge)}
.rule-card.tone-card-b>b{color:var(--cake-b-edge)}
.badge[hidden]{display:none}
.review{display:grid;gap:calc(.45 * var(--u));text-align:left}.review div{border-left:calc(.25 * var(--u)) solid var(--accent);padding:calc(.4 * var(--u)) calc(.7 * var(--u));background:rgba(255,235,160,.1);font-size:calc(1.15 * var(--u));line-height:1.3}.review b{color:var(--accent)}
.option.wrong:disabled{opacity:.7}
.right .option{text-align:right;grid-template-columns:1fr calc(2.6 * var(--u))}.right .option .key{order:2}.right .option.split{grid-template-columns:1fr 1fr calc(2.6 * var(--u))}.right .option.split .key{order:3}.option .half{text-align:left}
.feedback{display:none;padding:calc(.8 * var(--u)) calc(.9 * var(--u));border:1px solid rgba(255,246,217,.3);background:rgba(20,14,4,.85);font-size:calc(1.35 * var(--u));line-height:1.32}
.feedback.show{display:block}.feedback.good{border-color:var(--good)}.feedback.bad{border-color:var(--bad)}
.feedback strong{color:var(--accent)}.feedback .translation{font-size:calc(1.05 * var(--u))}
.continue,.start,.restart{text-decoration:none;align-self:flex-start;border:1px solid #fff8dc;background:linear-gradient(180deg,#fff0b8,var(--accent));color:var(--accent-ink);font-weight:700;letter-spacing:.07em;padding:calc(.8 * var(--u)) calc(1.2 * var(--u));cursor:pointer;font-size:calc(1.2 * var(--u));box-shadow:0 calc(.5 * var(--u)) calc(1.5 * var(--u)) rgba(0,0,0,.48)}
/* the gloss under a button sits on the light accent gradient, not on the dark
   panel: --muted there is cream on cream and reads as an empty second line. */
.continue .translation,.start .translation,.restart .translation{color:var(--accent-ink);opacity:.72}
.right .continue,.right .start,.right .restart{align-self:flex-end}.center .continue,.center .start,.center .restart{align-self:center}
.continue:hover,.start:hover,.restart:hover{filter:brightness(1.08)}
.rules-chips{display:flex;flex-wrap:wrap;gap:calc(.5 * var(--u))}.right .rules-chips{justify-content:flex-end}.center .rules-chips{justify-content:center}
.rules-chips span{border:1px solid var(--accent);color:var(--accent);padding:calc(.4 * var(--u)) calc(.65 * var(--u));font-size:calc(1 * var(--u));font-weight:700;letter-spacing:.06em}
.route-options{display:grid;grid-template-columns:1fr 1fr;gap:calc(.8 * var(--u))}
.route{border:1px solid rgba(255,246,217,.43);background:rgba(20,14,4,.82);color:#fff;padding:calc(1 * var(--u));cursor:pointer;text-align:left;min-height:calc(7 * var(--u));font-size:calc(1.25 * var(--u));line-height:1.3}
.route:hover{border-color:var(--accent);background:rgba(70,48,8,.92)}
.route b{display:block;color:var(--accent);font-size:calc(1.3 * var(--u));margin-bottom:calc(.4 * var(--u))}.route .translation{font-size:calc(1 * var(--u))}
/* the chapter picker on a page with `chapters`. One column, not the route
   fork's two: these are read in order, and a chapter's lead is a sentence
   rather than a label. Same sizes as .route so the two never disagree. */
.chapter-list{display:grid;grid-template-columns:1fr;gap:calc(.7 * var(--u))}
.chapter{border:1px solid rgba(255,246,217,.43);background:rgba(20,14,4,.82);color:#fff;padding:calc(1 * var(--u));cursor:pointer;text-align:left;font-size:calc(1.25 * var(--u));line-height:1.35}
.chapter:hover{border-color:var(--accent);background:rgba(70,48,8,.92)}
.chapter b{display:block;color:var(--accent);font-size:calc(1.3 * var(--u));margin-bottom:calc(.35 * var(--u))}.chapter .translation{font-size:calc(1 * var(--u))}
/* the READ ON row under a paged story block. The count sits left of the
   button so the eye finds "1 / 3" before it decides whether to tap. */
.story-pager{display:flex;align-items:center;gap:calc(1 * var(--u))}
.page-count{color:rgba(255,246,217,.62);font-size:calc(1 * var(--u));font-variant-numeric:tabular-nums;letter-spacing:.08em}
.story-pager .continue{margin-left:auto}
.rules-intro{display:grid;grid-template-columns:1fr 1fr;gap:calc(.75 * var(--u)) calc(1.4 * var(--u))}.rule-card:last-child{grid-column:1/-1}
.rule-card{white-space:pre-line;border:0;border-left:calc(.22 * var(--u)) solid rgba(255,246,217,.22);background:none;padding:calc(.1 * var(--u)) 0 calc(.1 * var(--u)) calc(.7 * var(--u));font-size:calc(1.08 * var(--u));line-height:1.3;text-align:left}
.rule-card b{display:block;color:var(--accent);font-size:calc(1.2 * var(--u));margin-bottom:calc(.15 * var(--u))}.rule-card .translation{font-size:calc(.95 * var(--u))}
.rule-note{color:#fff;font-size:calc(1.2 * var(--u));line-height:1.34;border:0;border-top:1px solid rgba(255,246,217,.18);padding:calc(.7 * var(--u)) 0 0;background:none;text-align:left}
.cover-title{font-size:calc(3.2 * var(--u));line-height:1}
.cover-title .big{display:block;font-size:1.7em;line-height:.95}
.final-score{font-size:calc(2.1 * var(--u));color:var(--accent);font-weight:700}
.small{font-size:calc(1 * var(--u));color:var(--muted)}
.corner-help{position:absolute;z-index:5;right:calc(1.5 * var(--u));bottom:calc(1.2 * var(--u));color:var(--soft);font-size:calc(.85 * var(--u));background:rgba(14,9,2,.7);padding:calc(.4 * var(--u)) calc(.55 * var(--u));pointer-events:none}
/* translation on: a little tighter, a little wider */
.tr-on .content{gap:calc(.55 * var(--u));padding:calc(1 * var(--u)) calc(1.2 * var(--u))}.tr-on .option{padding:calc(.5 * var(--u)) calc(.7 * var(--u))}.tr-on .options{gap:calc(.4 * var(--u))}.tr-on .title{font-size:calc(2.6 * var(--u))}
/* portrait / square-ish windows */
@media(max-aspect-ratio:4/3){.content{width:60%}.center .content{width:84%}.band .content{display:flex;flex-direction:column;gap:calc(.8 * var(--u))}.band .hide-btn{align-self:flex-end;margin-bottom:calc(-.3 * var(--u))}.hot-label{font-size:calc(1.8 * var(--u))}.lang-menu{min-width:calc(30 * var(--u))}.lang-item{font-size:calc(1.4 * var(--u))}.lang-item b{font-size:calc(1.3 * var(--u))}.title{font-size:calc(4.4 * var(--u))}.story,.prompt{font-size:calc(2.1 * var(--u))}.option,.feedback{font-size:calc(1.75 * var(--u))}.translation{font-size:calc(1.35 * var(--u))}.badge{font-size:calc(1.5 * var(--u))}.lang-btn,.utility{font-size:calc(1.4 * var(--u))}.clue{font-size:calc(1.7 * var(--u))}}
/* phones: the panel is a sheet across the bottom, sizes in px */
@media(max-width:700px){.hud{top:8px;left:8px;right:8px}.badge{font-size:11px;padding:5px 6px}.lang-btn,.utility{font-size:11px;padding:5px 6px}.zone{top:58px;bottom:10px;left:3%;right:3%;align-items:flex-end!important;justify-content:center!important}.content,.center .content,.tr-on .content{width:100%!important;margin:0!important;max-height:100%;text-align:left;padding:14px;gap:9px}.band .content{display:flex;flex-direction:column;margin-bottom:0!important}.band-text,.band-act{gap:9px}.right .content{text-align:left}.right .clue{border-right:0;border-left:4px solid var(--accent)}.right .option{text-align:left;grid-template-columns:24px 1fr}.right .option .key{order:0}.right .continue,.right .start,.right .restart,.center .continue,.center .start,.center .restart{align-self:flex-start}.right .hide-btn{align-self:flex-end}.hot{min-width:44px;min-height:44px}.hot i,.hot::before{inset:-4px}.hot i{box-shadow:0 0 0 2px #fff,0 0 0 4px rgba(70,45,0,.55),0 0 14px 3px rgba(255,240,170,.85)}.hot::before{border-width:2px}.hot-label{font-size:13px}.lang-menu{min-width:200px;padding:6px;gap:3px}.lang-item{font-size:13px;padding:6px 8px;grid-template-columns:32px 1fr}.lang-item b{font-size:12px}.hide-btn{font-size:12px}.title,.tr-on .title{font-size:26px}.cover-title{font-size:22px}.kicker{font-size:12px}.story,.prompt{font-size:17px}.clue{font-size:15px;padding:8px 10px;border-left-width:4px}.translation,.title .translation{font-size:13px}.option,.feedback{font-size:15px;padding:9px 10px}.option{grid-template-columns:24px 1fr;gap:8px}.option .key{width:22px;height:22px}.option .translation,.route .translation,.rule-card .translation,.feedback .translation{font-size:12px}.option.split{grid-template-columns:24px 1fr 1fr;gap:6px}.option .half{padding:6px 8px}.option .half small{font-size:10px}.option .half b{font-size:14px}.review div{font-size:13px;padding:6px 8px}.route-options,.rules-intro{grid-template-columns:1fr}.rule-card:last-child{grid-column:auto}.rule-card,.rule-note,.route,.chapter{font-size:14px;padding:9px}.rule-card b,.route b,.chapter b{font-size:14px}.rules-chips span{font-size:11px;padding:4px 7px}.final-score{font-size:19px}.small{font-size:12px}.continue,.start,.restart{font-size:14px;padding:11px 16px}.corner-help{display:none}}
"""

BODY = r"""
<main class="game" aria-live="polite">
  <section id="frame" class="frame left v-center">
    <img id="sceneImage" class="scene-img" alt="">
    <button id="hot" class="hot" aria-label="Show the text"><i></i><span id="hotLabel" class="hot-label">CLICK TO READ</span></button>
    <header class="hud">
      <div class="hud-group">
        <div class="badge"><span id="lblPoints">POINTS</span> <b id="score">0</b>/{{MAX}}</div>
        <div class="badge" id="tilesBadge"><span id="lblTiles">TILES</span> <b id="tiles"></b></div>
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
/* answer keys. Four options are house style (HOUSE-STYLE: "A/B/C/D labels"),
   and the engine used to bind only 1-3 — on a four-option lesson the fourth
   button was mouse-only, and it is the key on five of Frostbound's twelve. */
const NUM = ['1','2','3','4'];
/* `chapters` is a page that holds more than one game. Each chapter keeps its
   own start, score, endings, collectibles and chances, and the player picks
   one from a hub scene; nothing is carried between them. A page without
   `chapters` has state.chapter null and CH() is G, which is every lesson
   built before 2026-09-18 and is unchanged.
   The Kraken saga is the reason: three parts of fourteen questions each, one
   library card. Merging them into one 42-question run would have rewritten
   the game's own rules, which README.md section 1 forbids. */
const CH = () => (state.chapter == null || !G.chapters) ? G : G.chapters[state.chapter];
let state = fresh('off', null);
let sound=false;try{sound=localStorage.getItem('rpg-sound')==='1'}catch(_){}
/* two short tones, right and wrong — the Wonderland export's, kept */
function beep(ok){if(!sound)return;try{const c=new (window.AudioContext||window.webkitAudioContext)();const o=c.createOscillator(),g=c.createGain();o.type=ok?'square':'sawtooth';o.frequency.value=ok?620:180;g.gain.value=.03;o.connect(g);g.connect(c.destination);o.start();g.gain.exponentialRampToValueAtTime(.001,c.currentTime+.16);o.stop(c.currentTime+.18);o.onended=()=>c.close()}catch(_){}}
function setSound(on){sound=!!on;try{localStorage.setItem('rpg-sound',sound?'1':'0')}catch(_){}const b=document.getElementById('sound');b.setAttribute('aria-pressed',String(sound));b.firstChild.textContent=(sound?'🔊':'🔈')+' ';document.getElementById('soundLabel').textContent=ui(sound?'soundOn':'soundOff')}
function fresh(lang,ch){const c=(ch==null||!G.chapters)?G:G.chapters[ch];return {chapter:(ch==null||!G.chapters)?null:ch,scene:c.start,page:0,score:0,chances:c.chances,tiles:0,lang,open:false,route:[],results:{},attempts:{},mistakes:[],answered:0,finalCorrect:null,endingPick:null,endingMaster:false,endingMin:0}}
/* A scene's `story` is one block, or a list of them to be read a page at a
   time. The panel does not scroll by design (README section 1: never shrink
   type to fit), which caps a block at about 28 words — fine for the camp
   games, hopeless for a saga whose panels run 60 to 150. Paging is what the
   Kraken export did and it is the right answer: the reader taps READ ON and
   the question only appears under the last page. A scene with a single story
   block has one page and behaves exactly as before. */
const storyPages=s=>Array.isArray(s.story)?s.story:[s.story];
const frame=document.getElementById('frame'), content=document.getElementById('content'), sceneImage=document.getElementById('sceneImage');
const hot=document.getElementById('hot'), hotLabel=document.getElementById('hotLabel'), zone=document.getElementById('zone');
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const MARK=/\[\[(\/?)([ab])\]\]/g;
const bare=s=>String(s??'').replace(MARK,'');          /* plain text: alt, review, answer read-back */
const esct=s=>esc(s).replace(MARK,(_,c,k)=>c?'</span>':'<span class="tone-'+k+'">');
const tx=(o,l)=>o?(l&&o[l]?o[l]:o.en):'';
function ui(key,vars){let s=tx(G.labels[key],state.lang==='off'?null:state.lang);if(vars)for(const k in vars)s=s.replace('{'+k+'}',vars[k]);return s}
/* a gloss identical to the English (a formula, a name) is not shown — it would only repeat the line */
const gloss=obj=>state.lang!=='off'&&obj[state.lang]&&obj[state.lang]!==obj.en?obj[state.lang]:'';
function line(obj,cls=''){if(!obj)return '';const en=esct(obj.en),g=gloss(obj);return g?`<span class="${cls}">${en}<span class="translation">${esct(g)}</span></span>`:`<span class="${cls}">${en}</span>`}
function label(obj){if(!obj)return '';const g=gloss(obj);return g?`${esct(obj.en)}<span class="translation">${esct(g)}</span>`:esct(obj.en)}
/* an option is {en,…} or, for a two-blank item, {parts:[a,b], kinds:['a'|'b',…], tags:[{en,…},{en,…}]} — two coloured halves */
function optText(o){return bare(o.parts?o.parts.join(' / '):o.en)}
function optMarkup(o){if(!o.parts)return `<span>${label(o)}</span>`;return o.parts.map((p,i)=>`<span class="half ${o.kinds[i]}"><small>${label(G.tags[o.kinds[i]])}</small><b>${esc(p)}</b></span>`).join('')}
/* `tilesLabel` lets a chapter rename its own collectibles — the Kraken saga
   counts EVIDENCE in part one, MARKER BARRELS in part two and THE LAST FOUR
   in part three, on the same HUD badge. A lesson without one uses ui('tiles'). */
function updateHUD(){const c=CH();const onHub=G.scenes[state.scene]?.kind==='hub';document.getElementById('score').textContent=state.score;document.getElementById('tiles').textContent='◆'.repeat(state.tiles)+'◇'.repeat(Math.max(0,c.tiles-state.tiles));document.getElementById('chances').textContent='♥'.repeat(state.chances)+'♡'.repeat(Math.max(0,c.chances-state.chances));document.getElementById('lblPoints').textContent=ui('points');document.getElementById('lblTiles').textContent=c.tilesLabel?label(c.tilesLabel):ui('tiles');document.getElementById('lblChances').textContent=ui('chances');document.getElementById('tilesBadge').hidden=!c.tiles||onHub;document.getElementById('chancesBadge').hidden=!c.chances||onHub;document.getElementById('progressBadge').hidden=!c.total||onHub;if(c.total){document.getElementById('lblProgress').textContent=ui('progress');document.getElementById('progress').textContent=`${state.answered}/${c.total}`}document.getElementById('help').textContent=ui('help')}
/* A cover whose plate carries a painted title lockup has no title of its own: the h1 would only say the same thing again. */
/* the kicker and title belong to the scene, so they stay put while the story
   pages under them — a title that reappeared on every tap would read as a new
   scene each time. */
function head(s,pi){const has=s.title&&bare(s.title.en||'').trim();const t=s.kind==='intro'?`<span class="big">${label(s.title)}</span>`:label(s.title);return `${line(s.k,'kicker')}${has?`<h1 class="title ${s.kind==='intro'?'cover-title':''}">${t}</h1>`:''}${line(storyPages(s)[pi||0],'story')}`}
/* HOT = [cx, cy, w, h] as % of the PICTURE (3:2). The picture is object-fit:cover in the frame, so convert picture space to frame pixels; a phone shows a narrow central slice and the object stays on it. */
/* `fit:'contain'` shows the whole plate and letterboxes the remainder in the
   page's deep colour, instead of filling the frame and cropping. A 3:2 plate
   in a 16:9 window loses about 16% of its height to `cover`, and the slide
   below then puts that entire loss on one edge — which on the Kraken cover ate
   the word THE and on a quayside scene took both characters' heads off. When
   the art is the lesson, cropping it is not a trade worth making.
   The maths below already handles a letterboxed image: every `dw>W` / `dh>H`
   branch falls to centring, which is exactly right once the picture fits. */
/* a scene may carry its own imgW/imgH. Most games are one aspect throughout,
   but a cover is often drawn to the screen while the story plates are drawn to
   the art brief's ratio — Kraken's cover is 16:9 and its 58 plates are 3:2 —
   and the glow has to be placed in the picture's own space or it drifts. */
function placeHot(s){const h=s.hot,IW=s.imgW||G.imgW,IH=s.imgH||G.imgH;const W=frame.clientWidth,H=frame.clientHeight,sc=(G.fit==='contain'?Math.min:Math.max)(W/IW,H/IH),dw=IW*sc,dh=IH*sc;
  /* cover crops the picture; slide it so the object stays on screen (a portrait phone shows a third of the width) */
  const clamp=(v,a,b)=>Math.min(b,Math.max(a,v));const ox=dw>W?clamp(W/2-h[0]/100*dw,W-dw,0):(W-dw)/2,oy=dh>H?clamp(H/2-h[1]/100*dh,H-dh,0):(H-dh)/2;
  sceneImage.style.objectPosition=`${dw>W?ox/(W-dw)*100:50}% ${dh>H?oy/(H-dh)*100:50}%`;
  const cx=ox+h[0]/100*dw,cy=oy+h[1]/100*dh,w=h[2]/100*dw,hh=h[3]/100*dh;hot.style.left=cx+'px';hot.style.top=cy+'px';hot.style.width=w+'px';hot.style.height=hh+'px';hot.classList.toggle('above',cy+hh/2>H*.84);hotLabel.textContent=ui('read');
  document.getElementById('fsLabel').textContent=ui('fullscreen');document.getElementById('soundLabel').textContent=ui(sound?'soundOn':'soundOff');document.getElementById('langWord').textContent=ui('translate');document.getElementById('langCur').textContent=state.lang==='off'?'OFF':G.names[state.lang];
  document.querySelectorAll('.lang-item').forEach(b=>b.classList.toggle('active',b.dataset.lang===state.lang))}
function setOpen(on){state.open=!!on;if(on){const hr=hot.getBoundingClientRect(),zr=zone.getBoundingClientRect();const cl=zr.left+content.offsetLeft,ct=zr.top+content.offsetTop;content.style.transformOrigin=`${hr.left+hr.width/2-cl}px ${hr.top+hr.height/2-ct}px`}frame.classList.toggle('open',state.open)}
function openPanel(){if(!state.open)setOpen(true)}
function closePanel(){if(state.open)setOpen(false)}
function render(){const s=G.scenes[state.scene];frame.className=`frame ${s.pos||'left'} v-${s.v||'center'} k-${s.kind}${s.kind==='intro'?' is-cover':''}${RTL.includes(state.lang)?' rtl':''}${G.fit==='contain'?' fit-contain':''}`;sceneImage.src=G.dir+s.img;sceneImage.alt=bare((s.title&&s.title.en)||s.alt||'');placeHot(s);const tr=state.lang!=='off';frame.classList.toggle('tr-on',tr);frame.classList.toggle('has-rules',!!s.rules&&s.kind!=='intro');content.style.width=((s.width||(s.pos==='center'?64:s.pos==='band'?92:46))+(tr?(s.pos==='band'?3:8):0))+'%';content.style.marginLeft=s.pos==='left'&&s.inset?s.inset+'%':'';content.style.marginRight=s.pos==='right'&&s.inset?s.inset+'%':'';
  const hide=`<button class="hide-btn" onclick="closePanel()" title="Esc">✕ ${ui('hide')}</button>`;
  const np=storyPages(s).length,pi=Math.min(state.page||0,np-1);
  let html=head(s,pi),act='';
  /* mid-story: the only thing on offer is the next page. The scene's own
     action — question, routes, restart — waits for the last one. */
  if(pi<np-1){content.innerHTML=hide+html+`<div class="story-pager"><span class="page-count">${pi+1} / ${np}</span><button class="continue" onclick="nextPage()">${ui('readOn')}</button></div>`;content.scrollTop=0;updateHUD();setOpen(false);return}
  if(s.kind==='intro'){act+=`${s.rules?`<div class="rules-chips">${s.rules.map(r=>`<span>${label(r)}</span>`).join('')}</div>`:''}<button class="start" onclick="go('${s.next}')">${label(s.start)}</button>${s.small?`<div class="small">${label(s.small)}</div>`:''}`}
  else if(s.kind==='rules'){act+=`<div class="rules-intro">${s.rules.map(r=>`<div class="rule-card${r.tone?' tone-card-'+r.tone:''}"><b>${label(r.name)}</b>${label(r.form)}</div>`).join('')}</div>${s.note?`<div class="rule-note">${label(s.note)}</div>`:''}<button class="continue" onclick="go('${s.next}')">${s.button?label(s.button):ui('begin')}</button>`}
  else if(s.kind==='story'){act+=`${s.rules?`<div class="rules-intro">${s.rules.map(r=>`<div class="rule-card${r.tone?' tone-card-'+r.tone:''}"><b>${label(r.name)}</b>${label(r.form)}</div>`).join('')}</div>`:''}${s.note?`<div class="rule-note">${label(s.note)}</div>`:''}<button class="continue" onclick="go('${s.next}')">${s.button?label(s.button):ui('continue')}</button>`}
  else if(s.kind==='question'){act+=`${s.clue?`<div class="clue"><b>${ui('visual')}</b><br>${label(s.clue)}</div>`:''}<div class="prompt">${label(s.prompt)}</div><div class="options">${s.opts.map((o,i)=>`<button class="option${o.parts?' split':''}" data-i="${i}" onclick="answer(${i})"><span class="key">${i+1}</span>${optMarkup(o)}</button>`).join('')}</div><div id="feedback" class="feedback"></div><button id="continue" class="continue" hidden onclick="advance()">${ui('continue')}</button>`}
  else if(s.kind==='choice'){act+=`<div class="route-options">${s.routes.map((r,i)=>`<button class="route" onclick="chooseRoute(${i})"><b>${i+1} · ${label(r.name)}</b>${label(r.desc)}</button>`).join('')}</div>`}
  else if(s.kind==='hub'){act+=`<div class="chapter-list">${G.chapters.map((c,i)=>`<button class="chapter" onclick="startChapter(${i})"><b>${i+1} · ${label(c.title)}</b>${c.lead?label(c.lead):''}</button>`).join('')}</div>${s.small?`<div class="small">${label(s.small)}</div>`:''}`}
  else if(s.kind==='ending'){const c=CH();/* an ending may close with a paragraph that depends on the route taken (routeStory) */const rt=s.routeStory?(Object.entries(s.routeStory).find(([k])=>state.route.includes(k))||[])[1]:null;const rev=G.repair?(state.mistakes.length?`<div class="review">${state.mistakes.map(id=>{const m=G.scenes[id];return `<div>${esct(m.prompt.en)}<br><b>${esc(optText(m.opts[m.answer]))}</b> — ${label(m.fb)}</div>`}).join('')}</div>`:`<div class="small">${ui('perfect')}</div>`):'';const ft=G.repair?` · ${state.score/(G.points||1)}/${c.total} ${ui('firstTry')}`:'';
    /* the next chapter is offered from every ending, won or lost — a part
       three that can only be reached by mastering part two is a part three
       most learners never see. */
    const nx=(G.chapters&&state.chapter!=null&&state.chapter+1<G.chapters.length)?`<button class="start" onclick="startChapter(${state.chapter+1})">${ui('nextChapter',{n:state.chapter+2})}</button>`:'';
    const hub=(G.chapters)?`<button class="restart" onclick="toHub()">${ui('chapters')}</button>`:'';
    act+=`${rt?line(rt,'story'):''}<div class="final-score">${ui('finalScore')} ${state.score}/${c.max}${ft} · ${'◆'.repeat(state.tiles)}${'◇'.repeat(Math.max(0,c.tiles-state.tiles))}</div>${rev}${state.route.length?`<div class="small">${ui('route')}: ${esc(state.route.join(' · ').toUpperCase())}</div>`:''}${s.link?`<a class="start" href="${s.link}">${label(s.linkLabel)}</a>`:''}${nx}<button class="restart" onclick="restart()">${ui('restart')}</button>${hub}`}
  /* a band lays the two halves side by side; every other position stacks them */
  content.innerHTML=s.pos==='band'?`${hide}<div class="band-text">${html}</div><div class="band-act">${act}</div>`:hide+html+act;
  content.scrollTop=0;updateHUD();setOpen(false);
  if(s.kind==='question'&&Object.prototype.hasOwnProperty.call(state.results,state.scene))setTimeout(()=>displayAnswer(state.results[state.scene],false),0)}
hot.addEventListener('click',e=>{e.stopPropagation();openPanel()});
sceneImage.addEventListener('click',()=>{closeMenu();closePanel()});
window.addEventListener('resize',()=>placeHot(G.scenes[state.scene]));
const langMenu=document.getElementById('langMenu'), langBtn=document.getElementById('langBtn');
function closeMenu(){langMenu.hidden=true;langBtn.setAttribute('aria-expanded','false')}
function toggleMenu(){langMenu.hidden=!langMenu.hidden;langBtn.setAttribute('aria-expanded',String(!langMenu.hidden))}
function go(id){state.scene=id;state.page=0;render()}
/* paging keeps the panel up — the reader is mid-sentence, and folding it away
   on every tap would mean re-opening the object three times to read one scene */
function nextPage(){state.page=(state.page||0)+1;render();setOpen(true)}
function displayAnswer(i,apply){const s=G.scenes[state.scene];const buttons=[...document.querySelectorAll('.option')];const ok=i===s.answer;const p=s.points||G.points;const fb=document.getElementById('feedback');const expl=s.fb?`<br>${label(s.fb)}`:'';
  if(apply)beep(ok);
  if(G.repair&&!ok){/* repair mode: mark it, explain, let them try again */buttons[i].classList.add('wrong');buttons[i].disabled=true;fb.innerHTML=`<strong>${ui('tryAgain')}</strong>${expl}`;fb.className='feedback show bad';if(apply)requestAnimationFrame(()=>content.scrollTo({top:content.scrollHeight,behavior:'smooth'}));return}
  buttons.forEach(b=>b.disabled=true);buttons[i]?.classList.add(ok?'correct':'wrong');buttons[s.answer]?.classList.add('correct');
  const retried=G.repair&&(state.attempts[state.scene]||0)>0;
  if(apply){if(ok&&!retried){state.score+=p}if(ok&&s.relic)state.tiles=Math.min(CH().tiles,state.tiles+1);if(!ok)state.chances=Math.max(0,state.chances-1);if(s.final)state.finalCorrect=ok;state.answered++}
  const head=ok?(retried?ui('repaired'):ui(s.relic?'relic':'correct',{p})):ui('wrong');const was=ok?'':`<br>${ui('answerWas')} ${esc(optText(s.opts[s.answer]))}`;
  fb.innerHTML=`<strong>${head}</strong>${was}${expl}`;fb.className=`feedback show ${ok?'good':'bad'}`;document.getElementById('continue').hidden=false;updateHUD();if(apply)requestAnimationFrame(()=>content.scrollTo({top:content.scrollHeight,behavior:'smooth'}))}
function answer(i){if(Object.prototype.hasOwnProperty.call(state.results,state.scene))return;const s=G.scenes[state.scene];if(G.repair&&i!==s.answer){if(!(state.attempts[state.scene]||0))state.mistakes.push(state.scene);state.attempts[state.scene]=(state.attempts[state.scene]||0)+1;displayAnswer(i,true);return}state.results[state.scene]=i;displayAnswer(i,true)}
/* `alive` is "the player has not run out of chances". A repair-mode lesson has
   no chance counter at all (G.chances is 0 by design), so testing state.chances>0
   there is always false and silently kills every ending but `missing`/`failed` —
   a flawless Wonderland run scored 160/160 and was sent to the escape ending.
   With chances in play this is exactly the old test. */
/* `bands` is an ending chosen by score alone: [[min, sceneId], …] highest
   first, the first band the score reaches wins. An export whose endings are
   pure score thresholds (Frostbound: 64+ / 40-63 / below 40) has no tiles and
   no chances to reason about, and the tile/chance ladder below would send a
   64-point run to `missing` because G.tiles is 0. Lessons without `bands` are
   unchanged. */
/* `passScore` is the third way an export can decide an ending, after the
   tile/chance ladder and score-only `bands`: a pass mark, then the collection,
   then a perfect score. The Kraken export's own rule, verbatim —
   `chances<=0 || n<60 ? failed : items<4 ? missing : n===70 ? master : complete`
   — and it deliberately does not consult the final question, which the ladder
   below does. A 60/70 run with one collectible missing is `missing`; the
   ladder called it `failed` because the last answer was wrong, which is a
   different game from the one the export shipped. */
function resolve(){const c=CH();if(c.passScore!=null){const live=!c.chances||state.chances>0;if(!live||state.score<c.passScore)return c.endings.failed;if(state.tiles<c.tiles)return c.endings.missing;if(state.score>=c.max)return c.endings.master;return c.endings.complete}
  if(c.bands&&c.bands.length){const b=c.bands.find(b=>state.score>=b[0]);if(b)return b[1]}
  const alive=!c.chances||state.chances>0;const full=state.tiles>=c.tiles&&alive;const flawless=state.finalCorrect&&full&&state.score>=c.max;if(flawless&&(!state.endingPick||state.endingMaster))return c.endings.master;if(state.endingPick&&alive&&c.endings[state.endingPick]&&!(state.endingMin&&state.score<state.endingMin))return c.endings[state.endingPick];if(state.finalCorrect&&full&&state.score>=c.completeScore)return c.endings.complete;if(state.finalCorrect&&state.tiles<c.tiles)return c.endings.missing;return c.endings.failed}
/* `G.chances &&` is the same guard resolve() carries: a lesson with no chance
   counter at all (G.chances is 0 by design) has state.chances<=0 from the
   first frame, so the old test threw the learner to the failed ending on their
   first wrong answer. With chances in play this is exactly the old test. */
function advance(){const s=G.scenes[state.scene];const c=CH();if(c.chances&&state.chances<=0&&state.results[state.scene]!==s.answer){go(c.endings.failed);return}if(s.next==='resolve'){go(resolve());return}go(s.next)}
/* `endingMin` is a score floor on a route's own ending: the route decides WHICH
   reward ending you get, the floor decides whether you have earned one at all.
   Without it a route ending applies at any score. Frankenstein sets none, so its
   behaviour is unchanged. */
/* `points` on a route is the export kind whose story choices score (Frostbound:
   the careful road pays 4, the shortcut 2, and the ending bands read the
   total). A route without `points` scores nothing, as every route did before. */
function chooseRoute(i){const r=G.scenes[state.scene].routes[i];if(r.route)state.route.push(r.route);if(r.points)state.score+=r.points;if(r.ending){state.endingPick=r.ending;state.endingMaster=!!r.master;state.endingMin=r.endingMin||0}go(r.min!=null&&state.score<r.min?r.else:r.target)}
function restart(){state=fresh(state.lang,state.chapter);render()}
/* the hub and the chapters it starts. `toHub` resets to no chapter at all, so
   the HUD badges go quiet until one is picked. */
function startChapter(i){state=fresh(state.lang,i);render()}
function toHub(){state=fresh(state.lang,null);render()}
(function(){['off',...LANGS].forEach(l=>{const b=document.createElement('button');b.className='lang-item';b.dataset.lang=l;b.innerHTML=l==='off'?`<b>OFF</b><span>${esc(G.labels.off.en)}</span>`:`<b>${l.toUpperCase()}</b><span>${esc(G.names[l])}</span>`;b.addEventListener('click',()=>{state.lang=l;closeMenu();setLang()});langMenu.appendChild(b)});langBtn.addEventListener('click',e=>{e.stopPropagation();toggleMenu()});document.addEventListener('click',e=>{if(!langMenu.hidden&&!langMenu.contains(e.target))closeMenu()})})();
function setLang(){const wasOpen=state.open;render();if(wasOpen)setOpen(true)}
document.getElementById('sound').addEventListener('click',()=>{setSound(!sound);beep(true)});
document.getElementById('fullscreen').addEventListener('click',()=>{if(!document.fullscreenElement)document.documentElement.requestFullscreen?.();else document.exitFullscreen?.()});
document.addEventListener('keydown',e=>{const k=e.key;if(k.toLowerCase()==='l'){const all=['off',...LANGS];state.lang=all[(all.indexOf(state.lang)+1)%all.length];setLang();return}if(k==='Escape'){if(!langMenu.hidden){closeMenu();return}closePanel();return}if(k.toLowerCase()==='f'){document.getElementById('fullscreen').click();return}if(k.toLowerCase()==='s'){document.getElementById('sound').click();return}if(!state.open&&(k==='Enter'||NUM.includes(k))){openPanel();return}const s=G.scenes[state.scene];if(NUM.includes(k)){const i=Number(k)-1;if(s.kind==='question')document.querySelector(`.option[data-i="${i}"]`)?.click();if(s.kind==='choice')document.querySelectorAll('.route')[i]?.click();return}if(k==='Enter')document.querySelector('.continue:not([hidden]),.start,.restart')?.click()});
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


_MISSING = []


def _check_langs(obj, langs, path):
    """Every learner-facing string must carry `en` and every gloss language —
    a menu entry that falls back to English halfway down the panel is the
    half-finished screen HOUSE-STYLE §8 exists to prevent. Misses are
    collected and reported together, so one build run lists them all."""
    if isinstance(obj, dict) and 'en' in obj:
        missing = [l for l in langs if not obj.get(l)]
        if missing:
            _MISSING.append('%s: missing %s for %r' % (path, ','.join(missing), obj['en'][:70]))
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            _check_langs(v, langs, '%s.%s' % (path, k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _check_langs(v, langs, '%s[%d]' % (path, i))


def _opt_text(o):
    return o.get('en') or ' '.join(o.get('parts') or [])


def _check_answer_key(scenes):
    """The two answer-key gates, which an RPG had no enforcement for.

    A deck shuffles its options in the browser and applies A/B/C after
    (HOUSE-STYLE, "Multiple choice"), so neither gate can bite there. This
    engine renders `opts` in spec order — the first option really is the first
    button, every time — so the spec is the only place to get it right.

    The Frankenstein V32 export arrived with the answer in slot 0 on all 44
    questions. It is invisible in a diff of `'answer': 0` lines and obvious to
    the third student who notices. Builders distribute the key themselves;
    this refuses the build if one forgets.

    The length gate is HOUSE-STYLE's, verbatim: "The correct option must never
    be the longest one. This is a hard gate, not a preference." A correct
    answer written fuller than its distractors is scoreable without knowing
    any of the language being taught. Ties are fine — three options of equal
    length give nothing away.
    """
    qs = [(sid, s) for sid, s in scenes.items() if s.get('kind') == 'question']
    if not qs:
        return
    bad = []
    for sid, s in qs:
        opts = [_opt_text(o) for o in s['opts']]
        if len(opts) < 2:
            continue
        kl = len(opts[s['answer']])
        others = [len(o) for i, o in enumerate(opts) if i != s['answer']]
        hi, lo = max(others), min(others)
        if kl > hi * 1.10 and kl - hi >= 4:
            bad.append('%s: the key is the longest option, %d chars against %d (%.2fx) — %r'
                       % (sid, kl, hi, kl / hi, opts[s['answer']][:60]))
        if lo > kl * 1.50 and lo - kl >= 10:
            bad.append('%s: the key is the shortest option, %d chars against %d (%.2fx) — %r'
                       % (sid, kl, lo, lo / kl, opts[s['answer']][:60]))
    if len(qs) >= 4:
        tally = {}
        for _, s in qs:
            tally[s['answer']] = tally.get(s['answer'], 0) + 1
        top, n = max(tally.items(), key=lambda kv: kv[1])
        if n / len(qs) >= 0.80:
            bad.append('the key sits in slot %d on %d of %d questions (%d%%). Deal it across '
                       'the slots in the builder — this engine renders opts in spec order.'
                       % (top, n, len(qs), round(100 * n / len(qs))))
    if bad:
        raise SystemExit('answer key (HOUSE-STYLE):\n  ' + '\n  '.join(bad))


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
    # A chapter is a whole game's worth of spec on one page: its own start,
    # score, collectibles, chances and endings. The page-level values stay as
    # the defaults a lesson without chapters uses, so nothing built before
    # 2026-09-18 changes.
    for i, ch in enumerate(spec.get('chapters') or []):
        where = 'chapter %d (%s)' % (i + 1, (ch.get('title') or {}).get('en', '?'))
        if ch['start'] not in scenes:
            raise SystemExit('%s: start %r does not exist' % (where, ch['start']))
        for key, sid in ch['endings'].items():
            if scenes.get(sid, {}).get('kind') != 'ending':
                raise SystemExit('%s: ending %s -> %s is not an ending scene' % (where, key, sid))
        for k in ('max', 'tiles', 'chances'):
            if k not in ch:
                raise SystemExit('%s: needs %s — CH() reads it with no page-level fallback' % (where, k))
    if spec.get('chapters'):
        hubs = [sid for sid, s in scenes.items() if s['kind'] == 'hub']
        if len(hubs) != 1:
            raise SystemExit('a page with chapters needs exactly one hub scene, found %d' % len(hubs))
        if spec['start'] != hubs[0]:
            raise SystemExit('start should be the hub scene %r, not %r' % (hubs[0], spec['start']))
    bands = spec.get('bands') or []
    for i, (lo, sid) in enumerate(bands):
        if scenes.get(sid, {}).get('kind') != 'ending':
            raise SystemExit('band %d (%s+) -> %s is not an ending scene' % (i, lo, sid))
        if i and lo >= bands[i - 1][0]:
            raise SystemExit('bands must run highest first: %s+ follows %s+' % (lo, bands[i - 1][0]))
    if bands and bands[-1][0] > 0:
        raise SystemExit('the last band must be 0 — a score below %s reaches no ending' % bands[-1][0])
    _check_answer_key(scenes)
    labels = dict(LABELS, **spec.get('labels', {}))
    _check_langs(labels, langs, 'labels')
    # `opts` are left out on purpose: they are the English being taught, and
    # a gloss under an option is optional (HOUSE-STYLE §8 — never translate the
    # target language; Blocula glosses, the Wonderland export does not).
    _check_langs({k: {kk: vv for kk, vv in s.items() if kk in TEXT_KEYS or kk in ('rules', 'routes', 'button', 'routeStory')}
                  for k, s in scenes.items()}, langs, 'scenes')
    _check_langs(spec.get('tags', {}), langs, 'tags')
    # a chapter's name, its one-line lead and its collectible label are all
    # learner-facing, so they are glossed like any other string on the page
    _check_langs({'chapter %d' % (i + 1): {k: v for k, v in ch.items() if k in ('title', 'lead', 'tilesLabel')}
                  for i, ch in enumerate(spec.get('chapters') or [])}, langs, 'chapters')
    if _MISSING:
        raise SystemExit('%d untranslated strings:\n  ' % len(_MISSING) + '\n  '.join(_MISSING))
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
        'bands': spec.get('bands') or [],
        'chapters': spec.get('chapters') or None,
        'fit': spec.get('fit', 'cover'),
        'tags': spec.get('tags', {'a': {'en': 'NOW'}, 'b': {'en': 'USUALLY'}}),
    }
    css = (CSS.replace('{{ACCENT}}', spec['accent']).replace('{{ACCENT_INK}}', spec.get('accent_ink', '#1a1200'))
              .replace('{{DEEP}}', spec.get('deep', '#1a1200')).replace('{{PANEL}}', spec.get('panel', 'rgba(20,14,4,.88)'))
              # the cover caption is a gradient, not a box, so it needs more
              # alpha than the panel to hold a kicker over bright artwork.
              # A deck that thins its panel sets this; the rest inherit it.
              .replace('{{SCRIM}}', spec.get('scrim', spec.get('panel', 'rgba(20,14,4,.88)'))))
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
