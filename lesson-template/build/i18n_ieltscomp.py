# -*- coding: utf-8 -*-
"""Interface strings for IELTS Reading: Summary and Sentence Completion.

English, German and Spanish, teach cards in the six-item form.

Same split as the rest of the IELTS route (HOUSE-STYLE §8): the rule and the
reason travel, the English under test does not. The instruction lines, the
passage excerpts, the gapped summary sentences and the four candidate answers
on every item stay English in every gloss — the skill is counting the English
words, lifting the English word and reading the English sentence, and a
German rendering of any of them would hand over the answer.

The explanations are translated, and they cite the candidate answers in
English inside <em>, as the sibling deck cites its passage lines: the learner
needs to see which of the four they were shown is the one being named.

The sort items are translated, and deliberately: they are descriptions of
answers a candidate might write ("Three words when the limit is two"), not
the English being tested, and a learner sorting them in German is making the
same decision as one sorting them in English.
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
    coverTitle='Summary and <em>Sentence Completion</em>',
    coverSub='Where the word limit does the damage &mdash; answers come '
             'straight from the passage, spelling counts, and one word too '
             'many scores nothing',
    chipLevel='C1 · Advanced', chipFocus='Reading · both modules',
    chipCount='18 points',

    t1Eyebrow='Before you start',
    t1Title='Three gaps, one instruction line, and the line comes first',
    t1ah='What you are given',
    t1ab='A summary of part of the passage, or a set of separate sentences, '
         'with gaps in them. The words that fill the gaps are in the passage. '
         'The summary usually runs in passage order, but it covers only a '
         'section &mdash; find where that section starts and stay in it.',
    t1an='Academic and General Training set it the same way. Everything here '
         'applies to both.',
    t1bh='Read the instruction first',
    t1bb='<strong>NO MORE THAN TWO WORDS AND/OR A NUMBER. ONE WORD '
         'ONLY.</strong> The limit is printed above the gaps and it is the '
         'first thing to read &mdash; before the summary, before the passage. '
         'It decides what a correct answer looks like before you have found '
         'one.',
    t1bn='A hyphenated word is one word. A number is a number, not a word. '
         '<em>The</em> is a word, and it counts.',
    t1ch='Sometimes there is a box',
    t1cb='When the task gives you a list of words, A&ndash;H, you choose from '
         'the list, not from the passage, and you write the letter. The words '
         'may not be in the text at all, and the list has more options than '
         'gaps.',
    t1cn='Same skill underneath: find the place in the passage, then check '
         'the grammar of the gap.',

    t2Eyebrow='Before you start',
    t2Title='The word is in the passage. Lift it.',
    t2ah='Find the place by meaning',
    t2ab='The summary does not repeat the passage; it paraphrases everything '
         '<strong>around</strong> the gap. Match the meaning of the sentence '
         'to find the right lines, then read those lines for the one word '
         'the summary did not change.',
    t2an='A shared word tells you where to look. The gap word is usually the '
         'one word that was not paraphrased.',
    t2bh='Then copy it, exactly',
    t2bb='Same spelling, same form as printed. Do not make it plural, do not '
         'change the tense, do not add an article the summary already has. A '
         'correct idea in your own words scores nothing, because the marker '
         'compares your answer with the key, not with the passage.',
    t2bn='If your word is not in the passage, it is not the answer.',
    t2ch='The limit is a wall',
    t2cb='Under NO MORE THAN TWO WORDS, a three-word answer scores nothing '
         'however right it is. Not half a mark: nothing. When an answer runs '
         'over, the extra word is almost always an article or an adjective '
         'you did not need.',
    t2cn='Write the answer, count it, then read the instruction line again.',

    t3Eyebrow='Before you start',
    t3Title='Predict the word before you look for it',
    t3ah='Name the word class first',
    t3ab='Read the summary sentence with the gap in it and decide what it '
         'needs: a noun, a verb, an adjective, a number. A gap after '
         '<em>the</em> or <em>a</em> wants a noun; a gap after the subject '
         'wants a verb; a gap after <em>lasted</em> or <em>cost</em> wants an '
         'amount.',
    t3an='Decide this before you open the passage. Then you are looking for '
         'one kind of word, not any word.',
    t3bh='The answer must read as English',
    t3bb='Put your word in the gap and read the whole sentence. Singular or '
         'plural, past or present: the summary sentence decides, and the '
         'passage word usually already fits, because the summary was written '
         'from it.',
    t3bn='If the sentence does not read, you have the wrong form or the wrong '
         'place.',
    t3ch='Spelling counts',
    t3cb='Even in a copied word. Transfer it letter by letter and check it '
         'against the passage, capitals included. A word you knew, copied '
         'wrongly, scores exactly what a word you did not know would have.',
    t3cn='Reading has no transfer time. Write on the answer sheet as you go.',

    mcaEyebrow='Activity 1 · Read the instruction',
    mcaTitle='What does the limit allow?',
    mcbEyebrow='Activity 2 · Copy, do not paraphrase',
    mcbTitle='Which answer scores?',
    mccEyebrow='Activity 3 · The gap has a shape',
    mccTitle='Which form fits the sentence?',

    r1why='Two words and a number. <em>The</em> is a word, so <em>the 1997 '
          'survey results</em> is three; <em>results of the survey</em> is '
          'four; <em>survey results from 1997</em> is three and a number. '
          'Only the first fits.',
    r2why='A hyphen joins: <em>well-known</em> is one word. The other three '
          'are two words each, and under ONE WORD ONLY they score nothing.',
    r3why='<em>A fall of 200 tonnes</em> is four words and a number, one over '
          'the limit. <em>In 1846</em> is one word and a number, and the '
          'other two are three words and a number: all allowed.',
    r4why='With a list you write a letter, and the words in the list need '
          'not be in the passage at all. The list has more options than '
          'gaps, the summary still covers only a section, and words are '
          'still counted as words.',
    r5why='The passage says <em>a process known as bleaching</em>; the '
          'summary paraphrases <em>warmer water</em> as <em>rising sea '
          'temperatures</em> and leaves the gap word alone. <em>Coral '
          'whitening</em> is the right idea in different words, '
          '<em>bleached</em> is the wrong form, <em>known as bleaching</em> '
          'is three words.',
    r6why='<em>Limestone aquifer</em>, as printed. <em>Underground '
          'reservoir</em> is a paraphrase; <em>limestone aquifers</em> is the '
          'wrong form; <em>a limestone aquifer</em> repeats the article the '
          'summary already has and runs to three words.',
    r7why='<em>Visiting engineer</em>, two words, exactly as printed. The '
          'plural does not fit after <em>a</em>; <em>travelling '
          'technician</em> is your own words; the version with the article '
          'doubles the <em>a</em> and breaks the limit.',
    r8why='One word: <em>olives</em>, as the passage has it. <em>Olive</em> '
          'is the wrong form, <em>olive groves</em> is not in the text, and '
          '<em>planted olives</em> is two words under ONE WORD ONLY.',
    r9why='A possessive, <em>the keeper&rsquo;s</em>, needs a noun. Of the '
          'four passage words only <em>entries</em> is one, and '
          '<em>became</em> confirms it: a thing that became shorter.',
    r10why='Subject, gap, object: the gap is the verb, and the summary is in '
           'the past because the passage is. <em>Reinforced</em>. The noun '
           'and the -ing form do not make a sentence, and '
           '<em>reinforces</em> disagrees with <em>engineers</em>.',
    r11why='<em>Was not ______ until</em> wants a past participle: the '
           'passive. <em>Correctly identified</em> is what the passage '
           'prints, and it reads. Predict that shape and three options fall '
           'away before you look.',
    r12why='<em>Took</em> wants a length of time: a number and a plural noun. '
           '<em>Eleven years</em>, as printed. The singular does not agree, '
           'the ordinal is a different word, and the article makes three.',

    sortEyebrow='Activity 4 · What the marker does',
    sortTitle='Sort the six answers',
    sortHint='Drag each one into a column &mdash; or click an item, then the '
             'column you want it in.',
    sortBin1='Scores',
    sortBin2='Scores nothing',
    sort1='Two words copied exactly from the passage',
    sort2='A number written as digits',
    sort3='A hyphenated word under a one-word limit',
    sort4='Three words when the limit is two',
    sort5='The right idea in your own words',
    sort6='The passage word with a spelling mistake',
    sortWhy='The left column are all <strong>the passage, within the limit, '
            'spelt as printed</strong> &mdash; a number is one item, a '
            'hyphenated word is one word. The right column are three ways of '
            'understanding the text and scoring nothing for it: one word '
            'over the limit, a correct idea in different words, a copied '
            'word with a letter wrong. The marker does not read for meaning. '
            'The marker compares your answer with the key.',

    actTitle='Set the gaps yourself',
    actUse='Use at least three:',
    actSpeakBrief='In pairs, with a short article each. Write a three-gap '
                  'summary of yours &mdash; four sentences, a word limit '
                  'above them &mdash; and swap. Your partner fills the gaps '
                  'from the article only; you mark as the examiner would: '
                  'passage word, within the limit, spelt as printed, or '
                  'nothing.',
    actSpeak1='Before filling any gap, say out loud what word class it needs '
              'and which words in the sentence tell you so.',
    actSpeak2='For every answer, point at the words in the article. An answer '
              'you cannot point at is not accepted.',
    actSpeak3='Find one gap in your partner&rsquo;s summary that two '
              'passage words could fill, and rewrite the sentence so only '
              'one can.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Take a passage you read this week and write a '
                  'four-sentence summary of it with three gaps, the word '
                  'limit stated above it. Then write the key: the exact '
                  'passage words for each gap, and one tempting wrong answer '
                  'with why it scores nothing.',
    actPlaceholder='NO MORE THAN TWO WORDS. Summary: … Gap 1: … Tempting '
                   'wrong answer: …',
)

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Summary and <em>Sentence Completion</em>',
    coverSub='Wo das Wortlimit den Schaden anrichtet &mdash; die Antworten '
             'stehen wörtlich im Text, Rechtschreibung zählt, und ein Wort zu '
             'viel gibt null Punkte',
    chipLevel='C1 · Fortgeschritten', chipFocus='Reading · beide Module',
    chipCount='18 Punkte',

    t1Eyebrow='Bevor du beginnst',
    t1Title='Drei Lücken, eine Anweisungszeile, und die Zeile kommt zuerst',
    t1ah='Was du bekommst',
    t1ab='Eine Zusammenfassung eines Textabschnitts oder einzelne Sätze, '
         'jeweils mit Lücken. Die Wörter für die Lücken stehen im Text. Die '
         'Zusammenfassung folgt meist der Textreihenfolge, deckt aber nur '
         'einen Abschnitt ab &mdash; finde, wo der beginnt, und bleib darin.',
    t1an='Academic und General Training stellen die Aufgabe gleich. Alles '
         'hier gilt für beide.',
    t1bh='Lies zuerst die Anweisung',
    t1bb='<strong>NO MORE THAN TWO WORDS AND/OR A NUMBER. ONE WORD '
         'ONLY.</strong> Das Limit steht über den Lücken und ist das Erste, '
         'was du liest &mdash; vor der Zusammenfassung, vor dem Text. Es legt '
         'fest, wie eine richtige Antwort aussieht, bevor du eine gefunden '
         'hast.',
    t1bn='Ein Wort mit Bindestrich ist ein Wort. Eine Zahl ist eine Zahl, '
         'kein Wort. <em>The</em> ist ein Wort, und es zählt.',
    t1ch='Manchmal gibt es einen Kasten',
    t1cb='Gibt die Aufgabe eine Wortliste A&ndash;H vor, wählst du aus der '
         'Liste, nicht aus dem Text, und schreibst den Buchstaben. Die Wörter '
         'müssen gar nicht im Text vorkommen, und die Liste hat mehr '
         'Optionen als Lücken.',
    t1cn='Darunter dieselbe Fertigkeit: die Stelle im Text finden, dann die '
         'Grammatik der Lücke prüfen.',

    t2Eyebrow='Bevor du beginnst',
    t2Title='Das Wort steht im Text. Hol es heraus.',
    t2ah='Finde die Stelle über die Bedeutung',
    t2ab='Die Zusammenfassung wiederholt den Text nicht; sie paraphrasiert '
         'alles <strong>um</strong> die Lücke herum. Gleiche die Bedeutung '
         'des Satzes ab, um die richtigen Zeilen zu finden, und lies dann '
         'diese Zeilen nach dem einen Wort, das die Zusammenfassung nicht '
         'verändert hat.',
    t2an='Ein gemeinsames Wort sagt dir, wo du suchst. Das Lückenwort ist '
         'meist das eine Wort, das nicht paraphrasiert wurde.',
    t2bh='Dann kopiere es, genau',
    t2bb='Dieselbe Schreibung, dieselbe Form wie gedruckt. Kein Plural, '
         'keine andere Zeit, kein Artikel, den die Zusammenfassung schon '
         'hat. Eine richtige Idee in eigenen Worten gibt null Punkte, denn '
         'der Prüfer vergleicht deine Antwort mit dem Lösungsschlüssel, '
         'nicht mit dem Text.',
    t2bn='Steht dein Wort nicht im Text, ist es nicht die Antwort.',
    t2ch='Das Limit ist eine Mauer',
    t2cb='Unter NO MORE THAN TWO WORDS bringt eine Antwort aus drei Wörtern '
         'nichts, so richtig sie auch ist. Nicht einen halben Punkt: nichts. '
         'Läuft eine Antwort über, ist das überzählige Wort fast immer ein '
         'Artikel oder ein Adjektiv, das du nicht gebraucht hättest.',
    t2cn='Antwort schreiben, Wörter zählen, dann die Anweisungszeile noch '
         'einmal lesen.',

    t3Eyebrow='Bevor du beginnst',
    t3Title='Sag das Wort voraus, bevor du es suchst',
    t3ah='Erst die Wortart benennen',
    t3ab='Lies den Satz mit der Lücke und entscheide, was sie braucht: ein '
         'Nomen, ein Verb, ein Adjektiv, eine Zahl. Eine Lücke nach '
         '<em>the</em> oder <em>a</em> will ein Nomen; eine Lücke nach dem '
         'Subjekt will ein Verb; eine Lücke nach <em>lasted</em> oder '
         '<em>cost</em> will eine Menge.',
    t3an='Entscheide das, bevor du den Text aufschlägst. Dann suchst du eine '
         'Art von Wort, nicht irgendein Wort.',
    t3bh='Die Antwort muss sich als Englisch lesen',
    t3bb='Setz dein Wort in die Lücke und lies den ganzen Satz. Singular oder '
         'Plural, Vergangenheit oder Gegenwart: der Satz der Zusammenfassung '
         'entscheidet, und das Textwort passt meist schon, weil die '
         'Zusammenfassung daraus geschrieben wurde.',
    t3bn='Liest sich der Satz nicht, hast du die falsche Form oder die '
         'falsche Stelle.',
    t3ch='Rechtschreibung zählt',
    t3cb='Auch bei einem kopierten Wort. Übertrag es Buchstabe für Buchstabe '
         'und prüf es gegen den Text, Großbuchstaben eingeschlossen. Ein '
         'Wort, das du kanntest und falsch abgeschrieben hast, bringt genau '
         'so viel wie eines, das du nicht kanntest.',
    t3cn='Reading hat keine Übertragungszeit. Schreib direkt auf den '
         'Antwortbogen.',

    mcaEyebrow='Aktivität 1 · Lies die Anweisung',
    mcaTitle='Was erlaubt das Limit?',
    mcbEyebrow='Aktivität 2 · Kopieren, nicht paraphrasieren',
    mcbTitle='Welche Antwort zählt?',
    mccEyebrow='Aktivität 3 · Die Lücke hat eine Form',
    mccTitle='Welche Form passt in den Satz?',

    r1why='Zwei Wörter und eine Zahl. <em>The</em> ist ein Wort, also hat '
          '<em>the 1997 survey results</em> drei; <em>results of the '
          'survey</em> hat vier; <em>survey results from 1997</em> hat drei '
          'und eine Zahl. Nur das erste passt.',
    r2why='Ein Bindestrich verbindet: <em>well-known</em> ist ein Wort. Die '
          'anderen drei sind je zwei Wörter, und unter ONE WORD ONLY bringen '
          'sie nichts.',
    r3why='<em>A fall of 200 tonnes</em> sind vier Wörter und eine Zahl, '
          'eines über dem Limit. <em>In 1846</em> ist ein Wort und eine '
          'Zahl, die anderen beiden sind drei Wörter und eine Zahl: alle '
          'erlaubt.',
    r4why='Bei einer Liste schreibst du einen Buchstaben, und die Wörter der '
          'Liste müssen gar nicht im Text stehen. Die Liste hat mehr '
          'Optionen als Lücken, die Zusammenfassung deckt weiter nur einen '
          'Abschnitt ab, und Wörter werden weiter als Wörter gezählt.',
    r5why='Der Text sagt <em>a process known as bleaching</em>; die '
          'Zusammenfassung paraphrasiert <em>warmer water</em> als '
          '<em>rising sea temperatures</em> und lässt das Lückenwort in '
          'Ruhe. <em>Coral whitening</em> ist die richtige Idee in anderen '
          'Worten, <em>bleached</em> die falsche Form, <em>known as '
          'bleaching</em> drei Wörter.',
    r6why='<em>Limestone aquifer</em>, wie gedruckt. <em>Underground '
          'reservoir</em> ist eine Paraphrase; <em>limestone aquifers</em> '
          'die falsche Form; <em>a limestone aquifer</em> wiederholt den '
          'Artikel, den die Zusammenfassung schon hat, und kommt auf drei '
          'Wörter.',
    r7why='<em>Visiting engineer</em>, zwei Wörter, genau wie gedruckt. Der '
          'Plural passt nicht nach <em>a</em>; <em>travelling '
          'technician</em> sind deine eigenen Worte; die Version mit Artikel '
          'verdoppelt das <em>a</em> und sprengt das Limit.',
    r8why='Ein Wort: <em>olives</em>, wie es im Text steht. <em>Olive</em> '
          'ist die falsche Form, <em>olive groves</em> steht nicht im Text, '
          'und <em>planted olives</em> sind zwei Wörter unter ONE WORD ONLY.',
    r9why='Ein Possessiv, <em>the keeper&rsquo;s</em>, braucht ein Nomen. '
          'Von den vier Textwörtern ist nur <em>entries</em> eines, und '
          '<em>became</em> bestätigt es: etwas, das kürzer wurde.',
    r10why='Subjekt, Lücke, Objekt: die Lücke ist das Verb, und die '
           'Zusammenfassung steht in der Vergangenheit, weil der Text es '
           'tut. <em>Reinforced</em>. Nomen und -ing-Form ergeben keinen '
           'Satz, und <em>reinforces</em> passt nicht zu '
           '<em>engineers</em>.',
    r11why='<em>Was not ______ until</em> will ein Partizip Perfekt: das '
           'Passiv. <em>Correctly identified</em> steht so im Text, und es '
           'liest sich. Sag diese Form voraus, und drei Optionen fallen weg, '
           'bevor du hinschaust.',
    r12why='<em>Took</em> will eine Zeitspanne: eine Zahl und ein Nomen im '
           'Plural. <em>Eleven years</em>, wie gedruckt. Der Singular passt '
           'nicht, die Ordnungszahl ist ein anderes Wort, und der Artikel '
           'macht drei daraus.',

    sortEyebrow='Aktivität 4 · Was der Prüfer tut',
    sortTitle='Sortiere die sechs Antworten',
    sortHint='Zieh jede in eine Spalte &mdash; oder klicke ein Element an und '
             'dann die Spalte, in die es soll.',
    sortBin1='Zählt',
    sortBin2='Zählt nicht',
    sort1='Zwei Wörter, genau aus dem Text übernommen',
    sort2='Eine Zahl in Ziffern geschrieben',
    sort3='Ein Wort mit Bindestrich bei Limit „ein Wort“',
    sort4='Drei Wörter, wenn das Limit zwei ist',
    sort5='Die richtige Idee in eigenen Worten',
    sort6='Das Textwort mit einem Rechtschreibfehler',
    sortWhy='Die linke Spalte ist durchweg <strong>der Text, innerhalb des '
            'Limits, geschrieben wie gedruckt</strong> &mdash; eine Zahl ist '
            'ein Element, ein Wort mit Bindestrich ein Wort. Die rechte '
            'Spalte sind drei Wege, den Text zu verstehen und nichts dafür '
            'zu bekommen: ein Wort über dem Limit, eine richtige Idee in '
            'anderen Worten, ein kopiertes Wort mit einem falschen '
            'Buchstaben. Der Prüfer liest nicht auf Bedeutung. Der Prüfer '
            'vergleicht deine Antwort mit dem Lösungsschlüssel.',

    actTitle='Setz die Lücken selbst',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu zweit, jeder mit einem kurzen Artikel. Schreib zu '
                  'deinem eine Zusammenfassung mit drei Lücken &mdash; vier '
                  'Sätze, ein Wortlimit darüber &mdash; und tauscht. Dein '
                  'Partner füllt sie nur aus dem Artikel; du bewertest wie '
                  'der Prüfer: Textwort, im Limit, wie gedruckt, oder '
                  'nichts.',
    actSpeak1='Sag vor jeder Lücke laut, welche Wortart sie braucht und '
              'welche Wörter im Satz dir das verraten.',
    actSpeak2='Zeig bei jeder Antwort auf die Wörter im Artikel. Eine '
              'Antwort, auf die du nicht zeigen kannst, gilt nicht.',
    actSpeak3='Finde in der Zusammenfassung deines Partners eine Lücke, die '
              'zwei verschiedene Textwörter füllen könnten, und schreib den '
              'Satz so um, dass nur eines passt.',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Nimm einen Text von dieser Woche und schreib eine '
                  'Zusammenfassung aus vier Sätzen mit drei Lücken, das '
                  'Wortlimit darüber. Dann den Lösungsschlüssel: zu jeder '
                  'Lücke die genauen Textwörter, dazu eine verlockende '
                  'falsche Antwort und warum sie nichts bringt.',
    actPlaceholder='NO MORE THAN TWO WORDS. Summary: … Gap 1: … Tempting '
                   'wrong answer: …',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Summary and <em>Sentence Completion</em>',
    coverSub='Donde el límite de palabras hace el daño: las respuestas salen '
             'tal cual del texto, la ortografía cuenta y una palabra de más '
             'no puntúa nada',
    chipLevel='C1 · Avanzado', chipFocus='Reading · los dos módulos',
    chipCount='18 puntos',

    t1Eyebrow='Antes de empezar',
    t1Title='Tres huecos, una línea de instrucciones, y la línea va primero',
    t1ah='Lo que te dan',
    t1ab='Un resumen de parte del texto, o varias frases sueltas, con '
         'huecos. Las palabras que los rellenan están en el texto. El '
         'resumen suele seguir el orden del texto, pero cubre solo una '
         'sección: localiza dónde empieza esa sección y quédate en ella.',
    t1an='Academic y General Training la plantean igual. Todo esto vale para '
         'los dos.',
    t1bh='Lee primero la instrucción',
    t1bb='<strong>NO MORE THAN TWO WORDS AND/OR A NUMBER. ONE WORD '
         'ONLY.</strong> El límite está impreso encima de los huecos y es lo '
         'primero que se lee: antes del resumen, antes del texto. Decide qué '
         'aspecto tiene una respuesta correcta antes de que hayas encontrado '
         'una.',
    t1bn='Una palabra con guion es una palabra. Un número es un número, no '
         'una palabra. <em>The</em> es una palabra, y cuenta.',
    t1ch='A veces hay un recuadro',
    t1cb='Cuando la tarea te da una lista de palabras, A&ndash;H, eliges de '
         'la lista, no del texto, y escribes la letra. Las palabras pueden '
         'no estar en el texto en absoluto, y la lista tiene más opciones '
         'que huecos.',
    t1cn='Debajo, la misma destreza: encontrar el sitio en el texto y '
         'comprobar la gramática del hueco.',

    t2Eyebrow='Antes de empezar',
    t2Title='La palabra está en el texto. Sácala.',
    t2ah='Encuentra el sitio por el significado',
    t2ab='El resumen no repite el texto: parafrasea todo lo que hay '
         '<strong>alrededor</strong> del hueco. Coteja el significado de la '
         'frase para dar con las líneas correctas, y luego busca en esas '
         'líneas la única palabra que el resumen no ha cambiado.',
    t2an='Una palabra compartida te dice dónde mirar. La palabra del hueco '
         'suele ser la única que no se parafraseó.',
    t2bh='Y luego cópiala, exactamente',
    t2bb='La misma ortografía, la misma forma que está impresa. No la pongas '
         'en plural, no le cambies el tiempo, no le añadas un artículo que '
         'el resumen ya tiene. Una idea correcta con tus palabras no puntúa '
         'nada, porque el corrector compara tu respuesta con la clave, no '
         'con el texto.',
    t2bn='Si tu palabra no está en el texto, no es la respuesta.',
    t2ch='El límite es un muro',
    t2cb='Con NO MORE THAN TWO WORDS, una respuesta de tres palabras no '
         'puntúa nada por muy correcta que sea. Ni medio punto: nada. Cuando '
         'una respuesta se pasa, la palabra sobrante es casi siempre un '
         'artículo o un adjetivo que no hacía falta.',
    t2cn='Escribe la respuesta, cuéntala y vuelve a leer la línea de '
         'instrucciones.',

    t3Eyebrow='Antes de empezar',
    t3Title='Predice la palabra antes de buscarla',
    t3ah='Primero, nombra la clase de palabra',
    t3ab='Lee la frase del resumen con el hueco y decide qué necesita: un '
         'sustantivo, un verbo, un adjetivo, un número. Un hueco tras '
         '<em>the</em> o <em>a</em> pide un sustantivo; un hueco tras el '
         'sujeto pide un verbo; un hueco tras <em>lasted</em> o '
         '<em>cost</em> pide una cantidad.',
    t3an='Decídelo antes de abrir el texto. Así buscas un tipo de palabra, no '
         'cualquier palabra.',
    t3bh='La respuesta tiene que leerse como inglés',
    t3bb='Pon tu palabra en el hueco y lee la frase entera. Singular o '
         'plural, pasado o presente: lo decide la frase del resumen, y la '
         'palabra del texto suele encajar ya, porque el resumen se escribió '
         'a partir de ella.',
    t3bn='Si la frase no se lee bien, tienes la forma equivocada o el sitio '
         'equivocado.',
    t3ch='La ortografía cuenta',
    t3cb='Incluso en una palabra copiada. Pásala letra a letra y compruébala '
         'contra el texto, mayúsculas incluidas. Una palabra que conocías, '
         'copiada mal, puntúa exactamente lo mismo que una que no conocías.',
    t3cn='El Reading no tiene tiempo de transcripción. Escribe en la hoja de '
         'respuestas sobre la marcha.',

    mcaEyebrow='Actividad 1 · Lee la instrucción',
    mcaTitle='¿Qué permite el límite?',
    mcbEyebrow='Actividad 2 · Copiar, no parafrasear',
    mcbTitle='¿Qué respuesta puntúa?',
    mccEyebrow='Actividad 3 · El hueco tiene forma',
    mccTitle='¿Qué forma encaja en la frase?',

    r1why='Dos palabras y un número. <em>The</em> es una palabra, así que '
          '<em>the 1997 survey results</em> son tres; <em>results of the '
          'survey</em> son cuatro; <em>survey results from 1997</em> son '
          'tres y un número. Solo la primera cabe.',
    r2why='El guion une: <em>well-known</em> es una palabra. Las otras tres '
          'son dos palabras cada una, y con ONE WORD ONLY no puntúan nada.',
    r3why='<em>A fall of 200 tonnes</em> son cuatro palabras y un número, '
          'una por encima del límite. <em>In 1846</em> es una palabra y un '
          'número, y las otras dos son tres palabras y un número: todas '
          'permitidas.',
    r4why='Con una lista escribes una letra, y las palabras de la lista no '
          'tienen por qué estar en el texto. La lista tiene más opciones '
          'que huecos, el resumen sigue cubriendo solo una sección, y las '
          'palabras se siguen contando como palabras.',
    r5why='El texto dice <em>a process known as bleaching</em>; el resumen '
          'parafrasea <em>warmer water</em> como <em>rising sea '
          'temperatures</em> y deja en paz la palabra del hueco. <em>Coral '
          'whitening</em> es la idea correcta con otras palabras, '
          '<em>bleached</em> es la forma equivocada, <em>known as '
          'bleaching</em> son tres palabras.',
    r6why='<em>Limestone aquifer</em>, tal como está impreso. '
          '<em>Underground reservoir</em> es una paráfrasis; <em>limestone '
          'aquifers</em> es la forma equivocada; <em>a limestone '
          'aquifer</em> repite el artículo que el resumen ya tiene y llega a '
          'tres palabras.',
    r7why='<em>Visiting engineer</em>, dos palabras, exactamente como está '
          'impreso. El plural no encaja tras <em>a</em>; <em>travelling '
          'technician</em> son tus propias palabras; la versión con artículo '
          'duplica la <em>a</em> y rompe el límite.',
    r8why='Una palabra: <em>olives</em>, como la tiene el texto. '
          '<em>Olive</em> es la forma equivocada, <em>olive groves</em> no '
          'está en el texto, y <em>planted olives</em> son dos palabras con '
          'ONE WORD ONLY.',
    r9why='Un posesivo, <em>the keeper&rsquo;s</em>, necesita un sustantivo. '
          'De las cuatro palabras del texto solo <em>entries</em> lo es, y '
          '<em>became</em> lo confirma: algo que se volvió más corto.',
    r10why='Sujeto, hueco, objeto: el hueco es el verbo, y el resumen está en '
           'pasado porque el texto lo está. <em>Reinforced</em>. El '
           'sustantivo y la forma en -ing no hacen frase, y '
           '<em>reinforces</em> no concuerda con <em>engineers</em>.',
    r11why='<em>Was not ______ until</em> pide un participio: la pasiva. '
           '<em>Correctly identified</em> es lo que imprime el texto, y se '
           'lee bien. Predice esa forma y tres opciones caen antes de mirar.',
    r12why='<em>Took</em> pide una duración: un número y un sustantivo en '
           'plural. <em>Eleven years</em>, tal como está impreso. El singular '
           'no concuerda, el ordinal es otra palabra, y el artículo hace '
           'tres.',

    sortEyebrow='Actividad 4 · Lo que hace el corrector',
    sortTitle='Clasifica las seis respuestas',
    sortHint='Arrastra cada una a una columna &mdash; o haz clic en un '
             'elemento y luego en la columna que quieras.',
    sortBin1='Puntúa',
    sortBin2='No puntúa nada',
    sort1='Dos palabras copiadas tal cual del texto',
    sort2='Un número escrito en cifras',
    sort3='Una palabra con guion con límite de una palabra',
    sort4='Tres palabras cuando el límite es dos',
    sort5='La idea correcta con tus propias palabras',
    sort6='La palabra del texto con una falta de ortografía',
    sortWhy='La columna izquierda es toda <strong>el texto, dentro del '
            'límite, escrito como está impreso</strong>: un número es un '
            'elemento, una palabra con guion es una palabra. La derecha son '
            'tres maneras de entender el texto y no puntuar nada: una '
            'palabra por encima del límite, una idea correcta con otras '
            'palabras, una palabra copiada con una letra mal. El corrector '
            'no lee buscando significado. El corrector compara tu respuesta '
            'con la clave.',

    actTitle='Pon tú los huecos',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas, cada uno con un artículo corto. Escribe un '
                  'resumen del tuyo con tres huecos &mdash; cuatro frases, '
                  'un límite de palabras encima &mdash; e intercambiad. Tu '
                  'compañero los rellena solo con el artículo; tú corriges '
                  'como el examinador: palabra del texto, dentro del límite, '
                  'como está impresa, o nada.',
    actSpeak1='Antes de rellenar cada hueco, di en voz alta qué clase de '
              'palabra necesita y qué palabras de la frase te lo dicen.',
    actSpeak2='En cada respuesta, señala las palabras en el artículo. Una '
              'respuesta que no puedes señalar no se acepta.',
    actSpeak3='Busca en el resumen de tu compañero un hueco que dos palabras '
              'distintas del texto podrían rellenar, y reescribe la frase '
              'para que solo encaje una.',
    actWriteKind='Escritura · 150–200 palabras',
    actWriteBrief='Coge un texto que hayas leído esta semana y escribe un '
                  'resumen de cuatro frases con tres huecos, con el límite '
                  'de palabras encima. Luego la clave: las palabras exactas '
                  'del texto para cada hueco, y una respuesta equivocada '
                  'tentadora con por qué no puntúa nada.',
    actPlaceholder='NO MORE THAN TWO WORDS. Summary: … Gap 1: … Tempting '
                   'wrong answer: …',
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
