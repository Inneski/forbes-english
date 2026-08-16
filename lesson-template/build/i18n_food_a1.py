# -*- coding: utf-8 -*-
"""Interface strings for Ordering Food & Drink (A1, Part 1) — en, de, es.

Part 2 shipped with German only. This one adds Spanish, on Innes's ranking
that Spanish matters more than the other candidates for his students, and
because A1 is exactly where a learner still needs the *instruction* in their
own language even though the English being taught stays in English.

What translates: eyebrows, titles, hints, card notes, the activation brief,
the results messages. What does not: the six situations and their options, the
café dialogue, the five sentences to rebuild, and the phrases on the teaching
cards. Those are the lesson. The remaining seven languages ship as empty
objects — an honest empty is better than a half-filled language that appears
in the menu and then falls back to English halfway down the slide.
"""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Ordering Food &amp; <em>Drink</em>',
    coverSub='Part one: getting a table, ordering it, and asking for the bill',
    chipLevel='A1 · Part 1 of 2', chipFocus='Café &amp; restaurant English',
    chipCount='18 slides',

    askEyebrow='Before the questions',
    askTitle='Three openings do almost all of the work',
    ask1='For one thing, for yourself. <em>Please</em> is not optional in English — without it the same words sound like an order.',
    ask2='The same request from two people or more. <em>Could</em> is a step politer than <em>can</em>, and works everywhere <em>can</em> does.',
    ask3='This is how you order. Short for <em>I would like</em>. <em>I want</em> is correct English and still sounds rude here.',

    wordEyebrow='The words themselves',
    wordTitle='Four you cannot get through a meal without',
    word1='A <em>table</em> is what you ask for at the door, the <em>menu</em> is what you read, the <em>bill</em> is what you pay. American menus say <em>check</em> for the bill.',
    word2='The waiter&rsquo;s most common question. <em>Not yet</em> is the polite way to buy yourself another minute.',
    word3='The preposition never changes: allergic <strong>to</strong>. Not <em>of</em>, not <em>at</em>. This is the one phrase on the slide worth learning perfectly.',

    qEyebrow='In the café', qTitle='What do you say?',

    gapEyebrow='A whole visit, in order', gapTitle='Complete the conversation',
    bankLabel='Word bank:',
    gapHint='One word per gap. Every word in the bank is used exactly once across the two screens.',

    ordEyebrow='Say it in the right order', ordTitle='Build the sentence',
    ordHint='Click the words in order. Click a word you have placed to take it back.',

    actTitle='Now order something', actUse='Use at least four:',
    actSpeakBrief='One waiter, one customer. Then swap over, and change the order the second time.',
    actSpeak1='Arrive at the door. Ask for a table for two, and ask to sit outside.',
    actSpeak2='Ask for the menu. The waiter asks if you are ready — you are not. Buy a minute.',
    actSpeak3='Order one thing to eat and one thing to drink. Say <em>please</em> every time.',
    actSpeak4='Tell the waiter about an allergy, then ask for the bill.',
    actWriteKind='Writing · 40–60 words',
    actWriteBrief='Write out your conversation as a dialogue. The waiter speaks first.',
    actPlaceholder='Waiter: Good afternoon! Do you have a reservation?',

    resPerfect='Full marks. You could walk into a café today and be understood.',
    resStrong='Strong. The phrases have landed — say the polite openings out loud a few times.',
    resMid='A good base. Go back to the first two slides; most of the misses start there.',
    resLow='Read the first two slides again, then run it once more. The phrases first, the questions after.',
)

T['de'] = dict(
    coverTitle='Essen &amp; <em>Trinken</em> bestellen',
    coverSub='Teil eins: einen Tisch bekommen, bestellen und die Rechnung verlangen',
    chipLevel='A1 · Teil 1 von 2', chipFocus='Englisch im Café und Restaurant',
    chipCount='18 Folien',

    askEyebrow='Vor den Aufgaben',
    askTitle='Drei Einstiege erledigen fast alles',
    ask1='Für eine Sache, für Sie selbst. <em>Please</em> ist im Englischen nicht optional — ohne dieses Wort klingen dieselben Wörter wie ein Befehl.',
    ask2='Dieselbe Bitte, wenn Sie zu zweit oder mehr sind. <em>Could</em> ist eine Stufe höflicher als <em>can</em> und funktioniert überall dort, wo <em>can</em> funktioniert.',
    ask3='So bestellt man. Kurzform von <em>I would like</em>. <em>I want</em> ist korrektes Englisch und klingt hier trotzdem unhöflich.',

    wordEyebrow='Die Wörter selbst',
    wordTitle='Vier, ohne die kein Essen auskommt',
    word1='Einen <em>table</em> erfragt man an der Tür, das <em>menu</em> liest man, die <em>bill</em> bezahlt man. Auf amerikanischen Karten heißt die Rechnung <em>check</em>.',
    word2='Die häufigste Frage des Kellners. <em>Not yet</em> ist die höfliche Art, sich noch eine Minute zu verschaffen.',
    word3='Die Präposition ändert sich nie: allergic <strong>to</strong>. Nicht <em>of</em>, nicht <em>at</em>. Diese eine Wendung lohnt es sich perfekt zu lernen.',

    qEyebrow='Im Café', qTitle='Was sagen Sie?',

    gapEyebrow='Ein ganzer Besuch, der Reihe nach', gapTitle='Vervollständigen Sie das Gespräch',
    bankLabel='Wortliste:',
    gapHint='Ein Wort pro Lücke. Jedes Wort der Liste wird auf den beiden Folien genau einmal gebraucht.',

    ordEyebrow='In der richtigen Reihenfolge', ordTitle='Bauen Sie den Satz',
    ordHint='Klicken Sie die Wörter der Reihe nach an. Ein gesetztes Wort holen Sie mit einem Klick zurück.',

    actTitle='Jetzt bestellen Sie etwas', actUse='Mindestens vier verwenden:',
    actSpeakBrief='Einer bedient, einer bestellt. Dann tauschen — und beim zweiten Mal etwas anderes bestellen.',
    actSpeak1='Sie kommen an die Tür. Fragen Sie nach einem Tisch für zwei und darum, draußen zu sitzen.',
    actSpeak2='Bitten Sie um die Karte. Der Kellner fragt, ob Sie so weit sind — sind Sie nicht. Verschaffen Sie sich eine Minute.',
    actSpeak3='Bestellen Sie eine Speise und ein Getränk. Sagen Sie jedes Mal <em>please</em>.',
    actSpeak4='Nennen Sie dem Kellner eine Allergie und bitten Sie dann um die Rechnung.',
    actWriteKind='Schreiben · 40–60 Wörter',
    actWriteBrief='Schreiben Sie Ihr Gespräch als Dialog auf. Der Kellner beginnt.',
    actPlaceholder='Waiter: Good afternoon! Do you have a reservation?',

    resPerfect='Volle Punktzahl. Sie könnten heute in ein Café gehen und würden verstanden.',
    resStrong='Stark. Die Wendungen sitzen — sprechen Sie die höflichen Einstiege ein paar Mal laut.',
    resMid='Eine gute Grundlage. Gehen Sie zu den ersten beiden Folien zurück; dort beginnen die meisten Fehler.',
    resLow='Lesen Sie die ersten beiden Folien noch einmal und starten Sie neu. Erst die Wendungen, dann die Fragen.',
)

T['es'] = dict(
    coverTitle='Pedir comida y <em>bebida</em>',
    coverSub='Primera parte: conseguir mesa, pedir y pedir la cuenta',
    chipLevel='A1 · Parte 1 de 2', chipFocus='Inglés de cafetería y restaurante',
    chipCount='18 diapositivas',

    askEyebrow='Antes de las preguntas',
    askTitle='Tres fórmulas resuelven casi todo',
    ask1='Para una cosa y para usted solo. En inglés <em>please</em> no es opcional: sin esa palabra las mismas frases suenan a orden.',
    ask2='La misma petición cuando son dos o más. <em>Could</em> es un punto más cortés que <em>can</em> y sirve en todos los casos en que sirve <em>can</em>.',
    ask3='Así se pide. Es la forma corta de <em>I would like</em>. <em>I want</em> es inglés correcto y aun así suena maleducado aquí.',

    wordEyebrow='Las palabras mismas',
    wordTitle='Cuatro sin las que no se sale de una comida',
    word1='La <em>table</em> se pide en la puerta, el <em>menu</em> se lee y la <em>bill</em> se paga. En las cartas americanas la cuenta se llama <em>check</em>.',
    word2='La pregunta más frecuente del camarero. <em>Not yet</em> es la manera cortés de ganar un minuto más.',
    word3='La preposición no cambia nunca: allergic <strong>to</strong>. Ni <em>of</em> ni <em>at</em>. Es la única fórmula de la diapositiva que conviene aprender de memoria.',

    qEyebrow='En la cafetería', qTitle='¿Qué dice usted?',

    gapEyebrow='Una visita entera, por orden', gapTitle='Complete la conversación',
    bankLabel='Banco de palabras:',
    gapHint='Una palabra por hueco. Cada palabra del banco se usa exactamente una vez entre las dos pantallas.',

    ordEyebrow='Dígalo en el orden correcto', ordTitle='Construya la frase',
    ordHint='Haga clic en las palabras por orden. Vuelva a hacer clic en una palabra colocada para retirarla.',

    actTitle='Ahora pida algo', actUse='Use al menos cuatro:',
    actSpeakBrief='Uno hace de camarero y otro de cliente. Después cambien, y pidan otra cosa la segunda vez.',
    actSpeak1='Llegue a la puerta. Pida una mesa para dos y pida sentarse fuera.',
    actSpeak2='Pida la carta. El camarero pregunta si están listos; no lo están. Gane un minuto.',
    actSpeak3='Pida algo de comer y algo de beber. Diga <em>please</em> todas las veces.',
    actSpeak4='Cuéntele al camarero que tiene una alergia y después pida la cuenta.',
    actWriteKind='Escritura · 40–60 palabras',
    actWriteBrief='Escriba su conversación en forma de diálogo. Empieza el camarero.',
    actPlaceholder='Waiter: Good afternoon! Do you have a reservation?',

    resPerfect='Puntuación perfecta. Podría entrar hoy en una cafetería y le entenderían.',
    resStrong='Muy bien. Las fórmulas han calado: repita en voz alta las aperturas corteses.',
    resMid='Buena base. Vuelva a las dos primeras diapositivas; ahí empiezan casi todos los fallos.',
    resLow='Lea otra vez las dos primeras diapositivas y repita la lección. Primero las fórmulas, después las preguntas.',
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
