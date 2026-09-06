#!/usr/bin/env python3
"""The Lost Yellow Road — Past Continuous voxel-Oz RPG (A1–A2).

    python3 lesson-template/build/build_lost_yellow_road.py

Rebuilds block-camp/lost-yellow-road-rpg.html from
lesson-template/build/rpg/lost-yellow-road/data.json (the text of the
standalone export Innes sent on 2026-09-05, pulled out by
rpg/extract_standalone.py) plus everything below that the export did not
have: the hotspot on each picture, a rules briefing before the first
question, a one-line explanation under every answer, and the German/Spanish
for the chapter kickers, which the export left in English.

The export was a light, self-contained "Sherpa Yellow" page: a cream copy
column over the picture, story text at 15–17px, no hotspots. Innes's brief
was "text should be bigger and pop up when a glowing object is clicked",
i.e. bring it to the Blocula standard — see rpg/README.md.

Pictures: block-camp/lost-yellow-road-rpg/NN_name.webp, 1536×1024, as
exported. The cover doubles as the two success endings and the rules
briefing borrows the crossroads plate, exactly as the export did.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(open(os.path.join(HERE, 'rpg', 'lost-yellow-road', 'data.json'), encoding='utf-8'))
LANGS = ['es', 'de']

# ── hotspots: [cx, cy, w, h] in % of the 1536×1024 picture, then panel side,
# vertical anchor, optional panel width %. Picked from a gridded contact
# sheet (rpg/README.md §3) — the object is the one the clue talks about.
HOT = {
    'cover':       ([67, 20, 14, 22], 'left',   'center'),   # Emerald City on the horizon
    'rules':       ([70, 68, 14, 18], 'left',   'center', 56),  # the yellow road setting off; wide, five cards
    'storm':       ([36, 30, 14, 40], 'right',  'center'),   # the funnel
    'cellar':      ([58, 76,  9, 16], 'left',   'center'),   # Toto on the steps
    'house':       ([23, 33, 12, 14], 'right',  'center'),   # Dorothy at the window
    'aunt_em':     ([68, 62,  6,  9], 'left',   'center'),   # the lantern
    'route_one':   ([47, 76, 12, 26], 'center', 'top'),      # Dorothy at the fork
    'scarecrow':   ([66, 20,  8, 12], 'left',   'center'),   # the waving straw hand
    'munchkins':   ([46, 62, 20, 16], 'right',  'center', 38),  # the dancers
    'tin':         ([16, 70, 10, 18], 'right',  'center'),   # the axe on the ground
    'oil':         ([66, 52,  8, 12], 'left',   'center'),   # the oil can
    'tracks':      ([60, 78, 18, 16], 'right',  'top'),      # the paw marks
    'route_two':   ([64, 58, 10, 14], 'center', 'top'),      # where the road divides
    'lion':        ([68, 38, 10, 20], 'left',   'center'),   # the Lion behind the tree
    'poppies':     ([17, 55, 10, 14], 'right',  'center'),   # Dorothy asleep
    'mice':        ([70, 72, 12, 18], 'left',   'center'),   # the mouse queen's cart
    'witch':       ([31, 70, 22, 34], 'right',  'center'),   # the golden sphere
    'monkeys':     ([80, 22, 18, 26], 'left',   'top'),      # the winged monkey
    'bridge':      ([35, 72,  9, 14], 'right',  'center'),   # the glowing tile
    'route_three': ([14, 40, 10, 18], 'center', 'top'),      # the tower door
    'tower':       ([66, 22, 22, 22], 'left',   'center'),   # the guarded room
    'courtyard':   ([30, 76, 14, 14], 'right',  'center'),   # the axe on the rope
    'finale':      ([60, 52, 10, 14], 'left',   'center'),   # the bucket
    'end_master':  ([67, 20, 14, 22], 'left',   'center'),
    'end_complete':([67, 20, 14, 22], 'left',   'center'),
    'end_missing': ([50, 75, 24, 20], 'right',  'top'),      # the road breaking up
    'end_failed':  ([50, 75, 24, 20], 'right',  'top'),
}

# The export left the chapter kickers untranslated.
KICKER = {
    'CHAPTER 1 · KANSAS':            ('CAPÍTULO 1 · KANSAS', 'KAPITEL 1 · KANSAS'),
    'CHAPTER 1 · THE CELLAR':        ('CAPÍTULO 1 · EL SÓTANO', 'KAPITEL 1 · DER KELLER'),
    'CHAPTER 1 · THE CYCLONE':       ('CAPÍTULO 1 · EL CICLÓN', 'KAPITEL 1 · DER WIRBELSTURM'),
    'CHAPTER 1 · FIRST TILE':        ('CAPÍTULO 1 · PRIMERA BALDOSA', 'KAPITEL 1 · ERSTER WEGSTEIN'),
    'ROUTE CHOICE 1':                ('ELECCIÓN DE RUTA 1', 'ROUTENWAHL 1'),
    'ROUTE · CORNFIELD':             ('RUTA · EL MAIZAL', 'ROUTE · DAS MAISFELD'),
    'ROUTE · MUNCHKIN VILLAGE':      ('RUTA · LA ALDEA MUNCHKIN', 'ROUTE · DAS MUNCHKIN-DORF'),
    'CHAPTER 2 · YELLOW FOREST':     ('CAPÍTULO 2 · EL BOSQUE AMARILLO', 'KAPITEL 2 · DER GELBE WALD'),
    'CHAPTER 2 · SECOND TILE':       ('CAPÍTULO 2 · SEGUNDA BALDOSA', 'KAPITEL 2 · ZWEITER WEGSTEIN'),
    'CHAPTER 2 · FRESH TRACKS':      ('CAPÍTULO 2 · HUELLAS FRESCAS', 'KAPITEL 2 · FRISCHE SPUREN'),
    'ROUTE CHOICE 2':                ('ELECCIÓN DE RUTA 2', 'ROUTENWAHL 2'),
    'ROUTE · LION FOREST':           ('RUTA · EL BOSQUE DEL LEÓN', 'ROUTE · DER LÖWENWALD'),
    'ROUTE · POPPY FIELD':           ('RUTA · EL CAMPO DE AMAPOLAS', 'ROUTE · DAS MOHNFELD'),
    'CHAPTER 3 · FIELD MICE':        ('CAPÍTULO 3 · LOS RATONES DEL CAMPO', 'KAPITEL 3 · DIE FELDMÄUSE'),
    'CHAPTER 3 · THE WITCH':         ('CAPÍTULO 3 · LA BRUJA', 'KAPITEL 3 · DIE HEXE'),
    'CHAPTER 3 · ABOVE THE BRIDGE':  ('CAPÍTULO 3 · SOBRE EL PUENTE', 'KAPITEL 3 · ÜBER DER BRÜCKE'),
    'CHAPTER 3 · THIRD TILE':        ('CAPÍTULO 3 · TERCERA BALDOSA', 'KAPITEL 3 · DRITTER WEGSTEIN'),
    'ROUTE CHOICE 3':                ('ELECCIÓN DE RUTA 3', 'ROUTENWAHL 3'),
    'ROUTE · CASTLE TOWER':          ('RUTA · LA TORRE DEL CASTILLO', 'ROUTE · DER SCHLOSSTURM'),
    'ROUTE · FOURTH TILE':           ('RUTA · CUARTA BALDOSA', 'ROUTE · VIERTER WEGSTEIN'),
    'FINAL CHALLENGE':               ('DESAFÍO FINAL', 'LETZTE PRÜFUNG'),
}

# One line under every answer, right or wrong: the rule the item tests.
FB = {
    'storm':     ('WAS/WERE + verb-ING for an action in progress at a past moment. "The wind" is singular, so it takes WAS.',
                  'WAS/WERE + verbo-ING para una acción en curso en un momento del pasado. "The wind" es singular: WAS.',
                  'WAS/WERE + Verb-ING für eine Handlung, die in einem Moment der Vergangenheit gerade ablief. „The wind“ ist Singular: WAS.'),
    'cellar':    ('Dorothy and Toto are "they", so the verb is WERE + running.',
                  'Dorothy y Toto son "they": el verbo es WERE + running.',
                  'Dorothy und Toto sind „they“, also WERE + running.'),
    'house':     ('One farmhouse: WAS rising. "Rose ... now" mixes the past simple with a present time word.',
                  'Una sola casa: WAS rising. "Rose ... now" mezcla el pasado simple con una palabra de presente.',
                  'Ein Haus: WAS rising. „Rose … now“ mischt das Past Simple mit einem Wort für die Gegenwart.'),
    'aunt_em':   ('Two actions at the same time: "while" + past continuous. Aunt Em is "she", so WAS searching.',
                  'Dos acciones a la vez: "while" + pasado continuo. Aunt Em es "she": WAS searching.',
                  'Zwei Handlungen zur gleichen Zeit: „while“ + Past Continuous. Aunt Em ist „she“: WAS searching.'),
    'scarecrow': ('The Scarecrow is "he": HE WAS waving. The action was in progress when Dorothy looked.',
                  'El Espantapájaros es "he": HE WAS waving. La acción estaba en curso cuando Dorothy miró.',
                  'Die Vogelscheuche ist „he“: HE WAS waving. Die Handlung lief gerade, als Dorothy hinsah.'),
    'munchkins': ('The villagers are "they": THEY WERE dancing. "They danced" is a finished action, not one in progress.',
                  'Los aldeanos son "they": THEY WERE dancing. "They danced" es una acción terminada, no en curso.',
                  'Die Dorfbewohner sind „they“: THEY WERE dancing. „They danced“ ist abgeschlossen, nicht im Verlauf.'),
    'tin':       ('The negative is WAS/WERE + NOT + verb-ING. The Tin Woodman is "he": he WASN\'T moving.',
                  'La negación es WAS/WERE + NOT + verbo-ING. El Hombre de Hojalata es "he": he WASN\'T moving.',
                  'Die Verneinung ist WAS/WERE + NOT + Verb-ING. Der Blechmann ist „he“: he WASN\'T moving.'),
    'oil':       ('Two actions in progress at the same time: past continuous on BOTH sides of "while".',
                  'Dos acciones en curso al mismo tiempo: pasado continuo a AMBOS lados de "while".',
                  'Zwei gleichzeitig laufende Handlungen: Past Continuous auf BEIDEN Seiten von „while“.'),
    'tracks':    ('A question about the subject: WHAT + WAS + verb-ING? No "did" and no extra word order.',
                  'Una pregunta sobre el sujeto: WHAT + WAS + verbo-ING? Sin "did" y sin cambiar el orden.',
                  'Eine Frage nach dem Subjekt: WHAT + WAS + Verb-ING? Kein „did“, keine andere Wortstellung.'),
    'lion':      ('The Lion is "he": WAS roaring. "While he was hiding" tells you both actions were in progress.',
                  'El León es "he": WAS roaring. "While he was hiding" indica que las dos acciones estaban en curso.',
                  'Der Löwe ist „he“: WAS roaring. „While he was hiding“ zeigt: beide Handlungen liefen gerade.'),
    'poppies':   ('Dorothy and the Lion are "they": THEY WERE sleeping. "Right now" is present time, not past.',
                  'Dorothy y el León son "they": THEY WERE sleeping. "Right now" es tiempo presente, no pasado.',
                  'Dorothy und der Löwe sind „they“: THEY WERE sleeping. „Right now“ ist Gegenwart, nicht Vergangenheit.'),
    'mice':      ('The long background action is past continuous; the new event after "when" is past simple.',
                  'La acción larga de fondo va en pasado continuo; el evento nuevo después de "when" va en pasado simple.',
                  'Die lange Hintergrundhandlung steht im Past Continuous, das neue Ereignis nach „when“ im Past Simple.'),
    'witch':     ('The Witch is "she": SHE WAS watching. "Yesterday" + past simple describes a finished action, not the moment.',
                  'La Bruja es "she": SHE WAS watching. "Yesterday" + pasado simple describe una acción terminada, no el momento.',
                  'Die Hexe ist „she“: SHE WAS watching. „Yesterday“ + Past Simple beschreibt eine abgeschlossene Handlung, nicht den Moment.'),
    'monkeys':   ('The monkeys are "they": WERE flying — an action in progress while the group was crossing.',
                  'Los monos son "they": WERE flying, una acción en curso mientras el grupo cruzaba.',
                  'Die Affen sind „they“: WERE flying – eine laufende Handlung, während die Gruppe die Brücke überquerte.'),
    'bridge':    ('Word order: SUBJECT + WAS/WERE + verb-ING + object. "They were crossing the bridge."',
                  'Orden de palabras: SUJETO + WAS/WERE + verbo-ING + objeto. "They were crossing the bridge."',
                  'Wortstellung: SUBJEKT + WAS/WERE + Verb-ING + Objekt. „They were crossing the bridge.“'),
    'tower':     ('A yes/no question: WAS/WERE + subject + verb-ING? Dorothy is "she", so WAS Dorothy climbing?',
                  'Una pregunta de sí/no: WAS/WERE + sujeto + verbo-ING? Dorothy es "she": WAS Dorothy climbing?',
                  'Eine Ja/Nein-Frage: WAS/WERE + Subjekt + Verb-ING? Dorothy ist „she“: WAS Dorothy climbing?'),
    'courtyard': ('The Tin Woodman is "he": HE WAS cutting. The action was in progress when Toto found the tile.',
                  'El Hombre de Hojalata es "he": HE WAS cutting. La acción estaba en curso cuando Toto encontró la baldosa.',
                  'Der Blechmann ist „he“: HE WAS cutting. Die Handlung lief gerade, als Toto den Wegstein fand.'),
    'finale':    ('The threat was already happening (past continuous); the water was a sudden new event (past simple after "when").',
                  'La amenaza ya estaba ocurriendo (pasado continuo); el agua fue un evento nuevo y repentino (pasado simple tras "when").',
                  'Die Bedrohung lief bereits (Past Continuous); das Wasser war ein plötzliches neues Ereignis (Past Simple nach „when“).'),
}

RULES = {
    'kind': 'rules', 'img': '06_choice1_crossroads.webp',
    'k':     {'en': 'BEFORE THE ROAD · HOW THE GRAMMAR WORKS', 'es': 'ANTES DEL CAMINO · CÓMO FUNCIONA LA GRAMÁTICA', 'de': 'VOR DEM WEG · SO FUNKTIONIERT DIE GRAMMATIK'},
    'title': {'en': 'READ THE SIGNS', 'es': 'LEE LAS SEÑALES', 'de': 'LIES DIE ZEICHEN'},
    'story': {'en': 'Every question asks what was happening at one moment in the past. Look at the picture, find the action in progress, then choose the form that says so.',
              'es': 'Cada pregunta pide qué estaba pasando en un momento del pasado. Mira la imagen, encuentra la acción en curso y elige la forma que lo dice.',
              'de': 'Jede Frage fragt, was in einem Moment der Vergangenheit gerade geschah. Sieh dir das Bild an, finde die laufende Handlung und wähle die passende Form.'},
    'rules': [
        {'name': {'en': 'FORM · WAS / WERE + VERB-ING', 'es': 'FORMA · WAS / WERE + VERBO-ING', 'de': 'FORM · WAS / WERE + VERB-ING'},
         'form': {'en': 'I / he / she / it WAS running · you / we / they WERE running', 'es': 'I / he / she / it WAS running · you / we / they WERE running', 'de': 'I / he / she / it WAS running · you / we / they WERE running'}},
        {'name': {'en': 'IN PROGRESS · AT A PAST MOMENT', 'es': 'EN CURSO · EN UN MOMENTO DEL PASADO', 'de': 'IM VERLAUF · IN EINEM MOMENT DER VERGANGENHEIT'},
         'form': {'en': 'At that moment, the house was rising into the sky.', 'es': 'En ese momento, la casa se estaba elevando hacia el cielo.', 'de': 'In diesem Moment stieg das Haus gerade in den Himmel.'}},
        {'name': {'en': 'INTERRUPTED · WHEN + PAST SIMPLE', 'es': 'INTERRUMPIDA · WHEN + PASADO SIMPLE', 'de': 'UNTERBROCHEN · WHEN + PAST SIMPLE'},
         'form': {'en': 'They were sleeping WHEN the mice arrived.', 'es': 'Estaban durmiendo CUANDO llegaron los ratones.', 'de': 'Sie schliefen gerade, ALS die Mäuse ankamen.'}},
        {'name': {'en': 'TWO ACTIONS · WHILE', 'es': 'DOS ACCIONES · WHILE', 'de': 'ZWEI HANDLUNGEN · WHILE'},
         'form': {'en': 'Dorothy was oiling him WHILE Toto was watching.', 'es': 'Dorothy lo estaba engrasando MIENTRAS Toto miraba.', 'de': 'Dorothy ölte ihn, WÄHREND Toto zusah.'}},
        {'name': {'en': 'QUESTIONS AND NEGATIVES', 'es': 'PREGUNTAS Y NEGACIONES', 'de': 'FRAGEN UND VERNEINUNGEN'},
         'form': {'en': 'WAS Dorothy climbing the tower? · The Woodman WASN\'T moving.', 'es': '¿Estaba Dorothy subiendo la torre? · El Hombre de Hojalata NO se estaba moviendo.', 'de': 'Kletterte Dorothy gerade den Turm hinauf? · Der Blechmann bewegte sich NICHT.'}},
    ],
    'note': {'en': 'WAS with I, he, she, it. WERE with you, we, they. The verb always ends in -ING.',
             'es': 'WAS con I, he, she, it. WERE con you, we, they. El verbo siempre termina en -ING.',
             'de': 'WAS bei I, he, she, it. WERE bei you, we, they. Das Verb endet immer auf -ING.'},
    'next': 'storm',
}


def T(en, es=None, de=None):
    return {'en': en, 'es': es if es is not None else en, 'de': de if de is not None else en}


def place(sid, scene):
    hot, pos, v = HOT[sid][:3]
    scene.update({'hot': hot, 'pos': pos, 'v': v})
    if len(HOT[sid]) > 3:
        scene['width'] = HOT[sid][3]
    return scene


def build():
    c, cl = DATA['cover'], DATA['cover']['local']
    scenes = {
        'cover': place('cover', {
            'kind': 'intro', 'img': c['image'],
            'k': T(c['eyebrow'], cl['es']['eyebrow'], cl['de']['eyebrow']),
            'title': T(c['title'], cl['es']['title'], cl['de']['title']),
            'story': T(c['lead'], cl['es']['lead'], cl['de']['lead']),
            'rules': [T(r, cl['es']['rules'][i], cl['de']['rules'][i]) for i, r in enumerate(c['rules'])],
            'start': T(c['start'], cl['es']['start'], cl['de']['start']),
            'small': T(c['small'], cl['es']['small'], cl['de']['small']),
            'next': 'rules'}),
        'rules': place('rules', dict(RULES)),
    }
    for sid, s in DATA['scenes'].items():
        l = s['local']
        es, de = KICKER[s['act']]
        base = {'img': s['image'], 'k': T(s['act'], es, de),
                'title': T(s['title'], l['es']['title'], l['de']['title']),
                'story': T(s['story'], l['es']['story'], l['de']['story'])}
        if 'choices' in s:
            base['kind'] = 'choice'
            base['routes'] = [{'name': T(ch['label'], l['es']['choices'][i]['label'], l['de']['choices'][i]['label']),
                               'desc': T(ch['note'], l['es']['choices'][i]['note'], l['de']['choices'][i]['note']),
                               'route': ch['route'], 'target': ch['next']} for i, ch in enumerate(s['choices'])]
        else:
            base['kind'] = 'question'
            base['clue'] = T(s['clue'], l['es']['clue'], l['de']['clue'])
            base['prompt'] = T(s['prompt'], l['es']['prompt'], l['de']['prompt'])
            base['opts'] = [T(a['text'], l['es']['answers'][i], l['de']['answers'][i]) for i, a in enumerate(s['answers'])]
            base['answer'] = next(i for i, a in enumerate(s['answers']) if a.get('correct'))
            base['points'] = s.get('points', 5)
            if s.get('relic'):
                base['relic'] = True
            if s.get('finalChoice'):
                base['final'] = True
            base['fb'] = T(*FB[sid])
            # the export sent wrong answers down the same road as right ones;
            # the chance counter is the penalty, not a detour
            assert s['correctNext'] == s['wrongNext'], sid
            base['next'] = 'resolve' if s['correctNext'] == 'ending' else s['correctNext']
        scenes[sid] = place(sid, base)
    for key, e in DATA['endings'].items():
        sid = 'end_' + key
        el = e['local']
        scenes[sid] = place(sid, {
            'kind': 'ending', 'img': e['image'], 'success': e['success'],
            'k': T(e['label'], el['es']['label'], el['de']['label']),
            'title': T(e['title'], el['es']['title'], el['de']['title']),
            'story': T(e['text'], el['es']['text'], el['de']['text'])})

    u = DATA['ui']
    labels = {
        'points':     T('POINTS', u['es']['points'], u['de']['points']),
        'tiles':      T('ROAD TILES', u['es']['tiles'], u['de']['tiles']),
        'chances':    T('CHANCES', u['es']['chances'], u['de']['chances']),
        'visual':     T('VISUAL CLUE', u['es']['evidence'], u['de']['evidence']),
        'continue':   T('CONTINUE', u['es']['continue'], u['de']['continue']),
        'restart':    T('PLAY AGAIN', u['es']['playAgain'], u['de']['playAgain']),
        'finalScore': T('FINAL SCORE', u['es']['finalScore'], u['de']['finalScore']),
        'relic':      T('TILE RECOVERED · +{p} POINTS', u['es']['recovered'] + ' · +{p} ' + u['es']['points'], u['de']['recovered'] + ' · +{p} ' + u['de']['points']),
        'begin':      T('FOLLOW THE YELLOW ROAD', cl['es']['start'], cl['de']['start']),
    }

    spec = {
        'file': 'block-camp/lost-yellow-road-rpg.html',
        'img_dir': 'block-camp/lost-yellow-road-rpg',
        'title': 'The Lost Yellow Road — Past Continuous Voxel Oz RPG (A1-A2)',
        'description': 'An interactive A1-A2 English lesson from Forbes English: The Lost Yellow Road — Past Continuous Voxel Oz RPG (A1-A2).',
        'langs': LANGS,
        'accent': '#F1D779',        # camp 4, Past Continuous, on the Block Camp route map
        'accent_ink': '#1a1200', 'deep': '#2a1c00', 'panel': 'rgba(22,15,3,.88)',
        'labels': labels,
        'start': 'cover', 'scenes': scenes,
        'endings': {'master': 'end_master', 'complete': 'end_complete', 'missing': 'end_missing', 'failed': 'end_failed'},
        'max': 75, 'points': 5, 'tiles': 4, 'chances': 3, 'complete_score': 65,
    }
    return spec


if __name__ == '__main__':
    rpg.assemble(build())
