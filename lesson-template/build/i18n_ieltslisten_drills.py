# -*- coding: utf-8 -*-
"""Interface strings for the IELTS Listening drills.

All ten IELTS languages (`ielts_langs.LANGS`), teach cards in the
six-item form. English, German and Spanish from the start; French,
Italian, Portuguese, Russian, Arabic, Chinese and Japanese added on
2026-10-05 (conventions in `ielts_langs.py`).

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
from ielts_langs import TAIL_MORE

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
TAIL.update(TAIL_MORE)

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

# ── French ──────────────────────────────────────────────────────────
T['fr'] = dict(
    coverTitle='Nombres, orthographe <em>et accents</em>',
    coverSub='Les trois choses qui font perdre des points dans chaque section, '
             'entraînées séparément',
    chipLevel='B2&ndash;C1',
    chipFocus='Listening &middot; les quatre sections',
    chipCount='17 points',
    t1Eyebrow='Avant de commencer',
    t1Title="Ce ne sont pas des problèmes d'écoute. Ce sont des problèmes de "
            'convention.',
    t1ah="L'anglais dit les nombres à sa façon",
    t1ab="<em>Double oh</em>, c'est deux zéros. <em>Oh</em>, c'est un seul. "
         'Une chambre est <em>eight eighty</em>, pas eight hundred and '
         "eighty. Rien de tout cela n'est difficile à entendre — c'est "
         'difficile à <strong>anticiper</strong>.',
    t1an='Thirteen et thirty sont la paire la plus coûteuse de la langue. '
         "L'accent se déplace ; la voyelle, à peine.",
    t1bh='Les noms des lettres se confondent',
    audioOnce='Lancez la lecture quand vous êtes prêt. À la fin, vous pourrez la '
              'réécouter.',
    t1bb='<strong>A</strong> et <strong>E</strong>, <strong>E</strong> et '
         '<strong>I</strong>, <strong>G</strong> et <strong>J</strong>, '
         '<strong>M</strong> et <strong>N</strong>. Quatre paires, et à '
         'elles seules elles expliquent la plupart des réponses mal '
         "orthographiées de l'épreuve.",
    t1bn="E et I sont les pires, parce qu'ils sont inversés entre l'anglais "
         "et la plupart des langues européennes. Ce qu'on vous a appris à "
         "l'école joue ici activement contre vous.",
    t1ch='Six accents, un seul test',
    t1cb="L'anglais britannique, américain, australien, canadien, irlandais "
         'et néo-zélandais apparaissent tous dans de vrais sujets. Les deux '
         "enregistrements d'ici sont montés à partir de prises dans "
         'différents accents, vous travaillez donc les trois choses à la '
         'fois.',
    t1cn="On n'apprend pas un accent en une leçon. On peut cesser d'être "
         "surpris par lui, et c'est là l'essentiel du bénéfice.",
    numAudEyebrow="Exercice 1 &middot; L'enregistrement",
    numAudTitle='Cinq voix, cinq nombres',
    numAudNote='De courtes prises dans cinq accents. Regardez les espaces des '
               'diapositives suivantes, puis lancez la lecture — ici ou dans la '
               'barre au bas de ces diapositives. À la fin, vous pourrez la '
               "relancer d'ici : c'est un exercice, pas le test.",
    numEyebrow='Exercice 1 &middot; Les nombres',
    numTitle='Écrivez UN NOMBRE dans chaque espace',
    numHint="Écrivez des chiffres, pas des mots. Deux sont dits d'une manière "
            'rarement enseignée aux apprenants.',
    spellAudEyebrow="Exercice 2 &middot; L'enregistrement",
    spellAudTitle='Deux noms, épelés une fois chacun',
    spellAudNote='Deux prises, deux accents. Chaque nom est donné lettre par lettre '
                 'exactement une fois, à vitesse de parole, comme dans le vrai test. '
                 'Regardez les espaces de la diapositive suivante, puis lancez la '
                 'lecture.',
    spellEyebrow="Exercice 2 &middot; L'orthographe",
    spellTitle='Écrivez le nom exactement comme il a été épelé',
    spellHint="L'orthographe est notée. L'un de ces noms utilise la même "
              "convention « double » que l'exercice sur les nombres.",
    sortEyebrow='Exercice 3 &middot; Les paires qui se confondent',
    sortTitle='Quels noms de lettres se confondent vraiment ?',
    sortHint='Glissez chaque paire dans une colonne — ou cliquez sur une paire, '
             'puis sur la colonne voulue.',
    sortBin1='Se ressemblent',
    sortBin2='Rarement confondues',
    mcEyebrow='Exercice 4 &middot; Les conventions',
    mcTitle="Que fait vraiment l'anglais ici ?",
    d1why='44. <em>Double</em> devant un chiffre signifie deux fois ce '
          "chiffre, pour les nombres comme pour les lettres — c'est pourquoi "
          '<em>double F</em> dans un nom fonctionne de la même façon.',
    d2why="Thirteen et thirty. Les voyelles sont proches et c'est l'accent "
          "qui les distingue, si bien qu'à vitesse de parole un candidat qui "
          "attend une différence de voyelle n'entend rien.",
    d3why="Parce que l'anglais est une langue internationale et que le test "
          "est un test international. Ce n'est pas de la difficulté pour "
          'elle-même — un candidat rencontrera tous ces accents à '
          "l'université ou au travail.",
    d4why="Le reste du mot. Une lettre entendue isolément, c'est un pile ou "
          "face ; une lettre à l'intérieur d'un nom que l'on devine à moitié "
          "est généralement imposée par ce qui l'entoure.",
    actTitle='Dictez et vérifiez',
    actUse='Utilisez-en au moins trois :',
    actSpeakBrief='Par deux, à tour de rôle. Dictez cinq choses à votre partenaire : '
                  'un nom de famille, un numéro de téléphone, un prix, une date et un '
                  'numéro de chambre. Dites chacune une seule fois, à vitesse '
                  'normale. Puis échangez vos feuilles et corrigez-les — chaque '
                  'caractère faux est un point perdu, exactement comme dans le test.',
    actSpeak1='Utilisez <em>double</em> au moins une fois, dans un nombre et dans '
              'un nom.',
    actSpeak2='Mettez dans votre série un nombre qui contient thirteen ou thirty, '
              "et n'aidez pas.",
    actSpeak3='Épelez un nom qui contient deux des paires qui se confondent — un '
              'A et un E, ou un M et un N.',
    actWriteKind='Writing · 80–120 mots',
    actWriteBrief='Écrivez les cinq éléments que vous avez dictés, en chiffres et en '
                  "lettres, puis notez à côté de chacun l'erreur que vous attendiez "
                  "de votre partenaire. Nommer le piège à l'avance, c'est ce qui vous "
                  "empêche d'y tomber vous-même.",
    actPlaceholder='Surname: … (expected mistake: A heard as R)',
    g1why="« Double oh », c'est deux zéros : 004713. Qui compte six chiffres "
          "séparés n'en entend jamais six.",
    g2why='Treize cinquante, puis « not thirty, thirteen » : la paire la plus '
          'coûteuse de tous les nombres anglais.',
    g3why='Le quatorze. À vitesse normale, fourteenth et fortieth sonnent '
          'presque pareil, et un seul des deux est une vraie date.',
    g4why="Eight eighty. L'anglais dit un numéro de chambre par paires plutôt "
          "que comme un nombre entier, c'est pourquoi « eight hundred and "
          "eighty » est ce qu'un apprenant attend et n'entend jamais.",
    g5why='Dix-huit. Vingt est le plein tarif et il est dit en premier ; '
          "l'espace demande le tarif de réservation anticipée, c'est donc le "
          "chiffre lié à cette condition qu'il faut écrire.",
    s1why='Hargreaves. Les pièges sont les voyelles — un A, puis E et A '
          'ensemble — que les apprenants inversent parce que leur propre '
          'alphabet les nomme autrement, et le G, facilement écrit J.',
    s2why='Ffion, avec un double F. Quand un locuteur dit « double » devant '
          "une lettre, c'est deux fois celle-ci — la même convention que « "
          "double oh » dans un nombre, et c'est pourquoi les deux exercices "
          'tiennent dans une seule leçon.',
    pairsWhy='Les quatre de gauche sont celles qui se confondent vraiment dans '
             'les noms de lettres anglais, et à elles seules elles expliquent la '
             'plupart des réponses mal orthographiées de la section 1. Le '
             '<strong>A</strong> anglais sonne comme le E de la plupart des '
             'alphabets européens, et le <strong>E</strong> anglais comme leur '
             'I, si bien que A et E, et E et I, sont inversés par quiconque '
             'écoute avec son propre alphabet ; <strong>G</strong> et '
             '<strong>J</strong> partagent leur attaque et ne diffèrent que par '
             'la voyelle ; <strong>M</strong> et <strong>N</strong> ne diffèrent '
             'que par la nasale finale. W et Y, et K et Q, ne se ressemblent en '
             "rien une fois dits en entier — c'est pourquoi personne ne les "
             'confond.',
)

# ── Italian ─────────────────────────────────────────────────────────
T['it'] = dict(
    coverTitle='Numeri, spelling <em>e accenti</em>',
    coverSub='Le tre cose che fanno perdere punti in ogni sezione, allenate da '
             'sole',
    chipLevel='B2&ndash;C1',
    chipFocus='Listening &middot; tutte e quattro le sezioni',
    chipCount='17 punti',
    t1Eyebrow='Prima di cominciare',
    t1Title='Non sono problemi di ascolto. Sono problemi di convenzione.',
    t1ah="L'inglese dice i numeri a modo suo",
    t1ab='<em>Double oh</em> sono due zeri. <em>Oh</em> è uno. Una stanza è '
         '<em>eight eighty</em>, non eight hundred and eighty. Niente di '
         'tutto questo è difficile da sentire — è difficile da '
         '<strong>aspettarsi</strong>.',
    t1an='Thirteen e thirty sono la coppia più costosa della lingua. '
         "L'accento si sposta; la vocale quasi no.",
    t1bh='I nomi delle lettere si confondono',
    audioOnce='Premi play quando sei pronto. Alla fine potrai riascoltarlo.',
    t1bb='<strong>A</strong> ed <strong>E</strong>, <strong>E</strong> e '
         '<strong>I</strong>, <strong>G</strong> e <strong>J</strong>, '
         '<strong>M</strong> ed <strong>N</strong>. Quattro coppie, e tra '
         'loro spiegano la maggior parte delle risposte scritte male nella '
         'prova.',
    t1bn="E e I sono le peggiori, perché sono invertite tra l'inglese e la "
         'maggior parte delle lingue europee. Quello che ti hanno insegnato '
         'a scuola qui gioca attivamente contro di te.',
    t1ch='Sei accenti, un solo test',
    t1cb="L'inglese britannico, americano, australiano, canadese, irlandese "
         'e neozelandese compaiono tutti nelle prove reali. Le due '
         'registrazioni qui sono costruite da prese in accenti diversi, così '
         'alleni tutte e tre le cose insieme.',
    t1cn='Non si impara un accento in una lezione. Si può smettere di '
         'esserne sorpresi, ed è questo gran parte del beneficio.',
    numAudEyebrow='Esercizio 1 &middot; La registrazione',
    numAudTitle='Cinque voci, cinque numeri',
    numAudNote='Brevi prese in cinque accenti. Guarda gli spazi nelle slide '
               'successive, poi premi play — qui o nella barra in fondo a quelle '
               'slide. Alla fine potrai riascoltarla da qui: è un esercizio, non '
               'il test.',
    numEyebrow='Esercizio 1 &middot; I numeri',
    numTitle='Scrivi UN NUMERO in ogni spazio',
    numHint='Scrivi cifre, non parole. Due di questi vengono detti in un modo '
            "che a chi impara l'inglese si insegna di rado.",
    spellAudEyebrow='Esercizio 2 &middot; La registrazione',
    spellAudTitle='Due nomi, compitati una volta ciascuno',
    spellAudNote='Due prese, due accenti. Ogni nome viene dato lettera per lettera '
                 'esattamente una volta, a velocità di parlato, come nel test vero. '
                 'Guarda gli spazi nella slide successiva, poi premi play.',
    spellEyebrow='Esercizio 2 &middot; Lo spelling',
    spellTitle='Scrivi il nome esattamente come è stato compitato',
    spellHint='Lo spelling viene valutato. Uno di questi usa la stessa '
              "convenzione «double» dell'esercizio sui numeri.",
    sortEyebrow='Esercizio 3 &middot; Le coppie che si confondono',
    sortTitle='Quali nomi di lettere si confondono davvero?',
    sortHint='Trascina ogni coppia in una colonna — oppure clicca una coppia, '
             'poi la colonna in cui vuoi metterla.',
    sortBin1='Suonano simili',
    sortBin2='Raramente confuse',
    mcEyebrow='Esercizio 4 &middot; Le convenzioni',
    mcTitle="Che cosa fa davvero l'inglese qui?",
    d1why='44. <em>Double</em> prima di una cifra significa due volte quella '
          'cifra, nei numeri come nelle lettere — ed è per questo che '
          '<em>double F</em> in un nome funziona allo stesso modo.',
    d2why="Thirteen e thirty. Le vocali sono vicine ed è l'accento a "
          'separarle, così a velocità di parlato un candidato che si aspetta '
          'una differenza di vocale non sente nulla.',
    d3why="Perché l'inglese è una lingua internazionale e il test è un test "
          'internazionale. Non è difficoltà per il gusto di esserlo — un '
          "candidato incontrerà tutti questi accenti all'università o sul "
          'lavoro.',
    d4why='Il resto della parola. Una lettera sentita da sola è un lancio di '
          'moneta; una lettera dentro un nome che riesci a intravedere è di '
          'solito imposta da ciò che la circonda.',
    actTitle='Detta e controlla',
    actUse='Usane almeno tre:',
    actSpeakBrief='In coppia, a turno. Detta cinque cose al tuo compagno: un cognome, '
                  'un numero di telefono, un prezzo, una data e un numero di stanza. '
                  "Di' ciascuna una sola volta, a velocità normale. Poi scambiatevi i "
                  'fogli e correggeteli — ogni carattere sbagliato è un punto perso, '
                  'esattamente come nel test.',
    actSpeak1='Usa <em>double</em> almeno una volta, in un numero e in un nome.',
    actSpeak2='Metti nella tua serie un numero che contenga thirteen o thirty, e '
              'non aiutare.',
    actSpeak3='Compita un nome che contenga due delle coppie che si confondono — '
              'una A e una E, oppure una M e una N.',
    actWriteKind='Writing · 80–120 parole',
    actWriteBrief='Scrivi i cinque elementi che hai dettato, in cifre e in lettere, '
                  "poi scrivi accanto a ciascuno l'errore che ti aspettavi dal tuo "
                  'compagno. Dare un nome alla trappola in anticipo è ciò che ti '
                  'impedisce di caderci tu stesso.',
    actPlaceholder='Surname: … (expected mistake: A heard as R)',
    g1why='«Double oh» sono due zeri: 004713. Un candidato che conta sei '
          'cifre separate non ne sente mai sei.',
    g2why='Tredici e cinquanta, poi «not thirty, thirteen»: la coppia che '
          'costa più punti di qualsiasi altro numero in inglese.',
    g3why='Il quattordici. Gli ordinali si accavallano a velocità normale — '
          'fourteenth e fortieth suonano quasi uguali, e solo uno dei due è '
          'una data vera.',
    g4why="Eight eighty. L'inglese dice un numero di stanza a coppie invece "
          'che come numero intero, ed è per questo che «eight hundred and '
          'eighty» è ciò che chi impara si aspetta e non sente mai.',
    g5why='Diciotto. Venti è il prezzo pieno e viene detto per primo; lo '
          'spazio chiede il prezzo per chi prenota in anticipo, quindi la '
          'cifra legata a quella condizione è quella da scrivere.',
    s1why='Hargreaves. Le trappole sono le vocali — una A, poi E e A insieme '
          '— che chi impara inverte perché il proprio alfabeto le chiama in '
          'modo diverso, e la G, che si scrive facilmente J.',
    s2why='Ffion, con doppia F. Quando chi parla dice «double» prima di una '
          'lettera, sono due — la stessa convenzione di «double oh» in un '
          'numero, ed è per questo che i due esercizi stanno in una sola '
          'lezione.',
    pairsWhy='Le quattro a sinistra sono quelle che si confondono davvero nei '
             'nomi delle lettere inglesi, e tra loro spiegano la maggior parte '
             'delle risposte scritte male nella sezione 1. La <strong>A</strong> '
             'inglese suona come la E della maggior parte degli alfabeti '
             'europei, e la <strong>E</strong> inglese come la loro I, così A ed '
             'E, ed E e I, vengono invertite da chiunque ascolti con il proprio '
             'alfabeto; <strong>G</strong> e <strong>J</strong> condividono il '
             'suono iniziale e differiscono solo nella vocale; '
             '<strong>M</strong> ed <strong>N</strong> differiscono solo nella '
             'nasale finale. W e Y, e K e Q, non si somigliano affatto una volta '
             'dette per intero — ed è per questo che nessuno le fraintende.',
)

# ── Portuguese ──────────────────────────────────────────────────────
T['pt'] = dict(
    coverTitle='Números, ortografia <em>e sotaques</em>',
    coverSub='As três coisas que fazem perder pontos em todas as secções, '
             'treinadas em separado',
    chipLevel='B2&ndash;C1',
    chipFocus='Listening &middot; as quatro secções',
    chipCount='17 pontos',
    t1Eyebrow='Antes de começar',
    t1Title='Não são problemas de audição. São problemas de convenção.',
    t1ah='O inglês diz os números à sua maneira',
    t1ab='<em>Double oh</em> são dois zeros. <em>Oh</em> é um. Um quarto é '
         '<em>eight eighty</em>, não eight hundred and eighty. Nada disto é '
         'difícil de ouvir — é difícil de <strong>esperar</strong>.',
    t1an='Thirteen e thirty são o par mais caro da língua. O acento muda; a '
         'vogal quase não.',
    t1bh='Os nomes das letras confundem-se',
    audioOnce='Carrega em play quando estiveres pronto. Quando acabar, podes '
              'voltar a ouvir.',
    t1bb='<strong>A</strong> e <strong>E</strong>, <strong>E</strong> e '
         '<strong>I</strong>, <strong>G</strong> e <strong>J</strong>, '
         '<strong>M</strong> e <strong>N</strong>. Quatro pares, e entre '
         'eles explicam a maior parte das respostas mal escritas na prova.',
    t1bn='E e I são os piores, porque estão trocados entre o inglês e a '
         'maioria das línguas europeias. O que te ensinaram na escola joga '
         'aqui ativamente contra ti.',
    t1ch='Seis sotaques, um teste',
    t1cb='Inglês britânico, americano, australiano, canadiano, irlandês e '
         'neozelandês aparecem todos em provas reais. As duas gravações aqui '
         'são montadas a partir de takes em sotaques diferentes, por isso '
         'treinas as três coisas ao mesmo tempo.',
    t1cn='Não se aprende um sotaque numa lição. Pode-se deixar de ser '
         'apanhado de surpresa por ele, e isso é a maior parte do benefício.',
    numAudEyebrow='Exercício 1 &middot; A gravação',
    numAudTitle='Cinco vozes, cinco números',
    numAudNote='Takes curtos em cinco sotaques. Olha para os espaços nos '
               'diapositivos seguintes e depois carrega em play — aqui ou na barra '
               'ao fundo desses diapositivos. Quando acabar, podes voltar a ouvir '
               'a partir daqui: isto é um exercício, não o teste.',
    numEyebrow='Exercício 1 &middot; Números',
    numTitle='Escreve UM NÚMERO em cada espaço',
    numHint='Escreve algarismos, não palavras. Dois destes são ditos de uma '
            'forma que raramente se ensina a quem aprende inglês.',
    spellAudEyebrow='Exercício 2 &middot; A gravação',
    spellAudTitle='Dois nomes, soletrados uma vez cada',
    spellAudNote='Dois takes, dois sotaques. Cada nome é dado letra a letra '
                 'exatamente uma vez, à velocidade da fala, como no teste real. Olha '
                 'para os espaços no diapositivo seguinte e depois carrega em play.',
    spellEyebrow='Exercício 2 &middot; Ortografia',
    spellTitle='Escreve o nome exatamente como foi soletrado',
    spellHint='A ortografia conta. Um destes usa a mesma convenção «double» do '
              'exercício dos números.',
    sortEyebrow='Exercício 3 &middot; Os pares que se confundem',
    sortTitle='Que nomes de letras se confundem mesmo?',
    sortHint='Arrasta cada par para uma coluna — ou clica num par e depois na '
             'coluna onde o queres.',
    sortBin1='Soam parecido',
    sortBin2='Raramente confundidos',
    mcEyebrow='Exercício 4 &middot; As convenções',
    mcTitle='O que faz o inglês realmente aqui?',
    d1why='44. <em>Double</em> antes de um algarismo significa dois desse '
          'algarismo, tanto em números como em letras — e é por isso que '
          '<em>double F</em> num nome funciona da mesma forma.',
    d2why='Thirteen e thirty. As vogais são próximas e é o acento que as '
          'separa, por isso, à velocidade da fala, um candidato à espera de '
          'uma diferença de vogal não ouve nada.',
    d3why='Porque o inglês é uma língua internacional e o teste é um teste '
          'internacional. Não é dificuldade por dificuldade — um candidato '
          'vai encontrar todos estes sotaques numa universidade ou num local '
          'de trabalho.',
    d4why='O resto da palavra. Uma letra ouvida isolada é um cara ou coroa; '
          'uma letra dentro de um nome que já se adivinha é normalmente '
          'imposta pelo que a rodeia.',
    actTitle='Dita e verifica',
    actUse='Usa pelo menos três:',
    actSpeakBrief='A pares, à vez. Dita cinco coisas ao teu colega: um apelido, um '
                  'número de telefone, um preço, uma data e um número de quarto. Diz '
                  'cada uma só uma vez, a velocidade normal. Depois troquem as folhas '
                  'e corrijam-nas — cada carácter errado é um ponto perdido, '
                  'exatamente como no teste.',
    actSpeak1='Usa <em>double</em> pelo menos uma vez, num número e num nome.',
    actSpeak2='Põe no teu conjunto um número que contenha thirteen ou thirty, e '
              'não ajudes.',
    actSpeak3='Soletra um nome que contenha dois dos pares que se confundem — um '
              'A e um E, ou um M e um N.',
    actWriteKind='Writing · 80–120 palavras',
    actWriteBrief='Escreve os cinco itens que ditaste, em algarismos e letras, e '
                  'depois escreve ao lado de cada um o erro que esperavas que o teu '
                  'colega cometesse. Dar nome à armadilha de antemão é o que te '
                  'impede de cair nela.',
    actPlaceholder='Surname: … (expected mistake: A heard as R)',
    g1why='«Double oh» são dois zeros: 004713. Um candidato a contar seis '
          'algarismos separados nunca ouve seis.',
    g2why='Treze e cinquenta, depois «not thirty, thirteen»: o par que custa '
          'mais pontos do que qualquer outro número em inglês.',
    g3why='Dia catorze. Os ordinais atropelam-se à velocidade normal — '
          'fourteenth e fortieth saem parecidos, e só um deles é uma data '
          'real.',
    g4why='Eight eighty. O inglês diz um número de quarto aos pares, e não '
          'como um número inteiro, e é por isso que «eight hundred and '
          'eighty» é o que quem aprende espera e nunca ouve.',
    g5why='Dezoito. Vinte é o preço completo e é dito primeiro; o espaço pede '
          'o preço de reserva antecipada, por isso o valor ligado a essa '
          'condição é o que deves escrever.',
    s1why='Hargreaves. As armadilhas são as vogais — um A, depois E e A '
          'juntos — que quem aprende troca porque o seu próprio alfabeto lhes '
          'dá outros nomes, e o G, que facilmente se escreve J.',
    s2why='Ffion, com F duplo. Quando alguém diz «double» antes de uma letra, '
          'são duas — a mesma convenção de «double oh» num número, e é por '
          'isso que os dois exercícios cabem numa só lição.',
    pairsWhy='Os quatro da esquerda são os que realmente se confundem nos nomes '
             'das letras em inglês, e entre eles explicam a maior parte das '
             'respostas mal escritas da secção 1. O <strong>A</strong> inglês '
             'soa como o E da maioria dos alfabetos europeus, e o '
             '<strong>E</strong> inglês como o I deles, por isso A e E, e E e I, '
             'são trocados por quem ouve com o seu próprio alfabeto; '
             '<strong>G</strong> e <strong>J</strong> partilham o som inicial e '
             'diferem só na vogal; <strong>M</strong> e <strong>N</strong> '
             'diferem só na nasal final. W e Y, e K e Q, não soam nada parecido '
             'depois de ditos por inteiro — e é por isso que ninguém os ouve '
             'mal.',
)

# ── Russian ─────────────────────────────────────────────────────────
T['ru'] = dict(
    coverTitle='Числа, написание <em>и акценты</em>',
    coverSub='Три вещи, которые отнимают баллы в каждом разделе, отработанные по '
             'отдельности',
    chipLevel='B2&ndash;C1',
    chipFocus='Listening &middot; все четыре раздела',
    chipCount='17 баллов',
    t1Eyebrow='Перед началом',
    t1Title='Это не проблемы со слухом. Это проблемы с условностями.',
    t1ah='Английский произносит числа по-своему',
    t1ab='<em>Double oh</em> — это два нуля. <em>Oh</em> — один. Номер '
         'комнаты — <em>eight eighty</em>, а не eight hundred and eighty. '
         'Ничего из этого не трудно расслышать — трудно '
         '<strong>ожидать</strong>.',
    t1an='Thirteen и thirty — самая дорогая пара в языке. Ударение '
         'смещается; гласный почти нет.',
    t1bh='Названия букв сталкиваются',
    audioOnce='Нажмите play, когда будете готовы. Когда запись закончится, вы '
              'сможете прослушать её снова.',
    t1bb='<strong>A</strong> и <strong>E</strong>, <strong>E</strong> и '
         '<strong>I</strong>, <strong>G</strong> и <strong>J</strong>, '
         '<strong>M</strong> и <strong>N</strong>. Четыре пары, и на них '
         'приходится большинство ответов с ошибками в написании.',
    t1bn='E и I — худшие, потому что они поменяны местами между английским и '
         'большинством европейских языков. То, чему вас учили в школе, здесь '
         'активно работает против вас.',
    t1ch='Шесть акцентов, один тест',
    t1cb='Британский, американский, австралийский, канадский, ирландский и '
         'новозеландский английский — все встречаются в настоящих экзаменах. '
         'Две записи здесь собраны из дублей с разными акцентами, так что вы '
         'отрабатываете все три вещи сразу.',
    t1cn='Акцент нельзя выучить за один урок. Можно перестать удивляться '
         'ему, и в этом большая часть пользы.',
    numAudEyebrow='Упражнение 1 &middot; Запись',
    numAudTitle='Пять голосов, пять чисел',
    numAudNote='Короткие дубли с пятью акцентами. Посмотрите на пропуски на '
               'следующих слайдах, затем нажмите play — здесь или на панели внизу '
               'этих слайдов. Когда запись закончится, вы сможете запустить её '
               'отсюда снова: это упражнение, а не тест.',
    numEyebrow='Упражнение 1 &middot; Числа',
    numTitle='Напишите ОДНО ЧИСЛО в каждый пропуск',
    numHint='Пишите цифрами, а не словами. Два из них произносятся так, как '
            'изучающих английский учат редко.',
    spellAudEyebrow='Упражнение 2 &middot; Запись',
    spellAudTitle='Два имени, каждое продиктовано по буквам один раз',
    spellAudNote='Два дубля, два акцента. Каждое имя даётся по буквам ровно один '
                 'раз, в темпе речи, как в настоящем тесте. Посмотрите на пропуски '
                 'на следующем слайде, затем нажмите play.',
    spellEyebrow='Упражнение 2 &middot; Написание',
    spellTitle='Напишите имя точно так, как оно было продиктовано',
    spellHint='Написание оценивается. Одно из них использует ту же условность '
              '«double», что и упражнение с числами.',
    sortEyebrow='Упражнение 3 &middot; Пары, которые сталкиваются',
    sortTitle='Какие названия букв действительно путают?',
    sortHint='Перетащите каждую пару в столбец — или нажмите на пару, затем на '
             'нужный столбец.',
    sortBin1='Звучат похоже',
    sortBin2='Путают редко',
    mcEyebrow='Упражнение 4 &middot; Условности',
    mcTitle='Что английский на самом деле делает здесь?',
    d1why='44. <em>Double</em> перед цифрой означает две такие цифры — и в '
          'числах, и в буквах, — поэтому <em>double F</em> в имени работает '
          'так же.',
    d2why='Thirteen и thirty. Гласные близки, и разделяет их ударение, '
          'поэтому в темпе речи кандидат, ожидающий разницы в гласном, не '
          'слышит ничего.',
    d3why='Потому что английский — международный язык, а тест — международный '
          'тест. Это не сложность ради сложности: кандидат встретит все эти '
          'акценты в университете или на работе.',
    d4why='Остальная часть слова. Буква, услышанная отдельно, — подбрасывание '
          'монеты; буква внутри имени, которое вы наполовину видите, обычно '
          'определяется тем, что её окружает.',
    actTitle='Диктуйте и проверяйте',
    actUse='Используйте не менее трёх:',
    actSpeakBrief='В парах, по очереди. Продиктуйте партнёру пять вещей: фамилию, '
                  'номер телефона, цену, дату и номер комнаты. Каждую скажите один '
                  'раз, в обычном темпе. Затем обменяйтесь листами и проверьте их — '
                  'каждый неверный знак — потерянный балл, точно как в тесте.',
    actSpeak1='Используйте <em>double</em> хотя бы один раз — в числе и в имени.',
    actSpeak2='Включите в свой набор одно число с thirteen или thirty и не '
              'помогайте.',
    actSpeak3='Продиктуйте по буквам имя, содержащее две из сталкивающихся пар — '
              'A и E или M и N.',
    actWriteKind='Writing · 80–120 слов',
    actWriteBrief='Выпишите пять продиктованных пунктов цифрами и буквами, затем '
                  'рядом с каждым напишите ошибку, которую вы ожидали от партнёра. '
                  'Назвать ловушку заранее — это то, что не даёт попасть в неё '
                  'самому.',
    actPlaceholder='Surname: … (expected mistake: A heard as R)',
    g1why='«Double oh» — это два нуля: 004713. Кандидат, считающий шесть '
          'отдельных цифр, никогда не слышит шести.',
    g2why='Тринадцать пятьдесят, затем «not thirty, thirteen»: пара, которая '
          'стоит больше баллов, чем любое другое число в английском.',
    g3why='Четырнадцатое. Порядковые числительные сливаются в темпе речи — '
          'fourteenth и fortieth звучат похоже, и только одно из них '
          'настоящая дата.',
    g4why='Eight eighty. Английский называет номер комнаты парами, а не целым '
          'числом, поэтому «eight hundred and eighty» — то, чего ждёт '
          'учащийся и никогда не слышит.',
    g5why='Восемнадцать. Двадцать — полная цена, и она называется первой; '
          'пропуск спрашивает цену при раннем бронировании, так что писать '
          'надо число, связанное с этим условием.',
    s1why='Hargreaves. Ловушки — гласные: A, затем E и A вместе, — которые '
          'учащиеся меняют местами, потому что их собственный алфавит '
          'называет их иначе, и G, которую легко записать как J.',
    s2why='Ffion, с двойной F. Когда говорящий произносит «double» перед '
          'буквой, это две такие буквы — та же условность, что «double oh» в '
          'числе, и поэтому два упражнения входят в один урок.',
    pairsWhy='Четыре слева — те, что действительно сталкиваются в английских '
             'названиях букв, и на них приходится большинство ответов раздела 1 '
             'с ошибками в написании. Английское <strong>A</strong> звучит как E '
             'большинства европейских алфавитов, а английское <strong>E</strong> '
             '— как их I, поэтому A и E, E и I меняет местами каждый, кто '
             'слушает со своим алфавитом; <strong>G</strong> и '
             '<strong>J</strong> начинаются одинаково и различаются только '
             'гласным; <strong>M</strong> и <strong>N</strong> различаются '
             'только конечным носовым. W и Y, K и Q, произнесённые полностью, '
             'звучат совсем по-разному — поэтому их никто не путает.',
)

# ── Arabic ──────────────────────────────────────────────────────────
T['ar'] = dict(
    coverTitle='الأرقام والتهجئة <em>واللهجات</em>',
    coverSub='الأمور الثلاثة التي تُضيّع العلامات في كل قسم، مدرَّبة كل على حدة',
    chipLevel='B2&ndash;C1',
    chipFocus='Listening &middot; الأقسام الأربعة كلها',
    chipCount='17 نقطة',
    t1Eyebrow='قبل أن تبدأ',
    t1Title='هذه ليست مشكلات في الاستماع. إنها مشكلات في العُرف.',
    t1ah='الإنجليزية تقول الأرقام على طريقتها',
    t1ab='<em><bdi>Double oh</bdi></em> صفران. <em><bdi>Oh</bdi></em> صفر '
         'واحد. الغرفة هي <em><bdi>eight eighty</bdi></em>، لا <bdi>eight '
         'hundred and eighty</bdi>. لا شيء من هذا صعب السمع — بل صعب '
         '<strong>التوقع</strong>.',
    t1an='<bdi>Thirteen</bdi> و<bdi>thirty</bdi> أغلى زوج في اللغة. النبر '
         'ينتقل؛ والحرف المتحرك بالكاد.',
    t1bh='أسماء الحروف تتصادم',
    audioOnce='اضغط التشغيل حين تكون مستعدًا. حين ينتهي، يمكنك إعادته.',
    t1bb='<strong>A</strong> و<strong>E</strong>، <strong>E</strong> '
         'و<strong>I</strong>، <strong>G</strong> و<strong>J</strong>، '
         '<strong>M</strong> و<strong>N</strong>. أربعة أزواج، وهي معًا '
         'مسؤولة عن معظم الأجوبة المكتوبة خطأً في الورقة.',
    t1bn='<bdi>E</bdi> و<bdi>I</bdi> هما الأسوأ، لأنهما متبادلان بين '
         'الإنجليزية ومعظم اللغات الأوروبية. ما تعلّمته في المدرسة يعمل هنا '
         'ضدك فعليًا.',
    t1ch='ست لهجات، امتحان واحد',
    t1cb='الإنجليزية البريطانية والأمريكية والأسترالية والكندية والأيرلندية '
         'والنيوزيلندية كلها تظهر في أوراق حقيقية. التسجيلان هنا مركّبان من '
         'لقطات بلهجات مختلفة، فأنت تدرّب الأمور الثلاثة في وقت واحد.',
    t1cn='لا يمكنك أن تتعلم لهجة في درس واحد. لكن يمكنك أن تكفّ عن أن '
         'تفاجئك، وهذا معظم الفائدة.',
    numAudEyebrow='التدريب 1 &middot; التسجيل',
    numAudTitle='خمسة متكلمين، خمسة أرقام',
    numAudNote='لقطات قصيرة بخمس لهجات. انظر إلى الفراغات في الشرائح التالية، ثم '
               'اضغط التشغيل — هنا أو في الشريط أسفل تلك الشرائح. حين ينتهي يمكنك '
               'تشغيله من هنا مرة أخرى: هذا تدريب، لا الامتحان.',
    numEyebrow='التدريب 1 &middot; الأرقام',
    numTitle='اكتب رقمًا واحدًا في كل فراغ',
    numHint='اكتب أرقامًا، لا كلمات. اثنان من هذه يُقالان بطريقة نادرًا ما '
            'يتعلمها دارسو الإنجليزية.',
    spellAudEyebrow='التدريب 2 &middot; التسجيل',
    spellAudTitle='اسمان، يُتهجّى كل منهما مرة واحدة',
    spellAudNote='لقطتان، لهجتان. يُعطى كل اسم حرفًا حرفًا مرة واحدة بالضبط، بسرعة '
                 'الكلام، كما في الامتحان الحقيقي. انظر إلى الفراغات في الشريحة '
                 'التالية، ثم اضغط التشغيل.',
    spellEyebrow='التدريب 2 &middot; التهجئة',
    spellTitle='اكتب الاسم تمامًا كما تُهجّي',
    spellHint='التهجئة تُحتسب. أحد هذين يستعمل عُرف <bdi>"double"</bdi> نفسه كما '
              'في تدريب الأرقام.',
    sortEyebrow='التدريب 3 &middot; الأزواج التي تتصادم',
    sortTitle='أي أسماء الحروف تختلط فعلًا؟',
    sortHint='اسحب كل زوج إلى عمود — أو انقر على زوج، ثم على العمود الذي تريده '
             'فيه.',
    sortBin1='تتشابه في الصوت',
    sortBin2='نادرًا ما تختلط',
    mcEyebrow='التدريب 4 &middot; الأعراف',
    mcTitle='ماذا تفعل الإنجليزية هنا فعلًا؟',
    d1why='44. <em><bdi>Double</bdi></em> قبل رقم تعني اثنين منه، في الأرقام '
          'والحروف على السواء — ولهذا تعمل <em><bdi>double F</bdi></em> في '
          'اسم بالطريقة نفسها.',
    d2why='<bdi>Thirteen</bdi> و<bdi>thirty</bdi>. الحرفان المتحركان متقاربان '
          'والنبر هو ما يفصل بينهما، فبسرعة الكلام لا يسمع المرشح الذي يتوقع '
          'فرقًا في الحرف المتحرك شيئًا.',
    d3why='لأن الإنجليزية لغة عالمية والامتحان امتحان عالمي. ليست صعوبة '
          'لذاتها — فالمرشح سيلتقي كل هذه اللهجات في جامعة أو مكان عمل.',
    d4why='بقية الكلمة. الحرف المسموع منفردًا رمية عملة؛ أما الحرف داخل اسم '
          'تراه نصف رؤية فغالبًا ما يفرضه ما حوله.',
    actTitle='أملِ وتحقّق',
    actUse='استعمل ثلاثًا على الأقل:',
    actSpeakBrief='في أزواج، بالتناوب. أملِ على شريكك خمسة أشياء: اسم عائلة، رقم '
                  'هاتف، سعرًا، تاريخًا، ورقم غرفة. قل كل واحد مرة واحدة، بسرعة '
                  'عادية. ثم تبادلا الورقتين وصحّحاهما — كل حرف خاطئ علامة ضائعة، '
                  'تمامًا كما في الامتحان.',
    actSpeak1='استعمل <em><bdi>double</bdi></em> مرة واحدة على الأقل، في رقم وفي '
              'اسم.',
    actSpeak2='ضع في مجموعتك رقمًا واحدًا يحوي <bdi>thirteen</bdi> أو '
              '<bdi>thirty</bdi>، ولا تساعد.',
    actSpeak3='تهجَّ اسمًا يحوي اثنين من الأزواج المتصادمة — <bdi>A</bdi> '
              'و<bdi>E</bdi>، أو <bdi>M</bdi> و<bdi>N</bdi>.',
    actWriteKind='Writing · 80–120 كلمة',
    actWriteBrief='اكتب العناصر الخمسة التي أمليتها، بالأرقام والحروف، ثم اكتب بجانب '
                  'كل منها الخطأ الذي توقعت أن يقع فيه شريكك. تسمية الفخ مسبقًا هي ما '
                  'يمنعك من الوقوع فيه أنت.',
    actPlaceholder='Surname: … (expected mistake: A heard as R)',
    g1why='<bdi>"Double oh"</bdi> صفران: <bdi>004713</bdi>. المرشح الذي يعدّ '
          'ستة أرقام منفصلة لا يسمع ستة أبدًا.',
    g2why='<bdi>13.50</bdi>، ثم <bdi>"not thirty, thirteen"</bdi>: الزوج الذي '
          'يكلّف علامات أكثر من أي رقم آخر في الإنجليزية.',
    g3why='الرابع عشر. الأعداد الترتيبية تتداخل بسرعة الكلام — '
          '<bdi>fourteenth</bdi> و<bdi>fortieth</bdi> يخرجان متقاربين، وواحد '
          'منهما فقط تاريخ حقيقي.',
    g4why='<bdi>Eight eighty</bdi>. تقول الإنجليزية رقم الغرفة أزواجًا لا '
          'عددًا كاملًا، ولهذا فإن <bdi>"eight hundred and eighty"</bdi> هو '
          'ما يتوقعه الدارس ولا يسمعه أبدًا.',
    g5why='ثمانية عشر. عشرون هو السعر الكامل ويُقال أولًا؛ الفراغ يطلب سعر '
          'الحجز المبكر، فالرقم المرتبط بذلك الشرط هو ما يُكتب.',
    s1why='<bdi>Hargreaves</bdi>. الفخاخ هي الحروف المتحركة — <bdi>A</bdi>، '
          'ثم <bdi>E</bdi> و<bdi>A</bdi> معًا — التي يبدّلها الدارسون لأن '
          'ألفباءهم تسمّيها بأسماء أخرى، و<bdi>G</bdi> التي تُكتب بسهولة '
          '<bdi>J</bdi>.',
    s2why='<bdi>Ffion</bdi>، بحرف <bdi>F</bdi> مضاعف. حين يقول المتكلم '
          '<bdi>"double"</bdi> قبل حرف فهما حرفان — العُرف نفسه كما في '
          '<bdi>"double oh"</bdi> في رقم، ولهذا ينتمي التدريبان إلى درس واحد.',
    pairsWhy='الأربعة في عمود «تتشابه في الصوت» هي التي تتصادم فعلًا في أسماء '
             'الحروف الإنجليزية، وهي معًا مسؤولة عن معظم أجوبة القسم 1 المكتوبة '
             'خطأً. <strong>A</strong> الإنجليزية تُسمع كـ <bdi>E</bdi> في معظم '
             'الألفباءات الأوروبية، و<strong>E</strong> الإنجليزية كـ '
             '<bdi>I</bdi> عندهم، فيبدّل <bdi>A</bdi> و<bdi>E</bdi>، '
             'و<bdi>E</bdi> و<bdi>I</bdi>، كل من يسمع بألفبائه؛ '
             'و<strong>G</strong> و<strong>J</strong> يشتركان في الصوت الأول ولا '
             'يختلفان إلا في الحرف المتحرك؛ و<strong>M</strong> '
             'و<strong>N</strong> لا يختلفان إلا في الأنفي الأخير. أما '
             '<bdi>W</bdi> و<bdi>Y</bdi>، و<bdi>K</bdi> و<bdi>Q</bdi>، فلا '
             'يتشابهان في شيء حين يُقالان كاملين — ولهذا لا يخطئ فيهما أحد.',
)

# ── Chinese ─────────────────────────────────────────────────────────
T['zh'] = dict(
    coverTitle='数字、拼写<em>与口音</em>',
    coverSub='每个部分都会丢分的三件事，单独拿出来练',
    chipLevel='B2&ndash;C1',
    chipFocus='Listening &middot; 全部四个部分',
    chipCount='17 分',
    t1Eyebrow='开始之前',
    t1Title='这些不是听力问题，而是惯例问题。',
    t1ah='英语有自己说数字的方式',
    t1ab='<em>Double oh</em> 是两个零。<em>Oh</em> 是一个。房间号是 <em>eight '
         'eighty</em>，而不是 eight hundred and '
         'eighty。这些都不难听清——难的是<strong>预料到</strong>。',
    t1an='Thirteen 和 thirty 是这门语言里最费分的一对。重音移动了；元音几乎没动。',
    t1bh='字母名称会撞车',
    audioOnce='准备好了就按播放。结束后可以重放。',
    t1bb='<strong>A</strong> 和 <strong>E</strong>、<strong>E</strong> 和 '
         '<strong>I</strong>、<strong>G</strong> 和 '
         '<strong>J</strong>、<strong>M</strong> 和 '
         '<strong>N</strong>。四对字母，试卷上大多数拼错的答案都出在它们身上。',
    t1bn='E 和 I 最糟糕，因为在英语和大多数欧洲语言之间，这两个名称正好是对调的。你在学校学到的东西在这里会直接拖你后腿。',
    t1ch='六种口音，一场考试',
    t1cb='英国、美国、澳大利亚、加拿大、爱尔兰和新西兰英语都会出现在真题里。这里的两段录音由不同口音的片段拼成，所以你同时在练这三件事。',
    t1cn='一节课学不会一种口音。但你可以不再被它吓到，这就是大部分的收获。',
    numAudEyebrow='练习 1 &middot; 录音',
    numAudTitle='五位说话者，五个数字',
    numAudNote='五种口音的短片段。看一看接下来几页的空格，再按播放——在这里，或在那几页底部的播放栏。结束后可以从这里再放一遍：这是练习，不是考试。',
    numEyebrow='练习 1 &middot; 数字',
    numTitle='在每个空格里填写一个数字',
    numHint='写数字，不要写单词。其中两个的说法，英语学习者很少学过。',
    spellAudEyebrow='练习 2 &middot; 录音',
    spellAudTitle='两个名字，各拼读一次',
    spellAudNote='两段录音，两种口音。每个名字按正常语速逐字母拼读，恰好一次，和真实考试一样。看一看下一页的空格，再按播放。',
    spellEyebrow='练习 2 &middot; 拼写',
    spellTitle='按拼读原样写出名字',
    spellHint='拼写计分。其中一个用到了和数字练习相同的 "double" 惯例。',
    sortEyebrow='练习 3 &middot; 会撞车的字母对',
    sortTitle='哪些字母名称真的会被混淆？',
    sortHint='把每一对拖进一栏——或者先点一对，再点你想放的那一栏。',
    sortBin1='听起来相似',
    sortBin2='很少混淆',
    mcEyebrow='练习 4 &middot; 惯例',
    mcTitle='英语在这里到底怎么做？',
    d1why='44。数字前的 <em>double</em> 表示两个，数字和字母都一样——所以名字里的 <em>double F</em> '
          '也是同样的用法。',
    d2why='Thirteen 和 thirty。元音很接近，区分它们的是重音，所以按正常语速，一个等着听出元音差别的考生什么也听不出来。',
    d3why='因为英语是国际语言，而这是一场国际考试。这不是为难而为难——考生在大学或职场会遇到所有这些口音。',
    d4why='单词的其余部分。单独听一个字母是掷硬币；而一个名字你已经看出一半，里面的字母通常由周围的字母决定。',
    actTitle='听写并核对',
    actUse='至少使用三个：',
    actSpeakBrief='两人一组，轮流进行。向搭档听写五项：一个姓氏、一个电话号码、一个价格、一个日期和一个房间号。每项只说一次，正常语速。然后交换纸张互相批改——每个错字都是一分丢失，和考试完全一样。',
    actSpeak1='至少用一次 <em>double</em>，一次在数字里，一次在名字里。',
    actSpeak2='在你的那组里放一个含有 thirteen 或 thirty 的数字，而且不要帮忙。',
    actSpeak3='拼读一个含有两对易混字母的名字——一个 A 和一个 E，或者一个 M 和一个 N。',
    actWriteKind='Writing · 80–120 词',
    actWriteBrief='用数字和字母写出你听写的五项，然后在每项旁边写下你预料搭档会犯的错误。提前说出陷阱在哪里，正是让你自己不掉进去的办法。',
    actPlaceholder='Surname: … (expected mistake: A heard as R)',
    g1why='"Double oh" 是两个零：004713。一个数着六个独立数字的考生，永远听不到六个。',
    g2why='13.50，然后是 "not thirty, thirteen"：这一对比英语里任何其他数字都更费分。',
    g3why='十四号。序数词在正常语速下会粘在一起——fourteenth 和 fortieth 听起来很接近，而其中只有一个是真实的日期。',
    g4why='Eight eighty。英语说房间号是成对说的，而不是说成一个整数，所以 "eight hundred and eighty" '
          '是学习者预料会听到、却永远听不到的说法。',
    g5why='十八。二十是全价，而且先说出来；空格问的是早订价，所以要写的是和那个条件绑在一起的数字。',
    s1why='Hargreaves。陷阱在元音——一个 A，然后 E 和 A '
          '连在一起——学习者会调换它们，因为自己语言的字母表给它们起了不同的名字；还有 G，很容易被写成 J。',
    s2why='Ffion，两个 F。说话者在字母前说 "double"，意思就是两个——和数字里的 "double oh" '
          '是同一个惯例，所以这两项练习属于同一节课。',
    pairsWhy='"听起来相似" 一栏的四对，是英语字母名称里真正会撞车的，第 1 部分大多数拼错的答案都出在它们身上。英语的 '
             '<strong>A</strong> 听起来像大多数欧洲字母表的 E，英语的 <strong>E</strong> 听起来像它们的 '
             'I，所以任何用自己字母表去听的人都会把 A 和 E、E 和 I 调换；<strong>G</strong> 和 '
             '<strong>J</strong> 开头的音相同，只有元音不同；<strong>M</strong> 和 '
             '<strong>N</strong> 只有结尾的鼻音不同。W 和 Y、K 和 Q 完整说出来时毫不相似——所以没人会听错。',
)

# ── Japanese ────────────────────────────────────────────────────────
T['ja'] = dict(
    coverTitle='数字、スペリング、<em>そしてアクセント</em>',
    coverSub='どのセクションでも点を失う三つのこと、それだけを取り出して練習します',
    chipLevel='B2&ndash;C1',
    chipFocus='Listening &middot; 四つのセクションすべて',
    chipCount='17 点',
    t1Eyebrow='始める前に',
    t1Title='これはリスニングの問題ではありません。慣習の問題です。',
    t1ah='英語は数字を独自の言い方で言う',
    t1ab='<em>Double oh</em> はゼロが二つ。<em>Oh</em> は一つ。部屋番号は <em>eight '
         'eighty</em> で、eight hundred and eighty '
         'ではありません。どれも聞き取りにくいわけではありません。<strong>予期する</strong>のが難しいのです。',
    t1an='Thirteen と thirty は、この言語で最も高くつく一対です。強勢は動き、母音はほとんど動きません。',
    t1bh='文字の名前がぶつかる',
    audioOnce='準備ができたら再生を押してください。終わったら、もう一度聞けます。',
    t1bb='<strong>A</strong> と <strong>E</strong>、<strong>E</strong> と '
         '<strong>I</strong>、<strong>G</strong> と '
         '<strong>J</strong>、<strong>M</strong> と '
         '<strong>N</strong>。四つの組で、答案のスペルミスの大半はこれらから生じます。',
    t1bn='E と I '
         'が最悪です。英語と多くのヨーロッパ言語の間で、この二つの名前は入れ替わっているからです。学校で教わったことが、ここでは積極的にあなたの邪魔をします。',
    t1ch='六つのアクセント、一つの試験',
    t1cb='イギリス、アメリカ、オーストラリア、カナダ、アイルランド、ニュージーランドの英語がすべて実際の試験に登場します。ここにある二つの録音は異なるアクセントのテイクから作られているので、三つのことを同時に練習できます。',
    t1cn='アクセントは一回のレッスンでは身につきません。けれども、驚かされなくなることはできます。それが得られるものの大半です。',
    numAudEyebrow='ドリル 1 &middot; 録音',
    numAudTitle='五人の話者、五つの数字',
    numAudNote='五つのアクセントによる短いテイクです。次のスライドの空所を見てから、再生を押してください。ここでも、それらのスライドの下部のバーでも押せます。終わったら、ここからもう一度再生できます。これはドリルであって、試験ではありません。',
    numEyebrow='ドリル 1 &middot; 数字',
    numTitle='各空所に数字を一つ書きなさい',
    numHint='単語ではなく数字で書きましょう。このうち二つは、英語学習者がほとんど教わらない言い方で言われます。',
    spellAudEyebrow='ドリル 2 &middot; 録音',
    spellAudTitle='二つの名前、それぞれ一度だけスペルを読み上げます',
    spellAudNote='二つのテイク、二つのアクセント。各名前は本番の試験と同じく、話す速さで一文字ずつ、ちょうど一度だけ読み上げられます。次のスライドの空所を見てから、再生を押してください。',
    spellEyebrow='ドリル 2 &middot; スペリング',
    spellTitle='読み上げられたとおりに名前を書きなさい',
    spellHint='スペリングは採点されます。このうち一つは、数字のドリルと同じ "double" の慣習を使います。',
    sortEyebrow='ドリル 3 &middot; ぶつかる組',
    sortTitle='実際に混同される文字の名前はどれ？',
    sortHint='各組を列にドラッグしてください。または組をクリックしてから、入れたい列をクリックします。',
    sortBin1='似て聞こえる',
    sortBin2='めったに混同しない',
    mcEyebrow='ドリル 4 &middot; 慣習',
    mcTitle='英語はここで実際にどうするのか？',
    d1why='44。数字の前の <em>double</em> はそれが二つという意味で、数字でも文字でも同じです。だから名前の中の '
          '<em>double F</em> も同じように働きます。',
    d2why='Thirteen と '
          'thirty。母音は近く、二つを分けるのは強勢です。だから話す速さでは、母音の違いを待っている受験者には何も聞こえません。',
    d3why='英語が国際語で、この試験が国際試験だからです。難しさのための難しさではありません。受験者は大学や職場でこれらすべてに出会います。',
    d4why='単語の残りの部分です。単独で聞いた文字はコイン投げですが、半ば見えている名前の中の文字は、たいてい周りの文字によって決まります。',
    actTitle='書き取らせて確認する',
    actUse='少なくとも三つ使いましょう：',
    actSpeakBrief='ペアで、交代しながら。相手に五つのことを書き取らせます。姓、電話番号、値段、日付、部屋番号です。それぞれ一度だけ、普通の速さで言います。そのあと用紙を交換して採点しましょう。試験とまったく同じく、間違った文字一つごとに一点を失います。',
    actSpeak1='<em>double</em> を少なくとも一度、数字の中と名前の中で使いましょう。',
    actSpeak2='自分のセットに thirteen か thirty を含む数字を一つ入れ、助けないでください。',
    actSpeak3='ぶつかる組のうち二つを含む名前のスペルを読み上げましょう。A と E、または M と N です。',
    actWriteKind='Writing · 80–120 語',
    actWriteBrief='書き取らせた五つの項目を数字と文字で書き出し、それぞれの横に、相手がすると予想した間違いを書きましょう。罠にあらかじめ名前をつけることが、自分がそこに落ちないための方法です。',
    actPlaceholder='Surname: … (expected mistake: A heard as R)',
    g1why='"Double oh" はゼロが二つ：004713。六つの別々の数字を数えている受験者には、六つは決して聞こえません。',
    g2why='13.50、そして "not thirty, thirteen"。英語の他のどんな数字よりも多くの点を失わせる一対です。',
    g3why='十四日。序数は速く言うとつながってしまいます。fourteenth と fortieth '
          'は近く聞こえ、本物の日付はそのうち一つだけです。',
    g4why='Eight eighty。英語では部屋番号を一つの数としてではなく二つずつ言います。だから "eight hundred and '
          'eighty" は学習者が予期しながら決して聞くことのない言い方なのです。',
    g5why='十八。二十は正規の値段で、先に言われます。空所が求めているのは早期予約の値段なので、その条件に結びついた数字を書きます。',
    s1why='Hargreaves。罠は母音です。A、そして E と A '
          'が続きます。学習者は自分の文字の名前が違うためにこれらを入れ替えてしまいます。そして G は J と書きやすい文字です。',
    s2why='Ffion、F が二つ。話者が文字の前に "double" と言えばそれが二つという意味で、数字の "double oh" '
          'と同じ慣習です。だからこの二つのドリルは一つのレッスンに入っています。',
    pairsWhy='"似て聞こえる" の列の四組が、英語の文字の名前で実際にぶつかるものです。セクション 1 '
             'のスペルミスの大半はこれらから生じます。英語の <strong>A</strong> は多くのヨーロッパ言語のアルファベットの E '
             'のように、英語の <strong>E</strong> はそれらの I のように聞こえます。だから自分のアルファベットで聞く人は A '
             'と E、E と I を入れ替えてしまいます。<strong>G</strong> と <strong>J</strong> '
             'は出だしの音が同じで母音だけが違い、<strong>M</strong> と <strong>N</strong> '
             'は最後の鼻音だけが違います。W と Y、K と Q は、きちんと言えば少しも似ていません。だから誰も聞き間違えないのです。',
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
