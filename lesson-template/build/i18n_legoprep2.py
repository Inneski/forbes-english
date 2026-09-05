# -*- coding: utf-8 -*-
"""Interface strings for LEGO Prepositions & Phrasal Verbs — Part 2 (B2).

English, German and Spanish. Teach-card bodies use the six-item form. The
English being taught — question stems, options, gap sentences and the
True/False labels — stays English throughout.
"""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
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

T['en'] = dict(
    coverTitle='LEGO Prepositions &amp; Phrasal Verbs <em>Part 2</em>',
    coverSub='Fixed prepositions, idiomatic particles, and the lookalikes that trip B2 learners up',
    chipLevel='B2 · Upper-intermediate', chipFocus='Prepositions &amp; phrasal verbs',
    chipCount='27 questions',
    bankLabel='Word bank:',

    t1Eyebrow='Before you start', t1Title='One particle, more than one meaning',
    t1ah='The same particle, two different jobs', t1ab=
        'A LEGO set can <strong>sell out</strong> (no stock left) or be <strong>sold '
        'off</strong> (sold cheap to clear it) &mdash; one letter of difference, '
        'unrelated meanings.',
    t1an='Never assume a phrasal verb means what its parts suggest.',
    t1bh='Idiomatic, not physical', t1bb=
        '<strong>Get round to</strong> something has nothing to do with going around '
        'anything &mdash; it means finally finding the time. The literal image is '
        'gone; only the idiom is left.',
    t1bn='This is why phrasal verbs are learned as whole units, not built from their pieces.',
    t1ch='One verb, two senses', t1cb=
        '<strong>Make out</strong> can mean to understand ("make out why") or to '
        'discern a shape at a distance. Context decides which.',
    t1cn='A dictionary entry with three numbered senses is normal for a phrasal verb '
         '&mdash; a single English verb rarely has that many.',

    t2Eyebrow='Before you start', t2Title='Some prepositions are simply fixed',
    t2ah='No other choice', t2ab=
        'You <strong>look forward to</strong> something &mdash; never <em>forward '
        'for</em>, never <em>forward about</em>. The preposition is part of the '
        'phrase, not a free slot.',
    t2an='If a fixed phrase feels swappable, that feeling is wrong.',
    t2bh='Location prepositions are precise', t2bb=
        'Something sits <strong>at the bottom</strong> of a box, not <em>in the '
        'bottom</em>. <em>At</em> marks a specific point; <em>in</em> suggests a '
        'contained area &mdash; the wrong one still sounds like English, which is '
        'what makes it easy to miss.',
    t2bn='The same applies to <em>the impact of</em> something &mdash; never <em>impact in</em>.',
    t2ch='A line, not a scatter', t2cb=
        '<strong>Alongside</strong> a street means following its length, in a '
        'continuous row. <strong>In between</strong> means alternating positions. '
        'They describe different shapes, not the same idea twice.',
    t2cn='Picture the arrangement before choosing the preposition.',

    t3Eyebrow='Before you start', t3Title='Lookalikes that are not the same word',
    t3ah='<em>Apart from</em> vs <em>take apart</em>', t3ab=
        '<strong>Take apart</strong> is the phrasal verb: you take a model apart to '
        'sort the pieces. <strong>Apart from</strong> is a preposition meaning '
        '"except for". Neither can stand in for the other.',
    t3an='If you can replace it with "except for" and the sentence still works, it '
         'is the preposition, not the phrasal verb.',
    t3bh='A particle that does not exist', t3bb=
        '<strong>Sort out</strong> means to organise something. There is no '
        '<em>sort away</em>, no <em>sort off</em> &mdash; swapping the particle does '
        'not give you a rarer synonym, it gives you an error.',
    t3bn='When in doubt, the particle that exists is usually the only one that does.',
    t3ch='A verb that needs someone doing it', t3cb=
        '<strong>Run out of</strong> needs an active subject: "the store <strong>ran '
        'out of</strong> stock" &mdash; not "the stock <em>was run out of</em>". '
        'Passive grammar and a phrasal verb do not always combine.',
    t3cn='Say who is doing the running out.',

    mcEyebrow='Activity 1 · Multiple choice', mcTitle='Choose the preposition or phrasal verb',
    q1why='<strong>Off.</strong> "Fall off" means to drop from a surface &mdash; the '
          'gears were on the table and fell from it. "Down from" is possible but far '
          'less natural here.',
    q2why='<strong>Through.</strong> The pin passes through the beam, from one side '
          'to the other &mdash; a very common spatial preposition in technical '
          'instructions.',
    q3why='<strong>Out.</strong> "Sell out" means all stock is gone. "Sell off" '
          'means to dispose of at a reduced price &mdash; a different meaning '
          'entirely.',
    q4why='<strong>Got round to.</strong> It means to finally find time for '
          'something you have been postponing. The others involve travel, arrival '
          'and illness.',
    q5why='<strong>Alongside.</strong> It means beside or next to something, '
          'following its line or length &mdash; right for a parade down a street. '
          '"In between" would suggest alternating positions, not a continuous line.',
    q6why='<strong>Make out.</strong> Here it means to understand or discern '
          'something. The others mean tolerate, investigate and escape '
          'consequences.',

    fEyebrow='Activity 2 · Fill in the blank', fTitle='Complete each sentence from the word bank',
    fHint='Use each expression from the bank once at most.',
    f1why='<strong>Broke down.</strong> It means to stop working or functioning '
          '&mdash; used for machines, vehicles and systems.',
    f2why='<strong>Owing to.</strong> A formal phrase meaning because of or due to, '
          'introducing the reason for a situation.',
    f3why='<strong>In addition to.</strong> It means besides or as well as &mdash; '
          'adding extra information to what has already been stated.',
    f4why='<strong>Catch up on.</strong> It means to do something you missed or '
          'fell behind on &mdash; very common with tasks, news and work.',
    f5why='<strong>Stumbled upon.</strong> It means to find something by accident, '
          'without looking for it &mdash; a pleasant or surprising discovery.',

    tfEyebrow='Activity 3 · True or false', tfTitle='Is the underlined phrase used correctly?',
    t1why='<strong>True.</strong> "On top of" correctly describes one brick resting '
          'directly above another &mdash; the standard preposition for stacked '
          'bricks.',
    t2why='<strong>False.</strong> The phrasal verb is "take apart" (no "from"). '
          '"Apart from" is a preposition meaning "except for" &mdash; a completely '
          'different meaning.',
    t3why='<strong>False.</strong> "Run out of" needs a subject &mdash; "The store '
          'had run out of the minifigure." As written, the passive structure is '
          'broken.',
    t4why='<strong>True.</strong> "On time" correctly means at the scheduled or '
          'planned moment.',
    t5why='<strong>True.</strong> "Look up" means to search for information. With '
          'a noun object the particle can come before or after: "look up the '
          'piece" or "look the piece up" are both correct.',
    t6why='<strong>True.</strong> "Come along with" means to be included with or '
          'to accompany something.',

    matchEyebrow='Activity 4 · Building &amp; progress', matchTitle='Match the phrasal verb to its definition',
    matchHint='Click a phrase, then click what it means.',
    matchWhy='All five describe stages of making or building something. '
             '<em>Build up to</em> and <em>branch out into</em> both look forward; '
             '<em>fall apart</em> is the failure they are working against. '
             '<em>Piece together</em> and <em>go through with</em> are what '
             'finishing looks like &mdash; assembling the parts, and not giving up '
             'partway through.',

    ecEyebrow='Activity 5 · Error correction', ecTitle='Find the correct replacement',
    e1why='<strong>Up with.</strong> "Come up with" means to think of an idea. The '
          'particle order matters &mdash; it cannot simply be reversed.',
    e2why='<strong>Forward to.</strong> "Look forward to" is the fixed phrase '
          '&mdash; "to" is always the preposition in this idiom. "Look forward '
          'for" does not exist.',
    e3why='<strong>At the bottom.</strong> The correct phrase for a specific '
          'location. "In the bottom" is non-standard; we use "at" for a specific '
          'point within a larger area.',
    e4why='<strong>Sort out.</strong> It means to organise or deal with something '
          'effectively. "Sort away", "sort off" and "sort aside" are not standard '
          'phrasal verbs.',
    e5why='<strong>Impact of.</strong> The correct collocation &mdash; "the impact '
          'of [something]" describes consequences. "Impact in" is not standard.',

    actTitle='Explain the build', actUse='Use at least three:',
    actSpeakBrief='One of you is the LEGO instructor, one is a new builder who '
                  'keeps making mistakes. Four minutes each, then swap.',
    actSpeak1='Explain a mistake a beginner always makes, and say what they should do instead.',
    actSpeak2='Describe a set that <em>sold out</em> immediately, and one you are <em>looking forward to</em>.',
    actSpeak3='Tell your partner to <em>sort out</em> their pieces before they <em>take</em> anything <em>apart</em>.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Write a short guide for a new LEGO club member: what they must '
                  'do before starting a build, one mistake they should avoid, and '
                  'what to do if a piece is missing. Use at least three of the '
                  'expressions above.',
    actPlaceholder='Before you start, make sure you…',

    resPerfect='Full marks. Fixed prepositions and phrasal verbs, all landed.',
    resStrong='Strong. Look back at the true/false slides — that is usually where the last point goes.',
    resMid='Good base. Revisit the three opening slides: the preposition is fixed, not logical.',
    resLow='Read the three teaching slides again, then try the multiple choice once more.',
)

T['de'] = dict(
    coverTitle='LEGO-Präpositionen &amp; Phrasal Verbs <em>Teil 2</em>',
    coverSub='Feste Präpositionen, idiomatische Partikel und die Doppelgänger, die B2-Lernende stolpern lassen',
    chipLevel='B2 · Obere Mittelstufe', chipFocus='Präpositionen &amp; Phrasal Verbs',
    chipCount='27 Fragen',
    bankLabel='Wortspeicher:',

    t1Eyebrow='Bevor es losgeht', t1Title='Ein Partikel, mehr als eine Bedeutung',
    t1ah='Derselbe Partikel, zwei verschiedene Jobs', t1ab=
        'Ein LEGO-Set kann <strong>sell out</strong> (kein Bestand mehr) oder '
        '<strong>sold off</strong> (billig abverkauft) sein &mdash; ein Buchstabe '
        'Unterschied, völlig andere Bedeutung.',
    t1an='Nimm nie an, dass ein Phrasal Verb das bedeutet, was seine Teile nahelegen.',
    t1bh='Idiomatisch, nicht wörtlich', t1bb=
        '<strong>Get round to</strong> etwas hat nichts mit Herumgehen zu tun '
        '&mdash; es heißt, endlich Zeit dafür zu finden. Das wörtliche Bild ist '
        'weg; nur die Redewendung bleibt.',
    t1bn='Deshalb lernt man Phrasal Verbs als Ganzes, nicht aus ihren Teilen zusammengesetzt.',
    t1ch='Ein Verb, zwei Bedeutungen', t1cb=
        '<strong>Make out</strong> kann heißen, etwas zu verstehen ("make out '
        'why"), oder eine Form aus der Ferne zu erkennen. Der Kontext entscheidet.',
    t1cn='Ein Wörterbucheintrag mit drei nummerierten Bedeutungen ist bei einem '
         'Phrasal Verb normal &mdash; ein einzelnes englisches Verb hat das selten.',

    t2Eyebrow='Bevor es losgeht', t2Title='Manche Präpositionen sind einfach fest',
    t2ah='Keine andere Wahl', t2ab=
        'Man <strong>look forward to</strong> etwas &mdash; nie <em>forward '
        'for</em>, nie <em>forward about</em>. Die Präposition gehört zur Wendung, '
        'ist keine freie Lücke.',
    t2an='Fühlt sich eine feste Wendung austauschbar an, täuscht das Gefühl.',
    t2bh='Ortspräpositionen sind präzise', t2bb=
        'Etwas liegt <strong>at the bottom</strong> einer Kiste, nicht <em>in the '
        'bottom</em>. <em>At</em> markiert einen bestimmten Punkt, <em>in</em> '
        'legt einen umschlossenen Bereich nahe &mdash; die falsche Variante klingt '
        'trotzdem nach Englisch, darum übersieht man sie leicht.',
    t2bn='Dasselbe gilt für <em>the impact of</em> etwas &mdash; nie <em>impact in</em>.',
    t2ch='Eine Linie, keine Streuung', t2cb=
        '<strong>Alongside</strong> einer Straße folgt ihrer Länge, in einer '
        'durchgehenden Reihe. <strong>In between</strong> heißt abwechselnde '
        'Positionen. Sie beschreiben unterschiedliche Formen, nicht dieselbe Idee '
        'zweimal.',
    t2cn='Stell dir die Anordnung vor, bevor du die Präposition wählst.',

    t3Eyebrow='Bevor es losgeht', t3Title='Doppelgänger, die nicht dasselbe Wort sind',
    t3ah='<em>Apart from</em> vs. <em>take apart</em>', t3ab=
        '<strong>Take apart</strong> ist das Phrasal Verb: Man nimmt ein Modell '
        'auseinander, um die Teile zu sortieren. <strong>Apart from</strong> ist '
        'eine Präposition und heißt „außer“. Keins kann für das andere einspringen.',
    t3an='Kannst du es durch „außer“ ersetzen und der Satz funktioniert noch, ist '
         'es die Präposition, nicht das Phrasal Verb.',
    t3bh='Ein Partikel, den es nicht gibt', t3bb=
        '<strong>Sort out</strong> heißt, etwas zu ordnen. Es gibt kein <em>sort '
        'away</em>, kein <em>sort off</em> &mdash; einen anderen Partikel '
        'einzusetzen ergibt kein selteneres Synonym, sondern einen Fehler.',
    t3bn='Im Zweifel ist der existierende Partikel meist der einzig richtige.',
    t3ch='Ein Verb, das ein handelndes Subjekt braucht', t3cb=
        '<strong>Run out of</strong> braucht ein aktives Subjekt: „the store '
        '<strong>ran out of</strong> stock“ &mdash; nicht „the stock <em>was run '
        'out of</em>“. Passiv und Phrasal Verb passen nicht immer zusammen.',
    t3cn='Sag, wer das Ausgehen verursacht.',

    mcEyebrow='Aufgabe 1 · Multiple Choice', mcTitle='Wähle die Präposition oder das Phrasal Verb',
    q1why='<strong>Off.</strong> „Fall off“ heißt, von einer Fläche herunterzufallen '
          '&mdash; die Zahnräder lagen auf dem Tisch und fielen davon herunter. '
          '„Down from“ ist möglich, aber hier weit weniger natürlich.',
    q2why='<strong>Through.</strong> Der Stift geht durch den Balken, von einer '
          'Seite zur anderen &mdash; eine sehr gängige Ortspräposition in '
          'technischen Anleitungen.',
    q3why='<strong>Out.</strong> „Sell out“ heißt, der ganze Bestand ist weg. '
          '„Sell off“ heißt, zu einem reduzierten Preis loszuwerden &mdash; eine '
          'ganz andere Bedeutung.',
    q4why='<strong>Got round to.</strong> Es heißt, endlich Zeit für etwas zu '
          'finden, das man aufgeschoben hatte. Die anderen betreffen Reise, '
          'Ankunft und Krankheit.',
    q5why='<strong>Alongside.</strong> Es heißt neben oder entlang von etwas, '
          'seiner Linie folgend &mdash; passend für eine Parade eine Straße '
          'entlang. „In between“ würde abwechselnde Positionen nahelegen, keine '
          'durchgehende Linie.',
    q6why='<strong>Make out.</strong> Hier heißt es, etwas zu verstehen oder zu '
          'erkennen. Die anderen bedeuten ertragen, untersuchen und '
          'Konsequenzen entgehen.',

    fEyebrow='Aufgabe 2 · Lückentext', fTitle='Vervollständige jeden Satz mit dem Wortspeicher',
    fHint='Benutze jeden Ausdruck aus dem Speicher höchstens einmal.',
    f1why='<strong>Broke down.</strong> Es heißt, aufzuhören zu funktionieren '
          '&mdash; bei Maschinen, Fahrzeugen und Systemen.',
    f2why='<strong>Owing to.</strong> Eine formelle Wendung für „wegen“ oder '
          '„aufgrund von“, die den Grund für eine Situation einleitet.',
    f3why='<strong>In addition to.</strong> Es heißt „zusätzlich zu“ oder „außerdem“ '
          '&mdash; es ergänzt, was schon gesagt wurde.',
    f4why='<strong>Catch up on.</strong> Es heißt, etwas nachzuholen, das man '
          'verpasst hat &mdash; sehr gängig bei Aufgaben, Nachrichten und Arbeit.',
    f5why='<strong>Stumbled upon.</strong> Es heißt, etwas zufällig zu finden, '
          'ohne danach zu suchen &mdash; eine erfreuliche oder überraschende '
          'Entdeckung.',

    tfEyebrow='Aufgabe 3 · Wahr oder falsch', tfTitle='Ist die unterstrichene Wendung korrekt verwendet?',
    t1why='<strong>Wahr.</strong> „On top of“ beschreibt korrekt, dass ein Stein '
          'direkt auf einem anderen liegt &mdash; die Standardpräposition für '
          'gestapelte Steine.',
    t2why='<strong>Falsch.</strong> Das Phrasal Verb ist „take apart“ (ohne '
          '„from“). „Apart from“ ist eine Präposition und heißt „außer“ &mdash; '
          'eine völlig andere Bedeutung.',
    t3why='<strong>Falsch.</strong> „Run out of“ braucht ein Subjekt &mdash; „The '
          'store had run out of the minifigure.“ So wie geschrieben ist die '
          'Passivkonstruktion fehlerhaft.',
    t4why='<strong>Wahr.</strong> „On time“ heißt korrekt: zum geplanten Zeitpunkt.',
    t5why='<strong>Wahr.</strong> „Look up“ heißt, nach einer Information zu '
          'suchen. Mit einem Nomen kann der Partikel davor oder danach stehen: '
          '„look up the piece“ oder „look the piece up“ sind beide richtig.',
    t6why='<strong>Wahr.</strong> „Come along with“ heißt, bei etwas dabei zu '
          'sein oder es zu begleiten.',

    matchEyebrow='Aufgabe 4 · Bauen &amp; Fortschritt', matchTitle='Ordne dem Phrasal Verb seine Definition zu',
    matchHint='Klicke eine Wendung an, dann ihre Bedeutung.',
    matchWhy='Alle fünf beschreiben Phasen des Bauens oder Herstellens. <em>Build '
             'up to</em> und <em>branch out into</em> blicken beide nach vorn; '
             '<em>fall apart</em> ist das Scheitern, gegen das sie ankämpfen. '
             '<em>Piece together</em> und <em>go through with</em> zeigen, wie '
             'Fertigwerden aussieht &mdash; die Teile zusammensetzen und nicht '
             'auf halbem Weg aufgeben.',

    ecEyebrow='Aufgabe 5 · Fehlerkorrektur', ecTitle='Finde den richtigen Ersatz',
    e1why='<strong>Up with.</strong> „Come up with“ heißt, sich eine Idee '
          'auszudenken. Die Reihenfolge der Partikel zählt &mdash; sie kann '
          'nicht einfach umgedreht werden.',
    e2why='<strong>Forward to.</strong> „Look forward to“ ist die feste Wendung '
          '&mdash; „to“ ist bei diesem Idiom immer die Präposition. „Look '
          'forward for“ gibt es nicht.',
    e3why='<strong>At the bottom.</strong> Die richtige Wendung für einen '
          'bestimmten Ort. „In the bottom“ ist unüblich; für einen bestimmten '
          'Punkt in einem größeren Bereich nutzt man „at“.',
    e4why='<strong>Sort out.</strong> Es heißt, etwas zu ordnen oder zu erledigen. '
          '„Sort away“, „sort off“ und „sort aside“ sind keine gängigen Phrasal '
          'Verbs.',
    e5why='<strong>Impact of.</strong> Die richtige Kollokation &mdash; „the '
          'impact of [etwas]“ beschreibt Folgen. „Impact in“ ist nicht üblich.',

    actTitle='Erkläre den Bau', actUse='Benutze mindestens drei:',
    actSpeakBrief='Einer von euch ist der LEGO-Lehrer, der andere ein Anfänger, '
                  'der ständig Fehler macht. Je vier Minuten, dann tauschen.',
    actSpeak1='Erkläre einen Fehler, den Anfänger immer machen, und sag, was sie stattdessen tun sollten.',
    actSpeak2='Beschreibe ein Set, das sofort <em>sold out</em> war, und eines, auf das du dich <em>freust</em>.',
    actSpeak3='Sag deinem Partner, er soll seine Teile <em>sortieren</em>, bevor er etwas <em>auseinandernimmt</em>.',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Schreibe eine kurze Anleitung für ein neues Mitglied im '
                  'LEGO-Club: was es vor dem Bauen tun muss, einen Fehler, den es '
                  'vermeiden sollte, und was zu tun ist, wenn ein Teil fehlt. '
                  'Benutze mindestens drei der obigen Ausdrücke.',
    actPlaceholder='Before you start, make sure you…',

    resPerfect='Volle Punktzahl. Feste Präpositionen und Phrasal Verbs, alle sitzen.',
    resStrong='Stark. Sieh dir die Wahr/Falsch-Folien noch einmal an — dort geht meist der letzte Punkt verloren.',
    resMid='Gute Grundlage. Schau dir die drei Einstiegsfolien noch einmal an: die Präposition ist fest, nicht logisch.',
    resLow='Lies die drei Lehrfolien noch einmal und versuch dann das Multiple Choice erneut.',
)

T['es'] = dict(
    coverTitle='Preposiciones y Phrasal Verbs de LEGO <em>Parte 2</em>',
    coverSub='Preposiciones fijas, partículas idiomáticas y los parecidos que confunden a los alumnos de B2',
    chipLevel='B2 · Intermedio alto', chipFocus='Preposiciones y phrasal verbs',
    chipCount='27 preguntas',
    bankLabel='Banco de palabras:',

    t1Eyebrow='Antes de empezar', t1Title='Una partícula, más de un significado',
    t1ah='La misma partícula, dos trabajos distintos', t1ab=
        'Un set de LEGO puede <strong>sell out</strong> (no queda existencia) o '
        'estar <strong>sold off</strong> (vendido barato para liquidarlo) &mdash; '
        'una letra de diferencia, significados sin relación.',
    t1an='Nunca supongas que un phrasal verb significa lo que sugieren sus partes.',
    t1bh='Idiomático, no físico', t1bb=
        '<strong>Get round to</strong> algo no tiene nada que ver con rodear nada '
        '&mdash; significa encontrar por fin el tiempo. La imagen literal '
        'desaparece; solo queda el idiom.',
    t1bn='Por eso los phrasal verbs se aprenden como unidades completas, no '
         'construidos a partir de sus piezas.',
    t1ch='Un verbo, dos sentidos', t1cb=
        '<strong>Make out</strong> puede significar entender ("make out why") o '
        'distinguir una forma a distancia. El contexto decide cuál.',
    t1cn='Una entrada de diccionario con tres sentidos numerados es normal en un '
         'phrasal verb &mdash; un solo verbo en español rara vez tiene tantos.',

    t2Eyebrow='Antes de empezar', t2Title='Algunas preposiciones son simplemente fijas',
    t2ah='No hay otra opción', t2ab=
        'Uno <strong>look forward to</strong> algo &mdash; nunca <em>forward '
        'for</em>, nunca <em>forward about</em>. La preposición forma parte de '
        'la frase, no es un hueco libre.',
    t2an='Si una frase fija parece intercambiable, esa sensación está equivocada.',
    t2bh='Las preposiciones de lugar son precisas', t2bb=
        'Algo está <strong>at the bottom</strong> de una caja, no <em>in the '
        'bottom</em>. <em>At</em> marca un punto concreto; <em>in</em> sugiere un '
        'área contenida &mdash; la incorrecta sigue sonando a inglés, por eso es '
        'fácil pasarla por alto.',
    t2bn='Lo mismo se aplica a <em>the impact of</em> algo &mdash; nunca <em>impact in</em>.',
    t2ch='Una línea, no una dispersión', t2cb=
        '<strong>Alongside</strong> una calle significa seguir su longitud, en '
        'una fila continua. <strong>In between</strong> significa posiciones '
        'alternas. Describen formas distintas, no la misma idea dos veces.',
    t2cn='Imagina la disposición antes de elegir la preposición.',

    t3Eyebrow='Antes de empezar', t3Title='Parecidos que no son la misma palabra',
    t3ah='<em>Apart from</em> frente a <em>take apart</em>', t3ab=
        '<strong>Take apart</strong> es el phrasal verb: desmontas un modelo '
        'para clasificar las piezas. <strong>Apart from</strong> es una '
        'preposición que significa "excepto". Ninguna puede sustituir a la otra.',
    t3an='Si puedes cambiarlo por "excepto" y la frase sigue funcionando, es la '
         'preposición, no el phrasal verb.',
    t3bh='Una partícula que no existe', t3bb=
        '<strong>Sort out</strong> significa organizar algo. No existe <em>sort '
        'away</em>, ni <em>sort off</em> &mdash; cambiar la partícula no da un '
        'sinónimo más raro, da un error.',
    t3bn='En caso de duda, la partícula que existe suele ser la única correcta.',
    t3ch='Un verbo que necesita a alguien haciéndolo', t3cb=
        '<strong>Run out of</strong> necesita un sujeto activo: "the store '
        '<strong>ran out of</strong> stock" &mdash; no "the stock <em>was run '
        'out of</em>". La gramática pasiva y un phrasal verb no siempre '
        'combinan.',
    t3cn='Di quién se está quedando sin existencias.',

    mcEyebrow='Actividad 1 · Opción múltiple', mcTitle='Elige la preposición o el phrasal verb',
    q1why='<strong>Off.</strong> "Fall off" significa caerse de una superficie '
          '&mdash; los engranajes estaban sobre la mesa y cayeron de ella. "Down '
          'from" es posible, pero aquí mucho menos natural.',
    q2why='<strong>Through.</strong> El pasador atraviesa la viga, de un lado al '
          'otro &mdash; una preposición espacial muy común en instrucciones '
          'técnicas.',
    q3why='<strong>Out.</strong> "Sell out" significa que no queda existencia. '
          '"Sell off" significa deshacerse de algo a precio reducido &mdash; un '
          'significado totalmente distinto.',
    q4why='<strong>Got round to.</strong> Significa encontrar por fin tiempo '
          'para algo que se venía posponiendo. Las demás implican viaje, '
          'llegada y enfermedad.',
    q5why='<strong>Alongside.</strong> Significa al lado de algo, siguiendo su '
          'línea o longitud &mdash; adecuado para un desfile a lo largo de una '
          'calle. "In between" sugeriría posiciones alternas, no una línea '
          'continua.',
    q6why='<strong>Make out.</strong> Aquí significa entender o distinguir algo. '
          'Las demás significan tolerar, investigar y escapar de las '
          'consecuencias.',

    fEyebrow='Actividad 2 · Completa el hueco', fTitle='Completa cada frase con el banco de palabras',
    fHint='Usa cada expresión del banco como máximo una vez.',
    f1why='<strong>Broke down.</strong> Significa dejar de funcionar &mdash; se '
          'usa con máquinas, vehículos y sistemas.',
    f2why='<strong>Owing to.</strong> Una frase formal que significa "debido a", '
          'e introduce la razón de una situación.',
    f3why='<strong>In addition to.</strong> Significa "además de" &mdash; añade '
          'información extra a lo que ya se ha dicho.',
    f4why='<strong>Catch up on.</strong> Significa ponerse al día con algo que '
          'se había dejado atrás &mdash; muy común con tareas, noticias y '
          'trabajo.',
    f5why='<strong>Stumbled upon.</strong> Significa encontrar algo por '
          'casualidad, sin buscarlo &mdash; un descubrimiento agradable o '
          'sorprendente.',

    tfEyebrow='Actividad 3 · Verdadero o falso', tfTitle='¿Está bien usada la expresión subrayada?',
    t1why='<strong>Verdadero.</strong> "On top of" describe correctamente que '
          'una pieza descansa justo encima de otra &mdash; la preposición '
          'estándar para piezas apiladas.',
    t2why='<strong>Falso.</strong> El phrasal verb es "take apart" (sin '
          '"from"). "Apart from" es una preposición que significa "excepto" '
          '&mdash; un significado totalmente distinto.',
    t3why='<strong>Falso.</strong> "Run out of" necesita un sujeto &mdash; "The '
          'store had run out of the minifigure." Tal como está escrito, la '
          'estructura pasiva está mal formada.',
    t4why='<strong>Verdadero.</strong> "On time" significa correctamente: en el '
          'momento previsto.',
    t5why='<strong>Verdadero.</strong> "Look up" significa buscar información. '
          'Con un objeto nominal, la partícula puede ir antes o después: "look '
          'up the piece" o "look the piece up" son ambas correctas.',
    t6why='<strong>Verdadero.</strong> "Come along with" significa venir '
          'incluido con algo o acompañarlo.',

    matchEyebrow='Actividad 4 · Construir y progresar', matchTitle='Relaciona el phrasal verb con su definición',
    matchHint='Haz clic en una expresión y luego en su significado.',
    matchWhy='Las cinco describen etapas de construir o fabricar algo. <em>Build '
             'up to</em> y <em>branch out into</em> miran hacia delante; <em>fall '
             'apart</em> es el fracaso contra el que luchan. <em>Piece '
             'together</em> y <em>go through with</em> son cómo se ve terminar '
             '&mdash; ensamblar las piezas y no rendirse a mitad de camino.',

    ecEyebrow='Actividad 5 · Corrección de errores', ecTitle='Encuentra el reemplazo correcto',
    e1why='<strong>Up with.</strong> "Come up with" significa pensar una idea. '
          'El orden de las partículas importa &mdash; no se puede invertir sin '
          'más.',
    e2why='<strong>Forward to.</strong> "Look forward to" es la frase fija '
          '&mdash; "to" es siempre la preposición en este idiom. "Look forward '
          'for" no existe.',
    e3why='<strong>At the bottom.</strong> La frase correcta para un lugar '
          'concreto. "In the bottom" no es estándar; usamos "at" para un punto '
          'específico dentro de un área mayor.',
    e4why='<strong>Sort out.</strong> Significa organizar o resolver algo '
          'eficazmente. "Sort away", "sort off" y "sort aside" no son phrasal '
          'verbs estándar.',
    e5why='<strong>Impact of.</strong> La colocación correcta &mdash; "the '
          'impact of [algo]" describe consecuencias. "Impact in" no es '
          'estándar.',

    actTitle='Explica la construcción', actUse='Usa al menos tres:',
    actSpeakBrief='Uno de vosotros es el instructor de LEGO, el otro un '
                  'principiante que sigue cometiendo errores. Cuatro minutos '
                  'cada uno, luego cambiad.',
    actSpeak1='Explica un error que los principiantes siempre cometen, y di qué deberían hacer en su lugar.',
    actSpeak2='Describe un set que <em>se agotó</em> de inmediato, y otro que <em>esperas con ganas</em>.',
    actSpeak3='Dile a tu compañero que <em>ordene</em> sus piezas antes de <em>desmontar</em> nada.',
    actWriteKind='Escritura · 150–200 palabras',
    actWriteBrief='Escribe una breve guía para un nuevo socio del club de LEGO: '
                  'qué debe hacer antes de empezar a construir, un error que '
                  'debería evitar y qué hacer si falta una pieza. Usa al menos '
                  'tres de las expresiones anteriores.',
    actPlaceholder='Before you start, make sure you…',

    resPerfect='Puntuación perfecta. Preposiciones fijas y phrasal verbs, todo controlado.',
    resStrong='Muy bien. Repasa las diapositivas de verdadero/falso — ahí suele irse el último punto.',
    resMid='Buena base. Vuelve a las tres diapositivas iniciales: la preposición es fija, no lógica.',
    resLow='Lee otra vez las tres diapositivas de enseñanza y prueba de nuevo la opción múltiple.',
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
