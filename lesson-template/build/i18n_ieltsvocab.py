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
    coverSub='A quarter of the marks in Speaking and in Writing, and it is not '
             'the quarter that rewards rare words',
    chipLevel='C1 · Advanced', chipFocus='Speaking &amp; Writing',
    chipCount='18 points',

    t1Eyebrow='Before you start',
    t1Title='It does not reward rare words. It never has.',
    t1ah='What the descriptors ask for',
    t1ab='A range of vocabulary used with <strong>precision</strong> and '
         '<strong>flexibility</strong>, and <em>less common</em> words where '
         'they fit. Errors in word choice and collocation are named at every '
         'band.',
    t1an='Rarity with a miss scores below plainness with a hit.',
    t1bh='The near-miss costs more than the plain word',
    t1bb='A candidate who writes <em>ameliorate the traffic</em> has reached '
         'for a rare verb and attached it to the wrong object. The examiner '
         'sees the reach and the miss. <em>Ease the traffic</em> is plain, '
         'right, and scores higher.',
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
    t2ab='You <em>conduct</em> research, <em>reach</em> a decision and '
         '<em>draw</em> a conclusion. None of those verbs is rare; all three '
         'are fixed, and none of them is the one a dictionary gives you for '
         'the noun.',
    t2an='<em>Make research</em> and <em>do a decision</em> are the two this '
         'costs most often.',
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
    t3ah='Both papers score it',
    t3ab='Speaking and Writing are both marked on Lexical Resource. The work '
         'you do on saying one idea three ways is marked in both rooms '
         '&mdash; above all in Part 3 and in Task 2, where the ideas are '
         'abstract.',
    t3an='It is also what Reading tests, from the other side.',
    t3bh='Reword the question, do not copy it',
    t3bb='Words lifted straight from the prompt are not counted as your '
         'vocabulary. An opening that restates the question in your own terms '
         'is scored; one that repeats it is not.',
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
          'Count and rarity are not criteria; accuracy is, and inaccuracy is '
          'penalised by name.',
    v2why='<em>Ameliorate</em> takes a situation or a condition, not a thing. '
          'The reach is visible and so is the miss, and Lexical Resource is '
          'where it is charged.',
    v3why='The plain word that is exactly right. Precision is the descriptor; '
          'a thesaurus swap the writer cannot control is the commonest way to '
          'lose marks while trying to gain them.',
    v4why='They sit apart from the English around them, and examiners are '
          'trained to hear that. The phrase is not banned &mdash; it simply '
          'does not count as your own language.',
    v5why='<em>Conduct research</em>. The verb is fixed by the noun, and '
          '<em>make research</em> is the version that costs most often, '
          'because it is right in several other languages.',
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
    v10why='Speaking and Writing are both marked on Lexical Resource, so the '
           'same practice counts in two papers &mdash; and Part 3 and Task 2 '
           'are where a paraphrase does the most work.',
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
                  'automation, tourism. Five minutes to build a page together: '
                  'three ideas, and for each idea two phrases rather than two '
                  'words. Then argue the topic for two minutes using only what '
                  'is on your page.',
    actSpeak1='Every phrase on the page must be a pairing &mdash; a verb with '
              'its noun, or an adjective with its noun. No bare words.',
    actSpeak2='Your partner stops you whenever you use a word that is not on '
              'the page, and you have to say it again using one that is.',
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
    coverSub='Ein Viertel der Note im Speaking und im Writing &mdash; und nicht '
             'das Viertel, das seltene Wörter belohnt',
    chipLevel='C1 · Fortgeschritten', chipFocus='Speaking &amp; Writing',
    chipCount='18 Punkte',

    t1Eyebrow='Bevor du beginnst',
    t1Title='Seltene Wörter werden nicht belohnt. Nie gewesen.',
    t1ah='Was die Deskriptoren verlangen',
    t1ab='Ein breiter Wortschatz, verwendet mit <strong>Präzision</strong> '
         'und <strong>Flexibilität</strong>, und <em>weniger gebräuchliche</em> '
         'Wörter dort, wo sie passen. Fehler in Wortwahl und Kollokation '
         'werden in jedem Band ausdrücklich genannt.',
    t1an='Selten und daneben liegt unter schlicht und richtig.',
    t1bh='Der Fastreffer kostet mehr als das schlichte Wort',
    t1bb='Wer <em>ameliorate the traffic</em> schreibt, hat nach einem seltenen '
         'Verb gegriffen und es an das falsche Objekt gehängt. Der Prüfer '
         'sieht den Griff und den Fehlgriff. <em>Ease the traffic</em> ist '
         'schlicht, richtig und bringt mehr.',
    t1bn='Greif zum Wort, bei dem du sicher bist, und streck dich erst, wenn '
         'du die Passung kennst.',
    t1ch='Auswendiges hört man',
    t1cb='Listen mit „Band-9-Phrasen“ stehen neben der Antwort, die sie '
         'umgibt, und Prüfer sind darauf geschult, genau das zu hören. Steht '
         'eine davon in einer schlichten Antwort, hört der Prüfer, welche '
         'Sprache wirklich deine ist.',
    t1cn='Verräterisch ist der Bruch, nicht die Phrase selbst.',

    t2Eyebrow='Bevor du beginnst',
    t2Title='Die Einheit ist die Paarung, nicht das Wort',
    t2ah='Das Substantiv wählt das Verb',
    t2ab='Man <em>conducts</em> research, <em>reaches</em> a decision und '
         '<em>draws</em> a conclusion. Keines dieser Verben ist selten, alle '
         'drei sind fest, und keines steht im Wörterbuch beim Substantiv.',
    t2an='<em>Make research</em> und <em>do a decision</em> kosten hier am '
         'häufigsten.',
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
    t3ah='Beide Prüfungsteile bewerten es',
    t3ab='Speaking und Writing werden beide nach Lexical Resource bewertet. '
         'Die Arbeit daran, eine Idee auf drei Arten zu sagen, zählt in '
         'beiden Räumen &mdash; vor allem in Teil 3 und in Task 2, wo die '
         'Ideen abstrakt sind.',
    t3an='Und das Reading prüft genau dasselbe, nur von der anderen Seite.',
    t3bh='Formuliere die Frage um, kopier sie nicht',
    t3bb='Wörter, die direkt aus der Aufgabenstellung stammen, zählen nicht '
         'als dein Wortschatz. Eine Einleitung, die die Frage in eigenen '
         'Worten wiedergibt, wird bewertet; eine, die sie wiederholt, nicht.',
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
    mcbTitle='Welche Paarung verwendet das Englische?',
    mccEyebrow='Aktivität 3 · Es anders sagen',
    mccTitle='Umschreiben, und die Sammlung dahinter',

    v1why='Weniger gebräuchlicher Wortschatz, <em>genau</em> und '
          '<em>flexibel</em> verwendet. Anzahl und Seltenheit sind keine '
          'Kriterien; Genauigkeit schon, und Ungenauigkeit kostet.',
    v2why='<em>Ameliorate</em> nimmt eine Lage oder einen Zustand, kein Ding. '
          'Der Griff ist sichtbar und der Fehlgriff auch, und berechnet wird '
          'er bei Lexical Resource.',
    v3why='Das schlichte Wort, das genau passt. Präzision ist der Deskriptor; '
          'ein Thesaurus-Tausch, den man nicht beherrscht, ist der häufigste '
          'Weg, beim Punktesammeln Punkte zu verlieren.',
    v4why='Sie stehen neben dem Englisch um sie herum, und darauf sind Prüfer '
          'geschult. Die Phrase ist nicht verboten &mdash; sie zählt nur nicht '
          'als deine eigene Sprache.',
    v5why='<em>Conduct research</em>. Das Verb ist durch das Substantiv '
          'festgelegt, und <em>make research</em> kostet am häufigsten, weil '
          'es in mehreren anderen Sprachen richtig ist.',
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
    v10why='Speaking und Writing werden beide nach Lexical Resource bewertet, '
           'dieselbe Übung zählt also in zwei Prüfungsteilen &mdash; und in '
           'Teil 3 und Task 2 leistet eine Umformulierung am meisten.',
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
                  'gemeinsame Seite: drei Ideen, und zu jeder Idee zwei '
                  'Phrasen statt zwei Wörtern. Dann zwei Minuten über das '
                  'Thema sprechen, nur mit dem, was auf der Seite steht.',
    actSpeak1='Jede Phrase auf der Seite muss eine Paarung sein &mdash; Verb '
              'mit Substantiv oder Adjektiv mit Substantiv. Keine nackten '
              'Wörter.',
    actSpeak2='Dein Partner stoppt dich, sobald du ein Wort benutzt, das nicht '
              'auf der Seite steht, und du sagst es noch einmal mit einem, das '
              'daraufsteht.',
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
    sortWhy='Alles links dreht sich darum, Sprache zu <strong>benutzen</strong>; '
            'alles rechts darum, sie <strong>vorzuführen</strong>. Die '
            'Bewertungskriterien fragen, ob du sagen kannst, was du meinst, '
            'präzise und flexibel &mdash; ein schlichtes Wort, das trifft, '
            'schlägt also ein seltenes, das danebengeht, und eine ganz '
            'gelernte Wendung schlägt ein einzeln gelerntes Wort. In die '
            'rechte Spalte fließt die meiste Lernzeit.',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Lexical <em>Resource</em>',
    coverSub='Una cuarta parte de la nota en Speaking y en Writing, y no es la '
             'cuarta parte que premia las palabras raras',
    chipLevel='C1 · Avanzado', chipFocus='Speaking y Writing',
    chipCount='18 puntos',

    t1Eyebrow='Antes de empezar',
    t1Title='No premia las palabras raras. Nunca lo ha hecho.',
    t1ah='Qué piden los descriptores',
    t1ab='Un vocabulario amplio, usado con <strong>precisión</strong> y '
         '<strong>flexibilidad</strong>, y palabras <em>menos frecuentes</em> '
         'donde encajan. Los errores de elección de palabra y de colocación '
         'aparecen con nombre en todas las bandas.',
    t1an='Raro y fallado puntúa menos que llano y acertado.',
    t1bh='El casi-acierto cuesta más que la palabra llana',
    t1bb='Quien escribe <em>ameliorate the traffic</em> ha ido a por un verbo '
         'raro y lo ha pegado al objeto equivocado. El examinador ve el '
         'intento y el fallo. <em>Ease the traffic</em> es llano, correcto y '
         'puntúa más.',
    t1bn='Ve a por la palabra de la que estés seguro y estírate solo cuando '
         'sepas que encaja.',
    t1ch='Las frases memorizadas se oyen',
    t1cb='Las listas de «frases de band 9» quedan aparte del inglés que las '
         'rodea, y a los examinadores se les entrena para oír justo eso. Mete '
         'una en una respuesta llana y el examinador sabe qué lengua es de '
         'verdad la tuya.',
    t1cn='Lo que te delata es el desajuste, no la frase.',

    t2Eyebrow='Antes de empezar',
    t2Title='La unidad es la pareja, no la palabra',
    t2ah='El sustantivo elige el verbo',
    t2ab='Se <em>conducts</em> research, se <em>reaches</em> a decision y se '
         '<em>draws</em> a conclusion. Ninguno de esos verbos es raro, los '
         'tres son fijos, y ninguno aparece en el diccionario junto al '
         'sustantivo.',
    t2an='<em>Make research</em> y <em>do a decision</em> son los dos que más '
         'cuestan.',
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
    t3ah='Las dos pruebas la puntúan',
    t3ab='Speaking y Writing se califican los dos con Lexical Resource. El '
         'trabajo de decir una idea de tres maneras cuenta en las dos salas, '
         'sobre todo en la Parte 3 y en Task 2, donde las ideas son '
         'abstractas.',
    t3an='Y el Reading examina lo mismo, solo que desde el otro lado.',
    t3bh='Reformula la pregunta, no la copies',
    t3bb='Las palabras sacadas tal cual del enunciado no cuentan como tu '
         'vocabulario. Una introducción que replantea la pregunta con tus '
         'términos puntúa; una que la repite, no.',
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
    mcbTitle='¿Qué pareja usa el inglés?',
    mccEyebrow='Actividad 3 · Decirlo de otra manera',
    mccTitle='Parafrasear, y el banco que hay detrás',

    v1why='Léxico menos frecuente usado con <em>exactitud</em> y '
          '<em>flexibilidad</em>. Ni la cantidad ni la rareza son criterios; '
          'la exactitud sí, y la inexactitud se penaliza por su nombre.',
    v2why='<em>Ameliorate</em> lleva una situación o una condición, no una '
          'cosa. Se ve el intento y se ve el fallo, y se cobra en Lexical '
          'Resource.',
    v3why='La palabra llana que encaja exactamente. La precisión es el '
          'descriptor; un cambio de tesauro que no dominas es la forma más '
          'común de perder puntos intentando ganarlos.',
    v4why='Quedan aparte del inglés que las rodea, y a los examinadores se les '
          'entrena para oírlo. La frase no está prohibida: simplemente no '
          'cuenta como lengua tuya.',
    v5why='<em>Conduct research</em>. El verbo lo fija el sustantivo, y '
          '<em>make research</em> es la versión que más cuesta porque es la '
          'correcta en varios otros idiomas.',
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
    v10why='Speaking y Writing se califican los dos con Lexical Resource, así '
           'que la misma práctica cuenta en dos pruebas, y en la Parte 3 y en '
           'Task 2 es donde una paráfrasis rinde más.',
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
                  'página juntos: tres ideas y, por cada idea, dos frases en '
                  'lugar de dos palabras. Luego dos minutos defendiendo el '
                  'tema usando solo lo que hay en la página.',
    actSpeak1='Cada frase de la página tiene que ser una pareja: un verbo con '
              'su sustantivo, o un adjetivo con su sustantivo. Nada de '
              'palabras sueltas.',
    actSpeak2='Tu compañero te para en cuanto uses una palabra que no esté en '
              'la página, y tienes que decirlo otra vez con una que sí esté.',
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
    sortWhy='Todo lo de la izquierda trata de <strong>usar</strong> la lengua; '
            'todo lo de la derecha, de <strong>exhibirla</strong>. Los '
            'descriptores preguntan si sabes decir lo que quieres decir, con '
            'precisión y flexibilidad: así que una palabra sencilla que acierta '
            'gana a una rara que falla, y una expresión aprendida entera gana a '
            'una palabra aprendida suelta. La columna de la derecha es donde se '
            'va la mayor parte del tiempo de repaso.',
)


# ── French ─────────────────────────────────────────────────────────────
T['fr'] = dict(
    coverTitle='Lexical <em>Resource</em>',
    coverSub='Un quart des points à l’oral comme à l’écrit, et ce n’est pas le '
             'quart qui récompense les mots rares',
    chipLevel='C1 · Avancé', chipFocus='Speaking &amp; Writing',
    chipCount='18 points',

    t1Eyebrow='Avant de commencer',
    t1Title='Il ne récompense pas les mots rares. Jamais.',
    t1ah='Ce que demandent les descripteurs',
    t1ab='Un vocabulaire varié, employé avec <strong>précision</strong> et '
         '<strong>souplesse</strong>, et des mots <em>moins courants</em> là '
         'où ils conviennent. Les erreurs de choix de mot et de collocation sont '
         'citées à chaque band.',
    t1an='Un mot rare mal employé rapporte moins qu’un mot simple bien placé.',
    t1bh='Le presque-juste coûte plus cher que le mot simple',
    t1bb='Le candidat qui écrit <em>ameliorate the traffic</em> est allé '
         'chercher un verbe rare et l’a accroché au mauvais complément. '
         'L’examinateur voit l’effort et le raté. <em>Ease the traffic</em> est '
         'simple, juste, et rapporte davantage.',
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
    t2ab='On <em>conduct</em> research, on <em>reach</em> a decision et on '
         '<em>draw</em> a conclusion. Aucun de ces verbes n’est rare ; tous les '
         'trois sont figés, et aucun n’est celui que le dictionnaire vous donne '
         'pour le nom.',
    t2an='<em>Make research</em> et <em>do a decision</em> sont les deux qui '
         'coûtent le plus souvent.',
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
    t3ah='Les deux épreuves la notent',
    t3ab='Le Speaking et le Writing sont tous deux notés sur Lexical Resource. '
         'Le travail qui consiste à dire une idée de trois façons compte dans '
         'les deux salles &mdash; surtout dans la Partie 3 et dans la Task 2, '
         'où les idées sont abstraites.',
    t3an='C’est aussi ce que teste le Reading, de l’autre côté.',
    t3bh='Reformulez la question, ne la recopiez pas',
    t3bb='Les mots repris tels quels de l’énoncé ne comptent pas comme votre '
         'vocabulaire. Une introduction qui reformule la question avec vos '
         'propres termes est notée ; une qui la répète ne l’est pas.',
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
          '<em>souplesse</em>. Ni la quantité ni la rareté ne sont des critères ; '
          'l’exactitude, si, et l’inexactitude est pénalisée nommément.',
    v2why='<em>Ameliorate</em> s’emploie avec une situation ou un état, pas '
          'avec une chose. L’effort se voit, le raté aussi, et c’est Lexical '
          'Resource qui en paie le prix.',
    v3why='Le mot simple et parfaitement juste. Le descripteur, c’est la '
          'précision ; un synonyme tiré du dictionnaire que l’on ne maîtrise pas '
          'est la façon la plus courante de perdre des points en voulant en '
          'gagner.',
    v4why='Elles détonnent dans l’anglais qui les entoure, et les examinateurs '
          'sont formés pour l’entendre. L’expression n’est pas interdite &mdash; '
          'elle ne compte simplement pas comme votre propre langue.',
    v5why='<em>Conduct research</em>. Le verbe est imposé par le nom, et '
          '<em>make research</em> est la version qui coûte le plus souvent, parce '
          'qu’elle est juste dans plusieurs autres langues.',
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
    v10why='Le Speaking et le Writing sont tous deux notés sur Lexical Resource : '
           'le même entraînement compte donc dans deux épreuves &mdash; et c’est '
           'dans la Partie 3 et la Task 2 qu’une reformulation rend le plus de '
           'services.',
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
    sortWhy='Tout ce qui est à gauche concerne l’<strong>usage</strong> de la '
            'langue ; tout ce qui est à droite concerne son '
            '<strong>étalage</strong>. Les descripteurs demandent si vous savez '
            'dire ce que vous voulez dire, avec précision et souplesse &mdash; '
            'donc un mot simple qui porte l’emporte sur un mot rare qui manque sa '
            'cible, et une expression apprise en bloc l’emporte sur un mot appris '
            'seul. C’est dans la colonne de droite que part l’essentiel du temps '
            'de révision.',

    actTitle='Construisez une page de la réserve',
    actUse='Utilisez-en au moins trois :',
    actSpeakBrief='À deux. Prenez un thème &mdash; congestion, vieillissement, '
                  'automatisation, tourisme. Cinq minutes pour construire une '
                  'page ensemble : trois idées, et pour chaque idée deux '
                  'expressions plutôt que deux mots. Puis débattez du thème '
                  'pendant deux minutes en n’utilisant que ce qui est sur votre '
                  'page.',
    actSpeak1='Chaque expression de la page doit être une association &mdash; un '
              'verbe avec son nom, ou un adjectif avec son nom. Pas de mots '
              'isolés.',
    actSpeak2='Votre partenaire vous arrête chaque fois que vous employez un mot '
              'qui n’est pas sur la page, et vous devez le redire avec un mot qui '
              'y est.',
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
    coverSub='Un quarto dei punti nello Speaking e nel Writing, e non è il quarto '
             'che premia le parole rare',
    chipLevel='C1 · Avanzato', chipFocus='Speaking e Writing',
    chipCount='18 punti',

    t1Eyebrow='Prima di cominciare',
    t1Title='Non premia le parole rare. Non l’ha mai fatto.',
    t1ah='Che cosa chiedono i descrittori',
    t1ab='Un lessico vario, usato con <strong>precisione</strong> e '
         '<strong>flessibilità</strong>, e parole <em>meno comuni</em> dove '
         'ci stanno. Gli errori di scelta delle parole e di collocazione sono '
         'citati in ogni band.',
    t1an='Una parola rara sbagliata vale meno di una parola semplice azzeccata.',
    t1bh='Il quasi giusto costa più della parola semplice',
    t1bb='Chi scrive <em>ameliorate the traffic</em> ha cercato un verbo raro e '
         'l’ha attaccato al complemento sbagliato. L’esaminatore vede lo sforzo '
         'e l’errore. <em>Ease the traffic</em> è semplice, giusto, e vale di '
         'più.',
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
    t2ab='Si <em>conduct</em> research, si <em>reach</em> a decision e si '
         '<em>draw</em> a conclusion. Nessuno di questi verbi è raro; tutti e '
         'tre sono fissi, e nessuno è quello che il dizionario ti dà per il '
         'nome.',
    t2an='<em>Make research</em> e <em>do a decision</em> sono le due che costano '
         'più spesso.',
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
    t3ah='La valutano entrambe le prove',
    t3ab='Speaking e Writing sono valutati entrambi su Lexical Resource. Il '
         'lavoro che fai per dire un’idea in tre modi conta in tutte e due le '
         'aule &mdash; soprattutto nella Parte 3 e nella Task 2, dove le idee '
         'sono astratte.',
    t3an='È anche ciò che il Reading verifica, dall’altra parte.',
    t3bh='Riformula la domanda, non copiarla',
    t3bb='Le parole prese pari pari dalla traccia non contano come tuo '
         'vocabolario. Un’apertura che riformula la domanda con parole tue '
         'viene premiata; una che la ripete no.',
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
          '<em>flessibilità</em>. Quantità e rarità non sono criteri; la '
          'precisione sì, e l’imprecisione viene penalizzata esplicitamente.',
    v2why='<em>Ameliorate</em> si usa con una situazione o una condizione, non '
          'con una cosa. Lo sforzo si vede, e anche l’errore, ed è in Lexical '
          'Resource che si paga.',
    v3why='La parola semplice e perfettamente giusta. Il descrittore è la '
          'precisione; un sinonimo preso dal dizionario che non si sa gestire è '
          'il modo più comune di perdere punti cercando di guadagnarne.',
    v4why='Stonano con l’inglese che le circonda, e gli esaminatori sono '
          'addestrati a sentirlo. La frase non è vietata &mdash; semplicemente '
          'non conta come lingua tua.',
    v5why='<em>Conduct research</em>. Il verbo lo impone il nome, e <em>make '
          'research</em> è la versione che costa più spesso, perché in diverse '
          'altre lingue è giusta.',
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
    v10why='Speaking e Writing sono valutati entrambi su Lexical Resource, '
           'quindi lo stesso esercizio conta in due prove &mdash; e la Parte 3 e '
           'la Task 2 sono dove una riformulazione rende di più.',
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
    sortWhy='Tutto ciò che sta a sinistra riguarda l’<strong>uso</strong> della '
            'lingua; tutto ciò che sta a destra riguarda il suo '
            '<strong>sfoggio</strong>. I descrittori chiedono se sai dire ciò che '
            'intendi, con precisione e flessibilità &mdash; quindi una parola '
            'semplice che arriva a segno batte una rara che lo manca, e '
            'un’espressione imparata intera batte una parola imparata da sola. È '
            'nella colonna di destra che finisce la maggior parte del tempo di '
            'ripasso.',

    actTitle='Costruisci una pagina della banca',
    actUse='Usane almeno tre:',
    actSpeakBrief='In coppia. Prendete un tema &mdash; congestione, '
                  'invecchiamento, automazione, turismo. Cinque minuti per '
                  'costruire insieme una pagina: tre idee, e per ogni idea due '
                  'espressioni invece di due parole. Poi discutete il tema per '
                  'due minuti usando solo ciò che c’è sulla pagina.',
    actSpeak1='Ogni espressione sulla pagina deve essere una combinazione &mdash; '
              'un verbo con il suo nome, o un aggettivo con il suo nome. Niente '
              'parole isolate.',
    actSpeak2='Il tuo compagno ti ferma ogni volta che usi una parola che non è '
              'sulla pagina, e devi ridirlo usandone una che c’è.',
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
    coverSub='Um quarto da nota no Speaking e no Writing, e não é o quarto que '
             'premeia as palavras raras',
    chipLevel='C1 · Avançado', chipFocus='Speaking e Writing',
    chipCount='18 pontos',

    t1Eyebrow='Antes de começar',
    t1Title='Não premeia palavras raras. Nunca premiou.',
    t1ah='O que pedem os descritores',
    t1ab='Um vocabulário variado, usado com <strong>precisão</strong> e '
         '<strong>flexibilidade</strong>, e palavras <em>menos comuns</em> onde '
         'encaixam. Os erros de escolha de palavras e de colocação são referidos '
         'em todos os bands.',
    t1an='Uma palavra rara que falha vale menos do que uma palavra simples que '
         'acerta.',
    t1bh='O quase certo custa mais do que a palavra simples',
    t1bb='Quem escreve <em>ameliorate the traffic</em> foi buscar um verbo raro '
         'e agarrou-o ao complemento errado. O examinador vê o esforço e a '
         'falha. <em>Ease the traffic</em> é simples, está certo e vale mais.',
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
    t2ab='Faz-se <em>conduct</em> research, <em>reach</em> a decision e '
         '<em>draw</em> a conclusion. Nenhum destes verbos é raro; os três são '
         'fixos, e nenhum é o que o dicionário te dá para o nome.',
    t2an='<em>Make research</em> e <em>do a decision</em> são os dois que mais '
         'vezes custam pontos.',
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
    t3ah='As duas provas avaliam-na',
    t3ab='O Speaking e o Writing são ambos avaliados em Lexical Resource. O '
         'trabalho de dizer uma ideia de três maneiras conta nas duas salas '
         '&mdash; sobretudo na Parte 3 e na Task 2, onde as ideias são '
         'abstratas.',
    t3an='É também o que o Reading testa, do outro lado.',
    t3bh='Reformula a pergunta, não a copies',
    t3bb='As palavras tiradas tal e qual do enunciado não contam como '
         'vocabulário teu. Uma introdução que reformula a pergunta por palavras '
         'tuas conta; uma que a repete não.',
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

    v1why='Vocabulário menos comum usado com <em>precisão</em> e '
          '<em>flexibilidade</em>. Nem a quantidade nem a raridade são critérios; '
          'a precisão é, e a imprecisão é penalizada pelo nome.',
    v2why='<em>Ameliorate</em> usa-se com uma situação ou uma condição, não com '
          'uma coisa. O esforço vê-se, e a falha também, e é no Lexical Resource '
          'que se paga.',
    v3why='A palavra simples e exatamente certa. O descritor é a precisão; um '
          'sinónimo de dicionário que não se domina é a forma mais comum de '
          'perder pontos a tentar ganhá-los.',
    v4why='Destoam do inglês à volta, e os examinadores são treinados para dar '
          'por isso. A expressão não é proibida &mdash; simplesmente não conta '
          'como língua tua.',
    v5why='<em>Conduct research</em>. O verbo é imposto pelo nome, e <em>make '
          'research</em> é a versão que mais vezes custa pontos, porque está '
          'certa em várias outras línguas.',
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
    v10why='O Speaking e o Writing são ambos avaliados em Lexical Resource, por '
           'isso o mesmo treino conta em duas provas &mdash; e é na Parte 3 e na '
           'Task 2 que uma paráfrase rende mais.',
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
    sortWhy='Tudo o que está à esquerda tem a ver com <strong>usar</strong> a '
            'língua; tudo o que está à direita tem a ver com '
            '<strong>exibi-la</strong>. Os descritores perguntam se consegues '
            'dizer o que queres dizer, com precisão e flexibilidade &mdash; por '
            'isso uma palavra simples que acerta vale mais do que uma rara que '
            'falha, e uma expressão aprendida inteira vale mais do que uma palavra '
            'aprendida sozinha. É na coluna da direita que vai a maior parte do '
            'tempo de revisão.',

    actTitle='Constrói uma página do banco',
    actUse='Usa pelo menos três:',
    actSpeakBrief='Em pares. Escolham um tema &mdash; congestionamento, '
                  'envelhecimento, automação, turismo. Cinco minutos para '
                  'construírem juntos uma página: três ideias e, para cada uma, '
                  'duas expressões em vez de duas palavras. Depois discutam o '
                  'tema durante dois minutos usando só o que está na página.',
    actSpeak1='Cada expressão da página tem de ser uma combinação &mdash; um '
              'verbo com o seu nome, ou um adjetivo com o seu nome. Nada de '
              'palavras soltas.',
    actSpeak2='O teu colega interrompe-te sempre que usas uma palavra que não '
              'está na página, e tens de voltar a dizer a frase com uma que '
              'esteja.',
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
    coverSub='Четверть баллов в Speaking и в Writing &mdash; и это не та '
             'четверть, что награждает за редкие слова',
    chipLevel='C1 · Продвинутый', chipFocus='Speaking и Writing',
    chipCount='18 баллов',

    t1Eyebrow='Прежде чем начать',
    t1Title='Редкие слова здесь не награждают. И никогда не награждали.',
    t1ah='Чего требуют дескрипторы',
    t1ab='Разнообразной лексики, употреблённой <strong>точно</strong> и '
         '<strong>гибко</strong>, и <em>менее частотных</em> слов там, где они '
         'уместны. Ошибки в выборе слов и в сочетаемости названы в описании '
         'каждого балла.',
    t1an='Редкое слово мимо цели стоит меньше, чем простое слово в цель.',
    t1bh='Почти-попадание обходится дороже простого слова',
    t1bb='Кандидат, который пишет <em>ameliorate the traffic</em>, потянулся за '
         'редким глаголом и прицепил его не к тому дополнению. Экзаменатор видит '
         'и попытку, и промах. <em>Ease the traffic</em> &mdash; просто, верно и '
         'оценивается выше.',
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
    t2ab='По-английски <em>conduct</em> research, <em>reach</em> a decision и '
         '<em>draw</em> a conclusion. Ни один из этих глаголов не редкий; все три '
         'устойчивы, и ни один не совпадает с тем, что даёт словарь для '
         'существительного.',
    t2an='Чаще всего баллы отнимают <em>make research</em> и <em>do a '
         'decision</em>.',
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
    t3ah='Его оценивают оба экзамена',
    t3ab='И Speaking, и Writing оцениваются по Lexical Resource. Работа над тем, '
         'чтобы сказать одну мысль тремя способами, засчитывается в обеих '
         'аудиториях &mdash; прежде всего в части 3 и в Task 2, где идеи '
         'абстрактные.',
    t3an='Это же проверяет и Reading, только с другой стороны.',
    t3bh='Перефразируйте вопрос, а не копируйте его',
    t3bb='Слова, взятые прямо из задания, не засчитываются как ваша лексика. '
         'Вступление, которое пересказывает вопрос вашими словами, оценивается; '
         'вступление, которое его повторяет, &mdash; нет.',
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

    v1why='Менее частотная лексика, употреблённая <em>точно</em> и '
          '<em>гибко</em>. Количество и редкость &mdash; не критерии; точность '
          '&mdash; критерий, и неточность наказывается прямо.',
    v2why='<em>Ameliorate</em> сочетается с ситуацией или состоянием, а не с '
          'предметом. Попытка видна, промах тоже, и платят за это в Lexical '
          'Resource.',
    v3why='Простое и совершенно точное слово. Дескриптор &mdash; это точность; '
          'синоним из словаря, которым вы не владеете, &mdash; самый частый '
          'способ потерять баллы, пытаясь их набрать.',
    v4why='Они выбиваются из английского вокруг, и экзаменаторов учат это '
          'слышать. Фраза не запрещена &mdash; просто она не засчитывается как '
          'ваш собственный язык.',
    v5why='<em>Conduct research</em>. Глагол задан существительным, а <em>make '
          'research</em> отнимает баллы чаще всего, потому что во многих других '
          'языках так правильно.',
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
    v10why='И Speaking, и Writing оцениваются по Lexical Resource, так что одна и '
           'та же практика засчитывается на двух экзаменах &mdash; а больше всего '
           'перефразирование работает в части 3 и в Task 2.',
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
    sortWhy='Всё слева &mdash; про то, чтобы <strong>пользоваться</strong> '
            'языком; всё справа &mdash; про то, чтобы им '
            '<strong>красоваться</strong>. Дескрипторы спрашивают, можете ли вы '
            'сказать то, что имеете в виду, точно и гибко, &mdash; поэтому '
            'простое слово в цель лучше редкого мимо, а фраза, выученная целиком, '
            'лучше слова, выученного отдельно. Именно на правый столбец уходит '
            'большая часть времени подготовки.',

    actTitle='Соберите одну страницу запаса',
    actUse='Используйте хотя бы три:',
    actSpeakBrief='В парах. Возьмите тему &mdash; пробки, старение, '
                  'автоматизация, туризм. Пять минут, чтобы вместе собрать '
                  'страницу: три идеи и к каждой две фразы, а не два слова. '
                  'Потом две минуты спорьте на эту тему, используя только то, '
                  'что есть на странице.',
    actSpeak1='Каждая фраза на странице должна быть сочетанием &mdash; глагол со '
              'своим существительным или прилагательное со своим '
              'существительным. Никаких отдельных слов.',
    actSpeak2='Партнёр останавливает вас каждый раз, когда вы берёте слово не со '
              'страницы, и вам нужно сказать это снова словом, которое там '
              'есть.',
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
    coverSub='ربع الدرجات في Speaking وفي Writing، وليس هو الربع الذي يكافئ '
             'الكلمات النادرة',
    chipLevel='C1 · متقدّم', chipFocus='Speaking وWriting',
    chipCount='18 نقطة',

    t1Eyebrow='قبل أن تبدأ',
    t1Title='لا يكافئ الكلمات النادرة. ولم يفعل قط.',
    t1ah='ما تطلبه معايير التقييم',
    t1ab='مفردات متنوعة تُستخدم <strong>بدقة</strong> و<strong>مرونة</strong>، '
         'وكلمات <em>أقل شيوعًا</em> حيث تناسب. وأخطاء اختيار الكلمة والتلازم '
         'اللفظي مذكورة بالاسم في كل مستوى.',
    t1an='الكلمة النادرة التي تخطئ هدفها تنال أقل من الكلمة البسيطة التي تصيبه.',
    t1bh='شبه الإصابة يكلّف أكثر من الكلمة البسيطة',
    t1bb='المتقدّم الذي يكتب <em>ameliorate the traffic</em> مدّ يده إلى فعل '
         'نادر وألصقه بمفعول خاطئ. يرى الممتحن المحاولة ويرى الخطأ. أما '
         '<em>ease the traffic</em> فبسيطة وصحيحة وتنال أكثر.',
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
    t2ab='في الإنجليزية تقول <em>conduct</em> research و<em>reach</em> a '
         'decision و<em>draw</em> a conclusion. لا فعل منها نادر؛ الثلاثة ثابتة، '
         'ولا واحد منها هو ما يعطيك إياه القاموس للاسم.',
    t2an='أكثر ما يكلّف الدرجات هو <em>make research</em> و<em>do a '
         'decision</em>.',
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
    t3ah='الاختباران كلاهما يقيّمانها',
    t3ab='يُقيَّم Speaking وWriting كلاهما على Lexical Resource. فالعمل على قول '
         'فكرة واحدة بثلاث طرق يُحتسب في القاعتين، ولا سيما في الجزء 3 وفي Task '
         '2، حيث الأفكار مجرّدة.',
    t3an='وهو أيضًا ما يختبره Reading، من الجهة الأخرى.',
    t3bh='أعد صياغة السؤال ولا تنسخه',
    t3bb='الكلمات المأخوذة كما هي من نص السؤال لا تُحسب من مفرداتك. المقدّمة '
         'التي تعيد صياغة السؤال بكلماتك تُقيَّم، أما التي تكرّره فلا.',
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

    v1why='مفردات أقل شيوعًا تُستخدم <em>بدقة</em> و<em>مرونة</em>. فالعدد '
          'والندرة ليسا معيارين، أما الدقة فمعيار، وقلّة الدقة يُعاقَب عليها '
          'بالاسم.',
    v2why='الفعل <em>ameliorate</em> يأتي مع وضع أو حالة، لا مع شيء. المحاولة '
          'ظاهرة والخطأ كذلك، وثمنه يُدفع في Lexical Resource.',
    v3why='الكلمة البسيطة والصحيحة تمامًا. المعيار هو الدقة، والمرادف المأخوذ من '
          'القاموس الذي لا يتحكّم فيه الكاتب هو أكثر الطرق شيوعًا لخسارة '
          'الدرجات أثناء محاولة كسبها.',
    v4why='إنها تنفصل عن الإنجليزية من حولها، والممتحنون مدرَّبون على سماع ذلك. '
          'العبارة ليست ممنوعة، لكنها ببساطة لا تُحسب من لغتك أنت.',
    v5why='الصحيح <em>conduct research</em>. الفعل يفرضه الاسم، و<em>make '
          'research</em> هي الصيغة الأكثر تكلفةً، لأنها صحيحة في عدة لغات '
          'أخرى.',
    v6why='عبارة <em>strong rain</em> هي التي لا تقولها الإنجليزية، فالمطر يأخذ '
          '<em>heavy</em>. أما الأدلة والآراء والروائح فتأخذ كلها '
          '<em>strong</em>، ولا قاعدة تخبرك أيّ اسم يأخذ أيّها.',
    v7why='الفعل أو الصفة. الاسم هو عادةً الجزء الذي يعرفه المتعلّم أصلًا، وما '
          'يجب تعلّمه معه هو الكلمة التي يصادف أن يأخذها.',
    v8why='داخل عبارة. الكلمة مع ترجمتها كلمة تتعرّف عليها، أما الكلمة في صحبتها '
          'المعتادة فكلمة تستطيع إنتاجها، وهذه وحدها هي التي تُقيَّم.',
    v9why='إنها تغيّر القواعد والكلمات معًا: سؤال عمّا يظنّه الناس يصبح عبارة '
          'عمّا هو موضع خلاف. أما الثلاث الأخرى فتخلط نص السؤال وتعيده إليك.',
    v10why='يُقيَّم Speaking وWriting كلاهما على Lexical Resource، فالتمرين '
           'نفسه يُحتسب في اختبارين، والجزء 3 وTask 2 هما حيث تؤدّي إعادة '
           'الصياغة أكبر دور.',
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
    sortWhy='كل ما في عمود «يرفع المستوى» يتعلّق <strong>باستخدام</strong> اللغة، '
            'وكل ما في عمود «لا يفيد أو يكلّفك» يتعلّق <strong>باستعراضها</strong>. '
            'المعايير تسأل هل تستطيع أن تقول ما تعنيه بدقة ومرونة، ولذلك فالكلمة '
            'البسيطة التي تصيب تتفوّق على النادرة التي تخطئ، والعبارة المتعلَّمة '
            'كاملةً تتفوّق على الكلمة المتعلَّمة وحدها. وفي العمود الثاني يذهب '
            'معظم وقت المراجعة.',

    actTitle='ابنِ صفحة واحدة من الرصيد',
    actUse='استخدم ثلاثة منها على الأقل:',
    actSpeakBrief='اعملا في ثنائي. اختارا موضوعًا: الازدحام، أو الشيخوخة، أو '
                  'الأتمتة، أو السياحة. لديكما خمس دقائق لبناء صفحة معًا: ثلاث '
                  'أفكار، ولكل فكرة عبارتان لا كلمتان. ثم ناقشا الموضوع دقيقتين '
                  'مستخدمين ما في صفحتكما فقط.',
    actSpeak1='كل عبارة في الصفحة يجب أن تكون تلازمًا: فعلًا مع اسمه، أو صفةً مع '
              'اسمها. لا كلمات مفردة.',
    actSpeak2='يوقفك زميلك كلما استخدمت كلمة ليست في الصفحة، وعليك أن تقولها من '
              'جديد بكلمة موجودة فيها.',
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
    coverSub='口语和写作各占四分之一的分数——而这四分之一奖励的并不是生僻词',
    chipLevel='C1 · 高级', chipFocus='Speaking 与 Writing',
    chipCount='18 分',

    t1Eyebrow='开始之前',
    t1Title='它不奖励生僻词，从来都不。',
    t1ah='评分标准要求什么',
    t1ab='丰富的词汇，用得<strong>准确</strong>而<strong>灵活</strong>，在合适的'
         '地方用上<em>不太常见</em>的词。用词和搭配错误在每个分数段的描述里都'
         '被点名。',
    t1an='用错的生僻词，得分低于用对的普通词。',
    t1bh='差一点的词比普通词代价更大',
    t1bb='写出 <em>ameliorate the traffic</em> 的考生，去够了一个生僻动词，却接错'
         '了宾语。考官看得见这份努力，也看得见这个失误。<em>Ease the traffic</em> '
         '朴素、正确，得分反而更高。',
    t1bn='先用你有把握的词，确定搭配无误后再往上够。',
    t1ch='背下来的句子听得出来',
    t1cb='“9 分句型”清单里的句子和周围的回答格格不入，而考官受过的训练正是听出'
         '这一点。把一句塞进朴素的回答里，考官就知道哪种语言才是你真正的水平。',
    t1cn='露馅的是不协调，而不是句子本身。',

    t2Eyebrow='开始之前',
    t2Title='基本单位是搭配，不是单词',
    t2ah='名词决定动词',
    t2ab='英语说 <em>conduct</em> research、<em>reach</em> a decision、'
         '<em>draw</em> a conclusion。这些动词都不生僻；三个都是固定搭配，而且没有'
         '一个是词典给你的那个对应词。',
    t2an='最常丢分的是 <em>make research</em> 和 <em>do a decision</em>。',
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
    t3ah='两门考试都给它打分',
    t3ab='口语和写作都按 Lexical Resource 评分。把一个意思说成三种说法的练习，'
         '在两个考场里都算分——尤其是 Part 3 和 Task 2，那里的话题都很抽象。',
    t3an='阅读考的也是它，只是从另一个方向。',
    t3bh='改写题目，不要照抄',
    t3bb='直接从题目里搬来的词不算你的词汇。用自己的话重述题目的开头能得分；'
         '重复题目的开头则不能。',
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

    v1why='不太常见的词汇，用得<em>准确</em>、<em>灵活</em>。数量和生僻程度都不是'
          '标准；准确才是，不准确会被点名扣分。',
    v2why='<em>Ameliorate</em> 的对象是一种状况或状态，而不是一样东西。努力看得见，'
          '失误也看得见，代价记在 Lexical Resource 上。',
    v3why='朴素而完全准确的词。标准是准确；用一个自己驾驭不了的同义词替换，是'
          '想加分却丢分最常见的方式。',
    v4why='它们和周围的英语格格不入，而考官受过的训练正是听出这一点。这类句子'
          '并没有被禁止——只是不算你自己的语言。',
    v5why='<em>Conduct research</em>。动词由名词决定，而 <em>make research</em> '
          '是最常丢分的说法，因为在好几种语言里这样说是对的。',
    v6why='英语不说的是 <em>strong rain</em>——雨要用 <em>heavy</em>。证据、观点、'
          '气味都用 <em>strong</em>，没有规则告诉你哪个名词配哪个。',
    v7why='动词或形容词。名词通常是学习者已经会的部分——要跟着它一起学的，'
          '是它恰好搭配的那个词。',
    v8why='放在短语里。带翻译的单词是你认得的词；和它的固定搭配一起记住的词，'
          '才是你说得出、写得出的词，而只有这种才算分。',
    v9why='它不但换了词，还换了语法：一个关于人们怎么想的问题，变成了一个关于'
          '哪里有争议的陈述。另外三个只是把题目打乱再还给你。',
    v10why='口语和写作都按 Lexical Resource 评分，所以同样的练习在两门考试里'
           '都算数——而改写最能发挥作用的地方就是 Part 3 和 Task 2。',
    v11why='按观点。归在 <em>congestion</em> 下的词带着论点一起来；归在字母 C 下'
           '的词孤零零地来，而时间紧迫时，你缺的正是论点。',
    v12why='描述它的作用。改写正是这项标准所奖励的——母语里的词不是英语，发问'
           '不等于回答，猜出来的生僻词又是那个“差一点”。',

    sortEyebrow='练习 4 · 复习时间该花在哪里',
    sortTitle='给这六个习惯分类',
    sortHint='把每一项拖到一栏里——或者先点一项，再点你想放进的那一栏。',
    sortBin1='能提高分数段',
    sortBin2='没有用，甚至丢分',
    sortWhy='左边讲的都是<strong>使用</strong>语言；右边讲的都是<strong>炫耀'
            '</strong>语言。评分标准问的是你能不能准确、灵活地说出想说的意思——'
            '所以用对的普通词胜过用错的生僻词，整体学会的短语胜过孤立学会的单'
            '词。而大部分复习时间，恰恰花在了右栏。',

    actTitle='建起词库的一页',
    actUse='至少用上三个：',
    actSpeakBrief='两人一组。选一个话题——交通拥堵、人口老龄化、自动化、旅游。'
                  '用五分钟一起建一页：三个观点，每个观点配两个短语而不是两个'
                  '单词。然后就这个话题争论两分钟，只能用这一页上的内容。',
    actSpeak1='这一页上的每个短语都必须是搭配——动词加它的名词，或者形容词加它'
              '的名词。不要孤立的单词。',
    actSpeak2='只要你用了页面上没有的词，同伴就打断你，你必须换一个页面上有的'
              '词重说。',
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
    coverSub='Speaking でも Writing でも点数の4分の1。しかも、それは難しい単語に'
             '点をくれる4分の1ではありません',
    chipLevel='C1 · 上級', chipFocus='Speaking・Writing',
    chipCount='18 点',

    t1Eyebrow='始める前に',
    t1Title='難しい単語に点はつかない。これまでも、これからも。',
    t1ah='評価基準が求めるもの',
    t1ab='幅広い語彙を<strong>正確</strong>かつ<strong>柔軟</strong>に使い、合う'
         '場面では<em>あまり一般的でない</em>語も使うこと。語の選択やコロケーション'
         'の誤りは、どのバンドの記述にも明記されています。',
    t1an='外した難語は、当たった平易な語より点が低くなります。',
    t1bh='惜しい語は平易な語より高くつく',
    t1bb='<em>ameliorate the traffic</em> と書く受験者は、難しい動詞に手を伸ば'
         'し、間違った目的語につなげています。試験官には背伸びも失敗も見えます。'
         '<em>Ease the traffic</em> は平易で正しく、点も高くなります。',
    t1bn='確信のある語を使い、ぴったり合うとわかってから一歩広げましょう。',
    t1ch='丸暗記した表現は聞けばわかる',
    t1cb='「バンド9」表現集のフレーズは、周りの答えから浮いてしまいます。試験官'
         'はまさにそこを聞き取る訓練を受けています。平易な答えに一つ混ぜれば、どち'
         'らが本当のあなたの言葉かが伝わってしまいます。',
    t1cn='見破られるのはちぐはぐさであって、フレーズそのものではありません。',

    t2Eyebrow='始める前に',
    t2Title='単位は単語ではなく組み合わせ',
    t2ah='名詞が動詞を選ぶ',
    t2ab='英語では <em>conduct</em> research、<em>reach</em> a decision、'
         '<em>draw</em> a conclusion と言います。どの動詞も難しくはありませんが、'
         '三つとも決まった組み合わせで、辞書がその名詞に対して示す動詞ではありま'
         'せん。',
    t2an='最も点を落としやすいのは <em>make research</em> と <em>do a '
         'decision</em> です。',
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
    t3ah='二つの試験で採点される',
    t3ab='Speaking も Writing も Lexical Resource で採点されます。一つの考えを三'
         '通りに言う練習は、どちらの試験会場でも点になります――特に、話題が抽象的'
         'な Part 3 と Task 2 で。',
    t3an='Reading がテストしているのも、反対側から見た同じ技能です。',
    t3bh='問題文を写さず、言い換える',
    t3bb='問題文からそのまま取った語は、あなたの語彙として数えられません。問いを'
         '自分の言葉で言い直した書き出しは評価され、繰り返しただけの書き出しは評'
         '価されません。',
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

    v1why='あまり一般的でない語彙を<em>正確</em>かつ<em>柔軟</em>に使うこと。数や'
          '珍しさは基準ではありません。基準は正確さで、不正確さははっきり減点され'
          'ます。',
    v2why='<em>Ameliorate</em> がとるのは状況や状態で、物ではありません。背伸び'
          'も失敗も見え、その代償は Lexical Resource で払うことになります。',
    v3why='平易で、しかもぴったり正しい語です。基準は正確さで、使いこなせない類'
          '語への置き換えは、点を取ろうとして点を失う最もよくある形です。',
    v4why='周りの英語から浮いてしまい、試験官はそれを聞き取る訓練を受けていま'
          'す。フレーズが禁止されているわけではなく、あなた自身の言葉として数えら'
          'れないだけです。',
    v5why='<em>Conduct research</em>。動詞は名詞で決まります。<em>make '
          'research</em> は最も点を落としやすい形で、ほかのいくつもの言語ではそれ'
          'が正しいからです。',
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
    v10why='Speaking も Writing も Lexical Resource で採点されるので、同じ練習が'
           '二つの試験で点になります――そして言い換えが最も効くのは Part 3 と '
           'Task 2 です。',
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
    sortWhy='左はすべて言葉を<strong>使う</strong>こと、右はすべて言葉を<strong>'
            '見せびらかす</strong>ことです。評価基準が問うのは、言いたいことを正確'
            'かつ柔軟に言えるかどうか――だから、当たった平易な語は外れた難語に勝'
            'ち、丸ごと覚えたフレーズは単独で覚えた語に勝ちます。そして復習時間の'
            '大半が費やされているのは右の列です。',

    actTitle='語彙集を一ページ作る',
    actUse='少なくとも三つ使いましょう：',
    actSpeakBrief='ペアで。テーマを一つ選びます――交通渋滞、高齢化、自動化、観光。'
                  '五分で一緒に一ページ作ります：アイデアを三つ、それぞれに単語二'
                  'つではなくフレーズ二つ。そのあと二分間、ページにあるものだけを'
                  '使ってそのテーマについて議論しましょう。',
    actSpeak1='ページのどのフレーズも組み合わせにすること――動詞とその名詞、または'
              '形容詞とその名詞。単語だけはなしです。',
    actSpeak2='ページにない語を使うたびに相手が止め、あなたはページにある語で言い'
              '直さなければなりません。',
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
