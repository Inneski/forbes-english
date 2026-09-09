# -*- coding: utf-8 -*-
"""Interface strings for The Square — 44 words (A2).

English, German and Spanish, the minimum since 2026-09-04.

Teach cards use the six-item form, but with a twist that suits a vocabulary
deck rather than a grammar one: only the **body** carries a key. The card
heading is the English word itself and the note is an English example, so
both are passed with `None` for their key and never translate. That is
HOUSE-STYLE §8's scope boundary applied literally — the learner needs the
*definition* in their own language and the *word* in English, and a deck that
translates the headword has nothing left to teach.

The builder reads its English from T['en'] rather than repeating it as
literals, so the two cannot drift.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME
from i18n_square_extra import EXTRA, TAIL_EXTRA
from i18n_square_q import Q, M_DEFS          # noqa: F401  (M_DEFS: builder)

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

# The template's RPG ledger chrome. This deck has no ledger, but the markup
# that reads these keys ships in every page, and the I18N gate fails a page
# whose data-i18n has no English behind it.
TAIL = {
    'en': {'ledClues': "'Clues'", 'ledDp': "'DP'", 'ledTime': "'Time'"},
    'de': {'ledClues': "'Hinweise'", 'ledDp': "'DP'", 'ledTime': "'Zeit'"},
    'es': {'ledClues': "'Pistas'", 'ledDp': "'DP'", 'ledTime': "'Tiempo'"},
}

T = {}

# ══════════════════════════════════════════════════════════════════════
#  ENGLISH
# ══════════════════════════════════════════════════════════════════════
T['en'] = dict(
    coverTitle='The <em>Square</em>',
    coverSub='Forty-four words, one blocky afternoon',
    chipLevel='A2 · Elementary', chipFocus='Vocabulary', chipCount='24 slides',
    bankLabel='Word bank:',

    # ── stage eyebrows ────────────────────────────────────────────────
    e1='Things in the square',
    e2='Things people do',
    e3='Ideas, feelings, small words',
    e4='Practice',

    # ── teaching slides ───────────────────────────────────────────────
    s1t='Inside a building',
    s1ab='An opening in a wall, with glass in it. Light comes in; you look out.',
    s1bb='You open it to go into a room, a building or a car.',
    s1cb='The room where you wash.',
    s1db='A small, thick cloth on the floor. A carpet covers the whole floor; '
         'a rug does not.',

    s2t='In your bag',
    s2ab='A soft container, open at the top, for carrying things.',
    s2bb='A small bag sewn into your clothes.',
    s2cb='Flat, round money made of metal.',
    s2db='A lens with a handle. It makes small things look big.',

    s3t='To read, to play, to do',
    s3ab='A thin book with many pictures. It comes out every week or month.',
    s3bb="Big sheets of paper with today's news. It comes out every day.",
    s3cb='Games you play on a board, moving pieces — chess, for example.',
    s3db='School work you do at home. No plural: never <em>homeworks</em>.',

    s4t='On you, and on the table',
    s4ab='What you wear: trousers, dresses, jackets. Always plural.',
    s4bb='Short trousers a man wears to swim. Plural too.',
    s4cb='Bread made brown and hot. Say <em>a piece of toast</em>, not '
         '<em>a toast</em>.',
    s4db='A person you know and like.',

    s5t='What your hands do',
    s5ab='Move something away from you.',
    s5bb='Move something towards you.',
    s5cb='Put your arm out to touch or take something.',
    s5db='Bring your hand, or a bat, hard against something.',

    s6t='Hands, and where you go',
    s6ab='Mark a surface with something sharp.',
    s6bb='Put parts together: a house, a wall, a machine.',
    s6cb='Put things together to create something. Wider than <em>build</em> — '
         'you make a cake, but you build a house.',
    s6db='Move on your feet, one foot always on the ground.',

    s7t='Sound, direction, mind',
    s7ab='Push air through your lips and make a high, clear sound.',
    s7bb='Move on to a new point — a new subject, or a new direction.',
    s7cb='Have an opinion or an idea about something.',
    s7db='Have the information in your head already.',

    s8t='Starting, leaving, finishing',
    s8ab='When something begins to happen.',
    s8bb='Bring a job to an end. Complete it.',
    s8cb='Leave people who still need you. The verb is de-<em>SERT</em>; the '
         'dry, sandy <em>DE</em>-sert is the noun.',
    s8db='Something that happens, usually planned and important.',

    s9t='True, false, bad',
    s9ab='In agreement with the facts.',
    s9bb='Not true.',
    s9cb='Of poor quality, or of a low standard.',
    s9db='A man who does not follow the rules — often said with a smile.',

    s10t='Feelings, and how much',
    s10ab='Very annoyed. Mad.',
    s10bb='Of great value or effect. It matters.',
    s10cb='To a high degree. It makes an adjective stronger.',
    s10db='Occasionally — not all of the time.',

    s11t='The four smallest words',
    s11ab='Use it the first time you name something.',
    s11bb='Inside something, or surrounded by it.',
    s11cb='Two or more people or things you have already named.',
    s11db='An informal hello — and an informal goodbye. Italian, and English '
          'borrowed it.',

    # ── questions ─────────────────────────────────────────────────────
    q1t='Her arm went out',
    q2t='He walked away',
    q3t='One word, no plural',
    q4t='Every day, or every month?',

    g1t='In the square',
    g2t='Not every day',
    gapHint='Type one word in each space.',

    matchT='Word and meaning',
    matchHint='Click a word, then click what it means.',
    matchWhy='Four verbs and one noun, all of them things you can see happening '
             'in the square.',

    sortT='A thing, or an action?',
    sortHint='Drop each word into the right box.',
    sortWhy='A thing is a noun — you can put <em>a</em> or <em>the</em> in front '
            'of it. An action is a verb — you can put <em>I</em> in front of it.',

    orderT='Build the sentence',
    orderHint='Click the parts in the right order.',
    orderWhy='<em>Sometimes</em> can open a sentence. Then what you do, then why '
             'you do it, then when.',

    searchT='Find it before the clock stops',
    searchStem='Find the magnifying glass.',
    searchWhy='A <em>magnifying glass</em> is a round lens with a handle. The '
              'coin is round too, but it has no handle.',

    # ── results ───────────────────────────────────────────────────────
    resPerfect='Full marks. Forty-four words, and none of them slipped.',
    resStrong='Strong. Go back to the two gap-fill slides — that is usually '
              'where the last point goes.',
    resMid='A good half. Read the four noun slides again, then try once more.',
    resLow='Start again from the beginning and read each card out loud before '
           'you answer. These are words you meet every day.',

    # ── activation ────────────────────────────────────────────────────
    actTitle='Now use them',
    actUse='Use at least five:',
    actSpeakBrief='In pairs. Do not read the cards — say it.',
    actSpeak1='Look at the picture on the cover. Tell your partner five things '
              'you can see. Say <em>a</em> the first time and <em>the</em> after '
              'that.',
    actSpeak2='Your partner has a bag. Ask what is in it. Answer with three of '
              "today's words, and one thing that is not true.",
    actSpeak3='Tell your partner about your Sunday: what you sometimes do, what '
              'you finish before Monday, and one thing that makes you angry.',
    actWriteKind='Writing · homework',
    actWriteBrief='Your friend missed the event in the square on Saturday. Write '
                  'them a message: what started, what you saw, what you did, and '
                  'why you had to finish early. 120–150 words.',
    actPlaceholder='Ciao! You missed a good day…',
)

# ══════════════════════════════════════════════════════════════════════
#  GERMAN
# ══════════════════════════════════════════════════════════════════════
T['de'] = dict(
    coverTitle='The <em>Square</em>',
    coverSub='Vierundvierzig Wörter, ein Nachmittag aus Klötzchen',
    chipLevel='A2 · Grundstufe', chipFocus='Wortschatz', chipCount='24 Folien',
    bankLabel='Wortspeicher:',

    e1='Dinge auf dem Platz',
    e2='Was Menschen tun',
    e3='Ideen, Gefühle, kleine Wörter',
    e4='Übung',

    s1t='Im Gebäude',
    s1ab='Eine Öffnung in der Wand, mit Glas darin. Licht kommt herein; du '
         'schaust hinaus.',
    s1bb='Du öffnest sie, um in ein Zimmer, ein Gebäude oder ein Auto zu gehen.',
    s1cb='Der Raum, in dem man sich wäscht.',
    s1db='Ein kleines, dickes Tuch auf dem Boden. Ein Teppichboden bedeckt den '
         'ganzen Boden, ein <em>rug</em> nicht.',

    s2t='In deiner Tasche',
    s2ab='Ein weicher Behälter, oben offen, zum Tragen von Dingen.',
    s2bb='Eine kleine Tasche, die in die Kleidung eingenäht ist.',
    s2cb='Flaches, rundes Geld aus Metall.',
    s2db='Eine Linse mit Griff. Sie lässt kleine Dinge groß aussehen.',

    s3t='Lesen, spielen, erledigen',
    s3ab='Ein dünnes Heft mit vielen Bildern. Es erscheint jede Woche oder '
         'jeden Monat.',
    s3bb='Große Papierbögen mit den Nachrichten von heute. Erscheint täglich.',
    s3cb='Spiele auf einem Brett, bei denen man Figuren zieht — Schach zum '
         'Beispiel.',
    s3db='Schularbeit, die du zu Hause machst. Kein Plural: nie '
         '<em>homeworks</em>.',

    s4t='An dir und auf dem Tisch',
    s4ab='Was du trägst: Hosen, Kleider, Jacken. Immer Plural.',
    s4bb='Kurze Hose, die ein Mann zum Schwimmen trägt. Auch Plural.',
    s4cb='Brot, braun und heiß gemacht. Man sagt <em>a piece of toast</em>, '
         'nicht <em>a toast</em>.',
    s4db='Eine Person, die du kennst und magst.',

    s5t='Was deine Hände tun',
    s5ab='Etwas von dir weg bewegen.',
    s5bb='Etwas zu dir hin bewegen.',
    s5cb='Den Arm ausstrecken, um etwas zu berühren oder zu nehmen.',
    s5db='Die Hand oder einen Schläger hart gegen etwas führen.',

    s6t='Hände, und wohin du gehst',
    s6ab='Eine Oberfläche mit etwas Spitzem markieren.',
    s6bb='Teile zusammensetzen: ein Haus, eine Mauer, eine Maschine.',
    s6cb='Dinge zusammensetzen und etwas herstellen. Weiter als <em>build</em> — '
         'einen Kuchen macht man, ein Haus baut man.',
    s6db='Sich auf den Füßen fortbewegen, ein Fuß immer am Boden.',

    s7t='Klang, Richtung, Kopf',
    s7ab='Luft durch die Lippen pressen und einen hohen, klaren Ton machen.',
    s7bb='Zu einem neuen Punkt übergehen — ein neues Thema oder eine neue '
         'Richtung.',
    s7cb='Eine Meinung oder eine Idee zu etwas haben.',
    s7db='Die Information bereits im Kopf haben.',

    s8t='Anfangen, verlassen, beenden',
    s8ab='Wenn etwas zu geschehen beginnt.',
    s8bb='Eine Aufgabe zu Ende bringen. Sie abschließen.',
    s8cb='Menschen verlassen, die dich noch brauchen. Das Verb ist '
         'de-<em>SERT</em>; die trockene <em>DE</em>-sert ist das Nomen.',
    s8db='Etwas, das geschieht, meist geplant und wichtig.',

    s9t='Wahr, falsch, schlecht',
    s9ab='In Übereinstimmung mit den Tatsachen.',
    s9bb='Nicht wahr.',
    s9cb='Von schlechter Qualität oder niedrigem Niveau.',
    s9db='Ein Mann, der sich nicht an die Regeln hält — oft mit einem Lächeln '
         'gesagt.',

    s10t='Gefühle, und wie sehr',
    s10ab='Sehr verärgert. Wütend.',
    s10bb='Von großem Wert oder großer Wirkung. Es zählt.',
    s10cb='In hohem Maße. Es verstärkt ein Adjektiv.',
    s10db='Gelegentlich — nicht die ganze Zeit.',

    s11t='Die vier kleinsten Wörter',
    s11ab='Benutze es, wenn du etwas zum ersten Mal nennst.',
    s11bb='In etwas drin oder davon umgeben.',
    s11cb='Zwei oder mehr Personen oder Dinge, die du schon genannt hast.',
    s11db='Ein lockeres Hallo — und ein lockeres Tschüss. Italienisch, und das '
          'Englische hat es übernommen.',

    q1t='Ihr Arm ging vor',
    q2t='Er ging einfach weg',
    q3t='Ein Wort, kein Plural',
    q4t='Jeden Tag oder jeden Monat?',

    g1t='Auf dem Platz',
    g2t='Nicht jeden Tag',
    gapHint='Schreibe ein Wort in jede Lücke.',

    matchT='Wort und Bedeutung',
    matchHint='Klicke ein Wort an, dann seine Bedeutung.',
    matchWhy='Vier Verben und ein Nomen — alles Dinge, die man auf dem Platz '
             'sehen kann.',

    sortT='Ein Ding oder eine Handlung?',
    sortHint='Ziehe jedes Wort in das richtige Feld.',
    sortWhy='Ein Ding ist ein Nomen — man kann <em>a</em> oder <em>the</em> '
            'davorsetzen. Eine Handlung ist ein Verb — man kann <em>I</em> '
            'davorsetzen.',

    orderT='Bau den Satz',
    orderHint='Klicke die Teile in der richtigen Reihenfolge an.',
    orderWhy='<em>Sometimes</em> darf am Satzanfang stehen. Dann was du tust, '
             'dann warum, dann wann.',

    searchT='Finde es, bevor die Uhr abläuft',
    searchStem='Finde die <em>magnifying glass</em>.',
    searchWhy='Eine <em>magnifying glass</em> ist eine runde Linse mit Griff. '
              'Die Münze ist auch rund, hat aber keinen Griff.',

    resPerfect='Volle Punktzahl. Vierundvierzig Wörter, und keins ist '
               'durchgerutscht.',
    resStrong='Stark. Geh noch einmal zu den beiden Lückentexten — dort geht '
              'der letzte Punkt meist verloren.',
    resMid='Gut die Hälfte. Lies die vier Nomen-Folien noch einmal und '
           'versuch es dann erneut.',
    resLow='Fang von vorne an und lies jede Karte laut vor, bevor du '
           'antwortest. Das sind Wörter, die dir täglich begegnen.',

    actTitle='Jetzt anwenden',
    actUse='Benutze mindestens fünf:',
    actSpeakBrief='Zu zweit. Nicht ablesen — sprechen.',
    actSpeak1='Schaut euch das Bild auf dem Cover an. Nenne deiner Partnerin '
              'oder deinem Partner fünf Dinge, die du siehst. Sag beim ersten '
              'Mal <em>a</em> und danach <em>the</em>.',
    actSpeak2='Dein Gegenüber hat eine Tasche. Frag, was darin ist. Antworte '
              'mit drei Wörtern von heute und einer Sache, die nicht stimmt.',
    actSpeak3='Erzähl von deinem Sonntag: was du manchmal machst, was du vor '
              'Montag fertig hast, und eine Sache, die dich wütend macht.',
    actWriteKind='Schreiben · Hausaufgabe',
    actWriteBrief='Dein Freund hat das Ereignis auf dem Platz am Samstag '
                  'verpasst. Schreib ihm eine Nachricht: was angefangen hat, '
                  'was du gesehen hast, was du gemacht hast und warum du früh '
                  'aufhören musstest. 120–150 Wörter.',
    actPlaceholder='Ciao! You missed a good day…',
)

# ══════════════════════════════════════════════════════════════════════
#  SPANISH
# ══════════════════════════════════════════════════════════════════════
T['es'] = dict(
    coverTitle='The <em>Square</em>',
    coverSub='Cuarenta y cuatro palabras, una tarde de bloques',
    chipLevel='A2 · Elemental', chipFocus='Vocabulario', chipCount='24 diapositivas',
    bankLabel='Banco de palabras:',

    e1='Cosas de la plaza',
    e2='Lo que hace la gente',
    e3='Ideas, sentimientos, palabras pequeñas',
    e4='Práctica',

    s1t='Dentro de un edificio',
    s1ab='Una abertura en la pared, con cristal. Entra la luz; tú miras hacia '
         'fuera.',
    s1bb='La abres para entrar en una habitación, un edificio o un coche.',
    s1cb='La habitación donde te lavas.',
    s1db='Una tela pequeña y gruesa sobre el suelo. La moqueta cubre todo el '
         'suelo; un <em>rug</em> no.',

    s2t='En tu bolsa',
    s2ab='Un recipiente blando, abierto por arriba, para llevar cosas.',
    s2bb='Una bolsa pequeña cosida a la ropa.',
    s2cb='Dinero plano y redondo, hecho de metal.',
    s2db='Una lente con mango. Hace que las cosas pequeñas se vean grandes.',

    s3t='Leer, jugar, hacer',
    s3ab='Un cuadernillo con muchas fotos. Sale cada semana o cada mes.',
    s3bb='Hojas grandes de papel con las noticias de hoy. Sale cada día.',
    s3cb='Juegos que se juegan sobre un tablero, moviendo piezas — el ajedrez, '
         'por ejemplo.',
    s3db='Trabajo del colegio que haces en casa. Sin plural: nunca '
         '<em>homeworks</em>.',

    s4t='Encima de ti, y en la mesa',
    s4ab='Lo que llevas puesto: pantalones, vestidos, chaquetas. Siempre en '
         'plural.',
    s4bb='Pantalón corto que un hombre lleva para nadar. También plural.',
    s4cb='Pan puesto caliente y dorado. Se dice <em>a piece of toast</em>, no '
         '<em>a toast</em>.',
    s4db='Una persona a la que conoces y aprecias.',

    s5t='Lo que hacen tus manos',
    s5ab='Mover algo lejos de ti.',
    s5bb='Mover algo hacia ti.',
    s5cb='Estirar el brazo para tocar o coger algo.',
    s5db='Llevar la mano, o un bate, con fuerza contra algo.',

    s6t='Manos, y adónde vas',
    s6ab='Marcar una superficie con algo puntiagudo.',
    s6bb='Unir piezas: una casa, un muro, una máquina.',
    s6cb='Juntar cosas para crear algo. Más amplio que <em>build</em> — un '
         'pastel se hace, una casa se construye.',
    s6db='Moverte con los pies, siempre uno en el suelo.',

    s7t='Sonido, dirección, cabeza',
    s7ab='Soplar aire entre los labios y hacer un sonido agudo y claro.',
    s7bb='Pasar a un punto nuevo — un tema nuevo o una dirección nueva.',
    s7cb='Tener una opinión o una idea sobre algo.',
    s7db='Tener ya la información en la cabeza.',

    s8t='Empezar, abandonar, terminar',
    s8ab='Cuando algo empieza a ocurrir.',
    s8bb='Llevar una tarea a su fin. Completarla.',
    s8cb='Dejar a gente que todavía te necesita. El verbo es de-<em>SERT</em>; '
         'el <em>DE</em>-sert seco y arenoso es el sustantivo.',
    s8db='Algo que ocurre, normalmente planeado e importante.',

    s9t='Verdadero, falso, malo',
    s9ab='De acuerdo con los hechos.',
    s9bb='No verdadero.',
    s9cb='De mala calidad o de nivel bajo.',
    s9db='Un hombre que no sigue las reglas — se dice a menudo con una sonrisa.',

    s10t='Sentimientos, y cuánto',
    s10ab='Muy molesto. Enfadado.',
    s10bb='De gran valor o efecto. Importa.',
    s10cb='En alto grado. Refuerza un adjetivo.',
    s10db='De vez en cuando — no todo el tiempo.',

    s11t='Las cuatro palabras más pequeñas',
    s11ab='Úsalo la primera vez que nombras algo.',
    s11bb='Dentro de algo, o rodeado por ello.',
    s11cb='Dos o más personas o cosas que ya has nombrado.',
    s11db='Un hola informal — y un adiós informal. Es italiano, y el inglés lo '
          'ha tomado prestado.',

    q1t='Su brazo se estiró',
    q2t='Se marchó sin más',
    q3t='Una palabra, sin plural',
    q4t='¿Cada día o cada mes?',

    g1t='En la plaza',
    g2t='No todos los días',
    gapHint='Escribe una palabra en cada hueco.',

    matchT='Palabra y significado',
    matchHint='Haz clic en una palabra y luego en lo que significa.',
    matchWhy='Cuatro verbos y un sustantivo, todos ellos cosas que se pueden ver '
             'en la plaza.',

    sortT='¿Una cosa o una acción?',
    sortHint='Coloca cada palabra en la casilla correcta.',
    sortWhy='Una cosa es un sustantivo — puedes poner <em>a</em> o <em>the</em> '
            'delante. Una acción es un verbo — puedes poner <em>I</em> delante.',

    orderT='Construye la frase',
    orderHint='Haz clic en las partes en el orden correcto.',
    orderWhy='<em>Sometimes</em> puede abrir la frase. Después lo que haces, '
             'luego para qué, y al final cuándo.',

    searchT='Encuéntralo antes de que pare el reloj',
    searchStem='Encuentra la <em>magnifying glass</em>.',
    searchWhy='Una <em>magnifying glass</em> es una lente redonda con mango. La '
              'moneda también es redonda, pero no tiene mango.',

    resPerfect='Puntuación perfecta. Cuarenta y cuatro palabras, y no se te ha '
               'escapado ninguna.',
    resStrong='Muy bien. Vuelve a las dos diapositivas de huecos — ahí suele '
              'irse el último punto.',
    resMid='Media buena. Lee otra vez las cuatro diapositivas de sustantivos y '
           'vuelve a intentarlo.',
    resLow='Empieza de nuevo y lee cada tarjeta en voz alta antes de responder. '
           'Son palabras que aparecen todos los días.',

    actTitle='Ahora úsalas',
    actUse='Usa al menos cinco:',
    actSpeakBrief='En parejas. No leas las tarjetas — dilo.',
    actSpeak1='Mirad la imagen de la portada. Dile a tu compañero cinco cosas '
              'que ves. Di <em>a</em> la primera vez y <em>the</em> después.',
    actSpeak2='Tu compañero lleva una bolsa. Pregúntale qué hay dentro. '
              'Responde con tres palabras de hoy y una cosa que no sea verdad.',
    actSpeak3='Cuéntale tu domingo: qué haces a veces, qué terminas antes del '
              'lunes y una cosa que te pone furioso.',
    actWriteKind='Escritura · deberes',
    actWriteBrief='Tu amigo se perdió el evento de la plaza el sábado. Escríbele '
                  'un mensaje: qué empezó, qué viste, qué hiciste y por qué '
                  'tuviste que terminar pronto. 120–150 palabras.',
    actPlaceholder='Ciao! You missed a good day…',
)


T.update(EXTRA)
TAIL.update(TAIL_EXTRA)
for _c, _q in Q.items():                    # the question side, all ten
    T[_c].update(_q)


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
        print('%-3s %3d keys' % (c, len(d)),
              ('MISSING %s' % sorted(m)) if m else 'ok',
              ('EXTRA %s' % sorted(x)) if x else '')
