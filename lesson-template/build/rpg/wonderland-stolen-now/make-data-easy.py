#!/usr/bin/env python3
"""Build data-easy.json — Wonderland's easy-English layer (rpg/README.md §7).

    node -e '...' > easy.json      # see below
    python make-data-easy.py easy.json data-easy.json

The export (Wonderland_Easy_English.html, 2026-09-07) is a structural twin of
the original: the same 24 question ids in the same order, the same options
byte-for-byte and the same answer indices, only the prose simplified. That is
what makes a runtime toggle safe rather than a second deck, and it is worth
re-measuring before trusting a revised export.

Its text sits in JavaScript, like the original's. To get `easy.json`, slice
the script from `const q =` to the end of `const PANEL_RIGHT` (lines 125-657
of the 2026-09-07 file), append

    console.log(JSON.stringify({ACT_ONE,CAKE_ROUND,ACT_TWO,BOSS_ROUND,ENDINGS}))

and run it under node. Do not grep the file itself: line 120 is a single
7 MB line of inlined base64 pictures.

The export carries its own Spanish and German for the story lines, the
endings and the narrative screens. The question titles, prompts and
explanations it left English-only, so those es/de are written here — that is
the hand work this script exists to preserve. Everything else is a
transcription of the export's render functions.
"""
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

EASY = json.load(open(sys.argv[1], encoding='utf-8'))


def T(en, es=None, de=None):
    o = {'en': en}
    if es: o['es'] = es
    if de: o['de'] = de
    return o


def F(en):
    """A formula line — the same in every language, as in the base builder."""
    return {'en': en, 'es': en, 'de': en}


# id: (title es, title de, ask es, ask de, why es, why de)
Q = {
'03_rabbit_run': ('¡SIGUE AL CONEJO!', 'FOLGE DEM KANINCHEN!',
    '¡Mira! El Conejo ___ hacia el valle.', 'Schau! Das Kaninchen ___ zum Tal.',
    '«Look!» indica que la acción ocurre ahora. The Rabbit = he. Usa he + is + running.',
    '„Look!“ zeigt, dass die Handlung gerade passiert. The Rabbit = he. Benutze he + is + running.'),
'04_bridge_build': ('CONSTRUYE UN PUENTE', 'BAUE EINE BRÜCKE',
    'Alice y el Conejo ___ un puente nuevo ahora mismo.', 'Alice und das Kaninchen ___ gerade eine neue Brücke.',
    'Alice and the Rabbit = they. Usa they + are + building para una acción que ocurre ahora.',
    'Alice and the Rabbit = they. Benutze they + are + building für eine Handlung, die gerade passiert.'),
'05_mouse_swim': ('SALVA A LA RATONA', 'RETTE DIE MAUS',
    '¿___ la Ratona nadando con el reloj?', '___ die Maus gerade mit der Uhr am Schwimmen?',
    'The Mouse = she. Empieza la pregunta con Is: Is she swimming?',
    'The Mouse = she. Beginne die Frage mit Is: Is she swimming?'),
'06_guard_chase': ('ESCAPA DE LOS GUARDIAS', 'ENTKOMME DEN WACHEN',
    'Elige la oración correcta con «not».', 'Wähle den richtigen Satz mit „not“.',
    'The guards = they. Usa they + are not + catching. Are not puede acortarse a aren’t.',
    'The guards = they. Benutze they + are not + catching. Are not kann zu aren’t werden.'),
'07_cat_vanish': ('¿DÓNDE ESTÁ EL GATO?', 'WO IST DIE KATZE?',
    '¡Mira! El Gato ___ entre los bloques.', 'Schau! Die Katze ___ zwischen den Blöcken.',
    'The Cat = it. Usa it + is + disappearing para una acción que ocurre ahora.',
    'The Cat = it. Benutze it + is + disappearing für eine Handlung, die gerade passiert.'),
'08_tree_climb': ('SUBE AL ÁRBOL', 'KLETTERE AUF DEN BAUM',
    'Alice está ___ al árbol.', 'Alice ___ gerade auf den Baum.',
    'Añade -ing a climb: climbing. La b no se dobla.',
    'Hänge -ing an climb an: climbing. Das b wird nicht verdoppelt.'),
'09_mirror_guards': ('PASA JUNTO A LOS GUARDIAS', 'KOMM AN DEN WACHEN VORBEI',
    '¿Qué ___ mirando los guardias?', 'Was ___ die Wachen gerade?',
    'The guards = they. Usa What + are + they + watching?',
    'The guards = they. Benutze What + are + they + watching?'),
'10_mirror_key': ('COGE LA LLAVE MÁGICA', 'NIMM DEN ZAUBERSCHLÜSSEL',
    'Alice dice: «I ___ taking the key».', 'Alice sagt: „I ___ taking the key.“',
    'Con I se usa am: I am taking the key.',
    'Nach I steht am: I am taking the key.'),
'12_cake_growing': ('ALICE SE ESTÁ HACIENDO MÁS ALTA', 'ALICE WIRD GERADE GRÖSSER',
    'Alice normalmente ___ pequeña, pero ahora mismo ___ más alta.', 'Alice ___ normalerweise klein, aber gerade ___ sie größer.',
    'Usually indica lo normal: stays. Right now indica lo que está cambiando: is getting.',
    'Usually zeigt, was normal ist: stays. Right now zeigt, was sich gerade ändert: is getting.'),
'13_cake_routine': ('CADA MAÑANA / AHORA', 'JEDEN MORGEN / JETZT',
    'Cada mañana el Conejo ___ su reloj, pero ahora ___ hacia la puerta.', 'Jeden Morgen ___ das Kaninchen seine Uhr, aber jetzt ___ es zum Tor.',
    'Every morning indica una rutina: checks. Now indica una acción que ocurre ahora: is running.',
    'Every morning zeigt eine Routine: checks. Now zeigt eine Handlung, die gerade passiert: is running.'),
'14_cake_contrast': ('¿TÉ PARA UN BARCO?', 'TEE FÜR EIN BOOT?',
    'El Sombrerero normalmente ___ té, pero ahora mismo lo ___ en el motor.', 'Der Hutmacher ___ normalerweise Tee, aber gerade ___ er ihn in den Motor.',
    'Usually indica un hábito: drinks. Right now indica una acción que ocurre ahora: is pouring. Pour significa verter un líquido en algo.',
    'Usually zeigt eine Gewohnheit: drinks. Right now zeigt eine Handlung, die gerade passiert: is pouring. Pour heißt, eine Flüssigkeit in etwas zu gießen.'),
'15_cake_gate': ('ABRE LA PUERTA MÁGICA', 'ÖFFNE DAS ZAUBERTOR',
    'La puerta normalmente ___ a las doce. ¡Mira! Ahora ___.', 'Das Tor ___ normalerweise um zwölf Uhr. Schau! Jetzt ___ es.',
    'Usually indica la hora habitual de apertura: opens. «Look!» indica lo que ocurre ahora: is opening.',
    'Usually zeigt die normale Öffnungszeit: opens. „Look!“ zeigt, was jetzt passiert: is opening.'),
'17_boat_engine': ('HAZ QUE EL BARCO AVANCE', 'BRING DAS BOOT IN FAHRT',
    'El Sombrerero está ___ té en el motor.', 'Der Hutmacher ___ gerade Tee in den Motor.',
    'Para una acción que ocurre ahora, usa is + verbo-ing: is pouring. Pour significa verter un líquido en algo.',
    'Für eine Handlung, die gerade passiert: is + Verb-ing, also is pouring. Pour heißt, eine Flüssigkeit in etwas zu gießen.'),
'18_reverse_river': ('EL RÍO VA HACIA ATRÁS', 'DER FLUSS FLIESST RÜCKWÄRTS',
    'El agua ___ hacia atrás en este momento.', 'Das Wasser ___ im Moment rückwärts.',
    'At the moment significa ahora. Usa the water + is + moving.',
    'At the moment bedeutet jetzt. Benutze the water + is + moving.'),
'19_stone_ear': ('¡QUEDAOS EN SILENCIO!', 'SEID LEISE!',
    'Nosotros ___ ahora. Nos escondemos en silencio.', 'Wir ___ jetzt. Wir verstecken uns leise.',
    'Con we se usa are not + talking. Are not puede acortarse a aren’t: We aren’t talking.',
    'Nach we steht are not + talking. Are not kann zu aren’t werden: We aren’t talking.'),
'20_compass_island': ('ENCUENTRA A LA NIÑA PERDIDA', 'FINDE DAS VERSCHWUNDENE MÄDCHEN',
    'Elige la pregunta correcta.', 'Wähle die richtige Frage.',
    'Empieza con What, luego is y luego the compass: What is the compass showing?',
    'Beginne mit What, dann is, dann the compass: What is the compass showing?'),
'21_prison_gears': ('BAJA BAJO EL PALACIO', 'GEH UNTER DEN PALAST',
    'Las ruedas de metal ___ alrededor de las salas.', 'Die Metallräder ___ um die Räume.',
    'The wheels = they. Usa they + are + turning.',
    'The wheels = they. Benutze they + are + turning.'),
'22_clockmaker_trapped': ('AYUDA A LA RATONA', 'HILF DER MAUS',
    'La Ratona está ___ detrás de la rueda.', 'Die Maus ___ gerade hinter dem Rad.',
    'Aquí lie significa estar tumbado, no mentir. Lie cambia a lying: She is lying behind the wheel.',
    'Hier heißt lie „flach liegen“, nicht „lügen“. Aus lie wird lying: She is lying behind the wheel.'),
'23_broken_drill': ('LA HERRAMIENTA ESTÁ ROTA', 'DAS WERKZEUG IST KAPUTT',
    'Elige la oración correcta con «not».', 'Wähle den richtigen Satz mit „not“.',
    'The drill = it. Usa is not + working. Is not puede acortarse a isn’t: The drill isn’t working.',
    'The drill = it. Benutze is not + working. Is not kann zu isn’t werden: The drill isn’t working.'),
'24_heart_gear': ('UN REGALO DE LA RATONA', 'EIN GESCHENK VON DER MAUS',
    'Alice y la Ratona ___ juntas la rueda mágica.', 'Alice und die Maus ___ das Zauberrad gemeinsam.',
    'Alice and the Mouse = they. Usa they + are + carrying.',
    'Alice and the Mouse = they. Benutze they + are + carrying.'),
'26_freeze_attack': ('¡DETÉN AL GUARDIÁN!', 'STOPPE DEN WÄCHTER!',
    'El Guardián ___ una ola mágica ahora.', 'Der Wächter ___ jetzt eine Zauberwelle.',
    'Now indica que la acción ocurre ahora. Usa the Warden + is + sending.',
    'Now zeigt, dass die Handlung gerade passiert. Benutze the Warden + is + sending.'),
'27_shards_crown': ('TRABAJAD JUNTOS', 'ARBEITET ZUSAMMEN',
    'Alice y sus amigos ___ juntos en este momento.', 'Alice und ihre Freunde ___ im Moment zusammen.',
    'Alice and her friends = they. At the moment significa ahora. Usa they + are + fighting.',
    'Alice and her friends = they. At the moment bedeutet jetzt. Benutze they + are + fighting.'),
'28_queen_truth': ('LA REINA LO ENTIENDE', 'DIE KÖNIGIN VERSTEHT ES',
    '¿Qué oración es correcta?', 'Welcher Satz ist richtig?',
    'Understand se usa normalmente en presente simple, aunque hablemos de ahora. The Queen = she, así que añade -s: understands.',
    'Understand steht normalerweise im Present Simple, auch wenn es um jetzt geht. The Queen = she, also mit -s: understands.'),
'29_warden_break': ('EL GUARDIÁN DESAPARECE', 'DER WÄCHTER VERSCHWINDET',
    'Elige la pregunta correcta.', 'Wähle die richtige Frage.',
    'Empieza con Why, luego is y luego the Warden: Why is the Warden breaking apart? Breaking apart significa romperse en pedazos.',
    'Beginne mit Why, dann is, dann the Warden: Why is the Warden breaking apart? Breaking apart heißt in Stücke zerbrechen.'),
}

# base route name -> (easy name es, easy name de)
ROUTE = {
    'Follow the Rabbit':     ('SIGUE AL CONEJO', 'FOLGE DEM KANINCHEN'),
    'Follow the Cat':        ('SIGUE AL GATO', 'FOLGE DER KATZE'),
    'Take the Teacup Boat':  ('TOMA EL BARCO-TAZA', 'NIMM DAS TEETASSENBOOT'),
    'Enter the Gear Prison': ('RESCATA A LA RATONA', 'RETTE DIE MAUS'),
}
# the export renamed this branch; ROUTE_NAMES in the builder is keyed by the base name
RENAME = {'Enter the Gear Prison': 'Rescue the Mouse'}

# the easy detail lines, whose es/de the export supplied for the hard version only
ROUTE_DESC = {
    'Follow the Rabbit':     ('Ayuda al Conejo a cruzar un puente roto. Encuentra un reloj de plata mágico.',
                              'Hilf dem Kaninchen über eine kaputte Brücke. Finde eine magische Silberuhr.'),
    'Follow the Cat':        ('Sigue al Gato entre los árboles. Encuentra una llave de espejo mágica.',
                              'Folge der Katze durch die Bäume. Finde einen magischen Spiegelschlüssel.'),
    'Take the Teacup Boat':  ('Viaja en barco con el Sombrerero. Encuentra una brújula mágica.',
                              'Fahre mit dem Hutmacher im Boot. Finde einen magischen Kompass.'),
    'Enter the Gear Prison': ('Ayuda a la Ratona a escapar de la prisión. Encuentra una rueda de metal mágica.',
                              'Hilf der Maus aus dem Gefängnis. Finde ein magisches Metallrad.'),
}

ENDING_HEAD = {
    'restore': (T('WONDERLAND SAVED · GAME COMPLETE', 'PAÍS DE LAS MARAVILLAS A SALVO · JUEGO COMPLETO', 'WUNDERLAND GERETTET · SPIEL BEENDET'),
                T('WONDERLAND IS SAFE!', '¡EL PAÍS DE LAS MARAVILLAS ESTÁ A SALVO!', 'WUNDERLAND IST SICHER!')),
    'escape':  (T('A NEW HOME · GAME COMPLETE', 'UN NUEVO HOGAR · JUEGO COMPLETO', 'EIN NEUES ZUHAUSE · SPIEL BEENDET'),
                T('A NEW HOME', 'UN NUEVO HOGAR', 'EIN NEUES ZUHAUSE')),
    'flicker': (T('MORE WORK TO DO · GAME COMPLETE', 'QUEDA TRABAJO POR HACER · JUEGO COMPLETO', 'ES BLEIBT ARBEIT · SPIEL BEENDET'),
                T('ONE MORE ADVENTURE', 'UNA AVENTURA MÁS', 'NOCH EIN ABENTEUER')),
}

KICKER = {
    1: T('PART 1 · FIND THE FIRST MAGIC OBJECT', 'PARTE 1 · ENCUENTRA EL PRIMER OBJETO MÁGICO', 'TEIL 1 · FINDE DEN ERSTEN ZAUBERGEGENSTAND'),
    2: T('PART 2 · THE MAGIC CAKE CHALLENGE', 'PARTE 2 · EL RETO DEL PASTEL MÁGICO', 'TEIL 2 · DIE ZAUBERKUCHEN-PRÜFUNG'),
    3: T('PART 3 · FIND THE SECOND MAGIC OBJECT', 'PARTE 3 · ENCUENTRA EL SEGUNDO OBJETO MÁGICO', 'TEIL 3 · FINDE DEN ZWEITEN ZAUBERGEGENSTAND'),
    4: T('PART 4 · STOP THE WARDEN', 'PARTE 4 · DETÉN AL GUARDIÁN', 'TEIL 4 · STOPPE DEN WÄCHTER'),
}
ACT_OF = {}


def questions():
    out = {}
    order = []
    for k, act in (('ACT_ONE', 1), ('ACT_TWO', 3)):
        for br in EASY[k]:
            for qd in br['questions']:
                order.append((qd, act))
    for qd in EASY['CAKE_ROUND']:
        order.append((qd, 2))
    for qd in EASY['BOSS_ROUND']:
        order.append((qd, 4))
    for qd, act in order:
        es_t, de_t, es_a, de_a, es_w, de_w = Q[qd['id']]
        out[qd['id']] = {
            'k':     KICKER[act],
            'title': T(qd['title'].upper(), es_t, de_t),
            'story': T(qd['story'], qd['es'], qd['de']),
            'ask':   T(qd['ask'], es_a, de_a),
            'why':   T(qd['why'], es_w, de_w),
        }
    return out


def routes():
    out = {}
    for k in ('ACT_ONE', 'ACT_TWO'):
        for br in EASY[k]:
            base = next((b for b, e in RENAME.items() if e == br['name']), br['name'])
            es_n, de_n = ROUTE[base]
            es_d, de_d = ROUTE_DESC[base]
            out[base] = {'name': T(br['name'].upper(), es_n, de_n),
                         'desc': T(br['detail'], es_d, de_d)}
    return out


def endings():
    out = {}
    for key, e in EASY['ENDINGS'].items():
        k, title = ENDING_HEAD[key]
        out['end_' + key] = {'k': k, 'title': title, 'story': T(e['story'], e['es'], e['de'])}
    return out


# The narrative screens the export keeps inside its render functions,
# transcribed with the de/es it ships beside them.
SCENES = {
  'cover': {
    'k': T('ENGLISH ADVENTURE · EASY ENGLISH · 16 QUESTIONS',
           'AVENTURA EN INGLÉS · INGLÉS FÁCIL · 16 PREGUNTAS',
           'ENGLISCH-ABENTEUER · EINFACHES ENGLISCH · 16 FRAGEN'),
    'title': T('THE STOLEN NOW', 'EL AHORA ROBADO', 'DAS GESTOHLENE JETZT'),
    'story': T('Time is going wrong in Wonderland. The same afternoon keeps starting again. Soon, everyone will stop moving. Help Alice fix the palace clock and save her friends.',
               'En el País de las Maravillas, la misma tarde empieza una y otra vez. Pronto nadie podrá moverse. Ayuda a Alice a reparar el reloj del palacio y a salvar a sus amigos.',
               'In Wunderland beginnt derselbe Nachmittag immer wieder. Bald können sich alle nicht mehr bewegen. Hilf Alice, die Palastuhr zu reparieren und ihre Freunde zu retten.'),
    'rules': [T('+10 FIRST TRY', '+10 A LA PRIMERA', '+10 BEIM ERSTEN VERSUCH'),
              T('3 MAGIC OBJECTS', '3 OBJETOS MÁGICOS', '3 ZAUBERGEGENSTÄNDE'),
              T('16 QUESTIONS', '16 PREGUNTAS', '16 FRAGEN')],
    'start': T('START THE ADVENTURE', 'EMPEZAR LA AVENTURA', 'DAS ABENTEUER STARTEN'),
    'small': T('One player · easy English · two paths to choose · three endings',
               'Un jugador · inglés fácil · dos caminos a elegir · tres finales',
               'Ein Spieler · einfaches Englisch · zwei Wege zur Wahl · drei Enden'),
  },
  'prologue': {
    'k': T('THE STORY · TIME IS IN DANGER', 'LA HISTORIA · EL TIEMPO ESTÁ EN PELIGRO', 'DIE GESCHICHTE · DIE ZEIT IST IN GEFAHR'),
    'title': T('SOMEONE STOLE THE MAGIC CRYSTAL!', '¡ALGUIEN ROBÓ EL CRISTAL MÁGICO!', 'JEMAND HAT DEN ZAUBERKRISTALL GESTOHLEN!'),
    'story': T('The Time Warden, a dangerous shadow, steals the crystal from the palace clock. The crystal makes time work. Now people are stopping in the street. Even the rain is stopping in the air! Alice can still move. The Rabbit tells her what to do: find two magic objects to power the clock, open the magic gate, then go to the Queen’s palace and stop the Warden.',
               'El Guardián del Tiempo, una sombra peligrosa, roba el cristal del reloj del palacio. El cristal hace funcionar el tiempo. Ahora las personas se quedan inmóviles en la calle. ¡Incluso la lluvia se queda parada en el aire! Alice todavía puede moverse. El Conejo le dice qué hacer: encuentra dos objetos mágicos para el reloj, abre la puerta mágica y llega hasta la Reina para detener al Guardián.',
               'Der Zeitwächter, ein gefährlicher Schatten, stiehlt den Kristall aus der Palastuhr. Der Kristall lässt die Zeit laufen. Jetzt bleiben die Menschen auf der Straße stehen. Sogar der Regen bleibt in der Luft stehen! Alice kann sich noch bewegen. Das Kaninchen sagt ihr, was zu tun ist: Finde zwei magische Gegenstände für die Uhr, öffne das Zaubertor und erreiche die Königin, um den Wächter zu stoppen.'),
  },
  'rules': {
    'k': T('GRAMMAR HELP · BEFORE YOU START', 'AYUDA DE GRAMÁTICA · ANTES DE EMPEZAR', 'GRAMMATIKHILFE · BEVOR DU STARTEST'),
    'title': T('NOW OR EVERY DAY?', '¿AHORA O CADA DÍA?', 'JETZT ODER JEDEN TAG?'),
    'story': T('Use the present continuous for an action happening now: “Alice is running.” Use the present simple for things we do regularly and for facts: “I play every day.” “A rabbit has long ears.”',
               'Usa el presente continuo para una acción que ocurre ahora: «Alice is running». Usa el presente simple para lo que hacemos con regularidad y para los hechos: «I play every day». «A rabbit has long ears».',
               'Benutze das Present Continuous für eine Handlung, die gerade passiert: „Alice is running.“ Benutze das Present Simple für Regelmäßiges und für Fakten: „I play every day.“ „A rabbit has long ears.“'),
    'rules': [
      {'name': T('FORM · AM / IS / ARE + VERB-ING', 'FORMA · AM / IS / ARE + VERBO-ING', 'FORM · AM / IS / ARE + VERB-ING'),
       'form': F('I am playing · He / She / It is playing · You / We / They are playing')},
      {'name': T('NEGATIVE AND QUESTION', 'NEGACIÓN Y PREGUNTA', 'VERNEINUNG UND FRAGE'),
       'form': T('Alice is not sleeping. · Is Alice sleeping? Yes, she is. / No, she isn’t.',
                 'Alice no está durmiendo. · ¿Está durmiendo Alice? Sí. / No.',
                 'Alice schläft nicht. · Schläft Alice gerade? Ja. / Nein.')},
      {'name': T('SPELLING', 'ORTOGRAFÍA', 'SCHREIBWEISE'),
       'form': F('look → looking · make → making · run → running · lie → lying')},
      {'name': T('NOW CLUES', 'PISTAS DE «AHORA»', 'JETZT-SIGNALE'),
       'form': F('now · right now · at the moment · Look! · Listen!')},
      {'name': T('PRESENT SIMPLE · EVERY DAY AND FACTS', 'PRESENTE SIMPLE · CADA DÍA Y HECHOS', 'PRESENT SIMPLE · JEDEN TAG UND FAKTEN'),
       'form': T('I play every day. · She plays every day. · I know the answer.',
                 'I play every day. · She plays every day. · I know the answer. (con he/she/it se añade -s)',
                 'I play every day. · She plays every day. · I know the answer. (bei he/she/it kommt -s dazu)')},
    ],
    'note': T('Read the story, then choose an answer. A correct first answer gives you 10 points. If you make a mistake, read the help and try again — you can still finish the game. There are 16 questions and 160 possible points.',
              'Lee la historia y elige una respuesta. Una primera respuesta correcta vale 10 puntos. Si te equivocas, lee la ayuda e inténtalo otra vez: puedes terminar el juego igualmente. Hay 16 preguntas y 160 puntos posibles.',
              'Lies die Geschichte und wähle eine Antwort. Eine erste richtige Antwort gibt 10 Punkte. Bei einem Fehler liest du die Hilfe und versuchst es noch einmal – du kannst das Spiel trotzdem beenden. Es gibt 16 Fragen und 160 mögliche Punkte.'),
    'button': T('CHOOSE A PATH', 'ELIGE UN CAMINO', 'WÄHLE EINEN WEG'),
  },
  'choice1': {
    'k': T('CHOOSE A PATH · BOTH PATHS CAN WORK', 'ELIGE UN CAMINO · LOS DOS SIRVEN', 'WÄHLE EINEN WEG · BEIDE FUNKTIONIEREN'),
    'title': T('WHICH OBJECT WILL YOU FIND FIRST?', '¿QUÉ OBJETO ENCONTRARÁS PRIMERO?', 'WELCHEN GEGENSTAND FINDEST DU ZUERST?'),
    'story': T('You need one magic object from this area. Follow the Rabbit to find a silver watch, or follow the Cat to find a mirror key. Either object can help fix the clock.',
               'Necesitas un objeto mágico de esta zona. Sigue al Conejo para encontrar un reloj de plata, o sigue al Gato para encontrar una llave de espejo. Cualquiera de los dos sirve para reparar el reloj.',
               'Du brauchst einen Zaubergegenstand aus dieser Gegend. Folge dem Kaninchen zu einer Silberuhr oder der Katze zu einem Spiegelschlüssel. Beide helfen, die Uhr zu reparieren.'),
  },
  'cake_intro': {
    'k': T('PART 2 · THE MAGIC CAKE CHALLENGE', 'PARTE 2 · EL RETO DEL PASTEL MÁGICO', 'TEIL 2 · DIE ZAUBERKUCHEN-PRÜFUNG'),
    'title': T('PINK CAKE OR BLUE CAKE?', '¿PASTEL ROSA O PASTEL AZUL?', 'ROSA ODER BLAUER KUCHEN?'),
    'story': T('A magic gate blocks the path. Answer four questions to open it. Pink = happening now: “Alice is running.” Blue = usual actions or facts: “Alice runs every day.”',
               'Una puerta mágica bloquea el camino. Responde cuatro preguntas para abrirla. Rosa = ocurre ahora: «Alice is running». Azul = acciones habituales o hechos: «Alice runs every day».',
               'Ein Zaubertor versperrt den Weg. Beantworte vier Fragen, um es zu öffnen. Rosa = passiert gerade: „Alice is running.“ Blau = gewohnte Handlungen oder Fakten: „Alice runs every day.“'),
    'rules': [
      {'name': T('PINK · PRESENT CONTINUOUS', 'ROSA · PRESENTE CONTINUO', 'ROSA · PRESENT CONTINUOUS'),
       'form': T('am / is / are + verb-ing', 'am / is / are + verbo-ing', 'am / is / are + Verb-ing')},
      {'name': T('BLUE · PRESENT SIMPLE', 'AZUL · PRESENTE SIMPLE', 'BLAU · PRESENT SIMPLE'),
       'form': T('every day · usually · facts', 'cada día · normalmente · hechos', 'jeden Tag · normalerweise · Fakten')},
    ],
    'note': T('Each answer has two parts. Read from left to right. Left part goes in the first gap. Right part goes in the second gap. Click the answer with both correct words.',
              'Cada respuesta tiene dos partes. Lee de izquierda a derecha. La parte izquierda va en el primer hueco. La parte derecha va en el segundo. Pulsa la respuesta con las dos palabras correctas.',
              'Jede Antwort hat zwei Teile. Lies von links nach rechts. Der linke Teil gehört in die erste Lücke, der rechte in die zweite. Klicke die Antwort mit beiden richtigen Wörtern.'),
    'button': T('START THE CAKE QUESTIONS', 'EMPEZAR LAS PREGUNTAS DEL PASTEL', 'DIE KUCHENFRAGEN STARTEN'),
  },
  'choice2': {
    'k': T('CHOOSE A PATH · BOTH PATHS CAN WORK', 'ELIGE UN CAMINO · LOS DOS SIRVEN', 'WÄHLE EINEN WEG · BEIDE FUNKTIONIEREN'),
    'title': T('HOW WILL YOU ENTER THE PALACE?', '¿CÓMO ENTRARÁS EN EL PALACIO?', 'WIE KOMMST DU IN DEN PALAST?'),
    'story': T('You need one more magic object. Take a boat with the Hatter to find a compass, or help the Mouse escape from prison to get a magic metal wheel. Either object can help.',
               'Necesitas un objeto mágico más. Toma un barco con el Sombrerero para encontrar una brújula, o ayuda a la Ratona a escapar de la prisión para conseguir una rueda de metal mágica. Cualquiera de los dos sirve.',
               'Du brauchst noch einen Zaubergegenstand. Fahre mit dem Hutmacher im Boot zu einem Kompass, oder hilf der Maus aus dem Gefängnis und hol ein magisches Metallrad. Beide helfen.'),
  },
  'boss_intro': {
    'k': T('THE SECRET · WHY TIME IS STOPPING', 'EL SECRETO · POR QUÉ SE DETIENE EL TIEMPO', 'DAS GEHEIMNIS · WARUM DIE ZEIT STEHEN BLEIBT'),
    'title': T('THE QUEEN WANTS TO SAVE HER DAUGHTER', 'LA REINA QUIERE SALVAR A SU HIJA', 'DIE KÖNIGIN WILL IHRE TOCHTER RETTEN'),
    'story': T('Rose is the Queen’s daughter. The Queen is afraid that something bad will happen to her. She asks the Mouse to build a machine that stops time. It is called the Crown. But the magic goes wrong: Rose becomes trapped behind a magic wall. The Queen’s fear creates the Time Warden. Alice holds up her two magic objects. They help her keep moving. Answer four more questions to stop the Warden and free Rose.',
               'Rose es la hija de la Reina. La Reina teme que le pase algo malo. Le pide a la Ratona que construya una máquina que detenga el tiempo. Se llama la Corona. Pero la magia sale mal: Rose queda atrapada detrás de una pared mágica. El miedo de la Reina crea al Guardián del Tiempo. Alice levanta sus dos objetos mágicos: la ayudan a seguir moviéndose. Responde cuatro preguntas más para detener al Guardián y liberar a Rose.',
               'Rose ist die Tochter der Königin. Die Königin hat Angst, dass ihr etwas zustößt. Sie bittet die Maus, eine Maschine zu bauen, die die Zeit anhält. Sie heißt die Krone. Aber die Magie geht schief: Rose ist hinter einer magischen Wand gefangen. Die Angst der Königin erschafft den Zeitwächter. Alice hebt ihre zwei Zaubergegenstände hoch: Sie halten sie in Bewegung. Beantworte vier weitere Fragen, um den Wächter zu stoppen und Rose zu befreien.'),
    'button': T('HELP ALICE STOP THE WARDEN', 'AYUDA A ALICE A DETENER AL GUARDIÁN', 'HILF ALICE, DEN WÄCHTER ZU STOPPEN'),
  },
  'decision': {
    'k': T('YOUR LAST CHOICE · THREE POSSIBLE ENDINGS', 'TU ÚLTIMA ELECCIÓN · TRES FINALES POSIBLES', 'DEINE LETZTE WAHL · DREI MÖGLICHE ENDEN'),
    'title': T('FIX THE MACHINE OR BREAK IT?', '¿REPARAR LA MÁQUINA O ROMPERLA?', 'DIE MASCHINE REPARIEREN ODER ZERSTÖREN?'),
    'story': T('The Warden is gone. Rose still needs to get out. If Alice fixes the time machine, everyone can stay in Wonderland. If she breaks it, everyone must escape to a new home.',
               'El Guardián ya no está. Rose todavía necesita salir. Si Alice repara la máquina del tiempo, todos pueden quedarse en el País de las Maravillas. Si la rompe, todos tendrán que escapar a un nuevo hogar.',
               'Der Wächter ist weg. Rose muss noch heraus. Wenn Alice die Zeitmaschine repariert, können alle in Wunderland bleiben. Wenn sie sie zerstört, müssen alle in ein neues Zuhause fliehen.'),
    'routes': [
      {'name': T('FIX THE TIME MACHINE', 'REPARAR LA MÁQUINA DEL TIEMPO', 'DIE ZEITMASCHINE REPARIEREN'),
       'desc': T('120 points or more: fix it completely. Below 120: save Rose, but the machine still needs work.',
                 'Con 120 puntos o más la reparas del todo. Con menos de 120 salvas a Rose, pero la máquina aún necesita trabajo.',
                 'Mit 120 Punkten oder mehr reparierst du sie ganz. Unter 120 rettest du Rose, aber die Maschine braucht noch Arbeit.')},
      {'name': T('BREAK THE TIME MACHINE', 'ROMPER LA MÁQUINA DEL TIEMPO', 'DIE ZEITMASCHINE ZERSTÖREN'),
       'desc': T('Everyone escapes to a new home. You can choose this with any score.',
                 'Todos escapan a un nuevo hogar. Puedes elegirlo con cualquier puntuación.',
                 'Alle fliehen in ein neues Zuhause. Das kannst du mit jeder Punktzahl wählen.')},
    ],
  },
}

# Labels the easy version rewords too.
LABELS = {
    'tiles':    T('MAGIC OBJECTS', 'OBJETOS MÁGICOS', 'ZAUBERGEGENSTÄNDE'),
    'relic':    T('MAGIC OBJECT FOUND · +{p} POINTS', 'OBJETO MÁGICO ENCONTRADO · +{p} PUNTOS', 'ZAUBERGEGENSTAND GEFUNDEN · +{p} PUNKTE'),
    'correct':  T('CORRECT FIRST TRY · +{p} POINTS', 'CORRECTO A LA PRIMERA · +{p} PUNTOS', 'RICHTIG BEIM ERSTEN VERSUCH · +{p} PUNKTE'),
    'progress': T('QUESTIONS', 'PREGUNTAS', 'FRAGEN'),
    'review':   T('LOOK AGAIN AT THE QUESTIONS YOU TRIED TWICE', 'REPASA LAS PREGUNTAS QUE INTENTASTE DOS VECES', 'SIEH DIR DIE FRAGEN NOCH EINMAL AN, DIE DU ZWEIMAL VERSUCHT HAST'),
    'perfect':  T('You answered all 16 questions correctly on your first try!', '¡Respondiste bien las 16 preguntas a la primera!', 'Du hast alle 16 Fragen beim ersten Versuch richtig beantwortet!'),
    'restart':  T('PLAY A DIFFERENT PATH', 'JUEGA OTRO CAMINO', 'EINEN ANDEREN WEG SPIELEN'),
}

out = {'questions': questions(), 'routes': routes(), 'scenes': SCENES,
       'endings': endings(), 'labels': LABELS,
       'tags': {'a': T('PINK · NOW', 'ROSA · AHORA', 'ROSA · JETZT'),
                'b': T('BLUE · EVERY DAY', 'AZUL · CADA DÍA', 'BLAU · JEDEN TAG')}}
json.dump(out, open(sys.argv[2], 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1, sort_keys=False)
print('wrote %s — %d questions, %d routes, %d scenes, %d endings'
      % (sys.argv[2], len(out['questions']), len(out['routes']), len(out['scenes']), len(out['endings'])))
