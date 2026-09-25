# -*- coding: utf-8 -*-
"""Interface strings for Must & Have To — VfB Stuttgart (B1).

English, German, Spanish. Teach cards are six-item (the rule translates with
its heading); every explanation is a key, so it translates too; the English
under test — example sentences, stems, options, gap sentences, the chips —
stays English in every language (HOUSE-STYLE §8).

Grammar tokens are in CAPS and cited words in quotes, in all three languages
(SUBJECT + MUST + VERB; SUBJEKT / SUJETO in the translations).

The notes on the teaching cards are not word-for-word translations. The old
page glossed each form in Spanish (MUSTN'T = "no se puede / está
prohibido", DON'T HAVE TO = "no tener que / no es necesario"); those glosses
are kept in the Spanish notes. The German notes carry the trap that is
specific to German speakers and the reason this lesson exists for them:
MUSTN'T is "nicht dürfen", never "nicht müssen".
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'actEyebrow', 'btnCopy', 'btnCopied',
        'wordCount']

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

T['en'] = dict(
    coverTitle='Must &amp; <em>Have To</em>',
    coverSub='Positive and negative &mdash; the four key forms, in the colours '
             'of Stuttgart',
    chipLevel='B1 &middot; Intermediate',
    chipFocus='MUST &middot; HAVE TO &middot; the negative trap',
    chipCount='19 slides',

    taEyebrow='Tactics board &middot; 1 / 3',
    taTitle='Two ways to say it&rsquo;s necessary',
    ta1h='MUST &mdash; the speaker&rsquo;s own feeling',
    ta1b='Use MUST when the obligation comes from inside: your own belief, '
         'feeling or decision. <em>VfB must win this derby &mdash; it means '
         'everything!</em>',
    ta1n='MUST can also mean &ldquo;I&rsquo;m sure&rdquo;: <em>He must be '
         'exhausted after 120 minutes.</em> That is a conclusion, not an '
         'obligation.',
    ta2h='HAVE TO &mdash; a rule from outside',
    ta2b='Use HAVE TO when the obligation comes from outside: the rules, the '
         'referee, the coach. <em>VfB players have to wear red and white at '
         'home games.</em>',
    ta2n='In positive sentences both often work: <em>We must press / We have'
         ' to press.</em> In the negative, they split.',

    tbEyebrow='The critical rule &middot; 2 / 3',
    tbTitle='MUSTN&rsquo;T is not DON&rsquo;T HAVE TO',
    tb1h='MUSTN&rsquo;T &mdash; forbidden',
    tb1b='It is not allowed &mdash; by the rules, or by the speaker. '
         '<em>Players mustn&rsquo;t leave the pitch without the '
         'referee&rsquo;s permission.</em>',
    tb1n='Do it anyway: yellow card. Written rules use the full form: MUST '
         'NOT.',
    tb2h='DON&rsquo;T HAVE TO &mdash; not necessary',
    tb2b='There is no obligation &mdash; you can if you want to. <em>Players '
         'don&rsquo;t have to leave the pitch at half-time.</em>',
    tb2n='They can stay out and warm up if they like. One gets you a card; '
         'the other is just about where you stand.',

    tcEyebrow='The forms &middot; 3 / 3',
    tcTitle='MUST never changes. HAVE TO does.',
    tc1h='MUST &mdash; one form, always',
    tc1b='SUBJECT + MUST + VERB. No -S, no TO, no DO, no past form. <em>The '
         'keeper must stay focused.</em> Not &ldquo;musts&rdquo;, '
         '&ldquo;must stays&rdquo;, &ldquo;must to&rdquo; or &ldquo;does '
         '&hellip; must&rdquo;.',
    tc1n='For the past, use HAD TO &mdash; the past of both: <em>Yesterday '
         'VfB had to win.</em> Not &ldquo;Yesterday VfB must win&rdquo;.',
    tc2h='HAVE TO &mdash; a normal verb',
    tc2b='HAS TO with he, she and it. Questions and negatives use DO / DOES '
         '/ DID + HAVE TO: <em>Does the keeper have to wear gloves?</em> '
         '<em>The fans didn&rsquo;t have to queue for tickets.</em>',
    tc2n='After DOES and DIDN&rsquo;T, keep HAVE: not &ldquo;does &hellip; has '
         'to&rdquo;, not &ldquo;didn&rsquo;t had to&rdquo;.',

    gapEyebrow='Activity 1 &middot; Fill the gap',
    gapTitle='Complete the sentence',
    gapHint='Use a form from the bank. A contraction or the full form both '
            'count &mdash; &ldquo;mustn&rsquo;t&rdquo; or &ldquo;must '
            'not&rdquo;.',
    bankLabel='Word bank:',
    g1why='MUSTN&rsquo;T &mdash; handling the ball is forbidden by the rules, '
          'and the referee punishes it.',
    g2why='HAS TO &mdash; the striker is &ldquo;he&rdquo;, so HAVE becomes '
          'HAS, and the order comes from the coach. MUST is also correct.',
    g3why='DON&rsquo;T HAVE TO &mdash; &ldquo;if you prefer&rdquo; means it is '
          'their choice. It isn&rsquo;t forbidden, so not MUSTN&rsquo;T.',
    g4why='MUST &mdash; his own conviction, from inside. HAVE TO is also '
          'correct English here; MUST is just the more natural choice for a '
          'feeling.',
    g5why='DOESN&rsquo;T HAVE TO &mdash; no obligation, and the top scorer '
          'is &ldquo;he&rdquo;, so DON&rsquo;T becomes DOESN&rsquo;T. '
          'MUSTN&rsquo;T would mean he isn&rsquo;t allowed to play.',
    g6why='HAD TO &mdash; &ldquo;last season&rdquo; is the past, and MUST '
          'has no past form.',

    mcEyebrow='Activity 2 &middot; Choose',
    mcTitle='Choose the best answer',
    mcMean='What does this sentence mean?',
    mc3ctx='The transfer window closes on Friday. Which question is correct?',
    mc4ctx='Why does the coach say MUST here?',
    mc5ctx='Which sentence is correct English?',
    mc1why='MUSTN&rsquo;T = forbidden. &ldquo;Don&rsquo;t need to&rdquo; '
           'would be DON&rsquo;T HAVE TO, and &ldquo;probably '
           'won&rsquo;t&rdquo; is a guess, not a rule.',
    mc2why='DOESN&rsquo;T HAVE TO = not necessary. Nothing forbids him and '
           'nothing forces him &mdash; he may play, or he may not.',
    mc3why='DOES + SUBJECT + HAVE TO + VERB. After DOES, HAVE stays HAVE, '
           'and the verb after HAVE TO takes no -S. MUST never takes DO.',
    mc4why='Here MUST shows the speaker&rsquo;s own feeling &mdash; &ldquo;I'
           ' really believe it&rdquo;. Forbidden would be MUSTN&rsquo;T, '
           'optional would be DON&rsquo;T HAVE TO, and MUST has no past.',
    mc5why='SUBJECT + MUST + VERB. No -S on MUST, no -S on the verb after it, '
           'and no TO.',

    ordEyebrow='Activity 3 &middot; Build it',
    ordTitle='Build the sentence',
    orderHint='Click the pieces in order &middot; click one again to take it back',
    o1hint='Build a sentence that means: &ldquo;It is forbidden for VfB '
           'players to foul inside the box.&rdquo; One piece is left over.',
    o2hint='Build a question that means: &ldquo;Is it necessary for the '
           'captain to take the penalty?&rdquo; One piece is left over.',
    o3hint='Build a sentence that means: &ldquo;It wasn&rsquo;t necessary for '
           'VfB to play extra time.&rdquo; One piece is left over.',
    o1why='Forbidden = MUSTN&rsquo;T + VERB. DON&rsquo;T HAVE TO would mean '
          'fouling is optional.',
    o2why='A question with HAVE TO: DOES + SUBJECT + HAVE TO + VERB. After '
          'DOES, HAVE stays HAVE &mdash; not &ldquo;has to&rdquo;.',
    o3why='Past, and no obligation: DIDN&rsquo;T + HAVE TO + VERB. After '
          'DIDN&rsquo;T the verb goes back to HAVE &mdash; never '
          '&ldquo;didn&rsquo;t had to&rdquo;.',

    fixEyebrow='Activity 4 &middot; Spot the mistake',
    fixTitle='Correct the mistake',
    fixHint='Each sentence has one mistake. Type the correction in the box, '
            'using the right form of MUST or HAVE TO &mdash; change as '
            'little as you can.',
    e1why='SUBJECT + MUST NOT + VERB. No TO after MUST or MUSTN&rsquo;T.',
    e2why='DOES + SUBJECT + HAVE TO + VERB. MUST never takes -S and never '
          'takes DO, so not &ldquo;musts&rdquo; and not &ldquo;must&rdquo; '
          'either. NEED TO also works.',
    e3why='&ldquo;Last month&rdquo; is the past, and MUST has no past form: '
          'HAD TO + VERB. NEEDED TO also works.',
    e4why='Nobody is forcing him, so there is no obligation: DOESN&rsquo;T HAVE '
          'TO. MUSTN&rsquo;T would mean retiring is forbidden.',

    resNext='Now put the four forms to work &rarr;',
    resPerfect='Perfect score &mdash; Grammar Player of the Season. '
               'MUSTN&rsquo;T and DON&rsquo;T HAVE TO hold no secrets for you.',
    resStrong='Strong performance. A few tactical errors &mdash; look again at '
              'MUSTN&rsquo;T and DON&rsquo;T HAVE TO and you&rsquo;ll be '
              'unbeatable.',
    resMid='A solid first half. The second 45 minutes need more work &mdash; '
           'go back over the three tactics slides, then try again.',
    resLow='A tough result today. Even the best players repeat their drills '
           'hundreds of times. Reread the tactics slides and come back '
           'stronger.',

    actTitle='Welcome to the squad',
    actUse='Use at least four:',
    actSpeakKind='Speaking &middot; in pairs',
    actSpeakBrief='One of you is the captain of a football club; the other '
                  'has just signed and has questions. Four minutes, then '
                  'swap.',
    actSpeak1='Captain: tell the new player three things everyone at the '
              'club has to do, and two things they mustn&rsquo;t do.',
    actSpeak2='New player: ask two &ldquo;Do I have to&hellip;?&rdquo; '
              'questions. Captain: answer them, and tell them one thing they'
              ' don&rsquo;t have to do.',
    actSpeak3='Captain: tell them one thing you had to do in your first week'
              ' at the club, and one thing you were glad you didn&rsquo;t '
              'have to do.',
    actWriteKind='Writing &middot; 150&ndash;200 words',
    actWriteBrief='A player from abroad joins your club next week. Write them a '
                  'welcome email about the rules: what they have to do, what '
                  'they mustn&rsquo;t do, and what they don&rsquo;t have to '
                  'worry about. Use HAD TO at least once, for something new '
                  'players had to do last season.',
    actPlaceholder='Welcome to the club! Every player has to…',
)

T['de'] = dict(
    coverTitle='Must &amp; <em>Have To</em>',
    coverSub='Positiv und negativ &mdash; die vier wichtigsten Formen, in den '
             'Farben des VfB',
    chipLevel='B1 &middot; Mittelstufe',
    chipFocus='MUST &middot; HAVE TO &middot; die Verneinungsfalle',
    chipCount='19 Folien',

    taEyebrow='Taktiktafel &middot; 1 / 3',
    taTitle='Zwei Wege zu sagen, dass etwas nötig ist',
    ta1h='MUST &mdash; das eigene Gefühl des Sprechers',
    ta1b='MUST benutzt du, wenn die Verpflichtung von innen kommt: deine eigene '
         'Überzeugung, dein Gefühl oder deine Entscheidung. <em>VfB must win '
         'this derby &mdash; it means everything!</em>',
    ta1n='MUST kann auch &bdquo;ich bin sicher&ldquo; bedeuten: <em>He must '
         'be exhausted after 120 minutes.</em> Das ist eine '
         'Schlussfolgerung, keine Verpflichtung.',
    ta2h='HAVE TO &mdash; eine Regel von außen',
    ta2b='HAVE TO benutzt du, wenn die Verpflichtung von außen kommt: die '
         'Regeln, der Schiedsrichter, der Trainer. <em>VfB players have to '
         'wear red and white at home games.</em>',
    ta2n='In positiven Sätzen geht oft beides: <em>We must press / We have '
         'to press.</em> In der Verneinung trennen sie sich.',

    tbEyebrow='Die Schlüsselregel &middot; 2 / 3',
    tbTitle='MUSTN&rsquo;T ist nicht DON&rsquo;T HAVE TO',
    tb1h='MUSTN&rsquo;T &mdash; verboten',
    tb1b='Es ist nicht erlaubt &mdash; nach den Regeln oder weil der '
         'Sprecher es sagt. <em>Players mustn&rsquo;t leave the pitch '
         'without the referee&rsquo;s permission.</em>',
    tb1n='= nicht dürfen &mdash; NICHT &bdquo;nicht müssen&ldquo;. Wer es '
         'trotzdem tut, sieht Gelb. Geschriebene Regeln nehmen die Langform:'
         ' MUST NOT.',
    tb2h='DON&rsquo;T HAVE TO &mdash; nicht nötig',
    tb2b='Es gibt keine Verpflichtung &mdash; du kannst, wenn du willst. '
         '<em>Players don&rsquo;t have to leave the pitch at half-time.</em>',
    tb2n='= nicht müssen, nicht brauchen zu. Sie können in der Pause auf dem'
         ' Platz bleiben und sich aufwärmen &mdash; keine Karte, ihre '
         'Entscheidung.',

    tcEyebrow='Die Formen &middot; 3 / 3',
    tcTitle='MUST ändert sich nie. HAVE TO schon.',
    tc1h='MUST &mdash; immer dieselbe Form',
    tc1b='SUBJEKT + MUST + VERB. Kein -S, kein TO, kein DO, keine '
         'Vergangenheitsform. <em>The keeper must stay focused.</em> Nicht '
         '&bdquo;musts&ldquo;, &bdquo;must stays&ldquo;, &bdquo;must '
         'to&ldquo; oder &bdquo;does &hellip; must&ldquo;.',
    tc1n='Für die Vergangenheit nimmst du HAD TO &mdash; die Vergangenheit '
         'von beiden: <em>Yesterday VfB had to win.</em> Nicht '
         '&bdquo;Yesterday VfB must win&ldquo;.',
    tc2h='HAVE TO &mdash; ein ganz normales Verb',
    tc2b='HAS TO bei he, she und it. Fragen und Verneinungen bildest du mit '
         'DO / DOES / DID + HAVE TO: <em>Does the keeper have to wear '
         'gloves?</em> <em>The fans didn&rsquo;t have to queue for '
         'tickets.</em>',
    tc2n='Nach DOES und DIDN&rsquo;T bleibt HAVE: nicht &bdquo;does &hellip; '
         'has to&ldquo;, nicht &bdquo;didn&rsquo;t had to&ldquo;.',

    gapEyebrow='Aktivität 1 &middot; Lückentext',
    gapTitle='Vervollständige den Satz',
    gapHint='Nimm eine Form aus der Wortliste. Kurz- und Langform zählen '
            'beide &mdash; &bdquo;mustn&rsquo;t&ldquo; oder &bdquo;must '
            'not&ldquo;.',
    bankLabel='Wortliste:',
    g1why='MUSTN&rsquo;T &mdash; Handspiel ist nach den Regeln verboten, und '
          'der Schiedsrichter bestraft es.',
    g2why='HAS TO &mdash; der Stürmer ist &bdquo;he&ldquo;, also wird HAVE zu '
          'HAS, und die Anweisung kommt vom Trainer. MUST ist auch richtig.',
    g3why='DON&rsquo;T HAVE TO &mdash; &bdquo;if you prefer&ldquo; heißt, dass '
          'sie die Wahl haben. Es ist nicht verboten, also nicht '
          'MUSTN&rsquo;T.',
    g4why='MUST &mdash; seine eigene Überzeugung, von innen. HAVE TO ist hier '
          'auch richtiges Englisch; für ein Gefühl ist MUST nur die '
          'natürlichere Wahl.',
    g5why='DOESN&rsquo;T HAVE TO &mdash; keine Verpflichtung, und der '
          'Torjäger ist &bdquo;he&ldquo;, also wird DON&rsquo;T zu '
          'DOESN&rsquo;T. MUSTN&rsquo;T hieße, dass er nicht spielen darf.',
    g6why='HAD TO &mdash; &bdquo;last season&ldquo; heißt Vergangenheit, und'
          ' MUST hat keine Vergangenheitsform.',

    mcEyebrow='Aktivität 2 &middot; Auswählen',
    mcTitle='Wähle die beste Antwort',
    mcMean='Was bedeutet dieser Satz?',
    mc3ctx='Das Transferfenster schließt am Freitag. Welche Frage ist richtig?',
    mc4ctx='Warum sagt der Trainer hier MUST?',
    mc5ctx='Welcher Satz ist richtiges Englisch?',
    mc1why='MUSTN&rsquo;T = verboten. &bdquo;don&rsquo;t need to&ldquo; '
           '(nicht nötig) wäre DON&rsquo;T HAVE TO, und &bdquo;probably '
           'won&rsquo;t&ldquo; (wahrscheinlich nicht) ist eine Vermutung, '
           'keine Regel.',
    mc2why='DOESN&rsquo;T HAVE TO = nicht nötig. Nichts verbietet es ihm und '
           'nichts zwingt ihn &mdash; vielleicht spielt er, vielleicht nicht.',
    mc3why='DOES + SUBJEKT + HAVE TO + VERB. Nach DOES bleibt HAVE, und das '
           'Verb nach HAVE TO bekommt kein -S. MUST steht nie mit DO.',
    mc4why='Hier zeigt MUST das eigene Gefühl des Sprechers &mdash; &bdquo;I'
           ' really believe it&ldquo;. Verboten wäre MUSTN&rsquo;T, '
           'freiwillig wäre DON&rsquo;T HAVE TO, und MUST hat keine '
           'Vergangenheit.',
    mc5why='SUBJEKT + MUST + VERB. Kein -S an MUST, kein -S am Verb danach '
           'und kein TO.',

    ordEyebrow='Aktivität 3 &middot; Satzbau',
    ordTitle='Bau den Satz',
    orderHint='Klicke die Teile der Reihe nach an &middot; klicke ein Teil '
              'noch einmal an, um es zurückzunehmen',
    o1hint='Bilde einen Satz mit dieser Bedeutung: &bdquo;It is forbidden for '
           'VfB players to foul inside the box.&ldquo; Ein Teil bleibt übrig.',
    o2hint='Bilde eine Frage mit dieser Bedeutung: &bdquo;Is it necessary for '
           'the captain to take the penalty?&ldquo; Ein Teil bleibt übrig.',
    o3hint='Bilde einen Satz mit dieser Bedeutung: &bdquo;It wasn&rsquo;t '
           'necessary for VfB to play extra time.&ldquo; Ein Teil bleibt '
           'übrig.',
    o1why='Verboten = MUSTN&rsquo;T + VERB. DON&rsquo;T HAVE TO hieße, dass '
          'Foulen freiwillig ist.',
    o2why='Eine Frage mit HAVE TO: DOES + SUBJEKT + HAVE TO + VERB. Nach DOES '
          'bleibt HAVE &mdash; nicht &bdquo;has to&ldquo;.',
    o3why='Vergangenheit, keine Verpflichtung: DIDN&rsquo;T + HAVE TO + VERB. '
          'Nach DIDN&rsquo;T steht wieder HAVE &mdash; nie &bdquo;didn&rsquo;t '
          'had to&ldquo;.',

    fixEyebrow='Aktivität 4 &middot; Finde den Fehler',
    fixTitle='Korrigiere den Fehler',
    fixHint='Jeder Satz hat einen Fehler. Tippe die Korrektur in das Feld, '
            'mit der richtigen Form von MUST oder HAVE TO &mdash; ändere so '
            'wenig wie möglich.',
    e1why='SUBJEKT + MUST NOT + VERB. Kein TO nach MUST oder MUSTN&rsquo;T.',
    e2why='DOES + SUBJEKT + HAVE TO + VERB. MUST bekommt nie ein -S und '
          'steht nie mit DO, also weder &bdquo;musts&ldquo; noch '
          '&bdquo;must&ldquo;. NEED TO geht auch.',
    e3why='&bdquo;Last month&ldquo; heißt Vergangenheit, und MUST hat keine '
          'Vergangenheitsform: HAD TO + VERB. NEEDED TO geht auch.',
    e4why='Niemand zwingt ihn, also gibt es keine Verpflichtung: DOESN&rsquo;T '
          'HAVE TO. MUSTN&rsquo;T hieße, dass er nicht aufhören darf.',

    resNext='Jetzt setz die vier Formen ein &rarr;',
    resPerfect='Volle Punktzahl &mdash; Grammatikspieler der Saison. '
               'MUSTN&rsquo;T und DON&rsquo;T HAVE TO haben keine Geheimnisse '
               'mehr für dich.',
    resStrong='Starke Leistung. Ein paar taktische Fehler &mdash; schau dir '
              'MUSTN&rsquo;T und DON&rsquo;T HAVE TO noch einmal an, dann bist '
              'du unschlagbar.',
    resMid='Eine solide erste Halbzeit. In der zweiten ist noch Luft nach '
           'oben &mdash; geh die drei Taktikfolien noch einmal durch und '
           'versuch es dann wieder.',
    resLow='Heute ein hartes Ergebnis. Auch die besten Spieler wiederholen '
           'ihre Übungen hunderte Male. Lies die Taktikfolien noch einmal und '
           'komm stärker zurück.',

    actTitle='Willkommen im Team',
    actUse='Benutze mindestens vier:',
    actSpeakKind='Sprechen &middot; zu zweit',
    actSpeakBrief='Einer von euch ist Kapitän eines Fußballvereins, der '
                  'andere hat gerade unterschrieben und hat Fragen. Vier '
                  'Minuten, dann wechselt ihr.',
    actSpeak1='Kapitän: Nenne dem Neuen drei Dinge, die im Verein alle tun '
              'müssen, und zwei Dinge, die er nicht tun darf.',
    actSpeak2='Neuer Spieler: Stell zwei Fragen mit &bdquo;Do I have '
              'to&hellip;?&ldquo;. Kapitän: Antworte und nenne ihm eine '
              'Sache, die er nicht tun muss.',
    actSpeak3='Kapitän: Erzähl von einer Sache, die du in deiner ersten '
              'Woche im Verein tun musstest, und von einer, die du zum Glück'
              ' nicht tun musstest.',
    actWriteKind='Schreiben &middot; 150&ndash;200 Wörter',
    actWriteBrief='Nächste Woche kommt ein Spieler aus dem Ausland in deinen '
                  'Verein. Schreib ihm eine Willkommens-E-Mail über die Regeln: '
                  'was er tun muss, was er nicht tun darf und worüber er sich '
                  'keine Sorgen machen muss. Benutze mindestens einmal HAD TO, '
                  'für etwas, das neue Spieler letzte Saison tun mussten.',
    actPlaceholder='Welcome to the club! Every player has to…',
)

T['es'] = dict(
    coverTitle='Must &amp; <em>Have To</em>',
    coverSub='En afirmativo y en negativo &mdash; las cuatro formas clave, con '
             'los colores del VfB',
    chipLevel='B1 &middot; Intermedio',
    chipFocus='MUST &middot; HAVE TO &middot; la trampa de la negación',
    chipCount='19 diapositivas',

    taEyebrow='Pizarra táctica &middot; 1 / 3',
    taTitle='Dos formas de decir que algo es necesario',
    ta1h='MUST &mdash; el sentimiento de quien habla',
    ta1b='Usa MUST (deber, tener que) cuando la obligación viene de dentro: tu '
         'propia convicción, sentimiento o decisión. <em>VfB must win this '
         'derby &mdash; it means everything!</em>',
    ta1n='MUST también puede significar &laquo;estoy seguro&raquo;: <em>He '
         'must be exhausted after 120 minutes.</em> Es una deducción, no una'
         ' obligación.',
    ta2h='HAVE TO &mdash; una regla que viene de fuera',
    ta2b='Usa HAVE TO (tener que) cuando la obligación viene de fuera: las '
         'reglas, el árbitro, el entrenador. <em>VfB players have to wear red '
         'and white at home games.</em>',
    ta2n='En afirmativo a menudo valen los dos: <em>We must press / We have '
         'to press.</em> En negativo se separan.',

    tbEyebrow='La regla clave &middot; 2 / 3',
    tbTitle='MUSTN&rsquo;T no es DON&rsquo;T HAVE TO',
    tb1h='MUSTN&rsquo;T &mdash; prohibido',
    tb1b='No está permitido &mdash; por las reglas o porque lo dice quien '
         'habla. <em>Players mustn&rsquo;t leave the pitch without the '
         'referee&rsquo;s permission.</em>',
    tb1n='= no se puede, está prohibido. Si lo haces igualmente: tarjeta '
         'amarilla. Las reglas escritas usan la forma completa: MUST NOT.',
    tb2h='DON&rsquo;T HAVE TO &mdash; no es necesario',
    tb2b='No hay obligación &mdash; puedes hacerlo si quieres. <em>Players '
         'don&rsquo;t have to leave the pitch at half-time.</em>',
    tb2n='= no tener que, no es necesario. Pueden quedarse en el campo '
         'calentando si quieren &mdash; sin tarjeta, es su decisión.',

    tcEyebrow='Las formas &middot; 3 / 3',
    tcTitle='MUST nunca cambia. HAVE TO, sí.',
    tc1h='MUST &mdash; siempre la misma forma',
    tc1b='SUJETO + MUST + VERBO. Sin -S, sin TO, sin DO, sin forma de '
         'pasado. <em>The keeper must stay focused.</em> Ni '
         '&laquo;musts&raquo;, ni &laquo;must stays&raquo;, ni &laquo;must '
         'to&raquo;, ni &laquo;does &hellip; must&raquo;.',
    tc1n='Para el pasado, usa HAD TO &mdash; es el pasado de los dos: '
         '<em>Yesterday VfB had to win.</em> No &laquo;Yesterday VfB must '
         'win&raquo;.',
    tc2h='HAVE TO &mdash; un verbo normal',
    tc2b='HAS TO con he, she e it. Las preguntas y las negaciones usan DO / '
         'DOES / DID + HAVE TO: <em>Does the keeper have to wear '
         'gloves?</em> <em>The fans didn&rsquo;t have to queue for '
         'tickets.</em>',
    tc2n='Después de DOES y DIDN&rsquo;T, HAVE no cambia: ni &laquo;does '
         '&hellip; has to&raquo;, ni &laquo;didn&rsquo;t had to&raquo;.',

    gapEyebrow='Actividad 1 &middot; Rellena el hueco',
    gapTitle='Completa la frase',
    gapHint='Usa una forma del banco de palabras. Valen la contracción y la '
            'forma completa &mdash; &laquo;mustn&rsquo;t&raquo; o '
            '&laquo;must not&raquo;.',
    bankLabel='Banco de palabras:',
    g1why='MUSTN&rsquo;T &mdash; tocar el balón con la mano está prohibido por '
          'las reglas, y el árbitro lo castiga.',
    g2why='HAS TO &mdash; el delantero es &laquo;he&raquo;, así que HAVE pasa a '
          'HAS, y la orden viene del entrenador. MUST también es correcto.',
    g3why='DON&rsquo;T HAVE TO &mdash; &laquo;if you prefer&raquo; significa '
          'que pueden elegir. No está prohibido, así que no es MUSTN&rsquo;T.',
    g4why='MUST &mdash; es su propia convicción, desde dentro. HAVE TO también '
          'es inglés correcto aquí; para un sentimiento, MUST es simplemente '
          'lo más natural.',
    g5why='DOESN&rsquo;T HAVE TO &mdash; no hay obligación, y el máximo '
          'goleador es &laquo;he&raquo;, así que DON&rsquo;T pasa a '
          'DOESN&rsquo;T. MUSTN&rsquo;T significaría que no le dejan jugar.',
    g6why='HAD TO &mdash; &laquo;last season&raquo; indica pasado, y MUST no'
          ' tiene forma de pasado.',

    mcEyebrow='Actividad 2 &middot; Elige',
    mcTitle='Elige la mejor respuesta',
    mcMean='¿Qué significa esta frase?',
    mc3ctx='El mercado de fichajes cierra el viernes. ¿Qué pregunta es '
           'correcta?',
    mc4ctx='¿Por qué dice MUST aquí el entrenador?',
    mc5ctx='¿Qué frase es inglés correcto?',
    mc1why='MUSTN&rsquo;T = prohibido. &laquo;don&rsquo;t need to&raquo; (no'
           ' hace falta) sería DON&rsquo;T HAVE TO, y &laquo;probably '
           'won&rsquo;t&raquo; (probablemente no) es una suposición, no una '
           'regla.',
    mc2why='DOESN&rsquo;T HAVE TO = no es necesario. Nada se lo prohíbe y nada '
           'le obliga &mdash; puede que juegue o puede que no.',
    mc3why='DOES + SUJETO + HAVE TO + VERBO. Después de DOES, HAVE no '
           'cambia, y el verbo después de HAVE TO no lleva -S. MUST nunca va'
           ' con DO.',
    mc4why='Aquí MUST muestra el propio sentimiento de quien habla &mdash; '
           '&laquo;I really believe it&raquo;. Prohibido sería '
           'MUSTN&rsquo;T, opcional sería DON&rsquo;T HAVE TO, y MUST no '
           'tiene pasado.',
    mc5why='SUJETO + MUST + VERBO. Sin -S en MUST, sin -S en el verbo que va'
           ' detrás y sin TO.',

    ordEyebrow='Actividad 3 &middot; Construye',
    ordTitle='Construye la frase',
    orderHint='Haz clic en las piezas en orden &middot; vuelve a hacer clic '
              'en una para quitarla',
    o1hint='Construye una frase que signifique: &laquo;It is forbidden for VfB '
           'players to foul inside the box.&raquo; Sobra una pieza.',
    o2hint='Construye una pregunta que signifique: &laquo;Is it necessary for '
           'the captain to take the penalty?&raquo; Sobra una pieza.',
    o3hint='Construye una frase que signifique: &laquo;It wasn&rsquo;t '
           'necessary for VfB to play extra time.&raquo; Sobra una pieza.',
    o1why='Prohibido = MUSTN&rsquo;T + VERBO. DON&rsquo;T HAVE TO significaría '
          'que cometer faltas es opcional.',
    o2why='Una pregunta con HAVE TO: DOES + SUJETO + HAVE TO + VERBO. Después '
          'de DOES, HAVE no cambia &mdash; no &laquo;has to&raquo;.',
    o3why='Pasado y sin obligación: DIDN&rsquo;T + HAVE TO + VERBO. Después de '
          'DIDN&rsquo;T el verbo vuelve a HAVE &mdash; nunca '
          '&laquo;didn&rsquo;t had to&raquo;.',

    fixEyebrow='Actividad 4 &middot; Encuentra el error',
    fixTitle='Corrige el error',
    fixHint='Cada frase tiene un error. Escribe la corrección en el hueco, '
            'con la forma correcta de MUST o HAVE TO &mdash; cambia lo menos'
            ' posible.',
    e1why='SUJETO + MUST NOT + VERBO. Sin TO después de MUST o MUSTN&rsquo;T.',
    e2why='DOES + SUJETO + HAVE TO + VERBO. MUST nunca lleva -S ni va con '
          'DO, así que ni &laquo;musts&raquo; ni &laquo;must&raquo;. NEED TO'
          ' también vale.',
    e3why='&laquo;Last month&raquo; indica pasado, y MUST no tiene forma de '
          'pasado: HAD TO + VERBO. NEEDED TO también vale.',
    e4why='Nadie le obliga, así que no hay obligación: DOESN&rsquo;T HAVE TO. '
          'MUSTN&rsquo;T significaría que retirarse está prohibido.',

    resNext='Ahora pon en práctica las cuatro formas &rarr;',
    resPerfect='Puntuación perfecta &mdash; mejor jugador de gramática de la'
               ' temporada. MUSTN&rsquo;T y DON&rsquo;T HAVE TO ya no tienen'
               ' secretos para ti.',
    resStrong='Gran partido. Algunos errores tácticos &mdash; repasa '
              'MUSTN&rsquo;T y DON&rsquo;T HAVE TO y serás imbatible.',
    resMid='Una primera parte sólida. La segunda necesita más trabajo &mdash; '
           'repasa las tres diapositivas tácticas y vuelve a intentarlo.',
    resLow='Hoy, un resultado duro. Hasta los mejores jugadores repiten sus '
           'ejercicios cientos de veces. Vuelve a leer las diapositivas '
           'tácticas y vuelve más fuerte.',

    actTitle='Bienvenido al equipo',
    actUse='Usa al menos cuatro:',
    actSpeakKind='Conversación &middot; en parejas',
    actSpeakBrief='Uno de vosotros es el capitán de un club de fútbol; el '
                  'otro acaba de fichar y tiene preguntas. Cuatro minutos y '
                  'luego cambiad.',
    actSpeak1='Capitán: dile al nuevo tres cosas que todo el mundo en el '
              'club tiene que hacer y dos cosas que no debe hacer.',
    actSpeak2='Jugador nuevo: haz dos preguntas con &laquo;Do I have '
              'to&hellip;?&raquo;. Capitán: respóndelas y dile una cosa que '
              'no tiene que hacer.',
    actSpeak3='Capitán: cuéntale una cosa que tuviste que hacer en tu '
              'primera semana en el club y otra que, por suerte, no tuviste '
              'que hacer.',
    actWriteKind='Escritura &middot; 150&ndash;200 palabras',
    actWriteBrief='La semana que viene llega a tu club un jugador del '
                  'extranjero. Escríbele un correo de bienvenida sobre las '
                  'normas: qué tiene que hacer, qué no debe hacer y de qué no '
                  'tiene que preocuparse. Usa HAD TO al menos una vez, para '
                  'algo que los jugadores nuevos tuvieron que hacer la '
                  'temporada pasada.',
    actPlaceholder='Welcome to the club! Every player has to…',
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
