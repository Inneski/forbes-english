# -*- coding: utf-8 -*-
"""Spanish strings for Dead by Teatime. See i18n_dead_by_teatime.py.

Informal "tú", as the course chrome. T is the chrome, N the narrative behind
the Translate button, QT each question slide's eyebrow, title, instruction
(None where the stem is a gap: the English being taught stays English) and
explanation. Every CAPS grammar token and every cited English form stays
English, in Spanish quotes. Written in-session; no native check yet."""

T = dict(
    coverTitle='Dead by <em>Teatime</em>',
    coverSub='Lunes en Lowfield. A los vecinos les pasa algo, y tú tienes las únicas llaves de la bolera.',
    chipLevel='B1 · Intermedio', chipFocus='Must · have to · should · oraciones de relativo',
    chipCount='60–80 minutos',
    btnContinue='Continuar →', btnChoose='Elegir', btnHead='Rumbo a Lowfield Lanes →',
    btnRevisit='Cambiar de opinión',
    actBefore='Antes de empezar',

    howEyebrow='Cómo funciona el juego', howTitle='No pierdas los nervios.',
    howDp='Puntos', howDpBody='Una respuesta correcta suma <strong>+1 punto</strong>.',
    howTime='Nervios',
    howTimeBody='Empiezas con cinco. Una respuesta incorrecta cuesta uno. Si llegas a cero, el grupo deja de '
                'confiar en tus planes.',
    howClues='Paradas',
    howCluesBody='Tres paradas antes de la bolera, en el orden que quieras. Lowfield Lanes se abre cuando hayas '
                 'hecho las tres.',
    howAloud='Lee cada escena en voz alta y explica tu elección en inglés antes de hacer clic.',
    ledDp='Puntos', ledTime='Nervios', ledClues='Paradas',

    briefEyebrow='Prólogo · lunes, 7:40', briefTitle='Lowfield no está bien.',
    castEyebrow='Antes de salir · tu gente', castTitle='Quién es quién.',
    cast1='Tú', cast1Body='La persona que tiene las llaves de Lowfield Lanes.',
    cast2='Gaz', cast2Body='Tu compañero de piso, que nunca se ha despertado antes de las diez.',
    cast3='Nan', cast3Body='Tu abuela, cuyo bate de críquet tiene nombre.',
    cast4='Priya', cast4Body='La técnica de ambulancias que todavía tiene tu mejor sudadera.',
    cast5='Colin', cast5Body='El nuevo novio de Priya, que ha leído todos los manuales de supervivencia.',
    cast6='Mr Bell', cast6Body='El hombre cuya tienda de la esquina nunca cierra.',

    labEyebrow1='Antes de salir · tus herramientas · 1 de 2', labTitle1='Normas y consejos.',
    labEyebrow2='Antes de salir · tus herramientas · 2 de 2', labTitle2='Who, which, where, whose.',
    lab1='Una norma, o algo que tú crees necesario. MUSTN’T: está prohibido.',
    lab2='Una obligación que viene de fuera: una norma, un horario, la situación.',
    lab3='No es necesario, así que puedes elegir. No es lo mismo que MUSTN’T.',
    lab4='Un consejo: una buena idea, o una mala.',
    lab5='Personas: WHO. Cosas: WHICH. Ambas: THAT.',
    lab6='Un lugar donde pasa algo: WHERE. Posesión: WHOSE + sustantivo.',
    lab7='El pronombre puede desaparecer cuando le sigue un sujeto nuevo.',
    lab8='Información extra: entre comas, y nunca THAT.',

    hubEyebrow='Acto II · tres paradas', hubTitle='¿A quién vas a buscar primero?',
    stopA='Parada A · la casa de Nan', stopABody='Nan no contesta al teléfono.',
    stopB='Parada B · la base de ambulancias', stopBBody='El último mensaje de Priya vino de aquí.',
    stopC='Parada C · la tienda de Bell', stopCBody='Provisiones, y la única tienda que sigue abierta.',

    lanesEyebrow='Acto III · Lowfield Lanes', lanesTitle='Ocho pistas y una fachada de cristal.',
    sayLanes='Dilo en voz alta: tres normas para la bolera. Una con MUST, una con MUSTN’T y una con SHOULD.',
    forkEyebrow='Acto IV · medianoche', forkTitle='Se va la luz.',
    routeBack='Volver a arrancar el generador del patio', routeFront='Atrincherar las puertas de cristal',
    explainFirst='Explica tu elección en inglés antes de hacer clic.',
    dawnEyebrow='Acto V · por la mañana', dawnTitle='Luz del día.',
    sayDawn='Dilo en voz alta: describe a una persona del grupo en una frase, con WHO o WHOSE.',

    decisionEyebrow='La decisión', decisionTitle='¿Cómo salís de aquí?',
    voteBus='Todos al autobús', voteBusBody='Conduce Nan. Nadie protesta.',
    voteWait='Esperar al ejército', voteWaitBody='Quedarse detrás de la barricada.',
    voteSolo='Huir tú solo', voteSoloBody='Solo eres más rápido.',
    branchLocked='Ya nadie confía en tus planes',
    endBus='Final I · la huida lenta', endBusTitle='A quince kilómetros por hora.',
    endWait='Final II · la larga espera', endWaitTitle='Detrás de la nevera.',
    endSolo='Final III · tú solo', endSoloTitle='Nadie que sujete la puerta.',
    sayBus='Cuenta la historia de la noche en 60 segundos. Usa un WHO, un WHERE y un WHOSE.',
    sayWait='Escribe tres normas de la casa para el jueves: una con MUST, una con MUSTN’T y una con DON’T HAVE TO.',
    saySolo='¿Qué consejo te darías a ti mismo? Empieza con «You shouldn’t …». Luego cambia de opinión.',
    resRoute='Solo cuentan las preguntas que aparecieron en tu camino.',

    glossShow='Traducir', glossHide='Ocultar traducción',
    resPerfect='Impecable. Todos habéis salido.',
    resStrong='Muy buen trabajo. Solo algunos sustos.',
    resMid='Has sobrevivido, con algún que otro susto.',
    resLow='Vivo, por los pelos. Repasa tus herramientas.',

    actTitle='Ahora planea tu propia supervivencia.',
    actUse='Usa al menos tres de estas',
    actSpeakBrief='En parejas o en grupos de tres. Poneos de acuerdo en un plan y explicádselo a la clase.',
    actSpeak1='Tu ciudad recibe una alerta de emergencia. Acordad cinco normas para vuestro grupo: dos con MUST '
              'o MUSTN’T, dos con HAVE TO o DON’T HAVE TO, y una con SHOULD.',
    actSpeak2='Elegid vuestro refugio: un lugar que conozcáis bien. Describidlo con WHERE, WHO y WHICH: la '
              'habitación donde dormiríais, la persona que cocinaría.',
    actSpeak3='Elige a tres personas que conozcas para tu equipo. Describe a cada una en una frase, sin decir '
              'el nombre: «the one whose …», «the friend who …». Tu compañero adivina.',
    actWriteKind='Escritura · 120–180 palabras',
    actWriteBrief='Escribe el cartel para la puerta de tu refugio. Di quién puede entrar, qué hay que hacer y '
                  'qué está prohibido, de qué no hay que preocuparse, y da un consejo. Usa al menos dos oraciones '
                  'de relativo.',
    actPlaceholder='WELCOME TO …',
)

ACTS = {'Before you begin': 'Antes de empezar', 'Act I': 'Acto I', 'Act II': 'Acto II', 'Stop A': 'Parada A',
        'Stop B': 'Parada B', 'Stop C': 'Parada C', 'Act III': 'Acto III', 'Act IV': 'Acto IV',
        'Act V': 'Acto V', 'Ending': 'Final', 'Activation': 'Práctica'}

OF = '%d de %d'

N = {
    'brief': 'Lowfield, un pueblo tranquilo a las afueras de Londres. Lunes, 7:40 de la mañana. Tu móvil muestra '
             'cuarenta llamadas perdidas y una alerta de emergencia. A los vecinos les pasa algo. Eres el '
             'subdirector de Lowfield Lanes, la bolera, y tienes el único juego de llaves. Tu misión: llevar a '
             'tu gente hasta allí antes de que oscurezca.',
    'streets': 'Lowfield está en silencio, pero no del buen tipo. Antes de la bolera hay tres paradas. ¿En qué '
               'orden?',
    'lanes': 'La bolera brilla al final de la calle principal. Abres las puertas: ocho pistas, una cafetería, '
             'una máquina de gancho llena de peluches y una fachada de cristal que nunca se diseñó para dejar '
             'nada fuera.',
    'noise': 'Medianoche. Las luces parpadean y se apagan. El generador del patio trasero se ha parado, y las '
             'figuras de fuera se acercan al cristal. Dos ideas, y no hay tiempo para probar las dos.',
    'dawn': 'Por la mañana. La radio dice que el ejército está despejando el pueblo calle por calle. De día, '
            'las figuras de fuera son más lentas. En el aparcamiento está el minibús de la Liga de Bolos para '
            'Mayores de 70, y Nan tiene las llaves. Cómo no.',
    'end-bus': 'Os abrís paso por el aparcamiento con un bate de críquet, dos bolas de bolos y un libro muy gordo. Luego Nan conduce el minibús por el centro de la calle principal a quince kilómetros por hora. La mano de Gaz está bien. Geoffrey tiene una abolladura. A la salida del pueblo, un soldado os hace señas para que paséis.',
    'end-wait': 'Os quedáis detrás de la nevera de la cafetería hasta que llega el ejército, el jueves. Todos '
                'sobreviven, sobre todo a base de patatas fritas. Nan dice que ha pasado Navidades peores.',
    'end-solo': 'Te escapas solo por la puerta de atrás. Eres más rápido, sí. Pero la llave del almacén está en '
                'tu bolsillo, y la gente que has dejado atrás no puede llegar a la comida.',

    'q-q01': 'Las 7:40. Tu móvil vibra: ALERTA DE EMERGENCIA. Quédense en casa. Cierren las puertas con llave. '
             'Gaz la lee en voz alta con la boca llena de tostada.',
    'q-q02': 'Algo está arañando la puerta de la calle. Gaz alarga la mano hacia el pomo. La alerta decía: no '
             'abran la puerta a nadie.',
    'q-q03': 'En la tele, una presentadora muy tranquila explica las nuevas normas. Por la parte de abajo de la '
             'pantalla pasa un rótulo rojo: ¿LE HAN MORDIDO? VAYA AL HOSPITAL.',
    'q-q04': 'Gaz anuncia su plan: volver a la cama hasta que todo pase. Tú tienes una idea mejor. Nan vive '
             'sola, y no contesta al teléfono.',
    'q-q05': 'Nan espera en el recibidor con su bate de críquet. Lo llama Geoffrey. Con monstruos o sin ellos, '
             'en su casa hay normas.',
    'q-q06': 'Nan no se va sin sus pastillas para el corazón. Están en el baño de arriba, y allí arriba algo se '
             'mueve.',
    'q-q07': 'Subes a por las pastillas. En el rellano, algo en bata se da la vuelta y se tambalea hacia ti. Nan está justo detrás de ti con Geoffrey, ya en pleno golpe.',
    'q-q08': 'Bajas con las pastillas. Nan ha hecho una bolsa: galletas, una linterna, Geoffrey. Te pregunta si '
             'necesita su abrigo grande de invierno. Estamos en junio.',
    'q-q09': 'La base de ambulancias está vacía, salvo por un hombre en bata. Ha visto a Priya. Priya y tú '
             'estuvisteis juntos tres años.',
    'q-q10': 'En el aparcamiento, una ambulancia tiene las puertas traseras abiertas. Algo con uniforme verde está saliendo, con los brazos por delante. Agarras la puerta y empujas.',
    'q-q11': 'En la puerta del cuarto del fondo hay una nota con la letra de Priya: AQUÍ DENTRO. LLAMA TRES '
             'VECES SI ERES HUMANO.',
    'q-q12': 'Priya abre la puerta. Detrás de ella hay un hombre alto con sombrero de acampada y un libro que se '
             'llama Surviving Anything. «Este es Colin», dice.',
    'q-q13': 'La tienda de la esquina de Mr Bell está abierta. Cómo no. Mr Bell está detrás del mostrador bajo '
             'un cartel nuevo: SOLO EFECTIVO. PROHIBIDO MORDER.',
    'q-q14': 'Tienes diez minutos y una cesta. Gaz quiere patatas fritas. Nan quiere té. Tú quieres las pilas '
             'de linterna que Mr Bell guarda detrás del mostrador.',
    'q-q15': 'Un cliente en la caja gruñe y se abalanza sobre el mostrador. Mr Bell lo tumba con un periódico enrollado y vuelve a su crucigrama. No piensa irse.',
    'q-q16': 'Mr Bell te da un consejo para el camino: quédate en el centro de la calle y no corras. Se fijan '
             'en quien corre.',
    'q-q17': 'Colin abre su libro. «Regla número uno: asegurar las entradas.» Por una vez, tiene razón. Solo una '
             'puerta del edificio se cierra por dentro.',
    'q-q18': 'Colin escribe normas en mayúsculas en el marcador. Norma cuatro: PROHIBIDO HACER RUIDO DE NOCHE. '
             'Gaz pregunta si hablar también cuenta.',
    'q-q19': 'Priya viene contigo. El generador necesita una llave, y la llave está en el bolsillo de Colin. '
             'Colin está dormido en la pista tres.',
    'q-q20': 'Gaz y tú arrastráis la nevera de la cafetería hasta las puertas de cristal. Después de un metro, '
             'Gaz quiere un descanso.',
    'q-q21': 'A las dos de la mañana, tres de ellos se cuelan por el cristal roto. Priya rocía la entrada con el extintor para impedirles ver. Eso solo les da unos segundos. Gaz coge una bola de bolos y te mira: ¿a cuál primero?',
    'q-q22': 'El último cae en la pista uno. Gaz te enseña un pequeño mordisco en la mano. «Fue una bolsa de patatas», dice. «Probablemente.» Priya se lo limpia y le da tres instrucciones.',
    'q-q23': 'A las tres de la mañana, la máquina de gancho empieza a tocar su cancioncita. Algo se mueve dentro '
             'de la urna de cristal, detrás de los peluches.',
    'q-q24': 'Colin hojea su libro. No hay ningún capítulo sobre máquinas de gancho. Por primera vez, te pregunta '
             'qué hacer.',
    'q-q25': 'La máquina de gancho se abre de golpe y cae un zombi con camisa de bolos, con Mr Bell justo detrás. Lo tumba con su bolsa de dinero. «La tienda está cerrada», dice.',
    'q-q26': 'Seis de ellos están entre las puertas y el minibús, lentos a la luz del día. Nan levanta a Geoffrey. Colin levanta su libro. Todos te miran.',
}

QT = {
    'q01': ('Acto I · la alerta', 'Una alerta de emergencia.', None,
            'MUST + verbo en forma base, sin TO y sin -S: «must stay». MUST es igual con todos los sujetos.'),
    'q02': ('Acto I · la puerta', 'Algo está arañando.', None,
            'MUSTN’T: está prohibido. DON’T HAVE TO solo significa que no es necesario, y eso no es lo que dice '
            'la alerta. SHOULD nunca lleva TO.'),
    'q03': ('Acto I · las noticias', 'Las noticias de las ocho.', '¿Qué frase es correcta?',
            'ANYONE es una persona, así que WHO (o THAT). WHICH es para cosas. WHO ya es el sujeto, así que no '
            'hace falta HE.'),
    'q04': ('Acto I · el plan', 'Gaz tiene un plan.', None,
            'SHOULD + verbo en forma base da un consejo: «should check». Después de SHOULD no va TO. OUGHT '
            'necesita TO: «ought to check».'),
    'q05': ('Parada A · la casa de Nan', 'Nan abre la puerta.', None,
            'HAVE TO con I, YOU, WE, THEY; HAS TO con HE, SHE, IT. Una norma de la casa es una obligación que '
            'viene de fuera: «you have to wipe your feet».'),
    'q06': ('Parada A · las pastillas', 'Las pastillas de Nan.', None,
            'Información extra entre comas: WHICH para cosas, y nunca THAT después de una coma. WHO es para '
            'personas.'),
    'q07': ('Parada A · la escalera', '¡Agáchate!', None,
            'SHOULDN’T + verbo en forma base: el consejo de no hacer algo. La negación es SHOULDN’T, nunca DON’T '
            'SHOULD, y no lleva TO.'),
    'q08': ('Parada A · control', 'Nan viene contigo.', 'Elige la respuesta que significa que NO es necesario.',
            'Parada A completada. DON’T HAVE TO: no es necesario, así que Nan puede elegir. MUSTN’T lo '
            'prohibiría, y MUST no tiene forma con DON’T.'),
    'q09': ('Parada B · la base de ambulancias', '¿Dónde está Priya?', None,
            'WHO para una persona. WHICH es para cosas, y WHOSE para la posesión. Aquí también vale THAT, y '
            'también sin pronombre.'),
    'q10': ('Parada B · el aparcamiento', 'Ya no es un técnico de ambulancias.', None,
            'WHOSE + sustantivo indica posesión: sus brazos, así que «whose arms». Después de WHO haría falta un '
            'verbo («who is reaching out»), y nunca WHO + HIS.'),
    'q11': ('Parada B · una nota', 'Una nota en la puerta.', None,
            'Un lugar donde pasa algo lleva WHERE: «the place where she is hiding». WHICH solo necesita una '
            'preposición al final: «the place which she is hiding in».'),
    'q12': ('Parada B · control', 'Te presento a Colin.', '¿Qué frase lo describe correctamente?',
            'Parada B completada. La información extra va entre comas: «, WHOSE book …,». Después de una coma, '
            'nunca THAT; y WHOSE sustituye a WHO + HIS.'),
    'q13': ('Parada C · la tienda de Bell', 'Abierta, como siempre.', None,
            'La tienda es la que vende, así que es el sujeto: WHICH o THAT. WHERE necesita un sujeto nuevo: '
            '«the shop where you can buy batteries».'),
    'q14': ('Parada C · la lista', 'Una cesta.', '¿Qué frase es correcta?',
            'El pronombre puede desaparecer cuando le sigue un sujeto nuevo: «the batteries (that) Bell keeps». '
            'No repitas el objeto con THEM, y WHO es solo para personas.'),
    'q15': ('Parada C · la caja', 'Mr Bell se queda.', None,
            'SOMEBODY es singular, como HE o SHE, así que HAS TO: «somebody has to look after it». MUST nunca '
            'lleva TO.'),
    'q16': ('Parada C · control', 'Un consejo desde el mostrador.', 'Cuenta su consejo correctamente.',
            'Parada C completada. SHOULDN’T + verbo en forma base: un consejo. La negación nunca es DON’T SHOULD, '
            'y SHOULD nunca lleva TO.'),
    'q17': ('Acto III · el almacén', 'Una cerradura que funciona.', None,
            'La habitación es el objeto de LOCK, así que el pronombre puede desaparecer: «the room (that) we can '
            'lock». No añadas IT: el relativo ya representa la habitación.'),
    'q18': ('Acto III · normas de la casa', 'Las normas de Colin.', None,
            'MUSTN’T: prohibido, así que nada de gritar. DON’T HAVE TO: no es necesario, así que susurrar es '
            'opcional. HAVEN’T TO no existe en inglés.'),
    'q19': ('Acto IV · el patio trasero', 'El generador.', None,
            'WHO para una persona, y aquí es el sujeto: «the man who is asleep». WHOSE siempre necesita un '
            'sustantivo detrás: «the man whose key we need».'),
    'q20': ('Acto IV · las puertas de entrada', 'La barricada.', None,
            'HAVE TO: la situación lo hace necesario. DON’T HAVE TO significa lo contrario. SHOULD nunca lleva TO.'),
    'q21': ('Acto IV · las 2 de la mañana', 'El cristal cede.', None,
            'El que está más cerca de Nan es el sujeto de IS, así que THAT (o WHO). WHERE es para lugares, y WHOSE '
            'siempre necesita un sustantivo detrás.'),
    'q22': ('Acto IV · primeros auxilios', 'Priya toma el mando.', '¿Qué instrucción es un consejo y no una norma?',
            'SHOULD da un consejo: una buena idea. MUSTN’T y HAVE TO son normas, sin opción. Priya usa las tres, '
            'y Gaz no cumple ninguna.'),
    'q23': ('Acto IV · las 3 de la mañana', 'Un ruido en la oscuridad.', None,
            'Un lugar donde pasó algo lleva WHERE, es decir, «in which». WHICH solo necesitaría IN al final: '
            '«the machine which Gaz won a rabbit in».'),
    'q24': ('Acto IV · el manual', 'No hay capítulo para esto.', None,
            'Una pregunta con HAVE TO usa DO: «Do we have to open it?» MUST forma la pregunta sin DO: «Must we '
            'open it?» SHOULD nunca lleva TO.'),
    'q25': ('Acto IV · la máquina de gancho', 'Solo es Mr Bell.', '¿Qué frase es correcta?',
            'Información extra sobre una persona concreta: comas + WHO, nunca THAT. No repitas el sujeto: WHO ya '
            'representa a Mr Bell, así que sin HE.'),
    'q26': ('Acto V · la decisión', 'Toma la decisión.', '¿Qué frase da al grupo un consejo claro?',
            'SHOULD + verbo en forma base: «should leave». Es un consejo, no una orden: quieres que el grupo esté '
            'de acuerdo contigo.'),
}
