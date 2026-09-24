# -*- coding: utf-8 -*-
"""Interface strings for IELTS Reading: True / False / Not Given.

Ten languages: English, German and Spanish from the start; French,
Italian, Portuguese, Russian, Arabic, Chinese and Japanese added on
2026-09-24 (conventions in `ielts_langs.py`).

Same split as the rest of the IELTS route (HOUSE-STYLE §8): the rule and the
reason travel, the English under test does not. The passages and the statements
in the items stay English in every gloss — a Spanish rendering of the passage
would hand over the answer, because the whole skill is reading the English
sentence and deciding whether it says the thing.

The three verdicts are translated, though, and deliberately: <em>True</em>,
<em>False</em> and <em>Not Given</em> are the instruction, not the text under
test, and a learner who has not met "Not Given" before needs to know what it
claims before the first item, not after it.
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
    coverTitle='True, False, <em>Not Given</em>',
    coverSub='The question type that loses the most marks on the Reading '
             'paper &mdash; and the one that technique, not vocabulary, gets '
             'back',
    chipLevel='C1 · Advanced', chipFocus='Reading · both modules',
    chipCount='18 points',

    t1Eyebrow='Before you start',
    t1Title='Sixty minutes, three sections, no time at the end',
    t1ah='The shape of the paper',
    t1ab='Forty questions in sixty minutes, in three sections of about twenty '
         'minutes each. The third is usually the hardest &mdash; so a section '
         'that runs long is borrowing from the one that needs it most.',
    t1an='Academic sets one long passage per section; General Training starts '
         'with shorter texts. The technique is the same, so everything here '
         'applies to both.',
    t1bh='No transfer time. None.',
    t1bb='On paper, Listening gives you ten minutes at the end to copy your '
         'answers across. <strong>Reading does not.</strong> Write on the '
         'answer sheet as you go, because the invigilator stops you on the '
         'hour with whatever is on it.',
    t1bn='Answers left on the question paper score nothing. It is the single '
         'cheapest way to lose marks on this paper.',
    t1ch='The questions follow the text',
    t1cb='Most question types run in passage order, this one included. Answer '
         'four and you know roughly where the fifth is &mdash; you never have '
         'to search the whole passage twice.',
    t1cn='Matching Headings and Matching Information are the exceptions. They '
         'jump around.',

    t2Eyebrow='Before you start',
    t2Title='False and Not Given are not the same answer',
    t2ah='FALSE: the passage says otherwise',
    t2ab='There is a sentence in the text that <strong>contradicts</strong> '
         'the statement. You can put your finger on it. If someone asked you '
         'to prove the statement wrong, you would point at that line.',
    t2an='A number that disagrees, a date that does not match, an "only" '
         'against a "several" &mdash; all contradictions.',
    t2bh='NOT GIVEN: the passage is silent',
    t2bb='The text neither says it nor denies it. The statement may well be '
         'true out in the world; the passage simply does not go there.',
    t2bn='Not Given is not a punishment for missing something. It is a real '
         'answer, and roughly a third of them are.',
    t2ch='The test is one question',
    t2cb='<strong>Can I point at the sentence?</strong> If yes, the answer is '
         'True or False depending on what it says. If you are reasoning &mdash; '
         '&ldquo;well, it must be&rdquo; &mdash; the answer is Not Given.',
    t2cn='Reasoning feels like understanding, which is exactly why it costs so '
         'many marks here.',

    t3Eyebrow='Before you start',
    t3Title='Answer from the passage, never from what you know',
    t3ah='Your knowledge is the trap',
    t3ab='A statement can be perfectly true in the world and still Not Given '
         'in the text. The examiner is not asking whether it is true. They '
         'are asking what this passage says.',
    t3an='This is why candidates score worse on topics they know well.',
    t3bh='TRUE means the text says it',
    t3bb='Said in different words, almost always. The passage will not repeat '
         'the statement; it will paraphrase it. Matching meaning is the '
         'skill &mdash; matching words is a habit to break.',
    t3bn='<em>Attendance fell sharply after 1990</em> and <em>far fewer '
         'people came in the years that followed</em> are the same claim '
         'with no word in common.',
    t3ch='Word-matching fails both ways',
    t3cb='The same words can sit in a sentence that says the opposite, and a '
         'sentence with no shared words at all can state the claim exactly. '
         'Shared vocabulary tells you where to look, never what to answer.',
    t3cn='Use the repeated word to find the line. Then read the line.',

    t4Eyebrow='Before you start',
    t4Title='One word decides a third of these',
    t4ah='Absolutes',
    t4ab='<em>All</em>, <em>every</em>, <em>never</em>, <em>only</em>. A '
         'passage that says <em>most</em> makes a statement saying <em>all</em> '
         'FALSE &mdash; the two cannot both hold, and that is a contradiction '
         'you can point at.',
    t4an='<em>Most islanders</em> against <em>every islander</em> is a False, '
         'not a Not Given.',
    t4bh='Hedges',
    t4bb='<em>May</em>, <em>might</em>, <em>is thought to</em>, <em>suggests</em>. '
         'A hedged passage does not deny a confident statement &mdash; it just '
         'never makes it. That shape is usually Not Given.',
    t4bn='The difference from an absolute: <em>most</em> excludes <em>all</em>, '
         'but <em>may</em> excludes nothing.',
    t4ch='Comparatives need both sides',
    t4cb='<em>Wetter than</em>, <em>the largest</em>, <em>more common than</em>. '
         'Check that the passage actually compares the same two things &mdash; '
         'a text about one of them cannot support a claim about the pair.',
    t4cn='A passage naming one figure and a statement ranking two is a Not '
         'Given every time.',

    mcaEyebrow='Activity 1 · False, or Not Given?',
    mcaTitle='Read the passage. Then read the statement.',
    mcbEyebrow='Activity 2 · The passage, not the world',
    mcbTitle='What does this text actually say?',
    mccEyebrow='Activity 3 · The word that decides it',
    mccTitle='Most, all, may, never',

    r1why='The passage says it never closed, <em>not even during the two '
          'wars</em>. That is the statement, in different words. TRUE.',
    r2why='Twice a day in summer, says the passage. Three is a number that '
          'disagrees with a number in the text, which is a contradiction you '
          'can point at. FALSE.',
    r3why='The passage counts the Welsh volumes. It says nothing at all about '
          'what the library intends to do next. NOT GIVEN.',
    r4why='Began in 1954, finished two years later. The passage gives you the '
          'arithmetic rather than the date, and paraphrase includes doing the '
          'sum. TRUE.',
    r5why='The passage says polarised light stays usable <em>when the sun is '
          'behind cloud</em> &mdash; which is the opposite of the statement. '
          'FALSE, and note that it never uses the word "overcast".',
    r6why='The mill, the village and the dependence are all in the passage. A '
          'sale, a competitor and 1902 are not. NOT GIVEN.',
    r7why='Seventy per cent is most. The statement paraphrases the figure '
          'rather than repeating it, which is what TRUE usually looks like.',
    r8why='The passage says what the survey covered, not who paid for it. '
          'Funding is a reasonable thing to wonder about and the text does not '
          'go there. NOT GIVEN.',
    r9why='<em>Most</em> in the passage against <em>every</em> in the '
          'statement. An absolute is contradicted by a majority, so this is a '
          'FALSE rather than a Not Given.',
    r10why='The passage hedges about recovery time and says nothing whatever '
           'about approval. Silence, not denial. NOT GIVEN.',
    r11why='Less rain in the valley means a wetter coast &mdash; the same '
           'claim turned round. The words that carry it, <em>lower</em> and '
           '<em>wetter</em>, have nothing in common, which is why '
           'word-matching misses it. TRUE.',
    r12why='<em>Apart from two years in the 1980s</em> is the line you point '
           'at. <em>Never once</em> cannot survive it. FALSE.',

    sortEyebrow='Activity 4 · What tips you which way',
    sortTitle='Sort the six signals',
    sortHint='Drag each one into a column &mdash; or click an item, then the '
             'column you want it in.',
    sortBin1='Points to FALSE',
    sortBin2='Points to NOT GIVEN',

    actTitle='Prove it from the text',
    actUse='Use at least three:',
    actSpeakBrief='In pairs, with any passage you have to hand &mdash; a news '
                  'article will do. One of you writes four statements about '
                  'it: one true, one false, two not given. Swap, answer, and '
                  'then defend each verdict by reading out the line you based '
                  'it on. No line, no FALSE.',
    actSpeak1='Whoever answers must say which sentence decided it, out loud, '
              'before the verdict is accepted.',
    actSpeak2='For every NOT GIVEN, say what the passage would have had to '
              'contain for the answer to be FALSE instead.',
    actSpeak3='Find one statement in your partner&rsquo;s set that you could '
              'argue either way, and rewrite it so that it cannot be.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Take one passage and write three statements about it &mdash; '
                  'one TRUE, one FALSE, one NOT GIVEN &mdash; then write the '
                  'answer key, naming for each one the exact sentence that '
                  'decides it, or saying plainly that no sentence does.',
    actPlaceholder='Statement 1 (TRUE): … The line that decides it: …',
)

# The verdicts and the sort explanation sit in the data module, which keeps
# the only copy of the English. Until 2026-09-23 neither translated: the
# options were bare English in the markup and SORT_WHY a plain string.
from ieltsread_data import VERDICTS, SORT_WHY
T['en'].update(VERDICTS)
T['en']['sortWhy'] = SORT_WHY

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='True, False, <em>Not Given</em>',
    coverSub='Der Fragetyp, der im Reading die meisten Punkte kostet &mdash; '
             'und den Technik zurückholt, nicht Wortschatz',
    chipLevel='C1 · Fortgeschritten', chipFocus='Reading · beide Module',
    chipCount='18 Punkte',

    t1Eyebrow='Bevor du beginnst',
    t1Title='Sechzig Minuten, drei Teile, keine Zeit am Ende',
    t1ah='Der Aufbau der Prüfung',
    t1ab='Vierzig Fragen in sechzig Minuten, in drei Teilen zu je etwa '
         'zwanzig Minuten. Der dritte ist meist der schwerste &mdash; wer bei '
         'einem Teil überzieht, nimmt die Zeit genau dem weg, der sie braucht.',
    t1an='Academic gibt pro Teil einen langen Text; General Training beginnt '
         'mit kürzeren Texten. Die Technik ist dieselbe, also gilt alles hier '
         'für beide.',
    t1bh='Keine Übertragungszeit. Keine.',
    t1bb='Beim Listening auf Papier bekommst du am Ende zehn Minuten, um die '
         'Antworten zu übertragen. <strong>Beim Reading nicht.</strong> Schreib direkt '
         'auf den Antwortbogen &mdash; nach sechzig Minuten wird '
         'eingesammelt, mit dem, was daraufsteht.',
    t1bn='Antworten, die auf dem Fragebogen bleiben, zählen nicht. Der '
         'billigste Punkteverlust der ganzen Prüfung.',
    t1ch='Die Fragen folgen dem Text',
    t1cb='Die meisten Fragetypen laufen in Textreihenfolge, dieser auch. Nach '
         'vier Antworten weißt du ungefähr, wo die fünfte steht &mdash; du '
         'musst nie zweimal den ganzen Text absuchen.',
    t1cn='Matching Headings und Matching Information sind die Ausnahmen. Die '
         'springen.',

    t2Eyebrow='Bevor du beginnst',
    t2Title='False und Not Given sind nicht dieselbe Antwort',
    t2ah='FALSE: der Text sagt das Gegenteil',
    t2ab='Es gibt einen Satz im Text, der die Aussage '
         '<strong>widerlegt</strong>. Du kannst mit dem Finger darauf zeigen. '
         'Müsstest du beweisen, dass die Aussage falsch ist, zeigtest du auf '
         'genau diese Zeile.',
    t2an='Eine Zahl, die nicht passt, ein Datum, das nicht stimmt, ein „nur“ '
         'gegen ein „mehrere“ &mdash; alles Widersprüche.',
    t2bh='NOT GIVEN: der Text schweigt',
    t2bb='Der Text sagt es weder, noch bestreitet er es. Die Aussage mag in '
         'der Welt völlig zutreffen &mdash; dieser Text geht schlicht nicht '
         'darauf ein.',
    t2bn='Not Given ist keine Strafe dafür, etwas übersehen zu haben. Es ist '
         'eine echte Antwort, und etwa ein Drittel sind es.',
    t2ch='Die Prüfung ist eine einzige Frage',
    t2cb='<strong>Kann ich auf den Satz zeigen?</strong> Wenn ja, heißt die '
         'Antwort True oder False, je nachdem, was dort steht. Wenn du '
         'schließt &mdash; „das muss doch“ &mdash; heißt sie Not Given.',
    t2cn='Schließen fühlt sich nach Verstehen an. Genau deshalb kostet es hier '
         'so viele Punkte.',

    t3Eyebrow='Bevor du beginnst',
    t3Title='Antworte aus dem Text, nie aus deinem Wissen',
    t3ah='Dein Wissen ist die Falle',
    t3ab='Eine Aussage kann in der Welt völlig richtig und im Text trotzdem '
         'Not Given sein. Gefragt ist nicht, ob sie stimmt, sondern was '
         'dieser Text sagt.',
    t3an='Deshalb schneiden Kandidaten bei Themen, die sie gut kennen, oft '
         'schlechter ab.',
    t3bh='TRUE heißt: der Text sagt es',
    t3bb='Fast immer mit anderen Worten. Der Text wiederholt die Aussage '
         'nicht, er paraphrasiert sie. Bedeutung abgleichen ist die '
         'Fertigkeit &mdash; Wörter abgleichen ist die Gewohnheit, die weg '
         'muss.',
    t3bn='<em>Attendance fell sharply after 1990</em> und <em>far fewer '
         'people came in the years that followed</em> sind dieselbe '
         'Aussage ohne ein gemeinsames Wort.',
    t3ch='Wortabgleich versagt in beide Richtungen',
    t3cb='Dieselben Wörter können in einem Satz stehen, der das Gegenteil '
         'sagt, und ein Satz ohne ein einziges gemeinsames Wort kann die '
         'Aussage exakt treffen. Gleiche Wörter sagen dir, wo du suchst, nie '
         'was du antwortest.',
    t3cn='Nimm das wiederholte Wort, um die Zeile zu finden. Dann lies die '
         'Zeile.',

    t4Eyebrow='Bevor du beginnst',
    t4Title='Ein Wort entscheidet ein Drittel davon',
    t4ah='Absolute',
    t4ab='<em>All</em>, <em>every</em>, <em>never</em>, <em>only</em>. Sagt '
         'der Text <em>most</em>, ist eine Aussage mit <em>all</em> FALSE '
         '&mdash; beides kann nicht gelten, und das ist ein Widerspruch, auf '
         'den du zeigen kannst.',
    t4an='<em>Most islanders</em> gegen <em>every islander</em> ist ein False, '
         'kein Not Given.',
    t4bh='Abschwächungen',
    t4bb='<em>May</em>, <em>might</em>, <em>is thought to</em>, '
         '<em>suggests</em>. Ein abschwächender Text bestreitet eine '
         'sichere Aussage nicht &mdash; er trifft sie nur nie. Diese Form ist '
         'meist Not Given.',
    t4bn='Der Unterschied zum Absoluten: <em>most</em> schließt <em>all</em> '
         'aus, <em>may</em> schließt gar nichts aus.',
    t4ch='Vergleiche brauchen beide Seiten',
    t4cb='<em>Wetter than</em>, <em>the largest</em>, <em>more common than</em>. '
         'Prüfe, ob der Text wirklich dieselben zwei Dinge vergleicht &mdash; '
         'ein Text über eines davon trägt keine Aussage über das Paar.',
    t4cn='Ein Text mit einer Zahl und eine Aussage, die zwei Dinge ordnet, ist '
         'jedes Mal ein Not Given.',

    mcaEyebrow='Aktivität 1 · False oder Not Given?',
    mcaTitle='Lies den Text. Dann lies die Aussage.',
    mcbEyebrow='Aktivität 2 · Der Text, nicht die Welt',
    mcbTitle='Was sagt dieser Text tatsächlich?',
    mccEyebrow='Aktivität 3 · Das Wort, das entscheidet',
    mccTitle='Most, all, may, never',

    r1why='Der Text sagt, es habe nie geschlossen, <em>not even during the '
          'two wars</em>. Das ist die Aussage, anders formuliert. TRUE.',
    r2why='Zweimal täglich im Sommer, sagt der Text. Drei ist eine Zahl, die '
          'einer Zahl im Text widerspricht &mdash; ein Widerspruch, auf den '
          'du zeigen kannst. FALSE.',
    r3why='Der Text zählt die walisischen Bände. Was die Bibliothek vorhat, '
          'steht nirgends. NOT GIVEN.',
    r4why='1954 begonnen, zwei Jahre später fertig. Der Text liefert die '
          'Rechnung statt des Datums, und Paraphrase schließt das Rechnen '
          'ein. TRUE.',
    r5why='Der Text sagt, polarisiertes Licht bleibe nutzbar, <em>when the '
          'sun is behind cloud</em> &mdash; das Gegenteil der Aussage. FALSE, '
          'und das Wort „overcast“ kommt nirgends vor.',
    r6why='Mühle, Dorf und Abhängigkeit stehen im Text. Verkauf, Konkurrent '
          'und 1902 nicht. NOT GIVEN.',
    r7why='Siebzig Prozent sind das meiste. Die Aussage paraphrasiert die '
          'Zahl, statt sie zu wiederholen &mdash; so sieht TRUE meistens aus.',
    r8why='Der Text sagt, was die Studie erfasst hat, nicht wer sie bezahlt '
          'hat. Nach der Finanzierung zu fragen ist naheliegend; der Text geht '
          'nicht darauf ein. NOT GIVEN.',
    r9why='<em>Most</em> im Text gegen <em>every</em> in der Aussage. Ein '
          'Absolutes wird von einer Mehrheit widerlegt, also FALSE und nicht '
          'Not Given.',
    r10why='Der Text schwächt bei der Genesungszeit ab und sagt zur Zulassung '
           'überhaupt nichts. Schweigen, nicht Widerspruch. NOT GIVEN.',
    r11why='Weniger Regen im Tal heißt eine nassere Küste &mdash; dieselbe '
           'Aussage, umgedreht. Die tragenden Wörter, <em>lower</em> und '
           '<em>wetter</em>, haben nichts gemeinsam; deshalb versagt '
           'Wortabgleich hier. TRUE.',
    r12why='<em>Apart from two years in the 1980s</em> ist die Zeile, auf die '
           'du zeigst. <em>Never once</em> überlebt sie nicht. FALSE.',

    sortEyebrow='Aktivität 4 · Was wohin zeigt',
    sortTitle='Sortiere die sechs Signale',
    sortHint='Zieh jedes in eine Spalte &mdash; oder klicke ein Element an und '
             'dann die Spalte, in die es soll.',
    sortBin1='Deutet auf FALSE',
    sortBin2='Deutet auf NOT GIVEN',

    actTitle='Beweise es aus dem Text',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu zweit, mit irgendeinem Text zur Hand &mdash; ein '
                  'Zeitungsartikel genügt. Einer schreibt vier Aussagen dazu: '
                  'eine wahr, eine falsch, zwei nicht genannt. Tauschen, '
                  'beantworten, und jedes Urteil verteidigen, indem die Zeile '
                  'vorgelesen wird, auf der es beruht. Keine Zeile, kein '
                  'FALSE.',
    actSpeak1='Wer antwortet, muss laut sagen, welcher Satz entschieden hat, '
              'bevor das Urteil gilt.',
    actSpeak2='Sag bei jedem NOT GIVEN, was im Text hätte stehen müssen, damit '
              'die Antwort FALSE gewesen wäre.',
    actSpeak3='Finde in den Aussagen deines Partners eine, die man in beide '
              'Richtungen vertreten kann, und schreib sie so um, dass das '
              'nicht mehr geht.',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Nimm einen Text und schreib drei Aussagen dazu &mdash; eine '
                  'TRUE, eine FALSE, eine NOT GIVEN &mdash; und dann den '
                  'Lösungsschlüssel: zu jeder den genauen Satz, der '
                  'entscheidet, oder klar gesagt, dass es keinen gibt.',
    actPlaceholder='Statement 1 (TRUE): … The line that decides it: …',

    # The verdict glosses and the sort explanation; English from the data.
    optT='True &mdash; der Text sagt das klar',
    optF='False &mdash; der Text bestreitet das klar',
    optN='Not Given &mdash; der Text sagt dazu nichts',
    sortWhy='Alles in der linken Spalte nennt einen <strong>Satz, auf den du '
            'zeigen könntest</strong>. Alles in der rechten ist ein Weg, ohne '
            'einen solchen Satz zu einem Urteil zu kommen &mdash; '
            'Schlussfolgerung, Assoziation oder Allgemeinwissen. Das ist der '
            'ganze Unterschied: FALSE braucht eine Zeile im Text, die etwas '
            'anderes sagt, und wenn du nicht mit dem Finger darauf zeigen '
            'kannst, heißt die Antwort NOT GIVEN.',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='True, False, <em>Not Given</em>',
    coverSub='El tipo de pregunta que más puntos cuesta en el Reading, y el '
             'que se recupera con técnica, no con vocabulario',
    chipLevel='C1 · Avanzado', chipFocus='Reading · los dos módulos',
    chipCount='18 puntos',

    t1Eyebrow='Antes de empezar',
    t1Title='Sesenta minutos, tres partes, nada de tiempo al final',
    t1ah='La forma del examen',
    t1ab='Cuarenta preguntas en sesenta minutos, en tres partes de unos '
         'veinte minutos. La tercera suele ser la más difícil: si te alargas '
         'en una, le quitas el tiempo justo a la que más lo necesita.',
    t1an='Academic pone un texto largo por parte; General Training empieza '
         'con textos más cortos. La técnica es la misma, así que todo esto '
         'vale para los dos.',
    t1bh='No hay tiempo de transcripción. Ninguno.',
    t1bb='En el Listening en papel te dan diez minutos al final para pasar las '
         'respuestas. <strong>En el Reading no.</strong> Escribe en la hoja '
         'de respuestas sobre la marcha: a los sesenta minutos la recogen con '
         'lo que tenga.',
    t1bn='Las respuestas que se quedan en el cuadernillo no puntúan. Es la '
         'forma más barata de perder puntos en todo el examen.',
    t1ch='Las preguntas siguen al texto',
    t1cb='La mayoría de los tipos van en el orden del texto, este incluido. '
         'Con cuatro respondidas ya sabes más o menos dónde está la quinta: '
         'nunca hace falta recorrer el texto entero dos veces.',
    t1cn='Matching Headings y Matching Information son las excepciones. Esas '
         'saltan.',

    t2Eyebrow='Antes de empezar',
    t2Title='False y Not Given no son la misma respuesta',
    t2ah='FALSE: el texto dice lo contrario',
    t2ab='Hay una frase en el texto que <strong>contradice</strong> la '
         'afirmación. Puedes señalarla con el dedo. Si tuvieras que demostrar '
         'que la afirmación es falsa, señalarías esa línea.',
    t2an='Un número que no cuadra, una fecha que no coincide, un «solo» '
         'frente a un «varios»: todo eso son contradicciones.',
    t2bh='NOT GIVEN: el texto calla',
    t2bb='El texto ni lo dice ni lo niega. La afirmación puede ser '
         'perfectamente cierta en el mundo real; este texto sencillamente no '
         'entra ahí.',
    t2bn='Not Given no es un castigo por habérsete escapado algo. Es una '
         'respuesta de verdad, y lo es en torno a un tercio de las veces.',
    t2ch='La prueba es una sola pregunta',
    t2cb='<strong>¿Puedo señalar la frase?</strong> Si sí, la respuesta es '
         'True o False según lo que diga. Si estás deduciendo &mdash; «hombre, '
         'tiene que ser» &mdash; la respuesta es Not Given.',
    t2cn='Deducir se parece mucho a entender, y justo por eso cuesta tantos '
         'puntos aquí.',

    t3Eyebrow='Antes de empezar',
    t3Title='Responde desde el texto, nunca desde lo que sabes',
    t3ah='Tu conocimiento es la trampa',
    t3ab='Una afirmación puede ser del todo cierta en el mundo y aun así ser '
         'Not Given en el texto. No te preguntan si es verdad: te preguntan '
         'qué dice este texto.',
    t3an='Por eso se puntúa peor en los temas que uno domina.',
    t3bh='TRUE significa que el texto lo dice',
    t3bb='Casi siempre con otras palabras. El texto no repite la afirmación: '
         'la parafrasea. Cotejar significado es la destreza; cotejar palabras '
         'es la costumbre que hay que quitarse.',
    t3bn='<em>Attendance fell sharply after 1990</em> y <em>far fewer '
         'people came in the years that followed</em> son la misma '
         'afirmación sin una sola palabra en común.',
    t3ch='Cotejar palabras falla en los dos sentidos',
    t3cb='Las mismas palabras pueden estar en una frase que dice lo '
         'contrario, y una frase sin ninguna palabra compartida puede afirmar '
         'exactamente eso. El vocabulario repetido te dice dónde mirar, nunca '
         'qué responder.',
    t3cn='Usa la palabra repetida para encontrar la línea. Y luego lee la '
         'línea.',

    t4Eyebrow='Antes de empezar',
    t4Title='Una palabra decide un tercio de estas',
    t4ah='Absolutos',
    t4ab='<em>All</em>, <em>every</em>, <em>never</em>, <em>only</em>. Si el '
         'texto dice <em>most</em>, una afirmación con <em>all</em> es FALSE: '
         'no pueden cumplirse las dos, y esa contradicción se puede señalar.',
    t4an='<em>Most islanders</em> frente a <em>every islander</em> es un '
         'False, no un Not Given.',
    t4bh='Matizadores',
    t4bb='<em>May</em>, <em>might</em>, <em>is thought to</em>, '
         '<em>suggests</em>. Un texto que matiza no niega una afirmación '
         'rotunda: simplemente no llega a hacerla. Esa forma suele ser Not '
         'Given.',
    t4bn='La diferencia con un absoluto: <em>most</em> excluye <em>all</em>, '
         'pero <em>may</em> no excluye nada.',
    t4ch='Los comparativos necesitan los dos lados',
    t4cb='<em>Wetter than</em>, <em>the largest</em>, <em>more common '
         'than</em>. Comprueba que el texto compare de verdad las mismas dos '
         'cosas: un texto sobre una de ellas no sostiene una afirmación sobre '
         'el par.',
    t4cn='Un texto que da una cifra y una afirmación que ordena dos cosas es '
         'Not Given siempre.',

    mcaEyebrow='Actividad 1 · ¿False o Not Given?',
    mcaTitle='Lee el texto. Y luego lee la afirmación.',
    mcbEyebrow='Actividad 2 · El texto, no el mundo',
    mcbTitle='¿Qué dice realmente este texto?',
    mccEyebrow='Actividad 3 · La palabra que decide',
    mccTitle='Most, all, may, never',

    r1why='El texto dice que no cerró nunca, <em>not even during the two '
          'wars</em>. Es la afirmación con otras palabras. TRUE.',
    r2why='Dos veces al día en verano, dice el texto. Tres es un número que '
          'choca con un número del texto, y esa contradicción se puede '
          'señalar. FALSE.',
    r3why='El texto cuenta los volúmenes en galés. De lo que la biblioteca '
          'piensa hacer no dice nada. NOT GIVEN.',
    r4why='Empezó en 1954 y acabó dos años después. El texto te da la cuenta '
          'en vez de la fecha, y parafrasear incluye hacer la suma. TRUE.',
    r5why='El texto dice que la luz polarizada sigue sirviendo <em>when the '
          'sun is behind cloud</em>, que es lo contrario de la afirmación. '
          'FALSE, y fíjate en que la palabra «overcast» no aparece.',
    r6why='El molino, el pueblo y la dependencia están en el texto. La venta, '
          'el competidor y 1902 no. NOT GIVEN.',
    r7why='El setenta por ciento es la mayor parte. La afirmación parafrasea '
          'la cifra en lugar de repetirla, que es justo la pinta que suele '
          'tener un TRUE.',
    r8why='El texto dice qué abarcó la encuesta, no quién la pagó. Preguntarse '
          'por la financiación es razonable, y el texto no entra ahí. NOT '
          'GIVEN.',
    r9why='<em>Most</em> en el texto frente a <em>every</em> en la afirmación. '
          'Una mayoría contradice un absoluto, así que es FALSE y no Not '
          'Given.',
    r10why='El texto matiza sobre el tiempo de recuperación y de la '
           'autorización no dice absolutamente nada. Silencio, no negación. '
           'NOT GIVEN.',
    r11why='Que llueva menos en el valle es que la costa sea más húmeda: la '
           'misma afirmación del revés. Las palabras que la sostienen, '
           '<em>lower</em> y <em>wetter</em>, no tienen nada en común, y por '
           'eso cotejar palabras falla. TRUE.',
    r12why='<em>Apart from two years in the 1980s</em> es la línea que '
           'señalas. <em>Never once</em> no sobrevive a eso. FALSE.',

    sortEyebrow='Actividad 4 · Qué te inclina hacia dónde',
    sortTitle='Clasifica las seis señales',
    sortHint='Arrastra cada una a una columna &mdash; o haz clic en un '
             'elemento y luego en la columna que quieras.',
    sortBin1='Apunta a FALSE',
    sortBin2='Apunta a NOT GIVEN',

    actTitle='Demuéstralo con el texto',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas, con cualquier texto que tengáis a mano: vale '
                  'una noticia. Uno escribe cuatro afirmaciones sobre él: una '
                  'verdadera, una falsa y dos no dichas. Intercambiad, '
                  'responded y defended cada veredicto leyendo en voz alta la '
                  'línea en la que os basáis. Sin línea, no hay FALSE.',
    actSpeak1='Quien responde tiene que decir en voz alta qué frase lo ha '
              'decidido antes de que se acepte el veredicto.',
    actSpeak2='En cada NOT GIVEN, di qué habría tenido que poner el texto para '
              'que la respuesta fuera FALSE.',
    actSpeak3='Busca en las afirmaciones de tu compañero una que se pueda '
              'defender en los dos sentidos y reescríbela para que ya no se '
              'pueda.',
    actWriteKind='Escritura · 150–200 palabras',
    actWriteBrief='Coge un texto y escribe tres afirmaciones sobre él &mdash; '
                  'una TRUE, una FALSE y una NOT GIVEN &mdash; y luego la '
                  'clave: para cada una, la frase exacta que la decide, o '
                  'decir claramente que no hay ninguna.',
    actPlaceholder='Statement 1 (TRUE): … The line that decides it: …',

    # The verdict glosses and the sort explanation; English from the data.
    optT='True &mdash; el texto lo dice claramente',
    optF='False &mdash; el texto lo niega claramente',
    optN='Not Given &mdash; el texto no lo dice',
    sortWhy='Todo lo de la columna izquierda nombra una <strong>frase que '
            'podrías señalar</strong>. Todo lo de la derecha es una forma de '
            'llegar a un veredicto sin ella: deducción, asociación o cultura '
            'general. Esa es toda la diferencia: FALSE necesita una línea del '
            'texto que diga otra cosa, y si no puedes señalarla con el dedo, la '
            'respuesta es NOT GIVEN.',
)


# ── French ─────────────────────────────────────────────────────────────
T['fr'] = dict(
    coverTitle='True, False, <em>Not Given</em>',
    coverSub='Le type de question qui coûte le plus de points à l’épreuve de '
             'Reading &mdash; et celui que la technique, pas le vocabulaire, '
             'permet de récupérer',
    chipLevel='C1 · Avancé', chipFocus='Reading · les deux modules',
    chipCount='18 points',

    optT='True &mdash; le texte le dit clairement',
    optF='False &mdash; le texte le nie clairement',
    optN='Not Given &mdash; le texte ne le dit pas',

    t1Eyebrow='Avant de commencer',
    t1Title='Soixante minutes, trois parties, pas de temps à la fin',
    t1ah='La forme de l’épreuve',
    t1ab='Quarante questions en soixante minutes, en trois parties d’environ '
         'vingt minutes chacune. La troisième est en général la plus difficile '
         '&mdash; une partie qui déborde prend donc du temps à celle qui en a '
         'le plus besoin.',
    t1an='Academic propose un long texte par partie ; General Training '
         'commence par des textes plus courts. La technique est la même, donc '
         'tout ce qui suit vaut pour les deux.',
    t1bh='Pas de temps de report. Aucun.',
    t1bb='Sur papier, le Listening vous laisse dix minutes à la fin pour '
         'reporter vos réponses. <strong>Le Reading, non.</strong> Écrivez sur '
         'la feuille de réponses au fur et à mesure : au bout de l’heure, le '
         'surveillant la ramasse telle qu’elle est.',
    t1bn='Les réponses restées sur le sujet ne rapportent rien. C’est la façon '
         'la plus bête de perdre des points à cette épreuve.',
    t1ch='Les questions suivent le texte',
    t1cb='La plupart des types de questions suivent l’ordre du texte, celui-ci '
         'compris. Après quatre réponses, vous savez à peu près où se trouve la '
         'cinquième &mdash; vous n’avez jamais à parcourir tout le texte deux '
         'fois.',
    t1cn='Matching Headings et Matching Information sont les exceptions. Ils '
         'sautent d’un endroit à l’autre.',

    t2Eyebrow='Avant de commencer',
    t2Title='False et Not Given ne sont pas la même réponse',
    t2ah='FALSE : le texte dit le contraire',
    t2ab='Il y a dans le texte une phrase qui <strong>contredit</strong> '
         'l’affirmation. Vous pouvez mettre le doigt dessus. Si l’on vous '
         'demandait de prouver que l’affirmation est fausse, vous montreriez '
         'cette ligne.',
    t2an='Un nombre qui ne concorde pas, une date qui ne correspond pas, un '
         '« seulement » face à un « plusieurs » : autant de contradictions.',
    t2bh='NOT GIVEN : le texte se tait',
    t2bb='Le texte ne le dit pas et ne le nie pas. L’affirmation est peut-être '
         'vraie dans le monde réel ; le texte, simplement, n’en parle pas.',
    t2bn='Not Given n’est pas une punition pour avoir raté quelque chose. C’est '
         'une vraie réponse, et environ un tiers des réponses le sont.',
    t2ch='Le test tient en une question',
    t2cb='<strong>Puis-je montrer la phrase du doigt ?</strong> Si oui, la '
         'réponse est True ou False selon ce qu’elle dit. Si vous raisonnez '
         '&mdash; « bon, ce doit être le cas » &mdash; la réponse est Not '
         'Given.',
    t2cn='Raisonner donne l’impression de comprendre, et c’est exactement pour '
         'cela que cela coûte autant de points ici.',

    t3Eyebrow='Avant de commencer',
    t3Title='Répondez d’après le texte, jamais d’après ce que vous savez',
    t3ah='Vos connaissances sont le piège',
    t3ab='Une affirmation peut être tout à fait vraie dans le monde et pourtant '
         'Not Given dans le texte. L’examinateur ne vous demande pas si elle '
         'est vraie. Il vous demande ce que dit ce texte.',
    t3an='C’est pourquoi les candidats réussissent moins bien sur les sujets '
         'qu’ils connaissent bien.',
    t3bh='TRUE veut dire que le texte le dit',
    t3bb='Presque toujours avec d’autres mots. Le texte ne répète pas '
         'l’affirmation, il la reformule. Faire correspondre le sens, c’est la '
         'compétence ; faire correspondre les mots, c’est l’habitude à perdre.',
    t3bn='<em>Attendance fell sharply after 1990</em> et <em>far fewer people '
         'came in the years that followed</em> sont la même affirmation, sans '
         'un seul mot en commun.',
    t3ch='La recherche de mots échoue dans les deux sens',
    t3cb='Les mêmes mots peuvent se trouver dans une phrase qui dit le '
         'contraire, et une phrase sans aucun mot commun peut énoncer '
         'exactement l’affirmation. Le vocabulaire partagé vous dit où '
         'chercher, jamais quoi répondre.',
    t3cn='Servez-vous du mot répété pour trouver la ligne. Puis lisez la '
         'ligne.',

    t4Eyebrow='Avant de commencer',
    t4Title='Un seul mot en décide un tiers',
    t4ah='Les absolus',
    t4ab='<em>All</em>, <em>every</em>, <em>never</em>, <em>only</em>. Un texte '
         'qui dit <em>most</em> rend FALSE une affirmation qui dit <em>all</em> '
         '&mdash; les deux ne peuvent pas être vrais à la fois, et c’est une '
         'contradiction que l’on peut montrer du doigt.',
    t4an='<em>Most islanders</em> face à <em>every islander</em>, c’est un '
         'False, pas un Not Given.',
    t4bh='Les atténuations',
    t4bb='<em>May</em>, <em>might</em>, <em>is thought to</em>, '
         '<em>suggests</em>. Un texte qui atténue ne nie pas une affirmation '
         'catégorique &mdash; il ne la fait simplement jamais. Cette forme '
         'donne en général Not Given.',
    t4bn='La différence avec un absolu : <em>most</em> exclut <em>all</em>, '
         'mais <em>may</em> n’exclut rien.',
    t4ch='Un comparatif a besoin des deux côtés',
    t4cb='<em>Wetter than</em>, <em>the largest</em>, <em>more common '
         'than</em>. Vérifiez que le texte compare vraiment les deux mêmes '
         'choses &mdash; un texte sur l’une d’elles ne peut pas justifier une '
         'affirmation sur la paire.',
    t4cn='Un texte qui donne un seul chiffre et une affirmation qui en classe '
         'deux, c’est Not Given à chaque fois.',

    mcaEyebrow='Activité 1 · False, ou Not Given ?',
    mcaTitle='Lisez le texte. Puis lisez l’affirmation.',
    mcbEyebrow='Activité 2 · Le texte, pas le monde',
    mcbTitle='Que dit vraiment ce texte ?',
    mccEyebrow='Activité 3 · Le mot qui décide',
    mccTitle='Most, all, may, never',

    r1why='Le texte dit que le musée n’a jamais fermé, <em>not even during the '
          'two wars</em>. C’est l’affirmation, avec d’autres mots. TRUE.',
    r2why='Deux fois par jour en été, dit le texte. Trois est un nombre qui '
          'contredit un nombre du texte : une contradiction que l’on peut '
          'montrer du doigt. FALSE.',
    r3why='Le texte compte les volumes en gallois. Il ne dit absolument rien de '
          'ce que la bibliothèque compte faire. NOT GIVEN.',
    r4why='Commencée en 1954, achevée deux ans plus tard. Le texte vous donne '
          'le calcul plutôt que la date, et reformuler inclut faire '
          'l’addition. TRUE.',
    r5why='Le texte dit que la lumière polarisée reste utilisable <em>when the '
          'sun is behind cloud</em> &mdash; le contraire de l’affirmation. '
          'FALSE, et notez que le mot « overcast » n’y figure jamais.',
    r6why='Le moulin, le village et la dépendance sont tous dans le texte. Une '
          'vente, un concurrent et 1902 n’y sont pas. NOT GIVEN.',
    r7why='Soixante-dix pour cent, c’est la majeure partie. L’affirmation '
          'reformule le chiffre au lieu de le répéter : c’est à cela que '
          'ressemble le plus souvent un TRUE.',
    r8why='Le texte dit sur quoi a porté l’enquête, pas qui l’a financée. On '
          'peut raisonnablement se poser la question du financement, mais le '
          'texte n’en parle pas. NOT GIVEN.',
    r9why='<em>Most</em> dans le texte face à <em>every</em> dans '
          'l’affirmation. Une majorité contredit un absolu : c’est donc un '
          'FALSE et non un Not Given.',
    r10why='Le texte atténue au sujet du temps de rétablissement et ne dit '
           'strictement rien de l’autorisation. Un silence, pas un démenti. '
           'NOT GIVEN.',
    r11why='Moins de pluie dans la vallée, c’est une côte plus humide : la '
           'même affirmation retournée. Les mots qui la portent, '
           '<em>lower</em> et <em>wetter</em>, n’ont rien en commun, et c’est '
           'pour cela que la recherche de mots passe à côté. TRUE.',
    r12why='<em>Apart from two years in the 1980s</em> est la ligne que l’on '
           'montre du doigt. <em>Never once</em> n’y survit pas. FALSE.',

    sortEyebrow='Activité 4 · Ce qui fait pencher d’un côté',
    sortTitle='Classez les six signaux',
    sortHint='Faites glisser chacun dans une colonne &mdash; ou cliquez sur '
             'un élément, puis sur la colonne voulue.',
    sortBin1='Oriente vers FALSE',
    sortBin2='Oriente vers NOT GIVEN',
    sortWhy='Tout ce qui est dans la colonne de gauche désigne une '
            '<strong>phrase que l’on pourrait montrer du doigt</strong>. Tout '
            'ce qui est dans la colonne de droite est une façon d’arriver à un '
            'verdict sans elle : déduction, association ou culture générale. '
            'Toute la différence est là : FALSE exige une ligne du texte qui '
            'dit le contraire, et si vous ne pouvez pas mettre le doigt '
            'dessus, la réponse est NOT GIVEN.',

    actTitle='Prouvez-le par le texte',
    actUse='Utilisez-en au moins trois :',
    actSpeakBrief='À deux, avec n’importe quel texte sous la main &mdash; un '
                  'article de presse fera l’affaire. L’un de vous écrit quatre '
                  'affirmations à son sujet : une vraie, une fausse, deux non '
                  'mentionnées. Échangez, répondez, puis défendez chaque '
                  'verdict en lisant la ligne sur laquelle il repose. Pas de '
                  'ligne, pas de FALSE.',
    actSpeak1='Celui qui répond doit dire à voix haute quelle phrase a décidé, '
              'avant que le verdict soit accepté.',
    actSpeak2='Pour chaque NOT GIVEN, dites ce que le texte aurait dû contenir '
              'pour que la réponse soit FALSE.',
    actSpeak3='Trouvez dans les affirmations de votre partenaire une '
              'affirmation qu’on pourrait défendre dans les deux sens, et '
              'réécrivez-la pour que ce ne soit plus possible.',
    actWriteKind='Écriture · 150–200 mots',
    actWriteBrief='Prenez un texte et écrivez trois affirmations à son sujet '
                  '&mdash; une TRUE, une FALSE, une NOT GIVEN &mdash; puis le '
                  'corrigé, en indiquant pour chacune la phrase exacte qui '
                  'décide, ou en disant clairement qu’aucune phrase ne le '
                  'fait.',
    actPlaceholder='Statement 1 (TRUE): … The line that decides it: …',
)


# ── Italian ────────────────────────────────────────────────────────────
T['it'] = dict(
    coverTitle='True, False, <em>Not Given</em>',
    coverSub='Il tipo di domanda che fa perdere più punti nella prova di Reading '
             '&mdash; e quello che si recupera con la tecnica, non con il '
             'vocabolario',
    chipLevel='C1 · Avanzato', chipFocus='Reading · entrambi i moduli',
    chipCount='18 punti',

    optT='True &mdash; il testo lo dice chiaramente',
    optF='False &mdash; il testo lo nega chiaramente',
    optN='Not Given &mdash; il testo non lo dice',

    t1Eyebrow='Prima di cominciare',
    t1Title='Sessanta minuti, tre sezioni, niente tempo alla fine',
    t1ah='Com’è fatta la prova',
    t1ab='Quaranta domande in sessanta minuti, in tre sezioni da circa venti '
         'minuti ciascuna. La terza di solito è la più difficile &mdash; quindi '
         'una sezione che si allunga toglie tempo proprio a quella che ne ha '
         'più bisogno.',
    t1an='Academic propone un testo lungo per sezione; General Training '
         'comincia con testi più brevi. La tecnica è la stessa, quindi tutto '
         'quello che trovi qui vale per entrambi.',
    t1bh='Niente tempo per ricopiare. Zero.',
    t1bb='Su carta, il Listening ti dà dieci minuti alla fine per ricopiare le '
         'risposte. <strong>Il Reading no.</strong> Scrivi sul foglio delle '
         'risposte man mano: allo scadere dell’ora il sorvegliante lo ritira '
         'così com’è.',
    t1bn='Le risposte rimaste sul fascicolo delle domande non valgono nulla. È '
         'il modo più stupido di perdere punti in questa prova.',
    t1ch='Le domande seguono il testo',
    t1cb='La maggior parte dei tipi di domanda segue l’ordine del testo, '
         'compreso questo. Dopo quattro risposte sai più o meno dove si trova la '
         'quinta &mdash; non devi mai scorrere tutto il testo due volte.',
    t1cn='Matching Headings e Matching Information sono le eccezioni. Saltano '
         'da una parte all’altra.',

    t2Eyebrow='Prima di cominciare',
    t2Title='False e Not Given non sono la stessa risposta',
    t2ah='FALSE: il testo dice il contrario',
    t2ab='Nel testo c’è una frase che <strong>contraddice</strong> '
         'l’affermazione. Puoi metterci il dito sopra. Se qualcuno ti chiedesse '
         'di dimostrare che l’affermazione è falsa, indicheresti quella riga.',
    t2an='Un numero che non torna, una data che non corrisponde, un «solo» '
         'contro un «diversi»: tutte contraddizioni.',
    t2bh='NOT GIVEN: il testo tace',
    t2bb='Il testo non lo dice e non lo nega. L’affermazione può essere '
         'verissima nel mondo reale; il testo semplicemente non ne parla.',
    t2bn='Not Given non è una punizione perché ti è sfuggito qualcosa. È una '
         'risposta vera, e lo è circa un terzo delle volte.',
    t2ch='La prova è una sola domanda',
    t2cb='<strong>Posso indicare la frase?</strong> Se sì, la risposta è True '
         'o False a seconda di ciò che dice. Se stai ragionando &mdash; «be’, '
         'deve essere così» &mdash; la risposta è Not Given.',
    t2cn='Ragionare sembra capire, ed è proprio per questo che qui costa tanti '
         'punti.',

    t3Eyebrow='Prima di cominciare',
    t3Title='Rispondi in base al testo, mai in base a ciò che sai',
    t3ah='Quello che sai è la trappola',
    t3ab='Un’affermazione può essere verissima nel mondo e comunque Not Given '
         'nel testo. L’esaminatore non ti chiede se è vera. Ti chiede che cosa '
         'dice questo testo.',
    t3an='Ecco perché i candidati vanno peggio sugli argomenti che conoscono '
         'bene.',
    t3bh='TRUE significa che il testo lo dice',
    t3bb='Quasi sempre con altre parole. Il testo non ripete l’affermazione, la '
         'riformula. Far corrispondere il significato è l’abilità; far '
         'corrispondere le parole è l’abitudine da perdere.',
    t3bn='<em>Attendance fell sharply after 1990</em> e <em>far fewer people '
         'came in the years that followed</em> sono la stessa affermazione '
         'senza una parola in comune.',
    t3ch='Cercare le parole fallisce in tutti e due i sensi',
    t3cb='Le stesse parole possono stare in una frase che dice il contrario, e '
         'una frase senza nessuna parola in comune può esprimere esattamente '
         'l’affermazione. Il vocabolario condiviso ti dice dove guardare, mai '
         'che cosa rispondere.',
    t3cn='Usa la parola ripetuta per trovare la riga. Poi leggi la riga.',

    t4Eyebrow='Prima di cominciare',
    t4Title='Una sola parola ne decide un terzo',
    t4ah='Gli assoluti',
    t4ab='<em>All</em>, <em>every</em>, <em>never</em>, <em>only</em>. Un testo '
         'che dice <em>most</em> rende FALSE un’affermazione che dice '
         '<em>all</em> &mdash; le due cose non possono valere insieme, ed è una '
         'contraddizione che puoi indicare.',
    t4an='<em>Most islanders</em> contro <em>every islander</em> è un False, '
         'non un Not Given.',
    t4bh='Le attenuazioni',
    t4bb='<em>May</em>, <em>might</em>, <em>is thought to</em>, '
         '<em>suggests</em>. Un testo che attenua non nega un’affermazione '
         'sicura &mdash; semplicemente non la fa mai. Questa forma di solito è '
         'Not Given.',
    t4bn='La differenza con un assoluto: <em>most</em> esclude <em>all</em>, '
         'ma <em>may</em> non esclude niente.',
    t4ch='Un comparativo ha bisogno di entrambi i lati',
    t4cb='<em>Wetter than</em>, <em>the largest</em>, <em>more common '
         'than</em>. Controlla che il testo confronti davvero le stesse due '
         'cose &mdash; un testo su una sola di esse non può sostenere '
         'un’affermazione sulla coppia.',
    t4cn='Un testo che dà un solo dato e un’affermazione che ne mette in '
         'ordine due: è Not Given ogni volta.',

    mcaEyebrow='Attività 1 · False o Not Given?',
    mcaTitle='Leggi il testo. Poi leggi l’affermazione.',
    mcbEyebrow='Attività 2 · Il testo, non il mondo',
    mcbTitle='Che cosa dice davvero questo testo?',
    mccEyebrow='Attività 3 · La parola che decide',
    mccTitle='Most, all, may, never',

    r1why='Il testo dice che il museo non ha mai chiuso, <em>not even during '
          'the two wars</em>. È l’affermazione, con altre parole. TRUE.',
    r2why='Due volte al giorno in estate, dice il testo. Tre è un numero che '
          'contraddice un numero del testo: una contraddizione che puoi '
          'indicare. FALSE.',
    r3why='Il testo conta i volumi in gallese. Non dice assolutamente nulla su '
          'che cosa la biblioteca intenda fare. NOT GIVEN.',
    r4why='Iniziata nel 1954, finita due anni dopo. Il testo ti dà il calcolo '
          'invece della data, e riformulare comprende anche fare la somma. '
          'TRUE.',
    r5why='Il testo dice che la luce polarizzata resta utilizzabile <em>when '
          'the sun is behind cloud</em> &mdash; il contrario dell’affermazione. '
          'FALSE, e nota che la parola «overcast» non compare mai.',
    r6why='Il mulino, il paese e la dipendenza sono tutti nel testo. Una '
          'vendita, un concorrente e il 1902 no. NOT GIVEN.',
    r7why='Il settanta per cento è la maggior parte. L’affermazione riformula '
          'il dato invece di ripeterlo: è l’aspetto che di solito ha un TRUE.',
    r8why='Il testo dice che cosa ha riguardato l’indagine, non chi l’ha '
          'pagata. Chiedersi chi l’abbia finanziata è ragionevole, ma il testo '
          'non ne parla. NOT GIVEN.',
    r9why='<em>Most</em> nel testo contro <em>every</em> nell’affermazione. Una '
          'maggioranza contraddice un assoluto, quindi è FALSE e non Not Given.',
    r10why='Il testo attenua sul tempo di recupero e non dice proprio nulla '
           'sull’approvazione. Silenzio, non smentita. NOT GIVEN.',
    r11why='Meno pioggia nella valle vuol dire una costa più piovosa: la stessa '
           'affermazione rovesciata. Le parole che la reggono, <em>lower</em> e '
           '<em>wetter</em>, non hanno niente in comune, ed è per questo che '
           'cercare le parole non la trova. TRUE.',
    r12why='<em>Apart from two years in the 1980s</em> è la riga da indicare. '
           '<em>Never once</em> non ci sopravvive. FALSE.',

    sortEyebrow='Attività 4 · Che cosa ti fa pendere da una parte',
    sortTitle='Classifica i sei segnali',
    sortHint='Trascina ciascuno in una colonna &mdash; oppure clicca su un '
             'elemento e poi sulla colonna che vuoi.',
    sortBin1='Porta a FALSE',
    sortBin2='Porta a NOT GIVEN',
    sortWhy='Tutto ciò che sta nella colonna di sinistra indica una '
            '<strong>frase che potresti indicare col dito</strong>. Tutto ciò '
            'che sta nella colonna di destra è un modo di arrivare a un '
            'verdetto senza di essa: deduzione, associazione o cultura '
            'generale. Tutta la differenza è qui: FALSE richiede una riga del '
            'testo che dica il contrario, e se non riesci a indicarla, la '
            'risposta è NOT GIVEN.',

    actTitle='Dimostralo con il testo',
    actUse='Usane almeno tre:',
    actSpeakBrief='In coppia, con un testo qualsiasi a portata di mano &mdash; '
                  'va bene un articolo di giornale. Uno di voi scrive quattro '
                  'affermazioni sul testo: una vera, una falsa, due non dette. '
                  'Scambiatevele, rispondete e poi difendete ogni verdetto '
                  'leggendo la riga su cui si basa. Niente riga, niente FALSE.',
    actSpeak1='Chi risponde deve dire ad alta voce quale frase ha deciso, prima '
              'che il verdetto venga accettato.',
    actSpeak2='Per ogni NOT GIVEN, di’ che cosa avrebbe dovuto contenere il '
              'testo perché la risposta fosse FALSE.',
    actSpeak3='Trova tra le affermazioni del tuo compagno una che si potrebbe '
              'sostenere in tutti e due i sensi, e riscrivila perché non si '
              'possa più.',
    actWriteKind='Scrittura · 150–200 parole',
    actWriteBrief='Prendi un testo e scrivi tre affermazioni su di esso &mdash; '
                  'una TRUE, una FALSE, una NOT GIVEN &mdash; poi la chiave, '
                  'indicando per ciascuna la frase esatta che decide, o '
                  'dicendo chiaramente che non ce n’è nessuna.',
    actPlaceholder='Statement 1 (TRUE): … The line that decides it: …',
)


# ── Portuguese ─────────────────────────────────────────────────────────
T['pt'] = dict(
    coverTitle='True, False, <em>Not Given</em>',
    coverSub='O tipo de pergunta que mais pontos faz perder na prova de Reading '
             '&mdash; e o que se recupera com técnica, não com vocabulário',
    chipLevel='C1 · Avançado', chipFocus='Reading · os dois módulos',
    chipCount='18 pontos',

    optT='True &mdash; o texto afirma-o claramente',
    optF='False &mdash; o texto nega-o claramente',
    optN='Not Given &mdash; o texto não o diz',

    t1Eyebrow='Antes de começar',
    t1Title='Sessenta minutos, três partes, nenhum tempo no fim',
    t1ah='O formato da prova',
    t1ab='Quarenta perguntas em sessenta minutos, em três partes de cerca de '
         'vinte minutos cada. A terceira costuma ser a mais difícil &mdash; '
         'por isso, uma parte que se arrasta tira tempo precisamente à que '
         'mais precisa dele.',
    t1an='O Academic tem um texto longo por parte; o General Training começa '
         'com textos mais curtos. A técnica é a mesma, por isso tudo o que está '
         'aqui vale para os dois.',
    t1bh='Sem tempo para passar as respostas. Nenhum.',
    t1bb='Em papel, o Listening dá-te dez minutos no fim para passares as '
         'respostas. <strong>O Reading não.</strong> Escreve na folha de '
         'respostas à medida que avanças: ao fim da hora, o vigilante '
         'recolhe-a tal como estiver.',
    t1bn='As respostas que ficam no enunciado não contam. É a maneira mais '
         'barata de perder pontos nesta prova.',
    t1ch='As perguntas seguem o texto',
    t1cb='A maioria dos tipos de pergunta segue a ordem do texto, este '
         'incluído. Depois de quatro respostas, sabes mais ou menos onde está a '
         'quinta &mdash; nunca precisas de percorrer o texto todo duas vezes.',
    t1cn='Matching Headings e Matching Information são as exceções. Saltam de '
         'um lado para o outro.',

    t2Eyebrow='Antes de começar',
    t2Title='False e Not Given não são a mesma resposta',
    t2ah='FALSE: o texto diz o contrário',
    t2ab='Há no texto uma frase que <strong>contradiz</strong> a afirmação. '
         'Consegues pôr o dedo em cima dela. Se te pedissem para provar que a '
         'afirmação é falsa, apontarias para essa linha.',
    t2an='Um número que não bate certo, uma data que não coincide, um «só» '
         'contra um «vários»: tudo contradições.',
    t2bh='NOT GIVEN: o texto cala-se',
    t2bb='O texto nem o diz nem o nega. A afirmação pode muito bem ser '
         'verdadeira no mundo real; o texto simplesmente não fala disso.',
    t2bn='Not Given não é um castigo por te ter escapado alguma coisa. É uma '
         'resposta a sério, e é-o em cerca de um terço dos casos.',
    t2ch='O teste é uma única pergunta',
    t2cb='<strong>Consigo apontar para a frase?</strong> Se sim, a resposta é '
         'True ou False, conforme o que ela diz. Se estás a deduzir &mdash; '
         '«bem, tem de ser» &mdash; a resposta é Not Given.',
    t2cn='Deduzir parece compreender, e é exatamente por isso que custa tantos '
         'pontos aqui.',

    t3Eyebrow='Antes de começar',
    t3Title='Responde com base no texto, nunca no que sabes',
    t3ah='O que sabes é a armadilha',
    t3ab='Uma afirmação pode ser perfeitamente verdadeira no mundo e mesmo '
         'assim ser Not Given no texto. O examinador não te pergunta se é '
         'verdade. Pergunta-te o que diz este texto.',
    t3an='É por isso que os candidatos têm piores resultados nos temas que '
         'conhecem bem.',
    t3bh='TRUE quer dizer que o texto o diz',
    t3bb='Quase sempre por outras palavras. O texto não repete a afirmação: '
         'parafraseia-a. Fazer corresponder o sentido é a competência; fazer '
         'corresponder palavras é o hábito a perder.',
    t3bn='<em>Attendance fell sharply after 1990</em> e <em>far fewer people '
         'came in the years that followed</em> são a mesma afirmação, sem uma '
         'única palavra em comum.',
    t3ch='Procurar palavras falha nos dois sentidos',
    t3cb='As mesmas palavras podem estar numa frase que diz o contrário, e uma '
         'frase sem nenhuma palavra em comum pode afirmar exatamente o mesmo. '
         'O vocabulário partilhado diz-te onde procurar, nunca o que '
         'responder.',
    t3cn='Usa a palavra repetida para encontrar a linha. Depois lê a linha.',

    t4Eyebrow='Antes de começar',
    t4Title='Uma palavra decide um terço destas',
    t4ah='Os absolutos',
    t4ab='<em>All</em>, <em>every</em>, <em>never</em>, <em>only</em>. Um texto '
         'que diz <em>most</em> torna FALSE uma afirmação que diz <em>all</em> '
         '&mdash; as duas não podem ser verdade ao mesmo tempo, e isso é uma '
         'contradição para a qual podes apontar.',
    t4an='<em>Most islanders</em> contra <em>every islander</em> é um False, '
         'não um Not Given.',
    t4bh='As atenuações',
    t4bb='<em>May</em>, <em>might</em>, <em>is thought to</em>, '
         '<em>suggests</em>. Um texto que atenua não nega uma afirmação '
         'categórica &mdash; simplesmente nunca a faz. Essa forma costuma ser '
         'Not Given.',
    t4bn='A diferença em relação a um absoluto: <em>most</em> exclui '
         '<em>all</em>, mas <em>may</em> não exclui nada.',
    t4ch='Um comparativo precisa dos dois lados',
    t4cb='<em>Wetter than</em>, <em>the largest</em>, <em>more common '
         'than</em>. Confirma que o texto compara mesmo as duas coisas '
         '&mdash; um texto sobre uma delas não sustenta uma afirmação sobre o '
         'par.',
    t4cn='Um texto que dá um só número e uma afirmação que ordena dois é Not '
         'Given sempre.',

    mcaEyebrow='Atividade 1 · False ou Not Given?',
    mcaTitle='Lê o texto. Depois lê a afirmação.',
    mcbEyebrow='Atividade 2 · O texto, não o mundo',
    mcbTitle='O que diz realmente este texto?',
    mccEyebrow='Atividade 3 · A palavra que decide',
    mccTitle='Most, all, may, never',

    r1why='O texto diz que o museu nunca fechou, <em>not even during the two '
          'wars</em>. É a afirmação, por outras palavras. TRUE.',
    r2why='Duas vezes por dia no verão, diz o texto. Três é um número que '
          'contradiz um número do texto: uma contradição para a qual podes '
          'apontar. FALSE.',
    r3why='O texto conta os volumes em galês. Não diz rigorosamente nada sobre '
          'o que a biblioteca tenciona fazer. NOT GIVEN.',
    r4why='Começou em 1954 e ficou pronta dois anos depois. O texto dá-te a '
          'conta em vez da data, e parafrasear inclui fazer a soma. TRUE.',
    r5why='O texto diz que a luz polarizada continua a servir <em>when the sun '
          'is behind cloud</em> &mdash; o contrário da afirmação. FALSE, e '
          'repara que a palavra «overcast» nunca aparece.',
    r6why='O moinho, a aldeia e a dependência estão todos no texto. Uma venda, '
          'um concorrente e 1902 não estão. NOT GIVEN.',
    r7why='Setenta por cento é a maior parte. A afirmação parafraseia o número '
          'em vez de o repetir, que é o aspeto que um TRUE costuma ter.',
    r8why='O texto diz o que o inquérito abrangeu, não quem o pagou. É razoável '
          'perguntar pelo financiamento, e o texto não fala disso. NOT GIVEN.',
    r9why='<em>Most</em> no texto contra <em>every</em> na afirmação. Uma '
          'maioria contradiz um absoluto, por isso é FALSE e não Not Given.',
    r10why='O texto atenua quanto ao tempo de recuperação e não diz absolutamente '
           'nada sobre a aprovação. Silêncio, não negação. NOT GIVEN.',
    r11why='Menos chuva no vale quer dizer uma costa mais chuvosa: a mesma '
           'afirmação do avesso. As palavras que a sustentam, <em>lower</em> e '
           '<em>wetter</em>, não têm nada em comum, e é por isso que procurar '
           'palavras não a apanha. TRUE.',
    r12why='<em>Apart from two years in the 1980s</em> é a linha para a qual '
           'apontas. <em>Never once</em> não lhe sobrevive. FALSE.',

    sortEyebrow='Atividade 4 · O que te faz pender para cada lado',
    sortTitle='Classifica os seis sinais',
    sortHint='Arrasta cada um para uma coluna &mdash; ou clica num elemento e '
             'depois na coluna que quiseres.',
    sortBin1='Aponta para FALSE',
    sortBin2='Aponta para NOT GIVEN',
    sortWhy='Tudo o que está na coluna da esquerda nomeia uma <strong>frase '
            'para a qual poderias apontar</strong>. Tudo o que está na coluna '
            'da direita é uma forma de chegar a um veredicto sem ela: dedução, '
            'associação ou cultura geral. Toda a diferença está aqui: FALSE '
            'precisa de uma linha do texto que diga o contrário, e se não '
            'consegues pôr o dedo nela, a resposta é NOT GIVEN.',

    actTitle='Prova-o com o texto',
    actUse='Usa pelo menos três:',
    actSpeakBrief='Em pares, com um texto qualquer à mão &mdash; serve uma '
                  'notícia. Um de vocês escreve quatro afirmações sobre ele: '
                  'uma verdadeira, uma falsa, duas não mencionadas. Troquem, '
                  'respondam e depois defendam cada veredicto lendo a linha em '
                  'que se basearam. Sem linha, não há FALSE.',
    actSpeak1='Quem responde tem de dizer em voz alta que frase decidiu, antes '
              'de o veredicto ser aceite.',
    actSpeak2='Para cada NOT GIVEN, diz o que o texto teria de conter para a '
              'resposta ser FALSE.',
    actSpeak3='Encontra nas afirmações do teu colega uma que se possa defender '
              'nos dois sentidos, e reescreve-a para que já não se possa.',
    actWriteKind='Escrita · 150–200 palavras',
    actWriteBrief='Pega num texto e escreve três afirmações sobre ele &mdash; '
                  'uma TRUE, uma FALSE, uma NOT GIVEN &mdash; e depois a chave, '
                  'indicando para cada uma a frase exata que decide, ou dizendo '
                  'claramente que nenhuma frase o faz.',
    actPlaceholder='Statement 1 (TRUE): … The line that decides it: …',
)


# ── Russian ────────────────────────────────────────────────────────────
T['ru'] = dict(
    coverTitle='True, False, <em>Not Given</em>',
    coverSub='Тип вопросов, на котором в Reading теряют больше всего баллов, '
             '&mdash; и который возвращает техника, а не словарный запас',
    chipLevel='C1 · Продвинутый', chipFocus='Reading · оба модуля',
    chipCount='18 баллов',

    optT='True &mdash; в тексте это сказано прямо',
    optF='False &mdash; текст прямо это отрицает',
    optN='Not Given &mdash; в тексте об этом нет',

    t1Eyebrow='Прежде чем начать',
    t1Title='Шестьдесят минут, три части, в конце времени нет',
    t1ah='Как устроен экзамен',
    t1ab='Сорок вопросов за шестьдесят минут, в трёх частях примерно по '
         'двадцать минут. Третья обычно самая трудная &mdash; поэтому часть, '
         'которая затянулась, отнимает время у той, которой оно нужнее всего.',
    t1an='В Academic по одному длинному тексту на часть; General Training '
         'начинается с коротких текстов. Техника одна и та же, так что всё '
         'здесь подходит для обоих модулей.',
    t1bh='Времени на перенос нет. Совсем.',
    t1bb='На бумажном экзамене в Listening в конце дают десять минут, чтобы '
         'перенести ответы. <strong>В Reading &mdash; нет.</strong> Пишите '
         'сразу в бланк ответов: ровно через час его забирают в том виде, в '
         'каком он есть.',
    t1bn='Ответы, оставшиеся в листе с заданиями, не засчитываются. Это самый '
         'глупый способ потерять баллы на этом экзамене.',
    t1ch='Вопросы идут по тексту',
    t1cb='Большинство типов вопросов идут в порядке текста, этот тоже. '
         'Ответив на четыре, вы примерно знаете, где пятый, &mdash; искать по '
         'всему тексту дважды не придётся.',
    t1cn='Исключения &mdash; Matching Headings и Matching Information. Они '
         'прыгают по тексту.',

    t2Eyebrow='Прежде чем начать',
    t2Title='False и Not Given &mdash; разные ответы',
    t2ah='FALSE: текст говорит обратное',
    t2ab='В тексте есть предложение, которое <strong>противоречит</strong> '
         'утверждению. На него можно указать пальцем. Если бы вас попросили '
         'доказать, что утверждение неверно, вы указали бы на эту строку.',
    t2an='Число, которое не сходится, дата, которая не совпадает, «только» '
         'против «несколько» &mdash; всё это противоречия.',
    t2bh='NOT GIVEN: текст молчит',
    t2bb='Текст этого не говорит и не отрицает. Утверждение вполне может быть '
         'верным в реальном мире; просто текст об этом не говорит.',
    t2bn='Not Given &mdash; не наказание за то, что вы что-то пропустили. Это '
         'настоящий ответ, и таких примерно треть.',
    t2ch='Проверка &mdash; один вопрос',
    t2cb='<strong>Могу ли я указать на предложение?</strong> Если да, ответ '
         'True или False в зависимости от того, что в нём сказано. Если вы '
         'рассуждаете &mdash; «ну, должно же быть так» &mdash;, ответ Not '
         'Given.',
    t2cn='Рассуждение похоже на понимание, и именно поэтому здесь оно стоит '
         'так много баллов.',

    t3Eyebrow='Прежде чем начать',
    t3Title='Отвечайте по тексту, а не по тому, что знаете',
    t3ah='Ваши знания &mdash; ловушка',
    t3ab='Утверждение может быть совершенно верным в мире и всё равно быть Not '
         'Given в тексте. Экзаменатор не спрашивает, правда ли это. Он '
         'спрашивает, что сказано в этом тексте.',
    t3an='Поэтому на хорошо знакомых темах кандидаты набирают меньше.',
    t3bh='TRUE значит: в тексте это сказано',
    t3bb='Почти всегда другими словами. Текст не повторяет утверждение, а '
         'перефразирует его. Сопоставлять смысл &mdash; это навык; '
         'сопоставлять слова &mdash; привычка, от которой пора отказаться.',
    t3bn='<em>Attendance fell sharply after 1990</em> и <em>far fewer people '
         'came in the years that followed</em> &mdash; одно и то же '
         'утверждение без единого общего слова.',
    t3ch='Поиск по словам подводит в обе стороны',
    t3cb='Те же самые слова могут стоять в предложении, которое говорит '
         'обратное, а предложение без единого общего слова может точно '
         'выражать утверждение. Общие слова подсказывают, где искать, но '
         'никогда &mdash; что ответить.',
    t3cn='Найдите строку по повторяющемуся слову. Потом прочитайте строку.',

    t4Eyebrow='Прежде чем начать',
    t4Title='Треть таких вопросов решает одно слово',
    t4ah='Абсолюты',
    t4ab='<em>All</em>, <em>every</em>, <em>never</em>, <em>only</em>. Если в '
         'тексте <em>most</em>, то утверждение с <em>all</em> &mdash; FALSE: '
         'оба не могут быть верны одновременно, и на это противоречие можно '
         'указать.',
    t4an='<em>Most islanders</em> против <em>every islander</em> &mdash; это '
         'False, а не Not Given.',
    t4bh='Смягчения',
    t4bb='<em>May</em>, <em>might</em>, <em>is thought to</em>, '
         '<em>suggests</em>. Смягчённый текст не отрицает уверенное '
         'утверждение &mdash; он просто никогда его не делает. Обычно это Not '
         'Given.',
    t4bn='Отличие от абсолюта: <em>most</em> исключает <em>all</em>, а '
         '<em>may</em> не исключает ничего.',
    t4ch='Сравнению нужны обе стороны',
    t4cb='<em>Wetter than</em>, <em>the largest</em>, <em>more common '
         'than</em>. Проверьте, что текст действительно сравнивает те же два '
         'предмета: текст об одном из них не подтверждает утверждение о паре.',
    t4cn='Текст с одной цифрой и утверждение, которое сравнивает две, &mdash; '
         'это всегда Not Given.',

    mcaEyebrow='Задание 1 · False или Not Given?',
    mcaTitle='Прочитайте текст. Потом прочитайте утверждение.',
    mcbEyebrow='Задание 2 · Текст, а не мир',
    mcbTitle='Что на самом деле сказано в этом тексте?',
    mccEyebrow='Задание 3 · Слово, которое решает',
    mccTitle='Most, all, may, never',

    r1why='В тексте сказано, что музей не закрывался никогда, <em>not even '
          'during the two wars</em>. Это и есть утверждение, другими словами. '
          'TRUE.',
    r2why='Дважды в день летом, говорит текст. Три &mdash; число, которое '
          'противоречит числу в тексте, и на это противоречие можно указать. '
          'FALSE.',
    r3why='Текст считает тома на валлийском. О том, что библиотека собирается '
          'делать дальше, в нём нет ни слова. NOT GIVEN.',
    r4why='Начали в 1954-м, закончили через два года. Текст даёт вам не дату, '
          'а арифметику, и перефразирование включает в себя сложение. TRUE.',
    r5why='В тексте сказано, что поляризованный свет остаётся пригодным '
          '<em>when the sun is behind cloud</em>, &mdash; это обратное '
          'утверждению. FALSE; заметьте, что слово «overcast» в тексте не '
          'встречается.',
    r6why='Мельница, деревня и зависимость &mdash; всё это в тексте есть. '
          'Продажи, конкурента и 1902 года &mdash; нет. NOT GIVEN.',
    r7why='Семьдесят процентов &mdash; это большая часть. Утверждение '
          'перефразирует цифру, а не повторяет её: так обычно и выглядит TRUE.',
    r8why='Текст говорит, что охватило исследование, а не кто за него платил. '
          'Задаться вопросом о финансировании естественно, но текст об этом '
          'молчит. NOT GIVEN.',
    r9why='<em>Most</em> в тексте против <em>every</em> в утверждении. '
          'Большинство противоречит абсолюту, поэтому это FALSE, а не Not '
          'Given.',
    r10why='Текст смягчает высказывание о сроке восстановления и ничего не '
           'говорит об одобрении. Молчание, а не отрицание. NOT GIVEN.',
    r11why='Меньше дождей в долине &mdash; значит, на побережье влажнее: то же '
           'утверждение, только наоборот. Слова, на которых оно держится, '
           '<em>lower</em> и <em>wetter</em>, не имеют ничего общего, поэтому '
           'поиск по словам его пропускает. TRUE.',
    r12why='<em>Apart from two years in the 1980s</em> &mdash; строка, на '
           'которую вы указываете. <em>Never once</em> её не переживёт. FALSE.',

    sortEyebrow='Задание 4 · Что склоняет в какую сторону',
    sortTitle='Распределите шесть сигналов',
    sortHint='Перетащите каждый в столбец &mdash; или нажмите на него, а затем '
             'на нужный столбец.',
    sortBin1='Указывает на FALSE',
    sortBin2='Указывает на NOT GIVEN',
    sortWhy='Всё в левом столбце называет <strong>предложение, на которое можно '
            'указать</strong>. Всё в правом &mdash; способы прийти к вердикту '
            'без него: вывод, ассоциация или общие знания. В этом вся '
            'разница: для FALSE нужна строка текста, которая говорит обратное, '
            'а если указать на неё нельзя, ответ NOT GIVEN.',

    actTitle='Докажите по тексту',
    actUse='Используйте хотя бы три:',
    actSpeakBrief='В парах, с любым текстом под рукой &mdash; подойдёт новостная '
                  'статья. Один из вас пишет по нему четыре утверждения: одно '
                  'верное, одно неверное, два, о которых в тексте ничего нет. '
                  'Обменяйтесь, ответьте и защитите каждый вердикт, прочитав '
                  'строку, на которую вы опирались. Нет строки &mdash; нет '
                  'FALSE.',
    actSpeak1='Тот, кто отвечает, должен вслух назвать решающее предложение, '
              'прежде чем вердикт будет принят.',
    actSpeak2='Для каждого NOT GIVEN скажите, что должно было бы быть в тексте, '
              'чтобы ответом был FALSE.',
    actSpeak3='Найдите у партнёра утверждение, которое можно защищать в обе '
              'стороны, и перепишите его так, чтобы это стало невозможно.',
    actWriteKind='Письмо · 150–200 слов',
    actWriteBrief='Возьмите текст и напишите по нему три утверждения &mdash; '
                  'одно TRUE, одно FALSE, одно NOT GIVEN, &mdash; а затем ключ: '
                  'для каждого укажите точное предложение, которое решает '
                  'ответ, или прямо скажите, что такого предложения нет.',
    actPlaceholder='Statement 1 (TRUE): … The line that decides it: …',
)


# ── Arabic ─────────────────────────────────────────────────────────────
T['ar'] = dict(
    coverTitle='True, False, <em>Not Given</em>',
    coverSub='نوع الأسئلة الذي يُفقد أكبر عدد من الدرجات في اختبار Reading، '
             'والذي تستعيدها فيه التقنية لا المفردات',
    chipLevel='C1 · متقدّم', chipFocus='Reading · الوحدتان كلتاهما',
    chipCount='18 نقطة',

    optT='True &mdash; النص يذكر هذا صراحةً',
    optF='False &mdash; النص ينفي هذا صراحةً',
    optN='Not Given &mdash; النص لا يذكر ذلك',

    t1Eyebrow='قبل أن تبدأ',
    t1Title='ستون دقيقة، ثلاثة أقسام، ولا وقت في النهاية',
    t1ah='شكل الاختبار',
    t1ab='أربعون سؤالًا في ستين دقيقة، في ثلاثة أقسام لكل منها نحو عشرين '
         'دقيقة. والقسم الثالث عادةً هو الأصعب، لذا فالقسم الذي يطول يقتطع من '
         'وقت القسم الأحوج إليه.',
    t1an='في Academic نص طويل واحد لكل قسم، أما General Training فيبدأ بنصوص '
         'أقصر. والتقنية واحدة، فكل ما هنا يصلح للاثنين.',
    t1bh='لا وقت لنقل الإجابات. إطلاقًا.',
    t1bb='في الاختبار الورقي يمنحك Listening عشر دقائق في النهاية لنقل '
         'إجاباتك. <strong>أما Reading فلا.</strong> اكتب على ورقة الإجابة أولًا '
         'بأول، لأن المراقب يوقفك عند تمام الساعة ويأخذها بما عليها.',
    t1bn='الإجابات التي تبقى على ورقة الأسئلة لا تُحتسب. وهذه أرخص طريقة '
         'لخسارة الدرجات في هذا الاختبار.',
    t1ch='الأسئلة تتبع ترتيب النص',
    t1cb='معظم أنواع الأسئلة تسير بترتيب النص، ومنها هذا النوع. بعد أربع '
         'إجابات تعرف تقريبًا أين الخامسة، فلا تحتاج أبدًا إلى البحث في النص '
         'كله مرتين.',
    t1cn='الاستثناءان هما Matching Headings وMatching Information، فهما '
         'يتنقّلان في النص.',

    t2Eyebrow='قبل أن تبدأ',
    t2Title='False وNot Given ليسا الإجابة نفسها',
    t2ah='FALSE: النص يقول العكس',
    t2ab='في النص جملة <strong>تناقض</strong> العبارة، ويمكنك أن تضع إصبعك '
         'عليها. لو طُلب منك أن تثبت خطأ العبارة، لأشرت إلى ذلك السطر.',
    t2an='رقم لا يتطابق، أو تاريخ لا يتوافق، أو «فقط» في مقابل «عدة»: كلها '
         'تناقضات.',
    t2bh='NOT GIVEN: النص صامت',
    t2bb='النص لا يقول ذلك ولا ينفيه. قد تكون العبارة صحيحة تمامًا في الواقع، '
         'لكن النص ببساطة لا يتطرّق إليها.',
    t2bn='ليست Not Given عقوبةً لأن شيئًا فاتك. إنها إجابة حقيقية، ونحو ثلث '
         'الإجابات كذلك.',
    t2ch='الاختبار سؤال واحد',
    t2cb='<strong>هل أستطيع أن أشير إلى الجملة؟</strong> إن كان الجواب نعم، '
         'فالإجابة True أو False بحسب ما تقوله. وإن كنت تستنتج، «لا بدّ أن '
         'يكون كذلك»، فالإجابة Not Given.',
    t2cn='الاستنتاج يشبه الفهم، ولهذا بالذات يكلّف هنا درجات كثيرة.',

    t3Eyebrow='قبل أن تبدأ',
    t3Title='أجب من النص، لا مما تعرفه أبدًا',
    t3ah='معرفتك هي الفخّ',
    t3ab='قد تكون العبارة صحيحة تمامًا في الواقع ومع ذلك Not Given في النص. '
         'الممتحن لا يسألك هل هي صحيحة، بل يسألك ماذا يقول هذا النص.',
    t3an='ولهذا تكون نتائج المتقدّمين أسوأ في الموضوعات التي يعرفونها جيدًا.',
    t3bh='TRUE تعني أن النص يقول ذلك',
    t3bb='بكلمات أخرى في الأغلب. فالنص لا يكرّر العبارة بل يعيد صياغتها. '
         'مطابقة المعنى هي المهارة، ومطابقة الكلمات عادة يجب التخلّص منها.',
    t3bn='الجملتان <em>Attendance fell sharply after 1990</em> و<em>far fewer '
         'people came in the years that followed</em> تقولان الشيء نفسه دون '
         'كلمة مشتركة واحدة.',
    t3ch='مطابقة الكلمات تخذلك في الاتجاهين',
    t3cb='قد ترد الكلمات نفسها في جملة تقول العكس، وقد تعبّر جملة لا تشترك مع '
         'العبارة في أي كلمة عن معناها تمامًا. المفردات المشتركة تدلّك أين '
         'تبحث، لا بماذا تجيب.',
    t3cn='استخدم الكلمة المكرّرة لتجد السطر، ثم اقرأ السطر.',

    t4Eyebrow='قبل أن تبدأ',
    t4Title='كلمة واحدة تحسم ثلث هذه الأسئلة',
    t4ah='المطلقات',
    t4ab='كلمات مثل <em>All</em> و<em>every</em> و<em>never</em> '
         'و<em>only</em>: النص الذي يقول <em>most</em> يجعل العبارة التي تقول '
         '<em>all</em> خاطئة FALSE، فلا يمكن أن يصحّ الاثنان معًا، وهذا تناقض '
         'يمكنك الإشارة إليه.',
    t4an='عبارة <em>Most islanders</em> مقابل <em>every islander</em> هي False '
         'لا Not Given.',
    t4bh='التلطيف',
    t4bb='كلمات مثل <em>May</em> و<em>might</em> و<em>is thought to</em> '
         'و<em>suggests</em>: النص الملطَّف لا ينفي العبارة الجازمة، بل لا '
         'يقولها أصلًا. وهذا الشكل يكون عادةً Not Given.',
    t4bn='الفرق عن المطلق: <em>most</em> تستبعد <em>all</em>، أما <em>may</em> '
         'فلا تستبعد شيئًا.',
    t4ch='المقارنة تحتاج إلى الطرفين',
    t4cb='عبارات مثل <em>Wetter than</em> و<em>the largest</em> و<em>more '
         'common than</em>: تأكّد أن النص يقارن فعلًا بين الشيئين نفسيهما، '
         'فالنص الذي يتحدث عن أحدهما لا يدعم عبارة عن الاثنين.',
    t4cn='نص يذكر رقمًا واحدًا وعبارة ترتّب شيئين: هذا Not Given في كل مرة.',

    mcaEyebrow='النشاط 1 · False أم Not Given؟',
    mcaTitle='اقرأ النص، ثم اقرأ العبارة.',
    mcbEyebrow='النشاط 2 · النص لا العالم',
    mcbTitle='ماذا يقول هذا النص فعلًا؟',
    mccEyebrow='النشاط 3 · الكلمة الحاسمة',
    mccTitle='Most, all, may, never',

    r1why='يقول النص إن المتحف لم يُغلق قط، <em>not even during the two '
          'wars</em>. وهذه هي العبارة بكلمات أخرى. TRUE.',
    r2why='مرتان في اليوم صيفًا، كما يقول النص. والرقم ثلاثة يناقض رقمًا في '
          'النص، وهذا تناقض يمكنك الإشارة إليه. FALSE.',
    r3why='النص يعدّ المجلدات المكتوبة بالويلزية، ولا يقول شيئًا على الإطلاق '
          'عمّا تنوي المكتبة فعله. NOT GIVEN.',
    r4why='بدأ البناء عام 1954 وانتهى بعد عامين. النص يعطيك العملية الحسابية '
          'بدل التاريخ، وإعادة الصياغة تشمل إجراء الجمع. TRUE.',
    r5why='يقول النص إن الضوء المستقطب يبقى صالحًا للاستخدام <em>when the sun '
          'is behind cloud</em>، وهذا عكس العبارة. FALSE، ولاحظ أن كلمة '
          '«overcast» لا ترد في النص أبدًا.',
    r6why='المطحنة والقرية والاعتماد عليها كلها في النص. أما البيع والمنافس '
          'وعام 1902 فلا. NOT GIVEN.',
    r7why='سبعون في المئة هي الأغلبية. العبارة تعيد صياغة الرقم بدل تكراره، '
          'وهذا هو الشكل المعتاد لـ TRUE.',
    r8why='يقول النص ما شمله المسح، لا من موّله. والتساؤل عن التمويل أمر '
          'معقول، لكن النص لا يتطرّق إليه. NOT GIVEN.',
    r9why='كلمة <em>Most</em> في النص مقابل <em>every</em> في العبارة. '
          'الأغلبية تناقض المطلق، لذا فهي FALSE لا Not Given.',
    r10why='النص يلطّف الكلام عن مدة التعافي ولا يقول شيئًا على الإطلاق عن '
           'الموافقة. صمت لا نفي. NOT GIVEN.',
    r11why='قلة المطر في الوادي تعني ساحلًا أكثر مطرًا: العبارة نفسها مقلوبة. '
           'والكلمتان اللتان تحملانها، <em>lower</em> و<em>wetter</em>، لا '
           'يجمعهما شيء، ولهذا تفوتها مطابقة الكلمات. TRUE.',
    r12why='عبارة <em>Apart from two years in the 1980s</em> هي السطر الذي '
           'تشير إليه، و<em>never once</em> لا تصمد أمامه. FALSE.',

    sortEyebrow='النشاط 4 · ما الذي يرجّح كل جهة',
    sortTitle='صنِّف الإشارات الست',
    sortHint='اسحب كل إشارة إلى عمود، أو انقر عليها ثم على العمود الذي تريده.',
    sortBin1='يشير إلى FALSE',
    sortBin2='يشير إلى NOT GIVEN',
    sortWhy='كل ما في عمود «يشير إلى FALSE» يسمّي <strong>جملة يمكنك أن تشير '
            'إليها</strong>. وكل ما في العمود الآخر طريقة للوصول إلى حكم من '
            'دونها: الاستنتاج أو الربط أو المعلومات العامة. هذا هو الفرق كله: '
            'FALSE تحتاج إلى سطر في النص يقول العكس، فإن لم تستطع أن تضع إصبعك '
            'عليه فالإجابة NOT GIVEN.',

    actTitle='أثبِتها من النص',
    actUse='استخدم ثلاثة منها على الأقل:',
    actSpeakBrief='اعملا في ثنائي، ومعكما أي نص، ويكفي خبر صحفي. يكتب أحدكما '
                  'أربع عبارات عنه: واحدة صحيحة، وواحدة خاطئة، واثنتين غير '
                  'مذكورتين. تبادلا وأجيبا، ثم دافعا عن كل حكم بقراءة السطر '
                  'الذي بنيتماه عليه. لا سطر، لا FALSE.',
    actSpeak1='على من يجيب أن يقول بصوت عالٍ أي جملة حسمت الأمر قبل أن يُقبل '
              'الحكم.',
    actSpeak2='في كل NOT GIVEN، قل ما كان ينبغي أن يتضمّنه النص لتكون الإجابة '
              'FALSE.',
    actSpeak3='جِد بين عبارات زميلك عبارة يمكن الدفاع عنها في الاتجاهين، وأعد '
              'صياغتها بحيث لا يمكن ذلك.',
    actWriteKind='الكتابة · 150–200 كلمة',
    actWriteBrief='خذ نصًّا واكتب عنه ثلاث عبارات، واحدة TRUE وواحدة FALSE '
                  'وواحدة NOT GIVEN، ثم اكتب مفتاح الإجابة مع ذكر الجملة '
                  'الدقيقة التي تحسم كل واحدة، أو القول صراحةً إنه لا توجد جملة '
                  'تحسمها.',
    actPlaceholder='Statement 1 (TRUE): … The line that decides it: …',
)


# ── Chinese ────────────────────────────────────────────────────────────
T['zh'] = dict(
    coverTitle='True, False, <em>Not Given</em>',
    coverSub='阅读考试里最丢分的题型——而把分拿回来靠的是技巧，不是词汇',
    chipLevel='C1 · 高级', chipFocus='Reading · 两个模块通用',
    chipCount='18 分',

    optT='True &mdash; 文中明确这样说',
    optF='False &mdash; 文中明确否定这一点',
    optN='Not Given &mdash; 文中没有提到',

    t1Eyebrow='开始之前',
    t1Title='六十分钟，三个部分，最后没有时间',
    t1ah='试卷的结构',
    t1ab='六十分钟四十道题，分三个部分，每部分大约二十分钟。第三部分通常最难——'
         '所以哪一部分拖延了，占用的就是最需要时间的那一部分。',
    t1an='Academic 每部分一篇长文；General Training 从较短的文章开始。技巧相同，'
         '所以这里讲的一切两者都适用。',
    t1bh='没有誊写时间，一分钟都没有。',
    t1bb='纸笔考试中，Listening 最后有十分钟让你把答案誊到答题卡上。'
         '<strong>Reading 没有。</strong>边做边写在答题卡上，因为时间一到，监考'
         '就会把答题卡照原样收走。',
    t1bn='留在题目册上的答案一分不得。这是这门考试里最冤枉的丢分方式。',
    t1ch='题目顺序跟着文章走',
    t1cb='大多数题型按文章顺序出题，这一种也是。答完四道，你大致就知道第五道在'
         '哪里——永远不必把整篇文章找两遍。',
    t1cn='Matching Headings 和 Matching Information 是例外，它们会跳来跳去。',

    t2Eyebrow='开始之前',
    t2Title='False 和 Not Given 不是同一个答案',
    t2ah='FALSE：文中说的正好相反',
    t2ab='文中有一句话<strong>与题干相矛盾</strong>，你能用手指指出来。如果有人'
         '让你证明题干是错的，你会指着那一行。',
    t2an='数字对不上、日期不吻合、“只有”对“好几个”——都是矛盾。',
    t2bh='NOT GIVEN：文中没有说',
    t2bb='文中既没有这么说，也没有否认。题干在现实中可能完全正确，只是文章根本'
         '没有涉及。',
    t2bn='Not Given 不是因为你漏看了什么而受的惩罚。它是真正的答案，大约三分之一'
         '的题都是它。',
    t2ch='检验只有一个问题',
    t2cb='<strong>我能指出是哪一句吗？</strong>能，答案就是 True 或 False，看那'
         '句话怎么说。如果你是在推理——“嗯，应该是这样吧”——答案就是 Not Given。',
    t2cn='推理感觉像是理解了，正因如此，它在这里才让人丢那么多分。',

    t3Eyebrow='开始之前',
    t3Title='根据文章作答，绝不根据你知道的',
    t3ah='你的知识就是陷阱',
    t3ab='一个说法可能在现实中完全正确，在文中却仍然是 Not Given。考官问的不是'
         '它对不对，而是这篇文章说了什么。',
    t3an='这就是为什么考生在自己熟悉的话题上反而得分更低。',
    t3bh='TRUE 表示文中说了',
    t3bb='几乎总是换了说法。文章不会重复题干，而是改写它。匹配意思才是技能——'
         '匹配字词是要改掉的习惯。',
    t3bn='<em>Attendance fell sharply after 1990</em> 和 <em>far fewer people '
         'came in the years that followed</em> 是同一个说法，却没有一个相同'
         '的词。',
    t3ch='对字词两头都会失灵',
    t3cb='同样的词可能出现在意思相反的句子里，而一个字面上毫无重合的句子却可能'
         '恰好表达了题干的意思。相同的词汇告诉你去哪里找，从不告诉你答什么。',
    t3cn='用重复出现的词找到那一行，然后读那一行。',

    t4Eyebrow='开始之前',
    t4Title='一个词决定了三分之一的题',
    t4ah='绝对词',
    t4ab='<em>All</em>、<em>every</em>、<em>never</em>、<em>only</em>。文中说 '
         '<em>most</em>，题干说 <em>all</em>，题干就是 FALSE——两者不能同时'
         '成立，而这是可以指出来的矛盾。',
    t4an='<em>Most islanders</em> 对 <em>every islander</em>，是 False，不是 '
         'Not Given。',
    t4bh='模糊限制语',
    t4bb='<em>May</em>、<em>might</em>、<em>is thought to</em>、'
         '<em>suggests</em>。用了模糊限制语的文章并不否认一个肯定的说法——它只是'
         '从来没这么说。这种情况通常是 Not Given。',
    t4bn='与绝对词的区别：<em>most</em> 排除了 <em>all</em>，而 <em>may</em> '
         '什么也不排除。',
    t4ch='比较要两边都有',
    t4cb='<em>Wetter than</em>、<em>the largest</em>、<em>more common '
         'than</em>。确认文章真的在比较同样的两样东西——只讲其中一样的文章，'
         '支撑不了关于两者的说法。',
    t4cn='文中只给一个数字，题干却对两样东西排序：每次都是 Not Given。',

    mcaEyebrow='练习 1 · False 还是 Not Given？',
    mcaTitle='先读文章，再读题干。',
    mcbEyebrow='练习 2 · 看文章，不看现实',
    mcbTitle='这篇文章到底说了什么？',
    mccEyebrow='练习 3 · 起决定作用的词',
    mccTitle='Most, all, may, never',

    r1why='文中说博物馆从未关闭，<em>not even during the two wars</em>。这就是'
          '题干，只是换了说法。TRUE。',
    r2why='文中说夏天每天两班。三是一个与文中数字相矛盾的数字，这个矛盾可以指'
          '出来。FALSE。',
    r3why='文中数的是威尔士语藏书，对图书馆打算做什么只字未提。NOT GIVEN。',
    r4why='1954 年动工，两年后完工。文中给你的是算式而不是日期，而改写也包括做'
          '这道加法。TRUE。',
    r5why='文中说偏振光 <em>when the sun is behind cloud</em> 时依然可用——与题'
          '干正好相反。FALSE。注意，文中从没用过“overcast”这个词。',
    r6why='磨坊、村子以及村子对它的依赖都在文中；出售、竞争对手和 1902 年都不'
          '在。NOT GIVEN。',
    r7why='百分之七十就是大部分。题干改写了这个数字而不是照搬，TRUE 通常就是这'
          '个样子。',
    r8why='文中说的是调查覆盖了哪些人，而不是谁出的钱。想知道经费来源很合理，但'
          '文章没有涉及。NOT GIVEN。',
    r9why='文中的 <em>Most</em> 对题干的 <em>every</em>。多数与绝对说法相矛'
          '盾，所以是 FALSE，而不是 Not Given。',
    r10why='文中对康复时间用了模糊限制语，对审批则只字未提。是沉默，不是否认。'
           'NOT GIVEN。',
    r11why='山谷雨少，就是海岸更湿——同一个说法反过来讲。承载它的两个词 '
           '<em>lower</em> 和 <em>wetter</em> 毫无共同之处，所以对字词会漏掉'
           '它。TRUE。',
    r12why='<em>Apart from two years in the 1980s</em> 就是你要指出的那一行。'
           '<em>Never once</em> 经不起它。FALSE。',

    sortEyebrow='练习 4 · 什么让你倒向哪一边',
    sortTitle='给这六个信号分类',
    sortHint='把每一项拖到一栏里——或者先点一项，再点你想放进的那一栏。',
    sortBin1='指向 FALSE',
    sortBin2='指向 NOT GIVEN',
    sortWhy='左栏的每一项都指向一句<strong>你能指出来的话</strong>。右栏的每一项'
            '都是在没有这样一句话的情况下得出结论的方式：推理、联想或常识。区别'
            '就在这里：FALSE 需要文中有一行说法相反的话，如果你指不出来，答案就'
            '是 NOT GIVEN。',

    actTitle='用文章来证明',
    actUse='至少用上三个：',
    actSpeakBrief='两人一组，手边随便找一篇文章——新闻报道就行。一人就这篇文章写'
                  '四个说法：一个对的、一个错的、两个文中没提到的。交换、作答，'
                  '然后读出你判断所依据的那一行，为每个判断辩护。指不出那一行，'
                  '就不能判 FALSE。',
    actSpeak1='答题的人必须在判断被接受之前，大声说出是哪一句决定了答案。',
    actSpeak2='每个 NOT GIVEN，说说文章里要有什么内容，答案才会变成 FALSE。',
    actSpeak3='在同伴写的说法里找一个两种判断都说得通的，把它改写到只有一种判断'
              '成立。',
    actWriteKind='写作 · 150–200 词',
    actWriteBrief='找一篇文章，就它写三个说法——一个 TRUE、一个 FALSE、一个 NOT '
                  'GIVEN——然后写出答案：每一个都注明起决定作用的那一句原话，或者'
                  '明确说明没有这样的句子。',
    actPlaceholder='Statement 1 (TRUE): … The line that decides it: …',
)


# ── Japanese ───────────────────────────────────────────────────────────
T['ja'] = dict(
    coverTitle='True, False, <em>Not Given</em>',
    coverSub='Reading で最も点を落とす問題形式。そして、語彙ではなくテクニックで'
             '取り戻せる形式です',
    chipLevel='C1 · 上級', chipFocus='Reading · 両モジュール共通',
    chipCount='18 点',

    optT='True &mdash; 本文にはっきり書かれています',
    optF='False &mdash; 本文がはっきり否定しています',
    optN='Not Given &mdash; 本文には書かれていません',

    t1Eyebrow='始める前に',
    t1Title='60分、3セクション、最後に時間はなし',
    t1ah='試験の形',
    t1ab='60分で40問、各20分ほどの3セクションです。ふつう3つ目が最も難しいの'
         'で、どこかのセクションが長引くと、いちばん時間が必要なセクションから'
         '時間を奪うことになります。',
    t1an='Academic は各セクションに長文が1つ、General Training は短めの文章から'
         '始まります。テクニックは同じなので、ここで学ぶことはどちらにも使え'
         'ます。',
    t1bh='転記の時間はありません。一切。',
    t1bb='ペーパー試験の Listening には、最後に解答を書き写す時間が10分あります。'
         '<strong>Reading にはありません。</strong>解答用紙に直接書き進めてくだ'
         'さい。時間になると、試験官はそのままの状態で回収します。',
    t1bn='問題用紙に書いたままの答えは採点されません。この試験で最ももったいない'
         '失点のしかたです。',
    t1ch='設問は本文の順番どおり',
    t1cb='ほとんどの形式は本文の順に出題され、この形式もそうです。4問答えれば5'
         '問目のだいたいの位置がわかり、本文全体を二度探す必要はありません。',
    t1cn='例外は Matching Headings と Matching Information です。この二つは'
         'あちこちに飛びます。',

    t2Eyebrow='始める前に',
    t2Title='False と Not Given は同じ答えではない',
    t2ah='FALSE：本文が逆のことを言っている',
    t2ab='本文に、設問の文と<strong>矛盾する</strong>文があります。指で指し示す'
         'ことができます。設問が間違いだと証明するよう求められたら、その行を指'
         'すでしょう。',
    t2an='合わない数字、一致しない日付、「〜だけ」に対する「いくつか」――どれも'
         '矛盾です。',
    t2bh='NOT GIVEN：本文は何も言っていない',
    t2bb='本文はそうだとも、そうでないとも言っていません。設問の内容は現実には'
         '正しいかもしれませんが、本文はそこに触れていないだけです。',
    t2bn='Not Given は何かを見落とした罰ではありません。れっきとした答えで、全体'
         'のおよそ3分の1がそうです。',
    t2ch='確かめる問いは一つ',
    t2cb='<strong>その文を指させるか？</strong>指させるなら、答えはその文の内容'
         'に応じて True か False です。推論している――「まあ、そうに違いない」――'
         'なら、答えは Not Given です。',
    t2cn='推論は理解したような気にさせます。だからこそ、ここで多くの点を失うの'
         'です。',

    t3Eyebrow='始める前に',
    t3Title='知識ではなく、本文から答える',
    t3ah='あなたの知識こそが罠',
    t3ab='現実にはまったく正しい内容でも、本文では Not Given ということがあり'
         'ます。試験官が問うているのは、それが正しいかどうかではありません。'
         'この本文が何を言っているかです。',
    t3an='だから受験者は、よく知っている話題ほど点が取れないのです。',
    t3bh='TRUE は本文がそう言っているということ',
    t3bb='ほぼ必ず別の言葉で言っています。本文は設問をそのまま繰り返さず、言い'
         '換えます。意味を照合するのが技能であり、語句を照合するのはやめるべき'
         '癖です。',
    t3bn='<em>Attendance fell sharply after 1990</em> と <em>far fewer people '
         'came in the years that followed</em> は、共通の語が一つもないのに'
         '同じ内容です。',
    t3ch='語句の照合はどちらの方向にも失敗する',
    t3cb='同じ語句が逆のことを言う文に入っていることもあれば、共通の語が一つも'
         'ない文が設問の内容をそのまま述べていることもあります。共通の語句が教'
         'えてくれるのは探す場所であって、答えではありません。',
    t3cn='繰り返されている語で該当行を見つけ、それからその行を読みましょう。',

    t4Eyebrow='始める前に',
    t4Title='3分の1は一語で決まる',
    t4ah='絶対表現',
    t4ab='<em>All</em>、<em>every</em>、<em>never</em>、<em>only</em>。本文が '
         '<em>most</em> なら、<em>all</em> と言う設問は FALSE です――両方が同時に'
         '成り立つことはなく、それは指で示せる矛盾です。',
    t4an='<em>Most islanders</em> 対 <em>every islander</em> は False で、Not '
         'Given ではありません。',
    t4bh='ぼかし表現',
    t4bb='<em>May</em>、<em>might</em>、<em>is thought to</em>、'
         '<em>suggests</em>。ぼかした本文は、言い切った設問を否定しているわけで'
         'はなく、そもそもそうは言っていないのです。この形はたいてい Not Given '
         'です。',
    t4bn='絶対表現との違い：<em>most</em> は <em>all</em> を排除しますが、'
         '<em>may</em> は何も排除しません。',
    t4ch='比較には両側が必要',
    t4cb='<em>Wetter than</em>、<em>the largest</em>、<em>more common '
         'than</em>。本文が本当に同じ二つのものを比べているか確かめましょう。'
         '片方だけについての本文では、二つについての主張は裏づけられません。',
    t4cn='数字を一つだけ挙げる本文と、二つを順位づける設問――これは毎回 Not '
         'Given です。',

    mcaEyebrow='演習 1 · False か Not Given か？',
    mcaTitle='本文を読み、それから設問の文を読みましょう。',
    mcbEyebrow='演習 2 · 世の中ではなく本文',
    mcbTitle='この本文は実際に何と言っているか？',
    mccEyebrow='演習 3 · 決め手の一語',
    mccTitle='Most, all, may, never',

    r1why='本文は博物館が一度も閉館しなかったと述べています。<em>not even '
          'during the two wars</em>。これが別の言葉で言った設問の内容です。'
          'TRUE。',
    r2why='本文によれば夏は1日2便です。3は本文中の数字と矛盾する数字で、指で示'
          'せる矛盾です。FALSE。',
    r3why='本文はウェールズ語の蔵書の数を述べているだけで、図書館が今後何をする'
          'つもりかにはまったく触れていません。NOT GIVEN。',
    r4why='1954年に着工し、2年後に完成。本文は日付ではなく計算を示しており、言'
          'い換えには足し算も含まれます。TRUE。',
    r5why='本文は、偏光は <em>when the sun is behind cloud</em> でも使えると述べ'
          'ています――設問とは逆です。FALSE。なお「overcast」という語は本文に一'
          '度も出てきません。',
    r6why='水車小屋、村、そしてその依存関係はすべて本文にあります。売却、競合相'
          '手、1902年はありません。NOT GIVEN。',
    r7why='70パーセントは大部分です。設問は数字をそのまま繰り返さず言い換えてい'
          'ます。TRUE はたいていこういう形です。',
    r8why='本文が述べているのは調査の対象で、誰が費用を出したかではありません。'
          '資金について知りたくなるのは自然ですが、本文はそこに触れていません。'
          'NOT GIVEN。',
    r9why='本文の <em>Most</em> 対 設問の <em>every</em>。多数派は絶対表現と矛'
          '盾するので、Not Given ではなく FALSE です。',
    r10why='本文は回復期間についてぼかしていて、承認については何ひとつ述べていま'
           'せん。否定ではなく沈黙です。NOT GIVEN。',
    r11why='谷のほうが雨が少ないということは、海岸のほうが雨が多いということ――同'
           'じ内容を裏返したものです。それを担う <em>lower</em> と '
           '<em>wetter</em> には共通点がないので、語句の照合では見逃します。'
           'TRUE。',
    r12why='<em>Apart from two years in the 1980s</em> が指し示す行です。'
           '<em>Never once</em> はこれに耐えられません。FALSE。',

    sortEyebrow='演習 4 · どちらに傾かせるか',
    sortTitle='六つのシグナルを分類しましょう',
    sortHint='それぞれを列にドラッグしてください。または項目をクリックしてから、'
             '入れたい列をクリックします。',
    sortBin1='FALSE を示す',
    sortBin2='NOT GIVEN を示す',
    sortWhy='左の列はすべて<strong>指し示せる文</strong>を挙げています。右の列は'
            'すべて、そうした文なしに判定に至るやり方です――推論、連想、一般常識。'
            '違いはこれに尽きます。FALSE には本文に逆のことを言う行が必要で、それ'
            'を指し示せないなら答えは NOT GIVEN です。',

    actTitle='本文で証明する',
    actUse='少なくとも三つ使いましょう：',
    actSpeakBrief='ペアで、手近な文章を一つ用意します。ニュース記事で十分です。'
                  '一人がその文章について四つの文を書きます：正しいもの一つ、誤り'
                  '一つ、書かれていないもの二つ。交換して答え、根拠にした行を読み'
                  '上げてそれぞれの判定を説明します。行がなければ FALSE はなし'
                  'です。',
    actSpeak1='答える人は、判定が認められる前に、どの文が決め手になったかを声に'
              '出して言いましょう。',
    actSpeak2='NOT GIVEN のたびに、答えが FALSE になるには本文に何が書かれている'
              '必要があったかを言いましょう。',
    actSpeak3='相手の文の中から、どちらとも取れるものを一つ見つけ、そうならないよ'
              'うに書き直しましょう。',
    actWriteKind='ライティング · 150–200 語',
    actWriteBrief='文章を一つ選び、それについて三つの文――TRUE、FALSE、NOT GIVEN '
                  'を一つずつ――を書きましょう。次に解答を書き、それぞれについて'
                  '決め手となる文を正確に示すか、決め手となる文がないことをはっ'
                  'きり書きます。',
    actPlaceholder='Statement 1 (TRUE): … The line that decides it: …',
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
