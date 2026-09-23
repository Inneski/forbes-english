# -*- coding: utf-8 -*-
"""Interface strings for IELTS Reading: Matching Headings.

English, German and Spanish, teach cards in the six-item form.

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
    sortWhy='The left column all describe a heading that <strong>fits the '
            'paragraph as a whole</strong>: it names the job, it holds for '
            'every sentence, and it does not depend on any one of them. The '
            'right column are the three ways a heading looks right without '
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
