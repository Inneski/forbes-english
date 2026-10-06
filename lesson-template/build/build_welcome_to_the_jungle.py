#!/usr/bin/env python3
"""Welcome to the Jungle — Past Continuous voxel-jungle RPG (A2).

    python3 lesson-template/build/build_welcome_to_the_jungle.py

Rebuilds block-camp/welcome-to-the-jungle-rpg.html from
lesson-template/build/rpg/welcome-to-the-jungle-rpg/data.json — the text of
the standalone export Innes sent on 2026-10-05 as "The Drowned Sun", pulled
out by rpg/extract_standalone.py. Glosses come from the export's own `local`
blocks, flattened by rpg/make_translations.py.

**Renamed twice.** Innes asked for a new title with the file; it shipped for
one night as "The Sun Was Sinking" (block-camp/sun-was-sinking-rpg.html,
which src/index.js now redirects here), and on 2026-10-06 he named it:
"call it Welcome to the Jungle". The export's "THE DROWNED SUN" survives only
in data.json; the cover title and its nine glosses are TITLE below.

**The ChatGPT kind of export** (docs/CHATGPT-RPG-BRIEF.md), complete in the
same way as A Fistful of Lies — `meta`, `briefing`, per-scene `hotspot` and
`explanation`, nine languages — and built the same way. Same scoring as that
one too: 5 points a question, 3 chances, 4 sun tiles, 65 of 75 to pass, 15
questions on every path (3 + 2 + 5 + 2 + 3).

What this file does that the export did not:

  * **Every feedback line is rewritten to the house grammar-token rule** —
    the form in CAPS, cited words in double quotes ("Nia is "she", so the verb
    is WAS + listening"). The export's said "Use was + verb-ing ...", which a
    learner cannot tell apart from the sentence around it. Glosses for the
    new lines are FB below; the export's glosses of its own lines are unused.
  * **The briefing cards** follow The Lost Yellow Road's five, in its words,
    so the two Past Continuous adventures teach the form identically; their
    sentences are this story's. The export's game-rules note is kept.
  * **`rescue` offered "was hanged"** as a distractor, which is real English
    (the execution sense) and a teacher would have to accept it. It is
    "was hang" now.
  * **`engine` had no past time frame** — "The pumps ___ water away from
    the valley" — so nothing in the sentence asked for the continuous. It
    reads "When Nia found them, ...", and the clue says the same.
  * **Pictures for the briefing and three of the endings.** The export put
    the briefing and two endings on the cover and two on the last plate.
    The briefing takes the journal (Nia reading Ivo's notes), `complete` the
    sun turning in its socket, `missing` the pump wheel that still needs
    work, `failed` the flooded stair.
  * **Two hotspots moved:** `ledge` (the export's box sat on the wall beside
    the rope anchor) and `rescue` (on the ledge above the hook).

No soundtrack: deck_music.py has no track for this page yet.

Pictures: block-camp/welcome-to-the-jungle-rpg/*.webp, 1536x1024.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'welcome-to-the-jungle-rpg'
BASE = os.path.join(HERE, 'rpg', SLUG)
DATA = json.load(open(os.path.join(BASE, 'data.json'), encoding='utf-8'))
LANGS = rpg.NINE
# The Lost Yellow Road's briefing card headings, reused word for word; its
# translations directory holds their glosses in the seven languages it does
# not write inline (es and de are below).
LYR_TR = os.path.join(HERE, 'rpg', 'lost-yellow-road', 'translations')

# ── hotspots: [cx, cy, w, h] in % of the 1536x1024 picture, then panel side,
# vertical anchor, optional panel width %. The export's own boxes, checked on a
# gridded contact sheet; every object is on the right of its plate, so every
# panel goes left.
HOT = {
    'cover':    ([88, 68, 12, 15], 'left', 'center'),       # the turquoise compass
    'rules':    ([70, 55,  7, 10], 'left', 'center', 60),   # the journal clasp; five cards; 64 covers the clasp in es
    'entry':    ([87, 50, 12, 19], 'left', 'center'),       # the amber radio
    'bridge':   ([80, 55,  7, 11], 'left', 'center'),       # the compass on her belt
    'gate':     ([95, 24,  8, 22], 'left', 'center', 50),     # the jade switch
    'water':    ([90, 70, 13, 24], 'left', 'center'),       # the underwater lantern
    'wheel':    ([94, 53,  9, 30], 'left', 'center'),       # the wheel hub
    'ledge':    ([89, 62,  9, 16], 'left', 'center'),       # the rope anchor (export: x96 y67, beside it)
    'crane':    ([92, 63, 12, 20], 'left', 'center'),       # the crane lever
    'echo':     ([89, 65, 11, 20], 'left', 'center'),       # the sun tile in the wall
    'trap':     ([87, 77, 17, 10], 'left', 'center'),       # the floor switch
    'journal':  ([70, 55,  7, 10], 'left', 'center', 50),     # the journal clasp
    'engine':   ([92, 63,  9, 22], 'left', 'center'),       # the third sun tile
    'villain':  ([90, 74, 17, 12], 'left', 'center'),       # the empty sun socket
    'rescue':   ([88, 67, 12, 20], 'left', 'center'),       # the rope hook (export: y52, on the ledge above it)
    'rope':     ([92, 73, 14, 24], 'left', 'center'),       # the golden sun on the rope
    'record':   ([92, 64, 12, 17], 'left', 'center'),       # the amber recorder
    'flood':    ([90, 71, 14, 25], 'left', 'center'),       # the golden sun above the water
    'align':    ([86, 83, 17, 12], 'left', 'center'),       # the fourth sun tile
    'seal':     ([94, 44, 11, 35], 'left', 'center'),       # the sun in its socket
    'dawn':     ([90, 80, 12, 13], 'left', 'center'),       # the compass on the stone
    'fork':     ([87, 68, 15, 15], 'left', 'center'),       # the bronze route dial
    'decision': ([89, 67, 11, 16], 'left', 'center'),       # the sun fragment
    'end_master':   ([90, 80, 12, 13], 'left', 'center'),   # the compass on the stone
    'end_complete': ([94, 44, 11, 35], 'left', 'center'),   # the sun turning in its socket
    'end_missing':  ([94, 53,  9, 30], 'left', 'center'),   # the pump wheel, still to mend
    'end_failed':   ([90, 70, 13, 24], 'left', 'center'),   # the lantern in the flooded stair
}

# the export's endings pointed at two plates; each now takes the one its text describes
ENDINGS = {
    'master':   ('22_dawn.webp',  True),
    'complete': ('21_seal.webp',  True),
    'missing':  ('07_wheel.webp', False),
    'failed':   ('06_water.webp', False),
}


def T(en, **rest):
    return dict(en=en, **rest)


TITLE = T('WELCOME TO THE JUNGLE',
          es='BIENVENIDO A LA JUNGLA', de='WILLKOMMEN IM DSCHUNGEL', fr='BIENVENUE DANS LA JUNGLE',
          it='BENVENUTI NELLA GIUNGLA', pt='BEM-VINDO À SELVA', ru='ДОБРО ПОЖАЛОВАТЬ В ДЖУНГЛИ',
          ar='مرحبًا بك في الغابة', zh='欢迎来到丛林', ja='ジャングルへようこそ')

BRIEFING_KICKER = T(
    'BEFORE THE TEMPLE',
    es='ANTES DEL TEMPLO', de='VOR DEM TEMPEL', fr='AVANT LE TEMPLE',
    it='PRIMA DEL TEMPIO', pt='ANTES DO TEMPLO', ru='ПЕРЕД ХРАМОМ',
    ar='قبل المعبد', zh='进入神庙之前', ja='神殿に入る前に')

LABELS = {
    'tiles': T('SUN TILES',
               es='PIEZAS SOLARES', de='SONNENSTEINE', fr='TUILES SOLAIRES', it='TESSERE SOLARI',
               pt='PEÇAS SOLARES', ru='СОЛНЕЧНЫЕ ПЛИТКИ', ar='قطع الشمس', zh='太阳石板', ja='太陽のタイル'),
    'relic': T('SUN TILE FOUND · +{p} POINTS',
               es='PIEZA SOLAR ENCONTRADA · +{p} PUNTOS', de='SONNENSTEIN GEFUNDEN · +{p} PUNKTE',
               fr='TUILE SOLAIRE TROUVÉE · +{p} POINTS', it='TESSERA SOLARE TROVATA · +{p} PUNTI',
               pt='PEÇA SOLAR ENCONTRADA · +{p} PONTOS', ru='СОЛНЕЧНАЯ ПЛИТКА НАЙДЕНА · +{p} ОЧКОВ',
               ar='وُجدت قطعة شمس · +{p} نقاط', zh='找到太阳石板 · +{p} 分', ja='太陽のタイル発見 · +{p} ポイント'),
    'restart': T('EXPLORE AGAIN',
                 es='EXPLORAR DE NUEVO', de='ERNEUT ERKUNDEN', fr='EXPLORER À NOUVEAU',
                 it='ESPLORA DI NUOVO', pt='EXPLORAR DE NOVO', ru='ИССЛЕДОВАТЬ СНОВА',
                 ar='استكشف مجددًا', zh='再次探险', ja='もう一度探検する'),
}

# ── the five briefing cards: The Lost Yellow Road's headings, this story's
# sentences. A card that carries a pattern stays English in every gloss.
CARD_HEADS = [
    T('FORM · WAS / WERE + VERB-ING', es='FORMA · WAS / WERE + VERBO-ING', de='FORM · WAS / WERE + VERB-ING'),
    T('IN PROGRESS · AT A PAST MOMENT', es='EN CURSO · EN UN MOMENTO DEL PASADO',
      de='IM VERLAUF · IN EINEM MOMENT DER VERGANGENHEIT'),
    T('INTERRUPTED · WHEN + PAST SIMPLE', es='INTERRUMPIDA · WHEN + PASADO SIMPLE', de='UNTERBROCHEN · WHEN + PAST SIMPLE'),
    T('TWO ACTIONS · WHILE', es='DOS ACCIONES · WHILE', de='ZWEI HANDLUNGEN · WHILE'),
    T('QUESTIONS AND NEGATIVES', es='PREGUNTAS Y NEGACIONES', de='FRAGEN UND VERNEINUNGEN'),
]
PATTERN = 'I / he / she / it WAS climbing · you / we / they WERE waiting'


def card_forms():
    """Cards 2 and 3 are the export's own example sentences with the form in
    CAPS, so they keep the export's glosses; 1 is a pattern; 4 and 5 are new."""
    loc = DATA['briefing']['local']
    ex = lambda i: {l: loc[l]['cards'][i]['text'] for l in LANGS}
    return [
        T(PATTERN, **{l: PATTERN for l in LANGS}),
        T('At midnight, Nia WAS exploring the temple.', **ex(0)),
        T('Nia WAS crossing the bridge WHEN the rope broke.', **ex(4)),
        T('The blocks WERE falling WHILE Nia WAS escaping.',
          es='Los bloques caían MIENTRAS Nia escapaba.',
          de='Die Blöcke fielen, WÄHREND Nia gerade floh.',
          fr='Les blocs tombaient PENDANT QUE Nia s\'échappait.',
          it='I blocchi cadevano MENTRE Nia scappava.',
          pt='Os blocos caíam ENQUANTO a Nia fugia.',
          ru='Блоки падали, ПОКА Ния убегала.',
          ar='كانت الكتل تسقط بينما كانت نيا تهرب.',
          zh='尼娅逃跑的时候，石块正在落下。',
          ja='ニアが逃げている間、ブロックが落ちていた。'),
        T('WAS she listening? · The crane WASN\'T moving.',
          es='¿Estaba escuchando? · La grúa NO se movía.',
          de='Hörte sie gerade zu? · Der Kran bewegte sich NICHT.',
          fr='Est-ce qu\'elle écoutait ? · La grue NE bougeait PAS.',
          it='Stava ascoltando? · La gru NON si muoveva.',
          pt='Ela estava a ouvir? · A grua NÃO se mexia.',
          ru='Она слушала? · Кран НЕ двигался.',
          ar='هل كانت تستمع؟ · الرافعة لم تكن تتحرك.',
          zh='她当时在听吗？· 起重机当时没有动。',
          ja='彼女は聞いていた？ · クレーンは動いていなかった。'),
    ]


# ── one line under every answer, right or wrong: the rule the item tests, in
# the house form (CAPS for the form, double quotes for a cited word).
FB = {
    'entry': T('Nia is "she", so the verb is WAS + listening. WERE goes with you, we and they.',
               es='Nia es "she": el verbo es WAS + listening. WERE va con you, we y they.',
               de='Nia ist „she“, also WAS + listening. WERE steht bei you, we und they.',
               fr='Nia, c\'est "she" : le verbe est WAS + listening. WERE va avec you, we et they.',
               it='Nia è "she": il verbo è WAS + listening. WERE va con you, we e they.',
               pt='A Nia é "she": o verbo é WAS + listening. WERE vai com you, we e they.',
               ru='Ния — это "she", значит WAS + listening. WERE — с you, we и they.',
               ar='نيا هي "she"، لذلك الفعل WAS + listening. ونستخدم WERE مع you وwe وthey.',
               zh='Nia 是 "she"，所以用 WAS + listening。WERE 用于 you、we 和 they。',
               ja='Nia は "she" なので WAS + listening。WERE は you, we, they に使う。'),
    'bridge': T('The long action is WAS crossing. The short event that broke into it is past simple: "the rope broke".',
                es='La acción larga es WAS crossing. El hecho corto que la interrumpe va en pasado simple: "the rope broke".',
                de='Die lange Handlung ist WAS crossing. Das kurze Ereignis, das sie unterbricht, steht im Past Simple: „the rope broke“.',
                fr='L\'action longue est WAS crossing. L\'événement court qui l\'interrompt est au prétérit : "the rope broke".',
                it='L\'azione lunga è WAS crossing. L\'evento breve che la interrompe è al past simple: "the rope broke".',
                pt='A ação longa é WAS crossing. O acontecimento curto que a interrompe está no past simple: "the rope broke".',
                ru='Долгое действие — WAS crossing. Короткое событие, которое его прервало, — в Past Simple: "the rope broke".',
                ar='الفعل الطويل هو WAS crossing، والحدث القصير الذي قاطعه في الماضي البسيط: "the rope broke".',
                zh='较长的动作是 WAS crossing；打断它的短暂事件用一般过去时："the rope broke"。',
                ja='長い動作は WAS crossing。それを中断した短い出来事は過去形："the rope broke"。'),
    'gate': T('"Two explorers" are "they", so the verb is WERE + waiting.',
              es='"Two explorers" son "they": el verbo es WERE + waiting.',
              de='„Two explorers“ sind „they“, also WERE + waiting.',
              fr='"Two explorers", c\'est "they" : le verbe est WERE + waiting.',
              it='"Two explorers" sono "they": il verbo è WERE + waiting.',
              pt='"Two explorers" são "they": o verbo é WERE + waiting.',
              ru='"Two explorers" — это "they", значит WERE + waiting.',
              ar='"Two explorers" هما "they"، لذلك الفعل WERE + waiting.',
              zh='"Two explorers" 是 "they"，所以用 WERE + waiting。',
              ja='"Two explorers" は "they" なので WERE + waiting。'),
    'water': T('Nia is "she": WAS swimming. "Swim" doubles its M before -ING.',
               es='Nia es "she": WAS swimming. "Swim" duplica la M antes de -ING.',
               de='Nia ist „she“: WAS swimming. „Swim“ verdoppelt das M vor -ING.',
               fr='Nia, c\'est "she" : WAS swimming. "Swim" double son M avant -ING.',
               it='Nia è "she": WAS swimming. "Swim" raddoppia la M prima di -ING.',
               pt='A Nia é "she": WAS swimming. "Swim" dobra o M antes de -ING.',
               ru='Ния — "she": WAS swimming. В "swim" перед -ING удваивается M.',
               ar='نيا هي "she": WAS swimming. يتضاعف حرف M في "swim" قبل -ING.',
               zh='Nia 是 "she"：WAS swimming。"swim" 加 -ING 前要双写 M。',
               ja='Nia は "she"：WAS swimming。"swim" は -ING の前に M を重ねる。'),
    'wheel': T('One wheel is "it": WAS spinning. "Spin" doubles its N before -ING.',
               es='Una rueda es "it": WAS spinning. "Spin" duplica la N antes de -ING.',
               de='Ein Rad ist „it“: WAS spinning. „Spin“ verdoppelt das N vor -ING.',
               fr='Une roue, c\'est "it" : WAS spinning. "Spin" double son N avant -ING.',
               it='Una ruota è "it": WAS spinning. "Spin" raddoppia la N prima di -ING.',
               pt='Uma roda é "it": WAS spinning. "Spin" dobra o N antes de -ING.',
               ru='Одно колесо — "it": WAS spinning. В "spin" перед -ING удваивается N.',
               ar='العجلة الواحدة هي "it": WAS spinning. يتضاعف حرف N في "spin" قبل -ING.',
               zh='一个轮子是 "it"：WAS spinning。"spin" 加 -ING 前要双写 N。',
               ja='車輪ひとつは "it"：WAS spinning。"spin" は -ING の前に N を重ねる。'),
    'ledge': T('Nia is "she", so the verb is WAS + climbing. "Was climb" has no -ING.',
               es='Nia es "she": el verbo es WAS + climbing. "Was climb" no tiene -ING.',
               de='Nia ist „she“, also WAS + climbing. „Was climb“ fehlt das -ING.',
               fr='Nia, c\'est "she" : le verbe est WAS + climbing. "Was climb" n\'a pas de -ING.',
               it='Nia è "she": il verbo è WAS + climbing. "Was climb" non ha -ING.',
               pt='A Nia é "she": o verbo é WAS + climbing. "Was climb" não tem -ING.',
               ru='Ния — "she", значит WAS + climbing. В "was climb" нет -ING.',
               ar='نيا هي "she"، لذلك الفعل WAS + climbing. "Was climb" ينقصه -ING.',
               zh='Nia 是 "she"，所以用 WAS + climbing。"was climb" 少了 -ING。',
               ja='Nia は "she" なので WAS + climbing。"was climb" には -ING がない。'),
    'crane': T('The negative is WAS / WERE + NOT + verb-ING. The crane is "it": WAS NOT moving.',
               es='La negación es WAS / WERE + NOT + verbo-ING. La grúa es "it": WAS NOT moving.',
               de='Die Verneinung ist WAS / WERE + NOT + Verb-ING. Der Kran ist „it“: WAS NOT moving.',
               fr='La négation, c\'est WAS / WERE + NOT + verbe-ING. La grue, c\'est "it" : WAS NOT moving.',
               it='La negazione è WAS / WERE + NOT + verbo-ING. La gru è "it": WAS NOT moving.',
               pt='A negação é WAS / WERE + NOT + verbo-ING. A grua é "it": WAS NOT moving.',
               ru='Отрицание: WAS / WERE + NOT + глагол-ING. Кран — "it": WAS NOT moving.',
               ar='النفي هو WAS / WERE + NOT + فعل-ING. الرافعة هي "it": WAS NOT moving.',
               zh='否定式是 WAS / WERE + NOT + 动词-ING。起重机是 "it"：WAS NOT moving。',
               ja='否定は WAS / WERE + NOT + 動詞-ING。クレーンは "it"：WAS NOT moving。'),
    'echo': T('Ivo is "he": WAS holding. "Holded" is not a word; the past of "hold" is "held".',
              es='Ivo es "he": WAS holding. "Holded" no existe; el pasado de "hold" es "held".',
              de='Ivo ist „he“: WAS holding. „Holded“ gibt es nicht; die Vergangenheit von „hold“ ist „held“.',
              fr='Ivo, c\'est "he" : WAS holding. "Holded" n\'existe pas ; le passé de "hold" est "held".',
              it='Ivo è "he": WAS holding. "Holded" non esiste; il passato di "hold" è "held".',
              pt='O Ivo é "he": WAS holding. "Holded" não existe; o passado de "hold" é "held".',
              ru='Иво — "he": WAS holding. Слова "holded" нет; прошедшее от "hold" — "held".',
              ar='إيفو هو "he": WAS holding. كلمة "holded" غير موجودة؛ ماضي "hold" هو "held".',
              zh='Ivo 是 "he"：WAS holding。没有 "holded" 这个词，"hold" 的过去式是 "held"。',
              ja='Ivo は "he"：WAS holding。"holded" という語はない。"hold" の過去形は "held"。'),
    'trap': T('"The blocks" are "they": WERE falling. Both actions were in progress, so "while" joins them.',
              es='"The blocks" son "they": WERE falling. Las dos acciones estaban en curso, por eso las une "while".',
              de='„The blocks“ sind „they“: WERE falling. Beide Handlungen liefen gerade, deshalb verbindet sie „while“.',
              fr='"The blocks", c\'est "they" : WERE falling. Les deux actions étaient en cours, donc "while" les relie.',
              it='"The blocks" sono "they": WERE falling. Le due azioni erano in corso, quindi le unisce "while".',
              pt='"The blocks" são "they": WERE falling. As duas ações estavam a decorrer, por isso "while" liga-as.',
              ru='"The blocks" — это "they": WERE falling. Оба действия шли одновременно, поэтому их связывает "while".',
              ar='"The blocks" هي "they": WERE falling. كان الفعلان مستمرين، لذلك تربطهما "while".',
              zh='"The blocks" 是 "they"：WERE falling。两个动作都在进行，所以用 "while" 连接。',
              ja='"The blocks" は "they"：WERE falling。二つの動作が同時に進行中なので "while" でつなぐ。'),
    'journal': T('The negative is WAS + NOT + verb-ING: WAS NOT stealing. "Did not" takes the base verb: "did not steal".',
                 es='La negación es WAS + NOT + verbo-ING: WAS NOT stealing. "Did not" lleva el verbo base: "did not steal".',
                 de='Die Verneinung ist WAS + NOT + Verb-ING: WAS NOT stealing. Nach „did not“ steht die Grundform: „did not steal“.',
                 fr='La négation, c\'est WAS + NOT + verbe-ING : WAS NOT stealing. "Did not" prend la base verbale : "did not steal".',
                 it='La negazione è WAS + NOT + verbo-ING: WAS NOT stealing. "Did not" vuole il verbo base: "did not steal".',
                 pt='A negação é WAS + NOT + verbo-ING: WAS NOT stealing. "Did not" leva o verbo base: "did not steal".',
                 ru='Отрицание: WAS + NOT + глагол-ING: WAS NOT stealing. После "did not" — начальная форма: "did not steal".',
                 ar='النفي هو WAS + NOT + فعل-ING: WAS NOT stealing. بعد "did not" يأتي الفعل الأساسي: "did not steal".',
                 zh='否定式是 WAS + NOT + 动词-ING：WAS NOT stealing。"did not" 后接动词原形："did not steal"。',
                 ja='否定は WAS + NOT + 動詞-ING：WAS NOT stealing。"did not" の後は原形："did not steal"。'),
    'engine': T('"The pumps" are "they": WERE pushing. The action was already in progress when Nia found them.',
                es='"The pumps" son "they": WERE pushing. La acción ya estaba en curso cuando Nia las encontró.',
                de='„The pumps“ sind „they“: WERE pushing. Die Handlung lief schon, als Nia sie fand.',
                fr='"The pumps", c\'est "they" : WERE pushing. L\'action était déjà en cours quand Nia les a trouvées.',
                it='"The pumps" sono "they": WERE pushing. L\'azione era già in corso quando Nia le ha trovate.',
                pt='"The pumps" são "they": WERE pushing. A ação já estava a decorrer quando a Nia as encontrou.',
                ru='"The pumps" — это "they": WERE pushing. Действие уже шло, когда Ния их нашла.',
                ar='"The pumps" هي "they": WERE pushing. كان الفعل مستمرًا عندما وجدتها نيا.',
                zh='"The pumps" 是 "they"：WERE pushing。Nia 发现它们时，动作已经在进行。',
                ja='"The pumps" は "they"：WERE pushing。Nia が見つけたとき、動作はもう進行中だった。'),
    'villain': T('In a question, WAS / WERE comes before the subject: What WERE you looking for?',
                 es='En una pregunta, WAS / WERE va antes del sujeto: What WERE you looking for?',
                 de='In einer Frage steht WAS / WERE vor dem Subjekt: What WERE you looking for?',
                 fr='Dans une question, WAS / WERE vient avant le sujet : What WERE you looking for?',
                 it='In una domanda, WAS / WERE va prima del soggetto: What WERE you looking for?',
                 pt='Numa pergunta, WAS / WERE vem antes do sujeito: What WERE you looking for?',
                 ru='В вопросе WAS / WERE стоит перед подлежащим: What WERE you looking for?',
                 ar='في السؤال تأتي WAS / WERE قبل الفاعل: What WERE you looking for?',
                 zh='疑问句中 WAS / WERE 放在主语前：What WERE you looking for?',
                 ja='疑問文では WAS / WERE が主語の前に来る：What WERE you looking for?'),
    'rescue': T('Vale is "he": WAS hanging. The wave hit in the middle of that action.',
                es='Vale es "he": WAS hanging. La ola llegó en medio de esa acción.',
                de='Vale ist „he“: WAS hanging. Die Welle traf mitten in diese Handlung.',
                fr='Vale, c\'est "he" : WAS hanging. La vague a frappé au milieu de cette action.',
                it='Vale è "he": WAS hanging. L\'onda è arrivata nel mezzo di quell\'azione.',
                pt='O Vale é "he": WAS hanging. A onda chegou a meio dessa ação.',
                ru='Вейл — "he": WAS hanging. Волна ударила посреди этого действия.',
                ar='فيل هو "he": WAS hanging. ضربت الموجة في منتصف ذلك الفعل.',
                zh='Vale 是 "he"：WAS hanging。浪头打来时，这个动作正在进行。',
                ja='Vale は "he"：WAS hanging。波はその動作の最中に来た。'),
    'rope': T('Nia and Vale are "they", so the verb is WERE + holding.',
              es='Nia y Vale son "they": el verbo es WERE + holding.',
              de='Nia und Vale sind „they“, also WERE + holding.',
              fr='Nia et Vale, c\'est "they" : le verbe est WERE + holding.',
              it='Nia e Vale sono "they": il verbo è WERE + holding.',
              pt='A Nia e o Vale são "they": o verbo é WERE + holding.',
              ru='Ния и Вейл — это "they", значит WERE + holding.',
              ar='نيا وفيل هما "they"، لذلك الفعل WERE + holding.',
              zh='Nia 和 Vale 是 "they"，所以用 WERE + holding。',
              ja='Nia と Vale は "they" なので WERE + holding。'),
    'record': T('The recorder is "it": WAS working. "While" joins two actions in progress at the same time.',
                es='La grabadora es "it": WAS working. "While" une dos acciones en curso al mismo tiempo.',
                de='Das Aufnahmegerät ist „it“: WAS working. „While“ verbindet zwei gleichzeitig laufende Handlungen.',
                fr='L\'enregistreur, c\'est "it" : WAS working. "While" relie deux actions en cours en même temps.',
                it='Il registratore è "it": WAS working. "While" unisce due azioni in corso nello stesso momento.',
                pt='O gravador é "it": WAS working. "While" liga duas ações a decorrer ao mesmo tempo.',
                ru='Диктофон — "it": WAS working. "While" связывает два действия, идущих одновременно.',
                ar='جهاز التسجيل هو "it": WAS working. تربط "while" بين فعلين مستمرين في الوقت نفسه.',
                zh='录音机是 "it"：WAS working。"while" 连接同时进行的两个动作。',
                ja='レコーダーは "it"：WAS working。"while" は同時に進行中の二つの動作をつなぐ。'),
    'flood': T('"The water" is "it": WAS rising. "Rise" drops its E before -ING.',
               es='"The water" es "it": WAS rising. "Rise" pierde la E antes de -ING.',
               de='„The water“ ist „it“: WAS rising. „Rise“ verliert das E vor -ING.',
               fr='"The water", c\'est "it" : WAS rising. "Rise" perd son E avant -ING.',
               it='"The water" è "it": WAS rising. "Rise" perde la E prima di -ING.',
               pt='"The water" é "it": WAS rising. "Rise" perde o E antes de -ING.',
               ru='"The water" — это "it": WAS rising. В "rise" перед -ING выпадает E.',
               ar='"The water" هو "it": WAS rising. يُحذف حرف E من "rise" قبل -ING.',
               zh='"The water" 是 "it"：WAS rising。"rise" 加 -ING 前去掉 E。',
               ja='"The water" は "it"：WAS rising。"rise" は -ING の前で E を取る。'),
    'align': T('"Ivo and his team" are "they": WERE repairing. "Were repair" has no -ING.',
               es='"Ivo and his team" son "they": WERE repairing. "Were repair" no tiene -ING.',
               de='„Ivo and his team“ sind „they“: WERE repairing. „Were repair“ fehlt das -ING.',
               fr='"Ivo and his team", c\'est "they" : WERE repairing. "Were repair" n\'a pas de -ING.',
               it='"Ivo and his team" sono "they": WERE repairing. "Were repair" non ha -ING.',
               pt='"Ivo and his team" são "they": WERE repairing. "Were repair" não tem -ING.',
               ru='"Ivo and his team" — это "they": WERE repairing. В "were repair" нет -ING.',
               ar='"Ivo and his team" هم "they": WERE repairing. "Were repair" ينقصه -ING.',
               zh='"Ivo and his team" 是 "they"：WERE repairing。"were repair" 少了 -ING。',
               ja='"Ivo and his team" は "they"：WERE repairing。"were repair" には -ING がない。'),
    'seal': T('The negative is WERE + NOT + verb-ING. "The gears" are "they": WERE NOT turning.',
              es='La negación es WERE + NOT + verbo-ING. "The gears" son "they": WERE NOT turning.',
              de='Die Verneinung ist WERE + NOT + Verb-ING. „The gears“ sind „they“: WERE NOT turning.',
              fr='La négation, c\'est WERE + NOT + verbe-ING. "The gears", c\'est "they" : WERE NOT turning.',
              it='La negazione è WERE + NOT + verbo-ING. "The gears" sono "they": WERE NOT turning.',
              pt='A negação é WERE + NOT + verbo-ING. "The gears" são "they": WERE NOT turning.',
              ru='Отрицание: WERE + NOT + глагол-ING. "The gears" — это "they": WERE NOT turning.',
              ar='النفي هو WERE + NOT + فعل-ING. "The gears" هي "they": WERE NOT turning.',
              zh='否定式是 WERE + NOT + 动词-ING。"The gears" 是 "they"：WERE NOT turning。',
              ja='否定は WERE + NOT + 動詞-ING。"The gears" は "they"：WERE NOT turning。'),
    'dawn': T('Nia is "she": WAS saving. "Save" drops its E before -ING.',
              es='Nia es "she": WAS saving. "Save" pierde la E antes de -ING.',
              de='Nia ist „she“: WAS saving. „Save“ verliert das E vor -ING.',
              fr='Nia, c\'est "she" : WAS saving. "Save" perd son E avant -ING.',
              it='Nia è "she": WAS saving. "Save" perde la E prima di -ING.',
              pt='A Nia é "she": WAS saving. "Save" perde o E antes de -ING.',
              ru='Ния — "she": WAS saving. В "save" перед -ING выпадает E.',
              ar='نيا هي "she": WAS saving. يُحذف حرف E من "save" قبل -ING.',
              zh='Nia 是 "she"：WAS saving。"save" 加 -ING 前去掉 E。',
              ja='Nia は "she"：WAS saving。"save" は -ING の前で E を取る。'),
}

# ── `engine` gets a past time frame (docstring)
ENGINE_CLUE = T('The pumps were already working when Nia found them.',
                es='Las bombas ya estaban funcionando cuando Nia las encontró.',
                de='Die Pumpen arbeiteten schon, als Nia sie fand.',
                fr='Les pompes fonctionnaient déjà quand Nia les a trouvées.',
                it='Le pompe stavano già funzionando quando Nia le ha trovate.',
                pt='As bombas já estavam a funcionar quando a Nia as encontrou.',
                ru='Насосы уже работали, когда Ния их нашла.',
                ar='كانت المضخات تعمل بالفعل عندما وجدتها نيا.',
                zh='Nia 发现水泵时，它们已经在运转。',
                ja='Nia が見つけたとき、ポンプはもう動いていた。')
ENGINE_PROMPT = T('When Nia found them, the pumps ___ water away from the valley.',
                  es='Cuando Nia las encontró, las bombas ___ el agua lejos del valle.',
                  de='Als Nia sie fand, ___ die Pumpen das Wasser aus dem Tal.',
                  fr='Quand Nia les a trouvées, les pompes ___ l\'eau loin de la vallée.',
                  it='Quando Nia le ha trovate, le pompe ___ l\'acqua lontano dalla valle.',
                  pt='Quando a Nia as encontrou, as bombas ___ a água para longe do vale.',
                  ru='Когда Ния их нашла, насосы ___ воду из долины.',
                  ar='عندما وجدتها نيا، كانت المضخات ___ الماء بعيدًا عن الوادي.',
                  zh='Nia 发现水泵时，它们正在把水 ___ 出山谷。',
                  ja='Nia が見つけたとき、ポンプは谷から水を ___。')


def place(sid, scene):
    hot, pos, v = HOT[sid][:3]
    scene.update({'hot': hot, 'pos': pos, 'v': v})
    if len(HOT[sid]) > 3:
        scene['width'] = HOT[sid][3]
    return scene


def build():
    c, b = DATA['cover'], DATA['briefing']
    scenes = {
        'cover': place('cover', {
            'kind': 'intro', 'img': c['image'],
            'k': T(c['eyebrow']), 'title': TITLE, 'story': T(c['lead']),
            'rules': [T(r) for r in c['rules']],
            'start': T(c['start']), 'small': T(c['small']),
            'next': 'rules'}),
        'rules': place('rules', {
            'kind': 'rules', 'img': '12_journal.webp',
            'k': BRIEFING_KICKER, 'title': T(b['title']),
            'rules': [{'name': h, 'form': f} for h, f in zip(CARD_HEADS, card_forms())],
            'note': T(b['note']), 'button': T(b['button']),
            'next': DATA['first']}),
    }

    for sid, s in DATA['scenes'].items():
        base = {'img': s['image'], 'k': T(s['act']), 'title': T(s['title']),
                'story': T(s['story'])}
        if 'choices' in s:
            base['kind'] = 'choice'
            base['routes'] = [{'name': T(ch['label']), 'desc': T(ch['note']),
                               'route': ch['route'], 'target': ch['next']}
                              for ch in s['choices']]
        else:
            base['kind'] = 'question'
            base['clue'] = T(s['clue'])
            base['prompt'] = T(s['prompt'])
            base['opts'] = [T(a['text']) for a in s['answers']]
            base['answer'] = next(i for i, a in enumerate(s['answers']) if a.get('correct'))
            base['points'] = s.get('points', 5)
            if s.get('relic'):
                base['relic'] = True
            base['fb'] = FB[sid]
            # right and wrong answers share a road; the chance counter is the penalty
            assert s['correctNext'] == s['wrongNext'], sid
            base['next'] = s['correctNext']
        scenes[sid] = place(sid, base)

    scenes['engine']['clue'] = ENGINE_CLUE
    scenes['engine']['prompt'] = ENGINE_PROMPT
    # "was hanged" is real English (the execution sense); a teacher would have to accept it
    scenes['rescue']['opts'] = [T(o['en'].replace('was hanged', 'was hang')) for o in scenes['rescue']['opts']]
    # the last question decides whether a flawless run reaches the master ending
    scenes['dawn']['final'] = True

    for key, e in DATA['endings'].items():
        sid = 'end_' + key
        img, success = ENDINGS[key]
        end = {'kind': 'ending', 'img': img, 'success': success,
               'k': T(e['label']), 'title': T(e['title']), 'story': T(e['text'])}
        if e.get('routeTexts'):
            # keyed by the route name the decision scene pushes onto state.route
            end['routeStory'] = {r: T(t) for r, t in e['routeTexts'].items()}
        scenes[sid] = place(sid, end)

    sc = DATA['meta']['scoring']
    return {
        'file': 'block-camp/%s.html' % SLUG,
        'img_dir': 'block-camp/%s' % SLUG,
        'title': 'Welcome to the Jungle — Past Continuous Voxel Jungle RPG (A2)',
        'description': 'An interactive A2 English lesson from Forbes English: '
                       'Welcome to the Jungle — Past Continuous Voxel Jungle RPG (A2).',
        'langs': LANGS,
        # camp 4, Past Continuous, on the Block Camp route map. The export
        # asked for #86f5dc; README §1 says the camp colour wins.
        'accent': '#F1D779',
        'accent_ink': '#1a1200', 'deep': '#06201c', 'panel': 'rgba(5,22,20,.88)',
        'labels': LABELS,
        'start': 'cover', 'scenes': scenes,
        'endings': {'master': 'end_master', 'complete': 'end_complete',
                    'missing': 'end_missing', 'failed': 'end_failed'},
        'max': sc['max'], 'points': sc['points'], 'tiles': sc['tiles'],
        'chances': sc['chances'], 'complete_score': sc['pass'],
    }


if __name__ == '__main__':
    spec = rpg.apply_translations(build(), os.path.join(BASE, 'translations'))
    rpg.assemble(rpg.apply_translations(spec, LYR_TR))
