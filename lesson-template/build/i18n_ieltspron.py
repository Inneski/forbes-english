# -*- coding: utf-8 -*-
"""Interface strings for IELTS Pronunciation & fluency.

Ten languages: English, German and Spanish from the start; French,
Italian, Portuguese, Russian, Arabic, Chinese and Japanese added on
2026-09-24 (conventions in `ielts_langs.py`).

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
from ielts_langs import TAIL_MORE

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

TAIL.update(TAIL_MORE)

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
    t1ch='One sentence, six meanings',
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
           'answering, and restarting spends the time you have.',
    p11why='Not in itself. The descriptors mention accent only for its '
           'effect: at band 8 an L1 accent has minimal effect on '
           'intelligibility, at band 9 none. What is scored is how easily you '
           'are followed, and there is no native model to be measured against.',
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
    actWriteKind='Writing · 200–250 words',
    actWriteBrief='Write out a two-minute answer, then mark it up: a slash at '
                  'every group boundary and capitals on the word that takes '
                  'the beat in each group. Read it back and check the beats '
                  'land where the meaning is.',
    actPlaceholder='The place I would recommend / is a small town…',
)

# The sort explanation sits in the data module, which keeps the only copy
# of the English. It was a plain string there until 2026-09-23, so German and
# Spanish learners read it in English.
from ieltspron_data import SORT_WHY
T['en']['sortWhy'] = SORT_WHY

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
    t1ch='Ein Satz, sechs Bedeutungen',
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
    p11why='Nicht an sich. Die Deskriptoren nennen den Akzent nur wegen '
           'seiner Wirkung: in Band 8 beeinträchtigt ein L1-Akzent die '
           'Verständlichkeit kaum, in Band 9 gar nicht. Bewertet wird, wie '
           'leicht man dir folgt &mdash; ein Muttersprachler-Modell, an dem '
           'gemessen würde, gibt es nicht.',
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
    actWriteKind='Schreiben · 200–250 Wörter',
    actWriteBrief='Schreib eine Zwei-Minuten-Antwort auf und markiere sie: ein '
                  'Schrägstrich an jeder Gruppengrenze und Großbuchstaben auf '
                  'dem Wort, das in jeder Gruppe den Schlag trägt. Lies laut '
                  'und prüfe, ob die Schläge dort landen, wo die Bedeutung ist.',
    actPlaceholder='The place I would recommend / is a small town…',

    # The sort explanation; English from the data module.
    sortWhy='In der linken Spalte geht es darum, ob man dir folgen kann; in '
            'der rechten darum, ob du wie jemand anderes klingst. Bewertet wird '
            'nur das Erste. Wer am Akzent arbeitet und die Betonung flach '
            'lässt, hat die Übungszeit in die Spalte gesteckt, die keine Punkte '
            'bringt.',
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
    t1ch='Una frase, seis significados',
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
    p11why='No por sí mismo. Los descriptores mencionan el acento solo por su '
           'efecto: en la banda 8 un acento L1 apenas afecta a la '
           'inteligibilidad, y en la 9 no la afecta. Se califica lo fácil que '
           'es seguirte, y no hay un modelo nativo contra el que medirlo.',
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
    actWriteKind='Escritura · 200–250 palabras',
    actWriteBrief='Escribe una respuesta de dos minutos y márcala: una barra '
                  'en cada límite de grupo y mayúsculas en la palabra que '
                  'lleva el golpe en cada grupo. Léela en voz alta y comprueba '
                  'que los golpes caen donde está el significado.',
    actPlaceholder='The place I would recommend / is a small town…',

    # The sort explanation; English from the data module.
    sortWhy='La columna izquierda trata de si quien escucha puede seguirte; la '
            'derecha, de si suenas como otra persona. Solo lo primero puntúa. '
            'Quien trabaja su acento y deja plana la acentuación ha gastado la '
            'práctica en la columna que no da puntos.',
)


# ── French ─────────────────────────────────────────────────────────────
T['fr'] = dict(
    coverTitle='Pronunciation <em>&amp; Fluency</em>',
    coverSub='Un quart des points, et le quart que personne ne travaille : '
             'l’accent de mot, le découpage, et la pause qui passe pour de la '
             'réflexion',
    chipLevel='C1 · Avancé', chipFocus='Speaking · les trois parties',
    chipCount='18 points',

    t1Eyebrow='Avant de commencer',
    t1Title='Ce n’est pas un test d’accent. Ça ne l’a jamais été.',
    t1ah='Ce qui est vraiment noté',
    t1ab='Les descripteurs demandent avec quelle facilité on vous comprend, si '
         'vous maîtrisez les traits qui portent le sens, et combien d’effort '
         'l’auditeur doit fournir. Avoir l’air britannique ne figure sur aucune '
         'de ces listes.',
    t1an='Ici, les candidats perdent des points bien plus souvent pour une '
         'accentuation plate que pour un accent.',
    t1bh='L’accentuation marque le sens',
    t1bb='L’anglais met le temps fort sur les mots qui portent l’idée et laisse '
         'filer le reste. Aplatissez cela et chaque mot arrive avec le même '
         'poids : l’auditeur doit trouver l’idée tout seul.',
    t1bn='Deux syllabes, deux mots : <em>RECord</em> est le nom, <em>reCORD</em> '
         'le verbe.',
    t1ch='Une phrase, six sens',
    t1cb='&ldquo;I didn&rsquo;t say she stole the money&rdquo; veut dire six '
         'choses différentes selon le mot qui porte le temps fort. Les mots ne '
         'changent jamais ; seule l’accentuation change.',
    t1cn='Essayez à voix haute les six versions. Chacune nie quelque chose de '
         'différent.',

    t2Eyebrow='Avant de commencer',
    t2Title='La parole arrive par groupes, pas mot à mot',
    t2ah='Le groupe de sens',
    t2ab='L’anglais fluide se présente en courtes suites de mots dites d’un seul '
         'tenant, avec une petite coupure entre elles. La coupure n’est pas une '
         'hésitation &mdash; c’est la ponctuation de la langue parlée.',
    t2an='Trois à sept mots environ, c’est la taille naturelle d’un groupe.',
    t2bh='La frontière porte du sens',
    t2bb='Déplacez la coupure et vous déplacez le sens. La frontière de groupe '
         'fait le même travail qu’une virgule à l’écrit, et la mettre au mauvais '
         'endroit induit l’auditeur en erreur de la même façon.',
    t2bn='Lisez une phrase écrite à voix haute : les virgules vous montrent en '
         'général où finissent les groupes.',
    t2ch='À l’intérieur d’un groupe, continuez',
    t2cb='Une coupure à l’intérieur d’un groupe est celle qui trahit une '
         'difficulté : s’arrêter au milieu d’un groupe nominal dit à '
         'l’examinateur que vous avez perdu le mot, pas que vous pesez une idée.',
    t2cn='Faites vos pauses aux jointures, pas au milieu des morceaux.',

    t3Eyebrow='Avant de commencer',
    t3Title='La pause, et ce que vous y mettez',
    t3ah='Le silence est permis',
    t3ab='Un court silence à la fin d’un groupe passe pour de la réflexion. Le '
         'même silence au milieu d’une expression passe pour la recherche d’un '
         'mot. Le problème n’est pas la pause &mdash; c’est sa place.',
    t3an='Deux secondes à une jointure passent inaperçues. Deux secondes au '
         'milieu d’une expression s’entendent.',
    t3bh='Les tics sont pires que le silence',
    t3bb='<em>Errrm</em> et un premier mot répété attirent l’attention sur la '
         'difficulté. Une coupure nette, non. Si vous avez besoin d’un instant, '
         'prenez-le en silence &mdash; ou dites que vous le prenez.',
    t3bn='<em>That is a good question, actually</em> fait gagner le même temps '
         'et ne coûte rien.',
    t3ch='Contournez le mot perdu',
    t3cb='Si le mot ne vient pas, décrivez ce que fait la chose et gardez la '
         'parole. La reformulation est notée en Lexical Resource ; s’arrêter net '
         'est noté en Fluency, et pas avec indulgence.',
    t3cn='Ne vous arrêtez jamais pour demander un mot à l’examinateur. Il ne vous '
         'le donnera pas.',

    mcaEyebrow='Activité 1 · Où tombe le temps fort',
    mcaTitle='L’accentuation, et ce qui bouge quand elle bouge',
    mcbEyebrow='Activité 2 · Les groupes de sens',
    mcbTitle='Où la parole se coupe, et pourquoi c’est important',
    mccEyebrow='Activité 3 · Pauses et réparations',
    mccTitle='Réflexion, ou blocage ?',

    p1why='Les mots de contenu &mdash; ceux dont parle vraiment la phrase. La '
          'longueur, le souffle et la difficulté n’y sont pour rien ; un mot '
          'd’une syllabe prend le temps fort dès qu’il porte l’idée.',
    p2why='Chaque version nie une partie différente : accentuer le pronom nie que '
          'ce soit elle, accentuer le verbe nie le vol lui-même. Mêmes mots, six '
          'sens, portés entièrement par le temps fort.',
    p3why='Une accentuation plate laisse l’auditeur trouver l’idée seul, et '
          'l’effort de l’auditeur est inscrit dans les descripteurs. Les mots '
          'pris un à un peuvent être parfaitement clairs et coûter quand même des '
          'points.',
    p4why='<em>RECord</em> le nom, <em>reCORD</em> le verbe &mdash; et le même '
          'déplacement se retrouve dans <em>present</em>, <em>increase</em> et '
          '<em>contract</em>. Les trois autres gardent une seule accentuation.',
    p5why='Une courte suite de mots dite comme une seule unité de sens, en '
          'général de trois à sept mots. Ce n’est ni un décompte de souffle ni une '
          'proposition grammaticale, même si une proposition forme souvent un '
          'groupe.',
    p6why='Dite d’un seul tenant, la phrase dit que vous avez plusieurs frères et '
          'précise lequel. Coupée de part et d’autre de la relative, elle dit que '
          'vous en avez un seul et ajoute un fait à son sujet.',
    p7why='Aux jointures. Une coupure à l’intérieur d’un groupe dit à '
          'l’examinateur que vous avez perdu un mot ; une coupure à la fin d’un '
          'groupe est l’équivalent oral d’une virgule. Les virgules sont un '
          'repère, pas la règle.',
    p8why='Comme une réponse répétée d’avance. Les examinateurs sont formés pour '
          'entendre ce qui a été appris par cœur, et un débit sans coupure '
          'pendant deux minutes est l’un des signaux. La parole naturelle se '
          'groupe et respire.',
    p9why='Un court silence à une frontière. Les trois autres affichent toutes la '
          'difficulté : un tic au milieu d’une expression, une coupure au milieu '
          'd’un nom, et un premier mot répété jusqu’à ce que la suite arrive.',
    p10why='Décrivez-le et continuez. La reformulation est récompensée en Lexical '
           'Resource, un mot de votre langue n’est pas de l’anglais, demander '
           'n’est pas répondre, et recommencer dépense le temps dont vous '
           'disposez.',
    p11why='Pas en soi. Les descripteurs ne mentionnent l’accent que pour son '
           'effet : au band 8, un accent de langue maternelle a un effet minime sur '
           'l’intelligibilité, au band 9 aucun. Ce qui est noté, c’est la '
           'facilité avec laquelle on vous suit, et il n’y a aucun modèle natif '
           'auquel être comparé.',
    p12why='Mal prononcer les mots sur lesquels repose la réponse, parce que ce '
           'sont ceux dont l’auditeur a besoin. L’accent, une pause de réflexion '
           'et un débit posé ne coûtent rien du tout.',

    sortEyebrow='Activité 4 · Ce que le critère note vraiment',
    sortTitle='Classez les six habitudes',
    sortHint='Faites glisser chacune dans une colonne &mdash; ou cliquez sur '
             'un élément, puis sur la colonne voulue.',
    sortBin1='Vous coûte des points',
    sortBin2='Ne vous coûte rien',
    sortWhy='La colonne de gauche concerne la question de savoir si l’auditeur '
            'peut vous suivre ; celle de droite, si vous ressemblez à quelqu’un '
            'd’autre. Seule la première est notée. Un candidat qui travaille son '
            'accent et laisse son accentuation plate a consacré son entraînement '
            'à la colonne qui ne rapporte aucun point.',

    actTitle='Dites-le, et soyez suivi',
    actUse='Utilisez-en au moins trois :',
    actSpeakBrief='À deux, avec la carte de monologue de la Partie 2. Lisez à '
                  'votre partenaire une réponse de quatre lignes, volontairement '
                  'plate, puis relisez-la par groupes de sens avec le temps fort '
                  'sur les mots de contenu. Votre partenaire dit ce qui a changé.',
    actSpeak1='Dites &ldquo;I didn&rsquo;t say she stole the money&rdquo; six '
              'fois, un temps fort différent à chaque fois. Votre partenaire dit '
              'ce que vous avez nié.',
    actSpeak2='Prenez une question de Partie 3 et répondez par groupes de trois à '
              'sept mots, en ne faisant de pauses qu’aux jointures.',
    actSpeak3='Demandez à votre partenaire de vous interrompre avec un mot que vous '
              'ne connaissez pas. Contournez-le et gardez la parole &mdash; sans '
              'vous arrêter, sans demander.',
    actWriteKind='Écriture · 200–250 mots',
    actWriteBrief='Rédigez une réponse de deux minutes, puis annotez-la : une '
                  'barre oblique à chaque frontière de groupe et des majuscules '
                  'sur le mot qui porte le temps fort dans chaque groupe. '
                  'Relisez-la et vérifiez que les temps forts tombent là où est '
                  'le sens.',
    actPlaceholder='The place I would recommend / is a small town…',
)


# ── Italian ────────────────────────────────────────────────────────────
T['it'] = dict(
    coverTitle='Pronunciation <em>&amp; Fluency</em>',
    coverSub='Un quarto dei punti, e il quarto che nessuno allena: l’accento di '
             'parola, i gruppi di senso, e la pausa che sembra riflessione',
    chipLevel='C1 · Avanzato', chipFocus='Speaking · tutte e tre le parti',
    chipCount='18 punti',

    t1Eyebrow='Prima di cominciare',
    t1Title='Non è un test di accento. Non lo è mai stato.',
    t1ah='Che cosa viene valutato davvero',
    t1ab='I descrittori chiedono quanto facilmente ti si capisce, se controlli '
         'i tratti che portano il significato, e quanto sforzo deve fare chi '
         'ascolta. Sembrare britannico non compare in nessuno di questi elenchi.',
    t1an='Qui i candidati perdono punti molto più spesso per un accento di '
         'parola piatto che per l’accento regionale.',
    t1bh='L’accento di parola segna il significato',
    t1bb='L’inglese mette il battito sulle parole che portano il punto e lascia '
         'scorrere leggero il resto. Appiattisci tutto e ogni parola arriva con '
         'lo stesso peso, così chi ascolta deve trovare il punto da solo.',
    t1bn='Due sillabe, due parole: <em>RECord</em> è il nome, <em>reCORD</em> il '
         'verbo.',
    t1ch='Una frase, sei significati',
    t1cb='&ldquo;I didn&rsquo;t say she stole the money&rdquo; vuol dire sei cose '
         'diverse a seconda della parola che prende il battito. Le parole non '
         'cambiano mai; cambia solo l’accento.',
    t1cn='Prova ad alta voce tutte e sei. Ogni versione nega qualcosa di '
         'diverso.',

    t2Eyebrow='Prima di cominciare',
    t2Title='Il parlato arriva a gruppi, non a parole',
    t2ah='Il gruppo di senso',
    t2ab='L’inglese fluente arriva in brevi sequenze di parole dette come '
         'un’unità, con una piccola pausa tra l’una e l’altra. La pausa non è '
         'un’esitazione &mdash; è la punteggiatura della lingua parlata.',
    t2an='Da tre a sette parole circa è la misura naturale di un gruppo.',
    t2bh='Il confine porta significato',
    t2bb='Sposta la pausa e sposti il senso. Il confine del gruppo fa lo stesso '
         'lavoro di una virgola sulla pagina, e metterlo nel posto sbagliato '
         'inganna chi ascolta allo stesso modo.',
    t2bn='Leggi ad alta voce una frase scritta: di solito le virgole ti mostrano '
         'dove finiscono i gruppi.',
    t2ch='Dentro un gruppo, vai avanti',
    t2cb='Una pausa dentro un gruppo è quella che segnala difficoltà: fermarsi a '
         'metà di un sintagma nominale dice all’esaminatore che hai perso la '
         'parola, non che stai soppesando un’idea.',
    t2cn='Fermati nelle giunture, non dentro i pezzi.',

    t3Eyebrow='Prima di cominciare',
    t3Title='La pausa, e che cosa ci metti dentro',
    t3ah='Il silenzio è permesso',
    t3ab='Un breve silenzio alla fine di un gruppo sembra riflessione. Lo stesso '
         'silenzio a metà di un’espressione sembra la ricerca di una parola. Il '
         'problema non è la pausa &mdash; è dove la metti.',
    t3an='Due secondi in una giuntura passano inosservati. Due secondi dentro '
         'un’espressione si sentono.',
    t3bh='I riempitivi sono peggio del silenzio',
    t3bb='<em>Errrm</em> e una prima parola ripetuta attirano l’attenzione sulla '
         'difficoltà. Una pausa pulita no. Se ti serve un momento, prendilo in '
         'silenzio &mdash; oppure di’ che lo stai prendendo.',
    t3bn='<em>That is a good question, actually</em> fa guadagnare lo stesso '
         'tempo e non costa niente.',
    t3ch='Gira intorno alla parola persa',
    t3cb='Se la parola non viene, descrivi che cosa fa la cosa e tieni il turno. '
         'La riformulazione è valutata in Lexical Resource; fermarsi di colpo è '
         'valutato in Fluency, e non con indulgenza.',
    t3cn='Non fermarti mai a chiedere una parola all’esaminatore. Non te la '
         'darà.',

    mcaEyebrow='Attività 1 · Dove cade il battito',
    mcaTitle='L’accento, e che cosa si sposta quando si sposta',
    mcbEyebrow='Attività 2 · I gruppi di senso',
    mcbTitle='Dove si spezza il parlato, e perché conta',
    mccEyebrow='Attività 3 · Pause e recupero',
    mccTitle='Riflessione o blocco?',

    p1why='Le parole piene &mdash; quelle di cui la frase parla davvero. '
          'Lunghezza, respiro e difficoltà non c’entrano; una parola di una '
          'sillaba prende il battito ogni volta che porta il punto.',
    p2why='Ogni versione nega una parte diversa: accentare il pronome nega che '
          'sia stata lei, accentare il verbo nega il furto stesso. Stesse parole, '
          'sei significati, portati interamente dal battito.',
    p3why='Un accento piatto lascia chi ascolta a trovare il punto da solo, e lo '
          'sforzo di chi ascolta è scritto nei descrittori. Le singole parole '
          'possono essere chiarissime e costare comunque punti.',
    p4why='<em>RECord</em> il nome, <em>reCORD</em> il verbo &mdash; e lo stesso '
          'spostamento vale per <em>present</em>, <em>increase</em> e '
          '<em>contract</em>. Le altre tre mantengono un solo accento.',
    p5why='Una breve sequenza di parole detta come un’unica unità di '
          'significato, di solito da tre a sette parole. Non è un conteggio di '
          'respiri né una proposizione grammaticale, anche se spesso una '
          'proposizione forma un gruppo.',
    p6why='Detta come un’unità, la frase dice che hai diversi fratelli e indica '
          'quale. Spezzata ai due lati della relativa, dice che ne hai uno solo e '
          'aggiunge un fatto su di lui.',
    p7why='Nelle giunture. Una pausa dentro un gruppo dice all’esaminatore che '
          'hai perso una parola; una pausa alla fine di un gruppo è l’equivalente '
          'orale di una virgola. Le virgole sono una guida, non la regola.',
    p8why='Come una risposta preparata. Gli esaminatori sono addestrati a '
          'sentire il materiale imparato a memoria, e un parlato senza pause per '
          'due minuti è uno dei segnali. Il parlato naturale si raggruppa e '
          'respira.',
    p9why='Un breve silenzio su un confine. Le altre tre mettono tutte in '
          'mostra la difficoltà: un riempitivo dentro un’espressione, una pausa '
          'dentro un nome, e una prima parola ripetuta finché arriva il resto.',
    p10why='Descrivila e vai avanti. La riformulazione è premiata in Lexical '
           'Resource, una parola della tua lingua non è inglese, chiedere non è '
           'rispondere, e ricominciare consuma il tempo che hai.',
    p11why='Non di per sé. I descrittori citano l’accento solo per il suo '
           'effetto: al band 8 un accento della lingua madre ha un effetto minimo '
           'sulla comprensibilità, al band 9 nessuno. Viene valutato quanto '
           'facilmente ti si segue, e non esiste un modello nativo con cui '
           'confrontarti.',
    p12why='Pronunciare male le parole su cui si regge la risposta, perché sono '
           'quelle di cui chi ascolta ha bisogno. L’accento, una pausa per '
           'pensare e un ritmo misurato non costano niente.',

    sortEyebrow='Attività 4 · Che cosa valuta davvero il criterio',
    sortTitle='Classifica le sei abitudini',
    sortHint='Trascina ciascuna in una colonna &mdash; oppure clicca su un '
             'elemento e poi sulla colonna che vuoi.',
    sortBin1='Ti costa punti',
    sortBin2='Non ti costa niente',
    sortWhy='La colonna di sinistra riguarda la possibilità di chi ascolta di '
            'seguirti; quella di destra, se sembri qualcun altro. Solo la prima '
            'viene valutata. Un candidato che lavora sull’accento e lascia piatto '
            'l’accento di parola ha speso l’allenamento sulla colonna che non '
            'porta punti.',

    actTitle='Dillo, e fatti seguire',
    actUse='Usane almeno tre:',
    actSpeakBrief='In coppia, con la carta del monologo della Parte 2. Leggi al tuo '
                  'compagno una risposta di quattro righe, volutamente piatta, poi '
                  'rileggila a gruppi di senso con il battito sulle parole piene. '
                  'Il tuo compagno dice che cosa è cambiato.',
    actSpeak1='Di’ &ldquo;I didn&rsquo;t say she stole the money&rdquo; sei volte, '
              'con un battito diverso ogni volta. Il tuo compagno dice che cosa '
              'hai negato.',
    actSpeak2='Prendi una domanda della Parte 3 e rispondi a gruppi di tre-sette '
              'parole, fermandoti solo nelle giunture.',
    actSpeak3='Fatti interrompere dal compagno con una parola che non conosci. '
              'Girale intorno e tieni il turno &mdash; senza fermarti, senza '
              'chiedere.',
    actWriteKind='Scrittura · 200–250 parole',
    actWriteBrief='Scrivi una risposta di due minuti, poi annotala: una barra a '
                  'ogni confine di gruppo e le maiuscole sulla parola che prende '
                  'il battito in ogni gruppo. Rileggila e controlla che i battiti '
                  'cadano dove sta il significato.',
    actPlaceholder='The place I would recommend / is a small town…',
)


# ── Portuguese ─────────────────────────────────────────────────────────
T['pt'] = dict(
    coverTitle='Pronunciation <em>&amp; Fluency</em>',
    coverSub='Um quarto da nota, e o quarto que ninguém treina: a acentuação, '
             'os grupos de sentido e a pausa que soa a reflexão',
    chipLevel='C1 · Avançado', chipFocus='Speaking · as três partes',
    chipCount='18 pontos',

    t1Eyebrow='Antes de começar',
    t1Title='Não é um teste de sotaque. Nunca foi.',
    t1ah='O que é realmente avaliado',
    t1ab='Os descritores perguntam com que facilidade te compreendem, se '
         'controlas os traços que transportam o significado e quanto esforço '
         'tem de fazer quem ouve. Soar britânico não consta de nenhuma dessas '
         'listas.',
    t1an='Aqui, os candidatos perdem pontos muito mais vezes por uma '
         'acentuação plana do que pelo sotaque.',
    t1bh='A acentuação marca o significado',
    t1bb='O inglês põe a batida nas palavras que transportam a ideia e deixa o '
         'resto correr leve. Se achatares isso, cada palavra chega com o mesmo '
         'peso, e quem ouve tem de descobrir a ideia sozinho.',
    t1bn='Duas sílabas, duas palavras: <em>RECord</em> é o nome, '
         '<em>reCORD</em> é o verbo.',
    t1ch='Uma frase, seis significados',
    t1cb='&ldquo;I didn&rsquo;t say she stole the money&rdquo; quer dizer seis '
         'coisas diferentes consoante a palavra que leva a batida. As palavras '
         'nunca mudam; só muda a acentuação.',
    t1cn='Experimenta em voz alta as seis versões. Cada uma nega uma coisa '
         'diferente.',

    t2Eyebrow='Antes de começar',
    t2Title='A fala chega em grupos, não palavra a palavra',
    t2ah='O grupo de sentido',
    t2ab='O inglês fluente vem em sequências curtas de palavras ditas como uma '
         'unidade, com uma pequena pausa entre elas. A pausa não é uma hesitação '
         '&mdash; é a pontuação da língua falada.',
    t2an='Cerca de três a sete palavras é o tamanho natural de um grupo.',
    t2bh='A fronteira transporta significado',
    t2bb='Muda a pausa de sítio e mudas o sentido. A fronteira do grupo faz o '
         'mesmo trabalho que uma vírgula no papel, e pô-la no sítio errado engana '
         'quem ouve da mesma maneira.',
    t2bn='Lê uma frase escrita em voz alta: normalmente as vírgulas mostram-te '
         'onde acabam os grupos.',
    t2ch='Dentro de um grupo, continua',
    t2cb='Uma pausa dentro de um grupo é a que soa a dificuldade: parar a meio '
         'de um sintagma nominal diz ao examinador que perdeste a palavra, não '
         'que estás a ponderar uma ideia.',
    t2cn='Faz as pausas nas junções, não dentro das peças.',

    t3Eyebrow='Antes de começar',
    t3Title='A pausa, e o que lá pões',
    t3ah='O silêncio é permitido',
    t3ab='Um silêncio curto no fim de um grupo soa a reflexão. O mesmo silêncio '
         'a meio de uma expressão soa à procura de uma palavra. O problema não é '
         'a pausa &mdash; é o sítio onde está.',
    t3an='Dois segundos numa junção passam despercebidos. Dois segundos dentro '
         'de uma expressão ouvem-se.',
    t3bh='As muletas são piores do que o silêncio',
    t3bb='<em>Errrm</em> e uma primeira palavra repetida chamam a atenção para '
         'a dificuldade. Uma pausa limpa, não. Se precisares de um momento, '
         'toma-o em silêncio &mdash; ou diz que o estás a tomar.',
    t3bn='<em>That is a good question, actually</em> ganha o mesmo tempo e não '
         'custa nada.',
    t3ch='Contorna a palavra que perdeste',
    t3cb='Se a palavra não vier, descreve o que a coisa faz e não percas a vez. '
         'A paráfrase é avaliada em Lexical Resource; parar de repente é '
         'avaliado em Fluency, e não com brandura.',
    t3cn='Nunca pares para pedir uma palavra ao examinador: não ta vai dar.',

    mcaEyebrow='Atividade 1 · Onde cai a batida',
    mcaTitle='A acentuação, e o que se move quando ela se move',
    mcbEyebrow='Atividade 2 · Grupos de sentido',
    mcbTitle='Onde a fala se parte, e porque é que isso importa',
    mccEyebrow='Atividade 3 · Pausas e reparação',
    mccTitle='A pensar, ou encravado?',

    p1why='As palavras de conteúdo &mdash; aquelas de que a frase realmente '
          'trata. O comprimento, a respiração e a dificuldade nada têm a ver com '
          'isso; uma palavra de uma sílaba leva a batida sempre que transporta a '
          'ideia.',
    p2why='Cada versão nega uma parte diferente: acentuar o pronome nega que '
          'tenha sido ela, acentuar o verbo nega o próprio roubo. As mesmas '
          'palavras, seis significados, transportados inteiramente pela batida.',
    p3why='Uma acentuação plana deixa quem ouve a descobrir a ideia sozinho, e o '
          'esforço de quem ouve está escrito nos descritores. As palavras, uma a '
          'uma, podem ser perfeitamente claras e mesmo assim custar pontos.',
    p4why='<em>RECord</em> o nome, <em>reCORD</em> o verbo &mdash; e a mesma '
          'mudança acontece em <em>present</em>, <em>increase</em> e '
          '<em>contract</em>. As outras três mantêm um só padrão de acentuação.',
    p5why='Uma sequência curta de palavras dita como uma única unidade de '
          'sentido, normalmente de três a sete. Não é uma contagem de '
          'respirações nem uma oração gramatical, embora uma oração seja muitas '
          'vezes um grupo.',
    p6why='Dita como uma unidade, a frase diz que tens vários irmãos e '
          'identifica qual. Partida de um lado e do outro da oração relativa, diz '
          'que tens só um e acrescenta um facto sobre ele.',
    p7why='Nas junções. Uma pausa dentro de um grupo diz ao examinador que '
          'perdeste uma palavra; uma pausa no fim de um grupo é o equivalente '
          'falado de uma vírgula. As vírgulas são uma orientação, não a regra.',
    p8why='Como uma resposta ensaiada. Os examinadores são treinados para '
          'reconhecer material decorado, e uma fala sem pausas durante dois '
          'minutos é um dos sinais. A fala natural agrupa-se e respira.',
    p9why='Um silêncio curto numa fronteira. As outras três anunciam todas a '
          'dificuldade: uma muleta dentro de uma expressão, uma pausa dentro de '
          'um nome e uma primeira palavra repetida até chegar o resto.',
    p10why='Descreve-a e continua. A paráfrase é recompensada em Lexical '
           'Resource, uma palavra da tua língua não é inglês, perguntar não é '
           'responder, e recomeçar gasta o tempo que tens.',
    p11why='Não por si só. Os descritores só mencionam o sotaque pelo seu '
           'efeito: na band 8, um sotaque da língua materna tem um efeito mínimo '
           'na inteligibilidade; na band 9, nenhum. O que é avaliado é a '
           'facilidade com que te seguem, e não há nenhum modelo nativo com que '
           'sejas comparado.',
    p12why='Pronunciar mal as palavras em que assenta a resposta, porque são '
           'essas de que quem ouve precisa. O sotaque, uma pausa para pensar e um '
           'ritmo calmo não custam nada.',

    sortEyebrow='Atividade 4 · O que o critério avalia realmente',
    sortTitle='Classifica os seis hábitos',
    sortHint='Arrasta cada um para uma coluna &mdash; ou clica num elemento e '
             'depois na coluna que quiseres.',
    sortBin1='Custa-te pontos',
    sortBin2='Não te custa nada',
    sortWhy='A coluna da esquerda trata de saber se quem ouve te consegue '
            'seguir; a da direita, de saber se soas como outra pessoa. Só a '
            'primeira é avaliada. Um candidato que trabalha o sotaque e deixa a '
            'acentuação plana gastou o treino na coluna que não dá pontos.',

    actTitle='Di-lo, e faz-te entender',
    actUse='Usa pelo menos três:',
    actSpeakBrief='Em pares, com o cartão do monólogo da Parte 2. Lê ao teu '
                  'colega uma resposta de quatro linhas, deliberadamente plana, e '
                  'depois lê-a outra vez em grupos de sentido, com a batida nas '
                  'palavras de conteúdo. O teu colega diz o que mudou.',
    actSpeak1='Diz &ldquo;I didn&rsquo;t say she stole the money&rdquo; seis '
              'vezes, com uma batida diferente de cada vez. O teu colega diz o que '
              'negaste.',
    actSpeak2='Pega numa pergunta da Parte 3 e responde em grupos de três a sete '
              'palavras, fazendo pausas só nas junções.',
    actSpeak3='Pede ao teu colega que te interrompa com uma palavra que não '
              'conheces. Contorna-a e não percas a vez &mdash; sem parar, sem '
              'perguntar.',
    actWriteKind='Escrita · 200–250 palavras',
    actWriteBrief='Escreve uma resposta de dois minutos e depois marca-a: uma '
                  'barra em cada fronteira de grupo e maiúsculas na palavra que '
                  'leva a batida em cada grupo. Relê-a e verifica se as batidas '
                  'caem onde está o significado.',
    actPlaceholder='The place I would recommend / is a small town…',
)


# ── Russian ────────────────────────────────────────────────────────────
T['ru'] = dict(
    coverTitle='Pronunciation <em>&amp; Fluency</em>',
    coverSub='Четверть баллов, и та четверть, которую никто не тренирует: '
             'ударение, смысловые группы и пауза, которая звучит как размышление',
    chipLevel='C1 · Продвинутый', chipFocus='Speaking · все три части',
    chipCount='18 баллов',

    t1Eyebrow='Прежде чем начать',
    t1Title='Это не тест на акцент. И никогда им не был.',
    t1ah='Что оценивается на самом деле',
    t1ab='Дескрипторы спрашивают, насколько легко вас понять, владеете ли вы '
         'средствами, которые несут смысл, и сколько усилий приходится '
         'прилагать слушателю. Британского звучания нет ни в одном из этих '
         'списков.',
    t1an='Здесь кандидаты теряют баллы из-за речи без фразового ударения '
         'гораздо чаще, чем из-за акцента.',
    t1bh='Ударение отмечает смысл',
    t1bb='Английский ставит сильную долю на слова, которые несут главное, а '
         'остальное произносит легко. Выровняйте всё &mdash; и каждое слово '
         'придёт с одинаковым весом, так что слушателю придётся самому искать '
         'главное.',
    t1bn='Два слога, два слова: <em>RECord</em> &mdash; существительное, '
         '<em>reCORD</em> &mdash; глагол.',
    t1ch='Одно предложение, шесть смыслов',
    t1cb='&ldquo;I didn&rsquo;t say she stole the money&rdquo; означает шесть '
         'разных вещей в зависимости от того, какое слово получает ударение. '
         'Слова не меняются никогда; меняется только ударение.',
    t1cn='Попробуйте вслух все шесть вариантов. Каждый отрицает что-то своё.',

    t2Eyebrow='Прежде чем начать',
    t2Title='Речь идёт группами, а не отдельными словами',
    t2ah='Смысловая группа',
    t2ab='Беглый английский звучит короткими отрезками слов, произнесёнными '
         'как одно целое, с небольшим разрывом между ними. Разрыв &mdash; это '
         'не колебание, а пунктуация устной речи.',
    t2an='Примерно от трёх до семи слов &mdash; естественный размер группы.',
    t2bh='Граница несёт смысл',
    t2bb='Перенесите разрыв &mdash; и перенесёте смысл. Граница группы делает '
         'ту же работу, что запятая на письме, и, поставленная не туда, так же '
         'сбивает слушателя.',
    t2bn='Прочитайте письменное предложение вслух: запятые обычно показывают, '
         'где кончаются группы.',
    t2ch='Внутри группы не останавливайтесь',
    t2cb='Именно разрыв внутри группы выдаёт затруднение: пауза посреди '
         'именной группы говорит экзаменатору, что вы потеряли слово, а не что '
         'вы обдумываете мысль.',
    t2cn='Делайте паузы на стыках, а не внутри кусков.',

    t3Eyebrow='Прежде чем начать',
    t3Title='Пауза, и чем вы её заполняете',
    t3ah='Молчать можно',
    t3ab='Короткое молчание в конце группы звучит как размышление. Такое же '
         'молчание посреди фразы звучит как поиск слова. Проблема не в паузе '
         '&mdash; а в её месте.',
    t3an='Две секунды на стыке никто не замечает. Две секунды внутри фразы '
         'слышны.',
    t3bh='Заполнители пауз хуже тишины',
    t3bb='<em>Errrm</em> и повторённое первое слово привлекают внимание к '
         'затруднению. Чистый разрыв &mdash; нет. Если нужна секунда, возьмите '
         'её молча &mdash; или скажите, что берёте её.',
    t3bn='<em>That is a good question, actually</em> даёт столько же времени и '
         'ничего не стоит.',
    t3ch='Обойдите потерянное слово',
    t3cb='Если слово не приходит, опишите, что эта вещь делает, и продолжайте '
         'говорить. Перефразирование оценивается в Lexical Resource; внезапная '
         'остановка &mdash; в Fluency, и без снисхождения.',
    t3cn='Никогда не останавливайтесь, чтобы спросить слово у экзаменатора. '
         'Вам его не подскажут.',

    mcaEyebrow='Задание 1 · Куда падает ударение',
    mcaTitle='Ударение, и что сдвигается, когда сдвигается оно',
    mcbEyebrow='Задание 2 · Смысловые группы',
    mcbTitle='Где речь делится и почему это важно',
    mccEyebrow='Задание 3 · Паузы и исправления',
    mccTitle='Размышление или заминка?',

    p1why='Знаменательные слова &mdash; те, о которых на самом деле '
          'предложение. Длина, дыхание и сложность тут ни при чём; односложное '
          'слово получает ударение всякий раз, когда несёт главное.',
    p2why='Каждый вариант отрицает свою часть: ударение на местоимении '
          'отрицает, что это была она, ударение на глаголе отрицает саму кражу. '
          'Те же слова, шесть смыслов, и всё держится на ударении.',
    p3why='Речь без ударений оставляет слушателя самого искать главное, а '
          'усилие слушателя прописано в дескрипторах. Отдельные слова могут быть '
          'совершенно понятны и всё равно стоить баллов.',
    p4why='<em>RECord</em> &mdash; существительное, <em>reCORD</em> &mdash; '
          'глагол, и тот же сдвиг есть в <em>present</em>, <em>increase</em> и '
          '<em>contract</em>. Остальные три сохраняют одно ударение.',
    p5why='Короткий отрезок слов, произнесённый как одна смысловая единица, '
          'обычно от трёх до семи слов. Это не подсчёт вдохов и не '
          'грамматическое предложение, хотя предложение часто образует одну '
          'группу.',
    p6why='Произнесённое одной группой, предложение говорит, что у вас '
          'несколько братьев, и уточняет, какой именно. С разрывами по обе '
          'стороны придаточного оно говорит, что брат у вас один, и добавляет о '
          'нём факт.',
    p7why='На стыках. Разрыв внутри группы говорит экзаменатору, что вы '
          'потеряли слово; разрыв в конце группы &mdash; устный аналог запятой. '
          'Запятые &mdash; ориентир, а не правило.',
    p8why='Как заученный ответ. Экзаменаторов учат распознавать выученное '
          'наизусть, и речь без разрывов на протяжении двух минут &mdash; один '
          'из признаков. Естественная речь делится на группы и дышит.',
    p9why='Короткое молчание на границе. Остальные три выставляют затруднение '
          'напоказ: заполнитель внутри фразы, разрыв внутри существительного и '
          'первое слово, повторяемое, пока не придёт остальное.',
    p10why='Опишите его и продолжайте. Перефразирование вознаграждается в '
           'Lexical Resource, слово из родного языка &mdash; не английский, '
           'спросить &mdash; не значит ответить, а начинать заново &mdash; значит '
           'тратить своё время.',
    p11why='Не сам по себе. Дескрипторы упоминают акцент только ради его '
           'эффекта: на band 8 акцент родного языка минимально влияет на '
           'понятность, на band 9 не влияет вовсе. Оценивается то, насколько '
           'легко за вами следить, и нет никакого эталона носителя, с которым '
           'вас сравнивают.',
    p12why='Неправильно произносить слова, на которых держится ответ, потому '
           'что именно они нужны слушателю. Акцент, пауза на размышление и '
           'размеренный темп не стоят ничего.',

    sortEyebrow='Задание 4 · Что критерий оценивает на самом деле',
    sortTitle='Распределите шесть привычек',
    sortHint='Перетащите каждую в столбец &mdash; или нажмите на неё, а затем '
             'на нужный столбец.',
    sortBin1='Стоит вам баллов',
    sortBin2='Ничего вам не стоит',
    sortWhy='Левый столбец &mdash; о том, может ли слушатель следить за вами; '
            'правый &mdash; о том, звучите ли вы как кто-то другой. Оценивается '
            'только первое. Кандидат, который работает над акцентом и оставляет '
            'речь без ударений, потратил тренировку на столбец, который не '
            'приносит баллов.',

    actTitle='Скажите так, чтобы вас поняли',
    actUse='Используйте хотя бы три:',
    actSpeakBrief='В парах, с карточкой монолога из части 2. Прочитайте '
                  'партнёру ответ из четырёх строк нарочно ровно, без ударений, '
                  'а потом ещё раз &mdash; смысловыми группами, с ударением на '
                  'знаменательных словах. Партнёр говорит, что изменилось.',
    actSpeak1='Скажите &ldquo;I didn&rsquo;t say she stole the money&rdquo; шесть '
              'раз, каждый раз с ударением на другом слове. Партнёр называет, что '
              'вы отрицали.',
    actSpeak2='Возьмите вопрос из части 3 и ответьте группами по три&ndash;семь '
              'слов, делая паузы только на стыках.',
    actSpeak3='Пусть партнёр перебьёт вас словом, которого вы не знаете. '
              'Обойдите его и продолжайте говорить &mdash; без остановок и без '
              'вопросов.',
    actWriteKind='Письмо · 200–250 слов',
    actWriteBrief='Напишите ответ на две минуты, а затем разметьте его: косая '
                  'черта на каждой границе группы и заглавные буквы в слове, '
                  'которое несёт ударение в каждой группе. Перечитайте и '
                  'проверьте, что ударения падают туда, где смысл.',
    actPlaceholder='The place I would recommend / is a small town…',
)


# ── Arabic ─────────────────────────────────────────────────────────────
T['ar'] = dict(
    coverTitle='Pronunciation <em>&amp; Fluency</em>',
    coverSub='ربع الدرجات، والربع الذي لا يتدرّب عليه أحد: النبر، والتقسيم إلى '
             'مجموعات معنى، والوقفة التي تبدو تفكيرًا',
    chipLevel='C1 · متقدّم', chipFocus='Speaking · الأجزاء الثلاثة',
    chipCount='18 نقطة',

    t1Eyebrow='قبل أن تبدأ',
    t1Title='ليس اختبارًا للّكنة، ولم يكن كذلك قطّ.',
    t1ah='ما الذي يُقيَّم فعلًا',
    t1ab='تسأل معايير التقييم عن مدى سهولة فهمك، وهل تتحكّم في السمات التي '
         'تحمل المعنى، وكم من الجهد يبذله المستمع. أما أن تبدو بريطانيًا فليس '
         'في أيٍّ من هذه القوائم.',
    t1an='يخسر المرشّحون هنا درجات بسبب الكلام الرتيب بلا نبر أكثر بكثير مما '
         'يخسرونها بسبب اللكنة.',
    t1bh='النبر يحدّد المعنى',
    t1bb='تضع الإنجليزية الضربة القوية على الكلمات التي تحمل الفكرة، وتمرّ على '
         'الباقي خفيفًا. وإن سوّيتَ بينها وصلت كل كلمة بالوزن نفسه، فيضطر '
         'المستمع إلى استخلاص الفكرة وحده.',
    t1bn='مقطعان، وكلمتان: <em>RECord</em> اسم، و<em>reCORD</em> فعل.',
    t1ch='جملة واحدة، وستة معانٍ',
    t1cb='الجملة <bdi>&ldquo;I didn&rsquo;t say she stole the money&rdquo;</bdi> '
         'تعني ستة '
         'أشياء مختلفة بحسب الكلمة التي تأخذ الضربة. الكلمات لا تتغيّر أبدًا؛ '
         'النبر وحده يتغيّر.',
    t1cn='جرّبها بصوت عالٍ في صيغها الست. كل صيغة تنفي شيئًا مختلفًا.',

    t2Eyebrow='قبل أن تبدأ',
    t2Title='الكلام يأتي في مجموعات، لا كلمةً كلمة',
    t2ah='مجموعة المعنى',
    t2ab='تأتي الإنجليزية الطليقة في سلاسل قصيرة من الكلمات تُقال كوحدة واحدة، '
         'بينها فاصل صغير. الفاصل ليس ترددًا &mdash; إنه علامات الترقيم في '
         'اللغة المنطوقة.',
    t2an='من ثلاث كلمات إلى سبع تقريبًا هو الحجم الطبيعي للمجموعة.',
    t2bh='الحدّ يحمل معنى',
    t2bb='حرّك الفاصل تحرّك المعنى. حدّ المجموعة يؤدي العمل نفسه الذي تؤديه '
         'الفاصلة على الورق، ووضعه في المكان الخطأ يضلّل المستمع بالطريقة '
         'نفسها.',
    t2bn='اقرأ جملة مكتوبة بصوت عالٍ، وستُريك الفواصل عادةً أين تنتهي '
         'المجموعات.',
    t2ch='داخل المجموعة، واصل',
    t2cb='الفاصل داخل المجموعة هو الذي يبدو تعثّرًا: التوقف في منتصف عبارة '
         'اسمية يخبر الممتحن أنك فقدت الكلمة، لا أنك تزن فكرة.',
    t2cn='توقّف عند المفاصل، لا داخل القطع.',

    t3Eyebrow='قبل أن تبدأ',
    t3Title='الوقفة، وما تضعه فيها',
    t3ah='الصمت مسموح',
    t3ab='الصمت القصير في نهاية مجموعة يبدو تفكيرًا. والصمت نفسه في منتصف '
         'عبارة يبدو بحثًا عن كلمة. المشكلة ليست في الوقفة &mdash; بل في '
         'موضعها.',
    t3an='ثانيتان عند مفصل لا يلاحظهما أحد. ثانيتان داخل عبارة تُسمعان.',
    t3bh='أصوات الحشو أسوأ من الصمت',
    t3bb='صوت <em>Errrm</em> وتكرار الكلمة الأولى يلفتان الانتباه إلى التعثّر. '
         'أما الفاصل النظيف فلا. إن احتجت لحظة فخذها بهدوء &mdash; أو قل إنك '
         'تأخذها.',
    t3bn='عبارة <em>That is a good question, actually</em> تكسب الوقت نفسه ولا '
         'تكلّف شيئًا.',
    t3ch='التفّ حول الكلمة التي فقدتها',
    t3cb='إن لم تأتِ الكلمة، فصِف ما يفعله الشيء واحتفظ بدورك في الكلام. إعادة '
         'الصياغة تُقيَّم في Lexical Resource، والتوقف التام يُقيَّم في '
         'Fluency، وليس برفق.',
    t3cn='لا تتوقف أبدًا لتطلب كلمة من الممتحن. لن يعطيك إياها.',

    mcaEyebrow='النشاط 1 · أين تقع الضربة',
    mcaTitle='النبر، وما الذي يتحرّك حين يتحرّك',
    mcbEyebrow='النشاط 2 · مجموعات المعنى',
    mcbTitle='أين ينقسم الكلام، ولماذا يهمّ ذلك',
    mccEyebrow='النشاط 3 · الوقفات والإصلاح',
    mccTitle='تفكير، أم تعثّر؟',

    p1why='كلمات المحتوى &mdash; الكلمات التي تدور حولها الجملة فعلًا. لا علاقة '
          'للطول ولا للنَّفَس ولا للصعوبة بذلك؛ فالكلمة ذات المقطع الواحد تأخذ '
          'الضربة كلما حملت الفكرة.',
    p2why='كل صيغة تنفي جزءًا مختلفًا: نبر الضمير ينفي أنها هي، ونبر الفعل ينفي '
          'السرقة نفسها. الكلمات نفسها، وستة معانٍ، تحملها الضربة وحدها.',
    p3why='النبر الرتيب يترك المستمع يستخلص الفكرة وحده، وعبء المستمع مكتوب في '
          'معايير التقييم. قد تكون الكلمات منفردةً واضحة تمامًا، ومع ذلك تكلّف '
          'درجات.',
    p4why='الاسم <em>RECord</em>، والفعل <em>reCORD</em> &mdash; والتحوّل نفسه '
          'يجري في <em>present</em> و<em>increase</em> و<em>contract</em>. أما '
          'الثلاث الأخرى فتحتفظ بنمط نبر واحد.',
    p5why='سلسلة قصيرة من الكلمات تُقال كوحدة معنى واحدة، عادةً من ثلاث كلمات إلى '
          'سبع. ليست عدًّا للأنفاس ولا جملة نحوية، وإن كانت الجملة كثيرًا ما '
          'تشكّل مجموعة واحدة.',
    p6why='حين تُقال كوحدة واحدة، تقول الجملة إن لك عدة إخوة وتحدّد أيّهم. وحين '
          'تُقطع على جانبي جملة الصلة، تقول إن لك أخًا واحدًا وتضيف معلومة '
          'عنه.',
    p7why='عند المفاصل. الفاصل داخل المجموعة يخبر الممتحن أنك فقدت كلمة؛ '
          'والفاصل في نهايتها هو المقابل المنطوق للفاصلة. الفواصل دليل، لا '
          'قاعدة.',
    p8why='كإجابة محفوظة مسبقًا. الممتحنون مدرَّبون على سماع المادة المحفوظة، '
          'والكلام المتصل بلا فواصل لمدة دقيقتين إحدى العلامات. الكلام الطبيعي '
          'ينقسم إلى مجموعات ويتنفّس.',
    p9why='صمت قصير عند حدّ. أما الثلاث الأخرى فكلها تُعلن التعثّر: صوت حشو '
          'داخل عبارة، وفاصل داخل اسم، وكلمة أولى تتكرّر حتى يصل الباقي.',
    p10why='صِفها وواصل. إعادة الصياغة تُكافأ في Lexical Resource، والكلمة من '
           'لغتك الأم ليست إنجليزية، والسؤال ليس إجابة، والبدء من جديد يستهلك '
           'الوقت الذي لديك.',
    p11why='ليس في حدّ ذاتها. لا تذكر معايير التقييم اللكنة إلا من حيث أثرها: '
           'في band 8 يكون للكنة اللغة الأم أثر ضئيل في وضوح الكلام، وفي band 9 '
           'لا أثر لها. ما يُقيَّم هو سهولة متابعتك، ولا يوجد نموذج لمتحدث أصلي '
           'تُقاس عليه.',
    p12why='نطق الكلمات التي تقوم عليها الإجابة نطقًا خاطئًا، لأنها الكلمات التي '
           'يحتاجها المستمع. أما اللكنة، ووقفة التفكير، والإيقاع المتّزن، فلا '
           'تكلّف شيئًا على الإطلاق.',

    sortEyebrow='النشاط 4 · ما الذي يقيّمه المعيار فعلًا',
    sortTitle='صنّف العادات الست',
    sortHint='اسحب كل عادة إلى عمود، أو انقر عليها ثم على العمود الذي تريده.',
    sortBin1='يكلّفك درجات',
    sortBin2='لا يكلّفك شيئًا',
    sortWhy='عمود «يكلّفك درجات» يتعلّق بقدرة المستمع على متابعتك، وعمود «لا '
            'يكلّفك شيئًا» يتعلّق بما إذا كنت تبدو كشخص آخر. الأول وحده '
            'يُقيَّم. والمرشّح الذي يعمل على لكنته ويترك نبره رتيبًا قد أنفق '
            'تدريبه على العمود الذي لا درجات فيه.',

    actTitle='قلها بحيث يتابعك السامع',
    actUse='استخدم ثلاثة منها على الأقل:',
    actSpeakBrief='في أزواج، مع بطاقة الحديث الطويل من الجزء 2. اقرأ لزميلك '
                  'إجابة من أربعة أسطر برتابة متعمَّدة، ثم اقرأها مرة أخرى في '
                  'مجموعات معنى مع الضربة على كلمات المحتوى. يقول زميلك ما الذي '
                  'تغيّر.',
    actSpeak1='قل <bdi>&ldquo;I didn&rsquo;t say she stole the money&rdquo;</bdi> '
              'ست مرات، '
              'بضربة مختلفة في كل مرة. يذكر زميلك ما الذي نفيته.',
    actSpeak2='خذ سؤالًا من الجزء 3 وأجب عنه في مجموعات من ثلاث كلمات إلى سبع، '
              'ولا تتوقف إلا عند المفاصل.',
    actSpeak3='اطلب من زميلك أن يقاطعك بكلمة لا تعرفها. التفّ حولها واحتفظ '
              'بدورك &mdash; بلا توقف، وبلا سؤال.',
    actWriteKind='الكتابة · 200–250 كلمة',
    actWriteBrief='اكتب إجابة مدتها دقيقتان، ثم علّم عليها: خطًا مائلًا عند كل '
                  'حدّ مجموعة، والكلمة التي تأخذ الضربة في كل مجموعة بالأحرف '
                  'الكبيرة. ثم اقرأها مجددًا وتأكد أن الضربات تقع حيث يكون '
                  'المعنى.',
    actPlaceholder='The place I would recommend / is a small town…',
)


# ── Chinese ────────────────────────────────────────────────────────────
T['zh'] = dict(
    coverTitle='Pronunciation <em>&amp; Fluency</em>',
    coverSub='四分之一的分数，也是没人练的那四分之一：重音、意群，以及听起来像在'
             '思考的停顿',
    chipLevel='C1 · 高级', chipFocus='Speaking · 全部三个部分',
    chipCount='18 分',

    t1Eyebrow='开始之前',
    t1Title='这不是口音测试，从来都不是。',
    t1ah='真正评分的是什么',
    t1ab='评分标准问的是：别人理解你有多容易，你能否掌控承载意义的那些语音特征，'
         '以及听者需要付出多少努力。听起来像英国人，不在其中任何一条里。',
    t1an='在这一项上，考生因为重音平淡而丢分，远比因为口音丢分常见。',
    t1bh='重音标出意思',
    t1bb='英语把节拍放在承载要点的词上，其余的轻轻带过。把它说平了，每个词都以'
         '同样的分量到达，听者只能自己去找要点。',
    t1bn='两个音节，两个词：<em>RECord</em> 是名词，<em>reCORD</em> 是动词。',
    t1ch='一句话，六种意思',
    t1cb='&ldquo;I didn&rsquo;t say she stole the money&rdquo; 这句话，节拍落在'
         '哪个词上，意思就不同，一共六种。词从来不变，变的只是重音。',
    t1cn='把六个版本都大声试一遍。每个版本否认的东西都不一样。',

    t2Eyebrow='开始之前',
    t2Title='话是一组一组说出来的，不是一个词一个词',
    t2ah='意群',
    t2ab='流利的英语由一小串一小串的词组成，每串作为一个整体说出，中间有一个小'
         '小的停顿。这个停顿不是犹豫——它是口语的标点。',
    t2an='大约三到七个词，是一个意群的自然长度。',
    t2bh='边界承载意义',
    t2bb='移动停顿，就移动了意思。意群的边界和书面上的逗号做的是同一件事，放错'
         '位置同样会误导听者。',
    t2bn='把一句书面的句子大声读出来，逗号通常会告诉你意群在哪里结束。',
    t2ch='在意群内部，一口气说下去',
    t2cb='意群内部的停顿，才是暴露困难的那种：在名词短语中间停下来，告诉考官的'
         '是你把词忘了，而不是你在斟酌一个想法。',
    t2cn='在接缝处停顿，不要在块的中间停。',

    t3Eyebrow='开始之前',
    t3Title='停顿，以及你在停顿里放什么',
    t3ah='沉默是允许的',
    t3ab='在意群末尾短暂的沉默，听起来像在思考。同样长的沉默出现在短语中间，听'
         '起来像在找词。问题不在停顿——而在停顿的位置。',
    t3an='在接缝处停两秒，没人注意。在短语里面停两秒，谁都听得见。',
    t3bh='填充音比沉默更糟',
    t3bb='<em>Errrm</em> 和重复的第一个词，会把注意力引向你的困难。干净的停顿'
         '不会。如果需要一点时间，就安静地停一下——或者直接说你需要想一想。',
    t3bn='<em>That is a good question, actually</em> 能争取到同样的时间，却没有'
         '任何代价。',
    t3ch='绕过你忘掉的词',
    t3cb='如果那个词想不起来，就描述这个东西是做什么的，并且继续说下去。改述在 '
         'Lexical Resource 中评分；突然卡住在 Fluency 中评分，而且不会手下'
         '留情。',
    t3cn='永远不要停下来问考官某个词怎么说。考官不会告诉你。',

    mcaEyebrow='练习 1 · 节拍落在哪里',
    mcaTitle='重音，以及它移动时什么跟着移动',
    mcbEyebrow='练习 2 · 意群',
    mcbTitle='话在哪里断开，为什么这很重要',
    mccEyebrow='练习 3 · 停顿与补救',
    mccTitle='在思考，还是卡住了？',

    p1why='实词——句子真正在讲的那些词。长度、气息和难度都与此无关；单音节词只'
          '要承载要点，就会得到节拍。',
    p2why='每个版本否认的部分不同：重读代词，否认的是“是她”；重读动词，否认的是'
          '偷窃本身。同样的词，六种意思，完全由节拍承载。',
    p3why='平淡的重音让听者只能自己找要点，而听者的吃力程度就写在评分标准里。每'
          '个词单独听都可能非常清楚，却照样丢分。',
    p4why='<em>RECord</em> 是名词，<em>reCORD</em> 是动词——同样的转移也出现在 '
          '<em>present</em>、<em>increase</em> 和 <em>contract</em> 中。其余三'
          '个只有一种重音模式。',
    p5why='作为一个意义单位说出的一小串词，通常三到七个。它不是按换气来数的，也'
          '不是语法上的分句，虽然一个分句往往就是一个意群。',
    p6why='作为一个整体说出，这句话表示你有几个兄弟，并指明是哪一个。在关系从句'
          '两边断开，它表示你只有一个兄弟，并补充了关于他的一件事。',
    p7why='在接缝处。意群内部的停顿告诉考官你丢了一个词；意群末尾的停顿则相当于'
          '口语里的逗号。逗号是参考，不是规则。',
    p8why='像背好的答案。考官受过训练，能听出背诵的内容，而连续两分钟毫无停顿的'
          '表达正是信号之一。自然的话语会分组，也会换气。',
    p9why='在边界处短暂的沉默。其余三个都在暴露困难：短语里的填充音、名词中间的'
          '停顿，以及反复说第一个词直到后面的话出来。',
    p10why='描述它，然后继续说。改述在 Lexical Resource 中得到奖励；母语里的词'
           '不是英语；发问不是回答；从头再来会耗掉你的时间。',
    p11why='口音本身不会。评分标准提到口音，只是因为它的影响：8 分的描述是母语'
           '口音对可理解度影响极小，9 分则是没有影响。评的是别人跟上你有多容易，'
           '并没有一个母语者的模板来衡量你。',
    p12why='把答案所依靠的词读错，因为那正是听者需要的词。口音、思考时的停顿和从'
           '容的语速，都不会让你丢任何分。',

    sortEyebrow='练习 4 · 这项标准真正评的是什么',
    sortTitle='把六个习惯分类',
    sortHint='把每一项拖到一栏里——或者先点一项，再点你想放进的那一栏。',
    sortBin1='会让你丢分',
    sortBin2='不会让你丢分',
    sortWhy='左边一栏关乎听者能不能跟上你；右边一栏关乎你听起来像不像别人。只有'
            '前者计分。一个考生若苦练口音，却让重音一直平淡，就把练习花在了不计'
            '分的那一栏上。',

    actTitle='说出来，让人跟得上',
    actUse='至少用上三个：',
    actSpeakBrief='两人一组，用第二部分的长篇发言卡。先故意用平淡的语调给同伴读'
                  '一段四行的回答，再按意群重读一遍，把节拍放在实词上。同伴说出'
                  '有什么变化。',
    actSpeak1='把 &ldquo;I didn&rsquo;t say she stole the money&rdquo; 说六遍，'
              '每遍重读不同的词。同伴说出你否认了什么。',
    actSpeak2='选一个第三部分的问题，用三到七个词一组来回答，只在接缝处停顿。',
    actSpeak3='让同伴用一个你不认识的词打断你。绕过它，继续说下去——不停下，也'
              '不发问。',
    actWriteKind='写作 · 200–250 词',
    actWriteBrief='写出一段两分钟的回答，然后做标记：在每个意群边界画一条斜线，'
                  '把每组里得到节拍的词用大写字母写。再读一遍，检查节拍是否落在'
                  '意思所在的地方。',
    actPlaceholder='The place I would recommend / is a small town…',
)


# ── Japanese ───────────────────────────────────────────────────────────
T['ja'] = dict(
    coverTitle='Pronunciation <em>&amp; Fluency</em>',
    coverSub='点数の4分の1、そして誰も練習しない4分の1：強勢、意味のまとまり、'
             'そして考えているように聞こえるポーズ',
    chipLevel='C1 · 上級', chipFocus='Speaking · 全3パート',
    chipCount='18 点',

    t1Eyebrow='始める前に',
    t1Title='なまりのテストではありません。これまでも、ずっと。',
    t1ah='実際に採点されるもの',
    t1ab='評価基準が問うのは、あなたの話がどれだけ楽に理解できるか、意味を運ぶ'
         '特徴をコントロールできているか、そして聞き手がどれだけ努力しなければな'
         'らないかです。イギリス人らしく聞こえることは、どのリストにもありません。',
    t1an='このパートで受験者が点を落とすのは、なまりよりも、平板な強勢のほうが'
         'ずっと多いのです。',
    t1bh='強勢が意味を示す',
    t1bb='英語は、要点を運ぶ語に拍を置き、残りは軽く流します。それを平らにする'
         'と、どの語も同じ重さで届き、聞き手は自力で要点を探さなければなりませ'
         'ん。',
    t1bn='2音節で、2つの語：<em>RECord</em> は名詞、<em>reCORD</em> は動詞です。',
    t1ch='一つの文、六つの意味',
    t1cb='&ldquo;I didn&rsquo;t say she stole the money&rdquo; は、どの語が拍を'
         '取るかによって六つの違う意味になります。語は決して変わらず、変わるのは'
         '強勢だけです。',
    t1cn='六つすべてを声に出して試してみましょう。どれも違うものを否定してい'
         'ます。',

    t2Eyebrow='始める前に',
    t2Title='話し言葉は語ごとではなく、まとまりで届く',
    t2ah='意味のまとまり',
    t2ab='流暢な英語は、一つの単位として言われる短い語の連なりでできていて、そ'
         'の間に小さな区切りがあります。区切りはためらいではありません――話し言'
         '葉の句読点です。',
    t2an='およそ3～7語が、まとまりの自然な長さです。',
    t2bh='境界が意味を運ぶ',
    t2bb='区切りを動かせば、意味が動きます。まとまりの境界は紙の上の読点と同じ'
         '仕事をしていて、間違った場所に置けば同じように聞き手を惑わせます。',
    t2bn='書かれた文を声に出して読むと、たいていは読点がまとまりの終わりを教え'
         'てくれます。',
    t2ch='まとまりの中では、止まらずに',
    t2cb='困っているように聞こえるのは、まとまりの中の区切りです。名詞句の途中'
         'で止まると、考えを吟味しているのではなく、語を見失ったのだと試験官に'
         '伝わります。',
    t2cn='つなぎ目で区切り、かたまりの中では区切らないこと。',

    t3Eyebrow='始める前に',
    t3Title='ポーズと、そこに何を入れるか',
    t3ah='沈黙は許されている',
    t3ab='まとまりの終わりの短い沈黙は、考えているように聞こえます。同じ長さの'
         '沈黙が句の途中にあると、語を探しているように聞こえます。問題はポーズ'
         'ではなく――その位置です。',
    t3an='つなぎ目での2秒は誰も気にしません。句の中での2秒は聞こえてしまい'
         'ます。',
    t3bh='つなぎ言葉は沈黙より悪い',
    t3bb='<em>Errrm</em> や最初の語の繰り返しは、困っていることに注意を向けさせ'
         'ます。きれいな区切りはそうなりません。少し時間が必要なら、静かに取るか'
         '――取っていると口に出しましょう。',
    t3bn='<em>That is a good question, actually</em> なら同じだけ時間を稼げて、'
         '何も失いません。',
    t3ch='見失った語の周りを回って話す',
    t3cb='語が出てこなければ、そのものが何をするかを説明して、話し続けましょう。'
         '言い換えは Lexical Resource で評価され、ぴたりと止まることは Fluency '
         'で評価されます。しかも厳しく。',
    t3cn='試験官に語を尋ねるために止まってはいけません。教えてはもらえません。',

    mcaEyebrow='演習 1 · 拍はどこに落ちるか',
    mcaTitle='強勢と、それが動くときに動くもの',
    mcbEyebrow='演習 2 · 意味のまとまり',
    mcbTitle='話はどこで区切れ、なぜそれが大切か',
    mccEyebrow='演習 3 · ポーズと立て直し',
    mccTitle='考えている？ それとも詰まっている？',

    p1why='内容語――その文が実際に語っている語です。長さや息や難しさは関係あり'
          'ません。1音節の語でも、要点を運ぶときは拍を取ります。',
    p2why='それぞれの版が違う部分を否定します。代名詞に強勢を置けば彼女だったこ'
          'とを否定し、動詞に置けば盗み自体を否定します。同じ語で六つの意味、そ'
          'れを運ぶのは拍だけです。',
    p3why='平板な強勢は、要点を探す仕事を聞き手に任せてしまい、聞き手の負担は評'
          '価基準に書かれています。一つひとつの語がまったく明瞭でも、点を失うこ'
          'とがあります。',
    p4why='<em>RECord</em> は名詞、<em>reCORD</em> は動詞――同じ移動が '
          '<em>present</em>、<em>increase</em>、<em>contract</em> にも見られま'
          'す。ほかの三つは強勢のパターンが一つだけです。',
    p5why='一つの意味の単位として言われる短い語の連なりで、ふつうは3～7語です。'
          '息継ぎの回数でも文法上の節でもありませんが、一つの節がそのまま一つの'
          'まとまりになることはよくあります。',
    p6why='一つの単位として言えば、この文は兄弟が何人かいて、そのうちのどの人か'
          'を特定していることになります。関係節の両側で区切れば、兄弟は一人だけ'
          'で、その人についての事実を付け加えていることになります。',
    p7why='つなぎ目です。まとまりの中の区切りは、語を見失ったと試験官に伝えます。'
          'まとまりの終わりの区切りは、話し言葉の読点にあたります。読点は目安で'
          'あって、規則ではありません。',
    p8why='準備してきた答えのように。試験官は暗記した内容を聞き分ける訓練を受け'
          'ていて、2分間途切れない話し方はその合図の一つです。自然な話し言葉は'
          'まとまりに分かれ、息をつきます。',
    p9why='境界での短い沈黙です。ほかの三つはどれも困っていることを知らせてしま'
          'います：句の中のつなぎ言葉、名詞の途中の区切り、そして続きが出てくる'
          'まで繰り返される最初の語。',
    p10why='説明して、話し続けましょう。言い換えは Lexical Resource で評価されま'
           'す。母語の語は英語ではなく、尋ねることは答えることではなく、言い直'
           'すと持ち時間を使ってしまいます。',
    p11why='それ自体は問題ではありません。評価基準がなまりに触れるのは、その影'
           '響についてだけです：バンド8では母語のなまりが理解しやすさに与える影'
           '響はごくわずか、バンド9ではまったくありません。採点されるのは話のつ'
           'いていきやすさで、比べられるネイティブの手本はありません。',
    p12why='答えの土台になる語を誤って発音することです。聞き手が必要とするのはそ'
           'の語だからです。なまり、考えるためのポーズ、落ち着いた話す速さでは、'
           'まったく点を失いません。',

    sortEyebrow='演習 4 · この基準が実際に採点するもの',
    sortTitle='六つの習慣を分類しましょう',
    sortHint='それぞれを列にドラッグしてください。または項目をクリックしてから、'
             '入れたい列をクリックします。',
    sortBin1='点を失う',
    sortBin2='何も失わない',
    sortWhy='左の列は聞き手があなたの話についていけるかどうか、右の列はあなたが'
            '誰か別の人のように聞こえるかどうかの問題です。採点されるのは前者だ'
            'け。なまりを直す練習をして強勢を平板なままにする受験者は、点になら'
            'ない列に練習を費やしたことになります。',

    actTitle='話して、ついてきてもらう',
    actUse='少なくとも三つ使いましょう：',
    actSpeakBrief='ペアで、パート2のスピーチカードを使います。4行の答えをわざと'
                  '平板にパートナーに読み、次に意味のまとまりごとに、内容語に拍を'
                  '置いてもう一度読みましょう。パートナーは何が変わったかを言い'
                  'ます。',
    actSpeak1='&ldquo;I didn&rsquo;t say she stole the money&rdquo; を、毎回違う'
              '語に拍を置いて6回言いましょう。パートナーはあなたが何を否定した'
              'かを言います。',
    actSpeak2='パート3の質問を一つ選び、3～7語のまとまりで答えましょう。区切るの'
              'はつなぎ目だけです。',
    actSpeak3='パートナーに、あなたの知らない語で割り込んでもらいましょう。その語'
              'の周りを回って話し続けます――止まらず、尋ねずに。',
    actWriteKind='ライティング · 200–250 語',
    actWriteBrief='2分間の答えを書き出し、印をつけましょう：まとまりの境界ごとに'
                  'スラッシュ、各まとまりで拍を取る語は大文字に。読み返して、拍が'
                  '意味のあるところに落ちているか確かめましょう。',
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
