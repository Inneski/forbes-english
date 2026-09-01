# -*- coding: utf-8 -*-
"""Interface strings for The Social Edge (C2) — English, German and Spanish.

Innes asked for this lesson with Spanish and German support, so all three are
complete and all three appear in the switcher. The remaining seven stay as {}
and are therefore not offered — house style §8: partial is a failure, empty is
an honest placeholder.

Same scope boundary as every other deck. The switcher translates the app's own
chrome: cover, section titles, task instructions and hints, the notes under
each teaching card, the activation briefs and the result bands. It does NOT
translate the English being taught. Every stem, option, gap sentence, word
bank, sort item, order chunk, match pair, explanation and activation chip
stays in English in all three languages, because the target language of this
lesson IS argumentative register — translating *declines to examine* into
*sich nicht damit befasst* hands the learner the answer to a sort, a multiple
choice and half the activation stage.

That is why the teaching cards use deck.teach's five-item form: the term and
its English gloss carry no data-i18n and stay put, while the note underneath —
commentary about the term, not the term — translates. A learner switching to
Spanish sees the same English moves with Spanish guidance around them, which
is the support that was asked for.

One deliberate non-translation inside the German and Spanish text: where a
note quotes the English being taught (*converge*, *declines to examine*,
*were … to*, *not because X but because Y*) the quotation stays in English. It
is the object under discussion, not an instruction about the task. The
activation placeholder stays English for the same reason: it is the first
words of the learner's own answer.

coverTitle is identical in all three languages, and that is deliberate rather
than an unfinished cell. "The Social Edge" is the name the essay coins for its
own framework, and the match slide asks the learner to pair "the Social Edge
Paradox" with its definition; a German cover reading "Der soziale Vorsprung"
would name something the rest of the deck never mentions again. Every other
key is genuinely translated, so the I18N gate's key count is honest.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

# Emitted from CHROME verbatim, sorted in with the body.
#
# actSpeakKind and resNext are NOT lifted: CHROME carries 'Discussion · in
# pairs' and the generic results line, and this lesson runs its activation in
# threes (proposer, opponent, summariser) and wants its own hand-off sentence.
# Both are declared in T below instead.
LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel',
        'slideOf', 'fbCorrect', 'fbWrong', 'fbAnswer', 'btnCopy', 'btnCopied',
        'wordCount', 'btnOpen', 'actEyebrow']

# Template chrome that no lesson declares but check-lesson.js's I18N gate
# still resolves. Raw JS literals, emitted after the body.
TAIL = {
    'en': {'branchLocked': "'Your ledger does not support this ending'",
           'glossHide': "'Hide'",
           'glossShow': "'Translate'",
           'ledClues': "'Clues'",
           'ledDp': "'DP'",
           'ledTime': "'Time'"},
    'de': {'branchLocked': "'Dein Protokoll trägt dieses Ende nicht'",
           'glossHide': "'Ausblenden'",
           'glossShow': "'Übersetzen'",
           'ledClues': "'Hinweise'",
           'ledDp': "'DP'",
           'ledTime': "'Zeit'"},
    'es': {'branchLocked': "'Tu registro no admite este final'",
           'glossHide': "'Ocultar'",
           'glossShow': "'Traducir'",
           'ledClues': "'Pistas'",
           'ledDp': "'DP'",
           'ledTime': "'Tiempo'"},
}

T = {}

# ── ENGLISH ────────────────────────────────────────────────────────────
T['en'] = dict(
    coverTitle='The <em>Social Edge</em>',
    coverSub='Reading an argument that runs against the consensus — and building one: nominalisation, stance, concession and the metaphors that carry a claim',
    chipLevel='C2 &middot; Argument &amp; abstraction',
    chipFocus='Reporting, conceding, correcting the cause',
    chipCount='NSLIDES slides',

    t1Eyebrow='Density, and what it costs',
    t1Title='Nominalisation: turning a claim into a thing',
    t1n1='Once it is a noun, it can be the subject of your next sentence.',
    t1n2='Naming the thing is the first move in owning the argument about it.',
    t1n3='A nominalised pair is what makes a claim quotable.',
    t1n4='Same tell as the passive: ask who did it, and see whether the sentence can answer.',

    t2Eyebrow='Seven verbs, one scale',
    t2Title='The vocabulary of decline is not a synonym set',
    t2n1='About how many there are, never about quality.',
    t2n2='<em>Converge</em> is about similarity and can never mean <em>fewer</em>.',
    t2n3='<em>Erode</em> takes surfaces and institutions; <em>attenuate</em> takes signals and effects.',
    t2n4='<em>Collapse</em> is the end state. The other six are the road to it.',

    t3Eyebrow='Reporting, or agreeing',
    t3Title='The verb you choose is a verdict',
    t3n1='You have reported the claim. You have not signed it.',
    t3n2='Use one of these and you have agreed. That is a decision, not a style.',
    t3n3='These name what the source did not do &mdash; the sharpest tool in a critique.',
    t3n4='You describe the move rather than accepting the fact.',

    t4Eyebrow='The shape of an argument',
    t4Title='Concede properly, then turn once',
    t4n1='Give the strongest version of the other side. A weak concession reads as a trick.',
    t4n2='One sentence, and it carries the essay. Two pivots and the reader stops believing either.',
    t4n3='Set the consensus up in its own words, then break it with the evidence.',
    t4n4='You accept the fact and reassign its reason. Far harder to answer than a flat denial.',

    t5Eyebrow='Premises and payoff',
    t5Title='Conditional chains, and the inverted form',
    t5n1='Two premises, one conclusion. The dashes hold the second premise open.',
    t5n2='Formal, and it front-loads the condition. No <em>if</em>, and never <em>if &hellip; would</em>.',
    t5n3='<em>Suppose</em> sets it up and <em>would</em> runs to the end of it, without ever slipping into <em>will</em>.',
    t5n4='Hedge the conclusion. Hedge the premises too and you have argued nothing.',

    t6Eyebrow='Figurative language that argues',
    t6Title='A live metaphor makes a claim you can dispute',
    t6n1='It chooses the frame: intelligence as a crop, not as a machine.',
    t6n2='An extended metaphor has to stay inside one frame: consume, reinvest, run out.',
    t6n3='Taken from a field that defines it. It must survive being read literally.',
    t6n4='A live metaphor advances the argument. A dead one is just a word you reached for.',

    sortEyebrow='Whose claim is it?',
    sortTitleA='Reporting it, or agreeing with it?',
    sortHintA='Click a line, then the box it belongs in. Every line is about somebody else&rsquo;s work &mdash; the question is what the verb commits the writer to.',
    sortTitleB='Which move is the sentence making?',
    sortHintB='Click a line, then the box it belongs in. One box accepts the fact and changes only the reason given for it.',

    bankLabel='Word bank:',
    gapEyebrow='Precision under pressure',
    gapTitleA='Choose the verb that is actually true',
    gapHintA='One verb per gap, in the right form. Four of the seven are not needed &mdash; and two of those four are the ones people reach for by mistake.',
    gapTitleB='Pack the clause into a noun phrase',
    gapHintB='One noun per gap. Four of the seven are not needed. Each sentence says the same thing twice &mdash; once as a clause, once as a noun.',

    matEyebrow='The named things',
    matTitle='Match the term to what it actually names',
    matHint='Six coinages, six definitions. Every one of them is a whole finding compressed into a noun phrase &mdash; which is why they travel.',

    ordEyebrow='Build the argument',
    ordTitleA='The argument in one sentence',
    ordHintA='Click the parts in order: two premises, then what follows from them.',
    ordTitleB='Concede, then turn',
    ordHintB='Click the parts in order. The concession is real and it comes first.',

    qEyebrow='Choose the version that survives being quoted back',
    qTitle='Which one would you actually write?',

    actTitle='Now argue it',
    actUse='Use at least four:',
    actSpeakKind='Discussion &middot; in threes',
    actSpeakBrief='Twelve minutes. One proposes the cut, one opposes it, one has to summarise both positions fairly at the end.',
    actSpeak1='You chair the operating committee. Argue against a 30% cut to entry-level hiring on the pipeline, not on sentiment.',
    actSpeak2='Take the other side: the tacit-knowledge argument is what every incumbent says to protect headcount.',
    actSpeak3='Report Doshi and Hauser&rsquo;s finding in three sentences, without signing any of it.',
    actSpeak4='Your CTO calls the substrate argument unfalsifiable. Concede the strongest version of that, then pivot once.',
    actWriteKind='Writing &middot; 180&ndash;220 words',
    actWriteBrief='Write the one-page note to your board opposing a 30% cut to entry-level roles. Concede the cost case in full before you turn; name the mechanism, not the mood; keep one metaphor inside its own frame; close with what you would measure in twelve months.',
    actPlaceholder='Yes, the cost case is sound. But…',

    resNext='Recognising the moves is the easy half. Now make one of these arguments out loud →',
    resPerfect='Full marks. You can see the machinery &mdash; using it on someone who disagrees with you is the other half.',
    resStrong='Strong. Look again at what you missed: most of it turns on a verb that commits you further than you meant to go.',
    resMid='A usable base. Re-read the reporting verbs and the seven verbs of decline before you write anything.',
    resLow='Go back through the six teaching slides. Almost every miss here is a word used as though it were a synonym of another one.',
)

# ── GERMAN ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='The <em>Social Edge</em>',
    coverSub='Eine Argumentation lesen, die gegen den Konsens läuft — und selbst eine bauen: Nominalisierung, Haltung, Zugeständnis und die Metaphern, die eine These tragen',
    chipLevel='C2 &middot; Argumentation &amp; Abstraktion',
    chipFocus='Berichten, zugestehen, die Ursache korrigieren',
    chipCount='NSLIDES Folien',

    t1Eyebrow='Dichte, und was sie kostet',
    t1Title='Nominalisierung: aus einer Aussage ein Ding machen',
    t1n1='Als Substantiv kann es das Subjekt Ihres nächsten Satzes werden.',
    t1n2='Etwas zu benennen ist der erste Schritt, die Debatte darüber zu besitzen.',
    t1n3='Ein nominalisiertes Paar ist das, was eine These zitierfähig macht.',
    t1n4='Dasselbe Erkennungszeichen wie beim Passiv: Fragen Sie, wer es getan hat, und sehen Sie, ob der Satz antworten kann.',

    t2Eyebrow='Sieben Verben, eine Skala',
    t2Title='Das Vokabular des Rückgangs ist keine Synonymreihe',
    t2n1='Es geht um die Anzahl, nie um die Qualität.',
    t2n2='<em>Converge</em> meint Ähnlichkeit und kann nie <em>weniger</em> bedeuten.',
    t2n3='<em>Erode</em> nimmt Oberflächen und Institutionen, <em>attenuate</em> Signale und Wirkungen.',
    t2n4='<em>Collapse</em> ist der Endzustand. Die anderen sechs sind der Weg dorthin.',

    t3Eyebrow='Berichten oder zustimmen',
    t3Title='Das gewählte Verb ist ein Urteil',
    t3n1='Sie haben die These berichtet. Unterschrieben haben Sie sie nicht.',
    t3n2='Wer eines davon nimmt, hat zugestimmt. Das ist eine Entscheidung, kein Stil.',
    t3n3='Sie benennen, was die Quelle <em>nicht</em> getan hat &mdash; das schärfste Mittel der Kritik.',
    t3n4='Sie beschreiben den rhetorischen Zug, statt den Sachverhalt zu übernehmen.',

    t4Eyebrow='Die Form einer Argumentation',
    t4Title='Richtig zugestehen, dann einmal wenden',
    t4n1='Geben Sie die stärkste Fassung der Gegenseite. Ein schwaches Zugeständnis wirkt wie ein Trick.',
    t4n2='Ein Satz, und er trägt den ganzen Essay. Bei zwei Wendungen glaubt die Leserin keiner mehr.',
    t4n3='Bauen Sie den Konsens in seinen eigenen Worten auf und brechen Sie ihn dann mit Belegen.',
    t4n4='Sie akzeptieren den Sachverhalt und weisen ihm eine andere Ursache zu. Weit schwerer zu kontern als ein glattes Nein.',

    t5Eyebrow='Prämissen und Schluss',
    t5Title='Bedingungsketten und die invertierte Form',
    t5n1='Zwei Prämissen, ein Schluss. Die Gedankenstriche halten die zweite Prämisse offen.',
    t5n2='Formell, und die Bedingung steht vorn. Kein <em>if</em> &mdash; und niemals <em>if &hellip; would</em>.',
    t5n3='<em>Suppose</em> eröffnet es, <em>would</em> trägt bis zum Ende durch, ohne je in <em>will</em> zu rutschen.',
    t5n4='Schwächen Sie den Schluss ab. Schwächen Sie auch die Prämissen ab, haben Sie nichts behauptet.',

    t6Eyebrow='Bildsprache, die argumentiert',
    t6Title='Eine lebendige Metapher stellt eine bestreitbare Behauptung auf',
    t6n1='Sie wählt den Rahmen: Intelligenz als Anbau, nicht als Maschine.',
    t6n2='Eine ausgebaute Metapher muss in ihrem Rahmen bleiben: verbrauchen, reinvestieren, ausgehen.',
    t6n3='Aus einem Fach entlehnt, das den Begriff definiert. Sie muss die wörtliche Lesart überstehen.',
    t6n4='Eine lebendige Metapher bringt das Argument voran. Eine tote ist bloß ein Wort, nach dem Sie gegriffen haben.',

    sortEyebrow='Wessen These ist das?',
    sortTitleA='Berichtet oder zugestimmt?',
    sortHintA='Klicken Sie auf eine Zeile und dann auf das passende Feld. Jede Zeile handelt von fremder Arbeit &mdash; die Frage ist, worauf das Verb die schreibende Person festlegt.',
    sortTitleB='Welchen Zug macht der Satz?',
    sortHintB='Klicken Sie auf eine Zeile und dann auf das passende Feld. Ein Feld akzeptiert den Sachverhalt und ändert nur die angegebene Ursache.',

    bankLabel='Wortspeicher:',
    gapEyebrow='Präzision unter Druck',
    gapTitleA='Wählen Sie das Verb, das tatsächlich zutrifft',
    gapHintA='Ein Verb pro Lücke, in der richtigen Form. Vier der sieben werden nicht gebraucht &mdash; und zwei davon sind genau die, zu denen man irrtümlich greift.',
    gapTitleB='Packen Sie den Nebensatz in eine Nominalphrase',
    gapHintB='Ein Substantiv pro Lücke. Vier der sieben werden nicht gebraucht. Jeder Satz sagt dasselbe zweimal &mdash; einmal als Satz, einmal als Substantiv.',

    matEyebrow='Die benannten Dinge',
    matTitle='Ordnen Sie jedem Begriff zu, was er wirklich benennt',
    matHint='Sechs Prägungen, sechs Definitionen. Jede ist ein ganzer Befund, zusammengezogen in eine Nominalphrase &mdash; deshalb wandern sie so weit.',

    ordEyebrow='Bauen Sie die Argumentation',
    ordTitleA='Die Argumentation in einem Satz',
    ordHintA='Klicken Sie die Teile in der richtigen Reihenfolge an: zwei Prämissen, dann was daraus folgt.',
    ordTitleB='Zugestehen, dann wenden',
    ordHintB='Klicken Sie die Teile in der richtigen Reihenfolge an. Das Zugeständnis ist echt und kommt zuerst.',

    qEyebrow='Wählen Sie die Fassung, die es übersteht, zitiert zu werden',
    qTitle='Welche würden Sie wirklich schreiben?',

    actTitle='Jetzt argumentieren Sie',
    actUse='Verwenden Sie mindestens vier:',
    actSpeakKind='Diskussion &middot; zu dritt',
    actSpeakBrief='Zwölf Minuten. Einer schlägt die Kürzung vor, einer hält dagegen, einer fasst am Ende beide Positionen fair zusammen.',
    actSpeak1='Sie leiten den Ausschuss. Argumentieren Sie gegen 30% weniger Einstiegsstellen &mdash; über die Pipeline, nicht über das Gefühl.',
    actSpeak2='Gegenposition: Das Erfahrungswissen-Argument führt jeder an, um Stellen zu schützen.',
    actSpeak3='Berichten Sie den Befund von Doshi und Hauser in drei Sätzen, ohne ihn zu unterschreiben.',
    actSpeak4='Ihr CTO nennt das Substrat-Argument unwiderlegbar. Gestehen Sie die stärkste Fassung zu und wenden Sie einmal.',
    actWriteKind='Schreiben &middot; 180&ndash;220 Wörter',
    actWriteBrief='Einseitige Vorlage an den Vorstand gegen 30% weniger Einstiegsstellen. Gestehen Sie die Kosten voll zu, bevor Sie wenden; benennen Sie den Mechanismus, nicht die Stimmung; eine Metapher, in ihrem Rahmen; dazu Ihre Messgröße für zwölf Monate.',
    actPlaceholder='Yes, the cost case is sound. But…',

    resNext='Die Züge zu erkennen ist die leichte Hälfte. Jetzt führen Sie eines dieser Argumente laut aus →',
    resPerfect='Volle Punktzahl. Sie sehen die Mechanik &mdash; sie gegenüber jemandem einzusetzen, der widerspricht, ist die andere Hälfte.',
    resStrong='Stark. Sehen Sie sich die Fehler noch einmal an: Fast alle hängen an einem Verb, das Sie weiter festlegt, als Sie wollten.',
    resMid='Eine brauchbare Grundlage. Lesen Sie die Redeeinleitungsverben und die sieben Verben des Rückgangs noch einmal, bevor Sie etwas schreiben.',
    resLow='Gehen Sie die sechs Erklärfolien noch einmal durch. Fast jeder Fehler hier ist ein Wort, das wie ein Synonym eines anderen benutzt wurde.',
)

# ── SPANISH ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='The <em>Social Edge</em>',
    coverSub='Leer un argumento que va contra el consenso — y construir uno: nominalización, postura, concesión y las metáforas que sostienen una tesis',
    chipLevel='C2 &middot; Argumentación y abstracción',
    chipFocus='Referir, conceder, corregir la causa',
    chipCount='NSLIDES diapositivas',

    t1Eyebrow='Densidad, y lo que cuesta',
    t1Title='Nominalización: convertir una afirmación en una cosa',
    t1n1='Ya como sustantivo, puede ser el sujeto de tu frase siguiente.',
    t1n2='Nombrar algo es el primer paso para adueñarse del debate sobre ello.',
    t1n3='Un par nominalizado es lo que hace citable una tesis.',
    t1n4='La misma señal que en la pasiva: pregunta quién lo hizo y mira si la frase puede responder.',

    t2Eyebrow='Siete verbos, una escala',
    t2Title='El vocabulario del declive no es una lista de sinónimos',
    t2n1='Habla de cuántos hay, nunca de la calidad.',
    t2n2='<em>Converge</em> habla de parecido y nunca puede significar <em>menos</em>.',
    t2n3='<em>Erode</em> toma superficies e instituciones; <em>attenuate</em>, señales y efectos.',
    t2n4='<em>Collapse</em> es el estado final. Los otros seis son el camino hasta él.',

    t3Eyebrow='Referir o suscribir',
    t3Title='El verbo que eliges es un veredicto',
    t3n1='Has referido la tesis. No la has firmado.',
    t3n2='Si usas uno de estos, ya has dado tu conformidad. Es una decisión, no un estilo.',
    t3n3='Nombran lo que la fuente <em>no</em> hizo &mdash; la herramienta más afilada de una crítica.',
    t3n4='Describes la maniobra en lugar de aceptar el hecho.',

    t4Eyebrow='La forma de un argumento',
    t4Title='Concede de verdad y gira una sola vez',
    t4n1='Da la versión más fuerte de la otra parte. Una concesión débil suena a truco.',
    t4n2='Una frase, y sostiene el ensayo entero. Con dos giros el lector deja de creerse ninguno.',
    t4n3='Monta el consenso con sus propias palabras y luego rómpelo con la evidencia.',
    t4n4='Aceptas el hecho y le reasignas la causa. Mucho más difícil de rebatir que una negación.',

    t5Eyebrow='Premisas y conclusión',
    t5Title='Cadenas condicionales y la forma invertida',
    t5n1='Dos premisas, una conclusión. Las rayas mantienen abierta la segunda premisa.',
    t5n2='Formal, y coloca la condición al principio. Sin <em>if</em>, y nunca <em>if &hellip; would</em>.',
    t5n3='<em>Suppose</em> lo abre y <em>would</em> lo sostiene hasta el final, sin caer nunca en <em>will</em>.',
    t5n4='Matiza la conclusión. Si matizas también las premisas, no has afirmado nada.',

    t6Eyebrow='Lenguaje figurado que argumenta',
    t6Title='Una metáfora viva formula una tesis que se puede discutir',
    t6n1='Elige el marco: la inteligencia como cultivo, no como máquina.',
    t6n2='Una metáfora extendida debe quedarse en un solo marco: consumir, reinvertir, agotarse.',
    t6n3='Tomada de un campo que la define. Tiene que aguantar una lectura literal.',
    t6n4='Una metáfora viva hace avanzar el argumento. Una muerta es solo una palabra a mano.',

    sortEyebrow='¿De quién es la tesis?',
    sortTitleA='¿La refiere o la suscribe?',
    sortHintA='Haz clic en una línea y luego en su casilla. Todas hablan del trabajo de otra persona &mdash; la cuestión es a qué compromete el verbo a quien escribe.',
    sortTitleB='¿Qué maniobra hace la frase?',
    sortHintB='Haz clic en una línea y luego en su casilla. Una de las casillas acepta el hecho y solo cambia la causa que se le atribuye.',

    bankLabel='Banco de palabras:',
    gapEyebrow='Precisión bajo presión',
    gapTitleA='Elige el verbo que de verdad es cierto',
    gapHintA='Un verbo por hueco, en la forma correcta. Cuatro de los siete no hacen falta &mdash; y dos de esos cuatro son justo los que se usan por error.',
    gapTitleB='Comprime la oración en un sintagma nominal',
    gapHintB='Un sustantivo por hueco. Cuatro de los siete no hacen falta. Cada frase dice lo mismo dos veces &mdash; una como oración y otra como sustantivo.',

    matEyebrow='Las cosas con nombre',
    matTitle='Empareja cada término con lo que de verdad nombra',
    matHint='Seis acuñaciones, seis definiciones. Cada una es un hallazgo entero comprimido en un sintagma nominal &mdash; por eso viajan tan lejos.',

    ordEyebrow='Construye el argumento',
    ordTitleA='El argumento en una sola frase',
    ordHintA='Haz clic en las partes en orden: dos premisas y después lo que se sigue de ellas.',
    ordTitleB='Concede y luego gira',
    ordHintB='Haz clic en las partes en orden. La concesión es real y va primero.',

    qEyebrow='Elige la versión que aguanta que te la citen',
    qTitle='¿Cuál escribirías de verdad?',

    actTitle='Ahora defiéndelo',
    actUse='Usa al menos cuatro:',
    actSpeakKind='Debate &middot; en grupos de tres',
    actSpeakBrief='Doce minutos. Uno propone el recorte, otro se opone y otro tiene que resumir con justicia las dos posturas al final.',
    actSpeak1='Presides el comité operativo. Argumenta contra un recorte del 30% en puestos de entrada por la cantera, no por el sentimiento.',
    actSpeak2='Postura contraria: el argumento del conocimiento tácito lo alega cualquiera para proteger plantilla.',
    actSpeak3='Refiere el hallazgo de Doshi y Hauser en tres frases, sin firmarlo.',
    actSpeak4='Tu CTO dice que el argumento del sustrato es infalsable. Concede su versión más fuerte y gira una sola vez.',
    actWriteKind='Escritura &middot; 180&ndash;220 palabras',
    actWriteBrief='Escribe la nota de una página al consejo contra un recorte del 30% en puestos de entrada. Concede el argumento de costes antes de girar; nombra el mecanismo, no el ánimo; mantén una metáfora dentro de su marco; cierra con lo que medirías en doce meses.',
    actPlaceholder='Yes, the cost case is sound. But…',

    resNext='Reconocer las maniobras es la mitad fácil. Ahora defiende uno de estos argumentos en voz alta →',
    resPerfect='Puntuación perfecta. Ves la maquinaria &mdash; usarla ante alguien que te lleva la contraria es la otra mitad.',
    resStrong='Muy bien. Vuelve a mirar los fallos: casi todos dependen de un verbo que te compromete más de lo que pretendías.',
    resMid='Una base aprovechable. Relee los verbos de cita y los siete verbos del declive antes de escribir nada.',
    resLow='Vuelve a las seis diapositivas de explicación. Casi todo fallo aquí es una palabra usada como si fuera sinónimo de otra.',
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
