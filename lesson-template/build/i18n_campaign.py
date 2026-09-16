# -*- coding: utf-8 -*-
"""Interface strings for The Monthly Review (B2) — EN, DE, ES and Croatian.

English, German and Spanish are the site minimum (HOUSE-STYLE §8, and
CLAUDE.md's standing constraint of 2026-09-04). **Croatian is the fourth, and
it is the one that matters here** — the student this deck was written for is
Croatian, and this is the first lesson on the site to carry the language at
all. Adding it touched three shared files as well as this one:
`chrome_i18n.CHROME['hr']` for the twenty-six chrome strings, `LANGS` in
`lesson-template.html` for the switcher label, and `deck.assemble`'s
`all_langs` so every deck emits the empty placeholder. All three are additive:
a deck with no `hr` block simply never offers it.

The remaining seven stay as {} and are therefore not offered — partial is a
failure, empty is an honest placeholder.

The scope boundary, which this deck draws in a slightly different place from
the grammar decks and does so deliberately:

  * **Translated**: the cover, the section eyebrows and titles, the task
    hints, the sort bin labels, the *body and note of every teaching card*,
    the MC stems, the MC context lines, the activation briefs and the result
    bands. Everything that is scaffolding around the language.

  * **Not translated, in any language**: every multiple-choice option, gap
    sentence, word bank chip, sort item, order chunk, match pair, explanation
    and activation chip. Those are the English under test.

Two consequences worth stating, because both were decisions rather than
oversights.

The teaching cards use deck.teach's SIX-item form, so the rule text travels
with its heading — the five-item form leaves a German heading over an English
rule, which is the half-finished screen §8 exists to prevent. But `head_key`
is None on all twenty-three cards: the heading of each card IS the English
pattern being taught (<em>rise / fall by</em>, <em>coincided with</em>, <em>off
the top of my head</em>) and translating it would hand the learner the answer
to the gap fill and to four of the eight questions.

Every MC stem carries a key and translates, which the grammar decks do not do.
The reason is in deck.mc's own docstring: a stem with no blank in it — "Which
sentence states that accurately?" — is a question *about* English rather than
a piece of English under test, so translating it costs nothing and removes a
comprehension hurdle that is not the point of the exercise. The context lines
above them translate for the same reason: the situation is what makes the
item answerable at all.

Where a German or Spanish line quotes an English phrase (<em>off the top of my
head</em>, <em>we put it down to</em>, <em>pacing ahead</em>), the quotation
stays in English. It is the object under discussion, not instructions about
the task.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

# Emitted from CHROME verbatim, sorted in with the body.
#
# actSpeakKind and resNext are NOT lifted: CHROME carries the generic
# 'Discussion · in pairs' and results line, and this lesson wants its own
# hand-off sentence. Both are declared in T below instead.
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
    'hr': {'branchLocked': "'Tvoj zapisnik ne podržava ovaj završetak'",
           'glossHide': "'Sakrij'",
           'glossShow': "'Prevedi'",
           'ledClues': "'Tragovi'",
           'ledDp': "'DP'",
           'ledTime': "'Vrijeme'"},
}

T = {}

# ── ENGLISH ────────────────────────────────────────────────────────────
T['en'] = dict(
    coverTitle='The Monthly <em>Review</em>',
    coverSub='Reporting a campaign in English &mdash; the numbers, the reason, the proposal, and the question you did not prepare for',
    chipLevel='B2 &middot; Agency &amp; client reporting',
    chipFocus='Performance language and thinking on your feet',
    chipCount='NSLIDES slides',

    t1Eyebrow='The first sentence of every report',
    t1Title='Four patterns for a number that moved',
    t1b1='The <em>size</em> of the move: <em>CPA fell by 14%</em>.',
    t1n1='Never <em>fell with 14%</em>, never <em>fell on 14%</em>.',
    t1b2='The <em>level</em> it ended at: <em>CTR rose to 3.1%</em>.',
    t1n2='One says how far it moved, the other where it stopped.',
    t1b3='Both ends: <em>from &euro;38 to &euro;32 in three weeks</em>.',
    t1n3='Use it when the starting point is the point.',
    t1b4='The comparison: <em>spend is up 11% on last month</em>.',
    t1n4='Also <em>month on month</em>, <em>year on year</em>, <em>versus Q2</em>.',

    t2Eyebrow='The claim you can defend',
    t2Title='Cause, coincidence, or not yet known',
    t2b1='You are asserting a mechanism. Say it when you can show one.',
    t2n1='The client is entitled to ask <em>how do you know?</em>',
    t2b2='You are asserting timing, and nothing more than timing.',
    t2n2='Honest, and it survives someone explaining it differently.',
    t2b3='Your reading, marked as yours. A judgement, offered as one.',
    t2n3='The <em>we</em> is doing real work here. Keep it.',
    t2b4='A complete answer &mdash; if you add when you <em>will</em> know.',
    t2n4='Without a date it sounds like avoiding the question.',

    t3Eyebrow='Four pairs people collapse in English',
    t3Title='The metrics, said precisely',
    t3b1='Reach counts <em>people</em>. Impressions count <em>times shown</em>.',
    t3n1='Impressions are always the bigger number of the two.',
    t3b2='Clicks per impression; then actions per visit. Two stages.',
    t3n2='High CTR and low CVR is a landing-page conversation.',
    t3b3='Cost of a click, cost of a customer, revenue per unit spent.',
    t3n3='Only the last is a ratio: <em>a 4x ROAS</em>, not <em>4%</em>.',
    t3b4='Budget is allocated, spend is gone. <em>Pacing</em> is the gap.',
    t3n4='<em>We are pacing ahead</em> means it will run out early.',

    t4Eyebrow='Bad news, first, in one sentence',
    t4Title='Saying it missed without sounding careless',
    t4b1='<em>We came in under target on conversions</em> &mdash; the number, plainly.',
    t4n1='Careful: under <em>budget</em> is good news, under <em>target</em> is not.',
    t4b2='<em>That one&rsquo;s on us.</em> &middot; <em>That sat with the platform.</em>',
    t4n2='Either is fine. Having no answer is not.',
    t4b3='<em>We caught it on day seven and it is corrected.</em>',
    t4n3='A miss with a date and a fix stops being an argument.',

    t5Eyebrow='Who decides',
    t5Title='Proposing without taking the decision',
    t5b1='A proposal. It leaves the decision with the person paying.',
    t5n1='The safest opener when they have to sign it off.',
    t5b2='A decision already taken. You are informing, not asking.',
    t5n2='Correct for your own team. Risky with a client.',
    t5b3='<em>shift</em> &middot; <em>scale back</em> &middot; <em>pause</em> &middot; <em>hold off on</em> &middot; <em>double down on</em>',
    t5n3='<em>Shift budget out of X and into Y</em> is the fixed pattern.',
    t5b4='<em>I&rsquo;d give it another fortnight before we judge it.</em>',
    t5n4='A date turns &ldquo;wait&rdquo; into a plan.',

    t6Eyebrow='The question you did not prepare for',
    t6Title='Two seconds, bought properly',
    t6b1='Gives a figure and flags it as approximate, in four words.',
    t6n1='Then <em>but let me confirm that</em>. Always finish it.',
    t6b2='Declines to guess and promises the answer. Add <em>by this afternoon</em>.',
    t6n2='A promise with no time on it is not a promise.',
    t6b3='Buys the two seconds and sounds candid rather than stalling.',
    t6n3='Follow it with <em>the honest answer is</em> &mdash; then answer.',
    t6b4='Turns a guess into a checked answer, conceding nothing.',
    t6n4='Better than silence. Silence reads as not knowing.',

    sortEyebrow='Before you say why',
    sortTitle='How much does the sentence claim to know?',
    sortHint='Click a line, then the box it belongs in. Every line is about a real movement in the numbers &mdash; what changes is how much it claims about the reason.',
    sortBin1='Claims a cause',
    sortBin2='Claims only timing',
    sortBin3='Claims nothing yet',

    bankLabel='Word bank:',
    gapEyebrow='The grammar of the report',
    gapTitleA='Complete the movement',
    gapHintA='One word per gap. Three of the six are not needed.',
    gapTitleB='Complete the proposal',
    gapHintB='One verb per gap. Three of the six are not needed &mdash; and all three are real phrases from this lesson.',

    matEyebrow='Precision',
    matTitle='Match the metric to what it actually counts',
    matHint='Six terms, six definitions. Four of them are routinely used as if they were interchangeable; none of them are.',

    ordEyebrow='Build the sentence',
    ordTitleA='Headline first',
    ordHintA='Click the parts in order. The client hears the conclusion before the detail.',
    ordTitleB='A proposal they can say no to',
    ordHintB='Click the parts in order: the evidence, the proposal, the size of it, then the date.',

    qEyebrow='On the call',
    qTitle='Which one would you actually say?',
    q1Stem='Which sentence reports the size of the movement correctly?',
    q2Ctx='Click-through rate was 2.4% in June. It is 3.1% now.',
    q2Stem='Which sentence states that accurately?',
    q3Ctx='The campaign was shown 840,000 times, to 210,000 different people.',
    q3Stem='Which sentence reports that correctly?',
    q4Ctx='Conversions rose 20% in the week a competitor&rsquo;s site was down. You have no other evidence.',
    q4Stem='Which sentence can you defend if the client asks how you know?',
    q5Ctx='The client asks whether the new creative is working. It has been live four days.',
    q5Stem='Which answer is both honest and useful?',
    q6Ctx='Your team used the wrong audience for a week. The client will see it in the numbers.',
    q6Stem='Which sentence would you say first?',
    q7Ctx='You want to move budget between channels. The client has to sign it off.',
    q7Stem='Which sentence leaves the decision with them?',
    q8Ctx='Mid-call, the client asks for a figure you do not have in front of you.',
    q8Stem='Which reply keeps your credibility?',

    actTitle='Now run the review',
    actUse='Use at least four:',
    actSpeakKind='Discussion &middot; in pairs',
    actSpeakBrief='Twelve minutes, then swap. One runs the monthly review; one is the client who has not read the deck and interrupts.',
    actSpeak1='Open the review with the headline in two sentences: what moved, which way, by how much. No slides.',
    actSpeak2='Client: &ldquo;So why did conversions drop?&rdquo; You have the timing and no cause. Answer without inventing one.',
    actSpeak3='Client: &ldquo;What was last week&rsquo;s CPA?&rdquo; You do not have it. Answer, promise, keep the call moving.',
    actSpeak4='Propose moving a fifth of the budget. Leave the decision with them, and put a date on the review.',
    actWriteKind='Writing &middot; 160&ndash;200 words',
    actWriteBrief='Write the follow-up email that goes out after the call. Headline first; two numbers with the movement stated correctly; one thing that went wrong and where it sat; one proposal with a review date. Nothing the client has to scroll to find.',
    actPlaceholder='Thanks for your time this morning. The headline is…',

    resNext='Recognising the right sentence is the easy half. Now run the call &rarr;',
    resPerfect='Perfect score. You can hear the difference &mdash; saying it live, with a client interrupting, is the other half.',
    resStrong='Strong work. Look again at the ones you missed: almost all of them turn on one preposition or one verb.',
    resMid='A usable base. Re-read the four movement patterns and the cause slide before you speak.',
    resLow='Go back to the six teaching slides. Nearly every miss here is one word used as though it were a synonym of another.',
)

# ── GERMAN ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Das monatliche <em>Review</em>',
    coverSub='Eine Kampagne auf Englisch berichten &mdash; die Zahlen, der Grund, der Vorschlag und die Frage, auf die du dich nicht vorbereitet hast',
    chipLevel='B2 &middot; Agentur &amp; Kundenreporting',
    chipFocus='Sprache der Performance und spontanes Sprechen',
    chipCount='NSLIDES Folien',

    t1Eyebrow='Der erste Satz jedes Berichts',
    t1Title='Vier Muster für eine Zahl, die sich bewegt hat',
    t1b1='Die <em>Größe</em> der Veränderung: <em>CPA fell by 14%</em>.',
    t1n1='Nie <em>fell with 14%</em>, nie <em>fell on 14%</em>.',
    t1b2='Das erreichte <em>Niveau</em>: <em>CTR rose to 3.1%</em>.',
    t1n2='Das eine sagt, wie weit; das andere, wo es stehen blieb.',
    t1b3='Beide Enden: <em>from &euro;38 to &euro;32 in three weeks</em>.',
    t1n3='Nimm es, wenn der Ausgangspunkt die Pointe ist.',
    t1b4='Der Vergleich: <em>spend is up 11% on last month</em>.',
    t1n4='Auch <em>month on month</em>, <em>year on year</em>, <em>versus Q2</em>.',

    t2Eyebrow='Die Behauptung, die du halten kannst',
    t2Title='Ursache, zeitliches Zusammentreffen oder noch offen',
    t2b1='Du behauptest einen Mechanismus. Sag es, wenn du ihn zeigen kannst.',
    t2n1='Der Kunde darf fragen: <em>how do you know?</em>',
    t2b2='Du behauptest nur den Zeitpunkt &mdash; und sonst nichts.',
    t2n2='Ehrlich, und es hält stand, wenn jemand anders erklärt.',
    t2b3='Deine Lesart, als solche gekennzeichnet. Ein Urteil, offen als Urteil.',
    t2n3='Das <em>we</em> leistet hier echte Arbeit. Lass es stehen.',
    t2b4='Eine vollständige Antwort &mdash; wenn du sagst, wann du es <em>wissen wirst</em>.',
    t2n4='Ohne Datum klingt es nach Ausweichen.',

    t3Eyebrow='Vier Paare, die im Englischen verschmelzen',
    t3Title='Die Kennzahlen, präzise gesagt',
    t3b1='Reach zählt <em>Personen</em>. Impressions zählen <em>Einblendungen</em>.',
    t3n1='Impressions sind immer die größere der beiden Zahlen.',
    t3b2='Klicks pro Einblendung; dann Aktionen pro Besuch. Zwei Stufen.',
    t3n2='Hohe CTR, niedrige CVR: ein Gespräch über die Landingpage.',
    t3b3='Kosten eines Klicks, Kosten eines Kunden, Umsatz je Euro.',
    t3n3='Nur das Letzte ist ein Verhältnis: <em>a 4x ROAS</em>, nicht <em>4%</em>.',
    t3b4='Budget ist zugeteilt, Spend ist ausgegeben. <em>Pacing</em> ist die Lücke.',
    t3n4='<em>We are pacing ahead</em> heißt: es reicht nicht bis zum Monatsende.',

    t4Eyebrow='Schlechte Nachrichten zuerst, in einem Satz',
    t4Title='Ein verfehltes Ziel nennen, ohne nachlässig zu wirken',
    t4b1='<em>We came in under target on conversions</em> &mdash; die Zahl, schlicht.',
    t4n1='Achtung: under <em>budget</em> ist gut, under <em>target</em> nicht.',
    t4b2='<em>That one&rsquo;s on us.</em> &middot; <em>That sat with the platform.</em>',
    t4n2='Beides ist in Ordnung. Gar keine Antwort ist es nicht.',
    t4b3='<em>We caught it on day seven and it is corrected.</em>',
    t4n3='Ein Fehler mit Datum und Behebung ist keine Diskussion mehr.',

    t5Eyebrow='Wer entscheidet',
    t5Title='Vorschlagen, ohne die Entscheidung zu nehmen',
    t5b1='Ein Vorschlag. Die Entscheidung bleibt bei dem, der zahlt.',
    t5n1='Der sicherste Einstieg, wenn der Kunde freigeben muss.',
    t5b2='Eine bereits getroffene Entscheidung. Du informierst, du fragst nicht.',
    t5n2='Richtig im eigenen Team. Beim Kunden riskant.',
    t5b3='<em>shift</em> &middot; <em>scale back</em> &middot; <em>pause</em> &middot; <em>hold off on</em> &middot; <em>double down on</em>',
    t5n3='<em>Shift budget out of X and into Y</em> ist das feste Muster.',
    t5b4='<em>I&rsquo;d give it another fortnight before we judge it.</em>',
    t5n4='Ein Datum macht aus &bdquo;abwarten&ldquo; einen Plan.',

    t6Eyebrow='Die Frage, auf die du dich nicht vorbereitet hast',
    t6Title='Zwei Sekunden, richtig erkauft',
    t6b1='Nennt eine Zahl und markiert sie als ungefähr &mdash; in vier Wörtern.',
    t6n1='Dann <em>but let me confirm that</em>. Immer zu Ende sprechen.',
    t6b2='Rät nicht und verspricht die Antwort. Ergänze <em>by this afternoon</em>.',
    t6n2='Ein Versprechen ohne Zeitangabe ist keines.',
    t6b3='Kauft die zwei Sekunden und klingt offen statt ausweichend.',
    t6n3='Danach <em>the honest answer is</em> &mdash; und dann antworte.',
    t6b4='Macht aus einer Vermutung eine geprüfte Antwort, ohne etwas preiszugeben.',
    t6n4='Besser als Schweigen. Schweigen wirkt wie Nichtwissen.',

    sortEyebrow='Bevor du sagst, warum',
    sortTitle='Wie viel behauptet der Satz zu wissen?',
    sortHint='Klicke eine Zeile an, dann das passende Feld. Jede Zeile beschreibt eine echte Bewegung in den Zahlen &mdash; unterschiedlich ist nur, wie viel sie über den Grund behauptet.',
    sortBin1='Behauptet eine Ursache',
    sortBin2='Behauptet nur den Zeitpunkt',
    sortBin3='Behauptet noch nichts',

    bankLabel='Wortspeicher:',
    gapEyebrow='Die Grammatik des Berichts',
    gapTitleA='Vervollständige die Bewegung',
    gapHintA='Ein Wort pro Lücke. Drei der sechs werden nicht gebraucht.',
    gapTitleB='Vervollständige den Vorschlag',
    gapHintB='Ein Verb pro Lücke. Drei der sechs werden nicht gebraucht &mdash; und alle drei sind echte Wendungen aus dieser Lektion.',

    matEyebrow='Präzision',
    matTitle='Ordne jede Kennzahl dem zu, was sie wirklich zählt',
    matHint='Sechs Begriffe, sechs Definitionen. Vier davon werden regelmäßig wie Synonyme benutzt; keiner ist eines.',

    ordEyebrow='Bau den Satz',
    ordTitleA='Die Kernaussage zuerst',
    ordHintA='Klicke die Teile der Reihe nach an. Der Kunde hört das Ergebnis vor den Details.',
    ordTitleB='Ein Vorschlag, zu dem man Nein sagen kann',
    ordHintB='Klicke die Teile der Reihe nach an: die Grundlage, der Vorschlag, der Umfang, dann das Datum.',

    qEyebrow='Im Call',
    qTitle='Was würdest du tatsächlich sagen?',
    q1Stem='Welcher Satz gibt die Größe der Veränderung richtig wieder?',
    q2Ctx='Die Click-through-Rate lag im Juni bei 2,4%. Jetzt liegt sie bei 3,1%.',
    q2Stem='Welcher Satz gibt das korrekt wieder?',
    q3Ctx='Die Kampagne wurde 840.000-mal ausgespielt, an 210.000 verschiedene Personen.',
    q3Stem='Welcher Satz berichtet das richtig?',
    q4Ctx='Die Conversions stiegen um 20% in der Woche, in der die Website eines Wettbewerbers ausfiel. Weitere Belege hast du nicht.',
    q4Stem='Welchen Satz kannst du halten, wenn der Kunde fragt, woher du das weißt?',
    q5Ctx='Der Kunde fragt, ob das neue Creative funktioniert. Es läuft seit vier Tagen.',
    q5Stem='Welche Antwort ist ehrlich und zugleich brauchbar?',
    q6Ctx='Dein Team hat eine Woche lang die falsche Zielgruppe verwendet. Der Kunde wird es in den Zahlen sehen.',
    q6Stem='Welchen Satz würdest du zuerst sagen?',
    q7Ctx='Du willst Budget zwischen Kanälen verschieben. Der Kunde muss es freigeben.',
    q7Stem='Welcher Satz lässt die Entscheidung bei ihm?',
    q8Ctx='Mitten im Call fragt der Kunde nach einer Zahl, die du nicht vor dir liegen hast.',
    q8Stem='Welche Antwort erhält deine Glaubwürdigkeit?',

    actTitle='Jetzt führe das Review',
    actUse='Verwende mindestens vier:',
    actSpeakKind='Diskussion &middot; zu zweit',
    actSpeakBrief='Zwölf Minuten, dann Rollentausch. Eine Person führt das Monatsreview; die andere ist der Kunde, der die Unterlagen nicht gelesen hat und dazwischenredet.',
    actSpeak1='Eröffne das Review mit der Kernaussage in zwei Sätzen: was sich bewegt hat, in welche Richtung, um wie viel. Ohne Folien.',
    actSpeak2='Kunde: &bdquo;Warum sind die Conversions gefallen?&ldquo; Du hast den Zeitpunkt, aber keine Ursache. Antworte, ohne eine zu erfinden.',
    actSpeak3='Kunde: &bdquo;Wie hoch war der CPA letzte Woche?&ldquo; Du hast die Zahl nicht. Antworte, sag etwas zu, und halte den Call in Bewegung.',
    actSpeak4='Schlag vor, ein Fünftel des Budgets zu verschieben. Lass die Entscheidung beim Kunden und nenne ein Datum für die Überprüfung.',
    actWriteKind='Schreiben &middot; 160&ndash;200 Wörter',
    actWriteBrief='Schreibe die Follow-up-Mail nach dem Call. Kernaussage zuerst; zwei Zahlen mit korrekt formulierter Bewegung; eine Sache, die schiefgelaufen ist, und wo sie lag; ein Vorschlag mit Überprüfungsdatum. Nichts, wonach der Kunde scrollen muss.',
    actPlaceholder='Thanks for your time this morning. The headline is…',

    resNext='Den richtigen Satz zu erkennen ist die leichte Hälfte. Jetzt führe den Call &rarr;',
    resPerfect='Volle Punktzahl. Du hörst den Unterschied &mdash; ihn live zu sagen, während ein Kunde dazwischenredet, ist die andere Hälfte.',
    resStrong='Starke Leistung. Sieh dir die Fehler noch einmal an: fast alle hängen an einer Präposition oder einem Verb.',
    resMid='Eine brauchbare Grundlage. Lies die vier Bewegungsmuster und die Folie zur Ursache noch einmal, bevor du sprichst.',
    resLow='Geh zurück zu den sechs Erklärungsfolien. Fast jeder Fehler hier ist ein Wort, das wie ein Synonym eines anderen benutzt wurde.',
)

# ── SPANISH ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='La <em>revisión</em> mensual',
    coverSub='Informar de una campaña en inglés &mdash; las cifras, el motivo, la propuesta y la pregunta que no llevabas preparada',
    chipLevel='B2 &middot; Agencia y reporte al cliente',
    chipFocus='Lenguaje de resultados y hablar sin preparación',
    chipCount='NSLIDES diapositivas',

    t1Eyebrow='La primera frase de cualquier informe',
    t1Title='Cuatro patrones para una cifra que se ha movido',
    t1b1='El <em>tamaño</em> del movimiento: <em>CPA fell by 14%</em>.',
    t1n1='Nunca <em>fell with 14%</em>, nunca <em>fell on 14%</em>.',
    t1b2='El <em>nivel</em> al que llegó: <em>CTR rose to 3.1%</em>.',
    t1n2='Uno dice cuánto se movió; el otro, dónde se quedó.',
    t1b3='Los dos extremos: <em>from &euro;38 to &euro;32 in three weeks</em>.',
    t1n3='Úsalo cuando el punto de partida sea lo importante.',
    t1b4='La comparación: <em>spend is up 11% on last month</em>.',
    t1n4='También <em>month on month</em>, <em>year on year</em>, <em>versus Q2</em>.',

    t2Eyebrow='La afirmación que puedes sostener',
    t2Title='Causa, coincidencia o todavía no se sabe',
    t2b1='Estás afirmando un mecanismo. Dilo cuando puedas enseñarlo.',
    t2n1='El cliente tiene derecho a preguntar <em>how do you know?</em>',
    t2b2='Estás afirmando una coincidencia temporal, y nada más.',
    t2n2='Honesto, y aguanta que otro lo explique de otra manera.',
    t2b3='Tu lectura, marcada como tuya. Un juicio, presentado como tal.',
    t2n3='El <em>we</em> hace aquí un trabajo real. No lo quites.',
    t2b4='Una respuesta completa &mdash; si añades cuándo lo <em>vas a</em> saber.',
    t2n4='Sin una fecha suena a esquivar la pregunta.',

    t3Eyebrow='Cuatro pares que en inglés se confunden',
    t3Title='Las métricas, dichas con precisión',
    t3b1='Reach cuenta <em>personas</em>. Impressions cuenta <em>veces mostrado</em>.',
    t3n1='Las impresiones son siempre la mayor de las dos cifras.',
    t3b2='Clics por impresión; luego acciones por visita. Dos etapas.',
    t3n2='CTR alto y CVR bajo es una conversación sobre la landing.',
    t3b3='Coste de un clic, coste de un cliente, ingreso por euro gastado.',
    t3n3='Solo el último es un ratio: <em>a 4x ROAS</em>, no <em>4%</em>.',
    t3b4='El budget se asigna; el spend ya se fue. <em>Pacing</em> es la diferencia.',
    t3n4='<em>We are pacing ahead</em> significa que se acabará antes de tiempo.',

    t4Eyebrow='La mala noticia primero, en una frase',
    t4Title='Decir que no se llegó sin parecer descuidado',
    t4b1='<em>We came in under target on conversions</em> &mdash; la cifra, sin adornos.',
    t4n1='Ojo: under <em>budget</em> es buena noticia; under <em>target</em> no.',
    t4b2='<em>That one&rsquo;s on us.</em> &middot; <em>That sat with the platform.</em>',
    t4n2='Cualquiera de las dos vale. No tener respuesta, no.',
    t4b3='<em>We caught it on day seven and it is corrected.</em>',
    t4n3='Un fallo con fecha y con arreglo deja de ser una discusión.',

    t5Eyebrow='Quién decide',
    t5Title='Proponer sin quedarte con la decisión',
    t5b1='Una propuesta. Deja la decisión en manos de quien paga.',
    t5n1='La entrada más segura cuando el cliente tiene que aprobarlo.',
    t5b2='Una decisión ya tomada. Informas, no preguntas.',
    t5n2='Correcto con tu propio equipo. Arriesgado con un cliente.',
    t5b3='<em>shift</em> &middot; <em>scale back</em> &middot; <em>pause</em> &middot; <em>hold off on</em> &middot; <em>double down on</em>',
    t5n3='<em>Shift budget out of X and into Y</em> es el patrón fijo.',
    t5b4='<em>I&rsquo;d give it another fortnight before we judge it.</em>',
    t5n4='Una fecha convierte &laquo;esperar&raquo; en un plan.',

    t6Eyebrow='La pregunta que no llevabas preparada',
    t6Title='Dos segundos, bien comprados',
    t6b1='Da una cifra y la marca como aproximada, en cuatro palabras.',
    t6n1='Después <em>but let me confirm that</em>. Termínalo siempre.',
    t6b2='No adivina y promete la respuesta. Añade <em>by this afternoon</em>.',
    t6n2='Una promesa sin plazo no es una promesa.',
    t6b3='Compra los dos segundos y suena sincero, no evasivo.',
    t6n3='Sigue con <em>the honest answer is</em> &mdash; y entonces responde.',
    t6b4='Convierte una suposición en una respuesta comprobada, sin ceder nada.',
    t6n4='Mejor que el silencio. El silencio se lee como no saber.',

    sortEyebrow='Antes de decir por qué',
    sortTitle='¿Cuánto afirma saber la frase?',
    sortHint='Haz clic en una línea y luego en su casilla. Todas hablan de un movimiento real en las cifras &mdash; lo que cambia es cuánto afirman sobre el motivo.',
    sortBin1='Afirma una causa',
    sortBin2='Afirma solo coincidencia',
    sortBin3='Todavía no afirma nada',

    bankLabel='Banco de palabras:',
    gapEyebrow='La gramática del informe',
    gapTitleA='Completa el movimiento',
    gapHintA='Una palabra por hueco. Tres de las seis no hacen falta.',
    gapTitleB='Completa la propuesta',
    gapHintB='Un verbo por hueco. Tres de los seis no hacen falta &mdash; y los tres son expresiones reales de esta lección.',

    matEyebrow='Precisión',
    matTitle='Empareja cada métrica con lo que de verdad cuenta',
    matHint='Seis términos, seis definiciones. Cuatro se usan habitualmente como si fueran intercambiables; ninguno lo es.',

    ordEyebrow='Construye la frase',
    ordTitleA='Primero el titular',
    ordHintA='Haz clic en las partes en orden. El cliente oye la conclusión antes que el detalle.',
    ordTitleB='Una propuesta a la que se puede decir que no',
    ordHintB='Haz clic en las partes en orden: la base, la propuesta, el tamaño y la fecha.',

    qEyebrow='En la llamada',
    qTitle='¿Cuál dirías de verdad?',
    q1Stem='¿Qué frase expresa correctamente el tamaño del movimiento?',
    q2Ctx='El click-through rate era del 2,4% en junio. Ahora es del 3,1%.',
    q2Stem='¿Qué frase lo expresa con exactitud?',
    q3Ctx='La campaña se mostró 840.000 veces, a 210.000 personas distintas.',
    q3Stem='¿Qué frase lo informa correctamente?',
    q4Ctx='Las conversiones subieron un 20% la semana en que la web de un competidor estuvo caída. No tienes ninguna otra prueba.',
    q4Stem='¿Qué frase puedes defender si el cliente pregunta cómo lo sabes?',
    q5Ctx='El cliente pregunta si el nuevo creativo funciona. Lleva cuatro días activo.',
    q5Stem='¿Qué respuesta es honesta y además útil?',
    q6Ctx='Tu equipo usó el público equivocado durante una semana. El cliente lo verá en las cifras.',
    q6Stem='¿Qué frase dirías primero?',
    q7Ctx='Quieres mover presupuesto entre canales. El cliente tiene que aprobarlo.',
    q7Stem='¿Qué frase deja la decisión en sus manos?',
    q8Ctx='En mitad de la llamada, el cliente te pide una cifra que no tienes delante.',
    q8Stem='¿Qué respuesta mantiene tu credibilidad?',

    actTitle='Ahora dirige la revisión',
    actUse='Usa al menos cuatro:',
    actSpeakKind='Debate &middot; por parejas',
    actSpeakBrief='Doce minutos y cambio. Uno dirige la revisión mensual; el otro es el cliente que no ha leído el informe y va interrumpiendo.',
    actSpeak1='Abre la revisión con el titular en dos frases: qué se movió, en qué dirección y cuánto. Sin diapositivas.',
    actSpeak2='Cliente: &laquo;¿Y por qué bajaron las conversiones?&raquo; Tienes la coincidencia temporal y ninguna causa. Responde sin inventarte una.',
    actSpeak3='Cliente: &laquo;¿Cuál fue el CPA de la semana pasada?&raquo; No lo tienes. Responde, compromete algo y sigue con la llamada.',
    actSpeak4='Propón mover una quinta parte del presupuesto. Deja la decisión en sus manos y pon fecha a la revisión.',
    actWriteKind='Escritura &middot; 160&ndash;200 palabras',
    actWriteBrief='Escribe el correo de seguimiento posterior a la llamada. El titular primero; dos cifras con el movimiento bien formulado; algo que salió mal y de quién dependía; una propuesta con fecha de revisión. Nada que el cliente tenga que buscar hacia abajo.',
    actPlaceholder='Thanks for your time this morning. The headline is…',

    resNext='Reconocer la frase correcta es la mitad fácil. Ahora dirige la llamada &rarr;',
    resPerfect='Puntuación perfecta. Oyes la diferencia &mdash; decirlo en directo, con un cliente interrumpiendo, es la otra mitad.',
    resStrong='Muy bien. Vuelve a mirar los fallos: casi todos dependen de una preposición o de un verbo.',
    resMid='Una base aprovechable. Relee los cuatro patrones de movimiento y la diapositiva de la causa antes de hablar.',
    resLow='Vuelve a las seis diapositivas de explicación. Casi todo fallo aquí es una palabra usada como si fuera sinónimo de otra.',
)

# ── CROATIAN ───────────────────────────────────────────────────────────
# Added on Innes's instruction the same day the deck was built: the student
# this lesson was written for is Croatian, so this is the language he will
# actually switch into. It is the eleventh language the site knows about and
# the first added since the original ten came over from
# forbes-c1-negotiation.html — see chrome_i18n.CHROME['hr'] for the chrome
# half, LANGS in lesson-template.html for the switcher label, and deck.assemble's
# all_langs for the empty placeholder every other deck now emits.
#
# chipCount says "NSLIDES slajda", not "slajdova", and that is deliberate
# rather than a slip: Croatian takes the paucal after a number ending 2-4
# (23 slajda) and the genitive plural otherwise (25 slajdova). The chip is a
# static string with the count patched in at build time, so it is correct for
# this deck's 23 and would need changing if the deck ever grew past 24 or
# shrank below 22. The one place the rule is handled properly is
# CHROME['hr']['wordCount'], which is a function because the word counter
# genuinely varies at runtime.
T['hr'] = dict(
    coverTitle='Mjesečni <em>pregled</em>',
    coverSub='Izvještavanje o kampanji na engleskom &mdash; brojke, razlog, prijedlog i pitanje za koje se nisi pripremio',
    chipLevel='B2 &middot; Agencija i izvještavanje klijentu',
    chipFocus='Jezik rezultata i govor bez pripreme',
    chipCount='NSLIDES slajda',

    t1Eyebrow='Prva rečenica svakog izvještaja',
    t1Title='Četiri obrasca za brojku koja se pomaknula',
    t1b1='<em>Veličina</em> promjene: <em>CPA fell by 14%</em>.',
    t1n1='Nikad <em>fell with 14%</em>, nikad <em>fell on 14%</em>.',
    t1b2='<em>Razina</em> na kojoj je završila: <em>CTR rose to 3.1%</em>.',
    t1n2='Jedno kaže koliko se pomaknulo, drugo gdje je stalo.',
    t1b3='Oba kraja: <em>from &euro;38 to &euro;32 in three weeks</em>.',
    t1n3='Koristi kad je početna točka ono što je bitno.',
    t1b4='Usporedba: <em>spend is up 11% on last month</em>.',
    t1n4='Također <em>month on month</em>, <em>year on year</em>, <em>versus Q2</em>.',

    t2Eyebrow='Tvrdnja koju možeš obraniti',
    t2Title='Uzrok, poklapanje ili se još ne zna',
    t2b1='Tvrdiš da postoji mehanizam. Reci to kad ga možeš pokazati.',
    t2n1='Klijent ima pravo pitati <em>how do you know?</em>',
    t2b2='Tvrdiš samo vremensko poklapanje i ništa više od toga.',
    t2n2='Pošteno, i izdrži kad netko ponudi drugo objašnjenje.',
    t2b3='Tvoje čitanje, označeno kao tvoje. Procjena, ponuđena kao procjena.',
    t2n3='Ono <em>we</em> ovdje radi pravi posao. Nemoj ga izbaciti.',
    t2b4='Potpun odgovor &mdash; ako dodaš kada ćeš <em>znati</em>.',
    t2n4='Bez datuma zvuči kao izbjegavanje pitanja.',

    t3Eyebrow='Četiri para koja se na engleskom stapaju',
    t3Title='Metrike, izrečene precizno',
    t3b1='Reach broji <em>ljude</em>. Impressions broje <em>prikaze</em>.',
    t3n1='Impressions su uvijek veći od tih dvaju brojeva.',
    t3b2='Klikovi po prikazu; zatim radnje po posjetu. Dvije faze.',
    t3n2='Visok CTR i nizak CVR je razgovor o landing stranici.',
    t3b3='Cijena klika, cijena kupca, prihod po potrošenom euru.',
    t3n3='Samo je zadnje omjer: <em>a 4x ROAS</em>, ne <em>4%</em>.',
    t3b4='Budget se dodjeljuje, spend je potrošen. <em>Pacing</em> je razlika.',
    t3n4='<em>We are pacing ahead</em> znači da će ponestati prerano.',

    t4Eyebrow='Loša vijest prva, u jednoj rečenici',
    t4Title='Reći da cilj nije postignut, bez dojma nemara',
    t4b1='<em>We came in under target on conversions</em> &mdash; brojka, bez uvijanja.',
    t4n1='Pazi: under <em>budget</em> je dobra vijest, under <em>target</em> nije.',
    t4b2='<em>That one&rsquo;s on us.</em> &middot; <em>That sat with the platform.</em>',
    t4n2='Oboje je u redu. Nemati odgovor nije.',
    t4b3='<em>We caught it on day seven and it is corrected.</em>',
    t4n3='Propust s datumom i rješenjem prestaje biti rasprava.',

    t5Eyebrow='Tko odlučuje',
    t5Title='Predložiti, a ne odlučiti umjesto njih',
    t5b1='Prijedlog. Odluka ostaje kod onoga tko plaća.',
    t5n1='Najsigurniji početak kad klijent mora odobriti.',
    t5b2='Odluka koja je već donesena. Ti javljaš, ne pitaš.',
    t5n2='Ispravno unutar svog tima. S klijentom rizično.',
    t5b3='<em>shift</em> &middot; <em>scale back</em> &middot; <em>pause</em> &middot; <em>hold off on</em> &middot; <em>double down on</em>',
    t5n3='<em>Shift budget out of X and into Y</em> je ustaljeni obrazac.',
    t5b4='<em>I&rsquo;d give it another fortnight before we judge it.</em>',
    t5n4='Datum pretvara &bdquo;čekamo&ldquo; u plan.',

    t6Eyebrow='Pitanje za koje se nisi pripremio',
    t6Title='Dvije sekunde, kupljene kako treba',
    t6b1='Daje brojku i označava je kao približnu, u četiri riječi.',
    t6n1='Zatim <em>but let me confirm that</em>. Uvijek to dovrši.',
    t6b2='Ne nagađa i obećava odgovor. Dodaj <em>by this afternoon</em>.',
    t6n2='Obećanje bez roka nije obećanje.',
    t6b3='Kupuje te dvije sekunde i zvuči otvoreno, a ne izbjegavajuće.',
    t6n3='Nastavi s <em>the honest answer is</em> &mdash; pa onda odgovori.',
    t6b4='Pretvara nagađanje u provjeren odgovor, bez ikakvog ustupka.',
    t6n4='Bolje od šutnje. Šutnja se čita kao neznanje.',

    sortEyebrow='Prije nego kažeš zašto',
    sortTitle='Koliko rečenica tvrdi da zna?',
    sortHint='Klikni redak, pa kućicu u koju ide. Svaki redak govori o stvarnoj promjeni u brojkama &mdash; razlikuju se po tome koliko tvrde o razlogu.',
    sortBin1='Tvrdi uzrok',
    sortBin2='Tvrdi samo poklapanje',
    sortBin3='Još ništa ne tvrdi',

    bankLabel='Banka riječi:',
    gapEyebrow='Gramatika izvještaja',
    gapTitleA='Dopuni promjenu',
    gapHintA='Jedna riječ po praznini. Tri od šest nisu potrebne.',
    gapTitleB='Dopuni prijedlog',
    gapHintB='Jedan glagol po praznini. Tri od šest nisu potrebna &mdash; i sva tri su stvarni izrazi iz ove lekcije.',

    matEyebrow='Preciznost',
    matTitle='Spoji metriku s onim što stvarno broji',
    matHint='Šest pojmova, šest definicija. Četiri se redovito koriste kao da su zamjenjivi; nijedan nije.',

    ordEyebrow='Složi rečenicu',
    ordTitleA='Prvo glavna poruka',
    ordHintA='Klikni dijelove redom. Klijent čuje zaključak prije detalja.',
    ordTitleB='Prijedlog na koji se može reći ne',
    ordHintB='Klikni dijelove redom: podloga, prijedlog, opseg, pa datum.',

    qEyebrow='Na pozivu',
    qTitle='Što bi stvarno rekao?',
    q1Stem='Koja rečenica točno iznosi veličinu promjene?',
    q2Ctx='Click-through rate bio je 2,4% u lipnju. Sada je 3,1%.',
    q2Stem='Koja to iznosi točno?',
    q3Ctx='Kampanja je prikazana 840.000 puta, na 210.000 različitih ljudi.',
    q3Stem='Koja rečenica to točno izvještava?',
    q4Ctx='Konverzije su porasle 20% u tjednu u kojem stranica konkurenta nije radila. Drugih dokaza nemaš.',
    q4Stem='Koju rečenicu možeš obraniti ako klijent pita odakle to znaš?',
    q5Ctx='Klijent pita radi li novi creative. Aktivan je četiri dana.',
    q5Stem='Koji je odgovor i pošten i koristan?',
    q6Ctx='Tvoj tim je tjedan dana koristio pogrešnu publiku. Klijent će to vidjeti u brojkama.',
    q6Stem='Koju bi rečenicu rekao prvu?',
    q7Ctx='Želiš prebaciti budžet između kanala. Klijent to mora odobriti.',
    q7Stem='Koja rečenica ostavlja odluku njemu?',
    q8Ctx='Usred poziva klijent traži brojku koju nemaš pred sobom.',
    q8Stem='Koji odgovor čuva tvoj kredibilitet?',

    actTitle='Sada vodi pregled',
    actUse='Upotrijebi barem četiri:',
    actSpeakKind='Rasprava &middot; u paru',
    actSpeakBrief='Dvanaest minuta, pa zamjena. Jedan vodi mjesečni pregled; drugi je klijent koji nije pročitao materijale i upada u riječ.',
    actSpeak1='Otvori pregled glavnom porukom u dvije rečenice: što se pomaknulo, u kojem smjeru, koliko. Bez slajdova.',
    actSpeak2='Klijent: &bdquo;Zašto su pale konverzije?&ldquo; Imaš vremensko poklapanje, ali ne i uzrok. Odgovori bez izmišljanja.',
    actSpeak3='Klijent: &bdquo;Koliki je bio CPA prošli tjedan?&ldquo; Nemaš ga. Odgovori, obećaj i vodi poziv dalje.',
    actSpeak4='Predloži da se petina budžeta prebaci. Ostavi odluku klijentu i stavi datum na provjeru.',
    actWriteKind='Pisanje &middot; 160&ndash;200 riječi',
    actWriteBrief='Napiši mail koji ide nakon poziva. Prvo glavna poruka; dvije brojke s ispravno izrečenom promjenom; jedna stvar koja je pošla po zlu i gdje je bila; jedan prijedlog s datumom provjere. Ništa što klijent mora tražiti skrolanjem.',
    actPlaceholder='Thanks for your time this morning. The headline is…',

    resNext='Prepoznati pravu rečenicu je lakša polovica. Sada vodi poziv &rarr;',
    resPerfect='Sve točno. Čuješ razliku &mdash; reći to uživo, dok te klijent prekida, druga je polovica.',
    resStrong='Odlično. Pogledaj još jednom promašaje: gotovo svi vise o jednom prijedlogu ili jednom glagolu.',
    resMid='Upotrebljiva osnova. Ponovi četiri obrasca promjene i slajd o uzroku prije nego progovoriš.',
    resLow='Vrati se na šest slajdova s objašnjenjima. Gotovo svaka pogreška ovdje je riječ upotrijebljena kao da je sinonim druge.',
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
