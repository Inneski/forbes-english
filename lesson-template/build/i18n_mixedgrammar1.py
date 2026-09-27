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

# The passage, identical in every language: it is the English under test.
# Printed WITH its gaps on the story panel, so the learner reads the whole
# text before answering it in pieces. The first version printed it with the
# answers filled in, one slide before the slides that score them.
STORY_A = ('Elena usually ______ <em>(get up)</em> at seven o’clock, but this '
           'morning she ______ <em>(oversleep)</em> because her alarm didn’t ring. '
           'She ______ <em>(live)</em> in this apartment for almost three years '
           'now, and she loves the quiet street.')
STORY_B = ('Last night, while she ______ <em>(read)</em> a book, her neighbour '
           'knocked on the door to borrow some sugar. Tomorrow, Elena ______ '
           '<em>(meet)</em> her sister for lunch — they’ve already booked a table. '
           'If the weather ______ <em>(be)</em> nice this weekend, they ______ '
           '<em>(go)</em> to the coast afterwards. The new restaurant serves '
           '______ <em>(a lot of / much)</em> fresh seafood.')

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
    storyA=STORY_A,
    storyB=STORY_B,

    # ── multiple choice ───────────────────────────────────────────────
    # The scene, never the grammar or the answer: "If it rains" was the title
    # of an item whose key is "rains".
    q1t='At the door', q2t='The phone', q3t='Madrid', q4t='The tournament',
    q5t='Film of the year', q6t='In the car', q7t='The picnic',
    q8t='Free time', q9t='The bridge', q10t='The woman next door',

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

    # Not the error's name: "A double comparative" did the finding for them.
    ec1t='Five years', ec2t='A phone call', ec3t='The new song',
    ec4t='An old letter', ec5t='The wallet', ec6t='My cousin',
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
    storyA=STORY_A,
    storyB=STORY_B,

    q1t='An der Tür', q2t='Das Telefon', q3t='Madrid', q4t='Das Turnier',
    q5t='Film des Jahres', q6t='Im Auto', q7t='Das Picknick',
    q8t='Freizeit', q9t='Die Brücke', q10t='Die Frau von nebenan',

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

    ec1t='Fünf Jahre', ec2t='Ein Anruf', ec3t='Das neue Lied',
    ec4t='Ein alter Brief', ec5t='Das Portemonnaie', ec6t='Meine Cousine',
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
    storyA=STORY_A,
    storyB=STORY_B,

    q1t='En la puerta', q2t='El teléfono', q3t='Madrid', q4t='El torneo',
    q5t='La película del año', q6t='En el coche', q7t='El pícnic',
    q8t='Tiempo libre', q9t='El puente', q10t='La mujer de al lado',

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

    ec1t='Cinco años', ec2t='Una llamada', ec3t='La canción nueva',
    ec4t='Una carta antigua', ec5t='La cartera', ec6t='Mi prima',
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
# Ported 2026-09-25 from mixed_b1_<lang>.py P1 (19b39ed), replacing the
# first version, which cited forms in lowercase and single quotes. House
# convention: grammar forms in CAPS, cited words in double quotes.
EXPLAIN['en'] = dict(
    q1w="“Listen!” means now, so the action is in progress: IS + knocking. “Knocks” is a habit; “knocked” and “was knocking” are past.",
    q2w="WHILE + WAS / WERE + -ING gives the longer background action; the Past Simple (“rang”) interrupts it. The other three are present forms.",
    q3w="SINCE + a point in time (2019) needs HAS / HAVE + past participle. “Lived” cannot go with “since”, and the present forms cannot either.",
    q4w="“I think” introduces an opinion about the future: WILL + verb. “Is winning” would mean the match is happening now.",
    q5w="Compared with every film this year, so the superlative: THE BEST. “Goodest” and “more good” do not exist; “better” compares only two.",
    q6w="A law is a strong obligation: MUST + verb. “Might” and “could” are possibility; “would” is imaginary.",
    q7w="First conditional: IF + Present Simple, then WILL in the other clause. WILL never goes after IF here.",
    q8w="“Would learn” shows an imaginary situation, so the second conditional: IF + Past Simple (“had”).",
    q9w="A bridge does not build itself, so the passive: WAS + past participle. “Built” alone is active and has no subject doing it.",
    q10w="WHO for people. WHICH is for things, WHOSE for possession, WHERE for places.",

    t1w="False. A finished time takes the Past Simple: “I visited Paris in 2010”, not “I have visited”.",
    t2w="True. MUST has no past form of its own, so for the past we use HAD TO.",
    t3w="False. After IF, the Present Simple (“If it rains”); WILL goes in the other clause (“we’ll stay in”).",
    t4w="True. THE marks one thing as the only one in its group: THE best, THE tallest, THE most expensive.",
    t5w="True. “Is built”, “was written”, “has been finished”: always a form of BE + past participle.",
    t6w="True. THAT can replace either in everyday English, but WHO is only for people and WHICH only for things.",

    o1w="The passive: subject + WAS + past participle, then the time.",
    o2w="“Who lives next door” comes straight after “the man” and tells us which man. Then the main verb, IS.",
    o3w="Question word + DID + subject + base verb. After DID the verb has no -ED: “go”, not “went”.",
    o4w="Second conditional: IF + Past Simple (“were”), then WOULD (’D) + verb.",
    o5w="MUCH goes in front of a comparative to make it stronger; THAN introduces the second thing.",

    g1w="“Usually” is a habit: Present Simple, and “she” takes -S (“gets up”). “This morning” is finished: Past Simple “overslept” (irregular).",
    g2aw="“For almost three years now” runs up to today: HAS + lived. HAS BEEN living is also correct.",
    g2bw="WHILE + WAS + -ING for the longer action; the knock (“knocked”) interrupts it.",
    g3aw="A table is booked, so it is an arrangement: IS + meeting. IS GOING TO meet is also correct.",
    g3bw="First conditional. After IF, the Present Simple (“is”), never WILL.",
    g4aw="First conditional. The result takes WILL + go (“they’ll go”). ARE GOING TO go is also correct.",
    g4bw="In a positive sentence we say A LOT OF. MUCH is for negatives and questions: “They don’t serve much seafood.”",

    ec1w="FOR + a length of time (five years). SINCE + a starting point (2019, March).",
    ec2w="After IF in a first conditional, the Present Simple: “If I have time”. WILL stays in the other clause.",
    ec3w="“Better” is already a comparative. MORE + BETTER is never correct.",
    ec4w="The passive needs the past participle: write → wrote → WRITTEN.",
    ec5w="“Money” is uncountable: MUCH, not MANY. MANY is for plural nouns: “many coins”.",
    ec6w="WHICH is for things. For a person, WHO (or THAT).",
)

EXPLAIN['de'] = dict(
    q1w="„Listen!“ heißt jetzt, die Handlung läuft gerade: IS + knocking. „Knocks“ ist eine Gewohnheit; „knocked“ und „was knocking“ sind Vergangenheit.",
    q2w="WHILE + WAS / WERE + -ING für die längere Hintergrundhandlung; das Past Simple („rang“) unterbricht sie. Die anderen drei sind Gegenwartsformen.",
    q3w="SINCE + Zeitpunkt (2019) braucht HAS / HAVE + Partizip. „Lived“ passt nicht zu „since“, die Gegenwartsformen auch nicht.",
    q4w="„I think“ leitet eine Meinung über die Zukunft ein: WILL + Verb. „Is winning“ hieße, das Spiel läuft gerade.",
    q5w="Verglichen mit allen Filmen des Jahres, also der Superlativ: THE BEST. „Goodest“ und „more good“ gibt es nicht; „better“ vergleicht nur zwei.",
    q6w="Ein Gesetz ist eine starke Pflicht: MUST + Verb. „Might“ und „could“ drücken Möglichkeit aus, „would“ etwas Gedachtes.",
    q7w="Bedingungssatz Typ 1: IF + Present Simple, WILL im anderen Satzteil. Nach IF steht hier nie WILL.",
    q8w="„Would learn“ zeigt eine gedachte Situation, also Typ 2: IF + Past Simple („had“).",
    q9w="Eine Brücke baut sich nicht selbst, also Passiv: WAS + Partizip. „Built“ allein ist aktiv, und niemand tut es.",
    q10w="WHO für Personen. WHICH für Dinge, WHOSE für Besitz, WHERE für Orte.",

    t1w="Falsch. Eine abgeschlossene Zeit verlangt das Past Simple: „I visited Paris in 2010“, nicht „I have visited“.",
    t2w="Richtig. MUST hat keine eigene Vergangenheitsform, für die Vergangenheit nehmen wir HAD TO.",
    t3w="Falsch. Nach IF steht Present Simple („If it rains“); WILL kommt in den anderen Satzteil („we’ll stay in“).",
    t4w="Richtig. THE hebt eine Sache als die einzige ihrer Gruppe hervor: THE best, THE tallest, THE most expensive.",
    t5w="Richtig. „Is built“, „was written“, „has been finished“: immer eine Form von BE + Partizip.",
    t6w="Richtig. THAT kann im Alltag beide ersetzen, aber WHO steht nur für Personen und WHICH nur für Dinge.",

    o1w="Passiv: Subjekt + WAS + Partizip, dann die Zeit.",
    o2w="„Who lives next door“ steht direkt nach „the man“ und sagt, welcher Mann. Dann das Hauptverb, IS.",
    o3w="Fragewort + DID + Subjekt + Grundform. Nach DID hat das Verb kein -ED: „go“, nicht „went“.",
    o4w="Bedingungssatz Typ 2: IF + Past Simple („were“), dann WOULD (’D) + Verb.",
    o5w="MUCH vor dem Komparativ verstärkt ihn; THAN leitet das Zweite ein.",

    g1w="„Usually“ ist eine Gewohnheit: Present Simple, und „she“ bekommt -S („gets up“). „This morning“ ist vorbei: Past Simple „overslept“ (unregelmäßig).",
    g2aw="„For almost three years now“ reicht bis heute: HAS + lived. HAS BEEN living ist auch richtig.",
    g2bw="WHILE + WAS + -ING für die längere Handlung; das Klopfen („knocked“) unterbricht sie.",
    g3aw="Der Tisch ist reserviert, es ist also eine Verabredung: IS + meeting. IS GOING TO meet ist auch richtig.",
    g3bw="Bedingungssatz Typ 1. Nach IF steht Present Simple („is“), nie WILL.",
    g4aw="Bedingungssatz Typ 1. Die Folge bekommt WILL + go („they’ll go“). ARE GOING TO go ist auch richtig.",
    g4bw="Im bejahten Satz sagt man A LOT OF. MUCH steht in verneinten Sätzen und Fragen: „They don’t serve much seafood.“",

    ec1w="FOR + Zeitdauer (five years). SINCE + Zeitpunkt (2019, March).",
    ec2w="Nach IF im Bedingungssatz Typ 1 steht Present Simple: „If I have time“. WILL bleibt im anderen Satzteil.",
    ec3w="„Better“ ist schon ein Komparativ. MORE + BETTER ist nie richtig.",
    ec4w="Das Passiv braucht das Partizip: write → wrote → WRITTEN.",
    ec5w="„Money“ ist unzählbar: MUCH, nicht MANY. MANY steht vor Pluralnomen: „many coins“.",
    ec6w="WHICH steht für Dinge. Für eine Person WHO (oder THAT).",
)

EXPLAIN['es'] = dict(
    q1w="«Listen!» significa ahora: la acción está en curso, IS + knocking. «Knocks» es un hábito; «knocked» y «was knocking» son pasado.",
    q2w="WHILE + WAS / WERE + -ING da la acción de fondo, más larga; el Past Simple («rang») la interrumpe. Las otras tres son formas de presente.",
    q3w="SINCE + un momento (2019) pide HAS / HAVE + participio. «Lived» no va con «since», y las formas de presente tampoco.",
    q4w="«I think» introduce una opinión sobre el futuro: WILL + verbo. «Is winning» querría decir que el partido se juega ahora.",
    q5w="Comparado con todas las películas del año, así que el superlativo: THE BEST. «Goodest» y «more good» no existen; «better» compara solo dos.",
    q6w="Una ley es una obligación fuerte: MUST + verbo. «Might» y «could» son posibilidad; «would» es hipotético.",
    q7w="Primer condicional: IF + Present Simple, y WILL en la otra parte. Aquí WILL nunca va después de IF.",
    q8w="«Would learn» muestra una situación imaginaria, así que segundo condicional: IF + Past Simple («had»).",
    q9w="Un puente no se construye solo, así que la pasiva: WAS + participio. «Built» solo es activa y nadie hace la acción.",
    q10w="WHO para personas. WHICH para cosas, WHOSE para posesión, WHERE para lugares.",

    t1w="Falso. Un tiempo terminado pide el Past Simple: «I visited Paris in 2010», no «I have visited».",
    t2w="Verdadero. MUST no tiene pasado propio, así que para el pasado usamos HAD TO.",
    t3w="Falso. Después de IF, Present Simple («If it rains»); WILL va en la otra parte («we’ll stay in»).",
    t4w="Verdadero. THE señala una cosa como la única de su grupo: THE best, THE tallest, THE most expensive.",
    t5w="Verdadero. «Is built», «was written», «has been finished»: siempre una forma de BE + participio.",
    t6w="Verdadero. En el inglés de cada día THAT puede sustituir a los dos, pero WHO es solo para personas y WHICH solo para cosas.",

    o1w="La pasiva: sujeto + WAS + participio, y luego el tiempo.",
    o2w="«Who lives next door» va justo después de «the man» y dice qué hombre. Luego el verbo principal, IS.",
    o3w="Palabra interrogativa + DID + sujeto + infinitivo. Después de DID el verbo no lleva -ED: «go», no «went».",
    o4w="Segundo condicional: IF + Past Simple («were»), luego WOULD (’D) + verbo.",
    o5w="MUCH delante de un comparativo lo refuerza; THAN introduce lo segundo.",

    g1w="«Usually» es un hábito: Present Simple, y «she» lleva -S («gets up»). «This morning» ya terminó: Past Simple «overslept» (irregular).",
    g2aw="«For almost three years now» llega hasta hoy: HAS + lived. HAS BEEN living también es correcto.",
    g2bw="WHILE + WAS + -ING para la acción más larga; el golpe en la puerta («knocked») la interrumpe.",
    g3aw="La mesa está reservada, así que es un plan fijo: IS + meeting. IS GOING TO meet también es correcto.",
    g3bw="Primer condicional. Después de IF, Present Simple («is»), nunca WILL.",
    g4aw="Primer condicional. El resultado lleva WILL + go («they’ll go»). ARE GOING TO go también es correcto.",
    g4bw="En una frase afirmativa decimos A LOT OF. MUCH es para negativas y preguntas: «They don’t serve much seafood.»",

    ec1w="FOR + una duración (five years). SINCE + un punto de partida (2019, March).",
    ec2w="Después de IF en el primer condicional, Present Simple: «If I have time». WILL se queda en la otra parte.",
    ec3w="«Better» ya es comparativo. MORE + BETTER nunca es correcto.",
    ec4w="La pasiva necesita el participio: write → wrote → WRITTEN.",
    ec5w="«Money» es incontable: MUCH, no MANY. MANY es para sustantivos en plural: «many coins».",
    ec6w="WHICH es para cosas. Para una persona, WHO (o THAT).",
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
