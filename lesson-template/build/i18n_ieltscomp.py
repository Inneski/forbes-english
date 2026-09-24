# -*- coding: utf-8 -*-
"""Interface strings for IELTS Reading: Summary and Sentence Completion.

Ten languages: English, German and Spanish from the start; French,
Italian, Portuguese, Russian, Arabic, Chinese and Japanese added on
2026-09-24 (conventions in `ielts_langs.py`).

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
         'with gaps in them. The words that fill the gaps are in the '
         'passage. The summary usually runs in passage order and usually '
         'covers one section of it &mdash; find where that section starts '
         'and stay in it.',
    t1an='Academic and General Training set it the same way. Everything here '
         'applies to both.',
    t1bh='Read the instruction first',
    t1bb='<strong>NO MORE THAN TWO WORDS AND/OR A NUMBER. ONE WORD '
         'ONLY.</strong> The limit is printed above the gaps and it is the '
         'first thing to read &mdash; before the summary, before the passage. '
         'It decides what a correct answer looks like before you have found '
         'one.',
    t1bn='A hyphenated word is one word, and <em>the</em> is a word that '
         'counts. Under AND/OR A NUMBER, a number is allowed on top of the '
         'words; under a plain word limit, count it as a word.',
    t1ch='Sometimes there is a box',
    t1cb='When the task gives you a list of words, A&ndash;H, you choose from '
         'the list, not from the passage, and you write the letter. The words '
         'might not be in the text at all, and the list has more options than '
         'gaps.',
    t1cn='Same skill underneath: find the place in the passage, then check '
         'the grammar of the gap.',

    t2Eyebrow='Before you start',
    t2Title='The word is in the passage. Lift it.',
    t2ah='Find the place by meaning',
    t2ab='The summary rarely repeats the passage word for word; it '
         'paraphrases most of what is <strong>around</strong> the gap. Match '
         'the meaning of the sentence to find the right lines, then read '
         'those lines for the word the summary has left out.',
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
         'over, the extra word is often an article, an adjective or a '
         'preposition you did not need.',
    t2cn='Write the answer, count it, then read the instruction line again.',

    t3Eyebrow='Before you start',
    t3Title='Predict the word before you look for it',
    t3ah='Name the word class first',
    t3ab='Read the summary sentence with the gap in it and decide what it '
         'needs: a noun, a verb, an adjective, a number. A gap after '
         '<em>the</em> or <em>a</em> wants a noun, or an adjective if a noun '
         'follows the gap; a gap after the subject wants a verb; a gap after '
         '<em>lasted</em> or <em>cost</em> wants an amount.',
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
         'against the passage. A word you knew, copied '
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
          'Only <em>1997 survey results</em> fits.',
    r2why='A hyphen joins: <em>well-known</em> is one word. The other three '
          'are two words each, and under ONE WORD ONLY they score nothing.',
    r3why='<em>A fall of 200 tonnes</em> is four words and a number, one over '
          'the limit. <em>In 1846</em> is one word and a number, <em>nearly '
          '200 tonnes</em> two words and a number, and <em>some 200 tonnes '
          'each</em> three words and a number: all allowed.',
    r4why='With a list you write a letter, and the words in the list need '
          'not be in the passage at all. The list has more options than '
          'gaps, the summary usually still covers one section, and there is '
          'no word limit: the answer is a letter.',
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
    r12why='<em>Took</em> wants a length of time: a number and a plural '
           'noun. <em>Eleven years</em>, as printed. The singular does not '
           'agree, the ordinal is a different word, and <em>an</em> cannot '
           'go before a plural.',

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
    sortWhy='Everything that <strong>scores</strong> is the passage, within '
            'the limit, spelt as printed &mdash; a number is one item, a '
            'hyphenated word is one word. The other column holds three ways '
            'of understanding the text and scoring nothing for it: one word '
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
    t1ab='Eine Zusammenfassung eines Teils des Textes oder eine Reihe '
         'einzelner Sätze, jeweils mit Lücken. Die Wörter für die Lücken '
         'stehen im Text. Die Zusammenfassung folgt meist der Reihenfolge '
         'des Textes und deckt meist einen Abschnitt ab &mdash; finde, wo '
         'dieser Abschnitt beginnt, und bleib darin.',
    t1an='Academic und General Training stellen die Aufgabe gleich. Alles '
         'hier gilt für beide.',
    t1bh='Lies zuerst die Anweisung',
    t1bb='<strong>NO MORE THAN TWO WORDS AND/OR A NUMBER. ONE WORD '
         'ONLY.</strong> Das Limit steht über den Lücken und ist das Erste, '
         'was du liest &mdash; vor der Zusammenfassung, vor dem Text. Es legt '
         'fest, wie eine richtige Antwort aussieht, bevor du eine gefunden '
         'hast.',
    t1bn='Ein Wort mit Bindestrich ist ein Wort, und <em>the</em> ist ein '
         'Wort, das zählt. Bei AND/OR A NUMBER ist eine Zahl zusätzlich zu '
         'den Wörtern erlaubt; bei einem reinen Wortlimit zählt sie als Wort.',
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
    t2ab='Die Zusammenfassung wiederholt den Text selten Wort für Wort; sie '
         'paraphrasiert das meiste <strong>rund um</strong> die Lücke. '
         'Gleich die Bedeutung des Satzes ab, um die richtigen Zeilen zu '
         'finden, und such dann in diesen Zeilen das Wort, das die '
         'Zusammenfassung weggelassen hat.',
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
    t2cb='Bei NO MORE THAN TWO WORDS bringt eine Antwort aus drei Wörtern '
         'nichts, egal wie richtig sie ist. Kein halber Punkt: nichts. Wenn '
         'eine Antwort zu lang wird, ist das überzählige Wort oft ein '
         'Artikel, ein Adjektiv oder eine Präposition, die du nicht '
         'gebraucht hast.',
    t2cn='Antwort schreiben, Wörter zählen, dann die Anweisungszeile noch '
         'einmal lesen.',

    t3Eyebrow='Bevor du beginnst',
    t3Title='Sag das Wort voraus, bevor du es suchst',
    t3ah='Erst die Wortart benennen',
    t3ab='Lies den Satz mit der Lücke und entscheide, was sie braucht: ein '
         'Nomen, ein Verb, ein Adjektiv, eine Zahl. Eine Lücke nach '
         '<em>the</em> oder <em>a</em> will ein Nomen &mdash; oder ein '
         'Adjektiv, wenn nach der Lücke ein Nomen folgt; eine Lücke nach dem '
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
         'und prüf es gegen den Text. Ein '
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
          'und eine Zahl. Nur <em>1997 survey results</em> passt.',
    r2why='Ein Bindestrich verbindet: <em>well-known</em> ist ein Wort. Die '
          'anderen drei sind je zwei Wörter, und unter ONE WORD ONLY bringen '
          'sie nichts.',
    r3why='<em>A fall of 200 tonnes</em> sind vier Wörter und eine Zahl, '
          'eines über dem Limit. <em>In 1846</em> ist ein Wort und eine '
          'Zahl, <em>nearly 200 tonnes</em> zwei Wörter und eine Zahl, <em>some '
          '200 tonnes each</em> drei Wörter und eine Zahl: alle erlaubt.',
    r4why='Mit einer Liste schreibst du einen Buchstaben, und die Wörter der '
          'Liste müssen gar nicht im Text stehen. Die Liste hat mehr '
          'Optionen als Lücken, die Zusammenfassung deckt meist trotzdem '
          'einen Abschnitt ab, und es gibt kein Wortlimit: Die Antwort ist '
          'ein Buchstabe.',
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
    r12why='<em>Took</em> verlangt eine Zeitdauer: eine Zahl und ein Nomen '
           'im Plural. <em>Eleven years</em>, wie gedruckt. Der Singular '
           'passt nicht, die Ordnungszahl ist ein anderes Wort, und '
           '<em>an</em> kann nicht vor einem Plural stehen.',

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
    sortWhy='Alles, was <strong>zählt</strong>, ist der Text, innerhalb des '
            'Limits, geschrieben wie gedruckt &mdash; eine Zahl ist ein '
            'Element, ein Wort mit Bindestrich ist ein Wort. Die andere '
            'Spalte enthält drei Arten, den Text verstanden zu haben und '
            'trotzdem nichts dafür zu bekommen: ein Wort über dem Limit, '
            'eine richtige Idee in anderen Worten, ein abgeschriebenes Wort '
            'mit einem falschen Buchstaben. Der Korrektor liest nicht auf '
            'Bedeutung. Er vergleicht deine Antwort mit dem Schlüssel.',

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
    t1ab='Un resumen de una parte del texto, o una serie de frases sueltas, '
         'con huecos. Las palabras que llenan los huecos están en el texto. '
         'El resumen suele seguir el orden del texto y suele cubrir una '
         'sección &mdash; encuentra dónde empieza esa sección y no salgas de '
         'ella.',
    t1an='Academic y General Training la plantean igual. Todo esto vale para '
         'los dos.',
    t1bh='Lee primero la instrucción',
    t1bb='<strong>NO MORE THAN TWO WORDS AND/OR A NUMBER. ONE WORD '
         'ONLY.</strong> El límite está impreso encima de los huecos y es lo '
         'primero que se lee: antes del resumen, antes del texto. Decide qué '
         'aspecto tiene una respuesta correcta antes de que hayas encontrado '
         'una.',
    t1bn='Una palabra con guion es una palabra, y <em>the</em> es una '
         'palabra que cuenta. Con AND/OR A NUMBER, se permite un número '
         'además de las palabras; con un límite solo de palabras, cuéntalo '
         'como una palabra.',
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
    t2ab='El resumen rara vez repite el texto palabra por palabra; '
         'parafrasea casi todo lo que hay <strong>alrededor</strong> del '
         'hueco. Busca el sentido de la frase para encontrar las líneas '
         'correctas y luego lee esas líneas buscando la palabra que el '
         'resumen ha dejado fuera.',
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
         'puntúa, por correcta que sea. Ni medio punto: nada. Cuando una '
         'respuesta se pasa, la palabra de más suele ser un artículo, un '
         'adjetivo o una preposición que no necesitabas.',
    t2cn='Escribe la respuesta, cuéntala y vuelve a leer la línea de '
         'instrucciones.',

    t3Eyebrow='Antes de empezar',
    t3Title='Predice la palabra antes de buscarla',
    t3ah='Primero, nombra la clase de palabra',
    t3ab='Lee la frase del resumen con el hueco y decide qué necesita: un '
         'sustantivo, un verbo, un adjetivo, un número. Un hueco tras '
         '<em>the</em> o <em>a</em> pide un sustantivo, o un adjetivo si '
         'detrás del hueco viene un sustantivo; un hueco tras el sujeto pide '
         'un verbo; un hueco tras <em>lasted</em> o <em>cost</em> pide una '
         'cantidad.',
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
         'contra el texto. Una palabra que conocías, '
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
          'tres y un número. Solo cabe <em>1997 survey results</em>.',
    r2why='El guion une: <em>well-known</em> es una palabra. Las otras tres '
          'son dos palabras cada una, y con ONE WORD ONLY no puntúan nada.',
    r3why='<em>A fall of 200 tonnes</em> son cuatro palabras y un número, '
          'una por encima del límite. <em>In 1846</em> es una palabra y un '
          'número, <em>nearly 200 tonnes</em> dos palabras y un número, y '
          '<em>some 200 tonnes each</em> tres palabras y un número: todas '
          'permitidas.',
    r4why='Con una lista escribes una letra, y las palabras de la lista ni '
          'siquiera tienen que estar en el texto. La lista tiene más '
          'opciones que huecos, el resumen suele cubrir igualmente una '
          'sección, y no hay límite de palabras: la respuesta es una letra.',
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
           'plural. <em>Eleven years</em>, tal como está impreso. El '
           'singular no concuerda, el ordinal es otra palabra, y <em>an</em> '
           'no puede ir delante de un plural.',

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
    sortWhy='Todo lo que <strong>puntúa</strong> es el texto, dentro del '
            'límite, escrito como está impreso: un número es un elemento y '
            'una palabra con guion es una palabra. La otra columna recoge '
            'tres formas de entender el texto y no puntuar por ello: una '
            'palabra de más, una idea correcta con otras palabras, una '
            'palabra copiada con una letra mal. El corrector no lee buscando '
            'el sentido: compara tu respuesta con la clave.',

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


# ── French ─────────────────────────────────────────────────────────────
T['fr'] = dict(
    coverTitle='Summary and <em>Sentence Completion</em>',
    coverSub='Là où la limite de mots fait des dégâts &mdash; les réponses '
             'viennent tout droit du texte, l’orthographe compte, et un mot de '
             'trop ne rapporte rien',
    chipLevel='C1 · Avancé', chipFocus='Reading · les deux modules',
    chipCount='18 points',

    t1Eyebrow='Avant de commencer',
    t1Title='Trois trous, une ligne de consigne, et la ligne d’abord',
    t1ah='Ce qu’on vous donne',
    t1ab='Un résumé d’une partie du texte, ou une série de phrases séparées, '
         'avec des trous. Les mots qui remplissent les trous sont dans le '
         'texte. Le résumé suit en général l’ordre du texte et couvre en '
         'général une section &mdash; trouvez où commence cette section et '
         'restez-y.',
    t1an='Academic et General Training la présentent de la même façon. Tout ce '
         'qui suit vaut pour les deux.',
    t1bh='Lisez d’abord la consigne',
    t1bb='<strong>NO MORE THAN TWO WORDS AND/OR A NUMBER. ONE WORD '
         'ONLY.</strong> La limite est imprimée au-dessus des trous, et c’est '
         'la première chose à lire &mdash; avant le résumé, avant le texte. '
         'Elle décide à quoi ressemble une bonne réponse avant même que vous en '
         'ayez trouvé une.',
    t1bn='Un mot à trait d’union compte pour un mot, et <em>the</em> est un '
         'mot qui compte. Avec AND/OR A NUMBER, un nombre est permis en plus '
         'des mots ; avec une simple limite de mots, comptez-le comme un mot.',
    t1ch='Parfois il y a un encadré',
    t1cb='Quand la tâche vous donne une liste de mots, A&ndash;H, vous '
         'choisissez dans la liste, pas dans le texte, et vous écrivez la '
         'lettre. Les mots peuvent ne pas figurer du tout dans le texte, et la '
         'liste propose plus d’options que de trous.',
    t1cn='La même compétence au fond : trouver l’endroit dans le texte, puis '
         'vérifier la grammaire du trou.',

    t2Eyebrow='Avant de commencer',
    t2Title='Le mot est dans le texte. Prenez-le.',
    t2ah='Trouvez l’endroit par le sens',
    t2ab='Le résumé reprend rarement le texte mot pour mot ; il reformule '
         'l’essentiel de ce qui entoure le trou. Appuyez-vous sur le sens de '
         'la phrase pour trouver les bonnes lignes, puis cherchez dans ces '
         'lignes le mot que le résumé a laissé de côté.',
    t2an='Un mot commun vous dit où chercher. Le mot du trou est en général le '
         'seul qui n’a pas été reformulé.',
    t2bh='Puis recopiez-le, exactement',
    t2bb='Même orthographe, même forme que dans le texte. Ne le mettez pas au '
         'pluriel, ne changez pas le temps, n’ajoutez pas un article que le '
         'résumé a déjà. Une idée juste avec vos propres mots ne rapporte rien, '
         'car le correcteur compare votre réponse au corrigé, pas au texte.',
    t2bn='Si votre mot n’est pas dans le texte, ce n’est pas la réponse.',
    t2ch='La limite est un mur',
    t2cb='Avec NO MORE THAN TWO WORDS, une réponse de trois mots ne rapporte '
         'rien, aussi juste soit-elle. Pas un demi-point : rien. Quand une '
         'réponse déborde, le mot en trop est souvent un article, un '
         'adjectif ou une préposition dont vous n’aviez pas besoin.',
    t2cn='Écrivez la réponse, comptez les mots, puis relisez la consigne.',

    t3Eyebrow='Avant de commencer',
    t3Title='Prédisez le mot avant de le chercher',
    t3ah='Nommez d’abord la nature du mot',
    t3ab='Lisez la phrase du résumé qui contient le trou et décidez ce qu’il '
         'lui faut : un nom, un verbe, un adjectif, un nombre. Un trou après '
         '<em>the</em> ou <em>a</em> appelle un nom, ou un adjectif si un '
         'nom suit le trou ; un trou après le sujet appelle un verbe ; un '
         'trou après <em>lasted</em> ou <em>cost</em> appelle une quantité.',
    t3an='Décidez-le avant d’ouvrir le texte. Vous cherchez alors une seule '
         'sorte de mot, pas n’importe lequel.',
    t3bh='La réponse doit être de l’anglais correct',
    t3bb='Mettez votre mot dans le trou et lisez toute la phrase. Singulier ou '
         'pluriel, passé ou présent : c’est la phrase du résumé qui décide, et '
         'le mot du texte convient en général déjà, puisque le résumé a été '
         'écrit à partir de lui.',
    t3bn='Si la phrase ne tient pas, vous avez la mauvaise forme ou le mauvais '
         'endroit.',
    t3ch='L’orthographe compte',
    t3cb='Même pour un mot recopié. Recopiez-le lettre par lettre et '
         'vérifiez-le dans le texte. Un mot que vous connaissiez, mal recopié, '
         'rapporte exactement autant qu’un mot que vous ne connaissiez pas.',
    t3cn='Le Reading n’a pas de temps de report. Écrivez sur la feuille de '
         'réponses au fur et à mesure.',

    mcaEyebrow='Activité 1 · Lisez la consigne',
    mcaTitle='Qu’est-ce que la limite autorise ?',
    mcbEyebrow='Activité 2 · Recopiez, ne reformulez pas',
    mcbTitle='Quelle réponse rapporte des points ?',
    mccEyebrow='Activité 3 · Le trou a une forme',
    mccTitle='Quelle forme convient à la phrase ?',

    r1why='Deux mots et un nombre. <em>The</em> est un mot, donc <em>the 1997 '
          'survey results</em> en fait trois ; <em>results of the survey</em> '
          'en fait quatre ; <em>survey results from 1997</em> fait trois mots '
          'et un nombre. Seul <em>1997 survey results</em> tient dans la '
          'limite.',
    r2why='Le trait d’union unit : <em>well-known</em> compte pour un mot. Les '
          'trois autres font deux mots chacun, et avec ONE WORD ONLY ils ne '
          'rapportent rien.',
    r3why='<em>A fall of 200 tonnes</em> fait quatre mots et un nombre, un de '
          'trop. <em>In 1846</em> fait un mot et un nombre, <em>nearly 200 '
          'tonnes</em> deux mots et un nombre, et <em>some 200 tonnes each</em> '
          'trois mots et un nombre : tous autorisés.',
    r4why='Avec une liste, vous écrivez une lettre, et les mots de la liste '
          'ne figurent pas forcément dans le texte. La liste a plus '
          'd’options que de trous, le résumé couvre en général toujours une '
          'section, et il n’y a pas de limite de mots : la réponse est une '
          'lettre.',
    r5why='Le texte dit <em>a process known as bleaching</em> ; le résumé '
          'reformule <em>warmer water</em> en <em>rising sea temperatures</em> '
          'et laisse le mot du trou tel quel. <em>Coral whitening</em> est la '
          'bonne idée avec d’autres mots, <em>bleached</em> la mauvaise forme, '
          'et <em>known as bleaching</em> fait trois mots.',
    r6why='<em>Limestone aquifer</em>, tel qu’imprimé. <em>Underground '
          'reservoir</em> est une reformulation ; <em>limestone aquifers</em> '
          'est la mauvaise forme ; <em>a limestone aquifer</em> répète l’article '
          'que le résumé a déjà et atteint trois mots.',
    r7why='<em>Visiting engineer</em>, deux mots, exactement comme dans le '
          'texte. Le pluriel ne va pas après <em>a</em> ; <em>travelling '
          'technician</em>, ce sont vos propres mots ; la version avec '
          'l’article double le <em>a</em> et dépasse la limite.',
    r8why='Un mot : <em>olives</em>, comme dans le texte. <em>Olive</em> est la '
          'mauvaise forme, <em>olive groves</em> n’est pas dans le texte, et '
          '<em>planted olives</em> fait deux mots sous ONE WORD ONLY.',
    r9why='Un possessif, <em>the keeper&rsquo;s</em>, demande un nom. Des '
          'quatre mots du texte, seul <em>entries</em> en est un, et '
          '<em>became</em> le confirme : une chose qui est devenue plus '
          'courte.',
    r10why='Sujet, trou, complément : le trou est le verbe, et le résumé est au '
           'passé parce que le texte l’est. <em>Reinforced</em>. Le nom et la '
           'forme en -ing ne forment pas de phrase, et <em>reinforces</em> ne '
           's’accorde pas avec <em>engineers</em>.',
    r11why='<em>Was not ______ until</em> demande un participe passé : le '
           'passif. <em>Correctly identified</em> est ce que le texte imprime, '
           'et la phrase tient. Prédisez cette forme et trois options tombent '
           'avant même de regarder.',
    r12why='<em>Took</em> appelle une durée : un nombre et un nom au '
           'pluriel. <em>Eleven years</em>, tel qu’imprimé. Le singulier ne '
           's’accorde pas, l’ordinal est un autre mot, et <em>an</em> ne '
           'peut pas précéder un pluriel.',

    sortEyebrow='Activité 4 · Ce que fait le correcteur',
    sortTitle='Classez les six réponses',
    sortHint='Faites glisser chacune dans une colonne &mdash; ou cliquez sur '
             'un élément, puis sur la colonne voulue.',
    sortBin1='Rapporte des points',
    sortBin2='Ne rapporte rien',
    sort1='Deux mots recopiés exactement du texte',
    sort2='Un nombre écrit en chiffres',
    sort3='Un mot avec trait d’union sous une limite d’un mot',
    sort4='Trois mots quand la limite est de deux',
    sort5='La bonne idée avec vos propres mots',
    sort6='Le mot du texte avec une faute d’orthographe',
    sortWhy='Tout ce qui <strong>rapporte</strong>, c’est le texte, dans la '
            'limite, orthographié comme imprimé &mdash; un nombre compte '
            'pour un élément, un mot à trait d’union pour un mot. L’autre '
            'colonne réunit trois façons d’avoir compris le texte sans rien '
            'marquer : un mot de trop, une idée juste formulée autrement, un '
            'mot recopié avec une lettre fausse. Le correcteur ne lit pas le '
            'sens. Il compare votre réponse au corrigé.',

    actTitle='Créez vous-même les trous',
    actUse='Utilisez-en au moins trois :',
    actSpeakBrief='À deux, chacun avec un court article. Écrivez un résumé à '
                  'trois trous du vôtre &mdash; quatre phrases, une limite de '
                  'mots au-dessus &mdash; et échangez. Votre partenaire remplit '
                  'les trous uniquement à partir de l’article ; vous corrigez '
                  'comme l’examinateur : mot du texte, dans la limite, '
                  'orthographié comme imprimé, ou rien.',
    actSpeak1='Avant de remplir un trou, dites à voix haute de quelle nature de '
              'mot il a besoin et quels mots de la phrase vous l’indiquent.',
    actSpeak2='Pour chaque réponse, montrez les mots dans l’article. Une réponse '
              'que vous ne pouvez pas montrer n’est pas acceptée.',
    actSpeak3='Trouvez dans le résumé de votre partenaire un trou que deux mots '
              'du texte pourraient remplir, et réécrivez la phrase pour qu’un '
              'seul le puisse.',
    actWriteKind='Écriture · 150–200 mots',
    actWriteBrief='Prenez un texte lu cette semaine et écrivez-en un résumé de '
                  'quatre phrases avec trois trous, la limite de mots indiquée '
                  'au-dessus. Puis écrivez le corrigé : les mots exacts du texte '
                  'pour chaque trou, et une mauvaise réponse tentante, avec la '
                  'raison pour laquelle elle ne rapporte rien.',
    actPlaceholder='NO MORE THAN TWO WORDS. Summary: … Gap 1: … Tempting wrong '
                   'answer: …',
)


# ── Italian ────────────────────────────────────────────────────────────
T['it'] = dict(
    coverTitle='Summary and <em>Sentence Completion</em>',
    coverSub='Dove il limite di parole fa danni &mdash; le risposte vengono '
             'dritte dal testo, l’ortografia conta, e una parola di troppo vale '
             'zero',
    chipLevel='C1 · Avanzato', chipFocus='Reading · entrambi i moduli',
    chipCount='18 punti',

    t1Eyebrow='Prima di cominciare',
    t1Title='Tre spazi, una riga di istruzioni, e la riga viene prima',
    t1ah='Che cosa ti danno',
    t1ab='Un riassunto di una parte del testo, o una serie di frasi '
         'separate, con degli spazi vuoti. Le parole che li riempiono sono '
         'nel testo. Il riassunto di solito segue l’ordine del testo e di '
         'solito copre una sezione &mdash; trova dove comincia quella '
         'sezione e restaci dentro.',
    t1an='Academic e General Training lo propongono allo stesso modo. Tutto '
         'quello che trovi qui vale per entrambi.',
    t1bh='Leggi prima l’istruzione',
    t1bb='<strong>NO MORE THAN TWO WORDS AND/OR A NUMBER. ONE WORD '
         'ONLY.</strong> Il limite è stampato sopra gli spazi ed è la prima '
         'cosa da leggere &mdash; prima del riassunto, prima del testo. Decide '
         'com’è fatta una risposta giusta prima ancora che tu ne abbia trovata '
         'una.',
    t1bn='Una parola con il trattino conta come una parola, e <em>the</em> è '
         'una parola che conta. Con AND/OR A NUMBER, un numero è ammesso in '
         'più rispetto alle parole; con un semplice limite di parole, '
         'contalo come una parola.',
    t1ch='A volte c’è un riquadro',
    t1cb='Quando il compito ti dà un elenco di parole, A&ndash;H, scegli '
         'dall’elenco, non dal testo, e scrivi la lettera. Le parole possono '
         'anche non comparire nel testo, e l’elenco ha più opzioni che spazi.',
    t1cn='Sotto c’è la stessa abilità: trovare il punto nel testo, poi '
         'controllare la grammatica dello spazio.',

    t2Eyebrow='Prima di cominciare',
    t2Title='La parola è nel testo. Prendila.',
    t2ah='Trova il punto dal significato',
    t2ab='Il riassunto raramente ripete il testo parola per parola; '
         'parafrasa quasi tutto ciò che sta <strong>intorno</strong> allo '
         'spazio. Segui il senso della frase per trovare le righe giuste, '
         'poi cerca in quelle righe la parola che il riassunto ha lasciato '
         'fuori.',
    t2an='Una parola in comune ti dice dove guardare. La parola dello spazio di '
         'solito è l’unica che non è stata riformulata.',
    t2bh='Poi copiala, esattamente',
    t2bb='Stessa ortografia, stessa forma del testo. Non metterla al plurale, '
         'non cambiarne il tempo, non aggiungere un articolo che il riassunto ha '
         'già. Un’idea giusta con parole tue vale zero, perché il correttore '
         'confronta la tua risposta con la chiave, non con il testo.',
    t2bn='Se la tua parola non è nel testo, non è la risposta.',
    t2ch='Il limite è un muro',
    t2cb='Con NO MORE THAN TWO WORDS, una risposta di tre parole non vale '
         'nulla, per quanto giusta. Nemmeno mezzo punto: niente. Quando una '
         'risposta sfora, la parola in più è spesso un articolo, un '
         'aggettivo o una preposizione che non ti serviva.',
    t2cn='Scrivi la risposta, conta le parole, poi rileggi la riga '
         'dell’istruzione.',

    t3Eyebrow='Prima di cominciare',
    t3Title='Prevedi la parola prima di cercarla',
    t3ah='Prima stabilisci la categoria',
    t3ab='Leggi la frase del riassunto con lo spazio e decidi che cosa le '
         'serve: un nome, un verbo, un aggettivo, un numero. Uno spazio dopo '
         '<em>the</em> o <em>a</em> vuole un nome, o un aggettivo se dopo lo '
         'spazio viene un nome; uno spazio dopo il soggetto vuole un verbo; '
         'uno spazio dopo <em>lasted</em> o <em>cost</em> vuole una quantità.',
    t3an='Decidilo prima di aprire il testo. Così cerchi un solo tipo di '
         'parola, non una parola qualsiasi.',
    t3bh='La risposta deve essere inglese corretto',
    t3bb='Metti la tua parola nello spazio e leggi tutta la frase. Singolare o '
         'plurale, passato o presente: decide la frase del riassunto, e la '
         'parola del testo di solito ci sta già, perché il riassunto è stato '
         'scritto a partire da essa.',
    t3bn='Se la frase non regge, hai la forma sbagliata o il punto sbagliato.',
    t3ch='L’ortografia conta',
    t3cb='Anche in una parola copiata. Trascrivila lettera per lettera e '
         'confrontala con il testo. Una parola che conoscevi, copiata male, vale '
         'esattamente quanto una parola che non conoscevi.',
    t3cn='Il Reading non ha tempo per ricopiare. Scrivi sul foglio delle '
         'risposte man mano.',

    mcaEyebrow='Attività 1 · Leggi l’istruzione',
    mcaTitle='Che cosa consente il limite?',
    mcbEyebrow='Attività 2 · Copia, non riformulare',
    mcbTitle='Quale risposta prende punti?',
    mccEyebrow='Attività 3 · Lo spazio ha una forma',
    mccTitle='Quale forma va bene nella frase?',

    r1why='Due parole e un numero. <em>The</em> è una parola, quindi <em>the '
          '1997 survey results</em> sono tre; <em>results of the survey</em> '
          'sono quattro; <em>survey results from 1997</em> sono tre parole e un '
          'numero. Solo <em>1997 survey results</em> rientra nel limite.',
    r2why='Il trattino unisce: <em>well-known</em> è una parola sola. Le altre '
          'tre sono due parole ciascuna, e con ONE WORD ONLY valgono zero.',
    r3why='<em>A fall of 200 tonnes</em> sono quattro parole e un numero, una '
          'di troppo. <em>In 1846</em> è una parola e un numero, <em>nearly 200 '
          'tonnes</em> due parole e un numero, e <em>some 200 tonnes each</em> '
          'tre parole e un numero: tutte ammesse.',
    r4why='Con una lista scrivi una lettera, e le parole della lista possono '
          'non essere affatto nel testo. La lista ha più opzioni che spazi, '
          'il riassunto di solito copre comunque una sezione, e non c’è '
          'limite di parole: la risposta è una lettera.',
    r5why='Il testo dice <em>a process known as bleaching</em>; il riassunto '
          'riformula <em>warmer water</em> come <em>rising sea '
          'temperatures</em> e lascia com’è la parola dello spazio. <em>Coral '
          'whitening</em> è l’idea giusta con altre parole, <em>bleached</em> è '
          'la forma sbagliata, <em>known as bleaching</em> sono tre parole.',
    r6why='<em>Limestone aquifer</em>, così come è stampato. <em>Underground '
          'reservoir</em> è una riformulazione; <em>limestone aquifers</em> è '
          'la forma sbagliata; <em>a limestone aquifer</em> ripete l’articolo '
          'che il riassunto ha già e arriva a tre parole.',
    r7why='<em>Visiting engineer</em>, due parole, esattamente come nel testo. '
          'Il plurale non va dopo <em>a</em>; <em>travelling technician</em> '
          'sono parole tue; la versione con l’articolo raddoppia la <em>a</em> '
          'e sfora il limite.',
    r8why='Una parola: <em>olives</em>, come nel testo. <em>Olive</em> è la '
          'forma sbagliata, <em>olive groves</em> non è nel testo, e '
          '<em>planted olives</em> sono due parole con ONE WORD ONLY.',
    r9why='Un possessivo, <em>the keeper&rsquo;s</em>, vuole un nome. Delle '
          'quattro parole del testo solo <em>entries</em> lo è, e '
          '<em>became</em> lo conferma: una cosa che è diventata più corta.',
    r10why='Soggetto, spazio, complemento: lo spazio è il verbo, e il riassunto '
           'è al passato perché lo è il testo. <em>Reinforced</em>. Il nome e la '
           'forma in -ing non fanno una frase, e <em>reinforces</em> non '
           'concorda con <em>engineers</em>.',
    r11why='<em>Was not ______ until</em> vuole un participio passato: il '
           'passivo. <em>Correctly identified</em> è ciò che il testo stampa, e '
           'la frase regge. Prevedi questa forma e tre opzioni cadono prima '
           'ancora di guardare.',
    r12why='<em>Took</em> vuole una durata: un numero e un nome al plurale. '
           '<em>Eleven years</em>, come è stampato. Il singolare non '
           'concorda, l’ordinale è un’altra parola, e <em>an</em> non può '
           'stare davanti a un plurale.',

    sortEyebrow='Attività 4 · Che cosa fa il correttore',
    sortTitle='Classifica le sei risposte',
    sortHint='Trascina ciascuna in una colonna &mdash; oppure clicca su un '
             'elemento e poi sulla colonna che vuoi.',
    sortBin1='Prende punti',
    sortBin2='Vale zero',
    sort1='Due parole copiate esattamente dal testo',
    sort2='Un numero scritto in cifre',
    sort3='Una parola con il trattino e il limite di una parola',
    sort4='Tre parole quando il limite è due',
    sort5='L’idea giusta con parole tue',
    sort6='La parola del testo con un errore di ortografia',
    sortWhy='Tutto ciò che <strong>vale</strong> è il testo, entro il '
            'limite, scritto come è stampato &mdash; un numero è un '
            'elemento, una parola con il trattino è una parola. L’altra '
            'colonna raccoglie tre modi di aver capito il testo senza '
            'prendere nulla: una parola oltre il limite, un’idea giusta con '
            'altre parole, una parola copiata con una lettera sbagliata. Il '
            'correttore non legge il senso: confronta la tua risposta con la '
            'chiave.',

    actTitle='Prepara tu gli spazi',
    actUse='Usane almeno tre:',
    actSpeakBrief='In coppia, ciascuno con un breve articolo. Scrivi un riassunto '
                  'del tuo con tre spazi &mdash; quattro frasi, un limite di '
                  'parole sopra &mdash; e scambiatevelo. Il tuo compagno '
                  'riempie gli spazi solo dall’articolo; tu correggi come '
                  'farebbe l’esaminatore: parola del testo, entro il limite, '
                  'scritta come è stampata, oppure zero.',
    actSpeak1='Prima di riempire uno spazio, di’ ad alta voce di che tipo di '
              'parola ha bisogno e quali parole della frase te lo dicono.',
    actSpeak2='Per ogni risposta, indica le parole nell’articolo. Una risposta '
              'che non riesci a indicare non viene accettata.',
    actSpeak3='Trova nel riassunto del tuo compagno uno spazio che due parole '
              'del testo potrebbero riempire, e riscrivi la frase perché ne '
              'vada bene una sola.',
    actWriteKind='Scrittura · 150–200 parole',
    actWriteBrief='Prendi un testo che hai letto questa settimana e scrivine un '
                  'riassunto di quattro frasi con tre spazi, con il limite di '
                  'parole indicato sopra. Poi scrivi la chiave: le parole '
                  'esatte del testo per ogni spazio, e una risposta sbagliata '
                  'allettante, spiegando perché vale zero.',
    actPlaceholder='NO MORE THAN TWO WORDS. Summary: … Gap 1: … Tempting wrong '
                   'answer: …',
)


# ── Portuguese ─────────────────────────────────────────────────────────
T['pt'] = dict(
    coverTitle='Summary and <em>Sentence Completion</em>',
    coverSub='Onde o limite de palavras faz estragos &mdash; as respostas vêm '
             'diretamente do texto, a ortografia conta, e uma palavra a mais '
             'vale zero',
    chipLevel='C1 · Avançado', chipFocus='Reading · os dois módulos',
    chipCount='18 pontos',

    t1Eyebrow='Antes de começar',
    t1Title='Três espaços, uma linha de instruções, e a linha vem primeiro',
    t1ah='O que te dão',
    t1ab='Um resumo de uma parte do texto, ou uma série de frases soltas, '
         'com espaços. As palavras que preenchem os espaços estão no texto. '
         'O resumo costuma seguir a ordem do texto e costuma cobrir uma '
         'secção &mdash; encontra onde começa essa secção e não saias dela.',
    t1an='O Academic e o General Training apresentam-no da mesma forma. Tudo o '
         'que está aqui vale para os dois.',
    t1bh='Lê primeiro a instrução',
    t1bb='<strong>NO MORE THAN TWO WORDS AND/OR A NUMBER. ONE WORD '
         'ONLY.</strong> O limite está impresso por cima dos espaços e é a '
         'primeira coisa a ler &mdash; antes do resumo, antes do texto. Decide '
         'como é uma resposta certa antes mesmo de encontrares uma.',
    t1bn='Uma palavra com hífen conta como uma palavra, e <em>the</em> é uma '
         'palavra que conta. Com AND/OR A NUMBER, um número é permitido além '
         'das palavras; com um limite só de palavras, conta-o como uma '
         'palavra.',
    t1ch='Às vezes há uma caixa',
    t1cb='Quando a tarefa te dá uma lista de palavras, A&ndash;H, escolhes da '
         'lista, não do texto, e escreves a letra. As palavras podem nem estar '
         'no texto, e a lista tem mais opções do que espaços.',
    t1cn='Por baixo, a mesma competência: encontrar o sítio no texto e depois '
         'verificar a gramática do espaço.',

    t2Eyebrow='Antes de começar',
    t2Title='A palavra está no texto. Tira-a de lá.',
    t2ah='Encontra o sítio pelo sentido',
    t2ab='O resumo raramente repete o texto palavra por palavra; parafraseia '
         'quase tudo o que está <strong>à volta</strong> do espaço. Segue o '
         'sentido da frase para encontrar as linhas certas e depois procura '
         'nessas linhas a palavra que o resumo deixou de fora.',
    t2an='Uma palavra em comum diz-te onde procurar. A palavra do espaço é '
         'normalmente a única que não foi parafraseada.',
    t2bh='Depois copia-a, tal e qual',
    t2bb='A mesma ortografia, a mesma forma do texto. Não a ponhas no plural, '
         'não mudes o tempo verbal, não acrescentes um artigo que o resumo já '
         'tem. Uma ideia certa por palavras tuas vale zero, porque o corretor '
         'compara a tua resposta com a chave, não com o texto.',
    t2bn='Se a tua palavra não está no texto, não é a resposta.',
    t2ch='O limite é uma parede',
    t2cb='Com NO MORE THAN TWO WORDS, uma resposta de três palavras não vale '
         'nada, por muito certa que seja. Nem meio ponto: nada. Quando uma '
         'resposta passa do limite, a palavra a mais é muitas vezes um '
         'artigo, um adjetivo ou uma preposição de que não precisavas.',
    t2cn='Escreve a resposta, conta as palavras e volta a ler a instrução.',

    t3Eyebrow='Antes de começar',
    t3Title='Prevê a palavra antes de a procurar',
    t3ah='Primeiro, a classe da palavra',
    t3ab='Lê a frase do resumo que tem o espaço e decide do que precisa: um '
         'nome, um verbo, um adjetivo, um número. Um espaço depois de '
         '<em>the</em> ou <em>a</em> pede um nome, ou um adjetivo se a '
         'seguir ao espaço vier um nome; um espaço depois do sujeito pede um '
         'verbo; um espaço depois de <em>lasted</em> ou <em>cost</em> pede '
         'uma quantidade.',
    t3an='Decide isto antes de abrires o texto. Assim procuras um só tipo de '
         'palavra, e não uma palavra qualquer.',
    t3bh='A resposta tem de ser inglês correto',
    t3bb='Põe a tua palavra no espaço e lê a frase inteira. Singular ou plural, '
         'passado ou presente: quem decide é a frase do resumo, e a palavra do '
         'texto normalmente já encaixa, porque o resumo foi escrito a partir '
         'dela.',
    t3bn='Se a frase não funciona, tens a forma errada ou o sítio errado.',
    t3ch='A ortografia conta',
    t3cb='Mesmo numa palavra copiada. Passa-a letra a letra e confirma-a no '
         'texto. Uma palavra que conhecias, mal copiada, vale exatamente o mesmo '
         'que uma palavra que não conhecias.',
    t3cn='O Reading não tem tempo para passar as respostas. Escreve na folha de '
         'respostas à medida que avanças.',

    mcaEyebrow='Atividade 1 · Lê a instrução',
    mcaTitle='O que é que o limite permite?',
    mcbEyebrow='Atividade 2 · Copia, não parafraseies',
    mcbTitle='Que resposta conta?',
    mccEyebrow='Atividade 3 · O espaço tem uma forma',
    mccTitle='Que forma encaixa na frase?',

    r1why='Duas palavras e um número. <em>The</em> é uma palavra, por isso '
          '<em>the 1997 survey results</em> são três; <em>results of the '
          'survey</em> são quatro; <em>survey results from 1997</em> são três '
          'palavras e um número. Só <em>1997 survey results</em> cabe no '
          'limite.',
    r2why='O hífen une: <em>well-known</em> é uma palavra. As outras três são '
          'duas palavras cada, e com ONE WORD ONLY valem zero.',
    r3why='<em>A fall of 200 tonnes</em> são quatro palavras e um número, uma a '
          'mais. <em>In 1846</em> é uma palavra e um número, <em>nearly 200 '
          'tonnes</em> duas palavras e um número, e <em>some 200 tonnes '
          'each</em> três palavras e um número: todas permitidas.',
    r4why='Com uma lista escreves uma letra, e as palavras da lista nem '
          'precisam de estar no texto. A lista tem mais opções do que '
          'espaços, o resumo costuma cobrir na mesma uma secção, e não há '
          'limite de palavras: a resposta é uma letra.',
    r5why='O texto diz <em>a process known as bleaching</em>; o resumo '
          'parafraseia <em>warmer water</em> como <em>rising sea '
          'temperatures</em> e deixa a palavra do espaço intacta. <em>Coral '
          'whitening</em> é a ideia certa por outras palavras, <em>bleached</em> '
          'é a forma errada, <em>known as bleaching</em> são três palavras.',
    r6why='<em>Limestone aquifer</em>, tal como está impresso. <em>Underground '
          'reservoir</em> é uma paráfrase; <em>limestone aquifers</em> é a '
          'forma errada; <em>a limestone aquifer</em> repete o artigo que o '
          'resumo já tem e chega a três palavras.',
    r7why='<em>Visiting engineer</em>, duas palavras, tal como no texto. O '
          'plural não encaixa depois de <em>a</em>; <em>travelling '
          'technician</em> são palavras tuas; a versão com o artigo duplica o '
          '<em>a</em> e ultrapassa o limite.',
    r8why='Uma palavra: <em>olives</em>, como o texto a tem. <em>Olive</em> é a '
          'forma errada, <em>olive groves</em> não está no texto, e <em>planted '
          'olives</em> são duas palavras com ONE WORD ONLY.',
    r9why='Um possessivo, <em>the keeper&rsquo;s</em>, pede um nome. Das quatro '
          'palavras do texto, só <em>entries</em> o é, e <em>became</em> '
          'confirma-o: uma coisa que ficou mais curta.',
    r10why='Sujeito, espaço, complemento: o espaço é o verbo, e o resumo está no '
           'passado porque o texto está. <em>Reinforced</em>. O nome e a forma '
           'em -ing não formam uma frase, e <em>reinforces</em> não concorda com '
           '<em>engineers</em>.',
    r11why='<em>Was not ______ until</em> pede um particípio passado: a passiva. '
           '<em>Correctly identified</em> é o que o texto imprime, e a frase '
           'funciona. Prevê esta forma e três opções caem antes de olhares.',
    r12why='<em>Took</em> pede uma duração: um número e um nome no plural. '
           '<em>Eleven years</em>, tal como está impresso. O singular não '
           'concorda, o ordinal é outra palavra, e <em>an</em> não pode vir '
           'antes de um plural.',

    sortEyebrow='Atividade 4 · O que faz o corretor',
    sortTitle='Classifica as seis respostas',
    sortHint='Arrasta cada uma para uma coluna &mdash; ou clica num elemento e '
             'depois na coluna que quiseres.',
    sortBin1='Conta',
    sortBin2='Vale zero',
    sort1='Duas palavras copiadas tal e qual do texto',
    sort2='Um número escrito em algarismos',
    sort3='Uma palavra com hífen com o limite de uma palavra',
    sort4='Três palavras quando o limite é duas',
    sort5='A ideia certa por palavras tuas',
    sort6='A palavra do texto com um erro ortográfico',
    sortWhy='Tudo o que <strong>vale</strong> é o texto, dentro do limite, '
            'escrito como está impresso &mdash; um número é um elemento, uma '
            'palavra com hífen é uma palavra. A outra coluna reúne três '
            'maneiras de perceber o texto e não ganhar nada com isso: uma '
            'palavra a mais, uma ideia certa por outras palavras, uma '
            'palavra copiada com uma letra errada. O corretor não lê o '
            'sentido: compara a tua resposta com a chave.',

    actTitle='Cria tu os espaços',
    actUse='Usa pelo menos três:',
    actSpeakBrief='Em pares, cada um com um artigo curto. Escreve um resumo do '
                  'teu com três espaços &mdash; quatro frases, com um limite de '
                  'palavras por cima &mdash; e troquem. O teu colega preenche os '
                  'espaços só a partir do artigo; tu corriges como o '
                  'examinador: palavra do texto, dentro do limite, escrita como '
                  'está impressa, ou zero.',
    actSpeak1='Antes de preencheres um espaço, diz em voz alta de que classe de '
              'palavra precisa e que palavras da frase to indicam.',
    actSpeak2='Para cada resposta, aponta as palavras no artigo. Uma resposta '
              'para a qual não consegues apontar não é aceite.',
    actSpeak3='Encontra no resumo do teu colega um espaço que duas palavras do '
              'texto possam preencher, e reescreve a frase para que só uma '
              'possa.',
    actWriteKind='Escrita · 150–200 palavras',
    actWriteBrief='Pega num texto que leste esta semana e escreve um resumo de '
                  'quatro frases com três espaços, com o limite de palavras '
                  'indicado por cima. Depois escreve a chave: as palavras exatas '
                  'do texto para cada espaço, e uma resposta errada tentadora, '
                  'explicando porque vale zero.',
    actPlaceholder='NO MORE THAN TWO WORDS. Summary: … Gap 1: … Tempting wrong '
                   'answer: …',
)


# ── Russian ────────────────────────────────────────────────────────────
T['ru'] = dict(
    coverTitle='Summary and <em>Sentence Completion</em>',
    coverSub='Здесь больше всего вредит лимит слов: ответы берутся прямо из '
             'текста, орфография считается, а одно лишнее слово &mdash; это '
             'ноль',
    chipLevel='C1 · Продвинутый', chipFocus='Reading · оба модуля',
    chipCount='18 баллов',

    t1Eyebrow='Прежде чем начать',
    t1Title='Три пропуска, одна строка с инструкцией, и строка &mdash; первой',
    t1ah='Что вам дают',
    t1ab='Изложение части текста или ряд отдельных предложений с пропусками. '
         'Слова для пропусков есть в тексте. Изложение обычно идёт по '
         'порядку текста и обычно охватывает один его раздел &mdash; '
         'найдите, где этот раздел начинается, и не выходите за его пределы.',
    t1an='В Academic и General Training это задание устроено одинаково. Всё '
         'здесь подходит для обоих модулей.',
    t1bh='Сначала прочитайте инструкцию',
    t1bb='<strong>NO MORE THAN TWO WORDS AND/OR A NUMBER. ONE WORD '
         'ONLY.</strong> Лимит напечатан над пропусками, и читать его нужно '
         'первым &mdash; раньше изложения, раньше текста. Он определяет, как '
         'выглядит правильный ответ, ещё до того, как вы его нашли.',
    t1bn='Слово через дефис &mdash; одно слово, а <em>the</em> &mdash; '
         'слово, которое считается. При AND/OR A NUMBER число допускается '
         'сверх слов; при простом лимите слов считайте его словом.',
    t1ch='Иногда есть рамка со словами',
    t1cb='Когда задание даёт список слов A&ndash;H, вы выбираете из списка, а '
         'не из текста, и пишете букву. Этих слов может вообще не быть в '
         'тексте, а вариантов в списке больше, чем пропусков.',
    t1cn='Навык тот же: найти место в тексте, затем проверить грамматику '
         'пропуска.',

    t2Eyebrow='Прежде чем начать',
    t2Title='Слово есть в тексте. Возьмите его.',
    t2ah='Находите место по смыслу',
    t2ab='Изложение редко повторяет текст слово в слово; оно перефразирует '
         'почти всё <strong>вокруг</strong> пропуска. Ищите по смыслу '
         'предложения нужные строки, а потом ищите в них слово, которое '
         'изложение пропустило.',
    t2an='Общее слово подсказывает, где искать. Слово для пропуска &mdash; '
         'обычно единственное, которое не перефразировали.',
    t2bh='Потом перепишите его точно',
    t2bb='То же написание, та же форма, что в тексте. Не ставьте во '
         'множественное число, не меняйте время, не добавляйте артикль, который '
         'в изложении уже есть. Верная мысль своими словами &mdash; это ноль: '
         'проверяющий сравнивает ваш ответ с ключом, а не с текстом.',
    t2bn='Если вашего слова нет в тексте, это не ответ.',
    t2ch='Лимит &mdash; это стена',
    t2cb='При NO MORE THAN TWO WORDS ответ из трёх слов не приносит ничего, '
         'каким бы верным он ни был. Не половина балла: ноль. Когда ответ '
         'выходит за лимит, лишнее слово часто оказывается артиклем, '
         'прилагательным или предлогом, который был не нужен.',
    t2cn='Напишите ответ, посчитайте слова и снова прочитайте инструкцию.',

    t3Eyebrow='Прежде чем начать',
    t3Title='Предскажите слово, прежде чем искать его',
    t3ah='Сначала часть речи',
    t3ab='Прочитайте предложение изложения с пропуском и решите, что ему '
         'нужно: существительное, глагол, прилагательное, число. После '
         '<em>the</em> или <em>a</em> пропуск требует существительного, а '
         'если после пропуска идёт существительное &mdash; прилагательного; '
         'после подлежащего &mdash; глагола; после <em>lasted</em> или '
         '<em>cost</em> &mdash; количества.',
    t3an='Решите это до того, как откроете текст. Тогда вы ищете слово одного '
         'вида, а не любое слово.',
    t3bh='Ответ должен звучать по-английски',
    t3bb='Вставьте слово в пропуск и прочитайте всё предложение. Единственное '
         'или множественное число, прошедшее или настоящее время &mdash; решает '
         'предложение изложения, а слово из текста обычно уже подходит, ведь '
         'изложение писали по нему.',
    t3bn='Если предложение не складывается, у вас не та форма или не то место.',
    t3ch='Орфография считается',
    t3cb='Даже в переписанном слове. Переносите его буква за буквой и сверяйте '
         'с текстом. Знакомое слово, переписанное с ошибкой, стоит ровно '
         'столько же, сколько слово, которого вы не знали.',
    t3cn='В Reading нет времени на перенос. Пишите сразу в бланк ответов.',

    mcaEyebrow='Задание 1 · Прочитайте инструкцию',
    mcaTitle='Что позволяет лимит?',
    mcbEyebrow='Задание 2 · Переписывайте, а не перефразируйте',
    mcbTitle='Какой ответ засчитают?',
    mccEyebrow='Задание 3 · У пропуска есть форма',
    mccTitle='Какая форма подходит к предложению?',

    r1why='Два слова и число. <em>The</em> &mdash; слово, поэтому <em>the 1997 '
          'survey results</em> &mdash; это три слова; <em>results of the '
          'survey</em> &mdash; четыре; <em>survey results from 1997</em> '
          '&mdash; три слова и число. В лимит укладывается только <em>1997 '
          'survey results</em>.',
    r2why='Дефис соединяет: <em>well-known</em> &mdash; одно слово. Остальные '
          'три &mdash; по два слова, и при ONE WORD ONLY это ноль.',
    r3why='<em>A fall of 200 tonnes</em> &mdash; четыре слова и число, на одно '
          'больше лимита. <em>In 1846</em> &mdash; одно слово и число, '
          '<em>nearly 200 tonnes</em> &mdash; два слова и число, а <em>some 200 '
          'tonnes each</em> &mdash; три слова и число: всё допустимо.',
    r4why='Со списком вы пишете букву, и слов из списка может вообще не быть '
          'в тексте. В списке больше вариантов, чем пропусков, изложение '
          'обычно всё равно охватывает один раздел, а лимита слов нет: ответ '
          '&mdash; буква.',
    r5why='В тексте &mdash; <em>a process known as bleaching</em>; изложение '
          'перефразирует <em>warmer water</em> как <em>rising sea '
          'temperatures</em>, а слово для пропуска не трогает. <em>Coral '
          'whitening</em> &mdash; верная мысль другими словами, '
          '<em>bleached</em> &mdash; не та форма, <em>known as bleaching</em> '
          '&mdash; три слова.',
    r6why='<em>Limestone aquifer</em>, как напечатано. <em>Underground '
          'reservoir</em> &mdash; перефразирование; <em>limestone aquifers</em> '
          '&mdash; не та форма; <em>a limestone aquifer</em> повторяет артикль, '
          'который уже есть в изложении, и даёт три слова.',
    r7why='<em>Visiting engineer</em>, два слова, в точности как в тексте. '
          'Множественное число не подходит после <em>a</em>; <em>travelling '
          'technician</em> &mdash; ваши собственные слова; вариант с артиклем '
          'удваивает <em>a</em> и нарушает лимит.',
    r8why='Одно слово: <em>olives</em>, как в тексте. <em>Olive</em> &mdash; не '
          'та форма, <em>olive groves</em> в тексте нет, а <em>planted '
          'olives</em> &mdash; два слова при ONE WORD ONLY.',
    r9why='Притяжательный падеж, <em>the keeper&rsquo;s</em>, требует '
          'существительного. Из четырёх слов текста существительное только '
          '<em>entries</em>, и <em>became</em> это подтверждает: нечто стало '
          'короче.',
    r10why='Подлежащее, пропуск, дополнение: пропуск &mdash; это глагол, и '
           'изложение в прошедшем времени, потому что в нём текст. '
           '<em>Reinforced</em>. Существительное и форма на -ing не дают '
           'предложения, а <em>reinforces</em> не согласуется с '
           '<em>engineers</em>.',
    r11why='<em>Was not ______ until</em> требует причастия прошедшего времени: '
           'это пассив. <em>Correctly identified</em> &mdash; то, что напечатано '
           'в тексте, и предложение складывается. Предскажите эту форму, и три '
           'варианта отпадут ещё до того, как вы посмотрите.',
    r12why='<em>Took</em> требует продолжительности: числа и '
           'существительного во множественном числе. <em>Eleven years</em>, '
           'как напечатано. Единственное число не согласуется, порядковое '
           'числительное &mdash; другое слово, а <em>an</em> не ставится '
           'перед множественным числом.',

    sortEyebrow='Задание 4 · Что делает проверяющий',
    sortTitle='Распределите шесть ответов',
    sortHint='Перетащите каждый в столбец &mdash; или нажмите на него, а затем '
             'на нужный столбец.',
    sortBin1='Засчитывается',
    sortBin2='Ноль баллов',
    sort1='Два слова, переписанные из текста точно',
    sort2='Число, записанное цифрами',
    sort3='Слово через дефис при лимите в одно слово',
    sort4='Три слова при лимите в два',
    sort5='Верная мысль своими словами',
    sort6='Слово из текста с орфографической ошибкой',
    sortWhy='Всё, что <strong>засчитывается</strong>, &mdash; это текст, в '
            'пределах лимита, написанный как напечатано: число считается '
            'одним элементом, слово через дефис &mdash; одним словом. В '
            'другом столбце &mdash; три способа понять текст и ничего за это '
            'не получить: слово сверх лимита, верная мысль другими словами, '
            'переписанное слово с ошибкой в одной букве. Проверяющий не '
            'читает смысл: он сравнивает ваш ответ с ключом.',

    actTitle='Сделайте пропуски сами',
    actUse='Используйте хотя бы три:',
    actSpeakBrief='В парах, у каждого короткая статья. Напишите по своей '
                  'изложение с тремя пропусками &mdash; четыре предложения, над '
                  'ними лимит слов &mdash; и обменяйтесь. Партнёр заполняет '
                  'пропуски только по статье; вы проверяете, как экзаменатор: '
                  'слово из текста, в пределах лимита, написанное как '
                  'напечатано, &mdash; или ноль.',
    actSpeak1='Прежде чем заполнить пропуск, скажите вслух, какая часть речи '
              'нужна и какие слова предложения на это указывают.',
    actSpeak2='Для каждого ответа укажите слова в статье. Ответ, на который '
              'нельзя указать, не принимается.',
    actSpeak3='Найдите в изложении партнёра пропуск, который могут заполнить два '
              'слова из текста, и перепишите предложение так, чтобы подходило '
              'только одно.',
    actWriteKind='Письмо · 150–200 слов',
    actWriteBrief='Возьмите текст, который вы прочитали на этой неделе, и '
                  'напишите по нему изложение из четырёх предложений с тремя '
                  'пропусками, указав над ним лимит слов. Затем напишите ключ: '
                  'точные слова из текста для каждого пропуска и один '
                  'соблазнительный неверный ответ с объяснением, почему он даёт '
                  'ноль.',
    actPlaceholder='NO MORE THAN TWO WORDS. Summary: … Gap 1: … Tempting wrong '
                   'answer: …',
)


# ── Arabic ─────────────────────────────────────────────────────────────
T['ar'] = dict(
    coverTitle='Summary and <em>Sentence Completion</em>',
    coverSub='حيث يُحدث حدّ الكلمات الضرر: الإجابات تأتي من النص مباشرةً، '
             'والإملاء يُحتسب، وكلمة زائدة واحدة تعني صفرًا',
    chipLevel='C1 · متقدّم', chipFocus='Reading · الوحدتان كلتاهما',
    chipCount='18 نقطة',

    t1Eyebrow='قبل أن تبدأ',
    t1Title='ثلاث فجوات وسطر تعليمات، والسطر أولًا',
    t1ah='ما الذي يُعطى لك',
    t1ab='ملخّص لجزء من النص، أو مجموعة من الجمل المنفصلة، فيها فجوات. '
         'والكلمات التي تملأ الفجوات موجودة في النص. ويسير الملخّص عادةً '
         'بترتيب النص ويغطي عادةً قسمًا واحدًا منه &mdash; فجد أين يبدأ ذلك '
         'القسم وابقَ فيه.',
    t1an='يطرحه Academic وGeneral Training بالطريقة نفسها، فكل ما هنا يصلح '
         'للاثنين.',
    t1bh='اقرأ التعليمات أولًا',
    t1bb='<strong>NO MORE THAN TWO WORDS AND/OR A NUMBER. ONE WORD '
         'ONLY.</strong> الحدّ مطبوع فوق الفجوات، وهو أول ما يُقرأ، قبل الملخّص '
         'وقبل النص. فهو يحدّد شكل الإجابة الصحيحة قبل أن تجدها.',
    t1bn='الكلمة الموصولة بشرطة كلمة واحدة، و<em>the</em> كلمة تُحتسب. مع '
         'AND/OR A NUMBER يُسمح برقم فوق عدد الكلمات، ومع حدّ للكلمات وحدها '
         'احسبه كلمة.',
    t1ch='أحيانًا يكون هناك مربّع',
    t1cb='عندما تعطيك المهمة قائمة كلمات A&ndash;H، فأنت تختار من القائمة لا '
         'من النص، وتكتب الحرف. وقد لا تكون الكلمات في النص أصلًا، وفي القائمة '
         'خيارات أكثر من الفجوات.',
    t1cn='المهارة نفسها في العمق: جِد الموضع في النص، ثم تحقّق من قواعد الفجوة.',

    t2Eyebrow='قبل أن تبدأ',
    t2Title='الكلمة في النص. انقلها.',
    t2ah='جِد الموضع بالمعنى',
    t2ab='نادرًا ما يكرر الملخّص النص كلمةً كلمة، بل يعيد صياغة معظم ما '
         '<strong>حول</strong> الفجوة. طابق معنى الجملة لتجد السطور الصحيحة، '
         'ثم اقرأ تلك السطور بحثًا عن الكلمة التي أسقطها الملخّص.',
    t2an='الكلمة المشتركة تدلّك أين تبحث. وكلمة الفجوة هي عادةً الكلمة الوحيدة '
         'التي لم تُعَد صياغتها.',
    t2bh='ثم انسخها كما هي تمامًا',
    t2bb='الإملاء نفسه والصيغة نفسها كما في النص. لا تجمعها، ولا تغيّر زمنها، '
         'ولا تضف أداة تعريف موجودة في الملخّص أصلًا. الفكرة الصحيحة بكلماتك لا '
         'تنال شيئًا، لأن المصحّح يقارن إجابتك بمفتاح الإجابة لا بالنص.',
    t2bn='إذا لم تكن كلمتك في النص، فليست هي الإجابة.',
    t2ch='الحدّ جدار',
    t2cb='مع NO MORE THAN TWO WORDS لا تنال الإجابة المؤلفة من ثلاث كلمات '
         'شيئًا، مهما كانت صحيحة. لا نصف درجة: لا شيء. وحين تتجاوز الإجابة '
         'الحدّ، تكون الكلمة الزائدة غالبًا أداة تعريف أو صفة أو حرف جر لم '
         'تكن تحتاجه.',
    t2cn='اكتب الإجابة، وعُدّ كلماتها، ثم اقرأ سطر التعليمات من جديد.',

    t3Eyebrow='قبل أن تبدأ',
    t3Title='توقّع الكلمة قبل أن تبحث عنها',
    t3ah='حدّد نوع الكلمة أولًا',
    t3ab='اقرأ جملة الملخّص التي فيها الفجوة وقرّر ما تحتاجه: اسم، أو فعل، '
         'أو صفة، أو رقم. الفجوة بعد <em>the</em> أو <em>a</em> تريد اسمًا، '
         'أو صفة إذا جاء بعد الفجوة اسم؛ والفجوة بعد الفاعل تريد فعلًا؛ '
         'والفجوة بعد <em>lasted</em> أو <em>cost</em> تريد كمية.',
    t3an='قرّر ذلك قبل أن تفتح النص، فتبحث عن نوع واحد من الكلمات لا عن أيّ '
         'كلمة.',
    t3bh='يجب أن تكون الإجابة إنجليزية سليمة',
    t3bb='ضع كلمتك في الفجوة واقرأ الجملة كلها. المفرد أو الجمع، الماضي أو '
         'المضارع: جملة الملخّص هي التي تقرّر، وكلمة النص تناسب عادةً من '
         'البداية، لأن الملخّص كُتب انطلاقًا منها.',
    t3bn='إذا لم تستقم الجملة، فالصيغة خاطئة أو الموضع خاطئ.',
    t3ch='الإملاء يُحتسب',
    t3cb='حتى في الكلمة المنسوخة. انقلها حرفًا حرفًا وقارِنها بالنص. فالكلمة '
         'التي تعرفها إذا نُسخت خطأً تساوي تمامًا كلمة لم تكن تعرفها.',
    t3cn='لا وقت في Reading لنقل الإجابات. اكتب على ورقة الإجابة أولًا بأول.',

    mcaEyebrow='النشاط 1 · اقرأ التعليمات',
    mcaTitle='ماذا يسمح الحدّ؟',
    mcbEyebrow='النشاط 2 · انسخ ولا تُعِد الصياغة',
    mcbTitle='أيّ إجابة تُحتسب؟',
    mccEyebrow='النشاط 3 · للفجوة شكل',
    mccTitle='أيّ صيغة تناسب الجملة؟',

    r1why='كلمتان ورقم. <em>The</em> كلمة، لذا فإن <em>the 1997 survey '
          'results</em> ثلاث كلمات، و<em>results of the survey</em> أربع، '
          'و<em>survey results from 1997</em> ثلاث كلمات ورقم. وحدها <em>1997 '
          'survey results</em> تقع ضمن الحدّ.',
    r2why='الشرطة تصل: <em>well-known</em> كلمة واحدة. أما الثلاث الأخرى '
          'فكلمتان لكل منها، ومع ONE WORD ONLY لا تنال شيئًا.',
    r3why='عبارة <em>A fall of 200 tonnes</em> أربع كلمات ورقم، أي كلمة زائدة. '
          'و<em>In 1846</em> كلمة ورقم، و<em>nearly 200 tonnes</em> كلمتان ورقم، '
          'و<em>some 200 tonnes each</em> ثلاث كلمات ورقم: كلها مسموحة.',
    r4why='مع القائمة تكتب حرفًا، وقد لا تكون كلمات القائمة في النص أصلًا. '
          'في القائمة خيارات أكثر من الفجوات، ويغطي الملخّص عادةً قسمًا '
          'واحدًا مع ذلك، ولا يوجد حدّ للكلمات: الإجابة حرف.',
    r5why='يقول النص <em>a process known as bleaching</em>، والملخّص يعيد صياغة '
          '<em>warmer water</em> إلى <em>rising sea temperatures</em> ويترك '
          'كلمة الفجوة كما هي. فـ<em>coral whitening</em> هي الفكرة الصحيحة '
          'بكلمات أخرى، و<em>bleached</em> صيغة خاطئة، و<em>known as '
          'bleaching</em> ثلاث كلمات.',
    r6why='الإجابة <em>limestone aquifer</em> كما هي مطبوعة. أما '
          '<em>underground reservoir</em> فإعادة صياغة، و<em>limestone '
          'aquifers</em> صيغة خاطئة، و<em>a limestone aquifer</em> تكرّر أداة '
          'التعريف الموجودة في الملخّص وتصل إلى ثلاث كلمات.',
    r7why='الإجابة <em>visiting engineer</em>، كلمتان، كما في النص تمامًا. '
          'الجمع لا يناسب بعد <em>a</em>، و<em>travelling technician</em> '
          'كلماتك أنت، والصيغة التي فيها الأداة تكرّر <em>a</em> وتتجاوز الحدّ.',
    r8why='كلمة واحدة: <em>olives</em> كما وردت في النص. <em>Olive</em> صيغة '
          'خاطئة، و<em>olive groves</em> ليست في النص، و<em>planted olives</em> '
          'كلمتان مع ONE WORD ONLY.',
    r9why='صيغة الملكية <em>the keeper&rsquo;s</em> تحتاج إلى اسم. ومن كلمات '
          'النص الأربع وحدها <em>entries</em> اسم، و<em>became</em> تؤكّد ذلك: '
          'شيء صار أقصر.',
    r10why='فاعل ثم فجوة ثم مفعول: الفجوة هي الفعل، والملخّص بالماضي لأن النص '
           'كذلك. إذن <em>reinforced</em>. الاسم وصيغة -ing لا يكوّنان جملة، '
           'و<em>reinforces</em> لا تتّفق مع <em>engineers</em>.',
    r11why='التركيب <em>was not ______ until</em> يريد اسم مفعول، أي المبني '
           'للمجهول. و<em>correctly identified</em> هو ما يطبعه النص، والجملة '
           'تستقيم. توقّع هذا الشكل تسقط ثلاثة خيارات قبل أن تنظر.',
    r12why='الفعل <em>took</em> يريد مدة زمنية: رقمًا واسمًا جمعًا. '
           '<em>Eleven years</em> كما طُبعت. المفرد لا يتطابق، والعدد '
           'الترتيبي كلمة أخرى، و<em>an</em> لا تأتي قبل الجمع.',

    sortEyebrow='النشاط 4 · ماذا يفعل المصحّح',
    sortTitle='صنِّف الإجابات الست',
    sortHint='اسحب كل إجابة إلى عمود، أو انقر عليها ثم على العمود الذي تريده.',
    sortBin1='تُحتسب',
    sortBin2='لا تنال شيئًا',
    sort1='كلمتان منسوختان من النص تمامًا',
    sort2='رقم مكتوب بالأرقام',
    sort3='كلمة موصولة بشرطة مع حدّ كلمة واحدة',
    sort4='ثلاث كلمات والحدّ كلمتان',
    sort5='الفكرة الصحيحة بكلماتك',
    sort6='كلمة النص بخطأ إملائي',
    sortWhy='كل ما <strong>يُحتسب</strong> هو النص، ضمن الحدّ، ومكتوب كما '
            'طُبع: الرقم يُعدّ عنصرًا واحدًا، والكلمة الموصولة بشرطة كلمة '
            'واحدة. أما العمود الآخر ففيه ثلاث طرق لفهم النص دون نيل شيء: '
            'كلمة فوق الحدّ، وفكرة صحيحة بكلمات أخرى، وكلمة منقولة بحرف '
            'خاطئ. المصحّح لا يقرأ المعنى، بل يقارن إجابتك بمفتاح الإجابة.',

    actTitle='اصنع الفجوات بنفسك',
    actUse='استخدم ثلاثة منها على الأقل:',
    actSpeakBrief='اعملا في ثنائي، ومع كل منكما مقال قصير. اكتب ملخّصًا لمقالك '
                  'فيه ثلاث فجوات، أربع جمل وفوقها حدّ الكلمات، ثم تبادلا. يملأ '
                  'زميلك الفجوات من المقال وحده، وتصحّح أنت كما يصحّح الممتحن: '
                  'كلمة من النص، ضمن الحدّ، مكتوبة كما طُبعت، وإلا فصفر.',
    actSpeak1='قبل أن تملأ أيّ فجوة، قل بصوت عالٍ ما نوع الكلمة التي تحتاجها '
              'وأيّ كلمات الجملة تدلّك على ذلك.',
    actSpeak2='لكل إجابة، أشِر إلى الكلمات في المقال. الإجابة التي لا تستطيع '
              'الإشارة إليها لا تُقبل.',
    actSpeak3='جِد في ملخّص زميلك فجوة يمكن أن تملأها كلمتان من النص، وأعد '
              'كتابة الجملة بحيث لا تملؤها إلا واحدة.',
    actWriteKind='الكتابة · 150–200 كلمة',
    actWriteBrief='خذ نصًّا قرأته هذا الأسبوع واكتب عنه ملخّصًا من أربع جمل فيه '
                  'ثلاث فجوات، مع ذكر حدّ الكلمات فوقه. ثم اكتب مفتاح الإجابة: '
                  'كلمات النص الدقيقة لكل فجوة، وإجابة خاطئة مغرية مع سبب '
                  'حصولها على صفر.',
    actPlaceholder='NO MORE THAN TWO WORDS. Summary: … Gap 1: … Tempting wrong '
                   'answer: …',
)


# ── Chinese ────────────────────────────────────────────────────────────
T['zh'] = dict(
    coverTitle='Summary and <em>Sentence Completion</em>',
    coverSub='字数限制最伤人的题型——答案直接出自原文，拼写要算分，多一个词就是'
             '零分',
    chipLevel='C1 · 高级', chipFocus='Reading · 两个模块通用',
    chipCount='18 分',

    t1Eyebrow='开始之前',
    t1Title='三个空、一行说明，先读那一行',
    t1ah='题目给你什么',
    t1ab='一段对文章某部分的摘要，或几句独立的句子，里面有空格。填空的词都在原文里。摘要通常按原文顺序，而且通常只涵盖其中一部分——找到那一部分'
         '从哪里开始，就待在那里。',
    t1an='Academic 和 General Training 的出法一样。这里讲的都适用于两者。',
    t1bh='先读说明',
    t1bb='<strong>NO MORE THAN TWO WORDS AND/OR A NUMBER. ONE WORD '
         'ONLY.</strong> 字数限制印在空格上方，是第一个要读的东西——在摘要之前，'
         '在原文之前。你还没找到答案，它就已经决定了正确答案长什么样。',
    t1bn='带连字符的词算一个词，<em>the</em> 也是算数的一个词。在 AND/OR A NUMBER '
         '的要求下，数字可以另外加上；如果只有字数限制，数字要算作一个词。',
    t1ch='有时会有一个选项框',
    t1cb='如果题目给你一列词，A&ndash;H，你要从列表里选，而不是从原文里找，写'
         '的是字母。这些词可能根本不在原文里，而且选项比空格多。',
    t1cn='底层是同一个技能：先在原文里找到位置，再检查空格的语法。',

    t2Eyebrow='开始之前',
    t2Title='词就在原文里，把它拿过来。',
    t2ah='按意思找位置',
    t2ab='摘要很少逐字重复原文；空格<strong>周围</strong>的大部分内容都经过改写。按句子的意思找到对应的几行，再在这几行里找摘要'
         '漏掉的那个词。',
    t2an='共同的词告诉你去哪里找。要填的词通常就是唯一没被改写的那个。',
    t2bh='然后原样照抄',
    t2bb='拼写一样，形式也和原文一样。不要改成复数，不要改时态，不要加摘要里已'
         '经有的冠词。用自己的话写出正确意思也是零分，因为阅卷人拿你的答案和标'
         '准答案比，而不是和原文比。',
    t2bn='你的词如果不在原文里，就不是答案。',
    t2ch='字数限制是一堵墙',
    t2cb='在 NO MORE THAN TWO WORDS 的要求下，三个词的答案再对也不得分。不是半分，是零分。答案超了字数时，多出来的往往是'
         '你并不需要的冠词、形容词或介词。',
    t2cn='写下答案，数一数字数，再读一遍说明。',

    t3Eyebrow='开始之前',
    t3Title='找之前先预测是什么词',
    t3ah='先确定词性',
    t3ab='读有空格的那句摘要，判断它需要什么：名词、动词、形容词还是数字。<em>the</em> 或 <em>a</em> '
         '后面的空要名词，如果空后面跟着名词，就要形容词；主语后面的空要动词；<em>lasted</em> 或 <em>cost</em> '
         '后面的空要数量。',
    t3an='在打开原文之前就判断好。这样你找的是一类词，而不是随便哪个词。',
    t3bh='答案必须是通顺的英语',
    t3bb='把你的词放进空里，把整句读一遍。单数还是复数，过去还是现在：由摘要这'
         '句话决定，而原文的词通常本来就合适，因为摘要就是根据它写的。',
    t3bn='如果句子读不通，要么形式不对，要么位置不对。',
    t3ch='拼写要算分',
    t3cb='抄来的词也一样。一个字母一个字母地抄，再和原文核对。你认识的词抄错了，'
         '得分和你不认识的词完全一样。',
    t3cn='Reading 没有誊写时间，边做边写在答题卡上。',

    mcaEyebrow='练习 1 · 读说明',
    mcaTitle='字数限制允许什么？',
    mcbEyebrow='练习 2 · 照抄，不要改写',
    mcbTitle='哪个答案能得分？',
    mccEyebrow='练习 3 · 空格有形状',
    mccTitle='哪种形式放得进这句话？',

    r1why='两个词加一个数字。<em>The</em> 是一个词，所以 <em>the 1997 survey '
          'results</em> 是三个词；<em>results of the survey</em> 是四个；'
          '<em>survey results from 1997</em> 是三个词加一个数字。只有 <em>1997 '
          'survey results</em> 在限制之内。',
    r2why='连字符把词连在一起：<em>well-known</em> 算一个词。另外三个都是两个'
          '词，在 ONE WORD ONLY 下都是零分。',
    r3why='<em>A fall of 200 tonnes</em> 是四个词加一个数字，超了一个。<em>In '
          '1846</em> 是一个词加一个数字，<em>nearly 200 tonnes</em> 是两个词加'
          '一个数字，<em>some 200 tonnes each</em> 是三个词加一个数字：都可以。',
    r4why='有词表时你写字母，词表里的词甚至可能根本不在原文里。选项比空格多，摘要通常仍只涵盖一部分，而且没有字数限制：答案是一个字母。',
    r5why='原文说的是 <em>a process known as bleaching</em>；摘要把 <em>warmer '
          'water</em> 改写成 <em>rising sea temperatures</em>，而要填的词没有'
          '动。<em>Coral whitening</em> 意思对但换了说法，<em>bleached</em> 形式'
          '不对，<em>known as bleaching</em> 是三个词。',
    r6why='<em>Limestone aquifer</em>，照印刷原样。<em>Underground '
          'reservoir</em> 是改写；<em>limestone aquifers</em> 形式不对；<em>a '
          'limestone aquifer</em> 重复了摘要里已有的冠词，而且变成三个词。',
    r7why='<em>Visiting engineer</em>，两个词，和原文一模一样。<em>a</em> 后面'
          '不能接复数；<em>travelling technician</em> 是你自己的话；带冠词的版'
          '本把 <em>a</em> 重复了，还超了字数。',
    r8why='一个词：<em>olives</em>，和原文一样。<em>Olive</em> 形式不对，'
          '<em>olive groves</em> 不在原文里，<em>planted olives</em> 在 ONE '
          'WORD ONLY 下是两个词。',
    r9why='所有格 <em>the keeper&rsquo;s</em> 后面要名词。原文的四个词里只有 '
          '<em>entries</em> 是名词，<em>became</em> 也印证了这一点：某样东西变'
          '短了。',
    r10why='主语、空格、宾语：空格是动词，而原文是过去时，所以摘要也是。答案是 '
           '<em>reinforced</em>。名词和 -ing 形式都构不成句子，<em>reinforces</em> '
           '和 <em>engineers</em> 不一致。',
    r11why='<em>Was not ______ until</em> 要的是过去分词：被动语态。<em>Correctly '
           'identified</em> 是原文印的，句子也通。预测到这个形式，还没看选项就'
           '能排除三个。',
    r12why='<em>Took</em> 需要一段时长：一个数字加一个复数名词。<em>Eleven '
           'years</em>，按印刷原样。单数不一致，序数词是另一个词，而 <em>an</em> 不能放在复数前。',

    sortEyebrow='练习 4 · 阅卷人怎么做',
    sortTitle='给这六个答案分类',
    sortHint='把每一项拖到一栏里——或者先点一项，再点你想放进的那一栏。',
    sortBin1='得分',
    sortBin2='零分',
    sort1='从原文一字不差抄来的两个词',
    sort2='用阿拉伯数字写的数字',
    sort3='一词限制下的带连字符的词',
    sort4='限制两个词却写了三个词',
    sort5='用自己的话写出的正确意思',
    sort6='拼错了的原文单词',
    sortWhy='所有<strong>得分</strong>的答案，都是原文的词、在字数限制之内、按印刷原样拼写——数字算一项，带连字符的词算一个'
            '词。另一栏是看懂了原文却一分不得的三种情况：超出限制一个词、换了说法的正确意思、抄错一个字母的原词。阅卷人不看意思，只拿你的答案'
            '和答案对照。',

    actTitle='自己来出填空题',
    actUse='至少用上三个：',
    actSpeakBrief='两人一组，每人一篇短文。为自己那篇写一段有三个空的摘要——四句'
                  '话，上方写明字数限制——然后交换。同伴只能从文章里找词填空；你'
                  '像考官一样批改：原文的词、在限制之内、按印刷原样拼写，否则就'
                  '是零分。',
    actSpeak1='填任何一个空之前，先大声说出它需要什么词性，以及句中哪些词告诉了'
              '你这一点。',
    actSpeak2='每个答案都要在文章里指出原词。指不出来的答案不算。',
    actSpeak3='在同伴的摘要里找一个原文中两个词都能填的空，把句子改写到只有一个'
              '词能填。',
    actWriteKind='写作 · 150–200 词',
    actWriteBrief='找一篇你这周读过的文章，写一段四句话、三个空的摘要，在上方写'
                  '明字数限制。然后写出答案：每个空对应的原文原词，再写一个诱人'
                  '的错误答案，并说明它为什么是零分。',
    actPlaceholder='NO MORE THAN TWO WORDS. Summary: … Gap 1: … Tempting wrong '
                   'answer: …',
)


# ── Japanese ───────────────────────────────────────────────────────────
T['ja'] = dict(
    coverTitle='Summary and <em>Sentence Completion</em>',
    coverSub='語数制限がいちばん効いてくる形式。答えは本文からそのまま取り、つづ'
             'りも採点され、一語多いだけで0点です',
    chipLevel='C1 · 上級', chipFocus='Reading · 両モジュール共通',
    chipCount='18 点',

    t1Eyebrow='始める前に',
    t1Title='空所が三つ、指示が一行。まず読むのはその一行',
    t1ah='与えられるもの',
    t1ab='本文の一部の要約、または独立した文のまとまりで、空所があります。空所を埋める語は本文にあります。要約はふつう本文の順に進み、ふつうはそ'
         'の一部の範囲だけを扱います――その範囲がどこから始まるかを見つけ、その中にとどまりましょう。',
    t1an='Academic も General Training も出題のしかたは同じです。ここで学ぶこと'
         'はどちらにも使えます。',
    t1bh='まず指示文を読む',
    t1bb='<strong>NO MORE THAN TWO WORDS AND/OR A NUMBER. ONE WORD '
         'ONLY.</strong> 制限は空所の上に印刷されていて、最初に読むべきものです'
         '――要約より先、本文より先に。答えを見つける前から、正しい答えの形を決め'
         'てしまうからです。',
    t1bn='ハイフンでつながった語は一語で、<em>the</em> も数に入る一語です。AND/OR A NUMBER '
         'なら語に加えて数字を一つ書けますが、語数だけの制限なら数字も一語と数えます。',
    t1ch='語群の枠があることも',
    t1cb='A&ndash;H の語のリストが与えられたら、本文ではなくリストから選び、記号'
         'を書きます。リストの語は本文にまったく出てこないこともあり、選択肢は空'
         '所より多くなっています。',
    t1cn='根っこの技能は同じです。本文の該当箇所を見つけ、それから空所の文法を確'
         'かめます。',

    t2Eyebrow='始める前に',
    t2Title='語は本文にある。そのまま取る。',
    t2ah='意味で場所を見つける',
    t2ab='要約が本文を一語一語くり返すことはまれで、空所の<strong>まわり</strong>の大部分を言い換えています。文の意味を手がかり'
         'に該当する行を見つけ、その行の中で要約が抜いた語を探しましょう。',
    t2an='共通の語は探す場所を教えてくれます。空所の語は、たいてい言い換えられな'
         'かった唯一の語です。',
    t2bh='そして、そのまま写す',
    t2bb='つづりも形も本文と同じに。複数形にしない、時制を変えない、要約にすでに'
         'ある冠詞を足さない。自分の言葉で書いた正しい内容は0点です。採点者はあな'
         'たの答えを本文ではなく解答と照らし合わせるからです。',
    t2bn='その語が本文になければ、答えではありません。',
    t2ch='制限は壁',
    t2cb='NO MORE THAN TWO WORDS なら、三語の答えはどれほど正しくても0点です。半分の点もなく、0点。答えが制限を超えると'
         'き、余分な語はたいてい、要らなかった冠詞、形容詞、前置詞です。',
    t2cn='答えを書き、語数を数え、もう一度指示文を読みましょう。',

    t3Eyebrow='始める前に',
    t3Title='探す前に語を予測する',
    t3ah='まず品詞を決める',
    t3ab='空所のある要約の文を読み、何が必要かを決めます：名詞、動詞、形容詞、数字。<em>the</em> や <em>a</em> '
         'の後の空所は名詞、空所の後に名詞が続くなら形容詞、主語の後の空所は動詞、<em>lasted</em> や '
         '<em>cost</em> の後の空所は量です。',
    t3an='本文を開く前に決めましょう。そうすれば、どんな語でもなく、一種類の語を'
         '探すことになります。',
    t3bh='答えは英語として通じること',
    t3bb='語を空所に入れて、文全体を読みます。単数か複数か、過去か現在か：決める'
         'のは要約の文で、本文の語はたいていもともと合っています。要約はその語か'
         'ら書かれているからです。',
    t3bn='文が通じなければ、形か場所が間違っています。',
    t3ch='つづりも採点される',
    t3cb='写した語でも同じです。一文字ずつ写し、本文と照らし合わせましょう。知っ'
         'ている語でも写し間違えれば、知らなかった語とまったく同じ点です。',
    t3cn='Reading には転記の時間がありません。解答用紙に直接書き進めましょう。',

    mcaEyebrow='演習 1 · 指示文を読む',
    mcaTitle='制限は何を認めているか？',
    mcbEyebrow='演習 2 · 言い換えずに写す',
    mcbTitle='点になる答えはどれか？',
    mccEyebrow='演習 3 · 空所には形がある',
    mccTitle='文に合う形はどれか？',

    r1why='二語と数字一つ。<em>The</em> は一語なので、<em>the 1997 survey '
          'results</em> は三語、<em>results of the survey</em> は四語、'
          '<em>survey results from 1997</em> は三語と数字です。制限内に収まるの'
          'は <em>1997 survey results</em> だけです。',
    r2why='ハイフンはつなぎます。<em>well-known</em> は一語です。ほかの三つはそ'
          'れぞれ二語で、ONE WORD ONLY では0点です。',
    r3why='<em>A fall of 200 tonnes</em> は四語と数字で、一語多すぎます。<em>In '
          '1846</em> は一語と数字、<em>nearly 200 tonnes</em> は二語と数字、'
          '<em>some 200 tonnes each</em> は三語と数字：どれも認められます。',
    r4why='リストがあるときは記号を書き、リストの語が本文にまったくないこともあります。選択肢は空所より多く、要約はそれでもふつう一部の範囲だけ'
          'を扱い、語数制限はありません：答えは記号です。',
    r5why='本文は <em>a process known as bleaching</em> と言っています。要約は '
          '<em>warmer water</em> を <em>rising sea temperatures</em> と言い換え、'
          '空所の語はそのままです。<em>Coral whitening</em> は内容は正しいが別の'
          '言葉、<em>bleached</em> は形が違い、<em>known as bleaching</em> は三語'
          'です。',
    r6why='<em>Limestone aquifer</em>、印刷どおり。<em>Underground '
          'reservoir</em> は言い換え、<em>limestone aquifers</em> は形が違い、'
          '<em>a limestone aquifer</em> は要約にすでにある冠詞を重ねて三語になり'
          'ます。',
    r7why='<em>Visiting engineer</em>、二語で、本文とまったく同じです。<em>a</em> '
          'の後に複数形は合いません。<em>travelling technician</em> は自分の言葉'
          'で、冠詞つきの形は <em>a</em> が重なり、制限も超えます。',
    r8why='一語：本文どおりの <em>olives</em>。<em>Olive</em> は形が違い、'
          '<em>olive groves</em> は本文になく、<em>planted olives</em> は ONE '
          'WORD ONLY のもとで二語です。',
    r9why='所有格 <em>the keeper&rsquo;s</em> の後には名詞が必要です。本文の四つ'
          'の語で名詞は <em>entries</em> だけで、<em>became</em> もそれを裏づけて'
          'います：何かが短くなったのです。',
    r10why='主語、空所、目的語：空所は動詞で、本文が過去なので要約も過去です。'
           '<em>Reinforced</em>。名詞と -ing 形では文になりませんし、'
           '<em>reinforces</em> は <em>engineers</em> と一致しません。',
    r11why='<em>Was not ______ until</em> には過去分詞、つまり受け身が必要です。'
           '<em>Correctly identified</em> は本文に印刷されている語で、文も通じま'
           'す。この形を予測すれば、見る前に三つの選択肢が消えます。',
    r12why='<em>Took</em> には期間が必要です：数字と複数形の名詞。<em>Eleven '
           'years</em>、印刷どおり。単数形は一致せず、序数は別の語で、<em>an</em> は複数形の前には置けません。',

    sortEyebrow='演習 4 · 採点者がすること',
    sortTitle='六つの答えを分類しましょう',
    sortHint='それぞれを列にドラッグしてください。または項目をクリックしてから、'
             '入れたい列をクリックします。',
    sortBin1='点になる',
    sortBin2='0点',
    sort1='本文からそのまま写した二語',
    sort2='算用数字で書いた数',
    sort3='一語制限でのハイフンつきの語',
    sort4='制限が二語なのに三語',
    sort5='自分の言葉で書いた正しい内容',
    sort6='つづりを間違えた本文の語',
    sortWhy='<strong>点になる</strong>ものはすべて、本文の語を、制限内で、印刷どおりのつづりで書いたものです――数字は一項目'
            '、ハイフンつきの語は一語と数えます。もう一方の列は、本文を理解していながら点にならない三つのパターンです：制限を一語超えたもの、'
            '正しい内容を別の言葉で書いたもの、一文字写し間違えた語。採点者は意味を読みません。答えを解答と照らし合わせるだけです。',

    actTitle='空所を自分で作る',
    actUse='少なくとも三つ使いましょう：',
    actSpeakBrief='ペアで、それぞれ短い記事を一つ用意します。自分の記事について、'
                  '空所が三つある要約を書きます――四文で、上に語数制限を書きます'
                  '――そして交換します。相手は記事だけを見て空所を埋め、あなたは'
                  '試験官のように採点します：本文の語、制限内、印刷どおりのつづ'
                  'り。そうでなければ0点です。',
    actSpeak1='空所を埋める前に、どの品詞が必要か、そして文のどの語がそれを示し'
              'ているかを声に出して言いましょう。',
    actSpeak2='どの答えについても、記事の中の語を指し示しましょう。指し示せない答'
              'えは認められません。',
    actSpeak3='相手の要約から、本文の二つの語が入りうる空所を見つけ、一語しか入ら'
              'ないように文を書き直しましょう。',
    actWriteKind='ライティング · 150–200 語',
    actWriteBrief='今週読んだ文章を一つ選び、空所が三つある四文の要約を書き、上に'
                  '語数制限を書きましょう。次に解答を書きます：各空所に入る本文の'
                  '語そのものと、引っかかりやすい誤答を一つ、それが0点になる理由'
                  'とともに。',
    actPlaceholder='NO MORE THAN TWO WORDS. Summary: … Gap 1: … Tempting wrong '
                   'answer: …',
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
