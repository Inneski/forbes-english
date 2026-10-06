#!/usr/bin/env python3
"""Welcome to the Jungle — Past Continuous vs Past Simple voxel-jungle RPG (A2-B1).

    python3 lesson-template/build/build_welcome_to_the_jungle.py

Rebuilds block-camp/welcome-to-the-jungle-rpg.html from
lesson-template/build/rpg/welcome-to-the-jungle-rpg/data.json — the text of
the standalone export `Welcome_to_the_Jungle (1).html`, pulled out by
rpg/extract_standalone.py. Glosses come from the export's own `local`
blocks, flattened by rpg/make_translations.py.

**History.** The first export (2026-10-05, "The Drowned Sun") was Past
Continuous only, A2, and shipped for one night as "The Sun Was Sinking"
(src/index.js redirects that URL here). Innes named it "Welcome to the
Jungle" on 2026-10-06 and the same day sent this second export to replace
it: a new cast (Suri at the entrance, Tavi the pilot at the end), three
redrawn plates (02_radio, 10_echo, 22_dawn — same hotspot boxes, checked on
a contact sheet), and every question rewritten as a contrast, Past
Continuous against Past Simple, 9 continuous and 10 simple keys. Level
A2-B1. Same scoring: 5 points a question, 3 chances, 4 sun tiles, 65 of 75
to pass, 15 questions on every path.

**The ChatGPT kind of export** (docs/CHATGPT-RPG-BRIEF.md), complete —
`meta`, `briefing`, per-scene `hotspot` and `explanation`, nine languages —
and built like A Fistful of Lies. What this file does that the export did not:

  * **Every feedback line is in the house grammar-token form** — the form in
    CAPS, cited words in double quotes. The export's ("Snapped is the single
    event ...") cannot be told apart from the sentence around it. Glosses for
    the new lines are FB below; the export's glosses of its own are unused.
  * **The briefing cards** keep the export's headings and sentences with the
    forms in CAPS; the sentences keep the export's glosses.
  * **Five keys a teacher could not defend** (OPTION_FIX). In `water`,
    `ledge`, `echo` and `flood` the blank follows "while", where the past
    simple is ordinary English for a long action, so the export's
    past-simple distractor was also right. In `seal`, "The gears didn't turn
    because a stone was blocking them" was as good as the key. Each
    distractor is a wrong form now. The other meaning-based items keep both
    tenses as options: there the clue and the sentence ("once", "then",
    "when ... first saw it") make one of them wrong.
  * **A shorter briefing note** (NOTE): the export's repeated the cover's
    chips and pushed the BEGIN button below the fold in German and Spanish.
  * **Pictures for the briefing and three of the endings.** The export put
    the briefing and two endings on the cover and two on the last plate.
    The briefing takes the pump room (the widest panel the lesson needs), `complete` the sun turning in its socket,
    `missing` the pump wheel, `failed` the flooded stair.
  * **Two hotspots moved:** `ledge` (the export's box sat beside the rope
    anchor) and `rescue` (on the ledge above the hook).

Camp 4's colour (Past Continuous): the contrast with the past simple is
taught inside that camp, as The Lost Yellow Road's WHEN card does.

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

# ── hotspots: [cx, cy, w, h] in % of the 1536x1024 picture, then panel side,
# vertical anchor, optional panel width %. The export's own boxes, checked on a
# gridded contact sheet; every object is on the right of its plate, so every
# panel goes left.
HOT = {
    'cover':    ([88, 68, 12, 15], 'left', 'center'),       # the turquoise compass
    'rules':    ([92, 63,  9, 22], 'left', 'center', 72),   # the third sun tile; five cards and a long note need the width (the journal plate capped it at 60 and the button fell below the fold in es)
    'entry':    ([87, 50, 12, 19], 'left', 'center'),       # the amber radio
    'bridge':   ([80, 55,  7, 11], 'left', 'center'),       # the compass on her belt
    'gate':     ([95, 24,  8, 22], 'left', 'center', 50),     # the jade switch
    'water':    ([90, 70, 13, 24], 'left', 'center'),       # the underwater lantern
    'wheel':    ([94, 53,  9, 30], 'left', 'center'),       # the wheel hub
    'ledge':    ([89, 62,  9, 16], 'left', 'center'),       # the rope anchor (export: x96 y67, beside it)
    'crane':    ([92, 63, 12, 20], 'left', 'center', 50),      # the crane lever
    'echo':     ([89, 65, 11, 20], 'left', 'center', 58),      # the sun tile in the wall
    'trap':     ([87, 77, 17, 10], 'left', 'center', 50),      # the floor switch
    'journal':  ([70, 55,  7, 10], 'left', 'center', 50),     # the journal clasp
    'engine':   ([92, 63,  9, 22], 'left', 'center'),       # the third sun tile
    'villain':  ([90, 74, 17, 12], 'left', 'center'),       # the empty sun socket
    'rescue':   ([88, 67, 12, 20], 'left', 'center'),       # the rope hook (export: y52, on the ledge above it)
    'rope':     ([92, 73, 14, 24], 'left', 'center'),       # the golden sun on the rope
    'record':   ([92, 64, 12, 17], 'left', 'center'),       # the amber recorder
    'flood':    ([90, 71, 14, 25], 'left', 'center'),       # the golden sun above the water
    'align':    ([86, 83, 17, 12], 'left', 'center', 50),      # the fourth sun tile
    'seal':     ([94, 44, 11, 35], 'left', 'center'),       # the sun in its socket
    'dawn':     ([90, 80, 12, 13], 'left', 'center', 50),      # the compass on the stone
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


# ── the five briefing cards: the export's headings (glossed in translations/)
# and its example sentences with the forms in CAPS, which keep the export's
# glosses of the same sentences.
CARD_FORMS = [
    'They WERE crossing the bridge. The crossing was not finished.',
    'The rope SNAPPED. Nia CAUGHT it.',
    'They WERE crossing the bridge WHEN the rope SNAPPED.',
    'Nia WAS swimming WHILE water WAS rushing down the stairs.',
    'WAS she climbing? DID she fall? She DIDN\'T fall.',
]


def cards():
    b = DATA['briefing']
    out = []
    for i, (card, form) in enumerate(zip(b['cards'], CARD_FORMS)):
        gloss = {l: b['local'][l]['cards'][i]['text'] for l in LANGS}
        out.append({'name': T(card['head']), 'form': T(form, **gloss)})
    return out


# ── four stems put "while" in front of the blank, and after "while" the past
# simple is ordinary English for a long action ("Her torch flickered while
# Nia swam underwater"), so a teacher would have to accept the export's past
# simple distractor. Each is a wrong form now. `seal` had the same fault the
# other way round: "The gears didn't turn because a stone was blocking them"
# is as good as the key.
OPTION_FIX = {
    'water': ('swam', 'was swim'),
    'ledge': ('climbed', 'was climb'),
    'echo':  ('escaped', 'were escape'),
    'flood': ('rose', 'was rise'),
    'seal':  ('didn’t turn', 'didn’t turning'),
}

# ── one line under every answer, right or wrong: the rule the item tests, in
# the house form (CAPS for the form, double quotes for a cited word).
FB = {
    'entry': T('Nia was in the middle of her sentence: WAS speaking. The sudden event is past simple: the radio "went silent".',
               es='Nia estaba a mitad de la frase: WAS speaking. El hecho repentino va en pasado simple: la radio "went silent".',
               de='Nia war mitten im Satz: WAS speaking. Das plötzliche Ereignis steht im Past Simple: das Funkgerät „went silent“.',
               fr='Nia était au milieu de sa phrase : WAS speaking. L\'événement soudain est au prétérit : la radio "went silent".',
               it='Nia era a metà frase: WAS speaking. L\'evento improvviso è al past simple: la radio "went silent".',
               pt='A Nia estava a meio da frase: WAS speaking. O acontecimento súbito está no past simple: o rádio "went silent".',
               ru='Ния была на середине фразы: WAS speaking. Внезапное событие — в Past Simple: радио "went silent".',
               ar='كانت نيا في منتصف جملتها: WAS speaking. الحدث المفاجئ في الماضي البسيط: الراديو "went silent".',
               zh='Nia 话说到一半：WAS speaking。突然发生的事用一般过去时：收音机 "went silent"。',
               ja='Nia は話している途中だった：WAS speaking。突然の出来事は過去形：無線が "went silent"。'),
    'bridge': T('The rope breaks once, suddenly: past simple SNAPPED. The longer action around it is past continuous: "was crossing".',
                es='La cuerda se rompe una vez, de golpe: pasado simple SNAPPED. La acción más larga va en pasado continuo: "was crossing".',
                de='Das Seil reißt einmal, plötzlich: Past Simple SNAPPED. Die längere Handlung drumherum ist Past Continuous: „was crossing“.',
                fr='La corde casse une fois, d\'un coup : prétérit SNAPPED. L\'action plus longue autour est au passé continu : "was crossing".',
                it='La corda si spezza una volta, all\'improvviso: past simple SNAPPED. L\'azione più lunga intorno è al past continuous: "was crossing".',
                pt='A corda parte-se uma vez, de repente: past simple SNAPPED. A ação mais longa à volta está no past continuous: "was crossing".',
                ru='Верёвка рвётся один раз, внезапно: Past Simple SNAPPED. Более долгое действие вокруг — Past Continuous: "was crossing".',
                ar='ينقطع الحبل مرة واحدة فجأة: الماضي البسيط SNAPPED. والفعل الأطول حوله في الماضي المستمر: "was crossing".',
                zh='绳子突然断了一次：一般过去时 SNAPPED。周围较长的动作用过去进行时："was crossing"。',
                ja='ロープは一度、突然切れる：過去形 SNAPPED。その周りの長い動作は過去進行形："was crossing"。'),
    'gate': T('Finished steps, one after another, are past simple: the door "opened", then Nia PICKED UP the tile.',
              es='Los pasos terminados, uno tras otro, van en pasado simple: la puerta "opened" y luego Nia PICKED UP la pieza.',
              de='Abgeschlossene Schritte nacheinander stehen im Past Simple: die Tür „opened“, dann PICKED Nia die Platte UP.',
              fr='Des étapes terminées, l\'une après l\'autre, sont au prétérit : la porte "opened", puis Nia PICKED UP la tuile.',
              it='Passaggi conclusi, uno dopo l\'altro, vanno al past simple: la porta "opened", poi Nia PICKED UP la tessera.',
              pt='Passos terminados, um a seguir ao outro, vão no past simple: a porta "opened" e depois a Nia PICKED UP a peça.',
              ru='Законченные шаги один за другим — Past Simple: дверь "opened", потом Ния PICKED UP плитку.',
              ar='الخطوات المكتملة، واحدة تلو الأخرى، في الماضي البسيط: الباب "opened"، ثم PICKED UP نيا القطعة.',
              zh='一个接一个完成的步骤用一般过去时：门 "opened"，然后 Nia PICKED UP 石板。',
              ja='次々に終わった手順は過去形：ドアが "opened"、それから Nia はタイルを PICKED UP。'),
    'water': T('Nia is "she": WAS swimming. Her swim was in progress when the torch "flickered".',
               es='Nia es "she": WAS swimming. Estaba nadando cuando la linterna "flickered".',
               de='Nia ist „she“: WAS swimming. Sie schwamm gerade, als die Lampe „flickered“.',
               fr='Nia, c\'est "she" : WAS swimming. Elle nageait quand la lampe "flickered".',
               it='Nia è "she": WAS swimming. Stava nuotando quando la torcia "flickered".',
               pt='A Nia é "she": WAS swimming. Estava a nadar quando a lanterna "flickered".',
               ru='Ния — "she": WAS swimming. Она плыла, когда фонарь "flickered".',
               ar='نيا هي "she": WAS swimming. كانت تسبح عندما "flickered" المصباح.',
               zh='Nia 是 "she"：WAS swimming。手电 "flickered" 时，她正在游。',
               ja='Nia は "she"：WAS swimming。ライトが "flickered" とき、彼女は泳いでいた。'),
    'wheel': T('The wheel was already moving when Nia saw it: WAS turning. "Turned" would mean it started at that moment.',
               es='La rueda ya se movía cuando Nia la vio: WAS turning. "Turned" significaría que empezó en ese momento.',
               de='Das Rad drehte sich schon, als Nia es sah: WAS turning. „Turned“ hieße, es fing in dem Moment an.',
               fr='La roue tournait déjà quand Nia l\'a vue : WAS turning. "Turned" voudrait dire qu\'elle a démarré à ce moment-là.',
               it='La ruota si muoveva già quando Nia l\'ha vista: WAS turning. "Turned" vorrebbe dire che è partita in quel momento.',
               pt='A roda já se mexia quando a Nia a viu: WAS turning. "Turned" quereria dizer que começou nesse momento.',
               ru='Колесо уже двигалось, когда Ния его увидела: WAS turning. "Turned" значило бы, что оно начало вращаться в тот момент.',
               ar='كانت العجلة تتحرك بالفعل عندما رأتها نيا: WAS turning. "Turned" تعني أنها بدأت في تلك اللحظة.',
               zh='Nia 看到轮子时它已经在转：WAS turning。"turned" 意思是它在那一刻才开始转。',
               ja='Nia が見たとき、車輪はもう回っていた：WAS turning。"turned" だとその瞬間に回り始めた意味になる。'),
    'ledge': T('Nia is "she": WAS climbing. The climb was in progress when the stone "fell".',
               es='Nia es "she": WAS climbing. Estaba trepando cuando la piedra "fell".',
               de='Nia ist „she“: WAS climbing. Sie kletterte gerade, als der Stein „fell“.',
               fr='Nia, c\'est "she" : WAS climbing. Elle grimpait quand la pierre "fell".',
               it='Nia è "she": WAS climbing. Stava arrampicando quando la pietra "fell".',
               pt='A Nia é "she": WAS climbing. Estava a trepar quando a pedra "fell".',
               ru='Ния — "she": WAS climbing. Она лезла, когда камень "fell".',
               ar='نيا هي "she": WAS climbing. كانت تتسلق عندما "fell" الحجر.',
               zh='Nia 是 "she"：WAS climbing。石头 "fell" 时，她正在攀爬。',
               ja='Nia は "she"：WAS climbing。石が "fell" とき、彼女は登っていた。'),
    'crane': T('"Once" means one finished movement: past simple JOLTED. "Was jolting" would mean it kept moving.',
               es='"Once" indica un solo movimiento terminado: pasado simple JOLTED. "Was jolting" significaría que seguía moviéndose.',
               de='„Once“ heißt: eine abgeschlossene Bewegung, Past Simple JOLTED. „Was jolting“ hieße, es ruckelte weiter.',
               fr='"Once" signifie un seul mouvement terminé : prétérit JOLTED. "Was jolting" voudrait dire que ça continuait.',
               it='"Once" indica un solo movimento concluso: past simple JOLTED. "Was jolting" vorrebbe dire che continuava a muoversi.',
               pt='"Once" indica um só movimento terminado: past simple JOLTED. "Was jolting" quereria dizer que continuava a mexer-se.',
               ru='"Once" — одно законченное движение: Past Simple JOLTED. "Was jolting" значило бы, что оно продолжало дёргаться.',
               ar='"Once" تعني حركة واحدة مكتملة: الماضي البسيط JOLTED. أما "was jolting" فتعني أنها ظلت تهتز.',
               zh='"once" 表示一次完成的动作：一般过去时 JOLTED。"was jolting" 表示它一直在晃。',
               ja='"once" は一度きりの動き：過去形 JOLTED。"was jolting" だと揺れ続けていた意味になる。'),
    'echo': T('"The villagers" are "they": WERE escaping, the background action while Ivo "held" the gate.',
              es='"The villagers" son "they": WERE escaping, la acción de fondo mientras Ivo "held" la puerta.',
              de='„The villagers“ sind „they“: WERE escaping, die Hintergrundhandlung, während Ivo das Tor „held“.',
              fr='"The villagers", c\'est "they" : WERE escaping, l\'action de fond pendant qu\'Ivo "held" la porte.',
              it='"The villagers" sono "they": WERE escaping, l\'azione di sfondo mentre Ivo "held" il cancello.',
              pt='"The villagers" são "they": WERE escaping, a ação de fundo enquanto o Ivo "held" o portão.',
              ru='"The villagers" — это "they": WERE escaping, фоновое действие, пока Иво "held" ворота.',
              ar='"The villagers" هم "they": WERE escaping، الفعل الخلفي بينما "held" إيفو البوابة.',
              zh='"The villagers" 是 "they"：WERE escaping，是 Ivo "held" 住大门时的背景动作。',
              ja='"The villagers" は "they"：WERE escaping。Ivo が門を "held" 間の背景の動作。'),
    'trap': T('One block hits the floor once: past simple FELL. "Was reaching" is the longer action it interrupted.',
              es='Un bloque cae al suelo una vez: pasado simple FELL. "Was reaching" es la acción más larga que interrumpe.',
              de='Ein Block schlägt einmal auf: Past Simple FELL. „Was reaching“ ist die längere Handlung, die er unterbricht.',
              fr='Un bloc touche le sol une fois : prétérit FELL. "Was reaching" est l\'action plus longue qu\'il interrompt.',
              it='Un blocco colpisce il pavimento una volta: past simple FELL. "Was reaching" è l\'azione più lunga che interrompe.',
              pt='Um bloco bate no chão uma vez: past simple FELL. "Was reaching" é a ação mais longa que ele interrompe.',
              ru='Один блок падает на пол один раз: Past Simple FELL. "Was reaching" — более долгое действие, которое он прервал.',
              ar='تسقط كتلة واحدة على الأرض مرة واحدة: الماضي البسيط FELL. و"was reaching" هو الفعل الأطول الذي قاطعته.',
              zh='一块石头落地一次：一般过去时 FELL。"was reaching" 是被它打断的较长动作。',
              ja='ブロックが一度床に落ちる：過去形 FELL。"was reaching" はそれが中断した長い動作。'),
    'journal': T('Ivo finished closing the gate, so the sentence is past simple: I SHUT the gate. "I was shutting" leaves it unfinished.',
                 es='Ivo terminó de cerrar la puerta, así que la frase va en pasado simple: I SHUT the gate. "I was shutting" la deja sin terminar.',
                 de='Ivo hat das Tor ganz geschlossen, also Past Simple: I SHUT the gate. „I was shutting“ lässt es offen, ob er fertig wurde.',
                 fr='Ivo a fini de fermer la porte, donc la phrase est au prétérit : I SHUT the gate. "I was shutting" la laisse inachevée.',
                 it='Ivo ha finito di chiudere il cancello, quindi la frase è al past simple: I SHUT the gate. "I was shutting" la lascia incompiuta.',
                 pt='O Ivo acabou de fechar o portão, por isso a frase está no past simple: I SHUT the gate. "I was shutting" deixa-a por acabar.',
                 ru='Иво закрыл ворота до конца, поэтому Past Simple: I SHUT the gate. "I was shutting" оставляет действие незаконченным.',
                 ar='أنهى إيفو إغلاق البوابة، لذا الجملة في الماضي البسيط: I SHUT the gate. أما "I was shutting" فتتركها غير مكتملة.',
                 zh='Ivo 关完了大门，所以用一般过去时：I SHUT the gate。"I was shutting" 表示还没关完。',
                 ja='Ivo は門を閉め終えたので過去形：I SHUT the gate。"I was shutting" だと終わっていない。'),
    'engine': T('"Both pumps" are "they": WERE working. They were already running when Vale "reached" for the sun.',
                es='"Both pumps" son "they": WERE working. Ya funcionaban cuando Vale "reached" el sol.',
                de='„Both pumps“ sind „they“: WERE working. Sie liefen schon, als Vale nach der Sonne „reached“.',
                fr='"Both pumps", c\'est "they" : WERE working. Elles tournaient déjà quand Vale "reached" vers le soleil.',
                it='"Both pumps" sono "they": WERE working. Funzionavano già quando Vale "reached" il sole.',
                pt='"Both pumps" são "they": WERE working. Já estavam a funcionar quando o Vale "reached" o sol.',
                ru='"Both pumps" — это "they": WERE working. Они уже работали, когда Вейл "reached" к солнцу.',
                ar='"Both pumps" هما "they": WERE working. كانتا تعملان بالفعل عندما "reached" فيل نحو الشمس.',
                zh='"Both pumps" 是 "they"：WERE working。Vale "reached" 太阳时，它们已经在运转。',
                ja='"Both pumps" は "they"：WERE working。Vale が太陽に "reached" とき、もう動いていた。'),
    'villain': T('The pumps stop all at once: past simple STOPPED. "Was lifting" is the action in progress around it.',
                 es='Las bombas se paran de golpe: pasado simple STOPPED. "Was lifting" es la acción en curso alrededor.',
                 de='Die Pumpen stoppen auf einen Schlag: Past Simple STOPPED. „Was lifting“ ist die laufende Handlung drumherum.',
                 fr='Les pompes s\'arrêtent d\'un coup : prétérit STOPPED. "Was lifting" est l\'action en cours autour.',
                 it='Le pompe si fermano di colpo: past simple STOPPED. "Was lifting" è l\'azione in corso intorno.',
                 pt='As bombas param de uma vez: past simple STOPPED. "Was lifting" é a ação a decorrer à volta.',
                 ru='Насосы останавливаются разом: Past Simple STOPPED. "Was lifting" — действие, которое шло вокруг.',
                 ar='تتوقف المضخات دفعة واحدة: الماضي البسيط STOPPED. و"was lifting" هو الفعل المستمر حوله.',
                 zh='水泵一下子停了：一般过去时 STOPPED。"was lifting" 是周围正在进行的动作。',
                 ja='ポンプは一斉に止まる：過去形 STOPPED。"was lifting" はその周りで進行中の動作。'),
    'rescue': T('A question about an action in progress: WHAT + WAS + subject + verb-ING? "What did Vale do" asks about a finished action.',
                es='Pregunta por una acción en curso: WHAT + WAS + sujeto + verbo-ING? "What did Vale do" pregunta por una acción terminada.',
                de='Frage nach einer laufenden Handlung: WHAT + WAS + Subjekt + Verb-ING? „What did Vale do“ fragt nach einer abgeschlossenen.',
                fr='Question sur une action en cours : WHAT + WAS + sujet + verbe-ING ? "What did Vale do" porte sur une action terminée.',
                it='Domanda su un\'azione in corso: WHAT + WAS + soggetto + verbo-ING? "What did Vale do" chiede di un\'azione conclusa.',
                pt='Pergunta sobre uma ação a decorrer: WHAT + WAS + sujeito + verbo-ING? "What did Vale do" pergunta por uma ação terminada.',
                ru='Вопрос о действии в процессе: WHAT + WAS + подлежащее + глагол-ING? "What did Vale do" спрашивает о законченном действии.',
                ar='سؤال عن فعل مستمر: WHAT + WAS + الفاعل + فعل-ING؟ أما "What did Vale do" فتسأل عن فعل مكتمل.',
                zh='问正在进行的动作：WHAT + WAS + 主语 + 动词-ING？"What did Vale do" 问的是完成的动作。',
                ja='進行中の動作を尋ねる：WHAT + WAS + 主語 + 動詞-ING？"What did Vale do" は終わった動作を尋ねる。'),
    'rope': T('Two finished actions, one after the other: GRABBED, then "pulled". Both are past simple.',
              es='Dos acciones terminadas, una tras otra: GRABBED y luego "pulled". Las dos en pasado simple.',
              de='Zwei abgeschlossene Handlungen nacheinander: GRABBED, dann „pulled“. Beide im Past Simple.',
              fr='Deux actions terminées, l\'une après l\'autre : GRABBED, puis "pulled". Les deux au prétérit.',
              it='Due azioni concluse, una dopo l\'altra: GRABBED, poi "pulled". Entrambe al past simple.',
              pt='Duas ações terminadas, uma a seguir à outra: GRABBED e depois "pulled". Ambas no past simple.',
              ru='Два законченных действия одно за другим: GRABBED, потом "pulled". Оба в Past Simple.',
              ar='فعلان مكتملان، واحد بعد الآخر: GRABBED ثم "pulled". كلاهما في الماضي البسيط.',
              zh='两个先后完成的动作：GRABBED，然后 "pulled"。都用一般过去时。',
              ja='次々に終わった二つの動作：GRABBED、それから "pulled"。どちらも過去形。'),
    'record': T('The sudden finished event is past simple: Vale DROPPED the sun. Nia\'s jump is the background: "was jumping".',
                es='El hecho repentino y terminado va en pasado simple: Vale DROPPED the sun. El salto de Nia es el fondo: "was jumping".',
                de='Das plötzliche, abgeschlossene Ereignis steht im Past Simple: Vale DROPPED the sun. Nias Sprung ist der Hintergrund: „was jumping“.',
                fr='L\'événement soudain et terminé est au prétérit : Vale DROPPED the sun. Le saut de Nia est l\'arrière-plan : "was jumping".',
                it='L\'evento improvviso e concluso è al past simple: Vale DROPPED the sun. Il salto di Nia è lo sfondo: "was jumping".',
                pt='O acontecimento súbito e terminado está no past simple: Vale DROPPED the sun. O salto da Nia é o fundo: "was jumping".',
                ru='Внезапное законченное событие — Past Simple: Vale DROPPED the sun. Прыжок Нии — фон: "was jumping".',
                ar='الحدث المفاجئ المكتمل في الماضي البسيط: Vale DROPPED the sun. وقفزة نيا هي الخلفية: "was jumping".',
                zh='突然完成的事件用一般过去时：Vale DROPPED the sun。Nia 的跳跃是背景："was jumping"。',
                ja='突然終わった出来事は過去形：Vale DROPPED the sun。Nia のジャンプは背景："was jumping"。'),
    'flood': T('"The water" is "it": WAS rising, in progress at the same time as "was listening".',
               es='"The water" es "it": WAS rising, en curso al mismo tiempo que "was listening".',
               de='„The water“ ist „it“: WAS rising, gleichzeitig mit „was listening“ im Verlauf.',
               fr='"The water", c\'est "it" : WAS rising, en cours en même temps que "was listening".',
               it='"The water" è "it": WAS rising, in corso nello stesso momento di "was listening".',
               pt='"The water" é "it": WAS rising, a decorrer ao mesmo tempo que "was listening".',
               ru='"The water" — это "it": WAS rising, одновременно с "was listening".',
               ar='"The water" هو "it": WAS rising، مستمر في الوقت نفسه مع "was listening".',
               zh='"The water" 是 "it"：WAS rising，与 "was listening" 同时进行。',
               ja='"The water" は "it"：WAS rising。"was listening" と同時に進行中。'),
    'align': T('The next finished step is past simple: she "fitted" the tile, then she TURNED the dial.',
               es='El siguiente paso terminado va en pasado simple: "fitted" la pieza y luego TURNED el dial.',
               de='Der nächste abgeschlossene Schritt steht im Past Simple: Sie „fitted“ die Platte, dann TURNED sie die Scheibe.',
               fr='L\'étape terminée suivante est au prétérit : elle "fitted" la tuile, puis elle TURNED le cadran.',
               it='Il passaggio concluso successivo è al past simple: "fitted" la tessera, poi TURNED la manopola.',
               pt='O passo terminado seguinte está no past simple: "fitted" a peça e depois TURNED o mostrador.',
               ru='Следующий законченный шаг — Past Simple: она "fitted" плитку, потом TURNED диск.',
               ar='الخطوة المكتملة التالية في الماضي البسيط: "fitted" القطعة، ثم TURNED القرص.',
               zh='下一个完成的步骤用一般过去时：她 "fitted" 石板，然后 TURNED 转盘。',
               ja='次に終えた手順は過去形：タイルを "fitted"、それからダイヤルを TURNED。'),
    'seal': T('The negative is WERE + NOT + verb-ING. "The gears" are "they": WEREN\'T turning.',
              es='La negación es WERE + NOT + verbo-ING. "The gears" son "they": WEREN\'T turning.',
              de='Die Verneinung ist WERE + NOT + Verb-ING. „The gears“ sind „they“: WEREN\'T turning.',
              fr='La négation, c\'est WERE + NOT + verbe-ING. "The gears", c\'est "they" : WEREN\'T turning.',
              it='La negazione è WERE + NOT + verbo-ING. "The gears" sono "they": WEREN\'T turning.',
              pt='A negação é WERE + NOT + verbo-ING. "The gears" são "they": WEREN\'T turning.',
              ru='Отрицание: WERE + NOT + глагол-ING. "The gears" — это "they": WEREN\'T turning.',
              ar='النفي هو WERE + NOT + فعل-ING. "The gears" هي "they": WEREN\'T turning.',
              zh='否定式是 WERE + NOT + 动词-ING。"The gears" 是 "they"：WEREN\'T turning。',
              ja='否定は WERE + NOT + 動詞-ING。"The gears" は "they"：WEREN\'T turning。'),
    'dawn': T('Nia\'s rest was already in progress when the helicopter "landed": WAS resting.',
              es='Nia ya estaba descansando cuando el helicóptero "landed": WAS resting.',
              de='Nia ruhte sich schon aus, als der Hubschrauber „landed“: WAS resting.',
              fr='Nia se reposait déjà quand l\'hélicoptère "landed" : WAS resting.',
              it='Nia stava già riposando quando l\'elicottero "landed": WAS resting.',
              pt='A Nia já estava a descansar quando o helicóptero "landed": WAS resting.',
              ru='Ния уже отдыхала, когда вертолёт "landed": WAS resting.',
              ar='كانت نيا تستريح بالفعل عندما "landed" المروحية: WAS resting.',
              zh='直升机 "landed" 时，Nia 已经在休息：WAS resting。',
              ja='ヘリが "landed" とき、Nia はもう休んでいた：WAS resting。'),
}


# ── the export's briefing note repeated the cover's three chips and pushed the
# BEGIN button below the fold in German and Spanish; this keeps the advice and
# the win condition.
NOTE = T('Read the scene and the clue: the meaning decides the tense, not just "when" or "while". Win with all four sun tiles and 65 points.',
         es='Lee la escena y la pista: el significado decide el tiempo verbal, no solo "when" o "while". Gana con las cuatro piezas solares y 65 puntos.',
         de='Lies Szene und Hinweis: Die Bedeutung entscheidet über die Zeitform, nicht nur „when“ oder „while“. Gewinne mit allen vier Sonnensteinen und 65 Punkten.',
         fr='Lis la scène et l\'indice : le sens décide du temps, pas seulement "when" ou "while". Gagne avec les quatre tuiles solaires et 65 points.',
         it='Leggi la scena e l\'indizio: è il significato a decidere il tempo, non solo "when" o "while". Vinci con tutte e quattro le tessere solari e 65 punti.',
         pt='Lê a cena e a pista: é o significado que decide o tempo verbal, não só "when" ou "while". Ganha com as quatro peças solares e 65 pontos.',
         ru='Читай сцену и подсказку: время выбирает смысл, а не только "when" или "while". Победа — все четыре солнечные плитки и 65 очков.',
         ar='اقرأ المشهد والدليل: المعنى هو ما يحدد الزمن، لا "when" أو "while" وحدهما. تفوز بقطع الشمس الأربع و65 نقطة.',
         zh='读场景和提示：决定时态的是意思，而不只是 "when" 或 "while"。集齐四块太阳石板并拿到 65 分即可获胜。',
         ja='場面とヒントを読もう：時制を決めるのは意味であって、"when" や "while" だけではない。太陽のタイル四枚と 65 ポイントで勝利。')


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
            'kind': 'rules', 'img': '13_engine.webp',
            'k': BRIEFING_KICKER, 'title': T(b['title']),
            'rules': cards(),
            'note': NOTE, 'button': T(b['button']),
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

    for sid, (old, new) in OPTION_FIX.items():
        opts = [o['en'] for o in scenes[sid]['opts']]
        assert old in opts and opts[scenes[sid]['answer']] != old, sid
        scenes[sid]['opts'] = [T(new if o == old else o) for o in opts]
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
        'title': 'Welcome to the Jungle — Past Continuous vs Past Simple Voxel Jungle RPG (A2-B1)',
        'description': 'An interactive A2-B1 English lesson from Forbes English: '
                       'Welcome to the Jungle — Past Continuous vs Past Simple Voxel Jungle RPG (A2-B1).',
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
    rpg.assemble(rpg.apply_translations(build(), os.path.join(BASE, 'translations')))
