# -*- coding: utf-8 -*-
"""Interface strings for the Minecraft Trivia lesson (B1).

English, German and Spanish. Teach-card bodies use the six-item form; the
English being taught stays English.
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
    coverTitle='Things Only <em>Players</em> Know',
    coverSub='Minecraft trivia, and the English that explains how anything turns into anything else',
    chipLevel='B1 · Intermediate', chipFocus='Change-of-state verbs &amp; long options',
    chipCount='23 slides',

    chEyebrow='Before the questions', chTitle='How English says a thing became another thing',
    ch1h='The change verbs', ch1b=
        'Lightning <strong>transforms</strong> a pig <strong>into</strong> a zombie '
        'piglin. It <strong>turns into</strong> one; it <strong>becomes</strong> one. '
        '<em>Transform</em> and <em>turn</em> both take <em>into</em>, and neither '
        'takes <em>to</em>.',
    ch1n='<em>Revert back into</em> is common in game English, though <em>back</em> is doing no work.',
    ch2h='Rules prefer the passive', ch2b=
        'A Charged Creeper <strong>is created when</strong> lightning strikes. A sponge '
        '<strong>can only be obtained by</strong> defeating an Elder Guardian. The doer '
        'is the game, so nobody names it.',
    ch2n='<em>By</em> + <em>-ing</em> after a passive: <em>obtained by defeating</em>, never <em>by defeat</em>.',
    ch3h='Two conditionals for two kinds of rule', ch3b=
        'Zero for what is always so: <em>if you add a thirteenth block, it '
        '<strong>doesn&rsquo;t</strong> move</em>. First for what will happen to you: '
        '<em>if you attack one, nearby piglins <strong>will</strong> become hostile</em>.',
    ch3n='Present in the <em>if</em>-clause either way. Only the result half changes.',

    opEyebrow='The reading skill', opTitle='Four options that differ by one clause',
    op1h='The noun is never the answer', op1b=
        'Every option here names the same kind of thing. What separates them is the '
        'clause hung off it: <em>the Gold Pickaxe, <strong>despite having</strong> the '
        'lowest durability</em>. Scan for the clause, not the noun.',
    op1n='If two options start identically, the difference is somewhere after the comma.',
    op2h='Which, who, whose', op2b=
        '<em>Which</em> for items and events, <em>who</em> for mobs treated as animate, '
        '<em>whose</em> for a property they own: <em>a Charged Creeper, '
        '<strong>whose</strong> explosion radius is doubled</em>.',
    op2n='<em>Whose</em> is not only for people. It is the possessive of <em>which</em> too.',
    op3h='Concession is the giveaway', op3b=
        '<em>Despite</em>, <em>even though</em>, <em>although</em>, <em>but</em> mark '
        'the surprising fact, and a trivia question is usually asking for exactly that. '
        '<em>Despite</em> takes a noun or an <em>-ing</em>; <em>even though</em> takes a '
        'clause.',
    op3n='<em>Despite having</em> the lowest durability &mdash; not <em>despite it has</em>.',

    nuEyebrow='The detail', nuTitle='Numbers, and the words hung in front of nouns',
    nu1h='Say the number exactly', nu1b=
        'Coordinates go negative: diamonds sit at <strong>Y = -58</strong>, read '
        '<em>minus fifty-eight</em>. Limits are exact: <em>up to <strong>12</strong> '
        'blocks</em>, <em>exactly <strong>15</strong> bookshelves</em>.',
    nu1n='<em>Up to</em> is a maximum; <em>exactly</em> admits nothing either side.',
    nu2h='Compound premodifiers', nu2b=
        'English packs a whole description in front of the noun and hyphenates it: a '
        '<strong>gravity-affected</strong> block, an <strong>iron-tier</strong> tool, a '
        '<strong>10-block</strong> radius, a <strong>day/night</strong> cycle.',
    nu2n='The hyphen shows the words are working as one adjective. No plural inside it: <em>10-block</em>, not <em>10-blocks</em>.',
    nu3h='<em>Re-</em> means again', nu3b=
        'You <strong>respawn</strong> where you last slept, a curable villager '
        '<strong>reverts</strong> to a villager, and a thrown Eye of Ender may be '
        '<strong>retrieved</strong>. The prefix is productive and predictable.',
    nu3n='It is the same <em>re-</em> as in <em>rebuild</em>, <em>retry</em> and <em>reload</em>.',

    mcEyebrow='Activity 1 · Trivia', mcTitle='What does a player actually know?',
    q1why='<strong>The Gold Pickaxe.</strong> It mines faster than any other, including '
          'netherite &mdash; and it breaks almost immediately, which is why nobody uses '
          'it. The concession is the whole fact.',
    q2why='<strong>The bed explodes.</strong> Beds only work where there is a day and a '
          'night, and neither the Nether nor the End has one. The explosion is the '
          'game&rsquo;s way of saying so.',
    q3why='<strong>A pig model with its height and width values swapped.</strong> The '
          'Creeper is an accident that was kept. Its shape is a pig standing on end.',
    q4why='<strong>Creepers and Phantoms.</strong> Tamed cats keep both away, which makes '
          'a cat one of the cheapest defences in the game.',
    q5why='<strong>A Charged Creeper.</strong> The explosion radius and damage both '
          'double, and a mob killed by one drops its head &mdash; the only way to get '
          'most mob heads at all.',
    q6why='<strong>Placing a door underwater creates an air pocket.</strong> The door '
          'displaces the water in its own block, so you can breathe there. It is the '
          'oldest trick in underwater exploration.',

    dndEyebrow='Activity 2 · Complete the fact', dndTitle='Which word finishes the sentence?',
    q7why='<strong>Carrot on a stick.</strong> The saddle lets you ride the pig; the '
          'carrot on a stick is what steers it. Two separate items doing two separate '
          'jobs.',
    q8why='<strong>Zombie piglin.</strong> Lightning transforms the pig, and the piglin '
          'is hostile only if provoked &mdash; but provoke one and every piglin nearby '
          'joins in.',
    q9why='<strong>Status effects.</strong> Milk clears them all, good and bad alike, '
          'which is why you do not drink it in the middle of a fight you are winning.',
    q10why='<strong>Modified Jungle Edge.</strong> The rarest biome in the game, and it '
           'only generates where a jungle meets a swamp under narrow conditions.',
    q11why='<strong>Golden Apple.</strong> The ordinary one, thrown after a Splash Potion '
           'of Weakness. The enchanted Notch Apple would also work and is far too rare '
           'to spend on it.',
    q12why='<strong>Torch.</strong> A torch under sand or gravel breaks the falling block '
           'the moment it lands, which is how you clear a gravel column without digging '
           'it twice.',

    fibEyebrow='Activity 3 · The exact number', fibTitle='Type what the sentence needs',
    fibHint='Numbers may be written in digits or in words.',
    g1why='<strong>-58.</strong> Since 1.18 the world extends below zero and diamonds are '
          'commonest at Y = -58. The minus is part of the answer.',
    g2why='<strong>12.</strong> A piston pushes up to twelve blocks. Add a thirteenth and '
          'nothing moves at all &mdash; a zero conditional, and an absolute limit.',
    g3why='<strong>Eye of Ender.</strong> Thrown into the air, it flies toward the nearest '
          'stronghold; sometimes it shatters, which is why you take more than you think '
          'you need.',
    g4why='<strong>Blazes.</strong> Plural, because the verb is <em>are</em>. They are the '
          'only source of Blaze Rods, and Blaze Rods are the only route to Eyes of Ender.',
    g5why='<strong>15.</strong> Exactly fifteen bookshelves, placed one block away with '
          'air between. Fourteen gives you less; sixteen gives you nothing extra.',
    g6why='<strong>Cod.</strong> Raw cod or raw salmon will do it, and taming takes '
          'patience &mdash; approach slowly, stop when the cat stops.',

    matchEyebrow='Activity 4 · The strange facts', matchTitle='Match the thing to what is odd about it',
    matchHint='Click a name, then click the fact.',
    matchWhy='Read the right-hand column as sentences to copy rather than facts to learn. '
             'Every one is built the same way: a passive or a change verb, then '
             '<em>by</em> plus an <em>-ing</em> form, then the condition. <em>Can only be '
             'obtained by defeating an Elder Guardian</em> is the frame, and it will carry '
             'almost any rule you need to state.',

    ordEyebrow='Activity 5 · The run', ordTitle='Put the seven steps in order',
    ordHint='Click a step to place it, click a placed step to take it back.',
    o1why='Gather wood, stone and food; mine iron and then diamonds; build a Nether '
          'Portal; kill Blazes for Blaze Rods; craft Eyes of Ender; find the stronghold '
          'portal; defeat the Ender Dragon. Nothing here can be reordered, because each '
          'step is the material for the next: no iron, no diamonds; no Blaze Rods, no '
          'Eyes of Ender; no Eyes, no stronghold. That dependency is what makes it a '
          'procedure, and it is the frame for retelling it with <em>first</em>, <em>once '
          'you have</em>, <em>only then</em> and <em>finally</em>.',

    actTitle='Tell them the thing they do not know', actUse='Use at least four:',
    actSpeakBrief='One of you knows a game inside out; the other has played it for an '
                  'hour. Three minutes each, then swap.',
    actSpeak1='Explain a trick in a game you know, and say why it works.',
    actSpeak2='Describe something that turns into something else, and what triggers it.',
    actSpeak3='State a rule twice: once as a general truth, once as a warning to your partner.',
    actSpeak4='Tell your partner a fact that surprised you, starting with <em>despite</em> or <em>even though</em>.',
    actWriteKind='Writing · 150–180 words',
    actWriteBrief='Write six facts about a game, a sport or a hobby that a beginner would '
                  'not know. State each one as a rule rather than a story, use a passive '
                  'or a change verb in at least three of them, and make at least one turn '
                  'on a concession &mdash; the surprising part is what makes a fact worth '
                  'telling.',
    actPlaceholder='Despite being the weakest tool in the game, the gold pickaxe…',

    resPerfect='Full marks. You can read four long options and find the clause that separates them.',
    resStrong='Strong. Look again at the passive frames — <em>obtained by defeating</em> is the shape to keep.',
    resMid='Good base. Go back to the first slide: change verbs take <em>into</em>, and rules take the passive.',
    resLow='Read the three opening slides again. The trivia is the excuse; the English is the lesson.',
)

T['de'] = dict(
    coverTitle='Was nur <em>Spieler</em> wissen',
    coverSub='Minecraft-Trivia — und das Englisch, das erklärt, wie aus irgendetwas irgendetwas anderes wird',
    chipLevel='B1 · Mittelstufe', chipFocus='Verben der Zustandsänderung und lange Optionen',
    chipCount='23 Folien',

    chEyebrow='Vor den Fragen', chTitle='Wie das Englische sagt, dass etwas zu etwas anderem wurde',
    ch1h='Die Verben der Verwandlung', ch1b=
        'Ein Blitz <strong>transforms</strong> ein Schwein <strong>into</strong> einen '
        'Zombie-Piglin. Es <strong>turns into</strong> einen; es <strong>becomes</strong> '
        'einer. <em>Transform</em> und <em>turn</em> nehmen beide <em>into</em>, keines '
        '<em>to</em>.',
    ch1n='<em>Revert back into</em> ist im Spiel-Englisch üblich, auch wenn <em>back</em> nichts tut.',
    ch2h='Regeln stehen lieber im Passiv', ch2b=
        'Ein Charged Creeper <strong>is created when</strong> ein Blitz einschlägt. Ein '
        'Schwamm <strong>can only be obtained by</strong> einen Elder Guardian zu '
        'besiegen. Der Urheber ist das Spiel, also nennt ihn niemand.',
    ch2n='<em>By</em> + <em>-ing</em> nach einem Passiv: <em>obtained by defeating</em>, nie <em>by defeat</em>.',
    ch3h='Zwei Konditionale für zwei Arten von Regel', ch3b=
        'Typ 0 für das, was immer gilt: <em>if you add a thirteenth block, it '
        '<strong>doesn&rsquo;t</strong> move</em>. Typ I für das, was dir passieren wird: '
        '<em>if you attack one, nearby piglins <strong>will</strong> become hostile</em>.',
    ch3n='Im <em>if</em>-Satz steht so oder so Präsens. Nur die zweite Hälfte ändert sich.',

    opEyebrow='Die Lesefertigkeit', opTitle='Vier Optionen, die sich in einem Nebensatz unterscheiden',
    op1h='Das Substantiv ist nie die Antwort', op1b=
        'Jede Option nennt hier dieselbe Art von Sache. Was sie trennt, ist der Zusatz: '
        '<em>the Gold Pickaxe, <strong>despite having</strong> the lowest durability</em>. '
        'Such nach dem Zusatz, nicht nach dem Substantiv.',
    op1n='Wenn zwei Optionen gleich anfangen, liegt der Unterschied hinter dem Komma.',
    op2h='Which, who, whose', op2b=
        '<em>Which</em> für Dinge und Ereignisse, <em>who</em> für Mobs, die als belebt '
        'behandelt werden, <em>whose</em> für eine Eigenschaft, die sie haben: <em>a '
        'Charged Creeper, <strong>whose</strong> explosion radius is doubled</em>.',
    op2n='<em>Whose</em> ist nicht nur für Personen. Es ist auch der Genitiv von <em>which</em>.',
    op3h='Die Einräumung verrät es', op3b=
        '<em>Despite</em>, <em>even though</em>, <em>although</em>, <em>but</em> markieren '
        'die überraschende Tatsache — und genau danach fragt eine Trivia-Frage meist. '
        '<em>Despite</em> nimmt ein Substantiv oder ein <em>-ing</em>, <em>even though</em> '
        'einen Nebensatz.',
    op3n='<em>Despite having</em> the lowest durability — nicht <em>despite it has</em>.',

    nuEyebrow='Das Detail', nuTitle='Zahlen und die Wörter vor dem Substantiv',
    nu1h='Sag die Zahl genau', nu1b=
        'Koordinaten werden negativ: Diamanten liegen bei <strong>Y = -58</strong>, '
        'gelesen <em>minus fifty-eight</em>. Grenzen sind exakt: <em>up to '
        '<strong>12</strong> blocks</em>, <em>exactly <strong>15</strong> bookshelves</em>.',
    nu1n='<em>Up to</em> ist ein Maximum; <em>exactly</em> lässt in keine Richtung Spielraum.',
    nu2h='Zusammengesetzte Attribute', nu2b=
        'Das Englische packt eine ganze Beschreibung vor das Substantiv und bindet sie mit '
        'Bindestrich: ein <strong>gravity-affected</strong> block, ein '
        '<strong>iron-tier</strong> tool, ein <strong>10-block</strong> radius, ein '
        '<strong>day/night</strong> cycle.',
    nu2n='Der Bindestrich zeigt, dass die Wörter als ein Adjektiv arbeiten. Kein Plural darin: <em>10-block</em>, nicht <em>10-blocks</em>.',
    nu3h='<em>Re-</em> heißt wieder', nu3b=
        'Man <strong>respawn</strong>t dort, wo man zuletzt geschlafen hat, ein geheilter '
        'Dorfbewohner <strong>reverts</strong> zum Dorfbewohner, und ein geworfenes Eye of '
        'Ender lässt sich <strong>retrieve</strong>n. Das Präfix ist produktiv und '
        'berechenbar.',
    nu3n='Es ist dasselbe <em>re-</em> wie in <em>rebuild</em>, <em>retry</em> und <em>reload</em>.',

    mcEyebrow='Aufgabe 1 · Trivia', mcTitle='Was weiß eine Spielerin wirklich?',
    q1why='<strong>The Gold Pickaxe.</strong> Sie baut schneller ab als jede andere, auch '
          'als Netherit — und sie zerbricht fast sofort, weshalb sie niemand benutzt. Die '
          'Einräumung ist die ganze Tatsache.',
    q2why='<strong>The bed explodes.</strong> Betten funktionieren nur, wo es Tag und Nacht '
          'gibt, und weder Nether noch End hat beides. Die Explosion ist die Art, wie das '
          'Spiel das sagt.',
    q3why='<strong>A pig model with its height and width values swapped.</strong> Der '
          'Creeper ist ein Versehen, das man behalten hat. Seine Form ist ein Schwein, das '
          'hochkant steht.',
    q4why='<strong>Creepers and Phantoms.</strong> Gezähmte Katzen halten beide fern, was '
          'eine Katze zur billigsten Verteidigung im Spiel macht.',
    q5why='<strong>A Charged Creeper.</strong> Radius und Schaden verdoppeln sich, und ein '
          'davon getöteter Mob lässt seinen Kopf fallen — der einzige Weg zu den meisten '
          'Mob-Köpfen überhaupt.',
    q6why='<strong>Placing a door underwater creates an air pocket.</strong> Die Tür '
          'verdrängt das Wasser in ihrem eigenen Block, also kann man dort atmen. Der '
          'älteste Trick der Unterwassererkundung.',

    dndEyebrow='Aufgabe 2 · Vervollständige die Tatsache', dndTitle='Welches Wort beendet den Satz?',
    q7why='<strong>Carrot on a stick.</strong> Der Sattel erlaubt das Reiten; die Karotte am '
          'Stock lenkt. Zwei Gegenstände, zwei Aufgaben.',
    q8why='<strong>Zombie piglin.</strong> Der Blitz verwandelt das Schwein, und der Piglin '
          'ist nur feindlich, wenn man ihn reizt — dann aber macht jeder Piglin in der Nähe '
          'mit.',
    q9why='<strong>Status effects.</strong> Milch löscht alle, gute wie schlechte — deshalb '
          'trinkt man sie nicht mitten in einem Kampf, den man gerade gewinnt.',
    q10why='<strong>Modified Jungle Edge.</strong> Das seltenste Biom im Spiel; es entsteht '
           'nur dort, wo ein Dschungel unter engen Bedingungen auf einen Sumpf trifft.',
    q11why='<strong>Golden Apple.</strong> Der gewöhnliche, geworfen nach einem Splash '
           'Potion of Weakness. Der verzauberte Notch Apple ginge auch und ist viel zu '
           'selten dafür.',
    q12why='<strong>Torch.</strong> Eine Fackel unter Sand oder Kies zerbricht den fallenden '
           'Block im Moment des Aufkommens — so räumt man eine Kiessäule, ohne zweimal zu '
           'graben.',

    fibEyebrow='Aufgabe 3 · Die genaue Zahl', fibTitle='Tippe, was der Satz braucht',
    fibHint='Zahlen dürfen als Ziffern oder als Wörter geschrieben werden.',
    g1why='<strong>-58.</strong> Seit 1.18 reicht die Welt unter null, und Diamanten sind '
          'bei Y = -58 am häufigsten. Das Minus gehört zur Antwort.',
    g2why='<strong>12.</strong> Ein Kolben schiebt bis zu zwölf Blöcke. Nimm einen '
          'dreizehnten dazu, und gar nichts bewegt sich — Konditional 0, und eine absolute '
          'Grenze.',
    g3why='<strong>Eye of Ender.</strong> In die Luft geworfen fliegt es zur nächsten '
          'Festung; manchmal zerspringt es, weshalb man mehr mitnimmt, als man denkt.',
    g4why='<strong>Blazes.</strong> Plural, weil das Verb <em>are</em> ist. Sie sind die '
          'einzige Quelle für Blaze Rods, und Blaze Rods sind der einzige Weg zu Eyes of '
          'Ender.',
    g5why='<strong>15.</strong> Genau fünfzehn Bücherregale, einen Block entfernt, mit Luft '
          'dazwischen. Vierzehn gibt weniger; sechzehn gibt nichts dazu.',
    g6why='<strong>Cod.</strong> Roher Kabeljau oder roher Lachs tun es, und Zähmen braucht '
          'Geduld — langsam nähern, stehen bleiben, wenn die Katze stehen bleibt.',

    matchEyebrow='Aufgabe 4 · Die seltsamen Tatsachen', matchTitle='Ordne der Sache zu, was an ihr merkwürdig ist',
    matchHint='Klicke einen Namen an, dann die Tatsache.',
    matchWhy='Lies die rechte Spalte als Sätze zum Abschauen, nicht als Fakten zum Lernen. '
             'Jeder ist gleich gebaut: ein Passiv oder ein Verwandlungsverb, dann <em>by</em> '
             'plus <em>-ing</em>, dann die Bedingung. <em>Can only be obtained by defeating '
             'an Elder Guardian</em> ist das Muster, und es trägt fast jede Regel, die du '
             'formulieren musst.',

    ordEyebrow='Aufgabe 5 · Der Durchlauf', ordTitle='Bring die sieben Schritte in die richtige Reihenfolge',
    ordHint='Klicke einen Schritt an, um ihn zu setzen; klicke einen gesetzten an, um ihn zurückzunehmen.',
    o1why='Holz, Stein und Essen sammeln; Eisen und dann Diamanten abbauen; ein Nether-Portal '
          'bauen; Blazes für Blaze Rods töten; Eyes of Ender craften; das Festungsportal '
          'finden; den Enderdrachen besiegen. Nichts davon lässt sich umstellen, weil jeder '
          'Schritt das Material für den nächsten ist: kein Eisen, keine Diamanten; keine '
          'Blaze Rods, keine Eyes of Ender; keine Eyes, keine Festung. Diese Abhängigkeit '
          'macht daraus ein Verfahren — und den Rahmen zum Nacherzählen mit <em>first</em>, '
          '<em>once you have</em>, <em>only then</em> und <em>finally</em>.',

    actTitle='Erzähl ihnen, was sie nicht wissen', actUse='Benutze mindestens vier:',
    actSpeakBrief='Einer kennt ein Spiel in- und auswendig; die andere hat es eine Stunde '
                  'gespielt. Je drei Minuten, dann tauschen.',
    actSpeak1='Erklär einen Trick aus einem Spiel, das du kennst, und sag, warum er funktioniert.',
    actSpeak2='Beschreibe etwas, das sich in etwas anderes verwandelt, und was das auslöst.',
    actSpeak3='Formuliere eine Regel zweimal: einmal als allgemeine Wahrheit, einmal als Warnung an deinen Partner.',
    actSpeak4='Erzähl deinem Partner eine Tatsache, die dich überrascht hat, und fang mit <em>despite</em> oder <em>even though</em> an.',
    actWriteKind='Schreiben · 150–180 Wörter',
    actWriteBrief='Schreibe sechs Tatsachen über ein Spiel, einen Sport oder ein Hobby, die '
                  'ein Anfänger nicht wüsste. Formuliere jede als Regel statt als Geschichte, '
                  'benutze in mindestens dreien ein Passiv oder ein Verwandlungsverb, und '
                  'lass mindestens eine auf einer Einräumung drehen — das Überraschende ist '
                  'das, was eine Tatsache erzählenswert macht.',
    actPlaceholder='Despite being the weakest tool in the game, the gold pickaxe…',

    resPerfect='Volle Punktzahl. Du kannst vier lange Optionen lesen und den Nebensatz finden, der sie trennt.',
    resStrong='Stark. Sieh dir die Passivmuster noch einmal an — <em>obtained by defeating</em> ist die Form zum Behalten.',
    resMid='Gute Grundlage. Zurück zur ersten Folie: Verwandlungsverben nehmen <em>into</em>, und Regeln nehmen das Passiv.',
    resLow='Lies die drei Einstiegsfolien noch einmal. Die Trivia ist der Vorwand; das Englische ist die Lektion.',
)

T['es'] = dict(
    coverTitle='Lo que solo saben los <em>jugadores</em>',
    coverSub='Curiosidades de Minecraft y el inglés que explica cómo una cosa se convierte en otra',
    chipLevel='B1 · Intermedio', chipFocus='Verbos de cambio de estado y opciones largas',
    chipCount='23 diapositivas',

    chEyebrow='Antes de las preguntas', chTitle='Cómo dice el inglés que algo se convirtió en otra cosa',
    ch1h='Los verbos del cambio', ch1b=
        'Un rayo <strong>transforms</strong> un cerdo <strong>into</strong> un zombi '
        'piglin. <strong>Turns into</strong> uno; <strong>becomes</strong> uno. '
        '<em>Transform</em> y <em>turn</em> llevan los dos <em>into</em>, ninguno '
        '<em>to</em>.',
    ch1n='<em>Revert back into</em> es habitual en el inglés de los juegos, aunque <em>back</em> no aporte nada.',
    ch2h='Las reglas prefieren la pasiva', ch2b=
        'Un Charged Creeper <strong>is created when</strong> cae un rayo. Una esponja '
        '<strong>can only be obtained by</strong> derrotar a un Elder Guardian. El agente '
        'es el juego, así que nadie lo nombra.',
    ch2n='<em>By</em> + <em>-ing</em> tras una pasiva: <em>obtained by defeating</em>, nunca <em>by defeat</em>.',
    ch3h='Dos condicionales para dos tipos de regla', ch3b=
        'El cero para lo que siempre es así: <em>if you add a thirteenth block, it '
        '<strong>doesn&rsquo;t</strong> move</em>. El primero para lo que te va a pasar: '
        '<em>if you attack one, nearby piglins <strong>will</strong> become hostile</em>.',
    ch3n='En la oración con <em>if</em> va presente en los dos casos. Solo cambia la otra mitad.',

    opEyebrow='La destreza lectora', opTitle='Cuatro opciones que se diferencian en una cláusula',
    op1h='El sustantivo nunca es la respuesta', op1b=
        'Todas las opciones nombran aquí el mismo tipo de cosa. Lo que las separa es la '
        'cláusula colgada de él: <em>the Gold Pickaxe, <strong>despite having</strong> the '
        'lowest durability</em>. Busca la cláusula, no el sustantivo.',
    op1n='Si dos opciones empiezan igual, la diferencia está después de la coma.',
    op2h='Which, who, whose', op2b=
        '<em>Which</em> para objetos y sucesos, <em>who</em> para mobs tratados como '
        'animados, <em>whose</em> para una propiedad suya: <em>a Charged Creeper, '
        '<strong>whose</strong> explosion radius is doubled</em>.',
    op2n='<em>Whose</em> no es solo para personas. También es el posesivo de <em>which</em>.',
    op3h='La concesión te delata la respuesta', op3b=
        '<em>Despite</em>, <em>even though</em>, <em>although</em>, <em>but</em> marcan el '
        'dato sorprendente, y eso es justo lo que suele pedir una pregunta de curiosidades. '
        '<em>Despite</em> lleva sustantivo o <em>-ing</em>; <em>even though</em> lleva '
        'oración.',
    op3n='<em>Despite having</em> the lowest durability, no <em>despite it has</em>.',

    nuEyebrow='El detalle', nuTitle='Números y las palabras que van delante del sustantivo',
    nu1h='Di el número exacto', nu1b=
        'Las coordenadas se vuelven negativas: los diamantes están en <strong>Y = -58</strong>, '
        'que se lee <em>minus fifty-eight</em>. Los límites son exactos: <em>up to '
        '<strong>12</strong> blocks</em>, <em>exactly <strong>15</strong> bookshelves</em>.',
    nu1n='<em>Up to</em> es un máximo; <em>exactly</em> no admite margen a ningún lado.',
    nu2h='Modificadores compuestos', nu2b=
        'El inglés mete toda una descripción delante del sustantivo y la une con guion: un '
        'block <strong>gravity-affected</strong>, una herramienta <strong>iron-tier</strong>, '
        'un radio de <strong>10-block</strong>, un ciclo <strong>day/night</strong>.',
    nu2n='El guion muestra que las palabras funcionan como un solo adjetivo. Sin plural dentro: <em>10-block</em>, no <em>10-blocks</em>.',
    nu3h='<em>Re-</em> significa otra vez', nu3b=
        'Uno <strong>respawn</strong>ea donde durmió por última vez, un aldeano curado '
        '<strong>reverts</strong> a aldeano y un Eye of Ender lanzado puede '
        '<strong>retrieve</strong>arse. El prefijo es productivo y previsible.',
    nu3n='Es el mismo <em>re-</em> de <em>rebuild</em>, <em>retry</em> y <em>reload</em>.',

    mcEyebrow='Actividad 1 · Curiosidades', mcTitle='¿Qué sabe de verdad un jugador?',
    q1why='<strong>The Gold Pickaxe.</strong> Pica más rápido que ninguna otra, incluida la '
          'de netherita, y se rompe casi de inmediato, por eso no la usa nadie. La concesión '
          'es todo el dato.',
    q2why='<strong>The bed explodes.</strong> Las camas solo funcionan donde hay día y noche, '
          'y ni el Nether ni el End los tienen. La explosión es la manera que tiene el juego '
          'de decirlo.',
    q3why='<strong>A pig model with its height and width values swapped.</strong> El Creeper '
          'es un accidente que se conservó. Su forma es un cerdo puesto de pie.',
    q4why='<strong>Creepers and Phantoms.</strong> Los gatos domesticados mantienen a raya a '
          'los dos, lo que convierte a un gato en la defensa más barata del juego.',
    q5why='<strong>A Charged Creeper.</strong> El radio y el daño se duplican, y un mob '
          'muerto por uno suelta su cabeza: la única forma de conseguir casi todas las '
          'cabezas de mob.',
    q6why='<strong>Placing a door underwater creates an air pocket.</strong> La puerta '
          'desplaza el agua de su propio bloque, así que ahí se puede respirar. El truco más '
          'antiguo de la exploración submarina.',

    dndEyebrow='Actividad 2 · Completa el dato', dndTitle='¿Qué palabra cierra la frase?',
    q7why='<strong>Carrot on a stick.</strong> La silla te deja montar al cerdo; la zanahoria '
          'en un palo lo dirige. Dos objetos, dos funciones.',
    q8why='<strong>Zombie piglin.</strong> El rayo transforma al cerdo, y el piglin solo es '
          'hostil si lo provocas; pero provoca a uno y se suman todos los de alrededor.',
    q9why='<strong>Status effects.</strong> La leche los elimina todos, buenos y malos, por '
          'eso no se bebe en mitad de un combate que vas ganando.',
    q10why='<strong>Modified Jungle Edge.</strong> El bioma más raro del juego; solo se genera '
           'donde una jungla se encuentra con un pantano bajo condiciones muy concretas.',
    q11why='<strong>Golden Apple.</strong> La normal, lanzada tras una Splash Potion of '
           'Weakness. La Notch Apple encantada también valdría y es demasiado rara para '
           'gastarla en esto.',
    q12why='<strong>Torch.</strong> Una antorcha bajo la arena o la grava rompe el bloque que '
           'cae en cuanto aterriza: así se despeja una columna de grava sin cavar dos veces.',

    fibEyebrow='Actividad 3 · El número exacto', fibTitle='Escribe lo que pide la frase',
    fibHint='Los números pueden escribirse en cifras o en palabras.',
    g1why='<strong>-58.</strong> Desde la 1.18 el mundo baja de cero y los diamantes son más '
          'frecuentes en Y = -58. El menos forma parte de la respuesta.',
    g2why='<strong>12.</strong> Un pistón empuja hasta doce bloques. Añade un decimotercero y '
          'no se mueve nada: condicional cero, y un límite absoluto.',
    g3why='<strong>Eye of Ender.</strong> Lanzado al aire, vuela hacia la fortaleza más '
          'cercana; a veces se rompe, por eso se llevan más de los que uno cree necesitar.',
    g4why='<strong>Blazes.</strong> Plural, porque el verbo es <em>are</em>. Son la única '
          'fuente de Blaze Rods, y los Blaze Rods son el único camino a los Eyes of Ender.',
    g5why='<strong>15.</strong> Exactamente quince estanterías, a un bloque de distancia y con '
          'aire en medio. Catorce dan menos; dieciséis no dan nada más.',
    g6why='<strong>Cod.</strong> Bacalao o salmón crudos sirven, y domesticar exige paciencia: '
          'acércate despacio y párate cuando el gato se pare.',

    matchEyebrow='Actividad 4 · Los datos raros', matchTitle='Relaciona la cosa con lo que tiene de raro',
    matchHint='Haz clic en un nombre y luego en el dato.',
    matchWhy='Lee la columna derecha como frases para copiar, no como datos para memorizar. '
             'Todas están construidas igual: una pasiva o un verbo de cambio, luego <em>by</em> '
             'más un <em>-ing</em>, y luego la condición. <em>Can only be obtained by '
             'defeating an Elder Guardian</em> es el molde, y aguanta casi cualquier regla que '
             'necesites enunciar.',

    ordEyebrow='Actividad 5 · La partida', ordTitle='Ordena los siete pasos',
    ordHint='Haz clic en un paso para colocarlo; haz clic en uno colocado para retirarlo.',
    o1why='Reunir madera, piedra y comida; picar hierro y luego diamantes; construir un portal '
          'al Nether; matar Blazes para conseguir Blaze Rods; fabricar Eyes of Ender; encontrar '
          'el portal de la fortaleza; derrotar al Ender Dragon. Nada de esto se puede reordenar, '
          'porque cada paso es el material del siguiente: sin hierro no hay diamantes; sin Blaze '
          'Rods no hay Eyes of Ender; sin Eyes no hay fortaleza. Esa dependencia es lo que lo '
          'convierte en un procedimiento, y es el molde para volver a contarlo con '
          '<em>first</em>, <em>once you have</em>, <em>only then</em> y <em>finally</em>.',

    actTitle='Cuéntales lo que no saben', actUse='Usa al menos cuatro:',
    actSpeakBrief='Uno se sabe un juego de memoria; el otro lo ha jugado una hora. Tres minutos '
                  'cada uno, luego cambiad.',
    actSpeak1='Explica un truco de un juego que conozcas y di por qué funciona.',
    actSpeak2='Describe algo que se convierte en otra cosa y qué lo provoca.',
    actSpeak3='Enuncia una regla dos veces: una como verdad general y otra como aviso a tu compañero.',
    actSpeak4='Cuéntale a tu compañero un dato que te sorprendiera, empezando por <em>despite</em> o <em>even though</em>.',
    actWriteKind='Escritura · 150–180 palabras',
    actWriteBrief='Escribe seis datos sobre un juego, un deporte o una afición que un principiante '
                  'no sabría. Enuncia cada uno como regla y no como anécdota, usa una pasiva o un '
                  'verbo de cambio en al menos tres, y que al menos uno gire sobre una concesión: '
                  'lo sorprendente es lo que hace que un dato merezca contarse.',
    actPlaceholder='Despite being the weakest tool in the game, the gold pickaxe…',

    resPerfect='Puntuación perfecta. Sabes leer cuatro opciones largas y encontrar la cláusula que las separa.',
    resStrong='Muy bien. Repasa los moldes en pasiva: <em>obtained by defeating</em> es la forma que hay que guardar.',
    resMid='Buena base. Vuelve a la primera diapositiva: los verbos de cambio llevan <em>into</em> y las reglas llevan pasiva.',
    resLow='Relee las tres diapositivas iniciales. Las curiosidades son la excusa; el inglés es la lección.',
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
