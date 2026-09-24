# -*- coding: utf-8 -*-
"""Interface strings for IELTS Vocabulary: Lexical Resource.

Ten languages: English, German and Spanish from the start; French,
Italian, Portuguese, Russian, Arabic, Chinese and Japanese added on
2026-09-24 (conventions in `ielts_langs.py`).

The usual split (HOUSE-STYLE §8), and on this deck it matters more than
elsewhere: the collocations are the lesson. <em>Conduct research</em>,
<em>heavy traffic</em>, <em>reach a decision</em> stay English inside the
German and Spanish cards, because a German rendering of an English collocation
teaches nothing — the whole point is which English word the English noun takes.
What translates is the rule, and the reason the pairing is the unit.
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
    coverTitle='Lexical <em>Resource</em>',
    coverSub='A quarter of the marks in Speaking and in Writing, and rare '
             'words only count when they land',
    chipLevel='C1 · Advanced', chipFocus='Speaking &amp; Writing',
    chipCount='18 points',

    t1Eyebrow='Before you start',
    t1Title='It rewards the right word, not just the rare one',
    t1ah='What the descriptors ask for',
    t1ab='A range of vocabulary used with <strong>precision</strong> and '
         '<strong>flexibility</strong>, and <em>less common</em> words where '
         'they fit. Inaccurate word choice is named from band 8 down, and '
         'collocation at bands 7 and 8.',
    t1an='A miss is charged. So is a range that never leaves the plainest '
         'words.',
    t1bh='The near-miss costs more than the plain word',
    t1bb='A candidate who writes <em>ameliorate the traffic</em> has reached '
         'for a rare verb and given it the wrong object: <em>ameliorate</em> '
         'needs something already bad, like congestion or conditions. The '
         'examiner sees the reach and the miss. <em>Ease congestion</em> is '
         'plain, right, and does the job.',
    t1bn='Reach for the word you are sure of, then stretch once you are '
         'certain of the fit.',
    t1ch='Memorised phrases are audible',
    t1cb='Band 9 phrase lists sit apart from the answer around them, and '
         'examiners are trained to hear exactly that. Drop one into a plain '
         'answer and the examiner can tell which language is really yours.',
    t1cn='It is the mismatch that gives it away, not the phrase itself.',

    t2Eyebrow='Before you start',
    t2Title='The unit is the pairing, not the word',
    t2ah='The noun chooses the verb',
    t2ab='You <em>conduct</em> or <em>carry out</em> research, <em>make</em> '
         'or <em>reach</em> a decision, and <em>draw</em> or <em>come '
         'to</em> a conclusion. None of those verbs is rare, and none is '
         'free: the noun decides which verbs it accepts.',
    t2an='<em>Make research</em> and <em>do a decision</em> are two of the '
         'commonest misses.',
    t2bh='And the adjective',
    t2bb='<em>Heavy traffic</em>, <em>heavy rain</em>, <em>heavy losses</em>, '
         '<em>heavy fighting</em> &mdash; but never <em>heavy sunshine</em>. '
         'The adjective is chosen by the noun, and no rule predicts which.',
    t2bn='Which is why they are learnt whole, in the phrase, rather than '
         'derived.',
    t2ch='So write the phrase, not the word',
    t2cb='A notebook entry of one word plus a translation gives you a word you '
         'cannot use. An entry of the phrase it lives in gives you something '
         'you can say tomorrow.',
    t2cn='<em>Tackle congestion</em> is worth ten times <em>congestion = '
         '[your language]</em>.',

    t3Eyebrow='Before you start',
    t3Title='Paraphrase is the skill that pays twice',
    t3ah='Both papers reward it',
    t3ab='Speaking names paraphrase in its descriptors; Writing rewards the '
         'flexibility behind it and gives no credit for wording copied from '
         'the question. The work you do on saying one idea three ways counts '
         'in both rooms &mdash; above all in Part 3 and in Task 2, where the '
         'ideas are abstract.',
    t3an='It is also what Reading tests, from the other side.',
    t3bh='Reword the question, do not copy it',
    t3bb='Phrases copied from the prompt earn nothing as vocabulary. An '
         'opening in your own terms shows range; one that copies the '
         'question shows none.',
    t3bn='Change the grammar, not just the nouns: <em>should museums be '
         'free</em> becomes <em>whether entry should cost anything</em>.',
    t3ch='Build the bank by idea',
    t3cb='A topic bank sorted alphabetically gives you words. Sorted by idea '
         '&mdash; congestion, ageing, automation &mdash; each word arrives '
         'with an argument already attached, which is what you are short of '
         'under time.',
    t3cn='Ten ideas with three phrases each beats a hundred words with none.',

    mcaEyebrow='Activity 1 · Precision, not rarity',
    mcaTitle='What is actually being marked?',
    mcbEyebrow='Activity 2 · Words that travel together',
    mcbTitle='Which pairing does English use?',
    mccEyebrow='Activity 3 · Saying it another way',
    mccTitle='Paraphrase, and the bank behind it',

    v1why='Less common lexis used <em>accurately</em> and <em>flexibly</em>. '
          'The number of rare words is not counted; whether they are used '
          'accurately is, and inaccuracy is penalised by name.',
    v2why='<em>Ameliorate</em> needs something that is already bad &mdash; '
          'conditions, the effects, the problem. Traffic is not bad in '
          'itself; congestion is. The reach is visible and so is the miss, '
          'and Lexical Resource is where it is charged.',
    v3why='The plain word that is exactly right. Precision is the '
          'descriptor; a thesaurus swap the writer cannot control is a '
          'common way to lose marks while trying to gain them.',
    v4why='They sit apart from the English around them, and examiners are '
          'trained to hear that. A memorised phrase is not credited as your '
          'own language, and one that does not fit the question is an error '
          'like any other.',
    v5why='<em>Conduct research</em> &mdash; or <em>do</em> or <em>carry '
          'out</em> research. The noun decides which verbs it accepts, and '
          '<em>make research</em> is the miss that costs most often, because '
          'its equivalent is correct in several other languages.',
    v6why='<em>Strong rain</em> is the one English does not say &mdash; rain '
          'takes <em>heavy</em>. Evidence, opinions and smells all take '
          '<em>strong</em>, and no rule tells you which noun takes which.',
    v7why='The verb or the adjective. The noun is usually the part a learner '
          'already knows &mdash; what has to be learnt with it is the word it '
          'happens to take.',
    v8why='In a phrase. A word plus a translation is a word you can recognise; '
          'a word in the company it keeps is one you can produce, which is the '
          'only kind that is scored.',
    v9why='It changes the grammar as well as the words: a question about what '
          'people think becomes a statement about what is disputed. The other '
          'three shuffle the prompt and hand it back.',
    v10why='Both papers are marked on Lexical Resource: Speaking names '
           'paraphrase outright, and Writing rewards the flexibility it '
           'shows. So the same practice counts twice &mdash; and Part 3 and '
           'Task 2 are where a paraphrase does the most work.',
    v11why='By idea. A word filed under <em>congestion</em> arrives with an '
           'argument attached; a word filed under C arrives on its own, and '
           'under time an argument is what you are short of.',
    v12why='Describe what it does. Paraphrase is rewarded under this very '
           'criterion &mdash; a word from your own language is not English, '
           'asking is not answering, and a guessed rare word is the near-miss '
           'again.',

    sortEyebrow='Activity 4 · Where the revision time should go',
    sortTitle='Sort the six habits',
    sortHint='Drag each one into a column &mdash; or click an item, then the '
             'column you want it in.',
    sortBin1='Raises the band',
    sortBin2='Does nothing, or costs you',

    actTitle='Build one page of the bank',
    actUse='Use at least three:',
    actSpeakBrief='In pairs. Take one topic &mdash; congestion, ageing, '
                  'automation, tourism. Five minutes to build a page '
                  'together: three ideas, and for each idea two phrases '
                  'rather than two words. Then argue the topic for two '
                  'minutes using the phrases on your page.',
    actSpeak1='Every phrase on the page must be a pairing &mdash; a verb with '
              'its noun, or an adjective with its noun. No bare words.',
    actSpeak2='Your partner stops you whenever you reach for a content word '
              'that is not on the page, and you have to say it again using '
              'one that is.',
    actSpeak3='Take one idea and say it three ways: plainly, formally, and as '
              'you would say it to a friend.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Take a Task 2 question and write the opening paragraph '
                  'twice: once repeating the question wording, once rewording '
                  'it properly. Then underline in the second one every phrase '
                  'you would count as your own vocabulary, and say how many '
                  'there are.',
    actPlaceholder='Whether entry to museums should cost anything…',
)

# The sort explanation sits in the data module, which keeps the only copy
# of the English. It was a plain string there until 2026-09-23, so German and
# Spanish learners read it in English.
from ieltsvocab_data import SORT_WHY
T['en']['sortWhy'] = SORT_WHY

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Lexical <em>Resource</em>',
    coverSub='Ein Viertel der Punkte in Speaking und in Writing &mdash; und '
             'seltene Wörter zählen nur, wenn sie sitzen',
    chipLevel='C1 · Fortgeschritten', chipFocus='Speaking &amp; Writing',
    chipCount='18 Punkte',

    t1Eyebrow='Bevor du beginnst',
    t1Title='Belohnt wird das richtige Wort, nicht bloß das seltene',
    t1ah='Was die Deskriptoren verlangen',
    t1ab='Ein Wortschatz, der mit <strong>Präzision</strong> und '
         '<strong>Flexibilität</strong> eingesetzt wird, und <em>weniger '
         'gebräuchliche</em> Wörter dort, wo sie passen. Ungenaue Wortwahl '
         'wird ab Band 8 abwärts genannt, Wortverbindungen in Band 7 und 8.',
    t1an='Ein Fehlgriff wird angerechnet. Ein Wortschatz, der nie über die '
         'schlichtesten Wörter hinausgeht, ebenfalls.',
    t1bh='Der Fastreffer kostet mehr als das schlichte Wort',
    t1bb='Wer <em>ameliorate the traffic</em> schreibt, hat nach einem '
         'seltenen Verb gegriffen und ihm das falsche Objekt gegeben: '
         '<em>ameliorate</em> braucht etwas, das schon schlecht ist, etwa '
         'Staus oder Zustände. Der Prüfer sieht den Griff und den Fehlgriff. '
         '<em>Ease congestion</em> ist schlicht, richtig und erfüllt seinen '
         'Zweck.',
    t1bn='Greif zum Wort, bei dem du sicher bist, und streck dich erst, wenn '
         'du die Passung kennst.',
    t1ch='Auswendiges hört man',
    t1cb='Listen mit „Band-9-Phrasen“ stehen neben der Antwort, die sie '
         'umgibt, und Prüfer sind darauf geschult, genau das zu hören. Steht '
         'eine davon in einer schlichten Antwort, hört der Prüfer, welche '
         'Sprache wirklich deine ist.',
    t1cn='Verräterisch ist der Bruch, nicht die Phrase selbst.',

    t2Eyebrow='Bevor du beginnst',
    t2Title='Die Einheit ist die Wortverbindung, nicht das Wort',
    t2ah='Das Substantiv wählt das Verb',
    t2ab='Zu <em>research</em> gehören <em>conduct</em> oder <em>carry '
         'out</em>, zu <em>a decision</em> <em>make</em> oder '
         '<em>reach</em>, zu <em>a conclusion</em> <em>draw</em> oder '
         '<em>come to</em>. Keines dieser Verben ist selten, und keines ist '
         'frei wählbar: Das Substantiv entscheidet, welche Verben es zulässt.',
    t2an='<em>Make research</em> und <em>do a decision</em> gehören zu den '
         'häufigsten Fehlgriffen.',
    t2bh='Und das Adjektiv',
    t2bb='<em>Heavy traffic</em>, <em>heavy rain</em>, <em>heavy losses</em>, '
         '<em>heavy fighting</em> &mdash; aber nie <em>heavy sunshine</em>. '
         'Das Adjektiv wählt das Substantiv, und keine Regel sagt voraus, '
         'welches.',
    t2bn='Deshalb lernt man sie als Ganzes, in der Phrase, statt sie '
         'herzuleiten.',
    t2ch='Also schreib die Phrase, nicht das Wort',
    t2cb='Ein Eintrag aus einem Wort plus Übersetzung gibt dir ein Wort, das '
         'du nicht verwenden kannst. Ein Eintrag mit der Phrase, in der es '
         'lebt, gibt dir etwas, das du morgen sagen kannst.',
    t2cn='<em>Tackle congestion</em> ist zehnmal mehr wert als '
         '<em>congestion = Stau</em>.',

    t3Eyebrow='Bevor du beginnst',
    t3Title='Umschreiben ist die Fertigkeit, die doppelt zahlt',
    t3ah='Beide Prüfungsteile belohnen sie',
    t3ab='Speaking nennt Paraphrase ausdrücklich in seinen Deskriptoren; '
         'Writing belohnt die Flexibilität dahinter und rechnet aus der '
         'Aufgabe abgeschriebene Formulierungen nicht an. Die Arbeit, einen '
         'Gedanken auf drei Arten zu sagen, zählt in beiden Räumen &mdash; '
         'vor allem in Teil 3 und in Task 2, wo die Ideen abstrakt sind.',
    t3an='Und das Reading prüft genau dasselbe, nur von der anderen Seite.',
    t3bh='Formuliere die Frage um, kopier sie nicht',
    t3bb='Aus der Aufgabe abgeschriebene Wendungen bringen als Wortschatz '
         'nichts. Eine Einleitung in eigenen Worten zeigt Bandbreite; eine, '
         'die die Frage abschreibt, zeigt keine.',
    t3bn='Ändere die Grammatik, nicht nur die Substantive: <em>should museums '
         'be free</em> wird zu <em>whether entry should cost anything</em>.',
    t3ch='Bau die Sammlung nach Ideen',
    t3cb='Eine alphabetisch sortierte Sammlung gibt dir Wörter. Nach Ideen '
         'sortiert &mdash; Stau, Alterung, Automatisierung &mdash; kommt jedes '
         'Wort mit einem Argument im Schlepptau, und genau daran fehlt es '
         'unter Zeitdruck.',
    t3cn='Zehn Ideen mit je drei Phrasen schlagen hundert Wörter ohne.',

    mcaEyebrow='Aktivität 1 · Präzision, nicht Seltenheit',
    mcaTitle='Was wird hier eigentlich bewertet?',
    mcbEyebrow='Aktivität 2 · Wörter, die zusammen reisen',
    mcbTitle='Welche Wortverbindung verwendet das Englische?',
    mccEyebrow='Aktivität 3 · Es anders sagen',
    mccTitle='Umschreiben, und die Sammlung dahinter',

    v1why='Weniger gebräuchlicher Wortschatz, <em>genau</em> und '
          '<em>flexibel</em> eingesetzt. Gezählt wird nicht, wie viele '
          'seltene Wörter vorkommen, sondern ob sie genau sitzen &mdash; und '
          'Ungenauigkeit wird ausdrücklich bestraft.',
    v2why='<em>Ameliorate</em> braucht etwas, das schon schlecht ist &mdash; '
          'Zustände, die Folgen, das Problem. Verkehr ist an sich nicht '
          'schlecht, Stau schon. Der Griff ist sichtbar und der Fehlgriff '
          'auch, und angerechnet wird er unter Lexical Resource.',
    v3why='Das schlichte Wort, das genau passt. Präzision steht im '
          'Deskriptor; ein Synonym aus dem Thesaurus, das man nicht '
          'beherrscht, ist ein häufiger Weg, Punkte zu verlieren, während '
          'man welche gewinnen will.',
    v4why='Sie heben sich vom Englisch um sie herum ab, und Prüfer sind '
          'darauf geschult, das zu hören. Eine auswendig gelernte Wendung '
          'wird nicht als deine eigene Sprache angerechnet, und eine, die '
          'nicht zur Frage passt, ist ein Fehler wie jeder andere.',
    v5why='<em>Conduct research</em> &mdash; oder <em>do</em> bzw. <em>carry '
          'out research</em>. Das Substantiv entscheidet, welche Verben es '
          'zulässt, und <em>make research</em> ist der Fehlgriff, der am '
          'häufigsten kostet, weil die Entsprechung in mehreren anderen '
          'Sprachen richtig ist.',
    v6why='<em>Strong rain</em> sagt das Englische nicht &mdash; rain nimmt '
          '<em>heavy</em>. Evidence, opinions und smells nehmen alle '
          '<em>strong</em>, und keine Regel sagt dir, welches Substantiv '
          'welches nimmt.',
    v7why='Das Verb oder das Adjektiv. Das Substantiv kennt man meist schon '
          '&mdash; zu lernen ist das Wort, das es zufällig nimmt.',
    v8why='In einer Phrase. Wort plus Übersetzung ergibt ein Wort, das du '
          'wiedererkennst; ein Wort in seiner Gesellschaft ergibt eines, das '
          'du produzieren kannst, und nur das wird bewertet.',
    v9why='Es ändert die Grammatik und nicht nur die Wörter: aus einer Frage, '
          'was Leute denken, wird eine Aussage darüber, was strittig ist. Die '
          'anderen drei schieben die Aufgabe um und geben sie zurück.',
    v10why='Beide Prüfungsteile werden nach Lexical Resource bewertet: '
           'Speaking nennt Paraphrase ausdrücklich, und Writing belohnt die '
           'Flexibilität, die sie zeigt. Dieselbe Übung zählt also doppelt '
           '&mdash; und in Teil 3 und Task 2 leistet eine Paraphrase am '
           'meisten.',
    v11why='Nach Ideen. Ein Wort unter <em>congestion</em> kommt mit einem '
           'Argument; ein Wort unter C kommt allein, und unter Zeitdruck fehlt '
           'dir das Argument.',
    v12why='Beschreib, was es tut. Umschreiben wird genau von diesem Kriterium '
           'belohnt &mdash; ein Wort aus deiner Sprache ist kein Englisch, '
           'Fragen ist keine Antwort, und ein geratenes seltenes Wort ist '
           'wieder der Fastreffer.',

    sortEyebrow='Aktivität 4 · Wohin die Lernzeit gehört',
    sortTitle='Sortiere die sechs Gewohnheiten',
    sortHint='Zieh jede in eine Spalte &mdash; oder klicke ein Element an und '
             'dann die Spalte, in die es soll.',
    sortBin1='Hebt die Note',
    sortBin2='Bringt nichts oder kostet',

    actTitle='Baut eine Seite der Sammlung',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu zweit. Nehmt ein Thema &mdash; Stau, Alterung, '
                  'Automatisierung, Tourismus. Fünf Minuten für eine '
                  'gemeinsame Seite: drei Ideen und zu jeder Idee zwei '
                  'Wendungen statt zwei Wörtern. Dann diskutiert das Thema '
                  'zwei Minuten lang mit den Wendungen auf eurer Seite.',
    actSpeak1='Jede Phrase auf der Seite muss eine Wortverbindung sein &mdash; Verb '
              'mit Substantiv oder Adjektiv mit Substantiv. Keine nackten '
              'Wörter.',
    actSpeak2='Dein Partner unterbricht dich, sobald du nach einem '
              'Inhaltswort greifst, das nicht auf der Seite steht, und du '
              'musst es noch einmal mit einem sagen, das dort steht.',
    actSpeak3='Nimm eine Idee und sag sie auf drei Arten: schlicht, förmlich, '
              'und so, wie du es einem Freund sagen würdest.',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Nimm eine Task-2-Frage und schreib die Einleitung zweimal: '
                  'einmal mit den Wörtern der Aufgabe, einmal richtig '
                  'umformuliert. Unterstreich in der zweiten jede Phrase, die '
                  'du als eigenen Wortschatz zählen würdest, und sag, wie '
                  'viele es sind.',
    actPlaceholder='Whether entry to museums should cost anything…',

    # The sort explanation; English from the data module.
    sortWhy='Die Gewohnheiten, die das Band heben, drehen sich darum, '
            'Sprache zu <strong>benutzen</strong>; die anderen darum, sie '
            '<strong>vorzuzeigen</strong>. Die Deskriptoren fragen, ob du '
            'genau und flexibel sagen kannst, was du meinst &mdash; also '
            'schlägt ein Wort, das du beherrschst, ein seltenes, das '
            'danebengeht, und eine ganz gelernte Wendung ein einzeln '
            'gelerntes Wort. Die Vorzeige-Gewohnheiten fühlen sich wie '
            'Fortschritt an, und genau das ist die Falle.',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Lexical <em>Resource</em>',
    coverSub='Un cuarto de la nota en Speaking y en Writing, y las palabras '
             'raras solo cuentan cuando aciertan',
    chipLevel='C1 · Avanzado', chipFocus='Speaking y Writing',
    chipCount='18 puntos',

    t1Eyebrow='Antes de empezar',
    t1Title='Premia la palabra justa, no solo la rara',
    t1ah='Qué piden los descriptores',
    t1ab='Un vocabulario usado con <strong>precisión</strong> y '
         '<strong>flexibilidad</strong>, y palabras <em>menos comunes</em> '
         'donde encajan. La elección imprecisa de palabras se menciona de la '
         'banda 8 hacia abajo, y las colocaciones en las bandas 7 y 8.',
    t1an='Un fallo se penaliza. También un vocabulario que nunca sale de las '
         'palabras más sencillas.',
    t1bh='El casi-acierto cuesta más que la palabra llana',
    t1bb='Quien escribe <em>ameliorate the traffic</em> ha buscado un verbo '
         'raro y le ha dado el complemento equivocado: <em>ameliorate</em> '
         'necesita algo que ya es malo, como los atascos o unas condiciones. '
         'El examinador ve el intento y el fallo. <em>Ease congestion</em> '
         'es sencillo, correcto y cumple su función.',
    t1bn='Ve a por la palabra de la que estés seguro y estírate solo cuando '
         'sepas que encaja.',
    t1ch='Las frases memorizadas se oyen',
    t1cb='Las listas de «frases de band 9» quedan aparte del inglés que las '
         'rodea, y a los examinadores se les entrena para oír justo eso. Mete '
         'una en una respuesta llana y el examinador sabe qué lengua es de '
         'verdad la tuya.',
    t1cn='Lo que te delata es el desajuste, no la frase.',

    t2Eyebrow='Antes de empezar',
    t2Title='La unidad es la combinación, no la palabra',
    t2ah='El sustantivo elige el verbo',
    t2ab='Con <em>research</em> van <em>conduct</em> o <em>carry out</em>; '
         'con <em>a decision</em>, <em>make</em> o <em>reach</em>; con <em>a '
         'conclusion</em>, <em>draw</em> o <em>come to</em>. Ninguno de esos '
         'verbos es raro, y ninguno es libre: el sustantivo decide qué '
         'verbos acepta.',
    t2an='<em>Make research</em> y <em>do a decision</em> están entre los '
         'fallos más comunes.',
    t2bh='Y el adjetivo',
    t2bb='<em>Heavy traffic</em>, <em>heavy rain</em>, <em>heavy losses</em>, '
         '<em>heavy fighting</em>, pero nunca <em>heavy sunshine</em>. El '
         'adjetivo lo elige el sustantivo, y ninguna regla predice cuál.',
    t2bn='Por eso se aprenden enteras, dentro de la frase, en vez de '
         'deducirse.',
    t2ch='Así que apunta la frase, no la palabra',
    t2cb='Una entrada de una palabra con su traducción te da una palabra que '
         'no puedes usar. Una entrada con la frase en la que vive te da algo '
         'que puedes decir mañana.',
    t2cn='<em>Tackle congestion</em> vale diez veces más que <em>congestion = '
         'atasco</em>.',

    t3Eyebrow='Antes de empezar',
    t3Title='Parafrasear es la destreza que paga dos veces',
    t3ah='Las dos pruebas la premian',
    t3ab='Speaking nombra la paráfrasis en sus descriptores; Writing premia '
         'la flexibilidad que hay detrás y no puntúa lo copiado del '
         'enunciado. El trabajo de decir una idea de tres maneras cuenta en '
         'las dos salas &mdash; sobre todo en la Parte 3 y en Task 2, donde '
         'las ideas son abstractas.',
    t3an='Y el Reading examina lo mismo, solo que desde el otro lado.',
    t3bh='Reformula la pregunta, no la copies',
    t3bb='Las expresiones copiadas del enunciado no puntúan como '
         'vocabulario. Una introducción con tus propias palabras muestra '
         'variedad; una que copia la pregunta no muestra ninguna.',
    t3bn='Cambia la gramática, no solo los sustantivos: <em>should museums be '
         'free</em> pasa a <em>whether entry should cost anything</em>.',
    t3ch='Monta el banco por ideas',
    t3cb='Un banco ordenado alfabéticamente te da palabras. Ordenado por ideas '
         '&mdash; atascos, envejecimiento, automatización &mdash; cada palabra '
         'llega con un argumento ya enganchado, que es justo lo que falta con '
         'el reloj en marcha.',
    t3cn='Diez ideas con tres frases cada una ganan a cien palabras sin '
         'ninguna.',

    mcaEyebrow='Actividad 1 · Precisión, no rareza',
    mcaTitle='¿Qué se está calificando en realidad?',
    mcbEyebrow='Actividad 2 · Palabras que viajan juntas',
    mcbTitle='¿Qué combinación usa el inglés?',
    mccEyebrow='Actividad 3 · Decirlo de otra manera',
    mccTitle='Parafrasear, y el banco que hay detrás',

    v1why='Léxico menos común usado con <em>exactitud</em> y '
          '<em>flexibilidad</em>. No se cuenta cuántas palabras raras hay, '
          'sino si se usan con exactitud, y la inexactitud se penaliza '
          'expresamente.',
    v2why='<em>Ameliorate</em> necesita algo que ya es malo &mdash; unas '
          'condiciones, los efectos, el problema. El tráfico no es malo en '
          'sí; los atascos sí. El intento se ve y el fallo también, y es en '
          'Lexical Resource donde se cobra.',
    v3why='La palabra sencilla que es exactamente la correcta. La precisión '
          'es el descriptor; un sinónimo de diccionario que no dominas es '
          'una forma común de perder puntos intentando ganarlos.',
    v4why='Se despegan del inglés que las rodea, y los examinadores están '
          'formados para oírlo. Una frase memorizada no cuenta como lengua '
          'tuya, y una que no encaja con la pregunta es un error como '
          'cualquier otro.',
    v5why='<em>Conduct research</em> &mdash; o <em>do</em> o <em>carry out '
          'research</em>. El sustantivo decide qué verbos acepta, y <em>make '
          'research</em> es el fallo que más cuesta, porque su equivalente '
          'es correcto en varias otras lenguas.',
    v6why='<em>Strong rain</em> es la que el inglés no dice: rain lleva '
          '<em>heavy</em>. Evidence, opinions y smells llevan todas '
          '<em>strong</em>, y ninguna regla te dice qué sustantivo lleva '
          'cuál.',
    v7why='El verbo o el adjetivo. El sustantivo suele ser la parte que ya se '
          'sabe: lo que hay que aprender con él es la palabra que resulta que '
          'lleva.',
    v8why='En una frase. Palabra más traducción da una palabra que reconoces; '
          'una palabra con su compañía da una que puedes producir, y solo esa '
          'se califica.',
    v9why='Cambia la gramática además de las palabras: una pregunta sobre lo '
          'que piensa la gente pasa a ser una afirmación sobre lo que se '
          'discute. Las otras tres barajan el enunciado y lo devuelven.',
    v10why='Las dos pruebas se califican con Lexical Resource: Speaking '
           'nombra la paráfrasis expresamente, y Writing premia la '
           'flexibilidad que demuestra. Así que la misma práctica cuenta dos '
           'veces &mdash; y la Parte 3 y Task 2 son donde una paráfrasis '
           'rinde más.',
    v11why='Por ideas. Una palabra archivada en <em>congestion</em> llega con '
           'un argumento; una archivada en la C llega sola, y con el reloj en '
           'marcha lo que falta es el argumento.',
    v12why='Describe qué hace. Parafrasear lo premia este mismo criterio: una '
           'palabra de tu idioma no es inglés, preguntar no es responder, y '
           'una palabra rara adivinada es otra vez el casi-acierto.',

    sortEyebrow='Actividad 4 · Dónde debe ir el tiempo de estudio',
    sortTitle='Clasifica las seis costumbres',
    sortHint='Arrastra cada una a una columna &mdash; o haz clic en un '
             'elemento y luego en la columna que quieras.',
    sortBin1='Sube la nota',
    sortBin2='No hace nada, o te cuesta',

    actTitle='Montad una página del banco',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas. Coged un tema: atascos, envejecimiento, '
                  'automatización, turismo. Cinco minutos para montar una '
                  'página juntos: tres ideas y, por cada idea, dos '
                  'expresiones en lugar de dos palabras. Luego debatid el '
                  'tema durante dos minutos con las expresiones de vuestra '
                  'página.',
    actSpeak1='Cada frase de la página tiene que ser una combinación: un verbo con '
              'su sustantivo, o un adjetivo con su sustantivo. Nada de '
              'palabras sueltas.',
    actSpeak2='Tu compañero te para cada vez que buscas una palabra de '
              'contenido que no está en la página, y tienes que decirlo otra '
              'vez con una que sí esté.',
    actSpeak3='Coge una idea y dila de tres maneras: llana, formal, y como se '
              'la dirías a un amigo.',
    actWriteKind='Escritura · 150–200 palabras',
    actWriteBrief='Coge una pregunta de Task 2 y escribe el párrafo de '
                  'apertura dos veces: una repitiendo las palabras del '
                  'enunciado y otra reformulándolo de verdad. Luego subraya en '
                  'la segunda cada frase que contarías como vocabulario tuyo y '
                  'di cuántas hay.',
    actPlaceholder='Whether entry to museums should cost anything…',

    # The sort explanation; English from the data module.
    sortWhy='Los hábitos que suben la nota tratan de <strong>usar</strong> '
            'la lengua; los demás, de <strong>exhibirla</strong>. Los '
            'descriptores preguntan si sabes decir lo que quieres decir, con '
            'precisión y flexibilidad &mdash; así que una palabra que '
            'dominas vale más que una rara que falla, y una expresión '
            'aprendida entera vale más que una palabra aprendida sola. Los '
            'hábitos de exhibición parecen progreso, y ahí está la trampa.',
)


# ── French ─────────────────────────────────────────────────────────────
T['fr'] = dict(
    coverTitle='Lexical <em>Resource</em>',
    coverSub='Un quart des points en Speaking et en Writing, et les mots '
             'rares ne comptent que s’ils tombent juste',
    chipLevel='C1 · Avancé', chipFocus='Speaking &amp; Writing',
    chipCount='18 points',

    t1Eyebrow='Avant de commencer',
    t1Title='Il récompense le mot juste, pas seulement le mot rare',
    t1ah='Ce que demandent les descripteurs',
    t1ab='Un vocabulaire employé avec <strong>précision</strong> et '
         '<strong>souplesse</strong>, et des mots <em>moins courants</em> là '
         'où ils conviennent. Le choix de mots imprécis est nommé du band 8 '
         'vers le bas, les collocations aux bands 7 et 8.',
    t1an='Un raté se paie. Un vocabulaire qui ne quitte jamais les mots les '
         'plus simples aussi.',
    t1bh='Le presque-juste coûte plus cher que le mot simple',
    t1bb='Qui écrit <em>ameliorate the traffic</em> est allé chercher un '
         'verbe rare et lui a donné le mauvais complément : '
         '<em>ameliorate</em> exige quelque chose de déjà mauvais, comme les '
         'embouteillages ou des conditions. L’examinateur voit l’effort et '
         'le raté. <em>Ease congestion</em> est simple, juste, et fait le '
         'travail.',
    t1bn='Prenez le mot dont vous êtes sûr, puis allez plus loin une fois '
         'certain qu’il convient.',
    t1ch='Les expressions apprises par cœur s’entendent',
    t1cb='Les listes d’expressions « band 9 » détonnent dans la réponse qui '
         'les entoure, et les examinateurs sont formés pour l’entendre. Glissez-en '
         'une dans une réponse simple, et l’examinateur sait quelle langue est '
         'vraiment la vôtre.',
    t1cn='C’est le décalage qui trahit, pas l’expression elle-même.',

    t2Eyebrow='Avant de commencer',
    t2Title='L’unité, c’est l’association, pas le mot',
    t2ah='Le nom choisit le verbe',
    t2ab='Avec <em>research</em>, on emploie <em>conduct</em> ou <em>carry '
         'out</em> ; avec <em>a decision</em>, <em>make</em> ou '
         '<em>reach</em> ; avec <em>a conclusion</em>, <em>draw</em> ou '
         '<em>come to</em>. Aucun de ces verbes n’est rare, et aucun n’est '
         'libre : c’est le nom qui décide des verbes qu’il accepte.',
    t2an='<em>Make research</em> et <em>do a decision</em> sont parmi les '
         'ratés les plus courants.',
    t2bh='Et l’adjectif aussi',
    t2bb='<em>Heavy traffic</em>, <em>heavy rain</em>, <em>heavy losses</em>, '
         '<em>heavy fighting</em> &mdash; mais jamais <em>heavy sunshine</em>. '
         'C’est le nom qui choisit l’adjectif, et aucune règle ne prédit '
         'lequel.',
    t2bn='C’est pourquoi on les apprend en bloc, dans l’expression, plutôt que '
         'de les déduire.',
    t2ch='Notez donc l’expression, pas le mot',
    t2cb='Une entrée de carnet faite d’un mot et d’une traduction vous donne un '
         'mot que vous ne savez pas employer. Une entrée qui note l’expression '
         'où il vit vous donne quelque chose que vous pourrez dire demain.',
    t2cn='<em>Tackle congestion</em> vaut dix fois <em>congestion = [votre '
         'langue]</em>.',

    t3Eyebrow='Avant de commencer',
    t3Title='La reformulation rapporte deux fois',
    t3ah='Les deux épreuves la récompensent',
    t3ab='Le Speaking nomme la paraphrase dans ses descripteurs ; le Writing '
         'récompense la souplesse qu’elle suppose et ne crédite pas les '
         'formulations recopiées de l’énoncé. Le travail qui consiste à dire '
         'une idée de trois façons compte dans les deux salles &mdash; '
         'surtout en Partie 3 et en Task 2, où les idées sont abstraites.',
    t3an='C’est aussi ce que teste le Reading, de l’autre côté.',
    t3bh='Reformulez la question, ne la recopiez pas',
    t3bb='Les expressions recopiées de l’énoncé ne rapportent rien comme '
         'vocabulaire. Une introduction formulée avec vos propres mots '
         'montre l’étendue de votre vocabulaire ; une qui recopie la '
         'question n’en montre aucune.',
    t3bn='Changez la grammaire, pas seulement les noms : <em>should museums be '
         'free</em> devient <em>whether entry should cost anything</em>.',
    t3ch='Construisez votre réserve par idée',
    t3cb='Une réserve de vocabulaire classée par ordre alphabétique vous donne '
         'des mots. Classée par idée &mdash; congestion, vieillissement, '
         'automatisation &mdash;, chaque mot arrive avec un argument déjà '
         'attaché, et c’est justement ce qui vous manque sous la pression du '
         'temps.',
    t3cn='Dix idées avec trois expressions chacune valent mieux que cent mots '
         'sans aucune.',

    mcaEyebrow='Activité 1 · La précision, pas la rareté',
    mcaTitle='Qu’est-ce qui est vraiment noté ?',
    mcbEyebrow='Activité 2 · Les mots qui vont ensemble',
    mcbTitle='Quelle association l’anglais emploie-t-il ?',
    mccEyebrow='Activité 3 · Le dire autrement',
    mccTitle='La reformulation, et la réserve qui la nourrit',

    v1why='Un lexique moins courant employé avec <em>exactitude</em> et '
          '<em>souplesse</em>. On ne compte pas les mots rares ; on regarde '
          's’ils sont employés avec exactitude, et l’inexactitude est '
          'sanctionnée nommément.',
    v2why='<em>Ameliorate</em> exige quelque chose de déjà mauvais &mdash; '
          'des conditions, les effets, le problème. La circulation n’est pas '
          'mauvaise en soi ; les embouteillages, si. L’effort se voit, le '
          'raté aussi, et c’est en Lexical Resource qu’il se paie.',
    v3why='Le mot simple qui est exactement juste. La précision est dans le '
          'descripteur ; un synonyme de dictionnaire que l’on ne maîtrise '
          'pas est une façon courante de perdre des points en voulant en '
          'gagner.',
    v4why='Elles se détachent de l’anglais qui les entoure, et les '
          'examinateurs sont formés pour l’entendre. Une expression apprise '
          'par cœur n’est pas créditée comme votre propre langue, et une '
          'expression qui ne répond pas à la question est une erreur comme '
          'une autre.',
    v5why='<em>Conduct research</em> &mdash; ou <em>do</em> ou <em>carry out '
          'research</em>. Le nom décide des verbes qu’il accepte, et '
          '<em>make research</em> est le raté qui coûte le plus souvent, '
          'parce que son équivalent est correct dans plusieurs autres '
          'langues.',
    v6why='<em>Strong rain</em> est celle que l’anglais ne dit pas &mdash; la '
          'pluie prend <em>heavy</em>. Les preuves, les opinions et les odeurs '
          'prennent toutes <em>strong</em>, et aucune règle ne dit quel nom prend '
          'quoi.',
    v7why='Le verbe ou l’adjectif. Le nom est en général la partie que '
          'l’apprenant connaît déjà &mdash; ce qu’il faut apprendre avec lui, '
          'c’est le mot qu’il se trouve prendre.',
    v8why='Dans une expression. Un mot avec une traduction est un mot que vous '
          'reconnaissez ; un mot dans la compagnie qu’il fréquente est un mot '
          'que vous savez produire, et c’est le seul qui soit noté.',
    v9why='Elle change la grammaire autant que les mots : une question sur ce '
          'que pensent les gens devient une affirmation sur ce qui fait débat. '
          'Les trois autres mélangent l’énoncé et vous le rendent.',
    v10why='Les deux épreuves sont notées en Lexical Resource : le Speaking '
           'nomme la paraphrase explicitement, et le Writing récompense la '
           'souplesse qu’elle montre. Le même entraînement compte donc deux '
           'fois &mdash; et c’est en Partie 3 et en Task 2 qu’une paraphrase '
           'rapporte le plus.',
    v11why='Par idée. Un mot rangé sous <em>congestion</em> arrive avec un '
           'argument attaché ; un mot rangé sous C arrive seul, et sous la '
           'pression du temps, c’est un argument qui vous manque.',
    v12why='Décrivez ce qu’il fait. La reformulation est récompensée par ce '
           'critère même &mdash; un mot de votre langue n’est pas de l’anglais, '
           'demander n’est pas répondre, et un mot rare deviné, c’est encore le '
           'presque-juste.',

    sortEyebrow='Activité 4 · Où doit aller le temps de révision',
    sortTitle='Classez les six habitudes',
    sortHint='Faites glisser chacune dans une colonne &mdash; ou cliquez sur '
             'un élément, puis sur la colonne voulue.',
    sortBin1='Fait monter le band',
    sortBin2='Ne sert à rien, ou coûte des points',
    sortWhy='Les habitudes qui font monter le band consistent à '
            '<strong>employer</strong> la langue ; les autres, à '
            'l’<strong>exhiber</strong>. Les descripteurs demandent si vous '
            'savez dire ce que vous voulez dire, avec précision et souplesse '
            '&mdash; donc un mot que vous maîtrisez vaut mieux qu’un mot '
            'rare qui rate sa cible, et une expression apprise en entier '
            'vaut mieux qu’un mot appris seul. Les habitudes d’exhibition '
            'donnent l’impression de progresser : c’est là le piège.',

    actTitle='Construisez une page de la réserve',
    actUse='Utilisez-en au moins trois :',
    actSpeakBrief='À deux. Prenez un thème &mdash; congestion, '
                  'vieillissement, automatisation, tourisme. Cinq minutes '
                  'pour construire une page ensemble : trois idées, et pour '
                  'chaque idée deux expressions plutôt que deux mots. Puis '
                  'débattez du thème pendant deux minutes avec les '
                  'expressions de votre page.',
    actSpeak1='Chaque expression de la page doit être une association &mdash; un '
              'verbe avec son nom, ou un adjectif avec son nom. Pas de mots '
              'isolés.',
    actSpeak2='Votre partenaire vous arrête chaque fois que vous allez '
              'chercher un mot de contenu absent de la page, et vous devez '
              'reformuler avec un mot qui y figure.',
    actSpeak3='Prenez une idée et dites-la de trois façons : simplement, '
              'formellement, et comme vous la diriez à un ami.',
    actWriteKind='Écriture · 150–200 mots',
    actWriteBrief='Prenez une question de Task 2 et écrivez le premier '
                  'paragraphe deux fois : une fois en répétant les mots de la '
                  'question, une fois en la reformulant correctement. Puis '
                  'soulignez dans le second chaque expression que vous '
                  'compteriez comme votre propre vocabulaire, et dites combien il '
                  'y en a.',
    actPlaceholder='Whether entry to museums should cost anything…',
)


# ── Italian ────────────────────────────────────────────────────────────
T['it'] = dict(
    coverTitle='Lexical <em>Resource</em>',
    coverSub='Un quarto dei punti in Speaking e in Writing, e le parole rare '
             'contano solo quando vanno a segno',
    chipLevel='C1 · Avanzato', chipFocus='Speaking e Writing',
    chipCount='18 punti',

    t1Eyebrow='Prima di cominciare',
    t1Title='Premia la parola giusta, non solo quella rara',
    t1ah='Che cosa chiedono i descrittori',
    t1ab='Un lessico usato con <strong>precisione</strong> e '
         '<strong>flessibilità</strong>, e parole <em>meno comuni</em> dove '
         'calzano. La scelta imprecisa delle parole è nominata dal band 8 in '
         'giù, le collocazioni ai band 7 e 8.',
    t1an='Un errore si paga. Anche un lessico che non esce mai dalle parole '
         'più semplici.',
    t1bh='Il quasi giusto costa più della parola semplice',
    t1bb='Chi scrive <em>ameliorate the traffic</em> è andato a cercare un '
         'verbo raro e gli ha dato l’oggetto sbagliato: <em>ameliorate</em> '
         'vuole qualcosa che è già negativo, come gli ingorghi o certe '
         'condizioni. L’esaminatore vede lo sforzo e l’errore. <em>Ease '
         'congestion</em> è semplice, giusto e fa il suo lavoro.',
    t1bn='Scegli la parola di cui sei sicuro, e osa solo quando sei certo che '
         'calza.',
    t1ch='Le frasi imparate a memoria si sentono',
    t1cb='Gli elenchi di frasi «da band 9» stonano con la risposta intorno, e gli '
         'esaminatori sono addestrati a sentirlo. Infilane una in una risposta '
         'semplice e l’esaminatore capisce qual è davvero la tua lingua.',
    t1cn='A tradirla è lo scarto, non la frase in sé.',

    t2Eyebrow='Prima di cominciare',
    t2Title='L’unità è la combinazione, non la parola',
    t2ah='Il nome sceglie il verbo',
    t2ab='Con <em>research</em> vanno <em>conduct</em> o <em>carry out</em>; '
         'con <em>a decision</em>, <em>make</em> o <em>reach</em>; con <em>a '
         'conclusion</em>, <em>draw</em> o <em>come to</em>. Nessuno di '
         'questi verbi è raro, e nessuno è libero: è il nome a decidere '
         'quali verbi accetta.',
    t2an='<em>Make research</em> e <em>do a decision</em> sono tra gli '
         'errori più comuni.',
    t2bh='E anche l’aggettivo',
    t2bb='<em>Heavy traffic</em>, <em>heavy rain</em>, <em>heavy losses</em>, '
         '<em>heavy fighting</em> &mdash; ma mai <em>heavy sunshine</em>. '
         'L’aggettivo lo sceglie il nome, e nessuna regola dice quale.',
    t2bn='Per questo si imparano interi, nella frase, invece di ricavarli.',
    t2ch='Quindi scrivi la frase, non la parola',
    t2cb='Una voce di quaderno fatta di una parola e una traduzione ti dà una '
         'parola che non sai usare. Una voce con la frase in cui vive ti dà '
         'qualcosa che potrai dire domani.',
    t2cn='<em>Tackle congestion</em> vale dieci volte <em>congestion = [la tua '
         'lingua]</em>.',

    t3Eyebrow='Prima di cominciare',
    t3Title='La riformulazione paga due volte',
    t3ah='Entrambe le prove la premiano',
    t3ab='Lo Speaking nomina la parafrasi nei suoi descrittori; il Writing '
         'premia la flessibilità che c’è dietro e non dà credito alle '
         'formulazioni copiate dalla traccia. Il lavoro di dire un’idea in '
         'tre modi conta in entrambe le aule &mdash; soprattutto nella Parte '
         '3 e nella Task 2, dove le idee sono astratte.',
    t3an='È anche ciò che il Reading verifica, dall’altra parte.',
    t3bh='Riformula la domanda, non copiarla',
    t3bb='Le espressioni copiate dalla traccia non valgono nulla come '
         'lessico. Un’introduzione con parole tue mostra varietà; una che '
         'copia la domanda non ne mostra alcuna.',
    t3bn='Cambia la grammatica, non solo i nomi: <em>should museums be free</em> '
         'diventa <em>whether entry should cost anything</em>.',
    t3ch='Costruisci la tua banca per idee',
    t3cb='Una banca di vocaboli in ordine alfabetico ti dà parole. Ordinata per '
         'idee &mdash; congestione, invecchiamento, automazione &mdash; ogni '
         'parola arriva con un argomento già attaccato, ed è proprio ciò che ti '
         'manca sotto pressione.',
    t3cn='Dieci idee con tre espressioni ciascuna battono cento parole senza '
         'nessuna.',

    mcaEyebrow='Attività 1 · Precisione, non rarità',
    mcaTitle='Che cosa viene valutato davvero?',
    mcbEyebrow='Attività 2 · Parole che viaggiano insieme',
    mcbTitle='Quale combinazione usa l’inglese?',
    mccEyebrow='Attività 3 · Dirlo in un altro modo',
    mccTitle='La riformulazione, e la banca che la sostiene',

    v1why='Lessico meno comune usato con <em>precisione</em> e '
          '<em>flessibilità</em>. Non si conta quante parole rare ci sono, '
          'ma se sono usate con precisione, e l’imprecisione è penalizzata '
          'espressamente.',
    v2why='<em>Ameliorate</em> vuole qualcosa che è già negativo &mdash; '
          'delle condizioni, gli effetti, il problema. Il traffico in sé non '
          'è negativo; gli ingorghi sì. Lo sforzo si vede e l’errore pure, '
          'ed è in Lexical Resource che si paga.',
    v3why='La parola semplice che è esattamente giusta. La precisione è nel '
          'descrittore; un sinonimo da dizionario che non si padroneggia è '
          'un modo comune di perdere punti cercando di guadagnarne.',
    v4why='Si staccano dall’inglese che le circonda, e gli esaminatori sono '
          'formati per sentirlo. Una frase imparata a memoria non viene '
          'accreditata come lingua tua, e una che non risponde alla domanda '
          'è un errore come un altro.',
    v5why='<em>Conduct research</em> &mdash; oppure <em>do</em> o <em>carry '
          'out research</em>. È il nome a decidere quali verbi accetta, e '
          '<em>make research</em> è l’errore che costa più spesso, perché il '
          'suo equivalente è corretto in diverse altre lingue.',
    v6why='<em>Strong rain</em> è quella che l’inglese non dice &mdash; la '
          'pioggia vuole <em>heavy</em>. Prove, opinioni e odori vogliono tutti '
          '<em>strong</em>, e nessuna regola dice quale nome prende quale.',
    v7why='Il verbo o l’aggettivo. Il nome di solito è la parte che chi impara '
          'conosce già &mdash; ciò che va imparato con lui è la parola che '
          'capita a prendere.',
    v8why='In una frase. Una parola con una traduzione è una parola che '
          'riconosci; una parola in compagnia delle parole con cui sta è una '
          'parola che sai produrre, ed è l’unica che viene valutata.',
    v9why='Cambia la grammatica oltre alle parole: una domanda su ciò che la '
          'gente pensa diventa un’affermazione su ciò che è in discussione. Le '
          'altre tre rimescolano la traccia e te la restituiscono.',
    v10why='Entrambe le prove sono valutate su Lexical Resource: lo Speaking '
           'nomina la parafrasi espressamente, e il Writing premia la '
           'flessibilità che dimostra. Lo stesso esercizio conta quindi due '
           'volte &mdash; e la Parte 3 e la Task 2 sono dove una parafrasi '
           'rende di più.',
    v11why='Per idee. Una parola archiviata sotto <em>congestion</em> arriva '
           'con un argomento attaccato; una parola archiviata sotto la C arriva '
           'da sola, e sotto pressione è un argomento quello che ti manca.',
    v12why='Descrivi che cosa fa. La riformulazione è premiata proprio da questo '
           'criterio &mdash; una parola della tua lingua non è inglese, chiedere '
           'non è rispondere, e una parola rara tirata a indovinare è di nuovo il '
           'quasi giusto.',

    sortEyebrow='Attività 4 · Dove deve andare il tempo di ripasso',
    sortTitle='Classifica le sei abitudini',
    sortHint='Trascina ciascuna in una colonna &mdash; oppure clicca su un '
             'elemento e poi sulla colonna che vuoi.',
    sortBin1='Fa salire il band',
    sortBin2='Non serve, o costa punti',
    sortWhy='Le abitudini che fanno salire il band riguardano '
            'l’<strong>uso</strong> della lingua; le altre la sua '
            '<strong>esibizione</strong>. I descrittori chiedono se sai dire '
            'quello che intendi, con precisione e flessibilità &mdash; '
            'quindi una parola che padroneggi batte una rara che manca il '
            'bersaglio, e un’espressione imparata intera batte una parola '
            'imparata da sola. Le abitudini di esibizione danno '
            'l’impressione di fare progressi: è quella la trappola.',

    actTitle='Costruisci una pagina della banca',
    actUse='Usane almeno tre:',
    actSpeakBrief='In coppia. Prendete un tema &mdash; congestione, '
                  'invecchiamento, automazione, turismo. Cinque minuti per '
                  'costruire insieme una pagina: tre idee, e per ogni idea '
                  'due espressioni invece di due parole. Poi discutete il '
                  'tema per due minuti con le espressioni della vostra '
                  'pagina.',
    actSpeak1='Ogni espressione sulla pagina deve essere una combinazione &mdash; '
              'un verbo con il suo nome, o un aggettivo con il suo nome. Niente '
              'parole isolate.',
    actSpeak2='Il tuo compagno ti ferma ogni volta che cerchi una parola di '
              'contenuto che non è sulla pagina, e devi ridirlo usandone una '
              'che c’è.',
    actSpeak3='Prendi un’idea e dilla in tre modi: in modo semplice, formale, e '
              'come la diresti a un amico.',
    actWriteKind='Scrittura · 150–200 parole',
    actWriteBrief='Prendi una domanda di Task 2 e scrivi il primo paragrafo due '
                  'volte: una ripetendo le parole della domanda, una '
                  'riformulandola come si deve. Poi sottolinea nel secondo ogni '
                  'espressione che conteresti come tuo vocabolario, e di’ quante '
                  'sono.',
    actPlaceholder='Whether entry to museums should cost anything…',
)


# ── Portuguese ─────────────────────────────────────────────────────────
T['pt'] = dict(
    coverTitle='Lexical <em>Resource</em>',
    coverSub='Um quarto da nota em Speaking e em Writing, e as palavras '
             'raras só contam quando acertam',
    chipLevel='C1 · Avançado', chipFocus='Speaking e Writing',
    chipCount='18 pontos',

    t1Eyebrow='Antes de começar',
    t1Title='Premeia a palavra certa, não só a rara',
    t1ah='O que pedem os descritores',
    t1ab='Um vocabulário usado com <strong>precisão</strong> e '
         '<strong>flexibilidade</strong>, e palavras <em>menos comuns</em> '
         'onde encaixam. A escolha imprecisa de palavras é referida do band '
         '8 para baixo, e as colocações nos bands 7 e 8.',
    t1an='Um erro paga-se. Um vocabulário que nunca sai das palavras mais '
         'simples também.',
    t1bh='O quase certo custa mais do que a palavra simples',
    t1bb='Quem escreve <em>ameliorate the traffic</em> foi buscar um verbo '
         'raro e deu-lhe o complemento errado: <em>ameliorate</em> pede algo '
         'que já é mau, como os engarrafamentos ou certas condições. O '
         'examinador vê o esforço e o erro. <em>Ease congestion</em> é '
         'simples, certo e faz o trabalho.',
    t1bn='Usa a palavra de que tens a certeza e só arrisca quando souberes que '
         'encaixa.',
    t1ch='As expressões decoradas ouvem-se',
    t1cb='As listas de expressões «de band 9» destoam da resposta à volta, e os '
         'examinadores são treinados para dar por isso. Mete uma numa resposta '
         'simples e o examinador percebe qual é realmente a tua língua.',
    t1cn='É o contraste que denuncia, não a expressão em si.',

    t2Eyebrow='Antes de começar',
    t2Title='A unidade é a combinação, não a palavra',
    t2ah='O nome escolhe o verbo',
    t2ab='Com <em>research</em> vão <em>conduct</em> ou <em>carry out</em>; '
         'com <em>a decision</em>, <em>make</em> ou <em>reach</em>; com '
         '<em>a conclusion</em>, <em>draw</em> ou <em>come to</em>. Nenhum '
         'destes verbos é raro, e nenhum é livre: é o nome que decide que '
         'verbos aceita.',
    t2an='<em>Make research</em> e <em>do a decision</em> estão entre os '
         'erros mais comuns.',
    t2bh='E o adjetivo também',
    t2bb='<em>Heavy traffic</em>, <em>heavy rain</em>, <em>heavy losses</em>, '
         '<em>heavy fighting</em> &mdash; mas nunca <em>heavy sunshine</em>. É o '
         'nome que escolhe o adjetivo, e nenhuma regra prevê qual.',
    t2bn='Por isso aprendem-se inteiros, na expressão, em vez de se deduzirem.',
    t2ch='Por isso escreve a expressão, não a palavra',
    t2cb='Uma entrada no caderno com uma palavra e uma tradução dá-te uma '
         'palavra que não sabes usar. Uma entrada com a expressão em que ela vive '
         'dá-te uma coisa que podes dizer amanhã.',
    t2cn='<em>Tackle congestion</em> vale dez vezes mais do que <em>congestion '
         '= [a tua língua]</em>.',

    t3Eyebrow='Antes de começar',
    t3Title='A paráfrase compensa duas vezes',
    t3ah='As duas provas premeiam-na',
    t3ab='O Speaking refere a paráfrase nos seus descritores; o Writing '
         'premeia a flexibilidade que está por trás dela e não dá crédito às '
         'formulações copiadas do enunciado. O trabalho de dizer uma ideia '
         'de três maneiras conta nas duas salas &mdash; sobretudo na Parte 3 '
         'e na Task 2, onde as ideias são abstratas.',
    t3an='É também o que o Reading testa, do outro lado.',
    t3bh='Reformula a pergunta, não a copies',
    t3bb='As expressões copiadas do enunciado não valem nada como '
         'vocabulário. Uma introdução com as tuas próprias palavras mostra '
         'variedade; uma que copia a pergunta não mostra nenhuma.',
    t3bn='Muda a gramática, não só os nomes: <em>should museums be free</em> '
         'passa a <em>whether entry should cost anything</em>.',
    t3ch='Constrói o teu banco por ideias',
    t3cb='Um banco de vocabulário por ordem alfabética dá-te palavras. '
         'Organizado por ideias &mdash; congestionamento, envelhecimento, '
         'automação &mdash;, cada palavra chega com um argumento já agarrado, que '
         'é o que te falta quando o tempo aperta.',
    t3cn='Dez ideias com três expressões cada valem mais do que cem palavras '
         'sem nenhuma.',

    mcaEyebrow='Atividade 1 · Precisão, não raridade',
    mcaTitle='O que é que está realmente a ser avaliado?',
    mcbEyebrow='Atividade 2 · Palavras que andam juntas',
    mcbTitle='Que combinação usa o inglês?',
    mccEyebrow='Atividade 3 · Dizê-lo de outra maneira',
    mccTitle='A paráfrase, e o banco por trás dela',

    v1why='Léxico menos comum usado com <em>exatidão</em> e '
          '<em>flexibilidade</em>. Não se conta quantas palavras raras há, '
          'mas sim se são usadas com exatidão, e a inexatidão é penalizada '
          'expressamente.',
    v2why='<em>Ameliorate</em> pede algo que já é mau &mdash; condições, os '
          'efeitos, o problema. O trânsito não é mau em si; os '
          'engarrafamentos são. O esforço vê-se e o erro também, e é em '
          'Lexical Resource que se paga.',
    v3why='A palavra simples que é exatamente a certa. A precisão é o '
          'descritor; um sinónimo de dicionário que não se domina é uma '
          'forma comum de perder pontos a tentar ganhá-los.',
    v4why='Destacam-se do inglês à sua volta, e os examinadores são '
          'treinados para ouvir isso. Uma expressão decorada não é creditada '
          'como língua tua, e uma que não responde à pergunta é um erro como '
          'outro qualquer.',
    v5why='<em>Conduct research</em> &mdash; ou <em>do</em> ou <em>carry out '
          'research</em>. É o nome que decide que verbos aceita, e <em>make '
          'research</em> é o erro que mais custa, porque o seu equivalente '
          'está correto em várias outras línguas.',
    v6why='<em>Strong rain</em> é a que o inglês não diz &mdash; a chuva leva '
          '<em>heavy</em>. Provas, opiniões e cheiros levam todos '
          '<em>strong</em>, e nenhuma regra diz que nome leva qual.',
    v7why='O verbo ou o adjetivo. O nome é normalmente a parte que quem aprende '
          'já conhece &mdash; o que é preciso aprender com ele é a palavra que '
          'por acaso o acompanha.',
    v8why='Numa expressão. Uma palavra com uma tradução é uma palavra que '
          'reconheces; uma palavra com a companhia que lhe é própria é uma '
          'palavra que consegues produzir, e só essa é avaliada.',
    v9why='Muda a gramática, além das palavras: uma pergunta sobre o que as '
          'pessoas pensam passa a ser uma afirmação sobre o que está em '
          'discussão. As outras três baralham o enunciado e devolvem-to.',
    v10why='As duas provas são avaliadas em Lexical Resource: o Speaking '
           'refere a paráfrase expressamente, e o Writing premeia a '
           'flexibilidade que ela mostra. O mesmo treino conta, portanto, '
           'duas vezes &mdash; e a Parte 3 e a Task 2 são onde uma paráfrase '
           'rende mais.',
    v11why='Por ideias. Uma palavra arquivada em <em>congestion</em> chega com '
           'um argumento agarrado; uma palavra arquivada na letra C chega '
           'sozinha, e quando o tempo aperta é de um argumento que precisas.',
    v12why='Descreve o que faz. A paráfrase é premiada por este mesmo critério '
           '&mdash; uma palavra da tua língua não é inglês, perguntar não é '
           'responder, e uma palavra rara adivinhada é outra vez o quase certo.',

    sortEyebrow='Atividade 4 · Para onde deve ir o tempo de revisão',
    sortTitle='Classifica os seis hábitos',
    sortHint='Arrasta cada um para uma coluna &mdash; ou clica num elemento e '
             'depois na coluna que quiseres.',
    sortBin1='Faz subir o band',
    sortBin2='Não adianta, ou custa pontos',
    sortWhy='Os hábitos que fazem subir o band têm a ver com '
            '<strong>usar</strong> a língua; os outros, com '
            '<strong>exibi-la</strong>. Os descritores perguntam se '
            'consegues dizer o que queres dizer, com precisão e '
            'flexibilidade &mdash; por isso, uma palavra que dominas vale '
            'mais do que uma rara que falha, e uma expressão aprendida '
            'inteira vale mais do que uma palavra aprendida sozinha. Os '
            'hábitos de exibição dão a sensação de progresso, e é aí que '
            'está a armadilha.',

    actTitle='Constrói uma página do banco',
    actUse='Usa pelo menos três:',
    actSpeakBrief='Em pares. Escolham um tema &mdash; congestionamento, '
                  'envelhecimento, automação, turismo. Cinco minutos para '
                  'construírem juntos uma página: três ideias e, para cada '
                  'uma, duas expressões em vez de duas palavras. Depois '
                  'discutam o tema durante dois minutos com as expressões da '
                  'vossa página.',
    actSpeak1='Cada expressão da página tem de ser uma combinação &mdash; um '
              'verbo com o seu nome, ou um adjetivo com o seu nome. Nada de '
              'palavras soltas.',
    actSpeak2='O teu colega interrompe-te sempre que fores buscar uma '
              'palavra de conteúdo que não está na página, e tens de o dizer '
              'outra vez com uma que lá esteja.',
    actSpeak3='Pega numa ideia e di-la de três maneiras: de forma simples, de '
              'forma formal e como a dirias a um amigo.',
    actWriteKind='Escrita · 150–200 palavras',
    actWriteBrief='Pega numa pergunta de Task 2 e escreve o primeiro parágrafo '
                  'duas vezes: uma a repetir as palavras da pergunta, outra a '
                  'reformulá-la como deve ser. Depois sublinha no segundo cada '
                  'expressão que contarias como vocabulário teu, e diz quantas '
                  'são.',
    actPlaceholder='Whether entry to museums should cost anything…',
)


# ── Russian ────────────────────────────────────────────────────────────
T['ru'] = dict(
    coverTitle='Lexical <em>Resource</em>',
    coverSub='Четверть баллов в Speaking и в Writing, и редкие слова '
             'засчитываются, только когда попадают в цель',
    chipLevel='C1 · Продвинутый', chipFocus='Speaking и Writing',
    chipCount='18 баллов',

    t1Eyebrow='Прежде чем начать',
    t1Title='Вознаграждается точное слово, а не просто редкое',
    t1ah='Чего требуют дескрипторы',
    t1ab='Словарный запас, которым пользуются <strong>точно</strong> и '
         '<strong>гибко</strong>, и <em>менее распространённые</em> слова '
         'там, где они уместны. Неточный выбор слов упоминается начиная с '
         'band 8 и ниже, а сочетаемость &mdash; на band 7 и 8.',
    t1an='Промах наказывается. Как и запас, который никогда не выходит за '
         'пределы самых простых слов.',
    t1bh='Почти-попадание обходится дороже простого слова',
    t1bb='Кандидат, который пишет <em>ameliorate the traffic</em>, потянулся '
         'за редким глаголом и дал ему не то дополнение: <em>ameliorate</em> '
         'требует чего-то уже плохого, например пробок или условий. '
         'Экзаменатор видит и попытку, и промах. <em>Ease congestion</em> '
         '&mdash; просто, правильно и работает.',
    t1bn='Берите слово, в котором уверены, а тянитесь дальше, только когда '
         'знаете, что оно подходит.',
    t1ch='Заученные фразы слышно',
    t1cb='Фразы из списков «на band 9» выбиваются из ответа вокруг них, и '
         'экзаменаторов учат это слышать. Вставьте такую фразу в простой ответ, и '
         'экзаменатор поймёт, какой язык на самом деле ваш.',
    t1cn='Выдаёт несоответствие, а не сама фраза.',

    t2Eyebrow='Прежде чем начать',
    t2Title='Единица &mdash; сочетание, а не слово',
    t2ah='Существительное выбирает глагол',
    t2ab='С <em>research</em> сочетаются <em>conduct</em> или <em>carry '
         'out</em>, с <em>a decision</em> &mdash; <em>make</em> или '
         '<em>reach</em>, с <em>a conclusion</em> &mdash; <em>draw</em> или '
         '<em>come to</em>. Ни один из этих глаголов не редкий, и ни один не '
         'свободен: существительное само решает, какие глаголы оно принимает.',
    t2an='<em>Make research</em> и <em>do a decision</em> &mdash; одни из '
         'самых частых промахов.',
    t2bh='И прилагательное тоже',
    t2bb='<em>Heavy traffic</em>, <em>heavy rain</em>, <em>heavy losses</em>, '
         '<em>heavy fighting</em> &mdash; но никогда <em>heavy sunshine</em>. '
         'Прилагательное выбирает существительное, и никакое правило не '
         'предскажет какое.',
    t2bn='Поэтому их учат целиком, во фразе, а не выводят.',
    t2ch='Поэтому записывайте фразу, а не слово',
    t2cb='Запись в тетради «слово плюс перевод» даёт вам слово, которым вы не '
         'умеете пользоваться. Запись фразы, в которой оно живёт, даёт то, что '
         'вы сможете сказать завтра.',
    t2cn='<em>Tackle congestion</em> стоит в десять раз больше, чем '
         '<em>congestion = [ваш язык]</em>.',

    t3Eyebrow='Прежде чем начать',
    t3Title='Перефразирование окупается дважды',
    t3ah='Оба экзамена её вознаграждают',
    t3ab='Speaking прямо называет перефразирование в своих дескрипторах; '
         'Writing вознаграждает стоящую за ним гибкость и не засчитывает '
         'формулировки, списанные из задания. Работа над тем, чтобы сказать '
         'одну мысль тремя способами, засчитывается в обеих аудиториях '
         '&mdash; прежде всего в части 3 и в Task 2, где идеи абстрактны.',
    t3an='Это же проверяет и Reading, только с другой стороны.',
    t3bh='Перефразируйте вопрос, а не копируйте его',
    t3bb='Выражения, списанные из задания, ничего не дают как словарный '
         'запас. Вступление своими словами показывает диапазон; вступление, '
         'повторяющее вопрос, не показывает никакого.',
    t3bn='Меняйте грамматику, а не только существительные: <em>should museums '
         'be free</em> превращается в <em>whether entry should cost '
         'anything</em>.',
    t3ch='Собирайте запас по идеям',
    t3cb='Словарный запас по алфавиту даёт вам слова. Собранный по идеям '
         '&mdash; пробки, старение, автоматизация, &mdash; он приносит каждое '
         'слово вместе с готовым аргументом, а именно аргументов не хватает, '
         'когда время поджимает.',
    t3cn='Десять идей по три фразы лучше ста слов без единой.',

    mcaEyebrow='Задание 1 · Точность, а не редкость',
    mcaTitle='Что на самом деле оценивается?',
    mcbEyebrow='Задание 2 · Слова, которые ходят парами',
    mcbTitle='Какое сочетание говорят по-английски?',
    mccEyebrow='Задание 3 · Сказать по-другому',
    mccTitle='Перефразирование и запас за ним',

    v1why='Менее распространённая лексика, используемая <em>точно</em> и '
          '<em>гибко</em>. Редкие слова не подсчитывают; смотрят, точно ли '
          'они употреблены, а неточность прямо наказывается.',
    v2why='<em>Ameliorate</em> требует чего-то уже плохого &mdash; условий, '
          'последствий, проблемы. Движение само по себе не плохо, а пробки '
          '&mdash; да. Попытка видна, и промах тоже, и засчитывается он в '
          'Lexical Resource.',
    v3why='Простое слово, которое точно подходит. Точность &mdash; это '
          'дескриптор; синоним из словаря, которым вы не владеете, &mdash; '
          'частый способ потерять баллы, пытаясь их заработать.',
    v4why='Они выбиваются из английского вокруг них, и экзаменаторов учат '
          'это слышать. Заученную фразу не засчитывают как ваш собственный '
          'язык, а фраза, которая не отвечает на вопрос, &mdash; такая же '
          'ошибка, как любая другая.',
    v5why='<em>Conduct research</em> &mdash; или <em>do</em>, или <em>carry '
          'out research</em>. Существительное само решает, какие глаголы оно '
          'принимает, а <em>make research</em> &mdash; промах, который '
          'обходится дороже всего, потому что его аналог правилен в '
          'нескольких других языках.',
    v6why='<em>Strong rain</em> &mdash; этого английский не говорит: дождь '
          'требует <em>heavy</em>. Доказательства, мнения и запахи &mdash; все '
          'с <em>strong</em>, и никакое правило не скажет, какое '
          'существительное берёт какое слово.',
    v7why='Глагол или прилагательное. Существительное учащийся обычно уже знает '
          '&mdash; учить вместе с ним нужно то слово, которое с ним сочетается.',
    v8why='Во фразе. Слово с переводом &mdash; это слово, которое вы узнаёте; '
          'слово в привычном окружении &mdash; то, которое вы можете произвести, '
          'а оценивается только такое.',
    v9why='Он меняет не только слова, но и грамматику: вопрос о том, что думают '
          'люди, становится утверждением о том, что спорно. Остальные три лишь '
          'перетасовывают задание и возвращают его вам.',
    v10why='Оба экзамена оцениваются по Lexical Resource: Speaking прямо '
           'называет перефразирование, а Writing вознаграждает гибкость, '
           'которую оно показывает. Значит, одна и та же тренировка '
           'засчитывается дважды &mdash; а больше всего перефразирование '
           'даёт в части 3 и в Task 2.',
    v11why='По идеям. Слово в папке <em>congestion</em> приходит с готовым '
           'аргументом; слово на букву C приходит одно, а под давлением времени '
           'не хватает именно аргумента.',
    v12why='Опишите, что оно делает. Перефразирование поощряется именно этим '
           'критерием &mdash; слово из родного языка &mdash; не английский, '
           'спросить &mdash; не значит ответить, а угаданное редкое слово '
           '&mdash; снова почти-попадание.',

    sortEyebrow='Задание 4 · На что тратить время подготовки',
    sortTitle='Распределите шесть привычек',
    sortHint='Перетащите каждую в столбец &mdash; или нажмите на неё, а затем '
             'на нужный столбец.',
    sortBin1='Повышает балл',
    sortBin2='Ничего не даёт или стоит баллов',
    sortWhy='Привычки, которые повышают балл, &mdash; о том, чтобы '
            '<strong>пользоваться</strong> языком; остальные &mdash; о том, '
            'чтобы его <strong>демонстрировать</strong>. Дескрипторы '
            'спрашивают, можете ли вы точно и гибко сказать то, что имеете в '
            'виду, &mdash; поэтому слово, которым вы владеете, лучше '
            'редкого, которое промахивается, а выражение, выученное целиком, '
            'лучше слова, выученного отдельно. Привычки-демонстрации создают '
            'ощущение прогресса, и в этом ловушка.',

    actTitle='Соберите одну страницу запаса',
    actUse='Используйте хотя бы три:',
    actSpeakBrief='В парах. Возьмите тему &mdash; пробки, старение, '
                  'автоматизация, туризм. Пять минут, чтобы вместе собрать '
                  'страницу: три идеи и к каждой две фразы, а не два слова. '
                  'Потом две минуты обсуждайте тему, используя фразы со '
                  'своей страницы.',
    actSpeak1='Каждая фраза на странице должна быть сочетанием &mdash; глагол со '
              'своим существительным или прилагательное со своим '
              'существительным. Никаких отдельных слов.',
    actSpeak2='Партнёр останавливает вас каждый раз, когда вы тянетесь за '
              'знаменательным словом, которого нет на странице, и вы должны '
              'сказать это снова с тем, что там есть.',
    actSpeak3='Возьмите одну идею и скажите её тремя способами: просто, '
              'официально и так, как сказали бы другу.',
    actWriteKind='Письмо · 150–200 слов',
    actWriteBrief='Возьмите вопрос Task 2 и напишите первый абзац дважды: один '
                  'раз повторяя слова вопроса, другой &mdash; перефразировав его '
                  'как следует. Затем подчеркните во втором каждую фразу, которую '
                  'вы засчитали бы как свою лексику, и скажите, сколько их.',
    actPlaceholder='Whether entry to museums should cost anything…',
)


# ── Arabic ─────────────────────────────────────────────────────────────
T['ar'] = dict(
    coverTitle='Lexical <em>Resource</em>',
    coverSub='ربع الدرجات في Speaking وفي Writing، والكلمات النادرة لا '
             'تُحتسب إلا حين تصيب',
    chipLevel='C1 · متقدّم', chipFocus='Speaking وWriting',
    chipCount='18 نقطة',

    t1Eyebrow='قبل أن تبدأ',
    t1Title='يكافئ الكلمة الصحيحة، لا النادرة وحدها',
    t1ah='ما تطلبه معايير التقييم',
    t1ab='مفردات تُستخدم <strong>بدقة</strong> و<strong>مرونة</strong>، '
         'وكلمات <em>أقل شيوعًا</em> حيث تناسب. واختيار الكلمة غير الدقيق '
         'مذكور من band 8 نزولًا، والتلازم اللفظي في band 7 و8.',
    t1an='الإخفاق يُحسب عليك، وكذلك الحصيلة التي لا تتجاوز أبسط الكلمات.',
    t1bh='شبه الإصابة يكلّف أكثر من الكلمة البسيطة',
    t1bb='من يكتب <em>ameliorate the traffic</em> قد مدّ يده إلى فعل نادر '
         'وأعطاه المفعول الخطأ: فـ<em>ameliorate</em> تحتاج إلى شيء سيئ '
         'أصلًا، كالازدحام أو الظروف. يرى الممتحن المحاولة ويرى الإخفاق. أما '
         '<em>ease congestion</em> فبسيطة وصحيحة وتؤدي الغرض.',
    t1bn='استخدم الكلمة التي أنت واثق منها، ولا تتوسّع إلا حين تتأكد أنها '
         'تناسب.',
    t1ch='العبارات المحفوظة تُسمَع',
    t1cb='قوائم عبارات «band 9» تنفصل عن الإجابة من حولها، والممتحنون مدرَّبون '
         'على سماع ذلك تحديدًا. ضع واحدة منها في إجابة بسيطة، فيعرف الممتحن أيّ '
         'لغة هي لغتك حقًّا.',
    t1cn='ما يفضحها هو عدم الانسجام، لا العبارة نفسها.',

    t2Eyebrow='قبل أن تبدأ',
    t2Title='الوحدة هي التلازم، لا الكلمة',
    t2ah='الاسم يختار الفعل',
    t2ab='مع <em>research</em> يأتي <em>conduct</em> أو <em>carry out</em>، '
         'ومع <em>a decision</em> يأتي <em>make</em> أو <em>reach</em>، ومع '
         '<em>a conclusion</em> يأتي <em>draw</em> أو <em>come to</em>. لا '
         'فعل منها نادر، ولا فعل منها حرّ: الاسم هو الذي يقرر أي الأفعال '
         'يقبل.',
    t2an='عبارتا <em>make research</em> و<em>do a decision</em> من أشيع '
         'الأخطاء.',
    t2bh='والصفة كذلك',
    t2bb='نقول <em>heavy traffic</em> و<em>heavy rain</em> و<em>heavy '
         'losses</em> و<em>heavy fighting</em>، لكن لا نقول أبدًا <em>heavy '
         'sunshine</em>. الاسم هو الذي يختار الصفة، ولا قاعدة تتنبّأ بأيّها.',
    t2bn='ولهذا تُتعلَّم كاملةً داخل العبارة، لا تُستنتَج.',
    t2ch='فاكتب العبارة لا الكلمة',
    t2cb='مدخل في دفترك من كلمة وترجمة يعطيك كلمة لا تعرف كيف تستخدمها. أما '
         'مدخل يسجّل العبارة التي تعيش فيها فيعطيك شيئًا تستطيع قوله غدًا.',
    t2cn='عبارة <em>tackle congestion</em> تساوي عشرة أضعاف <em>congestion = '
         '[لغتك]</em>.',

    t3Eyebrow='قبل أن تبدأ',
    t3Title='إعادة الصياغة تُكافَأ مرتين',
    t3ah='الاختباران كلاهما يكافئانها',
    t3ab='تذكر معايير Speaking إعادة الصياغة صراحةً، ويكافئ Writing المرونة '
         'التي وراءها ولا يحتسب الصياغات المنقولة من نص السؤال. والعمل على '
         'قول فكرة واحدة بثلاث طرق يُحتسب في القاعتين &mdash; ولا سيما في '
         'الجزء 3 وفي Task 2، حيث الأفكار مجرّدة.',
    t3an='وهو أيضًا ما يختبره Reading، من الجهة الأخرى.',
    t3bh='أعد صياغة السؤال ولا تنسخه',
    t3bb='العبارات المنقولة من نص السؤال لا تُحتسب مفرداتٍ لك. المقدمة '
         'المكتوبة بكلماتك تُظهر تنوّعك، والمقدمة التي تنسخ السؤال لا تُظهر '
         'شيئًا.',
    t3bn='غيّر القواعد لا الأسماء فقط: <em>should museums be free</em> تصبح '
         '<em>whether entry should cost anything</em>.',
    t3ch='ابنِ رصيدك بحسب الفكرة',
    t3cb='رصيد مفردات مرتّب أبجديًّا يعطيك كلمات. أما إذا رُتّب بحسب الفكرة، '
         'كالازدحام والشيخوخة والأتمتة، فكل كلمة تأتي ومعها حجّة جاهزة، وهذا '
         'بالضبط ما ينقصك تحت ضغط الوقت.',
    t3cn='عشر أفكار في كل منها ثلاث عبارات خير من مئة كلمة بلا عبارة واحدة.',

    mcaEyebrow='النشاط 1 · الدقة لا الندرة',
    mcaTitle='ما الذي يُقيَّم فعلًا؟',
    mcbEyebrow='النشاط 2 · كلمات تسير معًا',
    mcbTitle='أيّ تلازم تستخدمه الإنجليزية؟',
    mccEyebrow='النشاط 3 · قُلها بطريقة أخرى',
    mccTitle='إعادة الصياغة والرصيد الذي وراءها',

    v1why='مفردات أقل شيوعًا تُستخدم <em>بدقة</em> و<em>مرونة</em>. لا يُعدّ '
          'عدد الكلمات النادرة، بل يُنظر هل استُخدمت بدقة، وعدم الدقة '
          'يُعاقَب عليه صراحةً.',
    v2why='الفعل <em>ameliorate</em> يحتاج إلى شيء سيئ أصلًا &mdash; الظروف، '
          'أو الآثار، أو المشكلة. حركة المرور ليست سيئة في ذاتها، أما '
          'الازدحام فسيئ. المحاولة ظاهرة والإخفاق ظاهر، ويُحتسب ذلك في '
          'Lexical Resource.',
    v3why='الكلمة البسيطة الصحيحة تمامًا. الدقة هي المعيار، والمرادف المأخوذ '
          'من قاموس المرادفات الذي لا يتقنه الكاتب طريقة شائعة لخسارة '
          'الدرجات في أثناء محاولة كسبها.',
    v4why='تنفصل عن الإنجليزية المحيطة بها، والممتحنون مدرَّبون على سماع '
          'ذلك. العبارة المحفوظة لا تُحتسب لغةً خاصة بك، والعبارة التي لا '
          'تناسب السؤال خطأ كأي خطأ آخر.',
    v5why='الصحيح <em>conduct research</em> &mdash; أو <em>do research</em> '
          'أو <em>carry out research</em>. الاسم هو الذي يقرر أي الأفعال '
          'يقبل، و<em>make research</em> أكثر الأخطاء كلفةً، لأن ما يقابلها '
          'صحيح في عدة لغات أخرى.',
    v6why='عبارة <em>strong rain</em> هي التي لا تقولها الإنجليزية، فالمطر يأخذ '
          '<em>heavy</em>. أما الأدلة والآراء والروائح فتأخذ كلها '
          '<em>strong</em>، ولا قاعدة تخبرك أيّ اسم يأخذ أيّها.',
    v7why='الفعل أو الصفة. الاسم هو عادةً الجزء الذي يعرفه المتعلّم أصلًا، وما '
          'يجب تعلّمه معه هو الكلمة التي يصادف أن يأخذها.',
    v8why='داخل عبارة. الكلمة مع ترجمتها كلمة تتعرّف عليها، أما الكلمة في صحبتها '
          'المعتادة فكلمة تستطيع إنتاجها، وهذه وحدها هي التي تُقيَّم.',
    v9why='إنها تغيّر القواعد والكلمات معًا: سؤال عمّا يظنّه الناس يصبح عبارة '
          'عمّا هو موضع خلاف. أما الثلاث الأخرى فتخلط نص السؤال وتعيده إليك.',
    v10why='يُقيَّم الاختباران كلاهما في Lexical Resource: تذكر معايير '
           'Speaking إعادة الصياغة صراحةً، ويكافئ Writing المرونة التي '
           'تُظهرها. فالتدريب نفسه يُحتسب مرتين &mdash; والجزء 3 وTask 2 هما '
           'حيث تؤدي إعادة الصياغة أكبر دور.',
    v11why='بحسب الفكرة. الكلمة المحفوظة تحت <em>congestion</em> تأتي ومعها حجّة، '
           'أما المحفوظة تحت حرف C فتأتي وحدها، وتحت ضغط الوقت الحجّة هي ما '
           'ينقصك.',
    v12why='صِف ما يفعله. إعادة الصياغة يكافئها هذا المعيار نفسه؛ فالكلمة من '
           'لغتك ليست إنجليزية، والسؤال ليس إجابة، والكلمة النادرة المخمَّنة هي '
           'شبه الإصابة مرة أخرى.',

    sortEyebrow='النشاط 4 · أين يجب أن يذهب وقت المراجعة',
    sortTitle='صنِّف العادات الست',
    sortHint='اسحب كل عادة إلى عمود، أو انقر عليها ثم على العمود الذي تريده.',
    sortBin1='يرفع المستوى',
    sortBin2='لا يفيد أو يكلّفك',
    sortWhy='العادات التي ترفع المستوى تتعلق <strong>باستخدام</strong> '
            'اللغة، والأخرى تتعلق <strong>باستعراضها</strong>. تسأل المعايير '
            'هل تستطيع أن تقول ما تعنيه بدقة ومرونة &mdash; ولذلك فالكلمة '
            'التي تتقنها أفضل من كلمة نادرة تخطئ الهدف، والعبارة المحفوظة '
            'كاملة أفضل من كلمة محفوظة وحدها. عادات الاستعراض توحي بالتقدّم، '
            'وهنا يكمن الفخ.',

    actTitle='ابنِ صفحة واحدة من الرصيد',
    actUse='استخدم ثلاثة منها على الأقل:',
    actSpeakBrief='اعملا في ثنائي. اختارا موضوعًا: الازدحام، أو الشيخوخة، أو '
                  'الأتمتة، أو السياحة. لديكما خمس دقائق لبناء صفحة معًا: '
                  'ثلاث أفكار، ولكل فكرة عبارتان لا كلمتان. ثم ناقشا الموضوع '
                  'دقيقتين مستخدمَين العبارات التي في صفحتكما.',
    actSpeak1='كل عبارة في الصفحة يجب أن تكون تلازمًا: فعلًا مع اسمه، أو صفةً مع '
              'اسمها. لا كلمات مفردة.',
    actSpeak2='يوقفك زميلك كلما مددت يدك إلى كلمة محتوى ليست في الصفحة، '
              'وعليك أن تقولها من جديد بكلمة موجودة فيها.',
    actSpeak3='خذ فكرة واحدة وقلها بثلاث طرق: ببساطة، وبرسمية، وكما تقولها '
              'لصديق.',
    actWriteKind='الكتابة · 150–200 كلمة',
    actWriteBrief='خذ سؤالًا من Task 2 واكتب الفقرة الأولى مرتين: مرة تكرّر فيها '
                  'كلمات السؤال، ومرة تعيد صياغته كما يجب. ثم ضع خطًّا في الثانية '
                  'تحت كل عبارة تعدّها من مفرداتك، وقل كم عددها.',
    actPlaceholder='Whether entry to museums should cost anything…',
)


# ── Chinese ────────────────────────────────────────────────────────────
T['zh'] = dict(
    coverTitle='Lexical <em>Resource</em>',
    coverSub='Speaking 和 Writing 四分之一的分数——生僻词只有用对了才算数',
    chipLevel='C1 · 高级', chipFocus='Speaking 与 Writing',
    chipCount='18 分',

    t1Eyebrow='开始之前',
    t1Title='它奖励的是恰当的词，而不只是生僻的词',
    t1ah='评分标准要求什么',
    t1ab='<strong>准确</strong>、<strong>灵活</strong>地运用词汇，并在合适的地方用上<em>不太常见</em>'
         '的词。用词不准确从 8 分往下都有提及，搭配则在 7 分和 8 分中提到。',
    t1an='用错会被扣分。永远只用最简单的词，同样会被扣分。',
    t1bh='差一点的词比普通词代价更大',
    t1bb='写出 <em>ameliorate the traffic</em> '
         '的考生，去够一个生僻动词，却给了它错误的宾语：<em>ameliorate</em> '
         '需要一个本来就不好的东西，比如拥堵或处境。考官看得见这一“够”，也看得见这一“失”。<em>Ease congestion</em> '
         '朴素、正确，而且管用。',
    t1bn='先用你有把握的词，确定搭配无误后再往上够。',
    t1ch='背下来的句子听得出来',
    t1cb='“9 分句型”清单里的句子和周围的回答格格不入，而考官受过的训练正是听出'
         '这一点。把一句塞进朴素的回答里，考官就知道哪种语言才是你真正的水平。',
    t1cn='露馅的是不协调，而不是句子本身。',

    t2Eyebrow='开始之前',
    t2Title='基本单位是搭配，不是单词',
    t2ah='名词决定动词',
    t2ab='<em>research</em> 搭配 <em>conduct</em> 或 <em>carry out</em>，<em>a '
         'decision</em> 搭配 <em>make</em> 或 <em>reach</em>，<em>a '
         'conclusion</em> 搭配 <em>draw</em> 或 <em>come '
         'to</em>。这些动词没有一个生僻，也没有一个能随便换：名词决定它接受哪些动词。',
    t2an='<em>Make research</em> 和 <em>do a decision</em> 是最常见的失误之一。',
    t2bh='形容词也一样',
    t2bb='<em>Heavy traffic</em>、<em>heavy rain</em>、<em>heavy losses</em>、'
         '<em>heavy fighting</em>——但从来没有 <em>heavy sunshine</em>。形容词由名'
         '词来选，没有规则能预测是哪个。',
    t2bn='所以要整体学、放在短语里学，而不是去推导。',
    t2ch='所以记短语，不记单词',
    t2cb='笔记本上只记一个单词加一个翻译，你得到的是一个不会用的词。把它所在的'
         '短语记下来，你得到的是明天就能说出口的东西。',
    t2cn='<em>Tackle congestion</em> 的价值是 <em>congestion = [你的母语]</em> 的'
         '十倍。',

    t3Eyebrow='开始之前',
    t3Title='改写的本事能拿两次分',
    t3ah='两门考试都奖励它',
    t3ab='Speaking 的评分标准明确提到改述；Writing 奖励其背后的灵活性，照抄题目的措辞则不计分。把一个意思用三种方式说出来的练习'
         '，在两个考场都算数——尤其是在第三部分和 Task 2，那里的观点都很抽象。',
    t3an='阅读考的也是它，只是从另一个方向。',
    t3bh='改写题目，不要照抄',
    t3bb='照抄题目的短语不算你的词汇。用自己的话写的开头能展示词汇广度；照抄题目的开头什么也展示不了。',
    t3bn='改的不只是名词，还有语法：<em>should museums be free</em> 变成 '
         '<em>whether entry should cost anything</em>。',
    t3ch='按观点建词库',
    t3cb='按字母排序的词库给你的是单词。按观点整理——交通拥堵、人口老龄化、'
         '自动化——每个词来的时候都带着一个现成的论点，而这正是你在时间紧迫时'
         '最缺的。',
    t3cn='十个观点、每个三个短语，胜过一百个孤零零的单词。',

    mcaEyebrow='练习 1 · 要准确，不要生僻',
    mcaTitle='真正评的是什么？',
    mcbEyebrow='练习 2 · 结伴出现的词',
    mcbTitle='英语用的是哪种搭配？',
    mccEyebrow='练习 3 · 换个说法',
    mccTitle='改写，以及背后的词库',

    v1why='<em>准确</em>、<em>灵活</em>地使用不太常见的词汇。不数你用了多少生僻词，而是看用得准不准，不准确会被明确扣分。',
    v2why='<em>Ameliorate</em> 需要一个本来就不好的东西——处境、后果、问题。交通本身不是坏事，拥堵才是。那一“够”看得见，'
          '那一“失”也看得见，扣分就扣在 Lexical Resource 上。',
    v3why='恰好准确的朴素词。准确正是评分标准的要求；用一个自己掌握不了的同义词替换，是想加分却丢分的常见方式。',
    v4why='它们和周围的英语格格不入，而考官受过的训练正是听出这一点。背下来的短语不算你自己的语言，而与问题不符的短语就和其他错误一样。',
    v5why='<em>Conduct research</em>——或者 <em>do research</em>、<em>carry out '
          'research</em>。名词决定它接受哪些动词，而 <em>make research</em> '
          '是代价最大的失误，因为它在好几种其他语言里的对应说法是对的。',
    v6why='英语不说的是 <em>strong rain</em>——雨要用 <em>heavy</em>。证据、观点、'
          '气味都用 <em>strong</em>，没有规则告诉你哪个名词配哪个。',
    v7why='动词或形容词。名词通常是学习者已经会的部分——要跟着它一起学的，'
          '是它恰好搭配的那个词。',
    v8why='放在短语里。带翻译的单词是你认得的词；和它的固定搭配一起记住的词，'
          '才是你说得出、写得出的词，而只有这种才算分。',
    v9why='它不但换了词，还换了语法：一个关于人们怎么想的问题，变成了一个关于'
          '哪里有争议的陈述。另外三个只是把题目打乱再还给你。',
    v10why='两门考试都按 Lexical Resource 评分：Speaking 明确提到改述，Writing '
           '奖励它所体现的灵活性。所以同样的练习算两次——而第三部分和 Task 2 正是改述最能发挥作用的地方。',
    v11why='按观点。归在 <em>congestion</em> 下的词带着论点一起来；归在字母 C 下'
           '的词孤零零地来，而时间紧迫时，你缺的正是论点。',
    v12why='描述它的作用。改写正是这项标准所奖励的——母语里的词不是英语，发问'
           '不等于回答，猜出来的生僻词又是那个“差一点”。',

    sortEyebrow='练习 4 · 复习时间该花在哪里',
    sortTitle='给这六个习惯分类',
    sortHint='把每一项拖到一栏里——或者先点一项，再点你想放进的那一栏。',
    sortBin1='能提高分数段',
    sortBin2='没有用，甚至丢分',
    sortWhy='能提高分数段的习惯，都是在<strong>使用</strong>语言；其余的则是在<strong>展示</strong>语言。评'
            '分标准问的是你能不能准确、灵活地说出想说的意思——所以一个你掌握的词胜过一个用错的生僻词，一个整体学会的短语胜过一个单独学的词。'
            '展示型的习惯让人感觉在进步，陷阱就在这里。',

    actTitle='建起词库的一页',
    actUse='至少用上三个：',
    actSpeakBrief='两人一组。选一个话题——交通拥堵、人口老龄化、自动化、旅游。用五分钟一起建一页：三个观点，每个观点配两个短语而不是两'
                  '个单词。然后用这一页上的短语，就这个话题争论两分钟。',
    actSpeak1='这一页上的每个短语都必须是搭配——动词加它的名词，或者形容词加它'
              '的名词。不要孤立的单词。',
    actSpeak2='只要你去找一个这一页上没有的实词，同伴就叫停，你得换用页上有的词重说一遍。',
    actSpeak3='拿一个观点，用三种方式说出来：朴素地说、正式地说，以及像对朋友'
              '那样说。',
    actWriteKind='写作 · 150–200 词',
    actWriteBrief='找一道 Task 2 题目，把开头段写两遍：一遍照搬题目的措辞，一遍'
                  '好好改写。然后在第二遍里给你算作自己词汇的每个短语画线，并说'
                  '出一共有几个。',
    actPlaceholder='Whether entry to museums should cost anything…',
)


# ── Japanese ───────────────────────────────────────────────────────────
T['ja'] = dict(
    coverTitle='Lexical <em>Resource</em>',
    coverSub='Speaking と Writing の点数の4分の1。珍しい語は、うまくはまったときだけ評価される',
    chipLevel='C1 · 上級', chipFocus='Speaking・Writing',
    chipCount='18 点',

    t1Eyebrow='始める前に',
    t1Title='評価されるのは適切な語。珍しい語だけではない',
    t1ah='評価基準が求めるもの',
    t1ab='<strong>正確に</strong>、<strong>柔軟に</strong>使われる語彙と、ふさわしい場面での<em>あまり一般'
         '的でない</em>語。語の選択の不正確さはバンド8以下で、コロケーションはバンド7と8で言及されています。',
    t1an='外せば減点。いちばん平易な語から一歩も出ない語彙も同じです。',
    t1bh='惜しい語は平易な語より高くつく',
    t1bb='<em>ameliorate the traffic</em> と書く受験者は、珍しい動詞に手を伸ばし、間違った目的語を与えています：'
         '<em>ameliorate</em> には、渋滞や状況のように、もともと悪いものが必要です。試験官には、手を伸ばしたことも外したこと'
         'も見えます。<em>Ease congestion</em> は平易で正しく、きちんと役目を果たします。',
    t1bn='確信のある語を使い、ぴったり合うとわかってから一歩広げましょう。',
    t1ch='丸暗記した表現は聞けばわかる',
    t1cb='「バンド9」表現集のフレーズは、周りの答えから浮いてしまいます。試験官'
         'はまさにそこを聞き取る訓練を受けています。平易な答えに一つ混ぜれば、どち'
         'らが本当のあなたの言葉かが伝わってしまいます。',
    t1cn='見破られるのはちぐはぐさであって、フレーズそのものではありません。',

    t2Eyebrow='始める前に',
    t2Title='単位は単語ではなく組み合わせ',
    t2ah='名詞が動詞を選ぶ',
    t2ab='<em>research</em> には <em>conduct</em> か <em>carry out</em>、<em>a '
         'decision</em> には <em>make</em> か <em>reach</em>、<em>a '
         'conclusion</em> には <em>draw</em> か <em>come '
         'to</em>。どの動詞も珍しくはなく、どれも自由には選べません：名詞がどの動詞を受け入れるかを決めるのです。',
    t2an='<em>Make research</em> と <em>do a decision</em> は、いちばんよくある誤りの一つです。',
    t2bh='形容詞も同じ',
    t2bb='<em>Heavy traffic</em>、<em>heavy rain</em>、<em>heavy losses</em>、'
         '<em>heavy fighting</em>――でも <em>heavy sunshine</em> とは決して言いませ'
         'ん。形容詞は名詞が選び、どれになるかを予測する規則はありません。',
    t2bn='だから、理屈で導くのではなく、フレーズごと丸ごと覚えるのです。',
    t2ch='だから単語ではなくフレーズを書く',
    t2cb='単語と訳語だけのノートでは、使えない単語が手に入るだけです。その語が使'
         'われるフレーズごと書いておけば、明日言えるものが手に入ります。',
    t2cn='<em>Tackle congestion</em> は <em>congestion = [あなたの言語]</em> の十'
         '倍の価値があります。',

    t3Eyebrow='始める前に',
    t3Title='言い換えは二度報われる技能',
    t3ah='どちらの試験でも評価される',
    t3ab='Speaking は評価基準の中で言い換えをはっきり挙げています。Writing '
         'はその背後にある柔軟さを評価し、問題文から写した言い回しは評価しません。一つの考えを三通りに言う練習は、どちらの試験室でも生きます――'
         'とくに抽象的な考えを扱うパート3と Task 2 で。',
    t3an='Reading がテストしているのも、反対側から見た同じ技能です。',
    t3bh='問題文を写さず、言い換える',
    t3bb='問題文から写した表現は、あなたの語彙として評価されません。自分の言葉で書いた導入は幅を示しますが、問題を写した導入は何も示しません。',
    t3bn='名詞だけでなく文法も変えましょう：<em>should museums be free</em> は '
         '<em>whether entry should cost anything</em> になります。',
    t3ch='語彙はアイデアごとにためる',
    t3cb='アルファベット順の語彙集が与えてくれるのは単語です。アイデアごと――交'
         '通渋滞、高齢化、自動化――に整理すれば、どの語も議論を一つ携えてやって来'
         'ます。時間に追われているとき足りないのは、まさにそれです。',
    t3cn='表現を三つずつ持った十のアイデアは、表現のない百の単語に勝ります。',

    mcaEyebrow='演習 1 · 珍しさではなく正確さ',
    mcaTitle='実際に採点されているのは何か？',
    mcbEyebrow='演習 2 · 一緒に使われる語',
    mcbTitle='英語が使う組み合わせはどれか？',
    mccEyebrow='演習 3 · 別の言い方をする',
    mccTitle='言い換えと、それを支える語彙',

    v1why='あまり一般的でない語彙を<em>正確に</em>、<em>柔軟に</em>使うこと。珍しい語の数は数えられず、正確に使われているかど'
          'うかが見られます。不正確さははっきり減点されます。',
    v2why='<em>Ameliorate</em> には、状況、影響、問題のように、もともと悪いものが必要です。交通そのものは悪くありませんが、'
          '渋滞は悪いものです。手を伸ばしたことも外したことも見え、それは Lexical Resource で減点されます。',
    v3why='ぴったり正しい平易な語。正確さこそが評価基準です。使いこなせない類語辞典の言い換えは、点を稼ごうとして点を失うよくある方法です。',
    v4why='周りの英語から浮いていて、試験官はそれを聞き取る訓練を受けています。暗記したフレーズはあなた自身の言葉として評価されず、問題に合わな'
          'いフレーズはほかの誤りと同じく誤りです。',
    v5why='<em>Conduct research</em>――または <em>do research</em>、<em>carry out '
          'research</em>。名詞がどの動詞を受け入れるかを決め、<em>make research</em> '
          'はもっとも高くつく誤りです。いくつかの言語では、それに当たる言い方が正しいからです。',
    v6why='英語が言わないのは <em>strong rain</em> です――雨は <em>heavy</em> を'
          'とります。証拠、意見、においはどれも <em>strong</em> をとり、どの名詞'
          'がどれをとるかを教えてくれる規則はありません。',
    v7why='動詞か形容詞です。名詞はたいてい学習者がすでに知っている部分で、一緒に'
          '覚えるべきなのは、その名詞がたまたまとる語のほうです。',
    v8why='フレーズの中で。訳語つきの単語は見てわかる語、いつも一緒に使われる語と'
          'セットで覚えた単語は自分で使える語で、採点されるのは後者だけです。',
    v9why='語だけでなく文法も変えています。人々がどう思うかという問いが、何が議論'
          'になっているかという文に変わっています。ほかの三つは問題文を並べ替えて'
          '返しているだけです。',
    v10why='どちらの試験も Lexical Resource で採点されます：Speaking は言い換えをはっきり挙げ、Writing '
           'は言い換えが示す柔軟さを評価します。同じ練習が二度効くわけです――そして言い換えがいちばん働くのはパート3と Task 2 です。',
    v11why='アイデアごとに。<em>congestion</em> の下にしまった語は議論と一緒に出'
           'てきます。C の下にしまった語は一つだけで出てきて、時間に追われていると'
           'き足りないのは議論のほうです。',
    v12why='それが何をするものかを説明します。言い換えはまさにこの基準で評価され'
           'ます――母語の語は英語ではなく、尋ねるのは答えることではなく、当てずっ'
           'ぽうの難語はまた「惜しい語」になります。',

    sortEyebrow='演習 4 · 復習の時間をどこに使うか',
    sortTitle='六つの習慣を分類しましょう',
    sortHint='それぞれを列にドラッグしてください。または項目をクリックしてから、'
             '入れたい列をクリックします。',
    sortBin1='バンドを上げる',
    sortBin2='効果なし、または減点',
    sortWhy='バンドを上げる習慣は、言葉を<strong>使う</strong>ことに関わり、ほかの習慣は言葉を<strong>見せびらかす<'
            '/strong>ことに関わります。評価基準が問うのは、言いたいことを正確に、柔軟に言えるかどうか――だから、使いこなせる語は外れ'
            'る珍しい語に勝り、まるごと覚えたフレーズは単独で覚えた語に勝ります。見せびらかす習慣は進歩している気にさせる、そこが落とし穴です'
            '。',

    actTitle='語彙集を一ページ作る',
    actUse='少なくとも三つ使いましょう：',
    actSpeakBrief='ペアで。テーマを一つ選びます――交通渋滞、高齢化、自動化、観光。五分で一緒に一ページ作ります：アイデアを三つ、それぞ'
                  'れに単語二つではなくフレーズ二つ。そのあと二分間、ページのフレーズを使ってそのテーマについて議論しましょう。',
    actSpeak1='ページのどのフレーズも組み合わせにすること――動詞とその名詞、または'
              '形容詞とその名詞。単語だけはなしです。',
    actSpeak2='ページにない内容語に手を伸ばしたら、パートナーが止めます。ページにある語を使って言い直さなければなりません。',
    actSpeak3='一つのアイデアを三通りに言いましょう：平易に、フォーマルに、そして友'
              'だちに言うように。',
    actWriteKind='ライティング · 150–200 語',
    actWriteBrief='Task 2 の問題を一つ選び、最初の段落を二回書きましょう。一回は問'
                  'いの言葉を繰り返して、もう一回はきちんと言い換えて。次に、二つ'
                  '目の中で自分の語彙と数えられるフレーズすべてに下線を引き、いく'
                  'つあるかを書きます。',
    actPlaceholder='Whether entry to museums should cost anything…',
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
