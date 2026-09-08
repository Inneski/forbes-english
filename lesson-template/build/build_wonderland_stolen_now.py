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

Two reading levels. rpg/wonderland-stolen-now/data-easy.json is the easy
layer, from the Easy English export of 2026-09-07 — a structural twin of the
original: same 24 question ids in the same order, options byte-for-byte
identical, same `correct` indices, simpler prose. It rides as a partial
`easy` scene (rpg/README.md §7), so both levels share one page, one set of
pictures and one answer key, and the 📖 button swaps the words mid-game
without touching the score. The export carried its own Spanish and German
for the story lines, the endings and the narrative screens; the question
titles, prompts and explanations it left English-only, so those es/de were
written for data-easy.json. The other seven glosses fall through to the
base text on purpose.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(open(os.path.join(HERE, 'rpg', 'wonderland-stolen-now', 'data.json'), encoding='utf-8'))
EASY = json.load(open(os.path.join(HERE, 'rpg', 'wonderland-stolen-now', 'data-easy.json'), encoding='utf-8'))
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

# The export wrote its endings and route blurbs at B1-B2 while every question
# is A1-A2 — Innes flagged the opening on 2026-09-08 and the same register ran
# to the last screen. These replace that prose at the level the deck teaches.
# data.json keeps the export's wording; nothing here changes an answer.
SIMPLER_ROUTE = {
    'Follow the Rabbit':     ('Cross the broken bridge and get the Silver Stopwatch.',
                              'Cruza el puente roto y consigue el Cronómetro de Plata.',
                              'Überquere die kaputte Brücke und hol die silberne Stoppuhr.'),
    'Follow the Cat':        ('Climb high above the trees and take back the Moon-Mirror Key.',
                              'Sube muy alto sobre los árboles y recupera la Llave del Espejo Lunar.',
                              'Klettere hoch über die Bäume und hol den Mondspiegelschlüssel zurück.'),
    'Take the Teacup Boat':  ('Travel on the backwards river with the Hatter and get the Teacup Compass.',
                              'Viaja por el río que va al revés con el Sombrerero y consigue la Brújula-Taza.',
                              'Fahre mit dem Hutmacher auf dem rückwärts fließenden Fluss und hol den Teetassenkompass.'),
    'Enter the Gear Prison': ('Help the Clockmaker Mouse escape and get the Heart Gear.',
                              'Ayuda a la Ratona Relojera a escapar y consigue el Engranaje del Corazón.',
                              'Hilf der Uhrmachermaus zu entkommen und hol das Herzrad.'),
}

SIMPLER_ENDING = {
    'restore': ('Alice puts her magic objects inside the Crown. The clocks start again, Rose comes back, and the Queen lets the day finish. The Queen gives Alice the Keeper\'s Crown — not to control time, but to keep it safe for everybody.',
                'Alice pone sus objetos mágicos dentro de la Corona. Los relojes vuelven a funcionar, Rose regresa y la Reina deja que el día termine. La Reina le da a Alice la Corona de la Guardiana: no para controlar el tiempo, sino para cuidarlo para todos.',
                'Alice legt ihre Zaubergegenstände in die Krone. Die Uhren laufen wieder, Rose kommt zurück, und die Königin lässt den Tag zu Ende gehen. Die Königin gibt Alice die Krone der Hüterin — nicht um die Zeit zu kontrollieren, sondern um sie für alle zu bewahren.'),
    'escape':  ('Alice breaks the machine and opens the palace doors. Rose, the Queen and everybody else run out into a new forest, and the old kingdom falls into pink blocks. Now nobody controls the next second.',
                'Alice rompe la máquina y abre las puertas del palacio. Rose, la Reina y todos los demás salen corriendo hacia un bosque nuevo, y el viejo reino se deshace en bloques rosas. Ahora nadie controla el siguiente segundo.',
                'Alice zerbricht die Maschine und öffnet die Palasttüren. Rose, die Königin und alle anderen laufen hinaus in einen neuen Wald, und das alte Königreich zerfällt in rosa Blöcke. Jetzt kontrolliert niemand die nächste Sekunde.'),
    'flicker': ('The Crown is working again, but its new heart is weak. Rose is free and the Warden is gone. The Hatter is keeping the gears turning while Alice looks for one last missing piece. Wonderland has a new morning — and a new quest.',
                'La Corona funciona otra vez, pero su nuevo corazón está débil. Rose está libre y el Guardián ha desaparecido. El Sombrerero mantiene los engranajes girando mientras Alice busca una última pieza. El País de las Maravillas tiene una mañana nueva y una misión nueva.',
                'Die Krone läuft wieder, aber ihr neues Herz ist schwach. Rose ist frei und der Wächter ist weg. Der Hutmacher hält die Zahnräder in Bewegung, während Alice ein letztes fehlendes Teil sucht. Wunderland hat einen neuen Morgen — und eine neue Quest.'),
}

def fold(base, over):
    """Merge one text object at a time, exactly as the runtime used to."""
    if over is None:
        return base
    if isinstance(over, dict) and 'en' in over:
        return dict(base, **over) if isinstance(base, dict) and 'en' in base else over
    if isinstance(over, list):
        return [fold(base[i] if isinstance(base, list) and i < len(base) else None, v)
                for i, v in enumerate(over)]
    if isinstance(over, dict):
        out = dict(base or {})
        for k, v in over.items():
            out[k] = fold(out.get(k), v)
        return out
    return over


def collapse(spec):
    """One reading level: fold the easy layer in and drop the switch.

    Innes, 2026-09-08: "Just keep the easy English version. A complicated
    version is redundant - the description must match the questions." Once the
    narrative was re-levelled the two levels sat a hair apart, so the deck
    ships the simpler wording and no reading-level button.

    Folding rather than replacing is what keeps nine languages on every
    screen: the export gave the easy text English, Spanish and German only,
    and the base text supplies the other seven, which describe the same scene.
    """
    frozen = ('img', 'hot', 'pos', 'v', 'width', 'inset', 'kind', 'answer',
              'next', 'opts', 'points', 'relic', 'final', 'success')
    for sid, sc in spec['scenes'].items():
        e = sc.pop('easy', None)
        if not e:
            continue
        # the overlay is wording only. It shares the pictures, the options and
        # the answer key with the text it replaces, and this is the gate that
        # keeps it that way now that nothing checks it at runtime.
        bad = [k for k in e if k in frozen] + [k for k in e if k not in sc]
        if bad:
            raise SystemExit('%s: the easy layer may not set %s' % (sid, ', '.join(sorted(set(bad)))))
        if 'routes' in e and [r.get('target') for r in e['routes']] != [r.get('target') for r in sc['routes']]:
            raise SystemExit('%s: the easy layer changes where a route goes' % sid)
        sc.update(fold(sc, e))
    # fold over rpg.LABELS, not just this deck's overrides: three of the easy
    # labels (progress, review, perfect) have no base override here, and
    # replacing the default outright would drop the seven glosses it ships.
    spec['labels'] = fold(dict(rpg.LABELS, **spec.get('labels', {})),
                          spec.pop('easy_labels', {}))
    spec['tags'] = fold(spec.get('tags', {}), spec.pop('easy_tags', {}))
    return spec


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
    e = EASY['questions'][qd['id']]
    s['easy'] = {'k': e['k'], 'title': e['title'], 'story': e['story'],
                 'prompt': e['ask'], 'fb': e['why']}
    return place(qd['id'], s)


def chain(questions, act, after):
    out = {}
    for i, qd in enumerate(questions):
        last = i == len(questions) - 1
        out[qd['id']] = question(qd, act, after if last else questions[i + 1]['id'], relic=last)
    return out


def build():
    scenes = {}

    def easy(sid, **extra):
        """Attach the easy-English overlay for `sid` to the scene just built.

        The overlay is a partial scene — only the keys whose wording changes.
        The picture, the hotspot, the options, the answer key and every `next`
        stay on the base scene, so the reader can switch level mid-game and
        keep both the score and the route. rpg.py refuses an overlay that
        reaches past that.
        """
        src = EASY['scenes'].get(sid) or EASY['endings'][sid]
        scenes[sid]['easy'] = dict(src, **extra)

    scenes['cover'] = place('cover', {
        'kind': 'intro', 'img': IMG('00_cover'),
        'k': T('WONDERLAND · PRESENT CONTINUOUS RPG', 'WONDERLAND · RPG DEL PRESENTE CONTINUO', 'WONDERLAND · PRESENT-CONTINUOUS-RPG'),
        'title': T('THE STOLEN NOW', 'EL AHORA ROBADO', 'DAS GESTOHLENE JETZT'),
        'story': T('Something is wrong with time in Wonderland. The same afternoon is starting again and again, and every time it is shorter. When the palace clock stops, everybody in Wonderland stops too.',
                   'Algo va mal con el tiempo en el País de las Maravillas. La misma tarde empieza una y otra vez, y cada vez es más corta. Cuando el reloj del palacio se pare, todos se pararán también.',
                   'Mit der Zeit in Wunderland stimmt etwas nicht. Derselbe Nachmittag beginnt immer wieder, und jedes Mal ist er kürzer. Wenn die Palastuhr stehen bleibt, bleiben alle mit ihr stehen.'),
        'rules': [T('+10 FIRST TRY', '+10 A LA PRIMERA', '+10 BEIM ERSTEN VERSUCH'), T('3 MAGIC OBJECTS', '3 OBJETOS MÁGICOS', '3 ZAUBERGEGENSTÄNDE'), T('16 SPELLS', '16 HECHIZOS', '16 ZAUBER')],
        'start': T('BEGIN THE QUEST', 'EMPEZAR LA MISIÓN', 'DIE QUEST BEGINNEN'),
        'small': T('One player · A1–A2 · two paths to choose · three endings', 'Un jugador · A1–A2 · dos caminos a elegir · tres finales', 'Ein Spieler · A1–A2 · zwei Wege zur Wahl · drei Enden'),
        'next': 'prologue'})
    easy('cover')
    scenes['prologue'] = place('prologue', {
        'kind': 'story', 'img': IMG('01_prologue'),
        'k': T('PROLOGUE · TIME IS STOPPING', 'PRÓLOGO · EL TIEMPO SE ESTÁ PARANDO', 'PROLOG · DIE ZEIT BLEIBT STEHEN'),
        'title': T('THE HEART OF THE CLOCK IS GONE', 'EL CORAZÓN DEL RELOJ HA DESAPARECIDO', 'DAS HERZ DER UHR IST WEG'),
        'story': T('The Time Warden is a dark shadow. It is taking the glowing Heart out of the palace clock. Look — the people in the street are not moving, and the rain is not falling. Only Alice, the Rabbit and the Cat can still move. The Rabbit says the Heart is now two magic objects. Find them both, open the great gate, and reach the Queen before the clock stops.',
                   'El Guardián del Tiempo es una sombra oscura. Está sacando el Corazón brillante del reloj del palacio. Mira: la gente de la calle no se mueve y la lluvia no cae. Solo Alice, el Conejo y el Gato pueden moverse todavía. El Conejo dice que el Corazón ahora son dos objetos mágicos. Encuéntralos los dos, abre la gran puerta y llega hasta la Reina antes de que el reloj se pare.',
                   'Der Zeitwächter ist ein dunkler Schatten. Er nimmt gerade das leuchtende Herz aus der Palastuhr. Schau: Die Leute auf der Straße bewegen sich nicht, und der Regen fällt nicht. Nur Alice, das Kaninchen und die Katze können sich noch bewegen. Das Kaninchen sagt, das Herz sind jetzt zwei Zaubergegenstände. Finde beide, öffne das große Tor und erreiche die Königin, bevor die Uhr stehen bleibt.'),
        'next': 'rules'})
    easy('prologue')
    scenes['rules'] = place('rules', {
        'kind': 'rules', 'img': IMG('01_prologue'),
        'k': T('BEFORE THE QUEST · YOUR GRAMMAR SPELLBOOK', 'ANTES DE LA MISIÓN · TU LIBRO DE HECHIZOS', 'VOR DER QUEST · DEIN GRAMMATIK-ZAUBERBUCH'),
        'title': T('NOW OR ALWAYS?', '¿AHORA O SIEMPRE?', 'JETZT ODER IMMER?'),
        'story': T('Use the present continuous for an action happening now: Alice is running. Use the present simple for things we do again and again, and for facts: Alice runs every day.',
                   'Usa el presente continuo para una acción que ocurre ahora: Alice is running. Usa el presente simple para lo que hacemos una y otra vez y para los hechos: Alice runs every day.',
                   'Benutze das Present Continuous für eine Handlung, die gerade passiert: Alice is running. Benutze das Present Simple für Dinge, die wir immer wieder tun, und für Fakten: Alice runs every day.'),
        'rules': [
            {'tone': 'a',
             'name': T('FORM · AM / IS / ARE + ING FORM', 'FORMA · AM / IS / ARE + FORMA -ING', 'FORM · AM / IS / ARE + ING-FORM'),
             'form': T('I am running · he / she / it is running · you / we / they are running')},
            {'name': T('NEGATIVE AND QUESTION', 'NEGACIÓN Y PREGUNTA', 'VERNEINUNG UND FRAGE'),
             'form': T('Alice is not sleeping. · Is Alice sleeping? Yes, she is. / No, she isn\'t.',
                       'Alice no está durmiendo. · ¿Está durmiendo Alice? Sí. / No.',
                       'Alice schläft nicht. · Schläft Alice gerade? Ja. / Nein.')},
            {'name': T('SPELLING', 'ORTOGRAFÍA', 'SCHREIBWEISE'),
             'form': T('look → looking · make → making · run → running · lie → lying')},
            {'name': T('NOW CLUES', 'PISTAS DE "AHORA"', 'JETZT-SIGNALE'),
             'form': T('now · right now · at the moment · Look! · Listen!')},
            {'tone': 'b',
             'name': T('PRESENT SIMPLE · EVERY DAY AND FACTS', 'PRESENTE SIMPLE · CADA DÍA Y HECHOS', 'PRESENT SIMPLE · JEDEN TAG UND FAKTEN'),
             'form': T('The Rabbit checks his watch every day. · I know the answer.',
                       'El Conejo mira su reloj todos los días. · Sé la respuesta.',
                       'Das Kaninchen schaut jeden Tag auf seine Uhr. · Ich weiß die Antwort.')},
        ],
        'note': T('Your first correct answer gives you 10 points. If you make a mistake, read the rule and repair the spell. There are 16 spells on every path and 160 points.',
                  'Tu primera respuesta correcta te da 10 puntos. Si te equivocas, lee la regla y repara el hechizo. Hay 16 hechizos en cada camino y 160 puntos.',
                  'Deine erste richtige Antwort gibt dir 10 Punkte. Wenn du einen Fehler machst, lies die Regel und repariere den Zauber. Es gibt 16 Zauber auf jedem Weg und 160 Punkte.'),
        'button': T('CHOOSE THE FIRST TRAIL', 'ELIGE EL PRIMER CAMINO', 'WÄHLE DEN ERSTEN PFAD'),
        'next': 'choice1'})
    easy('rules')

    def fork(sid, img, act, title, story, paths, after):
        routes, easy_routes = [], []
        for p in paths:
            es_n, de_n = ROUTE_NAMES[p['name']]
            en_d, es_d, de_d = SIMPLER_ROUTE[p['name']]
            routes.append({'name': T(p['name'].upper(), es_n, de_n), 'desc': T(en_d, es_d, de_d),
                           'route': p['reward'], 'target': p['questions'][0]['id']})
            er = EASY['routes'][p['name']]
            easy_routes.append(dict(routes[-1], name=er['name'], desc=er['desc']))
            scenes.update(chain(p['questions'], act, after))
        scenes[sid] = place(sid, {'kind': 'choice', 'img': IMG(img), 'k':
                                  T('ACT %s · CHOOSE A PATH · YOUR CHOICE CHANGES THE STORY' % ('I' if act == 1 else 'III'),
                                    'ACTO %s · ELIGE UN CAMINO · TU ELECCIÓN CAMBIA LA HISTORIA' % ('I' if act == 1 else 'III'),
                                    'AKT %s · WÄHLE EINEN WEG · DEINE WAHL ÄNDERT DIE GESCHICHTE' % ('I' if act == 1 else 'III')),
                                  'title': title, 'story': story, 'routes': routes})
        easy(sid, routes=easy_routes)

    fork('choice1', '02_fork_one', 1,
         T('WHERE IS THE FIRST MAGIC OBJECT?', '¿DÓNDE ESTÁ EL PRIMER OBJETO MÁGICO?', 'WO IST DER ERSTE ZAUBERGEGENSTAND?'),
         T('The Silver Stopwatch is on the other side of the Rabbit\'s broken bridge. The Moon-Mirror Key is high above the Cat\'s forest. Both objects can hold one true second.',
           'El Cronómetro de Plata está al otro lado del puente roto del Conejo. La Llave del Espejo Lunar está muy alto, sobre el bosque del Gato. Los dos objetos pueden guardar un segundo verdadero.',
           'Die silberne Stoppuhr ist auf der anderen Seite der kaputten Brücke des Kaninchens. Der Mondspiegelschlüssel ist hoch über dem Wald der Katze. Beide Gegenstände können eine wahre Sekunde halten.'),
         DATA['ACT_ONE'], 'cake_intro')

    scenes['cake_intro'] = place('cake_intro', {
        'kind': 'story', 'img': IMG('11_cake_chamber'),
        'k': T('ACT II · THE CATERPILLAR BAKER\'S TRIAL', 'ACTO II · LA PRUEBA DE LA ORUGA PASTELERA', 'AKT II · DIE PRÜFUNG DER RAUPENBÄCKERIN'),
        'title': T('PINK CAKE OR BLUE CAKE?', '¿PASTEL ROSA O PASTEL AZUL?', 'ROSA ODER BLAUER KUCHEN?'),
        'story': T('The palace gate is stuck between two kinds of time. Pink is the present continuous: something happening now. Blue is the present simple: things we do every day, and facts.',
                   'La puerta del palacio está atascada entre dos clases de tiempo. Rosa es el presente continuo: algo que ocurre ahora. Azul es el presente simple: lo que hacemos cada día y los hechos.',
                   'Das Palasttor steckt zwischen zwei Arten von Zeit fest. Rosa ist das Present Continuous: etwas, das gerade passiert. Blau ist das Present Simple: Dinge, die wir jeden Tag tun, und Fakten.'),
        'rules': [
            {'tone': 'a', 'name': T('PINK · PRESENT CONTINUOUS', 'ROSA · PRESENTE CONTINUO', 'ROSA · PRESENT CONTINUOUS'),
             'form': T('am / is / are + ING FORM', 'am / is / are + forma -ING', 'am / is / are + ING-Form')},
            {'tone': 'b', 'name': T('BLUE · PRESENT SIMPLE', 'AZUL · PRESENTE SIMPLE', 'BLAU · PRESENT SIMPLE'),
             'form': T('habits, routines and facts', 'hábitos, rutinas y hechos', 'Gewohnheiten, Routinen und Fakten')},
        ],
        'note': T('Every answer is a cake in two halves. The first half goes in the first gap, and the second half goes in the second gap.',
                  'Cada respuesta es un pastel en dos mitades. La primera mitad va en el primer hueco y la segunda mitad va en el segundo hueco.',
                  'Jede Antwort ist ein Kuchen in zwei Hälften. Die erste Hälfte gehört in die erste Lücke und die zweite Hälfte in die zweite Lücke.'),
        'button': T('TAKE THE FIRST PIECE', 'TOMA EL PRIMER TROZO', 'NIMM DAS ERSTE STÜCK'),
        'next': DATA['CAKE_ROUND'][0]['id']})
    easy('cake_intro')
    scenes.update(chain(DATA['CAKE_ROUND'], 2, 'choice2'))

    fork('choice2', '16_fork_two', 3,
         T('HOW WILL YOU ENTER THE PALACE?', '¿CÓMO ENTRARÁS EN EL PALACIO?', 'WIE KOMMST DU IN DEN PALAST?'),
         T('The Hatter knows a river that goes to the Teacup Compass. A friendly card guard can take Alice to the Clockmaker Mouse in prison, and to her Heart Gear.',
           'El Sombrerero conoce un río que lleva a la Brújula-Taza. Un guardia de cartas amable puede llevar a Alice hasta la Ratona Relojera en la prisión y hasta su Engranaje del Corazón.',
           'Der Hutmacher kennt einen Fluss, der zum Teetassenkompass führt. Eine freundliche Kartenwache kann Alice zur Uhrmachermaus im Gefängnis und zu ihrem Herzrad bringen.'),
         DATA['ACT_TWO'], 'boss_intro')

    scenes['boss_intro'] = place('boss_intro', {
        'kind': 'story', 'img': IMG('25_boss_reveal'),
        'k': T('THE SECRET · THE CLOCK IS STOPPING', 'EL SECRETO · EL RELOJ SE ESTÁ PARANDO', 'DAS GEHEIMNIS · DIE UHR BLEIBT STEHEN'),
        'title': T('THE WARDEN IS THE QUEEN\'S FEAR', 'EL GUARDIÁN ES EL MIEDO DE LA REINA', 'DER WÄCHTER IST DIE ANGST DER KÖNIGIN'),
        'story': T('Rose is the Queen\'s daughter, and she is trapped one second behind the clock. The Queen was afraid, so she asked the Clockmaker Mouse to stop tomorrow. The Queen\'s fear became the Warden, and the Warden took "now" from everybody. Alice is holding her two magic objects. They are keeping her friends moving, but only four more spells can stop the Warden.',
                   'Rose es la hija de la Reina y está atrapada un segundo detrás del reloj. La Reina tenía miedo, así que pidió a la Ratona Relojera que detuviera el mañana. El miedo de la Reina se convirtió en el Guardián, y el Guardián le quitó el «ahora» a todo el mundo. Alice está sujetando sus dos objetos mágicos: mantienen a sus amigos en movimiento, pero solo cuatro hechizos más pueden detener al Guardián.',
                   'Rose ist die Tochter der Königin, und sie ist eine Sekunde hinter der Uhr gefangen. Die Königin hatte Angst, also bat sie die Uhrmachermaus, das Morgen anzuhalten. Die Angst der Königin wurde zum Wächter, und der Wächter nahm allen das „Jetzt“. Alice hält gerade ihre zwei Zaubergegenstände. Sie halten ihre Freunde in Bewegung, aber nur vier weitere Zauber können den Wächter stoppen.'),
        'button': T('FIGHT FOR THE NEXT SECOND', 'LUCHA POR EL SIGUIENTE SEGUNDO', 'KÄMPFE UM DIE NÄCHSTE SEKUNDE'),
        'next': DATA['BOSS_ROUND'][0]['id']})
    easy('boss_intro')
    boss = chain(DATA['BOSS_ROUND'], 4, 'decision')
    boss[DATA['BOSS_ROUND'][-1]['id']].pop('relic', None)   # the third relic came from the cake gate
    scenes.update(boss)

    scenes['decision'] = place('decision', {
        'kind': 'choice', 'img': IMG('30_final_choice'),
        'k': T('FINAL DECISION · THREE ENDINGS', 'DECISIÓN FINAL · TRES FINALES', 'LETZTE ENTSCHEIDUNG · DREI ENDEN'),
        'title': T('REPAIR THE CROWN OR BREAK IT?', '¿REPARAR LA CORONA O ROMPERLA?', 'DIE KRONE REPARIEREN ODER ZERBRECHEN?'),
        'story': T('The Warden is gone, but the Crown still controls every clock in Wonderland. Alice can repair the Crown and trust the Queen. Or she can break it, and then everybody must start again somewhere new.',
                   'El Guardián ya no está, pero la Corona sigue controlando todos los relojes del País de las Maravillas. Alice puede reparar la Corona y confiar en la Reina. O puede romperla, y entonces todos tendrán que empezar de nuevo en otro lugar.',
                   'Der Wächter ist fort, aber die Krone steuert noch jede Uhr in Wunderland. Alice kann die Krone reparieren und der Königin vertrauen. Oder sie kann sie zerbrechen, und dann müssen alle woanders neu anfangen.'),
        'routes': [
            {'name': T('REPAIR THE CROWN', 'REPARAR LA CORONA', 'DIE KRONE REPARIEREN'),
             'desc': T('With 120 points or more you get the best ending.', 'Con 120 puntos o más consigues el mejor final.', 'Mit 120 Punkten oder mehr bekommst du das beste Ende.'),
             'target': 'end_restore', 'min': 120, 'else': 'end_flicker'},
            {'name': T('BREAK THE TIME MACHINE', 'ROMPER LA MÁQUINA DEL TIEMPO', 'DIE ZEITMASCHINE ZERSTÖREN'),
             'desc': T('Everybody is free, but nobody knows what happens next.', 'Todos son libres, pero nadie sabe qué pasa después.', 'Alle sind frei, aber niemand weiß, was dann passiert.'),
             'target': 'end_escape'},
        ]})
    easy('decision', routes=[dict(r, **EASY['scenes']['decision']['routes'][i])
                             for i, r in enumerate(scenes['decision']['routes'])])

    E = DATA['ENDINGS']
    for key, k, title in (
        ('restore', T('TRUE ENDING · QUEST COMPLETE', 'FINAL VERDADERO · MISIÓN COMPLETA', 'WAHRES ENDE · QUEST ABGESCHLOSSEN'), T('KEEPER OF NOW', 'GUARDIANA DEL AHORA', 'HÜTERIN DES JETZT')),
        ('escape',  T('FREEDOM ENDING · QUEST COMPLETE', 'FINAL DE LIBERTAD · MISIÓN COMPLETA', 'FREIHEITS-ENDE · QUEST ABGESCHLOSSEN'), T('A WORLD WITHOUT THE CROWN', 'UN MUNDO SIN LA CORONA', 'EINE WELT OHNE DIE KRONE')),
        ('flicker', T('HOPEFUL ENDING · QUEST COMPLETE', 'FINAL ESPERANZADOR · MISIÓN COMPLETA', 'HOFFNUNGSVOLLES ENDE · QUEST ABGESCHLOSSEN'), T('ONE MORE MORNING', 'UNA MAÑANA MÁS', 'NOCH EIN MORGEN')),
    ):
        e = E[key]
        scenes['end_' + key] = place('end_' + key, {
            'kind': 'ending', 'img': IMG(e['image']), 'success': key != 'flicker',
            'k': k, 'title': title, 'story': T(*SIMPLER_ENDING[key])})
        easy('end_' + key)

    labels = {
        'tiles':    T('MAGIC OBJECTS', 'OBJETOS MÁGICOS', 'ZAUBERGEGENSTÄNDE'),
        'relic':    T('MAGIC OBJECT FOUND · +{p} POINTS', 'OBJETO MÁGICO ENCONTRADO · +{p} PUNTOS', 'ZAUBERGEGENSTAND GEFUNDEN · +{p} PUNKTE'),
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
        'easy_labels': EASY['labels'], 'easy_tags': EASY['tags'],
        'start': 'cover', 'scenes': scenes,
        'endings': {'master': 'end_restore', 'complete': 'end_restore', 'missing': 'end_flicker', 'failed': 'end_escape'},
        'max': 160, 'points': 10, 'tiles': 3, 'chances': 0, 'total': 16, 'repair': True,
    }


if __name__ == '__main__':
    rpg.assemble(collapse(rpg.apply_translations(
        build(), os.path.join(HERE, 'rpg', 'wonderland-stolen-now', 'translations'))))
