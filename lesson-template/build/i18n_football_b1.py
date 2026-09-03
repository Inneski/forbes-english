# -*- coding: utf-8 -*-
"""Interface strings for Football Vocabulary (B1) — English, German, Spanish.

Spanish is here rather than left at `{}` because the lesson it replaces
carried a Spanish gloss on every single item. Dropping that to ship the
minimum en+de would have thrown away the one piece of L1 support the
original had.

Per house style §8 the English being taught never translates: stems,
options and the vocabulary chips stay English in all three builds. What
translates is the chrome, the teaching prose and the task instructions —
and, in `es`, the per-item gloss the old page carried.
"""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Football <em>English</em>',
    coverSub='Positions, fouls, set pieces and the words commentators actually use',
    chipLevel='B1 · Intermediate', chipFocus='Match-day vocabulary',
    chipCount='20 slides',

    whoEyebrow='Before the questions', whoTitle='Who is who on the pitch',
    who1h='The officials',
    who1b='The <strong>referee</strong> runs the match and blows the whistle. '
          'The <strong>linesman</strong> (or assistant referee) watches the lines '
          'and raises a flag for offside.',
    who1n='One referee, two linesmen. Only the referee can stop play.',
    who2h='The outfield',
    who2b='A <strong>defender</strong> stops attacks, a <strong>midfielder</strong> '
          'links defence and attack, a <strong>winger</strong> plays wide, and a '
          '<strong>striker</strong> plays furthest forward.',
    who2n='<em>Forward</em> and <em>striker</em> overlap; the striker is the one nearest goal.',
    who3h='The goal, and the bench',
    who3b='The <strong>goalkeeper</strong> is the only player allowed to use their '
          'hands. The <strong>coach</strong> (or manager) picks the team and makes '
          'the changes from the bench.',
    who3n='British commentary usually says <em>manager</em>; <em>coach</em> is understood everywhere.',

    stopEyebrow='The whistle', stopTitle='What stops play, and what restarts it',
    st1h='Stopped for an offence',
    st1b='A <strong>foul</strong> is an illegal action on an opponent. A '
         '<strong>yellow card</strong> is a warning; a <strong>red card</strong> '
         'sends the player off for good.',
    st1n='Two yellows in one match make a red. The team plays on with ten.',
    st2h='Stopped for offside',
    st2b='A player is <strong>offside</strong> if they are nearer the opponents&rsquo; '
         'goal line than both the ball and the second-last defender when the ball '
         'is played to them.',
    st2n='Offside is a position, not an action — you are <em>in</em> an offside position.',
    st3h='Restarting play',
    st3b='Over the touchline → <strong>throw-in</strong>. Over the goal line off an '
         'attacker → <strong>goal kick</strong>. Off a defender → <strong>corner</strong>. '
         'A foul in the box → <strong>penalty</strong>.',
    st3n='Which restart you get depends on who touched it last, not on who was fouled.',

    matchEyebrow='After the whistle', matchTitle='Words for how the match went',
    mt1h='Nothing conceded',
    mt1b='A <strong>clean sheet</strong> is a match in which your team let in no goals. '
         'It is credit to the goalkeeper and the defence together.',
    mt1n='You <em>keep</em> a clean sheet. You do not <em>make</em> or <em>do</em> one.',
    mt2h='Still level',
    mt2b='If the score is <strong>level</strong> after ninety minutes, a knockout match '
         'goes to <strong>extra time</strong> — two halves of fifteen minutes.',
    mt2n='<em>Injury time</em> is different: minutes added to the end of a normal half.',
    mt3h='Changes and mistakes',
    mt3b='A <strong>substitution</strong> replaces a player from the bench. An '
         '<strong>own goal</strong> is one you accidentally put into your own net.',
    mt3n='An own goal still counts — for the other team.',

    qEyebrow='Match report', qTitle='Choose the word that fits',

    q1why='The <strong>referee</strong> is the official in charge of the match, and the '
          'only one who can stop play — for fouls, injuries or anything dangerous.',
    q2why='A <strong>goal</strong> is scored when the whole ball crosses the goal line '
          'between the posts and under the crossbar. The whole ball, not most of it.',
    q3why='A <strong>foul</strong> is an illegal action against an opponent — tripping, '
          'pushing or holding. Inside the penalty area it becomes a penalty.',
    q4why='A <strong>red card</strong> is the most serious punishment in football. The '
          'player leaves the pitch and the team continues with one player fewer.',
    q5why='A player is <strong>offside</strong> if they are nearer to the opponents&rsquo; '
          'goal line than both the ball and the second-last defender when the ball is '
          'played to them.',
    q6why='The <strong>striker</strong> plays furthest forward and is usually the '
          'team&rsquo;s main goalscorer.',
    q7why='The <strong>goalkeeper</strong> is the only player allowed to use their hands, '
          'and the job is to stop the ball entering the goal.',
    q8why='A <strong>goal kick</strong> goes to the defending team when the ball crosses '
          'the goal line after last touching an attacker. Off a defender it would be a corner.',
    q9why='A <strong>throw-in</strong> restarts play after the ball crosses the touchline. '
          'The player throws with both hands, from behind the head.',
    q10why='To <strong>dribble</strong> is to move forward keeping close control of the '
           'ball, usually past opponents.',
    q11why='A <strong>clean sheet</strong> means the team conceded no goals — normally '
           'said in praise of the goalkeeper and the defence.',
    q12why='<strong>Extra time</strong> is an additional period, usually two halves of '
           'fifteen minutes, played when a knockout match is level and a winner is needed.',
    q13why='A <strong>substitution</strong> is when a player on the pitch is replaced by '
           'one from the bench.',
    q14why='An <strong>own goal</strong> is when a player accidentally puts the ball into '
           'their own team&rsquo;s goal. It counts as a goal for the opposition.',

    actTitle='Commentate on the match', actUse='Use at least four:',
    actSpeakBrief='One of you commentates, the other is the pundit who disagrees. '
                  'Ninety seconds each, then swap.',
    actSpeak1='Describe the goal that opened the scoring — who had the ball, what they did, where it went in.',
    actSpeak2='The referee has given a penalty. Argue that it was the right decision; your partner argues it was not.',
    actSpeak3='Your team is 1–0 up with ten minutes left. Tell the coach which substitution to make, and why.',
    actSpeak4='Sum the match up in thirty seconds without naming the score.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Write a short match report for a club website. Say how the goals came, '
                  'name one player who changed the game, and end with what the result means '
                  'for the table.',
    actPlaceholder='It finished 2–1 at a wet Estadio Municipal, and…',

    resPerfect='Full marks. You can follow a match in English and say what happened in it.',
    resStrong='Strong. The positions and the cards are secure — the restarts are where to look again.',
    resMid='A good base. Go back to the whistle slide: most misses are throw-in, goal kick and corner.',
    resLow='Read the three opening slides again, then run it once more. The vocabulary is small and it repeats.',
)

T['de'] = dict(
    coverTitle='Fußball<em>englisch</em>',
    coverSub='Positionen, Fouls, Standards — und die Wörter, die Kommentatoren wirklich benutzen',
    chipLevel='B1 · Mittelstufe', chipFocus='Wortschatz rund ums Spiel',
    chipCount='20 Folien',

    whoEyebrow='Vor den Fragen', whoTitle='Wer ist wer auf dem Platz',
    who1h='Die Offiziellen',
    who1b='Der <strong>referee</strong> leitet das Spiel und pfeift. Der '
          '<strong>linesman</strong> (Schiedsrichterassistent) beobachtet die Linien '
          'und hebt die Fahne bei Abseits.',
    who1n='Ein Schiedsrichter, zwei Assistenten. Nur der Schiedsrichter darf unterbrechen.',
    who2h='Das Feld',
    who2b='Ein <strong>defender</strong> verteidigt, ein <strong>midfielder</strong> '
          'verbindet Abwehr und Angriff, ein <strong>winger</strong> spielt außen, '
          'ein <strong>striker</strong> steht am weitesten vorne.',
    who2n='<em>Forward</em> und <em>striker</em> überschneiden sich; der striker ist der vorderste.',
    who3h='Das Tor und die Bank',
    who3b='Der <strong>goalkeeper</strong> ist der Einzige, der die Hände benutzen darf. '
          'Der <strong>coach</strong> (oder manager) stellt die Mannschaft auf und wechselt.',
    who3n='Im britischen Kommentar heißt es meist <em>manager</em>; <em>coach</em> versteht man überall.',

    stopEyebrow='Der Pfiff', stopTitle='Was das Spiel unterbricht — und was es fortsetzt',
    st1h='Unterbrechung wegen eines Vergehens',
    st1b='Ein <strong>foul</strong> ist ein regelwidriges Vergehen am Gegner. Eine '
         '<strong>yellow card</strong> ist eine Verwarnung, eine <strong>red card</strong> '
         'bedeutet Platzverweis.',
    st1n='Zwei Gelbe in einem Spiel ergeben Rot. Die Mannschaft spielt zu zehnt weiter.',
    st2h='Unterbrechung wegen Abseits',
    st2b='Ein Spieler steht im <strong>offside</strong>, wenn er der gegnerischen Torlinie '
         'näher ist als der Ball und der vorletzte Abwehrspieler, sobald der Ball zu ihm gespielt wird.',
    st2n='Abseits ist eine Position, keine Handlung — man ist <em>in</em> einer Abseitsposition.',
    st3h='Fortsetzung des Spiels',
    st3b='Über die Seitenlinie → <strong>throw-in</strong>. Über die Torlinie vom Angreifer → '
         '<strong>goal kick</strong>. Vom Verteidiger → <strong>corner</strong>. Foul im '
         'Strafraum → <strong>penalty</strong>.',
    st3n='Entscheidend ist, wer den Ball zuletzt berührt hat — nicht, wer gefoult wurde.',

    matchEyebrow='Nach dem Schlusspfiff', matchTitle='Wörter dafür, wie das Spiel lief',
    mt1h='Kein Gegentor',
    mt1b='Ein <strong>clean sheet</strong> ist ein Spiel ohne Gegentor. Das Verdienst '
         'teilen sich Torwart und Abwehr.',
    mt1n='Man <em>keeps</em> a clean sheet — nicht <em>make</em> oder <em>do</em>.',
    mt2h='Immer noch gleich',
    mt2b='Steht es nach neunzig Minuten <strong>level</strong>, geht ein K.-o.-Spiel in '
         'die <strong>extra time</strong> — zweimal fünfzehn Minuten.',
    mt2n='<em>Injury time</em> ist etwas anderes: Nachspielzeit am Ende einer regulären Halbzeit.',
    mt3h='Wechsel und Fehler',
    mt3b='Eine <strong>substitution</strong> bringt einen Spieler von der Bank. Ein '
         '<strong>own goal</strong> ist ein Eigentor.',
    mt3n='Ein Eigentor zählt trotzdem — für die andere Mannschaft.',

    qEyebrow='Spielbericht', qTitle='Wähle das passende Wort',

    q1why='Der <strong>referee</strong> leitet das Spiel und ist der Einzige, der '
          'unterbrechen darf — bei Fouls, Verletzungen oder Gefahr.',
    q2why='Ein <strong>goal</strong> zählt, wenn der Ball mit vollem Umfang die Torlinie '
          'zwischen den Pfosten und unter der Latte überquert. Der ganze Ball, nicht fast.',
    q3why='Ein <strong>foul</strong> ist ein regelwidriges Vergehen am Gegner — Beinstellen, '
          'Stoßen, Halten. Im Strafraum wird daraus ein Elfmeter.',
    q4why='Die <strong>red card</strong> ist die härteste Strafe. Der Spieler muss vom Platz, '
          'die Mannschaft spielt mit einem Mann weniger weiter.',
    q5why='Ein Spieler steht im <strong>offside</strong>, wenn er der gegnerischen Torlinie '
          'näher ist als der Ball und der vorletzte Abwehrspieler, sobald der Ball zu ihm '
          'gespielt wird.',
    q6why='Der <strong>striker</strong> steht am weitesten vorne und ist meist der '
          'Haupttorschütze der Mannschaft.',
    q7why='Der <strong>goalkeeper</strong> ist der einzige Spieler, der die Hände benutzen '
          'darf; seine Aufgabe ist es, den Ball aus dem Tor zu halten.',
    q8why='Einen <strong>goal kick</strong> gibt es für die verteidigende Mannschaft, wenn '
          'der Ball nach letzter Berührung eines Angreifers über die Torlinie geht. Vom '
          'Verteidiger wäre es ein Eckball.',
    q9why='Ein <strong>throw-in</strong> setzt das Spiel fort, nachdem der Ball die '
          'Seitenlinie überquert hat — mit beiden Händen, von hinten über den Kopf.',
    q10why='<strong>Dribble</strong> heißt, mit engem Ballkontakt nach vorne zu gehen, '
           'meist an Gegnern vorbei.',
    q11why='<strong>Clean sheet</strong> bedeutet, dass die Mannschaft kein Gegentor '
           'kassiert hat — ein Lob für Torwart und Abwehr.',
    q12why='<strong>Extra time</strong> ist die Verlängerung, meist zweimal fünfzehn '
           'Minuten, wenn ein K.-o.-Spiel unentschieden steht.',
    q13why='Eine <strong>substitution</strong> ist ein Wechsel: ein Spieler auf dem Platz '
           'wird durch einen von der Bank ersetzt.',
    q14why='Ein <strong>own goal</strong> ist ein Eigentor — es zählt für die gegnerische '
           'Mannschaft.',

    actTitle='Kommentiere das Spiel', actUse='Benutze mindestens vier:',
    actSpeakBrief='Einer kommentiert, der andere ist der Experte, der widerspricht. '
                  'Je neunzig Sekunden, dann tauschen.',
    actSpeak1='Beschreibe das Führungstor — wer hatte den Ball, was hat er gemacht, wo ging er rein.',
    actSpeak2='Der Schiedsrichter hat Elfmeter gegeben. Begründe, dass es richtig war; dein Partner hält dagegen.',
    actSpeak3='Deine Mannschaft führt 1:0, zehn Minuten sind noch zu spielen. Sag dem Trainer, wen er wechseln soll — und warum.',
    actSpeak4='Fasse das Spiel in dreißig Sekunden zusammen, ohne das Ergebnis zu nennen.',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Schreibe einen kurzen Spielbericht für die Vereinsseite. Erkläre, wie die '
                  'Tore fielen, nenne einen Spieler, der das Spiel gedreht hat, und schließe '
                  'damit, was das Ergebnis für die Tabelle bedeutet.',
    actPlaceholder='It finished 2–1 at a wet Estadio Municipal, and…',

    resPerfect='Volle Punktzahl. Du kannst ein Spiel auf Englisch verfolgen und erzählen, was passiert ist.',
    resStrong='Stark. Positionen und Karten sitzen — schau dir die Standards noch einmal an.',
    resMid='Gute Grundlage. Geh zurück zur Pfiff-Folie: die meisten Fehler sind throw-in, goal kick und corner.',
    resLow='Lies die ersten drei Folien noch einmal und mach dann eine zweite Runde. Der Wortschatz ist klein und wiederholt sich.',
)

T['es'] = dict(
    coverTitle='Inglés del <em>fútbol</em>',
    coverSub='Posiciones, faltas, jugadas a balón parado y las palabras que usan los comentaristas',
    chipLevel='B1 · Intermedio', chipFocus='Vocabulario de partido',
    chipCount='20 diapositivas',

    whoEyebrow='Antes de las preguntas', whoTitle='Quién es quién en el campo',
    who1h='Los oficiales',
    who1b='El <strong>referee</strong> dirige el partido y toca el silbato. El '
          '<strong>linesman</strong> (árbitro asistente) vigila las líneas y levanta '
          'la bandera en el fuera de juego.',
    who1n='Un árbitro y dos asistentes. Solo el árbitro puede detener el juego.',
    who2h='El campo',
    who2b='Un <strong>defender</strong> defiende, un <strong>midfielder</strong> une '
          'defensa y ataque, un <strong>winger</strong> juega por la banda y un '
          '<strong>striker</strong> es el más adelantado.',
    who2n='<em>Forward</em> y <em>striker</em> se solapan; el striker es el más cercano a portería.',
    who3h='La portería y el banquillo',
    who3b='El <strong>goalkeeper</strong> es el único que puede usar las manos. El '
          '<strong>coach</strong> (o manager) elige el once y hace los cambios.',
    who3n='En el comentario británico se dice <em>manager</em>; <em>coach</em> se entiende en todas partes.',

    stopEyebrow='El silbato', stopTitle='Qué detiene el juego y qué lo reanuda',
    st1h='Parado por una infracción',
    st1b='Una <strong>foul</strong> es una acción ilegal sobre un rival. La '
         '<strong>yellow card</strong> es un aviso; la <strong>red card</strong> '
         'supone la expulsión.',
    st1n='Dos amarillas en un partido son roja. El equipo sigue con diez.',
    st2h='Parado por fuera de juego',
    st2b='Un jugador está en <strong>offside</strong> si está más cerca de la línea de gol '
         'rival que el balón y que el penúltimo defensa en el momento del pase.',
    st2n='El fuera de juego es una posición, no una acción — se está <em>en</em> posición de offside.',
    st3h='Reanudar el juego',
    st3b='Por la banda → <strong>throw-in</strong>. Por la línea de gol tocando un atacante → '
         '<strong>goal kick</strong>. Tocando un defensa → <strong>corner</strong>. Falta en '
         'el área → <strong>penalty</strong>.',
    st3n='Lo que decide la reanudación es quién tocó el balón por última vez, no a quién hicieron falta.',

    matchEyebrow='Después del pitido', matchTitle='Palabras para contar cómo fue el partido',
    mt1h='Sin encajar',
    mt1b='Un <strong>clean sheet</strong> es un partido sin goles en contra. El mérito es '
         'del portero y de la defensa a la vez.',
    mt1n='Se dice <em>keep</em> a clean sheet — nunca <em>make</em> ni <em>do</em>.',
    mt2h='Todavía empatados',
    mt2b='Si el marcador sigue <strong>level</strong> tras noventa minutos, un partido '
         'eliminatorio va a la <strong>extra time</strong>: dos partes de quince minutos.',
    mt2n='<em>Injury time</em> es otra cosa: el descuento al final de una parte normal.',
    mt3h='Cambios y errores',
    mt3b='Una <strong>substitution</strong> mete a un jugador del banquillo. Un '
         '<strong>own goal</strong> es un gol en propia puerta.',
    mt3n='El gol en propia puerta cuenta igual — para el otro equipo.',

    qEyebrow='Crónica del partido', qTitle='Elige la palabra que encaja',

    q1why='<strong>Referee</strong> = árbitro. Es quien dirige el partido y el único que '
          'puede detener el juego: faltas, lesiones o cualquier situación peligrosa.',
    q2why='<strong>Goal</strong> = gol. Se marca cuando el balón entero cruza la línea de '
          'gol entre los postes y por debajo del larguero. Entero, no casi.',
    q3why='<strong>Foul</strong> = falta. Una acción ilegal sobre un rival: zancadilla, '
          'empujón o agarrón. Dentro del área se convierte en penalti.',
    q4why='<strong>Red card</strong> = tarjeta roja. Es el castigo más grave: el jugador se '
          'va y el equipo continúa con uno menos.',
    q5why='<strong>Offside</strong> = fuera de juego. El jugador está más cerca de la línea '
          'de gol rival que el balón y que el penúltimo defensa cuando le pasan el balón.',
    q6why='<strong>Striker</strong> = delantero centro. Juega en la posición más adelantada '
          'y suele ser el máximo goleador del equipo.',
    q7why='<strong>Goalkeeper</strong> = portero. El único jugador que puede usar las manos, '
          'y su trabajo es evitar que el balón entre.',
    q8why='<strong>Goal kick</strong> = saque de puerta. Es para el equipo que defiende cuando '
          'el balón sale por la línea de gol tras tocar un atacante. Si toca un defensa, sería córner.',
    q9why='<strong>Throw-in</strong> = saque de banda. Reanuda el juego cuando el balón cruza '
          'la línea de banda; se lanza con las dos manos por detrás de la cabeza.',
    q10why='<strong>Dribble</strong> = regatear. Avanzar manteniendo el control del balón, '
           'normalmente superando rivales.',
    q11why='<strong>Clean sheet</strong> = portería a cero. El equipo no encajó ningún gol; '
           'se dice como elogio al portero y a la defensa.',
    q12why='<strong>Extra time</strong> = prórroga. Un periodo añadido, normalmente dos partes '
           'de quince minutos, cuando una eliminatoria acaba en empate.',
    q13why='<strong>Substitution</strong> = sustitución. Un jugador del campo es reemplazado '
           'por otro del banquillo.',
    q14why='<strong>Own goal</strong> = gol en propia puerta. El jugador mete el balón sin '
           'querer en su propia portería, y cuenta para el rival.',

    actTitle='Narra el partido', actUse='Usa al menos cuatro:',
    actSpeakBrief='Uno narra y el otro es el comentarista que lleva la contraria. '
                  'Noventa segundos cada uno y se cambia.',
    actSpeak1='Describe el gol que abrió el marcador: quién tenía el balón, qué hizo y por dónde entró.',
    actSpeak2='El árbitro ha pitado penalti. Defiende que fue correcto; tu compañero sostiene que no.',
    actSpeak3='Tu equipo gana 1–0 y quedan diez minutos. Dile al entrenador qué cambio hacer, y por qué.',
    actSpeak4='Resume el partido en treinta segundos sin decir el resultado.',
    actWriteKind='Escritura · 150–200 palabras',
    actWriteBrief='Escribe una crónica breve para la web del club. Cuenta cómo llegaron los '
                  'goles, nombra a un jugador que cambió el partido y termina explicando qué '
                  'significa el resultado para la clasificación.',
    actPlaceholder='It finished 2–1 at a wet Estadio Municipal, and…',

    resPerfect='Puntuación perfecta. Puedes seguir un partido en inglés y contar lo que pasó.',
    resStrong='Muy bien. Posiciones y tarjetas están asentadas; repasa las reanudaciones.',
    resMid='Buena base. Vuelve a la diapositiva del silbato: la mayoría de fallos son throw-in, goal kick y corner.',
    resLow='Lee otra vez las tres primeras diapositivas y repite. El vocabulario es corto y se repite.',
)


# Template chrome that no lesson declares but check-lesson.js's I18N gate still
# resolves. Raw JS literals, emitted after the body. Copied verbatim from
# i18n_risk.py rather than re-invented.
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
