# -*- coding: utf-8 -*-
"""Interface strings for IELTS Vocabulary: Work, Automation and Cities.

Ten languages: English, German and Spanish from the start; French,
Italian, Portuguese, Russian, Arabic, Chinese and Japanese added on
2026-09-24 (conventions in `ielts_langs.py`).

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


# ── French ─────────────────────────────────────────────────────────────
T['fr'] = dict(
    coverTitle='Work, Automation <em>and Cities</em>',
    coverSub='Trois thèmes qui reviennent sans cesse en Part 3 et en Task 2, et '
             'les associations qui donnent à une réponse sur n’importe lequel '
             'd’entre eux l’air d’avoir été pensée',
    chipLevel='C1 · Avancé', chipFocus='Speaking &amp; Writing Task 2',
    chipCount='18 points',

    t1Eyebrow='Première idée',
    t1Title='Le travail : la flexibilité contre la sécurité',
    t1ah='Les associations',
    t1ab='<em>Job security</em>, <em>career prospects</em>, <em>a work&ndash;life '
         'balance</em> : des noms qui arrivent avec leur partenaire déjà fixé. On '
         '<em>work remotely</em> avec <em>a flexible schedule</em>, on <em>suffer '
         'burnout</em>, une entreprise <em>takes on staff</em>. Aucun de ces mots '
         'n’est rare. Les associations, c’est ce que dit l’anglais.',
    t1an='Apprenez <em>suffer burnout</em>. Pas <em>burnout</em>.',
    t1bh='La flexibilité contre l’isolement',
    t1bb='La question de Part 3 est presque toujours une variante de <em>is '
         'working from home good for people?</em> La réponse qui rapporte met '
         'deux associations en balance : <em>a flexible schedule</em> d’un côté, '
         'les collègues qu’on ne voit plus de l’autre.',
    t1bn='Une idée, deux expressions, et un <em>but</em> entre les deux.',
    t1ch='La sécurité contre les occasions',
    t1cb='<em>The gig economy</em> est derrière beaucoup des questions de Task 2 '
         'sur le travail. Présentez-la comme un échange : elle offre <em>a '
         'flexible schedule</em> et enlève la <em>job security</em> ; elle élargit '
         'les <em>career prospects</em> des uns et rétrécit ceux des autres.',
    t1cn='Dites ce qu’elle donne et ce qu’elle prend. Voilà le paragraphe.',

    t2Eyebrow='Deuxième idée',
    t2Title='L’automatisation : emplois perdus contre emplois créés',
    t2ah='Les associations',
    t2ab='<em>Automate routine tasks</em>, <em>replace workers</em>, '
         '<em>retrain the workforce</em> ; <em>productivity gains</em>, '
         '<em>low-skilled jobs</em>, <em>artificial intelligence</em>. Le nom '
         'amène son verbe : les tâches sont <em>automated</em>, les travailleurs '
         '<em>displaced</em>, une main-d’œuvre <em>retrained</em>.',
    t2an='Le verbe est <em>automate</em>, pas <em>automatise</em>.',
    t2bh='Perdus contre créés',
    t2bb='Chaque sujet sur l’automatisation est le même échange : les machines '
         '<em>displace</em> les travailleurs dans les <em>low-skilled jobs</em>, et '
         'les <em>productivity gains</em> financent des emplois qui n’existaient '
         'pas avant. Une réponse qui n’a que la première moitié vaut un band 6. '
         'Celle qui pèse les deux, c’est ce que demande la Part 3.',
    t2bn='Dites qui perd, dites qui gagne, et dites ce qui compte le plus.',
    t2ch='Qui forme qui',
    t2cb='Le second argument porte sur la responsabilité. Est-ce à l’État de '
         '<em>retrain the workforce</em>, ou à l’employeur qui l’a '
         '<em>replaced</em> ? <em>A universal basic income</em> est l’expression '
         'pour la réponse qui dit : ni l’un ni l’autre.',
    t2cn='Une association par position, et trois positions au choix.',

    t3Eyebrow='Troisième idée',
    t3Title='Les villes : la densité contre l’espace, la voiture contre le bus',
    t3ah='Les associations',
    t3ab='<em>Urban sprawl</em>, <em>affordable housing</em>, <em>public '
         'transport</em>, <em>green spaces</em>, <em>the cost of living</em>. Une '
         'municipalité <em>invests in infrastructure</em> et tente d’<em>ease '
         'congestion</em> ; un habitant a <em>a long commute</em> et supporte '
         'l’<em>overcrowding</em>.',
    t3an='La congestion est <em>eased</em>. Le trafic est <em>heavy</em>, jamais '
         '<em>strong</em>.',
    t3bh='La densité contre l’espace',
    t3bb='Le sujet de Task 2 est en général une version de <em>should cities '
         'build up or out?</em> En hauteur, c’est de l’<em>affordable '
         'housing</em> près du centre et moins d’<em>urban sprawl</em>, au prix '
         'de l’<em>overcrowding</em>. En largeur, ce sont des <em>green '
         'spaces</em> et <em>a long commute</em>.',
    t3bn='Les deux réponses ont un coût. Dites lequel.',
    t3ch='La voiture contre le bus',
    t3cb='La Part 3 demande comment <em>ease congestion</em>. La réponse de '
         'quelqu’un qui y a déjà réfléchi dit qu’une ville ne peut pas s’en '
         'sortir en construisant, parce que chaque nouvelle route se remplit ; '
         'l’argent va donc aux <em>public transport</em>. <em>Invest in '
         'infrastructure</em> est l’association qui porte l’idée.',
    t3cn='<em>The cost of living</em> clôt l’une ou l’autre réponse : qui que ce '
         'soit qui paie, c’est l’habitant.',

    mcaEyebrow='Activité 1 · Le travail',
    mcaTitle='Quelle association, et quel mot ?',
    mcbEyebrow='Activité 2 · L’automatisation',
    mcbTitle='Le nom amène son verbe',
    mccEyebrow='Activité 3 · Les villes',
    mccTitle='L’association simple est la plus précise',

    v1why='<em>Work remotely</em>. L’adverbe est imposé par le verbe : '
          '<em>distantly</em> décrit une façon de parler, et <em>at distance</em> '
          'et <em>from distance</em> sont fabriqués mot à mot à partir d’un '
          'dictionnaire.',
    v2why='<em>Job security</em>. <em>Work safety</em> existe en anglais et veut '
          'dire autre chose &mdash; les casques et les sorties de secours &mdash;, '
          'et c’est là le raté de précision. Les deux autres ne sont pas des '
          'associations que l’anglais possède.',
    v3why='<em>Suffer burnout</em>, comme <em>suffer losses</em> ou <em>suffer a '
          'setback</em> : le nom d’un dommage prend le verbe du dommage. '
          '<em>Make</em>, <em>get into</em> et <em>fall in</em>, c’est ce qu’on '
          'attrape quand on a appris l’expression comme un seul mot.',
    v4why='<em>Improve career prospects</em>. <em>Trajectories</em>, '
          '<em>futures</em> et <em>chances</em> vont chacun au-delà du nom '
          'qu’emploie l’anglais, et <em>augment</em> et <em>amplify</em> sont les '
          'verbes presque justes qui les accompagnent. L’association simple est '
          'la plus précise.',
    v5why='<em>Displace</em> est le verbe pour une personne ou un emploi chassés '
          'par quelque chose de nouveau. On <em>dislocate</em> une épaule, on '
          '<em>misplace</em> ses clés, on <em>evict</em> un locataire &mdash; trois '
          'vrais mots, chacun précis sur autre chose.',
    v6why='<em>Productivity gains</em>. La productivité a un <em>gain</em>, pas un '
          '<em>profit</em>, une <em>growth</em> ou un <em>winning</em> ; un nom '
          'choisit son nom partenaire aussi fermement qu’il choisit un verbe.',
    v7why='<em>Retrain the workforce</em>. Les trois autres sont le verbe qu’un '
          'apprenant fabrique avec <em>re-</em> plus un mot pour « enseigner ». '
          'L’anglais a déjà le verbe, et il prend <em>the workforce</em> comme '
          'complément.',
    v8why='<em>A universal basic income</em> est le nom de la mesure, et '
          'l’examinateur entend soit le nom, soit une devinette. Un <em>wage</em> '
          'et un <em>salary</em> rémunèrent un travail, et c’est justement la '
          'seule chose que ce revenu n’est pas.',
    v9why='<em>Urban sprawl</em>, et rien d’autre. <em>Sprawl</em> porte le '
          'jugement &mdash; une croissance anarchique et laide &mdash;, et c’est '
          'pourquoi c’est le mot dont l’argument a besoin, et pas <em>spread</em>.',
    v10why='<em>Affordable housing</em> est le terme qu’emploient l’urbaniste, '
           'l’élu et l’examinateur. <em>Economical</em> se dit d’une voiture, '
           '<em>reasonable</em> d’une personne, et <em>cheap-priced</em> n’est pas '
           'de l’anglais.',
    v11why='<em>Invest in</em>. La préposition fait partie de l’association et '
           'suit le verbe quoi qu’il vienne ensuite : <em>invest in '
           'infrastructure</em>, <em>invest in public transport</em>, <em>invest '
           'in people</em>.',
    v12why='<em>A long commute</em>. Les trois autres vont chercher un adjectif '
           'plus rare et un nom plus rare, et ratent les deux. L’association '
           'simple est celle qu’emploient tous les anglophones, et c’est '
           'exactement pour cela qu’elle rapporte.',

    sortEyebrow='Activité 4 · L’association, en entier',
    sortTitle='Classez les six associations',
    sortHint='Faites glisser chacune dans une colonne &mdash; ou cliquez sur '
             'un élément, puis sur la colonne voulue.',
    sortBin1='L’anglais dit cela',
    sortBin2='L’anglais ne le dit pas',
    sortWhy='Le nom choisit le verbe et l’adjectif. La congestion est '
            '<em>eased</em>, le personnel est <em>taken on</em>, et <em>the gig '
            'economy</em> est un nom figé. La congestion est <em>heavy</em> ou '
            '<em>severe</em>, le trafic est <em>heavy</em>, et le logement est '
            '<em>affordable</em> &mdash; les trois de droite sont ce qu’un '
            'apprenant fabrique à partir d’un dictionnaire, mot à mot. Apprenez '
            'l’expression en entier, et le choix n’est jamais à vous de le rater.',

    actTitle='Répondez avec la réserve',
    actUse='Utilisez-en au moins trois :',
    actSpeakBrief='À deux. L’un de vous est l’examinateur et pose des questions de '
                  'Part 3 sur le travail et les villes &mdash; <em>is working '
                  'from home good for a company? Should cities build up or out? '
                  'Who should pay to retrain people?</em> L’autre répond à '
                  'chacune pendant une minute en n’utilisant que la réserve de '
                  'cette leçon. Puis inversez.',
    actSpeak1='Chaque réponse met deux associations en balance &mdash; une pour '
              'chaque côté, avec <em>but</em> ou <em>whereas</em> entre les deux.',
    actSpeak2='L’examinateur vous arrête dès que vous employez un mot isolé là où '
              'la réserve a une association, et vous le redites avec '
              'l’expression.',
    actSpeak3='Une question sur trois est une relance &mdash; <em>why?</em> ou '
              '<em>can you give an example?</em> &mdash; et la réponse doit '
              'ajouter une association que vous n’avez pas encore utilisée.',
    actWriteKind='Écriture · 150–200 mots',
    actWriteBrief='Choisissez l’une des trois idées et écrivez un paragraphe de '
                  'développement de Task 2 : l’affirmation, l’argument, un '
                  'exemple, la concession. Utilisez au moins cinq associations '
                  'de la réserve et soulignez chacune. Puis relisez et comptez : '
                  'une phrase sans association ne fait rien pour votre Lexical '
                  'Resource.',
    actPlaceholder='Automation displaces workers in low-skilled jobs, but…',
)


# ── Italian ────────────────────────────────────────────────────────────
T['it'] = dict(
    coverTitle='Work, Automation <em>and Cities</em>',
    coverSub='Tre temi che tornano di continuo nella Part 3 e nella Task 2, e le '
             'combinazioni che fanno sembrare ragionata una risposta su '
             'ciascuno di essi',
    chipLevel='C1 · Avanzato', chipFocus='Speaking e Writing Task 2',
    chipCount='18 punti',

    t1Eyebrow='Prima idea',
    t1Title='Il lavoro: flessibilità contro sicurezza',
    t1ah='Le combinazioni',
    t1ab='<em>Job security</em>, <em>career prospects</em>, <em>a work&ndash;life '
         'balance</em>: nomi che arrivano con il partner già fissato. Si '
         '<em>work remotely</em> con <em>a flexible schedule</em>, si <em>suffer '
         'burnout</em>, un’azienda <em>takes on staff</em>. Nessuna di queste '
         'parole è rara. Le combinazioni sono ciò che dice l’inglese.',
    t1an='Impara <em>suffer burnout</em>. Non <em>burnout</em>.',
    t1bh='Flessibilità contro isolamento',
    t1bb='La domanda della Part 3 è quasi sempre una variante di <em>is working '
         'from home good for people?</em> La risposta che prende punti mette due '
         'combinazioni una contro l’altra: <em>a flexible schedule</em> da una '
         'parte, i colleghi che non vedi più dall’altra.',
    t1bn='Un’idea, due espressioni, e un <em>but</em> in mezzo.',
    t1ch='Sicurezza contro opportunità',
    t1cb='Dietro molte domande di Task 2 sul lavoro c’è <em>the gig economy</em>. '
         'Presentala come uno scambio: offre <em>a flexible schedule</em> e toglie '
         'la <em>job security</em>; allarga le <em>career prospects</em> di alcuni '
         'e restringe quelle di altri.',
    t1cn='Di’ che cosa dà e che cosa toglie. Ecco il paragrafo.',

    t2Eyebrow='Seconda idea',
    t2Title='L’automazione: posti persi contro posti creati',
    t2ah='Le combinazioni',
    t2ab='<em>Automate routine tasks</em>, <em>replace workers</em>, '
         '<em>retrain the workforce</em>; <em>productivity gains</em>, '
         '<em>low-skilled jobs</em>, <em>artificial intelligence</em>. Il nome si '
         'porta dietro il verbo: i compiti sono <em>automated</em>, i lavoratori '
         '<em>displaced</em>, una forza lavoro <em>retrained</em>.',
    t2an='Il verbo è <em>automate</em>, non <em>automatise</em>.',
    t2bh='Persi contro creati',
    t2bb='Ogni traccia sull’automazione è lo stesso scambio: le macchine '
         '<em>displace</em> i lavoratori nei <em>low-skilled jobs</em>, e i '
         '<em>productivity gains</em> pagano lavori che prima non esistevano. Una '
         'risposta con solo la prima metà vale un band 6. Quella che pesa '
         'entrambe è ciò che la Part 3 chiede.',
    t2bn='Di’ chi perde, di’ chi guadagna, e di’ che cosa conta di più.',
    t2ch='Chi riqualifica chi',
    t2cb='Il secondo argomento riguarda la responsabilità. Deve essere lo Stato a '
         '<em>retrain the workforce</em>, o il datore di lavoro che l’ha '
         '<em>replaced</em>? <em>A universal basic income</em> è l’espressione '
         'per la risposta che dice: nessuno dei due.',
    t2cn='Una combinazione per posizione, e tre posizioni tra cui scegliere.',

    t3Eyebrow='Terza idea',
    t3Title='Le città: densità contro spazio, l’auto contro l’autobus',
    t3ah='Le combinazioni',
    t3ab='<em>Urban sprawl</em>, <em>affordable housing</em>, <em>public '
         'transport</em>, <em>green spaces</em>, <em>the cost of living</em>. Un '
         'comune <em>invests in infrastructure</em> e cerca di <em>ease '
         'congestion</em>; un residente ha <em>a long commute</em> e sopporta '
         'l’<em>overcrowding</em>.',
    t3an='La congestione si <em>ease</em>. Il traffico è <em>heavy</em>, mai '
         '<em>strong</em>.',
    t3bh='Densità contro spazio',
    t3bb='La traccia di Task 2 è di solito una versione di <em>should cities '
         'build up or out?</em> In altezza vuol dire <em>affordable housing</em> '
         'vicino al centro e meno <em>urban sprawl</em>, al prezzo '
         'dell’<em>overcrowding</em>. In estensione vuol dire <em>green '
         'spaces</em> e <em>a long commute</em>.',
    t3bn='Tutte e due le risposte costano qualcosa. Di’ che cosa.',
    t3ch='L’auto contro l’autobus',
    t3cb='La Part 3 chiede come <em>ease congestion</em>. La risposta di chi ci '
         'ha già pensato dice che una città non ne esce costruendo, perché ogni '
         'nuova strada si riempie; quindi i soldi vanno al <em>public '
         'transport</em>. <em>Invest in infrastructure</em> è la combinazione che '
         'regge il punto.',
    t3cn='<em>The cost of living</em> chiude l’una e l’altra risposta: chiunque '
         'paghi, è il residente.',

    mcaEyebrow='Attività 1 · Il lavoro',
    mcaTitle='Quale combinazione, e quale parola?',
    mcbEyebrow='Attività 2 · L’automazione',
    mcbTitle='Il nome si porta dietro il verbo',
    mccEyebrow='Attività 3 · Le città',
    mccTitle='La combinazione semplice è quella precisa',

    v1why='<em>Work remotely</em>. L’avverbio lo impone il verbo: '
          '<em>distantly</em> è un modo di parlare, e <em>at distance</em> e '
          '<em>from distance</em> sono costruiti parola per parola da un '
          'dizionario.',
    v2why='<em>Job security</em>. <em>Work safety</em> esiste in inglese e vuol '
          'dire altro &mdash; caschi e uscite di sicurezza &mdash;, ed è questo '
          'l’errore di precisione. Le altre due non sono combinazioni che '
          'l’inglese conosce.',
    v3why='<em>Suffer burnout</em>, come <em>suffer losses</em> o <em>suffer a '
          'setback</em>: il nome di un danno vuole il verbo del danno. '
          '<em>Make</em>, <em>get into</em> e <em>fall in</em> sono ciò che si '
          'afferra quando l’espressione è stata imparata come una parola sola.',
    v4why='<em>Improve career prospects</em>. <em>Trajectories</em>, '
          '<em>futures</em> e <em>chances</em> vanno oltre il nome che usa '
          'l’inglese, e <em>augment</em> e <em>amplify</em> sono i verbi quasi '
          'giusti che li accompagnano. La combinazione semplice è quella precisa.',
    v5why='<em>Displace</em> è il verbo per una persona o un lavoro spinti via da '
          'qualcosa di nuovo. Si <em>dislocate</em> una spalla, si '
          '<em>misplace</em> un mazzo di chiavi, si <em>evict</em> un inquilino '
          '&mdash; tre parole vere, ciascuna precisa su qualcos’altro.',
    v6why='<em>Productivity gains</em>. La produttività ha un <em>gain</em>, non '
          'un <em>profit</em>, una <em>growth</em> o un <em>winning</em>; un nome '
          'sceglie il nome partner con la stessa fermezza con cui sceglie un '
          'verbo.',
    v7why='<em>Retrain the workforce</em>. Le altre tre sono il verbo che chi '
          'impara costruisce con <em>re-</em> più una parola per «insegnare». '
          'L’inglese il verbo ce l’ha già, e prende <em>the workforce</em> come '
          'complemento.',
    v8why='<em>A universal basic income</em> è il nome della misura, e '
          'l’esaminatore sente o il nome o un tentativo a caso. Un <em>wage</em> e '
          'un <em>salary</em> pagano un lavoro, ed è proprio l’unica cosa che '
          'questo reddito non è.',
    v9why='<em>Urban sprawl</em>, e solo quello. <em>Sprawl</em> contiene il '
          'giudizio &mdash; una crescita disordinata e brutta &mdash;, ed è per '
          'questo che è la parola di cui ha bisogno l’argomento, e '
          '<em>spread</em> no.',
    v10why='<em>Affordable housing</em> è il termine che usano l’urbanista, il '
           'politico e l’esaminatore. <em>Economical</em> si dice di un’auto, '
           '<em>reasonable</em> di una persona, e <em>cheap-priced</em> non è '
           'inglese.',
    v11why='<em>Invest in</em>. La preposizione fa parte della combinazione e '
           'viaggia con il verbo qualunque cosa segua: <em>invest in '
           'infrastructure</em>, <em>invest in public transport</em>, <em>invest '
           'in people</em>.',
    v12why='<em>A long commute</em>. Le altre tre cercano un aggettivo più raro e '
           'un nome più raro, e li sbagliano entrambi. La combinazione semplice è '
           'quella che usano tutti i parlanti inglesi, ed è proprio per questo '
           'che prende punti.',

    sortEyebrow='Attività 4 · La combinazione, intera',
    sortTitle='Classifica le sei combinazioni',
    sortHint='Trascina ciascuna in una colonna &mdash; oppure clicca su un '
             'elemento e poi sulla colonna che vuoi.',
    sortBin1='L’inglese dice così',
    sortBin2='L’inglese non lo dice',
    sortWhy='Il nome sceglie il verbo e l’aggettivo. La congestione si '
            '<em>ease</em>, il personale si <em>take on</em>, e <em>the gig '
            'economy</em> è un nome fisso. La congestione è <em>heavy</em> o '
            '<em>severe</em>, il traffico è <em>heavy</em>, e le case sono '
            '<em>affordable</em> &mdash; le tre a destra sono ciò che chi impara '
            'costruisce da un dizionario, parola per parola. Impara l’espressione '
            'intera e la scelta non sarà mai tua da sbagliare.',

    actTitle='Rispondi con la banca',
    actUse='Usane almeno tre:',
    actSpeakBrief='In coppia. Uno di voi fa l’esaminatore e pone domande di Part 3 '
                  'sul lavoro e sulle città &mdash; <em>is working from home good '
                  'for a company? Should cities build up or out? Who should pay '
                  'to retrain people?</em> L’altro risponde a ciascuna per un '
                  'minuto usando solo la banca di questa lezione. Poi vi '
                  'scambiate.',
    actSpeak1='Ogni risposta mette due combinazioni una contro l’altra &mdash; una '
              'per lato, con <em>but</em> o <em>whereas</em> in mezzo.',
    actSpeak2='L’esaminatore ti ferma appena usi una parola isolata dove la banca '
              'ha una combinazione, e tu lo ripeti con l’espressione.',
    actSpeak3='Una domanda su tre è un approfondimento &mdash; <em>why?</em> o '
              '<em>can you give an example?</em> &mdash; e la risposta deve '
              'aggiungere una combinazione che non hai ancora usato.',
    actWriteKind='Scrittura · 150–200 parole',
    actWriteBrief='Scegli una delle tre idee e scrivi un paragrafo centrale di Task '
                  '2: la tesi, l’argomento, un esempio, la concessione. Usa almeno '
                  'cinque combinazioni della banca e sottolineale tutte. Poi '
                  'rileggi e conta: una frase senza combinazioni non fa nulla per '
                  'il tuo Lexical Resource.',
    actPlaceholder='Automation displaces workers in low-skilled jobs, but…',
)


# ── Portuguese ─────────────────────────────────────────────────────────
T['pt'] = dict(
    coverTitle='Work, Automation <em>and Cities</em>',
    coverSub='Três temas que aparecem uma e outra vez na Part 3 e na Task 2, e as '
             'combinações que fazem uma resposta sobre qualquer um deles parecer '
             'pensada',
    chipLevel='C1 · Avançado', chipFocus='Speaking e Writing Task 2',
    chipCount='18 pontos',

    t1Eyebrow='Primeira ideia',
    t1Title='O trabalho: flexibilidade contra segurança',
    t1ah='As combinações',
    t1ab='<em>Job security</em>, <em>career prospects</em>, <em>a work&ndash;life '
         'balance</em>: nomes que chegam com o par já fixado. Faz-se <em>work '
         'remotely</em> com <em>a flexible schedule</em>, <em>suffer '
         'burnout</em>, e uma empresa <em>takes on staff</em>. Nenhuma destas '
         'palavras é rara. As combinações são o que o inglês diz.',
    t1an='Aprende <em>suffer burnout</em>. Não <em>burnout</em>.',
    t1bh='Flexibilidade contra isolamento',
    t1bb='A pergunta da Part 3 é quase sempre uma versão de <em>is working from '
         'home good for people?</em> A resposta que conta põe duas combinações '
         'uma contra a outra: <em>a flexible schedule</em> de um lado, os colegas '
         'que já não vês do outro.',
    t1bn='Uma ideia, duas expressões e um <em>but</em> no meio.',
    t1ch='Segurança contra oportunidade',
    t1cb='Por trás de muitas perguntas de Task 2 sobre trabalho está <em>the gig '
         'economy</em>. Apresenta-a como uma troca: oferece <em>a flexible '
         'schedule</em> e tira a <em>job security</em>; alarga as <em>career '
         'prospects</em> de uns e estreita as de outros.',
    t1cn='Diz o que dá e o que tira. É esse o parágrafo.',

    t2Eyebrow='Segunda ideia',
    t2Title='A automação: empregos perdidos contra empregos criados',
    t2ah='As combinações',
    t2ab='<em>Automate routine tasks</em>, <em>replace workers</em>, '
         '<em>retrain the workforce</em>; <em>productivity gains</em>, '
         '<em>low-skilled jobs</em>, <em>artificial intelligence</em>. O nome traz '
         'o seu verbo: as tarefas são <em>automated</em>, os trabalhadores '
         '<em>displaced</em>, uma força de trabalho <em>retrained</em>.',
    t2an='O verbo é <em>automate</em>, não <em>automatise</em>.',
    t2bh='Perdidos contra criados',
    t2bb='Todos os enunciados sobre automação são a mesma troca: as máquinas '
         '<em>displace</em> trabalhadores em <em>low-skilled jobs</em>, e os '
         '<em>productivity gains</em> pagam empregos que antes não existiam. Uma '
         'resposta só com a primeira metade vale um band 6. A que pesa as duas é '
         'o que a Part 3 pede.',
    t2bn='Diz quem perde, diz quem ganha e diz o que pesa mais.',
    t2ch='Quem requalifica quem',
    t2cb='O segundo argumento é sobre responsabilidade. Deve ser o Estado a '
         '<em>retrain the workforce</em>, ou o empregador que a <em>replaced</em>? '
         '<em>A universal basic income</em> é a expressão para a resposta que diz '
         'nem um nem outro.',
    t2cn='Uma combinação por posição, e três posições à escolha.',

    t3Eyebrow='Terceira ideia',
    t3Title='As cidades: densidade contra espaço, o carro contra o autocarro',
    t3ah='As combinações',
    t3ab='<em>Urban sprawl</em>, <em>affordable housing</em>, <em>public '
         'transport</em>, <em>green spaces</em>, <em>the cost of living</em>. Uma '
         'câmara municipal <em>invests in infrastructure</em> e tenta <em>ease '
         'congestion</em>; um morador tem <em>a long commute</em> e aguenta o '
         '<em>overcrowding</em>.',
    t3an='O congestionamento é <em>eased</em>. O trânsito é <em>heavy</em>, nunca '
         '<em>strong</em>.',
    t3bh='Densidade contra espaço',
    t3bb='O enunciado de Task 2 é normalmente uma versão de <em>should cities '
         'build up or out?</em> Crescer em altura significa <em>affordable '
         'housing</em> perto do centro e menos <em>urban sprawl</em>, à custa do '
         '<em>overcrowding</em>. Crescer para fora significa <em>green '
         'spaces</em> e <em>a long commute</em>.',
    t3bn='As duas respostas custam alguma coisa. Diz o quê.',
    t3ch='O carro contra o autocarro',
    t3cb='A Part 3 pergunta como <em>ease congestion</em>. A resposta de quem já '
         'pensou no assunto diz que uma cidade não sai do problema a construir '
         'estradas, porque cada estrada nova enche; por isso o dinheiro vai para '
         'o <em>public transport</em>. <em>Invest in infrastructure</em> é a '
         'combinação que sustenta o argumento.',
    t3cn='<em>The cost of living</em> fecha qualquer das respostas: seja quem for '
         'a pagar, quem paga é o morador.',

    mcaEyebrow='Atividade 1 · O trabalho',
    mcaTitle='Que combinação, e que palavra?',
    mcbEyebrow='Atividade 2 · A automação',
    mcbTitle='O nome traz o seu verbo',
    mccEyebrow='Atividade 3 · As cidades',
    mccTitle='A combinação simples é a precisa',

    v1why='<em>Work remotely</em>. O advérbio é imposto pelo verbo: '
          '<em>distantly</em> é uma maneira de falar, e <em>at distance</em> e '
          '<em>from distance</em> são construídos palavra a palavra a partir de '
          'um dicionário.',
    v2why='<em>Job security</em>. <em>Work safety</em> existe em inglês e quer '
          'dizer outra coisa &mdash; capacetes e saídas de emergência &mdash;, e é '
          'aí que está a falha de precisão. As outras duas não são combinações '
          'que o inglês tenha.',
    v3why='<em>Suffer burnout</em>, como <em>suffer losses</em> ou <em>suffer a '
          'setback</em>: o nome de um dano leva o verbo do dano. <em>Make</em>, '
          '<em>get into</em> e <em>fall in</em> são o que se agarra quando a '
          'expressão foi aprendida como uma só palavra.',
    v4why='<em>Improve career prospects</em>. <em>Trajectories</em>, '
          '<em>futures</em> e <em>chances</em> vão além do nome que o inglês usa, '
          'e <em>augment</em> e <em>amplify</em> são os verbos quase certos que '
          'os acompanham. A combinação simples é a precisa.',
    v5why='<em>Displace</em> é o verbo para uma pessoa ou um emprego empurrados '
          'para fora por algo novo. <em>Dislocate</em> é um ombro, '
          '<em>misplace</em> é um molho de chaves, <em>evict</em> é um inquilino '
          '&mdash; três palavras reais, cada uma precisa sobre outra coisa.',
    v6why='<em>Productivity gains</em>. A produtividade tem um <em>gain</em>, não '
          'um <em>profit</em>, uma <em>growth</em> ou um <em>winning</em>; um nome '
          'escolhe o nome que o acompanha com a mesma firmeza com que escolhe um '
          'verbo.',
    v7why='<em>Retrain the workforce</em>. As outras três são o verbo que quem '
          'aprende constrói com <em>re-</em> mais uma palavra para «ensinar». O '
          'inglês já tem o verbo, e ele leva <em>the workforce</em> como '
          'complemento.',
    v8why='<em>A universal basic income</em> é o nome da medida, e o examinador '
          'ouve o nome ou ouve um palpite. Um <em>wage</em> e um <em>salary</em> '
          'pagam trabalho, que é precisamente a única coisa que isto não é.',
    v9why='<em>Urban sprawl</em>, e só isso. <em>Sprawl</em> traz o juízo '
          '&mdash; crescimento desordenado e feio &mdash;, e é por isso que é a '
          'palavra de que o argumento precisa, e <em>spread</em> não.',
    v10why='<em>Affordable housing</em> é o termo que usam o urbanista, o '
           'político e o examinador. <em>Economical</em> é um carro, '
           '<em>reasonable</em> é uma pessoa, e <em>cheap-priced</em> não é '
           'inglês.',
    v11why='<em>Invest in</em>. A preposição faz parte da combinação e acompanha '
           'o verbo seja qual for o que vem a seguir: <em>invest in '
           'infrastructure</em>, <em>invest in public transport</em>, <em>invest '
           'in people</em>.',
    v12why='<em>A long commute</em>. As outras três vão buscar um adjetivo mais '
           'raro e um nome mais raro e falham nos dois. A combinação simples é a '
           'que todos os falantes de inglês usam, e é exatamente por isso que '
           'conta.',

    sortEyebrow='Atividade 4 · A combinação, inteira',
    sortTitle='Classifica as seis combinações',
    sortHint='Arrasta cada uma para uma coluna &mdash; ou clica num elemento e '
             'depois na coluna que quiseres.',
    sortBin1='O inglês diz isto',
    sortBin2='O inglês não diz isto',
    sortWhy='O nome escolhe o verbo e o adjetivo. O congestionamento é '
            '<em>eased</em>, o pessoal é <em>taken on</em>, e <em>the gig '
            'economy</em> é um nome fixo. O congestionamento é <em>heavy</em> ou '
            '<em>severe</em>, o trânsito é <em>heavy</em>, e a habitação é '
            '<em>affordable</em> &mdash; as três da direita são o que quem aprende '
            'constrói a partir de um dicionário, palavra a palavra. Aprende a '
            'expressão inteira, e a escolha nunca será tua para errar.',

    actTitle='Responde com o banco',
    actUse='Usa pelo menos três:',
    actSpeakBrief='Em pares. Um de vocês é o examinador e faz perguntas de Part 3 '
                  'sobre trabalho e cidades &mdash; <em>is working from home good '
                  'for a company? Should cities build up or out? Who should pay '
                  'to retrain people?</em> O outro responde a cada uma durante um '
                  'minuto usando só o banco desta lição. Depois troquem.',
    actSpeak1='Cada resposta põe duas combinações uma contra a outra &mdash; uma '
              'para cada lado, com <em>but</em> ou <em>whereas</em> no meio.',
    actSpeak2='O examinador interrompe-te assim que usas uma palavra solta onde o '
              'banco tem uma combinação, e tu voltas a dizer a frase com a '
              'expressão.',
    actSpeak3='Uma em cada três perguntas é de seguimento &mdash; <em>why?</em> ou '
              '<em>can you give an example?</em> &mdash; e a resposta tem de '
              'juntar uma combinação que ainda não usaste.',
    actWriteKind='Escrita · 150–200 palavras',
    actWriteBrief='Escolhe uma das três ideias e escreve um parágrafo de '
                  'desenvolvimento de Task 2: a afirmação, o argumento, um '
                  'exemplo, a concessão. Usa pelo menos cinco combinações do '
                  'banco e sublinha cada uma. Depois relê e conta: uma frase sem '
                  'nenhuma combinação não faz nada pelo teu Lexical Resource.',
    actPlaceholder='Automation displaces workers in low-skilled jobs, but…',
)


# ── Russian ────────────────────────────────────────────────────────────
T['ru'] = dict(
    coverTitle='Work, Automation <em>and Cities</em>',
    coverSub='Три темы, которые снова и снова встречаются в Part 3 и Task 2, и '
             'сочетания, благодаря которым ответ на любую из них звучит '
             'продуманно',
    chipLevel='C1 · Продвинутый', chipFocus='Speaking и Writing Task 2',
    chipCount='18 баллов',

    t1Eyebrow='Идея первая',
    t1Title='Работа: гибкость против стабильности',
    t1ah='Сочетания',
    t1ab='<em>Job security</em>, <em>career prospects</em>, <em>a work&ndash;life '
         'balance</em>: существительные, которые приходят с уже закреплённой '
         'парой. Вы <em>work remotely</em> по <em>a flexible schedule</em>, вы '
         '<em>suffer burnout</em>, компания <em>takes on staff</em>. Ни одно из '
         'этих слов не редкое. Сочетания &mdash; это то, как говорят '
         'по-английски.',
    t1an='Учите <em>suffer burnout</em>. Не <em>burnout</em>.',
    t1bh='Гибкость против изоляции',
    t1bb='Вопрос Part 3 почти всегда &mdash; вариант <em>is working from home '
         'good for people?</em> Ответ, который приносит баллы, сталкивает два '
         'сочетания: с одной стороны <em>a flexible schedule</em>, с другой '
         '&mdash; коллеги, которых вы больше не видите.',
    t1bn='Одна идея, две фразы и <em>but</em> между ними.',
    t1ch='Стабильность против возможностей',
    t1cb='За многими вопросами Task 2 о работе стоит <em>the gig economy</em>. '
         'Представьте её как обмен: она даёт <em>a flexible schedule</em> и '
         'отнимает <em>job security</em>; одним расширяет <em>career '
         'prospects</em>, другим сужает.',
    t1cn='Скажите, что она даёт и что отнимает. Это и есть абзац.',

    t2Eyebrow='Идея вторая',
    t2Title='Автоматизация: потерянные рабочие места против созданных',
    t2ah='Сочетания',
    t2ab='<em>Automate routine tasks</em>, <em>replace workers</em>, '
         '<em>retrain the workforce</em>; <em>productivity gains</em>, '
         '<em>low-skilled jobs</em>, <em>artificial intelligence</em>. '
         'Существительное приводит свой глагол: задачи <em>automated</em>, '
         'работники <em>displaced</em>, рабочая сила <em>retrained</em>.',
    t2an='Глагол &mdash; <em>automate</em>, а не <em>automatise</em>.',
    t2bh='Потерянные против созданных',
    t2bb='Любое задание про автоматизацию &mdash; один и тот же обмен: машины '
         '<em>displace</em> работников в <em>low-skilled jobs</em>, а '
         '<em>productivity gains</em> оплачивают работу, которой раньше не было. '
         'Ответ только с первой половиной &mdash; это band 6. Ответ, который '
         'взвешивает обе, &mdash; то, чего ждёт Part 3.',
    t2bn='Назовите, кто теряет, кто выигрывает, и что важнее.',
    t2ch='Кто кого переобучает',
    t2cb='Второй аргумент &mdash; об ответственности. Должно ли государство '
         '<em>retrain the workforce</em> или работодатель, который её '
         '<em>replaced</em>? <em>A universal basic income</em> &mdash; выражение '
         'для ответа «ни то, ни другое».',
    t2cn='Одно сочетание на позицию и три позиции на выбор.',

    t3Eyebrow='Идея третья',
    t3Title='Города: плотность против простора, машина против автобуса',
    t3ah='Сочетания',
    t3ab='<em>Urban sprawl</em>, <em>affordable housing</em>, <em>public '
         'transport</em>, <em>green spaces</em>, <em>the cost of living</em>. '
         'Городские власти <em>invest in infrastructure</em> и стараются <em>ease '
         'congestion</em>; у жителя <em>a long commute</em>, и он терпит '
         '<em>overcrowding</em>.',
    t3an='Пробки <em>eased</em>. Движение <em>heavy</em>, никогда не '
         '<em>strong</em>.',
    t3bh='Плотность против простора',
    t3bb='Задание Task 2 обычно &mdash; вариант <em>should cities build up or '
         'out?</em> Строить вверх &mdash; значит <em>affordable housing</em> '
         'ближе к центру и меньше <em>urban sprawl</em> ценой '
         '<em>overcrowding</em>. Строить вширь &mdash; значит <em>green '
         'spaces</em> и <em>a long commute</em>.',
    t3bn='Оба ответа чего-то стоят. Скажите чего.',
    t3ch='Машина против автобуса',
    t3cb='Part 3 спрашивает, как <em>ease congestion</em>. Ответ человека, '
         'который уже думал об этом, говорит: город не может выстроить себе выход '
         'из пробок, потому что каждая новая дорога заполняется; поэтому деньги '
         'идут на <em>public transport</em>. Мысль несёт сочетание <em>invest in '
         'infrastructure</em>.',
    t3cn='<em>The cost of living</em> завершает любой из ответов: кто бы ни '
         'платил, платит житель.',

    mcaEyebrow='Задание 1 · Работа',
    mcaTitle='Какое сочетание и какое слово?',
    mcbEyebrow='Задание 2 · Автоматизация',
    mcbTitle='Существительное приводит свой глагол',
    mccEyebrow='Задание 3 · Города',
    mccTitle='Простое сочетание и есть точное',

    v1why='<em>Work remotely</em>. Наречие задано глаголом: <em>distantly</em> '
          '&mdash; это манера речи, а <em>at distance</em> и <em>from '
          'distance</em> собраны по словарю слово за словом.',
    v2why='<em>Job security</em>. <em>Work safety</em> &mdash; настоящий '
          'английский, но значит другое: каски и пожарные выходы, &mdash; в этом '
          'и промах по точности. Двух других сочетаний в английском нет.',
    v3why='<em>Suffer burnout</em>, как <em>suffer losses</em> или <em>suffer a '
          'setback</em>: существительное, обозначающее ущерб, берёт глагол '
          'ущерба. <em>Make</em>, <em>get into</em> и <em>fall in</em> хватают '
          'тогда, когда выражение выучено как одно слово.',
    v4why='<em>Improve career prospects</em>. <em>Trajectories</em>, '
          '<em>futures</em> и <em>chances</em> уходят дальше того '
          'существительного, которое использует английский, а <em>augment</em> и '
          '<em>amplify</em> &mdash; сопровождающие их почти верные глаголы. '
          'Простое сочетание и есть точное.',
    v5why='<em>Displace</em> &mdash; глагол для человека или рабочего места, '
          'вытесненных чем-то новым. <em>Dislocate</em> &mdash; это плечо, '
          '<em>misplace</em> &mdash; ключи, <em>evict</em> &mdash; жилец: три '
          'настоящих слова, каждое точное, но о другом.',
    v6why='<em>Productivity gains</em>. У производительности &mdash; '
          '<em>gain</em>, а не <em>profit</em>, <em>growth</em> или '
          '<em>winning</em>; существительное выбирает партнёра-существительное '
          'так же твёрдо, как и глагол.',
    v7why='<em>Retrain the workforce</em>. Остальные три &mdash; глаголы, '
          'которые учащийся собирает из <em>re-</em> и слова «учить». В '
          'английском глагол уже есть, и дополнение у него &mdash; <em>the '
          'workforce</em>.',
    v8why='<em>A universal basic income</em> &mdash; название политики, и '
          'экзаменатор слышит либо название, либо догадку. <em>Wage</em> и '
          '<em>salary</em> платят за работу, а это ровно то единственное, чем '
          'этот доход не является.',
    v9why='<em>Urban sprawl</em>, и только так. <em>Sprawl</em> несёт оценку '
          '&mdash; неупорядоченный и некрасивый рост, &mdash; поэтому аргументу '
          'нужно именно это слово, а не <em>spread</em>.',
    v10why='<em>Affordable housing</em> &mdash; термин, которым пользуются и '
           'градостроитель, и политик, и экзаменатор. <em>Economical</em> '
           'говорят о машине, <em>reasonable</em> &mdash; о человеке, а '
           '<em>cheap-priced</em> &mdash; не английский.',
    v11why='<em>Invest in</em>. Предлог &mdash; часть сочетания и идёт с глаголом, '
           'что бы ни следовало дальше: <em>invest in infrastructure</em>, '
           '<em>invest in public transport</em>, <em>invest in people</em>.',
    v12why='<em>A long commute</em>. Остальные три тянутся за более редким '
           'прилагательным и более редким существительным и промахиваются с '
           'обоими. Простое сочетание &mdash; то, которым пользуется любой '
           'носитель английского, и именно поэтому оно приносит баллы.',

    sortEyebrow='Задание 4 · Сочетание целиком',
    sortTitle='Распределите шесть сочетаний',
    sortHint='Перетащите каждое в столбец &mdash; или нажмите на него, а затем '
             'на нужный столбец.',
    sortBin1='Так говорят по-английски',
    sortBin2='Так по-английски не говорят',
    sortWhy='Существительное выбирает глагол и прилагательное. Пробки '
            '<em>eased</em>, персонал <em>taken on</em>, а <em>the gig '
            'economy</em> &mdash; устойчивое название. Пробки <em>heavy</em> или '
            '<em>severe</em>, движение <em>heavy</em>, жильё <em>affordable</em> '
            '&mdash; три варианта справа учащийся собирает по словарю, слово за '
            'словом. Учите выражение целиком, и ошибиться в выборе у вас просто '
            'не будет возможности.',

    actTitle='Отвечайте из запаса',
    actUse='Используйте хотя бы три:',
    actSpeakBrief='В парах. Один из вас &mdash; экзаменатор и задаёт вопросы Part 3 '
                  'о работе и городах: <em>is working from home good for a '
                  'company? Should cities build up or out? Who should pay to '
                  'retrain people?</em> Другой отвечает на каждый по минуте, '
                  'используя только запас из этого урока. Потом поменяйтесь.',
    actSpeak1='Каждый ответ сталкивает два сочетания &mdash; по одному на каждую '
              'сторону, с <em>but</em> или <em>whereas</em> между ними.',
    actSpeak2='Экзаменатор останавливает вас, как только вы используете отдельное '
              'слово там, где в запасе есть сочетание, и вы повторяете с '
              'выражением.',
    actSpeak3='Каждый третий вопрос &mdash; уточняющий: <em>why?</em> или <em>can '
              'you give an example?</em> &mdash; и в ответе должно появиться '
              'сочетание, которого вы ещё не использовали.',
    actWriteKind='Письмо · 150–200 слов',
    actWriteBrief='Выберите одну из трёх идей и напишите по ней абзац основной '
                  'части Task 2: тезис, аргумент, пример, уступка. Используйте не '
                  'меньше пяти сочетаний из запаса и подчеркните каждое. Потом '
                  'перечитайте и посчитайте: предложение без сочетания ничего не '
                  'делает для вашего Lexical Resource.',
    actPlaceholder='Automation displaces workers in low-skilled jobs, but…',
)


# ── Arabic ─────────────────────────────────────────────────────────────
T['ar'] = dict(
    coverTitle='Work, Automation <em>and Cities</em>',
    coverSub='ثلاثة موضوعات تتكرّر كثيرًا في Part 3 وTask 2، والتلازمات التي تجعل '
             'الإجابة عن أيٍّ منها تبدو مدروسة',
    chipLevel='C1 · متقدّم', chipFocus='Speaking وWriting Task 2',
    chipCount='18 نقطة',

    t1Eyebrow='الفكرة الأولى',
    t1Title='العمل: المرونة مقابل الأمان',
    t1ah='التلازمات',
    t1ab='الأسماء <em>job security</em> و<em>career prospects</em> و<em>a '
         'work&ndash;life balance</em> تأتي وشريكها ثابت. تقول <em>work '
         'remotely</em> بـ<em>a flexible schedule</em>، و<em>suffer burnout</em>، '
         'والشركة <em>takes on staff</em>. لا كلمة منها نادرة، فالتلازمات هي ما '
         'تقوله الإنجليزية.',
    t1an='تعلّم <em>suffer burnout</em> لا <em>burnout</em> وحدها.',
    t1bh='المرونة مقابل العزلة',
    t1bb='سؤال Part 3 يكاد يكون دائمًا صيغة من <em>is working from home good for '
         'people?</em> والإجابة التي تنال الدرجات تضع تلازمين في كفّتين: <em>a '
         'flexible schedule</em> في جهة، والزملاء الذين لم تعد تراهم في الجهة '
         'الأخرى.',
    t1bn='فكرة واحدة، وعبارتان، و<em>but</em> بينهما.',
    t1ch='الأمان مقابل الفرص',
    t1cb='وراء كثير من أسئلة Task 2 عن العمل <em>the gig economy</em>. اعرضه '
         'على أنه مقايضة: يمنح <em>a flexible schedule</em> ويسلب <em>job '
         'security</em>، ويوسّع <em>career prospects</em> لبعضهم ويضيّقها '
         'لآخرين.',
    t1cn='قل ماذا يعطي وماذا يأخذ. هذه هي الفقرة.',

    t2Eyebrow='الفكرة الثانية',
    t2Title='الأتمتة: وظائف تضيع مقابل وظائف تُخلق',
    t2ah='التلازمات',
    t2ab='<em>Automate routine tasks</em> و<em>replace workers</em> و<em>retrain '
         'the workforce</em>، ثم <em>productivity gains</em> و<em>low-skilled '
         'jobs</em> و<em>artificial intelligence</em>. الاسم يجلب فعله: المهام '
         '<em>automated</em>، والعمال <em>displaced</em>، والقوى العاملة '
         '<em>retrained</em>.',
    t2an='الفعل هو <em>automate</em> لا <em>automatise</em>.',
    t2bh='ما يضيع مقابل ما يُخلق',
    t2bb='كل سؤال عن الأتمتة هو المقايضة نفسها: الآلات <em>displace</em> العمال '
         'في <em>low-skilled jobs</em>، و<em>productivity gains</em> تموّل وظائف '
         'لم تكن موجودة من قبل. الإجابة التي تكتفي بالنصف الأول تساوي band 6، '
         'والتي توازن بين النصفين هي ما يطلبه Part 3.',
    t2bn='سمِّ من يخسر، وسمِّ من يكسب، وقل أيّهما أهم.',
    t2ch='من يعيد تأهيل من',
    t2cb='الحجّة الثانية عن المسؤولية. هل على الدولة أن <em>retrain the '
         'workforce</em>، أم على صاحب العمل الذي <em>replaced</em> العمال؟ '
         'وعبارة <em>a universal basic income</em> هي اسم الإجابة التي تقول: لا '
         'هذا ولا ذاك.',
    t2cn='تلازم واحد لكل موقف، وثلاثة مواقف تختار منها.',

    t3Eyebrow='الفكرة الثالثة',
    t3Title='المدن: الكثافة مقابل المساحة، والسيارة مقابل الحافلة',
    t3ah='التلازمات',
    t3ab='<em>Urban sprawl</em> و<em>affordable housing</em> و<em>public '
         'transport</em> و<em>green spaces</em> و<em>the cost of living</em>. '
         'البلدية <em>invests in infrastructure</em> وتحاول أن <em>ease '
         'congestion</em>، والساكن لديه <em>a long commute</em> ويتحمّل '
         '<em>overcrowding</em>.',
    t3an='الازدحام <em>eased</em>. والمرور <em>heavy</em>، لا <em>strong</em> '
         'أبدًا.',
    t3bh='الكثافة مقابل المساحة',
    t3bb='سؤال Task 2 يكون عادةً صيغة من <em>should cities build up or out?</em> '
         'البناء إلى الأعلى يعني <em>affordable housing</em> قرب المركز وقدرًا أقل '
         'من <em>urban sprawl</em>، بثمن هو <em>overcrowding</em>. والتوسّع إلى '
         'الخارج يعني <em>green spaces</em> و<em>a long commute</em>.',
    t3bn='كلتا الإجابتين لها ثمن. قل ما هو.',
    t3ch='السيارة مقابل الحافلة',
    t3cb='يسأل Part 3 كيف <em>ease congestion</em>. والإجابة التي فكّر صاحبها في '
         'الأمر من قبل تقول إن المدينة لا تستطيع أن تبني طريقها للخروج، لأن كل '
         'طريق جديد يمتلئ، لذا يذهب المال إلى <em>public transport</em>. '
         'والتلازم الذي يحمل الفكرة هو <em>invest in infrastructure</em>.',
    t3cn='عبارة <em>the cost of living</em> تختم أيًّا من الإجابتين: أيًّا كان '
         'من يدفع، فالساكن هو من يدفع.',

    mcaEyebrow='النشاط 1 · العمل',
    mcaTitle='أيّ تلازم، وأيّ كلمة؟',
    mcbEyebrow='النشاط 2 · الأتمتة',
    mcbTitle='الاسم يجلب فعله',
    mccEyebrow='النشاط 3 · المدن',
    mccTitle='التلازم البسيط هو الدقيق',

    v1why='الصحيح <em>work remotely</em>. الظرف يفرضه الفعل: <em>distantly</em> '
          'طريقة في الكلام، و<em>at distance</em> و<em>from distance</em> '
          'مبنيّتان كلمةً كلمةً من قاموس.',
    v2why='الصحيح <em>job security</em>. أما <em>work safety</em> فإنجليزية '
          'حقيقية لكنها تعني شيئًا آخر، الخوذ ومخارج الطوارئ، وهنا خطأ الدقة. '
          'والاثنتان الأخريان ليستا تلازمين في الإنجليزية.',
    v3why='الصحيح <em>suffer burnout</em>، مثل <em>suffer losses</em> و<em>suffer '
          'a setback</em>: اسم الضرر يأخذ فعل الضرر. أما <em>make</em> و<em>get '
          'into</em> و<em>fall in</em> فهي ما يمدّ إليه المتعلّم يده حين يتعلّم '
          'العبارة على أنها كلمة واحدة.',
    v4why='الصحيح <em>improve career prospects</em>. <em>Trajectories</em> '
          'و<em>futures</em> و<em>chances</em> كلها تتجاوز الاسم الذي تستخدمه '
          'الإنجليزية، و<em>augment</em> و<em>amplify</em> فعلان شبه صحيحين '
          'يرافقانها. التلازم البسيط هو الدقيق.',
    v5why='الفعل <em>displace</em> يُستخدم للشخص أو الوظيفة التي يزيحها شيء '
          'جديد. أما <em>dislocate</em> فللكتف، و<em>misplace</em> لمجموعة '
          'مفاتيح، و<em>evict</em> لمستأجر: ثلاث كلمات حقيقية، كلٌّ منها دقيق في '
          'شيء آخر.',
    v6why='الصحيح <em>productivity gains</em>. للإنتاجية <em>gain</em>، لا '
          '<em>profit</em> ولا <em>growth</em> ولا <em>winning</em>؛ فالاسم '
          'يختار الاسم الشريك بالحزم نفسه الذي يختار به الفعل.',
    v7why='الصحيح <em>retrain the workforce</em>. الثلاثة الأخرى فعل يبنيه '
          'المتعلّم من <em>re-</em> مع كلمة للتعليم. والإنجليزية لديها الفعل '
          'أصلًا، ومفعوله <em>the workforce</em>.',
    v8why='عبارة <em>a universal basic income</em> اسم السياسة نفسها، والممتحن '
          'يسمع إما الاسم وإما تخمينًا. أما <em>wage</em> و<em>salary</em> '
          'فيُدفعان مقابل عمل، وهذا بالضبط الشيء الوحيد الذي ليس عليه هذا الدخل.',
    v9why='الصحيح <em>urban sprawl</em> ولا شيء غيره. كلمة <em>sprawl</em> تحمل '
          'الحكم، أي نموًّا عشوائيًّا قبيحًا، ولهذا هي الكلمة التي تحتاجها الحجّة '
          'لا <em>spread</em>.',
    v10why='المصطلح <em>affordable housing</em> يستخدمه المخطّط والسياسي '
           'والممتحن جميعًا. <em>Economical</em> تُقال للسيارة، '
           'و<em>reasonable</em> للشخص، و<em>cheap-priced</em> ليست إنجليزية.',
    v11why='الصحيح <em>invest in</em>. حرف الجر جزء من التلازم ويرافق الفعل '
           'أيًّا كان ما يليه: <em>invest in infrastructure</em> و<em>invest in '
           'public transport</em> و<em>invest in people</em>.',
    v12why='الصحيح <em>a long commute</em>. الثلاثة الأخرى تمدّ يدها إلى صفة '
           'أندر واسم أندر وتخطئ في الاثنين. التلازم البسيط هو ما يستخدمه كل '
           'متحدّث بالإنجليزية، ولهذا بالضبط ينال الدرجة.',

    sortEyebrow='النشاط 4 · التلازم كاملًا',
    sortTitle='صنِّف التلازمات الستة',
    sortHint='اسحب كل تلازم إلى عمود، أو انقر عليه ثم على العمود الذي تريده.',
    sortBin1='هكذا تقول الإنجليزية',
    sortBin2='الإنجليزية لا تقول هذا',
    sortWhy='الاسم يختار الفعل والصفة. فالازدحام <em>eased</em>، والموظفون '
            '<em>taken on</em>، و<em>the gig economy</em> اسم ثابت. والازدحام '
            '<em>heavy</em> أو <em>severe</em>، والمرور <em>heavy</em>، والسكن '
            '<em>affordable</em>. أما الثلاثة في عمود «الإنجليزية لا تقول هذا» فهي '
            'ما يبنيه المتعلّم من قاموس كلمةً كلمة. تعلّم العبارة كاملة، فلا يبقى '
            'الاختيار بيدك لتخطئ فيه.',

    actTitle='أجب من الرصيد',
    actUse='استخدم ثلاثة منها على الأقل:',
    actSpeakBrief='اعملا في ثنائي. أحدكما الممتحن ويطرح أسئلة من Part 3 عن العمل '
                  'والمدن: <em>is working from home good for a company? Should '
                  'cities build up or out? Who should pay to retrain people?</em> '
                  'والآخر يجيب عن كل سؤال دقيقة كاملة مستخدمًا رصيد هذا الدرس '
                  'وحده. ثم تبادلا.',
    actSpeak1='كل إجابة تضع تلازمين في كفّتين، واحدًا لكل جهة، و<em>but</em> أو '
              '<em>whereas</em> بينهما.',
    actSpeak2='يوقفك الممتحن لحظة تستخدم كلمة مفردة حيث في الرصيد تلازم، فتقولها '
              'من جديد بالعبارة.',
    actSpeak3='كل ثالث سؤال سؤال متابعة، مثل <em>why?</em> أو <em>can you give an '
              'example?</em>، ويجب أن تضيف الإجابة تلازمًا لم تستخدمه بعد.',
    actWriteKind='الكتابة · 150–200 كلمة',
    actWriteBrief='اختر إحدى الأفكار الثلاث واكتب عنها فقرة من صلب مقال Task 2: '
                  'الادّعاء، والحجّة، ومثالًا، والتسليم. استخدم خمسة تلازمات على '
                  'الأقل من الرصيد وضع خطًّا تحت كل منها. ثم أعد قراءتها وعُدّ: '
                  'الجملة التي لا تلازم فيها لا تضيف شيئًا إلى Lexical Resource '
                  'لديك.',
    actPlaceholder='Automation displaces workers in low-skilled jobs, but…',
)


# ── Chinese ────────────────────────────────────────────────────────────
T['zh'] = dict(
    coverTitle='Work, Automation <em>and Cities</em>',
    coverSub='Part 3 和 Task 2 里反复出现的三个话题，以及让你在任何一个话题上的'
             '回答都显得深思熟虑的搭配',
    chipLevel='C1 · 高级', chipFocus='Speaking 与 Writing Task 2',
    chipCount='18 分',

    t1Eyebrow='观点一',
    t1Title='工作：灵活与稳定',
    t1ah='搭配',
    t1ab='<em>Job security</em>、<em>career prospects</em>、<em>a work&ndash;life '
         'balance</em>：这些名词带着固定的搭档一起出现。你 <em>work remotely</em>，'
         '有 <em>a flexible schedule</em>，你 <em>suffer burnout</em>，公司 '
         '<em>takes on staff</em>。这些词都不生僻，搭配本身就是英语的说法。',
    t1an='记 <em>suffer burnout</em>，而不是 <em>burnout</em>。',
    t1bh='灵活与孤立',
    t1bb='Part 3 的问题几乎总是 <em>is working from home good for people?</em> '
         '的某种变体。得分的回答把两个搭配放在一起对照：一边是 <em>a flexible '
         'schedule</em>，另一边是你再也见不到的同事。',
    t1bn='一个观点，两个短语，中间一个 <em>but</em>。',
    t1ch='稳定与机会',
    t1cb='很多关于工作的 Task 2 题目背后都是 <em>the gig economy</em>。把它当作一'
         '种交换来论证：它给了你 <em>a flexible schedule</em>，拿走了 <em>job '
         'security</em>；它拓宽了一些人的 <em>career prospects</em>，又收窄了另'
         '一些人的。',
    t1cn='说出它给了什么、拿走了什么，这就是一段。',

    t2Eyebrow='观点二',
    t2Title='自动化：失去的岗位与新增的岗位',
    t2ah='搭配',
    t2ab='<em>Automate routine tasks</em>、<em>replace workers</em>、<em>retrain '
         'the workforce</em>；<em>productivity gains</em>、<em>low-skilled '
         'jobs</em>、<em>artificial intelligence</em>。名词自带动词：任务被 '
         '<em>automated</em>，工人被 <em>displaced</em>，劳动力被 '
         '<em>retrained</em>。',
    t2an='动词是 <em>automate</em>，不是 <em>automatise</em>。',
    t2bh='失去与新增',
    t2bb='每道自动化题目都是同一种交换：机器 <em>displace</em> 了 <em>low-skilled '
         'jobs</em> 里的工人，而 <em>productivity gains</em> 又养活了以前不存在的'
         '工作。只写了前一半的回答是 band 6。把两边都权衡到的回答，才是 Part 3 '
         '想要的。',
    t2bn='说出谁受损、谁受益，再说哪个更重要。',
    t2ch='谁来培训谁',
    t2cb='第二个论点关于责任。该由国家 <em>retrain the workforce</em>，还是由 '
         '<em>replaced</em> 了这些工人的雇主来做？<em>A universal basic '
         'income</em> 则是“两者都不”这个回答的说法。',
    t2cn='每种立场配一个搭配，有三种立场可选。',

    t3Eyebrow='观点三',
    t3Title='城市：密度与空间，汽车与公交',
    t3ah='搭配',
    t3ab='<em>Urban sprawl</em>、<em>affordable housing</em>、<em>public '
         'transport</em>、<em>green spaces</em>、<em>the cost of living</em>。市'
         '政府 <em>invests in infrastructure</em>，努力 <em>ease congestion</em>；'
         '居民有 <em>a long commute</em>，还要忍受 <em>overcrowding</em>。',
    t3an='拥堵用 <em>eased</em>。车流是 <em>heavy</em>，从来不是 '
         '<em>strong</em>。',
    t3bh='密度与空间',
    t3bb='Task 2 的题目通常是 <em>should cities build up or out?</em> 的某种说法。'
         '往高处建，意味着市中心附近有 <em>affordable housing</em>、更少的 '
         '<em>urban sprawl</em>，代价是 <em>overcrowding</em>。往外扩，意味着 '
         '<em>green spaces</em> 和 <em>a long commute</em>。',
    t3bn='两种回答都有代价。说出是什么。',
    t3ch='汽车与公交',
    t3cb='Part 3 会问怎样 <em>ease congestion</em>。想过这个问题的人会说：城市不'
         '能靠修路摆脱拥堵，因为每条新路都会被填满；所以钱应该投向 <em>public '
         'transport</em>。承载这个观点的搭配是 <em>invest in '
         'infrastructure</em>。',
    t3cn='<em>The cost of living</em> 可以为任何一种回答收尾：不管谁出钱，最终买'
         '单的都是居民。',

    mcaEyebrow='练习 1 · 工作',
    mcaTitle='哪个搭配，哪个词？',
    mcbEyebrow='练习 2 · 自动化',
    mcbTitle='名词自带动词',
    mccEyebrow='练习 3 · 城市',
    mccTitle='朴素的搭配才是准确的搭配',

    v1why='<em>Work remotely</em>。副词由动词决定：<em>distantly</em> 是一种说话'
          '方式，<em>at distance</em> 和 <em>from distance</em> 则是照着词典一个'
          '词一个词拼出来的。',
    v2why='<em>Job security</em>。<em>Work safety</em> 是真实的英语，但意思不同——'
          '指安全帽和紧急出口——这就是用词不准的失误。另外两个在英语里根本不是'
          '搭配。',
    v3why='<em>Suffer burnout</em>，就像 <em>suffer losses</em> 或 <em>suffer a '
          'setback</em>：表示损害的名词要配表示遭受的动词。<em>Make</em>、'
          '<em>get into</em> 和 <em>fall in</em> 是把这个短语当成一个词来学的人'
          '顺手抓来的。',
    v4why='<em>Improve career prospects</em>。<em>Trajectories</em>、'
          '<em>futures</em> 和 <em>chances</em> 都偏离了英语实际用的那个名词，'
          '<em>augment</em> 和 <em>amplify</em> 是跟着它们的差一点的动词。朴素的'
          '搭配才是准确的搭配。',
    v5why='<em>Displace</em> 用于被新事物挤走的人或岗位。<em>Dislocate</em> 说的'
          '是肩膀，<em>misplace</em> 说的是一串钥匙，<em>evict</em> 说的是房客——'
          '三个真实的词，各自准确地说着别的事。',
    v6why='<em>Productivity gains</em>。生产率用 <em>gain</em>，不用 '
          '<em>profit</em>、<em>growth</em> 或 <em>winning</em>；名词选搭档名词，'
          '和选动词一样坚定。',
    v7why='<em>Retrain the workforce</em>。另外三个是学习者用 <em>re-</em> 加一个'
          '表示“教”的词拼出来的动词。英语本来就有这个动词，宾语就是 <em>the '
          'workforce</em>。',
    v8why='<em>A universal basic income</em> 是这项政策的名称，考官听到的要么是'
          '名称，要么是猜测。<em>Wage</em> 和 <em>salary</em> 是为工作支付的报'
          '酬，而这恰恰是这笔收入唯一不是的东西。',
    v9why='<em>Urban sprawl</em>，只能是它。<em>Sprawl</em> 本身带着评判——无计划'
          '又难看的扩张——所以论证需要的是这个词，而不是 <em>spread</em>。',
    v10why='<em>Affordable housing</em> 是规划师、政客和考官都用的说法。'
           '<em>Economical</em> 说的是汽车，<em>reasonable</em> 说的是人，'
           '<em>cheap-priced</em> 则不是英语。',
    v11why='<em>Invest in</em>。介词是搭配的一部分，后面接什么都跟着动词走：'
           '<em>invest in infrastructure</em>、<em>invest in public '
           'transport</em>、<em>invest in people</em>。',
    v12why='<em>A long commute</em>。另外三个去够更生僻的形容词和更生僻的名词，'
           '结果两样都没用对。朴素的搭配是每个说英语的人都在用的，也正因为这样'
           '才能得分。',

    sortEyebrow='练习 4 · 完整的搭配',
    sortTitle='给这六个搭配分类',
    sortHint='把每一项拖到一栏里——或者先点一项，再点你想放进的那一栏。',
    sortBin1='英语这样说',
    sortBin2='英语不这样说',
    sortWhy='名词决定动词和形容词。拥堵用 <em>eased</em>，员工用 <em>taken '
            'on</em>，<em>the gig economy</em> 是固定名称。拥堵是 <em>heavy</em> '
            '或 <em>severe</em>，车流是 <em>heavy</em>，住房是 '
            '<em>affordable</em>——右栏那三个，是学习者照着词典一个词一个词拼出来'
            '的。把短语整体记住，就根本轮不到你选错。',

    actTitle='从词库里作答',
    actUse='至少用上三个：',
    actSpeakBrief='两人一组。一人当考官，问关于工作和城市的 Part 3 问题——'
                  '<em>is working from home good for a company? Should cities '
                  'build up or out? Who should pay to retrain people?</em> 另一人'
                  '每题回答一分钟，只能用本课的词库。然后交换。',
    actSpeak1='每个回答都要把两个搭配对照起来——每边一个，中间用 <em>but</em> 或 '
              '<em>whereas</em>。',
    actSpeak2='只要你在词库有搭配的地方用了孤立的单词，考官就立刻打断，你要用那个'
              '短语重说。',
    actSpeak3='每三个问题里有一个是追问——<em>why?</em> 或 <em>can you give an '
              'example?</em>——回答必须加上一个你还没用过的搭配。',
    actWriteKind='写作 · 150–200 词',
    actWriteBrief='从三个观点中选一个，写一段 Task 2 的主体段：观点、论证、例子、'
                  '让步。至少用上词库里的五个搭配，并给每一个画线。然后回头数一'
                  '数：没有搭配的句子，对你的 Lexical Resource 毫无贡献。',
    actPlaceholder='Automation displaces workers in low-skilled jobs, but…',
)


# ── Japanese ───────────────────────────────────────────────────────────
T['ja'] = dict(
    coverTitle='Work, Automation <em>and Cities</em>',
    coverSub='Part 3 と Task 2 に何度も出てくる三つのテーマと、どれについての答え'
             'もよく考えられたものに聞こえさせる組み合わせ',
    chipLevel='C1 · 上級', chipFocus='Speaking・Writing Task 2',
    chipCount='18 点',

    t1Eyebrow='アイデア 1',
    t1Title='仕事：柔軟さ対安定',
    t1ah='組み合わせ',
    t1ab='<em>Job security</em>、<em>career prospects</em>、<em>a work&ndash;life '
         'balance</em>：相手が決まった状態でやって来る名詞です。<em>a flexible '
         'schedule</em> で <em>work remotely</em> し、<em>suffer burnout</em> し、'
         '会社は <em>takes on staff</em> します。どの語も難しくありません。組み合'
         'わせこそが英語の言い方です。',
    t1an='<em>burnout</em> ではなく <em>suffer burnout</em> を覚えましょう。',
    t1bh='柔軟さ対孤立',
    t1bb='Part 3 の質問は、ほぼいつも <em>is working from home good for '
         'people?</em> の変形です。点になる答えは二つの組み合わせを突き合わせま'
         'す。一方に <em>a flexible schedule</em>、もう一方にもう会わなくなった同'
         '僚たち。',
    t1bn='一つのアイデアに二つのフレーズ、その間に <em>but</em>。',
    t1ch='安定対チャンス',
    t1cb='仕事についての Task 2 の問題の多くには <em>the gig economy</em> があり'
         'ます。取引として論じましょう。<em>a flexible schedule</em> を与え、'
         '<em>job security</em> を奪う。ある人の <em>career prospects</em> を広げ、'
         '別の人のそれを狭める。',
    t1cn='何を与え、何を奪うかを言う。それが段落です。',

    t2Eyebrow='アイデア 2',
    t2Title='自動化：失われる仕事対生まれる仕事',
    t2ah='組み合わせ',
    t2ab='<em>Automate routine tasks</em>、<em>replace workers</em>、<em>retrain '
         'the workforce</em>；<em>productivity gains</em>、<em>low-skilled '
         'jobs</em>、<em>artificial intelligence</em>。名詞が動詞を連れてきま'
         'す。作業は <em>automated</em>、労働者は <em>displaced</em>、労働力は '
         '<em>retrained</em> されます。',
    t2an='動詞は <em>automatise</em> ではなく <em>automate</em> です。',
    t2bh='失われる対生まれる',
    t2bb='自動化の問題はどれも同じ取引です。機械は <em>low-skilled jobs</em> の労'
         '働者を <em>displace</em> し、<em>productivity gains</em> が以前はなかった'
         '仕事の財源になります。前半だけの答えは band 6。両方を天秤にかける答えこ'
         'そ、Part 3 が求めているものです。',
    t2bn='誰が失い、誰が得るかを言い、どちらが重要かを言いましょう。',
    t2ch='誰が誰を再訓練するか',
    t2cb='二つ目の議論は責任についてです。<em>retrain the workforce</em> すべきな'
         'のは国か、それとも労働者を <em>replaced</em> した雇用主か。<em>A '
         'universal basic income</em> は、どちらでもないと答えるための言葉です。',
    t2cn='立場ごとに組み合わせが一つ、選べる立場は三つ。',

    t3Eyebrow='アイデア 3',
    t3Title='都市：密度対空間、車対バス',
    t3ah='組み合わせ',
    t3ab='<em>Urban sprawl</em>、<em>affordable housing</em>、<em>public '
         'transport</em>、<em>green spaces</em>、<em>the cost of living</em>。'
         '自治体は <em>invests in infrastructure</em> して <em>ease '
         'congestion</em> しようとし、住民は <em>a long commute</em> を抱え、'
         '<em>overcrowding</em> に耐えます。',
    t3an='渋滞は <em>eased</em>。交通量は <em>heavy</em> で、決して '
         '<em>strong</em> ではありません。',
    t3bh='密度対空間',
    t3bb='Task 2 の問題は、たいてい <em>should cities build up or out?</em> の一'
         '種です。上に伸ばせば、中心部の近くに <em>affordable housing</em> ができ、'
         '<em>urban sprawl</em> は減りますが、代償は <em>overcrowding</em> です。'
         '外に広げれば、<em>green spaces</em> と <em>a long commute</em> です。',
    t3bn='どちらの答えにも代償があります。それが何かを言いましょう。',
    t3ch='車対バス',
    t3cb='Part 3 は <em>ease congestion</em> する方法を尋ねます。前に考えたことの'
         'ある人の答えは、新しい道路はどれも埋まってしまうので、都市は道路を造っ'
         'て抜け出すことはできない、だからお金は <em>public transport</em> に回す、'
         'と言います。要点を運ぶ組み合わせは <em>invest in infrastructure</em> '
         'です。',
    t3cn='<em>The cost of living</em> でどちらの答えも締めくくれます。誰が払うにせ'
         'よ、結局払うのは住民です。',

    mcaEyebrow='演習 1 · 仕事',
    mcaTitle='どの組み合わせで、どの語か？',
    mcbEyebrow='演習 2 · 自動化',
    mcbTitle='名詞が動詞を連れてくる',
    mccEyebrow='演習 3 · 都市',
    mccTitle='平易な組み合わせこそ正確',

    v1why='<em>Work remotely</em>。副詞は動詞で決まります。<em>distantly</em> は話'
          'し方の様子で、<em>at distance</em> と <em>from distance</em> は辞書か'
          'ら一語ずつ組み立てたものです。',
    v2why='<em>Job security</em>。<em>Work safety</em> は実在する英語ですが意味が'
          '違います――ヘルメットや非常口のことで、ここが正確さの落とし穴です。ほか'
          'の二つは英語にある組み合わせではありません。',
    v3why='<em>Suffer burnout</em>。<em>suffer losses</em> や <em>suffer a '
          'setback</em> と同じで、損害を表す名詞は損害の動詞をとります。'
          '<em>Make</em>、<em>get into</em>、<em>fall in</em> は、表現を一語とし'
          'て覚えたときに手を伸ばしてしまう語です。',
    v4why='<em>Improve career prospects</em>。<em>Trajectories</em>、'
          '<em>futures</em>、<em>chances</em> はどれも英語が使う名詞から外れ、'
          '<em>augment</em> と <em>amplify</em> はそれに添えられた惜しい動詞です。'
          '平易な組み合わせこそ正確です。',
    v5why='<em>Displace</em> は、新しいものに押し出される人や仕事に使う動詞で'
          'す。<em>dislocate</em> は肩、<em>misplace</em> は鍵の束、<em>evict</em> '
          'は借家人――三つとも実在する語ですが、それぞれ別のことに正確なのです。',
    v6why='<em>Productivity gains</em>。生産性がとるのは <em>gain</em> で、'
          '<em>profit</em>、<em>growth</em>、<em>winning</em> ではありません。名'
          '詞は動詞を選ぶのと同じくらいはっきりと、相手の名詞を選びます。',
    v7why='<em>Retrain the workforce</em>。ほかの三つは、学習者が <em>re-</em> と'
          '「教える」を表す語で組み立てた動詞です。英語にはすでにその動詞があり、'
          '<em>the workforce</em> を目的語にとります。',
    v8why='<em>A universal basic income</em> は政策の名前で、試験官に聞こえるのは'
          '名前か当て推量かのどちらかです。<em>wage</em> と <em>salary</em> は労働'
          'の対価として払われるもので、これはまさにこの収入が唯一そうでないもの'
          'です。',
    v9why='<em>Urban sprawl</em>、これだけです。<em>Sprawl</em> には評価が含まれ'
          'ています――無計画で見苦しい広がり――だから議論に必要なのはこの語で、'
          '<em>spread</em> ではありません。',
    v10why='<em>Affordable housing</em> は都市計画家も政治家も試験官も使う言葉で'
           'す。<em>economical</em> は車、<em>reasonable</em> は人に使い、'
           '<em>cheap-priced</em> は英語ではありません。',
    v11why='<em>Invest in</em>。前置詞は組み合わせの一部で、後に何が続いても動詞'
           'と一緒に移動します：<em>invest in infrastructure</em>、<em>invest in '
           'public transport</em>、<em>invest in people</em>。',
    v12why='<em>A long commute</em>。ほかの三つは、より珍しい形容詞と名詞に手を伸'
           'ばし、どちらも外しています。平易な組み合わせは英語話者なら誰でも使う'
           'もので、だからこそ点になります。',

    sortEyebrow='演習 4 · 組み合わせを丸ごと',
    sortTitle='六つの組み合わせを分類しましょう',
    sortHint='それぞれを列にドラッグしてください。または項目をクリックしてから、'
             '入れたい列をクリックします。',
    sortBin1='英語ではこう言う',
    sortBin2='英語ではこう言わない',
    sortWhy='名詞が動詞と形容詞を選びます。渋滞は <em>eased</em>、スタッフは '
            '<em>taken on</em>、<em>the gig economy</em> は決まった呼び名です。渋'
            '滞は <em>heavy</em> か <em>severe</em>、交通量は <em>heavy</em>、住宅'
            'は <em>affordable</em>――右の三つは、学習者が辞書から一語ずつ組み立て'
            'たものです。表現を丸ごと覚えれば、選び間違える余地はそもそもありま'
            'せん。',

    actTitle='語彙集から答える',
    actUse='少なくとも三つ使いましょう：',
    actSpeakBrief='ペアで。一人が試験官になり、仕事と都市について Part 3 の質問を'
                  'します――<em>is working from home good for a company? Should '
                  'cities build up or out? Who should pay to retrain people?</em> '
                  'もう一人は、このレッスンの語彙集だけを使って、それぞれに一分ず'
                  'つ答えます。そのあと交代しましょう。',
    actSpeak1='どの答えも二つの組み合わせを突き合わせること――それぞれの側に一つず'
              'つ、間に <em>but</em> か <em>whereas</em>。',
    actSpeak2='語彙集に組み合わせがあるところで単語だけを使ったら、試験官はすぐに止'
              'め、あなたはフレーズで言い直します。',
    actSpeak3='三問に一問はフォローアップ――<em>why?</em> または <em>can you give '
              'an example?</em>――で、答えにはまだ使っていない組み合わせを一つ加えな'
              'ければなりません。',
    actWriteKind='ライティング · 150–200 語',
    actWriteBrief='三つのアイデアから一つ選び、Task 2 の本論の段落を書きましょう：'
                  '主張、根拠、例、譲歩。語彙集の組み合わせを少なくとも五つ使い、'
                  'それぞれに下線を引きます。そのあと読み返して数えましょう。組み'
                  '合わせのない文は、あなたの Lexical Resource に何の貢献もしてい'
                  'ません。',
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
