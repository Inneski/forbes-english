# -*- coding: utf-8 -*-
"""Interface strings for the B1 Mixed Grammar Test (Part 1).

English, German and Spanish — the minimum since 2026-09-04. `assemble()`
still defaults to ('en', 'de'), so the builder passes langs explicitly.

What is NOT translated, deliberately (HOUSE-STYLE §8): every question stem,
every option, every gap sentence, every sentence chunk in the reordering
task and every error-correction sentence. Those ARE the English being
tested. What translates is the chrome around them — stage names, slide
titles, instructions, explanations and the activation brief.

The explanations DO translate, and that is the point of putting them here
rather than in the builder as literals. A B1 learner who got the item wrong
is the one who most needs the reason, and they need it in a language they
already have. The English sentence being explained stays English inside the
translated text, which is why the German and Spanish strings quote forms
like 'was cooking' rather than translating them.

The builder reads its English from T['en'] rather than repeating it as
literals — two copies of a sentence drift, and the symptom is bizarre: the
slide renders correctly until the learner picks English in the switcher, at
which point the text changes.
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

T = {}

# ══════════════════════════════════════════════════════════════════════
#  ENGLISH
# ══════════════════════════════════════════════════════════════════════
T['en'] = dict(
    coverTitle='Mixed <em>Grammar</em> Test',
    coverSub='Ten grammar areas, one test — tenses, modals, conditionals, passives and more',
    chipLevel='B1 · Intermediate', chipFocus='Mixed grammar', chipCount='45 slides',
    bankLabel='Word bank:',

    # ── stage dividers ────────────────────────────────────────────────
    d1t='Multiple Choice', d1n='Section 1 · ten sentences, ten grammar points',
    d2t='Elena’s Week', d2n='Section 2 · read, then fill the gaps',
    d3t='True or False', d3n='Section 3 · some of these are myths',
    d4t='Build the Sentence', d4n='Section 4 · put the parts in order',
    d5t='Find the Mistake', d5n='Section 5 · one error in each sentence',

    # ── stage eyebrows ────────────────────────────────────────────────
    e1='Multiple choice', e2='Elena’s week', e3='True or false',
    e4='Build the sentence', e5='Find the mistake',

    # ── section opener panels ─────────────────────────────────────────
    s1t='One sentence, one decision',
    s1a='Ten sentences are waiting, and each one tests a different piece of B1 grammar — a tense, a modal, a conditional, a passive, a relative pronoun.',
    s1b='Read the whole sentence before you choose. The word that decides the answer is usually not the gap itself but something beside it: <em>Listen!</em>, <em>while</em>, <em>since</em>, <em>it’s the law</em>.',

    s2t='Read it once, then fill it in',
    s2a='Elena’s week runs from an ordinary morning to a weekend that has not happened yet, so the passage moves through six tenses without announcing any of them.',
    s2b='Each gap names a verb in brackets. Put it in the form the sentence needs — the time words around it will tell you which.',

    s3t='Six rules, and some of them are wrong',
    s3a='Every statement here is something learners are commonly told. Four are accurate. Two are the kind of half-rule that survives because nobody checks it.',
    s3b='Decide on the rule itself, not on whether the example sounds familiar.',

    s4t='The parts are right, the order is not',
    s4a='Each sentence has been cut at its joints — not into single words, but into the phrases that actually do the grammatical work.',
    s4b='Click a part to place it, click a placed part to take it back. The whole sentence scores one point: half-right word order is not half-right English.',

    s5t='One mistake, one correction',
    s5a='Every sentence below contains exactly one grammar error, and it is the kind a B1 learner makes for a reason rather than by accident.',
    s5b='Type the whole sentence, corrected. Capitals and full stops are ignored, and the usual contracted forms are accepted.',

    # ── the reading passage ───────────────────────────────────────────
    storyT='Elena’s week',
    storyA='Elena usually <em>gets up</em> at seven o’clock, but this morning she <em>overslept</em> because her alarm didn’t ring. She <em>has lived</em> in this apartment for almost three years now, and she loves the quiet street.',
    storyB='Last night, while she <em>was reading</em> a book, her neighbour knocked on the door to borrow some sugar. Tomorrow, Elena <em>is meeting</em> her sister for lunch. If the weather <em>is</em> nice this weekend, they <em>will go</em> to the coast afterwards.',

    # ── multiple choice ───────────────────────────────────────────────
    q1t='Right now', q2t='Interrupted', q3t='Since 2019', q4t='A prediction',
    q5t='The best of them', q6t='The law', q7t='If it rains',
    q8t='If I had the time', q9t='Built in 1889', q10t='The woman next door',

    # ── true or false ─────────────────────────────────────────────────
    t1t='Present perfect and finished time', t2t='Must and have to',
    t3t='Will in the if-clause', t4t='The before a superlative',
    t5t='How the passive is built', t6t='Who and which',
    tfStem='True or false?',

    # ── reordering ────────────────────────────────────────────────────
    o1t='A passive sentence', o2t='A relative clause', o3t='A past question',
    o4t='A second conditional', o5t='A comparison',
    orderHint='Click the parts in the right order to rebuild the sentence.',

    # ── gaps ──────────────────────────────────────────────────────────
    g1t='Elena’s morning', g2t='Three years, and last night',
    g3t='Tomorrow, and the weekend', g4t='At the restaurant',
    gapHint='Write the verb in the form the sentence needs.',

    ec1t='For or since', ec2t='Will in the if-clause', ec3t='A double comparative',
    ec4t='The wrong participle', ec5t='Much or many', ec6t='Which or who',
    ecHint='Type the whole sentence, corrected.',

    # ── activation ────────────────────────────────────────────────────
    actTitle='Now use it',
    actUse='Use at least three of these:',
    actSpeakBrief='In pairs. Take one prompt each and talk for two minutes without stopping — your partner listens for the forms above and tells you afterwards which ones you actually used.',
    actSpeak1='Describe a morning that went wrong. Say what you usually do, what you were doing when it went wrong, and what happened as a result.',
    actSpeak2='Your partner is deciding whether to move to another city. Give them three pieces of advice using <em>must</em>, <em>have to</em> and <em>should</em>, and say what you would do if you were them.',
    actSpeak3='Describe the building you live in, or one you know well — when it was built, who lives there, and what is the best thing about it.',
    actWriteKind='Writing',
    actWriteBrief='Write an email to a friend who is coming to stay next month (150–200 words). Say how long you have lived where you live, what you were doing when they last visited, what you will do if the weather is good, and what the best place nearby is.',
    actPlaceholder='Hi Sam, I can’t believe it’s nearly a year since…',
)

# ══════════════════════════════════════════════════════════════════════
#  GERMAN
# ══════════════════════════════════════════════════════════════════════
T['de'] = dict(
    coverTitle='Mixed <em>Grammar</em> Test',
    coverSub='Zehn Grammatikbereiche, ein Test — Zeiten, Modalverben, Konditionalsätze, Passiv und mehr',
    chipLevel='B1 · Mittelstufe', chipFocus='Gemischte Grammatik', chipCount='45 Folien',
    bankLabel='Wortliste:',

    d1t='Multiple Choice', d1n='Teil 1 · zehn Sätze, zehn Grammatikpunkte',
    d2t='Elenas Woche', d2n='Teil 2 · lesen, dann die Lücken füllen',
    d3t='Richtig oder falsch', d3n='Teil 3 · manches davon ist ein Mythos',
    d4t='Satzbau', d4n='Teil 4 · die Teile in die richtige Reihenfolge',
    d5t='Fehler finden', d5n='Teil 5 · ein Fehler pro Satz',

    e1='Multiple Choice', e2='Elenas Woche', e3='Richtig oder falsch',
    e4='Satzbau', e5='Fehler finden',

    s1t='Ein Satz, eine Entscheidung',
    s1a='Zehn Sätze warten, und jeder prüft einen anderen Baustein der B1-Grammatik — eine Zeitform, ein Modalverb, einen Konditionalsatz, ein Passiv, ein Relativpronomen.',
    s1b='Lies den ganzen Satz, bevor du wählst. Das Wort, das die Antwort bestimmt, steht meist nicht in der Lücke, sondern daneben: <em>Listen!</em>, <em>while</em>, <em>since</em>, <em>it’s the law</em>.',

    s2t='Einmal lesen, dann ausfüllen',
    s2a='Elenas Woche reicht von einem ganz normalen Morgen bis zu einem Wochenende, das noch nicht stattgefunden hat — der Text durchläuft sechs Zeitformen, ohne eine davon anzukündigen.',
    s2b='In jeder Lücke steht ein Verb in Klammern. Setz es in die Form, die der Satz braucht — die Zeitangaben ringsum verraten dir, welche.',

    s3t='Sechs Regeln, und einige stimmen nicht',
    s3a='Jede Aussage hier bekommen Lernende regelmäßig zu hören. Vier sind richtig. Zwei sind die Art halbe Regel, die sich hält, weil niemand sie überprüft.',
    s3b='Entscheide über die Regel selbst, nicht darüber, ob dir das Beispiel bekannt vorkommt.',

    s4t='Die Teile stimmen, die Reihenfolge nicht',
    s4a='Jeder Satz wurde an seinen Fugen zerteilt — nicht in einzelne Wörter, sondern in die Wortgruppen, die grammatisch tatsächlich etwas leisten.',
    s4b='Klick ein Teil an, um es zu setzen, und ein gesetztes Teil, um es zurückzunehmen. Der ganze Satz zählt einen Punkt: eine halb richtige Wortstellung ist kein halb richtiges Englisch.',

    s5t='Ein Fehler, eine Korrektur',
    s5a='Jeder Satz unten enthält genau einen Grammatikfehler, und zwar die Sorte, die B1-Lernende aus einem Grund machen und nicht aus Versehen.',
    s5b='Schreib den ganzen Satz korrigiert. Groß- und Kleinschreibung und Satzzeichen werden ignoriert, die üblichen Kurzformen werden akzeptiert.',

    storyT='Elenas Woche',
    storyA='Elena usually <em>gets up</em> at seven o’clock, but this morning she <em>overslept</em> because her alarm didn’t ring. She <em>has lived</em> in this apartment for almost three years now, and she loves the quiet street.',
    storyB='Last night, while she <em>was reading</em> a book, her neighbour knocked on the door to borrow some sugar. Tomorrow, Elena <em>is meeting</em> her sister for lunch. If the weather <em>is</em> nice this weekend, they <em>will go</em> to the coast afterwards.',

    q1t='Gerade jetzt', q2t='Unterbrochen', q3t='Seit 2019', q4t='Eine Vorhersage',
    q5t='Der beste von allen', q6t='Das Gesetz', q7t='Wenn es regnet',
    q8t='Wenn ich Zeit hätte', q9t='1889 gebaut', q10t='Die Frau von nebenan',

    t1t='Present Perfect und abgeschlossene Zeit', t2t='Must und have to',
    t3t='Will im if-Satz', t4t='The vor dem Superlativ',
    t5t='Wie das Passiv gebildet wird', t6t='Who und which',
    tfStem='Richtig oder falsch?',

    o1t='Ein Passivsatz', o2t='Ein Relativsatz', o3t='Eine Frage in der Vergangenheit',
    o4t='Ein Konditionalsatz Typ II', o5t='Ein Vergleich',
    orderHint='Klick die Teile in der richtigen Reihenfolge an, um den Satz wieder aufzubauen.',

    g1t='Elenas Morgen', g2t='Drei Jahre, und gestern Abend',
    g3t='Morgen, und das Wochenende', g4t='Im Restaurant',
    gapHint='Schreib das Verb in der Form, die der Satz braucht.',

    ec1t='For oder since', ec2t='Will im if-Satz', ec3t='Ein doppelter Komparativ',
    ec4t='Das falsche Partizip', ec5t='Much oder many', ec6t='Which oder who',
    ecHint='Schreib den ganzen Satz korrigiert.',

    actTitle='Jetzt anwenden',
    actUse='Verwende mindestens drei davon:',
    actSpeakBrief='Zu zweit. Nehmt euch je eine Aufgabe und sprecht zwei Minuten ohne Pause — die andere Person hört auf die Formen oben und sagt dir danach, welche du tatsächlich benutzt hast.',
    actSpeak1='Beschreib einen Morgen, der schiefgegangen ist. Sag, was du normalerweise machst, was du gerade gemacht hast, als es schiefging, und was dabei herauskam.',
    actSpeak2='Deine Partnerin oder dein Partner überlegt, in eine andere Stadt zu ziehen. Gib drei Ratschläge mit <em>must</em>, <em>have to</em> und <em>should</em>, und sag, was du an ihrer Stelle tun würdest.',
    actSpeak3='Beschreib das Gebäude, in dem du wohnst, oder eines, das du gut kennst — wann es gebaut wurde, wer dort wohnt und was das Beste daran ist.',
    actWriteKind='Schreiben',
    actWriteBrief='Schreib eine E-Mail an eine Freundin oder einen Freund, die oder der nächsten Monat zu Besuch kommt (150–200 Wörter). Sag, wie lange du schon dort wohnst, wo du wohnst, was du gerade gemacht hast, als sie oder er das letzte Mal da war, was ihr macht, wenn das Wetter gut ist, und was der schönste Ort in der Nähe ist.',
    actPlaceholder='Hi Sam, I can’t believe it’s nearly a year since…',
)

# ══════════════════════════════════════════════════════════════════════
#  SPANISH
# ══════════════════════════════════════════════════════════════════════
T['es'] = dict(
    coverTitle='Mixed <em>Grammar</em> Test',
    coverSub='Diez áreas gramaticales, un test — tiempos verbales, modales, condicionales, pasiva y más',
    chipLevel='B1 · Intermedio', chipFocus='Gramática mixta', chipCount='45 diapositivas',
    bankLabel='Banco de palabras:',

    d1t='Opción múltiple', d1n='Sección 1 · diez frases, diez puntos gramaticales',
    d2t='La semana de Elena', d2n='Sección 2 · lee y completa los huecos',
    d3t='Verdadero o falso', d3n='Sección 3 · algunos de estos son mitos',
    d4t='Construye la frase', d4n='Sección 4 · ordena las partes',
    d5t='Encuentra el error', d5n='Sección 5 · un error en cada frase',

    e1='Opción múltiple', e2='La semana de Elena', e3='Verdadero o falso',
    e4='Construye la frase', e5='Encuentra el error',

    s1t='Una frase, una decisión',
    s1a='Te esperan diez frases, y cada una evalúa una pieza distinta de la gramática de B1: un tiempo verbal, un modal, un condicional, una pasiva, un pronombre relativo.',
    s1b='Lee la frase entera antes de elegir. La palabra que decide la respuesta casi nunca está en el hueco, sino al lado: <em>Listen!</em>, <em>while</em>, <em>since</em>, <em>it’s the law</em>.',

    s2t='Léelo una vez y luego complétalo',
    s2a='La semana de Elena va de una mañana corriente a un fin de semana que todavía no ha ocurrido, así que el texto recorre seis tiempos verbales sin anunciar ninguno.',
    s2b='Cada hueco lleva un verbo entre paréntesis. Ponlo en la forma que pide la frase: las expresiones de tiempo que lo rodean te dicen cuál.',

    s3t='Seis reglas, y algunas son falsas',
    s3a='Todo lo que se afirma aquí es algo que se les dice a menudo a los estudiantes. Cuatro afirmaciones son correctas. Dos son esa clase de media regla que sobrevive porque nadie la comprueba.',
    s3b='Decide sobre la regla en sí, no sobre si el ejemplo te suena familiar.',

    s4t='Las partes están bien, el orden no',
    s4a='Cada frase se ha cortado por sus junturas: no en palabras sueltas, sino en los grupos que de verdad hacen el trabajo gramatical.',
    s4b='Haz clic en una parte para colocarla y en una ya colocada para retirarla. La frase entera vale un punto: un orden a medias no es inglés a medias.',

    s5t='Un error, una corrección',
    s5a='Cada frase de abajo contiene exactamente un error de gramática, y es de los que un estudiante de B1 comete por una razón, no por descuido.',
    s5b='Escribe la frase entera, corregida. Se ignoran mayúsculas y puntos, y se aceptan las contracciones habituales.',

    storyT='La semana de Elena',
    storyA='Elena usually <em>gets up</em> at seven o’clock, but this morning she <em>overslept</em> because her alarm didn’t ring. She <em>has lived</em> in this apartment for almost three years now, and she loves the quiet street.',
    storyB='Last night, while she <em>was reading</em> a book, her neighbour knocked on the door to borrow some sugar. Tomorrow, Elena <em>is meeting</em> her sister for lunch. If the weather <em>is</em> nice this weekend, they <em>will go</em> to the coast afterwards.',

    q1t='Ahora mismo', q2t='Interrumpido', q3t='Desde 2019', q4t='Una predicción',
    q5t='La mejor de todas', q6t='La ley', q7t='Si llueve',
    q8t='Si tuviera tiempo', q9t='Construido en 1889', q10t='La mujer de al lado',

    t1t='Present perfect y tiempo terminado', t2t='Must y have to',
    t3t='Will en la oración con if', t4t='The delante del superlativo',
    t5t='Cómo se forma la pasiva', t6t='Who y which',
    tfStem='¿Verdadero o falso?',

    o1t='Una frase en pasiva', o2t='Una oración de relativo', o3t='Una pregunta en pasado',
    o4t='Un condicional de tipo 2', o5t='Una comparación',
    orderHint='Haz clic en las partes en el orden correcto para reconstruir la frase.',

    g1t='La mañana de Elena', g2t='Tres años, y anoche',
    g3t='Mañana, y el fin de semana', g4t='En el restaurante',
    gapHint='Escribe el verbo en la forma que pide la frase.',

    ec1t='For o since', ec2t='Will en la oración con if', ec3t='Un comparativo doble',
    ec4t='El participio equivocado', ec5t='Much o many', ec6t='Which o who',
    ecHint='Escribe la frase entera, corregida.',

    actTitle='Ahora úsalo',
    actUse='Usa al menos tres de estos:',
    actSpeakBrief='En parejas. Tomad una consigna cada uno y hablad dos minutos sin parar — tu pareja escucha buscando las formas de arriba y después te dice cuáles has usado de verdad.',
    actSpeak1='Describe una mañana que salió mal. Di qué haces normalmente, qué estabas haciendo cuando salió mal y qué pasó como consecuencia.',
    actSpeak2='Tu pareja está pensando en mudarse a otra ciudad. Dale tres consejos usando <em>must</em>, <em>have to</em> y <em>should</em>, y di qué harías tú en su lugar.',
    actSpeak3='Describe el edificio donde vives, o uno que conozcas bien: cuándo se construyó, quién vive allí y qué es lo mejor de él.',
    actWriteKind='Escritura',
    actWriteBrief='Escribe un correo a una amiga o amigo que viene a quedarse el mes que viene (150–200 palabras). Di cuánto tiempo llevas viviendo donde vives, qué estabas haciendo la última vez que os visteis, qué haréis si hace buen tiempo y cuál es el mejor sitio de la zona.',
    actPlaceholder='Hi Sam, I can’t believe it’s nearly a year since…',
)


# ══════════════════════════════════════════════════════════════════════
#  EXPLANATIONS — one per scored item, and they translate
# ══════════════════════════════════════════════════════════════════════
# HOUSE-STYLE §7: data-explain takes either a sentence or a UI_I18N key, and
# "a key translates with the rest of the deck, and is the better choice on a
# lesson that ships more than one language". This one ships three, so these
# are keys. The English form under discussion stays English inside the German
# and Spanish text — 'was cooking' is the thing being explained, not a word to
# translate.
EXPLAIN = {}

EXPLAIN['en'] = dict(
    q1w="Present Continuous, for something happening right now. ‘Listen!’ points at this moment, so ‘knocks’, ‘knocked’ and ‘was knocking’ all miss it.",
    q2w="‘While’ + Past Continuous sets a longer background action that another past event cuts into — here ‘rang’. The other three are present tenses and cannot sit beside a past event.",
    q3w="‘Since’ + a point in time needs the Present Perfect. ‘Lives’ and ‘is living’ are present tenses, and ‘lived’ is Past Simple, which ‘since 2019’ will not take.",
    q4w="‘I think…’ introduces an opinion with no evidence behind it, and that is the classic trigger for ‘will’. The others are present or past forms and predict nothing.",
    q5w="‘The’ plus a comparison against everything else in a group calls for the superlative. ‘The goodest’ and ‘more good’ are not English forms at all, and ‘the better’ is a comparative.",
    q6w="‘Must’ is strong obligation, which is what a law is. ‘Might’ and ‘could’ are possibility, and ‘would’ belongs to hypothetical situations.",
    q7w="The if-clause of a First Conditional takes the Present Simple. ‘Will rain’ and ‘would rain’ cannot go inside it, and ‘rained’ is the wrong tense for a real future possibility.",
    q8w="‘Would learn’ in the main clause makes this a Second Conditional, and its if-clause needs the Past Simple. The situation is imagined, not likely.",
    q9w="A bridge does not build itself, so this needs the passive: ‘be’ + past participle. ‘Built’ alone has lost its auxiliary, and the other two are active.",
    q10w="‘Who’ opens a relative clause describing a person. ‘Which’ is for things, ‘whose’ shows possession, and ‘where’ points at a place.",

    t1w="False. The Present Perfect never combines with a finished time expression. For ‘yesterday’ or ‘in 2010’ English uses the Past Simple: ‘I visited Paris in 2010.’",
    t2w="True. ‘Must’ has no past form of its own, so for obligation in the past English switches to ‘had to’.",
    t3w="False. The if-clause takes the Present Simple — ‘If it rains…’ — and ‘will’ goes in the main clause: ‘…we’ll cancel the picnic.’",
    t4w="True. ‘The’ marks one thing out as unique inside its group: the best, the tallest, the most expensive.",
    t5w="True. Always ‘be’ plus the past participle of the main verb: is built, was written, has been finished.",
    t6w="True. ‘Who’ is kept for people and ‘which’ for things — though ‘that’ can replace either one in everyday speech.",

    o1w="Passive: subject + ‘be’ (was) + past participle (built). The date goes last.",
    o2w="‘Who lives next door’ is a relative clause describing ‘the man’, so it sits directly after it and before the main verb.",
    o3w="Question word + auxiliary (‘did’) + subject + base verb. Note that ‘go’ stays in its base form once ‘did’ has taken the past.",
    o4w="Second Conditional: if + Past Simple (‘were’), then would + base verb (‘I’d travel’).",
    o5w="‘Much’ intensifies the comparative ‘bigger’, and ‘than’ introduces the second thing being compared.",

    g1w="Two different times in one sentence, which is why it is one row and not two.",
    g1aw="‘Usually’ marks a habit, so this is the Present Simple: gets up.",
    g1bw="‘This morning’ with a finished event takes the Past Simple. Oversleep is irregular: overslept.",
    g2aw="‘For almost three years now’ is a period running up to the present, which is the Present Perfect: has lived.",
    g2bw="‘While’ marks the longer background action that ‘knocked’ interrupts, so it takes the Past Continuous: was reading.",
    g3aw="A fixed arrangement — the table is already booked — takes the Present Continuous even though it is in the future: is meeting.",
    g3bw="The if-clause of a First Conditional takes the Present Simple, never ‘will’.",
    g4aw="The main clause of a First Conditional is where ‘will’ belongs: will go.",
    g4bw="‘Seafood’ is uncountable, so it takes ‘a lot of’ or ‘much’ — never ‘many’.",

    ec1w="‘For’ goes with a length of time (‘five years’); ‘since’ goes with a starting point (‘2019’, ‘March’). A duration needs ‘for’.",
    ec2w="The if-clause of a First Conditional never takes ‘will’ — only the main clause does.",
    ec3w="‘Better’ is already a comparative, so it never takes ‘more’ in front of it. Double comparatives like ‘more better’ do not exist in standard English.",
    ec4w="The passive needs the past participle, not the past simple: write → wrote → written. So ‘was wrote’ becomes ‘was written’.",
    ec5w="‘Money’ is uncountable, so it pairs with ‘much’. ‘Many’ is for countable plural nouns.",
    ec6w="‘Which’ refers to things, not people, so this needs ‘who’. ‘That’ is also accepted here — it can replace either in everyday speech.",
)

EXPLAIN['de'] = dict(
    q1w="Present Continuous, für etwas, das gerade jetzt passiert. ‘Listen!’ zeigt auf diesen Moment, also passen ‘knocks’, ‘knocked’ und ‘was knocking’ alle nicht.",
    q2w="‘While’ + Past Continuous beschreibt eine längere Hintergrundhandlung, in die ein anderes Ereignis hineinschneidet — hier ‘rang’. Die anderen drei sind Präsensformen und können nicht neben einem Ereignis in der Vergangenheit stehen.",
    q3w="‘Since’ + Zeitpunkt verlangt das Present Perfect. ‘Lives’ und ‘is living’ sind Präsensformen, und ‘lived’ ist Past Simple, was ‘since 2019’ nicht zulässt.",
    q4w="‘I think…’ leitet eine Meinung ohne konkrete Anhaltspunkte ein, und das ist der klassische Auslöser für ‘will’. Die anderen sind Gegenwarts- oder Vergangenheitsformen und sagen nichts voraus.",
    q5w="‘The’ plus ein Vergleich mit allem anderen in einer Gruppe verlangt den Superlativ. ‘The goodest’ und ‘more good’ gibt es im Englischen gar nicht, und ‘the better’ ist ein Komparativ.",
    q6w="‘Must’ ist starke Verpflichtung, und genau das ist ein Gesetz. ‘Might’ und ‘could’ drücken Möglichkeit aus, ‘would’ gehört zu hypothetischen Situationen.",
    q7w="Der if-Satz eines First Conditional steht im Present Simple. ‘Will rain’ und ‘would rain’ können nicht hinein, und ‘rained’ ist die falsche Zeit für eine reale Zukunftsmöglichkeit.",
    q8w="‘Would learn’ im Hauptsatz macht daraus ein Second Conditional, und dessen if-Satz braucht das Past Simple. Die Situation ist vorgestellt, nicht wahrscheinlich.",
    q9w="Eine Brücke baut sich nicht selbst, also braucht es das Passiv: ‘be’ + Partizip Perfekt. ‘Built’ allein fehlt das Hilfsverb, die beiden anderen sind aktiv.",
    q10w="‘Who’ eröffnet einen Relativsatz über eine Person. ‘Which’ steht für Dinge, ‘whose’ zeigt Besitz an, und ‘where’ verweist auf einen Ort.",

    t1w="Falsch. Das Present Perfect steht nie mit einer abgeschlossenen Zeitangabe. Für ‘yesterday’ oder ‘in 2010’ nimmt das Englische das Past Simple: ‘I visited Paris in 2010.’",
    t2w="Richtig. ‘Must’ hat keine eigene Vergangenheitsform, deshalb wechselt das Englische für Verpflichtung in der Vergangenheit zu ‘had to’.",
    t3w="Falsch. Der if-Satz steht im Present Simple — ‘If it rains…’ — und ‘will’ gehört in den Hauptsatz: ‘…we’ll cancel the picnic.’",
    t4w="Richtig. ‘The’ hebt eine Sache als einzigartig in ihrer Gruppe hervor: the best, the tallest, the most expensive.",
    t5w="Richtig. Immer ‘be’ plus Partizip Perfekt des Hauptverbs: is built, was written, has been finished.",
    t6w="Richtig. ‘Who’ bleibt Personen vorbehalten und ‘which’ den Dingen — auch wenn ‘that’ in der Alltagssprache beides ersetzen kann.",

    o1w="Passiv: Subjekt + ‘be’ (was) + Partizip Perfekt (built). Die Jahreszahl steht am Ende.",
    o2w="‘Who lives next door’ ist ein Relativsatz zu ‘the man’, steht also direkt dahinter und vor dem Hauptverb.",
    o3w="Fragewort + Hilfsverb (‘did’) + Subjekt + Grundform. Beachte: ‘go’ bleibt in der Grundform, sobald ‘did’ die Vergangenheit übernommen hat.",
    o4w="Second Conditional: if + Past Simple (‘were’), dann would + Grundform (‘I’d travel’).",
    o5w="‘Much’ verstärkt den Komparativ ‘bigger’, und ‘than’ leitet das zweite Vergleichsobjekt ein.",

    g1w="Zwei verschiedene Zeiten in einem Satz — deshalb ist es eine Zeile und nicht zwei.",
    g1aw="‘Usually’ kennzeichnet eine Gewohnheit, also Present Simple: gets up.",
    g1bw="‘This morning’ mit einem abgeschlossenen Ereignis verlangt das Past Simple. Oversleep ist unregelmäßig: overslept.",
    g2aw="‘For almost three years now’ ist ein Zeitraum, der bis in die Gegenwart reicht — das ist das Present Perfect: has lived.",
    g2bw="‘While’ markiert die längere Hintergrundhandlung, die ‘knocked’ unterbricht, also Past Continuous: was reading.",
    g3aw="Eine feste Verabredung — der Tisch ist schon reserviert — steht im Present Continuous, auch wenn sie in der Zukunft liegt: is meeting.",
    g3bw="Der if-Satz eines First Conditional steht im Present Simple, nie mit ‘will’.",
    g4aw="Der Hauptsatz eines First Conditional ist der Ort für ‘will’: will go.",
    g4bw="‘Seafood’ ist nicht zählbar, nimmt also ‘a lot of’ oder ‘much’ — nie ‘many’.",

    ec1w="‘For’ steht bei einer Zeitdauer (‘five years’), ‘since’ bei einem Anfangspunkt (‘2019’, ‘March’). Eine Dauer braucht ‘for’.",
    ec2w="Der if-Satz eines First Conditional nimmt nie ‘will’ — das tut nur der Hauptsatz.",
    ec3w="‘Better’ ist bereits ein Komparativ und steht deshalb nie mit ‘more’ davor. Doppelte Komparative wie ‘more better’ gibt es im Standardenglischen nicht.",
    ec4w="Das Passiv braucht das Partizip Perfekt, nicht das Past Simple: write → wrote → written. Aus ‘was wrote’ wird also ‘was written’.",
    ec5w="‘Money’ ist nicht zählbar und steht deshalb mit ‘much’. ‘Many’ gehört zu zählbaren Pluralformen.",
    ec6w="‘Which’ bezieht sich auf Dinge, nicht auf Personen, hier braucht es also ‘who’. ‘That’ wird hier ebenfalls akzeptiert — es kann in der Alltagssprache beides ersetzen.",
)

EXPLAIN['es'] = dict(
    q1w="Present Continuous, para algo que está ocurriendo ahora mismo. ‘Listen!’ señala este momento, así que ‘knocks’, ‘knocked’ y ‘was knocking’ no encajan.",
    q2w="‘While’ + Past Continuous describe una acción de fondo más larga que otro hecho pasado interrumpe — aquí ‘rang’. Las otras tres son formas de presente y no pueden acompañar a un hecho en pasado.",
    q3w="‘Since’ + un momento concreto exige el Present Perfect. ‘Lives’ e ‘is living’ son presentes, y ‘lived’ es Past Simple, que no admite ‘since 2019’.",
    q4w="‘I think…’ introduce una opinión sin pruebas detrás, y ese es el detonante clásico de ‘will’. Las demás son formas de presente o pasado y no predicen nada.",
    q5w="‘The’ más una comparación con todo lo demás de un grupo pide el superlativo. ‘The goodest’ y ‘more good’ no existen en inglés, y ‘the better’ es un comparativo.",
    q6w="‘Must’ expresa obligación fuerte, que es justo lo que es una ley. ‘Might’ y ‘could’ expresan posibilidad, y ‘would’ pertenece a situaciones hipotéticas.",
    q7w="La oración con if de un First Conditional va en Present Simple. ‘Will rain’ y ‘would rain’ no caben dentro, y ‘rained’ es el tiempo equivocado para una posibilidad futura real.",
    q8w="‘Would learn’ en la oración principal convierte esto en un Second Conditional, y su oración con if necesita el Past Simple. La situación es imaginada, no probable.",
    q9w="Un puente no se construye solo, así que hace falta la pasiva: ‘be’ + participio. A ‘built’ solo le falta el auxiliar, y las otras dos son activas.",
    q10w="‘Who’ abre una oración de relativo referida a una persona. ‘Which’ es para cosas, ‘whose’ indica posesión y ‘where’ señala un lugar.",

    t1w="Falso. El Present Perfect nunca se combina con una expresión de tiempo terminado. Para ‘yesterday’ o ‘in 2010’ el inglés usa el Past Simple: ‘I visited Paris in 2010.’",
    t2w="Verdadero. ‘Must’ no tiene forma de pasado propia, así que para la obligación en pasado el inglés pasa a ‘had to’.",
    t3w="Falso. La oración con if va en Present Simple — ‘If it rains…’ — y ‘will’ va en la principal: ‘…we’ll cancel the picnic.’",
    t4w="Verdadero. ‘The’ señala algo como único dentro de su grupo: the best, the tallest, the most expensive.",
    t5w="Verdadero. Siempre ‘be’ más el participio del verbo principal: is built, was written, has been finished.",
    t6w="Verdadero. ‘Who’ se reserva para personas y ‘which’ para cosas — aunque ‘that’ puede sustituir a cualquiera de los dos en el habla cotidiana.",

    o1w="Pasiva: sujeto + ‘be’ (was) + participio (built). La fecha va al final.",
    o2w="‘Who lives next door’ es una oración de relativo referida a ‘the man’, así que va justo detrás y antes del verbo principal.",
    o3w="Palabra interrogativa + auxiliar (‘did’) + sujeto + verbo en forma base. Fíjate en que ‘go’ se queda en forma base una vez que ‘did’ ha asumido el pasado.",
    o4w="Second Conditional: if + Past Simple (‘were’), y luego would + forma base (‘I’d travel’).",
    o5w="‘Much’ intensifica el comparativo ‘bigger’, y ‘than’ introduce el segundo elemento de la comparación.",

    g1w="Dos tiempos distintos en una sola frase, y por eso es una fila y no dos.",
    g1aw="‘Usually’ marca un hábito, así que es Present Simple: gets up.",
    g1bw="‘This morning’ con un hecho terminado pide el Past Simple. Oversleep es irregular: overslept.",
    g2aw="‘For almost three years now’ es un periodo que llega hasta el presente, es decir el Present Perfect: has lived.",
    g2bw="‘While’ marca la acción de fondo más larga que ‘knocked’ interrumpe, así que va en Past Continuous: was reading.",
    g3aw="Un plan fijado — la mesa ya está reservada — va en Present Continuous aunque se refiera al futuro: is meeting.",
    g3bw="La oración con if de un First Conditional va en Present Simple, nunca con ‘will’.",
    g4aw="La oración principal de un First Conditional es donde va ‘will’: will go.",
    g4bw="‘Seafood’ es incontable, así que lleva ‘a lot of’ o ‘much’ — nunca ‘many’.",

    ec1w="‘For’ acompaña a una duración (‘five years’); ‘since’ acompaña a un punto de partida (‘2019’, ‘March’). Una duración necesita ‘for’.",
    ec2w="La oración con if de un First Conditional nunca lleva ‘will’ — solo la principal lo hace.",
    ec3w="‘Better’ ya es un comparativo, así que nunca lleva ‘more’ delante. Los comparativos dobles como ‘more better’ no existen en inglés estándar.",
    ec4w="La pasiva necesita el participio, no el pasado simple: write → wrote → written. Así que ‘was wrote’ pasa a ‘was written’.",
    ec5w="‘Money’ es incontable, así que se combina con ‘much’. ‘Many’ es para sustantivos contables en plural.",
    ec6w="‘Which’ se refiere a cosas, no a personas, así que aquí hace falta ‘who’. ‘That’ también se acepta — puede sustituir a cualquiera de los dos en el habla cotidiana.",
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
