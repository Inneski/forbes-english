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
    t1ab='<em>Job security</em>, <em>career prospects</em>, '
         '<em>work&ndash;life balance</em>: phrases whose words come as a '
         'set. You <em>work remotely</em> or <em>work from home</em>, people '
         '<em>suffer from burnout</em>, a firm <em>takes on staff</em>. None '
         'of these words is rare; what an examiner notices is whether they '
         'come in the right pairs.',
    t1an='Learn the whole phrase, <em>suffer from burnout</em>, not just the '
         'noun <em>burnout</em>.',
    t1bh='Flexibility against isolation',
    t1bb='A common Part 3 question is some form of <em>is working from home '
         'good for people?</em> A strong answer weighs the two sides against '
         'each other: <em>a flexible schedule</em> on one, the colleagues '
         'you no longer see on the other.',
    t1bn='One idea, two phrases, and <em>but</em> between them.',
    t1ch='Security against opportunity',
    t1cb='When a Task 2 question asks how work is changing, <em>the gig '
         'economy</em> is an obvious example. Argue it as a trade: it offers '
         '<em>a flexible schedule</em> and takes away <em>job security</em>; '
         'it widens <em>career prospects</em> for some and narrows them for '
         'others.',
    t1cn='Say what it gives and what it takes. That is the paragraph.',

    t2Eyebrow='Idea two',
    t2Title='Automation: jobs lost against jobs created',
    t2ah='The pairings',
    t2ab='<em>Automate routine tasks</em>, <em>replace workers</em>, '
         '<em>retrain the workforce</em>; <em>productivity gains</em>, '
         '<em>low-skilled jobs</em>, <em>artificial intelligence</em>. The '
         'noun brings its verb: tasks are <em>automated</em>, workers are '
         '<em>displaced</em>, a workforce is <em>retrained</em>.',
    t2an='<em>Automate</em> is the verb everyone uses. <em>Automatise</em> '
         'is in the dictionary, but it is rare enough to sound like a '
         'translation.',
    t2bh='Lost against created',
    t2bb='Most automation questions come down to one trade: machines '
         '<em>displace</em> workers in <em>low-skilled jobs</em>, and the '
         '<em>productivity gains</em> can pay for jobs that did not exist '
         'before. Weigh both halves. A one-sided answer soon runs out of '
         'things to say; a balanced one keeps going, and gives you a reason '
         'to use <em>whereas</em> and <em>on the other hand</em>.',
    t2bn='Name who loses, name who gains, and say which matters more.',
    t2ch='Who retrains whom',
    t2cb='The second argument is about responsibility. Should the state '
         '<em>retrain the workforce</em>, or the employer that '
         '<em>replaced</em> it? <em>A universal basic income</em> names a '
         'third answer: pay everyone a regular sum.',
    t2cn='One pairing per position, and three positions to choose from.',

    t3Eyebrow='Idea three',
    t3Title='Cities: density against space, the car against the bus',
    t3ah='The pairings',
    t3ab='<em>Urban sprawl</em>, <em>affordable housing</em>, <em>public '
         'transport</em>, <em>green spaces</em>, <em>the cost of living</em>. '
         'A council <em>invests in infrastructure</em> and tries to <em>ease '
         'congestion</em>; a resident has <em>a long commute</em> and puts '
         'up with <em>overcrowding</em>.',
    t3an='You <em>ease</em> or <em>reduce</em> congestion. Traffic is '
         '<em>heavy</em>, not <em>strong</em>.',
    t3bh='Density against space',
    t3bb='A typical Task 2 question on cities is some version of <em>should '
         'cities build up or out?</em> Building up can put <em>affordable '
         'housing</em> near the centre and limit <em>urban sprawl</em>, at '
         'the risk of <em>overcrowding</em>. Building out gives people more '
         'room, at the cost of <em>green spaces</em> and <em>a long '
         'commute</em>.',
    t3bn='Both answers cost something. Say what.',
    t3ch='The car against the bus',
    t3cb='Part 3 may ask how to <em>ease congestion</em>. One well-known '
         'argument is that a city cannot build its way out, because new '
         'roads soon fill with new traffic, so the money should go to '
         '<em>public transport</em>. <em>Invest in public transport</em> '
         'makes that point; <em>invest in infrastructure</em> is the wider '
         'term.',
    t3cn='Either answer can end on <em>the cost of living</em>: ask who pays '
         'in the end.',

    mcaEyebrow='Activity 1 · Work',
    mcaTitle='Which pairing, and which word?',
    mcbEyebrow='Activity 2 · Automation',
    mcbTitle='The noun brings its verb',
    mccEyebrow='Activity 3 · Cities',
    mccTitle='The plain pairing is the precise one',

    v1why='<em>Work remotely</em>, or <em>work from home</em>. '
          '<em>Distantly</em> describes a manner or a family tie &mdash; '
          '<em>smiled distantly</em>, <em>distantly related</em> &mdash; not '
          'a way of working. <em>At a distance</em> and <em>from a '
          'distance</em> are about how far away something is, and without '
          'the <em>a</em> they are not English at all.',
    v2why='<em>Job security</em>. <em>Work safety</em> is real English and '
          'means something else &mdash; helmets and fire exits &mdash; which '
          'is the precision miss. The other two are not pairings English has.',
    v3why='<em>Suffer from burnout</em>, as you <em>suffer from stress</em> '
          'or <em>suffer from insomnia</em>: an illness or a condition '
          'usually takes <em>suffer from</em>. <em>Get into</em>, <em>fall '
          'in</em> and <em>make</em> are what a learner reaches for when the '
          'noun was learnt without its verb. English also has a verb of its '
          'own: nurses <em>burn out</em>.',
    v4why='<em>Improve career prospects</em>. <em>Career trajectory</em> is '
          'real English, but nothing <em>augments</em> one; <em>enlarge a '
          'career future</em> and <em>amplify a career chance</em> are built '
          'one word at a time, and English does not say them. The plain '
          'pairing is the precise one.',
    v5why='<em>Displace</em> is the verb for workers pushed out of their '
          'jobs by something new. <em>Deport</em> is a person sent out of a '
          'country, <em>misplace</em> is a set of keys, <em>evict</em> is a '
          'tenant &mdash; three real words, each precise about something '
          'else.',
    v6why='<em>Productivity gains</em>, or <em>productivity growth</em>. '
          '<em>Profits</em>, <em>earnings</em> and <em>winnings</em> are '
          'money someone receives, and productivity is not money: it is how '
          'much is produced for the work put in.',
    v7why='<em>Retrain the workforce</em>: give workers new skills. '
          '<em>Reteach</em> means teach a lesson again, <em>re-form</em> '
          'means form again, and <em>re-school</em> is not a verb English '
          'uses.',
    v8why='<em>A universal basic income</em> is the name of the policy, and '
          'anything else sounds like a guess. A <em>wage</em> and a '
          '<em>salary</em> are paid for work, which this is not, and '
          '<em>payment</em> is too general to be the name of anything.',
    v9why='<em>Urban sprawl</em> is the fixed term, and it carries a '
          'judgement: growth that is unplanned and swallows land. '
          '<em>Spreading</em>, <em>stretch</em> and <em>widening</em> '
          'describe the movement, but English does not pair any of them with '
          '<em>urban</em> to name it.',
    v10why='<em>Affordable housing</em> is the standard term, used by '
           'planners, politicians and newspapers alike. <em>Economical</em> '
           'describes something cheap to run, like a car; '
           '<em>reasonable</em> goes with a price or a rent, not with '
           'housing; and <em>cheap-priced</em> is not English.',
    v11why='<em>Invest in</em>: money is invested <em>in</em> something '
           '&mdash; <em>in infrastructure</em>, <em>in public '
           'transport</em>, <em>in people</em>. <em>On</em>, <em>to</em> and '
           '<em>at</em> are common learner errors, and none of them goes '
           'with <em>invest</em>.',
    v12why='<em>A long commute</em>. The other three reach for a rarer '
           'adjective and a rarer noun and miss on both: English does not '
           'call the trip to work a <em>transit</em>, a <em>journeying</em> '
           'or a <em>travelling</em>. The plain pairing is the one English '
           'speakers actually use.',

    sortEyebrow='Activity 4 · The pairing, whole',
    sortTitle='Sort the six pairings',
    sortHint='Drag each one into a column &mdash; or click an item, then the '
             'column you want it in.',
    sortBin1='Natural English',
    sortBin2='Not natural',
    sortWhy='The noun chooses its verb and its adjective. Congestion is '
            '<em>eased</em>, staff are <em>taken on</em>, and <em>the gig '
            'economy</em> is a fixed name. Congestion is <em>heavy</em> or '
            '<em>severe</em>, not <em>big</em>; traffic is <em>heavy</em>, '
            'not <em>strong</em>; housing is <em>affordable</em> or '
            '<em>cheap</em>, not <em>cheap-priced</em>. Those three are what '
            'a learner builds from a dictionary, one word at a time. Learn '
            'the phrase whole and you never have to build it.',

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
                  'underline each one. Then read it back: a sentence with no '
                  'precise pairing in it is a missed chance to show range.',
    actPlaceholder='Automation displaces workers in low-skilled jobs, but…',
)

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Arbeit, Automatisierung <em>und Städte</em>',
    coverSub='Drei Themen, die in Teil 3 und in Task 2 immer wieder kommen '
             '&mdash; und die Wortverbindungen, mit denen eine Antwort zu jedem '
             'davon durchdacht klingt',
    chipLevel='C1 · Fortgeschritten', chipFocus='Speaking &amp; Writing Task 2',
    chipCount='18 Punkte',

    t1Eyebrow='Idee eins',
    t1Title='Arbeit: Flexibilität gegen Sicherheit',
    t1ah='Die Wortverbindungen',
    t1ab='<em>Job security</em>, <em>career prospects</em>, '
         '<em>work&ndash;life balance</em>: Wendungen, deren Wörter im Paket '
         'kommen. Man <em>works remotely</em> oder <em>works from home</em>, '
         'Menschen <em>suffer from burnout</em>, eine Firma <em>takes on '
         'staff</em>. Keines dieser Wörter ist selten; der Prüfer achtet '
         'darauf, ob sie in den richtigen Verbindungen kommen.',
    t1an='Lern die ganze Wendung, <em>suffer from burnout</em>, nicht nur '
         'das Substantiv <em>burnout</em>.',
    t1bh='Flexibilität gegen Isolation',
    t1bb='Eine häufige Frage in Teil 3 ist eine Form von <em>is working from '
         'home good for people?</em> Eine starke Antwort wägt die beiden '
         'Seiten gegeneinander ab: <em>a flexible schedule</em> auf der '
         'einen, die Kollegen, die man nicht mehr sieht, auf der anderen.',
    t1bn='Eine Idee, zwei Phrasen, und <em>but</em> dazwischen.',
    t1ch='Sicherheit gegen Chance',
    t1cb='Wenn eine Task-2-Frage wissen will, wie sich die Arbeit verändert, '
         'ist <em>the gig economy</em> ein naheliegendes Beispiel. '
         'Argumentiere mit einem Tausch: Sie bietet <em>a flexible '
         'schedule</em> und nimmt <em>job security</em>; sie erweitert für '
         'manche die <em>career prospects</em> und verengt sie für andere.',
    t1cn='Sag, was sie gibt und was sie nimmt. Das ist der Absatz.',

    t2Eyebrow='Idee zwei',
    t2Title='Automatisierung: verlorene gegen neue Jobs',
    t2ah='Die Wortverbindungen',
    t2ab='<em>Automate routine tasks</em>, <em>replace workers</em>, '
         '<em>retrain the workforce</em>; <em>productivity gains</em>, '
         '<em>low-skilled jobs</em>, <em>artificial intelligence</em>. Das '
         'Substantiv bringt sein Verb mit: Aufgaben werden <em>automated</em>, '
         'Arbeiter werden <em>displaced</em>, eine Belegschaft wird '
         '<em>retrained</em>.',
    t2an='<em>Automate</em> ist das Verb, das alle benutzen. '
         '<em>Automatise</em> steht im Wörterbuch, ist aber so selten, dass '
         'es nach Übersetzung klingt.',
    t2bh='Verloren gegen geschaffen',
    t2bb='Die meisten Fragen zur Automatisierung laufen auf denselben Tausch '
         'hinaus: Maschinen <em>displace</em> Arbeitskräfte in '
         '<em>low-skilled jobs</em>, und die <em>productivity gains</em> '
         'können Stellen finanzieren, die es vorher nicht gab. Wäge beide '
         'Hälften ab. Einer einseitigen Antwort geht bald der Stoff aus; '
         'eine ausgewogene trägt weiter und gibt dir Anlass, '
         '<em>whereas</em> und <em>on the other hand</em> zu benutzen.',
    t2bn='Nenn, wer verliert, nenn, wer gewinnt, und sag, was schwerer wiegt.',
    t2ch='Wer schult wen um',
    t2cb='Das zweite Argument handelt von Verantwortung. Soll der Staat '
         '<em>retrain the workforce</em> oder der Arbeitgeber, der die Leute '
         '<em>replaced</em> hat? <em>A universal basic income</em> benennt '
         'eine dritte Antwort: stattdessen allen regelmäßig einen Betrag '
         'zahlen.',
    t2cn='Eine Wortverbindung pro Position, und drei Positionen zur Auswahl.',

    t3Eyebrow='Idee drei',
    t3Title='Städte: Dichte gegen Raum, das Auto gegen den Bus',
    t3ah='Die Wortverbindungen',
    t3ab='<em>Urban sprawl</em>, <em>affordable housing</em>, <em>public '
         'transport</em>, <em>green spaces</em>, <em>the cost of living</em>. '
         'Eine Stadtverwaltung <em>invests in infrastructure</em> und '
         'versucht, <em>ease congestion</em>; ein Bewohner hat <em>a long '
         'commute</em> und erträgt <em>overcrowding</em>.',
    t3an='Stau kann man <em>ease</em> oder <em>reduce</em>. Verkehr ist '
         '<em>heavy</em>, nicht <em>strong</em>.',
    t3bh='Dichte gegen Raum',
    t3bb='Eine typische Task-2-Frage zu Städten ist eine Version von '
         '<em>should cities build up or out?</em> In die Höhe zu bauen kann '
         '<em>affordable housing</em> nahe am Zentrum schaffen und <em>urban '
         'sprawl</em> begrenzen, mit dem Risiko von <em>overcrowding</em>. '
         'In die Breite zu bauen gibt den Menschen mehr Platz, auf Kosten '
         'von <em>green spaces</em> und mit <em>a long commute</em>.',
    t3bn='Beide Antworten kosten etwas. Sag, was.',
    t3ch='Das Auto gegen den Bus',
    t3cb='Teil 3 fragt vielleicht, wie man <em>ease congestion</em> kann. '
         'Ein bekanntes Argument lautet: Eine Stadt kann sich nicht aus dem '
         'Stau herausbauen, weil sich neue Straßen bald mit neuem Verkehr '
         'füllen; also sollte das Geld in <em>public transport</em> fließen. '
         '<em>Invest in public transport</em> trägt dieses Argument; '
         '<em>invest in infrastructure</em> ist der weitere Begriff.',
    t3cn='Beide Antworten können mit <em>the cost of living</em> enden: '
         'Frag, wer am Ende bezahlt.',

    mcaEyebrow='Aktivität 1 · Arbeit',
    mcaTitle='Welche Wortverbindung, und welches Wort?',
    mcbEyebrow='Aktivität 2 · Automatisierung',
    mcbTitle='Das Substantiv bringt sein Verb mit',
    mccEyebrow='Aktivität 3 · Städte',
    mccTitle='Die schlichte Wortverbindung ist die genaue',

    v1why='<em>Work remotely</em> oder <em>work from home</em>. '
          '<em>Distantly</em> beschreibt eine Art und Weise oder eine '
          'Verwandtschaft &mdash; <em>smiled distantly</em>, <em>distantly '
          'related</em> &mdash;, keine Arbeitsform. <em>At a distance</em> '
          'und <em>from a distance</em> sagen, wie weit etwas entfernt ist, '
          'und ohne das <em>a</em> sind sie gar kein Englisch.',
    v2why='<em>Job security</em>. <em>Work safety</em> ist echtes Englisch und '
          'heißt etwas anderes &mdash; Helme und Notausgänge &mdash;, das ist '
          'der Präzisionsfehler. Die anderen beiden sind keine Wortverbindungen, die '
          'das Englische hat.',
    v3why='<em>Suffer from burnout</em>, so wie <em>suffer from stress</em> '
          'oder <em>suffer from insomnia</em>: Eine Krankheit oder ein '
          'Zustand nimmt meist <em>suffer from</em>. Zu <em>get into</em>, '
          '<em>fall in</em> und <em>make</em> greift, wer das Substantiv '
          'ohne sein Verb gelernt hat. Das Englische hat auch ein eigenes '
          'Verb: Pflegekräfte <em>burn out</em>.',
    v4why='<em>Improve career prospects</em>. <em>Career trajectory</em> ist '
          'echtes Englisch, aber niemand <em>augments</em> eine; <em>enlarge '
          'a career future</em> und <em>amplify a career chance</em> sind '
          'Wort für Wort gebaut, und so sagt man es auf Englisch nicht. Die '
          'schlichte Wortverbindung ist die genaue.',
    v5why='<em>Displace</em> ist das Verb für Arbeitskräfte, die etwas Neues '
          'aus ihren Stellen drängt. <em>Deport</em> ist ein Mensch, der '
          'außer Landes gebracht wird, <em>misplace</em> ist ein '
          'Schlüsselbund, <em>evict</em> ist ein Mieter &mdash; drei echte '
          'Wörter, jedes genau für etwas anderes.',
    v6why='<em>Productivity gains</em> oder <em>productivity growth</em>. '
          '<em>Profits</em>, <em>earnings</em> und <em>winnings</em> sind '
          'Geld, das jemand bekommt, und Produktivität ist kein Geld: Sie '
          'sagt, wie viel für die geleistete Arbeit herauskommt.',
    v7why='<em>Retrain the workforce</em>: Arbeitskräften neue Fähigkeiten '
          'geben. <em>Reteach</em> heißt, eine Lektion noch einmal '
          'unterrichten, <em>re-form</em> heißt, sich neu formieren (eine '
          'Gruppe, eine Reihe), und <em>re-school</em> ist kein Verb, das '
          'das Englische benutzt.',
    v8why='<em>A universal basic income</em> ist der Name der Maßnahme, und '
          'alles andere klingt geraten. <em>Wage</em> und <em>salary</em> '
          'werden für Arbeit gezahlt, und genau das ist es hier nicht; '
          '<em>payment</em> ist zu allgemein, um der Name von irgendetwas zu '
          'sein.',
    v9why='<em>Urban sprawl</em> ist der feste Begriff, und er trägt eine '
          'Wertung: Wachstum, das ungeplant ist und Land verschlingt. '
          '<em>Spreading</em>, <em>stretch</em> und <em>widening</em> '
          'beschreiben die Bewegung, aber keines davon verbindet das '
          'Englische mit <em>urban</em>, um sie zu benennen.',
    v10why='<em>Affordable housing</em> ist der Standardbegriff, den Planer, '
           'Politiker und Zeitungen gleichermaßen benutzen. '
           '<em>Economical</em> beschreibt etwas, das im Unterhalt billig '
           'ist, etwa ein Auto; <em>reasonable</em> passt zu einem Preis '
           'oder einer Miete, nicht zu Wohnraum; und <em>cheap-priced</em> '
           'ist kein Englisch.',
    v11why='<em>Invest in</em>: Geld wird <em>in</em> etwas investiert '
           '&mdash; <em>in infrastructure</em>, <em>in public '
           'transport</em>, <em>in people</em>. <em>On</em>, <em>to</em> und '
           '<em>at</em> sind typische Lernerfehler, und keines davon passt '
           'zu <em>invest</em>.',
    v12why='<em>A long commute</em>. Die anderen drei greifen nach einem '
           'selteneren Adjektiv und einem selteneren Substantiv und liegen '
           'bei beiden daneben: Den Weg zur Arbeit nennt das Englische nicht '
           '<em>transit</em>, <em>journeying</em> oder <em>travelling</em>. '
           'Die schlichte Wortverbindung ist die, die Englischsprecher '
           'tatsächlich benutzen.',

    sortEyebrow='Aktivität 4 · Die Wortverbindung als Ganzes',
    sortTitle='Sortiere die sechs Wortverbindungen',
    sortHint='Zieh jede in eine Spalte &mdash; oder klicke ein Element an und '
             'dann die Spalte, in die es soll.',
    sortBin1='Natürliches Englisch',
    sortBin2='Nicht natürlich',
    sortWhy='Das Substantiv wählt sein Verb und sein Adjektiv. Stau wird '
            '<em>eased</em>, Personal wird <em>taken on</em>, und <em>the '
            'gig economy</em> ist ein fester Name. Stau ist <em>heavy</em> '
            'oder <em>severe</em>, nicht <em>big</em>; Verkehr ist '
            '<em>heavy</em>, nicht <em>strong</em>; Wohnraum ist '
            '<em>affordable</em> oder <em>cheap</em>, nicht '
            '<em>cheap-priced</em>. Diese drei baut, wer mit dem Wörterbuch '
            'Wort für Wort vorgeht. Lern die Wendung als Ganzes, dann musst '
            'du sie nie selbst bauen.',

    actTitle='Antworte aus der Sammlung',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu zweit. Einer ist der Prüfer und stellt Fragen aus Teil '
                  '3 zu Arbeit und Städten &mdash; <em>is working from home '
                  'good for a company? Should cities build up or out? Who '
                  'should pay to retrain people?</em> Der andere beantwortet '
                  'jede eine Minute lang, nur mit der Sammlung auf diesem '
                  'Deck. Dann tauschen.',
    actSpeak1='Jede Antwort stellt zwei Wortverbindungen gegeneinander &mdash; eine '
              'pro Seite, mit <em>but</em> oder <em>whereas</em> dazwischen.',
    actSpeak2='Der Prüfer stoppt dich, sobald du ein nacktes Wort benutzt, wo '
              'die Sammlung eine Wortverbindung hat, und du sagst es noch einmal mit '
              'der Phrase.',
    actSpeak3='Jede dritte Frage ist eine Nachfrage &mdash; <em>why?</em> oder '
              '<em>can you give an example?</em> &mdash;, und die Antwort '
              'muss eine Wortverbindung ergänzen, die du noch nicht benutzt hast.',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Wähl eine der drei Ideen und schreib dazu einen '
                  'Hauptteil-Absatz für Task 2: Behauptung, Argument, '
                  'Beispiel, Einschränkung. Verwende mindestens fünf '
                  'Wortverbindungen aus der Sammlung und unterstreiche jede. '
                  'Dann lies ihn noch einmal: Ein Satz ohne genaue '
                  'Wortverbindung ist eine verpasste Chance, Bandbreite zu '
                  'zeigen.',
    actPlaceholder='Automation displaces workers in low-skilled jobs, but…',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Trabajo, automatización <em>y ciudades</em>',
    coverSub='Tres temas que salen una y otra vez en la Parte 3 y en Task 2, '
             'y las combinaciones que hacen que una respuesta sobre cualquiera de '
             'ellos suene pensada',
    chipLevel='C1 · Avanzado', chipFocus='Speaking y Writing Task 2',
    chipCount='18 puntos',

    t1Eyebrow='Idea uno',
    t1Title='Trabajo: flexibilidad contra seguridad',
    t1ah='Las combinaciones',
    t1ab='<em>Job security</em>, <em>career prospects</em>, '
         '<em>work&ndash;life balance</em>: expresiones cuyas palabras '
         'vienen en bloque. Se <em>works remotely</em> o <em>works from '
         'home</em>, la gente <em>suffers from burnout</em>, una empresa '
         '<em>takes on staff</em>. Ninguna de estas palabras es rara; lo que '
         'nota el examinador es si llegan en las combinaciones correctas.',
    t1an='Aprende la expresión entera, <em>suffer from burnout</em>, no solo '
         'el sustantivo <em>burnout</em>.',
    t1bh='Flexibilidad contra aislamiento',
    t1bb='Una pregunta habitual de la Parte 3 es alguna forma de <em>is '
         'working from home good for people?</em> Una buena respuesta sopesa '
         'los dos lados: <em>a flexible schedule</em> en uno, los compañeros '
         'a los que ya no ves en el otro.',
    t1bn='Una idea, dos frases, y <em>but</em> en medio.',
    t1ch='Seguridad contra oportunidad',
    t1cb='Cuando una pregunta de Task 2 plantea cómo está cambiando el '
         'trabajo, <em>the gig economy</em> es un ejemplo evidente. '
         'Arguméntalo como un intercambio: ofrece <em>a flexible '
         'schedule</em> y quita <em>job security</em>; amplía las <em>career '
         'prospects</em> de unos y reduce las de otros.',
    t1cn='Di qué da y qué quita. Ese es el párrafo.',

    t2Eyebrow='Idea dos',
    t2Title='Automatización: empleos perdidos contra empleos creados',
    t2ah='Las combinaciones',
    t2ab='<em>Automate routine tasks</em>, <em>replace workers</em>, '
         '<em>retrain the workforce</em>; <em>productivity gains</em>, '
         '<em>low-skilled jobs</em>, <em>artificial intelligence</em>. El '
         'sustantivo trae su verbo: las tareas se <em>automated</em>, los '
         'trabajadores son <em>displaced</em>, una plantilla es '
         '<em>retrained</em>.',
    t2an='<em>Automate</em> es el verbo que usa todo el mundo. '
         '<em>Automatise</em> está en el diccionario, pero es tan raro que '
         'suena a traducción.',
    t2bh='Perdidos contra creados',
    t2bb='La mayoría de las preguntas sobre automatización se reducen al '
         'mismo intercambio: las máquinas <em>displace</em> a trabajadores '
         'en <em>low-skilled jobs</em>, y las <em>productivity gains</em> '
         'pueden pagar empleos que antes no existían. Sopesa las dos '
         'mitades. A una respuesta parcial pronto se le acaba lo que decir; '
         'una equilibrada sigue adelante y te da motivos para usar '
         '<em>whereas</em> y <em>on the other hand</em>.',
    t2bn='Nombra quién pierde, nombra quién gana, y di qué pesa más.',
    t2ch='Quién reconvierte a quién',
    t2cb='El segundo argumento trata de la responsabilidad. ¿Debe el Estado '
         '<em>retrain the workforce</em>, o la empresa que la '
         '<em>replaced</em>? <em>A universal basic income</em> da nombre a '
         'una tercera respuesta: pagar en su lugar a todo el mundo una '
         'cantidad fija.',
    t2cn='Una combinación por postura, y tres posturas donde elegir.',

    t3Eyebrow='Idea tres',
    t3Title='Ciudades: densidad contra espacio, el coche contra el autobús',
    t3ah='Las combinaciones',
    t3ab='<em>Urban sprawl</em>, <em>affordable housing</em>, <em>public '
         'transport</em>, <em>green spaces</em>, <em>the cost of living</em>. '
         'Un ayuntamiento <em>invests in infrastructure</em> e intenta '
         '<em>ease congestion</em>; un vecino tiene <em>a long commute</em> y '
         'aguanta <em>overcrowding</em>.',
    t3an='Con <em>congestion</em>, el verbo es <em>ease</em> o '
         '<em>reduce</em>. El tráfico es <em>heavy</em>, no <em>strong</em>.',
    t3bh='Densidad contra espacio',
    t3bb='Una pregunta típica de Task 2 sobre ciudades es alguna versión de '
         '<em>should cities build up or out?</em> Construir en altura puede '
         'poner <em>affordable housing</em> cerca del centro y limitar el '
         '<em>urban sprawl</em>, con el riesgo del <em>overcrowding</em>. '
         'Construir hacia fuera da más espacio a la gente, a costa de los '
         '<em>green spaces</em> y de <em>a long commute</em>.',
    t3bn='Las dos respuestas cuestan algo. Di qué.',
    t3ch='El coche contra el autobús',
    t3cb='La Parte 3 puede preguntar cómo <em>ease congestion</em>. Un '
         'argumento conocido es que una ciudad no puede salir del atasco '
         'construyendo, porque las carreteras nuevas pronto se llenan de '
         'tráfico nuevo, así que el dinero debería ir al <em>public '
         'transport</em>. <em>Invest in public transport</em> expresa esa '
         'idea; <em>invest in infrastructure</em> es el término más amplio.',
    t3cn='Cualquiera de las dos respuestas puede cerrar con <em>the cost of '
         'living</em>: pregunta quién paga al final.',

    mcaEyebrow='Actividad 1 · Trabajo',
    mcaTitle='¿Qué combinación, y qué palabra?',
    mcbEyebrow='Actividad 2 · Automatización',
    mcbTitle='El sustantivo trae su verbo',
    mccEyebrow='Actividad 3 · Ciudades',
    mccTitle='La combinación sencilla es la precisa',

    v1why='<em>Work remotely</em>, o <em>work from home</em>. '
          '<em>Distantly</em> describe una manera o un parentesco &mdash; '
          '<em>smiled distantly</em>, <em>distantly related</em> &mdash;, no '
          'una forma de trabajar. <em>At a distance</em> y <em>from a '
          'distance</em> hablan de lo lejos que está algo, y sin la '
          '<em>a</em> ni siquiera son inglés.',
    v2why='<em>Job security</em>. <em>Work safety</em> es inglés de verdad y '
          'significa otra cosa &mdash; cascos y salidas de emergencia &mdash;, '
          'que es el fallo de precisión. Las otras dos no son combinaciones que el '
          'inglés tenga.',
    v3why='<em>Suffer from burnout</em>, igual que <em>suffer from '
          'stress</em> o <em>suffer from insomnia</em>: una enfermedad o un '
          'estado suele llevar <em>suffer from</em>. <em>Get into</em>, '
          '<em>fall in</em> y <em>make</em> son lo que se busca cuando el '
          'sustantivo se aprendió sin su verbo. El inglés también tiene un '
          'verbo propio: las enfermeras <em>burn out</em>.',
    v4why='<em>Improve career prospects</em>. <em>Career trajectory</em> es '
          'inglés real, pero nadie la <em>augments</em>; <em>enlarge a '
          'career future</em> y <em>amplify a career chance</em> están '
          'construidas palabra por palabra, y el inglés no las dice. La '
          'combinación sencilla es la precisa.',
    v5why='<em>Displace</em> es el verbo para trabajadores a los que algo '
          'nuevo expulsa de su empleo. <em>Deport</em> es una persona '
          'expulsada de un país, <em>misplace</em> es un manojo de llaves, '
          '<em>evict</em> es un inquilino &mdash; tres palabras reales, cada '
          'una precisa para otra cosa.',
    v6why='<em>Productivity gains</em>, o <em>productivity growth</em>. '
          '<em>Profits</em>, <em>earnings</em> y <em>winnings</em> son '
          'dinero que alguien recibe, y la productividad no es dinero: es '
          'cuánto se produce por el trabajo invertido.',
    v7why='<em>Retrain the workforce</em>: dar nuevas competencias a los '
          'trabajadores. <em>Reteach</em> significa volver a enseñar una '
          'lección, <em>re-form</em> significa volver a constituirse (un '
          'grupo, una fila), y <em>re-school</em> no es un verbo que use el '
          'inglés.',
    v8why='<em>A universal basic income</em> es el nombre de la medida, y '
          'cualquier otra cosa suena a suposición. Un <em>wage</em> y un '
          '<em>salary</em> se pagan por trabajar, que es justo lo que esto '
          'no es, y <em>payment</em> es demasiado general para ser el nombre '
          'de nada.',
    v9why='<em>Urban sprawl</em> es el término fijo, y lleva un juicio: un '
          'crecimiento sin planificar que se traga el suelo. '
          '<em>Spreading</em>, <em>stretch</em> y <em>widening</em> '
          'describen el movimiento, pero el inglés no combina ninguno con '
          '<em>urban</em> para nombrarlo.',
    v10why='<em>Affordable housing</em> es el término estándar, el que usan '
           'por igual urbanistas, políticos y periódicos. '
           '<em>Economical</em> describe algo barato de mantener, como un '
           'coche; <em>reasonable</em> va con un precio o un alquiler, no '
           'con la vivienda; y <em>cheap-priced</em> no es inglés.',
    v11why='<em>Invest in</em>: el dinero se invierte <em>in</em> algo '
           '&mdash; <em>in infrastructure</em>, <em>in public '
           'transport</em>, <em>in people</em>. <em>On</em>, <em>to</em> y '
           '<em>at</em> son errores típicos de quien aprende, y ninguno va '
           'con <em>invest</em>.',
    v12why='<em>A long commute</em>. Las otras tres buscan un adjetivo más '
           'raro y un sustantivo más raro y fallan en los dos: el inglés no '
           'llama al trayecto al trabajo <em>transit</em>, '
           '<em>journeying</em> ni <em>travelling</em>. La combinación '
           'sencilla es la que de verdad usan los hablantes de inglés.',

    sortEyebrow='Actividad 4 · La combinación entera',
    sortTitle='Clasifica las seis combinaciones',
    sortHint='Arrastra cada una a una columna &mdash; o haz clic en un '
             'elemento y luego en la columna que quieras.',
    sortBin1='Inglés natural',
    sortBin2='No es natural',
    sortWhy='El sustantivo elige su verbo y su adjetivo. Con '
            '<em>congestion</em> va <em>ease</em>, con <em>staff</em> va '
            '<em>take on</em>, y <em>the gig economy</em> es un nombre fijo. '
            'La congestión es <em>heavy</em> o <em>severe</em>, no '
            '<em>big</em>; el tráfico es <em>heavy</em>, no <em>strong</em>; '
            'la vivienda es <em>affordable</em> o <em>cheap</em>, no '
            '<em>cheap-priced</em>. Esas tres las construye quien aprende a '
            'partir del diccionario, palabra por palabra. Aprende la '
            'expresión entera y nunca tendrás que construirla.',

    actTitle='Responde desde el banco',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas. Uno hace de examinador y plantea preguntas de '
                  'la Parte 3 sobre trabajo y ciudades &mdash; <em>is working '
                  'from home good for a company? Should cities build up or '
                  'out? Who should pay to retrain people?</em> El otro '
                  'responde a cada una durante un minuto usando solo el banco '
                  'de esta lección. Luego cambiad.',
    actSpeak1='Cada respuesta enfrenta dos combinaciones &mdash; una por cada lado, '
              'con <em>but</em> o <em>whereas</em> en medio.',
    actSpeak2='El examinador te para en cuanto uses una palabra suelta donde '
              'el banco tiene una combinación, y lo dices otra vez con la frase.',
    actSpeak3='Cada tercera pregunta es de seguimiento &mdash; <em>why?</em> o '
              '<em>can you give an example?</em> &mdash;, y la respuesta tiene '
              'que añadir una combinación que aún no hayas usado.',
    actWriteKind='Escritura · 150–200 palabras',
    actWriteBrief='Elige una de las tres ideas y escribe sobre ella un '
                  'párrafo de desarrollo de Task 2: la afirmación, el '
                  'argumento, un ejemplo, la concesión. Usa al menos cinco '
                  'combinaciones del banco y subraya cada una. Luego '
                  'reléelo: una frase sin ninguna combinación precisa es una '
                  'ocasión perdida de mostrar variedad.',
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
    t1ab='<em>Job security</em>, <em>career prospects</em>, '
         '<em>work&ndash;life balance</em> : des expressions dont les mots '
         'vont ensemble. On <em>works remotely</em> ou <em>works from '
         'home</em>, on <em>suffers from burnout</em>, une entreprise '
         '<em>takes on staff</em>. Aucun de ces mots n’est rare ; ce que '
         'l’examinateur remarque, c’est s’ils arrivent dans les bonnes '
         'associations.',
    t1an='Apprenez l’expression entière, <em>suffer from burnout</em>, pas '
         'seulement le nom <em>burnout</em>.',
    t1bh='La flexibilité contre l’isolement',
    t1bb='Une question fréquente de la Partie 3 est une variante de <em>is '
         'working from home good for people?</em> Une bonne réponse met les '
         'deux côtés en balance : <em>a flexible schedule</em> d’un côté, '
         'les collègues que l’on ne voit plus de l’autre.',
    t1bn='Une idée, deux expressions, et un <em>but</em> entre les deux.',
    t1ch='La sécurité contre les occasions',
    t1cb='Quand une question de Task 2 porte sur l’évolution du travail, '
         '<em>the gig economy</em> est un exemple évident. Présentez-la '
         'comme un échange : elle offre <em>a flexible schedule</em> et '
         'retire <em>job security</em> ; elle élargit les <em>career '
         'prospects</em> des uns et réduit celles des autres.',
    t1cn='Dites ce qu’elle donne et ce qu’elle prend. Voilà le paragraphe.',

    t2Eyebrow='Deuxième idée',
    t2Title='L’automatisation : emplois perdus contre emplois créés',
    t2ah='Les associations',
    t2ab='<em>Automate routine tasks</em>, <em>replace workers</em>, '
         '<em>retrain the workforce</em> ; <em>productivity gains</em>, '
         '<em>low-skilled jobs</em>, <em>artificial intelligence</em>. Le nom '
         'amène son verbe : les tâches sont <em>automated</em>, les travailleurs '
         '<em>displaced</em>, une main-d’œuvre <em>retrained</em>.',
    t2an='<em>Automate</em> est le verbe que tout le monde emploie. '
         '<em>Automatise</em> figure au dictionnaire, mais il est si rare '
         'qu’il sonne comme une traduction.',
    t2bh='Perdus contre créés',
    t2bb='La plupart des questions sur l’automatisation reviennent au même '
         'échange : les machines <em>displace</em> des travailleurs dans des '
         '<em>low-skilled jobs</em>, et les <em>productivity gains</em> '
         'peuvent financer des emplois qui n’existaient pas avant. Pesez les '
         'deux moitiés. Une réponse à sens unique est vite à court d’idées ; '
         'une réponse équilibrée continue, et vous donne une raison '
         'd’employer <em>whereas</em> et <em>on the other hand</em>.',
    t2bn='Dites qui perd, dites qui gagne, et dites ce qui compte le plus.',
    t2ch='Qui forme qui',
    t2cb='Le deuxième argument porte sur la responsabilité. Est-ce à l’État '
         'de <em>retrain the workforce</em>, ou à l’employeur qui l’a '
         '<em>replaced</em> ? <em>A universal basic income</em> désigne une '
         'troisième réponse : verser plutôt à chacun une somme régulière.',
    t2cn='Une association par position, et trois positions au choix.',

    t3Eyebrow='Troisième idée',
    t3Title='Les villes : la densité contre l’espace, la voiture contre le bus',
    t3ah='Les associations',
    t3ab='<em>Urban sprawl</em>, <em>affordable housing</em>, <em>public '
         'transport</em>, <em>green spaces</em>, <em>the cost of living</em>. Une '
         'municipalité <em>invests in infrastructure</em> et tente d’<em>ease '
         'congestion</em> ; un habitant a <em>a long commute</em> et supporte '
         'l’<em>overcrowding</em>.',
    t3an='Avec <em>congestion</em>, le verbe est <em>ease</em> ou '
         '<em>reduce</em>. La circulation est <em>heavy</em>, pas '
         '<em>strong</em>.',
    t3bh='La densité contre l’espace',
    t3bb='Une question typique de Task 2 sur les villes est une variante de '
         '<em>should cities build up or out?</em> Construire en hauteur peut '
         'mettre de l’<em>affordable housing</em> près du centre et limiter '
         'l’<em>urban sprawl</em>, au risque de l’<em>overcrowding</em>. '
         'Construire en largeur donne plus d’espace, au prix des <em>green '
         'spaces</em> et d’<em>a long commute</em>.',
    t3bn='Les deux réponses ont un coût. Dites lequel.',
    t3ch='La voiture contre le bus',
    t3cb='La Partie 3 peut demander comment <em>ease congestion</em>. Un '
         'argument bien connu veut qu’une ville ne puisse pas sortir des '
         'embouteillages en construisant, car les nouvelles routes se '
         'remplissent vite de nouveaux véhicules ; l’argent devrait donc '
         'aller au <em>public transport</em>. <em>Invest in public '
         'transport</em> porte cette idée ; <em>invest in '
         'infrastructure</em> est le terme plus large.',
    t3cn='Les deux réponses peuvent se conclure sur <em>the cost of '
         'living</em> : demandez qui paie à la fin.',

    mcaEyebrow='Activité 1 · Le travail',
    mcaTitle='Quelle association, et quel mot ?',
    mcbEyebrow='Activité 2 · L’automatisation',
    mcbTitle='Le nom amène son verbe',
    mccEyebrow='Activité 3 · Les villes',
    mccTitle='L’association simple est la plus précise',

    v1why='<em>Work remotely</em>, ou <em>work from home</em>. '
          '<em>Distantly</em> décrit une manière ou un lien de parenté '
          '&mdash; <em>smiled distantly</em>, <em>distantly related</em> '
          '&mdash;, pas une façon de travailler. <em>At a distance</em> et '
          '<em>from a distance</em> disent à quelle distance se trouve '
          'quelque chose, et sans le <em>a</em> ce n’est pas de l’anglais du '
          'tout.',
    v2why='<em>Job security</em>. <em>Work safety</em> existe en anglais et veut '
          'dire autre chose &mdash; les casques et les sorties de secours &mdash;, '
          'et c’est là le raté de précision. Les deux autres ne sont pas des '
          'associations que l’anglais possède.',
    v3why='<em>Suffer from burnout</em>, comme <em>suffer from stress</em> '
          'ou <em>suffer from insomnia</em> : une maladie ou un état prend '
          'en général <em>suffer from</em>. <em>Get into</em>, <em>fall '
          'in</em> et <em>make</em>, c’est ce qu’on attrape quand on a '
          'appris le nom sans son verbe. L’anglais a aussi un verbe à lui : '
          'les infirmières <em>burn out</em>.',
    v4why='<em>Improve career prospects</em>. <em>Career trajectory</em> '
          'existe bien en anglais, mais personne n’en <em>augments</em> une '
          '; <em>enlarge a career future</em> et <em>amplify a career '
          'chance</em> sont construits mot à mot, et l’anglais ne les dit '
          'pas. L’association simple est la plus précise.',
    v5why='<em>Displace</em> est le verbe pour des travailleurs chassés de '
          'leur emploi par quelque chose de nouveau. <em>Deport</em>, c’est '
          'une personne expulsée d’un pays, <em>misplace</em>, un trousseau '
          'de clés, <em>evict</em>, un locataire &mdash; trois vrais mots, '
          'chacun précis pour autre chose.',
    v6why='<em>Productivity gains</em>, ou <em>productivity growth</em>. '
          '<em>Profits</em>, <em>earnings</em> et <em>winnings</em> sont de '
          'l’argent que quelqu’un reçoit, et la productivité n’est pas de '
          'l’argent : c’est ce que l’on produit pour le travail fourni.',
    v7why='<em>Retrain the workforce</em> : donner de nouvelles compétences '
          'aux travailleurs. <em>Reteach</em> veut dire enseigner de nouveau '
          'une leçon, <em>re-form</em> veut dire se reformer (un groupe, une '
          'file), et <em>re-school</em> n’est pas un verbe anglais.',
    v8why='<em>A universal basic income</em> est le nom de la mesure, et '
          'tout le reste sonne comme une devinette. Un <em>wage</em> et un '
          '<em>salary</em> rémunèrent un travail, ce que ce n’est justement '
          'pas, et <em>payment</em> est trop général pour être le nom de '
          'quoi que ce soit.',
    v9why='<em>Urban sprawl</em> est le terme consacré, et il porte un '
          'jugement : une croissance non planifiée qui dévore le terrain. '
          '<em>Spreading</em>, <em>stretch</em> et <em>widening</em> '
          'décrivent le mouvement, mais l’anglais n’associe aucun d’eux à '
          '<em>urban</em> pour le nommer.',
    v10why='<em>Affordable housing</em> est le terme standard, employé aussi '
           'bien par les urbanistes que par les responsables politiques et '
           'la presse. <em>Economical</em> décrit ce qui coûte peu à '
           'l’usage, comme une voiture ; <em>reasonable</em> va avec un prix '
           'ou un loyer, pas avec le logement ; et <em>cheap-priced</em> '
           'n’est pas de l’anglais.',
    v11why='<em>Invest in</em> : on investit <em>in</em> quelque chose '
           '&mdash; <em>in infrastructure</em>, <em>in public '
           'transport</em>, <em>in people</em>. <em>On</em>, <em>to</em> et '
           '<em>at</em> sont des erreurs typiques d’apprenant, et aucune ne '
           'va avec <em>invest</em>.',
    v12why='<em>A long commute</em>. Les trois autres vont chercher un '
           'adjectif plus rare et un nom plus rare, et ratent les deux : '
           'l’anglais n’appelle pas le trajet domicile-travail un '
           '<em>transit</em>, un <em>journeying</em> ou un '
           '<em>travelling</em>. L’association simple est celle qu’emploient '
           'vraiment les anglophones.',

    sortEyebrow='Activité 4 · L’association, en entier',
    sortTitle='Classez les six associations',
    sortHint='Faites glisser chacune dans une colonne &mdash; ou cliquez sur '
             'un élément, puis sur la colonne voulue.',
    sortBin1='Anglais naturel',
    sortBin2='Pas naturel',
    sortWhy='Le nom choisit son verbe et son adjectif. Avec '
            '<em>congestion</em>, on emploie <em>ease</em> ; avec '
            '<em>staff</em>, <em>take on</em> ; et <em>the gig economy</em> '
            'est un nom figé. La congestion est <em>heavy</em> ou '
            '<em>severe</em>, pas <em>big</em> ; la circulation est '
            '<em>heavy</em>, pas <em>strong</em> ; le logement est '
            '<em>affordable</em> ou <em>cheap</em>, pas '
            '<em>cheap-priced</em>. Ces trois-là, un apprenant les construit '
            'à partir du dictionnaire, mot à mot. Apprenez l’expression '
            'entière et vous n’aurez jamais à la construire.',

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
    actWriteBrief='Choisissez l’une des trois idées et rédigez sur elle un '
                  'paragraphe de développement pour Task 2 : l’affirmation, '
                  'l’argument, un exemple, la concession. Utilisez au moins '
                  'cinq associations de la banque et soulignez chacune. Puis '
                  'relisez : une phrase sans association précise est une '
                  'occasion manquée de montrer l’étendue de votre '
                  'vocabulaire.',
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
    t1ab='<em>Job security</em>, <em>career prospects</em>, '
         '<em>work&ndash;life balance</em>: espressioni le cui parole '
         'arrivano in blocco. Si <em>works remotely</em> o <em>works from '
         'home</em>, la gente <em>suffers from burnout</em>, un’azienda '
         '<em>takes on staff</em>. Nessuna di queste parole è rara; quello '
         'che l’esaminatore nota è se arrivano nelle combinazioni giuste.',
    t1an='Impara l’espressione intera, <em>suffer from burnout</em>, non '
         'solo il nome <em>burnout</em>.',
    t1bh='Flessibilità contro isolamento',
    t1bb='Una domanda frequente della Parte 3 è una variante di <em>is '
         'working from home good for people?</em> Una buona risposta mette '
         'sulla bilancia i due lati: <em>a flexible schedule</em> da una '
         'parte, i colleghi che non vedi più dall’altra.',
    t1bn='Un’idea, due espressioni, e un <em>but</em> in mezzo.',
    t1ch='Sicurezza contro opportunità',
    t1cb='Quando una domanda di Task 2 chiede come sta cambiando il lavoro, '
         '<em>the gig economy</em> è un esempio ovvio. Presentala come uno '
         'scambio: offre <em>a flexible schedule</em> e toglie <em>job '
         'security</em>; allarga le <em>career prospects</em> di alcuni e '
         'restringe quelle di altri.',
    t1cn='Di’ che cosa dà e che cosa toglie. Ecco il paragrafo.',

    t2Eyebrow='Seconda idea',
    t2Title='L’automazione: posti persi contro posti creati',
    t2ah='Le combinazioni',
    t2ab='<em>Automate routine tasks</em>, <em>replace workers</em>, '
         '<em>retrain the workforce</em>; <em>productivity gains</em>, '
         '<em>low-skilled jobs</em>, <em>artificial intelligence</em>. Il nome si '
         'porta dietro il verbo: i compiti sono <em>automated</em>, i lavoratori '
         '<em>displaced</em>, una forza lavoro <em>retrained</em>.',
    t2an='<em>Automate</em> è il verbo che usano tutti. <em>Automatise</em> '
         'è nel dizionario, ma è così raro che suona come una traduzione.',
    t2bh='Persi contro creati',
    t2bb='La maggior parte delle domande sull’automazione si riduce allo '
         'stesso scambio: le macchine <em>displace</em> lavoratori nei '
         '<em>low-skilled jobs</em>, e i <em>productivity gains</em> possono '
         'pagare lavori che prima non esistevano. Pesa entrambe le metà. A '
         'una risposta unilaterale mancano presto le cose da dire; una '
         'equilibrata va avanti e ti dà un motivo per usare <em>whereas</em> '
         'e <em>on the other hand</em>.',
    t2bn='Di’ chi perde, di’ chi guadagna, e di’ che cosa conta di più.',
    t2ch='Chi riqualifica chi',
    t2cb='Il secondo argomento riguarda la responsabilità. Deve essere lo '
         'Stato a <em>retrain the workforce</em>, o il datore di lavoro che '
         'l’ha <em>replaced</em>? <em>A universal basic income</em> dà il '
         'nome a una terza risposta: pagare invece a tutti una somma '
         'regolare.',
    t2cn='Una combinazione per posizione, e tre posizioni tra cui scegliere.',

    t3Eyebrow='Terza idea',
    t3Title='Le città: densità contro spazio, l’auto contro l’autobus',
    t3ah='Le combinazioni',
    t3ab='<em>Urban sprawl</em>, <em>affordable housing</em>, <em>public '
         'transport</em>, <em>green spaces</em>, <em>the cost of living</em>. Un '
         'comune <em>invests in infrastructure</em> e cerca di <em>ease '
         'congestion</em>; un residente ha <em>a long commute</em> e sopporta '
         'l’<em>overcrowding</em>.',
    t3an='Con <em>congestion</em> il verbo è <em>ease</em> o '
         '<em>reduce</em>. Il traffico è <em>heavy</em>, non <em>strong</em>.',
    t3bh='Densità contro spazio',
    t3bb='Una tipica domanda di Task 2 sulle città è una variante di '
         '<em>should cities build up or out?</em> Costruire in altezza può '
         'portare <em>affordable housing</em> vicino al centro e limitare '
         'l’<em>urban sprawl</em>, con il rischio '
         'dell’<em>overcrowding</em>. Costruire in larghezza dà più spazio '
         'alle persone, a spese dei <em>green spaces</em> e con <em>a long '
         'commute</em>.',
    t3bn='Tutte e due le risposte costano qualcosa. Di’ che cosa.',
    t3ch='L’auto contro l’autobus',
    t3cb='La Parte 3 può chiedere come <em>ease congestion</em>. Un '
         'argomento noto è che una città non può uscire dal traffico '
         'costruendo, perché le strade nuove si riempiono presto di traffico '
         'nuovo; quindi i soldi dovrebbero andare al <em>public '
         'transport</em>. <em>Invest in public transport</em> esprime questo '
         'punto; <em>invest in infrastructure</em> è il termine più ampio.',
    t3cn='Tutte e due le risposte possono chiudersi su <em>the cost of '
         'living</em>: chiediti chi paga alla fine.',

    mcaEyebrow='Attività 1 · Il lavoro',
    mcaTitle='Quale combinazione, e quale parola?',
    mcbEyebrow='Attività 2 · L’automazione',
    mcbTitle='Il nome si porta dietro il verbo',
    mccEyebrow='Attività 3 · Le città',
    mccTitle='La combinazione semplice è quella precisa',

    v1why='<em>Work remotely</em>, oppure <em>work from home</em>. '
          '<em>Distantly</em> descrive un modo o una parentela &mdash; '
          '<em>smiled distantly</em>, <em>distantly related</em> &mdash;, '
          'non un modo di lavorare. <em>At a distance</em> e <em>from a '
          'distance</em> dicono quanto è lontano qualcosa, e senza la '
          '<em>a</em> non sono proprio inglese.',
    v2why='<em>Job security</em>. <em>Work safety</em> esiste in inglese e vuol '
          'dire altro &mdash; caschi e uscite di sicurezza &mdash;, ed è questo '
          'l’errore di precisione. Le altre due non sono combinazioni che '
          'l’inglese conosce.',
    v3why='<em>Suffer from burnout</em>, come <em>suffer from stress</em> o '
          '<em>suffer from insomnia</em>: una malattia o una condizione di '
          'solito vuole <em>suffer from</em>. <em>Get into</em>, <em>fall '
          'in</em> e <em>make</em> sono ciò che si prende quando il nome è '
          'stato imparato senza il suo verbo. L’inglese ha anche un verbo '
          'tutto suo: le infermiere <em>burn out</em>.',
    v4why='<em>Improve career prospects</em>. <em>Career trajectory</em> è '
          'inglese vero, ma nessuno ne <em>augments</em> una; <em>enlarge a '
          'career future</em> e <em>amplify a career chance</em> sono '
          'costruite parola per parola, e l’inglese non le dice. La '
          'combinazione semplice è quella precisa.',
    v5why='<em>Displace</em> è il verbo per i lavoratori spinti fuori dal '
          'loro posto da qualcosa di nuovo. <em>Deport</em> è una persona '
          'espulsa da un paese, <em>misplace</em> è un mazzo di chiavi, '
          '<em>evict</em> è un inquilino &mdash; tre parole vere, ognuna '
          'precisa per qualcos’altro.',
    v6why='<em>Productivity gains</em>, oppure <em>productivity growth</em>. '
          '<em>Profits</em>, <em>earnings</em> e <em>winnings</em> sono '
          'soldi che qualcuno riceve, e la produttività non è denaro: è '
          'quanto si produce per il lavoro impiegato.',
    v7why='<em>Retrain the workforce</em>: dare nuove competenze ai '
          'lavoratori. <em>Reteach</em> vuol dire insegnare di nuovo una '
          'lezione, <em>re-form</em> vuol dire ricomporsi (un gruppo, una '
          'fila), e <em>re-school</em> non è un verbo che l’inglese usa.',
    v8why='<em>A universal basic income</em> è il nome della misura, e '
          'qualsiasi altra cosa sembra tirata a indovinare. <em>Wage</em> e '
          '<em>salary</em> si pagano per il lavoro, che è proprio ciò che '
          'questo non è, e <em>payment</em> è troppo generico per essere il '
          'nome di qualcosa.',
    v9why='<em>Urban sprawl</em> è il termine fisso, e contiene un giudizio: '
          'una crescita non pianificata che divora il territorio. '
          '<em>Spreading</em>, <em>stretch</em> e <em>widening</em> '
          'descrivono il movimento, ma l’inglese non ne abbina nessuno a '
          '<em>urban</em> per dargli un nome.',
    v10why='<em>Affordable housing</em> è il termine standard, usato allo '
           'stesso modo da urbanisti, politici e giornali. '
           '<em>Economical</em> descrive qualcosa che costa poco da '
           'mantenere, come un’auto; <em>reasonable</em> va con un prezzo o '
           'un affitto, non con le case; e <em>cheap-priced</em> non è '
           'inglese.',
    v11why='<em>Invest in</em>: il denaro si investe <em>in</em> qualcosa '
           '&mdash; <em>in infrastructure</em>, <em>in public '
           'transport</em>, <em>in people</em>. <em>On</em>, <em>to</em> e '
           '<em>at</em> sono errori tipici di chi impara, e nessuno va con '
           '<em>invest</em>.',
    v12why='<em>A long commute</em>. Le altre tre cercano un aggettivo più '
           'raro e un nome più raro e sbagliano su entrambi: l’inglese non '
           'chiama il tragitto per il lavoro <em>transit</em>, '
           '<em>journeying</em> o <em>travelling</em>. La combinazione '
           'semplice è quella che chi parla inglese usa davvero.',

    sortEyebrow='Attività 4 · La combinazione, intera',
    sortTitle='Classifica le sei combinazioni',
    sortHint='Trascina ciascuna in una colonna &mdash; oppure clicca su un '
             'elemento e poi sulla colonna che vuoi.',
    sortBin1='Inglese naturale',
    sortBin2='Non naturale',
    sortWhy='Il nome sceglie il suo verbo e il suo aggettivo. Con '
            '<em>congestion</em> si usa <em>ease</em>, con <em>staff</em> si '
            'usa <em>take on</em>, e <em>the gig economy</em> è un nome '
            'fisso. La congestione è <em>heavy</em> o <em>severe</em>, non '
            '<em>big</em>; il traffico è <em>heavy</em>, non '
            '<em>strong</em>; le case sono <em>affordable</em> o '
            '<em>cheap</em>, non <em>cheap-priced</em>. Quelle tre le '
            'costruisce chi impara partendo dal dizionario, parola per '
            'parola. Impara l’espressione intera e non dovrai mai costruirla.',

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
    actWriteBrief='Scegli una delle tre idee e scrivi su di essa un '
                  'paragrafo centrale per Task 2: la tesi, l’argomento, un '
                  'esempio, la concessione. Usa almeno cinque combinazioni '
                  'della raccolta e sottolineale tutte. Poi rileggilo: una '
                  'frase senza una combinazione precisa è un’occasione persa '
                  'per mostrare varietà.',
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
    t1ab='<em>Job security</em>, <em>career prospects</em>, '
         '<em>work&ndash;life balance</em>: expressões cujas palavras vêm em '
         'bloco. Diz-se <em>work remotely</em> ou <em>work from home</em>, '
         'as pessoas <em>suffer from burnout</em>, uma empresa <em>takes on '
         'staff</em>. Nenhuma destas palavras é rara; o que o examinador '
         'nota é se chegam nas combinações certas.',
    t1an='Aprende a expressão inteira, <em>suffer from burnout</em>, e não '
         'só o nome <em>burnout</em>.',
    t1bh='Flexibilidade contra isolamento',
    t1bb='Uma pergunta frequente da Parte 3 é uma variante de <em>is working '
         'from home good for people?</em> Uma boa resposta põe os dois lados '
         'na balança: <em>a flexible schedule</em> de um lado, os colegas '
         'que já não vês do outro.',
    t1bn='Uma ideia, duas expressões e um <em>but</em> no meio.',
    t1ch='Segurança contra oportunidade',
    t1cb='Quando uma pergunta de Task 2 quer saber como o trabalho está a '
         'mudar, <em>the gig economy</em> é um exemplo óbvio. Apresenta-a '
         'como uma troca: oferece <em>a flexible schedule</em> e tira '
         '<em>job security</em>; alarga as <em>career prospects</em> de uns '
         'e estreita as de outros.',
    t1cn='Diz o que dá e o que tira. É esse o parágrafo.',

    t2Eyebrow='Segunda ideia',
    t2Title='A automação: empregos perdidos contra empregos criados',
    t2ah='As combinações',
    t2ab='<em>Automate routine tasks</em>, <em>replace workers</em>, '
         '<em>retrain the workforce</em>; <em>productivity gains</em>, '
         '<em>low-skilled jobs</em>, <em>artificial intelligence</em>. O nome traz '
         'o seu verbo: as tarefas são <em>automated</em>, os trabalhadores '
         '<em>displaced</em>, uma força de trabalho <em>retrained</em>.',
    t2an='<em>Automate</em> é o verbo que toda a gente usa. '
         '<em>Automatise</em> está no dicionário, mas é tão raro que soa a '
         'tradução.',
    t2bh='Perdidos contra criados',
    t2bb='A maioria das perguntas sobre automação resume-se à mesma troca: '
         'as máquinas <em>displace</em> trabalhadores em <em>low-skilled '
         'jobs</em>, e os <em>productivity gains</em> podem pagar empregos '
         'que antes não existiam. Pesa as duas metades. Uma resposta '
         'unilateral fica depressa sem nada para dizer; uma equilibrada '
         'continua e dá-te razões para usar <em>whereas</em> e <em>on the '
         'other hand</em>.',
    t2bn='Diz quem perde, diz quem ganha e diz o que pesa mais.',
    t2ch='Quem requalifica quem',
    t2cb='O segundo argumento é sobre responsabilidade. Deve ser o Estado a '
         '<em>retrain the workforce</em>, ou o empregador que a '
         '<em>replaced</em>? <em>A universal basic income</em> dá nome a uma '
         'terceira resposta: pagar antes a todos uma quantia regular.',
    t2cn='Uma combinação por posição, e três posições à escolha.',

    t3Eyebrow='Terceira ideia',
    t3Title='As cidades: densidade contra espaço, o carro contra o autocarro',
    t3ah='As combinações',
    t3ab='<em>Urban sprawl</em>, <em>affordable housing</em>, <em>public '
         'transport</em>, <em>green spaces</em>, <em>the cost of living</em>. Uma '
         'câmara municipal <em>invests in infrastructure</em> e tenta <em>ease '
         'congestion</em>; um morador tem <em>a long commute</em> e aguenta o '
         '<em>overcrowding</em>.',
    t3an='Com <em>congestion</em>, o verbo é <em>ease</em> ou '
         '<em>reduce</em>. O trânsito é <em>heavy</em>, não <em>strong</em>.',
    t3bh='Densidade contra espaço',
    t3bb='Uma pergunta típica de Task 2 sobre cidades é uma versão de '
         '<em>should cities build up or out?</em> Construir em altura pode '
         'pôr <em>affordable housing</em> perto do centro e limitar o '
         '<em>urban sprawl</em>, com o risco de <em>overcrowding</em>. '
         'Construir para fora dá mais espaço às pessoas, à custa dos '
         '<em>green spaces</em> e com <em>a long commute</em>.',
    t3bn='As duas respostas custam alguma coisa. Diz o quê.',
    t3ch='O carro contra o autocarro',
    t3cb='A Parte 3 pode perguntar como <em>ease congestion</em>. Um '
         'argumento conhecido é que uma cidade não consegue sair do trânsito '
         'a construir, porque as estradas novas depressa se enchem de '
         'trânsito novo; por isso, o dinheiro deve ir para o <em>public '
         'transport</em>. <em>Invest in public transport</em> exprime essa '
         'ideia; <em>invest in infrastructure</em> é o termo mais amplo.',
    t3cn='Qualquer das respostas pode fechar com <em>the cost of '
         'living</em>: pergunta quem paga no fim.',

    mcaEyebrow='Atividade 1 · O trabalho',
    mcaTitle='Que combinação, e que palavra?',
    mcbEyebrow='Atividade 2 · A automação',
    mcbTitle='O nome traz o seu verbo',
    mccEyebrow='Atividade 3 · As cidades',
    mccTitle='A combinação simples é a precisa',

    v1why='<em>Work remotely</em>, ou <em>work from home</em>. '
          '<em>Distantly</em> descreve uma maneira ou um parentesco &mdash; '
          '<em>smiled distantly</em>, <em>distantly related</em> &mdash;, '
          'não uma forma de trabalhar. <em>At a distance</em> e <em>from a '
          'distance</em> dizem a que distância está alguma coisa, e sem o '
          '<em>a</em> nem sequer são inglês.',
    v2why='<em>Job security</em>. <em>Work safety</em> existe em inglês e quer '
          'dizer outra coisa &mdash; capacetes e saídas de emergência &mdash;, e é '
          'aí que está a falha de precisão. As outras duas não são combinações '
          'que o inglês tenha.',
    v3why='<em>Suffer from burnout</em>, tal como <em>suffer from '
          'stress</em> ou <em>suffer from insomnia</em>: uma doença ou um '
          'estado costuma levar <em>suffer from</em>. <em>Get into</em>, '
          '<em>fall in</em> e <em>make</em> são o que se agarra quando o '
          'nome foi aprendido sem o seu verbo. O inglês também tem um verbo '
          'próprio: os enfermeiros <em>burn out</em>.',
    v4why='<em>Improve career prospects</em>. <em>Career trajectory</em> é '
          'inglês verdadeiro, mas ninguém <em>augments</em> uma; <em>enlarge '
          'a career future</em> e <em>amplify a career chance</em> são '
          'construídas palavra a palavra, e o inglês não as diz. A '
          'combinação simples é a precisa.',
    v5why='<em>Displace</em> é o verbo para trabalhadores empurrados para '
          'fora do emprego por algo novo. <em>Deport</em> é uma pessoa '
          'expulsa de um país, <em>misplace</em> é um molho de chaves, '
          '<em>evict</em> é um inquilino &mdash; três palavras verdadeiras, '
          'cada uma precisa para outra coisa.',
    v6why='<em>Productivity gains</em>, ou <em>productivity growth</em>. '
          '<em>Profits</em>, <em>earnings</em> e <em>winnings</em> são '
          'dinheiro que alguém recebe, e a produtividade não é dinheiro: é '
          'quanto se produz pelo trabalho investido.',
    v7why='<em>Retrain the workforce</em>: dar novas competências aos '
          'trabalhadores. <em>Reteach</em> quer dizer voltar a ensinar uma '
          'lição, <em>re-form</em> quer dizer voltar a juntar-se (um grupo, '
          'uma fila), e <em>re-school</em> não é um verbo que o inglês use.',
    v8why='<em>A universal basic income</em> é o nome da medida, e qualquer '
          'outra coisa soa a palpite. Um <em>wage</em> e um <em>salary</em> '
          'pagam-se pelo trabalho, que é precisamente o que isto não é, e '
          '<em>payment</em> é demasiado geral para ser o nome de alguma '
          'coisa.',
    v9why='<em>Urban sprawl</em> é o termo fixo, e traz um juízo: '
          'crescimento não planeado que devora território. '
          '<em>Spreading</em>, <em>stretch</em> e <em>widening</em> '
          'descrevem o movimento, mas o inglês não junta nenhum deles a '
          '<em>urban</em> para lhe dar nome.',
    v10why='<em>Affordable housing</em> é o termo padrão, usado por '
           'urbanistas, políticos e jornais. <em>Economical</em> descreve '
           'algo barato de manter, como um carro; <em>reasonable</em> vai '
           'com um preço ou uma renda, não com habitação; e '
           '<em>cheap-priced</em> não é inglês.',
    v11why='<em>Invest in</em>: o dinheiro investe-se <em>in</em> alguma '
           'coisa &mdash; <em>in infrastructure</em>, <em>in public '
           'transport</em>, <em>in people</em>. <em>On</em>, <em>to</em> e '
           '<em>at</em> são erros típicos de quem aprende, e nenhum vai com '
           '<em>invest</em>.',
    v12why='<em>A long commute</em>. As outras três procuram um adjetivo '
           'mais raro e um nome mais raro e falham nos dois: o inglês não '
           'chama ao percurso para o trabalho <em>transit</em>, '
           '<em>journeying</em> nem <em>travelling</em>. A combinação '
           'simples é a que quem fala inglês usa de facto.',

    sortEyebrow='Atividade 4 · A combinação, inteira',
    sortTitle='Classifica as seis combinações',
    sortHint='Arrasta cada uma para uma coluna &mdash; ou clica num elemento e '
             'depois na coluna que quiseres.',
    sortBin1='Inglês natural',
    sortBin2='Não é natural',
    sortWhy='O nome escolhe o seu verbo e o seu adjetivo. Com '
            '<em>congestion</em> usa-se <em>ease</em>, com <em>staff</em> '
            'usa-se <em>take on</em>, e <em>the gig economy</em> é um nome '
            'fixo. O congestionamento é <em>heavy</em> ou <em>severe</em>, '
            'não <em>big</em>; o trânsito é <em>heavy</em>, não '
            '<em>strong</em>; a habitação é <em>affordable</em> ou '
            '<em>cheap</em>, não <em>cheap-priced</em>. Essas três são as '
            'que quem aprende constrói a partir do dicionário, palavra a '
            'palavra. Aprende a expressão inteira e nunca terás de a '
            'construir.',

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
    actWriteBrief='Escolhe uma das três ideias e escreve sobre ela um '
                  'parágrafo de desenvolvimento para Task 2: a afirmação, o '
                  'argumento, um exemplo, a concessão. Usa pelo menos cinco '
                  'combinações do banco e sublinha cada uma. Depois relê: '
                  'uma frase sem nenhuma combinação precisa é uma '
                  'oportunidade perdida de mostrar variedade.',
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
    t1ab='<em>Job security</em>, <em>career prospects</em>, '
         '<em>work&ndash;life balance</em>: выражения, слова в которых идут '
         'комплектом. Люди <em>work remotely</em> или <em>work from '
         'home</em>, <em>suffer from burnout</em>, компания <em>takes on '
         'staff</em>. Ни одно из этих слов не редкое; экзаменатор замечает, '
         'приходят ли они в правильных сочетаниях.',
    t1an='Учите выражение целиком, <em>suffer from burnout</em>, а не только '
         'существительное <em>burnout</em>.',
    t1bh='Гибкость против изоляции',
    t1bb='Частый вопрос части 3 &mdash; какой-нибудь вариант <em>is working '
         'from home good for people?</em> Сильный ответ взвешивает обе '
         'стороны: с одной &mdash; <em>a flexible schedule</em>, с другой '
         '&mdash; коллеги, которых вы больше не видите.',
    t1bn='Одна идея, две фразы и <em>but</em> между ними.',
    t1ch='Стабильность против возможностей',
    t1cb='Когда вопрос Task 2 касается того, как меняется работа, <em>the '
         'gig economy</em> &mdash; очевидный пример. Стройте аргумент как '
         'обмен: она даёт <em>a flexible schedule</em> и отнимает <em>job '
         'security</em>; одним расширяет <em>career prospects</em>, другим '
         'сужает.',
    t1cn='Скажите, что она даёт и что отнимает. Это и есть абзац.',

    t2Eyebrow='Идея вторая',
    t2Title='Автоматизация: потерянные рабочие места против созданных',
    t2ah='Сочетания',
    t2ab='<em>Automate routine tasks</em>, <em>replace workers</em>, '
         '<em>retrain the workforce</em>; <em>productivity gains</em>, '
         '<em>low-skilled jobs</em>, <em>artificial intelligence</em>. '
         'Существительное приводит свой глагол: задачи <em>automated</em>, '
         'работники <em>displaced</em>, рабочая сила <em>retrained</em>.',
    t2an='<em>Automate</em> &mdash; глагол, которым пользуются все. '
         '<em>Automatise</em> есть в словаре, но он так редок, что звучит '
         'как перевод.',
    t2bh='Потерянные против созданных',
    t2bb='Большинство вопросов об автоматизации сводится к одному обмену: '
         'машины <em>displace</em> работников на <em>low-skilled jobs</em>, '
         'а <em>productivity gains</em> могут оплатить рабочие места, '
         'которых раньше не было. Взвешивайте обе половины. Однобокому '
         'ответу скоро нечего сказать; сбалансированный продолжается и даёт '
         'повод использовать <em>whereas</em> и <em>on the other hand</em>.',
    t2bn='Назовите, кто теряет, кто выигрывает, и что важнее.',
    t2ch='Кто кого переобучает',
    t2cb='Второй аргумент &mdash; об ответственности. Кто должен <em>retrain '
         'the workforce</em>: государство или работодатель, который её '
         '<em>replaced</em>? <em>A universal basic income</em> называет '
         'третий ответ: вместо этого платить всем регулярную сумму.',
    t2cn='Одно сочетание на позицию и три позиции на выбор.',

    t3Eyebrow='Идея третья',
    t3Title='Города: плотность против простора, машина против автобуса',
    t3ah='Сочетания',
    t3ab='<em>Urban sprawl</em>, <em>affordable housing</em>, <em>public '
         'transport</em>, <em>green spaces</em>, <em>the cost of living</em>. '
         'Городские власти <em>invest in infrastructure</em> и стараются <em>ease '
         'congestion</em>; у жителя <em>a long commute</em>, и он терпит '
         '<em>overcrowding</em>.',
    t3an='С <em>congestion</em> сочетаются глаголы <em>ease</em> и '
         '<em>reduce</em>. Движение бывает <em>heavy</em>, а не '
         '<em>strong</em>.',
    t3bh='Плотность против простора',
    t3bb='Типичный вопрос Task 2 о городах &mdash; какой-нибудь вариант '
         '<em>should cities build up or out?</em> Строительство вверх может '
         'разместить <em>affordable housing</em> ближе к центру и ограничить '
         '<em>urban sprawl</em>, но грозит <em>overcrowding</em>. '
         'Строительство вширь даёт людям больше места ценой <em>green '
         'spaces</em> и <em>a long commute</em>.',
    t3bn='Оба ответа чего-то стоят. Скажите чего.',
    t3ch='Машина против автобуса',
    t3cb='В части 3 могут спросить, как <em>ease congestion</em>. Известный '
         'аргумент: город не может выстроить себе выход из пробок, потому '
         'что новые дороги быстро заполняются новым транспортом, &mdash; '
         'значит, деньги должны идти в <em>public transport</em>. <em>Invest '
         'in public transport</em> выражает эту мысль; <em>invest in '
         'infrastructure</em> &mdash; более широкий термин.',
    t3cn='Любой из ответов можно закончить на <em>the cost of living</em>: '
         'спросите, кто в итоге платит.',

    mcaEyebrow='Задание 1 · Работа',
    mcaTitle='Какое сочетание и какое слово?',
    mcbEyebrow='Задание 2 · Автоматизация',
    mcbTitle='Существительное приводит свой глагол',
    mccEyebrow='Задание 3 · Города',
    mccTitle='Простое сочетание и есть точное',

    v1why='<em>Work remotely</em> или <em>work from home</em>. '
          '<em>Distantly</em> описывает манеру или родство &mdash; '
          '<em>smiled distantly</em>, <em>distantly related</em>, &mdash; а '
          'не способ работы. <em>At a distance</em> и <em>from a '
          'distance</em> говорят о том, насколько что-то далеко, а без '
          '<em>a</em> это вообще не английский.',
    v2why='<em>Job security</em>. <em>Work safety</em> &mdash; настоящий '
          'английский, но значит другое: каски и пожарные выходы, &mdash; в этом '
          'и промах по точности. Двух других сочетаний в английском нет.',
    v3why='<em>Suffer from burnout</em> &mdash; так же, как <em>suffer from '
          'stress</em> или <em>suffer from insomnia</em>: болезнь или '
          'состояние обычно требует <em>suffer from</em>. <em>Get into</em>, '
          '<em>fall in</em> и <em>make</em> &mdash; то, за что хватаются, '
          'когда существительное выучено без своего глагола. У английского '
          'есть и собственный глагол: медсёстры <em>burn out</em>.',
    v4why='<em>Improve career prospects</em>. <em>Career trajectory</em> '
          '&mdash; настоящий английский, но её никто не <em>augments</em>; '
          '<em>enlarge a career future</em> и <em>amplify a career '
          'chance</em> собраны по одному слову, и по-английски так не '
          'говорят. Простое сочетание и есть точное.',
    v5why='<em>Displace</em> &mdash; глагол для работников, которых '
          'вытеснило с работы что-то новое. <em>Deport</em> &mdash; это '
          'человек, высланный из страны, <em>misplace</em> &mdash; связка '
          'ключей, <em>evict</em> &mdash; жилец: три настоящих слова, каждое '
          'точно о другом.',
    v6why='<em>Productivity gains</em> или <em>productivity growth</em>. '
          '<em>Profits</em>, <em>earnings</em> и <em>winnings</em> &mdash; '
          'это деньги, которые кто-то получает, а производительность &mdash; '
          'не деньги: это то, сколько производится на вложенный труд.',
    v7why='<em>Retrain the workforce</em>: дать работникам новые навыки. '
          '<em>Reteach</em> значит заново преподать урок, <em>re-form</em> '
          '&mdash; заново построиться (о группе, о шеренге), а '
          '<em>re-school</em> &mdash; не английский глагол.',
    v8why='<em>A universal basic income</em> &mdash; название этой меры, и '
          'всё остальное звучит как догадка. <em>Wage</em> и <em>salary</em> '
          'платят за работу, а это как раз не оплата труда; <em>payment</em> '
          'же слишком общее слово, чтобы быть названием чего-либо.',
    v9why='<em>Urban sprawl</em> &mdash; устойчивый термин, и в нём есть '
          'оценка: незапланированный рост, поглощающий землю. '
          '<em>Spreading</em>, <em>stretch</em> и <em>widening</em> '
          'описывают движение, но ни одно из них английский не сочетает с '
          '<em>urban</em>, чтобы его назвать.',
    v10why='<em>Affordable housing</em> &mdash; стандартный термин, которым '
           'одинаково пользуются градостроители, политики и газеты. '
           '<em>Economical</em> описывает то, что дёшево в использовании, '
           'например машину; <em>reasonable</em> сочетается с ценой или '
           'арендной платой, а не с жильём; <em>cheap-priced</em> &mdash; '
           'вообще не английский.',
    v11why='<em>Invest in</em>: деньги вкладывают <em>in</em> что-то &mdash; '
           '<em>in infrastructure</em>, <em>in public transport</em>, <em>in '
           'people</em>. <em>On</em>, <em>to</em> и <em>at</em> &mdash; '
           'типичные ошибки учащихся, и ни один из них не сочетается с '
           '<em>invest</em>.',
    v12why='<em>A long commute</em>. Остальные три тянутся к более редкому '
           'прилагательному и более редкому существительному и промахиваются '
           'с обоими: дорогу на работу по-английски не называют '
           '<em>transit</em>, <em>journeying</em> или <em>travelling</em>. '
           'Простое сочетание &mdash; то, которым носители языка '
           'действительно пользуются.',

    sortEyebrow='Задание 4 · Сочетание целиком',
    sortTitle='Распределите шесть сочетаний',
    sortHint='Перетащите каждое в столбец &mdash; или нажмите на него, а затем '
             'на нужный столбец.',
    sortBin1='Естественный английский',
    sortBin2='Неестественно',
    sortWhy='Существительное само выбирает глагол и прилагательное. С '
            '<em>congestion</em> сочетается <em>ease</em>, со <em>staff</em> '
            '&mdash; <em>take on</em>, а <em>the gig economy</em> &mdash; '
            'устойчивое название. Пробки бывают <em>heavy</em> или '
            '<em>severe</em>, а не <em>big</em>; движение &mdash; '
            '<em>heavy</em>, а не <em>strong</em>; жильё &mdash; '
            '<em>affordable</em> или <em>cheap</em>, а не '
            '<em>cheap-priced</em>. Эти три учащийся собирает по словарю, '
            'слово за словом. Учите выражение целиком &mdash; и собирать его '
            'не придётся.',

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
    actWriteBrief='Выберите одну из трёх идей и напишите по ней абзац '
                  'основной части для Task 2: тезис, аргумент, пример, '
                  'уступка. Используйте не меньше пяти сочетаний из банка и '
                  'подчеркните каждое. Затем перечитайте: предложение без '
                  'точного сочетания &mdash; упущенный шанс показать '
                  'диапазон.',
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
    t1ab='عبارات <em>job security</em> و<em>career prospects</em> '
         'و<em>work&ndash;life balance</em> كلماتها تأتي معًا. وبالإنجليزية '
         'نقول <em>work remotely</em> أو <em>work from home</em>، '
         'و<em>suffer from burnout</em>، والشركة <em>takes on staff</em>. لا '
         'كلمة من هذه نادرة؛ ما يلاحظه الممتحن هو هل تأتي في تلازماتها '
         'الصحيحة.',
    t1an='تعلّم العبارة كاملة، <em>suffer from burnout</em>، لا الاسم '
         '<em>burnout</em> وحده.',
    t1bh='المرونة مقابل العزلة',
    t1bb='من أسئلة الجزء 3 الشائعة صيغةٌ ما من <em>is working from home good '
         'for people?</em> والإجابة القوية توازن بين الجانبين: <em>a '
         'flexible schedule</em> في جانب، والزملاء الذين لم تعد تراهم في '
         'الجانب الآخر.',
    t1bn='فكرة واحدة، وعبارتان، و<em>but</em> بينهما.',
    t1ch='الأمان مقابل الفرص',
    t1cb='حين يسأل سؤال Task 2 عن تغيّر العمل، تكون <em>the gig economy</em> '
         'مثالًا واضحًا. اعرضها كمقايضة: تمنح <em>a flexible schedule</em> '
         'وتسلب <em>job security</em>، وتوسّع <em>career prospects</em> لبعض '
         'الناس وتضيّقها لآخرين.',
    t1cn='قل ماذا يعطي وماذا يأخذ. هذه هي الفقرة.',

    t2Eyebrow='الفكرة الثانية',
    t2Title='الأتمتة: وظائف تضيع مقابل وظائف تُخلق',
    t2ah='التلازمات',
    t2ab='<em>Automate routine tasks</em> و<em>replace workers</em> و<em>retrain '
         'the workforce</em>، ثم <em>productivity gains</em> و<em>low-skilled '
         'jobs</em> و<em>artificial intelligence</em>. الاسم يجلب فعله: المهام '
         '<em>automated</em>، والعمال <em>displaced</em>، والقوى العاملة '
         '<em>retrained</em>.',
    t2an='كلمة <em>automate</em> هي الفعل الذي يستخدمه الجميع. أما '
         '<em>automatise</em> فموجودة في القاموس، لكنها نادرة إلى حدّ أنها '
         'تبدو ترجمة.',
    t2bh='ما يضيع مقابل ما يُخلق',
    t2bb='معظم أسئلة الأتمتة تعود إلى المقايضة نفسها: الآلات '
         '<em>displace</em> العمال في <em>low-skilled jobs</em>، '
         'و<em>productivity gains</em> يمكن أن تموّل وظائف لم تكن موجودة من '
         'قبل. وازن بين النصفين. الإجابة ذات الجانب الواحد تنفد منها الأفكار '
         'سريعًا، أما المتوازنة فتستمر وتمنحك سببًا لاستخدام '
         '<em>whereas</em> و<em>on the other hand</em>.',
    t2bn='سمِّ من يخسر، وسمِّ من يكسب، وقل أيّهما أهم.',
    t2ch='من يعيد تأهيل من',
    t2cb='الحجة الثانية تتعلق بالمسؤولية. هل على الدولة أن <em>retrain the '
         'workforce</em>، أم على صاحب العمل الذي <em>replaced</em> العمال؟ '
         'وعبارة <em>a universal basic income</em> تسمّي إجابة ثالثة: أن '
         'يُدفع للجميع مبلغ منتظم بدلًا من ذلك.',
    t2cn='تلازم واحد لكل موقف، وثلاثة مواقف تختار منها.',

    t3Eyebrow='الفكرة الثالثة',
    t3Title='المدن: الكثافة مقابل المساحة، والسيارة مقابل الحافلة',
    t3ah='التلازمات',
    t3ab='<em>Urban sprawl</em> و<em>affordable housing</em> و<em>public '
         'transport</em> و<em>green spaces</em> و<em>the cost of living</em>. '
         'البلدية <em>invests in infrastructure</em> وتحاول أن <em>ease '
         'congestion</em>، والساكن لديه <em>a long commute</em> ويتحمّل '
         '<em>overcrowding</em>.',
    t3an='مع <em>congestion</em> يأتي الفعل <em>ease</em> أو '
         '<em>reduce</em>. وحركة المرور <em>heavy</em>، لا <em>strong</em>.',
    t3bh='الكثافة مقابل المساحة',
    t3bb='من أسئلة Task 2 النموذجية عن المدن صيغةٌ ما من <em>should cities '
         'build up or out?</em> البناء إلى الأعلى قد يضع <em>affordable '
         'housing</em> قرب المركز ويحدّ من <em>urban sprawl</em>، مع خطر '
         '<em>overcrowding</em>. والبناء إلى الخارج يمنح الناس مساحة أكبر، '
         'على حساب <em>green spaces</em> ومع <em>a long commute</em>.',
    t3bn='كلتا الإجابتين لها ثمن. قل ما هو.',
    t3ch='السيارة مقابل الحافلة',
    t3cb='قد يسأل الجزء 3 كيف <em>ease congestion</em>. ومن الحجج المعروفة '
         'أن المدينة لا تستطيع الخروج من الازدحام بالبناء، لأن الطرق الجديدة '
         'سرعان ما تمتلئ بحركة مرور جديدة، ولذلك ينبغي أن يذهب المال إلى '
         '<em>public transport</em>. عبارة <em>invest in public '
         'transport</em> تحمل هذه الفكرة، و<em>invest in infrastructure</em> '
         'هي المصطلح الأوسع.',
    t3cn='يمكن أن تنتهي كلتا الإجابتين بـ<em>the cost of living</em>: اسأل '
         'من يدفع في النهاية.',

    mcaEyebrow='النشاط 1 · العمل',
    mcaTitle='أيّ تلازم، وأيّ كلمة؟',
    mcbEyebrow='النشاط 2 · الأتمتة',
    mcbTitle='الاسم يجلب فعله',
    mccEyebrow='النشاط 3 · المدن',
    mccTitle='التلازم البسيط هو الدقيق',

    v1why='الصحيح <em>work remotely</em> أو <em>work from home</em>. كلمة '
          '<em>distantly</em> تصف طريقة أو قرابة &mdash; <em>smiled '
          'distantly</em> و<em>distantly related</em> &mdash; لا أسلوب عمل. '
          'أما <em>at a distance</em> و<em>from a distance</em> فتتحدثان عن '
          'بُعد الشيء، ومن دون <em>a</em> ليستا إنجليزية أصلًا.',
    v2why='الصحيح <em>job security</em>. أما <em>work safety</em> فإنجليزية '
          'حقيقية لكنها تعني شيئًا آخر، الخوذ ومخارج الطوارئ، وهنا خطأ الدقة. '
          'والاثنتان الأخريان ليستا تلازمين في الإنجليزية.',
    v3why='الصحيح <em>suffer from burnout</em>، كما تقول <em>suffer from '
          'stress</em> أو <em>suffer from insomnia</em>: المرض أو الحالة '
          'يأخذ عادةً <em>suffer from</em>. أما <em>get into</em> و<em>fall '
          'in</em> و<em>make</em> فهي ما يلجأ إليه المتعلم حين يكون قد حفظ '
          'الاسم من دون فعله. وللإنجليزية فعل خاص أيضًا: الممرضات <em>burn '
          'out</em>.',
    v4why='الصحيح <em>improve career prospects</em>. عبارة <em>career '
          'trajectory</em> إنجليزية حقيقية، لكن لا أحد <em>augments</em> '
          'مسارًا مهنيًا؛ و<em>enlarge a career future</em> و<em>amplify a '
          'career chance</em> مبنيتان كلمةً كلمة، ولا تقولهما الإنجليزية. '
          'التلازم البسيط هو الدقيق.',
    v5why='الفعل <em>displace</em> هو فعل العمال الذين يدفعهم شيء جديد خارج '
          'وظائفهم. أما <em>deport</em> فلشخص يُرحَّل من بلد، '
          'و<em>misplace</em> لمجموعة مفاتيح، و<em>evict</em> لمستأجر '
          '&mdash; ثلاث كلمات حقيقية، كل منها دقيقة في شيء آخر.',
    v6why='الصحيح <em>productivity gains</em>، أو <em>productivity '
          'growth</em>. أما <em>profits</em> و<em>earnings</em> '
          'و<em>winnings</em> فهي مال يتلقاه أحد، والإنتاجية ليست مالًا: '
          'إنها مقدار ما يُنتَج مقابل العمل المبذول.',
    v7why='الصحيح <em>retrain the workforce</em>: أي منح العمال مهارات '
          'جديدة. أما <em>reteach</em> فتعني تدريس درس مرة أخرى، '
          'و<em>re-form</em> تعني إعادة التشكّل (لمجموعة أو صف)، '
          'و<em>re-school</em> ليست فعلًا تستخدمه الإنجليزية.',
    v8why='عبارة <em>a universal basic income</em> هي اسم هذه السياسة، وأي '
          'شيء آخر يبدو تخمينًا. فـ<em>wage</em> و<em>salary</em> يُدفعان '
          'مقابل العمل، وهذا بالضبط ما ليست عليه هذه الدفعة، '
          'و<em>payment</em> أعمّ من أن تكون اسمًا لشيء.',
    v9why='عبارة <em>urban sprawl</em> هي المصطلح الثابت، وفيها حكم: نموّ '
          'غير مخطط يبتلع الأرض. أما <em>spreading</em> و<em>stretch</em> '
          'و<em>widening</em> فتصف الحركة، لكن الإنجليزية لا تقرن أيًّا منها '
          'بـ<em>urban</em> لتسميتها.',
    v10why='عبارة <em>affordable housing</em> هي المصطلح المعتمد، يستخدمه '
           'المخططون والسياسيون والصحف على السواء. أما <em>economical</em> '
           'فتصف شيئًا رخيص التشغيل كالسيارة، و<em>reasonable</em> تأتي مع '
           'السعر أو الإيجار لا مع السكن، و<em>cheap-priced</em> ليست '
           'إنجليزية.',
    v11why='الصحيح <em>invest in</em>: يُستثمر المال <em>in</em> شيء ما '
           '&mdash; <em>in infrastructure</em> و<em>in public transport</em> '
           'و<em>in people</em>. أما <em>on</em> و<em>to</em> و<em>at</em> '
           'فأخطاء شائعة عند المتعلمين، ولا يأتي أيّ منها مع <em>invest</em>.',
    v12why='الصحيح <em>a long commute</em>. الخيارات الثلاثة الأخرى تلجأ إلى '
           'صفة أندر واسم أندر فتخطئ فيهما معًا: الإنجليزية لا تسمّي الطريق '
           'إلى العمل <em>transit</em> ولا <em>journeying</em> ولا '
           '<em>travelling</em>. التلازم البسيط هو ما يستخدمه المتحدثون '
           'بالإنجليزية فعلًا.',

    sortEyebrow='النشاط 4 · التلازم كاملًا',
    sortTitle='صنِّف التلازمات الستة',
    sortHint='اسحب كل تلازم إلى عمود، أو انقر عليه ثم على العمود الذي تريده.',
    sortBin1='إنجليزية طبيعية',
    sortBin2='غير طبيعية',
    sortWhy='الاسم يختار فعله وصفته. مع <em>congestion</em> يأتي '
            '<em>ease</em>، ومع <em>staff</em> يأتي <em>take on</em>، '
            'و<em>the gig economy</em> اسم ثابت. والازدحام <em>heavy</em> أو '
            '<em>severe</em> لا <em>big</em>، وحركة المرور <em>heavy</em> لا '
            '<em>strong</em>، والسكن <em>affordable</em> أو <em>cheap</em> '
            'لا <em>cheap-priced</em>. تلك الثلاثة يبنيها المتعلم من القاموس '
            'كلمةً كلمة. تعلّم العبارة كاملة ولن تضطر أبدًا إلى بنائها.',

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
    actWriteBrief='اختر إحدى الأفكار الثلاث واكتب عنها فقرة من صلب مقال Task '
                  '2: الادعاء، والحجة، ومثال، والتنازل. استخدم خمسة تلازمات '
                  'على الأقل من البنك وضع خطًا تحت كل منها. ثم أعد قراءتها: '
                  'الجملة التي لا تلازم دقيقًا فيها فرصة ضائعة لإظهار تنوّع '
                  'مفرداتك.',
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
    t1ab='<em>Job security</em>、<em>career prospects</em>、<em>work&ndash;life'
         ' balance</em>：这些短语里的词是成套出现的。英语说 <em>work remotely</em> 或 <em>work '
         'from home</em>，人会 <em>suffer from burnout</em>，公司会 <em>take on '
         'staff</em>。这些词没有一个是生僻词；考官注意的是它们有没有以正确的搭配出现。',
    t1an='要学整个短语 <em>suffer from burnout</em>，而不只是名词 <em>burnout</em>。',
    t1bh='灵活与孤立',
    t1bb='第三部分常见的一类问题是 <em>is working from home good for people?</em> '
         '的某种变体。好的回答会权衡两面：一边是 <em>a flexible schedule</em>，另一边是再也见不到的同事。',
    t1bn='一个观点，两个短语，中间一个 <em>but</em>。',
    t1ch='稳定与机会',
    t1cb='当 Task 2 的问题问到工作如何变化时，<em>the gig economy</em> '
         '是一个明显的例子。把它当作一场交换来论证：它提供 <em>a flexible schedule</em>，却拿走 <em>job '
         'security</em>；它让一些人的 <em>career prospects</em> 变宽，让另一些人的变窄。',
    t1cn='说出它给了什么、拿走了什么，这就是一段。',

    t2Eyebrow='观点二',
    t2Title='自动化：失去的岗位与新增的岗位',
    t2ah='搭配',
    t2ab='<em>Automate routine tasks</em>、<em>replace workers</em>、<em>retrain '
         'the workforce</em>；<em>productivity gains</em>、<em>low-skilled '
         'jobs</em>、<em>artificial intelligence</em>。名词自带动词：任务被 '
         '<em>automated</em>，工人被 <em>displaced</em>，劳动力被 '
         '<em>retrained</em>。',
    t2an='<em>Automate</em> 是人人都用的动词。<em>Automatise</em> 词典里有，但罕见到听起来像翻译。',
    t2bh='失去与新增',
    t2bb='大多数关于自动化的问题都归结为同一种交换：机器在 <em>low-skilled jobs</em> 中 '
         '<em>displace</em> 工人，而 <em>productivity gains</em> '
         '可以为以前不存在的工作买单。两半都要权衡。一边倒的回答很快就没话可说；平衡的回答能继续说下去，也让你有理由用上 '
         '<em>whereas</em> 和 <em>on the other hand</em>。',
    t2bn='说出谁受损、谁受益，再说哪个更重要。',
    t2ch='谁来培训谁',
    t2cb='第二个论点关乎责任。应该由国家来 <em>retrain the workforce</em>，还是由 '
         '<em>replaced</em> 了这些工人的雇主来做？<em>A universal basic income</em> '
         '说出了第三种答案：改为定期给每个人发一笔钱。',
    t2cn='每种立场配一个搭配，有三种立场可选。',

    t3Eyebrow='观点三',
    t3Title='城市：密度与空间，汽车与公交',
    t3ah='搭配',
    t3ab='<em>Urban sprawl</em>、<em>affordable housing</em>、<em>public '
         'transport</em>、<em>green spaces</em>、<em>the cost of living</em>。市'
         '政府 <em>invests in infrastructure</em>，努力 <em>ease congestion</em>；'
         '居民有 <em>a long commute</em>，还要忍受 <em>overcrowding</em>。',
    t3an='和 <em>congestion</em> 搭配的动词是 <em>ease</em> 或 <em>reduce</em>。交通是 '
         '<em>heavy</em>，不是 <em>strong</em>。',
    t3bh='密度与空间',
    t3bb='Task 2 关于城市的典型问题是 <em>should cities build up or out?</em> '
         '的某种变体。向上建可以把 <em>affordable housing</em> 放在市中心附近，并限制 <em>urban '
         'sprawl</em>，但有 <em>overcrowding</em> 的风险。向外建给人更多空间，代价是 <em>green '
         'spaces</em> 和 <em>a long commute</em>。',
    t3bn='两种回答都有代价。说出是什么。',
    t3ch='汽车与公交',
    t3cb='第三部分可能会问如何 <em>ease congestion</em>。一个有名的论点是：城市没法靠修路摆脱拥堵，因为新路很快就会被新'
         '增的车流填满，所以钱应该投向 <em>public transport</em>。<em>Invest in public '
         'transport</em> 说出了这个观点；<em>invest in infrastructure</em> 是更宽泛的说法。',
    t3cn='两种回答都可以落到 <em>the cost of living</em> 上：问一问最后是谁在买单。',

    mcaEyebrow='练习 1 · 工作',
    mcaTitle='哪个搭配，哪个词？',
    mcbEyebrow='练习 2 · 自动化',
    mcbTitle='名词自带动词',
    mccEyebrow='练习 3 · 城市',
    mccTitle='朴素的搭配才是准确的搭配',

    v1why='<em>Work remotely</em>，或者 <em>work from '
          'home</em>。<em>Distantly</em> 描述的是一种态度或亲缘关系——<em>smiled '
          'distantly</em>、<em>distantly related</em>——而不是一种工作方式。<em>At a '
          'distance</em> 和 <em>from a distance</em> 说的是某物有多远，而且少了 <em>a</em> '
          '就根本不是英语。',
    v2why='<em>Job security</em>。<em>Work safety</em> 是真实的英语，但意思不同——'
          '指安全帽和紧急出口——这就是用词不准的失误。另外两个在英语里根本不是'
          '搭配。',
    v3why='<em>Suffer from burnout</em>，就像 <em>suffer from stress</em> 或 '
          '<em>suffer from insomnia</em>：疾病或状态通常用 <em>suffer '
          'from</em>。<em>Get into</em>、<em>fall in</em> 和 <em>make</em> '
          '是只学了名词、没学它的动词时会抓来用的词。英语还有一个现成的动词：护士们 <em>burn out</em>。',
    v4why='<em>Improve career prospects</em>。<em>Career trajectory</em> '
          '是地道的英语，但没有人会 <em>augment</em> 它；<em>enlarge a career future</em> '
          '和 <em>amplify a career chance</em> '
          '是一个词一个词拼出来的，英语不这么说。朴素的搭配才是准确的搭配。',
    v5why='<em>Displace</em> 是指工人被新事物挤出工作岗位的动词。<em>Deport</em> '
          '是把人驱逐出境，<em>misplace</em> 是放错地方的一串钥匙，<em>evict</em> '
          '是被赶走的租户——三个真实存在的词，各自精确地指别的事。',
    v6why='<em>Productivity gains</em>，或者 <em>productivity '
          'growth</em>。<em>Profits</em>、<em>earnings</em> 和 '
          '<em>winnings</em> 都是某人收到的钱，而生产率不是钱：它是投入的劳动能产出多少。',
    v7why='<em>Retrain the workforce</em>：让工人掌握新技能。<em>Reteach</em> '
          '是把一课再教一遍，<em>re-form</em> 是重新组成（一个团体、一个队列），而 <em>re-school</em> '
          '不是英语里用的动词。',
    v8why='<em>A universal basic income</em> '
          '是这项政策的名称，说成别的都像是在猜。<em>Wage</em> 和 <em>salary</em> '
          '是为工作支付的，而这恰恰不是；<em>payment</em> 又太笼统，当不了任何东西的名称。',
    v9why='<em>Urban sprawl</em> 是固定术语，而且带有评判：无规划、吞噬土地的扩张。<em>Spreading</em>、'
          '<em>stretch</em> 和 <em>widening</em> 描述的是这种移动，但英语不会用其中任何一个和 '
          '<em>urban</em> 搭配来称呼它。',
    v10why='<em>Affordable housing</em> 是标准术语，规划者、政界人士和报纸都这么用。<em>Economical<'
           '/em> 形容用起来省钱的东西，比如汽车；<em>reasonable</em> '
           '搭配价格或租金，不搭配住房；<em>cheap-priced</em> 不是英语。',
    v11why='<em>Invest in</em>：钱是投 <em>in</em> 某样东西——<em>in '
           'infrastructure</em>、<em>in public transport</em>、<em>in '
           'people</em>。<em>On</em>、<em>to</em> 和 <em>at</em> '
           '是学习者的常见错误，没有一个能和 <em>invest</em> 搭配。',
    v12why='<em>A long commute</em>。另外三个都去找更生僻的形容词和名词，结果两头落空：英语不会把上班的路程叫作 '
           '<em>transit</em>、<em>journeying</em> 或 '
           '<em>travelling</em>。朴素的搭配才是说英语的人真正用的。',

    sortEyebrow='练习 4 · 完整的搭配',
    sortTitle='给这六个搭配分类',
    sortHint='把每一项拖到一栏里——或者先点一项，再点你想放进的那一栏。',
    sortBin1='地道的英语',
    sortBin2='不地道',
    sortWhy='名词自己挑选动词和形容词。<em>Congestion</em> 搭配 '
            '<em>ease</em>，<em>staff</em> 搭配 <em>take on</em>，<em>the gig '
            'economy</em> 是固定名称。拥堵是 <em>heavy</em> 或 <em>severe</em>，不是 '
            '<em>big</em>；交通是 <em>heavy</em>，不是 <em>strong</em>；住房是 '
            '<em>affordable</em> 或 <em>cheap</em>，不是 '
            '<em>cheap-priced</em>。那三个是学习者查着词典一个词一个词拼出来的。把整个短语学下来，就永远不用自己拼。',

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
    actWriteBrief='从三个观点中选一个，为它写一段 Task 2 的主体段落：论点、论证、例子、让步。至少用上词库里的五个搭配，并在每个'
                  '下面画线。然后重读一遍：一个句子里没有任何精准的搭配，就是错过了一次展示词汇广度的机会。',
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
    t1ab='<em>Job security</em>、<em>career prospects</em>、<em>work&ndash;life'
         ' balance</em>：語がセットでやって来る表現です。英語では <em>work remotely</em> や '
         '<em>work from home</em> と言い、人は <em>suffer from burnout</em>、会社は '
         '<em>takes on staff</em>。どの語も珍しくはありません。試験官が気づくのは、それが正しい組み合わせで出てくるかどう'
         'かです。',
    t1an='名詞の <em>burnout</em> だけでなく、<em>suffer from burnout</em> '
         'という表現ごと覚えましょう。',
    t1bh='柔軟さ対孤立',
    t1bb='パート3でよくある質問の一つは、<em>is working from home good for people?</em> '
         'の何らかの形です。強い答えは両側を比べます：一方に <em>a flexible '
         'schedule</em>、もう一方にもう会わなくなった同僚。',
    t1bn='一つのアイデアに二つのフレーズ、その間に <em>but</em>。',
    t1ch='安定対チャンス',
    t1cb='Task 2 の問題が仕事の変化について問うとき、<em>the gig economy</em> '
         'はわかりやすい例です。取引として論じましょう：<em>a flexible schedule</em> を与え、<em>job '
         'security</em> を奪う。ある人の <em>career prospects</em> を広げ、別の人のものを狭める。',
    t1cn='何を与え、何を奪うかを言う。それが段落です。',

    t2Eyebrow='アイデア 2',
    t2Title='自動化：失われる仕事対生まれる仕事',
    t2ah='組み合わせ',
    t2ab='<em>Automate routine tasks</em>、<em>replace workers</em>、<em>retrain '
         'the workforce</em>；<em>productivity gains</em>、<em>low-skilled '
         'jobs</em>、<em>artificial intelligence</em>。名詞が動詞を連れてきま'
         'す。作業は <em>automated</em>、労働者は <em>displaced</em>、労働力は '
         '<em>retrained</em> されます。',
    t2an='<em>Automate</em> が誰もが使う動詞です。<em>Automatise</em> '
         'も辞書にはありますが、翻訳のように聞こえるほどまれです。',
    t2bh='失われる対生まれる',
    t2bb='自動化についての問題のほとんどは同じ取引に行き着きます：機械が <em>low-skilled jobs</em> の労働者を '
         '<em>displace</em> し、<em>productivity gains</em> '
         'がそれまでなかった仕事の元手になりうる。両方の半分を比べましょう。一方的な答えはすぐに言うことがなくなりますが、バランスの取れた答えは'
         '続けられ、<em>whereas</em> や <em>on the other hand</em> を使う理由も生まれます。',
    t2bn='誰が失い、誰が得るかを言い、どちらが重要かを言いましょう。',
    t2ch='誰が誰を再訓練するか',
    t2cb='二つ目の議論は責任についてです。<em>retrain the workforce</em> すべきなのは国か、それとも労働者を '
         '<em>replaced</em> した雇用主か？ <em>A universal basic income</em> '
         'は第三の答えに名前を与えます：代わりに全員に定期的に一定額を払うこと。',
    t2cn='立場ごとに組み合わせが一つ、選べる立場は三つ。',

    t3Eyebrow='アイデア 3',
    t3Title='都市：密度対空間、車対バス',
    t3ah='組み合わせ',
    t3ab='<em>Urban sprawl</em>、<em>affordable housing</em>、<em>public '
         'transport</em>、<em>green spaces</em>、<em>the cost of living</em>。'
         '自治体は <em>invests in infrastructure</em> して <em>ease '
         'congestion</em> しようとし、住民は <em>a long commute</em> を抱え、'
         '<em>overcrowding</em> に耐えます。',
    t3an='<em>congestion</em> と組む動詞は <em>ease</em> か <em>reduce</em>。交通量は '
         '<em>heavy</em> で、<em>strong</em> ではありません。',
    t3bh='密度対空間',
    t3bb='都市についての典型的な Task 2 の問題は、<em>should cities build up or out?</em> '
         'の何らかの形です。上に建てれば、中心部の近くに <em>affordable housing</em> を置き、<em>urban '
         'sprawl</em> を抑えられるかもしれませんが、<em>overcrowding</em> '
         'の危険があります。外に広げれば人々により広い空間を与えますが、その代わりに <em>green spaces</em> '
         'を失い、<em>a long commute</em> を招きます。',
    t3bn='どちらの答えにも代償があります。それが何かを言いましょう。',
    t3ch='車対バス',
    t3cb='パート3では <em>ease congestion</em> の方法を聞かれるかもしれません。よく知られた議論に、新しい道路はすぐ新'
         'しい車で埋まるので、都市は道路を造って渋滞から抜け出すことはできない、というものがあります。だからお金は <em>public '
         'transport</em> に回すべきだ、と。<em>Invest in public transport</em> '
         'がこの主張を運び、<em>invest in infrastructure</em> はより広い言い方です。',
    t3cn='どちらの答えも <em>the cost of living</em> で締めくくれます：最後に誰が払うのかを問いましょう。',

    mcaEyebrow='演習 1 · 仕事',
    mcaTitle='どの組み合わせで、どの語か？',
    mcbEyebrow='演習 2 · 自動化',
    mcbTitle='名詞が動詞を連れてくる',
    mccEyebrow='演習 3 · 都市',
    mccTitle='平易な組み合わせこそ正確',

    v1why='<em>Work remotely</em>、または <em>work from '
          'home</em>。<em>Distantly</em> は態度や血縁を表す語で――<em>smiled '
          'distantly</em>、<em>distantly related</em>――働き方ではありません。<em>At a '
          'distance</em> と <em>from a distance</em> '
          'は何かがどれだけ離れているかを言う表現で、<em>a</em> がなければそもそも英語ではありません。',
    v2why='<em>Job security</em>。<em>Work safety</em> は実在する英語ですが意味が'
          '違います――ヘルメットや非常口のことで、ここが正確さの落とし穴です。ほか'
          'の二つは英語にある組み合わせではありません。',
    v3why='<em>Suffer from burnout</em>。<em>suffer from stress</em> や '
          '<em>suffer from insomnia</em> と同じで、病気や状態にはふつう <em>suffer '
          'from</em> を使います。<em>Get into</em>、<em>fall in</em>、<em>make</em> '
          'は、名詞を動詞なしで覚えたときに手を伸ばしてしまう語です。英語には専用の動詞もあります：看護師は <em>burn '
          'out</em> します。',
    v4why='<em>Improve career prospects</em>。<em>Career trajectory</em> '
          'は本物の英語ですが、それを <em>augment</em> する人はいません。<em>enlarge a career '
          'future</em> や <em>amplify a career chance</em> '
          'は一語ずつ組み立てたもので、英語ではそう言いません。平易な組み合わせこそ正確です。',
    v5why='<em>Displace</em> は、何か新しいものに仕事から押し出される労働者に使う動詞です。<em>Deport</em> '
          'は国外に追放される人、<em>misplace</em> は置き忘れた鍵、<em>evict</em> '
          'は立ち退かされる借家人――どれも本物の語で、それぞれ別のものについて正確です。',
    v6why='<em>Productivity gains</em>、または <em>productivity '
          'growth</em>。<em>Profits</em>、<em>earnings</em>、<em>winnings</em> '
          'は誰かが受け取るお金ですが、生産性はお金ではなく、投じた労働でどれだけ生み出せるかです。',
    v7why='<em>Retrain the workforce</em>：労働者に新しい技能を身につけさせること。<em>Reteach</em'
          '> は授業をもう一度教えること、<em>re-form</em> は（集団や列を）組み直すことで、<em>re-school</em'
          '> は英語で使われる動詞ではありません。',
    v8why='<em>A universal basic income</em> '
          'がこの政策の名前で、ほかの言い方は当て推量に聞こえます。<em>Wage</em> と <em>salary</em> '
          'は労働への対価で、これはまさにそうではないもの。<em>payment</em> は一般的すぎて、何かの名前にはなりません。',
    v9why='<em>Urban sprawl</em> が決まった用語で、評価も含んでいます：計画のない、土地を飲み込む成長。<em>Sprea'
          'ding</em>、<em>stretch</em>、<em>widening</em> は広がる動きを表しますが、英語ではどれも '
          '<em>urban</em> と組み合わせてそれを呼びません。',
    v10why='<em>Affordable housing</em> が標準的な用語で、都市計画の専門家も政治家も新聞も使います。<em>Eco'
           'nomical</em> は車のように維持費の安いものを表し、<em>reasonable</em> '
           'は住宅ではなく値段や家賃と組みます。<em>cheap-priced</em> は英語ではありません。',
    v11why='<em>Invest in</em>：お金は何か <em>in</em> 投資されます――<em>in '
           'infrastructure</em>、<em>in public transport</em>、<em>in '
           'people</em>。<em>On</em>、<em>to</em>、<em>at</em> は学習者によくある誤りで、どれも '
           '<em>invest</em> とは組みません。',
    v12why='<em>A long commute</em>。ほかの三つは、よりまれな形容詞とよりまれな名詞に手を伸ばして、両方で外しています：'
           '英語では通勤の道のりを <em>transit</em>、<em>journeying</em>、<em>travelling</'
           'em> とは呼びません。平易な組み合わせこそ、英語の話し手が実際に使うものです。',

    sortEyebrow='演習 4 · 組み合わせを丸ごと',
    sortTitle='六つの組み合わせを分類しましょう',
    sortHint='それぞれを列にドラッグしてください。または項目をクリックしてから、'
             '入れたい列をクリックします。',
    sortBin1='自然な英語',
    sortBin2='不自然',
    sortWhy='名詞が自分の動詞と形容詞を選びます。<em>congestion</em> には '
            '<em>ease</em>、<em>staff</em> には <em>take on</em>、そして <em>the '
            'gig economy</em> は決まった名前です。渋滞は <em>heavy</em> か <em>severe</em> '
            'で <em>big</em> ではなく、交通量は <em>heavy</em> で <em>strong</em> '
            'ではなく、住宅は <em>affordable</em> か <em>cheap</em> で '
            '<em>cheap-priced</em> ではありません。その三つは、学習者が辞書から一語ずつ組み立てたものです。表現ごと覚え'
            'れば、組み立てる必要はありません。',

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
    actWriteBrief='三つのアイデアから一つ選び、それについて Task 2 の本論の段落を書きましょう：主張、論拠、例、譲歩。語彙集から'
                  '少なくとも五つの組み合わせを使い、それぞれに下線を引きます。そして読み返しましょう：正確な組み合わせが一つもない文は'
                  '、語彙の幅を見せる機会を逃しています。',
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
