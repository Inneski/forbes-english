# -*- coding: utf-8 -*-
"""B1 Mixed Grammar Tests — Spanish. Same keys as mixed_b1_en.py.

Tense names stay in English; the other area names translate. English
examples stay English, in «» quotes.
"""

AREA = dict(
    presSimple='Present Simple', presCont='Present Continuous',
    pastSimple='Past Simple', pastCont='Past Continuous',
    presPerf='Present Perfect', futSimple='Futuro con WILL',
    compar='Comparativos y superlativos', modals='Verbos modales',
    cond='Condicionales', passive='La pasiva', relative='Oraciones de relativo',
    questions='Preguntas', quant='Cuantificadores', prep='Preposiciones',
    stative='Verbos de estado',
)

COMMON = dict(
    chipLevel='B1 &middot; Intermedio',
    chipFocus='35 puntos &middot; cinco partes',
    chipCount='{N} diapositivas',

    eIntro='Antes de empezar',
    tIntro='Un test, diez áreas de gramática',
    introA='Cinco partes',
    introAb='10 de opción múltiple &middot; una historia con 8 huecos &middot; '
            '6 de verdadero o falso &middot; 5 frases para construir &middot; '
            '6 errores para corregir.',
    introAn='Cada respuesta se explica en cuanto la das.',
    introB='Qué evalúa',
    introBb='Tiempos presentes, pasados y perfectos, WILL, comparativos, '
            'verbos modales, condicionales, la pasiva, oraciones de relativo y '
            'preguntas.',
    introBn='Trabaja solo y no busques nada. Tu nota solo sirve si es honesta.',

    eMC='Parte 1 &middot; Opción múltiple',
    tMC='Elige la forma correcta',
    eStory='Parte 2 &middot; Lectura',
    eTF='Parte 3 &middot; Verdadero o falso',
    tTF='¿Es cierta esta regla?',
    eOrder='Parte 4 &middot; Construir frases',
    tOrder='Ordena las partes',
    hOrder='Haz clic en un bloque para colocarlo y en uno colocado para '
           'quitarlo. Un punto por la frase entera.',
    eFix='Parte 5 &middot; Corrección de errores',
    tFix='Encuentra el error y corrígelo',
    hFix='Cada frase tiene un error. Escribe la frase entera otra vez, '
         'corregida.',

    resPerfect='Impecable. La gramática B1 ya es natural para ti &mdash; es '
               'hora de empezar el B2.',
    resStrong='Sólido. Quedan algunos huecos; la lista de abajo te dice '
              'exactamente cuáles.',
    resMid='Buen progreso. Lee las explicaciones de los que fallaste y vuelve '
           'a intentarlo.',
    resLow='Sigue construyendo. Repasa despacio la lista de abajo y haz el '
           'test otra vez mañana.',

    actUse='Usa al menos tres',
    actSpeakBrief='En parejas. Usa la gramática entre paréntesis.',
    actWriteKind='Escritura',
)

P1 = dict(
    coverTitle='Test de gramática <em>mixta</em>',
    coverSub='Diez áreas de gramática, un test: tiempos verbales, modales, '
             'condicionales, la pasiva y más.',
    tStory='El día de Elena',
    hSt1='Escribe el verbo entre paréntesis en la forma correcta. '
         '&laquo;Oversleep&raquo; = quedarse dormido.',
    hSt2='Escribe el verbo entre paréntesis en la forma correcta. '
         '&laquo;Borrow&raquo; = pedir prestado.',
    hSt3='El último hueco necesita un cuantificador, no un verbo: elige uno de '
         'los dos entre paréntesis.',
    gTournament='&laquo;Tournament&raquo; = torneo.',
    gSeatbelt='&laquo;Seatbelt&raquo; = cinturón de seguridad.',

    x_mc1='&laquo;Listen!&raquo; significa ahora: la acción está en curso, IS '
          '+ knocking. &laquo;Knocks&raquo; es un hábito; &laquo;knocked&raquo; '
          'y &laquo;was knocking&raquo; son pasado.',
    x_mc2='WHILE + WAS / WERE + -ING da la acción de fondo, más larga; el Past '
          'Simple (&laquo;rang&raquo;) la interrumpe. Las otras tres son formas '
          'de presente.',
    x_mc3='SINCE + un momento (2019) pide HAS / HAVE + participio. '
          '&laquo;Lived&raquo; no va con &laquo;since&raquo;, y las formas de '
          'presente tampoco.',
    x_mc4='&laquo;I think&raquo; introduce una opinión sobre el futuro: WILL + '
          'verbo. &laquo;Is winning&raquo; querría decir que el partido se '
          'juega ahora.',
    x_mc5='Comparado con todas las películas del año, así que el superlativo: '
          'THE BEST. &laquo;Goodest&raquo; y &laquo;more good&raquo; no '
          'existen; &laquo;better&raquo; compara solo dos.',
    x_mc6='Una ley es una obligación fuerte: MUST + verbo. &laquo;Might&raquo; '
          'y &laquo;could&raquo; son posibilidad; &laquo;would&raquo; es '
          'hipotético.',
    x_mc7='Primer condicional: IF + Present Simple, y WILL en la otra parte. '
          'Aquí WILL nunca va después de IF.',
    x_mc8='&laquo;Would learn&raquo; muestra una situación imaginaria, así que '
          'segundo condicional: IF + Past Simple (&laquo;had&raquo;).',
    x_mc9='Un puente no se construye solo, así que la pasiva: WAS + '
          'participio. &laquo;Built&raquo; solo es activa y nadie hace la '
          'acción.',
    x_mc10='WHO para personas. WHICH para cosas, WHOSE para posesión, WHERE '
           'para lugares.',

    x_st1='&laquo;Usually&raquo; es un hábito: Present Simple, y '
          '&laquo;she&raquo; lleva -S (&laquo;gets up&raquo;). &laquo;This '
          'morning&raquo; ya terminó: Past Simple &laquo;overslept&raquo; '
          '(irregular).',
    x_st2='&laquo;For almost three years now&raquo; llega hasta hoy: HAS + '
          'lived. HAS BEEN living también es correcto.',
    x_st3='WHILE + WAS + -ING para la acción más larga; el golpe en la puerta '
          '(&laquo;knocked&raquo;) la interrumpe.',
    x_st4='La mesa está reservada, así que es un plan fijo: IS + meeting. IS '
          'GOING TO meet también es correcto.',
    x_st5='Primer condicional. Después de IF, Present Simple '
          '(&laquo;is&raquo;), no WILL; el resultado lleva WILL + go.',
    x_st6='En una frase afirmativa decimos A LOT OF. MUCH es para negativas y '
          'preguntas: &laquo;They don&rsquo;t serve much seafood.&raquo;',

    tf1='Usamos el Present Perfect con un tiempo terminado, como '
        '&laquo;yesterday&raquo; o &laquo;in 2010&raquo;.',
    tf2='&laquo;Must&raquo; y &laquo;have to&raquo; expresan obligación, pero '
        'solo &laquo;have to&raquo; tiene forma de pasado: &laquo;had '
        'to&raquo;.',
    tf3='En el primer condicional usamos &laquo;will&raquo; después de '
        '&laquo;if&raquo;.',
    tf4='Delante de un superlativo suele ir &laquo;the&raquo;.',
    tf5='La pasiva es BE + participio.',
    tf6='En las oraciones de relativo usamos &laquo;who&raquo; para personas '
        'y &laquo;which&raquo; para cosas.',
    x_tf1='Falso. Un tiempo terminado pide el Past Simple: &laquo;I visited '
          'Paris in 2010&raquo;, no &laquo;I have visited&raquo;.',
    x_tf2='Verdadero. MUST no tiene pasado propio, así que para el pasado '
          'usamos HAD TO.',
    x_tf3='Falso. Después de IF, Present Simple (&laquo;If it rains&raquo;); '
          'WILL va en la otra parte (&laquo;we&rsquo;ll stay in&raquo;).',
    x_tf4='Verdadero. THE señala una cosa como la única de su grupo: THE best, '
          'THE tallest, THE most expensive.',
    x_tf5='Verdadero. &laquo;Is built&raquo;, &laquo;was written&raquo;, '
          '&laquo;has been finished&raquo;: siempre una forma de BE + '
          'participio.',
    x_tf6='Verdadero. En el inglés de cada día THAT puede sustituir a los dos, '
          'pero WHO es solo para personas y WHICH solo para cosas.',

    x_or1='La pasiva: sujeto + WAS + participio, y luego el tiempo.',
    x_or2='&laquo;Who lives next door&raquo; va justo después de &laquo;the '
          'man&raquo; y dice qué hombre. Luego el verbo principal, IS.',
    x_or3='Palabra interrogativa + DID + sujeto + infinitivo. Después de DID '
          'el verbo no lleva -ED: &laquo;go&raquo;, no &laquo;went&raquo;.',
    x_or4='Segundo condicional: IF + Past Simple (&laquo;were&raquo;), luego '
          'WOULD (&rsquo;D) + verbo.',
    x_or5='MUCH delante de un comparativo lo refuerza; THAN introduce lo '
          'segundo.',

    x_fx1='FOR + una duración (five years). SINCE + un punto de partida '
          '(2019, March).',
    x_fx2='Después de IF en el primer condicional, Present Simple: &laquo;If I '
          'have time&raquo;. WILL se queda en la otra parte.',
    x_fx3='&laquo;Better&raquo; ya es comparativo. MORE + BETTER nunca es '
          'correcto.',
    x_fx4='La pasiva necesita el participio: write &rarr; wrote &rarr; '
          'WRITTEN.',
    x_fx5='&laquo;Money&raquo; es incontable: MUCH, no MANY. MANY es para '
          'sustantivos en plural: &laquo;many coins&raquo;.',
    x_fx6='WHICH es para cosas. Para una persona, WHO (o THAT).',

    actTitle='Ahora úsalo',
    actSpeak1='Tu mañana normal, y luego qué fue distinto esta mañana. '
              '(Present Simple, Past Simple)',
    actSpeak2='¿Qué harías con un año entero libre? Pregúntaselo también a tu '
              'pareja. (segundo condicional)',
    actSpeak3='Un edificio famoso de tu ciudad: ¿cuándo y quién lo construyó? '
              '(la pasiva)',
    actWriteBrief='Un email, 120&ndash;150 palabras, a un amigo que viene la '
                  'semana que viene: tus planes, qué tiene que traer y qué '
                  'haréis si llueve.',
    actPlaceholder='Hi! I can&rsquo;t wait to see you next week&hellip;',
)

P2 = dict(
    coverTitle='Test de gramática mixta <em>parte 2</em>',
    coverSub='Diez puntos de gramática más, todo frases nuevas: tiempos '
             'verbales, modales, condicionales, la pasiva y más.',
    tStory='El viaje de Diego',
    hSt1='Escribe el verbo entre paréntesis en la forma correcta.',
    hSt2='Escribe el verbo entre paréntesis en la forma correcta. '
         '&laquo;Suitcase&raquo; = maleta.',
    hSt3='Escribe el verbo entre paréntesis en la forma correcta. '
         '&laquo;Delayed&raquo; = retrasado.',
    gForbidden='&laquo;Forbidden&raquo; = prohibido.',

    x_mc1='&laquo;Be quiet!&raquo; significa ahora: la acción está en curso, '
          'IS + sleeping. &laquo;Sleeps&raquo; es un hábito; las otras dos son '
          'pasado.',
    x_mc2='WHILE + WERE + -ING da la acción de fondo que las luces '
          '(&laquo;went out&raquo;) interrumpieron. Las otras son formas de '
          'presente.',
    x_mc3='&laquo;For ten years now&raquo; llega hasta hoy: HAVE + known. '
          '&laquo;Are knowing&raquo; está mal porque KNOW no es una acción en '
          'curso; &laquo;knew&raquo; dice que ya terminó.',
    x_mc4='Una promesa es una decisión que se toma al hablar: WILL + verbo. '
          '&laquo;Am helping&raquo; necesitaría un plan ya acordado.',
    x_mc5='Comparado con todas las ciudades, así que el superlativo: THE + '
          'busiEST. &laquo;Busier&raquo; compara dos; &laquo;most '
          'busiest&raquo; lo dice dos veces.',
    x_mc6='&laquo;Forbidden&raquo; es una prohibición: MUSTN&rsquo;T. '
          '&laquo;Don&rsquo;t have to&raquo; significa que no es necesario, '
          'casi lo contrario.',
    x_mc7='Primer condicional: IF + Present Simple, y WON&rsquo;T / WILL en la '
          'otra parte.',
    x_mc8='&laquo;Could join&raquo; muestra una situación imaginaria: IF + '
          'Past Simple, y con BE usamos WERE para todas las personas.',
    x_mc9='El cuadro no se pintó solo, así que la pasiva: WAS + participio, y '
          'BY nombra al pintor.',
    x_mc10='WHICH (o THAT) para cosas. WHO es para personas, WHOSE para '
           'posesión, WHERE para lugares.',

    x_st1='&laquo;Every summer&raquo; es un hábito: Present Simple, y '
          '&laquo;he&raquo; lleva -S.',
    x_st2='&laquo;Last month&raquo; ya terminó: Past Simple '
          '&laquo;booked&raquo;. El amigo lo recomendó antes; '
          '&laquo;recommended&raquo; y &laquo;had recommended&raquo; son '
          'correctos.',
    x_st3='&laquo;Never &hellip; before&raquo; es su vida hasta ahora: HAS + '
          'NEVER + visited.',
    x_st4='WHILE + WAS + -ING para la acción más larga; el momento en que se '
          'dio cuenta la interrumpe.',
    x_st5='El asiento está elegido, así que es un plan fijo: IS + flying. IS '
          'GOING TO fly también es correcto.',
    x_st6='Primer condicional. Después de IF, Present Simple '
          '(&laquo;is&raquo;); el resultado lleva WILL + miss. MIGHT miss '
          'también es correcto.',

    tf1='El Present Continuous puede expresar un plan fijo en el futuro, como '
        '&laquo;I&rsquo;m flying to Rome on Monday.&raquo;',
    tf2='&laquo;Mustn&rsquo;t&raquo; y &laquo;don&rsquo;t have to&raquo; '
        'significan lo mismo.',
    tf3='En el segundo condicional solemos usar &laquo;were&raquo; en vez de '
        '&laquo;was&raquo; con I, he, she e it.',
    tf4='Los adjetivos de dos sílabas siempre llevan &laquo;more&raquo;, nunca '
        '&laquo;-er&raquo;.',
    tf5='La pasiva de &laquo;People speak English here&raquo; es '
        '&laquo;English is spoken here.&raquo;',
    tf6='&laquo;Whose&raquo; se usa para hablar de posesión.',
    x_tf1='Verdadero. Cuando el plan está fijado (un billete, una hora), el '
          'Present Continuous es la opción natural.',
    x_tf2='Falso. MUSTN&rsquo;T significa que no está permitido. DON&rsquo;T '
          'HAVE TO significa que no es necesario. Son casi opuestos.',
    x_tf3='Verdadero. &laquo;If I were you&raquo;, &laquo;If he were '
          'taller&raquo;. &laquo;Was&raquo; es común al hablar, pero WERE es '
          'la forma estándar.',
    x_tf4='Falso. Muchos llevan -ER: happy &rarr; happier, easy &rarr; '
          'easier, narrow &rarr; narrower.',
    x_tf5='Verdadero. El objeto (&laquo;English&raquo;) pasa a ser el sujeto, '
          'y el verbo pasa a IS + participio.',
    x_tf6='Verdadero. &laquo;Whose car is this?&raquo; &middot; &laquo;the '
          'man whose car was stolen&raquo;.',

    x_or1='Una pregunta en pasiva: WAS + sujeto + participio, y luego BY + '
          'quién lo hizo.',
    x_or2='WHERE introduce una oración sobre un lugar: &laquo;where we had '
          'dinner&raquo; dice qué restaurante.',
    x_or3='HOW LONG + HAVE + sujeto + participio: la pregunta en Present '
          'Perfect.',
    x_or4='Segundo condicional: IF + Past Simple (&laquo;had&raquo;), luego '
          'WOULD + verbo.',
    x_or5='THE + comparativo, THE + comparativo: dos cosas que cambian a la '
          'vez.',

    x_fx1='AGREE es una opinión, no una acción en curso: Present Simple, '
          '&laquo;I agree&raquo;.',
    x_fx2='MARRIED TO someone, no &laquo;married with&raquo;.',
    x_fx3='Después de IF en el segundo condicional, Past Simple: &laquo;If I '
          'had&raquo;. WOULD se queda en la otra parte.',
    x_fx4='&laquo;Easy&raquo; termina en -Y, así que lleva -IER: EASIER, no '
          '&laquo;more easy&raquo;.',
    x_fx5='En la pasiva, BY nombra quién lo hizo: &laquo;sent by the '
          'manager&raquo;. FOR sería quien lo recibe.',
    x_fx6='WHOSE ya significa &laquo;his&raquo;, así que &laquo;his&raquo; '
          'sobra. Bórralo.',

    actTitle='Ahora úsalo',
    actSpeak1='Tus planes para el sábado, y qué harás si llueve. (Present '
              'Continuous, primer condicional)',
    actSpeak2='En el trabajo o la escuela: tres cosas que no puedes hacer y '
              'tres que no tienes que hacer. (modales)',
    actSpeak3='Un viaje que salió mal: ¿qué estabas haciendo cuando pasó? '
              '(Past Continuous)',
    actWriteBrief='Una reseña, 120&ndash;150 palabras, de un lugar que '
                  'conoces: desde cuándo, por qué es famoso y por qué es el '
                  'mejor (o el peor).',
    actPlaceholder='I have been to &hellip; three times, and &hellip;',
)
