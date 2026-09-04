# -*- coding: utf-8 -*-
"""Interface strings for the Minecraft B1 lesson.

English, German and Spanish. Teach-card bodies use the six-item form so the
rule travels with its heading; the English being taught stays English.
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
    coverTitle='Surviving the <em>First Night</em>',
    coverSub='The tenses a player needs to tell the story, and the words the game gives them',
    chipLevel='B1 · Intermediate', chipFocus='Tense choice &amp; game vocabulary',
    chipCount='20 slides',

    tnEyebrow='Before the questions', tnTitle='Three tenses, three jobs',
    tn1h='What you always do', tn1b=
        'The present simple carries habits and rules: <em>when I find diamonds, I '
        '<strong>always make</strong> armour</em>. It is the tense for what is true '
        'every time, not what is happening now.',
    tn1n='<em>Every morning I am checking my chest</em> is the classic B1 slip. A routine is not in progress.',
    tn2h='What has just happened', tn2b=
        'The present perfect links a finished action to now: <em>I <strong>have '
        'just</strong> found a village</em>. <em>Just</em> means a moment ago, '
        '<em>already</em> means sooner than expected, <em>yet</em> means still not.',
    tn2n='Add <em>yesterday</em> and it breaks &mdash; a finished time needs the past simple.',
    tn3h='How long it has been going on', tn3b=
        '<em>I <strong>have been playing for</strong> two hours</em>. The activity is '
        'still running and the sentence measures it. <strong>For</strong> takes a '
        'length of time; <strong>since</strong> takes a starting point.',
    tn3n='<em>For two hours</em>, <em>since Tuesday</em>. Ask whether the word names a stretch or a moment.',

    coEyebrow='The pairings', coTitle='The word the game actually uses',
    co1h='Verbs that only take one noun', co1b=
        'You <strong>sleep in</strong> a bed, not rest in one. You <strong>take '
        'damage</strong>, never make it. You <strong>carry</strong> a torch, you do not '
        'wear it. Each pairing is fixed and has to be learned whole.',
    co1n='<em>Make damage</em> is the commonest of these errors, and it is not English.',
    co2h='Words that describe how often', co2b=
        'Diamonds are <strong>rare</strong>, or <em>uncommon</em> &mdash; that is about '
        'how seldom they appear. <em>Difficult</em> and <em>hard</em> are about the '
        'effort of getting them, which is a different claim.',
    co2n='Rare things can be easy to get once found. The two words are not interchangeable.',
    co3h='The connector that warns', co3b=
        '<strong>Otherwise</strong> introduces what happens if you do not: <em>build a '
        'shelter, <strong>otherwise</strong> mobs will attack</em>. <em>Or</em> and '
        '<em>or else</em> do the same job in a lower register.',
    co3n='It always points forward to a consequence, and the consequence is always the bad one.',

    vcEyebrow='The vocabulary', vcTitle='Game words that are ordinary English underneath',
    vc1h='<em>Spawn</em> and <em>respawn</em>', vc1b=
        'To <strong>spawn</strong> is to appear in the world &mdash; the first time, or '
        'after dying. The <em>re-</em> in <strong>respawn</strong> means again, exactly '
        'as it does in <em>rebuild</em> and <em>retry</em>.',
    vc1n='Your <em>spawn point</em> is where you reappear: your bed, or where the world started you.',
    vc2h='<em>Craft</em>, <em>mine</em>, <em>smelt</em>', vc2b=
        'To <strong>craft</strong> is to make something with skill from materials. To '
        '<strong>mine</strong> is to dig for stone, coal or iron. To '
        '<strong>smelt</strong> is to heat raw ore in a furnace until it becomes usable '
        'metal.',
    vc2n='All three are real English outside the game, and all three mean the same thing there.',
    vc3h='<em>Mob</em>, <em>biome</em>, <em>inventory</em>', vc3b=
        'A <strong>mob</strong> is any moving creature, friendly or not. A '
        '<strong>biome</strong> is a region with its own weather, plants and landscape. '
        'Your <strong>inventory</strong> is everything you are carrying.',
    vc3n='<em>Biome</em> and <em>inventory</em> are used unchanged in geography and in business.',

    mcEyebrow='Activity 1 · Multiple choice', mcTitle='What do you know, and how do you say it?',
    q1why='<strong>Dangerous mobs like zombies, skeletons and creepers start to appear.</strong> '
          'Darkness is what lets hostile mobs spawn, which is why the first thing a new '
          'player is told is to build a shelter before nightfall.',
    q2why='<strong>You need obsidian blocks arranged in a rectangular frame.</strong> '
          'Obsidian is made where water meets lava, and the frame has to be a rectangle '
          'before it will light.',
    q3why='<strong>I have been playing for two hours and I have just built my first '
          'house.</strong> Two present perfects doing two jobs: the continuous measures '
          'the two hours, and <em>have just built</em> reports something finished a '
          'moment ago.',
    q4why='<strong>You need to give them both some wheat, which puts them in love '
          'mode.</strong> Both animals have to be fed, and wheat is the food cows take. '
          'Other animals take other food, which is part of the game&rsquo;s vocabulary.',
    q5why='<strong>When I find diamonds, I always make armour before I go to fight '
          'monsters.</strong> A habit takes the present simple throughout, including in '
          'the <em>when</em> clause. Continuous forms describe what is happening now, '
          'not what is always true.',
    q6why='<strong>You appear at your spawn point &mdash; usually your bed or the world '
          'start point.</strong> Sleeping in a bed sets the spawn point, which is why '
          'sleeping is worth doing even when you are not tired.',

    fibEyebrow='Activity 2 · The exact word', fibTitle='Complete the sentence',
    fibHint='The clue in brackets tells you what kind of word you need.',
    g1why='<strong>Craft.</strong> To make something new by combining materials. '
          '<em>Make</em>, <em>create</em> and <em>build</em> are all accepted, but '
          '<em>craft</em> is the word the game uses.',
    g2why='<strong>Otherwise.</strong> It introduces the consequence of not doing the '
          'thing. <em>Or</em> and <em>or else</em> say the same in a more spoken '
          'register.',
    g3why='<strong>Collected.</strong> Past simple, because the sentence is telling a '
          'story of finished actions in order. <em>Gathered</em>, <em>got</em> and '
          '<em>obtained</em> all work.',
    g4why='<strong>Can.</strong> Present ability or possibility. <em>Could</em> would '
          'make it hypothetical, and the sentence is describing what is actually '
          'available once the horse is tamed.',
    g5why='<strong>For.</strong> <em>For</em> takes a length of time, <em>since</em> '
          'takes the moment it started. Three hours is a length.',
    g6why='<strong>Just.</strong> A moment ago, and it sits between <em>have</em> and '
          'the participle. <em>Already</em> would mean sooner than expected; <em>yet</em> '
          'only works in negatives and questions.',

    bankLabel='Word bank:',
    dndEyebrow='Activity 3 · The right pairing', dndTitle='Which phrase belongs?',
    dndHint='Twenty-four phrases, six gaps. Most of them belong to no gap here.',
    d1why='<strong>Sleep.</strong> You <em>sleep in</em> a bed. <em>Rest in</em> a bed '
          'is English but does not set your spawn point, and the game only counts '
          'sleeping.',
    d2why='<strong>Rare.</strong> How seldom a thing appears. <em>Uncommon</em> is '
          'accepted; <em>difficult</em> and <em>hard</em> describe the effort, which is '
          'a different claim.',
    d3why='<strong>Take damage.</strong> Fixed: you <em>take</em> damage, you never '
          '<em>make</em> it. The thing that causes it does the damage.',
    d4why='<strong>Carry.</strong> A torch is held, not worn. <em>Wear</em> is for '
          'clothes and armour.',
    d5why='<strong>Final boss.</strong> The fixed gaming term for the enemy at the end '
          'of a game. <em>Hardest mob</em> and <em>last enemy</em> both describe it and '
          'neither is the term.',
    d6why='<strong>Eat.</strong> Plain and right. <em>Consume</em> is accepted but '
          'belongs to a nutrition label rather than a player talking.',

    matchEyebrow='Activity 4 · The glossary', matchTitle='Match the term to its meaning',
    matchHint='Click a term, then click what it means.',
    matchWhy='Every one of these seven is a real English word doing a job in the game. '
             '<em>Craft</em>, <em>mine</em> and <em>smelt</em> are what people did with '
             'materials long before there was a game to do it in; <em>mob</em>, '
             '<em>biome</em> and <em>inventory</em> come from crowds, geography and '
             'shopkeeping. Knowing the everyday sense is what lets you use them outside '
             'Minecraft.',

    ordEyebrow='Activity 5 · The first night', ordTitle='Put the seven steps in order',
    ordHint='Click a step to place it, click a placed step to take it back.',
    o1why='You appear in a new world, punch a tree for wood, craft a wooden pickaxe, '
          'mine stone and coal, build a shelter before dark, light it with torches, and '
          'sleep until morning. Each step exists because of the one before it: no wood, '
          'no pickaxe; no pickaxe, no stone; no shelter and no light, and the mobs spawn '
          'where you are standing. That dependency is what makes it a procedure rather '
          'than a list, and it is the frame for retelling it with <em>first</em>, '
          '<em>then</em>, <em>after that</em> and <em>until</em>.',

    actTitle='Tell someone how to survive', actUse='Use at least four:',
    actSpeakBrief='One of you has played for years, the other has never opened the game. '
                  'Three minutes each, then swap.',
    actSpeak1='Explain the first ten minutes of a new world to someone who has never played anything.',
    actSpeak2='Say what you have been doing in a game recently and what you have just finished.',
    actSpeak3='Describe your routine in a game you play — what you always do, and in what order.',
    actSpeak4='Warn your partner about three dangers, using <em>otherwise</em> each time.',
    actWriteKind='Writing · 120–150 words',
    actWriteBrief='Write the survival guide you would give a friend on their first night. '
                  'Say what they must do and in what order, what happens otherwise, and '
                  'what you have learned from playing. Use the present simple for the '
                  'rules and the present perfect for your own experience.',
    actPlaceholder='The first thing you have to do is…',

    resPerfect='Full marks. You can tell the story and you have the words the game uses for it.',
    resStrong='Strong. Check the pairings again — <em>take damage</em> and <em>carry a torch</em> are where the last mark goes.',
    resMid='Good base. Go back to the first slide: habits take the present simple, and <em>for</em> takes a length of time.',
    resLow='Read the three opening slides again. Three tenses, three jobs, and the rest is vocabulary.',
)

T['de'] = dict(
    coverTitle='Die <em>erste Nacht</em> überstehen',
    coverSub='Die Zeitformen, mit denen ein Spieler die Geschichte erzählt — und die Wörter, die das Spiel ihm gibt',
    chipLevel='B1 · Mittelstufe', chipFocus='Zeitwahl und Spielvokabular',
    chipCount='20 Folien',

    tnEyebrow='Vor den Fragen', tnTitle='Drei Zeitformen, drei Aufgaben',
    tn1h='Was du immer tust', tn1b=
        'Das Present Simple trägt Gewohnheiten und Regeln: <em>when I find diamonds, I '
        '<strong>always make</strong> armour</em>. Es ist die Zeit für das, was jedes '
        'Mal gilt, nicht für das, was gerade passiert.',
    tn1n='<em>Every morning I am checking my chest</em> ist der klassische B1-Fehler. Eine Routine läuft nicht gerade ab.',
    tn2h='Was gerade passiert ist', tn2b=
        'Das Present Perfect verbindet eine abgeschlossene Handlung mit jetzt: <em>I '
        '<strong>have just</strong> found a village</em>. <em>Just</em> heißt eben '
        'gerade, <em>already</em> früher als erwartet, <em>yet</em> noch nicht.',
    tn2n='Setz <em>yesterday</em> dazu und es bricht — abgeschlossene Zeit braucht das Past Simple.',
    tn3h='Wie lange es schon läuft', tn3b=
        '<em>I <strong>have been playing for</strong> two hours</em>. Die Tätigkeit läuft '
        'noch, und der Satz misst sie. <strong>For</strong> nimmt eine Zeitspanne, '
        '<strong>since</strong> einen Startpunkt.',
    tn3n='<em>For two hours</em>, <em>since Tuesday</em>. Frag, ob das Wort eine Spanne oder einen Moment nennt.',

    coEyebrow='Die festen Verbindungen', coTitle='Das Wort, das das Spiel wirklich benutzt',
    co1h='Verben, die nur ein Substantiv nehmen', co1b=
        'Du <strong>sleep in</strong> einem Bett, nicht <em>rest in</em>. Du '
        '<strong>take damage</strong>, nie <em>make</em>. Du <strong>carry</strong> eine '
        'Fackel, du trägst sie nicht am Körper. Jede Verbindung ist fest.',
    co1n='<em>Make damage</em> ist der häufigste dieser Fehler — und es gibt ihn im Englischen nicht.',
    co2h='Wörter für die Häufigkeit', co2b=
        'Diamanten sind <strong>rare</strong> oder <em>uncommon</em> — das sagt, wie '
        'selten sie vorkommen. <em>Difficult</em> und <em>hard</em> sagen etwas über den '
        'Aufwand, sie zu bekommen, und das ist eine andere Aussage.',
    co2n='Seltenes kann leicht zu holen sein, wenn man es gefunden hat. Die Wörter sind nicht austauschbar.',
    co3h='Der Konnektor, der warnt', co3b=
        '<strong>Otherwise</strong> leitet ein, was passiert, wenn du es nicht tust: '
        '<em>build a shelter, <strong>otherwise</strong> mobs will attack</em>. <em>Or</em> '
        'und <em>or else</em> tun dasselbe in tieferem Register.',
    co3n='Es zeigt immer auf eine Folge — und immer auf die schlechte.',

    vcEyebrow='Das Vokabular', vcTitle='Spielwörter, die darunter normales Englisch sind',
    vc1h='<em>Spawn</em> und <em>respawn</em>', vc1b=
        '<strong>Spawn</strong> heißt in der Welt erscheinen — beim ersten Mal oder nach '
        'dem Tod. Das <em>re-</em> in <strong>respawn</strong> heißt wieder, genau wie in '
        '<em>rebuild</em> und <em>retry</em>.',
    vc1n='Dein <em>spawn point</em> ist, wo du wieder auftauchst: dein Bett oder der Startpunkt der Welt.',
    vc2h='<em>Craft</em>, <em>mine</em>, <em>smelt</em>', vc2b=
        '<strong>Craft</strong> heißt, aus Material mit Geschick etwas herstellen. '
        '<strong>Mine</strong> heißt, nach Stein, Kohle oder Eisen graben. '
        '<strong>Smelt</strong> heißt, Roherz im Ofen zu brauchbarem Metall schmelzen.',
    vc2n='Alle drei sind echtes Englisch außerhalb des Spiels und bedeuten dort dasselbe.',
    vc3h='<em>Mob</em>, <em>biome</em>, <em>inventory</em>', vc3b=
        'Ein <strong>mob</strong> ist jedes bewegliche Wesen, freundlich oder nicht. Ein '
        '<strong>biome</strong> ist eine Region mit eigenem Wetter, eigenen Pflanzen und '
        'eigener Landschaft. Dein <strong>inventory</strong> ist alles, was du trägst.',
    vc3n='<em>Biome</em> und <em>inventory</em> werden unverändert in Geografie und Wirtschaft benutzt.',

    mcEyebrow='Aufgabe 1 · Multiple Choice', mcTitle='Was weißt du — und wie sagst du es?',
    q1why='<strong>Dangerous mobs like zombies, skeletons and creepers start to appear.</strong> '
          'Die Dunkelheit ist es, die feindliche Mobs spawnen lässt. Darum lautet der '
          'erste Rat an neue Spieler, vor Einbruch der Nacht einen Unterstand zu bauen.',
    q2why='<strong>You need obsidian blocks arranged in a rectangular frame.</strong> '
          'Obsidian entsteht, wo Wasser auf Lava trifft, und der Rahmen muss ein Rechteck '
          'sein, bevor er sich entzünden lässt.',
    q3why='<strong>I have been playing for two hours and I have just built my first '
          'house.</strong> Zwei Present Perfects mit zwei Aufgaben: die Verlaufsform misst '
          'die zwei Stunden, <em>have just built</em> meldet etwas eben Abgeschlossenes.',
    q4why='<strong>You need to give them both some wheat, which puts them in love '
          'mode.</strong> Beide Tiere müssen gefüttert werden, und Kühe nehmen Weizen. '
          'Andere Tiere nehmen anderes Futter — auch das gehört zum Vokabular.',
    q5why='<strong>When I find diamonds, I always make armour before I go to fight '
          'monsters.</strong> Eine Gewohnheit steht durchgehend im Present Simple, auch im '
          '<em>when</em>-Satz. Verlaufsformen beschreiben, was jetzt passiert.',
    q6why='<strong>You appear at your spawn point — usually your bed or the world start '
          'point.</strong> Im Bett zu schlafen setzt den Spawnpunkt. Darum lohnt sich '
          'Schlafen auch, wenn man nicht müde ist.',

    fibEyebrow='Aufgabe 2 · Das genaue Wort', fibTitle='Vervollständige den Satz',
    fibHint='Der Hinweis in Klammern sagt, welche Art von Wort gebraucht wird.',
    g1why='<strong>Craft.</strong> Aus Material etwas Neues herstellen. <em>Make</em>, '
          '<em>create</em> und <em>build</em> werden akzeptiert, aber <em>craft</em> ist '
          'das Wort des Spiels.',
    g2why='<strong>Otherwise.</strong> Es leitet die Folge davon ein, es nicht zu tun. '
          '<em>Or</em> und <em>or else</em> sagen dasselbe gesprochener.',
    g3why='<strong>Collected.</strong> Past Simple, denn der Satz erzählt abgeschlossene '
          'Handlungen der Reihe nach. <em>Gathered</em>, <em>got</em> und <em>obtained</em> '
          'gehen auch.',
    g4why='<strong>Can.</strong> Gegenwärtige Fähigkeit oder Möglichkeit. <em>Could</em> '
          'machte es hypothetisch, aber der Satz beschreibt, was nach dem Zähmen '
          'tatsächlich geht.',
    g5why='<strong>For.</strong> <em>For</em> nimmt eine Zeitspanne, <em>since</em> den '
          'Moment des Beginns. Drei Stunden sind eine Spanne.',
    g6why='<strong>Just.</strong> Eben gerade, und es steht zwischen <em>have</em> und dem '
          'Partizip. <em>Already</em> hieße früher als erwartet; <em>yet</em> geht nur in '
          'Verneinungen und Fragen.',

    bankLabel='Wortspeicher:',
    dndEyebrow='Aufgabe 3 · Die richtige Verbindung', dndTitle='Welche Wendung gehört hin?',
    dndHint='Vierundzwanzig Wendungen, sechs Lücken. Die meisten gehören in keine davon.',
    d1why='<strong>Sleep.</strong> Man <em>sleeps in</em> einem Bett. <em>Rest in</em> ist '
          'Englisch, setzt aber keinen Spawnpunkt — das Spiel zählt nur Schlafen.',
    d2why='<strong>Rare.</strong> Wie selten etwas vorkommt. <em>Uncommon</em> wird '
          'akzeptiert; <em>difficult</em> und <em>hard</em> meinen den Aufwand.',
    d3why='<strong>Take damage.</strong> Fest: man <em>nimmt</em> Schaden, man macht ihn '
          'nie. Das Verursachende richtet den Schaden an.',
    d4why='<strong>Carry.</strong> Eine Fackel wird gehalten, nicht getragen. <em>Wear</em> '
          'gilt für Kleidung und Rüstung.',
    d5why='<strong>Final boss.</strong> Der feste Gaming-Begriff für den Gegner am Ende '
          'eines Spiels. <em>Hardest mob</em> und <em>last enemy</em> beschreiben ihn, sind '
          'aber nicht der Begriff.',
    d6why='<strong>Eat.</strong> Schlicht und richtig. <em>Consume</em> wird akzeptiert, '
          'gehört aber auf ein Nährwertetikett.',

    matchEyebrow='Aufgabe 4 · Das Glossar', matchTitle='Ordne dem Begriff seine Bedeutung zu',
    matchHint='Klicke einen Begriff an, dann seine Bedeutung.',
    matchWhy='Alle sieben sind echte englische Wörter, die im Spiel eine Aufgabe haben. '
             '<em>Craft</em>, <em>mine</em> und <em>smelt</em> taten Menschen mit Material, '
             'lange bevor es ein Spiel dazu gab; <em>mob</em>, <em>biome</em> und '
             '<em>inventory</em> kommen von Menschenmenge, Geografie und Warenwirtschaft. '
             'Die Alltagsbedeutung zu kennen ist das, was sie außerhalb von Minecraft '
             'benutzbar macht.',

    ordEyebrow='Aufgabe 5 · Die erste Nacht', ordTitle='Bring die sieben Schritte in die richtige Reihenfolge',
    ordHint='Klicke einen Schritt an, um ihn zu setzen; klicke einen gesetzten an, um ihn zurückzunehmen.',
    o1why='Du erscheinst in einer neuen Welt, schlägst einen Baum für Holz, craftest eine '
          'Holzspitzhacke, baust Stein und Kohle ab, baust vor der Dunkelheit einen '
          'Unterstand, machst ihn mit Fackeln hell und schläfst bis zum Morgen. Jeder '
          'Schritt existiert wegen des vorigen: kein Holz, keine Spitzhacke; keine '
          'Spitzhacke, kein Stein; kein Unterstand und kein Licht, und die Mobs spawnen '
          'dort, wo du stehst. Diese Abhängigkeit macht daraus ein Verfahren statt einer '
          'Liste — und den Rahmen zum Nacherzählen mit <em>first</em>, <em>then</em>, '
          '<em>after that</em> und <em>until</em>.',

    actTitle='Erklär jemandem das Überleben', actUse='Benutze mindestens vier:',
    actSpeakBrief='Einer spielt seit Jahren, die andere hat das Spiel nie geöffnet. Je '
                  'drei Minuten, dann tauschen.',
    actSpeak1='Erklär die ersten zehn Minuten einer neuen Welt jemandem, der noch nie irgendetwas gespielt hat.',
    actSpeak2='Sag, was du in letzter Zeit in einem Spiel gemacht hast und was du gerade fertig hast.',
    actSpeak3='Beschreibe deine Routine in einem Spiel, das du spielst — was du immer tust und in welcher Reihenfolge.',
    actSpeak4='Warne deinen Partner vor drei Gefahren und benutze jedes Mal <em>otherwise</em>.',
    actWriteKind='Schreiben · 120–150 Wörter',
    actWriteBrief='Schreibe die Überlebensanleitung, die du einer Freundin für ihre erste '
                  'Nacht geben würdest. Sag, was sie tun muss und in welcher Reihenfolge, '
                  'was sonst passiert und was du selbst gelernt hast. Present Simple für '
                  'die Regeln, Present Perfect für deine eigene Erfahrung.',
    actPlaceholder='The first thing you have to do is…',

    resPerfect='Volle Punktzahl. Du kannst die Geschichte erzählen und hast die Wörter dafür.',
    resStrong='Stark. Sieh dir die festen Verbindungen noch einmal an — bei <em>take damage</em> und <em>carry a torch</em> geht der letzte Punkt verloren.',
    resMid='Gute Grundlage. Zurück zur ersten Folie: Gewohnheiten stehen im Present Simple, und <em>for</em> nimmt eine Zeitspanne.',
    resLow='Lies die drei Einstiegsfolien noch einmal. Drei Zeitformen, drei Aufgaben — der Rest ist Vokabular.',
)

T['es'] = dict(
    coverTitle='Sobrevivir a la <em>primera noche</em>',
    coverSub='Los tiempos verbales que un jugador necesita para contarlo y las palabras que le da el juego',
    chipLevel='B1 · Intermedio', chipFocus='Elección de tiempo y vocabulario del juego',
    chipCount='20 diapositivas',

    tnEyebrow='Antes de las preguntas', tnTitle='Tres tiempos, tres funciones',
    tn1h='Lo que haces siempre', tn1b=
        'El presente simple lleva las costumbres y las reglas: <em>when I find diamonds, '
        'I <strong>always make</strong> armour</em>. Es el tiempo de lo que es cierto '
        'siempre, no de lo que ocurre ahora.',
    tn1n='<em>Every morning I am checking my chest</em> es el fallo clásico de B1. Una rutina no está en curso.',
    tn2h='Lo que acaba de pasar', tn2b=
        'El presente perfecto une una acción terminada con el ahora: <em>I <strong>have '
        'just</strong> found a village</em>. <em>Just</em> es hace un momento, '
        '<em>already</em> antes de lo esperado, <em>yet</em> todavía no.',
    tn2n='Añade <em>yesterday</em> y se rompe: un tiempo cerrado pide el pasado simple.',
    tn3h='Cuánto tiempo lleva', tn3b=
        '<em>I <strong>have been playing for</strong> two hours</em>. La actividad sigue y '
        'la frase la mide. <strong>For</strong> lleva una duración; <strong>since</strong>, '
        'un punto de inicio.',
    tn3n='<em>For two hours</em>, <em>since Tuesday</em>. Pregunta si la palabra nombra un tramo o un momento.',

    coEyebrow='Las combinaciones', coTitle='La palabra que usa de verdad el juego',
    co1h='Verbos que solo admiten un sustantivo', co1b=
        '<strong>Sleep in</strong> a bed, no <em>rest in</em>. <strong>Take damage</strong>, '
        'nunca <em>make</em>. <strong>Carry</strong> una antorcha; no se lleva puesta. Cada '
        'combinación es fija y se aprende entera.',
    co1n='<em>Make damage</em> es el más común de estos errores, y no existe en inglés.',
    co2h='Palabras sobre la frecuencia', co2b=
        'Los diamantes son <strong>rare</strong>, o <em>uncommon</em>: eso dice cada cuánto '
        'aparecen. <em>Difficult</em> y <em>hard</em> hablan del esfuerzo de conseguirlos, '
        'que es otra afirmación.',
    co2n='Algo raro puede ser fácil de coger una vez encontrado. No son intercambiables.',
    co3h='El conector que avisa', co3b=
        '<strong>Otherwise</strong> introduce lo que pasa si no lo haces: <em>build a '
        'shelter, <strong>otherwise</strong> mobs will attack</em>. <em>Or</em> y <em>or '
        'else</em> hacen lo mismo en un registro más bajo.',
    co3n='Siempre señala una consecuencia, y siempre la mala.',

    vcEyebrow='El vocabulario', vcTitle='Palabras del juego que por debajo son inglés corriente',
    vc1h='<em>Spawn</em> y <em>respawn</em>', vc1b=
        '<strong>Spawn</strong> es aparecer en el mundo: la primera vez o tras morir. El '
        '<em>re-</em> de <strong>respawn</strong> significa otra vez, igual que en '
        '<em>rebuild</em> y <em>retry</em>.',
    vc1n='Tu <em>spawn point</em> es donde reapareces: tu cama o donde te dejó el mundo al empezar.',
    vc2h='<em>Craft</em>, <em>mine</em>, <em>smelt</em>', vc2b=
        '<strong>Craft</strong> es hacer algo con destreza a partir de materiales. '
        '<strong>Mine</strong> es excavar en busca de piedra, carbón o hierro. '
        '<strong>Smelt</strong> es fundir mineral bruto en un horno hasta obtener metal '
        'utilizable.',
    vc2n='Los tres son inglés real fuera del juego y significan lo mismo dentro.',
    vc3h='<em>Mob</em>, <em>biome</em>, <em>inventory</em>', vc3b=
        'Un <strong>mob</strong> es cualquier criatura que se mueve, amistosa o no. Un '
        '<strong>biome</strong> es una región con su clima, sus plantas y su paisaje. Tu '
        '<strong>inventory</strong> es todo lo que llevas encima.',
    vc3n='<em>Biome</em> e <em>inventory</em> se usan igual en geografía y en gestión de empresas.',

    mcEyebrow='Actividad 1 · Opción múltiple', mcTitle='¿Qué sabes y cómo lo dices?',
    q1why='<strong>Dangerous mobs like zombies, skeletons and creepers start to appear.</strong> '
          'La oscuridad es lo que permite que aparezcan los mobs hostiles. Por eso lo '
          'primero que se le dice a un jugador nuevo es que construya un refugio antes de '
          'que anochezca.',
    q2why='<strong>You need obsidian blocks arranged in a rectangular frame.</strong> La '
          'obsidiana se forma donde el agua toca la lava, y el marco tiene que ser un '
          'rectángulo para poder encenderlo.',
    q3why='<strong>I have been playing for two hours and I have just built my first '
          'house.</strong> Dos presentes perfectos con dos funciones: el continuo mide las '
          'dos horas y <em>have just built</em> informa de algo terminado hace un momento.',
    q4why='<strong>You need to give them both some wheat, which puts them in love '
          'mode.</strong> Hay que alimentar a los dos animales, y las vacas comen trigo. '
          'Otros animales comen otras cosas, y eso también es vocabulario.',
    q5why='<strong>When I find diamonds, I always make armour before I go to fight '
          'monsters.</strong> Una costumbre va en presente simple de principio a fin, '
          'incluida la oración con <em>when</em>. Los continuos describen lo que pasa ahora.',
    q6why='<strong>You appear at your spawn point — usually your bed or the world start '
          'point.</strong> Dormir en una cama fija el punto de reaparición. Por eso vale la '
          'pena dormir aunque no tengas sueño.',

    fibEyebrow='Actividad 2 · La palabra exacta', fibTitle='Completa la frase',
    fibHint='La pista entre paréntesis dice qué tipo de palabra hace falta.',
    g1why='<strong>Craft.</strong> Hacer algo nuevo combinando materiales. <em>Make</em>, '
          '<em>create</em> y <em>build</em> se aceptan, pero <em>craft</em> es la palabra '
          'del juego.',
    g2why='<strong>Otherwise.</strong> Introduce la consecuencia de no hacerlo. <em>Or</em> '
          'y <em>or else</em> dicen lo mismo en registro más hablado.',
    g3why='<strong>Collected.</strong> Pasado simple, porque la frase cuenta acciones '
          'terminadas en orden. <em>Gathered</em>, <em>got</em> y <em>obtained</em> también '
          'valen.',
    g4why='<strong>Can.</strong> Capacidad o posibilidad presente. <em>Could</em> lo haría '
          'hipotético, y la frase describe lo que realmente se puede una vez domado el '
          'caballo.',
    g5why='<strong>For.</strong> <em>For</em> lleva una duración, <em>since</em> el momento '
          'en que empezó. Tres horas son una duración.',
    g6why='<strong>Just.</strong> Hace un momento, y va entre <em>have</em> y el participio. '
          '<em>Already</em> sería antes de lo esperado; <em>yet</em> solo funciona en '
          'negativas y preguntas.',

    bankLabel='Banco de palabras:',
    dndEyebrow='Actividad 3 · La combinación correcta', dndTitle='¿Qué expresión encaja?',
    dndHint='Veinticuatro expresiones, seis huecos. La mayoría no encaja en ninguno.',
    d1why='<strong>Sleep.</strong> Se <em>sleeps in</em> una cama. <em>Rest in</em> es '
          'inglés pero no fija el punto de reaparición: el juego solo cuenta dormir.',
    d2why='<strong>Rare.</strong> Cada cuánto aparece algo. <em>Uncommon</em> se acepta; '
          '<em>difficult</em> y <em>hard</em> describen el esfuerzo.',
    d3why='<strong>Take damage.</strong> Fijo: se <em>toma</em> daño, nunca se hace. Lo que '
          'lo causa es lo que lo produce.',
    d4why='<strong>Carry.</strong> Una antorcha se lleva en la mano, no puesta. <em>Wear</em> '
          'es para ropa y armadura.',
    d5why='<strong>Final boss.</strong> El término fijo del mundo del videojuego para el '
          'enemigo del final. <em>Hardest mob</em> y <em>last enemy</em> lo describen pero '
          'no son el término.',
    d6why='<strong>Eat.</strong> Simple y correcto. <em>Consume</em> se acepta pero suena a '
          'etiqueta nutricional.',

    matchEyebrow='Actividad 4 · El glosario', matchTitle='Relaciona el término con su significado',
    matchHint='Haz clic en un término y luego en lo que significa.',
    matchWhy='Las siete son palabras inglesas reales que en el juego hacen un trabajo. '
             '<em>Craft</em>, <em>mine</em> y <em>smelt</em> es lo que la gente hacía con los '
             'materiales mucho antes de que hubiera un juego; <em>mob</em>, <em>biome</em> e '
             '<em>inventory</em> vienen de la multitud, la geografía y el comercio. Conocer '
             'el sentido corriente es lo que permite usarlas fuera de Minecraft.',

    ordEyebrow='Actividad 5 · La primera noche', ordTitle='Ordena los siete pasos',
    ordHint='Haz clic en un paso para colocarlo; haz clic en uno colocado para retirarlo.',
    o1why='Apareces en un mundo nuevo, golpeas un árbol para sacar madera, fabricas un pico '
          'de madera, picas piedra y carbón, construyes un refugio antes de que oscurezca, '
          'lo iluminas con antorchas y duermes hasta la mañana. Cada paso existe por el '
          'anterior: sin madera no hay pico; sin pico no hay piedra; sin refugio y sin luz, '
          'los mobs aparecen justo donde estás. Esa dependencia es lo que lo convierte en un '
          'procedimiento y no en una lista, y es el molde para volver a contarlo con '
          '<em>first</em>, <em>then</em>, <em>after that</em> y <em>until</em>.',

    actTitle='Explica a alguien cómo sobrevivir', actUse='Usa al menos cuatro:',
    actSpeakBrief='Uno lleva años jugando; el otro no ha abierto el juego nunca. Tres '
                  'minutos cada uno, luego cambiad.',
    actSpeak1='Explica los diez primeros minutos de un mundo nuevo a alguien que no ha jugado nunca a nada.',
    actSpeak2='Di qué has estado haciendo últimamente en un juego y qué acabas de terminar.',
    actSpeak3='Describe tu rutina en un juego al que juegas: qué haces siempre y en qué orden.',
    actSpeak4='Avisa a tu compañero de tres peligros, usando <em>otherwise</em> cada vez.',
    actWriteKind='Escritura · 120–150 palabras',
    actWriteBrief='Escribe la guía de supervivencia que le darías a un amigo para su primera '
                  'noche. Di qué tiene que hacer y en qué orden, qué pasa si no, y qué has '
                  'aprendido tú jugando. Presente simple para las reglas y presente perfecto '
                  'para tu experiencia.',
    actPlaceholder='The first thing you have to do is…',

    resPerfect='Puntuación perfecta. Sabes contarlo y tienes las palabras que usa el juego.',
    resStrong='Muy bien. Repasa las combinaciones: en <em>take damage</em> y <em>carry a torch</em> se va el último punto.',
    resMid='Buena base. Vuelve a la primera diapositiva: las costumbres van en presente simple, y <em>for</em> lleva una duración.',
    resLow='Relee las tres diapositivas iniciales. Tres tiempos, tres funciones, y el resto es vocabulario.',
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
