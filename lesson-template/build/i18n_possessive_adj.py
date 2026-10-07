# -*- coding: utf-8 -*-
"""Interface strings for My Cat, Your Dog — possessive adjectives and THIS /
THAT (A1, young learners). English, German and Spanish.

What translates: the chrome, slide titles, the rule on every teach card, the
THIS / THAT situations, every explanation, the task instructions. What does
not (HOUSE-STYLE §8): the reading panels, stems, options, gap sentences, the
sort and order pieces, the English examples under the cards, and the
translation rows — those are German and English on purpose, in every UI
language, because the stage is a German ⇄ English game.

Short sentences throughout: the readers are about nine. Grammar words in
CAPS, cited sentences in double quotes, as in the other decks. The teach card
tC1 compares English with the UI language's own possessives (MEIN / MEINE in
German, MI / MIS in Spanish), so each language gets the comparison that is
true for it.

coverSub is also the meta description: tools/seo.py strips tags WITHOUT
adding a space, so each <br> has a space in front of it.
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
    coverTitle='My Cat,<br><em>Your</em> Dog',
    coverSub='Possessive adjectives — my, your, his, her, its, our, their — <br>and this / that, with a German ⇄ English translation game',
    chipLevel='A1', chipFocus='my · your · his · her', chipCount='36 slides',
    bankLabel='Word bank:',

    d1t='Meet the Pets', d1n='Stage 1 · my, your, our, their',
    d2t='His, Her or Its?', d2n='Stage 2 · who is the owner?',
    d3t='This or That?', d3n='Stage 3 · near and far',
    d4t='The Pet Show', d4n='Stage 4 · translate it!',

    e1='My · your · our · their', e2='His · her · its', e3='This · that',
    e4='Translate', eR='The rule',

    p1t='Meet Mia and Pepper', p2t='Leo and Biscuit', p3t='Here or over there?',
    p4t='The school pet show',

    tAt='Who owns it?',
    tA1='The owner is me.',
    tA2='The owner is the person I am talking to.',
    tA3='The owners are me and other people.',
    tA4='The owners are other people.',

    tBt='His, her or its?',
    tB1='The owner is a boy or a man.',
    tB2='The owner is a girl or a woman.',
    tB3='The owner is an animal or a thing.',

    tCt='Three tips',
    tC1='In German you say MEIN Hund, MEINE Katze, MEINE Hunde. In English it is always MY. It never changes!',
    tC2='HIS or HER? Look at the OWNER, not the animal. A girl’s dog is HER dog.',
    tC3='ITS = it owns it. IT’S = it is. No apostrophe for the owner!',

    tDt='How the game works',
    tD1='Read the German sentence. Write it in English.',
    tD2='Tap the switch at the top. Now read the English and write it in German.',
    tD3='Press Check. Compare your sentence with the answer.',

    matchT='Find the partner',
    matchHint='Tap a word on the left, then its partner on the right.',
    matchW='I → MY, you → YOUR, he → HIS, she → HER, it → ITS, we → OUR, they → THEIR.',

    mcT='Choose the right word', mc3T='Near or far?',
    q1w='Mia is talking about her own cat, so she says MY.',
    q2w='Leo is talking TO Mia. The cat belongs to the person he is talking to: YOUR.',
    q3w='Mum and Dad talk about themselves and the family: WE → OUR.',
    q4w='The owners are Ella and Sam — two other people: THEY → THEIR.',
    q5w='The owner is Leo, a boy: HIS dog.',
    q6w='The owner is Mum, a woman: HER horse.',
    q7w='The garden belongs to the house — a thing: ITS. "It’s" means "it is".',
    c8='Mia holds Snowy in her arms.',
    c9='Grandpa’s horse is far away, in the field.',
    c10='Leo’s dog is sitting next to him.',
    c11='The goldfish is over there, on the teacher’s desk.',
    q8w='Snowy is close — in Mia’s arms. Close: THIS.',
    q9w='The horse is far away. Far: THAT.',
    q10w='The dog is right next to Leo. Close: THIS.',
    q11w='The goldfish is over there. Far: THAT.',

    gapT='Write the missing word',
    gapHint='Look at the word in brackets. Write MY, YOUR, HIS, HER, ITS, OUR or THEIR.',
    g1w='I → MY: "MY name is Mia."',
    g2w='you → YOUR: "What is YOUR name?"',
    g3w='we → OUR: "OUR house has a big garden."',
    g4w='he → HIS: "Leo loves HIS dog."',
    g5w='she → HER: "Mia brushes HER cat."',
    g6w='it → ITS: the leaves belong to the tree. No apostrophe!',

    sortT='His or her?',
    sortHint='Look at the owner. Put each pet in the right box.',
    binA='HIS', binB='HER',
    sortWhy='Leo, Grandpa, Dad and Mr Brown are boys and men: HIS. Mia, Mum, Ella and Grandma are girls and women: HER. The animal does not matter.',

    orderT='Make the sentence',
    orderHint='Tap the words in the right order. One word is extra!',
    o1w='"This is OUR rabbit." WE is the person, OUR is the owner word.',
    o2w='"That is THEIR tortoise." THEY is the people, THEIR is the owner word.',
    o3w='"HER cat is called Pepper." SHE is the girl, HER is the owner word.',

    trT='Translate the sentence',
    tw1='"Das ist meine Katze." = "This is my cat." MEIN and MEINE are both MY.',
    tw2='"Ist das dein Hund?" = "Is this your dog?" DEIN and DEINE are both YOUR.',
    tw3='"Unser Kaninchen heißt Snowy." = "Our rabbit is called Snowy." HEISST = IS CALLED.',
    tw4='"Leo liebt seinen Hund." = "Leo loves his dog." SEIN, SEINE, SEINEN are all HIS.',
    tw5='"Mia spielt mit ihrer Katze." = "Mia plays with her cat." IHR, IHRE, IHRER are all HER.',
    tw6='"Der Hund mag seinen Ball." = "The dog likes its ball." For an animal, ITS. For your own pet, HIS or HER is fine too.',
    tw7='"Ella und Sam lieben ihre Schildkröte." = "Ella and Sam love their tortoise." Two owners: THEIR.',
    tw8='"Das hier ist dein Fisch." = "This is your fish." HIER = close: THIS.',
    tw9='"Das da drüben ist unser Pferd." = "That is our horse." DA DRÜBEN = far: THAT.',

    # ── activation ───────────────────────────────────────────────────
    actTitle='Show and tell!',
    actUse='Use these words:',
    actSpeakBrief='Talk about your family and your pets — or the pet you would like to have.',
    actSpeak1='Do you have a pet? "This is my dog. His name is …"',
    actSpeak2='Talk about a friend’s or a cousin’s pet: "Her cat is … / His fish is …"',
    actSpeak3='Point at things in the room: "This is my pen. That is your bag."',
    actWriteKind='Writing · 5 sentences',
    actWriteBrief='Write five sentences about your family and pets. Use MY, HIS, HER, OUR and THEIR.',
    actPlaceholder='This is my …',

    resPerfect='Perfect! You know all the owner words.',
    resStrong='Very good! Look again at HIS and HER: who is the owner?',
    resMid='Good start! Go back to the rule slides and try again.',
    resLow='Read the cards again, slowly, then try a second time.',
)

# ══════════════════════════════════════════════════════════════════════
#  GERMAN
# ══════════════════════════════════════════════════════════════════════
T['de'] = dict(
    coverTitle='My Cat,<br><em>Your</em> Dog',
    coverSub='Possessivbegleiter — my, your, his, her, its, our, their — <br>und this / that, mit einem Übersetzungsspiel Deutsch ⇄ Englisch',
    chipLevel='A1', chipFocus='my · your · his · her', chipCount='36 Folien',
    bankLabel='Wortkasten:',

    d1t='Die Haustiere', d1n='Teil 1 · my, your, our, their',
    d2t='His, her oder its?', d2n='Teil 2 · Wem gehört es?',
    d3t='This oder that?', d3n='Teil 3 · nah und fern',
    d4t='Die Haustier-Show', d4n='Teil 4 · Übersetze!',

    e1='My · your · our · their', e2='His · her · its', e3='This · that',
    e4='Übersetzen', eR='Die Regel',

    p1t='Mia und Pepper', p2t='Leo und Biscuit', p3t='Hier oder da drüben?',
    p4t='Die Haustier-Show in der Schule',

    tAt='Wem gehört es?',
    tA1='Es gehört mir.',
    tA2='Es gehört der Person, mit der ich spreche.',
    tA3='Es gehört mir und anderen Leuten.',
    tA4='Es gehört anderen Leuten.',

    tBt='His, her oder its?',
    tB1='Es gehört einem Jungen oder einem Mann.',
    tB2='Es gehört einem Mädchen oder einer Frau.',
    tB3='Es gehört einem Tier oder einer Sache.',

    tCt='Drei Tipps',
    tC1='Auf Deutsch sagst du MEIN Hund, MEINE Katze, MEINE Hunde. Auf Englisch heißt es immer MY. Es ändert sich nie!',
    tC2='HIS oder HER? Schau auf den BESITZER, nicht auf das Tier. Der Hund eines Mädchens ist HER dog.',
    tC3='ITS = es gehört ihm. IT’S = it is (es ist). Beim Besitzer kein Apostroph!',

    tDt='So geht das Spiel',
    tD1='Lies den deutschen Satz. Schreib ihn auf Englisch.',
    tD2='Tippe oben auf den Schalter. Jetzt liest du Englisch und schreibst Deutsch.',
    tD3='Drück auf „Prüfen“. Vergleiche deinen Satz mit der Lösung.',

    matchT='Finde den Partner',
    matchHint='Tippe links auf ein Wort und dann rechts auf seinen Partner.',
    matchW='I → MY, you → YOUR, he → HIS, she → HER, it → ITS, we → OUR, they → THEIR.',

    mcT='Wähle das richtige Wort', mc3T='Nah oder fern?',
    q1w='Mia spricht über ihre eigene Katze. Darum sagt sie MY.',
    q2w='Leo spricht MIT Mia. Die Katze gehört der Person, mit der er spricht: YOUR.',
    q3w='Mama und Papa sprechen über sich und die Familie: WE → OUR.',
    q4w='Die Besitzer sind Ella und Sam — zwei andere Leute: THEY → THEIR.',
    q5w='Der Besitzer ist Leo, ein Junge: HIS dog.',
    q6w='Die Besitzerin ist Mama, eine Frau: HER horse.',
    q7w='Der Garten gehört dem Haus — einer Sache: ITS. „It’s“ heißt „it is“.',
    c8='Mia hält Snowy im Arm.',
    c9='Opas Pferd ist weit weg, auf der Wiese.',
    c10='Leos Hund sitzt direkt neben ihm.',
    c11='Der Goldfisch ist da drüben, auf dem Lehrerpult.',
    q8w='Snowy ist ganz nah — in Mias Arm. Nah: THIS.',
    q9w='Das Pferd ist weit weg. Fern: THAT.',
    q10w='Der Hund ist direkt neben Leo. Nah: THIS.',
    q11w='Der Goldfisch ist da drüben. Fern: THAT.',

    gapT='Schreib das fehlende Wort',
    gapHint='Schau auf das Wort in Klammern. Schreib MY, YOUR, HIS, HER, ITS, OUR oder THEIR.',
    g1w='I → MY: „MY name is Mia.“',
    g2w='you → YOUR: „What is YOUR name?“',
    g3w='we → OUR: „OUR house has a big garden.“',
    g4w='he → HIS: „Leo loves HIS dog.“',
    g5w='she → HER: „Mia brushes HER cat.“',
    g6w='it → ITS: Die Blätter gehören dem Baum. Kein Apostroph!',

    sortT='His oder her?',
    sortHint='Schau auf den Besitzer. Leg jedes Tier in die richtige Box.',
    binA='HIS', binB='HER',
    sortWhy='Leo, Opa, Papa und Mr Brown sind Jungen und Männer: HIS. Mia, Mama, Ella und Oma sind Mädchen und Frauen: HER. Das Tier ist egal.',

    orderT='Bau den Satz',
    orderHint='Tippe die Wörter in der richtigen Reihenfolge an. Ein Wort ist zu viel!',
    o1w='„This is OUR rabbit.“ WE ist die Person, OUR ist das Besitzwort.',
    o2w='„That is THEIR tortoise.“ THEY sind die Leute, THEIR ist das Besitzwort.',
    o3w='„HER cat is called Pepper.“ SHE ist das Mädchen, HER ist das Besitzwort.',

    trT='Übersetze den Satz',
    tw1='„Das ist meine Katze.“ = „This is my cat.“ MEIN und MEINE sind beide MY.',
    tw2='„Ist das dein Hund?“ = „Is this your dog?“ DEIN und DEINE sind beide YOUR.',
    tw3='„Unser Kaninchen heißt Snowy.“ = „Our rabbit is called Snowy.“ HEISST = IS CALLED.',
    tw4='„Leo liebt seinen Hund.“ = „Leo loves his dog.“ SEIN, SEINE, SEINEN sind alle HIS.',
    tw5='„Mia spielt mit ihrer Katze.“ = „Mia plays with her cat.“ IHR, IHRE, IHRER sind alle HER.',
    tw6='„Der Hund mag seinen Ball.“ = „The dog likes its ball.“ Für ein Tier: ITS. Für dein eigenes Haustier geht auch HIS oder HER.',
    tw7='„Ella und Sam lieben ihre Schildkröte.“ = „Ella and Sam love their tortoise.“ Zwei Besitzer: THEIR.',
    tw8='„Das hier ist dein Fisch.“ = „This is your fish.“ HIER = nah: THIS.',
    tw9='„Das da drüben ist unser Pferd.“ = „That is our horse.“ DA DRÜBEN = fern: THAT.',

    actTitle='Zeig und erzähl!',
    actUse='Benutze diese Wörter:',
    actSpeakBrief='Erzähl von deiner Familie und deinen Haustieren — oder von dem Haustier, das du gern hättest.',
    actSpeak1='Hast du ein Haustier? „This is my dog. His name is …“',
    actSpeak2='Erzähl vom Haustier eines Freundes oder einer Cousine: „Her cat is … / His fish is …“',
    actSpeak3='Zeig auf Sachen im Raum: „This is my pen. That is your bag.“',
    actWriteKind='Schreiben · 5 Sätze',
    actWriteBrief='Schreib fünf Sätze über deine Familie und deine Haustiere. Benutze MY, HIS, HER, OUR und THEIR.',
    actPlaceholder='This is my …',

    resPerfect='Perfekt! Du kennst alle Besitzwörter.',
    resStrong='Sehr gut! Schau dir HIS und HER noch einmal an: Wer ist der Besitzer?',
    resMid='Guter Anfang! Geh zurück zu den Regel-Folien und versuch es noch einmal.',
    resLow='Lies die Karten noch einmal langsam und versuch es dann ein zweites Mal.',
)

# ══════════════════════════════════════════════════════════════════════
#  SPANISH
# ══════════════════════════════════════════════════════════════════════
T['es'] = dict(
    coverTitle='My Cat,<br><em>Your</em> Dog',
    coverSub='Adjetivos posesivos — my, your, his, her, its, our, their — <br>y this / that, con un juego de traducción alemán ⇄ inglés',
    chipLevel='A1', chipFocus='my · your · his · her', chipCount='36 diapositivas',
    bankLabel='Banco de palabras:',

    d1t='Las mascotas', d1n='Parte 1 · my, your, our, their',
    d2t='¿His, her o its?', d2n='Parte 2 · ¿de quién es?',
    d3t='¿This o that?', d3n='Parte 3 · cerca y lejos',
    d4t='El concurso de mascotas', d4n='Parte 4 · ¡tradúcelo!',

    e1='My · your · our · their', e2='His · her · its', e3='This · that',
    e4='Traducir', eR='La regla',

    p1t='Mia y Pepper', p2t='Leo y Biscuit', p3t='¿Aquí o allí?',
    p4t='El concurso de mascotas del colegio',

    tAt='¿De quién es?',
    tA1='Es mío.',
    tA2='Es de la persona con la que hablo.',
    tA3='Es mío y de otras personas.',
    tA4='Es de otras personas.',

    tBt='¿His, her o its?',
    tB1='Es de un niño o de un hombre.',
    tB2='Es de una niña o de una mujer.',
    tB3='Es de un animal o de una cosa.',

    tCt='Tres consejos',
    tC1='En español dices MI perro y MIS perros. En inglés siempre es MY: MY dog, MY dogs. ¡Nunca cambia!',
    tC2='¿HIS o HER? Mira al DUEÑO, no al animal. El perro de una niña es HER dog.',
    tC3='ITS = es suyo (de una cosa o un animal). IT’S = it is (es). ¡Sin apóstrofo para el dueño!',

    tDt='Cómo funciona el juego',
    tD1='Lee la frase en alemán. Escríbela en inglés.',
    tD2='Toca el interruptor de arriba. Ahora lee el inglés y escríbelo en alemán.',
    tD3='Pulsa «Comprobar». Compara tu frase con la respuesta.',

    matchT='Encuentra la pareja',
    matchHint='Toca una palabra a la izquierda y luego su pareja a la derecha.',
    matchW='I → MY, you → YOUR, he → HIS, she → HER, it → ITS, we → OUR, they → THEIR.',

    mcT='Elige la palabra correcta', mc3T='¿Cerca o lejos?',
    q1w='Mia habla de su propia gata, así que dice MY.',
    q2w='Leo habla CON Mia. La gata es de la persona con la que habla: YOUR.',
    q3w='Mamá y papá hablan de sí mismos y de la familia: WE → OUR.',
    q4w='Los dueños son Ella y Sam, otras dos personas: THEY → THEIR.',
    q5w='El dueño es Leo, un niño: HIS dog.',
    q6w='La dueña es mamá, una mujer: HER horse.',
    q7w='El jardín es de la casa, una cosa: ITS. "It’s" significa "it is".',
    c8='Mia tiene a Snowy en brazos.',
    c9='El caballo del abuelo está lejos, en el campo.',
    c10='El perro de Leo está sentado a su lado.',
    c11='El pez está allí, en la mesa del profesor.',
    q8w='Snowy está muy cerca, en los brazos de Mia. Cerca: THIS.',
    q9w='El caballo está lejos. Lejos: THAT.',
    q10w='El perro está justo al lado de Leo. Cerca: THIS.',
    q11w='El pez está allí. Lejos: THAT.',

    gapT='Escribe la palabra que falta',
    gapHint='Mira la palabra entre paréntesis. Escribe MY, YOUR, HIS, HER, ITS, OUR o THEIR.',
    g1w='I → MY: "MY name is Mia."',
    g2w='you → YOUR: "What is YOUR name?"',
    g3w='we → OUR: "OUR house has a big garden."',
    g4w='he → HIS: "Leo loves HIS dog."',
    g5w='she → HER: "Mia brushes HER cat."',
    g6w='it → ITS: las hojas son del árbol. ¡Sin apóstrofo!',

    sortT='¿His o her?',
    sortHint='Mira al dueño. Pon cada mascota en la caja correcta.',
    binA='HIS', binB='HER',
    sortWhy='Leo, el abuelo, papá y Mr Brown son niños y hombres: HIS. Mia, mamá, Ella y la abuela son niñas y mujeres: HER. El animal no importa.',

    orderT='Forma la frase',
    orderHint='Toca las palabras en el orden correcto. ¡Sobra una palabra!',
    o1w='"This is OUR rabbit." WE es la persona, OUR es la palabra del dueño.',
    o2w='"That is THEIR tortoise." THEY son las personas, THEIR es la palabra del dueño.',
    o3w='"HER cat is called Pepper." SHE es la niña, HER es la palabra del dueño.',

    trT='Traduce la frase',
    tw1='"Das ist meine Katze." = "This is my cat." MEIN y MEINE son las dos MY.',
    tw2='"Ist das dein Hund?" = "Is this your dog?" DEIN y DEINE son las dos YOUR.',
    tw3='"Unser Kaninchen heißt Snowy." = "Our rabbit is called Snowy." HEISST = IS CALLED.',
    tw4='"Leo liebt seinen Hund." = "Leo loves his dog." SEIN, SEINE y SEINEN son todas HIS.',
    tw5='"Mia spielt mit ihrer Katze." = "Mia plays with her cat." IHR, IHRE e IHRER son todas HER.',
    tw6='"Der Hund mag seinen Ball." = "The dog likes its ball." Para un animal, ITS. Para tu propia mascota también vale HIS o HER.',
    tw7='"Ella und Sam lieben ihre Schildkröte." = "Ella and Sam love their tortoise." Dos dueños: THEIR.',
    tw8='"Das hier ist dein Fisch." = "This is your fish." HIER = cerca: THIS.',
    tw9='"Das da drüben ist unser Pferd." = "That is our horse." DA DRÜBEN = lejos: THAT.',

    actTitle='¡Enseña y cuenta!',
    actUse='Usa estas palabras:',
    actSpeakBrief='Habla de tu familia y de tus mascotas, o de la mascota que te gustaría tener.',
    actSpeak1='¿Tienes mascota? "This is my dog. His name is …"',
    actSpeak2='Habla de la mascota de un amigo o de una prima: "Her cat is … / His fish is …"',
    actSpeak3='Señala cosas de la clase: "This is my pen. That is your bag."',
    actWriteKind='Escritura · 5 frases',
    actWriteBrief='Escribe cinco frases sobre tu familia y tus mascotas. Usa MY, HIS, HER, OUR y THEIR.',
    actPlaceholder='This is my …',

    resPerfect='¡Perfecto! Conoces todas las palabras de dueño.',
    resStrong='¡Muy bien! Mira otra vez HIS y HER: ¿quién es el dueño?',
    resMid='¡Buen comienzo! Vuelve a las diapositivas de la regla e inténtalo otra vez.',
    resLow='Lee las tarjetas otra vez, despacio, y luego inténtalo una segunda vez.',
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
