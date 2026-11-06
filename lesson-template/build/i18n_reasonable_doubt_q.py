# -*- coding: utf-8 -*-
"""The question slides of Reasonable Doubt in German and Spanish. See build_reasonable_doubt.py.

Innes, 2026-11-06, on the DE/ES deck: "Has not been translated at all barely".
Only the stories and the menus translated; every question slide's eyebrow,
title, instruction and explanation was English. Per node: (eyebrow, title,
instruction stem or None, explanation). A stem with a gap (___) is the
English being taught and stays English (HOUSE-STYLE §8), so it is None here;
so do the options. In the explanations the grammar tokens stay in CAPS and
every cited English form stays English, in the language's own quotes.
Written in-session, informal du / tú; no native check yet.
"""
QT = {}

QT['de'] = {
    'q04': ('Akt I · die erste Abstimmung', 'Elf Hände gehen hoch.',
            'Welche Antwort drückt Unsicherheit treffend aus?',
            'I DON’T KNOW räumt Unsicherheit ein; SHOULD schlägt einen nächsten Schritt vor. MUST und CAN’T '
            'behaupten eine Gewissheit, die ein Gefühl nicht geben kann.'),
    'q05': ('Akt I · höflich widersprechen', 'Bleib standhaft.',
            'Welche Antwort stellt die Behauptung respektvoll infrage?',
            'I SEE YOUR POINT, BUT … gesteht den Punkt zu, bevor du widersprichst – so widersprichst du, ohne '
            'anzugreifen. Eine Frage hält das Gespräch offen.'),
    'q07': ('Akte A · das Messer', 'Ein ungewöhnlicher Gegenstand.', None,
            'Eine Möglichkeit in der Vergangenheit: MIGHT HAVE + Partizip Perfekt, „might have belonged“. MUST HAVE '
            'behauptet Gewissheit, und nach HAVE steht immer das Partizip Perfekt.'),
    'q08': ('Akte A · eine Behauptung prüfen', 'Ein zweites Messer.',
            'Welcher Satz zieht einen starken negativen Schluss über die Vergangenheit?',
            'Ein starker negativer Schluss über die Vergangenheit: CAN’T HAVE BEEN. Nach einem Modalverb wird HAVE '
            'nie zu HAS. Ein zweites Messer widerlegt „unique“, nicht die ganze Anklage.'),
    'q09': ('Akte A · die Behauptung begrenzen', 'Was beweist das?',
            'Wähle die vorsichtigste Schlussfolgerung.',
            'WEAKENS hält die Schlussfolgerung innerhalb dessen, was die Beweise tragen. PROVES und EVERY PART machen '
            'aus einem Zweifel die Behauptung, alles sei falsch.'),
    'q10': ('Akte A · even if', 'Zugestehen. Dann widersprechen.', None,
            'EVEN IF + Nebensatz akzeptiert den Punkt, nicht die Schlussfolgerung. DESPITE steht nie mit „of“; '
            'IN SPITE braucht OF.'),
    'q11': ('Akte A · Beweis-Kontrolle', 'Der erste Zweifel kommt in die Akte.',
            'Welche Notiz gehört in die Akte?',
            'Akte A ist abgeschlossen. Die Notiz stellt eine Behauptung infrage – dass das Messer einzigartig war – '
            'und bleibt bei den Beweisen. PROVES und MUST behaupten viel mehr.'),
    'q12': ('Akte B · was konnte er hören?', 'Eine Stimme unter dem Zug.',
            'Welcher Satz stellt die Aussage infrage, ohne zu viel Gewissheit zu behaupten?',
            'MIGHT HAVE MADE nennt ein mögliches Hindernis. Es nennt den Zeugen keinen Lügner und behauptet nicht, '
            'die Worte seien unmöglich zu hören gewesen.'),
    'q13': ('Akte B · indirekte Rede', 'Was der Zeuge sagte.',
            'Wähle die richtig zurückverschobene Wiedergabe.',
            'Zeitverschiebung: HEARD wird zu HAD HEARD. Man sagt SAY something, aber TELL someone something: '
            '„He told us that he had heard …“ geht auch.'),
    'q14': ('Akte B · Ereignisse ordnen', 'Die Länge eines Flurs.', None,
            'Das frühere von zwei vergangenen Ereignissen steht im Past Perfect, HAD + Partizip Perfekt: '
            '„had disappeared“. Das spätere, „reached“, steht im Past Simple.'),
    'q15': ('Akte B · die irreale Vergangenheit', 'Die Zeit nachprüfen.', None,
            'IF + HAD + Partizip Perfekt gehört zu COULDN’T HAVE + Partizip Perfekt, für eine irreale Vergangenheit. '
            'Nach HAVE steht immer das Partizip Perfekt: „reached“.'),
    'q16': ('Akte B · Beweis-Kontrolle', 'Ein Irrtum ist keine Lüge.',
            'Wähle eine vorsichtige Aussage über den Zeugen.',
            'Akte B ist abgeschlossen. MAY HAVE MISJUDGED lässt einen ehrlichen Irrtum zu; MUST HAVE LIED behauptet '
            'eine absichtliche Lüge.'),
    'q17': ('Akte C · eine Behauptung, etwas gesehen zu haben', 'Jenseits der Gleise.', None,
            'CLAIM + TO HAVE + Partizip Perfekt gibt eine Behauptung über ein früheres Ereignis wieder. Das '
            'Partizip Perfekt von „see“ ist „seen“, nicht „saw“.'),
    'q18': ('Akte C · Möglichkeit, kein Beweis', 'Ein Hindernis in Bewegung.',
            'Wähle die richtige Form für eine Möglichkeit in der Vergangenheit.',
            'COULD HAVE + Partizip Perfekt: eine Möglichkeit in der Vergangenheit. Nach einem Modalverb wird HAVE '
            'nie zu HAS, und das Verb steht im Partizip Perfekt: „blocked“.'),
    'q19': ('Akte C · eine kleine Beobachtung', 'Die Spuren einer Brille.',
            'Welcher Satz macht aus einer Vermutung keine Gewissheit?',
            'MAY NOT HAVE BEEN + -ING: ein möglicher andauernder Zustand in der Vergangenheit. Die Spuren werfen '
            'eine Frage auf, ohne sie zu beantworten – PROVE und DEFINITELY gehen zu weit.'),
    'q20': ('Akte C · although', 'Sicherheit und Genauigkeit.', None,
            'ALTHOUGH steht mit einem Nebensatz: „she sounded certain“. DESPITE steht mit einem Nomen oder -ING, '
            '„despite sounding certain“, und nie mit OF.'),
    'q21': ('Akte C · Beweis-Kontrolle', 'Der letzte Zweifel kommt in die Akte.', None,
            'Akte C ist abgeschlossen. MIGHT NOT HAVE + Partizip Perfekt: eine mögliche Folge einer irrealen '
            'Bedingung in der Vergangenheit. Du behauptest nicht zu wissen, was sie sah.'),
    'q23': ('Akt III · einen Vorschlag machen', 'Ein heimlicher Sinneswandel.', None,
            'WOULD RATHER + ein neues Subjekt + Past Simple drückt einen Wunsch für jetzt oder später aus: '
            '„I’d rather we voted“. Die Vergangenheitsform bedeutet hier keine vergangene Zeit.'),
    'q24': ('Akt III · auf die Bedeutung hören', 'Der erste Verbündete.',
            'Welcher Satz gibt seine Haltung treffend wieder?',
            'DESERVE A FAIR HEARING heißt, dass man die Zweifel ernsthaft anhören soll. Es heißt nicht, dass er weiß, '
            'dass der junge Mann unschuldig ist.'),
    'q25': ('Akt III · ein Motiv infrage stellen', 'Kein Argument.',
            'Welche Antwort lenkt die Stimme zurück auf die Beweise?',
            'DEPEND ON nennt die richtige Grundlage für eine Stimme. Du stellst seinen Grund infrage, nicht seine '
            'Intelligenz.'),
    'q26': ('Akt III · eine Verallgemeinerung infrage stellen', 'Wenn das Vorurteil spricht.',
            'Welche Antwort stellt den fehlerhaften Schluss direkt infrage?',
            'Benenne den Denkfehler und kehre dann zu den Beweisen zurück. Wer auf ein Klischee mit einem anderen '
            'antwortet, wiederholt denselben Fehler.'),
    'q28': ('Akt IV · der Weg des Zuhörens', 'Raum für eine Stimme.', None,
            'HEAR SOMEONE OUT: zuhören, bis jemand fertig ist. Ein Pronomen steht zwischen den beiden Wörtern: '
            '„hear him out“, nie „hear out him“.'),
    'q29': ('Akt IV · der direkte Weg', 'Die Temperatur senken.', None,
            'UNLESS bedeutet IF … NOT: Wir kommen nicht weiter, wenn wir einander nicht ausreden lassen. Es nennt '
            'die Bedingung.'),
    'q30': ('Akt IV · despite + Nomen', 'Regen am Fenster.', None,
            'DESPITE + Nomen: „despite the tension“. ALTHOUGH und EVEN THOUGH brauchen einen Nebensatz: '
            '„although the room was tense“.'),
    'q31': ('Akt IV · eine andere Erklärung', 'Ein Gedächtnis unter Druck.',
            'Welche Erklärung ist vorsichtig und passend?',
            'Eine Gedächtnislücke hat mehr als eine Erklärung. MAY HAVE AFFECTED bietet eine an, ohne zu behaupten, '
            'sie sei bewiesen.'),
    'q32': ('Akt IV · eine Entscheidung wiedergeben', 'Eine Stimme ändert sich.',
            'Wähle die richtige Wiedergabe.',
            'Zeitverschiebung: WILL wird zu WOULD und MY zu HIS, weil du die Worte eines anderen wiedergibst. TELL '
            'braucht eine Person: „He told us …“.'),
    'q33': ('Akt V · Beweise und Gefühl', 'Der letzte Widerstand.',
            'Welche Frage verbindet Mitgefühl mit der Rückkehr zu den Beweisen?',
            'COULD … BE INFLUENCING wirft eine Möglichkeit auf, statt einen Vorwurf zu machen. Ein starkes Gefühl '
            'macht eine Behauptung nicht falsch.'),
    'q35': ('Akt V · Behauptung, Grund, Grenze', 'Das letzte Argument.',
            'Welche Zusammenfassung lässt sich am besten verteidigen?',
            'Ein starkes Argument nennt seine Grenze. Die Jury entscheidet, ob die Schuld bewiesen ist, nicht, was '
            'wirklich geschah.'),
}

QT['es'] = {
    'q04': ('Acto I · la primera votación', 'Once manos se alzan.',
            '¿Qué respuesta expresa la incertidumbre con precisión?',
            'I DON’T KNOW admite la incertidumbre; SHOULD propone un siguiente paso. MUST y CAN’T afirman una '
            'certeza que una sensación no puede dar.'),
    'q05': ('Acto I · discrepar con educación', 'Mantente firme.',
            '¿Qué respuesta cuestiona la afirmación con respeto?',
            'I SEE YOUR POINT, BUT … concede el punto antes de cuestionarlo, así que discrepas sin atacar. Una '
            'pregunta mantiene abierto el debate.'),
    'q07': ('Expediente A · la navaja', 'Un objeto poco común.', None,
            'Una posibilidad en el pasado: MIGHT HAVE + participio, «might have belonged». MUST HAVE afirma certeza, '
            'y después de HAVE el verbo siempre va en participio.'),
    'q08': ('Expediente A · poner a prueba una afirmación', 'Una segunda navaja.',
            '¿Qué frase saca una deducción negativa firme sobre el pasado?',
            'Una deducción negativa firme sobre el pasado: CAN’T HAVE BEEN. Después de un modal, HAVE nunca pasa a '
            'HAS. Una segunda navaja desmiente «unique», no toda la acusación.'),
    'q09': ('Expediente A · limitar la afirmación', '¿Qué demuestra eso?',
            'Elige la conclusión más prudente.',
            'WEAKENS mantiene la conclusión dentro de lo que sostienen las pruebas. PROVES y EVERY PART convierten '
            'una duda en la afirmación de que todo es falso.'),
    'q10': ('Expediente A · even if', 'Concede. Después, cuestiona.', None,
            'EVEN IF + oración acepta el punto, no la conclusión. DESPITE nunca lleva «of»; IN SPITE necesita OF.'),
    'q11': ('Expediente A · control de pruebas', 'Archiva la primera duda.',
            '¿Qué nota va en el expediente?',
            'Expediente A completo. La nota cuestiona una afirmación, que la navaja era única, y no va más allá de '
            'las pruebas. PROVES y MUST afirman mucho más.'),
    'q12': ('Expediente B · ¿qué podía oír?', 'Una voz bajo un tren.',
            '¿Qué frase cuestiona el testimonio sin exagerar la certeza?',
            'MIGHT HAVE MADE plantea un obstáculo posible. No llama mentiroso al testigo ni afirma que fuera '
            'imposible oír las palabras.'),
    'q13': ('Expediente B · estilo indirecto', 'Lo que dijo el testigo.',
            'Elige la versión en estilo indirecto con el cambio de tiempo correcto.',
            'Cambio de tiempo: HEARD pasa a HAD HEARD. Se dice SAY something, pero TELL someone something: '
            '«He told us that he had heard…» también vale.'),
    'q14': ('Expediente B · ordenar los hechos', 'La longitud de un pasillo.', None,
            'El primero de dos hechos pasados va en past perfect, HAD + participio: «had disappeared». El '
            'posterior, «reached», va en past simple.'),
    'q15': ('Expediente B · el pasado irreal', 'Comprueba el tiempo.', None,
            'IF + HAD + participio va con COULDN’T HAVE + participio para un pasado irreal. Después de HAVE, '
            'siempre el participio: «reached».'),
    'q16': ('Expediente B · control de pruebas', 'Equivocarse no es mentir.',
            'Elige una afirmación prudente sobre el testigo.',
            'Expediente B completo. MAY HAVE MISJUDGED admite un error honesto; MUST HAVE LIED afirma una mentira '
            'deliberada.'),
    'q17': ('Expediente C · haber visto algo', 'Al otro lado de las vías.', None,
            'CLAIM + TO HAVE + participio transmite una afirmación sobre un hecho anterior. El participio de «see» '
            'es «seen», no «saw».'),
    'q18': ('Expediente C · posibilidad, no prueba', 'Un obstáculo en movimiento.',
            'Elige la forma correcta de posibilidad en el pasado.',
            'COULD HAVE + participio: una posibilidad en el pasado. Después de un modal, HAVE nunca pasa a HAS, y '
            'el verbo va en participio: «blocked».'),
    'q19': ('Expediente C · una pequeña observación', 'Las marcas de unas gafas.',
            '¿Qué frase evita convertir una inferencia en certeza?',
            'MAY NOT HAVE BEEN + -ING: un posible estado continuo en el pasado. Las marcas plantean una pregunta '
            'sin responderla, así que PROVE y DEFINITELY van demasiado lejos.'),
    'q20': ('Expediente C · although', 'Seguridad y exactitud.', None,
            'ALTHOUGH va con una oración: «she sounded certain». DESPITE va con un sustantivo o -ING, «despite '
            'sounding certain», y nunca con OF.'),
    'q21': ('Expediente C · control de pruebas', 'Archiva la última duda.', None,
            'Expediente C completo. MIGHT NOT HAVE + participio: una posible consecuencia de una condición irreal '
            'en el pasado. No afirmas saber qué vio.'),
    'q23': ('Acto III · hacer una propuesta', 'Un cambio de opinión en privado.', None,
            'WOULD RATHER + un sujeto nuevo + past simple expresa una preferencia presente o futura: «I’d rather '
            'we voted». Aquí la forma pasada no indica tiempo pasado.'),
    'q24': ('Acto III · escuchar el sentido', 'El primer aliado.',
            '¿Qué frase resume bien su postura?',
            'DESERVE A FAIR HEARING significa que hay que escuchar las dudas en serio. No significa que él sepa que '
            'el joven es inocente.'),
    'q25': ('Acto III · cuestionar un motivo', 'No es un argumento.',
            '¿Qué respuesta devuelve el voto a las pruebas?',
            'DEPEND ON nombra la base correcta de un voto. Cuestionas su motivo, no su inteligencia.'),
    'q26': ('Acto III · cuestionar una generalización', 'Cuando habla el prejuicio.',
            '¿Qué respuesta cuestiona directamente el razonamiento erróneo?',
            'Nombra el error de razonamiento y vuelve a las pruebas. Responder a un estereotipo con otro repite el '
            'mismo error.'),
    'q28': ('Acto IV · la ruta de escuchar', 'Espacio para una voz.', None,
            'HEAR SOMEONE OUT: escuchar hasta que alguien termine. El pronombre va entre las dos palabras: «hear '
            'him out», nunca «hear out him».'),
    'q29': ('Acto IV · la ruta directa', 'Bajar la tensión.', None,
            'UNLESS significa IF … NOT: no avanzaremos si no nos dejamos terminar. Expresa la condición.'),
    'q30': ('Acto IV · despite + sustantivo', 'Lluvia en la ventana.', None,
            'DESPITE + sustantivo: «despite the tension». ALTHOUGH y EVEN THOUGH necesitan una oración: «although '
            'the room was tense».'),
    'q31': ('Acto IV · otra explicación', 'Una memoria bajo presión.',
            '¿Qué explicación es prudente y pertinente?',
            'Un fallo de memoria tiene más de una explicación. MAY HAVE AFFECTED ofrece una sin afirmar que esté '
            'demostrada.'),
    'q32': ('Acto IV · transmitir una decisión', 'Un voto que cambia.',
            'Elige la versión correcta en estilo indirecto.',
            'Cambio de tiempo: WILL pasa a WOULD y MY a HIS, porque transmites las palabras de otra persona. TELL '
            'necesita una persona: «He told us…».'),
    'q33': ('Acto V · pruebas y emoción', 'La última resistencia.',
            '¿Qué pregunta une la empatía con la vuelta a las pruebas?',
            'COULD … BE INFLUENCING plantea una posibilidad en lugar de acusar. Una emoción fuerte no hace falsa '
            'una afirmación.'),
    'q35': ('Acto V · afirmación, razón, límite', 'El argumento final.',
            '¿Qué resumen se puede defender mejor?',
            'Un argumento sólido señala su límite. El jurado decide si se ha probado la culpabilidad, no qué pasó '
            'de verdad.'),
}

# The act label the deck bar shows (data-act), per language
ACTS = {
    'en': {'Before you begin': 'Before you begin', 'Act I': 'Act I', 'Act II': 'Act II', 'Act III': 'Act III',
           'Act IV': 'Act IV', 'Act V': 'Act V', 'File A': 'File A', 'File B': 'File B', 'File C': 'File C',
           'Verdict': 'Verdict', 'Ending': 'Ending', 'Activation': 'Activation'},
    'de': {'Before you begin': 'Bevor du beginnst', 'Act I': 'Akt I', 'Act II': 'Akt II', 'Act III': 'Akt III',
           'Act IV': 'Akt IV', 'Act V': 'Akt V', 'File A': 'Akte A', 'File B': 'Akte B', 'File C': 'Akte C',
           'Verdict': 'Urteil', 'Ending': 'Ende', 'Activation': 'Anwenden'},
    'es': {'Before you begin': 'Antes de empezar', 'Act I': 'Acto I', 'Act II': 'Acto II', 'Act III': 'Acto III',
           'Act IV': 'Acto IV', 'Act V': 'Acto V', 'File A': 'Expediente A', 'File B': 'Expediente B',
           'File C': 'Expediente C', 'Verdict': 'Veredicto', 'Ending': 'Final', 'Activation': 'Práctica'},
}

# "1 of 5" on the eyebrow, per language
OF = {'en': '%d of %d', 'de': '%d von %d', 'es': '%d de %d'}
