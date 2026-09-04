# -*- coding: utf-8 -*-
"""Interface strings for Lego Car Building (B2), Part I.

English, German and Spanish. Teach-card bodies use the six-item form so the
rule travels with its heading; the vocabulary being taught stays English.
"""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

TAIL = {
    'en': {'branchLocked': "'Your ledger does not support this ending'",
           'glossHide': "'Hide'", 'glossShow': "'Translate'",
           'ledClues': "'Clues'", 'ledDp': "'DP'", 'ledTime': "'Time'"},
    'de': {'branchLocked': "'Dein Protokoll trägt dieses Ende nicht'",
           'glossHide': "'Ausblenden'", 'glossShow': "'Übersetzen'",
           'ledClues': "'Hinweise'", 'ledDp': "'DP'", 'ledTime': "'Zeit'"},
    'es': {'branchLocked': "'Tu registro no admite este final'",
           'glossHide': "'Ocultar'", 'glossShow': "'Traducir'",
           'ledClues': "'Pistas'", 'ledDp': "'DP'", 'ledTime': "'Tiempo'"},
}

T = {}

T['en'] = dict(
    coverTitle='Lego Car Building <em>Part I</em>',
    coverSub='The words engineers actually use, and why the near-synonym is always wrong',
    chipLevel='B2 · Upper-intermediate', chipFocus='Design &amp; engineering vocabulary',
    chipCount='17 slides',

    deEyebrow='Before the questions', deTitle='Words for the thing before the thing',
    de1h='<em>Prototype</em> and <em>blueprint</em>', de1b=
        'A <strong>blueprint</strong> is the plan on paper. A <strong>prototype</strong> '
        'is the first one you actually build, made to be tested and thrown away. One '
        'is a drawing, the other is an object.',
    de1n='You draw a blueprint, you build a prototype. The verbs do not swap.',
    de2h='<em>Modular</em> and <em>iterative</em>', de2b=
        '<strong>Modular</strong> describes the thing: built from self-contained '
        'sections you can replace one at a time. <strong>Iterative</strong> describes '
        'the process: build, test, change, build again.',
    de2n='A modular design makes an iterative process cheap. They are not the same idea.',
    de3h='<em>Load-bearing</em> and <em>tolerance</em>', de3b=
        'A <strong>load-bearing</strong> part holds weight the rest depends on. '
        '<strong>Tolerance</strong> is how much error a fit will accept before it stops '
        'working &mdash; the gap between good enough and not.',
    de3n='Both come from real engineering, and both are used unchanged in everyday B2 English.',

    pvEyebrow='The register', pvTitle='Phrasal verbs are the technical ones here',
    pv1h='Before you start', pv1b=
        '<strong>Lay out</strong> the pieces &mdash; spread them where you can see '
        'them. <strong>Cross-reference</strong> the diagram with the parts list &mdash; '
        'check one against the other. Both are preparation, and both are separable.',
    pv1n='<em>Lay them out</em>, <em>cross-reference it against</em> &mdash; the object can sit inside.',
    pv2h='While you build', pv2b=
        'Pieces <strong>snap into</strong> place. When one does not, you '
        '<strong>troubleshoot</strong> the problem &mdash; work through it in order '
        'until you find the cause.',
    pv2n='<em>Troubleshoot</em> is one word and takes a direct object. Not <em>troubleshoot for</em>.',
    pv3h='At the end', pv3b=
        'You <strong>fine-tune</strong> the mechanism: small adjustments to something '
        'that already works. Not repair, not redesign &mdash; the last five per cent.',
    pv3n='If it is broken you fix it. You only fine-tune something already close.',

    prEyebrow='The C1 habit at B2', prTitle='The distractor is the near-synonym',
    pr1h='Read what the word rules out', pr1b=
        '<em>Align</em> is about position, not connection, so gluing and reinforcing '
        'are both wrong however sensible they sound. Each of these words says one '
        'thing and excludes the rest.',
    pr1n='Ask what the word does <em>not</em> mean. That is usually faster.',
    pr2h='<em>Orientation</em> is direction, not place', pr2b=
        'A beam in the wrong <strong>orientation</strong> is in the right position and '
        'facing the wrong way. Wrong length, wrong colour and unattached are three '
        'different errors with three different names.',
    pr2n='Position, orientation, dimension, colour &mdash; four properties, four words.',
    pr3h='<em>Retrofit</em> has a time built into it', pr3b=
        'To <strong>retrofit</strong> is to add something <em>after</em> the thing was '
        'finished. Rebuilding it, or leaving it alone, or stripping a feature out are '
        'all different actions.',
    pr3n='The word carries a sequence. That is what makes it precise.',

    mcEyebrow='Activity 1 · Multiple choice', mcTitle='What does the term actually mean?',
    q1why='<strong>To position something so it lines up correctly.</strong> '
          '<em>Align</em> is about relative position and nothing else &mdash; not '
          'joining, not reinforcing, not rebuilding.',
    q2why='<strong>It compensates for the difference in wheel speed during turns.</strong> '
          'On a bend the outer wheel travels further, so it has to turn faster. The '
          'differential lets it. It adds no power and locks nothing.',
    q3why='<strong>She had placed the piece facing the wrong direction or angle.</strong> '
          '<em>Orientation</em> is which way round something faces. Wrong colour, wrong '
          'length and not attached are three other errors with three other names.',
    q4why='<strong>The model was robust and held together even under physical stress.</strong> '
          '<em>Structural integrity</em> is about staying intact under load. It says '
          'nothing about weight, detail or how easily it comes apart.',
    q5why='<strong>To add a new feature to something that was already completed.</strong> '
          'The <em>retro-</em> is doing the work: the addition comes after the build was '
          'finished, not during it and not instead of it.',

    bankLabel='Word bank:',
    fibEyebrow='Activity 2 · The design vocabulary', fibTitle='One word fits each gap',
    fibHint='Eight words in the bank, five gaps. The three left over are the near-misses.',
    g1why='<strong>Prototype.</strong> The first working model, built to test an idea '
          'before anything goes into production. A blueprint would be the drawing.',
    g2why='<strong>Modular.</strong> Self-contained sections, each buildable and '
          'replaceable on its own. It describes the design, not the way it was arrived '
          'at.',
    g3why='<strong>Blueprint.</strong> The technical plan you build from. She is '
          'checking a document, not an object.',
    g4why='<strong>Load-bearing.</strong> A part that carries weight the rest of the '
          'structure depends on. Remove it and everything above comes down.',
    g5why='<strong>Iterative.</strong> Repeated cycles of test and refinement, each one '
          'improving on the last. It describes the process, not the product.',

    dndEyebrow='Activity 3 · The phrasal verbs', dndTitle='Complete the instruction',
    dndHint='Seven phrases in the bank, five gaps. Two belong to no gap here.',
    d1why='<strong>Lay out.</strong> Spread everything where you can see it, before you '
          'start. It is the preparation step, and it is separable: <em>lay them out</em>.',
    d2why='<strong>Troubleshoot.</strong> Work through a problem in order until you find '
          'the cause. One word, and it takes a direct object.',
    d3why='<strong>Snap into.</strong> The click of a piece seating firmly in its '
          'correct position &mdash; and the reason Lego works at all.',
    d4why='<strong>Cross-reference.</strong> Check one source against another. The '
          'diagram against the parts list, and neither on its own.',
    d5why='<strong>Fine-tune.</strong> Small, precise adjustments to something that '
          'already works. The last five per cent, not the repair.',

    actTitle='Talk through the build', actUse='Use at least four:',
    actSpeakBrief='One of you designed it, the other has to build it from your '
                  'description alone. Four minutes each, then swap.',
    actSpeak1='Describe how you would prepare a complex build before touching a single piece.',
    actSpeak2='Explain a mechanism you understand — gears, hinges, suspension — to someone who does not.',
    actSpeak3='Something in your build does not fit. Talk your partner through troubleshooting it.',
    actSpeak4='Describe a design you would call modular, and say what that buys you.',
    actWriteKind='Writing · 150–180 words',
    actWriteBrief='Write the design note that goes with a prototype. Say what the '
                  'blueprint specified, which parts are load-bearing, where the '
                  'tolerances are tight, and what the next iteration will change. Write '
                  'it for an engineer, not a customer.',
    actPlaceholder='The first prototype was laid out from the blueprint on…',

    resPerfect='Full marks. You are choosing by what the word excludes, which is the whole B2 move.',
    resStrong='Strong. Look again at the phrasal verbs — that is usually the last mark here.',
    resMid='Good base. Go back to the first slide: blueprint and prototype are a drawing and an object.',
    resLow='Read the three opening slides again. Every wrong answer here is a real word in the wrong place.',
)

T['de'] = dict(
    coverTitle='Lego-Autobau <em>Teil I</em>',
    coverSub='Die Wörter, die Ingenieure wirklich benutzen — und warum das Fast-Synonym immer falsch ist',
    chipLevel='B2 · Obere Mittelstufe', chipFocus='Vokabular für Konstruktion und Technik',
    chipCount='17 Folien',

    deEyebrow='Vor den Fragen', deTitle='Wörter für das Ding vor dem Ding',
    de1h='<em>Prototype</em> und <em>blueprint</em>', de1b=
        'Ein <strong>blueprint</strong> ist der Plan auf Papier. Ein '
        '<strong>prototype</strong> ist das erste tatsächlich gebaute Exemplar, gemacht '
        'zum Testen und zum Wegwerfen. Das eine ist eine Zeichnung, das andere ein '
        'Gegenstand.',
    de1n='Man zeichnet einen blueprint und baut einen prototype. Die Verben tauschen nicht.',
    de2h='<em>Modular</em> und <em>iterative</em>', de2b=
        '<strong>Modular</strong> beschreibt die Sache: aus in sich geschlossenen '
        'Abschnitten gebaut, die man einzeln ersetzen kann. <strong>Iterative</strong> '
        'beschreibt den Prozess: bauen, testen, ändern, wieder bauen.',
    de2n='Ein modularer Entwurf macht einen iterativen Prozess billig. Dasselbe ist es nicht.',
    de3h='<em>Load-bearing</em> und <em>tolerance</em>', de3b=
        'Ein <strong>load-bearing</strong> Teil trägt Last, auf die der Rest angewiesen '
        'ist. <strong>Tolerance</strong> ist, wie viel Abweichung eine Passung erlaubt, '
        'bevor sie nicht mehr funktioniert.',
    de3n='Beides kommt aus der Technik und wird im Alltagsenglisch auf B2 unverändert benutzt.',

    pvEyebrow='Das Register', pvTitle='Hier sind die Phrasal Verbs die Fachsprache',
    pv1h='Bevor du anfängst', pv1b=
        'Die Teile <strong>lay out</strong> &mdash; so ausbreiten, dass du sie siehst. '
        'Das Diagramm mit der Teileliste <strong>cross-reference</strong> &mdash; eins '
        'gegen das andere prüfen. Beides ist Vorbereitung, und beides ist trennbar.',
    pv1n='<em>Lay them out</em>, <em>cross-reference it against</em> — das Objekt darf dazwischen.',
    pv2h='Während du baust', pv2b=
        'Teile <strong>snap into</strong> place. Wenn eines das nicht tut, '
        '<strong>troubleshoot</strong>est du das Problem &mdash; der Reihe nach, bis du '
        'die Ursache hast.',
    pv2n='<em>Troubleshoot</em> ist ein Wort und nimmt ein direktes Objekt. Nicht <em>troubleshoot for</em>.',
    pv3h='Am Ende', pv3b=
        'Du <strong>fine-tune</strong>st den Mechanismus: kleine Anpassungen an etwas, '
        'das schon funktioniert. Keine Reparatur, kein Neuentwurf &mdash; die letzten '
        'fünf Prozent.',
    pv3n='Ist es kaputt, reparierst du es. Fine-tunen kannst du nur, was fast stimmt.',

    prEyebrow='Die C1-Gewohnheit auf B2', prTitle='Der Distraktor ist das Fast-Synonym',
    pr1h='Lies, was das Wort ausschließt', pr1b=
        '<em>Align</em> geht um Position, nicht um Verbindung &mdash; kleben und '
        'verstärken sind also falsch, so plausibel sie klingen. Jedes dieser Wörter sagt '
        'eine Sache und schließt den Rest aus.',
    pr1n='Frag, was das Wort <em>nicht</em> heißt. Das geht meist schneller.',
    pr2h='<em>Orientation</em> ist Richtung, nicht Ort', pr2b=
        'Ein Balken in der falschen <strong>orientation</strong> liegt an der richtigen '
        'Stelle und zeigt in die falsche Richtung. Falsche Länge, falsche Farbe und '
        'nicht befestigt sind drei andere Fehler mit drei anderen Namen.',
    pr2n='Position, Orientierung, Maß, Farbe — vier Eigenschaften, vier Wörter.',
    pr3h='In <em>retrofit</em> steckt eine Zeitangabe', pr3b=
        '<strong>Retrofit</strong> heißt, etwas hinzuzufügen, <em>nachdem</em> die Sache '
        'fertig war. Neu bauen, so lassen oder ein Merkmal entfernen sind alles andere '
        'Handlungen.',
    pr3n='Das Wort trägt eine Reihenfolge in sich. Das macht es präzise.',

    mcEyebrow='Aufgabe 1 · Multiple Choice', mcTitle='Was heißt der Begriff wirklich?',
    q1why='<strong>To position something so it lines up correctly.</strong> <em>Align</em> '
          'geht um relative Position und um sonst nichts — nicht verbinden, nicht '
          'verstärken, nicht neu bauen.',
    q2why='<strong>It compensates for the difference in wheel speed during turns.</strong> '
          'In der Kurve legt das äußere Rad einen längeren Weg zurück, muss sich also '
          'schneller drehen. Das Differential lässt das zu.',
    q3why='<strong>She had placed the piece facing the wrong direction or angle.</strong> '
          '<em>Orientation</em> ist, wie herum etwas zeigt. Falsche Farbe, falsche Länge '
          'und nicht befestigt sind drei andere Fehler.',
    q4why='<strong>The model was robust and held together even under physical stress.</strong> '
          '<em>Structural integrity</em> heißt: unter Last ganz bleiben. Über Gewicht, '
          'Detailtreue oder Zerlegbarkeit sagt es nichts.',
    q5why='<strong>To add a new feature to something that was already completed.</strong> '
          'Das <em>retro-</em> tut die Arbeit: Die Ergänzung kommt nach dem fertigen Bau, '
          'nicht währenddessen und nicht statt seiner.',

    bankLabel='Wortspeicher:',
    fibEyebrow='Aufgabe 2 · Das Konstruktionsvokabular', fibTitle='In jede Lücke passt ein Wort',
    fibHint='Acht Wörter im Speicher, fünf Lücken. Die drei übrigen sind die Fast-Treffer.',
    g1why='<strong>Prototype.</strong> Das erste funktionierende Modell, gebaut, um eine '
          'Idee zu prüfen, bevor irgendetwas in Produktion geht. Der blueprint wäre die '
          'Zeichnung.',
    g2why='<strong>Modular.</strong> In sich geschlossene Abschnitte, jeder einzeln baubar '
          'und ersetzbar. Beschreibt den Entwurf, nicht den Weg dorthin.',
    g3why='<strong>Blueprint.</strong> Der technische Plan, nach dem gebaut wird. Sie prüft '
          'ein Dokument, keinen Gegenstand.',
    g4why='<strong>Load-bearing.</strong> Ein Teil, das Last trägt, auf die der Rest der '
          'Konstruktion angewiesen ist. Nimm es weg, und alles darüber fällt.',
    g5why='<strong>Iterative.</strong> Wiederholte Zyklen aus Test und Verfeinerung, jeder '
          'besser als der vorige. Beschreibt den Prozess, nicht das Produkt.',

    dndEyebrow='Aufgabe 3 · Die Phrasal Verbs', dndTitle='Vervollständige die Anweisung',
    dndHint='Sieben Wendungen im Speicher, fünf Lücken. Zwei gehören in keine davon.',
    d1why='<strong>Lay out.</strong> Alles so ausbreiten, dass du es siehst, bevor du '
          'anfängst. Der Vorbereitungsschritt, und trennbar: <em>lay them out</em>.',
    d2why='<strong>Troubleshoot.</strong> Ein Problem der Reihe nach durchgehen, bis die '
          'Ursache dasteht. Ein Wort, mit direktem Objekt.',
    d3why='<strong>Snap into.</strong> Das Klicken eines Teils, das fest an seiner Stelle '
          'sitzt — und der Grund, warum Lego überhaupt funktioniert.',
    d4why='<strong>Cross-reference.</strong> Eine Quelle gegen eine andere prüfen. Das '
          'Diagramm gegen die Teileliste, und keines allein.',
    d5why='<strong>Fine-tune.</strong> Kleine, genaue Anpassungen an etwas, das schon '
          'läuft. Die letzten fünf Prozent, nicht die Reparatur.',

    actTitle='Sprich den Bau durch', actUse='Benutze mindestens vier:',
    actSpeakBrief='Einer hat es entworfen, die andere muss es allein nach deiner '
                  'Beschreibung bauen. Je vier Minuten, dann tauschen.',
    actSpeak1='Beschreibe, wie du einen komplexen Bau vorbereiten würdest, bevor du ein einziges Teil anfasst.',
    actSpeak2='Erklär einen Mechanismus, den du verstehst — Zahnräder, Scharniere, Federung —, jemandem, der ihn nicht kennt.',
    actSpeak3='Etwas an deinem Bau passt nicht. Führ deinen Partner durch das Troubleshooting.',
    actSpeak4='Beschreibe einen Entwurf, den du modular nennen würdest, und sag, was dir das bringt.',
    actWriteKind='Schreiben · 150–180 Wörter',
    actWriteBrief='Schreibe die Entwurfsnotiz zu einem Prototyp. Sag, was der Blueprint '
                  'vorgab, welche Teile tragend sind, wo die Toleranzen eng sind und was '
                  'die nächste Iteration ändern wird. Schreib für eine Ingenieurin, nicht '
                  'für einen Kunden.',
    actPlaceholder='The first prototype was laid out from the blueprint on…',

    resPerfect='Volle Punktzahl. Du wählst nach dem, was das Wort ausschließt — genau darum geht es auf B2.',
    resStrong='Stark. Sieh dir die Phrasal Verbs noch einmal an; dort fehlt hier meist der letzte Punkt.',
    resMid='Gute Grundlage. Zurück zur ersten Folie: blueprint und prototype sind eine Zeichnung und ein Gegenstand.',
    resLow='Lies die drei Einstiegsfolien noch einmal. Jede falsche Antwort hier ist ein echtes Wort an der falschen Stelle.',
)

T['es'] = dict(
    coverTitle='Construir coches de Lego <em>Parte I</em>',
    coverSub='Las palabras que usan de verdad los ingenieros y por qué el casi sinónimo siempre falla',
    chipLevel='B2 · Intermedio alto', chipFocus='Vocabulario de diseño e ingeniería',
    chipCount='17 diapositivas',

    deEyebrow='Antes de las preguntas', deTitle='Palabras para la cosa antes de la cosa',
    de1h='<em>Prototype</em> y <em>blueprint</em>', de1b=
        'Un <strong>blueprint</strong> es el plano sobre papel. Un '
        '<strong>prototype</strong> es el primero que construyes de verdad, hecho para '
        'probarlo y tirarlo. Uno es un dibujo; el otro, un objeto.',
    de1n='Se dibuja un blueprint y se construye un prototype. Los verbos no se intercambian.',
    de2h='<em>Modular</em> e <em>iterative</em>', de2b=
        '<strong>Modular</strong> describe la cosa: hecha de secciones autónomas que se '
        'pueden sustituir de una en una. <strong>Iterative</strong> describe el proceso: '
        'construir, probar, cambiar, volver a construir.',
    de2n='Un diseño modular abarata un proceso iterativo. No son la misma idea.',
    de3h='<em>Load-bearing</em> y <em>tolerance</em>', de3b=
        'Una pieza <strong>load-bearing</strong> sostiene el peso del que depende el '
        'resto. <strong>Tolerance</strong> es cuánto error admite un ajuste antes de '
        'dejar de funcionar.',
    de3n='Ambas vienen de la ingeniería real y se usan igual en el inglés corriente de B2.',

    pvEyebrow='El registro', pvTitle='Aquí los phrasal verbs son el lenguaje técnico',
    pv1h='Antes de empezar', pv1b=
        '<strong>Lay out</strong> las piezas: extiéndelas donde puedas verlas. '
        '<strong>Cross-reference</strong> el diagrama con la lista: comprueba uno contra '
        'la otra. Los dos son preparación y los dos son separables.',
    pv1n='<em>Lay them out</em>, <em>cross-reference it against</em>: el objeto puede ir en medio.',
    pv2h='Mientras construyes', pv2b=
        'Las piezas <strong>snap into</strong> place. Cuando una no lo hace, '
        '<strong>troubleshoot</strong>eas el problema: lo recorres en orden hasta dar con '
        'la causa.',
    pv2n='<em>Troubleshoot</em> es una sola palabra y lleva objeto directo. No <em>troubleshoot for</em>.',
    pv3h='Al final', pv3b=
        '<strong>Fine-tune</strong> el mecanismo: ajustes pequeños a algo que ya funciona. '
        'Ni reparación ni rediseño: el último cinco por ciento.',
    pv3n='Si está roto, lo arreglas. Solo se puede afinar lo que ya está cerca.',

    prEyebrow='La costumbre de C1 en B2', prTitle='El distractor es el casi sinónimo',
    pr1h='Lee lo que la palabra descarta', pr1b=
        '<em>Align</em> va de posición, no de unión, así que pegar y reforzar están mal '
        'por muy sensatos que suenen. Cada una de estas palabras dice una cosa y excluye '
        'el resto.',
    pr1n='Pregunta qué <em>no</em> significa la palabra. Suele ser más rápido.',
    pr2h='<em>Orientation</em> es dirección, no lugar', pr2b=
        'Una viga con la <strong>orientation</strong> equivocada está en el sitio correcto '
        'y mirando al lado equivocado. Longitud, color y falta de fijación son tres '
        'errores distintos con tres nombres distintos.',
    pr2n='Posición, orientación, medida, color: cuatro propiedades, cuatro palabras.',
    pr3h='<em>Retrofit</em> lleva el tiempo dentro', pr3b=
        '<strong>Retrofit</strong> es añadir algo <em>después</em> de terminado. '
        'Reconstruirlo, dejarlo igual o quitarle una función son acciones distintas.',
    pr3n='La palabra lleva una secuencia dentro. Eso es lo que la hace precisa.',

    mcEyebrow='Actividad 1 · Opción múltiple', mcTitle='¿Qué significa de verdad el término?',
    q1why='<strong>To position something so it lines up correctly.</strong> <em>Align</em> '
          'va de posición relativa y de nada más: ni unir, ni reforzar, ni reconstruir.',
    q2why='<strong>It compensates for the difference in wheel speed during turns.</strong> '
          'En una curva la rueda exterior recorre más distancia, así que gira más rápido. '
          'El diferencial se lo permite.',
    q3why='<strong>She had placed the piece facing the wrong direction or angle.</strong> '
          '<em>Orientation</em> es hacia dónde mira algo. Color, longitud y falta de '
          'fijación son otros tres errores.',
    q4why='<strong>The model was robust and held together even under physical stress.</strong> '
          '<em>Structural integrity</em> es mantenerse entero bajo carga. No dice nada del '
          'peso, del detalle ni de lo fácil que sea desmontarlo.',
    q5why='<strong>To add a new feature to something that was already completed.</strong> '
          'El <em>retro-</em> hace el trabajo: la incorporación llega después de terminada '
          'la construcción.',

    bankLabel='Banco de palabras:',
    fibEyebrow='Actividad 2 · El vocabulario de diseño', fibTitle='Una palabra por hueco',
    fibHint='Ocho palabras en el banco, cinco huecos. Las tres sobrantes son los casi aciertos.',
    g1why='<strong>Prototype.</strong> El primer modelo funcional, construido para probar '
          'una idea antes de producir nada. El blueprint sería el dibujo.',
    g2why='<strong>Modular.</strong> Secciones autónomas, cada una construible y '
          'sustituible por separado. Describe el diseño, no cómo se llegó a él.',
    g3why='<strong>Blueprint.</strong> El plano técnico según el que se construye. Ella '
          'está comprobando un documento, no un objeto.',
    g4why='<strong>Load-bearing.</strong> Una pieza que soporta el peso del que depende el '
          'resto de la estructura. Quítala y se viene abajo todo lo de arriba.',
    g5why='<strong>Iterative.</strong> Ciclos repetidos de prueba y refinamiento, cada uno '
          'mejor que el anterior. Describe el proceso, no el producto.',

    dndEyebrow='Actividad 3 · Los phrasal verbs', dndTitle='Completa la instrucción',
    dndHint='Siete expresiones en el banco, cinco huecos. Dos no encajan en ninguno.',
    d1why='<strong>Lay out.</strong> Extenderlo todo donde puedas verlo, antes de empezar. '
          'Es el paso de preparación, y es separable: <em>lay them out</em>.',
    d2why='<strong>Troubleshoot.</strong> Recorrer un problema en orden hasta dar con la '
          'causa. Una palabra, y lleva objeto directo.',
    d3why='<strong>Snap into.</strong> El clic de una pieza que se asienta firme en su '
          'sitio, y la razón por la que Lego funciona.',
    d4why='<strong>Cross-reference.</strong> Comprobar una fuente contra otra: el diagrama '
          'contra la lista de piezas, y ninguno por su cuenta.',
    d5why='<strong>Fine-tune.</strong> Ajustes pequeños y precisos a algo que ya funciona. '
          'El último cinco por ciento, no la reparación.',

    actTitle='Repasa la construcción en voz alta', actUse='Usa al menos cuatro:',
    actSpeakBrief='Uno lo diseñó y el otro tiene que construirlo solo con tu descripción. '
                  'Cuatro minutos cada uno, luego cambiad.',
    actSpeak1='Describe cómo prepararías una construcción compleja antes de tocar una sola pieza.',
    actSpeak2='Explica un mecanismo que entiendas — engranajes, bisagras, suspensión — a alguien que no.',
    actSpeak3='Algo de tu construcción no encaja. Guía a tu compañero por el proceso para localizarlo.',
    actSpeak4='Describe un diseño que llamarías modular y di qué te aporta eso.',
    actWriteKind='Escritura · 150–180 palabras',
    actWriteBrief='Escribe la nota de diseño que acompaña a un prototipo. Di qué '
                  'especificaba el plano, qué piezas son portantes, dónde son estrechas '
                  'las tolerancias y qué cambiará la siguiente iteración. Escríbelo para '
                  'un ingeniero, no para un cliente.',
    actPlaceholder='The first prototype was laid out from the blueprint on…',

    resPerfect='Puntuación perfecta. Eliges por lo que la palabra descarta, que es todo el salto de B2.',
    resStrong='Muy bien. Repasa los phrasal verbs: ahí suele quedarse el último punto.',
    resMid='Buena base. Vuelve a la primera diapositiva: blueprint y prototype son un dibujo y un objeto.',
    resLow='Relee las tres diapositivas iniciales. Cada respuesta incorrecta es una palabra real en el sitio equivocado.',
)


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    rows = ['    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
            for k in sorted(d)]
    rows += ['    %s: %s' % (k, TAIL[code][k]) for k in sorted(TAIL[code])]
    return '{\n' + ',\n'.join(rows) + '\n  }'


if __name__ == '__main__':
    base = set(T['en'])
    for c, d in T.items():
        m, x = base - set(d), set(d) - base
        print('%-3s %2d' % (c, len(d)), ('MISSING %s' % sorted(m)) if m else '',
              ('EXTRA %s' % sorted(x)) if x else '')
