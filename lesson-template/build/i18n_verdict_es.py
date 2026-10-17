# -*- coding: utf-8 -*-
"""Spanish strings for Anatomy of a Verdict. See i18n_verdict.py.

Written in-session, informal "tú" as the course chrome; no native check yet.
T is the chrome, N the narrative glosses behind the Translate button. Every
CAPS grammar token stays in English."""
T = dict(
    coverTitle='Anatomy of a <em>Verdict</em>',
    coverSub='Once miembros del jurado dicen que ella lo empujó. Tú eres la número doce, y no estás segura.',
    chipLevel='C1 · Avanzado', chipFocus='Concesión · el lenguaje de la argumentación',
    chipCount='60–75 minutos',
    btnContinue='Continuar →',
    actBefore='Antes de empezar',

    howEyebrow='Cómo funciona la deliberación', howTitle='Cada argumento tiene un precio.',
    howDp='Puntos', howDpBody='Un argumento correcto suma <strong>+1 punto</strong>.',
    howTime='Paciencia',
    howTimeBody='La sala empieza con cuatro. Un argumento incorrecto cuesta una. A cero, nadie te escucha.',
    howClues='Votos',
    howCluesBody='Se puede convencer a cuatro miembros del jurado. Para el mejor veredicto necesitas los cuatro.',
    ledDp='Puntos', ledTime='Paciencia', ledClues='Votos',

    labEyebrow='Antes de deliberar', labTitle='Cómo conceder un punto.',
    voteTurned='Un voto cambia', voteHeld='El voto se mantiene',
    chooseA='Volver a escuchar la grabación', chooseB='Estudiar la escalera',
    chooseC='Interrogar al testigo', chooseD='Rehacer la cronología',
    explainFirst='Explica tu elección en inglés antes de hacer clic.',

    boardEyebrow='Tu alegato final · ronda oral', boardTitle='Defiende el caso en voz alta.',
    lockEyebrow='El último argumento', lockTitle='Completa las dos frases.',

    ledgerEyebrow='Ha llegado la última papeleta', ledgerTitle='Tu balance decide el veredicto.',
    gold='Unanimidad', goldBody='Todos los votos cambiados, y la sala todavía escucha.',
    silver='Mayoría', silverBody='Bastantes argumentos aguantaron para un veredicto por mayoría.',
    shadow='Sin veredicto', shadowBody='La sala nunca se pone de acuerdo.',
    ledgerNote='Los finales que no te has ganado están bloqueados.',
    branchLocked='Tu balance no permite este veredicto',
    endGold='Veredicto unánime', endSilver='Veredicto por mayoría', endShadow='Jurado sin acuerdo',
    revealKick='Lo que las pruebas podían demostrar',
    resRoute='Solo cuentan las preguntas que encontraste en tu camino.',

    glossShow='Traducir', glossHide='Ocultar traducción',
    resPerfect='Impecable. Todos los argumentos aguantaron.',
    resStrong='Buen trabajo. La sala te escuchó.',
    resMid='Un caso razonable, con huecos que una abogada encontraría.',
    resLow='La duda era razonable. Los argumentos, no.',

    actTitle='Ahora argumenta tú.',
    actUse='Usa al menos tres de estas',
    actSpeakBrief='En parejas o en grupos de tres. Primero concede, luego da la vuelta al argumento.',
    actSpeak1='Eres Victor. Argumenta que Ruth es culpable. Tu compañero concede cada punto y luego le da la vuelta.',
    actSpeak2='Eres la abogada de Ruth. Admite tres hechos en su contra y muestra por qué ninguno demuestra un empujón.',
    actSpeak3='Piensa en una vez en que cambiaste de opinión. Explica qué sigues creyendo y qué te hizo cambiar.',
    actWriteKind='Escritura · 150–250 palabras',
    actWriteBrief='Escribe la nota que el presidente del jurado envía al juez explicando cómo llegó el jurado a su '
                  'veredicto. Concede tres puntos contra Ruth y da la vuelta a cada uno.',
    actPlaceholder='Señoría: …',
)

N = {
    'casefile': '<strong>Martes</strong> Ruth y Simon discuten. Simon lo graba con el móvil.<br>'
                '<strong>Miércoles 14:25</strong> La cámara de un timbre muestra la furgoneta de Ruth saliendo del molino.<br>'
                '<strong>14:30</strong> Kit, el aprendiz, dice que oyó un grito.<br>'
                '<strong>14:52</strong> Ruth llama al 999. Simon yace al pie de la escalera de hierro.',
    'casefile-note': 'Nadie vio la caída. La barandilla de la galería está rota. Ruth dice que había salido a comprar arcilla.',
    'dec1-a': 'Tu oficio. Cada segundo de la grabación de Simon, cada eco, cada hueco.',
    'dec1-b': 'El oficio de Priya. Las fotos de la policía, la barandilla, el moratón.',
    'dec2-a': 'Kit Marlow, diecinueve años, el aprendiz. Dice que oyó un grito.',
    'dec2-b': 'La cámara de un timbre, una furgoneta blanca, una llamada al 999. Veintisiete minutos.',
    'agnes-yes': 'Agnes deja el lápiz. «De acuerdo. No culpable, por ahora». Su mano se levanta con la tuya.',
    'agnes-no': 'Agnes frunce el ceño ante la frase y no apunta nada. «Vuelve a intentarlo luego, querida». Su voto sigue donde estaba.',
    'priya-yes': 'Priya se levanta y va a la ventana. Cuando vuelve a sentarse, vota contigo.',
    'priya-no': 'Priya niega con la cabeza. «No puedo cambiar mi voto por una sensación». La sala se impacienta.',
    'gerald-yes': 'Gerald se vuelve a poner el reloj y mira la mesa. «No culpable. Apúntelo». El presidente del jurado ha cambiado.',
    'gerald-no': 'Gerald vuelve a mirar el reloj. «Creo que ya hemos oído bastante». Su voto no se mueve.',
    'victor-yes': 'Victor abre las manos. Durante mucho rato no dice nada. Luego: «No culpable». Doce a cero.',
    'victor-no': 'Victor vuelve a cruzar los brazos. «Ya he dicho lo que tenía que decir». La sala tiene que arreglárselas sin él.',
    'board': 'Antes de la última votación, di tres concesiones en voz alta: admite cada vez un hecho contra Ruth y luego dale la vuelta.',
    'end-gold': 'Doce papeletas, una palabra. Ruth Adair se agarra a la barandilla del banquillo y no llora. '
                'Nunca sabrás qué pasó en esa escalera. De eso se trataba: nadie en aquella sala podía saberlo.',
    't-end-gold': 'Veredicto · unánime · no culpable',
    'end-silver': 'Once a uno basta después de tanto tiempo, dice el juez. Victor no quiso moverse, y quizá nunca pudo. '
                  'Ruth sale a la lluvia, y tú sales detrás de ella.',
    't-end-silver': 'Veredicto · once a uno · no culpable',
    'end-shadow': 'Cuatro horas, tres votaciones, y la sala nunca se pone de acuerdo. El juez os disuelve. '
                  'Habrá un nuevo juicio, doce personas nuevas, la misma grabación.',
    't-end-shadow': 'Sin veredicto · jurado sin acuerdo · nuevo juicio',
    'reveal-a': '<strong>Lo que las pruebas demostraron</strong><br>Discutieron el día anterior. Ruth mintió sobre la hora a la que salió. '
                'Simon cayó de la galería entre las dos y las tres.',
    'reveal-b': '<strong>Lo que nunca demostraron</strong><br>Un empujón. El golpe sonó lejos de la voz de Ruth, la barandilla estaba podrida, '
                'el testigo llevaba auriculares y la furgoneta estaba en la carretera.',
    'reveal-c': 'Un jurado no decide qué pasó. Decide si las pruebas dejan una duda razonable.',

    's-room1': 'Gerald Pryce, el presidente del jurado, cuenta las papeletas. «Once culpable. Uno no culpable». Todas las cabezas se vuelven hacia ti.',
    'c-room1': 'Ruth le gritó a Simon el día anterior. Aun así, tienes dudas.',
    's-room2': 'Danny Rourke es taxista y tiene opinión sobre todo. «Estaba furiosa. Él está muerto. Caso cerrado».',
    'c-room2': 'Aceptas que estaba furiosa. La furia, por sí sola, no demuestra nada.',
    's-room3': 'Agnes Bell, directora de colegio jubilada, ha llenado cuatro páginas a lápiz. Levanta la vista. «Venga. Convénceme».',
    'c-room3': 'Ruth mintió a la policía sobre cuándo salió. No puedes negarlo.',
    's-room4': 'El ujier trae el portátil. La grabación del móvil de Simon suena otra vez: gritos, un golpe y luego Ruth llorando.',
    'c-room4': 'Eres ingeniera de sonido. El golpe es muy difícil de situar.',
    's-room6': 'Gerald mira el reloj. «Mire, la respeto. Pero vamos once a uno, y tengo un tren a las seis».',
    'c-room6': 'Tú también respetas a Gerald. Aun así, quieres que se vuelvan a examinar las pruebas.',
    's-rec1': 'Auriculares puestos. La voz de Ruth: «¡Nunca terminas nada!». Luego Simon, riéndose. Danny se inclina. «¿Lo oyes? Furiosa».',
    'c-rec1': 'Suena furiosa. Pero Simon se ríe, así que no tenía miedo.',
    's-rec2': 'Repites el golpe cinco veces. El eco es largo: ocurrió lejos del móvil, cerca de la cocina.',
    'c-rec2': 'La voz de Ruth está cerca del móvil justo en el momento del golpe.',
    's-rec4': 'Le pones a Danny el eco y luego el hueco del archivo. Por una vez se queda callado. «Vale. No está tan claro como pensaba».',
    'c-rec4': 'Danny sigue creyéndola capaz. Pero admite que hay dudas.',
    's-stair1': 'Priya Sandhu, enfermera de urgencias, extiende las fotos de la policía bajo la lámpara. Escalera de hierro, una galería alta, una barandilla colgando de un perno.',
    'c-stair1': 'La barandilla está rota. La acusación dice que Ruth la rompió en un forcejeo.',
    's-stair2': 'Priya se agarra el brazo. «Una mano deja una marca así. Una barandilla también, si la agarras al caer».',
    'c-stair2': 'Intentas de todas las maneras leer el moratón como un agarrón. Sigue encajando con una caída.',
    's-stair4': 'En la foto, el perno está oxidado de lado a lado. En marzo Simon escribió a un albañil por la barandilla. Nunca lo contrató.',
    'c-stair4': 'Puede que Ruth estuviera en la escalera o puede que no. La barandilla era peligrosa de todos modos.',
    's-after1': 'La comida llega en cajas de plástico. Victor Lane, casero, no ha tocado la suya. «Los artistas. Todos mienten».',
    'c-after1': 'Victor la ha juzgado por su oficio, no por las pruebas. Mantienes la calma.',
    's-after2': 'Gerald convoca una segunda votación. Esta vez las manos suben más despacio. Victor da un golpe en la mesa. «Esto es ridículo».',
    'c-after2': 'La votación se ha movido. Victor está tan seguro como antes.',
    's-after3': 'Estás en la ventana con Agnes y Priya. Lluvia sobre el aparcamiento. «No es mala persona», dice Agnes. «Solo está cansado».',
    'c-after3': 'Victor es grosero. Agnes cree que de todos modos merece ser escuchado.',
    's-wit1': 'Kit Marlow, el aprendiz, dijo ante el tribunal que oyó «un grito y luego un golpe sordo» en la escalera a las dos y media.',
    'c-wit1': 'Kit parecía sincero. También llevaba auriculares en el torno de alfarero.',
    's-wit2': 'Prueba 14: los auriculares de Kit, encontrados en el torno. Conoces este modelo. Aísla casi todo.',
    'c-wit2': 'La música de Kit estaba alta. Un grito podría colarse, por poco.',
    's-wit3': 'Gerald se pone él mismo los auriculares y pone música. Agnes grita detrás de él. Gerald no se da la vuelta.',
    'c-wit3': 'Gerald no oyó casi nada. Quería irse a casa. Ahora quiere hacerlo bien.',
    's-clock1': 'La cámara del timbre de un vecino muestra la furgoneta de Ruth saliendo del molino a las 14:25. Su llamada al 999 llega a las 14:52.',
    'c-clock1': 'Simon murió entre las dos y las tres, así que las horas no la exculpan.',
    's-clock2': 'En el juicio se leyó el GPS de la furgoneta: doce minutos hasta el proveedor de arcilla, doce de vuelta, una parada por el camino.',
    'c-clock2': 'Podría haber conducido deprisa. El GPS dice que respetó el límite.',
    's-clock3': 'Gerald se quita el reloj y lo deja sobre la mesa. «Doce de ida, doce de vuelta y una parada. No cuadra».',
    'c-clock3': 'A Gerald le importa su tren. Ahora le importa más la cronología.',
    's-vote1': 'Vuelve a ser once a uno, al revés. Victor se mira las manos. «Mi hijo también se marchó. Nunca dijo por qué».',
    'c-vote1': 'Victor está dolido. Lo entiendes, y aun así necesitas su voto.',
    's-vote2': 'El ujier llama a la puerta. Gerald tiende la mano para recoger las papeletas. La de Victor es la última en caer al montón.',
    'c-vote2': 'Nunca sabrás qué pasó en esa escalera. La duda es razonable.',
}
