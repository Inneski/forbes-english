# -*- coding: utf-8 -*-
"""Interface strings for Head to Toe (C1) — EN, DE and ES.

English, German and Spanish are the site minimum (HOUSE-STYLE §8, CLAUDE.md's
standing constraint of 2026-09-04). The remaining languages stay as {} and are
therefore not offered; partial is a failure, empty is an honest placeholder.

The scope boundary on a vocabulary deck, drawn where §8 draws it:

  * **Translated** — the cover, the stage eyebrows and titles, the divider
    captions, every task hint, the body and note of both teaching cards, the
    MC context lines and stems, the sort bins, the activation briefs and the
    result bands. All of it scaffolding around the language.

  * **Not translated** — the thirty-six words themselves, their definitions,
    the gap sentences, the word banks, the sort items, the order chunks, the
    MC options and the activation chips. That is the English under test.

One deliberate exception, and it is the reason the old lesson's German is not
lost. `m1Why`…`m6Why` are the feedback lines under each matching round, and in
German and Spanish they carry the **glossary** — *forehead = Stirn = frente* —
which is exactly what the 2026-08 scrolling version showed after a correct
match. deck.match refuses to gloss the term itself (it would turn matching
into reading off), so the equivalents ride in the feedback instead, where they
arrive after the learner has already had to recall the word. The English
version of the same key is a usage note, because a translation into English is
of no use to someone reading the deck in English.

Gap-row and MC explanations are written as sentences rather than keys, so they
stay English in every language: they are notes about English usage, and that
is how most of the library writes them (HOUSE-STYLE §7).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel',
        'slideOf', 'fbCorrect', 'fbWrong', 'fbAnswer', 'btnCopy', 'btnCopied',
        'wordCount', 'btnOpen', 'actEyebrow']

TAIL = {
    'en': {'branchLocked': "'Your ledger does not support this ending'",
           'glossHide': "'Hide'",
           'glossShow': "'Translate'",
           'ledClues': "'Clues'",
           'ledDp': "'DP'",
           'ledTime': "'Time'"},
    'de': {'branchLocked': "'Dein Protokoll trägt dieses Ende nicht'",
           'glossHide': "'Ausblenden'",
           'glossShow': "'Übersetzen'",
           'ledClues': "'Hinweise'",
           'ledDp': "'DP'",
           'ledTime': "'Zeit'"},
    'es': {'branchLocked': "'Tu registro no admite este final'",
           'glossHide': "'Ocultar'",
           'glossShow': "'Traducir'",
           'ledClues': "'Pistas'",
           'ledDp': "'DP'",
           'ledTime': "'Tiempo'"},
}

T = {}

# ── ENGLISH ────────────────────────────────────────────────────────────
T['en'] = dict(
    coverTitle='Head to <em>Toe</em>',
    coverSub='Thirty-six words for the human body &mdash; and the precision to say which one hurts',
    chipLevel='C1 &middot; Vocabulary',
    chipFocus='Naming the body, inside and out',
    chipCount='NSLIDES slides',

    # ── stage 1 ──
    s1Eyebrow='Stage one &middot; above the collarbone',
    d1Title='Above the collarbone',
    d1Note='Twelve words',
    m1Title='The upper face',
    m1Hint='Six words, six definitions. Click a word, then the definition that fits it.',
    m1Why='All six sit above the eye line. <em>Eyelash</em> and <em>eyebrow</em> are '
          'countable and usually plural in use &mdash; <em>her eyelashes</em>, '
          '<em>he raised his eyebrows</em> &mdash; while the lobe is the only soft part of the ear.',
    m2Title='The lower face, and the neck',
    m2Hint='Six more. Two of them name the same region from outside and from inside.',
    m2Why='<em>Neck</em> is the outside, <em>throat</em> the passage within it: a stiff neck '
          'and a sore throat are different complaints. The <em>jaw</em> is the hinge, the '
          '<em>chin</em> the point at the front of it.',

    # ── stage 2 ──
    s2Eyebrow='Stage two &middot; the trunk, opened',
    d2Title='The trunk, opened',
    d2Note='Twelve words',
    m3Title='The frame',
    m3Hint='Bone and outline first: what holds the trunk up and gives it a shape.',
    m3Why='<em>Rib</em> and <em>vertebra</em> are countable, <em>spine</em> and '
          '<em>pelvis</em> are single structures. Note that <em>hip</em> names the joint '
          'and the width of the body at that point, which is why trousers have a hip measurement.',
    m4Title='What is inside it',
    m4Hint='Five organs and one kind of vessel. Say them singular or plural as the definition does.',
    m4Why='<em>Intestines</em> is normally plural, <em>stomach</em> singular. In everyday '
          'English <em>my stomach hurts</em> covers the whole abdomen, not only the organ &mdash; '
          'a doctor would ask you to point.',

    # ── stage 3 ──
    s3Eyebrow='Stage three &middot; arm, hand, leg, foot',
    d3Title='Arm, hand, leg, foot',
    d3Note='Twelve words',
    m5Title='The arm and the hand',
    m5Hint='Six words from the shoulder down to the fingers.',
    m5Why='The <em>thumb</em> is not called a finger in English: <em>four fingers and a '
          'thumb</em>. <em>Knuckle</em> is any joint in a finger, and the ones that show on '
          'a fist are simply the biggest.',
    m6Title='The leg and the foot',
    m6Hint='Six words from the hip down to the ground.',
    m6Why='<em>Shin</em> is the hard front edge, <em>calf</em> the muscle behind it &mdash; '
          'you bark your shin on a table and pull your calf running. <em>Sole</em> is the '
          'underside of the foot and of the shoe on it.',

    # ── teaching ──
    t1Eyebrow='Two words, one place',
    t1Title='Where English splits what other languages join',
    t1b1='The neck is the outside &mdash; you turn it, you wear a scarf on it. The throat is the passage inside, where swallowing happens.',
    t1n1='<em>A sore throat</em>, but <em>a stiff neck</em>. Never the other way round.',
    t1b2='The jaw is the hinged bone that opens and shuts the mouth. The chin is only the point at the front of it.',
    t1n2='<em>His jaw dropped.</em> &middot; <em>She rested her chin on her hand.</em>',
    t1b3='The forehead is the flat front above the eyebrows; the temples are the two flat sides, just behind the eyes.',
    t1n3='A headache sits in the temples. Worry shows on the forehead.',

    t2Eyebrow='Joints, muscle, bone',
    t2Title='What you sprain, pull and break',
    t2b1='Elbow, wrist, knuckle, ankle and hip are joints: places where two bones meet and move.',
    t2n1='You <em>sprain</em> a joint, <em>pull</em> a muscle and <em>break</em> a bone.',
    t2b2='Shin and calf are the two halves of the lower leg &mdash; hard edge in front, soft muscle behind.',
    t2n2='<em>I barked my shin.</em> &middot; <em>I pulled a calf muscle.</em>',
    t2b3='Palm and sole are the two flat undersides: one on the hand, one on the foot.',
    t2n3='A shoe has a sole too, and it is the same word for the same reason.',

    # ── sort ──
    sortEyebrow='Everything you have met so far',
    sortTitle='Bone, organ, or joint?',
    sortHint='Thirteen parts, three kinds. Drop each one where it belongs.',
    sortBin1='Bone',
    sortBin2='Organ',
    sortBin3='Joint',
    sortWhy='A joint is a meeting place, not a part &mdash; which is why you sprain one '
            'rather than break it. The five organs here are the ones a doctor can refer to '
            'by name in ordinary conversation.',

    # ── order ──
    ordEyebrow='The whole body, in one line',
    ordTitle='Top to bottom',
    ordHint='Eight parts. Put them in order, starting at the top of the head.',
    ordWhy='Forehead, jaw, throat, chest, waist, thigh, shin, heel &mdash; the order a '
           'doctor works down in, and the order this deck taught them in.',

    # ── multiple choice ──
    qEyebrow='Say which one',
    qTitle='One word does the job',
    q1Ctx='You have been on a plane for six hours and the back of your lower leg is aching.',
    q1Stem='Which part is aching?',
    q2Ctx='It hurts inside when you swallow, and your voice has almost gone.',
    q2Stem='What is sore?',
    q3Ctx='A watch goes here. A ring will not fit.',
    q3Stem='Which joint is it?',
    q4Ctx='Three of these four are places where two bones meet and move.',
    q4Stem='Which one is not a joint?',
    q5Ctx='The doctor says the trouble is in the large organ tucked under the ribs on your right.',
    q5Stem='Which organ is that?',

    # ── gap fill ──
    gapEyebrow='At the doctor&rsquo;s',
    bankLabel='Word bank:',
    g1Title='Where does it hurt?',
    g1Hint='One word per gap. The bank holds three words you will not need.',
    g2Title='And what happened?',
    g2Hint='Same again. Say the part, not the place you were standing.',

    # ── results and activation ──
    resNext='Recognising the word is the easy half. Now say where it hurts &rarr;',
    resPerfect='Every one. You can name this body inside and out.',
    resStrong='Strong. Check the misses &mdash; most of them are a pair this deck warned you about.',
    resMid='A usable base. Go back to the two teaching slides before you speak.',
    resLow='Work through the three charts again, slowly, then run it a second time.',

    actTitle='Now say where it hurts',
    actUse='Use at least four:',
    actSpeakKind='Discussion &middot; in pairs',
    actSpeakBrief='Ten minutes, then swap. One of you is at the doctor&rsquo;s; the other is the doctor, and asks where exactly, how long, and how bad.',
    actSpeak1='You came off a bike three days ago. Describe everything that hurts, working down from the head. Words only &mdash; no pointing.',
    actSpeak2='You are the doctor. Make your patient say whether the pain is inside or outside, and whether it is bone, muscle or joint.',
    actSpeak3='Describe somebody in the room without naming them. Three parts of the body, no clothes and no hair.',
    actSpeak4='Your partner mimes an injury. Name the part and what they did to it before the mime finishes.',
    actWriteKind='Writing &middot; 150&ndash;200 words',
    actWriteBrief='Write the message you send your insurer after a fall on the stairs. What you landed on, which parts took the impact, what you can and cannot move now, and what the doctor said. No diagram &mdash; the words have to carry it.',
    actPlaceholder='I slipped on the third step from the bottom and landed on…',
)

# ── GERMAN ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Head to <em>Toe</em>',
    coverSub='Sechsunddrei&szlig;ig Wörter für den menschlichen Körper &mdash; und die Präzision zu sagen, welches davon wehtut',
    chipLevel='C1 &middot; Wortschatz',
    chipFocus='Den Körper benennen, innen wie au&szlig;en',
    chipCount='NSLIDES Folien',

    s1Eyebrow='Etappe eins &middot; oberhalb des Schlüsselbeins',
    d1Title='Oberhalb des Schlüsselbeins',
    d1Note='Zwölf Wörter',
    m1Title='Das obere Gesicht',
    m1Hint='Sechs Wörter, sechs Definitionen. Klicke ein Wort an, dann die passende Definition.',
    m1Why='forehead = die Stirn &middot; temple = die Schläfe &middot; eyebrow = die Augenbraue '
          '&middot; eyelash = die Wimper &middot; nostril = das Nasenloch &middot; '
          'earlobe = das Ohrläppchen',
    m2Title='Das untere Gesicht und der Hals',
    m2Hint='Sechs weitere. Zwei davon benennen dieselbe Region &mdash; einmal von au&szlig;en, einmal von innen.',
    m2Why='cheek = die Wange &middot; lip = die Lippe &middot; chin = das Kinn &middot; '
          'jaw = der Kiefer &middot; throat = die Kehle (innen) &middot; neck = der Hals (au&szlig;en)',

    s2Eyebrow='Etappe zwei &middot; der Rumpf, geöffnet',
    d2Title='Der Rumpf, geöffnet',
    d2Note='Zwölf Wörter',
    m3Title='Das Gerüst',
    m3Hint='Zuerst Knochen und Umriss: was den Rumpf trägt und ihm seine Form gibt.',
    m3Why='chest = die Brust &middot; waist = die Taille &middot; hip = die Hüfte &middot; '
          'pelvis = das Becken &middot; spine = die Wirbelsäule &middot; rib = die Rippe',
    m4Title='Was darin liegt',
    m4Hint='Fünf Organe und eine Art von Gefä&szlig;. Singular oder Plural, so wie die Definition es sagt.',
    m4Why='stomach = der Magen &middot; lung = die Lunge &middot; liver = die Leber &middot; '
          'kidney = die Niere &middot; intestines = der Darm &middot; veins = die Venen',

    s3Eyebrow='Etappe drei &middot; Arm, Hand, Bein, Fu&szlig;',
    d3Title='Arm, Hand, Bein, Fu&szlig;',
    d3Note='Zwölf Wörter',
    m5Title='Arm und Hand',
    m5Hint='Sechs Wörter von der Schulter bis zu den Fingern.',
    m5Why='armpit = die Achselhöhle &middot; elbow = der Ellbogen &middot; wrist = das Handgelenk '
          '&middot; palm = die Handfläche &middot; knuckle = der Fingerknöchel &middot; '
          'thumb = der Daumen',
    m6Title='Bein und Fu&szlig;',
    m6Hint='Sechs Wörter von der Hüfte bis zum Boden.',
    m6Why='thigh = der Oberschenkel &middot; shin = das Schienbein &middot; calf = die Wade '
          '&middot; ankle = der Knöchel &middot; heel = die Ferse &middot; sole = die Fu&szlig;sohle',

    t1Eyebrow='Zwei Wörter, eine Stelle',
    t1Title='Wo das Englische trennt, was andere Sprachen zusammenfassen',
    t1b1='Der <em>neck</em> ist die Au&szlig;enseite &mdash; man dreht ihn, man trägt einen Schal darum. Der <em>throat</em> ist der Gang im Inneren, durch den geschluckt wird.',
    t1n1='<em>A sore throat</em>, aber <em>a stiff neck</em>. Nie umgekehrt.',
    t1b2='Der <em>jaw</em> ist der bewegliche Knochen, der den Mund öffnet und schlie&szlig;t. Der <em>chin</em> ist nur die Spitze vorne daran.',
    t1n2='<em>His jaw dropped.</em> &middot; <em>She rested her chin on her hand.</em>',
    t1b3='Die <em>forehead</em> ist die flache Vorderseite über den Augenbrauen; die <em>temples</em> sind die beiden flachen Seiten hinter den Augen.',
    t1n3='Kopfschmerzen sitzen in den <em>temples</em>. Sorge zeigt sich auf der <em>forehead</em>.',

    t2Eyebrow='Gelenk, Muskel, Knochen',
    t2Title='Was man verstaucht, zerrt und bricht',
    t2b1='Elbow, wrist, knuckle, ankle und hip sind Gelenke: Stellen, an denen zwei Knochen aufeinandertreffen und sich bewegen.',
    t2n1='Man <em>sprains</em> ein Gelenk, <em>pulls</em> einen Muskel und <em>breaks</em> einen Knochen.',
    t2b2='Shin und calf sind die beiden Hälften des Unterschenkels &mdash; harte Kante vorn, weicher Muskel hinten.',
    t2n2='<em>I barked my shin.</em> &middot; <em>I pulled a calf muscle.</em>',
    t2b3='Palm und sole sind die beiden flachen Unterseiten: eine an der Hand, eine am Fu&szlig;.',
    t2n3='Auch ein Schuh hat eine <em>sole</em> &mdash; dasselbe Wort aus demselben Grund.',

    sortEyebrow='Alles, was bisher vorkam',
    sortTitle='Knochen, Organ oder Gelenk?',
    sortHint='Dreizehn Teile, drei Arten. Ordne jedes dorthin, wo es hingehört.',
    sortBin1='Knochen',
    sortBin2='Organ',
    sortBin3='Gelenk',
    sortWhy='Ein Gelenk ist eine Verbindungsstelle, kein Körperteil &mdash; deshalb verstaucht '
            'man es, statt es zu brechen. Die fünf Organe hier sind die, die eine Ärztin im '
            'normalen Gespräch beim Namen nennt.',

    ordEyebrow='Der ganze Körper in einer Reihe',
    ordTitle='Von oben nach unten',
    ordHint='Acht Körperteile. Bring sie in die richtige Reihenfolge, beginnend am Kopf.',
    ordWhy='Forehead, jaw, throat, chest, waist, thigh, shin, heel &mdash; die Reihenfolge, '
           'in der eine Ärztin nach unten geht, und die Reihenfolge dieses Decks.',

    qEyebrow='Sag, welches',
    qTitle='Ein Wort trifft es',
    q1Ctx='Du sitzt seit sechs Stunden im Flugzeug, und die Rückseite deines Unterschenkels schmerzt.',
    q1Stem='Welcher Teil schmerzt?',
    q2Ctx='Beim Schlucken tut es innen weh, und die Stimme ist fast weg.',
    q2Stem='Was ist entzündet?',
    q3Ctx='Hier trägt man eine Uhr. Ein Ring passt nicht darüber.',
    q3Stem='Welches Gelenk ist es?',
    q4Ctx='Drei dieser vier sind Stellen, an denen zwei Knochen aufeinandertreffen und sich bewegen.',
    q4Stem='Welches ist kein Gelenk?',
    q5Ctx='Die Ärztin sagt, das Problem liege in dem gro&szlig;en Organ unter den Rippen auf deiner rechten Seite.',
    q5Stem='Welches Organ ist das?',

    gapEyebrow='Beim Arzt',
    bankLabel='Wortspeicher:',
    g1Title='Wo tut es weh?',
    g1Hint='Ein Wort pro Lücke. Der Speicher enthält drei Wörter, die du nicht brauchst.',
    g2Title='Und was ist passiert?',
    g2Hint='Dasselbe noch einmal. Nenne den Körperteil, nicht den Ort.',

    resNext='Das Wort zu erkennen ist die leichtere Hälfte. Jetzt sag, wo es wehtut &rarr;',
    resPerfect='Alles richtig. Du kannst diesen Körper innen wie au&szlig;en benennen.',
    resStrong='Stark. Sieh dir die Fehler an &mdash; fast alle betreffen ein Paar, vor dem dieses Deck gewarnt hat.',
    resMid='Brauchbare Grundlage. Geh zu den beiden Erklärfolien zurück, bevor du sprichst.',
    resLow='Arbeite die drei Tafeln noch einmal in Ruhe durch und starte dann neu.',

    actTitle='Jetzt sag, wo es wehtut',
    actUse='Verwende mindestens vier:',
    actSpeakKind='Gespräch &middot; zu zweit',
    actSpeakBrief='Zehn Minuten, dann Wechsel. Eine Person ist beim Arzt, die andere ist der Arzt und fragt nach: wo genau, seit wann, wie schlimm.',
    actSpeak1='Du bist vor drei Tagen vom Rad gestürzt. Beschreibe alles, was wehtut, von oben nach unten. Nur Worte &mdash; nicht zeigen.',
    actSpeak2='Du bist der Arzt. Lass deine Patientin sagen, ob der Schmerz innen oder au&szlig;en sitzt und ob es Knochen, Muskel oder Gelenk ist.',
    actSpeak3='Beschreibe jemanden im Raum, ohne den Namen zu nennen. Drei Körperteile, keine Kleidung, keine Haare.',
    actSpeak4='Dein Gegenüber spielt eine Verletzung pantomimisch vor. Benenne den Körperteil und was passiert ist, bevor die Pantomime endet.',
    actWriteKind='Schreiben &middot; 150&ndash;200 Wörter',
    actWriteBrief='Schreib die Nachricht an deine Versicherung nach einem Sturz auf der Treppe. Worauf du gefallen bist, welche Körperteile den Aufprall abbekommen haben, was du jetzt bewegen kannst und was nicht, und was die Ärztin gesagt hat. Keine Skizze &mdash; die Wörter müssen es tragen.',
    actPlaceholder='I slipped on the third step from the bottom and landed on…',
)

# ── SPANISH ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Head to <em>Toe</em>',
    coverSub='Treinta y seis palabras para el cuerpo humano &mdash; y la precisión para decir cuál duele',
    chipLevel='C1 &middot; Vocabulario',
    chipFocus='Nombrar el cuerpo, por dentro y por fuera',
    chipCount='NSLIDES diapositivas',

    s1Eyebrow='Etapa uno &middot; por encima de la clavícula',
    d1Title='Por encima de la clavícula',
    d1Note='Doce palabras',
    m1Title='La parte alta de la cara',
    m1Hint='Seis palabras, seis definiciones. Pulsa una palabra y luego la definición que le corresponde.',
    m1Why='forehead = la frente &middot; temple = la sien &middot; eyebrow = la ceja &middot; '
          'eyelash = la pestaña &middot; nostril = la fosa nasal &middot; '
          'earlobe = el lóbulo de la oreja',
    m2Title='La parte baja de la cara, y el cuello',
    m2Hint='Seis más. Dos de ellas nombran la misma zona: una por fuera y otra por dentro.',
    m2Why='cheek = la mejilla &middot; lip = el labio &middot; chin = la barbilla &middot; '
          'jaw = la mandíbula &middot; throat = la garganta (dentro) &middot; '
          'neck = el cuello (fuera)',

    s2Eyebrow='Etapa dos &middot; el tronco, abierto',
    d2Title='El tronco, abierto',
    d2Note='Doce palabras',
    m3Title='La estructura',
    m3Hint='Primero el hueso y el contorno: lo que sostiene el tronco y le da forma.',
    m3Why='chest = el pecho &middot; waist = la cintura &middot; hip = la cadera &middot; '
          'pelvis = la pelvis &middot; spine = la columna vertebral &middot; rib = la costilla',
    m4Title='Lo que hay dentro',
    m4Hint='Cinco órganos y un tipo de vaso. Singular o plural, según lo diga la definición.',
    m4Why='stomach = el estómago &middot; lung = el pulmón &middot; liver = el hígado &middot; '
          'kidney = el riñón &middot; intestines = los intestinos &middot; veins = las venas',

    s3Eyebrow='Etapa tres &middot; brazo, mano, pierna, pie',
    d3Title='Brazo, mano, pierna, pie',
    d3Note='Doce palabras',
    m5Title='El brazo y la mano',
    m5Hint='Seis palabras desde el hombro hasta los dedos.',
    m5Why='armpit = la axila &middot; elbow = el codo &middot; wrist = la muñeca &middot; '
          'palm = la palma &middot; knuckle = el nudillo &middot; thumb = el pulgar',
    m6Title='La pierna y el pie',
    m6Hint='Seis palabras desde la cadera hasta el suelo.',
    m6Why='thigh = el muslo &middot; shin = la espinilla &middot; calf = la pantorrilla '
          '&middot; ankle = el tobillo &middot; heel = el talón &middot; sole = la planta del pie',

    t1Eyebrow='Dos palabras, un mismo sitio',
    t1Title='Donde el inglés separa lo que otras lenguas unen',
    t1b1='El <em>neck</em> es la parte de fuera &mdash; lo giras, le pones una bufanda. El <em>throat</em> es el conducto interior por el que se traga.',
    t1n1='<em>A sore throat</em>, pero <em>a stiff neck</em>. Nunca al revés.',
    t1b2='El <em>jaw</em> es el hueso con bisagra que abre y cierra la boca. El <em>chin</em> es sólo la punta delantera.',
    t1n2='<em>His jaw dropped.</em> &middot; <em>She rested her chin on her hand.</em>',
    t1b3='La <em>forehead</em> es la parte plana de delante, encima de las cejas; los <em>temples</em> son los dos lados planos, detrás de los ojos.',
    t1n3='El dolor de cabeza se siente en los <em>temples</em>. La preocupación se ve en la <em>forehead</em>.',

    t2Eyebrow='Articulación, músculo, hueso',
    t2Title='Lo que se tuerce, se tira y se rompe',
    t2b1='Elbow, wrist, knuckle, ankle y hip son articulaciones: puntos donde dos huesos se encuentran y se mueven.',
    t2n1='Se <em>sprains</em> una articulación, se <em>pulls</em> un músculo y se <em>breaks</em> un hueso.',
    t2b2='Shin y calf son las dos mitades de la parte baja de la pierna: borde duro delante, músculo blando detrás.',
    t2n2='<em>I barked my shin.</em> &middot; <em>I pulled a calf muscle.</em>',
    t2b3='Palm y sole son las dos superficies planas de abajo: una en la mano, otra en el pie.',
    t2n3='Un zapato también tiene <em>sole</em>: la misma palabra por la misma razón.',

    sortEyebrow='Todo lo visto hasta aquí',
    sortTitle='¿Hueso, órgano o articulación?',
    sortHint='Trece partes, tres clases. Coloca cada una donde corresponde.',
    sortBin1='Hueso',
    sortBin2='Órgano',
    sortBin3='Articulación',
    sortWhy='Una articulación es un punto de encuentro, no una pieza &mdash; por eso se tuerce '
            'en lugar de romperse. Los cinco órganos de aquí son los que un médico nombra en '
            'una conversación corriente.',

    ordEyebrow='Todo el cuerpo, en una línea',
    ordTitle='De arriba abajo',
    ordHint='Ocho partes. Ponlas en orden, empezando por lo más alto de la cabeza.',
    ordWhy='Forehead, jaw, throat, chest, waist, thigh, shin, heel &mdash; el orden en que baja '
           'un médico, y el orden en que este deck las enseñó.',

    qEyebrow='Di cuál',
    qTitle='Una sola palabra sirve',
    q1Ctx='Llevas seis horas en un avión y te duele la parte de atrás de la pierna, por debajo de la rodilla.',
    q1Stem='¿Qué parte duele?',
    q2Ctx='Duele por dentro al tragar y casi te has quedado sin voz.',
    q2Stem='¿Qué tienes irritado?',
    q3Ctx='Aquí se lleva el reloj. Un anillo no cabe.',
    q3Stem='¿Qué articulación es?',
    q4Ctx='Tres de estas cuatro son puntos donde dos huesos se encuentran y se mueven.',
    q4Stem='¿Cuál no es una articulación?',
    q5Ctx='El médico dice que el problema está en el órgano grande que queda bajo las costillas del lado derecho.',
    q5Stem='¿Qué órgano es?',

    gapEyebrow='En la consulta',
    bankLabel='Banco de palabras:',
    g1Title='¿Dónde duele?',
    g1Hint='Una palabra por hueco. El banco trae tres que no vas a necesitar.',
    g2Title='¿Y qué pasó?',
    g2Hint='Otra vez igual. Nombra la parte del cuerpo, no el lugar.',

    resNext='Reconocer la palabra es la mitad fácil. Ahora di dónde duele &rarr;',
    resPerfect='Todas. Puedes nombrar este cuerpo por dentro y por fuera.',
    resStrong='Muy bien. Mira los fallos: casi todos son una pareja de las que avisó este deck.',
    resMid='Base utilizable. Vuelve a las dos diapositivas de explicación antes de hablar.',
    resLow='Repasa las tres láminas con calma y hazlo otra vez.',

    actTitle='Ahora di dónde duele',
    actUse='Usa al menos cuatro:',
    actSpeakKind='Conversación &middot; en parejas',
    actSpeakBrief='Diez minutos y se cambia. Uno está en la consulta; el otro es el médico y pregunta dónde exactamente, desde cuándo y cuánto duele.',
    actSpeak1='Te caíste de la bici hace tres días. Describe todo lo que duele, de la cabeza hacia abajo. Sólo con palabras: no señales.',
    actSpeak2='Eres el médico. Haz que tu paciente diga si el dolor es por dentro o por fuera, y si es hueso, músculo o articulación.',
    actSpeak3='Describe a alguien de la sala sin decir su nombre. Tres partes del cuerpo, sin ropa y sin pelo.',
    actSpeak4='Tu pareja imita una lesión. Nombra la parte y lo que se hizo antes de que termine la mímica.',
    actWriteKind='Escritura &middot; 150&ndash;200 palabras',
    actWriteBrief='Escribe el mensaje que mandas a tu seguro después de una caída por las escaleras. Sobre qué caíste, qué partes recibieron el golpe, qué puedes mover ahora y qué no, y qué dijo el médico. Sin dibujo: las palabras tienen que sostenerlo.',
    actPlaceholder='I slipped on the third step from the bottom and landed on…',
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
