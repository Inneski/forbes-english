# -*- coding: utf-8 -*-
"""Interface strings for IELTS Reading: True / False / Not Given.

English, German and Spanish, teach cards in the six-item form.

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
    coverTitle='True, False, <em>Not Given</em>',
    coverSub='The question type that loses the most marks on the Reading '
             'paper &mdash; and the one that technique, not vocabulary, gets '
             'back',
    chipLevel='C1 · Advanced', chipFocus='Reading · both modules',
    chipCount='18 points',

    t1Eyebrow='Before you start',
    t1Title='Sixty minutes, three passages, no time at the end',
    t1ah='The shape of the paper',
    t1ab='Three passages, forty questions, sixty minutes. Roughly twenty '
         'minutes each, and the third is usually the hardest &mdash; so a '
         'passage that runs long is borrowing from the one that needs it '
         'most.',
    t1an='Academic and General Training differ in the texts, not in the '
         'technique. Everything here applies to both.',
    t1bh='No transfer time. None.',
    t1bb='Listening gives you ten minutes at the end to copy your answers '
         'across. <strong>Reading does not.</strong> Write on the answer '
         'sheet as you go, because the invigilator stops you on the hour with '
         'whatever is on it.',
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
    r11why='Lower inland is wetter on the coast &mdash; the same claim turned '
           'round, with no word in common. TRUE, and a good example of why '
           'word-matching misses.',
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

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='True, False, <em>Not Given</em>',
    coverSub='Der Fragetyp, der im Reading die meisten Punkte kostet &mdash; '
             'und den Technik zurückholt, nicht Wortschatz',
    chipLevel='C1 · Fortgeschritten', chipFocus='Reading · beide Module',
    chipCount='18 Punkte',

    t1Eyebrow='Bevor du beginnst',
    t1Title='Sechzig Minuten, drei Texte, keine Zeit am Ende',
    t1ah='Der Aufbau der Prüfung',
    t1ab='Drei Texte, vierzig Fragen, sechzig Minuten. Etwa zwanzig Minuten '
         'pro Text, und der dritte ist meist der schwerste &mdash; wer bei '
         'einem Text überzieht, nimmt sie genau dem weg, der sie braucht.',
    t1an='Academic und General Training unterscheiden sich in den Texten, '
         'nicht in der Technik. Alles hier gilt für beide.',
    t1bh='Keine Übertragungszeit. Keine.',
    t1bb='Beim Listening bekommst du am Ende zehn Minuten, um die Antworten '
         'zu übertragen. <strong>Beim Reading nicht.</strong> Schreib direkt '
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
    r11why='Weniger Regen im Landesinneren heißt mehr an der Küste &mdash; '
           'dieselbe Aussage umgedreht, ohne ein gemeinsames Wort. TRUE, und '
           'ein gutes Beispiel dafür, warum Wortabgleich versagt.',
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
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='True, False, <em>Not Given</em>',
    coverSub='El tipo de pregunta que más puntos cuesta en el Reading, y el '
             'que se recupera con técnica, no con vocabulario',
    chipLevel='C1 · Avanzado', chipFocus='Reading · los dos módulos',
    chipCount='18 puntos',

    t1Eyebrow='Antes de empezar',
    t1Title='Sesenta minutos, tres textos, nada de tiempo al final',
    t1ah='La forma del examen',
    t1ab='Tres textos, cuarenta preguntas, sesenta minutos. Unos veinte '
         'minutos por texto, y el tercero suele ser el más difícil: si te '
         'alargas en uno, se los quitas justo al que más los necesita.',
    t1an='Academic y General Training se diferencian en los textos, no en la '
         'técnica. Todo esto vale para los dos.',
    t1bh='No hay tiempo de transcripción. Ninguno.',
    t1bb='En el Listening te dan diez minutos al final para pasar las '
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
    r11why='Que llueva menos tierra adentro es que la costa sea más húmeda: la '
           'misma afirmación del revés, sin una palabra en común. TRUE, y un '
           'buen ejemplo de por qué cotejar palabras falla.',
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
