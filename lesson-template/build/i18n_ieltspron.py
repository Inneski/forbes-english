# -*- coding: utf-8 -*-
"""Interface strings for IELTS Pronunciation & fluency.

English, German and Spanish, teach cards in the six-item form.

Same split as the rest of the route (HOUSE-STYLE §8): the rule and the reason
translate, the English under test does not. The stress examples — <em>RECord</em>
against <em>reCORD</em>, and the six readings of "I didn't say she stole the
money" — stay English in every gloss, because the beat the learner has to
produce is a fact about the English sentence and not about its translation.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
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

# ── English ────────────────────────────────────────────────────────────
T['en'] = dict(
    coverTitle='Pronunciation <em>&amp; Fluency</em>',
    coverSub='A quarter of the marks, and the quarter nobody practises: '
             'stress, chunking, and the pause that reads as thinking',
    chipLevel='C1 · Advanced', chipFocus='Speaking · all three parts',
    chipCount='18 points',

    t1Eyebrow='Before you start',
    t1Title='It is not an accent test. It never was.',
    t1ah='What is actually scored',
    t1ab='The descriptors ask how easily you can be understood, whether you '
         'control the features that carry meaning, and how much effort the '
         'listener has to make. Sounding British is on none of those lists.',
    t1an='Candidates lose marks here for flat stress far more often than for '
         'an accent.',
    t1bh='Stress marks the meaning',
    t1bb='English puts the beat on the words that carry the point and lets the '
         'rest run light. Flatten that and every word arrives with equal '
         'weight, so the listener has to work out the point unaided.',
    t1bn='Two syllables, two words: <em>RECord</em> is the noun, '
         '<em>reCORD</em> is the verb.',
    t1ch='Six sentences, six words',
    t1cb='&ldquo;I didn&rsquo;t say she stole the money&rdquo; means six '
         'different things depending on which word takes the beat. The words '
         'never change; only the stress does.',
    t1cn='Try it aloud on each of the six. Every version denies something '
         'different.',

    t2Eyebrow='Before you start',
    t2Title='Speech arrives in groups, not in words',
    t2ah='The thought group',
    t2ab='Fluent English comes in short runs of words said as one unit, with a '
         'small break between them. The break is not a hesitation &mdash; it '
         'is the punctuation of spoken language.',
    t2an='Roughly three to seven words is the natural size of a group.',
    t2bh='The boundary carries meaning',
    t2bb='Move the break and you move the sense. The group boundary is doing '
         'the same job a comma does on the page, and putting it in the wrong '
         'place misleads the listener in the same way.',
    t2bn='Read a written sentence aloud and the commas usually show you where '
         'the groups end.',
    t2ch='Inside a group, keep going',
    t2cb='A break inside a group is the one that reads as trouble: pausing in '
         'the middle of a noun phrase tells the examiner you have lost the '
         'word, not that you are weighing an idea.',
    t2cn='Pause at the joins, not inside the pieces.',

    t3Eyebrow='Before you start',
    t3Title='The pause, and what you put in it',
    t3ah='Silence is allowed',
    t3ab='A short silence at the end of a group reads as thinking. The same '
         'length of silence in the middle of a phrase reads as a search for a '
         'word. The pause is not the problem &mdash; its position is.',
    t3an='Two seconds at a join is unremarkable. Two seconds inside a phrase '
         'is audible.',
    t3bh='Fillers are worse than silence',
    t3bb='<em>Errrm</em> and a repeated first word draw attention to the '
         'trouble. A clean break does not. If you need a moment, take it '
         'quietly &mdash; or say that you are taking it.',
    t3bn='<em>That is a good question, actually</em> buys the same time and '
         'costs nothing.',
    t3ch='Talk around the word you lost',
    t3cb='If the word will not come, describe what the thing does and keep the '
         'turn. Paraphrase is scored under Lexical Resource; stopping dead is '
         'scored under Fluency, and not kindly.',
    t3cn='Never stop to ask the examiner for a word. They will not give you '
         'one.',

    mcaEyebrow='Activity 1 · Where the beat falls',
    mcaTitle='Stress, and what moves when it moves',
    mcbEyebrow='Activity 2 · Thought groups',
    mcbTitle='Where speech breaks, and why it matters',
    mccEyebrow='Activity 3 · Pausing and repair',
    mccTitle='Thinking, or stalling?',

    p1why='The content words &mdash; the ones the sentence is actually about. '
          'Length, breath and difficulty have nothing to do with it; a '
          'one-syllable word takes the beat whenever it carries the point.',
    p2why='Each version denies a different part: stressing the pronoun denies '
          'that it was her, stressing the verb denies the theft itself. Same '
          'words, six meanings, carried entirely by the beat.',
    p3why='Flat stress leaves the listener to work out the point unaided, and '
          'the strain on the listener is written into the descriptors. The '
          'individual words can be perfectly clear and still cost marks.',
    p4why='<em>RECord</em> the noun, <em>reCORD</em> the verb &mdash; and the '
          'same shift runs through <em>present</em>, <em>increase</em> and '
          '<em>contract</em>. The other three keep one stress pattern.',
    p5why='A short run of words said as one unit of meaning, usually three to '
          'seven. It is not a breath count and not a grammatical clause, '
          'though a clause is often one group.',
    p6why='Grouped as one unit, the sentence says you have several brothers '
          'and identifies which. Broken either side of the relative clause, it '
          'says you have one and adds a fact about him.',
    p7why='At the joins. A break inside a group tells the examiner you lost a '
          'word; a break at the end of one is the spoken equivalent of a '
          'comma. Commas are a guide, not the rule.',
    p8why='As a rehearsed answer. Examiners are trained to hear memorised '
          'material, and unbroken delivery over two minutes is one of the '
          'signals. Natural speech groups and breathes.',
    p9why='A short silence at a boundary. The other three all advertise the '
          'trouble: a filler inside a phrase, a break inside a noun, and a '
          'first word repeated until the rest arrives.',
    p10why='Describe it and keep going. Paraphrase is rewarded under Lexical '
           'Resource, a first-language word is not English, asking is not '
           'answered, and restarting spends the time you have.',
    p11why='No. What is scored is intelligibility and the effort the listener '
           'has to make. Accent is explicitly not a band descriptor &mdash; '
           'and there is no native model for it to be measured against.',
    p12why='Mispronouncing the words the answer is built on, because those are '
           'the words the listener needs. Accent, a thinking pause and a '
           'measured pace cost nothing at all.',

    sortEyebrow='Activity 4 · What the criterion actually scores',
    sortTitle='Sort the six habits',
    sortHint='Drag each one into a column &mdash; or click an item, then the '
             'column you want it in.',
    sortBin1='Costs you marks',
    sortBin2='Costs you nothing',

    actTitle='Say it, and be followed',
    actUse='Use at least three:',
    actSpeakBrief='In pairs, with the long-turn card from Part 2. Read your '
                  'partner a four-line answer, deliberately flat, then read it '
                  'again in thought groups with the beat on the content words. '
                  'Your partner says what changed.',
    actSpeak1='Say &ldquo;I didn&rsquo;t say she stole the money&rdquo; six '
              'times, one beat each. Your partner names what you denied.',
    actSpeak2='Take a Part 3 question and answer it in groups of three to '
              'seven words, pausing only at the joins.',
    actSpeak3='Have your partner interrupt with a word you do not know. Talk '
              'around it and keep the turn &mdash; no stopping, no asking.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Write out a two-minute answer, then mark it up: a slash at '
                  'every group boundary and capitals on the word that takes '
                  'the beat in each group. Read it back and check the beats '
                  'land where the meaning is.',
    actPlaceholder='The place I would recommend / is a small town…',
)

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Aussprache <em>&amp; Sprachfluss</em>',
    coverSub='Ein Viertel der Note &mdash; und das Viertel, das niemand übt: '
             'Betonung, Sinngruppen und die Pause, die nach Denken klingt',
    chipLevel='C1 · Fortgeschritten', chipFocus='Speaking · alle drei Teile',
    chipCount='18 Punkte',

    t1Eyebrow='Bevor du beginnst',
    t1Title='Es ist kein Akzenttest. Das war es nie.',
    t1ah='Was wirklich bewertet wird',
    t1ab='Die Deskriptoren fragen, wie leicht man dich versteht, ob du die '
         'bedeutungstragenden Merkmale beherrschst und wie viel Mühe das '
         'Zuhören kostet. Britisch zu klingen steht auf keiner dieser Listen.',
    t1an='Für flache Betonung verlieren Kandidaten hier weit häufiger Punkte '
         'als für einen Akzent.',
    t1bh='Betonung markiert die Bedeutung',
    t1bb='Englisch legt den Schlag auf die Wörter, die den Punkt tragen, und '
         'lässt den Rest leicht laufen. Wer das einebnet, liefert jedes Wort '
         'mit gleichem Gewicht &mdash; und der Zuhörer sucht den Punkt allein.',
    t1bn='Zwei Silben, zwei Wörter: <em>RECord</em> ist das Substantiv, '
         '<em>reCORD</em> das Verb.',
    t1ch='Sechs Sätze, sechs Wörter',
    t1cb='&bdquo;I didn&rsquo;t say she stole the money&ldquo; bedeutet sechs '
         'verschiedene Dinge, je nachdem, welches Wort den Schlag bekommt. Die '
         'Wörter ändern sich nie, nur die Betonung.',
    t1cn='Sprich alle sechs laut. Jede Fassung bestreitet etwas anderes.',

    t2Eyebrow='Bevor du beginnst',
    t2Title='Sprache kommt in Gruppen, nicht in Wörtern',
    t2ah='Die Sinngruppe',
    t2ab='Flüssiges Englisch kommt in kurzen Wortfolgen, die als eine Einheit '
         'gesprochen werden, mit einer kleinen Lücke dazwischen. Diese Lücke '
         'ist kein Zögern &mdash; sie ist die Zeichensetzung des Sprechens.',
    t2an='Etwa drei bis sieben Wörter ist die natürliche Größe einer Gruppe.',
    t2bh='Die Grenze trägt Bedeutung',
    t2bb='Verschiebst du die Lücke, verschiebst du den Sinn. Die Gruppengrenze '
         'tut dasselbe wie ein Komma auf dem Papier &mdash; an der falschen '
         'Stelle führt sie den Zuhörer genauso in die Irre.',
    t2bn='Lies einen geschriebenen Satz laut: die Kommas zeigen meist, wo die '
         'Gruppen enden.',
    t2ch='Innerhalb einer Gruppe: weiter',
    t2cb='Die Lücke innerhalb einer Gruppe ist die, die nach Problem klingt: '
         'eine Pause mitten in einer Nominalphrase sagt dem Prüfer, dass dir '
         'das Wort fehlt &mdash; nicht, dass du einen Gedanken abwägst.',
    t2cn='Pausiere an den Fugen, nicht in den Teilen.',

    t3Eyebrow='Bevor du beginnst',
    t3Title='Die Pause &mdash; und was du hineinlegst',
    t3ah='Stille ist erlaubt',
    t3ab='Eine kurze Stille am Ende einer Gruppe klingt nach Denken. Dieselbe '
         'Stille mitten in einer Phrase klingt nach Wortsuche. Nicht die Pause '
         'ist das Problem, sondern ihre Position.',
    t3an='Zwei Sekunden an einer Fuge fallen nicht auf. Zwei Sekunden in einer '
         'Phrase schon.',
    t3bh='Füllwörter sind schlimmer als Stille',
    t3bb='<em>Errrm</em> und ein wiederholtes erstes Wort lenken die '
         'Aufmerksamkeit auf das Problem. Eine saubere Pause nicht. Brauchst '
         'du einen Moment, nimm ihn leise &mdash; oder sag, dass du ihn nimmst.',
    t3bn='<em>That is a good question, actually</em> kauft dieselbe Zeit und '
         'kostet nichts.',
    t3ch='Rede um das fehlende Wort herum',
    t3cb='Kommt das Wort nicht, beschreibe, was die Sache tut, und behalte das '
         'Rederecht. Umschreibung zählt unter Lexical Resource; stehen zu '
         'bleiben zählt unter Fluency, und nicht freundlich.',
    t3cn='Halte nie an, um den Prüfer nach einem Wort zu fragen. Er gibt dir '
         'keines.',

    mcaEyebrow='Aktivität 1 · Wo der Schlag liegt',
    mcaTitle='Betonung &mdash; und was sich mit ihr verschiebt',
    mcbEyebrow='Aktivität 2 · Sinngruppen',
    mcbTitle='Wo Sprache bricht, und warum das zählt',
    mccEyebrow='Aktivität 3 · Pausen und Reparatur',
    mccTitle='Denken oder Stocken?',

    p1why='Die Inhaltswörter &mdash; die, um die es im Satz geht. Länge, Atem '
          'und Schwierigkeit spielen keine Rolle; ein einsilbiges Wort bekommt '
          'den Schlag, sobald es den Punkt trägt.',
    p2why='Jede Fassung bestreitet etwas anderes: betontes Pronomen bestreitet, '
          'dass sie es war; betontes Verb bestreitet den Diebstahl selbst. '
          'Gleiche Wörter, sechs Bedeutungen, allein durch den Schlag.',
    p3why='Flache Betonung überlässt dem Zuhörer die Arbeit, und genau dieser '
          'Aufwand steht in den Deskriptoren. Die einzelnen Wörter können '
          'völlig klar sein und trotzdem Punkte kosten.',
    p4why='<em>RECord</em> das Substantiv, <em>reCORD</em> das Verb &mdash; '
          'ebenso bei <em>present</em>, <em>increase</em> und '
          '<em>contract</em>. Die anderen drei behalten ein Betonungsmuster.',
    p5why='Eine kurze Wortfolge, als eine Bedeutungseinheit gesprochen, meist '
          'drei bis sieben Wörter. Es ist keine Atemzählung und kein '
          'grammatischer Satz, auch wenn ein Satz oft eine Gruppe ist.',
    p6why='Als eine Einheit gesprochen, sagt der Satz, dass du mehrere Brüder '
          'hast, und benennt welchen. Mit Lücken um den Relativsatz sagt er, '
          'du hast einen, und fügt eine Information über ihn an.',
    p7why='An den Fugen. Ein Bruch in der Gruppe sagt dem Prüfer, dass dir ein '
          'Wort fehlt; einer am Ende ist das gesprochene Komma. Kommas sind '
          'ein Anhaltspunkt, keine Regel.',
    p8why='Nach auswendig Gelerntem. Prüfer sind darauf geschult, memorierte '
          'Antworten zu hören, und zwei Minuten ohne Bruch sind eines der '
          'Signale. Natürliche Rede gruppiert und atmet.',
    p9why='Eine kurze Stille an einer Grenze. Die anderen drei machen das '
          'Problem hörbar: ein Füllwort in der Phrase, ein Bruch in einem '
          'Substantiv, ein erstes Wort, bis der Rest kommt.',
    p10why='Beschreib es und mach weiter. Umschreibung wird unter Lexical '
           'Resource belohnt, ein Wort aus der Muttersprache ist kein '
           'Englisch, Fragen ist keine Antwort, und Neuanfangen kostet Zeit.',
    p11why='Nein. Bewertet werden Verständlichkeit und der Aufwand des '
           'Zuhörers. Akzent ist ausdrücklich kein Deskriptor &mdash; und es '
           'gibt kein Muttersprachler-Modell, an dem er gemessen würde.',
    p12why='Die Wörter falsch auszusprechen, auf denen die Antwort steht, denn '
           'genau die braucht der Zuhörer. Akzent, eine Denkpause und ein '
           'ruhiges Tempo kosten gar nichts.',

    sortEyebrow='Aktivität 4 · Was das Kriterium wirklich bewertet',
    sortTitle='Sortiere die sechs Gewohnheiten',
    sortHint='Zieh jede in eine Spalte &mdash; oder klicke ein Element an und '
             'dann die Spalte, in die es soll.',
    sortBin1='Kostet Punkte',
    sortBin2='Kostet nichts',

    actTitle='Sprich &mdash; und werde verstanden',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu zweit, mit der Karte aus Teil 2. Lies deinem Partner '
                  'eine vierzeilige Antwort absichtlich flach vor, dann noch '
                  'einmal in Sinngruppen mit dem Schlag auf den '
                  'Inhaltswörtern. Dein Partner sagt, was sich geändert hat.',
    actSpeak1='Sag &bdquo;I didn&rsquo;t say she stole the money&ldquo; '
              'sechsmal, je ein Schlag. Dein Partner nennt, was du bestreitest.',
    actSpeak2='Nimm eine Teil-3-Frage und beantworte sie in Gruppen von drei '
              'bis sieben Wörtern &mdash; Pause nur an den Fugen.',
    actSpeak3='Lass deinen Partner mit einem Wort dazwischengehen, das du '
              'nicht kennst. Rede darum herum und behalte das Wort &mdash; '
              'kein Anhalten, kein Fragen.',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Schreib eine Zwei-Minuten-Antwort auf und markiere sie: ein '
                  'Schrägstrich an jeder Gruppengrenze und Großbuchstaben auf '
                  'dem Wort, das in jeder Gruppe den Schlag trägt. Lies laut '
                  'und prüfe, ob die Schläge dort landen, wo die Bedeutung ist.',
    actPlaceholder='The place I would recommend / is a small town…',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Pronunciación <em>y fluidez</em>',
    coverSub='Una cuarta parte de la nota, y la que nadie practica: acento '
             'tónico, grupos de sentido y la pausa que suena a pensar',
    chipLevel='C1 · Avanzado', chipFocus='Speaking · las tres partes',
    chipCount='18 puntos',

    t1Eyebrow='Antes de empezar',
    t1Title='No es un examen de acento. Nunca lo fue.',
    t1ah='Qué se califica de verdad',
    t1ab='Los descriptores preguntan con qué facilidad se te entiende, si '
         'controlas los rasgos que llevan el significado y cuánto esfuerzo le '
         'cuesta a quien escucha. Sonar británico no está en ninguna lista.',
    t1an='Aquí se pierden más puntos por una entonación plana que por el '
         'acento.',
    t1bh='El acento tónico marca el sentido',
    t1bb='El inglés pone el golpe en las palabras que llevan la idea y deja '
         'correr el resto. Si lo aplanas, cada palabra llega con el mismo '
         'peso y quien escucha tiene que deducir la idea solo.',
    t1bn='Dos sílabas, dos palabras: <em>RECord</em> es el sustantivo, '
         '<em>reCORD</em> el verbo.',
    t1ch='Seis frases, seis palabras',
    t1cb='&laquo;I didn&rsquo;t say she stole the money&raquo; significa seis '
         'cosas distintas según qué palabra reciba el golpe. Las palabras no '
         'cambian nunca; solo cambia la acentuación.',
    t1cn='Pruébalas las seis en voz alta. Cada versión niega algo distinto.',

    t2Eyebrow='Antes de empezar',
    t2Title='El habla llega en grupos, no en palabras',
    t2ah='El grupo de sentido',
    t2ab='El inglés fluido llega en tiradas cortas de palabras dichas como una '
         'unidad, con una pequeña separación entre ellas. Esa separación no es '
         'una duda: es la puntuación de la lengua hablada.',
    t2an='De tres a siete palabras es el tamaño natural de un grupo.',
    t2bh='El límite lleva significado',
    t2bb='Mueve la separación y mueves el sentido. El límite de grupo hace lo '
         'mismo que una coma en el papel, y colocado donde no toca despista a '
         'quien escucha exactamente igual.',
    t2bn='Lee en voz alta una frase escrita: las comas suelen enseñarte dónde '
         'acaban los grupos.',
    t2ch='Dentro de un grupo, sigue',
    t2cb='La separación dentro de un grupo es la que suena a problema: parar '
         'en mitad de un sintagma nominal le dice al examinador que has '
         'perdido la palabra, no que estás sopesando una idea.',
    t2cn='Pausa en las juntas, no dentro de las piezas.',

    t3Eyebrow='Antes de empezar',
    t3Title='La pausa, y qué metes dentro',
    t3ah='El silencio está permitido',
    t3ab='Un silencio breve al final de un grupo suena a estar pensando. El '
         'mismo silencio en mitad de una frase suena a búsqueda de palabra. El '
         'problema no es la pausa: es dónde cae.',
    t3an='Dos segundos en una junta no llaman la atención. Dos segundos dentro '
         'de una frase, sí.',
    t3bh='Las muletillas son peores que el silencio',
    t3bb='<em>Errrm</em> y repetir la primera palabra señalan el problema. Una '
         'pausa limpia, no. Si necesitas un momento, tómalo en silencio o di '
         'que te lo estás tomando.',
    t3bn='<em>That is a good question, actually</em> compra el mismo tiempo y '
         'no cuesta nada.',
    t3ch='Rodea la palabra que has perdido',
    t3cb='Si la palabra no llega, describe qué hace esa cosa y conserva el '
         'turno. La paráfrasis puntúa en Lexical Resource; quedarse parado '
         'puntúa en Fluency, y no a tu favor.',
    t3cn='Nunca pares para pedirle una palabra al examinador. No te la va a '
         'dar.',

    mcaEyebrow='Actividad 1 · Dónde cae el golpe',
    mcaTitle='El acento tónico y lo que se mueve con él',
    mcbEyebrow='Actividad 2 · Grupos de sentido',
    mcbTitle='Dónde se corta el habla, y por qué importa',
    mccEyebrow='Actividad 3 · Pausas y reparación',
    mccTitle='¿Pensando o atascado?',

    p1why='Las palabras con contenido, las que dicen de qué va la frase. La '
          'longitud, la respiración y la dificultad no cuentan: una palabra de '
          'una sílaba se lleva el golpe si carga con la idea.',
    p2why='Cada versión niega una parte distinta: acentuar el pronombre niega '
          'que fuera ella; acentuar el verbo niega el robo. Las mismas '
          'palabras, seis sentidos, todo a cargo del golpe.',
    p3why='La acentuación plana deja el trabajo a quien escucha, y ese '
          'esfuerzo está escrito en los descriptores. Las palabras sueltas '
          'pueden oírse perfectamente y aun así costar puntos.',
    p4why='<em>RECord</em> el sustantivo, <em>reCORD</em> el verbo, y lo mismo '
          'pasa con <em>present</em>, <em>increase</em> y <em>contract</em>. '
          'Las otras tres mantienen un solo patrón.',
    p5why='Una tirada corta de palabras dicha como una unidad de sentido, casi '
          'siempre de tres a siete. No es un recuento de respiraciones ni una '
          'oración gramatical, aunque una oración suele ser un grupo.',
    p6why='Dicha como una sola unidad, la frase dice que tienes varios '
          'hermanos e identifica cuál. Con separaciones a ambos lados de la '
          'relativa, dice que tienes uno y añade un dato sobre él.',
    p7why='En las juntas. Un corte dentro del grupo le dice al examinador que '
          'has perdido una palabra; uno al final es la coma hablada. Las comas '
          'orientan, no mandan.',
    p8why='A respuesta aprendida de memoria. A los examinadores se les entrena '
          'para detectarla, y dos minutos sin un solo corte es una de las '
          'señales. El habla natural agrupa y respira.',
    p9why='Un silencio breve en un límite. Las otras tres anuncian el '
          'problema: una muletilla dentro de la frase, un corte dentro de un '
          'sustantivo y una primera palabra repetida hasta que llega el resto.',
    p10why='Descríbelo y sigue. La paráfrasis se premia en Lexical Resource, '
           'una palabra de tu idioma no es inglés, preguntar no es responder, '
           'y volver a empezar gasta el tiempo que tienes.',
    p11why='No. Se califican la inteligibilidad y el esfuerzo de quien '
           'escucha. El acento no es un descriptor, y no hay un modelo nativo '
           'contra el que medirlo.',
    p12why='Pronunciar mal las palabras sobre las que se sostiene la '
           'respuesta, porque son las que quien escucha necesita. El acento, '
           'una pausa para pensar y un ritmo tranquilo no cuestan nada.',

    sortEyebrow='Actividad 4 · Qué califica de verdad el criterio',
    sortTitle='Clasifica las seis costumbres',
    sortHint='Arrastra cada una a una columna &mdash; o haz clic en un '
             'elemento y luego en la columna que quieras.',
    sortBin1='Te cuesta puntos',
    sortBin2='No te cuesta nada',

    actTitle='Dilo y hazte seguir',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas, con la tarjeta del turno largo de la Parte 2. '
                  'Léele a tu compañero una respuesta de cuatro líneas, plana '
                  'a propósito, y luego otra vez en grupos de sentido con el '
                  'golpe en las palabras con contenido. Que diga qué cambió.',
    actSpeak1='Di &laquo;I didn&rsquo;t say she stole the money&raquo; seis '
              'veces, un golpe cada vez. Tu compañero dice qué has negado.',
    actSpeak2='Coge una pregunta de la Parte 3 y respóndela en grupos de tres '
              'a siete palabras, pausando solo en las juntas.',
    actSpeak3='Que tu compañero te interrumpa con una palabra que no conozcas. '
              'Rodéala y conserva el turno: sin parar y sin preguntar.',
    actWriteKind='Escritura · 150–200 palabras',
    actWriteBrief='Escribe una respuesta de dos minutos y márcala: una barra '
                  'en cada límite de grupo y mayúsculas en la palabra que '
                  'lleva el golpe en cada grupo. Léela en voz alta y comprueba '
                  'que los golpes caen donde está el significado.',
    actPlaceholder='The place I would recommend / is a small town…',
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
