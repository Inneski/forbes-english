# -*- coding: utf-8 -*-
"""Interface strings for the Minecraft C1 lesson.

English, German and Spanish. Teach-card bodies use the six-item form; the
English being taught — the register itself — stays English.
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
    coverTitle='Writing About <em>Minecraft</em>',
    coverSub='The same game, described by a player and described by a scholar',
    chipLevel='C1 · Advanced', chipFocus='Academic register &amp; collocation',
    chipCount='23 slides',

    reEyebrow='Before the questions', reTitle='Formality is a whole clause, not a word',
    re1h='The verbs that carry it', re1b=
        'A thing <strong>constitutes</strong> something rather than <em>is</em> it. A '
        'region is <strong>characterised by</strong> its features. A behaviour '
        '<strong>underpins</strong> what follows. A system <strong>serves as</strong> a '
        'channel for something.',
    re1n='Four verbs, and between them they carry most academic description.',
    re2h='What disqualifies an option', re2b=
        'Vague quantifiers (<em>wood and stone and stuff</em>), discourse markers '
        '(<em>basically</em>, <em>honestly</em>), and the defining relative opened with '
        '<em>is when</em>. Each one is fine in speech and none survives in an essay.',
    re2n='<em>A biome is when the land is different</em> &mdash; the giveaway construction.',
    re3h='The trap', re3b=
        'A formal word inside a casual frame is still casual: <em>we do resource '
        'acquisition</em> uses the phrase and gets it wrong, because the phrase needs no '
        'verb at all.',
    re3n='The whole clause has to change. That is what makes this hard.',

    coEyebrow='The fixed pairings', coTitle='Six collocations and their near-misses',
    co1h='Prepositions the verb fixes', co1b=
        'You <strong>adhere to</strong> guidelines, and you <em>comply with</em> them '
        '&mdash; never <em>comply to</em>. Something is <strong>regarded as</strong> a '
        'thing or <em>considered to be</em> one, never <em>viewed for</em> it.',
    co1n='<em>Capitalise on</em>, not <em>at</em>. There is no rule; the verb simply takes one.',
    co2h='Connotation decides two of them', co2b=
        'To <strong>exploit</strong> a mechanic is neutral and technical; <em>misuse</em> '
        'and <em>abuse</em> import a judgement the sentence is not making. To '
        '<strong>harness</strong> potential is positive, where <em>exploit</em> would '
        'insult the people described.',
    co2n='The same act, three attitudes. At C1 the attitude is the answer.',
    co3h='Terms a field has fixed', co3b=
        'Content built to rules is <strong>procedurally generated</strong>. That is the '
        'industry&rsquo;s own term; <em>randomly constructed</em> and <em>computationally '
        'rendered</em> describe nothing in particular and would not be understood.',
    co3n='When a field has a term, the near-synonym is not a stylistic choice.',

    lxEyebrow='The lexis', lxTitle='Words that only work in one grammar',
    lx1h='<em>Spawn</em> is intransitive here', lx1b=
        'Mobs <strong>spawn</strong>; nobody spawns them. The word describes appearing '
        'under conditions, so a transitive use &mdash; <em>the game spawns mobs</em> in '
        'the sense of <em>creates</em> &mdash; misses what it means.',
    lx1n='<em>Venture forth</em> is the same shape: intransitive, and it takes no object.',
    lx2h='<em>Iterative</em> is not <em>repetitive</em>', lx2b=
        'An <strong>iterative</strong> process repeats in order to refine: each cycle '
        'improves on the last. <em>Repetitive</em> means the same thing again with no '
        'gain, which is the opposite claim about the work.',
    lx2n='It comes from software, and it is now standard in any writing about design.',
    lx3h='The abstract nouns', lx3b=
        '<strong>Vigilance</strong> is watchfulness maintained against a hazard. A '
        '<strong>conduit</strong> is a channel, usually metaphorical. Cultural '
        '<strong>resonance</strong> is reach and significance beyond the original field.',
    lx3n='All three are formal, all three have plain equivalents, and the register is the point.',

    mcEyebrow='Activity 1 · Register', mcTitle='Which sentence would survive in an essay?',
    q1why='<strong>Upon entering a new biome, hostile mobs may spawn automatically if '
          'lighting levels are low.</strong> Formal throughout: <em>upon entering</em> '
          'for the time clause, <em>may</em> for the hedge, and <em>spawn</em> used '
          'intransitively, which is what it means.',
    q2why='<strong>A biome constitutes a distinct geographical region within the game '
          'world, characterised by particular climate and terrain.</strong> A defining '
          'sentence in academic form. <em>A biome is when&hellip;</em> is the '
          'construction that gives a definition away.',
    q3why='<strong>Had been fortifying.</strong> The action ran up to a stated past '
          'moment and was over by it. Past continuous gives no endpoint; the present '
          'perfect continuous cannot sit in a past time frame at all.',
    q4why='<strong>Minecraft&rsquo;s development followed an iterative process, with '
          'frequent updates refining gameplay mechanics.</strong> <em>Iterative</em> is '
          'the precise word for repeated cycles that improve something. Not '
          '<em>repetitive</em>, which says the opposite.',
    q5why='<strong>Resource acquisition constitutes the foundational economic behaviour '
          'underpinning all subsequent progression.</strong> <em>Resource acquisition</em> '
          'is a noun phrase and needs no verb of its own. <em>We do resource '
          'acquisition</em> is the formal word inside a casual frame.',
    q6why='<strong>Players must venture forth into unexplored territories to gather rare '
          'materials unavailable near spawn.</strong> <em>Venture forth</em> is '
          'intransitive: you venture forth <em>into</em> a place; you do not venture it.',

    dndEyebrow='Activity 2 · Collocation', dndTitle='Which phrase does the sentence take?',
    q7why='<strong>Adhere to.</strong> Guidelines are adhered to, or complied with. '
          '<em>Comply to</em> and <em>conform at</em> are the errors the pairing exists '
          'to catch.',
    q8why='<strong>Substantially augmented.</strong> An adverb of degree with a formal '
          'verb of increase. <em>Increased up</em> and <em>expanded over</em> add a '
          'particle the verb does not take.',
    q9why='<strong>Regarded as.</strong> The fixed frame is <em>regarded as</em> or '
          '<em>considered to be</em>. <em>Viewed for</em> and <em>known by</em> point at '
          'a purpose and an identifier, which is not what the sentence claims.',
    q10why='<strong>Exploit.</strong> The neutral technical verb for making use of a '
           'mechanic. <em>Misuse</em> and <em>abuse</em> carry a judgement the sentence '
           'is not making.',
    q11why='<strong>Procedurally generated.</strong> The industry&rsquo;s own term for '
           'content built from rules. <em>Randomly constructed</em> and '
           '<em>computationally rendered</em> would not be recognised as naming anything.',
    q12why='<strong>Harnessed.</strong> To harness is to put something to good use, and '
           'the sentence is describing teachers favourably. <em>Exploited</em> would say '
           'the opposite about the same act.',

    bankLabel='Word bank:',
    fibEyebrow='Activity 3 · The formal word', fibTitle='One word completes the sentence',
    fibHint='Six words in the bank, six gaps. Several near-synonyms are also accepted.',
    g1why='<strong>Vigilance.</strong> Watchfulness maintained against a hazard, and it '
          'collocates with <em>constant</em> and with <em>maintain</em>.',
    g2why='<strong>Lauded.</strong> Formally praised, and it takes <em>for</em> plus a '
          'gerund. <em>Praised</em> and <em>acclaimed</em> are accepted and sit a step '
          'lower.',
    g3why='<strong>Conduit.</strong> A channel through which something passes, used '
          'metaphorically here. <em>Mechanism</em> and <em>means</em> both work; '
          '<em>conduit</em> is the image.',
    g4why='<strong>Algorithmically.</strong> An adverb formed from the field&rsquo;s own '
          'noun, modifying <em>deterministic</em>. The hedge <em>to a certain extent</em> '
          'is doing work beside it.',
    g5why='<strong>Resonance.</strong> Reach and significance beyond the original field, '
          'which is exactly the claim being made about a game.',
    g6why='<strong>Manipulate.</strong> To handle or alter discrete units deliberately. '
          'Neutral in technical writing, whatever it means about people.',

    matchEyebrow='Activity 4 · The terminology', matchTitle='Match the term to its definition',
    matchHint='Click a term, then click what it means.',
    matchWhy='Seven terms, and every definition here is itself a model of the register '
             'the lesson is teaching: a noun phrase, a formal verb, and no <em>is '
             'when</em> anywhere. Read them as sentences to copy, not only as meanings '
             'to learn.',

    ordEyebrow='Activity 5 · The paragraph', ordTitle='Build the argued paragraph',
    ordHint='Click a sentence to place it, click a placed sentence to take it back.',
    o1why='The order is forced by five signals, and they are the transferable part. The '
          'origin and date come first because everything else refers back to them; the '
          'concessive opener (<em>despite its simple graphics</em>) introduces the '
          'technical claim; <em>this system</em> is a demonstrative reference that can '
          'only follow the sentence naming Redstone; <em>consequently</em> marks the '
          'educational result as a consequence rather than a coincidence; and the '
          'evidence formula (<em>is perhaps best evidenced by the fact that</em>) has to '
          'follow the claim it evidences. The closing move widens to what scholars make '
          'of it, which is where an academic paragraph usually ends.',

    actTitle='Present the case', actUse='Use at least four:',
    actSpeakBrief='One of you is arguing that games belong in a curriculum; the other '
                  'chairs the committee and is not persuaded. Four minutes each, then '
                  'swap.',
    actSpeak1='Define something from a game you know, in a sentence that would survive in an essay.',
    actSpeak2='Make a claim, then hedge it, then evidence it — in that order and in three sentences.',
    actSpeak3='Concede your opponent&rsquo;s strongest point and then turn it, starting with <em>despite</em>.',
    actSpeak4='Describe what a system does without once saying that it <em>is</em> anything.',
    actWriteKind='Writing · 200–250 words',
    actWriteBrief='Write the opening of a paper arguing that a game deserves academic '
                  'attention. Define your object, concede the obvious objection, make one '
                  'claim and evidence it, and close by saying what the field currently '
                  'holds. Hedge what deserves hedging and let no clause slip into speech.',
    actPlaceholder='Minecraft constitutes an unusually productive object of study because…',

    resPerfect='Full marks. You are reading the whole clause, which is what separates C1 from a formal word list.',
    resStrong='Strong. Look again at the collocations — the prepositions are where the last marks sit.',
    resMid='Good ground. Re-read the first slide: a formal word in a casual frame is still casual.',
    resLow='Work through the three opening slides again. Every wrong answer here is real English in the wrong register.',
)

T['de'] = dict(
    coverTitle='Über <em>Minecraft</em> schreiben',
    coverSub='Dasselbe Spiel, beschrieben von einem Spieler und beschrieben von einer Wissenschaftlerin',
    chipLevel='C1 · Fortgeschritten', chipFocus='Akademisches Register und Kollokation',
    chipCount='23 Folien',

    reEyebrow='Vor den Fragen', reTitle='Förmlichkeit ist ein ganzer Satz, kein Wort',
    re1h='Die Verben, die sie tragen', re1b=
        'Eine Sache <strong>constitutes</strong> etwas, statt es zu <em>sein</em>. Eine '
        'Region ist <strong>characterised by</strong> ihre Merkmale. Ein Verhalten '
        '<strong>underpins</strong>, was folgt. Ein System <strong>serves as</strong> '
        'Kanal für etwas.',
    re1n='Vier Verben, und zusammen tragen sie den größten Teil akademischer Beschreibung.',
    re2h='Was eine Option disqualifiziert', re2b=
        'Unbestimmte Mengenangaben (<em>wood and stone and stuff</em>), Diskursmarker '
        '(<em>basically</em>, <em>honestly</em>) und der Definitionssatz mit <em>is '
        'when</em>. Jedes davon geht gesprochen und keines überlebt im Aufsatz.',
    re2n='<em>A biome is when the land is different</em> — die verräterische Konstruktion.',
    re3h='Die Falle', re3b=
        'Ein förmliches Wort in einem umgangssprachlichen Rahmen bleibt umgangssprachlich: '
        '<em>we do resource acquisition</em> benutzt die Wendung und macht sie falsch, '
        'denn die Wendung braucht überhaupt kein Verb.',
    re3n='Der ganze Satz muss sich ändern. Das ist das Schwere daran.',

    coEyebrow='Die festen Verbindungen', coTitle='Sechs Kollokationen und ihre Fast-Treffer',
    co1h='Präpositionen, die das Verb festlegt', co1b=
        'Man <strong>adheres to</strong> Richtlinien und <em>complies with</em> ihnen — '
        'nie <em>comply to</em>. Etwas ist <strong>regarded as</strong> etwas oder '
        '<em>considered to be</em> etwas, nie <em>viewed for</em>.',
    co1n='<em>Capitalise on</em>, nicht <em>at</em>. Es gibt keine Regel; das Verb nimmt eine.',
    co2h='Zwei entscheidet die Konnotation', co2b=
        'Eine Spielmechanik zu <strong>exploit</strong>en ist neutral und technisch; '
        '<em>misuse</em> und <em>abuse</em> tragen ein Urteil hinein, das der Satz nicht '
        'fällt. Potenzial zu <strong>harness</strong>en ist positiv, wo <em>exploit</em> '
        'die Beschriebenen beleidigen würde.',
    co2n='Dieselbe Handlung, drei Haltungen. Auf C1 ist die Haltung die Antwort.',
    co3h='Begriffe, die ein Fach festgelegt hat', co3b=
        'Regelbasiert erzeugte Inhalte sind <strong>procedurally generated</strong>. Das '
        'ist der Begriff der Branche; <em>randomly constructed</em> und <em>computationally '
        'rendered</em> benennen nichts Bestimmtes und würden nicht verstanden.',
    co3n='Wo ein Fach einen Begriff hat, ist das Fast-Synonym keine Stilfrage.',

    lxEyebrow='Der Wortschatz', lxTitle='Wörter, die nur in einer Grammatik funktionieren',
    lx1h='<em>Spawn</em> ist hier intransitiv', lx1b=
        'Mobs <strong>spawn</strong>en; niemand spawnt sie. Das Wort beschreibt ein '
        'Erscheinen unter Bedingungen, also verfehlt eine transitive Verwendung im Sinn '
        'von <em>erzeugen</em> seine Bedeutung.',
    lx1n='<em>Venture forth</em> hat dieselbe Form: intransitiv, ohne Objekt.',
    lx2h='<em>Iterative</em> ist nicht <em>repetitive</em>', lx2b=
        'Ein <strong>iterative</strong>r Prozess wiederholt sich, um zu verfeinern: Jeder '
        'Durchgang verbessert den vorigen. <em>Repetitive</em> heißt dasselbe noch einmal '
        'ohne Gewinn — die gegenteilige Aussage über die Arbeit.',
    lx2n='Es kommt aus der Softwareentwicklung und ist heute Standard in jedem Text über Design.',
    lx3h='Die abstrakten Substantive', lx3b=
        '<strong>Vigilance</strong> ist aufrechterhaltene Wachsamkeit gegenüber einer '
        'Gefahr. Ein <strong>conduit</strong> ist ein Kanal, meist im übertragenen Sinn. '
        'Kulturelle <strong>resonance</strong> ist Reichweite über das eigene Feld hinaus.',
    lx3n='Alle drei sind förmlich, alle drei haben schlichte Entsprechungen — und darum geht es.',

    mcEyebrow='Aufgabe 1 · Register', mcTitle='Welcher Satz überlebt in einem Aufsatz?',
    q1why='<strong>Upon entering a new biome, hostile mobs may spawn automatically if '
          'lighting levels are low.</strong> Durchgehend förmlich: <em>upon entering</em> '
          'für den Temporalsatz, <em>may</em> als Abschwächung, <em>spawn</em> intransitiv.',
    q2why='<strong>A biome constitutes a distinct geographical region within the game '
          'world, characterised by particular climate and terrain.</strong> Eine Definition '
          'in akademischer Form. <em>A biome is when…</em> verrät jede Definition.',
    q3why='<strong>Had been fortifying.</strong> Die Handlung lief bis zu einem genannten '
          'Zeitpunkt in der Vergangenheit und war dann vorbei. Die Past Continuous gibt '
          'keinen Endpunkt; die Present Perfect Continuous verträgt keinen Vergangenheits­rahmen.',
    q4why='<strong>Minecraft&rsquo;s development followed an iterative process, with '
          'frequent updates refining gameplay mechanics.</strong> <em>Iterative</em> ist '
          'das genaue Wort für verbessernde Wiederholung. Nicht <em>repetitive</em>, das '
          'sagt das Gegenteil.',
    q5why='<strong>Resource acquisition constitutes the foundational economic behaviour '
          'underpinning all subsequent progression.</strong> <em>Resource acquisition</em> '
          'ist eine Nominalphrase und braucht kein eigenes Verb. <em>We do resource '
          'acquisition</em> ist das förmliche Wort im lockeren Rahmen.',
    q6why='<strong>Players must venture forth into unexplored territories to gather rare '
          'materials unavailable near spawn.</strong> <em>Venture forth</em> ist '
          'intransitiv: man venture forth <em>into</em> einen Ort.',

    dndEyebrow='Aufgabe 2 · Kollokation', dndTitle='Welche Wendung nimmt der Satz?',
    q7why='<strong>Adhere to.</strong> Richtlinien werden <em>adhered to</em> oder '
          '<em>complied with</em>. <em>Comply to</em> und <em>conform at</em> sind die '
          'Fehler, für die es die Aufgabe gibt.',
    q8why='<strong>Substantially augmented.</strong> Ein Gradadverb mit einem förmlichen '
          'Verb der Zunahme. <em>Increased up</em> und <em>expanded over</em> hängen dem '
          'Verb eine Partikel an, die es nicht nimmt.',
    q9why='<strong>Regarded as.</strong> Der feste Rahmen ist <em>regarded as</em> oder '
          '<em>considered to be</em>. <em>Viewed for</em> und <em>known by</em> zeigen auf '
          'Zweck und Kennzeichen.',
    q10why='<strong>Exploit.</strong> Das neutrale Fachverb für das Nutzen einer Mechanik. '
           '<em>Misuse</em> und <em>abuse</em> tragen ein Urteil hinein.',
    q11why='<strong>Procedurally generated.</strong> Der Branchenbegriff für regelbasiert '
           'erzeugte Inhalte. <em>Randomly constructed</em> und <em>computationally '
           'rendered</em> würden als Benennung nicht erkannt.',
    q12why='<strong>Harnessed.</strong> Etwas nutzbar machen, und der Satz beschreibt '
           'Lehrkräfte wohlwollend. <em>Exploited</em> sagte über dieselbe Handlung das '
           'Gegenteil.',

    bankLabel='Wortspeicher:',
    fibEyebrow='Aufgabe 3 · Das förmliche Wort', fibTitle='Ein Wort vervollständigt den Satz',
    fibHint='Sechs Wörter im Speicher, sechs Lücken. Mehrere Fast-Synonyme werden auch akzeptiert.',
    g1why='<strong>Vigilance.</strong> Aufrechterhaltene Wachsamkeit gegenüber einer '
          'Gefahr; kollokiert mit <em>constant</em> und mit <em>maintain</em>.',
    g2why='<strong>Lauded.</strong> Förmlich gelobt, mit <em>for</em> plus Gerundium. '
          '<em>Praised</em> und <em>acclaimed</em> werden akzeptiert und liegen eine Stufe '
          'tiefer.',
    g3why='<strong>Conduit.</strong> Ein Kanal, durch den etwas läuft, hier im übertragenen '
          'Sinn. <em>Mechanism</em> und <em>means</em> gehen auch; <em>conduit</em> ist das '
          'Bild.',
    g4why='<strong>Algorithmically.</strong> Ein Adverb aus dem Fachsubstantiv, das '
          '<em>deterministic</em> näher bestimmt. Die Abschwächung <em>to a certain '
          'extent</em> arbeitet daneben mit.',
    g5why='<strong>Resonance.</strong> Reichweite und Bedeutung über das eigene Feld '
          'hinaus — genau die Behauptung, die hier über ein Spiel aufgestellt wird.',
    g6why='<strong>Manipulate.</strong> Einzelne Einheiten gezielt bearbeiten oder '
          'verändern. Im Fachtext neutral.',

    matchEyebrow='Aufgabe 4 · Die Terminologie', matchTitle='Ordne dem Begriff seine Definition zu',
    matchHint='Klicke einen Begriff an, dann seine Bedeutung.',
    matchWhy='Sieben Begriffe — und jede Definition hier ist selbst ein Muster des '
             'Registers, um das es geht: eine Nominalphrase, ein förmliches Verb und '
             'nirgends ein <em>is when</em>. Lies sie als Sätze zum Abschauen, nicht nur '
             'als Bedeutungen zum Lernen.',

    ordEyebrow='Aufgabe 5 · Der Absatz', ordTitle='Bau den argumentierenden Absatz',
    ordHint='Klicke einen Satz an, um ihn zu setzen; klicke einen gesetzten an, um ihn zurückzunehmen.',
    o1why='Die Reihenfolge erzwingen fünf Signale, und die sind das Übertragbare. Ursprung '
          'und Jahr stehen vorn, weil alles Weitere darauf zurückverweist; der '
          'Konzessivauftakt (<em>despite its simple graphics</em>) führt die technische '
          'Behauptung ein; <em>this system</em> ist ein Demonstrativverweis und kann nur '
          'auf den Satz folgen, der Redstone nennt; <em>consequently</em> markiert das '
          'Bildungsergebnis als Folge statt als Zufall; und die Belegformel (<em>is perhaps '
          'best evidenced by the fact that</em>) muss auf die Behauptung folgen, die sie '
          'belegt. Der Schluss weitet auf die Forschung — dort endet ein akademischer '
          'Absatz meist.',

    actTitle='Trag den Fall vor', actUse='Benutze mindestens vier:',
    actSpeakBrief='Einer argumentiert, dass Spiele in einen Lehrplan gehören; die andere '
                  'leitet den Ausschuss und ist nicht überzeugt. Je vier Minuten, dann '
                  'tauschen.',
    actSpeak1='Definiere etwas aus einem Spiel, das du kennst, in einem Satz, der im Aufsatz bestehen würde.',
    actSpeak2='Stell eine Behauptung auf, schwäche sie ab, belege sie — in dieser Reihenfolge, in drei Sätzen.',
    actSpeak3='Räum das stärkste Argument der Gegenseite ein und dreh es dann um; fang mit <em>despite</em> an.',
    actSpeak4='Beschreibe, was ein System tut, ohne ein einziges Mal zu sagen, dass es etwas <em>ist</em>.',
    actWriteKind='Schreiben · 200–250 Wörter',
    actWriteBrief='Schreibe den Anfang eines Aufsatzes, der begründet, warum ein Spiel '
                  'akademische Aufmerksamkeit verdient. Definiere deinen Gegenstand, räum '
                  'den naheliegenden Einwand ein, stell eine Behauptung auf und belege sie, '
                  'und schließe mit dem Stand der Forschung. Schwäche ab, wo es angebracht '
                  'ist, und lass keinen Satz ins Gesprochene rutschen.',
    actPlaceholder='Minecraft constitutes an unusually productive object of study because…',

    resPerfect='Volle Punktzahl. Du liest den ganzen Satz — das unterscheidet C1 von einer Liste förmlicher Wörter.',
    resStrong='Stark. Sieh dir die Kollokationen noch einmal an; bei den Präpositionen liegen die letzten Punkte.',
    resMid='Gute Grundlage. Lies die erste Folie noch einmal: Ein förmliches Wort im lockeren Rahmen bleibt locker.',
    resLow='Arbeite die drei Einstiegsfolien noch einmal durch. Jede falsche Antwort ist echtes Englisch im falschen Register.',
)

T['es'] = dict(
    coverTitle='Escribir sobre <em>Minecraft</em>',
    coverSub='El mismo juego, descrito por un jugador y descrito por una académica',
    chipLevel='C1 · Avanzado', chipFocus='Registro académico y colocación',
    chipCount='23 diapositivas',

    reEyebrow='Antes de las preguntas', reTitle='La formalidad es la oración entera, no una palabra',
    re1h='Los verbos que la sostienen', re1b=
        'Una cosa <strong>constitutes</strong> algo en lugar de <em>ser</em>lo. Una región '
        'está <strong>characterised by</strong> sus rasgos. Un comportamiento '
        '<strong>underpins</strong> lo que sigue. Un sistema <strong>serves as</strong> '
        'canal para algo.',
    re1n='Cuatro verbos, y entre ellos sostienen casi toda la descripción académica.',
    re2h='Lo que descarta una opción', re2b=
        'Los cuantificadores vagos (<em>wood and stone and stuff</em>), los marcadores '
        'discursivos (<em>basically</em>, <em>honestly</em>) y la relativa definitoria con '
        '<em>is when</em>. Cada uno vale al hablar y ninguno sobrevive en un ensayo.',
    re2n='<em>A biome is when the land is different</em>: la construcción que delata.',
    re3h='La trampa', re3b=
        'Una palabra formal dentro de un marco coloquial sigue siendo coloquial: <em>we do '
        'resource acquisition</em> usa la expresión y la estropea, porque la expresión no '
        'necesita ningún verbo.',
    re3n='Tiene que cambiar la oración entera. Eso es lo difícil.',

    coEyebrow='Las combinaciones fijas', coTitle='Seis colocaciones y sus casi aciertos',
    co1h='Preposiciones que fija el verbo', co1b=
        'Se <strong>adhere to</strong> unas directrices y se <em>complies with</em> ellas, '
        'nunca <em>comply to</em>. Algo es <strong>regarded as</strong> una cosa o '
        '<em>considered to be</em> una cosa, nunca <em>viewed for</em>.',
    co1n='<em>Capitalise on</em>, no <em>at</em>. No hay regla; el verbo elige una.',
    co2h='En dos decide la connotación', co2b=
        '<strong>Exploit</strong> una mecánica es neutro y técnico; <em>misuse</em> y '
        '<em>abuse</em> traen un juicio que la frase no emite. <strong>Harness</strong> el '
        'potencial es positivo, donde <em>exploit</em> insultaría a quien se describe.',
    co2n='El mismo acto, tres actitudes. En C1 la actitud es la respuesta.',
    co3h='Términos que un campo ha fijado', co3b=
        'El contenido construido por reglas es <strong>procedurally generated</strong>. Ese '
        'es el término del sector; <em>randomly constructed</em> y <em>computationally '
        'rendered</em> no nombran nada concreto y no se entenderían.',
    co3n='Cuando un campo tiene un término, el casi sinónimo no es una elección de estilo.',

    lxEyebrow='El léxico', lxTitle='Palabras que solo funcionan en una gramática',
    lx1h='<em>Spawn</em> aquí es intransitivo', lx1b=
        'Los mobs <strong>spawn</strong>; nadie los spawnea. La palabra describe aparecer '
        'bajo ciertas condiciones, así que un uso transitivo con el sentido de <em>crear</em> '
        'pierde lo que significa.',
    lx1n='<em>Venture forth</em> tiene la misma forma: intransitivo y sin objeto.',
    lx2h='<em>Iterative</em> no es <em>repetitive</em>', lx2b=
        'Un proceso <strong>iterative</strong> se repite para refinar: cada ciclo mejora el '
        'anterior. <em>Repetitive</em> es lo mismo otra vez sin ganancia, que es la '
        'afirmación contraria sobre el trabajo.',
    lx2n='Viene del software y hoy es estándar en cualquier texto sobre diseño.',
    lx3h='Los sustantivos abstractos', lx3b=
        '<strong>Vigilance</strong> es atención sostenida frente a un peligro. Un '
        '<strong>conduit</strong> es un canal, casi siempre metafórico. La '
        '<strong>resonance</strong> cultural es alcance más allá del campo de origen.',
    lx3n='Las tres son formales, las tres tienen equivalente llano, y de eso va el registro.',

    mcEyebrow='Actividad 1 · Registro', mcTitle='¿Qué frase sobreviviría en un ensayo?',
    q1why='<strong>Upon entering a new biome, hostile mobs may spawn automatically if '
          'lighting levels are low.</strong> Formal de principio a fin: <em>upon entering</em> '
          'para la temporal, <em>may</em> como matiz y <em>spawn</em> en uso intransitivo.',
    q2why='<strong>A biome constitutes a distinct geographical region within the game world, '
          'characterised by particular climate and terrain.</strong> Una definición en forma '
          'académica. <em>A biome is when…</em> delata cualquier definición.',
    q3why='<strong>Had been fortifying.</strong> La acción llegó hasta un momento pasado '
          'concreto y terminó ahí. El pasado continuo no da final; el presente perfecto '
          'continuo no admite marco pasado.',
    q4why='<strong>Minecraft&rsquo;s development followed an iterative process, with frequent '
          'updates refining gameplay mechanics.</strong> <em>Iterative</em> es la palabra '
          'exacta para ciclos que mejoran. No <em>repetitive</em>, que dice lo contrario.',
    q5why='<strong>Resource acquisition constitutes the foundational economic behaviour '
          'underpinning all subsequent progression.</strong> <em>Resource acquisition</em> es '
          'un sintagma nominal y no necesita verbo propio. <em>We do resource acquisition</em> '
          'es la palabra formal en marco coloquial.',
    q6why='<strong>Players must venture forth into unexplored territories to gather rare '
          'materials unavailable near spawn.</strong> <em>Venture forth</em> es intransitivo: '
          'se venture forth <em>into</em> un lugar.',

    dndEyebrow='Actividad 2 · Colocación', dndTitle='¿Qué expresión pide la frase?',
    q7why='<strong>Adhere to.</strong> A las directrices se <em>adhere to</em> o se '
          '<em>complies with</em>. <em>Comply to</em> y <em>conform at</em> son los errores '
          'que la actividad busca.',
    q8why='<strong>Substantially augmented.</strong> Un adverbio de grado con un verbo formal '
          'de aumento. <em>Increased up</em> y <em>expanded over</em> añaden una partícula que '
          'el verbo no lleva.',
    q9why='<strong>Regarded as.</strong> El marco fijo es <em>regarded as</em> o '
          '<em>considered to be</em>. <em>Viewed for</em> y <em>known by</em> apuntan a una '
          'finalidad y a un identificador.',
    q10why='<strong>Exploit.</strong> El verbo técnico neutro para aprovechar una mecánica. '
           '<em>Misuse</em> y <em>abuse</em> traen un juicio.',
    q11why='<strong>Procedurally generated.</strong> El término propio del sector para el '
           'contenido construido por reglas. <em>Randomly constructed</em> y '
           '<em>computationally rendered</em> no se reconocerían como nombre de nada.',
    q12why='<strong>Harnessed.</strong> Aprovechar algo bien, y la frase describe a los '
           'docentes con buenos ojos. <em>Exploited</em> diría lo contrario del mismo acto.',

    bankLabel='Banco de palabras:',
    fibEyebrow='Actividad 3 · La palabra formal', fibTitle='Una palabra completa la frase',
    fibHint='Seis palabras en el banco, seis huecos. También se aceptan varios casi sinónimos.',
    g1why='<strong>Vigilance.</strong> Atención sostenida frente a un peligro; se combina con '
          '<em>constant</em> y con <em>maintain</em>.',
    g2why='<strong>Lauded.</strong> Elogiado formalmente, y lleva <em>for</em> más gerundio. '
          '<em>Praised</em> y <em>acclaimed</em> se aceptan y bajan un escalón.',
    g3why='<strong>Conduit.</strong> Un canal por el que pasa algo, aquí metafórico. '
          '<em>Mechanism</em> y <em>means</em> también valen; <em>conduit</em> es la imagen.',
    g4why='<strong>Algorithmically.</strong> Un adverbio formado del sustantivo del campo, que '
          'modifica a <em>deterministic</em>. El matiz <em>to a certain extent</em> trabaja a '
          'su lado.',
    g5why='<strong>Resonance.</strong> Alcance e importancia más allá del campo de origen, que '
          'es justo lo que se afirma de un juego.',
    g6why='<strong>Manipulate.</strong> Manejar o alterar unidades discretas a propósito. '
          'Neutro en escritura técnica.',

    matchEyebrow='Actividad 4 · La terminología', matchTitle='Relaciona el término con su definición',
    matchHint='Haz clic en un término y luego en lo que significa.',
    matchWhy='Siete términos, y cada definición es en sí misma un modelo del registro que '
             'enseña la lección: un sintagma nominal, un verbo formal y ningún <em>is when</em> '
             'por ninguna parte. Léelas como frases para copiar, no solo como significados que '
             'aprender.',

    ordEyebrow='Actividad 5 · El párrafo', ordTitle='Construye el párrafo argumentado',
    ordHint='Haz clic en una frase para colocarla; haz clic en una colocada para retirarla.',
    o1why='El orden lo imponen cinco señales, y son la parte transferible. El origen y la fecha '
          'van primero porque todo lo demás remite a ellos; el arranque concesivo (<em>despite '
          'its simple graphics</em>) introduce la afirmación técnica; <em>this system</em> es '
          'una referencia demostrativa y solo puede seguir a la frase que nombra Redstone; '
          '<em>consequently</em> marca el resultado educativo como consecuencia y no como '
          'casualidad; y la fórmula de evidencia (<em>is perhaps best evidenced by the fact '
          'that</em>) tiene que ir tras la afirmación que evidencia. El cierre se amplía a lo '
          'que dice la investigación, que es donde suele terminar un párrafo académico.',

    actTitle='Presenta el caso', actUse='Usa al menos cuatro:',
    actSpeakBrief='Uno defiende que los videojuegos tienen sitio en un plan de estudios; la '
                  'otra preside la comisión y no está convencida. Cuatro minutos cada uno, '
                  'luego cambiad.',
    actSpeak1='Define algo de un juego que conozcas, en una frase que sobreviviría en un ensayo.',
    actSpeak2='Haz una afirmación, matízala y evidénciala, en ese orden y en tres frases.',
    actSpeak3='Concede el mejor argumento de tu rival y luego dale la vuelta, empezando por <em>despite</em>.',
    actSpeak4='Describe lo que hace un sistema sin decir ni una vez que <em>es</em> algo.',
    actWriteKind='Escritura · 200–250 palabras',
    actWriteBrief='Escribe el arranque de un artículo que defienda que un juego merece atención '
                  'académica. Define tu objeto, concede la objeción evidente, haz una afirmación '
                  'y evidénciala, y cierra con lo que sostiene hoy el campo. Matiza lo que lo '
                  'merezca y que ninguna oración se deslice hacia lo hablado.',
    actPlaceholder='Minecraft constitutes an unusually productive object of study because…',

    resPerfect='Puntuación perfecta. Lees la oración entera, que es lo que separa C1 de una lista de palabras formales.',
    resStrong='Muy bien. Repasa las colocaciones: en las preposiciones están los últimos puntos.',
    resMid='Buena base. Relee la primera diapositiva: una palabra formal en marco coloquial sigue siendo coloquial.',
    resLow='Vuelve a trabajar las tres diapositivas iniciales. Cada respuesta incorrecta es inglés real en el registro equivocado.',
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
