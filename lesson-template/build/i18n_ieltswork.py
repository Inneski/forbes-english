# -*- coding: utf-8 -*-
"""Interface strings for IELTS Vocabulary: Work, Automation and Cities.

English, German and Spanish, teach cards in the six-item form.

The usual split (HOUSE-STYLE §8), and on a topic-bank deck it is the whole
lesson: the pairings are the thing being learnt. <em>Take on staff</em>,
<em>productivity gains</em>, <em>ease congestion</em> stay English inside the
German and Spanish cards, the explanations and the sort, because a German
rendering of an English collocation teaches nothing — the point is which
English word the English noun takes. What translates is the argument each
idea is attached to, and the reason the pairing is the unit.

`sortWhy` is a key rather than a sentence so the sort's explanation
translates too; the engine's `explainOf` resolves it.
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
    coverTitle='Work, Automation <em>and Cities</em>',
    coverSub='Three topics that come up again and again in Part 3 and Task 2, '
             'and the pairings that make an answer on any of them sound '
             'thought through',
    chipLevel='C1 · Advanced', chipFocus='Speaking &amp; Writing Task 2',
    chipCount='18 points',

    t1Eyebrow='Idea one',
    t1Title='Work: flexibility against security',
    t1ah='The pairings',
    t1ab='<em>Job security</em>, <em>career prospects</em>, <em>a work&ndash;life '
         'balance</em>: nouns that arrive with their partner fixed. You '
         '<em>work remotely</em> on <em>a flexible schedule</em>, you '
         '<em>suffer burnout</em>, a firm <em>takes on staff</em>. None of '
         'the words is rare. The pairings are what English says.',
    t1an='Learn <em>suffer burnout</em>. Not <em>burnout</em>.',
    t1bh='Flexibility against isolation',
    t1bb='The Part 3 question is nearly always a form of <em>is working from '
         'home good for people?</em> The answer that scores holds two '
         'pairings against each other: <em>a flexible schedule</em> on one '
         'side, the colleagues you no longer see on the other.',
    t1bn='One idea, two phrases, and <em>but</em> between them.',
    t1ch='Security against opportunity',
    t1cb='<em>The gig economy</em> is behind many of the Task 2 questions '
         'on work. Argue it as a trade: it offers <em>a flexible '
         'schedule</em> and takes away <em>job security</em>; it widens '
         '<em>career prospects</em> for some and narrows them for others.',
    t1cn='Say what it gives and what it takes. That is the paragraph.',

    t2Eyebrow='Idea two',
    t2Title='Automation: jobs lost against jobs created',
    t2ah='The pairings',
    t2ab='<em>Automate routine tasks</em>, <em>replace workers</em>, '
         '<em>retrain the workforce</em>; <em>productivity gains</em>, '
         '<em>low-skilled jobs</em>, <em>artificial intelligence</em>. The '
         'noun brings its verb: tasks are <em>automated</em>, workers are '
         '<em>displaced</em>, a workforce is <em>retrained</em>.',
    t2an='The verb is <em>automate</em>, not <em>automatise</em>.',
    t2bh='Lost against created',
    t2bb='Every automation prompt is the same trade: machines <em>displace</em> '
         'workers in <em>low-skilled jobs</em>, and the <em>productivity '
         'gains</em> pay for jobs that did not exist before. An answer with '
         'only the first half is a band 6. The one that weighs both is what '
         'Part 3 is asking for.',
    t2bn='Name who loses, name who gains, and say which matters more.',
    t2ch='Who retrains whom',
    t2cb='The second argument is about responsibility. Should the state '
         '<em>retrain the workforce</em>, or the employer that <em>replaced</em> '
         'it? <em>A universal basic income</em> is the phrase for the answer '
         'that says neither.',
    t2cn='One pairing per position, and three positions to choose from.',

    t3Eyebrow='Idea three',
    t3Title='Cities: density against space, the car against the bus',
    t3ah='The pairings',
    t3ab='<em>Urban sprawl</em>, <em>affordable housing</em>, <em>public '
         'transport</em>, <em>green spaces</em>, <em>the cost of living</em>. '
         'A council <em>invests in infrastructure</em> and tries to <em>ease '
         'congestion</em>; a resident has <em>a long commute</em> and puts '
         'up with <em>overcrowding</em>.',
    t3an='Congestion is <em>eased</em>. Traffic is <em>heavy</em>, never '
         '<em>strong</em>.',
    t3bh='Density against space',
    t3bb='The Task 2 prompt is usually a version of <em>should cities build '
         'up or out?</em> Up means <em>affordable housing</em> near the '
         'centre and less <em>urban sprawl</em>, at the price of '
         '<em>overcrowding</em>. Out means <em>green spaces</em> and <em>a '
         'long commute</em>.',
    t3bn='Both answers cost something. Say what.',
    t3ch='The car against the bus',
    t3cb='Part 3 asks how to <em>ease congestion</em>. The answer that has '
         'thought about it before says a city cannot build its way out, '
         'because every new road fills; so the money goes to <em>public '
         'transport</em> instead. <em>Invest in infrastructure</em> is the '
         'pairing that carries the point.',
    t3cn='<em>The cost of living</em> closes either answer: whoever pays, it '
         'is the resident.',

    mcaEyebrow='Activity 1 · Work',
    mcaTitle='Which pairing, and which word?',
    mcbEyebrow='Activity 2 · Automation',
    mcbTitle='The noun brings its verb',
    mccEyebrow='Activity 3 · Cities',
    mccTitle='The plain pairing is the precise one',

    v1why='<em>Work remotely</em>. The adverb is fixed by the verb: '
          '<em>distantly</em> is a manner of speaking, and <em>at distance</em> '
          'and <em>from distance</em> are built one word at a time from a '
          'dictionary.',
    v2why='<em>Job security</em>. <em>Work safety</em> is real English and '
          'means something else &mdash; helmets and fire exits &mdash; which '
          'is the precision miss. The other two are not pairings English has.',
    v3why='<em>Suffer burnout</em>, like <em>suffer losses</em> or <em>suffer '
          'a setback</em>: the noun for damage takes the verb for damage. '
          '<em>Make</em>, <em>get into</em> and <em>fall in</em> are what a '
          'learner reaches for when the phrase was learnt as one word.',
    v4why='<em>Improve career prospects</em>. <em>Trajectories</em>, '
          '<em>futures</em> and <em>chances</em> each reach past the noun '
          'English uses, and <em>augment</em> and <em>amplify</em> are the '
          'near-miss verbs that go with them. The plain pairing is the '
          'precise one.',
    v5why='<em>Displace</em> is the verb for a person or a job pushed out by '
          'something new. <em>Dislocate</em> is a shoulder, <em>misplace</em> '
          'is a set of keys, <em>evict</em> is a tenant &mdash; three real '
          'words, each precise about something else.',
    v6why='<em>Productivity gains</em>. Productivity has a gain, not a profit, '
          'a growth or a winning; a noun chooses its partner noun as firmly '
          'as it chooses a verb.',
    v7why='<em>Retrain the workforce</em>. The other three are the verb a '
          'learner builds from <em>re-</em> plus a word for teaching. English '
          'already has the verb, and it takes <em>the workforce</em> as its '
          'object.',
    v8why='<em>A universal basic income</em> is the name of the policy, and an '
          'examiner hears the name or hears a guess. A wage and a salary are '
          'paid for work, which is the one thing this is not.',
    v9why='<em>Urban sprawl</em>, and only that. <em>Sprawl</em> carries the '
          'judgement &mdash; growth that is unplanned and ugly &mdash; which '
          'is why it is the word the argument needs and <em>spread</em> is '
          'not.',
    v10why='<em>Affordable housing</em> is the term a planner, a politician and '
           'an examiner all use. <em>Economical</em> is a car, '
           '<em>reasonable</em> is a person, and <em>cheap-priced</em> is not '
           'English.',
    v11why='<em>Invest in</em>. The preposition is part of the pairing and '
           'travels with the verb whatever follows: <em>invest in '
           'infrastructure</em>, <em>invest in public transport</em>, '
           '<em>invest in people</em>.',
    v12why='<em>A long commute</em>. The other three reach for a rarer '
           'adjective and a rarer noun and miss on both. The plain pairing is '
           'the one every English speaker uses, which is exactly why it '
           'scores.',

    sortEyebrow='Activity 4 · The pairing, whole',
    sortTitle='Sort the six pairings',
    sortHint='Drag each one into a column &mdash; or click an item, then the '
             'column you want it in.',
    sortBin1='English says this',
    sortBin2='English does not',
    sortWhy='The noun chooses the verb and the adjective. Congestion is '
            '<em>eased</em>, staff are <em>taken on</em>, and <em>the gig '
            'economy</em> is a fixed name. Congestion is <em>heavy</em> or '
            '<em>severe</em>, traffic is <em>heavy</em>, and housing is '
            '<em>affordable</em> &mdash; the three on the right are what a '
            'learner builds from a dictionary, one word at a time. Learn the '
            'phrase whole and the choice is never yours to get wrong.',

    actTitle='Answer from the bank',
    actUse='Use at least three:',
    actSpeakBrief='In pairs. One of you is the examiner and asks Part 3 '
                  'questions on work and cities &mdash; <em>is working from '
                  'home good for a company? Should cities build up or out? '
                  'Who should pay to retrain people?</em> The other answers '
                  'each one for a minute using only the bank on this deck. '
                  'Then swap.',
    actSpeak1='Every answer holds two pairings against each other &mdash; one '
              'for each side, with <em>but</em> or <em>whereas</em> between '
              'them.',
    actSpeak2='The examiner stops you the moment you use a bare word where '
              'the bank has a pairing, and you say it again with the phrase.',
    actSpeak3='Every third question is a follow-up &mdash; <em>why?</em> or '
              '<em>can you give an example?</em> &mdash; and the answer has '
              'to add a pairing you have not used yet.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Choose one of the three ideas and write a Task 2 body '
                  'paragraph on it: the claim, the argument, an example, the '
                  'concession. Use at least five pairings from the bank and '
                  'underline each one. Then read it back and count: a '
                  'sentence with no pairing in it is doing nothing for '
                  'your Lexical Resource.',
    actPlaceholder='Automation displaces workers in low-skilled jobs, but…',
)

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Arbeit, Automatisierung <em>und Städte</em>',
    coverSub='Drei Themen, die in Teil 3 und in Task 2 immer wieder kommen '
             '&mdash; und die Paarungen, mit denen eine Antwort zu jedem '
             'davon durchdacht klingt',
    chipLevel='C1 · Fortgeschritten', chipFocus='Speaking &amp; Writing Task 2',
    chipCount='18 Punkte',

    t1Eyebrow='Idee eins',
    t1Title='Arbeit: Flexibilität gegen Sicherheit',
    t1ah='Die Paarungen',
    t1ab='<em>Job security</em>, <em>career prospects</em>, <em>a work&ndash;life '
         'balance</em>: Substantive, die mit festem Partner ankommen. Man '
         '<em>works remotely</em> nach <em>a flexible schedule</em>, man '
         '<em>suffers burnout</em>, eine Firma <em>takes on staff</em>. '
         'Keines der Wörter ist selten. Die Paarungen sind das, was das '
         'Englische sagt.',
    t1an='Lern <em>suffer burnout</em>. Nicht <em>burnout</em>.',
    t1bh='Flexibilität gegen Isolation',
    t1bb='Die Frage in Teil 3 ist fast immer eine Form von <em>is working '
         'from home good for people?</em> Die Antwort, die zählt, stellt '
         'zwei Paarungen gegeneinander: <em>a flexible schedule</em> auf der '
         'einen Seite, die Kollegen, die man nicht mehr sieht, auf der '
         'anderen.',
    t1bn='Eine Idee, zwei Phrasen, und <em>but</em> dazwischen.',
    t1ch='Sicherheit gegen Chance',
    t1cb='<em>The gig economy</em> steckt hinter vielen Task-2-Fragen zur '
         'Arbeit. Argumentiere sie als Tausch: Sie bietet <em>a flexible '
         'schedule</em> und nimmt <em>job security</em>; sie erweitert '
         '<em>career prospects</em> für die einen und verengt sie für die '
         'anderen.',
    t1cn='Sag, was sie gibt und was sie nimmt. Das ist der Absatz.',

    t2Eyebrow='Idee zwei',
    t2Title='Automatisierung: verlorene gegen neue Jobs',
    t2ah='Die Paarungen',
    t2ab='<em>Automate routine tasks</em>, <em>replace workers</em>, '
         '<em>retrain the workforce</em>; <em>productivity gains</em>, '
         '<em>low-skilled jobs</em>, <em>artificial intelligence</em>. Das '
         'Substantiv bringt sein Verb mit: Aufgaben werden <em>automated</em>, '
         'Arbeiter werden <em>displaced</em>, eine Belegschaft wird '
         '<em>retrained</em>.',
    t2an='Das Verb heißt <em>automate</em>, nicht <em>automatise</em>.',
    t2bh='Verloren gegen geschaffen',
    t2bb='Jede Aufgabe zur Automatisierung ist derselbe Tausch: Maschinen '
         '<em>displace</em> Arbeiter in <em>low-skilled jobs</em>, und die '
         '<em>productivity gains</em> bezahlen Jobs, die es vorher nicht gab. '
         'Eine Antwort mit nur der ersten Hälfte ist Band 6. Die, die beides '
         'abwägt, ist das, wonach Teil 3 fragt.',
    t2bn='Nenn, wer verliert, nenn, wer gewinnt, und sag, was schwerer wiegt.',
    t2ch='Wer schult wen um',
    t2cb='Das zweite Argument handelt von Verantwortung. Soll der Staat '
         '<em>retrain the workforce</em>, oder der Arbeitgeber, der sie '
         '<em>replaced</em> hat? <em>A universal basic income</em> ist die '
         'Phrase für die Antwort, die sagt: keiner von beiden.',
    t2cn='Eine Paarung pro Position, und drei Positionen zur Auswahl.',

    t3Eyebrow='Idee drei',
    t3Title='Städte: Dichte gegen Raum, das Auto gegen den Bus',
    t3ah='Die Paarungen',
    t3ab='<em>Urban sprawl</em>, <em>affordable housing</em>, <em>public '
         'transport</em>, <em>green spaces</em>, <em>the cost of living</em>. '
         'Eine Stadtverwaltung <em>invests in infrastructure</em> und '
         'versucht, <em>ease congestion</em>; ein Bewohner hat <em>a long '
         'commute</em> und erträgt <em>overcrowding</em>.',
    t3an='Congestion wird <em>eased</em>. Traffic ist <em>heavy</em>, nie '
         '<em>strong</em>.',
    t3bh='Dichte gegen Raum',
    t3bb='Die Task-2-Aufgabe ist meist eine Version von <em>should cities '
         'build up or out?</em> Nach oben heißt <em>affordable housing</em> '
         'nahe am Zentrum und weniger <em>urban sprawl</em>, um den Preis von '
         '<em>overcrowding</em>. Nach außen heißt <em>green spaces</em> und '
         '<em>a long commute</em>.',
    t3bn='Beide Antworten kosten etwas. Sag, was.',
    t3ch='Das Auto gegen den Bus',
    t3cb='Teil 3 fragt, wie man <em>ease congestion</em> kann. Die Antwort, '
         'die schon einmal darüber nachgedacht hat, sagt: Eine Stadt kann '
         'sich nicht herausbauen, denn jede neue Straße füllt sich; also geht '
         'das Geld in <em>public transport</em>. <em>Invest in '
         'infrastructure</em> ist die Paarung, die den Punkt trägt.',
    t3cn='<em>The cost of living</em> schließt beide Antworten ab: Wer auch '
         'zahlt, es ist der Bewohner.',

    mcaEyebrow='Aktivität 1 · Arbeit',
    mcaTitle='Welche Paarung, und welches Wort?',
    mcbEyebrow='Aktivität 2 · Automatisierung',
    mcbTitle='Das Substantiv bringt sein Verb mit',
    mccEyebrow='Aktivität 3 · Städte',
    mccTitle='Die schlichte Paarung ist die genaue',

    v1why='<em>Work remotely</em>. Das Adverb ist durch das Verb festgelegt: '
          '<em>distantly</em> ist eine Art zu sprechen, und <em>at '
          'distance</em> und <em>from distance</em> sind Wort für Wort aus '
          'dem Wörterbuch gebaut.',
    v2why='<em>Job security</em>. <em>Work safety</em> ist echtes Englisch und '
          'heißt etwas anderes &mdash; Helme und Notausgänge &mdash;, das ist '
          'der Präzisionsfehler. Die anderen beiden sind keine Paarungen, die '
          'das Englische hat.',
    v3why='<em>Suffer burnout</em>, wie <em>suffer losses</em> oder <em>suffer '
          'a setback</em>: Das Substantiv für Schaden nimmt das Verb für '
          'Schaden. <em>Make</em>, <em>get into</em> und <em>fall in</em> sind '
          'das, wonach man greift, wenn die Phrase als ein Wort gelernt '
          'wurde.',
    v4why='<em>Improve career prospects</em>. <em>Trajectories</em>, '
          '<em>futures</em> und <em>chances</em> greifen alle über das '
          'Substantiv hinaus, das das Englische verwendet, und '
          '<em>augment</em> und <em>amplify</em> sind die Fastreffer-Verben '
          'dazu. Die schlichte Paarung ist die genaue.',
    v5why='<em>Displace</em> ist das Verb für einen Menschen oder einen Job, '
          'den etwas Neues verdrängt. <em>Dislocate</em> ist eine Schulter, '
          '<em>misplace</em> ein Schlüsselbund, <em>evict</em> ein Mieter '
          '&mdash; drei echte Wörter, jedes genau für etwas anderes.',
    v6why='<em>Productivity gains</em>. Produktivität hat einen gain, keinen '
          'profit, growth oder winning; ein Substantiv wählt sein '
          'Partnersubstantiv so fest wie sein Verb.',
    v7why='<em>Retrain the workforce</em>. Die anderen drei sind das Verb, das '
          'man sich aus <em>re-</em> plus einem Wort fürs Lehren baut. Das '
          'Englische hat das Verb schon, und es nimmt <em>the workforce</em> '
          'als Objekt.',
    v8why='<em>A universal basic income</em> ist der Name der Maßnahme, und '
          'ein Prüfer hört den Namen oder hört eine Vermutung. Wage und '
          'salary werden für Arbeit gezahlt, und genau das ist dies nicht.',
    v9why='<em>Urban sprawl</em>, und nur das. <em>Sprawl</em> trägt das Urteil '
          '&mdash; ungeplantes, hässliches Wachstum &mdash;, deshalb ist es '
          'das Wort, das das Argument braucht, und <em>spread</em> nicht.',
    v10why='<em>Affordable housing</em> ist der Begriff, den Planer, Politiker '
           'und Prüfer alle verwenden. <em>Economical</em> ist ein Auto, '
           '<em>reasonable</em> ein Mensch, und <em>cheap-priced</em> ist kein '
           'Englisch.',
    v11why='<em>Invest in</em>. Die Präposition gehört zur Paarung und reist '
           'mit dem Verb, was auch folgt: <em>invest in infrastructure</em>, '
           '<em>invest in public transport</em>, <em>invest in people</em>.',
    v12why='<em>A long commute</em>. Die anderen drei greifen nach einem '
           'selteneren Adjektiv und einem selteneren Substantiv und liegen '
           'bei beiden daneben. Die schlichte Paarung ist die, die jeder '
           'Englischsprecher benutzt, und genau deshalb zählt sie.',

    sortEyebrow='Aktivität 4 · Die Paarung als Ganzes',
    sortTitle='Sortiere die sechs Paarungen',
    sortHint='Zieh jede in eine Spalte &mdash; oder klicke ein Element an und '
             'dann die Spalte, in die es soll.',
    sortBin1='Das sagt das Englische',
    sortBin2='Das sagt es nicht',
    sortWhy='Das Substantiv wählt Verb und Adjektiv. Congestion wird '
            '<em>eased</em>, staff werden <em>taken on</em>, und <em>the gig '
            'economy</em> ist ein fester Name. Congestion ist <em>heavy</em> '
            'oder <em>severe</em>, traffic ist <em>heavy</em>, und housing '
            'ist <em>affordable</em> &mdash; die drei rechts sind das, was man '
            'sich aus dem Wörterbuch baut, Wort für Wort. Lern die Phrase als '
            'Ganzes, dann gibt es keine Wahl, die du falsch treffen kannst.',

    actTitle='Antworte aus der Sammlung',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu zweit. Einer ist der Prüfer und stellt Fragen aus Teil '
                  '3 zu Arbeit und Städten &mdash; <em>is working from home '
                  'good for a company? Should cities build up or out? Who '
                  'should pay to retrain people?</em> Der andere beantwortet '
                  'jede eine Minute lang, nur mit der Sammlung auf diesem '
                  'Deck. Dann tauschen.',
    actSpeak1='Jede Antwort stellt zwei Paarungen gegeneinander &mdash; eine '
              'pro Seite, mit <em>but</em> oder <em>whereas</em> dazwischen.',
    actSpeak2='Der Prüfer stoppt dich, sobald du ein nacktes Wort benutzt, wo '
              'die Sammlung eine Paarung hat, und du sagst es noch einmal mit '
              'der Phrase.',
    actSpeak3='Jede dritte Frage ist eine Nachfrage &mdash; <em>why?</em> oder '
              '<em>can you give an example?</em> &mdash;, und die Antwort '
              'muss eine Paarung ergänzen, die du noch nicht benutzt hast.',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Wähl eine der drei Ideen und schreib dazu einen '
                  'Hauptteil-Absatz für Task 2: Behauptung, Argument, '
                  'Beispiel, Einschränkung. Verwende mindestens fünf '
                  'Paarungen aus der Sammlung und unterstreich jede. Dann lies '
                  'es noch einmal und zähl: Ein Satz ohne Paarung tut nichts '
                  'für deine Lexical Resource.',
    actPlaceholder='Automation displaces workers in low-skilled jobs, but…',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Trabajo, automatización <em>y ciudades</em>',
    coverSub='Tres temas que salen una y otra vez en la Parte 3 y en Task 2, '
             'y las parejas que hacen que una respuesta sobre cualquiera de '
             'ellos suene pensada',
    chipLevel='C1 · Avanzado', chipFocus='Speaking y Writing Task 2',
    chipCount='18 puntos',

    t1Eyebrow='Idea uno',
    t1Title='Trabajo: flexibilidad contra seguridad',
    t1ah='Las parejas',
    t1ab='<em>Job security</em>, <em>career prospects</em>, <em>a work&ndash;life '
         'balance</em>: sustantivos que llegan con su compañero fijado. Se '
         '<em>works remotely</em> con <em>a flexible schedule</em>, se '
         '<em>suffers burnout</em>, una empresa <em>takes on staff</em>. '
         'Ninguna de las palabras es rara. Las parejas son lo que dice el '
         'inglés.',
    t1an='Aprende <em>suffer burnout</em>. No <em>burnout</em>.',
    t1bh='Flexibilidad contra aislamiento',
    t1bb='La pregunta de la Parte 3 es casi siempre una forma de <em>is '
         'working from home good for people?</em> La respuesta que puntúa '
         'enfrenta dos parejas: <em>a flexible schedule</em> a un lado, los '
         'compañeros a los que ya no ves al otro.',
    t1bn='Una idea, dos frases, y <em>but</em> en medio.',
    t1ch='Seguridad contra oportunidad',
    t1cb='<em>The gig economy</em> está detrás de muchas de las preguntas '
         'de Task 2 sobre el trabajo. Defiéndela como un intercambio: ofrece '
         '<em>a flexible schedule</em> y quita <em>job security</em>; amplía '
         '<em>career prospects</em> para unos y los estrecha para otros.',
    t1cn='Di qué da y qué quita. Ese es el párrafo.',

    t2Eyebrow='Idea dos',
    t2Title='Automatización: empleos perdidos contra empleos creados',
    t2ah='Las parejas',
    t2ab='<em>Automate routine tasks</em>, <em>replace workers</em>, '
         '<em>retrain the workforce</em>; <em>productivity gains</em>, '
         '<em>low-skilled jobs</em>, <em>artificial intelligence</em>. El '
         'sustantivo trae su verbo: las tareas se <em>automated</em>, los '
         'trabajadores son <em>displaced</em>, una plantilla es '
         '<em>retrained</em>.',
    t2an='El verbo es <em>automate</em>, no <em>automatise</em>.',
    t2bh='Perdidos contra creados',
    t2bb='Todo enunciado sobre automatización es el mismo intercambio: las '
         'máquinas <em>displace</em> a los trabajadores de <em>low-skilled '
         'jobs</em>, y los <em>productivity gains</em> pagan empleos que '
         'antes no existían. Una respuesta con solo la primera mitad es un '
         'band 6. La que sopesa las dos es lo que pide la Parte 3.',
    t2bn='Nombra quién pierde, nombra quién gana, y di qué pesa más.',
    t2ch='Quién reconvierte a quién',
    t2cb='El segundo argumento va de responsabilidad. ¿Debe el Estado '
         '<em>retrain the workforce</em>, o la empresa que la '
         '<em>replaced</em>? <em>A universal basic income</em> es la frase '
         'para la respuesta que dice: ninguno de los dos.',
    t2cn='Una pareja por postura, y tres posturas donde elegir.',

    t3Eyebrow='Idea tres',
    t3Title='Ciudades: densidad contra espacio, el coche contra el autobús',
    t3ah='Las parejas',
    t3ab='<em>Urban sprawl</em>, <em>affordable housing</em>, <em>public '
         'transport</em>, <em>green spaces</em>, <em>the cost of living</em>. '
         'Un ayuntamiento <em>invests in infrastructure</em> e intenta '
         '<em>ease congestion</em>; un vecino tiene <em>a long commute</em> y '
         'aguanta <em>overcrowding</em>.',
    t3an='Congestion se <em>eased</em>. Traffic es <em>heavy</em>, nunca '
         '<em>strong</em>.',
    t3bh='Densidad contra espacio',
    t3bb='El enunciado de Task 2 suele ser una versión de <em>should cities '
         'build up or out?</em> Hacia arriba significa <em>affordable '
         'housing</em> cerca del centro y menos <em>urban sprawl</em>, al '
         'precio de <em>overcrowding</em>. Hacia fuera significa <em>green '
         'spaces</em> y <em>a long commute</em>.',
    t3bn='Las dos respuestas cuestan algo. Di qué.',
    t3ch='El coche contra el autobús',
    t3cb='La Parte 3 pregunta cómo <em>ease congestion</em>. La respuesta que '
         'ya lo ha pensado dice que una ciudad no puede salir construyendo, '
         'porque cada carretera nueva se llena; así que el dinero va a '
         '<em>public transport</em>. <em>Invest in infrastructure</em> es la '
         'pareja que carga con el argumento.',
    t3cn='<em>The cost of living</em> cierra cualquiera de las dos '
         'respuestas: pague quien pague, es el vecino.',

    mcaEyebrow='Actividad 1 · Trabajo',
    mcaTitle='¿Qué pareja, y qué palabra?',
    mcbEyebrow='Actividad 2 · Automatización',
    mcbTitle='El sustantivo trae su verbo',
    mccEyebrow='Actividad 3 · Ciudades',
    mccTitle='La pareja llana es la precisa',

    v1why='<em>Work remotely</em>. El adverbio lo fija el verbo: '
          '<em>distantly</em> es una manera de hablar, y <em>at distance</em> '
          'y <em>from distance</em> están montados palabra a palabra desde el '
          'diccionario.',
    v2why='<em>Job security</em>. <em>Work safety</em> es inglés de verdad y '
          'significa otra cosa &mdash; cascos y salidas de emergencia &mdash;, '
          'que es el fallo de precisión. Las otras dos no son parejas que el '
          'inglés tenga.',
    v3why='<em>Suffer burnout</em>, como <em>suffer losses</em> o <em>suffer a '
          'setback</em>: el sustantivo del daño lleva el verbo del daño. '
          '<em>Make</em>, <em>get into</em> y <em>fall in</em> son lo que se '
          'busca cuando la frase se aprendió como una sola palabra.',
    v4why='<em>Improve career prospects</em>. <em>Trajectories</em>, '
          '<em>futures</em> y <em>chances</em> van más allá del sustantivo '
          'que usa el inglés, y <em>augment</em> y <em>amplify</em> son los '
          'verbos casi-acertados que los acompañan. La pareja llana es la '
          'precisa.',
    v5why='<em>Displace</em> es el verbo para una persona o un empleo que algo '
          'nuevo empuja fuera. <em>Dislocate</em> es un hombro, '
          '<em>misplace</em> unas llaves, <em>evict</em> un inquilino: tres '
          'palabras reales, cada una precisa para otra cosa.',
    v6why='<em>Productivity gains</em>. La productividad tiene gain, no '
          'profit, growth ni winning; un sustantivo elige su sustantivo '
          'compañero con la misma firmeza que su verbo.',
    v7why='<em>Retrain the workforce</em>. Las otras tres son el verbo que uno '
          'se monta con <em>re-</em> más una palabra de enseñar. El inglés ya '
          'tiene el verbo, y lleva <em>the workforce</em> de objeto.',
    v8why='<em>A universal basic income</em> es el nombre de la medida, y el '
          'examinador oye el nombre u oye una suposición. Wage y salary se '
          'pagan por trabajar, que es justo lo que esto no es.',
    v9why='<em>Urban sprawl</em>, y solo eso. <em>Sprawl</em> lleva el juicio '
          '&mdash; crecimiento sin plan y feo &mdash;, por eso es la palabra '
          'que el argumento necesita y <em>spread</em> no.',
    v10why='<em>Affordable housing</em> es el término que usan igual un '
           'urbanista, un político y un examinador. <em>Economical</em> es un '
           'coche, <em>reasonable</em> es una persona, y <em>cheap-priced</em> '
           'no es inglés.',
    v11why='<em>Invest in</em>. La preposición forma parte de la pareja y '
           'viaja con el verbo venga lo que venga detrás: <em>invest in '
           'infrastructure</em>, <em>invest in public transport</em>, '
           '<em>invest in people</em>.',
    v12why='<em>A long commute</em>. Las otras tres buscan un adjetivo más raro '
           'y un sustantivo más raro y fallan en los dos. La pareja llana es '
           'la que usa cualquier hablante de inglés, y justo por eso puntúa.',

    sortEyebrow='Actividad 4 · La pareja entera',
    sortTitle='Clasifica las seis parejas',
    sortHint='Arrastra cada una a una columna &mdash; o haz clic en un '
             'elemento y luego en la columna que quieras.',
    sortBin1='Esto lo dice el inglés',
    sortBin2='Esto no lo dice',
    sortWhy='El sustantivo elige el verbo y el adjetivo. Congestion se '
            '<em>eased</em>, staff se <em>taken on</em>, y <em>the gig '
            'economy</em> es un nombre fijo. Congestion es <em>heavy</em> o '
            '<em>severe</em>, traffic es <em>heavy</em>, y housing es '
            '<em>affordable</em>: '
            'las tres de la derecha son lo que uno se monta con el '
            'diccionario, palabra a palabra. Aprende la frase entera y la '
            'elección nunca será tuya para fallarla.',

    actTitle='Responde desde el banco',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas. Uno hace de examinador y plantea preguntas de '
                  'la Parte 3 sobre trabajo y ciudades &mdash; <em>is working '
                  'from home good for a company? Should cities build up or '
                  'out? Who should pay to retrain people?</em> El otro '
                  'responde a cada una durante un minuto usando solo el banco '
                  'de esta lección. Luego cambiad.',
    actSpeak1='Cada respuesta enfrenta dos parejas &mdash; una por cada lado, '
              'con <em>but</em> o <em>whereas</em> en medio.',
    actSpeak2='El examinador te para en cuanto uses una palabra suelta donde '
              'el banco tiene una pareja, y lo dices otra vez con la frase.',
    actSpeak3='Cada tercera pregunta es de seguimiento &mdash; <em>why?</em> o '
              '<em>can you give an example?</em> &mdash;, y la respuesta tiene '
              'que añadir una pareja que aún no hayas usado.',
    actWriteKind='Escritura · 150–200 palabras',
    actWriteBrief='Elige una de las tres ideas y escribe sobre ella un párrafo '
                  'de desarrollo de Task 2: la afirmación, el argumento, un '
                  'ejemplo, la concesión. Usa al menos cinco parejas del banco '
                  'y subraya cada una. Luego reléelo y cuenta: una frase sin '
                  'pareja no hace nada por tu Lexical Resource.',
    actPlaceholder='Automation displaces workers in low-skilled jobs, but…',
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
