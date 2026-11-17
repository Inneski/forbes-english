# -*- coding: utf-8 -*-
"""Interface strings for Talk Me Through the Last Job: Customer Interviews
on Site (B2-C1). English, German, Spanish.

What translates (HOUSE-STYLE §8): the chrome, titles, eyebrows, every rule
bullet, every situation line, every explanation, the role cards and the task
instructions. What does not: the trade words, the quotes from customers, the
options, the gap sentences, the order pieces and the talk prompts -- those
are the English being practised.

Cited English in CAPS or in double quotes, as in the other decks.
coverSub is also the meta description (tools/seo.py).
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount',
        'actSpeakWord', 'actWriteWord']

T = {}

# ══════════════════════════════════════════════════════════════════════
#  ENGLISH
# ══════════════════════════════════════════════════════════════════════
T['en'] = dict(
    coverTitle='Talk Me Through <em>the Last Job</em>',
    coverSub='Market-research conversations with roofers, carpenters and builders’ merchants in the UK and Ireland: their words, what they really mean, and the questions that get the truth.',
    chipLevel='B2–C1', chipFocus='Speaking · customer interviews', chipCount='30 slides',

    eW='Warm-up', tkWT='Before we start',
    e1='The words on the roof', e2='What they really mean', e3='Questions that get the truth',
    e4='Run the conversation',

    # ── stage 1 ──
    r1T='Your catalogue word, their word',
    r1a='BREATHER MEMBRANE: the underlay that lets vapour out and keeps rain out. Many roofers still say “felt”.',
    r1b='VCL (vapour control layer): the UK name for a vapour barrier.',
    r1c='LAPS are the overlaps between sheets. You TAPE the laps.',
    r1d='TO SPEC: to name a product in the specification.',
    r1e='TO SWAP IT OUT: to fit a cheaper product instead.',
    r1f='FIRST FIX: the work before plastering. SECOND FIX: after it.',
    r1g='BUILDERS’ MERCHANT: the trade’s shop, your retailer.',
    r1h='THE TRADE: professional customers, not the public.',
    r1i='IT MOVES: it sells. IT DOESN’T MOVE: it sits on the shelf.',
    pRoof='On the roof', pTrade='In the trade', pCounter='At the counter',

    mT='What it means on site',
    mHint='Click a word, then the line that explains it.',
    mWhy='These are the words a roofer or a merchant will use with you. If they use them and you do not, the conversation stays formal.',

    mc1T='Which word fits?',
    q1w='TO SPEC (past: SPECCED) = to name it in the specification. Then the contractor SWAPPED IT OUT, a very common story on price.',
    q2w='A CALLBACK is a return visit to fix a problem on a finished job. Roofers count them, because they cost time and reputation.',
    q3w='THE TRADE = professional customers as a group, with a plural verb in British English: “the trade ASK for it”.',
    q4w='The VCL goes on at FIRST FIX, before the plasterboard. SECOND FIX is the finishing work after plastering.',

    # ── stage 2 ──
    r2T='Praise comes small, complaints come soft',
    r2a='British and Irish customers often praise by saying less.',
    r2b='NOT BAD AT ALL is real praise. QUITE GOOD often means only “OK”.',
    r2c='In Ireland, GRAND means fine. It is not enthusiasm.',
    r2d='IT’S GRAND, IT DOES THE JOB: no complaint, and no love either.',
    r2e='Complaints are softened with A BIT, NOT REALLY and NOT MAD ABOUT.',
    r2f='A BIT OF A FAFF = it wastes time. On a roof, that is a real problem.',
    pPraise='Praise', pGrand='“It’s grand”', pSoft='Soft complaints',

    mc2T='What are they telling you?',
    c5='A roofer in Galway, about your breather membrane:',
    c6='A carpenter in Kent, about fitting your VCL:',
    c7='A roofer in Leeds, about your new tape:',
    c8='A branch manager at a builders’ merchant:',
    c9='A roofer in Cork, about the price:',
    c10='A contractor in Manchester, about changing supplier:',
    q5w='GRAND in Ireland = fine, acceptable. DOES THE JOB = it works, nothing more. Do not record this as enthusiasm.',
    q6w='A FAFF = a lot of fuss, time and effort. A BIT softens it, but the problem is real: time on site is money.',
    q7w='NOT BAD AT ALL is real praise, said modestly. TO BE FAIR adds: I am giving it credit.',
    q8w='IT DOESN’T MOVE = it does not sell. A merchant measures a product by how fast it leaves the shelf.',
    q9w='DEAR = expensive. FIERCE is an Irish intensifier = very. FOR WHAT IT IS = for the value you get.',
    q10w='I WOULDN’T SAY NO = yes, possibly. The condition comes after IF: the price. Your next question is “What would the price need to be?”',

    tk2T='Your customers',

    # ── stage 3 ──
    r3T='Open, probe, play back',
    r3a='Ask about one real, recent job, not opinions in general.',
    r3b='Then stop talking. Silence gets the detail.',
    r3c='When a word is vague, ask what it means to them.',
    r3d='Do not suggest the answer inside the question.',
    r3e='Say it back in your words, and let them correct you.',
    r3f='A correction is good data: it shows what really matters.',
    pOpen='Open', pProbe='Probe', pBack='Play back',

    mc3T='Choose the better question',
    c11='You want to know if roofers like your new tape.',
    c12='The roofer says your membrane is “fiddly”.',
    c13='You want to know who chooses the membrane.',
    s11='Which question gets the most honest answer?',
    s12='What is the best next question?',
    s13='Which question tells you the most?',
    q11w='HOW DO YOU GET ON WITH…? is open and neutral. The others put the answer in the customer’s mouth, and polite customers agree.',
    q12w='A probe repeats THEIR word and asks what it means. The others change the subject or suggest the answer.',
    q13w='One real, recent job gives you a fact. ALWAYS, WOULD YOU and IS IT USUALLY invite a general, polite answer.',

    gapT='One word in each gap',
    gHint='These are the moves from the last slides.',
    g1w='TALK ME THROUGH (or WALK ME THROUGH) = describe it step by step. The best first question.',
    g2w='WHEN YOU SAY…, WHAT DO YOU MEAN? repeats their word and asks for detail.',
    g3w='CAN YOU GIVE ME AN EXAMPLE? turns an opinion into a story you can use.',
    g4w='SO IF I’VE UNDERSTOOD YOU CORRECTLY… is a play-back. It invites a correction.',
    g5w='WHAT WOULD IT TAKE FOR YOU TO…? asks for the condition for change.',
    g6w='MAKE (or TAKE) A DECISION. Ask who, not whether.',

    orderT='Build the line',
    orderHint='Click the pieces in order.',
    o1w='A play-back: SO IF I’VE GOT THIS RIGHT, then the point, as a question they can correct.',
    o2w='WHAT WOULD IT TAKE FOR YOU TO + verb? The condition for change, in one question.',

    # ── stage 4 ──
    roleWho='Your customer', roleFind='Find out', roleRule='Before you move on: one probe and one play-back.',
    role1T='Declan, roofer, Galway',
    role1d='Runs a small firm with four lads. Buys from the local merchant. Uses your breather membrane “sometimes”. Your teacher plays Declan.',
    role1a='Why only sometimes? What decides it on each job?',
    role1b='What goes wrong on the roof in wind and rain?',
    role1c='Who else has a say: the merchant, the builder, the architect?',
    role2T='Sarah, site manager, Kent',
    role2d='Builds timber-frame houses. Her carpenters fit the VCL at first fix, and every house has an air test. Your teacher plays Sarah.',
    role2a='Talk her through the last house: where did the VCL get cut or damaged?',
    role2b='What happened at the air test, and what did it cost?',
    role2c='What would it take for her carpenters to change tape?',
    role3T='Gary, builders’ merchant, Manchester',
    role3d='Manages a branch with a busy trade counter. Stocks two of your competitors and one of your products. Your teacher plays Gary.',
    role3a='What do the trade ask for by name, and why?',
    role3b='What moves, and what doesn’t? What does he do with stock that doesn’t move?',
    role3c='What would get your products more space on his shelves?',

    debT='Report back in 60 seconds',

    # ── activation ──
    actTitle='Your next site visit',
    actUse='Use at least three:',
    actSpeakBrief='Plan the real thing. Your next customer in England or Ireland is a roofer, a carpenter or a merchant: choose one.',
    actSpeak1='Run a ten-minute interview with your teacher as that customer. Start with TALK ME THROUGH and one real, recent job.',
    actSpeak2='Every time you hear a soft word (A BIT, NOT BAD, GRAND), probe it before you move on.',
    actSpeak3='Close with a play-back of the three main points. Then report them to the team in 60 seconds.',
    actWriteKind='Your interview guide',
    actWriteBrief='Write the guide you will take on your next visit (150–200 words): one line on what you want to learn, eight open questions in order, three probes ready for vague answers, and your closing play-back. Write it as you will say it.',
    actPlaceholder='Goal: find out why… 1. Talk me through…',
)

# ══════════════════════════════════════════════════════════════════════
#  GERMAN
# ══════════════════════════════════════════════════════════════════════
T['de'] = dict(
    coverTitle='Talk Me Through <em>the Last Job</em>',
    coverSub='Marktforschung mit Dachdeckern, Zimmerleuten und Baustoffhändlern in Großbritannien und Irland: ihre Wörter, was sie wirklich meinen, und Fragen, die die Wahrheit bringen.',
    chipLevel='B2–C1', chipFocus='Sprechen · Kundengespräche', chipCount='30 Folien',

    eW='Zum Einstieg', tkWT='Bevor wir anfangen',
    e1='Die Wörter auf dem Dach', e2='Was sie wirklich meinen', e3='Fragen, die die Wahrheit bringen',
    e4='Führe das Gespräch',

    r1T='Dein Katalogwort, ihr Wort',
    r1a='BREATHER MEMBRANE: die Unterdeckbahn, die Dampf hinauslässt und Regen abhält. Viele Dachdecker sagen noch „felt“.',
    r1b='VCL (vapour control layer): der britische Name für eine Dampfbremse.',
    r1c='LAPS sind die Überlappungen zwischen den Bahnen. Man TAPED die Laps.',
    r1d='TO SPEC: ein Produkt in der Ausschreibung vorschreiben.',
    r1e='TO SWAP IT OUT: stattdessen ein billigeres Produkt einbauen.',
    r1f='FIRST FIX: die Arbeit vor dem Verputzen. SECOND FIX: danach.',
    r1g='BUILDERS’ MERCHANT: der Baustoffhandel, dein Händler.',
    r1h='THE TRADE: die Profikunden, nicht die Privatkunden.',
    r1i='IT MOVES: es verkauft sich. IT DOESN’T MOVE: es bleibt im Regal liegen.',
    pRoof='Auf dem Dach', pTrade='In der Branche', pCounter='An der Theke',

    mT='Was es auf der Baustelle heißt',
    mHint='Klicke auf ein Wort, dann auf die passende Erklärung.',
    mWhy='Diese Wörter benutzt ein Dachdecker oder Händler mit dir. Wenn er sie benutzt und du nicht, bleibt das Gespräch förmlich.',

    mc1T='Welches Wort passt?',
    q1w='TO SPEC (Vergangenheit: SPECCED) = in der Ausschreibung vorschreiben. Dann hat der Bauunternehmer es ausgetauscht (SWAPPED IT OUT), eine sehr häufige Geschichte beim Preis.',
    q2w='Ein CALLBACK ist ein erneuter Einsatz, um einen Mangel an einem fertigen Auftrag zu beheben. Dachdecker zählen sie, denn sie kosten Zeit und Ruf.',
    q3w='THE TRADE = die Profikunden als Gruppe, im britischen Englisch mit Verb im Plural: „the trade ASK for it“.',
    q4w='Die VCL kommt beim FIRST FIX, vor den Gipskartonplatten. SECOND FIX ist der Ausbau nach dem Verputzen.',

    r2T='Lob kommt klein, Kritik kommt weich',
    r2a='Britische und irische Kunden loben oft, indem sie weniger sagen.',
    r2b='NOT BAD AT ALL ist echtes Lob. QUITE GOOD heißt oft nur „okay“.',
    r2c='In Irland heißt GRAND „in Ordnung“. Es ist keine Begeisterung.',
    r2d='IT’S GRAND, IT DOES THE JOB: keine Beschwerde, aber auch keine Liebe.',
    r2e='Kritik wird abgeschwächt mit A BIT, NOT REALLY und NOT MAD ABOUT.',
    r2f='A BIT OF A FAFF = es kostet unnötig Zeit. Auf dem Dach ist das ein echtes Problem.',
    pPraise='Lob', pGrand='„It’s grand“', pSoft='Weiche Kritik',

    mc2T='Was sagen sie dir?',
    c5='Ein Dachdecker in Galway, über deine Unterdeckbahn:',
    c6='Ein Zimmermann in Kent, über das Verlegen deiner VCL:',
    c7='Ein Dachdecker in Leeds, über dein neues Klebeband:',
    c8='Ein Filialleiter bei einem Baustoffhändler:',
    c9='Ein Dachdecker in Cork, über den Preis:',
    c10='Ein Bauunternehmer in Manchester, über einen Lieferantenwechsel:',
    q5w='GRAND heißt in Irland: in Ordnung, akzeptabel. DOES THE JOB = es funktioniert, mehr nicht. Notiere das nicht als Begeisterung.',
    q6w='A FAFF = viel Umstand, Zeit und Mühe. A BIT schwächt es ab, aber das Problem ist echt: Zeit auf der Baustelle ist Geld.',
    q7w='NOT BAD AT ALL ist echtes Lob, bescheiden gesagt. TO BE FAIR heißt: Ich erkenne es an.',
    q8w='IT DOESN’T MOVE = es verkauft sich nicht. Ein Händler misst ein Produkt daran, wie schnell es aus dem Regal geht.',
    q9w='DEAR = teuer. FIERCE ist eine irische Verstärkung = sehr. FOR WHAT IT IS = für das, was man dafür bekommt.',
    q10w='I WOULDN’T SAY NO = ja, vielleicht. Die Bedingung kommt nach IF: der Preis. Deine nächste Frage: „What would the price need to be?“',

    tk2T='Deine Kunden',

    r3T='Öffnen, nachhaken, zurückspiegeln',
    r3a='Frag nach einem echten, kürzlichen Auftrag, nicht nach allgemeinen Meinungen.',
    r3b='Dann hör auf zu reden. Schweigen bringt die Details.',
    r3c='Wenn ein Wort vage ist, frag, was es für sie bedeutet.',
    r3d='Leg die Antwort nicht schon in die Frage.',
    r3e='Sag es in deinen Worten zurück und lass dich korrigieren.',
    r3f='Eine Korrektur sind gute Daten: Sie zeigt, was wirklich zählt.',
    pOpen='Öffnen', pProbe='Nachhaken', pBack='Zurückspiegeln',

    mc3T='Wähle die bessere Frage',
    c11='Du willst wissen, ob Dachdecker dein neues Klebeband mögen.',
    c12='Der Dachdecker sagt, deine Bahn sei „fiddly“ (fummelig).',
    c13='Du willst wissen, wer die Bahn auswählt.',
    s11='Welche Frage bringt die ehrlichste Antwort?',
    s12='Was ist die beste nächste Frage?',
    s13='Welche Frage verrät dir am meisten?',
    q11w='HOW DO YOU GET ON WITH…? ist offen und neutral. Die anderen legen dem Kunden die Antwort in den Mund, und höfliche Kunden stimmen zu.',
    q12w='Beim Nachhaken wiederholt man IHR Wort und fragt, was es bedeutet. Die anderen wechseln das Thema oder schlagen die Antwort vor.',
    q13w='Ein echter, kürzlicher Auftrag liefert eine Tatsache. ALWAYS, WOULD YOU und IS IT USUALLY laden zu einer allgemeinen, höflichen Antwort ein.',

    gapT='Ein Wort pro Lücke',
    gHint='Das sind die Gesprächszüge von den letzten Folien.',
    g1w='TALK ME THROUGH (oder WALK ME THROUGH) = Schritt für Schritt beschreiben. Die beste erste Frage.',
    g2w='WHEN YOU SAY…, WHAT DO YOU MEAN? wiederholt ihr Wort und fragt nach Details.',
    g3w='CAN YOU GIVE ME AN EXAMPLE? macht aus einer Meinung eine Geschichte, mit der du arbeiten kannst.',
    g4w='SO IF I’VE UNDERSTOOD YOU CORRECTLY… spiegelt zurück. Es lädt zur Korrektur ein.',
    g5w='WHAT WOULD IT TAKE FOR YOU TO…? fragt nach der Bedingung für einen Wechsel.',
    g6w='MAKE (oder TAKE) A DECISION. Frag nach dem Wer, nicht nach dem Ob.',

    orderT='Bau den Satz',
    orderHint='Klicke die Teile in der richtigen Reihenfolge an.',
    o1w='Zurückspiegeln: SO IF I’VE GOT THIS RIGHT, dann der Punkt, als Frage, die man korrigieren kann.',
    o2w='WHAT WOULD IT TAKE FOR YOU TO + Verb? Die Bedingung für einen Wechsel, in einer Frage.',

    roleWho='Dein Kunde', roleFind='Finde heraus', roleRule='Bevor du weitermachst: einmal nachhaken, einmal zurückspiegeln.',
    role1T='Declan, Dachdecker, Galway',
    role1d='Führt eine kleine Firma mit vier Leuten. Kauft beim örtlichen Händler. Verwendet deine Unterdeckbahn „manchmal“. Deine Lehrkraft spielt Declan.',
    role1a='Warum nur manchmal? Was entscheidet das bei jedem Auftrag?',
    role1b='Was geht auf dem Dach bei Wind und Regen schief?',
    role1c='Wer redet noch mit: der Händler, der Bauunternehmer, der Architekt?',
    role2T='Sarah, Bauleiterin, Kent',
    role2d='Baut Holzrahmenhäuser. Ihre Zimmerleute verlegen die VCL beim First Fix, und jedes Haus bekommt einen Luftdichtheitstest. Deine Lehrkraft spielt Sarah.',
    role2a='Lass sie das letzte Haus durchgehen: Wo wurde die VCL aufgeschnitten oder beschädigt?',
    role2b='Was ist beim Luftdichtheitstest passiert, und was hat es gekostet?',
    role2c='Was müsste passieren, damit ihre Zimmerleute das Klebeband wechseln?',
    role3T='Gary, Baustoffhändler, Manchester',
    role3d='Leitet eine Filiale mit einer vollen Profitheke. Führt zwei deiner Konkurrenten und eines deiner Produkte. Deine Lehrkraft spielt Gary.',
    role3a='Wonach fragen die Profis mit Namen, und warum?',
    role3b='Was verkauft sich und was nicht? Was macht er mit Ware, die liegen bleibt?',
    role3c='Was würde deinen Produkten mehr Platz in seinen Regalen verschaffen?',

    debT='Berichte in 60 Sekunden',

    actTitle='Dein nächster Baustellenbesuch',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Plane den Ernstfall. Dein nächster Kunde in England oder Irland ist ein Dachdecker, ein Zimmermann oder ein Händler: Wähle einen aus.',
    actSpeak1='Führe ein zehnminütiges Interview mit deiner Lehrkraft als diesem Kunden. Beginne mit TALK ME THROUGH und einem echten, kürzlichen Auftrag.',
    actSpeak2='Jedes Mal, wenn du ein weiches Wort hörst (A BIT, NOT BAD, GRAND), hak nach, bevor du weitermachst.',
    actSpeak3='Schließe mit einer Zusammenfassung der drei wichtigsten Punkte. Dann berichte sie dem Team in 60 Sekunden.',
    actWriteKind='Dein Gesprächsleitfaden',
    actWriteBrief='Schreib den Leitfaden für deinen nächsten Besuch (150–200 Wörter): eine Zeile dazu, was du herausfinden willst, acht offene Fragen in der richtigen Reihenfolge, drei Nachfragen für vage Antworten und deine abschließende Zusammenfassung. Schreib es so, wie du es sagen wirst.',
    actPlaceholder='Ziel: herausfinden, warum… 1. Talk me through…',
)

# ══════════════════════════════════════════════════════════════════════
#  SPANISH
# ══════════════════════════════════════════════════════════════════════
T['es'] = dict(
    coverTitle='Talk Me Through <em>the Last Job</em>',
    coverSub='Investigación de mercado con techadores, carpinteros y almacenes del Reino Unido e Irlanda: su vocabulario, lo que de verdad quieren decir y las preguntas clave.',
    chipLevel='B2–C1', chipFocus='Oral · entrevistas', chipCount='30 diapositivas',

    eW='Para empezar', tkWT='Antes de empezar',
    e1='Las palabras del tejado', e2='Lo que de verdad quieren decir', e3='Preguntas que sacan la verdad',
    e4='Lleva la conversación',

    r1T='Tu palabra de catálogo, su palabra',
    r1a='BREATHER MEMBRANE: la lámina bajo teja que deja salir el vapor y no deja entrar la lluvia. Muchos techadores aún dicen “felt”.',
    r1b='VCL (vapour control layer): el nombre británico de la barrera de vapor.',
    r1c='LAPS son los solapes entre láminas. Los solapes se sellan con cinta (TAPE).',
    r1d='TO SPEC: prescribir un producto en el pliego de condiciones.',
    r1e='TO SWAP IT OUT: poner un producto más barato en su lugar.',
    r1f='FIRST FIX: el trabajo antes del enlucido. SECOND FIX: el de después.',
    r1g='BUILDERS’ MERCHANT: el almacén de materiales, tu distribuidor.',
    r1h='THE TRADE: los clientes profesionales, no el público.',
    r1i='IT MOVES: se vende. IT DOESN’T MOVE: se queda en la estantería.',
    pRoof='En el tejado', pTrade='En el oficio', pCounter='En el mostrador',

    mT='Lo que significa en la obra',
    mHint='Haz clic en una palabra y luego en la explicación que le corresponde.',
    mWhy='Son las palabras que usará contigo un techador o un distribuidor. Si él las usa y tú no, la conversación se queda en lo formal.',

    mc1T='¿Qué palabra encaja?',
    q1w='TO SPEC (pasado: SPECCED) = prescribirlo en el pliego. Luego el contratista lo cambió (SWAPPED IT OUT), una historia muy común por el precio.',
    q2w='Un CALLBACK es volver a una obra terminada para arreglar un problema. Los techadores los cuentan, porque cuestan tiempo y reputación.',
    q3w='THE TRADE = los clientes profesionales como grupo, con el verbo en plural en inglés británico: “the trade ASK for it”.',
    q4w='La VCL se coloca en el FIRST FIX, antes de las placas de yeso. El SECOND FIX es el acabado después del enlucido.',

    r2T='El elogio llega pequeño, la queja llega suave',
    r2a='Los clientes británicos e irlandeses suelen elogiar diciendo menos.',
    r2b='NOT BAD AT ALL es un elogio de verdad. QUITE GOOD a menudo solo significa “bien”.',
    r2c='En Irlanda, GRAND significa “está bien”. No es entusiasmo.',
    r2d='IT’S GRAND, IT DOES THE JOB: ninguna queja, pero tampoco cariño.',
    r2e='Las quejas se suavizan con A BIT, NOT REALLY y NOT MAD ABOUT.',
    r2f='A BIT OF A FAFF = hace perder tiempo. En un tejado, eso es un problema real.',
    pPraise='Elogio', pGrand='“It’s grand”', pSoft='Quejas suaves',

    mc2T='¿Qué te están diciendo?',
    c5='Un techador en Galway, sobre tu lámina transpirable:',
    c6='Un carpintero en Kent, sobre colocar tu VCL:',
    c7='Un techador en Leeds, sobre tu nueva cinta:',
    c8='El jefe de un almacén de materiales:',
    c9='Un techador en Cork, sobre el precio:',
    c10='Un contratista en Manchester, sobre cambiar de proveedor:',
    q5w='GRAND en Irlanda = bien, aceptable. DOES THE JOB = funciona, nada más. No lo anotes como entusiasmo.',
    q6w='A FAFF = mucho lío, tiempo y esfuerzo. A BIT lo suaviza, pero el problema es real: el tiempo en obra es dinero.',
    q7w='NOT BAD AT ALL es un elogio real, dicho con modestia. TO BE FAIR añade: le doy su mérito.',
    q8w='IT DOESN’T MOVE = no se vende. Un distribuidor mide un producto por lo rápido que sale de la estantería.',
    q9w='DEAR = caro. FIERCE es un intensificador irlandés = muy. FOR WHAT IT IS = para lo que ofrece.',
    q10w='I WOULDN’T SAY NO = sí, quizá. La condición va después de IF: el precio. Tu siguiente pregunta: “What would the price need to be?”',

    tk2T='Tus clientes',

    r3T='Abrir, indagar, devolver',
    r3a='Pregunta por un trabajo real y reciente, no por opiniones en general.',
    r3b='Luego deja de hablar. El silencio trae los detalles.',
    r3c='Cuando una palabra es vaga, pregunta qué significa para ellos.',
    r3d='No pongas la respuesta dentro de la pregunta.',
    r3e='Repítelo con tus palabras y deja que te corrijan.',
    r3f='Una corrección es un buen dato: muestra lo que de verdad importa.',
    pOpen='Abrir', pProbe='Indagar', pBack='Devolver',

    mc3T='Elige la mejor pregunta',
    c11='Quieres saber si a los techadores les gusta tu nueva cinta.',
    c12='El techador dice que tu lámina es “fiddly” (engorrosa).',
    c13='Quieres saber quién elige la lámina.',
    s11='¿Qué pregunta consigue la respuesta más sincera?',
    s12='¿Cuál es la mejor siguiente pregunta?',
    s13='¿Qué pregunta te dice más?',
    q11w='HOW DO YOU GET ON WITH…? es abierta y neutral. Las demás ponen la respuesta en boca del cliente, y los clientes educados dicen que sí.',
    q12w='Indagar es repetir SU palabra y preguntar qué significa. Las demás cambian de tema o sugieren la respuesta.',
    q13w='Un trabajo real y reciente te da un hecho. ALWAYS, WOULD YOU e IS IT USUALLY invitan a una respuesta general y educada.',

    gapT='Una palabra en cada hueco',
    gHint='Son los recursos de las diapositivas anteriores.',
    g1w='TALK ME THROUGH (o WALK ME THROUGH) = descríbelo paso a paso. La mejor primera pregunta.',
    g2w='WHEN YOU SAY…, WHAT DO YOU MEAN? repite su palabra y pide detalles.',
    g3w='CAN YOU GIVE ME AN EXAMPLE? convierte una opinión en una historia que puedes usar.',
    g4w='SO IF I’VE UNDERSTOOD YOU CORRECTLY… devuelve lo dicho. Invita a corregir.',
    g5w='WHAT WOULD IT TAKE FOR YOU TO…? pregunta por la condición para cambiar.',
    g6w='MAKE (o TAKE) A DECISION. Pregunta quién, no si.',

    orderT='Construye la frase',
    orderHint='Haz clic en las piezas en orden.',
    o1w='Devolver: SO IF I’VE GOT THIS RIGHT, y luego el punto, como pregunta que pueden corregir.',
    o2w='WHAT WOULD IT TAKE FOR YOU TO + verbo? La condición para cambiar, en una sola pregunta.',

    roleWho='Tu cliente', roleFind='Averigua', roleRule='Antes de seguir: una pregunta para indagar y una para devolver.',
    role1T='Declan, techador, Galway',
    role1d='Dirige una empresa pequeña con cuatro operarios. Compra en el almacén local. Usa tu lámina transpirable “a veces”. Tu profesor hace de Declan.',
    role1a='¿Por qué solo a veces? ¿Qué lo decide en cada obra?',
    role1b='¿Qué sale mal en el tejado con viento y lluvia?',
    role1c='¿Quién más opina: el almacén, el constructor, el arquitecto?',
    role2T='Sarah, jefa de obra, Kent',
    role2d='Construye casas de entramado de madera. Sus carpinteros colocan la VCL en el first fix, y cada casa pasa una prueba de estanqueidad. Tu profesor hace de Sarah.',
    role2a='Que te cuente la última casa: ¿dónde se cortó o se dañó la VCL?',
    role2b='¿Qué pasó en la prueba de estanqueidad y cuánto costó?',
    role2c='¿Qué haría falta para que sus carpinteros cambiaran de cinta?',
    role3T='Gary, almacén de materiales, Manchester',
    role3d='Dirige una sucursal con un mostrador profesional muy activo. Tiene dos de tus competidores y uno de tus productos. Tu profesor hace de Gary.',
    role3a='¿Qué piden los profesionales por su nombre, y por qué?',
    role3b='¿Qué se vende y qué no? ¿Qué hace con lo que no sale?',
    role3c='¿Qué daría a tus productos más espacio en sus estanterías?',

    debT='Informa en 60 segundos',

    actTitle='Tu próxima visita a obra',
    actUse='Usa al menos tres:',
    actSpeakBrief='Prepara la visita real. Tu próximo cliente en Inglaterra o Irlanda es un techador, un carpintero o un distribuidor: elige uno.',
    actSpeak1='Haz una entrevista de diez minutos con tu profesor en el papel de ese cliente. Empieza con TALK ME THROUGH y un trabajo real y reciente.',
    actSpeak2='Cada vez que oigas una palabra suave (A BIT, NOT BAD, GRAND), indaga antes de seguir.',
    actSpeak3='Cierra devolviendo los tres puntos principales. Luego infórmalos al equipo en 60 segundos.',
    actWriteKind='Tu guion de entrevista',
    actWriteBrief='Escribe el guion para tu próxima visita (150–200 palabras): una línea sobre lo que quieres averiguar, ocho preguntas abiertas en orden, tres preguntas para indagar ante respuestas vagas y tu resumen final. Escríbelo tal como lo vas a decir.',
    actPlaceholder='Objetivo: averiguar por qué… 1. Talk me through…',
)


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    rows = ['    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
            for k in sorted(d)]
    return '{\n' + ',\n'.join(rows) + '\n  }'


if __name__ == '__main__':
    base = set(T['en'])
    for c, d in T.items():
        m, x = base - set(d), set(d) - base
        print('%-3s %3d keys' % (c, len(d)),
              ('MISSING %s' % sorted(m)) if m else 'ok',
              ('EXTRA %s' % sorted(x)) if x else '')
