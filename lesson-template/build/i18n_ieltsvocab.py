# -*- coding: utf-8 -*-
"""Interface strings for IELTS Vocabulary: Lexical Resource.

English, German and Spanish, teach cards in the six-item form.

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
    coverTitle='Lexical <em>Resource</em>',
    coverSub='A quarter of the marks in Speaking and in Task 2, and it is not '
             'the quarter that rewards rare words',
    chipLevel='C1 · Advanced', chipFocus='Speaking &amp; Writing Task 2',
    chipCount='18 points',

    t1Eyebrow='Before you start',
    t1Title='It does not reward rare words. It never has.',
    t1ah='What the descriptors ask for',
    t1ab='<em>Less common</em> vocabulary, used with <strong>precision</strong> '
         'and <strong>flexibility</strong>. Two of those three words are about '
         'accuracy, and inaccuracy is penalised by name.',
    t1an='Rarity with a miss scores below plainness with a hit. Every time.',
    t1bh='The near-miss costs more than the plain word',
    t1bb='A candidate who writes <em>ameliorate the traffic</em> has reached '
         'for a rare verb and attached it to the wrong object. The examiner '
         'sees the reach and the miss. <em>Ease the traffic</em> is plain, '
         'right, and scores higher.',
    t1bn='Reach for the word you are sure of, then stretch once you are '
         'certain of the fit.',
    t1ch='Memorised phrases are audible',
    t1cb='Band 9 phrase lists sit apart from the answer around them, and '
         'examiners are trained to hear exactly that. A learnt phrase in a '
         'plain answer marks the plain answer as the real one.',
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
    t3ab='Speaking Part 3 and Writing Task 2 carry the same criterion. The '
         'work you do on saying one idea three ways is marked in both rooms, '
         'which is the best return on revision time in the whole exam.',
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
    v10why='Speaking Part 3 and Task 2 are marked on the same criterion, so '
           'the same practice raises two bands. Nothing else in the exam pays '
           'twice like that.',
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

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Lexical <em>Resource</em>',
    coverSub='Ein Viertel der Note im Speaking und in Task 2 &mdash; und nicht '
             'das Viertel, das seltene Wörter belohnt',
    chipLevel='C1 · Fortgeschritten', chipFocus='Speaking &amp; Writing Task 2',
    chipCount='18 Punkte',

    t1Eyebrow='Bevor du beginnst',
    t1Title='Seltene Wörter werden nicht belohnt. Nie gewesen.',
    t1ah='Was die Deskriptoren verlangen',
    t1ab='<em>Weniger gebräuchlicher</em> Wortschatz, verwendet mit '
         '<strong>Präzision</strong> und <strong>Flexibilität</strong>. Zwei '
         'dieser drei Begriffe betreffen Genauigkeit, und Ungenauigkeit wird '
         'ausdrücklich abgezogen.',
    t1an='Selten und daneben liegt unter schlicht und richtig. Jedes Mal.',
    t1bh='Der Fastreffer kostet mehr als das schlichte Wort',
    t1bb='Wer <em>ameliorate the traffic</em> schreibt, hat nach einem seltenen '
         'Verb gegriffen und es an das falsche Objekt gehängt. Der Prüfer '
         'sieht den Griff und den Fehlgriff. <em>Ease the traffic</em> ist '
         'schlicht, richtig und bringt mehr.',
    t1bn='Greif zum Wort, bei dem du sicher bist, und streck dich erst, wenn '
         'du die Passung kennst.',
    t1ch='Auswendiges hört man',
    t1cb='Listen mit „Band-9-Phrasen“ stehen neben der Antwort, die sie '
         'umgibt, und Prüfer sind darauf geschult, genau das zu hören. Eine '
         'gelernte Phrase in einer schlichten Antwort markiert die schlichte '
         'als die echte.',
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
    t3ab='Speaking Teil 3 und Writing Task 2 tragen dasselbe Kriterium. Die '
         'Arbeit daran, eine Idee auf drei Arten zu sagen, wird in beiden '
         'Räumen bewertet &mdash; die beste Rendite auf Lernzeit in der ganzen '
         'Prüfung.',
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
    v10why='Speaking Teil 3 und Task 2 werden nach demselben Kriterium '
           'bewertet, dieselbe Übung hebt also zwei Noten. Nichts sonst in '
           'der Prüfung zahlt so doppelt.',
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
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Lexical <em>Resource</em>',
    coverSub='Una cuarta parte de la nota en Speaking y en Task 2, y no es la '
             'cuarta parte que premia las palabras raras',
    chipLevel='C1 · Avanzado', chipFocus='Speaking y Writing Task 2',
    chipCount='18 puntos',

    t1Eyebrow='Antes de empezar',
    t1Title='No premia las palabras raras. Nunca lo ha hecho.',
    t1ah='Qué piden los descriptores',
    t1ab='Vocabulario <em>menos frecuente</em>, usado con '
         '<strong>precisión</strong> y <strong>flexibilidad</strong>. Dos de '
         'esas tres palabras van de exactitud, y la inexactitud se penaliza '
         'por su nombre.',
    t1an='Raro y fallado puntúa menos que llano y acertado. Siempre.',
    t1bh='El casi-acierto cuesta más que la palabra llana',
    t1bb='Quien escribe <em>ameliorate the traffic</em> ha ido a por un verbo '
         'raro y lo ha pegado al objeto equivocado. El examinador ve el '
         'intento y el fallo. <em>Ease the traffic</em> es llano, correcto y '
         'puntúa más.',
    t1bn='Ve a por la palabra de la que estés seguro y estírate solo cuando '
         'sepas que encaja.',
    t1ch='Las frases memorizadas se oyen',
    t1cb='Las listas de «frases de band 9» quedan aparte del inglés que las '
         'rodea, y a los examinadores se les entrena para oír justo eso. Una '
         'frase aprendida dentro de una respuesta llana señala a la llana como '
         'la de verdad.',
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
    t3ab='Speaking Parte 3 y Writing Task 2 llevan el mismo criterio. El '
         'trabajo de decir una idea de tres maneras se califica en las dos '
         'salas: el mejor rendimiento por hora de estudio de todo el examen.',
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
    v10why='Speaking Parte 3 y Task 2 se califican con el mismo criterio, así '
           'que la misma práctica sube dos notas. Nada más en el examen paga '
           'así de doble.',
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
