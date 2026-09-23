# -*- coding: utf-8 -*-
"""Interface strings for the IELTS Listening drills.

English, German and Spanish, teach cards in the six-item form.

The letters and the numbers stay English everywhere, obviously — the lesson
exists because English letter names collide with each other and English says
numbers its own way. What translates is the rule, and on this deck that matters
more than usual: a German or Spanish speaker needs to be told in their own
language that E and I swap places between English and almost every European
language, because that is the single confusion this drill exists to break.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount',
        'audioPlay', 'audioPlaying', 'audioDone', 'audioReplay',
        'audioMissing']

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

# ── English ────────────────────────────────────────────────────────────
T['en'] = dict(
    coverTitle='Numbers, spelling <em>and accents</em>',
    coverSub='The three things that lose marks in every section, drilled on '
             'their own',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; all four sections',
    chipCount='17 points',

    t1Eyebrow='Before you start',
    t1Title='These are not listening problems. They are convention problems.',
    t1ah='English says numbers its own way',
    t1ab='<em>Double oh</em> is two noughts. <em>Oh</em> is one. A room is '
         '<em>eight eighty</em>, not eight hundred and eighty. None of this is '
         'hard to hear &mdash; it is hard to <strong>expect</strong>.',
    t1an='Thirteen and thirty are the costliest pair in the language. The '
         'stress moves; the vowel barely does.',
    t1bh='Letter names collide',
    audioOnce='Press play when you are ready. When it ends, you can replay it.',
    t1bb='<strong>A</strong> and <strong>E</strong>, <strong>E</strong> and '
         '<strong>I</strong>, <strong>G</strong> and <strong>J</strong>, '
         '<strong>M</strong> and <strong>N</strong>. Four pairs, and between '
         'them they account for most of the misspelled answers on the paper.',
    t1bn='E and I are the worst, because they are swapped between English and '
         'most European languages. What you were taught at school is actively '
         'against you here.',
    t1ch='Six accents, one test',
    t1cb='British, American, Australian, Canadian, Irish and New Zealand '
         'English all appear in real papers. The two recordings here are built '
         'from takes in different accents, so you are drilling all three '
         'things at once.',
    t1cn='You cannot learn an accent in a lesson. You can stop being surprised '
         'by one, and that is most of the benefit.',

    numAudEyebrow='Drill 1 &middot; The recording',
    numAudTitle='Five speakers, five numbers',
    numAudNote='Short takes in five accents. Look at the gaps on the next '
               'slides, then press play &mdash; here or in the bar at the foot '
               'of those slides. When it ends you can play it again from here: '
               'this is a drill, not the test.',

    numEyebrow='Drill 1 &middot; Numbers',
    numTitle='Write ONE NUMBER in each gap',
    numHint='Write figures, not words. Two of these are said in a way English '
            'learners are rarely taught.',

    spellAudEyebrow='Drill 2 &middot; The recording',
    spellAudTitle='Two names, spelled once each',
    spellAudNote='Two takes, two accents. Each name is given letter by letter '
                 'exactly once, at speaking speed, as in the real test. Look at '
                 'the gaps on the next slide, then press play.',

    spellEyebrow='Drill 2 &middot; Spelling',
    spellTitle='Write the name exactly as it was spelled',
    spellHint='Spelling is marked. One of these uses the same "double" '
              'convention as the numbers drill.',

    sortEyebrow='Drill 3 &middot; The pairs that collide',
    sortTitle='Which letter names actually get confused?',
    sortHint='Drag each pair into a column &mdash; or click one, then the '
             'column you want it in.',
    sortBin1='Sound alike',
    sortBin2='Rarely confused',

    mcEyebrow='Drill 4 &middot; The conventions',
    mcTitle='What does English actually do here?',

    d1why='44. <em>Double</em> before a digit means two of it, in numbers and '
          'in letters alike &mdash; which is why <em>double F</em> in a name '
          'works the same way.',
    d2why='Thirteen and thirty. The vowels are close and the stress is what '
          'separates them, so at speaking speed a candidate expecting a vowel '
          'difference hears nothing.',
    d3why='Because English is an international language and the test is an '
          'international test. It is not difficulty for its own sake &mdash; a '
          'candidate will meet all of these at a university or a workplace.',
    d4why='The rest of the word. A letter heard in isolation is a coin toss; a '
          'letter inside a name you can half-see is usually forced by what '
          'surrounds it.',

    actTitle='Dictate and check',
    actUse='Use at least three:',
    actSpeakBrief='In pairs, taking turns. Dictate five things to your '
                  'partner: a surname, a phone number, a price, a date and a '
                  'room number. Say each one once, at normal speed. Then swap '
                  'papers and mark them &mdash; every wrong character is a '
                  'lost mark, exactly as in the test.',
    actSpeak1='Use <em>double</em> at least once, in a number and in a name.',
    actSpeak2='Put one number in your set that contains a thirteen or a '
              'thirty, and do not help.',
    actSpeak3='Spell one name containing two of the colliding pairs &mdash; '
              'an A and an E, or an M and an N.',
    actWriteKind='Writing · 80–120 words',
    actWriteBrief='Write out the five items you dictated, in figures and '
                  'letters, then write beside each one the mistake you '
                  'expected your partner to make. Naming the trap in advance '
                  'is what stops you walking into it yourself.',
    actPlaceholder='Surname: … (expected mistake: A heard as R)',
)

# The drill explanations sit beside their answers in the data module, which
# keeps the only copy of the English; they were plain strings there until
# 2026-09-23, so German and Spanish learners read them in English.
from ieltslisten_drills_data import NUMBERS_A, NUMBERS_B, SPELLING, PAIRS_WHY
T['en'].update(('g%dwhy' % (i + 1), r[2])
               for i, r in enumerate(NUMBERS_A + NUMBERS_B))
T['en'].update(('s%dwhy' % (i + 1), r[2]) for i, r in enumerate(SPELLING))
T['en']['pairsWhy'] = PAIRS_WHY

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Zahlen, Buchstabieren <em>und Akzente</em>',
    coverSub='Die drei Dinge, die in jedem Teil Punkte kosten &mdash; einzeln '
             'geübt',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; alle vier Teile',
    chipCount='17 Punkte',

    t1Eyebrow='Bevor du beginnst',
    t1Title='Das sind keine Hörprobleme. Das sind Konventionsprobleme.',
    t1ah='Englisch sagt Zahlen auf seine eigene Art',
    t1ab='<em>Double oh</em> sind zwei Nullen. <em>Oh</em> ist eine. Ein '
         'Zimmer ist <em>eight eighty</em>, nicht eight hundred and eighty. '
         'Nichts davon ist schwer zu hören &mdash; es ist schwer zu '
         '<strong>erwarten</strong>.',
    t1an='Thirteen und thirty sind das teuerste Paar der Sprache. Die Betonung '
         'wandert, der Vokal kaum.',
    t1bh='Buchstabennamen kollidieren',
    audioOnce='Drücke Play, wenn du bereit bist. Danach kannst du es noch einmal hören.',
    t1bb='<strong>A</strong> und <strong>E</strong>, <strong>E</strong> und '
         '<strong>I</strong>, <strong>G</strong> und <strong>J</strong>, '
         '<strong>M</strong> und <strong>N</strong>. Vier Paare, und zusammen '
         'verursachen sie die meisten falsch geschriebenen Antworten.',
    t1bn='E und I sind die schlimmsten, weil sie zwischen Englisch und fast '
         'allen europäischen Sprachen vertauscht sind. Was du in der Schule '
         'gelernt hast, arbeitet hier gegen dich.',
    t1ch='Sechs Akzente, eine Prüfung',
    t1cb='Britisches, amerikanisches, australisches, kanadisches, irisches und '
         'neuseeländisches Englisch kommen in echten Prüfungen vor. Die beiden '
         'Aufnahmen hier bestehen aus Takes in verschiedenen Akzenten &mdash; '
         'du übst also alle drei Dinge gleichzeitig.',
    t1cn='Einen Akzent lernt man nicht in einer Stunde. Man kann aufhören, '
         'sich von ihm überraschen zu lassen, und das ist der größte Teil des '
         'Nutzens.',

    numAudEyebrow='Übung 1 &middot; Die Aufnahme',
    numAudTitle='Fünf Sprecher, fünf Zahlen',
    numAudNote='Kurze Takes in fünf Akzenten. Sieh dir die Lücken auf den '
               'nächsten Folien an, dann drücke Play &mdash; hier oder in der '
               'Leiste unten auf diesen Folien. Danach kannst du es von hier '
               'noch einmal abspielen: das ist eine Übung, nicht die Prüfung.',

    numEyebrow='Übung 1 &middot; Zahlen',
    numTitle='Schreibe EINE ZAHL in jede Lücke',
    numHint='Schreib Ziffern, keine Wörter. Zwei davon werden so gesagt, wie '
            'es Englischlernenden selten beigebracht wird.',

    spellAudEyebrow='Übung 2 &middot; Die Aufnahme',
    spellAudTitle='Zwei Namen, je einmal buchstabiert',
    spellAudNote='Zwei Takes, zwei Akzente. Jeder Name wird genau einmal '
                 'buchstabiert, in normalem Sprechtempo &mdash; so wie in der '
                 'echten Prüfung. Sieh dir zuerst die Lücken auf der nächsten '
                 'Folie an, dann drücke Play.',

    spellEyebrow='Übung 2 &middot; Buchstabieren',
    spellTitle='Schreib den Namen genau so, wie er buchstabiert wurde',
    spellHint='Rechtschreibung wird bewertet. Einer davon nutzt dieselbe '
              '„double“-Konvention wie die Zahlenübung.',

    sortEyebrow='Übung 3 &middot; Die Paare, die kollidieren',
    sortTitle='Welche Buchstabennamen werden wirklich verwechselt?',
    sortHint='Zieh jedes Paar in eine Spalte &mdash; oder klick eins an und '
             'dann die Spalte.',
    sortBin1='Klingen gleich',
    sortBin2='Selten verwechselt',

    mcEyebrow='Übung 4 &middot; Die Konventionen',
    mcTitle='Was macht das Englische hier eigentlich?',

    d1why='44. <em>Double</em> vor einer Ziffer heißt zwei davon &mdash; bei '
          'Zahlen wie bei Buchstaben, weshalb <em>double F</em> in einem Namen '
          'genauso funktioniert.',
    d2why='Thirteen und thirty. Die Vokale liegen nah beieinander, getrennt '
          'werden sie durch die Betonung &mdash; wer auf einen Vokalunterschied '
          'wartet, hört im Sprechtempo gar nichts.',
    d3why='Weil Englisch eine internationale Sprache ist und die Prüfung eine '
          'internationale Prüfung. Es ist keine Schikane: An einer Universität '
          'oder im Beruf trifft man all diese Akzente.',
    d4why='Der Rest des Wortes. Ein isolierter Buchstabe ist ein Münzwurf; '
          'einer in einem Namen, den man halb erkennt, wird meist von seiner '
          'Umgebung erzwungen.',

    actTitle='Diktieren und prüfen',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu zweit, abwechselnd. Diktiere deinem Partner fünf Dinge: '
                  'einen Nachnamen, eine Telefonnummer, einen Preis, ein Datum '
                  'und eine Zimmernummer. Jedes einmal, in normalem Tempo. '
                  'Dann Blätter tauschen und korrigieren &mdash; jedes falsche '
                  'Zeichen ist ein Punkt, wie in der Prüfung.',
    actSpeak1='Benutze <em>double</em> mindestens einmal, in einer Zahl und in '
              'einem Namen.',
    actSpeak2='Bau eine Zahl mit einer Dreizehn oder einer Dreißig ein &mdash; '
              'und hilf nicht.',
    actSpeak3='Buchstabiere einen Namen mit zwei der kollidierenden Paare '
              '&mdash; ein A und ein E, oder ein M und ein N.',
    actWriteKind='Schreiben · 80–120 Wörter',
    actWriteBrief='Schreib die fünf diktierten Dinge in Ziffern und Buchstaben '
                  'auf und daneben jeweils den Fehler, den du bei deinem '
                  'Partner erwartet hast. Die Falle vorher zu benennen ist, '
                  'was einen selbst davor bewahrt.',
    actPlaceholder='Surname: … (expected mistake: A heard as R)',

    # Drills 1-3: the English is registered from the data module, below.
    g1why='„Double oh“ sind zwei Nullen: 004713. Wer sechs einzelne Ziffern '
          'zählt, hört nie sechs.',
    g2why='Dreizehn fünfzig, dann „not thirty, thirteen“: das Paar, das mehr '
          'Punkte kostet als jede andere Zahl im Englischen.',
    g3why='Der Vierzehnte. Ordnungszahlen verschwimmen im Tempo &mdash; '
          'fourteenth und fortieth klingen ähnlich, und nur eines davon ist ein '
          'echtes Datum.',
    g4why='Eight eighty. Im Englischen sagt man Zimmernummern paarweise statt '
          'als ganze Zahl &mdash; deshalb erwarten Lernende „eight hundred and '
          'eighty“ und hören es nie.',
    g5why='Achtzehn. Zwanzig ist der volle Preis und kommt zuerst; die Lücke '
          'fragt nach dem Frühbucherpreis, also schreibst du die Zahl, die an '
          'diese Bedingung geknüpft ist.',
    s1why='Hargreaves. Die Fallen sind die Vokale &mdash; ein A, dann E und A '
          'zusammen &mdash;, die Lernende vertauschen, weil ihr eigenes '
          'Alphabet sie anders benennt, und das G, das man leicht als J '
          'schreibt.',
    s2why='Ffion, mit doppeltem F. Sagt jemand „double“ vor einem Buchstaben, '
          'sind es zwei davon &mdash; dieselbe Konvention wie „double oh“ bei '
          'einer Zahl, und deshalb gehören die beiden Übungen in eine Lektion.',
    pairsWhy='Die vier links sind die, die bei englischen Buchstabennamen '
             'wirklich kollidieren, und auf sie gehen die meisten falsch '
             'geschriebenen Antworten in Section 1 zurück. Das englische '
             '<strong>A</strong> klingt wie das deutsche E und das englische '
             '<strong>E</strong> wie das deutsche I, also werden A und E sowie '
             'E und I von allen vertauscht, die mit ihrem eigenen Alphabet '
             'hören; <strong>G</strong> und <strong>J</strong> beginnen gleich '
             'und unterscheiden sich nur im Vokal; <strong>M</strong> und '
             '<strong>N</strong> nur im Nasal am Ende. W und Y sowie K und Q '
             'klingen, voll ausgesprochen, völlig verschieden &mdash; deshalb '
             'verhört sich dabei niemand.',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Números, deletreo <em>y acentos</em>',
    coverSub='Las tres cosas que cuestan puntos en todas las secciones, '
             'practicadas por separado',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; las cuatro secciones',
    chipCount='17 puntos',

    t1Eyebrow='Antes de empezar',
    t1Title='No son problemas de oído. Son problemas de convención.',
    t1ah='El inglés dice los números a su manera',
    t1ab='<em>Double oh</em> son dos ceros. <em>Oh</em> es uno. Una habitación '
         'es <em>eight eighty</em>, no eight hundred and eighty. Nada de esto '
         'cuesta oírlo: cuesta <strong>esperarlo</strong>.',
    t1an='Thirteen y thirty son el par más caro del idioma. Lo que se mueve es '
         'el acento; la vocal casi no.',
    t1bh='Los nombres de las letras chocan',
    audioOnce='Dale a reproducir cuando estés listo. Al terminar puedes volver a oírlo.',
    t1bb='<strong>A</strong> y <strong>E</strong>, <strong>E</strong> e '
         '<strong>I</strong>, <strong>G</strong> y <strong>J</strong>, '
         '<strong>M</strong> y <strong>N</strong>. Cuatro pares que, entre '
         'todos, causan la mayoría de las respuestas mal escritas del examen.',
    t1bn='E e I son los peores, porque están intercambiados entre el inglés y '
         'casi todas las lenguas europeas. Lo que aprendiste en el colegio '
         'juega en tu contra aquí.',
    t1ch='Seis acentos, un examen',
    t1cb='En los exámenes reales aparecen el inglés británico, americano, '
         'australiano, canadiense, irlandés y neozelandés. Las dos grabaciones '
         'de aquí están hechas con tomas en acentos distintos, así que '
         'practicas las tres cosas a la vez.',
    t1cn='Un acento no se aprende en una clase. Lo que sí se puede es dejar de '
         'que te sorprenda, y ahí está casi todo el beneficio.',

    numAudEyebrow='Ejercicio 1 &middot; La grabación',
    numAudTitle='Cinco hablantes, cinco números',
    numAudNote='Tomas cortas en cinco acentos. Mira los huecos de las '
               'diapositivas siguientes y luego dale a reproducir, aquí o en la '
               'barra de abajo de esas diapositivas. Al terminar puedes volver a '
               'ponerla desde aquí: esto es un ejercicio, no el examen.',

    numEyebrow='Ejercicio 1 &middot; Números',
    numTitle='Escribe UN NÚMERO en cada hueco',
    numHint='Escribe cifras, no palabras. Dos de estos se dicen de una forma '
            'que rara vez se enseña.',

    spellAudEyebrow='Ejercicio 2 &middot; La grabación',
    spellAudTitle='Dos nombres, deletreados una vez cada uno',
    spellAudNote='Dos tomas, dos acentos. Cada nombre se deletrea exactamente '
                 'una vez, a velocidad normal, como en el examen real. Mira '
                 'primero los huecos de la diapositiva siguiente y luego dale a '
                 'reproducir.',

    spellEyebrow='Ejercicio 2 &middot; Deletreo',
    spellTitle='Escribe el nombre tal y como se deletreó',
    spellHint='Se corrige la ortografía. Uno de ellos usa la misma convención '
              '«double» que el ejercicio de números.',

    sortEyebrow='Ejercicio 3 &middot; Los pares que chocan',
    sortTitle='¿Qué nombres de letras se confunden de verdad?',
    sortHint='Arrastra cada par a una columna &mdash; o haz clic en uno y '
             'luego en la columna.',
    sortBin1='Suenan igual',
    sortBin2='Rara vez se confunden',

    mcEyebrow='Ejercicio 4 &middot; Las convenciones',
    mcTitle='¿Qué hace el inglés aquí en realidad?',

    d1why='44. <em>Double</em> delante de un dígito significa dos de ese '
          'dígito, igual en números que en letras: por eso <em>double F</em> '
          'en un nombre funciona igual.',
    d2why='Thirteen y thirty. Las vocales son parecidas y lo que las separa es '
          'el acento, así que a velocidad normal quien espera una diferencia '
          'de vocal no oye nada.',
    d3why='Porque el inglés es una lengua internacional y el examen también. '
          'No es dificultad por gusto: en una universidad o en un trabajo se '
          'van a encontrar todos.',
    d4why='El resto de la palabra. Una letra suelta es cara o cruz; una letra '
          'dentro de un nombre que medio reconoces suele venir forzada por lo '
          'que la rodea.',

    actTitle='Dicta y corrige',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas, por turnos. Dicta a tu compañero cinco cosas: '
                  'un apellido, un número de teléfono, un precio, una fecha y '
                  'un número de habitación. Cada una una sola vez, a velocidad '
                  'normal. Luego intercambiad papeles y corregid: cada '
                  'carácter mal es un punto, igual que en el examen.',
    actSpeak1='Usa <em>double</em> al menos una vez, en un número y en un '
              'nombre.',
    actSpeak2='Mete en tu lista un número con un thirteen o un thirty, y no '
              'ayudes.',
    actSpeak3='Deletrea un nombre que lleve dos de los pares que chocan: una A '
              'y una E, o una M y una N.',
    actWriteKind='Escritura · 80–120 palabras',
    actWriteBrief='Escribe las cinco cosas que dictaste, en cifras y letras, y '
                  'al lado de cada una el error que esperabas que cometiera tu '
                  'compañero. Nombrar la trampa por adelantado es lo que evita '
                  'que caigas tú en ella.',
    actPlaceholder='Surname: … (expected mistake: A heard as R)',

    # Drills 1-3: the English is registered from the data module, below.
    g1why='«Double oh» son dos ceros: 004713. Quien cuenta seis cifras sueltas '
          'nunca oye seis.',
    g2why='Trece cincuenta, y luego «not thirty, thirteen»: la pareja que más '
          'puntos cuesta de todos los números en inglés.',
    g3why='El catorce. Los ordinales se funden al hablar rápido: fourteenth y '
          'fortieth suenan parecidos, y solo uno de ellos es una fecha real.',
    g4why='Eight eighty. En inglés un número de habitación se dice por '
          'parejas, no como número entero; por eso quien aprende espera «eight '
          'hundred and eighty» y nunca lo oye.',
    g5why='Dieciocho. Veinte es el precio completo y se dice primero; el hueco '
          'pide el precio con reserva anticipada, así que hay que escribir la '
          'cifra ligada a esa condición.',
    s1why='Hargreaves. Las trampas son las vocales (una A, y luego E y A '
          'juntas), que se intercambian porque el alfabeto propio las nombra '
          'de otra manera, y la G, que es fácil escribir como J.',
    s2why='Ffion, con doble F. Cuando alguien dice «double» delante de una '
          'letra, son dos: la misma convención que «double oh» en un número, y '
          'por eso los dos ejercicios van en la misma lección.',
    pairsWhy='Las cuatro de la izquierda son las que de verdad chocan en los '
             'nombres de las letras en inglés, y entre ellas explican la mayoría '
             'de las respuestas mal escritas de la Section 1. La '
             '<strong>A</strong> inglesa suena como la E española, y la '
             '<strong>E</strong> inglesa como la I española, así que A y E, y E '
             'e I, las intercambia cualquiera que oiga con su propio alfabeto; '
             '<strong>G</strong> y <strong>J</strong> empiezan igual y solo se '
             'diferencian en la vocal; <strong>M</strong> y <strong>N</strong>, '
             'solo en la nasal final. W e Y, y K y Q, no se parecen en nada '
             'dichas enteras, y por eso nadie las confunde.',
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
