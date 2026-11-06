# -*- coding: utf-8 -*-
"""Active & Passive Voice — Refinery Quiz Part 2 (B2). House style 2, 16 slides.

Rebuilt 2026-11-06 from `active_passive_refinery_quiz_part2.html`, a
ten-question scrolling quiz for a refinery fire-team deputy lead (FRTU
Grammar Series). All ten questions are kept: six multiple choice, two
gap-fills, two sentence builds. The art is Part 1's own four plates in
refinery/, reused as the revamp list said ("wire, order nothing"): no
stand-ins.

Fixed:
  * Q6's key ("I suspended the hot work permit at 16:00 pending
    investigation") was the only long option. The distractors now carry
    the same length.
  * Q10 offered "Sentence A" … "Sentence E" while the deck labels its own
    options A-D after shuffling, so "Sentence D" could sit beside the
    letter B. The options are now the sentences themselves (four of them).
    Its explanation also says WHY "was arrive" fails: ARRIVE takes no
    object, so it has no passive at all.
  * The two sentence builds dealt every word as a separate piece,
    including the full stop. They are now chunked at the joints being
    taught (WAS / CHECKED, WILL / BE / BRIEFED), each with a decoy.
Added: the passive forms and the active-or-passive choice as rule cards,
two speaking fields and the activation.

Run from the repo root:  py lesson-template/build/build_refinery_quiz2.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='active_passive_refinery_quiz_part2.html',
    title='Active & Passive Voice — Refinery Quiz Part 2 (B2)',
    folder='refinery',
    scheme='slate',
    art={},              # every slot is one of Part 1's plates
    act='refinery-scene-1',
)


def q(stem, options, n, ctx=None):
    d = dict(stem=stem, options=options, correct=0, why='w%d' % n)
    if ctx:
        d['ctx'] = ctx
    return d


VOICE = [
    q('Which radio message is clearest?', [
        'Request a second hose line from the south gate immediately.',
        'A second hose line is to be requested from the south gate by you immediately.',
        'It has been decided that a second hose line should be requested.',
        'The requesting of a second hose line from the south gate is recommended.'], 1, 'c1'),
    q('Choose the version with correct and consistent passive voice.', [
        'At 07:15, a gas leak was discovered at the CDU inlet. The control room was notified and the valve was isolated manually.',
        'At 07:15, I discovered a gas leak at the CDU inlet. The control room was notified and we isolated the valve manually.',
        'At 07:15, a gas leak was discovered at the CDU inlet. The control room was notified and we isolated the valve manually.',
        'At 07:15, someone discovered a gas leak at the CDU inlet and the control room was notified by us.'], 2, 'c2'),
    q('Which sentence most clearly assigns responsibility for the action?', [
        'I suspended the hot work permit at 16:00 pending investigation.',
        'The hot work permit was suspended at 16:00 pending an investigation.',
        'Hot work was suspended at 16:00 by someone, pending investigation.',
        'The suspension of the hot work permit was carried out at 16:00.'], 6, 'c6'),
    q('Which sentence combines active and passive voice best?', [
        'The scaffold has been erected and confirmed safe. We will start work at 06:00.',
        'The scaffold has been erected, and it was confirmed safe by us and we will start work at 06:00.',
        'We erected the scaffold and it was confirmed safe by us. The start of work will be at 06:00.',
        'The scaffold was being erected and safety was confirmed and work start will be 06:00.'], 8, 'c8'),
]
FORM = [
    q('Which sentence uses the present perfect passive correctly?', [
        'The bund wall has been repaired.', 'The bund wall is repaired last week.',
        'The bund wall was been repaired.', 'The bund wall have been repaired.'], 4),
    q('Which sentence from the investigation report has an incorrect passive?', [
        'The incident commander was arrive on scene at 14:35.',
        'The leak was first detected at 14:22 by the area operator.',
        'All non-essential personnel were evacuated to the muster point.',
        'A full investigation has been launched by the HSE team.'], 10),
]

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'When do you use the radio at work, and what do you say?',
        'What goes into a good shift handover?',
        'Who reads your incident reports?',
        'Is it better to say “I did it” or “It was done”? When?',
        'What must be checked before a unit restarts?',
        'What makes a message clear under pressure?',
    ], 'refinery-scene-0', 3),
    ('rules', 'eR', 'rFormT', [
        ('is / are + participle', ['rF1'], 'The pump <strong>is serviced</strong> twice a year.'),
        ('was / were + participle', ['rF2'], 'All equipment <strong>was checked</strong>.'),
        ('has / have been + participle', ['rF3'], 'The bund wall <strong>has been repaired</strong>.'),
        ('must / will + be + participle', ['rF4'], 'Detectors <strong>must be calibrated</strong>. Staff <strong>will be briefed</strong>.'),
    ], None),
    ('rules', 'eR', 'rUseT', [
        ('pActive', ['rU1', 'rU2'], '<strong>Request</strong> a second hose line. <strong>I suspended</strong> the permit.'),
        ('pPassive', ['rU3', 'rU4'], 'A gas leak <strong>was discovered</strong> at 07:15.'),
        ('pMix', ['rU5'], 'The scaffold <strong>has been erected</strong>. <strong>We will start</strong> at 06:00.'),
    ], None),
    ('mc', 'e1', 'mcT', VOICE, 'refinery-scene-0', None),
    ('mc', 'e2', 'mcT', FORM, 'refinery-scene-1', 'left'),
    ('gap', 'e2', 'gapT', 'gHint', [
        ('The firewater pump ______ (service) twice a year under the maintenance schedule.',
         ['is serviced|gets serviced'], 'w3'),
        ('All gas detectors ______ (calibrate, MUST) before the unit restart.', ['must be calibrated'], 'w7'),
    ]),
    ('order', 'e2', 'orderT', 'orderHint', [
        (['All equipment', 'was', 'checked', 'before the operation.'], ['were'], 'w5'),
        (['All personnel', 'will', 'be', 'briefed', 'before the operation.'], ['been'], 'w9'),
    ], 'refinery-scene-3', None),
    ('talk', 'eT', 'tk2T', [
        'Give a radio command to your team in <strong>active</strong> voice.',
        'Report a leak in two sentences, <strong>passive</strong>: what <strong>was found</strong>, what <strong>was done</strong>?',
        'What <strong>has been repaired</strong> or <strong>replaced</strong> at your site this month?',
        'What <strong>must be checked</strong> at the start of every shift?',
        'Hand over to the next shift: what <strong>did you</strong> do, what <strong>will be done</strong> next?',
        'When is it wrong to hide who did something?',
    ], None, 3),
]
SPEC['chips'] = ['must be checked', 'was found', 'I suspended', 'will be briefed', 'has been repaired']

W = {
    'en': [
        'A radio command is fastest as an active imperative: REQUEST … The passive versions are longer and hide who should act.',
        'All three verbs are passive: WAS DISCOVERED, WAS NOTIFIED, WAS ISOLATED. The others mix in WE or SOMEONE.',
        'IS SERVICED: the present simple passive for a regular schedule. IS / ARE + past participle.',
        'HAS BEEN + participle: the present perfect passive. WAS REPAIRED would be the past simple; HAVE needs a plural.',
        'WAS CHECKED: the past simple passive, WAS + participle. EQUIPMENT is uncountable, so WERE is left over.',
        'A handover note needs an owner: I SUSPENDED names who acted. The passive versions leave the actor unclear.',
        'A modal passive: MUST + BE + participle → MUST BE CALIBRATED.',
        'Passive for the status, where who built it does not matter; active for the instruction, which needs a WE.',
        'WILL + BE + participle: the future passive. BEEN is left over.',
        'ARRIVE takes no object, so it has no passive at all: “The incident commander ARRIVED on scene at 14:35.”',
    ],
    'de': [
        'Ein Funkbefehl ist als aktiver Imperativ am schnellsten: REQUEST … Die Passivformen sind länger und verschweigen, wer handeln soll.',
        'Alle drei Verben stehen im Passiv: WAS DISCOVERED, WAS NOTIFIED, WAS ISOLATED. Die anderen mischen WE oder SOMEONE hinein.',
        'IS SERVICED: Passiv im Present Simple für einen regelmäßigen Plan. IS / ARE + Partizip.',
        'HAS BEEN + Partizip: Passiv im Present Perfect. WAS REPAIRED wäre Past Simple; HAVE braucht ein Pluralsubjekt.',
        'WAS CHECKED: Passiv im Past Simple, WAS + Partizip. EQUIPMENT ist unzählbar, also bleibt WERE übrig.',
        'Eine Übergabenotiz braucht einen Verantwortlichen: I SUSPENDED nennt, wer gehandelt hat. Die Passivformen lassen das offen.',
        'Ein Modalpassiv: MUST + BE + Partizip → MUST BE CALIBRATED.',
        'Passiv für den Status, wo es egal ist, wer das Gerüst gebaut hat; Aktiv für die Anweisung, die ein WE braucht.',
        'WILL + BE + Partizip: Passiv im Futur. BEEN bleibt übrig.',
        'ARRIVE hat kein Objekt, also gibt es kein Passiv: „The incident commander ARRIVED on scene at 14:35.“',
    ],
    'es': [
        'Una orden por radio es más rápida en imperativo activo: REQUEST … Las versiones pasivas son más largas y ocultan quién debe actuar.',
        'Los tres verbos están en pasiva: WAS DISCOVERED, WAS NOTIFIED, WAS ISOLATED. Las demás mezclan WE o SOMEONE.',
        'IS SERVICED: pasiva en present simple para un calendario regular. IS / ARE + participio.',
        'HAS BEEN + participio: pasiva en present perfect. WAS REPAIRED sería past simple; HAVE necesita un sujeto plural.',
        'WAS CHECKED: pasiva en past simple, WAS + participio. EQUIPMENT es incontable, así que sobra WERE.',
        'Una nota de relevo necesita un responsable: I SUSPENDED dice quién actuó. Las versiones pasivas lo dejan sin aclarar.',
        'Una pasiva con modal: MUST + BE + participio → MUST BE CALIBRATED.',
        'Pasiva para el estado, donde no importa quién montó el andamio; activa para la instrucción, que necesita un WE.',
        'WILL + BE + participio: la pasiva en futuro. Sobra BEEN.',
        'ARRIVE no lleva objeto, así que no tiene pasiva: «The incident commander ARRIVED on scene at 14:35».',
    ],
}

T = {
    'en': dict(
        coverTitle='Active &amp; <br><em>Passive</em>',
        coverSub='Refinery quiz, Part 2: which voice to use on the radio, in a handover and in an incident report, and the passive in every tense.',
        chipLevel='B2', chipFocus='active · passive · all tenses', chipCount='16 slides',
        eW='Warm-up', eT='Let’s talk', eR='The rule', e1='Which voice?', e2='The forms',
        tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the best answer',
        c1='Your supervisor radios you during an incident.',
        c2='An extract from an incident report.',
        c6='You are writing a shift handover note as deputy lead.',
        c8='You are briefing your team before a scheduled flare tip replacement.',
        rFormT='The passive in every tense',
        rF1='Present simple: a routine or a schedule.', rF2='Past simple: a finished event.',
        rF3='Present perfect: done, and the result matters now.', rF4='Modals and the future: BE never changes.',
        rUseT='Active or passive?', pActive='Active', pPassive='Passive', pMix='Both',
        rU1='Commands on the radio: short, and nobody has to guess who acts.',
        rU2='Handover notes: name who did it.',
        rU3='Reports: what happened matters more than who.',
        rU4='Keep one voice through a report.',
        rU5='Passive for the status, active for the instruction.',
        gapT='Write the passive', gHint='Use the passive of the verb in brackets.',
        orderT='Build the sentence', orderHint='Click the pieces in order. One piece is left over.',
        actTitle='The handover', actUse='Use at least three:',
        actSpeakBrief='In pairs: one of you is ending a shift, the other is starting it.',
        actSpeak1='Hand over the shift: what WAS DONE, what HAS BEEN REPAIRED, what MUST BE CHECKED.',
        actSpeak2='Give two radio commands in active voice. Your partner repeats them back.',
        actSpeak3='Swap roles. This time, name who did each action: I, WE, THE TEAM.',
        actWriteKind='Writing',
        actWriteBrief='Write a short incident report (120–150 words) on a small leak: what WAS FOUND, what WAS DONE, what WILL BE CHECKED, all passive. End with one active sentence naming who owns the follow-up.',
        actPlaceholder='At 09:40, a small leak was found …',
    ),
    'de': dict(
        coverTitle='Active &amp; <br><em>Passive</em>',
        coverSub='Raffinerie-Quiz, Teil 2: welches Genus verbi am Funk, bei der Schichtübergabe und im Störfallbericht, und das Passiv in jeder Zeitform.',
        chipLevel='B2', chipFocus='Aktiv · Passiv · alle Zeiten', chipCount='16 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Die Regel', e1='Aktiv oder Passiv?', e2='Die Formen',
        tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle die beste Antwort',
        c1='Dein Vorgesetzter funkt dich während eines Störfalls an.',
        c2='Ein Auszug aus einem Störfallbericht.',
        c6='Du schreibst als stellvertretende Leitung eine Schichtübergabe.',
        c8='Du weist dein Team vor einem geplanten Fackelkopf-Austausch ein.',
        rFormT='Das Passiv in jeder Zeitform',
        rF1='Present Simple: eine Routine oder ein Plan.', rF2='Past Simple: ein abgeschlossenes Ereignis.',
        rF3='Present Perfect: erledigt, und das Ergebnis zählt jetzt.', rF4='Modalverben und Futur: BE ändert sich nie.',
        rUseT='Aktiv oder Passiv?', pActive='Aktiv', pPassive='Passiv', pMix='Beides',
        rU1='Befehle am Funk: kurz, und niemand muss raten, wer handelt.',
        rU2='Übergabenotizen: nenne, wer es getan hat.',
        rU3='Berichte: Was passiert ist, zählt mehr als wer.',
        rU4='Bleib in einem Bericht bei einem Genus.',
        rU5='Passiv für den Status, Aktiv für die Anweisung.',
        gapT='Schreib das Passiv', gHint='Verwende das Passiv des Verbs in Klammern.',
        orderT='Bilde den Satz', orderHint='Klicke die Teile der Reihe nach an. Ein Teil bleibt übrig.',
        actTitle='Die Übergabe', actUse='Verwende mindestens drei:',
        actSpeakBrief='Zu zweit: Eine Person beendet eine Schicht, die andere beginnt sie.',
        actSpeak1='Übergib die Schicht: was getan wurde (WAS DONE), was repariert wurde (HAS BEEN REPAIRED), was geprüft werden muss (MUST BE CHECKED).',
        actSpeak2='Gib zwei Funkbefehle im Aktiv. Dein Partner wiederholt sie.',
        actSpeak3='Tauscht die Rollen. Diesmal nennst du, wer jede Handlung ausgeführt hat: I, WE, THE TEAM.',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib einen kurzen Störfallbericht (120–150 Wörter) über ein kleines Leck: WAS FOUND, WAS DONE, WILL BE CHECKED, alles im Passiv. Schließe mit einem Aktivsatz: Wer kümmert sich um die Nachverfolgung?',
        actPlaceholder='At 09:40, a small leak was found …',
    ),
    'es': dict(
        coverTitle='Active &amp; <br><em>Passive</em>',
        coverSub='Cuestionario de refinería, parte 2: qué voz usar por radio, en un relevo y en un informe de incidentes, y la pasiva en todos los tiempos.',
        chipLevel='B2', chipFocus='activa · pasiva · todos los tiempos', chipCount='16 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='La regla', e1='¿Qué voz?', e2='Las formas',
        tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige la mejor respuesta',
        c1='Tu supervisor te llama por radio durante un incidente.',
        c2='Un fragmento de un informe de incidentes.',
        c6='Escribes una nota de relevo de turno como segundo al mando.',
        c8='Estás dando instrucciones a tu equipo antes de un cambio programado de la punta de la antorcha.',
        rFormT='La pasiva en todos los tiempos',
        rF1='Present simple: una rutina o un calendario.', rF2='Past simple: un hecho terminado.',
        rF3='Present perfect: hecho, y el resultado importa ahora.', rF4='Modales y futuro: BE nunca cambia.',
        rUseT='¿Activa o pasiva?', pActive='Activa', pPassive='Pasiva', pMix='Las dos',
        rU1='Órdenes por radio: cortas, y nadie tiene que adivinar quién actúa.',
        rU2='Notas de relevo: di quién lo hizo.',
        rU3='Informes: lo que pasó importa más que quién.',
        rU4='Mantén una sola voz en todo el informe.',
        rU5='Pasiva para el estado, activa para la instrucción.',
        gapT='Escribe la pasiva', gHint='Usa la pasiva del verbo entre paréntesis.',
        orderT='Construye la oración', orderHint='Haz clic en las piezas en orden. Sobra una pieza.',
        actTitle='El relevo', actUse='Usa al menos tres:',
        actSpeakBrief='En parejas: uno termina un turno y el otro lo empieza.',
        actSpeak1='Entrega el turno: qué se hizo (WAS DONE), qué se ha reparado (HAS BEEN REPAIRED) y qué hay que revisar (MUST BE CHECKED).',
        actSpeak2='Da dos órdenes por radio en voz activa. Tu compañero las repite.',
        actSpeak3='Cambien los papeles. Esta vez, di quién hizo cada acción: I, WE, THE TEAM.',
        actWriteKind='Escritura',
        actWriteBrief='Escribe un informe de incidentes corto (120–150 palabras) sobre una pequeña fuga: WAS FOUND, WAS DONE, WILL BE CHECKED, todo en pasiva. Termina con una oración activa: ¿quién se encarga del seguimiento?',
        actPlaceholder='At 09:40, a small leak was found …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T)
