# -*- coding: utf-8 -*-
"""Interface strings for IELTS Reading: Matching Headings.

Ten languages: English, German and Spanish from the start; French,
Italian, Portuguese, Russian, Arabic, Chinese and Japanese added on
2026-09-24 (conventions in `ielts_langs.py`).

Same split as the rest of the IELTS route (HOUSE-STYLE §8): the rule and the
reason travel, the English under test does not. The paragraphs and the
headings in the items stay English in every gloss — a German rendering of the
paragraph would hand over the answer, because the whole skill is reading an
English paragraph and deciding which English heading covers it.

The explanations translate, and where one cites a phrase from the paragraph
(<em>Consider</em>, <em>A word of caution</em>) the citation stays English
inside the translated sentence, so the learner is shown the words that
decided it rather than a translation of them.

The sort explanation travels through a key (`sortWhy`) rather than as a
sentence in the builder, so it translates with the rest of the slide. The
six sort items themselves are the English being sorted and stay English,
as the sibling deck's do.
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
    coverTitle='Matching <em>Headings</em>',
    coverSub='A Reading task that does not run in passage order '
             '&mdash; so the technique is different',
    chipLevel='C1 · Advanced', chipFocus='Reading · both modules',
    chipCount='18 points',

    t1Eyebrow='Before you start',
    t1Title='More headings than paragraphs, and no order to lean on',
    t1ah='The shape of the task',
    t1ab='A list of headings numbered i, ii, iii, and a passage with '
         'paragraphs lettered A to G. Each paragraph takes one heading. '
         'There are always more headings than paragraphs, so two or three '
         'are never used &mdash; and they are written to be tempting.',
    t1an='Seven paragraphs, ten headings, three decoys. That is the usual '
         'arithmetic.',
    t1bh='A type that jumps',
    t1bb='Most question types follow the passage. This one, like Matching '
         'Information, does not: heading i can belong to paragraph F, and '
         'the order of the list tells you nothing about where to look. '
         'Answering four tells you nothing about the fifth.',
    t1bn='It usually comes first on its passage, before the questions that '
         'do run in order.',
    t1ch='Read the paragraph before the list',
    t1cb='The trap is to read ten headings first and then hunt for them in '
         'the text &mdash; ten ideas in your head, all looking for a home. '
         'Read paragraph A, say in your own words what it is about, and only '
         'then look at the list for the heading that says the same.',
    t1cn='Your own summary first, the list second. Every time.',

    t2Eyebrow='Before you start',
    t2Title='Ask what the paragraph is doing, not what it is about',
    t2ah='Function over topic',
    t2ab='Two paragraphs can share a topic and do different jobs with it: '
         'one introduces a problem, the next gives an example, a third '
         'weighs two views, a fourth proposes a fix. The heading names the '
         'job. A heading that only names the topic fits half the passage.',
    t2an='Introducing, illustrating, comparing, warning, proposing. Five '
         'verbs cover most of what a paragraph does.',
    t2bh='The topic sentence moves around',
    t2bb='It is usually first, and the people who write these tests know '
         'you know that. A paragraph can open with an example and state its '
         'point at the end, or bury it in the middle after a concession. '
         'Read to the last sentence before you decide.',
    t2bn='A heading that matches only the first sentence is the commonest '
         'wrong answer on the paper.',
    t2ch='A repeated word is bait',
    t2cb='If a heading uses a word that sits in the paragraph, be '
         'suspicious. The right heading paraphrases: it says what the '
         'paragraph means in words the paragraph did not use. The wrong '
         'ones are built from its vocabulary, so that a candidate scanning '
         'for words finds them.',
    t2cn='Matching a word takes a second. Matching an idea takes a '
         'sentence. Spend the sentence.',

    t3Eyebrow='Before you start',
    t3Title='Sure ones first, cross it out, two-fit goes last',
    t3ah='Do the certain ones first',
    t3ab='Some paragraphs have one obvious heading. Take them, whatever '
         'letter they carry. Every certain match shortens the list for the '
         'ones you are not sure of, and the hardest paragraph is often '
         'decided by what is left rather than by what it says.',
    t3an='Do not work A to G. Work easy to hard.',
    t3bh='Cross it out once used',
    t3bb='Each heading is used once. Strike it off the list the moment you '
         'commit to it, and strike off the paragraph too. A list that still '
         'shows ten headings with two paragraphs to go is asking '
         'you to reconsider every decision you have already made.',
    t3bn='Pencil, not memory. Under time you will forget which you have '
         'used.',
    t3ch='When a heading fits two paragraphs',
    t3cb='Leave it. Do the rest, and come back with the list shorter. Then '
         'ask of each paragraph: does this heading cover the whole of it, or '
         'just one sentence? One of the two has a better heading elsewhere, '
         'and elimination decides what reading could not.',
    t3cn='Too general and too specific both fail. The right heading fits '
         'the paragraph and fits nothing else.',

    mcaEyebrow='Activity 1 · The main idea',
    mcaTitle='Read the paragraph. Which heading covers all of it?',
    mcbEyebrow='Activity 2 · What is it doing?',
    mcbTitle='Name the job, not the subject',
    mccEyebrow='Activity 3 · Order of attack',
    mccTitle='Which move, and which heading?',

    r1why='The crabs and the one per cent are details; the oceans as a '
          'whole are more than the paragraph covers. The one heading that '
          'holds for every sentence is the size set against the life.',
    r2why='The first station, the second, the foundations underfoot: every '
          'sentence is about one site carrying two stations. The passengers '
          'are a detail, and the demolition is never explained.',
    r3why='Handwriting copied, space left for capitals, copies sold as '
          'manuscripts &mdash; three details, one idea: printing pretending '
          'not to be printing. The history of printing would fit any '
          'paragraph in the passage.',
    r4why='The year and the first reaction are single sentences. The '
          'paragraph is the whole arc &mdash; ban, complaint, success, and '
          'the complainers priced out. The heading has to carry the ending.',
    r5why='<em>Consider</em> is the giveaway: the paragraph is holding up '
          'one case. The week in port and the engine are its details; world '
          'trade is the topic of the passage, not the job of this paragraph.',
    r6why='It opens by refusing a conclusion and closes with a '
          'recommendation. That is a defence. The families and the weak '
          'results are the evidence, not the point.',
    r7why='<em>A word of caution</em> tells you the function in four words. '
          'The paragraph is not reporting the figures or the landline '
          'households; it is telling you how far to trust them.',
    r8why='Supporters, critics, and a last sentence about the two never '
          'meeting. The villages and the electricity are what each side '
          'says; the heading has to name the standoff.',
    r9why='Certainty first, whatever the letter. Each sure match removes a '
          'heading from the list, and the difficult paragraphs are decided '
          'by what is left.',
    r10why='Ask what each paragraph is doing. C is about the cost; E '
           'mentions the cost and then does something else. A heading that '
           'fits one sentence of E fits all of C.',
    r11why='Three cities, the result in each, none reversed: the heading has '
           'to cover all three and the outcome. Transport policy covers too '
           'much, and one city covers too little.',
    r12why='Five headings are already spent. Cross them out and the last two '
           'paragraphs are choosing from five, not ten. Rereading costs the '
           'time you do not have.',

    sortEyebrow='Activity 4 · Right heading, or trap?',
    sortTitle='Sort the six signals',
    sortHint='Drag each one into a column &mdash; or click an item, then the '
             'column you want it in.',
    sortBin1='Points to the right heading',
    sortBin2='A trap',
    sortWhy='Everything in the left column describes a heading that <strong>fits '
            'the paragraph as a whole</strong>: it names the job, it holds for '
            'every sentence, and it does not depend on any one of them. The '
            'right column holds the three ways a heading looks right without '
            'being right &mdash; a shared word, a match with the opening '
            'line only, a fit that another paragraph could claim just as '
            'well. Each is a decoy doing exactly what it was written to do.',

    actTitle='Write the headings yourself',
    actUse='Use at least three:',
    actSpeakBrief='In pairs, with any article to hand. One of you writes a '
                  'heading for each paragraph, then adds two extra headings '
                  'that fit nothing &mdash; one that repeats a word from the '
                  'text, one that is too general. Shuffle the list, swap, '
                  'and match. Then argue every match.',
    actSpeak1='Whoever matches must say what each paragraph is doing &mdash; '
              'introducing, comparing, warning &mdash; before naming its '
              'heading.',
    actSpeak2='For each decoy, say which paragraph it was written to tempt '
              'you towards, and what gives it away.',
    actSpeak3='Find one heading in your partner&rsquo;s set that fits two '
              'paragraphs, and rewrite it so that it fits only one.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Take a passage of three paragraphs and write a heading '
                  'for each. Under every heading, quote the one sentence '
                  'that proves it is the main idea, and say in a line why '
                  'the heading covers the whole paragraph rather than that '
                  'sentence alone.',
    actPlaceholder='Paragraph A — heading: … The sentence that proves it: …',
)

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Matching <em>Headings</em>',
    coverSub='Eine Reading-Aufgabe, die nicht in Textreihenfolge läuft '
             '&mdash; und deshalb eine andere Technik braucht',
    chipLevel='C1 · Fortgeschritten', chipFocus='Reading · beide Module',
    chipCount='18 Punkte',

    t1Eyebrow='Bevor du beginnst',
    t1Title='Mehr Überschriften als Absätze, und keine Reihenfolge als Halt',
    t1ah='Der Aufbau der Aufgabe',
    t1ab='Eine Liste von Überschriften, nummeriert i, ii, iii, und ein Text '
         'mit Absätzen A bis G. Jeder Absatz bekommt eine Überschrift. Es '
         'gibt immer mehr Überschriften als Absätze, zwei oder drei bleiben '
         'also übrig &mdash; und die sind so geschrieben, dass sie locken.',
    t1an='Sieben Absätze, zehn Überschriften, drei Köder. Das ist die übliche '
         'Rechnung.',
    t1bh='Ein Typ, der springt',
    t1bb='Die meisten Fragetypen folgen dem Text. Dieser nicht, genauso wenig '
         'wie Matching Information: Überschrift i '
         'kann zu Absatz F gehören, und die Reihenfolge der Liste verrät '
         'nichts darüber, wo du suchen musst. Vier gelöst heißt nicht, dass '
         'du weißt, wo die fünfte steht.',
    t1bn='Er kommt meist als Erstes zu seinem Text, vor den Fragen, die der '
         'Reihe nach laufen.',
    t1ch='Erst der Absatz, dann die Liste',
    t1cb='Die Falle: erst zehn Überschriften lesen und sie dann im Text '
         'suchen &mdash; zehn Ideen im Kopf, die alle ein Zuhause wollen. '
         'Lies Absatz A, sag mit eigenen Worten, worum es geht, und such '
         'erst dann in der Liste die Überschrift, die dasselbe sagt.',
    t1cn='Erst deine Zusammenfassung, dann die Liste. Jedes Mal.',

    t2Eyebrow='Bevor du beginnst',
    t2Title='Frag, was der Absatz tut, nicht wovon er handelt',
    t2ah='Funktion vor Thema',
    t2ab='Zwei Absätze können dasselbe Thema haben und Verschiedenes damit '
         'tun: einer führt ein Problem ein, der nächste bringt ein Beispiel, '
         'ein dritter wägt zwei Sichten ab, ein vierter schlägt eine Lösung '
         'vor. Die Überschrift nennt die Aufgabe. Eine, die nur das Thema '
         'nennt, passt auf den halben Text.',
    t2an='Einführen, veranschaulichen, vergleichen, warnen, vorschlagen. '
         'Fünf Verben decken das meiste ab, was ein Absatz tut.',
    t2bh='Der Kernsatz wandert',
    t2bb='Meist steht er vorn, und wer diese Tests schreibt, weiß, dass du '
         'das weißt. Ein Absatz kann mit einem Beispiel beginnen und seinen '
         'Punkt am Ende machen, oder ihn nach einem Zugeständnis in der '
         'Mitte verstecken. Lies bis zum letzten Satz, bevor du '
         'entscheidest.',
    t2bn='Eine Überschrift, die nur zum ersten Satz passt, ist die häufigste '
         'falsche Antwort der ganzen Prüfung.',
    t2ch='Ein wiederholtes Wort ist ein Köder',
    t2cb='Steht in einer Überschrift ein Wort aus dem Absatz, sei '
         'misstrauisch. Die richtige Überschrift paraphrasiert: Sie sagt, '
         'was der Absatz meint, mit Wörtern, die der Absatz nicht benutzt. '
         'Die falschen sind aus seinem Wortschatz gebaut, damit sie findet, '
         'wer nach Wörtern sucht.',
    t2cn='Ein Wort abgleichen dauert eine Sekunde. Eine Idee abgleichen '
         'dauert einen Satz. Gib den Satz aus.',

    t3Eyebrow='Bevor du beginnst',
    t3Title='Die sicheren zuerst, streichen, Doppeltreffer zuletzt',
    t3ah='Erst die sicheren',
    t3ab='Manche Absätze haben eine offensichtliche Überschrift. Nimm sie, '
         'egal welchen Buchstaben sie tragen. Jeder sichere Treffer kürzt '
         'die Liste für die unsicheren, und der schwerste Absatz wird oft '
         'durch das entschieden, was übrig bleibt, nicht durch das, was er '
         'sagt.',
    t3an='Nicht A bis G. Leicht bis schwer.',
    t3bh='Streichen, sobald vergeben',
    t3bb='Jede Überschrift wird einmal benutzt. Streich sie von der Liste, '
         'sobald du dich festlegst, und streich den Absatz gleich mit. Eine '
         'Liste, die für die letzten zwei Absätze noch zehn Überschriften '
         'zeigt, verlangt, dass du jede Entscheidung noch einmal '
         'überdenkst.',
    t3bn='Bleistift, nicht Gedächtnis. Unter Zeitdruck vergisst du, welche '
         'schon weg sind.',
    t3ch='Wenn eine Überschrift auf zwei Absätze passt',
    t3cb='Lass sie liegen. Mach den Rest und komm mit kürzerer Liste '
         'zurück. Dann frag bei jedem der beiden Absätze: Deckt die '
         'Überschrift den ganzen Absatz ab oder nur einen Satz? Einer der '
         'beiden hat woanders eine bessere, und das Ausschließen '
         'entscheidet, was Lesen nicht konnte.',
    t3cn='Zu allgemein und zu speziell scheitern beide. Die richtige '
         'Überschrift passt auf den Absatz und auf nichts sonst.',

    mcaEyebrow='Aktivität 1 · Die Hauptidee',
    mcaTitle='Lies den Absatz. Welche Überschrift deckt ihn ganz ab?',
    mcbEyebrow='Aktivität 2 · Was tut er?',
    mcbTitle='Nenn die Aufgabe, nicht das Thema',
    mccEyebrow='Aktivität 3 · Reihenfolge des Angriffs',
    mccTitle='Welcher Zug, und welche Überschrift?',

    r1why='Die Krabben und das eine Prozent sind Details; die Ozeane als '
          'Ganzes sind mehr, als der Absatz abdeckt. Die eine Überschrift, '
          'die für jeden Satz gilt, setzt die Größe gegen das Leben.',
    r2why='Der erste Bahnhof, der zweite, die Fundamente unter den Füßen: '
          'Jeder Satz handelt von einem Ort mit zwei Bahnhöfen. Die '
          'Fahrgäste sind ein Detail, und der Abriss wird nie erklärt.',
    r3why='Kopierte Handschrift, Platz für Initialen, als Manuskripte '
          'verkaufte Exemplare &mdash; drei Details, eine Idee: Druck, der '
          'so tut, als wäre er keiner. Die Geschichte des Buchdrucks passt '
          'auf jeden Absatz des Textes.',
    r4why='Das Jahr und die erste Reaktion sind einzelne Sätze. Der Absatz '
          'ist der ganze Bogen &mdash; Verbot, Klage, Erfolg, und die '
          'Kläger, die sich die Straße nicht mehr leisten können. Die '
          'Überschrift muss das Ende tragen.',
    r5why='<em>Consider</em> verrät es: Der Absatz hält einen Fall hoch. Die '
          'Woche im Hafen und der Motor sind seine Details; der Welthandel '
          'ist das Thema des Textes, nicht die Aufgabe dieses Absatzes.',
    r6why='Er beginnt damit, einen Schluss abzulehnen, und endet mit einer '
          'Empfehlung. Das ist eine Verteidigung. Die Familien und die '
          'schwachen Ergebnisse sind die Belege, nicht der Punkt.',
    r7why='<em>A word of caution</em> nennt die Funktion in vier Wörtern. '
          'Der Absatz berichtet weder die Zahlen noch die Festnetzhaushalte; '
          'er sagt dir, wie weit du ihnen trauen darfst.',
    r8why='Befürworter, Kritiker, und ein letzter Satz darüber, dass die '
          'beiden sich nie begegnen. Die Dörfer und der Strom sind, was jede '
          'Seite sagt; die Überschrift muss die Pattsituation benennen.',
    r9why='Sicherheit zuerst, egal welcher Buchstabe. Jeder sichere Treffer '
          'nimmt eine Überschrift von der Liste, und die schweren Absätze '
          'entscheidet, was übrig ist.',
    r10why='Frag, was jeder Absatz tut. C handelt von den Kosten; E erwähnt '
           'die Kosten und tut dann etwas anderes. Eine Überschrift, die auf '
           'einen Satz von E passt, passt auf ganz C.',
    r11why='Drei Städte, das Ergebnis in jeder, keine hat es zurückgenommen: '
           'Die Überschrift muss alle drei und den Ausgang abdecken. '
           'Verkehrspolitik deckt zu viel ab, eine Stadt zu wenig.',
    r12why='Fünf Überschriften sind schon vergeben. Streich sie, und die '
           'letzten zwei Absätze wählen aus fünf statt aus zehn. Neu lesen '
           'kostet die Zeit, die du nicht hast.',

    sortEyebrow='Aktivität 4 · Richtige Überschrift oder Falle?',
    sortTitle='Sortiere die sechs Signale',
    sortHint='Zieh jedes in eine Spalte &mdash; oder klicke ein Element an und '
             'dann die Spalte, in die es soll.',
    sortBin1='Deutet auf die richtige Überschrift',
    sortBin2='Eine Falle',
    sortWhy='Die linke Spalte beschreibt durchweg eine Überschrift, die '
            '<strong>auf den ganzen Absatz passt</strong>: Sie nennt die '
            'Aufgabe, sie gilt für jeden Satz, und sie hängt an keinem '
            'einzelnen davon. Die rechte Spalte sind die drei Arten, wie '
            'eine Überschrift richtig aussieht, ohne richtig zu sein '
            '&mdash; ein gemeinsames Wort, ein Treffer nur mit dem ersten '
            'Satz, eine Passung, die ein anderer Absatz genauso '
            'beanspruchen könnte. Jede ist ein Köder, der genau das tut, '
            'wofür er geschrieben wurde.',

    actTitle='Schreib die Überschriften selbst',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu zweit, mit irgendeinem Artikel zur Hand. Einer '
                  'schreibt zu jedem Absatz eine Überschrift und fügt zwei '
                  'dazu, die auf nichts passen &mdash; eine, die ein Wort '
                  'aus dem Text wiederholt, eine, die zu allgemein ist. '
                  'Liste mischen, tauschen, zuordnen. Dann jede Zuordnung '
                  'verteidigen.',
    actSpeak1='Wer zuordnet, muss sagen, was jeder Absatz tut &mdash; '
              'einführen, vergleichen, warnen &mdash;, bevor er die '
              'Überschrift nennt.',
    actSpeak2='Sag zu jedem Köder, zu welchem Absatz er dich locken sollte '
              'und woran man ihn erkennt.',
    actSpeak3='Finde in den Überschriften deines Partners eine, die auf zwei '
              'Absätze passt, und schreib sie so um, dass sie nur auf einen '
              'passt.',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Nimm einen Text mit drei Absätzen und schreib zu jedem '
                  'eine Überschrift. Zitiere unter jeder den einen Satz, der '
                  'beweist, dass sie die Hauptidee trifft, und sag in einer '
                  'Zeile, warum die Überschrift den ganzen Absatz abdeckt '
                  'und nicht nur diesen Satz.',
    actPlaceholder='Paragraph A — heading: … The sentence that proves it: …',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Matching <em>Headings</em>',
    coverSub='Una tarea del Reading que no sigue el orden del texto, y '
             'por eso la técnica es otra',
    chipLevel='C1 · Avanzado', chipFocus='Reading · los dos módulos',
    chipCount='18 puntos',

    t1Eyebrow='Antes de empezar',
    t1Title='Más títulos que párrafos, y ningún orden al que agarrarse',
    t1ah='La forma de la tarea',
    t1ab='Una lista de títulos numerados i, ii, iii, y un texto con párrafos '
         'de la A a la G. Cada párrafo recibe un título. Siempre hay más '
         'títulos que párrafos, así que dos o tres sobran, y están escritos '
         'para tentar.',
    t1an='Siete párrafos, diez títulos, tres señuelos. Esa es la cuenta '
         'habitual.',
    t1bh='Un tipo que salta',
    t1bb='Casi todos los tipos de pregunta siguen el texto. Este no, igual '
         'que Matching Information: el '
         'título i puede ser del párrafo F, y el orden de la lista no te '
         'dice nada sobre dónde mirar. Resolver cuatro no te dice dónde está '
         'el quinto.',
    t1bn='Suele ser lo primero de su texto, antes de las preguntas que sí '
         'van en orden.',
    t1ch='Primero el párrafo, luego la lista',
    t1cb='La trampa es leer primero diez títulos y luego buscarlos en el '
         'texto: diez ideas en la cabeza, todas buscando sitio. Lee el '
         'párrafo A, di con tus palabras de qué va, y solo entonces busca '
         'en la lista el título que dice lo mismo.',
    t1cn='Primero tu resumen, después la lista. Siempre.',

    t2Eyebrow='Antes de empezar',
    t2Title='Pregunta qué hace el párrafo, no de qué trata',
    t2ah='Función antes que tema',
    t2ab='Dos párrafos pueden compartir tema y hacer cosas distintas con él: '
         'uno plantea un problema, el siguiente da un ejemplo, un tercero '
         'sopesa dos posturas, un cuarto propone una solución. El título '
         'nombra la tarea. Un título que solo nombra el tema encaja con '
         'medio texto.',
    t2an='Plantear, ilustrar, comparar, advertir, proponer. Cinco verbos '
         'cubren casi todo lo que hace un párrafo.',
    t2bh='La frase clave se mueve',
    t2bb='Suele ir la primera, y quien escribe estos exámenes sabe que lo '
         'sabes. Un párrafo puede abrir con un ejemplo y dar su idea al '
         'final, o esconderla en medio tras una concesión. Lee hasta la '
         'última frase antes de decidir.',
    t2bn='Un título que solo encaja con la primera frase es la respuesta '
         'equivocada más frecuente de todo el examen.',
    t2ch='Una palabra repetida es un cebo',
    t2cb='Si un título usa una palabra que está en el párrafo, desconfía. El '
         'título correcto parafrasea: dice lo que el párrafo quiere decir '
         'con palabras que el párrafo no usa. Los incorrectos están hechos '
         'con su vocabulario, para que los encuentre quien busca palabras.',
    t2cn='Cotejar una palabra lleva un segundo. Cotejar una idea lleva una '
         'frase. Gasta la frase.',

    t3Eyebrow='Antes de empezar',
    t3Title='Los seguros primero, tachar, el doble encaje al final',
    t3ah='Primero los seguros',
    t3ab='Algunos párrafos tienen un título evidente. Cógelos, lleven la '
         'letra que lleven. Cada acierto seguro acorta la lista para los '
         'dudosos, y el párrafo más difícil se decide muchas veces por lo '
         'que queda, no por lo que dice.',
    t3an='No vayas de la A a la G. Ve de fácil a difícil.',
    t3bh='Táchalo en cuanto lo uses',
    t3bb='Cada título se usa una vez. Táchalo de la lista en cuanto te '
         'decidas, y tacha también el párrafo. Una lista que todavía enseña '
         'diez títulos para los dos últimos párrafos te está pidiendo que '
         'reconsideres cada decisión que ya has tomado.',
    t3bn='Lápiz, no memoria. Con el reloj encima olvidarás cuáles has '
         'usado.',
    t3ch='Cuando un título encaja en dos párrafos',
    t3cb='Déjalo. Haz el resto y vuelve con la lista más corta. Luego '
         'pregunta de cada párrafo: ¿este título cubre todo el párrafo o '
         'solo una frase? Uno de los dos tiene un título mejor en otra '
         'parte, y la eliminación decide lo que la lectura no pudo.',
    t3cn='Demasiado general y demasiado concreto fallan los dos. El título '
         'correcto encaja con el párrafo y con nada más.',

    mcaEyebrow='Actividad 1 · La idea principal',
    mcaTitle='Lee el párrafo. ¿Qué título lo cubre entero?',
    mcbEyebrow='Actividad 2 · ¿Qué está haciendo?',
    mcbTitle='Nombra la tarea, no el tema',
    mccEyebrow='Actividad 3 · Orden de ataque',
    mccTitle='¿Qué movimiento, y qué título?',

    r1why='Los cangrejos y el uno por ciento son detalles; los océanos en su '
          'conjunto son más de lo que el párrafo abarca. El único título '
          'que vale para cada frase es el tamaño frente a la vida.',
    r2why='La primera estación, la segunda, los cimientos bajo los pies: '
          'cada frase habla de un sitio con dos estaciones. Los pasajeros '
          'son un detalle, y la demolición nunca se explica.',
    r3why='Caligrafía copiada, hueco para las capitales, ejemplares vendidos '
          'como manuscritos: tres detalles, una idea: la imprenta fingiendo '
          'no serlo. La historia de la imprenta encajaría con cualquier '
          'párrafo del texto.',
    r4why='El año y la primera reacción son frases sueltas. El párrafo es '
          'el arco entero: prohibición, queja, éxito, y los quejosos '
          'expulsados por el precio. El título tiene que cargar con el '
          'final.',
    r5why='<em>Consider</em> lo delata: el párrafo está mostrando un caso. La '
          'semana en el puerto y el motor son sus detalles; el comercio '
          'mundial es el tema del texto, no la tarea de este párrafo.',
    r6why='Abre rechazando una conclusión y cierra con una recomendación. '
          'Eso es una defensa. Las familias y los resultados flojos son la '
          'prueba, no la idea.',
    r7why='<em>A word of caution</em> te da la función en cuatro palabras. '
          'El párrafo no informa de las cifras ni de los hogares con fijo; '
          'te dice hasta dónde fiarte de ellas.',
    r8why='Partidarios, críticos, y una última frase sobre que los dos '
          'nunca se encuentran. Los pueblos y la electricidad son lo que '
          'dice cada bando; el título tiene que nombrar el bloqueo.',
    r9why='La certeza primero, sea cual sea la letra. Cada acierto seguro '
          'quita un título de la lista, y los párrafos difíciles los decide '
          'lo que queda.',
    r10why='Pregunta qué hace cada párrafo. C trata del coste; E menciona el '
           'coste y luego hace otra cosa. Un título que encaja con una '
           'frase de E encaja con todo C.',
    r11why='Tres ciudades, el resultado en cada una, ninguna se ha echado '
           'atrás: el título tiene que cubrir las tres y el desenlace. La '
           'política de transporte abarca demasiado, y una ciudad demasiado '
           'poco.',
    r12why='Cinco títulos ya están gastados. Táchalos y los dos últimos '
           'párrafos eligen entre cinco, no entre diez. Releer cuesta el '
           'tiempo que no tienes.',

    sortEyebrow='Actividad 4 · ¿Título correcto o trampa?',
    sortTitle='Clasifica las seis señales',
    sortHint='Arrastra cada una a una columna &mdash; o haz clic en un '
             'elemento y luego en la columna que quieras.',
    sortBin1='Apunta al título correcto',
    sortBin2='Una trampa',
    sortWhy='La columna izquierda describe siempre un título que '
            '<strong>encaja con el párrafo entero</strong>: nombra la '
            'tarea, vale para cada frase y no depende de ninguna en '
            'concreto. La derecha son las tres maneras en que un título '
            'parece correcto sin serlo: una palabra compartida, un encaje '
            'solo con la primera línea, un ajuste que otro párrafo podría '
            'reclamar igual. Cada una es un señuelo haciendo justo lo que '
            'se escribió para hacer.',

    actTitle='Escribe tú los títulos',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas, con cualquier artículo a mano. Uno escribe un '
                  'título para cada párrafo y añade dos que no encajen con '
                  'nada: uno que repita una palabra del texto y otro '
                  'demasiado general. Barajad la lista, intercambiad y '
                  'emparejad. Luego defended cada emparejamiento.',
    actSpeak1='Quien empareja tiene que decir qué hace cada párrafo '
              '&mdash; plantear, comparar, advertir &mdash; antes de nombrar '
              'su título.',
    actSpeak2='De cada señuelo, di hacia qué párrafo se escribió para '
              'tentarte y qué lo delata.',
    actSpeak3='Busca en los títulos de tu compañero uno que encaje en dos '
              'párrafos y reescríbelo para que encaje solo en uno.',
    actWriteKind='Escritura · 150–200 palabras',
    actWriteBrief='Coge un texto de tres párrafos y escribe un título para '
                  'cada uno. Bajo cada título, cita la única frase que '
                  'demuestra que es la idea principal, y di en una línea por '
                  'qué el título cubre el párrafo entero y no solo esa '
                  'frase.',
    actPlaceholder='Paragraph A — heading: … The sentence that proves it: …',
)


# ── French ─────────────────────────────────────────────────────────────
T['fr'] = dict(
    coverTitle='Matching <em>Headings</em>',
    coverSub='Une tâche de Reading qui ne suit pas l’ordre du texte &mdash; la '
             'technique est donc différente',
    chipLevel='C1 · Avancé', chipFocus='Reading · les deux modules',
    chipCount='18 points',

    t1Eyebrow='Avant de commencer',
    t1Title='Plus de titres que de paragraphes, et aucun ordre sur lequel '
            's’appuyer',
    t1ah='La forme de la tâche',
    t1ab='Une liste de titres numérotés i, ii, iii, et un texte dont les '
         'paragraphes vont de A à G. Chaque paragraphe reçoit un titre. Il y a '
         'toujours plus de titres que de paragraphes, donc deux ou trois ne '
         'servent jamais &mdash; et ils sont écrits pour être tentants.',
    t1an='Sept paragraphes, dix titres, trois leurres. C’est le calcul '
         'habituel.',
    t1bh='Un type qui saute',
    t1bb='La plupart des types de questions suivent le texte. Celui-ci, comme '
         'Matching Information, ne le fait pas : le titre i peut appartenir au '
         'paragraphe F, et l’ordre de la liste ne dit rien de l’endroit où '
         'chercher. En trouver quatre ne dit rien du cinquième.',
    t1bn='Il vient en général en premier sur son texte, avant les questions '
         'qui, elles, suivent l’ordre.',
    t1ch='Lisez le paragraphe avant la liste',
    t1cb='Le piège consiste à lire d’abord les dix titres puis à les chercher '
         'dans le texte &mdash; dix idées en tête, toutes en quête d’un point '
         'de chute. Lisez le paragraphe A, dites avec vos mots de quoi il '
         'parle, et seulement ensuite cherchez dans la liste le titre qui dit '
         'la même chose.',
    t1cn='Votre résumé d’abord, la liste ensuite. À chaque fois.',

    t2Eyebrow='Avant de commencer',
    t2Title='Demandez-vous ce que fait le paragraphe, pas de quoi il parle',
    t2ah='La fonction avant le sujet',
    t2ab='Deux paragraphes peuvent partager un sujet et en faire des choses '
         'différentes : l’un présente un problème, le suivant donne un exemple, '
         'un troisième pèse deux points de vue, un quatrième propose une '
         'solution. Le titre nomme la fonction. Un titre qui ne nomme que le '
         'sujet convient à la moitié du texte.',
    t2an='Présenter, illustrer, comparer, mettre en garde, proposer. Cinq '
         'verbes couvrent l’essentiel de ce que fait un paragraphe.',
    t2bh='La phrase principale se déplace',
    t2bb='Elle vient en général en premier, et ceux qui rédigent ces tests '
         'savent que vous le savez. Un paragraphe peut s’ouvrir sur un exemple '
         'et énoncer son idée à la fin, ou l’enfouir au milieu après une '
         'concession. Lisez jusqu’à la dernière phrase avant de décider.',
    t2bn='Un titre qui ne correspond qu’à la première phrase est la mauvaise '
         'réponse la plus courante de l’épreuve.',
    t2ch='Un mot répété est un appât',
    t2cb='Si un titre utilise un mot qui figure dans le paragraphe, méfiez-vous. '
         'Le bon titre reformule : il dit ce que signifie le paragraphe avec '
         'des mots que le paragraphe n’a pas employés. Les mauvais sont '
         'construits avec son vocabulaire, pour qu’un candidat qui cherche des '
         'mots les trouve.',
    t2cn='Faire correspondre un mot prend une seconde. Faire correspondre une '
         'idée prend une phrase. Prenez le temps de la phrase.',

    t3Eyebrow='Avant de commencer',
    t3Title='Les sûrs d’abord, rayez, les doubles à la fin',
    t3ah='Faites d’abord ceux dont vous êtes sûr',
    t3ab='Certains paragraphes ont un titre évident. Prenez-les, quelle que '
         'soit leur lettre. Chaque correspondance sûre raccourcit la liste pour '
         'ceux dont vous doutez, et le paragraphe le plus difficile est souvent '
         'tranché par ce qui reste plutôt que par ce qu’il dit.',
    t3an='Ne travaillez pas de A à G. Travaillez du plus facile au plus '
         'difficile.',
    t3bh='Rayez-le une fois utilisé',
    t3bb='Chaque titre ne sert qu’une fois. Rayez-le de la liste dès que vous '
         'vous engagez, et rayez aussi le paragraphe. Une liste qui affiche '
         'encore dix titres alors qu’il reste deux paragraphes vous invite à '
         'remettre en cause toutes les décisions déjà prises.',
    t3bn='Le crayon, pas la mémoire. Sous la pression du temps, vous oublierez '
         'lesquels vous avez utilisés.',
    t3ch='Quand un titre convient à deux paragraphes',
    t3cb='Laissez-le. Faites le reste et revenez avec une liste plus courte. '
         'Puis demandez-vous pour chaque paragraphe : ce titre le couvre-t-il '
         'entièrement, ou une seule phrase ? L’un des deux a un meilleur titre '
         'ailleurs, et l’élimination tranche là où la lecture ne le pouvait '
         'pas.',
    t3cn='Trop général et trop précis échouent tous les deux. Le bon titre '
         'convient au paragraphe et à rien d’autre.',

    mcaEyebrow='Activité 1 · L’idée principale',
    mcaTitle='Lisez le paragraphe. Quel titre le couvre entièrement ?',
    mcbEyebrow='Activité 2 · Que fait-il ?',
    mcbTitle='Nommez la fonction, pas le sujet',
    mccEyebrow='Activité 3 · L’ordre d’attaque',
    mccTitle='Quelle démarche, et quel titre ?',

    r1why='Les crabes et le un pour cent sont des détails ; les océans dans '
          'leur ensemble dépassent ce que couvre le paragraphe. Le seul titre '
          'valable pour chaque phrase est celui qui met la taille en regard de '
          'la vie.',
    r2why='La première gare, la deuxième, les fondations sous les pieds : '
          'chaque phrase parle d’un même site portant deux gares. Les voyageurs '
          'sont un détail, et la démolition n’est jamais expliquée.',
    r3why='L’écriture manuscrite copiée, la place laissée pour les lettrines, '
          'les exemplaires vendus comme des manuscrits &mdash; trois détails, '
          'une idée : l’imprimerie qui fait semblant de ne pas en être. '
          'L’histoire de l’imprimerie conviendrait à n’importe quel paragraphe '
          'du texte.',
    r4why='L’année et la première réaction tiennent chacune en une phrase. Le '
          'paragraphe, c’est l’arc entier &mdash; interdiction, plainte, '
          'succès, et les plaignants évincés par les prix. Le titre doit porter '
          'la fin.',
    r5why='<em>Consider</em> vous met sur la piste : le paragraphe présente un '
          'cas. La semaine au port et le moteur sont ses détails ; le commerce '
          'mondial est le sujet du texte, pas la fonction de ce paragraphe.',
    r6why='Il s’ouvre en refusant une conclusion et se ferme sur une '
          'recommandation. C’est une défense. Les familles et les résultats '
          'faibles sont les preuves, pas l’idée.',
    r7why='<em>A word of caution</em> vous donne la fonction en quatre mots. Le '
          'paragraphe ne rapporte pas les chiffres ni les foyers équipés d’un '
          'téléphone fixe ; il vous dit jusqu’où leur faire confiance.',
    r8why='Des partisans, des détracteurs, et une dernière phrase sur les deux '
          'camps qui ne se rencontrent jamais. Les villages et l’électricité '
          'sont ce que dit chaque camp ; le titre doit nommer l’impasse.',
    r9why='La certitude d’abord, quelle que soit la lettre. Chaque '
          'correspondance sûre retire un titre de la liste, et les paragraphes '
          'difficiles sont tranchés par ce qui reste.',
    r10why='Demandez-vous ce que fait chaque paragraphe. C parle du coût ; E '
           'mentionne le coût puis fait autre chose. Un titre qui convient à '
           'une phrase de E convient à tout C.',
    r11why='Trois villes, le résultat dans chacune, aucun retour en arrière : '
           'le titre doit couvrir les trois et le résultat. La politique des '
           'transports couvre trop, et une seule ville trop peu.',
    r12why='Cinq titres sont déjà utilisés. Rayez-les, et les deux derniers '
           'paragraphes choisissent parmi cinq, pas dix. Tout relire coûte le '
           'temps que vous n’avez pas.',

    sortEyebrow='Activité 4 · Bon titre, ou piège ?',
    sortTitle='Classez les six signaux',
    sortHint='Faites glisser chacun dans une colonne &mdash; ou cliquez sur '
             'un élément, puis sur la colonne voulue.',
    sortBin1='Oriente vers le bon titre',
    sortBin2='Un piège',
    sortWhy='Tout ce qui est dans la colonne de gauche décrit un titre qui '
            '<strong>convient au paragraphe dans son ensemble</strong> : il '
            'nomme la fonction, il vaut pour chaque phrase, et il ne dépend '
            'd’aucune en particulier. La colonne de droite réunit les trois '
            'façons dont un titre semble juste sans l’être &mdash; un mot '
            'partagé, une correspondance avec la seule première ligne, une '
            'adéquation qu’un autre paragraphe pourrait revendiquer tout '
            'autant. Chacun est un leurre qui fait exactement ce pour quoi il a '
            'été écrit.',

    actTitle='Écrivez vous-même les titres',
    actUse='Utilisez-en au moins trois :',
    actSpeakBrief='À deux, avec n’importe quel article sous la main. L’un de '
                  'vous écrit un titre pour chaque paragraphe, puis ajoute deux '
                  'titres en trop qui ne conviennent à rien &mdash; l’un qui '
                  'reprend un mot du texte, l’autre trop général. Mélangez la '
                  'liste, échangez et associez. Puis défendez chaque '
                  'association.',
    actSpeak1='Celui qui associe doit dire ce que fait chaque paragraphe '
              '&mdash; présenter, comparer, mettre en garde &mdash; avant de '
              'nommer son titre.',
    actSpeak2='Pour chaque leurre, dites vers quel paragraphe il devait vous '
              'attirer, et ce qui le trahit.',
    actSpeak3='Trouvez dans la liste de votre partenaire un titre qui convient à '
              'deux paragraphes, et réécrivez-le pour qu’il ne convienne plus '
              'qu’à un seul.',
    actWriteKind='Écriture · 150–200 mots',
    actWriteBrief='Prenez un texte de trois paragraphes et écrivez un titre pour '
                  'chacun. Sous chaque titre, citez la phrase qui prouve que '
                  'c’est l’idée principale, et dites en une ligne pourquoi le '
                  'titre couvre tout le paragraphe et pas seulement cette '
                  'phrase.',
    actPlaceholder='Paragraph A — heading: … The sentence that proves it: …',
)


# ── Italian ────────────────────────────────────────────────────────────
T['it'] = dict(
    coverTitle='Matching <em>Headings</em>',
    coverSub='Un compito di Reading che non segue l’ordine del testo &mdash; '
             'quindi la tecnica è diversa',
    chipLevel='C1 · Avanzato', chipFocus='Reading · entrambi i moduli',
    chipCount='18 punti',

    t1Eyebrow='Prima di cominciare',
    t1Title='Più titoli che paragrafi, e nessun ordine a cui appoggiarsi',
    t1ah='Com’è fatto il compito',
    t1ab='Un elenco di titoli numerati i, ii, iii, e un testo con i paragrafi '
         'dalla A alla G. A ogni paragrafo va un titolo. I titoli sono sempre '
         'più dei paragrafi, quindi due o tre non si usano mai &mdash; e sono '
         'scritti apposta per tentarti.',
    t1an='Sette paragrafi, dieci titoli, tre esche. È il conto abituale.',
    t1bh='Un tipo che salta',
    t1bb='La maggior parte dei tipi di domanda segue il testo. Questo, come '
         'Matching Information, no: il titolo i può appartenere al paragrafo F, '
         'e l’ordine dell’elenco non ti dice nulla su dove guardare. '
         'Risolverne quattro non ti dice nulla del quinto.',
    t1bn='Di solito è il primo compito sul suo testo, prima delle domande che '
         'seguono l’ordine.',
    t1ch='Leggi il paragrafo prima dell’elenco',
    t1cb='La trappola è leggere prima i dieci titoli e poi cercarli nel testo '
         '&mdash; dieci idee in testa, tutte in cerca di casa. Leggi il '
         'paragrafo A, di’ con parole tue di che cosa parla, e solo allora '
         'cerca nell’elenco il titolo che dice la stessa cosa.',
    t1cn='Prima il tuo riassunto, poi l’elenco. Ogni volta.',

    t2Eyebrow='Prima di cominciare',
    t2Title='Chiediti che cosa fa il paragrafo, non di che cosa parla',
    t2ah='La funzione prima dell’argomento',
    t2ab='Due paragrafi possono avere lo stesso argomento e farci cose diverse: '
         'uno introduce un problema, il successivo porta un esempio, un terzo '
         'mette a confronto due punti di vista, un quarto propone una '
         'soluzione. Il titolo dà il nome alla funzione. Un titolo che nomina '
         'solo l’argomento va bene per metà del testo.',
    t2an='Introdurre, illustrare, confrontare, avvertire, proporre. Cinque '
         'verbi coprono quasi tutto ciò che fa un paragrafo.',
    t2bh='La frase chiave si sposta',
    t2bb='Di solito è la prima, e chi scrive questi test sa che tu lo sai. Un '
         'paragrafo può aprirsi con un esempio ed enunciare l’idea alla fine, '
         'o nasconderla a metà dopo una concessione. Leggi fino all’ultima '
         'frase prima di decidere.',
    t2bn='Un titolo che corrisponde solo alla prima frase è la risposta '
         'sbagliata più comune della prova.',
    t2ch='Una parola ripetuta è un’esca',
    t2cb='Se un titolo usa una parola che sta nel paragrafo, diffida. Il titolo '
         'giusto riformula: dice che cosa significa il paragrafo con parole che '
         'il paragrafo non ha usato. Quelli sbagliati sono costruiti con il suo '
         'vocabolario, perché un candidato che cerca parole li trovi.',
    t2cn='Far corrispondere una parola richiede un secondo. Far corrispondere '
         'un’idea richiede una frase. Spendi la frase.',

    t3Eyebrow='Prima di cominciare',
    t3Title='Prima i sicuri, cancella, i doppi alla fine',
    t3ah='Fai prima quelli sicuri',
    t3ab='Alcuni paragrafi hanno un titolo ovvio. Prendili, qualunque lettera '
         'abbiano. Ogni abbinamento sicuro accorcia l’elenco per quelli su cui '
         'hai dubbi, e il paragrafo più difficile spesso si decide per ciò che '
         'resta più che per ciò che dice.',
    t3an='Non lavorare dalla A alla G. Lavora dal facile al difficile.',
    t3bh='Cancellalo una volta usato',
    t3bb='Ogni titolo si usa una volta sola. Cancellalo dall’elenco appena ti '
         'decidi, e cancella anche il paragrafo. Un elenco che mostra ancora '
         'dieci titoli quando mancano due paragrafi ti invita a rimettere in '
         'discussione ogni decisione già presa.',
    t3bn='Matita, non memoria. Sotto pressione dimenticherai quali hai già '
         'usato.',
    t3ch='Quando un titolo va bene per due paragrafi',
    t3cb='Lascialo. Fai il resto e torna con l’elenco più corto. Poi chiediti '
         'per ogni paragrafo: questo titolo lo copre tutto, o solo una frase? '
         'Uno dei due ha un titolo migliore altrove, e l’eliminazione decide ciò '
         'che la lettura non poteva.',
    t3cn='Troppo generale e troppo specifico falliscono entrambi. Il titolo '
         'giusto va bene per il paragrafo e per nient’altro.',

    mcaEyebrow='Attività 1 · L’idea principale',
    mcaTitle='Leggi il paragrafo. Quale titolo lo copre tutto?',
    mcbEyebrow='Attività 2 · Che cosa sta facendo?',
    mcbTitle='Nomina la funzione, non l’argomento',
    mccEyebrow='Attività 3 · L’ordine d’attacco',
    mccTitle='Quale mossa, e quale titolo?',

    r1why='I granchi e l’uno per cento sono dettagli; gli oceani nel loro '
          'insieme vanno oltre ciò che copre il paragrafo. L’unico titolo che '
          'vale per ogni frase è quello che mette a confronto le dimensioni con '
          'la vita.',
    r2why='La prima stazione, la seconda, le fondamenta sotto i piedi: ogni '
          'frase parla di un unico luogo che ospita due stazioni. I passeggeri '
          'sono un dettaglio, e la demolizione non viene mai spiegata.',
    r3why='La grafia a mano copiata, lo spazio lasciato per le iniziali, le '
          'copie vendute come manoscritti &mdash; tre dettagli, un’idea: la '
          'stampa che finge di non essere stampa. La storia della stampa '
          'andrebbe bene per qualsiasi paragrafo del testo.',
    r4why='L’anno e la prima reazione sono frasi singole. Il paragrafo è '
          'l’intero arco &mdash; divieto, protesta, successo, e chi protestava '
          'tagliato fuori dai prezzi. Il titolo deve contenere il finale.',
    r5why='<em>Consider</em> è l’indizio: il paragrafo presenta un caso. La '
          'settimana in porto e il motore sono i suoi dettagli; il commercio '
          'mondiale è l’argomento del testo, non la funzione di questo '
          'paragrafo.',
    r6why='Si apre rifiutando una conclusione e si chiude con una '
          'raccomandazione. È una difesa. Le famiglie e i risultati deboli sono '
          'le prove, non il punto.',
    r7why='<em>A word of caution</em> ti dà la funzione in quattro parole. Il '
          'paragrafo non riporta i dati né le famiglie con il telefono fisso; '
          'ti dice quanto fidarti di quei dati.',
    r8why='Sostenitori, critici e un’ultima frase sui due fronti che non si '
          'incontrano mai. I villaggi e l’elettricità sono ciò che dice '
          'ciascuna parte; il titolo deve nominare lo stallo.',
    r9why='Prima la certezza, qualunque sia la lettera. Ogni abbinamento sicuro '
          'toglie un titolo dall’elenco, e i paragrafi difficili si decidono con '
          'ciò che resta.',
    r10why='Chiediti che cosa fa ogni paragrafo. C parla del costo; E cita il '
           'costo e poi fa altro. Un titolo che va bene per una frase di E va '
           'bene per tutto C.',
    r11why='Tre città, il risultato in ciascuna, nessun passo indietro: il '
           'titolo deve coprire tutte e tre e l’esito. La politica dei '
           'trasporti copre troppo, e una sola città troppo poco.',
    r12why='Cinque titoli sono già usati. Cancellali, e gli ultimi due '
           'paragrafi scelgono tra cinque, non tra dieci. Rileggere tutto costa '
           'il tempo che non hai.',

    sortEyebrow='Attività 4 · Titolo giusto o trappola?',
    sortTitle='Classifica i sei segnali',
    sortHint='Trascina ciascuno in una colonna &mdash; oppure clicca su un '
             'elemento e poi sulla colonna che vuoi.',
    sortBin1='Porta al titolo giusto',
    sortBin2='Una trappola',
    sortWhy='Tutto ciò che sta nella colonna di sinistra descrive un titolo che '
            '<strong>va bene per il paragrafo nel suo insieme</strong>: nomina '
            'la funzione, vale per ogni frase e non dipende da nessuna in '
            'particolare. La colonna di destra raccoglie i tre modi in cui un '
            'titolo sembra giusto senza esserlo &mdash; una parola in comune, '
            'una corrispondenza con la sola prima riga, un’adeguatezza che un '
            'altro paragrafo potrebbe rivendicare altrettanto. Ognuno è '
            'un’esca che fa esattamente ciò per cui è stata scritta.',

    actTitle='Scrivi tu i titoli',
    actUse='Usane almeno tre:',
    actSpeakBrief='In coppia, con un articolo qualsiasi a portata di mano. Uno di '
                  'voi scrive un titolo per ogni paragrafo, poi aggiunge due '
                  'titoli in più che non vanno bene per nessuno &mdash; uno che '
                  'ripete una parola del testo, uno troppo generale. Mescolate '
                  'l’elenco, scambiatevelo e abbinate. Poi discutete ogni '
                  'abbinamento.',
    actSpeak1='Chi abbina deve dire che cosa fa ogni paragrafo &mdash; '
              'introdurre, confrontare, avvertire &mdash; prima di nominarne il '
              'titolo.',
    actSpeak2='Per ogni esca, di’ verso quale paragrafo doveva attirarti e che '
              'cosa la tradisce.',
    actSpeak3='Trova nell’elenco del tuo compagno un titolo che va bene per due '
              'paragrafi e riscrivilo perché vada bene per uno solo.',
    actWriteKind='Scrittura · 150–200 parole',
    actWriteBrief='Prendi un testo di tre paragrafi e scrivi un titolo per '
                  'ciascuno. Sotto ogni titolo, cita la frase che dimostra che è '
                  'l’idea principale, e spiega in una riga perché il titolo copre '
                  'tutto il paragrafo e non solo quella frase.',
    actPlaceholder='Paragraph A — heading: … The sentence that proves it: …',
)


# ── Portuguese ─────────────────────────────────────────────────────────
T['pt'] = dict(
    coverTitle='Matching <em>Headings</em>',
    coverSub='Uma tarefa de Reading que não segue a ordem do texto &mdash; por '
             'isso a técnica é diferente',
    chipLevel='C1 · Avançado', chipFocus='Reading · os dois módulos',
    chipCount='18 pontos',

    t1Eyebrow='Antes de começar',
    t1Title='Mais títulos do que parágrafos, e nenhuma ordem em que te apoiar',
    t1ah='O formato da tarefa',
    t1ab='Uma lista de títulos numerados i, ii, iii, e um texto com parágrafos '
         'de A a G. Cada parágrafo leva um título. Há sempre mais títulos do '
         'que parágrafos, por isso dois ou três nunca são usados &mdash; e são '
         'escritos para tentar.',
    t1an='Sete parágrafos, dez títulos, três iscos. É a conta habitual.',
    t1bh='Um tipo que salta',
    t1bb='A maioria dos tipos de pergunta segue o texto. Este, tal como '
         'Matching Information, não: o título i pode pertencer ao parágrafo F, '
         'e a ordem da lista não te diz nada sobre onde procurar. Acertar em '
         'quatro não te diz nada sobre o quinto.',
    t1bn='Costuma ser a primeira tarefa sobre o seu texto, antes das perguntas '
         'que seguem a ordem.',
    t1ch='Lê o parágrafo antes da lista',
    t1cb='A armadilha é ler primeiro os dez títulos e depois procurá-los no '
         'texto &mdash; dez ideias na cabeça, todas à procura de casa. Lê o '
         'parágrafo A, diz por palavras tuas de que trata, e só depois procura '
         'na lista o título que diz o mesmo.',
    t1cn='Primeiro o teu resumo, depois a lista. Sempre.',

    t2Eyebrow='Antes de começar',
    t2Title='Pergunta o que o parágrafo está a fazer, não de que trata',
    t2ah='A função antes do tema',
    t2ab='Dois parágrafos podem partilhar um tema e fazer coisas diferentes com '
         'ele: um apresenta um problema, o seguinte dá um exemplo, um terceiro '
         'pesa duas opiniões, um quarto propõe uma solução. O título nomeia a '
         'função. Um título que só nomeia o tema serve para metade do texto.',
    t2an='Apresentar, ilustrar, comparar, alertar, propor. Cinco verbos cobrem '
         'quase tudo o que um parágrafo faz.',
    t2bh='A frase principal muda de lugar',
    t2bb='Costuma vir primeiro, e quem escreve estes testes sabe que tu sabes '
         'isso. Um parágrafo pode abrir com um exemplo e dizer a ideia no fim, '
         'ou escondê-la a meio, depois de uma concessão. Lê até à última frase '
         'antes de decidir.',
    t2bn='Um título que só corresponde à primeira frase é a resposta errada '
         'mais comum da prova.',
    t2ch='Uma palavra repetida é um isco',
    t2cb='Se um título usa uma palavra que está no parágrafo, desconfia. O '
         'título certo parafraseia: diz o que o parágrafo quer dizer com '
         'palavras que o parágrafo não usou. Os errados são construídos com o '
         'seu vocabulário, para que um candidato à procura de palavras os '
         'encontre.',
    t2cn='Fazer corresponder uma palavra leva um segundo. Fazer corresponder '
         'uma ideia leva uma frase. Gasta a frase.',

    t3Eyebrow='Antes de começar',
    t3Title='Primeiro os certos, risca, os duplos no fim',
    t3ah='Faz primeiro os que tens a certeza',
    t3ab='Alguns parágrafos têm um título óbvio. Fica com eles, seja qual for a '
         'letra. Cada correspondência certa encurta a lista para os que te '
         'deixam dúvidas, e o parágrafo mais difícil decide-se muitas vezes '
         'pelo que sobra, e não pelo que diz.',
    t3an='Não trabalhes de A a G. Trabalha do fácil para o difícil.',
    t3bh='Risca-o depois de usado',
    t3bb='Cada título usa-se uma só vez. Risca-o da lista assim que te decides, '
         'e risca também o parágrafo. Uma lista que ainda mostra dez títulos '
         'quando faltam dois parágrafos está a convidar-te a rever todas as '
         'decisões que já tomaste.',
    t3bn='Lápis, não memória. Com o tempo a apertar, vais esquecer-te de quais '
         'já usaste.',
    t3ch='Quando um título serve para dois parágrafos',
    t3cb='Deixa-o. Faz o resto e volta com a lista mais curta. Depois pergunta '
         'a cada parágrafo: este título cobre-o por inteiro, ou só uma frase? '
         'Um dos dois tem um título melhor noutro lado, e a eliminação decide o '
         'que a leitura não conseguia.',
    t3cn='Demasiado geral e demasiado específico falham os dois. O título certo '
         'serve para o parágrafo e para mais nada.',

    mcaEyebrow='Atividade 1 · A ideia principal',
    mcaTitle='Lê o parágrafo. Que título o cobre por inteiro?',
    mcbEyebrow='Atividade 2 · O que está a fazer?',
    mcbTitle='Nomeia a função, não o tema',
    mccEyebrow='Atividade 3 · A ordem de ataque',
    mccTitle='Que jogada, e que título?',

    r1why='Os caranguejos e o um por cento são pormenores; os oceanos no seu '
          'conjunto vão além do que o parágrafo cobre. O único título que vale '
          'para todas as frases é o que põe o tamanho frente à vida.',
    r2why='A primeira estação, a segunda, as fundações debaixo dos pés: todas '
          'as frases falam de um só local com duas estações. Os passageiros '
          'são um pormenor, e a demolição nunca é explicada.',
    r3why='A letra manuscrita copiada, o espaço deixado para as capitulares, as '
          'cópias vendidas como manuscritos &mdash; três pormenores, uma ideia: '
          'a imprensa a fingir que não o é. A história da imprensa serviria '
          'para qualquer parágrafo do texto.',
    r4why='O ano e a primeira reação são frases soltas. O parágrafo é o arco '
          'inteiro &mdash; proibição, queixa, sucesso, e os queixosos afastados '
          'pelos preços. O título tem de conter o final.',
    r5why='<em>Consider</em> é a pista: o parágrafo apresenta um caso. A semana '
          'no porto e o motor são os seus pormenores; o comércio mundial é o '
          'tema do texto, não a função deste parágrafo.',
    r6why='Abre recusando uma conclusão e fecha com uma recomendação. É uma '
          'defesa. As famílias e os resultados fracos são as provas, não a '
          'ideia.',
    r7why='<em>A word of caution</em> dá-te a função em quatro palavras. O '
          'parágrafo não relata os números nem os lares com telefone fixo; '
          'diz-te até que ponto confiar neles.',
    r8why='Defensores, críticos e uma última frase sobre os dois lados que '
          'nunca se encontram. As aldeias e a eletricidade são o que cada lado '
          'diz; o título tem de nomear o impasse.',
    r9why='Primeiro a certeza, seja qual for a letra. Cada correspondência '
          'certa tira um título da lista, e os parágrafos difíceis decidem-se '
          'pelo que sobra.',
    r10why='Pergunta o que faz cada parágrafo. C fala do custo; E menciona o '
           'custo e depois faz outra coisa. Um título que serve para uma frase '
           'de E serve para todo o C.',
    r11why='Três cidades, o resultado em cada uma, nenhum recuo: o título tem de '
           'cobrir as três e o desfecho. A política de transportes cobre '
           'demasiado, e uma só cidade cobre de menos.',
    r12why='Cinco títulos já estão usados. Risca-os, e os dois últimos '
           'parágrafos escolhem entre cinco, não entre dez. Reler tudo custa o '
           'tempo que não tens.',

    sortEyebrow='Atividade 4 · Título certo ou armadilha?',
    sortTitle='Classifica os seis sinais',
    sortHint='Arrasta cada um para uma coluna &mdash; ou clica num elemento e '
             'depois na coluna que quiseres.',
    sortBin1='Aponta para o título certo',
    sortBin2='Uma armadilha',
    sortWhy='Tudo o que está na coluna da esquerda descreve um título que '
            '<strong>serve para o parágrafo no seu todo</strong>: nomeia a '
            'função, vale para todas as frases e não depende de nenhuma em '
            'particular. A coluna da direita reúne as três maneiras de um título '
            'parecer certo sem o ser &mdash; uma palavra partilhada, uma '
            'correspondência só com a primeira linha, um encaixe que outro '
            'parágrafo podia reclamar da mesma forma. Cada um é um isco a fazer '
            'exatamente aquilo para que foi escrito.',

    actTitle='Escreve tu os títulos',
    actUse='Usa pelo menos três:',
    actSpeakBrief='Em pares, com um artigo qualquer à mão. Um de vocês escreve um '
                  'título para cada parágrafo e depois junta dois títulos a mais '
                  'que não servem para nenhum &mdash; um que repete uma palavra '
                  'do texto, outro demasiado geral. Baralhem a lista, troquem e '
                  'façam as correspondências. Depois discutam cada uma.',
    actSpeak1='Quem faz as correspondências tem de dizer o que cada parágrafo '
              'está a fazer &mdash; apresentar, comparar, alertar &mdash; antes '
              'de dizer o título.',
    actSpeak2='Para cada isco, diz para que parágrafo te devia atrair e o que o '
              'denuncia.',
    actSpeak3='Encontra na lista do teu colega um título que sirva para dois '
              'parágrafos e reescreve-o para que sirva só para um.',
    actWriteKind='Escrita · 150–200 palavras',
    actWriteBrief='Pega num texto de três parágrafos e escreve um título para '
                  'cada um. Por baixo de cada título, cita a frase que prova que '
                  'é a ideia principal e diz numa linha porque é que o título '
                  'cobre o parágrafo inteiro e não só essa frase.',
    actPlaceholder='Paragraph A — heading: … The sentence that proves it: …',
)


# ── Russian ────────────────────────────────────────────────────────────
T['ru'] = dict(
    coverTitle='Matching <em>Headings</em>',
    coverSub='Задание Reading, которое не идёт по порядку текста, &mdash; '
             'поэтому и техника другая',
    chipLevel='C1 · Продвинутый', chipFocus='Reading · оба модуля',
    chipCount='18 баллов',

    t1Eyebrow='Прежде чем начать',
    t1Title='Заголовков больше, чем абзацев, и опереться на порядок нельзя',
    t1ah='Как устроено задание',
    t1ab='Список заголовков с номерами i, ii, iii и текст с абзацами от A до G. '
         'Каждому абзацу нужен один заголовок. Заголовков всегда больше, чем '
         'абзацев, поэтому два-три так и не пригодятся &mdash; и написаны они '
         'так, чтобы соблазнять.',
    t1an='Семь абзацев, десять заголовков, три приманки. Обычная арифметика.',
    t1bh='Тип, который прыгает',
    t1bb='Большинство типов вопросов идут по тексту. Этот, как и Matching '
         'Information, &mdash; нет: заголовок i может относиться к абзацу F, а '
         'порядок списка ничего не говорит о том, где искать. Четыре ответа '
         'ничего не подскажут о пятом.',
    t1bn='Обычно это задание идёт первым по своему тексту, перед вопросами, '
         'которые идут по порядку.',
    t1ch='Читайте абзац раньше списка',
    t1cb='Ловушка в том, чтобы сначала прочитать десять заголовков, а потом '
         'искать их в тексте, &mdash; в голове десять идей, и каждая ищет, куда '
         'пристроиться. Прочитайте абзац A, скажите своими словами, о чём он, и '
         'только потом ищите в списке заголовок, который говорит то же самое.',
    t1cn='Сначала ваше резюме, потом список. Всегда.',

    t2Eyebrow='Прежде чем начать',
    t2Title='Спрашивайте, что абзац делает, а не о чём он',
    t2ah='Функция важнее темы',
    t2ab='Два абзаца могут иметь одну тему и делать с ней разное: один '
         'представляет проблему, следующий приводит пример, третий взвешивает '
         'две точки зрения, четвёртый предлагает решение. Заголовок называет '
         'функцию. Заголовок, который называет только тему, подходит к '
         'половине текста.',
    t2an='Вводить, иллюстрировать, сравнивать, предостерегать, предлагать. '
         'Пять глаголов покрывают почти всё, что делает абзац.',
    t2bh='Главное предложение перемещается',
    t2bb='Обычно оно первое, и составители тестов знают, что вы это знаете. '
         'Абзац может начаться с примера и высказать мысль в конце или спрятать '
         'её в середине после уступки. Дочитайте до последнего предложения, '
         'прежде чем решать.',
    t2bn='Заголовок, совпадающий только с первым предложением, &mdash; самая '
         'частая ошибка на экзамене.',
    t2ch='Повторённое слово &mdash; наживка',
    t2cb='Если в заголовке есть слово из абзаца, будьте начеку. Верный '
         'заголовок перефразирует: он передаёт смысл абзаца словами, которых в '
         'абзаце нет. Неверные собраны из его лексики, чтобы их нашёл тот, кто '
         'ищет слова.',
    t2cn='Сопоставить слово &mdash; секунда. Сопоставить мысль &mdash; целое '
         'предложение. Потратьте это предложение.',

    t3Eyebrow='Прежде чем начать',
    t3Title='Сначала верные, вычёркивайте, двойные &mdash; в конце',
    t3ah='Начинайте с верных',
    t3ab='У некоторых абзацев один очевидный заголовок. Берите их, какая бы '
         'буква у них ни была. Каждое верное совпадение сокращает список для '
         'тех, в которых вы не уверены, а самый трудный абзац часто решает то, '
         'что осталось, а не то, что в нём сказано.',
    t3an='Не идите от A к G. Идите от лёгкого к трудному.',
    t3bh='Использовали &mdash; вычеркните',
    t3bb='Каждый заголовок используется один раз. Вычеркните его из списка, как '
         'только решили, и вычеркните абзац тоже. Список, где всё ещё десять '
         'заголовков, когда осталось два абзаца, предлагает вам пересмотреть '
         'все уже принятые решения.',
    t3bn='Карандаш, а не память. Под давлением времени вы забудете, какие уже '
         'использовали.',
    t3ch='Когда заголовок подходит к двум абзацам',
    t3cb='Оставьте его. Сделайте остальное и вернитесь, когда список станет '
         'короче. Потом спросите о каждом абзаце: этот заголовок покрывает его '
         'целиком или только одно предложение? У одного из двух есть заголовок '
         'получше, и исключение решает то, чего не решило чтение.',
    t3cn='Слишком общий и слишком частный не подходят оба. Верный заголовок '
         'подходит к абзацу и больше ни к чему.',

    mcaEyebrow='Задание 1 · Главная мысль',
    mcaTitle='Прочитайте абзац. Какой заголовок покрывает его целиком?',
    mcbEyebrow='Задание 2 · Что он делает?',
    mcbTitle='Называйте функцию, а не тему',
    mccEyebrow='Задание 3 · Порядок действий',
    mccTitle='Какой ход и какой заголовок?',

    r1why='Крабы и один процент &mdash; детали; океаны в целом шире того, что '
          'охватывает абзац. Единственный заголовок, верный для каждого '
          'предложения, &mdash; тот, что сопоставляет размер с жизнью.',
    r2why='Первая станция, вторая, фундаменты под ногами: каждое предложение '
          '&mdash; об одном месте, где две станции. Пассажиры &mdash; деталь, а '
          'снос нигде не объясняется.',
    r3why='Скопированный почерк, место для заглавных букв, экземпляры, '
          'проданные как рукописи, &mdash; три детали, одна мысль: печать, '
          'которая притворяется не печатью. История книгопечатания подошла бы к '
          'любому абзацу текста.',
    r4why='Год и первая реакция &mdash; отдельные предложения. Абзац &mdash; '
          'это вся дуга: запрет, жалоба, успех и жалобщики, вытесненные ценами. '
          'Заголовок должен вмещать концовку.',
    r5why='<em>Consider</em> выдаёт всё: абзац показывает один случай. Неделя в '
          'порту и двигатель &mdash; его детали; мировая торговля &mdash; тема '
          'текста, а не функция этого абзаца.',
    r6why='Он начинается с отказа от вывода и заканчивается рекомендацией. Это '
          'защита. Семьи и слабые результаты &mdash; доказательства, а не '
          'главная мысль.',
    r7why='<em>A word of caution</em> называет функцию в четырёх словах. Абзац '
          'не пересказывает цифры и не говорит о домохозяйствах со стационарным '
          'телефоном; он говорит, насколько им можно доверять.',
    r8why='Сторонники, критики и последнее предложение о том, что стороны так и '
          'не сходятся. Деревни и электричество &mdash; то, что говорит каждая '
          'сторона; заголовок должен назвать тупик.',
    r9why='Сначала уверенность, какая бы ни была буква. Каждое верное '
          'совпадение убирает заголовок из списка, а трудные абзацы решаются '
          'тем, что осталось.',
    r10why='Спросите, что делает каждый абзац. C &mdash; о стоимости; E '
           'упоминает стоимость, а потом делает другое. Заголовок, подходящий к '
           'одному предложению E, подходит ко всему C.',
    r11why='Три города, результат в каждом, ни одного отката: заголовок должен '
           'охватывать все три и итог. Транспортная политика &mdash; слишком '
           'широко, один город &mdash; слишком узко.',
    r12why='Пять заголовков уже использованы. Вычеркните их, и последние два '
           'абзаца выбирают из пяти, а не из десяти. Перечитывание съест время, '
           'которого у вас нет.',

    sortEyebrow='Задание 4 · Верный заголовок или ловушка?',
    sortTitle='Распределите шесть сигналов',
    sortHint='Перетащите каждый в столбец &mdash; или нажмите на него, а затем '
             'на нужный столбец.',
    sortBin1='Указывает на верный заголовок',
    sortBin2='Ловушка',
    sortWhy='Всё в левом столбце описывает заголовок, который <strong>подходит '
            'к абзацу целиком</strong>: он называет функцию, верен для каждого '
            'предложения и не зависит ни от одного из них. В правом столбце '
            '&mdash; три способа, которыми заголовок кажется верным, не будучи '
            'им: общее слово, совпадение только с первой строкой, соответствие, '
            'на которое с тем же успехом может претендовать другой абзац. Каждый '
            'из них &mdash; приманка, которая делает ровно то, ради чего '
            'написана.',

    actTitle='Напишите заголовки сами',
    actUse='Используйте хотя бы три:',
    actSpeakBrief='В парах, с любой статьёй под рукой. Один из вас пишет '
                  'заголовок к каждому абзацу, а потом добавляет два лишних, '
                  'которые ни к чему не подходят: один повторяет слово из '
                  'текста, другой слишком общий. Перемешайте список, '
                  'обменяйтесь и сопоставьте. Потом обсудите каждое '
                  'сопоставление.',
    actSpeak1='Тот, кто сопоставляет, должен сказать, что делает каждый абзац '
              '&mdash; вводит, сравнивает, предостерегает, &mdash; прежде чем '
              'назвать заголовок.',
    actSpeak2='Про каждую приманку скажите, к какому абзацу она должна была вас '
              'притянуть и что её выдаёт.',
    actSpeak3='Найдите в списке партнёра заголовок, подходящий к двум абзацам, '
              'и перепишите его так, чтобы он подходил только к одному.',
    actWriteKind='Письмо · 150–200 слов',
    actWriteBrief='Возьмите текст из трёх абзацев и напишите заголовок к '
                  'каждому. Под каждым заголовком процитируйте предложение, '
                  'которое доказывает, что это главная мысль, и одной строкой '
                  'объясните, почему заголовок покрывает весь абзац, а не только '
                  'это предложение.',
    actPlaceholder='Paragraph A — heading: … The sentence that proves it: …',
)


# ── Arabic ─────────────────────────────────────────────────────────────
T['ar'] = dict(
    coverTitle='Matching <em>Headings</em>',
    coverSub='مهمة في Reading لا تسير بترتيب النص، ولذلك تختلف التقنية',
    chipLevel='C1 · متقدّم', chipFocus='Reading · الوحدتان كلتاهما',
    chipCount='18 نقطة',

    t1Eyebrow='قبل أن تبدأ',
    t1Title='عناوين أكثر من الفقرات، ولا ترتيب تستند إليه',
    t1ah='شكل المهمة',
    t1ab='قائمة عناوين مرقّمة i وii وiii، ونص فقراته مرقّمة بالأحرف من A إلى '
         'G. لكل فقرة عنوان واحد. والعناوين دائمًا أكثر من الفقرات، فيبقى اثنان '
         'أو ثلاثة بلا استخدام، وهي مكتوبة لتُغريك.',
    t1an='سبع فقرات، وعشرة عناوين، وثلاثة طُعوم. هذا هو الحساب المعتاد.',
    t1bh='نوع يقفز',
    t1bb='معظم أنواع الأسئلة تتبع ترتيب النص. أما هذا النوع، مثل Matching '
         'Information، فلا يتبعه: قد يكون العنوان i للفقرة F، وترتيب القائمة '
         'لا يدلّك على مكان البحث. وحلّ أربعة لا يخبرك شيئًا عن الخامس.',
    t1bn='يأتي عادةً أولًا على نصّه، قبل الأسئلة التي تتبع الترتيب.',
    t1ch='اقرأ الفقرة قبل القائمة',
    t1cb='الفخّ أن تقرأ العناوين العشرة أولًا ثم تبحث عنها في النص، فتدور في '
         'رأسك عشر أفكار كلها تبحث عن مكان. اقرأ الفقرة A، وقل بكلماتك عمّا '
         'تتحدث، وبعد ذلك فقط ابحث في القائمة عن العنوان الذي يقول الشيء '
         'نفسه.',
    t1cn='ملخّصك أولًا، ثم القائمة. في كل مرة.',

    t2Eyebrow='قبل أن تبدأ',
    t2Title='اسأل ماذا تفعل الفقرة، لا عمّا تتحدث',
    t2ah='الوظيفة قبل الموضوع',
    t2ab='قد تشترك فقرتان في موضوع واحد وتقوم كل منهما بعمل مختلف: واحدة تعرض '
         'مشكلة، والتالية تضرب مثالًا، وثالثة توازن بين رأيين، ورابعة تقترح '
         'حلًّا. العنوان يسمّي الوظيفة. والعنوان الذي يسمّي الموضوع فقط يناسب '
         'نصف النص.',
    t2an='العرض والتمثيل والمقارنة والتحذير والاقتراح: خمسة أفعال تغطي معظم ما '
         'تفعله الفقرة.',
    t2bh='الجملة الرئيسية تتنقّل',
    t2bb='تأتي عادةً أولًا، وواضعو هذه الاختبارات يعرفون أنك تعرف ذلك. قد تبدأ '
         'الفقرة بمثال وتذكر فكرتها في النهاية، أو تدفنها في الوسط بعد تسليم. '
         'اقرأ حتى الجملة الأخيرة قبل أن تقرّر.',
    t2bn='العنوان الذي لا يطابق إلا الجملة الأولى هو أكثر الإجابات الخاطئة '
         'شيوعًا في الاختبار.',
    t2ch='الكلمة المكرّرة طُعم',
    t2cb='إذا استخدم عنوانٌ كلمةً موجودة في الفقرة، فكن حذرًا. العنوان الصحيح '
         'يعيد الصياغة: يقول ما تعنيه الفقرة بكلمات لم تستخدمها. أما العناوين '
         'الخاطئة فمبنية من مفرداتها، ليجدها المتقدّم الذي يبحث عن الكلمات.',
    t2cn='مطابقة كلمة تستغرق ثانية، ومطابقة فكرة تستغرق جملة. أنفِق الجملة.',

    t3Eyebrow='قبل أن تبدأ',
    t3Title='المؤكَّد أولًا، اشطب، والمزدوج في الآخر',
    t3ah='ابدأ بما أنت متأكد منه',
    t3ab='لبعض الفقرات عنوان واضح. خذه أيًّا كان حرفها. كل مطابقة مؤكّدة تقصّر '
         'القائمة لما لست متأكدًا منه، وكثيرًا ما يحسم الفقرةَ الأصعب ما تبقّى '
         'لا ما تقوله.',
    t3an='لا تعمل من A إلى G، بل من السهل إلى الصعب.',
    t3bh='اشطبه بعد استخدامه',
    t3bb='يُستخدم كل عنوان مرة واحدة. اشطبه من القائمة لحظة تقرّر، واشطب الفقرة '
         'أيضًا. القائمة التي ما زالت تعرض عشرة عناوين وقد بقيت فقرتان تدعوك إلى '
         'مراجعة كل قرار اتخذته.',
    t3bn='القلم لا الذاكرة. تحت ضغط الوقت ستنسى أيّها استخدمت.',
    t3ch='عندما يناسب عنوانٌ فقرتين',
    t3cb='اتركه. أنجز الباقي وعُد إليه والقائمة أقصر. ثم اسأل عن كل فقرة: هل '
         'يغطيها هذا العنوان كلها أم جملة واحدة منها؟ لإحدى الفقرتين عنوان أفضل '
         'في مكان آخر، والاستبعاد يحسم ما لم تحسمه القراءة.',
    t3cn='العنوان العام جدًّا والمحدّد جدًّا يفشلان كلاهما. العنوان الصحيح '
         'يناسب الفقرة ولا يناسب غيرها.',

    mcaEyebrow='النشاط 1 · الفكرة الرئيسية',
    mcaTitle='اقرأ الفقرة. أيّ عنوان يغطيها كلها؟',
    mcbEyebrow='النشاط 2 · ماذا تفعل الفقرة؟',
    mcbTitle='سمِّ الوظيفة لا الموضوع',
    mccEyebrow='النشاط 3 · ترتيب الهجوم',
    mccTitle='أيّ خطوة، وأيّ عنوان؟',

    r1why='السرطانات والواحد في المئة تفاصيل، والمحيطات كلها أوسع مما تغطيه '
          'الفقرة. العنوان الوحيد الذي يصحّ على كل جملة هو الذي يضع الحجم في '
          'مقابل الحياة.',
    r2why='المحطة الأولى، والثانية، والأساسات تحت الأقدام: كل جملة تتحدث عن موقع '
          'واحد يحمل محطتين. الركاب تفصيل، والهدم لا يُشرح أبدًا.',
    r3why='خطّ اليد المنسوخ، والفراغ المتروك للحروف الكبيرة، والنسخ المبيعة على '
          'أنها مخطوطات: ثلاثة تفاصيل وفكرة واحدة، هي الطباعة التي تتظاهر بأنها '
          'ليست طباعة. أما تاريخ الطباعة فيناسب أيّ فقرة في النص.',
    r4why='السنة وردّ الفعل الأول جملتان منفردتان. الفقرة هي القوس كله: منع، '
          'فشكوى، فنجاح، ثم إقصاء الشاكين بالأسعار. والعنوان يجب أن يحمل '
          'الخاتمة.',
    r5why='كلمة <em>Consider</em> تكشف الأمر: الفقرة تعرض حالة واحدة. الأسبوع في '
          'الميناء والمحرّك تفاصيلها، والتجارة العالمية موضوع النص لا وظيفة هذه '
          'الفقرة.',
    r6why='تبدأ برفض استنتاج وتنتهي بتوصية. هذا دفاع. والأسر والنتائج الضعيفة هي '
          'الأدلة، لا الفكرة.',
    r7why='عبارة <em>A word of caution</em> تعطيك الوظيفة في أربع كلمات. الفقرة لا '
          'تنقل الأرقام ولا تتحدث عن الأسر ذات الهاتف الأرضي، بل تقول لك إلى أيّ '
          'حدّ تثق بها.',
    r8why='مؤيّدون ومعارضون وجملة أخيرة عن طرفين لا يلتقيان أبدًا. القرى '
          'والكهرباء هي ما يقوله كل طرف، والعنوان يجب أن يسمّي هذا الانسداد.',
    r9why='اليقين أولًا أيًّا كان الحرف. كل مطابقة مؤكّدة تُخرج عنوانًا من '
          'القائمة، والفقرات الصعبة يحسمها ما تبقّى.',
    r10why='اسأل ماذا تفعل كل فقرة. الفقرة C عن التكلفة، أما E فتذكر التكلفة ثم '
           'تفعل شيئًا آخر. والعنوان الذي يناسب جملة من E يناسب C كلها.',
    r11why='ثلاث مدن، ونتيجة في كل منها، ولا تراجع في أيّ منها: يجب أن يغطي '
           'العنوان المدن الثلاث والنتيجة. سياسة النقل تغطي أكثر من اللازم، '
           'والمدينة الواحدة أقل من اللازم.',
    r12why='خمسة عناوين استُخدمت بالفعل. اشطبها، فتختار الفقرتان الأخيرتان من '
           'خمسة لا من عشرة. وإعادة القراءة تكلّفك وقتًا لا تملكه.',

    sortEyebrow='النشاط 4 · عنوان صحيح أم فخّ؟',
    sortTitle='صنِّف الإشارات الست',
    sortHint='اسحب كل إشارة إلى عمود، أو انقر عليها ثم على العمود الذي تريده.',
    sortBin1='يشير إلى العنوان الصحيح',
    sortBin2='فخّ',
    sortWhy='كل ما في عمود «يشير إلى العنوان الصحيح» يصف عنوانًا <strong>يناسب '
            'الفقرة كلها</strong>: يسمّي الوظيفة، ويصحّ على كل جملة، ولا يعتمد '
            'على جملة بعينها. أما عمود «فخّ» فيضمّ الطرق الثلاث التي يبدو بها '
            'العنوان صحيحًا وهو ليس كذلك: كلمة مشتركة، أو تطابق مع السطر الأول '
            'وحده، أو ملاءمة يمكن أن تدّعيها فقرة أخرى بالقدر نفسه. كل منها طُعم '
            'يفعل تمامًا ما كُتب ليفعله.',

    actTitle='اكتب العناوين بنفسك',
    actUse='استخدم ثلاثة منها على الأقل:',
    actSpeakBrief='اعملا في ثنائي، ومعكما أي مقال. يكتب أحدكما عنوانًا لكل فقرة، '
                  'ثم يضيف عنوانين زائدين لا يناسبان شيئًا: واحد يكرّر كلمة من '
                  'النص، وآخر عام جدًّا. اخلطا القائمة وتبادلاها وطابقا. ثم '
                  'ناقشا كل مطابقة.',
    actSpeak1='على من يطابق أن يقول ماذا تفعل كل فقرة، عرضًا أو مقارنةً أو '
              'تحذيرًا، قبل أن يذكر عنوانها.',
    actSpeak2='عن كل طُعم، قل إلى أيّ فقرة كُتب ليجذبك، وما الذي يكشفه.',
    actSpeak3='جِد في قائمة زميلك عنوانًا يناسب فقرتين، وأعد كتابته ليناسب '
              'فقرة واحدة فقط.',
    actWriteKind='الكتابة · 150–200 كلمة',
    actWriteBrief='خذ نصًّا من ثلاث فقرات واكتب عنوانًا لكل فقرة. تحت كل عنوان، '
                  'اقتبس الجملة التي تثبت أنه الفكرة الرئيسية، وقل في سطر واحد '
                  'لماذا يغطي العنوان الفقرة كلها لا تلك الجملة وحدها.',
    actPlaceholder='Paragraph A — heading: … The sentence that proves it: …',
)


# ── Chinese ────────────────────────────────────────────────────────────
T['zh'] = dict(
    coverTitle='Matching <em>Headings</em>',
    coverSub='一个不按文章顺序出题的阅读任务——所以技巧也不一样',
    chipLevel='C1 · 高级', chipFocus='Reading · 两个模块通用',
    chipCount='18 分',

    t1Eyebrow='开始之前',
    t1Title='标题比段落多，而且没有顺序可依',
    t1ah='题目的形式',
    t1ab='一列用 i、ii、iii 编号的标题，加上一篇段落编为 A 到 G 的文章。每段配一'
         '个标题。标题总是比段落多，所以总有两三个用不上——而它们正是写来诱惑你'
         '的。',
    t1an='七个段落，十个标题，三个干扰项。这是常见的配比。',
    t1bh='一种会跳的题型',
    t1bb='大多数题型按文章顺序出题。这一种和 Matching Information 一样不按顺序：'
         '标题 i 可能属于段落 F，列表的顺序也不会告诉你去哪里找。答对四个，对第五'
         '个毫无帮助。',
    t1bn='它通常是这篇文章的第一组题，排在按顺序出题的题目前面。',
    t1ch='先读段落，再看列表',
    t1cb='陷阱在于先读十个标题，再去文中找——脑子里装着十个念头，个个都在找落脚'
         '处。先读段落 A，用自己的话说出它讲什么，然后才去列表里找说的是同一件事'
         '的标题。',
    t1cn='先写自己的概括，再看列表。每次都如此。',

    t2Eyebrow='开始之前',
    t2Title='问段落在做什么，而不是它讲什么',
    t2ah='功能重于话题',
    t2ab='两个段落可以话题相同，做的事却不同：一段提出问题，下一段举例，第三段权'
         '衡两种观点，第四段提出解决办法。标题点出的是功能。只点出话题的标题，'
         '文中一半的段落都能套上。',
    t2an='引出、举例、比较、警示、建议。五个动词就涵盖了段落的大部分功能。',
    t2bh='主题句会挪位置',
    t2bb='它通常在开头，而出题人知道你知道这一点。一个段落可能以例子开头、在结尾'
         '才点明观点，也可能在让步之后把观点藏在中间。读到最后一句再做决定。',
    t2bn='只和第一句对得上的标题，是整份试卷上最常见的错误答案。',
    t2ch='重复的词是诱饵',
    t2cb='如果标题用了段落里出现的词，就要警惕。正确的标题是改写过的：它用段落'
         '没用过的词说出段落的意思。错误的标题恰恰用段落里的词拼成，好让只会找'
         '词的考生找到它们。',
    t2cn='对一个词只要一秒，对一个意思要一句话。把这句话的时间花掉。',

    t3Eyebrow='开始之前',
    t3Title='先做有把握的，划掉，两可的放最后',
    t3ah='先做有把握的',
    t3ab='有些段落的标题一眼就能看出。不管它是哪个字母，先拿下。每确定一个，'
         '没把握的那几个可选范围就小一些，而最难的那一段，往往是靠剩下的标题'
         '而不是靠它的内容来决定的。',
    t3an='不要按 A 到 G 的顺序做，要从易到难。',
    t3bh='用过就划掉',
    t3bb='每个标题只用一次。一旦确定就从列表中划掉，同时划掉那个段落。只剩两段'
         '了，列表上却还是十个标题，这等于让你把已经做过的每个决定重新考虑一遍。',
    t3bn='靠铅笔，别靠记忆。时间一紧，你会忘了哪些已经用过。',
    t3ch='一个标题同时适合两段时',
    t3cb='先放着。做完其余的，等列表变短再回来。然后逐段问：这个标题覆盖的是整'
         '段，还是只是一句话？两段中有一段在别处有更好的标题，排除法能决定阅读'
         '决定不了的事。',
    t3cn='太笼统和太具体都不对。正确的标题只适合这一段，别的都不适合。',

    mcaEyebrow='练习 1 · 主旨',
    mcaTitle='读这一段。哪个标题能涵盖全段？',
    mcbEyebrow='练习 2 · 它在做什么？',
    mcbTitle='说出功能，而不是话题',
    mccEyebrow='练习 3 · 攻题顺序',
    mccTitle='用哪一步，选哪个标题？',

    r1why='螃蟹和百分之一是细节；整个海洋则超出了这一段的范围。唯一对每一句都成'
          '立的标题，是把体量和生命放在一起对照的那个。',
    r2why='第一个车站、第二个车站、脚下的地基：每一句都在讲同一个地点先后有两座'
          '车站。乘客是细节，拆除则从未解释。',
    r3why='照抄的手写字体、为大写首字母留的空、当作手抄本出售的印本——三个细节，'
          '一个意思：假装不是印刷品的印刷品。“印刷史”放在文中任何一段都说得通。',
    r4why='年份和最初的反应各只占一句。这一段讲的是完整的过程——禁令、抱怨、成功，'
          '以及抱怨的人被价格挤出市场。标题必须包括这个结局。',
    r5why='<em>Consider</em> 暴露了功能：这一段在举一个例子。港口里的一周和发动机'
          '是例子的细节；世界贸易是整篇文章的话题，不是这一段的功能。',
    r6why='它以拒绝一个结论开头，以一条建议结尾。这是在辩护。那些家庭和不理想的'
          '结果是证据，不是观点。',
    r7why='<em>A word of caution</em> 用四个词点明了功能。这一段不是在报告数字，'
          '也不是在讲装固定电话的家庭，而是在告诉你这些数字能信几分。',
    r8why='支持者、批评者，最后一句说双方始终谈不拢。村庄和电力是双方各自的说法；'
          '标题必须点出这种僵局。',
    r9why='先做有把握的，不管是哪个字母。每确定一个，列表上就少一个标题，难的'
          '段落就由剩下的标题来决定。',
    r10why='问每一段在做什么。C 讲的是成本；E 提到了成本，接着做了别的事。一个只'
           '适合 E 中一句话的标题，适合整个 C。',
    r11why='三个城市、每个城市的结果、没有一个走回头路：标题必须涵盖三个城市和'
           '结果。“交通政策”太宽，只讲一个城市又太窄。',
    r12why='五个标题已经用掉了。把它们划掉，最后两段就只在五个而不是十个标题里'
           '选。全部重读，花的是你没有的时间。',

    sortEyebrow='练习 4 · 正确标题，还是陷阱？',
    sortTitle='给这六个信号分类',
    sortHint='把每一项拖到一栏里——或者先点一项，再点你想放进的那一栏。',
    sortBin1='指向正确标题',
    sortBin2='陷阱',
    sortWhy='左栏的每一项描述的都是<strong>适合整段</strong>的标题：它点出功能，'
            '对每一句都成立，而且不依赖其中任何一句。右栏是标题看似正确、实则'
            '不对的三种情况——共用一个词、只和第一行对得上、另一段也同样适合。'
            '每一个都是干扰项，做的正是它被写出来要做的事。',

    actTitle='自己来写标题',
    actUse='至少用上三个：',
    actSpeakBrief='两人一组，手边随便准备一篇文章。一人为每一段写一个标题，再加'
                  '两个哪一段都不适合的多余标题——一个重复文中的某个词，一个太'
                  '笼统。打乱列表、交换、配对。然后为每一个配对说理。',
    actSpeak1='配对的人必须先说出每一段在做什么——引出、比较、警示——再说出它的'
              '标题。',
    actSpeak2='每个干扰项，说说它是写来引你配给哪一段的，以及是什么露出了破绽。',
    actSpeak3='在同伴的列表里找一个同时适合两段的标题，把它改写到只适合其中'
              '一段。',
    actWriteKind='写作 · 150–200 词',
    actWriteBrief='找一篇三段的文章，为每一段写一个标题。在每个标题下面，引用能'
                  '证明它是主旨的那一句话，再用一行说明为什么这个标题涵盖的是整'
                  '段，而不只是那一句。',
    actPlaceholder='Paragraph A — heading: … The sentence that proves it: …',
)


# ── Japanese ───────────────────────────────────────────────────────────
T['ja'] = dict(
    coverTitle='Matching <em>Headings</em>',
    coverSub='本文の順番どおりに進まない Reading の課題。だからテクニックも違い'
             'ます',
    chipLevel='C1 · 上級', chipFocus='Reading · 両モジュール共通',
    chipCount='18 点',

    t1Eyebrow='始める前に',
    t1Title='段落より見出しが多く、頼れる順番もない',
    t1ah='課題の形',
    t1ab='i、ii、iii と番号のついた見出しのリストと、A から G の段落がある本文。各'
         '段落に見出しを一つ選びます。見出しは必ず段落より多いので、二つか三つは'
         '使われません――そしてそれらは、つい選びたくなるように書かれています。',
    t1an='段落が七つ、見出しが十、おとりが三つ。これがよくある構成です。',
    t1bh='あちこちに飛ぶ形式',
    t1bb='ほとんどの形式は本文の順に進みます。この形式は Matching Information と'
         '同じく、そうなりません。見出し i が段落 F のものかもしれず、リストの順番'
         'はどこを探すべきかを何も教えてくれません。四つ答えても五つ目の手がかりに'
         'はなりません。',
    t1bn='ふつうはその本文の最初の設問で、順番どおりに進む設問より前に来ます。',
    t1ch='リストより先に段落を読む',
    t1cb='罠は、先に十の見出しを読んでから本文で探すことです――頭の中に十のアイデア'
         'があって、どれも置き場所を探している状態になります。段落 A を読み、何に'
         'ついての段落かを自分の言葉で言い、それからはじめて、同じことを言っている'
         '見出しをリストから探しましょう。',
    t1cn='まず自分の要約、次にリスト。毎回そうします。',

    t2Eyebrow='始める前に',
    t2Title='何についての段落かではなく、何をしている段落かを問う',
    t2ah='話題より機能',
    t2ab='二つの段落が同じ話題で、違う役割を果たすことがあります。一つは問題を提'
         '示し、次は例を挙げ、三つ目は二つの見方を比べ、四つ目は解決策を提案する。'
         '見出しが名づけるのは役割です。話題だけを名づけた見出しは、本文の半分に'
         '当てはまってしまいます。',
    t2an='導入する、例を示す、比べる、警告する、提案する。この五つの動詞で、段落'
         'の役割のほとんどをカバーできます。',
    t2bh='主題文は動き回る',
    t2bb='ふつうは最初にありますが、出題者はあなたがそれを知っていることを知って'
         'います。段落は例から始めて最後に要点を述べることも、譲歩のあとで真ん中'
         'に要点を埋めることもあります。最後の文まで読んでから決めましょう。',
    t2bn='最初の文とだけ合う見出しは、この試験で最もよくある誤答です。',
    t2ch='繰り返された語はエサ',
    t2cb='段落にある語が見出しに使われていたら、疑ってください。正しい見出しは言'
         'い換えています。段落が使っていない言葉で、段落の意味を言っているのです。'
         '誤りの見出しは段落の語彙で組み立てられていて、語を探す受験者に見つかるよ'
         'うにできています。',
    t2cn='語を照合するのは一秒、考えを照合するには一文かかります。その一文をかけ'
         'ましょう。',

    t3Eyebrow='始める前に',
    t3Title='確実なものから、消していき、二つに合うものは最後',
    t3ah='確実なものから',
    t3ab='見出しが明らかな段落があります。記号が何であれ、それを先に取りましょう。'
         '確実な組み合わせが一つ決まるたびに、迷っている段落の選択肢が減ります。い'
         'ちばん難しい段落は、その内容よりも残った見出しで決まることがよくあります。',
    t3an='A から G の順に解かないこと。易しいものから難しいものへ。',
    t3bh='使ったら消す',
    t3bb='見出しはそれぞれ一度しか使いません。決めたらすぐリストから消し、段落も'
         '消しましょう。残り二段落なのにリストに十の見出しが残っていたら、それまで'
         'の判断を全部見直せと言われているようなものです。',
    t3bn='記憶ではなく鉛筆で。時間に追われると、どれを使ったか忘れます。',
    t3ch='見出しが二つの段落に合うとき',
    t3cb='いったん置いておきます。残りを解き、リストが短くなってから戻りましょう。'
         'そして各段落について、この見出しは段落全体を覆っているか、それとも一文だ'
         'けかを問います。どちらか一方には別のもっと良い見出しがあり、読んでも決ま'
         'らなかったことが消去法で決まります。',
    t3cn='一般的すぎても具体的すぎてもだめです。正しい見出しはその段落に合い、ほ'
         'かのどれにも合いません。',

    mcaEyebrow='演習 1 · 要旨',
    mcaTitle='段落を読みましょう。全体を覆う見出しはどれか？',
    mcbEyebrow='演習 2 · 何をしているか？',
    mcbTitle='話題ではなく役割を名づける',
    mccEyebrow='演習 3 · 攻める順番',
    mccTitle='どの手順で、どの見出しか？',

    r1why='カニと1パーセントは細部です。海全体は段落が扱う範囲を超えています。す'
          'べての文に当てはまる見出しは、大きさを命と対比させたものだけです。',
    r2why='一つ目の駅、二つ目の駅、足元の基礎：どの文も、二つの駅を抱えた一つの場'
          '所の話です。乗客は細部で、取り壊しの理由は一度も説明されません。',
    r3why='写された手書きの書体、大文字のために空けた場所、写本として売られた本――'
          '三つの細部、一つの考え：印刷ではないふりをする印刷です。「印刷の歴史」な'
          'ら、本文のどの段落にも当てはまってしまいます。',
    r4why='年と最初の反応は、それぞれ一文にすぎません。段落は全体の流れです――禁止、'
          '苦情、成功、そして苦情を言った人々が値段で締め出されたこと。見出しは結末'
          'まで含んでいなければなりません。',
    r5why='<em>Consider</em> が手がかりです。この段落は一つの事例を示しています。'
          '港での一週間とエンジンはその細部で、世界の貿易は本文全体の話題であって、'
          'この段落の役割ではありません。',
    r6why='結論を拒むところから始まり、提言で終わります。これは擁護です。家族たち'
          'と振るわない結果は根拠であって、要点ではありません。',
    r7why='<em>A word of caution</em> が四語で役割を告げています。この段落は数字を'
          '報告しているのでも、固定電話のある世帯の話をしているのでもなく、その数字'
          'をどこまで信じてよいかを伝えています。',
    r8why='支持者、批判者、そして両者が決して歩み寄らないという最後の一文。村と電'
          '気はそれぞれの側の言い分で、見出しはこの膠着状態を名づけなければなりま'
          'せん。',
    r9why='記号に関係なく、確実なものから。確実な組み合わせが一つ決まるたびにリス'
          'トから見出しが一つ減り、難しい段落は残ったもので決まります。',
    r10why='各段落が何をしているかを問いましょう。C は費用の話です。E は費用に触れ'
           'たあと別のことをしています。E の一文に合う見出しは、C 全体に合います。',
    r11why='三つの都市、それぞれの結果、どれも元に戻っていない：見出しは三都市すべ'
           'てと結果を覆う必要があります。「交通政策」では広すぎ、一都市では狭すぎ'
           'ます。',
    r12why='すでに五つの見出しを使っています。それを消せば、最後の二段落は十では'
           'なく五つから選べます。全部読み直せば、ない時間を使うことになります。',

    sortEyebrow='演習 4 · 正しい見出しか、罠か？',
    sortTitle='六つのシグナルを分類しましょう',
    sortHint='それぞれを列にドラッグしてください。または項目をクリックしてから、'
             '入れたい列をクリックします。',
    sortBin1='正しい見出しを示す',
    sortBin2='罠',
    sortWhy='左の列はすべて、<strong>段落全体に合う</strong>見出しを表しています。'
            '役割を名づけ、どの文にも当てはまり、特定の一文に頼っていません。右の'
            '列は、正しく見えて実は正しくない三つのパターンです――共通の語、最初の'
            '行とだけの一致、別の段落にも同じように当てはまること。どれも、書かれ'
            'た目的どおりに働くおとりです。',

    actTitle='見出しを自分で書く',
    actUse='少なくとも三つ使いましょう：',
    actSpeakBrief='ペアで、手近な記事を一つ用意します。一人が各段落に見出しを書き、'
                  'さらにどれにも合わない見出しを二つ加えます――本文の語を繰り返す'
                  'ものと、一般的すぎるもの。リストを混ぜて交換し、組み合わせま'
                  'す。そのあと、一つひとつの組み合わせについて議論しましょう。',
    actSpeak1='組み合わせる人は、見出しを言う前に、各段落が何をしているか――導入、'
              '比較、警告――を言いましょう。',
    actSpeak2='おとりごとに、どの段落へ誘うために書かれたのか、何でそれが見破れるの'
              'かを言いましょう。',
    actSpeak3='相手のリストから二つの段落に合う見出しを一つ見つけ、一つの段落にだけ'
              '合うように書き直しましょう。',
    actWriteKind='ライティング · 150–200 語',
    actWriteBrief='三段落の文章を一つ選び、各段落に見出しを書きましょう。各見出し'
                  'の下に、それが要旨であることを証明する一文を引用し、見出しがそ'
                  'の一文だけでなく段落全体を覆っている理由を一行で書きます。',
    actPlaceholder='Paragraph A — heading: … The sentence that proves it: …',
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
