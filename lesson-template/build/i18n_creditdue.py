# -*- coding: utf-8 -*-
"""Interface strings for Credit Where It's Due (C1) — EN, DE, ES, RU.

HOUSE-STYLE §8, and the same boundary its sibling draws: the chrome
translates, and every line the learner is expected to SAY stays English.
So stems, options, gap sentences, the word banks, the sort items, the order
chunks and the phrase-bank round are English in all four languages; the
titles, eyebrows, hints, the cards that explain a rule, the situation lines
and the activation briefs are not.

The two FORM cards carry no head key. Their headings ARE the pattern —
WHAT + CLAUSE + WAS / IS, and I + PAST SIMPLE against IT + WAS + DONE — so
they stay English everywhere. A translated heading over an English pattern
is the half-finished screen §8 exists to prevent.

resNext and actSpeakKind are declared here rather than lifted from CHROME,
because the builder emits its own text in both slots; lifting one and
emitting the other is what makes a slide change when a learner switches
language and back.

Two lengths are load-bearing and were measured, not guessed. `actUse` is
short in German and Russian because a longer label wraps the chip row to a
third line and the row comes straight out of the activation panel's height.
Every activation brief is one line for the same reason — the panel clips at
--act-panel-h and the list no longer scrolls, so a task that runs to two
lines is a task the class never sees.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'btnFull',
        'scoreLabel', 'slideOf', 'fbCorrect', 'fbWrong', 'fbAnswer',
        'btnCopy', 'btnCopied', 'wordCount', 'actEyebrow', 'actSpeakWord',
        'actWriteWord']

# Template chrome no lesson declares, which the I18N gate still resolves.
TAIL = {
    'en': {'branchLocked': "'Your ledger does not support this ending'",
           'glossHide': "'Hide'", 'glossShow': "'Translate'",
           'ledClues': "'Clues'", 'ledDp': "'DP'", 'ledTime': "'Time'"},
    'de': {'branchLocked': "'Dein Protokoll trägt dieses Ende nicht'",
           'glossHide': "'Ausblenden'", 'glossShow': "'Übersetzen'",
           'ledClues': "'Hinweise'", 'ledDp': "'DP'", 'ledTime': "'Zeit'"},
    'es': {'branchLocked': "'Tu registro no permite este final'",
           'glossHide': "'Ocultar'", 'glossShow': "'Traducir'",
           'ledClues': "'Pistas'", 'ledDp': "'DP'", 'ledTime': "'Tiempo'"},
    'ru': {'branchLocked': "'Ваш журнал не допускает такой финал'",
           'glossHide': "'Скрыть'", 'glossShow': "'Перевести'",
           'ledClues': "'Подсказки'", 'ledDp': "'DP'", 'ledTime': "'Время'"},
}

T = {}

T['en'] = dict(
    coverTitle='Credit Where It&rsquo;s <em>Due</em>',
    coverSub='You said it on Tuesday. He said it on Thursday. The room heard '
             'it on Thursday.',
    chipLevel='C1 &middot; Recognition at work',
    chipFocus='Claiming work without grandstanding',
    chipCount='COUNT slides',

    caseEyebrow='The situation',
    caseTitle='Said on Tuesday, heard on Thursday',
    caseH1='What you did',
    case1='You proposed it in a Tuesday stand-up, in one sentence, and nobody '
          'picked it up.',
    caseN1='One sentence in a stand-up is still a proposal.',
    caseH2='What he did',
    case2='On Thursday he put the same idea to the director, in more detail, '
          'as his own.',
    caseN2='More detail is not more authorship.',
    caseH3='What the room believes',
    case3='The room believes what it heard last, from whoever had the floor '
          'longest.',
    caseN3='You are not correcting a lie. You are correcting a record.',

    cleftEyebrow='The first move',
    cleftTitle='Put your name in the sentence',
    cleftN1='Front-loads the author, not the argument.',
    cleftH2='Why not just say it was yours',
    cleft2='&ldquo;That was mine&rdquo; asks the room to judge two people. A '
           'cleft asks it to remember a date.',
    cleftN2='You want the record corrected, not a winner declared.',

    termsEyebrow='The vocabulary',
    termsTitleA='Taking it, and giving it',
    termsTitleB='Showing what was yours',
    termsHint='Click a term, then the line that defines it.',

    reclaimEyebrow='Say it in the room',
    reclaimTitle='Complete the line',
    reclaimHint='One word per gap; each is used once across both screens.',
    bankLabel='Word bank:',

    roomEyebrow='In the room',
    roomTitle='What do you actually say?',
    roomCtx1='He has just put your Tuesday idea to the director as his own.',
    roomCtx2='A colleague restates your point five minutes after you made it.',
    roomCtx3='The director thanks the team and names everyone but you.',

    movesEyebrow='Three moves',
    movesTitle='How credit actually gets recorded',
    movesH1='Reclaim in the room',
    moves1='Same meeting, one sentence, with a date in it. Then hand the floor '
           'straight back.',
    movesN1='Later is a complaint. Now is a correction.',
    movesH2='Build the trail',
    moves2='Put the idea in writing before the meeting, to more than one '
           'person. A dated line beats a good memory.',
    movesN2='Not suspicious. Legible.',
    movesH3='Give first, then take',
    moves3='Name two people, then name what you did. Generous first makes the '
           'claim sound like a fact.',
    movesN3='The order is the whole trick.',

    sortEyebrow='Before you say it',
    sortTitle='Claims it, or gives it away?',
    sortHint='Click a line, then the box it belongs in.',
    sortBin1='Puts your name on it',
    sortBin2='Signs it over to somebody else',

    ordEyebrow='Say it cleanly',
    ordTitle='Build the sentence',
    ordHint='Click the parts in order.',

    voiceEyebrow='Active or passive',
    voiceTitle='Which voice puts you in it',
    voiceN1='The passive hides the agent. Here the agent is the point.',
    voiceH2='Where the passive still earns its place',
    voice2='Use it for the parts that were not yours, so the parts that were '
           'stand out by contrast.',
    voiceN2='Two actives in a paragraph of passives are the two anybody reads.',

    numEyebrow='Put a number on it',
    numTitle='Complete the line',
    numHint='One word per gap; each is used once across both screens.',

    mailEyebrow='Before the meeting',
    mailTitle='Put it in writing first',
    mailCtx='You want the idea on the record before Thursday.',

    funcEyebrow='The phrase bank',
    funcTitle='What each line actually does',
    funcHint='Click a line, then the job it does in the room.',

    resNext='Now claim it out loud &rarr;',
    resPerfect='Full marks. You can hear the difference &mdash; saying it in '
               'the room is the harder half.',
    resStrong='Strong. Look again at the misses: most of them gave the work '
              'away politely.',
    resMid='A workable base. Re-read the cleft and the two voices before you '
           'speak.',
    resLow='Work through the three moves again. Nearly every miss is a passive '
           'where your own name belonged.',

    actTitle='Now claim it out loud',
    actUse='Use at least four:',
    actSpeakKind='Speaking',
    actSpeakBrief='In pairs. Three minutes each, then swap roles and run it '
                  'again.',
    actSpeak1='He has just presented your idea. Reclaim it in one sentence.',
    actSpeak2='Swap. The director thanks everyone but you. Get into the record.',
    actSpeak3='Same meeting, and he is a friend. What changes, and what must '
              'not?',
    actSpeak4='The other side: when is claiming credit the wrong move?',
    actWriteKind='Writing &middot; 180&ndash;220 words',
    actWriteBrief='The email that puts your idea on the record before Thursday: '
                  'one date, two numbers, one name that is not yours.',
    actPlaceholder='Ahead of Thursday &mdash; the two-week pilot I suggested in '
                   'Tuesday&rsquo;s stand-up, with the numbers behind '
                   'it&hellip;',
)

T['de'] = dict(
    coverTitle='Ehre, <em>wem</em> Ehre',
    coverSub='Sie haben es am Dienstag gesagt. Er am Donnerstag. Geh&ouml;rt '
             'hat der Raum den Donnerstag.',
    chipLevel='C1 &middot; Anerkennung im Job',
    chipFocus='Leistung zeigen, ohne sich aufzuspielen',
    chipCount='COUNT Folien',

    caseEyebrow='Die Ausgangslage',
    caseTitle='Dienstag gesagt, Donnerstag geh&ouml;rt',
    caseH1='Was Sie getan haben',
    case1='Sie haben es im Dienstags-Stand-up vorgeschlagen, in einem Satz, '
          'und niemand hat es aufgegriffen.',
    caseN1='Ein Satz im Stand-up ist trotzdem ein Vorschlag.',
    caseH2='Was er getan hat',
    case2='Am Donnerstag hat er dieselbe Idee der Direktorin vorgelegt, '
          'ausf&uuml;hrlicher, als seine eigene.',
    caseN2='Mehr Details sind nicht mehr Urheberschaft.',
    caseH3='Was der Raum glaubt',
    case3='Der Raum glaubt, was er zuletzt geh&ouml;rt hat &mdash; von dem, '
          'der am l&auml;ngsten das Wort hatte.',
    caseN3='Sie korrigieren keine L&uuml;ge. Sie korrigieren einen Eintrag.',

    cleftEyebrow='Der erste Schritt',
    cleftTitle='Bringen Sie Ihren Namen in den Satz',
    cleftN1='Stellt den Urheber nach vorn, nicht den Streit.',
    cleftH2='Warum nicht einfach sagen, es war Ihre Idee',
    cleft2='&bdquo;That was mine&ldquo; zwingt den Raum, zwischen zwei '
           'Personen zu urteilen. Ein Cleft-Satz l&auml;sst ihn nur ein Datum '
           'erinnern.',
    cleftN2='Sie wollen den Eintrag korrigiert, keinen Sieger.',

    termsEyebrow='Der Wortschatz',
    termsTitleA='Nehmen und geben',
    termsTitleB='Zeigen, was von Ihnen kam',
    termsHint='Klicken Sie auf einen Begriff und dann auf die Definition.',

    reclaimEyebrow='Sagen Sie es im Raum',
    reclaimTitle='Vervollst&auml;ndigen Sie den Satz',
    reclaimHint='Ein Wort pro L&uuml;cke; jedes wird auf beiden Bildschirmen '
                'einmal gebraucht.',
    bankLabel='Wortliste:',

    roomEyebrow='Im Raum',
    roomTitle='Was sagen Sie jetzt wirklich?',
    roomCtx1='Er hat Ihre Dienstags-Idee gerade als seine eigene vorgelegt.',
    roomCtx2='Ein Kollege wiederholt Ihren Punkt f&uuml;nf Minuten sp&auml;ter.',
    roomCtx3='Die Direktorin dankt dem Team und nennt alle au&szlig;er Ihnen.',

    movesEyebrow='Drei Schritte',
    movesTitle='Wie Anerkennung tats&auml;chlich festgehalten wird',
    movesH1='Im Raum zur&uuml;ckholen',
    moves1='Dieselbe Besprechung, ein Satz, mit Datum. Dann geben Sie das Wort '
           'sofort zur&uuml;ck.',
    movesN1='Sp&auml;ter ist eine Beschwerde. Jetzt ist eine Korrektur.',
    movesH2='Die Spur anlegen',
    moves2='Schreiben Sie die Idee vor der Besprechung auf, an mehr als eine '
           'Person. Eine datierte Zeile schl&auml;gt ein gutes Ged&auml;chtnis.',
    movesN2='Nicht misstrauisch. Nachvollziehbar.',
    movesH3='Erst geben, dann nehmen',
    moves3='Nennen Sie zwei Personen, dann Ihren Anteil. Zuerst gro&szlig;'
           'z&uuml;gig &mdash; dann klingt der Anspruch wie eine Tatsache.',
    movesN3='Die Reihenfolge ist der ganze Trick.',

    sortEyebrow='Bevor Sie es sagen',
    sortTitle='Beansprucht es &mdash; oder verschenkt es?',
    sortHint='Klicken Sie auf eine Zeile und dann auf das passende Feld.',
    sortBin1='Setzt Ihren Namen darauf',
    sortBin2='&Uuml;berschreibt es jemand anderem',

    ordEyebrow='Sauber formulieren',
    ordTitle='Bauen Sie den Satz',
    ordHint='Klicken Sie die Teile der Reihe nach an.',

    voiceEyebrow='Aktiv oder Passiv',
    voiceTitle='Welche Form bringt Sie hinein',
    voiceN1='Das Passiv verbirgt den Handelnden. Hier ist er der Punkt.',
    voiceH2='Wo das Passiv trotzdem hingeh&ouml;rt',
    voice2='F&uuml;r die Teile, die nicht von Ihnen kamen &mdash; dann heben '
           'sich Ihre durch den Kontrast ab.',
    voiceN2='Zwei Aktivs in einem Absatz voller Passivs sind die zwei, die '
            'gelesen werden.',

    numEyebrow='Machen Sie eine Zahl daraus',
    numTitle='Vervollst&auml;ndigen Sie den Satz',
    numHint='Ein Wort pro L&uuml;cke; jedes wird auf beiden Bildschirmen '
            'einmal gebraucht.',

    mailEyebrow='Vor der Besprechung',
    mailTitle='Erst schriftlich festhalten',
    mailCtx='Sie wollen die Idee vor Donnerstag aktenkundig haben.',

    funcEyebrow='Die Formulierungen',
    funcTitle='Was jede Zeile tats&auml;chlich bewirkt',
    funcHint='Klicken Sie auf eine Zeile und dann auf ihre Funktion.',

    resNext='Jetzt sagen Sie es laut &rarr;',
    resPerfect='Volle Punktzahl. Den Unterschied h&ouml;ren Sie &mdash; ihn im '
               'Raum zu sagen ist die schwerere H&auml;lfte.',
    resStrong='Stark. Sehen Sie sich die Fehler an: Die meisten haben die '
              'Arbeit h&ouml;flich verschenkt.',
    resMid='Brauchbare Grundlage. Lesen Sie den Cleft-Satz und die zwei Formen '
           'noch einmal.',
    resLow='Gehen Sie die drei Schritte noch einmal durch. Fast jeder Fehler '
           'ist ein Passiv, wo Ihr Name hingeh&ouml;rt h&auml;tte.',

    actTitle='Jetzt sagen Sie es laut',
    actUse='Mindestens vier:',
    actSpeakKind='Sprechen',
    actSpeakBrief='Zu zweit. Je drei Minuten, dann Rollen tauschen und noch '
                  'einmal durchspielen.',
    actSpeak1='Er hat gerade Ihre Idee vorgestellt. Holen Sie sie in einem '
              'Satz zur&uuml;ck.',
    actSpeak2='Tauschen. Die Direktorin dankt allen au&szlig;er Ihnen. Kommen '
              'Sie in den Eintrag.',
    actSpeak3='Dieselbe Besprechung, aber er ist ein Freund. Was &auml;ndert '
              'sich, was nicht?',
    actSpeak4='Die Gegenseite: Wann ist es falsch, Anerkennung einzufordern?',
    actWriteKind='Schreiben &middot; 180&ndash;220 W&ouml;rter',
    actWriteBrief='Die E-Mail, die Ihre Idee vor Donnerstag festh&auml;lt: ein '
                  'Datum, zwei Zahlen, ein Name, der nicht Ihrer ist.',
    actPlaceholder='Ahead of Thursday &mdash; the two-week pilot I suggested in '
                   'Tuesday&rsquo;s stand-up, with the numbers behind '
                   'it&hellip;',
)

T['es'] = dict(
    coverTitle='A quien <em>corresponde</em>',
    coverSub='T&uacute; lo dijiste el martes. &Eacute;l lo dijo el jueves. La '
             'sala oy&oacute; el jueves.',
    chipLevel='C1 &middot; Reconocimiento en el trabajo',
    chipFocus='Reclamar tu trabajo sin darte importancia',
    chipCount='COUNT diapositivas',

    caseEyebrow='La situaci&oacute;n',
    caseTitle='Dicho el martes, o&iacute;do el jueves',
    caseH1='Lo que hiciste',
    case1='Lo propusiste en la reuni&oacute;n del martes, en una frase, y nadie '
          'lo recogi&oacute;.',
    caseN1='Una frase en una reuni&oacute;n sigue siendo una propuesta.',
    caseH2='Lo que hizo &eacute;l',
    case2='El jueves llev&oacute; la misma idea a la directora, con m&aacute;s '
          'detalle, como suya.',
    caseN2='M&aacute;s detalle no es m&aacute;s autor&iacute;a.',
    caseH3='Lo que cree la sala',
    case3='La sala cree lo &uacute;ltimo que oy&oacute;, de quien tuvo la '
          'palabra m&aacute;s tiempo.',
    caseN3='No corriges una mentira. Corriges un registro.',

    cleftEyebrow='El primer movimiento',
    cleftTitle='Mete tu nombre en la frase',
    cleftN1='Pone delante al autor, no la discusi&oacute;n.',
    cleftH2='Por qu&eacute; no decir simplemente que era tuya',
    cleft2='&laquo;That was mine&raquo; obliga a la sala a juzgar entre dos '
           'personas. Una frase hendida solo le pide recordar una fecha.',
    cleftN2='Quieres el registro corregido, no un ganador.',

    termsEyebrow='El vocabulario',
    termsTitleA='Tomarlo y darlo',
    termsTitleB='Mostrar lo que fue tuyo',
    termsHint='Haz clic en un t&eacute;rmino y luego en su definici&oacute;n.',

    reclaimEyebrow='D&iacute;lo en la sala',
    reclaimTitle='Completa la frase',
    reclaimHint='Una palabra por hueco; cada una se usa una vez entre las dos '
                'pantallas.',
    bankLabel='Lista de palabras:',

    roomEyebrow='En la sala',
    roomTitle='&iquest;Qu&eacute; dices exactamente?',
    roomCtx1='Acaba de presentar tu idea del martes a la directora como suya.',
    roomCtx2='Un compa&ntilde;ero repite tu idea cinco minutos despu&eacute;s.',
    roomCtx3='La directora da las gracias al equipo y nombra a todos menos a ti.',

    movesEyebrow='Tres movimientos',
    movesTitle='C&oacute;mo queda registrado el m&eacute;rito',
    movesH1='Recup&eacute;ralo en la sala',
    moves1='La misma reuni&oacute;n, una frase, con una fecha dentro. Y devuelve '
           'la palabra enseguida.',
    movesN1='Despu&eacute;s es una queja. Ahora es una correcci&oacute;n.',
    movesH2='Construye el rastro',
    moves2='Pon la idea por escrito antes de la reuni&oacute;n, a m&aacute;s de '
           'una persona. Una l&iacute;nea con fecha gana a la memoria.',
    movesN2='No es desconfianza. Es dejar rastro.',
    movesH3='Primero dar, luego tomar',
    moves3='Nombra a dos personas y luego lo tuyo. Generoso primero: as&iacute; '
           'el m&eacute;rito suena a hecho.',
    movesN3='El orden es todo el truco.',

    sortEyebrow='Antes de decirlo',
    sortTitle='&iquest;Lo reclama o lo regala?',
    sortHint='Haz clic en una l&iacute;nea y luego en su caja.',
    sortBin1='Pone tu nombre encima',
    sortBin2='Se lo cede a otra persona',

    ordEyebrow='D&iacute;lo limpio',
    ordTitle='Construye la frase',
    ordHint='Haz clic en las partes por orden.',

    voiceEyebrow='Activa o pasiva',
    voiceTitle='Qu&eacute; voz te mete dentro',
    voiceN1='La pasiva esconde al agente. Aqu&iacute; el agente es el asunto.',
    voiceH2='D&oacute;nde s&iacute; vale la pasiva',
    voice2='Para las partes que no fueron tuyas, y as&iacute; las que s&iacute; '
           'destacan por contraste.',
    voiceN2='Dos activas en un p&aacute;rrafo de pasivas son las dos que se leen.',

    numEyebrow='Ponle un n&uacute;mero',
    numTitle='Completa la frase',
    numHint='Una palabra por hueco; cada una se usa una vez entre las dos '
            'pantallas.',

    mailEyebrow='Antes de la reuni&oacute;n',
    mailTitle='Primero por escrito',
    mailCtx='Quieres la idea registrada antes del jueves.',

    funcEyebrow='El banco de frases',
    funcTitle='Qu&eacute; hace realmente cada l&iacute;nea',
    funcHint='Haz clic en una l&iacute;nea y luego en su funci&oacute;n.',

    resNext='Ahora recl&aacute;malo en voz alta &rarr;',
    resPerfect='Puntuaci&oacute;n perfecta. Oyes la diferencia &mdash; decirlo '
               'en la sala es la mitad dif&iacute;cil.',
    resStrong='Muy bien. Mira los fallos: casi todos regalan el trabajo con '
              'mucha educaci&oacute;n.',
    resMid='Una base v&aacute;lida. Repasa la frase hendida y las dos voces '
           'antes de hablar.',
    resLow='Repasa los tres movimientos. Casi todos los fallos son una pasiva '
           'donde iba tu nombre.',

    actTitle='Ahora recl&aacute;malo en voz alta',
    actUse='Usa al menos cuatro:',
    actSpeakKind='Hablar',
    actSpeakBrief='En parejas. Tres minutos cada uno, luego cambiad de papel y '
                  'repetid.',
    actSpeak1='Acaba de presentar tu idea. Recup&eacute;rala en una frase.',
    actSpeak2='Cambiad. La directora nombra a todos menos a ti. Entra en el '
              'registro.',
    actSpeak3='La misma reuni&oacute;n, pero es amigo tuyo. &iquest;Qu&eacute; '
              'cambia y qu&eacute; no?',
    actSpeak4='La otra parte: &iquest;cu&aacute;ndo reclamar es un error?',
    actWriteKind='Escritura &middot; 180&ndash;220 palabras',
    actWriteBrief='El correo que deja tu idea registrada antes del jueves: una '
                  'fecha, dos n&uacute;meros, un nombre que no es el tuyo.',
    actPlaceholder='Ahead of Thursday &mdash; the two-week pilot I suggested in '
                   'Tuesday&rsquo;s stand-up, with the numbers behind '
                   'it&hellip;',
)

T['ru'] = dict(
    coverTitle='Заслуга — <em>чья</em>',
    coverSub='Вы сказали это во вторник. Он — в четверг. Зал услышал в четверг.',
    chipLevel='C1 &middot; Признание на работе',
    chipFocus='Заявить о своей работе без самолюбования',
    chipCount='COUNT слайдов',

    caseEyebrow='Ситуация',
    caseTitle='Сказано во вторник, услышано в четверг',
    caseH1='Что сделали вы',
    case1='Вы предложили это на летучке во вторник, одной фразой, и никто не '
          'подхватил.',
    caseN1='Одна фраза на летучке — всё равно предложение.',
    caseH2='Что сделал он',
    case2='В четверг он изложил ту же идею директору, подробнее, как свою.',
    caseN2='Больше подробностей — не больше авторства.',
    caseH3='Во что верит зал',
    case3='Зал верит тому, что услышал последним, — от того, кто дольше держал '
          'слово.',
    caseN3='Вы поправляете не ложь, а запись.',

    cleftEyebrow='Первый шаг',
    cleftTitle='Впишите своё имя во фразу',
    cleftN1='Впереди идёт автор, а не спор.',
    cleftH2='Почему не сказать просто, что идея ваша',
    cleft2='&laquo;That was mine&raquo; заставляет зал судить двух людей. '
           'Расщеплённая фраза просит лишь вспомнить дату.',
    cleftN2='Вам нужна исправленная запись, а не победитель.',

    termsEyebrow='Лексика',
    termsTitleA='Взять и отдать',
    termsTitleB='Показать, что было вашим',
    termsHint='Нажмите на термин, затем на строку с определением.',

    reclaimEyebrow='Скажите это в зале',
    reclaimTitle='Дополните фразу',
    reclaimHint='По одному слову в пропуск; каждое используется один раз на '
                'двух экранах.',
    bankLabel='Банк слов:',

    roomEyebrow='В зале',
    roomTitle='Что вы скажете на самом деле?',
    roomCtx1='Он только что изложил вашу вторничную идею директору как свою.',
    roomCtx2='Коллега повторяет вашу мысль через пять минут после вас.',
    roomCtx3='Директор благодарит команду и называет всех, кроме вас.',

    movesEyebrow='Три шага',
    movesTitle='Как заслуга попадает в запись',
    movesH1='Вернуть это в зале',
    moves1='Та же встреча, одна фраза, с датой внутри. И сразу верните слово.',
    movesN1='Потом — это жалоба. Сейчас — это поправка.',
    movesH2='Оставить след',
    moves2='Изложите идею письменно до встречи и не одному человеку. Строка с '
           'датой сильнее хорошей памяти.',
    movesN2='Не подозрительность. Прослеживаемость.',
    movesH3='Сначала отдать, потом взять',
    moves3='Назовите двоих, потом своё. Сначала щедрость — и притязание звучит '
           'как факт.',
    movesN3='Порядок — это и есть весь приём.',

    sortEyebrow='Прежде чем сказать',
    sortTitle='Заявляет или отдаёт?',
    sortHint='Нажмите на строку, затем на нужное поле.',
    sortBin1='Ставит на этом ваше имя',
    sortBin2='Переписывает это на другого',

    ordEyebrow='Скажите это чисто',
    ordTitle='Соберите фразу',
    ordHint='Нажимайте на части по порядку.',

    voiceEyebrow='Актив или пассив',
    voiceTitle='Какой залог оставляет вас внутри',
    voiceN1='Пассив прячет исполнителя. Здесь исполнитель — самое важное.',
    voiceH2='Где пассив всё же уместен',
    voice2='Для того, что делали не вы, — тогда ваше выделяется на контрасте.',
    voiceN2='Два актива среди пассивов — это те два, которые прочтут.',

    numEyebrow='Переведите в цифру',
    numTitle='Дополните фразу',
    numHint='По одному слову в пропуск; каждое используется один раз на двух '
            'экранах.',

    mailEyebrow='До встречи',
    mailTitle='Сначала письменно',
    mailCtx='Вы хотите зафиксировать идею до четверга.',

    funcEyebrow='Банк фраз',
    funcTitle='Что на самом деле делает каждая фраза',
    funcHint='Нажмите на строку, затем на её роль в разговоре.',

    resNext='Теперь скажите это вслух &rarr;',
    resPerfect='Полный балл. Разницу вы слышите — сказать это в зале труднее.',
    resStrong='Сильно. Посмотрите на ошибки: почти все вежливо отдают работу.',
    resMid='Рабочая основа. Перечитайте расщеплённую фразу и два залога.',
    resLow='Пройдите три шага заново. Почти каждая ошибка — пассив там, где '
           'должно стоять ваше имя.',

    actTitle='Теперь скажите это вслух',
    actUse='Минимум четыре:',
    actSpeakKind='Говорение',
    actSpeakBrief='В парах. По три минуты каждому, затем поменяйтесь ролями.',
    actSpeak1='Он только что представил вашу идею. Верните её одной фразой.',
    actSpeak2='Поменяйтесь. Директор благодарит всех, кроме вас. Войдите в запись.',
    actSpeak3='Та же встреча, но он ваш друг. Что меняется, а что нет?',
    actSpeak4='Другая сторона: когда заявлять о заслуге — ошибка?',
    actWriteKind='Письмо &middot; 180&ndash;220 слов',
    actWriteBrief='Письмо, которое фиксирует вашу идею до четверга: одна дата, '
                  'две цифры, одно чужое имя.',
    actPlaceholder='Ahead of Thursday &mdash; the two-week pilot I suggested in '
                   'Tuesday&rsquo;s stand-up, with the numbers behind '
                   'it&hellip;',
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
