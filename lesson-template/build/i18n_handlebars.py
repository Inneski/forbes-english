# -*- coding: utf-8 -*-
"""Interface strings for Beyond the Handlebars (B2/C1) — EN, DE, ES.

House-style rule 8: the target language stays in English. Every stem, option,
gap sentence, collocation and explanation is the thing under test, so none of
it translates. What German and Spanish cover is the chrome — the cover, the
eyebrows, the section titles, the hints, the role-play briefs, the discussion
prompts and the activation stage.

Spanish is not optional here. `assemble()` still defaults to ('en', 'de') and
three decks went out EN+DE before anyone noticed; the builder passes
langs=('en', 'de', 'es') explicitly and this module carries all three.

ledDp/ledTime/ledClues come from CHROME rather than being declared here: the
template's deck bar carries a hidden RPG ledger whose three labels are
data-i18n, and a deck built from the current template fails the checker's
"data-i18n with no English key" rule unless they resolve.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'actEyebrow', 'actSpeakKind',
        'btnCopy', 'btnCopied', 'wordCount', 'ledDp', 'ledTime',
        'ledClues', 'actSpeakWord', 'actWriteWord']

T = {}

T['en'] = dict(
    coverTitle='Beyond the <em>handlebars</em>',
    coverSub='The parts of a bicycle, the words that ride with them, and the conversations they start',
    chipLevel='B2 / C1 &middot; Vocabulary',
    chipFocus='Precision &amp; inference',
    chipCount='COUNT slides',

    bankLabel='Word bank:',

    fitSaddle='Saddle &amp; seatpost',
    fitSaddleN='Adjust the seatpost, not the saddle, for height.',
    fitTubes='Top tube, down tube, seat tube',
    fitTubesN='Together they are the frame &mdash; never &ldquo;the body&rdquo;.',
    ctlBars='Drop handlebars',
    ctlBarsN='&ldquo;She moved her hands onto the drops.&rdquo;',
    ctlStem='Stem &amp; fork',
    ctlStemN='The stem sets how far forward you reach.',
    drvFront='At the front',
    drvFrontN='Pedals clip to the end of each crank arm.',
    drvRear='At the back',
    drvRearN='Chainrings at the front, cassette at the back.',

    preCad='Cadence',
    preCadN='Maintain a steady cadence.',
    preTrac='Traction',
    preTracN='The rear tyre lost traction on the gravel.',
    preRim='Rim vs hub',
    preRimN='The spokes connect the rim to the hub.',

    colMaintain='maintain a steady cadence',
    colMaintainN='Also: maintain a pace, maintain your line.',
    colShift='shift <strong>into</strong> a lower gear',
    colShiftN='Also: change into a lower gear.',
    colLose='lose traction',
    colLoseN='Also: lose grip, lose the back wheel.',
    colInto='ride <strong>into</strong> a headwind',
    colIntoN='Also: ride into a crosswind, ride with a tailwind.',

    idBack='backpedal',
    idBackN='The spokesperson began to backpedal under questioning.',
    idUphill='an uphill struggle',
    idUphillN='Changing the policy was an uphill struggle.',
    idGear='get into gear',
    idGearN='We have talked for weeks &mdash; it is time to get into gear.',

    ridersEyebrow='Break the ice',
    ridersTitle='What kind of cyclist are you?',
    ridersHint='Click a rider. Read what the riding involves, then answer the question underneath.',
    ridersAsk='Talk about it',

    fitEyebrow='The bike, decoded',
    fitTitle='Where you sit, and what holds you',
    controlEyebrow='The bike, decoded',
    controlTitle='What you steer with',
    driveEyebrow='The bike, decoded',
    driveTitle='Where the power goes',

    mapOneEyebrow='The bike, decoded',
    mapOneTitle='Frame, fit and control',
    mapTwoEyebrow='The bike, decoded',
    mapTwoTitle='Wheels, braking and drivetrain',
    mapHint='Click a number. Say what the part does, then use it in a sentence of your own.',
    mapPick='Choose a component',
    mapNote='Teaching schematic &middot; not a specified production model.',

    preEyebrow='Make it precise',
    preTitle='Three that get confused',
    vocabEyebrow='Make it precise',
    vocabTitle='Not just &ldquo;that bit&rdquo;',

    collTeachEyebrow='Sound like a rider',
    collTeachTitle='Words that ride together',
    collEyebrow='Natural combinations',
    collTitle='Which word does English put here?',

    readOneEyebrow='Read between the lines',
    readOneTitle='Buying speed',
    readTwoEyebrow='Read between the lines',
    readTwoTitle='Finding perspective',
    readAskOne='Pause and predict: what might Maya change next? What does the highlighted phrase suggest?',
    readAskTwo='Find the sentence that balances the writer&rsquo;s argument. Why is it there?',

    inferEyebrow='Meaning beneath the words',
    inferTitle='What is the writer really saying?',

    shopEyebrow='Role play',
    shopTitle='&ldquo;It only happens on hills&rdquo;',
    shopHint='Take a role each. Run it twice, then swap and try a rubbing brake instead.',
    shopRiderRole='A &middot; The rider',
    shopRiderBrief='Your chain slips when you press hard on the pedals. It started two rides ago.',
    shopRiderTask='Describe when it happens. Ask for an estimate. Agree a spending limit.',
    shopMechRole='B &middot; The mechanic',
    shopMechBrief='You need to inspect the bike before you can identify the cause.',
    shopMechTask='Clarify the symptoms. Explain what you cannot yet know. Agree to call before extra work.',
    shopBorrow='Borrow a phrase',
    shopModel='Show a model dialogue',
    shopModelHide='Hide the dialogue',

    idiomTeachEyebrow='When cycling becomes a metaphor',
    idiomTeachTitle='Take the language further',
    idiomEyebrow='Off the bike',
    idiomTitle='One idiom per space',
    idiomHint='Three idioms, three sentences, each used once. Case does not matter.',

    tradeEyebrow='Would you rather&hellip;?',
    tradeTitle='There is always a trade-off',
    tradeHint='State a preference, concede a drawback, then say what would change your mind.',
    tradeNext='Another dilemma &rarr;',
    tradeCount='Dilemma',

    debateEyebrow='Debate and negotiate',
    debateTitle='Who is the city for?',
    debateMotion='Replace town-centre parking with a protected cycle lane.',
    debateTask='Agree one recommendation and two conditions.',
    debateRoleA='The commuter',
    debateBriefA='You need a continuous route and junctions you can trust.',
    debateRoleB='The shop owner',
    debateBriefB='You need deliveries to arrive and customers to reach the door.',
    debateRoleC='The access advocate',
    debateBriefC='You speak for crossings, bus stops and disabled residents.',
    debateStart='Start',
    debateReset='Reset',
    debateTimer='90-second final pitch',

    resNext='You can name the parts and question the claims. Now use both &rarr;',

    actTitle='Your next conversation starts here',
    actUse='Use these',
    actWriteKind='Writing',
    actSpeakBrief='Without looking back at the deck, work through all three in pairs.',
    actSpeak1='Name three components and say what each one does.',
    actSpeak2='Describe a fault using two natural combinations.',
    actSpeak3='Qualify one claim about the cause &mdash; what makes you think that?',
    actWriteBrief='Write 150&ndash;180 words: is premium equipment worth it? Use four target expressions, one concession and one conditional sentence.',
    actPlaceholder='It depends on what the rider is actually trying to fix…',
)

T['de'] = dict(
    coverTitle='Jenseits des <em>Lenkers</em>',
    coverSub='Die Teile eines Fahrrads, die Wörter, die dazugehören, und die Gespräche, die daraus entstehen',
    chipLevel='B2 / C1 &middot; Wortschatz',
    chipFocus='Präzision &amp; Schlussfolgern',
    chipCount='COUNT Folien',

    bankLabel='Wortspeicher:',

    fitSaddle='Sattel &amp; Sattelstütze',
    fitSaddleN='Die Höhe stellst du über die Sattelstütze ein, nicht über den Sattel.',
    fitTubes='Oberrohr, Unterrohr, Sitzrohr',
    fitTubesN='Zusammen sind sie der Rahmen &mdash; nie &bdquo;der Körper&ldquo;.',
    ctlBars='Rennlenker',
    ctlBarsN='&bdquo;Sie griff in den Unterlenker.&ldquo;',
    ctlStem='Vorbau &amp; Gabel',
    ctlStemN='Der Vorbau bestimmt, wie weit du nach vorn greifst.',
    drvFront='Vorn',
    drvFrontN='Die Pedale werden an das Ende der Kurbel geschraubt.',
    drvRear='Hinten',
    drvRearN='Kettenblätter vorn, Kassette hinten.',

    preCad='Cadence (Trittfrequenz)',
    preCadN='Maintain a steady cadence.',
    preTrac='Traction (Grip)',
    preTracN='The rear tyre lost traction on the gravel.',
    preRim='Rim und hub (Felge und Nabe)',
    preRimN='The spokes connect the rim to the hub.',

    colMaintain='maintain a steady cadence',
    colMaintainN='Auch: maintain a pace, maintain your line.',
    colShift='shift <strong>into</strong> a lower gear',
    colShiftN='Auch: change into a lower gear.',
    colLose='lose traction',
    colLoseN='Auch: lose grip, lose the back wheel.',
    colInto='ride <strong>into</strong> a headwind',
    colIntoN='Auch: ride into a crosswind, ride with a tailwind.',

    idBack='backpedal',
    idBackN='Einen Rückzieher machen: The spokesperson began to backpedal.',
    idUphill='an uphill struggle',
    idUphillN='Ein zähes Unterfangen: Changing the policy was an uphill struggle.',
    idGear='get into gear',
    idGearN='In die Gänge kommen: It is time to get into gear.',

    ridersEyebrow='Zum Einstieg',
    ridersTitle='Was für ein Radfahrer bist du?',
    ridersHint='Klicke auf einen Typ. Lies, was diese Art zu fahren ausmacht, und beantworte dann die Frage darunter.',
    ridersAsk='Sprecht darüber',

    fitEyebrow='Das Rad, erklärt',
    fitTitle='Wo du sitzt und was dich trägt',
    controlEyebrow='Das Rad, erklärt',
    controlTitle='Womit du lenkst',
    driveEyebrow='Das Rad, erklärt',
    driveTitle='Wohin die Kraft geht',

    mapOneEyebrow='Das Rad, erklärt',
    mapOneTitle='Rahmen, Sitzposition und Steuerung',
    mapTwoEyebrow='Das Rad, erklärt',
    mapTwoTitle='Laufräder, Bremsen und Antrieb',
    mapHint='Klicke auf eine Zahl. Sag, was das Teil tut, und verwende es dann in einem eigenen Satz.',
    mapPick='Bauteil auswählen',
    mapNote='Lehrskizze &middot; kein bestimmtes Serienmodell.',

    preEyebrow='Genau werden',
    preTitle='Drei, die verwechselt werden',
    vocabEyebrow='Genau werden',
    vocabTitle='Nicht einfach &bdquo;das Ding da&ldquo;',

    collTeachEyebrow='Klingen wie ein Radfahrer',
    collTeachTitle='Wörter, die zusammen fahren',
    collEyebrow='Feste Verbindungen',
    collTitle='Welches Wort setzt das Englische hier ein?',

    readOneEyebrow='Zwischen den Zeilen lesen',
    readOneTitle='Geschwindigkeit kaufen',
    readTwoEyebrow='Zwischen den Zeilen lesen',
    readTwoTitle='Den Blick zurechtrücken',
    readAskOne='Kurz innehalten: Was könnte Maya als Nächstes ändern? Was sagt die hervorgehobene Wendung aus?',
    readAskTwo='Finde den Satz, der das Argument der Autorin ausbalanciert. Warum steht er da?',

    inferEyebrow='Was zwischen den Worten steht',
    inferTitle='Was sagt die Autorin eigentlich?',

    shopEyebrow='Rollenspiel',
    shopTitle='&bdquo;Nur an Steigungen&ldquo;',
    shopHint='Übernehmt je eine Rolle. Spielt es zweimal durch, tauscht dann und nehmt eine schleifende Bremse.',
    shopRiderRole='A &middot; Der Radfahrer',
    shopRiderBrief='Deine Kette rutscht, wenn du kräftig in die Pedale trittst. Es begann vor zwei Ausfahrten.',
    shopRiderTask='Beschreibe, wann es passiert. Frag nach einem Kostenvoranschlag. Vereinbare eine Obergrenze.',
    shopMechRole='B &middot; Der Mechaniker',
    shopMechBrief='Du musst das Rad prüfen, bevor du die Ursache benennen kannst.',
    shopMechTask='Kläre die Symptome. Erkläre, was du noch nicht wissen kannst. Sag zu, vor Mehrarbeit anzurufen.',
    shopBorrow='Nimm dir eine Wendung',
    shopModel='Musterdialog zeigen',
    shopModelHide='Dialog ausblenden',

    idiomTeachEyebrow='Wenn Radfahren zur Metapher wird',
    idiomTeachTitle='Die Sprache weiterdenken',
    idiomEyebrow='Abseits des Rads',
    idiomTitle='Eine Redewendung pro Lücke',
    idiomHint='Drei Redewendungen, drei Sätze, jede genau einmal. Groß- und Kleinschreibung spielt keine Rolle.',

    tradeEyebrow='Was wäre dir lieber?',
    tradeTitle='Es gibt immer einen Zielkonflikt',
    tradeHint='Nenne eine Präferenz, räume einen Nachteil ein und sag, was deine Meinung ändern würde.',
    tradeNext='Nächstes Dilemma &rarr;',
    tradeCount='Dilemma',

    debateEyebrow='Debattieren und verhandeln',
    debateTitle='Für wen ist die Stadt da?',
    debateMotion='Parkplätze in der Innenstadt durch einen geschützten Radweg ersetzen.',
    debateTask='Einigt euch auf eine Empfehlung und zwei Bedingungen.',
    debateRoleA='Der Pendler',
    debateBriefA='Du brauchst eine durchgehende Route und Kreuzungen, denen du trauen kannst.',
    debateRoleB='Die Ladeninhaberin',
    debateBriefB='Lieferungen müssen ankommen und Kundschaft muss bis zur Tür kommen.',
    debateRoleC='Die Interessenvertretung',
    debateBriefC='Du sprichst für Überwege, Bushaltestellen und Menschen mit Behinderung.',
    debateStart='Start',
    debateReset='Zurücksetzen',
    debateTimer='90 Sekunden Schlussplädoyer',

    resNext='Du kannst die Teile benennen und Behauptungen hinterfragen. Jetzt beides anwenden &rarr;',

    actTitle='Hier beginnt dein nächstes Gespräch',
    actUse='Verwende diese',
    actWriteKind='Schreiben',
    actSpeakBrief='Ohne zurückzublättern: Arbeitet alle drei Punkte zu zweit durch.',
    actSpeak1='Nenne drei Bauteile und sag, was jedes davon tut.',
    actSpeak2='Beschreibe einen Defekt mit zwei festen Verbindungen.',
    actSpeak3='Schränke eine Aussage zur Ursache ein &mdash; woran machst du das fest?',
    actWriteBrief='Schreibe 150&ndash;180 Wörter: Lohnt sich hochwertige Ausrüstung? Verwende vier Zielausdrücke, ein Zugeständnis und einen Konditionalsatz.',
    actPlaceholder='Es kommt darauf an, was der Fahrer eigentlich beheben will…',
)

T['es'] = dict(
    coverTitle='Más allá del <em>manillar</em>',
    coverSub='Las piezas de una bicicleta, las palabras que las acompañan y las conversaciones que provocan',
    chipLevel='B2 / C1 &middot; Vocabulario',
    chipFocus='Precisión e inferencia',
    chipCount='COUNT diapositivas',

    bankLabel='Banco de palabras:',

    fitSaddle='Sillín y tija',
    fitSaddleN='La altura se ajusta con la tija, no con el sillín.',
    fitTubes='Tubo superior, tubo diagonal, tubo del sillín',
    fitTubesN='Juntos son el cuadro &mdash; nunca &laquo;el cuerpo&raquo;.',
    ctlBars='Manillar de carretera',
    ctlBarsN='&laquo;Bajó las manos a la parte curva.&raquo;',
    ctlStem='Potencia y horquilla',
    ctlStemN='La potencia decide cuánto tienes que estirarte.',
    drvFront='Delante',
    drvFrontN='Los pedales se enroscan al extremo de cada biela.',
    drvRear='Detrás',
    drvRearN='Platos delante, casete detrás.',

    preCad='Cadence (cadencia)',
    preCadN='Maintain a steady cadence.',
    preTrac='Traction (agarre)',
    preTracN='The rear tyre lost traction on the gravel.',
    preRim='Rim y hub (llanta y buje)',
    preRimN='The spokes connect the rim to the hub.',

    colMaintain='maintain a steady cadence',
    colMaintainN='También: maintain a pace, maintain your line.',
    colShift='shift <strong>into</strong> a lower gear',
    colShiftN='También: change into a lower gear.',
    colLose='lose traction',
    colLoseN='También: lose grip, lose the back wheel.',
    colInto='ride <strong>into</strong> a headwind',
    colIntoN='También: ride into a crosswind, ride with a tailwind.',

    idBack='backpedal',
    idBackN='Desdecirse: The spokesperson began to backpedal.',
    idUphill='an uphill struggle',
    idUphillN='Una tarea cuesta arriba: Changing the policy was an uphill struggle.',
    idGear='get into gear',
    idGearN='Ponerse en marcha: It is time to get into gear.',

    ridersEyebrow='Para romper el hielo',
    ridersTitle='¿Qué tipo de ciclista eres?',
    ridersHint='Haz clic en un perfil. Lee en qué consiste esa forma de rodar y responde a la pregunta de abajo.',
    ridersAsk='Hablad de ello',

    fitEyebrow='La bicicleta, por dentro',
    fitTitle='Dónde te sientas y qué te sostiene',
    controlEyebrow='La bicicleta, por dentro',
    controlTitle='Con qué diriges',
    driveEyebrow='La bicicleta, por dentro',
    driveTitle='Adónde va la fuerza',

    mapOneEyebrow='La bicicleta, por dentro',
    mapOneTitle='Cuadro, postura y dirección',
    mapTwoEyebrow='La bicicleta, por dentro',
    mapTwoTitle='Ruedas, frenos y transmisión',
    mapHint='Haz clic en un número. Di qué hace la pieza y úsala luego en una frase propia.',
    mapPick='Elige un componente',
    mapNote='Esquema didáctico &middot; no es un modelo de producción concreto.',

    preEyebrow='Hazlo preciso',
    preTitle='Tres que se confunden',
    vocabEyebrow='Hazlo preciso',
    vocabTitle='No solo &laquo;esa pieza de ahí&raquo;',

    collTeachEyebrow='Habla como un ciclista',
    collTeachTitle='Palabras que ruedan juntas',
    collEyebrow='Combinaciones naturales',
    collTitle='¿Qué palabra pone aquí el inglés?',

    readOneEyebrow='Leer entre líneas',
    readOneTitle='Comprar velocidad',
    readTwoEyebrow='Leer entre líneas',
    readTwoTitle='Recuperar la perspectiva',
    readAskOne='Haz una pausa: ¿qué podría cambiar Maya después? ¿Qué sugiere la expresión resaltada?',
    readAskTwo='Busca la frase que equilibra el argumento de la autora. ¿Por qué está ahí?',

    inferEyebrow='El sentido bajo las palabras',
    inferTitle='¿Qué está diciendo realmente la autora?',

    shopEyebrow='Juego de rol',
    shopTitle='&laquo;Solo pasa en las cuestas&raquo;',
    shopHint='Tomad un papel cada uno. Hacedlo dos veces, luego cambiad y probad con un freno que roza.',
    shopRiderRole='A &middot; El ciclista',
    shopRiderBrief='La cadena patina cuando aprietas fuerte los pedales. Empezó hace dos salidas.',
    shopRiderTask='Describe cuándo ocurre. Pide un presupuesto. Acuerda un límite de gasto.',
    shopMechRole='B &middot; El mecánico',
    shopMechBrief='Necesitas revisar la bicicleta antes de poder identificar la causa.',
    shopMechTask='Aclara los síntomas. Explica lo que aún no puedes saber. Acuerda llamar antes de hacer trabajo extra.',
    shopBorrow='Toma prestada una fórmula',
    shopModel='Ver un diálogo modelo',
    shopModelHide='Ocultar el diálogo',

    idiomTeachEyebrow='Cuando el ciclismo se vuelve metáfora',
    idiomTeachTitle='Lleva el idioma más lejos',
    idiomEyebrow='Fuera de la bici',
    idiomTitle='Una expresión por hueco',
    idiomHint='Tres expresiones, tres frases, cada una una sola vez. Las mayúsculas no importan.',

    tradeEyebrow='¿Qué preferirías?',
    tradeTitle='Siempre hay una contrapartida',
    tradeHint='Expresa una preferencia, admite un inconveniente y di qué te haría cambiar de opinión.',
    tradeNext='Otro dilema &rarr;',
    tradeCount='Dilema',

    debateEyebrow='Debatir y negociar',
    debateTitle='¿Para quién es la ciudad?',
    debateMotion='Sustituir el aparcamiento del centro por un carril bici protegido.',
    debateTask='Acordad una recomendación y dos condiciones.',
    debateRoleA='La persona que va al trabajo',
    debateBriefA='Necesitas una ruta continua y cruces en los que puedas confiar.',
    debateRoleB='El comerciante',
    debateBriefB='Necesitas que lleguen las entregas y que la clientela alcance la puerta.',
    debateRoleC='La defensora de la accesibilidad',
    debateBriefC='Hablas por los pasos de peatones, las paradas de autobús y las personas con discapacidad.',
    debateStart='Empezar',
    debateReset='Reiniciar',
    debateTimer='Alegato final de 90 segundos',

    resNext='Sabes nombrar las piezas y cuestionar las afirmaciones. Ahora usa ambas cosas &rarr;',

    actTitle='Aquí empieza tu próxima conversación',
    actUse='Usa estas',
    actWriteKind='Escritura',
    actSpeakBrief='Sin mirar atrás, trabajad los tres puntos en parejas.',
    actSpeak1='Nombra tres componentes y di qué hace cada uno.',
    actSpeak2='Describe una avería usando dos combinaciones naturales.',
    actSpeak3='Matiza una afirmación sobre la causa: ¿en qué te basas?',
    actWriteBrief='Escribe 150&ndash;180 palabras: ¿merece la pena el equipamiento de gama alta? Usa cuatro expresiones objetivo, una concesión y una oración condicional.',
    actPlaceholder='Depende de qué esté intentando resolver realmente el ciclista…',
)


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    return '{\n' + ',\n'.join(
        '    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
        for k in sorted(d)) + '\n  }'


if __name__ == '__main__':
    base = set(T['en'])
    for c, d in T.items():
        m, x = base - set(d), set(d) - base
        print('%-3s %2d' % (c, len(d)), ('MISSING %s' % sorted(m)) if m else '',
              ('EXTRA %s' % sorted(x)) if x else '')
