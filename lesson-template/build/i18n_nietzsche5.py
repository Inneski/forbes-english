# -*- coding: utf-8 -*-
"""Interface strings for Nietzsche on Film — C1 Vocabulary, Part V.

English, German and Spanish. Teach-card bodies use the six-item form so the
rule travels with its heading. The English being taught — the terms, the
stems, the options — stays English throughout, which on a vocabulary deck is
most of the visible text.
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
    coverTitle='Nietzsche <em>on Film</em>',
    coverSub='The vocabulary of film criticism, and the C1 skill of choosing a word by its register rather than its meaning',
    chipLevel='C1 · Advanced', chipFocus='Film criticism vocabulary',
    chipCount='21 slides',

    termEyebrow='Before the questions', termTitle='Terms that only look like ordinary words',
    te1h='<em>Mise-en-scène</em> is not the camera', te1b=
        'It is everything composed <em>inside</em> the frame &mdash; set, light, '
        'costume, where the actors stand. <strong>Cinematography</strong> is the '
        'camera and the lighting technique; <strong>blocking</strong> is movement '
        'alone.',
    te1n='Three terms, three different jobs. Critics do not use them loosely.',
    te2h='Diegetic means inside the story', te2b=
        'A piano playing in the room is <strong>diegetic</strong>: the characters '
        'could hear it. A score is <strong>non-diegetic</strong>: only the audience '
        'can. The line is drawn by who can hear it, not by what it sounds like.',
    te2n='A radio a character switches on is diegetic. The same tune over the credits is not.',
    te3h='<em>Verisimilitude</em> is not realism', te3b=
        'Verisimilitude is seeming true <em>within the conventions of the work</em>. '
        'Realism names an artistic movement. <strong>Authenticity</strong> is a '
        'cultural claim; <strong>continuity</strong> is only consistency between '
        'shots.',
    te3n='A fantasy film can have high verisimilitude. It cannot be realist.',

    regEyebrow='The C1 move', regTitle='Four words, one meaning, four temperatures',
    re1h='The distractors are not wrong', re1b=
        'At C1 the wrong answer is rarely false. <em>Derivative</em>, '
        '<em>imitative</em>, <em>unoriginal</em> and <em>ersatz</em> all say a work '
        'copies. Only <strong>ersatz</strong> accuses it of pretending to be the real '
        'thing.',
    re1n='Read what the sentence is doing, not only what it means.',
    re2h='Register follows the document', re2b=
        'In a press release a director does not <em>bail out</em> or <em>quit</em>; '
        'she <strong>withdraws</strong>. The informal word is not a smaller version '
        'of the formal one &mdash; it carries a judgement the formal one refuses.',
    re2n='The right word in the wrong register is still the wrong word.',
    re3h='Praise has a scale too', re3b=
        '<em>Memorable</em> is unforgettable. <em>Outstanding</em> is very good. '
        '<strong>Definitive</strong> claims something narrower and larger: the '
        'version future performances will be measured against.',
    re3n='Ask what the critic is committing to, not how enthusiastic they sound.',

    formEyebrow='The mechanics', formTitle='Collocation, and the shape of a word',
    fo1h='Fixed phrases have no logic to appeal to', fo1b=
        'A studio <strong>greenlights</strong> a film; nothing else does. Funding '
        'arrives <strong>at the eleventh hour</strong>, never <em>in</em> or '
        '<em>on</em> it. These are learned whole or got wrong.',
    fo1n='<em>Authorised</em> and <em>permitted</em> are not wrong English. They are the wrong industry.',
    fo2h='Suffixes carry word class', fo2b=
        '<em>-al</em> and <em>-ment</em> tend to make nouns, <em>-ive</em> and '
        '<em>-ic</em> adjectives, <em>-ly</em> adverbs. <em>Evoke</em> becomes '
        '<strong>evocative</strong>, the way <em>demonstrate</em> becomes '
        '<em>demonstrative</em>.',
    fo2n='If the suffix does not exist (<em>evocational</em>), the word does not either.',
    fo3h='A nominalisation is not a gerund', fo3b=
        '<strong>Portrayal</strong> is the noun that formal criticism reaches for. '
        '<em>Portraying</em> is a verb doing a noun&rsquo;s work &mdash; possible, '
        'weaker; <em>portrait</em> is a different object altogether.',
    fo3n='Academic register prefers the derived noun. It is why this prose feels dense.',

    s1Eyebrow='Section 1 · Critical terminology', s1Title='The term the field would use',
    s2Eyebrow='Section 2 · Precise collocation', s2Title='The word that goes with this word',
    s3Eyebrow='Section 3 · Register and connotation', s3Title='Right meaning, wrong temperature',
    s4Eyebrow='Section 4 · Phrasal verbs and idiom', s4Title='What a professional would actually say',
    s5Eyebrow='Section 5 · Word formation', s5Title='The right shape of the right word',

    q1why='<strong>Mise-en-scène.</strong> Everything composed inside the frame as a '
          'whole: set, light, costume, placement. <em>Cinematography</em> is the '
          'camera work, <em>blocking</em> is movement planning, <em>production '
          'design</em> is the built environment alone.',
    q2why='<strong>Non-diegetic.</strong> A leitmotif tied to a character&rsquo;s '
          'memory exists for the audience, not inside the world &mdash; nobody on '
          'screen hears it. Diegetic sound is what the characters could hear.',
    q3why='<strong>Verisimilitude.</strong> The quality of seeming true within the '
          'work&rsquo;s own conventions, and the term criticism prefers. '
          '<em>Realism</em> names a movement; <em>authenticity</em> is a cultural '
          'claim; <em>continuity</em> is consistency between shots.',
    q4why='<strong>Greenlit.</strong> The industry&rsquo;s own verb for giving a film '
          'official approval to proceed. <em>Authorised</em>, <em>permitted</em> and '
          '<em>validated</em> are all possible English and all sound like a form, not '
          'a studio.',
    q5why='<strong>At.</strong> <em>At the eleventh hour</em> is fixed: the preposition '
          'never varies. It comes from the parable of labourers hired in the last hour '
          'of the day, and there is nothing to reason from &mdash; it is learned whole.',
    q6why='<strong>Unprecedented.</strong> The sentence supplies its own definition: no '
          'major studio <em>had taken that risk</em> before. <em>Groundbreaking</em> '
          'claims the decision opened new territory, which the stem does not say; '
          '<em>unparalleled</em> is about quality and <em>pioneering</em> is usually '
          'said of people.',
    q7why='<strong>Ersatz.</strong> A poor substitute that passes itself off as the '
          'real thing &mdash; the only one of the four that accuses. <em>Derivative</em> '
          'is softer, <em>imitative</em> merely descriptive, <em>unoriginal</em> the '
          'most everyday.',
    q8why='<strong>Withdraw.</strong> A press release is neutral and professional. '
          '<em>Walk away</em> implies principle, <em>bail out</em> implies abandonment, '
          '<em>quit</em> is blunt. All three say something the studio is not saying.',
    q9why='<strong>Definitive.</strong> The version that becomes the standard, and a '
          'claim about critical consensus rather than enthusiasm. <em>Memorable</em>, '
          '<em>outstanding</em> and <em>powerful</em> are all praise; none of them '
          'settles the question for everyone after.',
    q10why='<strong>Do away with.</strong> To abolish entirely, which is what losing key '
           'set pieces means. <em>Cut down on</em> is reduce, <em>put off</em> is '
           'postpone, and <em>get rid of</em> is right in meaning but too informal for '
           'this sentence.',
    q11why='<strong>Countenance.</strong> Formal: to permit or sanction. <em>Put up '
           'with</em> and <em>stand for</em> mean tolerate and sit lower in register; '
           '<em>go along with</em> means agree, which changes what the studio is '
           'refusing.',
    q12why='<strong>Eschewed.</strong> Deliberately abstained, usually on principle, and '
           'the word a director reaches for in a festival Q&amp;A. <em>Avoided</em> is '
           'neutral, <em>shunned</em> is emotional, and <em>refrained from</em> makes it '
           'self-restraint rather than artistic choice.',
    q13why='<strong>Portrayal.</strong> The nominalisation of <em>portray</em>, and what '
           'formal criticism uses. <em>Portraying</em> is a gerund and stylistically '
           'weaker; <em>portrait</em> is a likeness, not an act of representation; '
           '<em>portrayal&rsquo;s</em> is a possessive with nothing to possess.',
    q14why='<strong>Evocative.</strong> <em>-ive</em> makes an adjective from a verb, as '
           'in <em>demonstrate &rarr; demonstrative</em>. <em>Evocating</em> and '
           '<em>evocational</em> are not English words, and <em>evoked</em> would mean '
           'the motifs had been called up, not that they call things up.',
    q15why='<strong>Restrained.</strong> The <em>-ed</em> participle used as an adjective '
           'describes the quality of the performance. <em>Restraining</em> would mean it '
           'holds something else back; <em>restraint</em> is the noun and cannot modify '
           '<em>performance</em>; <em>restrictive</em> is a different root with a '
           'different meaning.',

    actTitle='Review the film', actUse='Use at least four:',
    actSpeakBrief='One of you has just seen the film and thinks it works; the other '
                  'reviews for a broadsheet and does not. Four minutes each, then swap.',
    actSpeak1='Describe one scene by its mise-en-scène, without saying &ldquo;good&rdquo; or &ldquo;beautiful&rdquo;.',
    actSpeak2='Criticise a performance you otherwise admired. Pick the word that carries exactly as much blame as you mean.',
    actSpeak3='Defend the non-diegetic score against the charge that it tells the audience what to feel.',
    actSpeak4='Say what the film gets right about Nietzsche and what it flattens &mdash; and hedge the second.',
    actWriteKind='Writing · 200–250 words',
    actWriteBrief='Write the review a quality newspaper would print. Praise one thing '
                  'precisely, object to one thing precisely, and let the register do the '
                  'work: no intensifiers, and no word chosen for being stronger rather '
                  'than right.',
    actPlaceholder='For all the assurance of its mise-en-scène, the film…',

    resPerfect='Full marks. You are choosing by register and precision, which is the whole test.',
    resStrong='Strong. Look again at the connotation section — that is where the last marks sit.',
    resMid='Good ground. Re-read the second teaching slide: at C1 the distractors are true, only colder or warmer than the sentence needs.',
    resLow='Work through the three opening slides again. Every wrong answer here is a real English word used in the wrong place.',
)

T['de'] = dict(
    coverTitle='Nietzsche <em>im Film</em>',
    coverSub='Das Vokabular der Filmkritik — und die C1-Fähigkeit, ein Wort nach seinem Register zu wählen, nicht nach seiner Bedeutung',
    chipLevel='C1 · Fortgeschritten', chipFocus='Vokabular der Filmkritik',
    chipCount='21 Folien',

    termEyebrow='Vor den Fragen', termTitle='Begriffe, die nur wie gewöhnliche Wörter aussehen',
    te1h='<em>Mise-en-scène</em> ist nicht die Kamera', te1b=
        'Es ist alles, was <em>im</em> Bild komponiert ist &mdash; Bühnenbild, Licht, '
        'Kostüm, Position der Darsteller. <strong>Cinematography</strong> ist Kamera '
        'und Lichttechnik, <strong>blocking</strong> allein die Bewegung.',
    te1n='Drei Begriffe, drei verschiedene Aufgaben. Die Kritik benutzt sie nicht beliebig.',
    te2h='Diegetisch heißt: in der Geschichte', te2b=
        'Ein Klavier, das im Raum spielt, ist <strong>diegetic</strong>: Die Figuren '
        'könnten es hören. Eine Filmmusik ist <strong>non-diegetic</strong>: nur das '
        'Publikum hört sie. Entscheidend ist, wer hört, nicht wie es klingt.',
    te2n='Ein Radio, das eine Figur einschaltet, ist diegetisch. Dieselbe Melodie im Abspann nicht.',
    te3h='<em>Verisimilitude</em> ist nicht Realismus', te3b=
        'Verisimilitude heißt: wahr wirken <em>innerhalb der Konventionen des '
        'Werks</em>. Realismus benennt eine Kunstrichtung. <strong>Authenticity</strong> '
        'ist ein kultureller Anspruch, <strong>continuity</strong> nur Anschluss '
        'zwischen Einstellungen.',
    te3n='Ein Fantasyfilm kann hohe Verisimilitude haben. Realistisch kann er nicht sein.',

    regEyebrow='Der C1-Schritt', regTitle='Vier Wörter, eine Bedeutung, vier Temperaturen',
    re1h='Die Distraktoren sind nicht falsch', re1b=
        'Auf C1 ist die falsche Antwort selten unwahr. <em>Derivative</em>, '
        '<em>imitative</em>, <em>unoriginal</em> und <em>ersatz</em> sagen alle, dass '
        'ein Werk abschreibt. Nur <strong>ersatz</strong> wirft ihm vor, sich als das '
        'Echte auszugeben.',
    re1n='Lies, was der Satz tut, nicht nur, was er bedeutet.',
    re2h='Das Register folgt der Textsorte', re2b=
        'In einer Pressemitteilung macht eine Regisseurin keinen Rückzieher und '
        '<em>quits</em> nicht; sie <strong>withdraws</strong>. Das informelle Wort ist '
        'keine kleinere Fassung des formellen &mdash; es enthält ein Urteil, das das '
        'formelle verweigert.',
    re2n='Das richtige Wort im falschen Register ist immer noch das falsche Wort.',
    re3h='Auch Lob hat eine Skala', re3b=
        '<em>Memorable</em> heißt unvergesslich, <em>outstanding</em> sehr gut. '
        '<strong>Definitive</strong> behauptet etwas Engeres und Größeres: die Fassung, '
        'an der sich künftige messen lassen müssen.',
    re3n='Frag, worauf die Kritik sich festlegt, nicht wie begeistert sie klingt.',

    formEyebrow='Die Mechanik', formTitle='Kollokation und die Form eines Wortes',
    fo1h='Feste Wendungen kennen keine Logik', fo1b=
        'Ein Studio <strong>greenlights</strong> einen Film; sonst niemand. Geld kommt '
        '<strong>at the eleventh hour</strong>, nie <em>in</em> oder <em>on</em>. Das '
        'lernt man als Ganzes oder macht es falsch.',
    fo1n='<em>Authorised</em> und <em>permitted</em> sind kein falsches Englisch. Es ist die falsche Branche.',
    fo2h='Suffixe tragen die Wortart', fo2b=
        '<em>-al</em> und <em>-ment</em> bilden meist Substantive, <em>-ive</em> und '
        '<em>-ic</em> Adjektive, <em>-ly</em> Adverbien. Aus <em>evoke</em> wird '
        '<strong>evocative</strong>, wie aus <em>demonstrate</em> '
        '<em>demonstrative</em>.',
    fo2n='Gibt es das Suffix nicht (<em>evocational</em>), dann das Wort auch nicht.',
    fo3h='Eine Nominalisierung ist kein Gerundium', fo3b=
        '<strong>Portrayal</strong> ist das Substantiv, zu dem die formelle Kritik '
        'greift. <em>Portraying</em> ist ein Verb in der Rolle eines Substantivs '
        '&mdash; möglich, schwächer; <em>portrait</em> ist etwas ganz anderes.',
    fo3n='Das akademische Register bevorzugt das abgeleitete Substantiv. Daher wirkt diese Prosa so dicht.',

    s1Eyebrow='Abschnitt 1 · Fachbegriffe der Kritik', s1Title='Der Begriff, den das Fach benutzt',
    s2Eyebrow='Abschnitt 2 · Genaue Kollokation', s2Title='Das Wort, das zu diesem Wort gehört',
    s3Eyebrow='Abschnitt 3 · Register und Konnotation', s3Title='Richtige Bedeutung, falsche Temperatur',
    s4Eyebrow='Abschnitt 4 · Phrasal Verbs und Idiome', s4Title='Was ein Profi tatsächlich sagen würde',
    s5Eyebrow='Abschnitt 5 · Wortbildung', s5Title='Die richtige Form des richtigen Wortes',

    q1why='<strong>Mise-en-scène.</strong> Alles, was im Bild als Ganzes komponiert ist: '
          'Bühnenbild, Licht, Kostüm, Position. <em>Cinematography</em> ist die '
          'Kameraarbeit, <em>blocking</em> die Bewegungsplanung, <em>production '
          'design</em> nur die gebaute Umgebung.',
    q2why='<strong>Non-diegetic.</strong> Ein Leitmotiv, das an die Erinnerung einer '
          'Figur gebunden ist, existiert für das Publikum, nicht in der Welt &mdash; '
          'niemand auf der Leinwand hört es.',
    q3why='<strong>Verisimilitude.</strong> Innerhalb der eigenen Konventionen wahr '
          'wirken, und der Begriff, den die Kritik bevorzugt. <em>Realism</em> benennt '
          'eine Richtung, <em>authenticity</em> ist ein kultureller Anspruch, '
          '<em>continuity</em> der Anschluss zwischen Einstellungen.',
    q4why='<strong>Greenlit.</strong> Das branchen­eigene Verb dafür, dass ein Film '
          'offiziell losgehen darf. <em>Authorised</em>, <em>permitted</em> und '
          '<em>validated</em> sind mögliches Englisch und klingen nach Formular, nicht '
          'nach Studio.',
    q5why='<strong>At.</strong> <em>At the eleventh hour</em> ist fest: Die Präposition '
          'wechselt nie. Sie stammt aus dem Gleichnis von den Arbeitern der letzten '
          'Stunde &mdash; hier gibt es nichts abzuleiten.',
    q6why='<strong>Unprecedented.</strong> Der Satz liefert seine eigene Definition: '
          'Kein großes Studio <em>hatte dieses Risiko</em> je auf sich genommen. '
          '<em>Groundbreaking</em> behauptet, die Entscheidung habe Neuland eröffnet, '
          'was der Satz nicht sagt; <em>unparalleled</em> betrifft Qualität, '
          '<em>pioneering</em> sagt man meist über Personen.',
    q7why='<strong>Ersatz.</strong> Ein schlechter Ersatz, der sich als das Echte '
          'ausgibt &mdash; das einzige der vier, das einen Vorwurf enthält. '
          '<em>Derivative</em> ist milder, <em>imitative</em> beschreibend, '
          '<em>unoriginal</em> am alltäglichsten.',
    q8why='<strong>Withdraw.</strong> Eine Pressemitteilung ist neutral und '
          'professionell. <em>Walk away</em> unterstellt Prinzipien, <em>bail out</em> '
          'Fahnenflucht, <em>quit</em> ist schroff &mdash; alle drei sagen etwas, das '
          'das Studio nicht sagt.',
    q9why='<strong>Definitive.</strong> Die Fassung, die zum Maßstab wird, und damit '
          'eine Aussage über den Konsens der Kritik, nicht über Begeisterung. '
          '<em>Memorable</em>, <em>outstanding</em> und <em>powerful</em> sind alle Lob '
          'und entscheiden nichts für die Nachwelt.',
    q10why='<strong>Do away with.</strong> Ganz abschaffen &mdash; und genau das heißt '
           'es, zentrale Szenenbauten zu verlieren. <em>Cut down on</em> ist reduzieren, '
           '<em>put off</em> verschieben, <em>get rid of</em> trifft die Bedeutung, ist '
           'aber zu informell.',
    q11why='<strong>Countenance.</strong> Formell: zulassen, gutheißen. <em>Put up '
           'with</em> und <em>stand for</em> heißen dulden und stehen tiefer im '
           'Register; <em>go along with</em> heißt zustimmen und ändert, was das Studio '
           'ablehnt.',
    q12why='<strong>Eschewed.</strong> Bewusst verzichtet, meist aus Prinzip &mdash; das '
           'Wort für ein Festival-Q&amp;A. <em>Avoided</em> ist neutral, <em>shunned</em> '
           'emotional, <em>refrained from</em> macht daraus Selbstbeherrschung statt '
           'künstlerischer Entscheidung.',
    q13why='<strong>Portrayal.</strong> Die Nominalisierung von <em>portray</em>, und was '
           'die formelle Kritik benutzt. <em>Portraying</em> ist ein Gerundium und '
           'stilistisch schwächer, <em>portrait</em> ein Bildnis, '
           '<em>portrayal&rsquo;s</em> ein Genitiv ohne Bezug.',
    q14why='<strong>Evocative.</strong> <em>-ive</em> bildet aus einem Verb ein Adjektiv, '
           'wie <em>demonstrate &rarr; demonstrative</em>. <em>Evocating</em> und '
           '<em>evocational</em> gibt es nicht, und <em>evoked</em> hieße, die Motive '
           'seien hervorgerufen worden, nicht dass sie etwas hervorrufen.',
    q15why='<strong>Restrained.</strong> Das <em>-ed</em>-Partizip als Adjektiv '
           'beschreibt die Qualität der Darstellung. <em>Restraining</em> hieße, sie '
           'halte etwas anderes zurück; <em>restraint</em> ist das Substantiv und kann '
           '<em>performance</em> nicht näher bestimmen; <em>restrictive</em> hat eine '
           'andere Wurzel.',

    actTitle='Besprich den Film', actUse='Benutze mindestens vier:',
    actSpeakBrief='Einer hat den Film gerade gesehen und findet, er funktioniert; die '
                  'andere schreibt für eine überregionale Zeitung und findet das nicht. '
                  'Je vier Minuten, dann tauschen.',
    actSpeak1='Beschreibe eine Szene über ihre Mise-en-scène, ohne &bdquo;gut&ldquo; oder &bdquo;schön&ldquo;.',
    actSpeak2='Kritisiere eine Darstellung, die du sonst bewundert hast. Wähl das Wort mit genau so viel Vorwurf, wie du meinst.',
    actSpeak3='Verteidige die nicht-diegetische Musik gegen den Vorwurf, sie sage dem Publikum, was es fühlen soll.',
    actSpeak4='Sag, was der Film an Nietzsche richtig trifft und was er einebnet — und schwäche das Zweite ab.',
    actWriteKind='Schreiben · 200–250 Wörter',
    actWriteBrief='Schreibe die Kritik, die eine Qualitätszeitung drucken würde. Lobe '
                  'eine Sache präzise, wende eine präzise ein, und lass das Register die '
                  'Arbeit tun: keine Verstärker und kein Wort, das nur stärker ist statt '
                  'richtig.',
    actPlaceholder='For all the assurance of its mise-en-scène, the film…',

    resPerfect='Volle Punktzahl. Du wählst nach Register und Präzision — genau darum geht es hier.',
    resStrong='Stark. Sieh dir den Abschnitt zur Konnotation noch einmal an; dort liegen die letzten Punkte.',
    resMid='Gute Grundlage. Lies die zweite Lehrfolie noch einmal: Auf C1 sind die Distraktoren wahr, nur kälter oder wärmer als der Satz es braucht.',
    resLow='Arbeite die drei Einstiegsfolien noch einmal durch. Jede falsche Antwort hier ist ein echtes englisches Wort an der falschen Stelle.',
)

T['es'] = dict(
    coverTitle='Nietzsche <em>en el cine</em>',
    coverSub='El vocabulario de la crítica de cine y la destreza C1 de elegir una palabra por su registro y no por su significado',
    chipLevel='C1 · Avanzado', chipFocus='Vocabulario de crítica de cine',
    chipCount='21 diapositivas',

    termEyebrow='Antes de las preguntas', termTitle='Términos que solo parecen palabras corrientes',
    te1h='<em>Mise-en-scène</em> no es la cámara', te1b=
        'Es todo lo compuesto <em>dentro</em> del encuadre: decorado, luz, vestuario, '
        'dónde se colocan los actores. <strong>Cinematography</strong> es el trabajo de '
        'cámara y la iluminación; <strong>blocking</strong>, solo el movimiento.',
    te1n='Tres términos, tres funciones distintas. La crítica no los usa a la ligera.',
    te2h='Diegético significa dentro de la historia', te2b=
        'Un piano que suena en la habitación es <strong>diegetic</strong>: los '
        'personajes podrían oírlo. Una banda sonora es <strong>non-diegetic</strong>: '
        'solo la oye el público. La línea la traza quién puede oírlo, no cómo suena.',
    te2n='Una radio que enciende un personaje es diegética. La misma melodía en los créditos, no.',
    te3h='<em>Verisimilitude</em> no es realismo', te3b=
        'Verisimilitude es parecer verdadero <em>dentro de las convenciones de la '
        'obra</em>. El realismo nombra un movimiento artístico. '
        '<strong>Authenticity</strong> es una reivindicación cultural; '
        '<strong>continuity</strong>, solo la coherencia entre planos.',
    te3n='Una película fantástica puede tener mucha verisimilitude. Realista no puede ser.',

    regEyebrow='El movimiento de C1', regTitle='Cuatro palabras, un significado, cuatro temperaturas',
    re1h='Los distractores no son falsos', re1b=
        'En C1 la respuesta incorrecta rara vez es falsa. <em>Derivative</em>, '
        '<em>imitative</em>, <em>unoriginal</em> y <em>ersatz</em> dicen todas que una '
        'obra copia. Solo <strong>ersatz</strong> la acusa de hacerse pasar por la '
        'auténtica.',
    re1n='Lee lo que hace la frase, no solo lo que significa.',
    re2h='El registro sigue al documento', re2b=
        'En una nota de prensa una directora no <em>bails out</em> ni <em>quits</em>; '
        '<strong>withdraws</strong>. La palabra informal no es una versión menor de la '
        'formal &mdash; lleva un juicio que la formal se niega a emitir.',
    re2n='La palabra correcta en el registro equivocado sigue siendo la palabra equivocada.',
    re3h='El elogio también tiene escala', re3b=
        '<em>Memorable</em> es inolvidable. <em>Outstanding</em> es muy bueno. '
        '<strong>Definitive</strong> afirma algo más estrecho y más grande: la versión '
        'con la que se medirán las siguientes.',
    re3n='Pregunta a qué se compromete la crítica, no cuánto entusiasmo aparenta.',

    formEyebrow='La mecánica', formTitle='Colocación y la forma de la palabra',
    fo1h='Las frases fijas no admiten razonamiento', fo1b=
        'Un estudio <strong>greenlights</strong> una película; nadie más. La '
        'financiación llega <strong>at the eleventh hour</strong>, nunca <em>in</em> ni '
        '<em>on</em>. Se aprenden enteras o se dicen mal.',
    fo1n='<em>Authorised</em> y <em>permitted</em> no son inglés incorrecto. Son el sector equivocado.',
    fo2h='Los sufijos llevan la categoría', fo2b=
        '<em>-al</em> y <em>-ment</em> suelen formar sustantivos; <em>-ive</em> e '
        '<em>-ic</em>, adjetivos; <em>-ly</em>, adverbios. De <em>evoke</em> sale '
        '<strong>evocative</strong>, igual que de <em>demonstrate</em> sale '
        '<em>demonstrative</em>.',
    fo2n='Si el sufijo no existe (<em>evocational</em>), la palabra tampoco.',
    fo3h='Una nominalización no es un gerundio', fo3b=
        '<strong>Portrayal</strong> es el sustantivo al que acude la crítica formal. '
        '<em>Portraying</em> es un verbo haciendo el trabajo de un sustantivo &mdash; '
        'posible, más débil; <em>portrait</em> es otra cosa distinta.',
    fo3n='El registro académico prefiere el sustantivo derivado. Por eso esta prosa resulta densa.',

    s1Eyebrow='Sección 1 · Terminología crítica', s1Title='El término que usaría el campo',
    s2Eyebrow='Sección 2 · Colocación precisa', s2Title='La palabra que acompaña a esta palabra',
    s3Eyebrow='Sección 3 · Registro y connotación', s3Title='Significado correcto, temperatura equivocada',
    s4Eyebrow='Sección 4 · Phrasal verbs y modismos', s4Title='Lo que diría de verdad un profesional',
    s5Eyebrow='Sección 5 · Formación de palabras', s5Title='La forma correcta de la palabra correcta',

    q1why='<strong>Mise-en-scène.</strong> Todo lo compuesto dentro del encuadre como '
          'conjunto: decorado, luz, vestuario, colocación. <em>Cinematography</em> es el '
          'trabajo de cámara, <em>blocking</em> la planificación del movimiento, '
          '<em>production design</em> solo el entorno construido.',
    q2why='<strong>Non-diegetic.</strong> Un leitmotiv ligado al recuerdo de un personaje '
          'existe para el público, no dentro del mundo &mdash; nadie en pantalla lo oye.',
    q3why='<strong>Verisimilitude.</strong> Parecer verdadero dentro de las convenciones '
          'de la propia obra, y el término que prefiere la crítica. <em>Realism</em> '
          'nombra un movimiento; <em>authenticity</em> es una reivindicación cultural; '
          '<em>continuity</em> es coherencia entre planos.',
    q4why='<strong>Greenlit.</strong> El verbo propio del sector para dar luz verde '
          'oficial a una película. <em>Authorised</em>, <em>permitted</em> y '
          '<em>validated</em> son inglés posible y suenan a impreso, no a estudio.',
    q5why='<strong>At.</strong> <em>At the eleventh hour</em> es fija: la preposición no '
          'varía nunca. Viene de la parábola de los jornaleros contratados en la última '
          'hora, y no hay nada que deducir.',
    q6why='<strong>Unprecedented.</strong> La frase da su propia definición: ningún gran '
          'estudio <em>había corrido ese riesgo</em>. <em>Groundbreaking</em> afirma que '
          'la decisión abrió terreno nuevo, cosa que la frase no dice; '
          '<em>unparalleled</em> habla de calidad y <em>pioneering</em> suele decirse de '
          'personas.',
    q7why='<strong>Ersatz.</strong> Un sustituto pobre que se hace pasar por lo auténtico '
          '&mdash; la única de las cuatro que acusa. <em>Derivative</em> es más suave, '
          '<em>imitative</em> meramente descriptiva, <em>unoriginal</em> la más '
          'cotidiana.',
    q8why='<strong>Withdraw.</strong> Una nota de prensa es neutra y profesional. '
          '<em>Walk away</em> insinúa principios, <em>bail out</em> abandono, '
          '<em>quit</em> es brusco: las tres dicen algo que el estudio no dice.',
    q9why='<strong>Definitive.</strong> La versión que se convierte en el patrón, y por '
          'tanto una afirmación sobre el consenso crítico, no sobre el entusiasmo. '
          '<em>Memorable</em>, <em>outstanding</em> y <em>powerful</em> son elogios y no '
          'zanjan nada.',
    q10why='<strong>Do away with.</strong> Suprimir por completo, que es lo que significa '
           'perder decorados clave. <em>Cut down on</em> es reducir, <em>put off</em> '
           'aplazar, y <em>get rid of</em> acierta en el sentido pero es demasiado '
           'informal aquí.',
    q11why='<strong>Countenance.</strong> Formal: permitir o sancionar. <em>Put up '
           'with</em> y <em>stand for</em> significan tolerar y bajan de registro; '
           '<em>go along with</em> es aceptar, lo que cambia qué está rechazando el '
           'estudio.',
    q12why='<strong>Eschewed.</strong> Se abstuvo deliberadamente, casi siempre por '
           'principio, y es la palabra para un coloquio de festival. <em>Avoided</em> es '
           'neutra, <em>shunned</em> emocional, y <em>refrained from</em> lo convierte en '
           'autocontrol en vez de decisión artística.',
    q13why='<strong>Portrayal.</strong> La nominalización de <em>portray</em>, y lo que '
           'usa la crítica formal. <em>Portraying</em> es un gerundio y estilísticamente '
           'más débil; <em>portrait</em> es un retrato, no un acto de representación; '
           '<em>portrayal&rsquo;s</em> es un posesivo sin nada que poseer.',
    q14why='<strong>Evocative.</strong> <em>-ive</em> forma un adjetivo a partir de un '
           'verbo, como <em>demonstrate &rarr; demonstrative</em>. <em>Evocating</em> y '
           '<em>evocational</em> no existen, y <em>evoked</em> significaría que los '
           'motivos han sido evocados, no que evocan.',
    q15why='<strong>Restrained.</strong> El participio en <em>-ed</em> usado como '
           'adjetivo describe la cualidad de la interpretación. <em>Restraining</em> '
           'querría decir que sujeta otra cosa; <em>restraint</em> es el sustantivo y no '
           'puede modificar a <em>performance</em>; <em>restrictive</em> viene de otra '
           'raíz.',

    actTitle='Reseña la película', actUse='Usa al menos cuatro:',
    actSpeakBrief='Uno acaba de ver la película y cree que funciona; el otro escribe '
                  'críticas para un diario y no lo cree. Cuatro minutos cada uno, luego '
                  'cambiad.',
    actSpeak1='Describe una escena por su mise-en-scène, sin decir &ldquo;buena&rdquo; ni &ldquo;bonita&rdquo;.',
    actSpeak2='Critica una interpretación que por lo demás admiraste. Elige la palabra con el reproche exacto que quieres.',
    actSpeak3='Defiende la música no diegética frente a la acusación de que le dice al público qué sentir.',
    actSpeak4='Di qué acierta la película sobre Nietzsche y qué aplana — y matiza lo segundo.',
    actWriteKind='Escritura · 200–250 palabras',
    actWriteBrief='Escribe la crítica que publicaría un diario de calidad. Elogia una '
                  'cosa con precisión, objeta una con precisión y deja que el registro '
                  'haga el trabajo: sin intensificadores y sin palabras elegidas por ser '
                  'más fuertes en vez de justas.',
    actPlaceholder='For all the assurance of its mise-en-scène, the film…',

    resPerfect='Puntuación perfecta. Eliges por registro y precisión, que es de lo que va toda la prueba.',
    resStrong='Muy bien. Vuelve a mirar la sección de connotación: ahí están los últimos puntos.',
    resMid='Buena base. Relee la segunda diapositiva de teoría: en C1 los distractores son ciertos, solo más fríos o más cálidos de lo que pide la frase.',
    resLow='Vuelve a trabajar las tres diapositivas iniciales. Cada respuesta incorrecta de aquí es una palabra inglesa real en el sitio equivocado.',
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
