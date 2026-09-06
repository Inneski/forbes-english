#!/usr/bin/env python3
"""Wonderland: The Stolen Now — Present Continuous voxel RPG (A1–A2).

    python3 lesson-template/build/build_wonderland_stolen_now.py

Rebuilds block-camp/wonderland-stolen-now-rpg.html from
lesson-template/build/rpg/wonderland-stolen-now/data.json (the question
tables and endings of the export Innes sent on 2026-09-05, pulled out of its
script with node) plus everything the export kept elsewhere or did not have:
the cover, prologue, forks, cake briefing, boss reveal and final decision,
which lived inside its render functions and are transcribed here; the
hotspot on each picture; a rules briefing; and Spanish and German for the
question titles, prompts, explanations, kickers and choice labels, which the
export left English-only (only the story lines and the endings were
translated).

This export was a different generator from the Oz one — 16:9 pictures, a
`q()` table per act, a two-blank "cake" item type and a repair-until-correct
rule: 10 points for a first-try answer, a wrong answer shows the rule and
lets you try again, sixteen questions on any route, 160 points. The engine
grew `repair`, `total`, split options and a score-gated route for it (see
rpg/README.md §6). The final decision sends Restore to the true ending at
120+ points and to the hopeful one below that; Break always escapes.

Pictures: block-camp/wonderland-stolen-now-rpg/NN_name.webp, 1536×864, as
exported. The rules briefing borrows the prologue plate.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(open(os.path.join(HERE, 'rpg', 'wonderland-stolen-now', 'data.json'), encoding='utf-8'))
LANGS = rpg.NINE   # es, de inline; the other seven from rpg/wonderland-stolen-now/translations/
IMG = lambda n: n + '.webp'


def T(en, es=None, de=None):
    return {'en': en, 'es': es if es is not None else en, 'de': de if de is not None else en}


# ── hotspots: [cx, cy, w, h] in % of the 16:9 picture, panel side, vertical
# anchor, optional panel width. Picked from gridded contact sheets.
HOT = {
    'cover':                 ([65, 22, 12, 22], 'left',   'center'),      # the palace clock in the rift
    'prologue':              ([82, 10, 12, 16], 'left',   'center'),      # the Warden with the stolen Heart
    'rules':                 ([66,  9,  8, 14], 'left',   'center', 56),  # the stopped clock tower
    'choice1':               ([50, 72, 12, 28], 'center', 'top'),         # Alice at the fork
    '03_rabbit_run':         ([78, 50, 12, 20], 'left',   'center'),      # the Rabbit with his watch
    '04_bridge_build':       ([42, 47,  8, 12], 'right',  'center'),      # the rose block going in
    '05_mouse_swim':         ([55, 62,  9, 12], 'left',   'center'),      # the Mouse in the rapids
    '06_guard_chase':        ([25, 42, 20, 30], 'right',  'center'),      # the card guards
    '07_cat_vanish':         ([69, 11, 10, 14], 'left',   'center'),      # the Cat's grin
    '08_tree_climb':         ([42, 50, 10, 18], 'right',  'center'),      # Alice on the stairs
    '09_mirror_guards':      ([72, 20, 14, 22], 'left',   'center'),      # the mirror portal
    '10_mirror_key':         ([55, 33,  8, 12], 'left',   'center'),      # the key in Alice's hand
    'cake_intro':            ([60, 32, 12, 18], 'left',   'center', 50),  # the Caterpillar Baker
    '12_cake_growing':       ([40, 25, 16, 30], 'right',  'center'),      # Alice growing
    '13_cake_routine':       ([63, 45,  8, 16], 'left',   'center'),      # the Rabbit running
    '14_cake_contrast':      ([78, 20, 12, 20], 'left',   'center'),      # the Hatter pouring tea
    '15_cake_gate':          ([50, 35, 10, 30], 'right',  'center', 40),  # where the two doors meet
    'choice2':               ([50, 60, 10, 26], 'center', 'top'),         # Alice between the routes
    '17_boat_engine':        ([60, 35, 12, 18], 'left',   'center'),      # tea into the engine
    '18_reverse_river':      ([70, 32, 12, 30], 'left',   'center'),      # the backwards waterfall
    '19_stone_ear':          ([25, 68, 16, 22], 'right',  'center'),      # Alice and the Hatter hiding
    '20_compass_island':     ([42, 45,  8, 10], 'right',  'center'),      # the compass
    '21_prison_gears':       ([75, 40, 16, 26], 'left',   'center'),      # the great gear
    '22_clockmaker_trapped': ([56, 32, 10, 14], 'left',   'center'),      # the trapped Mouse
    '23_broken_drill':       ([60, 35, 18, 20], 'left',   'center'),      # the drill
    '24_heart_gear':         ([42, 56,  8, 12], 'right',  'center'),      # the Heart Gear
    'boss_intro':            ([60, 30, 12, 24], 'left',   'center'),      # the Queen
    '26_freeze_attack':      ([52, 22, 14, 26], 'right',  'center', 40),  # the Warden sending the wave
    '27_shards_crown':       ([62, 38, 20, 22], 'left',   'center'),      # the Crown
    '28_queen_truth':        ([82, 30, 10, 22], 'left',   'center'),      # Rose beyond the wall
    '29_warden_break':       ([72, 25, 18, 26], 'left',   'center'),      # the Warden breaking up
    'decision':              ([48, 60, 10, 24], 'right',  'center', 40),  # Alice at the controls
    'end_restore':           ([32, 30,  8, 12], 'right',  'center'),      # the Crown held high
    'end_escape':            ([20, 30, 16, 26], 'right',  'center'),      # the portal they came through
    'end_flicker':           ([58, 12, 12, 18], 'left',   'center'),      # the flickering heart
}

KICKER = {
    1: T('ACT I · THE FIRST RELIC', 'ACTO I · LA PRIMERA RELIQUIA', 'AKT I · DAS ERSTE RELIKT'),
    2: T('ACT II · PINK CAKE OR BLUE CAKE?', 'ACTO II · ¿PASTEL ROSA O AZUL?', 'AKT II · ROSA ODER BLAUER KUCHEN?'),
    3: T('ACT III · THE SECOND RELIC', 'ACTO III · LA SEGUNDA RELIQUIA', 'AKT III · DAS ZWEITE RELIKT'),
    4: T('ACT IV · THE LAST MOVING SECOND', 'ACTO IV · EL ÚLTIMO SEGUNDO EN MOVIMIENTO', 'AKT IV · DIE LETZTE BEWEGTE SEKUNDE'),
}

# id: (title es, title de, prompt es, prompt de, explanation es, explanation de)
Q = {
    '03_rabbit_run': ('EMPIEZA LA PERSECUCIÓN', 'DIE JAGD BEGINNT',
        '¡Mira! El Conejo ___ hacia el cañón.', 'Schau! Das Kaninchen ___ zur Schlucht.',
        '"Look!" indica que ocurre ahora: he is running.', '„Look!“ zeigt: Es passiert jetzt gerade – he is running.'),
    '04_bridge_build': ('PUENTE BAJO PRESIÓN', 'BRÜCKE UNTER DRUCK',
        'Alice y el Conejo ___ un puente nuevo ahora mismo.', 'Alice und das Kaninchen ___ gerade eine neue Brücke.',
        'Alice y el Conejo = they. Usa "are building".', 'Alice und das Kaninchen = they. Benutze „are building“.'),
    '05_mouse_swim': ('LA RELOJERA EN LOS RÁPIDOS', 'DIE UHRMACHERIN IN DEN STROMSCHNELLEN',
        '¿___ la Ratona Relojera nadando con el cronómetro?', '___ die Uhrmachermaus gerade mit der Stoppuhr am Schwimmen?',
        'La Ratona = she. Pon "is" delante del sujeto: Is she swimming?', 'Die Maus = she. Setze „is“ vor das Subjekt: Is she swimming?'),
    '06_guard_chase': ('UN SEGUNDO POR DELANTE', 'EINE SEKUNDE VORAUS',
        'Elige la oración negativa correcta.', 'Wähle den richtigen verneinten Satz.',
        'Usa they + are not / aren\'t + catching.', 'Benutze they + are not / aren’t + catching.'),
    '07_cat_vanish': ('UN GUÍA QUE DESAPARECE', 'EIN VERSCHWINDENDER FÜHRER',
        'El Gato ___ entre las plataformas.', 'Die Katze ___ zwischen den Plattformen.',
        'El Gato = it. Para una acción en curso, usa "is disappearing".', 'Die Katze = it. Für eine laufende Handlung: „is disappearing“.'),
    '08_tree_climb': ('SOBRE EL BOSQUE QUE SE REPITE', 'ÜBER DEM SICH WIEDERHOLENDEN WALD',
        'Alice está ___ las escaleras del árbol-seta.', 'Alice ___ gerade die Pilzbaum-Treppe hinauf.',
        'Climb + ing = climbing. No dobles la "b".', 'Climb + ing = climbing. Das „b“ wird nicht verdoppelt.'),
    '09_mirror_guards': ('LOS VIGILANTES DEL ESPEJO', 'DIE WÄCHTER AM SPIEGEL',
        '¿Qué ___ mirando los guardias?', 'Was ___ die Wachen gerade?',
        'Orden de la pregunta: What + are + the guards + watching?', 'Fragestellung: What + are + the guards + watching?'),
    '10_mirror_key': ('LA LLAVE ENTRE SEGUNDOS', 'DER SCHLÜSSEL ZWISCHEN DEN SEKUNDEN',
        'Completa la frase de Alice: "I ___ taking the key."', 'Vervollständige Alices Satz: „I ___ taking the key.“',
        'Después de I usa "am": I am taking.', 'Nach I steht „am“: I am taking.'),
    '12_cake_growing': ('TAMAÑO HABITUAL / TAMAÑO QUE CAMBIA', 'NORMALE GRÖSSE / GRÖSSE IM WANDEL',
        'Alice normalmente ___ pequeña, pero ahora mismo ___ más alta.', 'Alice ___ normalerweise klein, aber gerade ___ sie größer.',
        'Rutina/estado: stays. Ocurre ahora mismo: is getting.', 'Routine/Zustand: stays. Passiert gerade: is getting.'),
    '13_cake_routine': ('RUTINA DIARIA / ACCIÓN AHORA', 'TÄGLICHE ROUTINE / HANDLUNG JETZT',
        'Cada mañana el Conejo ___ su reloj, pero ahora ___ hacia la puerta.', 'Jeden Morgen ___ das Kaninchen seine Uhr, aber jetzt ___ es zum Tor.',
        'Rutina repetida: checks. Acción que ocurre ahora: is running.', 'Wiederholte Routine: checks. Handlung jetzt: is running.'),
    '14_cake_contrast': ('TÉ HABITUAL / COMBUSTIBLE DE EMERGENCIA', 'GEWOHNTER TEE / NOTFALL-TREIBSTOFF',
        'El Sombrerero normalmente ___ té, pero hoy lo ___ en el motor.', 'Der Hutmacher ___ normalerweise Tee, aber heute ___ er ihn in den Motor.',
        'Rutina: drinks. Ocurre hoy/ahora: is pouring.', 'Routine: drinks. Passiert heute/jetzt: is pouring.'),
    '15_cake_gate': ('LA PUERTA DEL AHORA Y EL SIEMPRE', 'DAS TOR VON JETZT UND IMMER',
        'La puerta normalmente ___ a mediodía. ¡Mira! Ahora ___.', 'Das Tor ___ normalerweise um zwölf. Schau! Jetzt ___ es.',
        'Presente simple para la rutina: opens. Presente continuo para ahora: is opening.', 'Present Simple für die Routine: opens. Present Continuous für jetzt: is opening.'),
    '17_boat_engine': ('EL TÉ AHORA ES COMBUSTIBLE', 'TEE IST JETZT TREIBSTOFF',
        'El Sombrerero está ___ té en el motor.', 'Der Hutmacher ___ gerade Tee in den Motor.',
        'Después de "is", usa la forma -ING: pouring.', 'Nach „is“ kommt die ING-Form: pouring.'),
    '18_reverse_river': ('EL RÍO RECHAZA EL MAÑANA', 'DER FLUSS VERWEIGERT DAS MORGEN',
        'El agua ___ hacia atrás en este momento.', 'Das Wasser ___ im Moment rückwärts.',
        '"At the moment" señala presente continuo: is moving.', '„At the moment“ signalisiert Present Continuous: is moving.'),
    '19_stone_ear': ('LA CAVERNA ESCUCHA', 'DIE HÖHLE HÖRT ZU',
        'Nosotros ___ ahora. Nos escondemos en silencio.', 'Wir ___ jetzt. Wir verstecken uns leise.',
        'We + are not / aren\'t + talking.', 'We + are not / aren’t + talking.'),
    '20_compass_island': ('UNA BRÚJULA PARA UN SEGUNDO VERDADERO', 'EIN KOMPASS FÜR EINE WAHRE SEKUNDE',
        'Elige la pregunta correcta.', 'Wähle die richtige Frage.',
        'Orden de la pregunta: What + is + the compass + showing?', 'Fragestellung: What + is + the compass + showing?'),
    '21_prison_gears': ('CELDAS ENTRE SEGUNDOS', 'ZELLEN ZWISCHEN DEN SEKUNDEN',
        'Los engranajes de la prisión ___ alrededor de las celdas.', 'Die Zahnräder des Gefängnisses ___ um die Zellen.',
        'Gears = they. Usa "are turning".', 'Gears = they. Benutze „are turning“.'),
    '22_clockmaker_trapped': ('LA CREADORA DE LA CORONA', 'DIE ERBAUERIN DER KRONE',
        'La Ratona Relojera está ___ detrás del engranaje.', 'Die Uhrmachermaus ___ hinter dem Zahnrad.',
        'Lie cambia a lying: she is lying behind the gear.', 'Aus lie wird lying: she is lying behind the gear.'),
    '23_broken_drill': ('GÍRALO A MANO', 'DREH ES VON HAND',
        'Elige la oración negativa correcta.', 'Wähle den richtigen verneinten Satz.',
        'It + is not / isn\'t + working.', 'It + is not / isn’t + working.'),
    '24_heart_gear': ('LA VERDAD DENTRO DEL ENGRANAJE DEL CORAZÓN', 'DIE WAHRHEIT IM HERZRAD',
        'Alice y la Ratona ___ juntas el Engranaje del Corazón.', 'Alice und die Maus ___ das Herzrad gemeinsam.',
        'Dos personas = they: usa "are carrying".', 'Zwei Personen = they, also „are carrying“.'),
    '26_freeze_attack': ('EMPIEZA LA ÚLTIMA BATALLA', 'DIE LETZTE SCHLACHT BEGINNT',
        'El Guardián ___ una ola de tiempo ahora.', 'Der Wächter ___ jetzt eine Zeitwelle.',
        'El ataque ocurre ahora: it is sending a time wave.', 'Der Angriff passiert jetzt: it is sending a time wave.'),
    '27_shards_crown': ('REPARA LA CORONA', 'REPARIERE DIE KRONE',
        'Alice y sus amigos ___ juntos en este momento.', 'Alice und ihre Freunde ___ im Moment zusammen.',
        'Alice y sus amigos = they. Usa "are fighting".', 'Alice und ihre Freunde = they. Benutze „are fighting“.'),
    '28_queen_truth': ('LA REINA DICE LA VERDAD', 'DIE KÖNIGIN SAGT DIE WAHRHEIT',
        '¿Qué oración es correcta?', 'Welcher Satz ist richtig?',
        '"Understand" describe un estado. Usa presente simple: understands.', '„Understand“ beschreibt hier einen Zustand. Present Simple: understands.'),
    '29_warden_break': ('LA SOMBRA PIERDE SU FORMA', 'DER SCHATTEN VERLIERT SEINE FORM',
        'Elige la pregunta correcta.', 'Wähle die richtige Frage.',
        'Orden de la pregunta: Why + is + the Warden + breaking apart?', 'Fragestellung: Why + is + the Warden + breaking apart?'),
}

ROUTE_NAMES = {
    'Follow the Rabbit':     ('SIGUE AL CONEJO', 'FOLGE DEM KANINCHEN'),
    'Follow the Cat':        ('SIGUE AL GATO', 'FOLGE DER KATZE'),
    'Take the Teacup Boat':  ('TOMA EL BARCO-TAZA', 'NIMM DAS TEETASSENBOOT'),
    'Enter the Gear Prison': ('ENTRA EN LA PRISIÓN DE ENGRANAJES', 'BETRITT DAS ZAHNRADGEFÄNGNIS'),
}


def place(sid, scene):
    hot, pos, v = HOT[sid][:3]
    scene.update({'hot': hot, 'pos': pos, 'v': v})
    if len(HOT[sid]) > 3:
        scene['width'] = HOT[sid][3]
    return scene


def question(qd, act, nxt, relic=False):
    es_t, de_t, es_p, de_p, es_w, de_w = Q[qd['id']]
    if qd['type'] == 'cake':
        opts = [{'parts': o['parts'], 'kinds': ['a' if c == 'pink' else 'b' for c in o['colours']]} for o in qd['options']]
    else:
        opts = [{'en': o} for o in qd['options']]   # the English being taught — no gloss (the export had none)
    s = {'kind': 'question', 'img': IMG(qd['id']), 'k': KICKER[act],
         'title': T(qd['title'].upper(), es_t, de_t),
         'story': T(qd['story'], qd['es'], qd['de']),
         'prompt': T(qd['ask'], es_p, de_p),
         'opts': opts, 'answer': qd['correct'], 'fb': T(qd['why'], es_w, de_w),
         'points': 10, 'next': nxt}
    if relic:
        s['relic'] = True
    return place(qd['id'], s)


def chain(questions, act, after):
    out = {}
    for i, qd in enumerate(questions):
        last = i == len(questions) - 1
        out[qd['id']] = question(qd, act, after if last else questions[i + 1]['id'], relic=last)
    return out


def build():
    scenes = {}
    scenes['cover'] = place('cover', {
        'kind': 'intro', 'img': IMG('00_cover'),
        'k': T('WONDERLAND · PRESENT CONTINUOUS RPG', 'WONDERLAND · RPG DEL PRESENTE CONTINUO', 'WONDERLAND · PRESENT-CONTINUOUS-RPG'),
        'title': T('THE STOLEN NOW', 'EL AHORA ROBADO', 'DAS GESTOHLENE JETZT'),
        'story': T('The last afternoon is repeating. Each loop is shorter. When the palace clock reaches zero, everybody in Wonderland will become a frozen memory.',
                   'La última tarde se repite. Cada bucle es más corto. Cuando el reloj llegue a cero, todos se convertirán en un recuerdo congelado.',
                   'Der letzte Nachmittag wiederholt sich. Jede Schleife wird kürzer. Wenn die Palastuhr null erreicht, werden alle zu einer eingefrorenen Erinnerung.'),
        'rules': [T('+10 FIRST TRY', '+10 A LA PRIMERA', '+10 BEIM ERSTEN VERSUCH'), T('3 RELICS', '3 RELIQUIAS', '3 RELIKTE'), T('16 SPELLS', '16 HECHIZOS', '16 ZAUBER')],
        'start': T('BEGIN THE QUEST', 'EMPEZAR LA MISIÓN', 'DIE QUEST BEGINNEN'),
        'small': T('Single player · A1–A2 · two branching acts · three endings', 'Un jugador · A1–A2 · dos actos con ramas · tres finales', 'Ein Spieler · A1–A2 · zwei verzweigte Akte · drei Enden'),
        'next': 'prologue'})
    scenes['prologue'] = place('prologue', {
        'kind': 'story', 'img': IMG('01_prologue'),
        'k': T('PROLOGUE · SIXTEEN MOVING SECONDS REMAIN', 'PRÓLOGO · QUEDAN DIECISÉIS SEGUNDOS EN MOVIMIENTO', 'PROLOG · SECHZEHN BEWEGTE SEKUNDEN BLEIBEN'),
        'title': T('THE HEART OF NOW HAS BEEN STOLEN', 'HAN ROBADO EL CORAZÓN DEL AHORA', 'DAS HERZ DES JETZT WURDE GESTOHLEN'),
        'story': T('The Time Warden tears the glowing Heart from the palace clock. Dancers freeze in mid-step. Raindrops hang above the street. Only Alice, the Rabbit and the Cat can still move. The Rabbit says the Heart has split into two relics. Find both, cross the Gate of Now and Always, and reach the Queen before the final bell disappears.',
                   'El Guardián del Tiempo arranca el Corazón del reloj. Los bailarines se congelan a mitad de paso. Solo Alice, el Conejo y el Gato pueden moverse. El Corazón se ha partido en dos reliquias: encuentra las dos, cruza la Puerta del Ahora y el Siempre y llega hasta la Reina antes de que desaparezca la última campanada.',
                   'Der Zeitwächter reißt das Herz aus der Palastuhr. Tänzer erstarren mitten im Schritt. Nur Alice, das Kaninchen und die Katze können sich noch bewegen. Das Herz ist in zwei Relikte zersprungen: Finde beide, durchquere das Tor von Jetzt und Immer und erreiche die Königin, bevor der letzte Glockenschlag verschwindet.'),
        'next': 'rules'})
    scenes['rules'] = place('rules', {
        'kind': 'rules', 'img': IMG('01_prologue'),
        'k': T('BEFORE THE QUEST · YOUR GRAMMAR SPELLBOOK', 'ANTES DE LA MISIÓN · TU LIBRO DE HECHIZOS', 'VOR DER QUEST · DEIN GRAMMATIK-ZAUBERBUCH'),
        'title': T('NOW OR ALWAYS?', '¿AHORA O SIEMPRE?', 'JETZT ODER IMMER?'),
        'story': T('Use the present continuous for actions happening now or around now. Use the present simple for habits, routines, facts and most state verbs.',
                   'Usa el presente continuo para acciones que ocurren ahora o en este periodo. Usa el presente simple para hábitos, rutinas, hechos y la mayoría de los verbos de estado.',
                   'Benutze das Present Continuous für Handlungen, die jetzt oder um jetzt herum passieren. Benutze das Present Simple für Gewohnheiten, Routinen, Fakten und die meisten Zustandsverben.'),
        'rules': [
            {'name': T('FORM · AM / IS / ARE + ING FORM', 'FORMA · AM / IS / ARE + FORMA -ING', 'FORM · AM / IS / ARE + ING-FORM'),
             'form': T('I am running · he / she / it is running · you / we / they are running')},
            {'name': T('NEGATIVE AND QUESTION', 'NEGACIÓN Y PREGUNTA', 'VERNEINUNG UND FRAGE'),
             'form': T('Alice is not sleeping. · Is Alice sleeping? Yes, she is. / No, she isn\'t.',
                       'Alice no está durmiendo. · ¿Está durmiendo Alice? Sí. / No.',
                       'Alice schläft nicht. · Schläft Alice gerade? Ja. / Nein.')},
            {'name': T('SPELLING', 'ORTOGRAFÍA', 'SCHREIBWEISE'),
             'form': T('look → looking · make → making · run → running · lie → lying')},
            {'name': T('NOW CLUES', 'PISTAS DE "AHORA"', 'JETZT-SIGNALE'),
             'form': T('now · right now · at the moment · Look! · Listen!')},
            {'name': T('PRESENT SIMPLE · HABITS AND FACTS', 'PRESENTE SIMPLE · HÁBITOS Y HECHOS', 'PRESENT SIMPLE · GEWOHNHEITEN UND FAKTEN'),
             'form': T('The Rabbit checks his watch every day. · I know the answer.',
                       'El Conejo mira su reloj todos los días. · Sé la respuesta.',
                       'Das Kaninchen schaut jeden Tag auf seine Uhr. · Ich weiß die Antwort.')},
        ],
        'note': T('Each first correct answer earns 10 points. A mistake shows the rule; repair the spell to continue. Sixteen spells on every route, 160 points.',
                  'Cada primera respuesta correcta vale 10 puntos. Un error muestra la regla; repara el hechizo para continuar. Dieciséis hechizos en cada ruta, 160 puntos.',
                  'Jede beim ersten Versuch richtige Antwort bringt 10 Punkte. Ein Fehler zeigt die Regel; repariere den Zauber, um weiterzugehen. Sechzehn Zauber auf jeder Route, 160 Punkte.'),
        'button': T('CHOOSE THE FIRST TRAIL', 'ELIGE EL PRIMER CAMINO', 'WÄHLE DEN ERSTEN PFAD'),
        'next': 'choice1'})

    def fork(sid, img, act, title, story, paths, after):
        routes = []
        for p in paths:
            es_n, de_n = ROUTE_NAMES[p['name']]
            routes.append({'name': T(p['name'].upper(), es_n, de_n), 'desc': T(p['detail'], p['es'], p['de']),
                           'route': p['reward'], 'target': p['questions'][0]['id']})
            scenes.update(chain(p['questions'], act, after))
        scenes[sid] = place(sid, {'kind': 'choice', 'img': IMG(img), 'k':
                                  T('ACT %s · BRANCHING QUEST · YOUR CHOICE CHANGES THE STORY' % ('I' if act == 1 else 'III'),
                                    'ACTO %s · MISIÓN CON RAMAS · TU ELECCIÓN CAMBIA LA HISTORIA' % ('I' if act == 1 else 'III'),
                                    'AKT %s · VERZWEIGTE QUEST · DEINE WAHL ÄNDERT DIE GESCHICHTE' % ('I' if act == 1 else 'III')),
                                  'title': title, 'story': story, 'routes': routes})

    fork('choice1', '02_fork_one', 1,
         T('WHERE IS THE FIRST RELIC?', '¿DÓNDE ESTÁ LA PRIMERA RELIQUIA?', 'WO IST DAS ERSTE RELIKT?'),
         T('The Silver Stopwatch lies beyond the Rabbit\'s collapsing bridge. The Moon-Mirror Key is hidden above the Cat\'s forest. Either relic can hold one true second.',
           'El Cronómetro de Plata está más allá del puente del Conejo, que se derrumba. La Llave del Espejo Lunar se esconde sobre el bosque del Gato. Cualquiera de las dos guarda un segundo verdadero.',
           'Die silberne Stoppuhr liegt hinter der einstürzenden Brücke des Kaninchens. Der Mondspiegelschlüssel ist über dem Wald der Katze versteckt. Jedes Relikt kann eine wahre Sekunde halten.'),
         DATA['ACT_ONE'], 'cake_intro')

    scenes['cake_intro'] = place('cake_intro', {
        'kind': 'story', 'img': IMG('11_cake_chamber'),
        'k': T('ACT II · THE CATERPILLAR BAKER\'S TRIAL', 'ACTO II · LA PRUEBA DE LA ORUGA PASTELERA', 'AKT II · DIE PRÜFUNG DER RAUPENBÄCKERIN'),
        'title': T('PINK CAKE OR BLUE CAKE?', '¿PASTEL ROSA O PASTEL AZUL?', 'ROSA ODER BLAUER KUCHEN?'),
        'story': T('The palace gate is caught between two kinds of time. Pink means present continuous: actions happening now. Blue means present simple: routines, facts and repeated actions.',
                   'La puerta del palacio está atrapada entre dos clases de tiempo. Rosa = presente continuo: acciones que ocurren ahora. Azul = presente simple: rutinas, hechos y acciones repetidas.',
                   'Das Palasttor steckt zwischen zwei Arten von Zeit fest. Rosa = Present Continuous: Handlungen, die jetzt passieren. Blau = Present Simple: Routinen, Fakten und wiederholte Handlungen.'),
        'rules': [
            {'name': T('PINK · PRESENT CONTINUOUS', 'ROSA · PRESENTE CONTINUO', 'ROSA · PRESENT CONTINUOUS'),
             'form': T('am / is / are + ING FORM', 'am / is / are + forma -ING', 'am / is / are + ING-Form')},
            {'name': T('BLUE · PRESENT SIMPLE', 'AZUL · PRESENTE SIMPLE', 'BLAU · PRESENT SIMPLE'),
             'form': T('habits, routines and facts', 'hábitos, rutinas y hechos', 'Gewohnheiten, Routinen und Fakten')},
        ],
        'note': T('Every answer is one cake split down the middle. Match the first coloured half to the first blank and the second half to the second blank.',
                  'Cada respuesta es un pastel partido por la mitad. La primera mitad de color va en el primer hueco y la segunda en el segundo.',
                  'Jede Antwort ist ein in der Mitte geteilter Kuchen. Die erste farbige Hälfte gehört in die erste Lücke, die zweite in die zweite.'),
        'button': T('TAKE THE FIRST PIECE', 'TOMA EL PRIMER TROZO', 'NIMM DAS ERSTE STÜCK'),
        'next': DATA['CAKE_ROUND'][0]['id']})
    scenes.update(chain(DATA['CAKE_ROUND'], 2, 'choice2'))

    fork('choice2', '16_fork_two', 3,
         T('HOW WILL YOU ENTER THE PALACE?', '¿CÓMO ENTRARÁS EN EL PALACIO?', 'WIE KOMMST DU IN DEN PALAST?'),
         T('The Hatter knows a river route to the Teacup Compass. A rebel card guard can lead Alice to the imprisoned Clockmaker and her Heart Gear.',
           'El Sombrerero conoce una ruta por el río hasta la Brújula-Taza. Un guardia de cartas rebelde puede llevar a Alice hasta la Relojera prisionera y su Engranaje del Corazón.',
           'Der Hutmacher kennt einen Flussweg zum Teetassenkompass. Eine rebellische Kartenwache kann Alice zur gefangenen Uhrmacherin und ihrem Herzrad führen.'),
         DATA['ACT_TWO'], 'boss_intro')

    scenes['boss_intro'] = place('boss_intro', {
        'kind': 'story', 'img': IMG('25_boss_reveal'),
        'k': T('THE REVEAL · THE CLOCK REACHES ZERO', 'LA REVELACIÓN · EL RELOJ LLEGA A CERO', 'DIE ENTHÜLLUNG · DIE UHR ERREICHT NULL'),
        'title': T('THE WARDEN IS THE QUEEN\'S FEAR', 'EL GUARDIÁN ES EL MIEDO DE LA REINA', 'DER WÄCHTER IST DIE ANGST DER KÖNIGIN'),
        'story': T('A child named Rose is trapped one second beyond the clock. Terrified of losing her, the Queen ordered the Clockmaker to stop tomorrow. Her fear grew into the Warden, and the Warden stole the present from everyone. Alice raises her two relics. They hold the arena in motion, but only four final grammar spells can break the Warden\'s control.',
                   'Una niña llamada Rose está atrapada un segundo más allá del reloj. Aterrada de perderla, la Reina ordenó a la Relojera detener el mañana. Su miedo se convirtió en el Guardián, y el Guardián robó el presente a todos. Alice levanta sus dos reliquias: mantienen la arena en movimiento, pero solo cuatro hechizos finales pueden romper el control del Guardián.',
                   'Ein Kind namens Rose ist eine Sekunde hinter der Uhr gefangen. Aus Angst, sie zu verlieren, ließ die Königin die Uhrmacherin das Morgen anhalten. Ihre Angst wurde zum Wächter, und der Wächter stahl allen die Gegenwart. Alice hebt ihre zwei Relikte: Sie halten die Arena in Bewegung, aber nur vier letzte Grammatikzauber können den Wächter brechen.'),
        'button': T('FIGHT FOR THE NEXT SECOND', 'LUCHA POR EL SIGUIENTE SEGUNDO', 'KÄMPFE UM DIE NÄCHSTE SEKUNDE'),
        'next': DATA['BOSS_ROUND'][0]['id']})
    boss = chain(DATA['BOSS_ROUND'], 4, 'decision')
    boss[DATA['BOSS_ROUND'][-1]['id']].pop('relic', None)   # the third relic came from the cake gate
    scenes.update(boss)

    scenes['decision'] = place('decision', {
        'kind': 'choice', 'img': IMG('30_final_choice'),
        'k': T('FINAL DECISION · THREE ENDINGS', 'DECISIÓN FINAL · TRES FINALES', 'LETZTE ENTSCHEIDUNG · DREI ENDEN'),
        'title': T('WHO SHOULD OWN TOMORROW?', '¿QUIÉN DEBE SER DUEÑO DEL MAÑANA?', 'WEM SOLL DAS MORGEN GEHÖREN?'),
        'story': T('The Warden is gone, but the Crown still controls every clock. Alice can restore it and trust the Queen to share time, or destroy it and lead Wonderland into an unknown dawn.',
                   'El Guardián ya no está, pero la Corona sigue controlando todos los relojes. Alice puede restaurarla y confiar en que la Reina comparta el tiempo, o destruirla y guiar al País de las Maravillas hacia un amanecer desconocido.',
                   'Der Wächter ist fort, aber die Krone steuert noch jede Uhr. Alice kann sie wiederherstellen und darauf vertrauen, dass die Königin die Zeit teilt – oder sie zerstören und Wunderland in eine unbekannte Morgendämmerung führen.'),
        'routes': [
            {'name': T('RESTORE THE CROWN', 'RESTAURAR LA CORONA', 'DIE KRONE WIEDERHERSTELLEN'),
             'desc': T('Requires 120 points for the strongest ending.', 'Con 120 puntos consigues el final más fuerte.', 'Mit 120 Punkten bekommst du das stärkste Ende.'),
             'target': 'end_restore', 'min': 120, 'else': 'end_flicker'},
            {'name': T('BREAK THE TIME MACHINE', 'ROMPER LA MÁQUINA DEL TIEMPO', 'DIE ZEITMASCHINE ZERSTÖREN'),
             'desc': T('Choose freedom, risk and a world without controlled clocks.', 'Elige la libertad, el riesgo y un mundo sin relojes controlados.', 'Wähle Freiheit, Risiko und eine Welt ohne kontrollierte Uhren.'),
             'target': 'end_escape'},
        ]})

    E = DATA['ENDINGS']
    for key, k, title in (
        ('restore', T('TRUE ENDING · QUEST COMPLETE', 'FINAL VERDADERO · MISIÓN COMPLETA', 'WAHRES ENDE · QUEST ABGESCHLOSSEN'), T('KEEPER OF NOW', 'GUARDIANA DEL AHORA', 'HÜTERIN DES JETZT')),
        ('escape',  T('FREEDOM ENDING · QUEST COMPLETE', 'FINAL DE LIBERTAD · MISIÓN COMPLETA', 'FREIHEITS-ENDE · QUEST ABGESCHLOSSEN'), T('A WORLD WITHOUT THE CROWN', 'UN MUNDO SIN LA CORONA', 'EINE WELT OHNE DIE KRONE')),
        ('flicker', T('HOPEFUL ENDING · QUEST COMPLETE', 'FINAL ESPERANZADOR · MISIÓN COMPLETA', 'HOFFNUNGSVOLLES ENDE · QUEST ABGESCHLOSSEN'), T('ONE MORE DAWN', 'UN AMANECER MÁS', 'NOCH EINE MORGENDÄMMERUNG')),
    ):
        e = E[key]
        scenes['end_' + key] = place('end_' + key, {
            'kind': 'ending', 'img': IMG(e['image']), 'success': key != 'flicker',
            'k': k, 'title': title, 'story': T(e['story'], e['es'], e['de'])})

    labels = {
        'tiles':    T('RELICS', 'RELIQUIAS', 'RELIKTE'),
        'relic':    T('RELIC RECOVERED · +{p} POINTS', 'RELIQUIA RECUPERADA · +{p} PUNTOS', 'RELIKT GEBORGEN · +{p} PUNKTE'),
        'correct':  T('FIRST-TRY SPELL · +{p} POINTS', 'HECHIZO A LA PRIMERA · +{p} PUNTOS', 'ZAUBER BEIM ERSTEN VERSUCH · +{p} PUNKTE'),
        'restart':  T('PLAY A DIFFERENT ROUTE', 'JUEGA OTRA RUTA', 'EINE ANDERE ROUTE SPIELEN'),
    }
    return {
        'file': 'block-camp/wonderland-stolen-now-rpg.html',
        'img_dir': 'block-camp/wonderland-stolen-now-rpg',
        'img_w': 1536, 'img_h': 864,
        'title': 'Wonderland: The Stolen Now — Present Continuous Voxel RPG (A1-A2)',
        'description': 'An interactive A1-A2 English lesson from Forbes English: Wonderland: The Stolen Now — Present Continuous Voxel RPG (A1-A2).',
        'langs': LANGS,
        'accent': '#E66085',        # camp 2, Present Continuous, on the Block Camp route map
        'accent_ink': '#1f0716', 'deep': '#2d1024', 'panel': 'rgba(30,9,26,.9)',
        'labels': labels,
        'tags': {'a': T('PINK · NOW', 'ROSA · AHORA', 'ROSA · JETZT'), 'b': T('BLUE · USUAL', 'AZUL · HABITUAL', 'BLAU · GEWOHNT')},
        'start': 'cover', 'scenes': scenes,
        'endings': {'master': 'end_restore', 'complete': 'end_restore', 'missing': 'end_flicker', 'failed': 'end_escape'},
        'max': 160, 'points': 10, 'tiles': 3, 'chances': 0, 'total': 16, 'repair': True,
    }


if __name__ == '__main__':
    rpg.assemble(rpg.apply_translations(build(), os.path.join(HERE, 'rpg', 'wonderland-stolen-now', 'translations')))
