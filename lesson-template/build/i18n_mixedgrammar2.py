# -*- coding: utf-8 -*-
"""Interface strings for the B1 Mixed Grammar Test (Part 2).

English, German and Spanish — the minimum since 2026-09-04. `assemble()`
still defaults to ('en', 'de'), so the builder passes langs explicitly.

What is NOT translated, deliberately (HOUSE-STYLE §8): every question stem,
every option, every story sentence, every sentence chunk and every sentence
to correct, and the six true/false statements, as in Part 1. Those are the
English under test. What translates is the chrome around them — stage names,
slide titles, instructions, glosses, explanations and the activation brief.

The explanations are ported from `mixed_b1_en.py`, `mixed_b1_de.py` and
`mixed_b1_es.py` — the text written for the editorial build (19b39ed) that
this deck supersedes. They follow the house convention: grammar forms in
CAPS, cited words in double quotes, in each language's own quotation marks,
and the English form under discussion stays English inside German and
Spanish text.

Slide titles name the scene, never the grammar point or the answer: a title
reading "If it rains" over an item whose key is "rains" gives the point away.

The builder reads its English from T['en'] rather than repeating it as
literals — two copies of a sentence drift.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

# The template's RPG ledger chrome. This deck has no ledger, but the markup
# that reads these keys ships in every page and the I18N gate fails a page
# whose data-i18n has no English behind it.
TAIL = {
    'en': {'ledClues': "'Clues'", 'ledDp': "'DP'", 'ledTime': "'Time'"},
    'de': {'ledClues': "'Hinweise'", 'ledDp': "'DP'", 'ledTime': "'Zeit'"},
    'es': {'ledClues': "'Pistas'", 'ledDp': "'DP'", 'ledTime': "'Tiempo'"},
}

# The passage, identical in every language: it is the English under test.
# Printed WITH its gaps on the story panel, so the learner reads the whole
# text before answering it in pieces — never with the answers filled in.
STORY_A = ('Diego ______ <em>(travel)</em> to Italy every summer, but this year '
           'he’s trying something different. Last month, he ______ <em>(book)</em> '
           'a flight to Lisbon after a friend ______ <em>(recommend)</em> it. '
           'He ______ <em>(never / visit)</em> Portugal before, so he’s very excited.')
STORY_B = ('Last week, while he ______ <em>(pack)</em> his suitcase, he realised '
           'he’d left his passport at his parents’ house. Next Friday, Diego '
           '______ <em>(fly)</em> from Madrid to Lisbon — he’s already chosen his '
           'seat. If the flight ______ <em>(be)</em> delayed, he ______ '
           '<em>(miss)</em> his hotel check-in time.')

T = {}

# ══════════════════════════════════════════════════════════════════════
#  ENGLISH
# ══════════════════════════════════════════════════════════════════════
T['en'] = dict(
    coverTitle='Mixed Grammar Test <em>Part 2</em>',
    coverSub='Ten more grammar areas, all new sentences — tenses, modals, conditionals, passives and more',
    chipLevel='B1 · Intermediate', chipFocus='Mixed grammar', chipCount='44 slides',
    bankLabel='Word bank:',

    # ── stage dividers ────────────────────────────────────────────────
    d1t='Multiple Choice', d1n='Section 1 · ten new sentences, ten grammar points',
    d2t='Diego’s Trip', d2n='Section 2 · read, then fill the gaps',
    d3t='True or False', d3n='Section 3 · some of these are myths',
    d4t='Build the Sentence', d4n='Section 4 · put the parts in order',
    d5t='Find the Mistake', d5n='Section 5 · one error in each sentence',

    # ── stage eyebrows ────────────────────────────────────────────────
    e1='Multiple choice', e2='Diego’s trip', e3='True or false',
    e4='Build the sentence', e5='Find the mistake',

    # ── section opener panels ─────────────────────────────────────────
    s1t='Ten new sentences',
    s1a='The same ten areas of B1 grammar as Part 1 — tenses, modals, conditionals, the passive, relative clauses — and not one sentence you have seen before.',
    s1b='Read the whole sentence before you choose. The word that decides the answer is usually beside the gap, not in it: “Be quiet!”, “while”, “for ten years now”, “strictly forbidden”.',

    s2t='Read it once, then fill it in',
    s2a='Diego’s story runs from a summer habit to a flight next Friday, so it moves through six tenses without announcing any of them.',
    s2b='Each gap names a verb in brackets. Put it in the form the sentence needs — the time words around it will tell you which.',

    s3t='Six rules, and some of them are wrong',
    s3a='Every statement here is something learners are commonly told. Four are accurate. Two are the kind of half-rule that survives because nobody checks it.',
    s3b='Decide on the rule itself, not on whether the example sounds familiar.',

    s4t='The parts are right, the order is not',
    s4a='Each sentence has been cut at its joints — not into single words, but into the phrases that actually do the grammatical work.',
    s4b='Click a part to place it, click a placed part to take it back. The whole sentence scores one point: half-right word order is not half-right English.',

    s5t='One mistake, one correction',
    s5a='Every sentence below contains exactly one grammar error, and it is the kind a B1 learner makes for a reason rather than by accident.',
    s5b='Type the whole sentence, corrected. Capitals don’t matter, a missing full stop or comma is not a mistake, and the usual contracted forms are accepted.',

    # ── the reading passage ───────────────────────────────────────────
    storyT='Diego’s trip', storyA=STORY_A, storyB=STORY_B,

    # ── multiple choice: the scene, never the answer ──────────────────
    q1t='The baby', q2t='Film night', q3t='Old friends', q4t='A favour',
    q5t='Tokyo', q6t='Indoors', q7t='The machine', q8t='The team',
    q9t='A famous painting', q10t='A good book',
    q6g='“Forbidden” = not allowed by a rule.',

    # ── true or false ─────────────────────────────────────────────────
    t1t='Plans and the Present Continuous', t2t='Mustn’t and don’t have to',
    t3t='Were or was', t4t='Two-syllable adjectives',
    t5t='Active into passive', t6t='Whose',
    tfStem='True or false?',

    # ── reordering ────────────────────────────────────────────────────
    o1t='A passive question', o2t='A relative clause', o3t='A question about time',
    o4t='A second conditional', o5t='A double comparison',
    orderHint='Click the parts in the right order to rebuild the sentence.',

    # ── gaps ──────────────────────────────────────────────────────────
    g1t='Every summer', g2t='Before the trip', g3t='Next Friday',
    g1h='Write the verb in brackets in the correct form.',
    g2h='Write the verb in brackets in the correct form. “Suitcase” = the bag you pack for a trip.',
    g3h='Write the verb in brackets in the correct form. “Delayed” = later than planned.',

    ec1t='You’re right', ec2t='Married', ec3t='A house', ec4t='The exercise',
    ec5t='The email', ec6t='The car',
    ecHint='Type the whole sentence, corrected.',

    # ── activation ────────────────────────────────────────────────────
    actTitle='Now use it',
    actUse='Use at least three of these:',
    actSpeakBrief='In pairs. Take one prompt each and talk for two minutes without stopping, using the grammar in brackets — your partner listens for the forms above and tells you afterwards which ones you actually used.',
    actSpeak1='Your plans for Saturday, and what you’ll do if it rains. (Present Continuous, first conditional)',
    actSpeak2='At work or school: three things you mustn’t do, and three you don’t have to do. (modal verbs)',
    actSpeak3='A trip that went wrong: what were you doing when it happened, and what happened next? (Past Continuous, Past Simple)',
    actWriteKind='Writing',
    actWriteBrief='Write a review for a travel website (150–200 words) of a place you know well. Say how long you have known it, what it is famous for, and why it is the best — or the worst — of its kind.',
    actPlaceholder='I have been to … three times, and …',
)

# ══════════════════════════════════════════════════════════════════════
#  GERMAN
# ══════════════════════════════════════════════════════════════════════
T['de'] = dict(
    coverTitle='Mixed Grammar Test <em>Part 2</em>',
    coverSub='Zehn weitere Grammatikbereiche, alles neue Sätze — Zeiten, Modalverben, Konditionalsätze, Passiv und mehr',
    chipLevel='B1 · Mittelstufe', chipFocus='Gemischte Grammatik', chipCount='44 Folien',
    bankLabel='Wortliste:',

    d1t='Multiple Choice', d1n='Teil 1 · zehn neue Sätze, zehn Grammatikpunkte',
    d2t='Diegos Reise', d2n='Teil 2 · lesen, dann die Lücken füllen',
    d3t='Richtig oder falsch', d3n='Teil 3 · manches davon ist ein Mythos',
    d4t='Satzbau', d4n='Teil 4 · die Teile in die richtige Reihenfolge',
    d5t='Fehler finden', d5n='Teil 5 · ein Fehler pro Satz',

    e1='Multiple Choice', e2='Diegos Reise', e3='Richtig oder falsch',
    e4='Satzbau', e5='Fehler finden',

    s1t='Zehn neue Sätze',
    s1a='Dieselben zehn Bereiche der B1-Grammatik wie in Teil 1 — Zeitformen, Modalverben, Konditionalsätze, Passiv, Relativsätze — und kein einziger Satz, den du schon kennst.',
    s1b='Lies den ganzen Satz, bevor du wählst. Das Wort, das die Antwort bestimmt, steht meist neben der Lücke, nicht darin: „Be quiet!“, „while“, „for ten years now“, „strictly forbidden“.',

    s2t='Einmal lesen, dann ausfüllen',
    s2a='Diegos Geschichte reicht von einer Sommergewohnheit bis zu einem Flug am nächsten Freitag — sie durchläuft sechs Zeitformen, ohne eine davon anzukündigen.',
    s2b='In jeder Lücke steht ein Verb in Klammern. Setz es in die Form, die der Satz braucht — die Zeitangaben ringsum verraten dir, welche.',

    s3t='Sechs Regeln, und einige stimmen nicht',
    s3a='Jede Aussage hier bekommen Lernende regelmäßig zu hören. Vier sind richtig. Zwei sind die Art halbe Regel, die sich hält, weil niemand sie überprüft.',
    s3b='Entscheide über die Regel selbst, nicht darüber, ob dir das Beispiel bekannt vorkommt.',

    s4t='Die Teile stimmen, die Reihenfolge nicht',
    s4a='Jeder Satz wurde an seinen Fugen zerteilt — nicht in einzelne Wörter, sondern in die Wortgruppen, die grammatisch tatsächlich etwas leisten.',
    s4b='Klick ein Teil an, um es zu setzen, und ein gesetztes Teil, um es zurückzunehmen. Der ganze Satz zählt einen Punkt: eine halb richtige Wortstellung ist kein halb richtiges Englisch.',

    s5t='Ein Fehler, eine Korrektur',
    s5a='Jeder Satz unten enthält genau einen Grammatikfehler, und zwar die Sorte, die B1-Lernende aus einem Grund machen und nicht aus Versehen.',
    s5b='Schreib den ganzen Satz korrigiert. Groß- und Kleinschreibung spielt keine Rolle, ein fehlender Punkt oder ein fehlendes Komma ist kein Fehler, und die üblichen Kurzformen werden akzeptiert.',

    storyT='Diegos Reise', storyA=STORY_A, storyB=STORY_B,

    q1t='Das Baby', q2t='Filmabend', q3t='Alte Freunde', q4t='Ein Gefallen',
    q5t='Tokio', q6t='Drinnen', q7t='Die Maschine', q8t='Die Mannschaft',
    q9t='Ein berühmtes Gemälde', q10t='Ein gutes Buch',
    q6g='„Forbidden“ = verboten.',

    t1t='Pläne und das Present Continuous', t2t='Mustn’t und don’t have to',
    t3t='Were oder was', t4t='Zweisilbige Adjektive',
    t5t='Aus Aktiv wird Passiv', t6t='Whose',
    tfStem='Richtig oder falsch?',

    o1t='Eine Frage im Passiv', o2t='Ein Relativsatz', o3t='Eine Frage nach der Dauer',
    o4t='Ein Konditionalsatz Typ II', o5t='Ein doppelter Vergleich',
    orderHint='Klick die Teile in der richtigen Reihenfolge an, um den Satz wieder aufzubauen.',

    g1t='Jeden Sommer', g2t='Vor der Reise', g3t='Nächsten Freitag',
    g1h='Setz das Verb in Klammern in die richtige Form.',
    g2h='Setz das Verb in Klammern in die richtige Form. „Suitcase“ = Koffer.',
    g3h='Setz das Verb in Klammern in die richtige Form. „Delayed“ = verspätet.',

    ec1t='Du hast recht', ec2t='Verheiratet', ec3t='Ein Haus', ec4t='Die Übung',
    ec5t='Die E-Mail', ec6t='Das Auto',
    ecHint='Schreib den ganzen Satz korrigiert.',

    actTitle='Jetzt anwenden',
    actUse='Verwende mindestens drei davon:',
    actSpeakBrief='Zu zweit. Nehmt euch je eine Aufgabe und sprecht zwei Minuten ohne Pause, mit der Grammatik in Klammern — die andere Person hört auf die Formen oben und sagt dir danach, welche du tatsächlich benutzt hast.',
    actSpeak1='Deine Pläne für Samstag, und was du machst, wenn es regnet. (Present Continuous, Konditionalsatz Typ I)',
    actSpeak2='In der Arbeit oder in der Schule: drei Dinge, die du nicht tun darfst, und drei, die du nicht tun musst. (Modalverben)',
    actSpeak3='Eine Reise, die schiefging: Was hast du gerade gemacht, als es passierte, und was geschah dann? (Past Continuous, Past Simple)',
    actWriteKind='Schreiben',
    actWriteBrief='Schreib eine Bewertung für eine Reise-Website (150–200 Wörter) über einen Ort, den du gut kennst. Sag, seit wann du ihn kennst, wofür er berühmt ist und warum er der beste — oder der schlechteste — seiner Art ist.',
    actPlaceholder='I have been to … three times, and …',
)

# ══════════════════════════════════════════════════════════════════════
#  SPANISH
# ══════════════════════════════════════════════════════════════════════
T['es'] = dict(
    coverTitle='Mixed Grammar Test <em>Part 2</em>',
    coverSub='Diez áreas gramaticales más, todo frases nuevas — tiempos verbales, modales, condicionales, pasiva y más',
    chipLevel='B1 · Intermedio', chipFocus='Gramática mixta', chipCount='44 diapositivas',
    bankLabel='Banco de palabras:',

    d1t='Opción múltiple', d1n='Sección 1 · diez frases nuevas, diez puntos gramaticales',
    d2t='El viaje de Diego', d2n='Sección 2 · lee y completa los huecos',
    d3t='Verdadero o falso', d3n='Sección 3 · algunos de estos son mitos',
    d4t='Construye la frase', d4n='Sección 4 · ordena las partes',
    d5t='Encuentra el error', d5n='Sección 5 · un error en cada frase',

    e1='Opción múltiple', e2='El viaje de Diego', e3='Verdadero o falso',
    e4='Construye la frase', e5='Encuentra el error',

    s1t='Diez frases nuevas',
    s1a='Las mismas diez áreas de la gramática de B1 que en la parte 1 — tiempos verbales, modales, condicionales, la pasiva, las oraciones de relativo — y ni una sola frase que ya hayas visto.',
    s1b='Lee la frase entera antes de elegir. La palabra que decide la respuesta suele estar al lado del hueco, no en él: «Be quiet!», «while», «for ten years now», «strictly forbidden».',

    s2t='Léelo una vez y luego complétalo',
    s2a='La historia de Diego va de una costumbre de verano a un vuelo el viernes que viene, así que recorre seis tiempos verbales sin anunciar ninguno.',
    s2b='Cada hueco lleva un verbo entre paréntesis. Ponlo en la forma que pide la frase: las expresiones de tiempo que lo rodean te dicen cuál.',

    s3t='Seis reglas, y algunas son falsas',
    s3a='Todo lo que se afirma aquí es algo que se les dice a menudo a los estudiantes. Cuatro afirmaciones son correctas. Dos son esa clase de media regla que sobrevive porque nadie la comprueba.',
    s3b='Decide sobre la regla en sí, no sobre si el ejemplo te suena familiar.',

    s4t='Las partes están bien, el orden no',
    s4a='Cada frase se ha cortado por sus junturas: no en palabras sueltas, sino en los grupos que de verdad hacen el trabajo gramatical.',
    s4b='Haz clic en una parte para colocarla y en una ya colocada para retirarla. La frase entera vale un punto: un orden a medias no es inglés a medias.',

    s5t='Un error, una corrección',
    s5a='Cada frase de abajo contiene exactamente un error de gramática, y es de los que un estudiante de B1 comete por una razón, no por descuido.',
    s5b='Escribe la frase entera, corregida. Las mayúsculas no importan, un punto o una coma que falten no cuentan como error, y se aceptan las contracciones habituales.',

    storyT='El viaje de Diego', storyA=STORY_A, storyB=STORY_B,

    q1t='El bebé', q2t='Noche de cine', q3t='Viejos amigos', q4t='Un favor',
    q5t='Tokio', q6t='Aquí dentro', q7t='La máquina', q8t='El equipo',
    q9t='Un cuadro famoso', q10t='Un buen libro',
    q6g='«Forbidden» = prohibido.',

    t1t='Planes y el Present Continuous', t2t='Mustn’t y don’t have to',
    t3t='Were o was', t4t='Adjetivos de dos sílabas',
    t5t='De activa a pasiva', t6t='Whose',
    tfStem='¿Verdadero o falso?',

    o1t='Una pregunta en pasiva', o2t='Una oración de relativo', o3t='Una pregunta sobre el tiempo',
    o4t='Un condicional de tipo 2', o5t='Una doble comparación',
    orderHint='Haz clic en las partes en el orden correcto para reconstruir la frase.',

    g1t='Cada verano', g2t='Antes del viaje', g3t='El viernes que viene',
    g1h='Escribe el verbo entre paréntesis en la forma correcta.',
    g2h='Escribe el verbo entre paréntesis en la forma correcta. «Suitcase» = maleta.',
    g3h='Escribe el verbo entre paréntesis en la forma correcta. «Delayed» = retrasado.',

    ec1t='Tienes razón', ec2t='Casada', ec3t='Una casa', ec4t='El ejercicio',
    ec5t='El correo', ec6t='El coche',
    ecHint='Escribe la frase entera, corregida.',

    actTitle='Ahora úsalo',
    actUse='Usa al menos tres de estos:',
    actSpeakBrief='En parejas. Tomad una consigna cada uno y hablad dos minutos sin parar, usando la gramática entre paréntesis — tu pareja escucha buscando las formas de arriba y después te dice cuáles has usado de verdad.',
    actSpeak1='Tus planes para el sábado, y qué harás si llueve. (Present Continuous, primer condicional)',
    actSpeak2='En el trabajo o en clase: tres cosas que no puedes hacer y tres que no tienes que hacer. (modales)',
    actSpeak3='Un viaje que salió mal: ¿qué estabas haciendo cuando pasó, y qué pasó después? (Past Continuous, Past Simple)',
    actWriteKind='Escritura',
    actWriteBrief='Escribe una reseña para una web de viajes (150–200 palabras) sobre un lugar que conozcas bien. Di desde cuándo lo conoces, por qué es famoso y por qué es el mejor — o el peor — de su tipo.',
    actPlaceholder='I have been to … three times, and …',
)


# ══════════════════════════════════════════════════════════════════════
#  EXPLANATIONS — one per scored item, and they translate
# ══════════════════════════════════════════════════════════════════════
# HOUSE-STYLE §7: data-explain takes a sentence or a UI_I18N key, and a key
# "is the better choice on a lesson that ships more than one language".
# Ported from mixed_b1_<lang>.py P2 (19b39ed); the key map is x_mc → q,
# x_tf → t, x_or → o, x_st → the six story rows, x_fx → ec.
EXPLAIN = {}
EXPLAIN['en'] = dict(
    q1w="“Be quiet!” means now, so the action is in progress: IS + sleeping. “Sleeps” is a habit; the other two are past.",
    q2w="WHILE + WERE + -ING gives the background action that the lights (“went out”) interrupted. The others are present forms.",
    q3w="“For ten years now” runs up to today: HAVE + known. “Are knowing” is wrong because KNOW is not an action in progress; “knew” says it has ended.",
    q4w="A promise is a decision made as you speak: WILL + verb. “Am helping” would need an arrangement already made.",
    q5w="Compared with every city, so the superlative: THE + busiEST. “Busier” compares two; “most busiest” says it twice.",
    q6w="“Forbidden” is a rule against it: MUSTN’T. “Don’t have to” means it is not necessary, which is almost the opposite.",
    q7w="First conditional: IF + Present Simple, then WON’T / WILL in the other clause.",
    q8w="“Could join” shows an imaginary situation: IF + Past Simple, and with BE we use WERE for every person.",
    q9w="The painting did not paint itself, so the passive: WAS + past participle, and BY names the painter.",
    q10w="WHICH (or THAT) for things. WHO is for people, WHOSE for possession, WHERE for places.",

    t1w="True. When the plan is fixed (a ticket, a time), the Present Continuous is the natural choice.",
    t2w="False. MUSTN’T means it is not allowed. DON’T HAVE TO means it is not necessary. They are nearly opposites.",
    t3w="True. “If I were you”, “If he were taller”. “Was” is common in speech, but WERE is the standard form.",
    t4w="False. Many take -ER: happy → happier, easy → easier, narrow → narrower.",
    t5w="True. The object (“English”) becomes the subject, and the verb becomes IS + past participle.",
    t6w="True. “Whose car is this?” · “the man whose car was stolen”.",

    o1w="A passive question: WAS + subject + past participle, then BY + who did it.",
    o2w="WHERE introduces a clause about a place: “where we had dinner” tells us which restaurant.",
    o3w="HOW LONG + HAVE + subject + past participle: the Present Perfect question.",
    o4w="Second conditional: IF + Past Simple (“had”), then WOULD + verb.",
    o5w="THE + comparative, THE + comparative: two things that change together.",

    g1aw="“Every summer” is a habit: Present Simple, and “he” takes -S. HAS TRAVELLED is also correct: every summer up to this one.",
    g1bw="“Last month” is finished: Past Simple “booked”. The friend recommended it first; “recommended” and “had recommended” are both correct.",
    g2aw="“Never … before” is his life up to now: HAS + NEVER + visited.",
    g2bw="WHILE + WAS + -ING for the longer action; the moment he realised interrupts it.",
    g3aw="A seat is chosen, so it is an arrangement: IS + flying. IS GOING TO fly is also correct.",
    g3bw="First conditional. After IF, Present Simple (“is”); the result takes WILL + miss. MIGHT miss is also correct.",

    ec1w="AGREE is an opinion, not an action in progress, so the Present Simple: “I agree”.",
    ec2w="MARRIED TO someone, not “married with”.",
    ec3w="After IF in a second conditional, the Past Simple: “If I had”. WOULD stays in the other clause.",
    ec4w="“Easy” ends in -Y, so it takes -IER: EASIER, not “more easy”.",
    ec5w="In the passive, BY names who did it: “sent by the manager”. FOR means the person receiving it.",
    ec6w="WHOSE already means “his”, so “his” is said twice. Delete it.",
)

EXPLAIN['de'] = dict(
    q1w="„Be quiet!“ heißt jetzt, die Handlung läuft gerade: IS + sleeping. „Sleeps“ ist eine Gewohnheit; die anderen beiden sind Vergangenheit.",
    q2w="WHILE + WERE + -ING für die Hintergrundhandlung, die das Licht („went out“) unterbrach. Die anderen sind Gegenwartsformen.",
    q3w="„For ten years now“ reicht bis heute: HAVE + known. „Are knowing“ ist falsch, weil KNOW keine laufende Handlung ist; „knew“ sagt, dass es vorbei ist.",
    q4w="Ein Versprechen ist eine Entscheidung beim Sprechen: WILL + Verb. „Am helping“ bräuchte eine feste Verabredung.",
    q5w="Verglichen mit allen Städten, also der Superlativ: THE + busiEST. „Busier“ vergleicht zwei; „most busiest“ sagt es doppelt.",
    q6w="„Forbidden“ ist ein Verbot: MUSTN’T. „Don’t have to“ heißt, es ist nicht nötig — fast das Gegenteil.",
    q7w="Bedingungssatz Typ 1: IF + Present Simple, dann WON’T / WILL im anderen Satzteil.",
    q8w="„Could join“ zeigt eine gedachte Situation: IF + Past Simple, und bei BE nehmen wir WERE für alle Personen.",
    q9w="Das Bild hat sich nicht selbst gemalt, also Passiv: WAS + Partizip, und BY nennt den Maler.",
    q10w="WHICH (oder THAT) für Dinge. WHO für Personen, WHOSE für Besitz, WHERE für Orte.",

    t1w="Richtig. Wenn der Plan feststeht (ein Ticket, eine Uhrzeit), ist das Present Continuous die natürliche Wahl.",
    t2w="Falsch. MUSTN’T heißt, es ist verboten. DON’T HAVE TO heißt, es ist nicht nötig. Sie sind fast Gegensätze.",
    t3w="Richtig. „If I were you“, „If he were taller“. „Was“ hört man oft, aber WERE ist die Standardform.",
    t4w="Falsch. Viele nehmen -ER: happy → happier, easy → easier, narrow → narrower.",
    t5w="Richtig. Das Objekt („English“) wird zum Subjekt, und das Verb wird IS + Partizip.",
    t6w="Richtig. „Whose car is this?“ · „the man whose car was stolen“.",

    o1w="Eine Passivfrage: WAS + Subjekt + Partizip, dann BY + wer es getan hat.",
    o2w="WHERE leitet einen Satz über einen Ort ein: „where we had dinner“ sagt, welches Restaurant.",
    o3w="HOW LONG + HAVE + Subjekt + Partizip: die Frage im Present Perfect.",
    o4w="Bedingungssatz Typ 2: IF + Past Simple („had“), dann WOULD + Verb.",
    o5w="THE + Komparativ, THE + Komparativ: zwei Dinge, die sich zusammen verändern.",

    g1aw="„Every summer“ ist eine Gewohnheit: Present Simple, und „he“ bekommt -S. HAS TRAVELLED ist auch richtig: jeden Sommer bis zu diesem.",
    g1bw="„Last month“ ist vorbei: Past Simple „booked“. Der Freund hat es vorher empfohlen; „recommended“ und „had recommended“ sind beide richtig.",
    g2aw="„Never … before“ ist sein Leben bis jetzt: HAS + NEVER + visited.",
    g2bw="WHILE + WAS + -ING für die längere Handlung; der Moment, in dem er es merkte, unterbricht sie.",
    g3aw="Der Sitzplatz ist gewählt, es ist also fest geplant: IS + flying. IS GOING TO fly ist auch richtig.",
    g3bw="Bedingungssatz Typ 1. Nach IF Present Simple („is“); die Folge bekommt WILL + miss. MIGHT miss ist auch richtig.",

    ec1w="AGREE ist eine Meinung, keine laufende Handlung, also Present Simple: „I agree“.",
    ec2w="MARRIED TO someone, nicht „married with“.",
    ec3w="Nach IF im Bedingungssatz Typ 2 steht Past Simple: „If I had“. WOULD bleibt im anderen Satzteil.",
    ec4w="„Easy“ endet auf -Y, also -IER: EASIER, nicht „more easy“.",
    ec5w="Im Passiv nennt BY, wer es getan hat: „sent by the manager“. FOR wäre der Empfänger.",
    ec6w="WHOSE heißt schon „his“, also steht „his“ doppelt. Streich es.",
)

EXPLAIN['es'] = dict(
    q1w="«Be quiet!» significa ahora: la acción está en curso, IS + sleeping. «Sleeps» es un hábito; las otras dos son pasado.",
    q2w="WHILE + WERE + -ING da la acción de fondo que las luces («went out») interrumpieron. Las otras son formas de presente.",
    q3w="«For ten years now» llega hasta hoy: HAVE + known. «Are knowing» está mal porque KNOW no es una acción en curso; «knew» dice que ya terminó.",
    q4w="Una promesa es una decisión que se toma al hablar: WILL + verbo. «Am helping» necesitaría un plan ya acordado.",
    q5w="Comparado con todas las ciudades, así que el superlativo: THE + busiEST. «Busier» compara dos; «most busiest» lo dice dos veces.",
    q6w="«Forbidden» es una prohibición: MUSTN’T. «Don’t have to» significa que no es necesario, casi lo contrario.",
    q7w="Primer condicional: IF + Present Simple, y WON’T / WILL en la otra parte.",
    q8w="«Could join» muestra una situación imaginaria: IF + Past Simple, y con BE usamos WERE para todas las personas.",
    q9w="El cuadro no se pintó solo, así que la pasiva: WAS + participio, y BY nombra al pintor.",
    q10w="WHICH (o THAT) para cosas. WHO es para personas, WHOSE para posesión, WHERE para lugares.",

    t1w="Verdadero. Cuando el plan está fijado (un billete, una hora), el Present Continuous es la opción natural.",
    t2w="Falso. MUSTN’T significa que no está permitido. DON’T HAVE TO significa que no es necesario. Son casi opuestos.",
    t3w="Verdadero. «If I were you», «If he were taller». «Was» es común al hablar, pero WERE es la forma estándar.",
    t4w="Falso. Muchos llevan -ER: happy → happier, easy → easier, narrow → narrower.",
    t5w="Verdadero. El objeto («English») pasa a ser el sujeto, y el verbo pasa a IS + participio.",
    t6w="Verdadero. «Whose car is this?» · «the man whose car was stolen».",

    o1w="Una pregunta en pasiva: WAS + sujeto + participio, y luego BY + quién lo hizo.",
    o2w="WHERE introduce una oración sobre un lugar: «where we had dinner» dice qué restaurante.",
    o3w="HOW LONG + HAVE + sujeto + participio: la pregunta en Present Perfect.",
    o4w="Segundo condicional: IF + Past Simple («had»), luego WOULD + verbo.",
    o5w="THE + comparativo, THE + comparativo: dos cosas que cambian a la vez.",

    g1aw="«Every summer» es un hábito: Present Simple, y «he» lleva -S. HAS TRAVELLED también es correcto: cada verano hasta este.",
    g1bw="«Last month» ya terminó: Past Simple «booked». El amigo lo recomendó antes; «recommended» y «had recommended» son correctos.",
    g2aw="«Never … before» es su vida hasta ahora: HAS + NEVER + visited.",
    g2bw="WHILE + WAS + -ING para la acción más larga; el momento en que se dio cuenta la interrumpe.",
    g3aw="El asiento está elegido, así que es un plan fijo: IS + flying. IS GOING TO fly también es correcto.",
    g3bw="Primer condicional. Después de IF, Present Simple («is»); el resultado lleva WILL + miss. MIGHT miss también es correcto.",

    ec1w="AGREE es una opinión, no una acción en curso: Present Simple, «I agree».",
    ec2w="MARRIED TO someone, no «married with».",
    ec3w="Después de IF en el segundo condicional, Past Simple: «If I had». WOULD se queda en la otra parte.",
    ec4w="«Easy» termina en -Y, así que lleva -IER: EASIER, no «more easy».",
    ec5w="En la pasiva, BY nombra quién lo hizo: «sent by the manager». FOR sería quien lo recibe.",
    ec6w="WHOSE ya significa «his», así que «his» sobra. Bórralo.",
)

for _c in T:
    T[_c].update(EXPLAIN[_c])


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
