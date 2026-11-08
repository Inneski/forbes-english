# -*- coding: utf-8 -*-
"""Interface strings for Money Affirmations: Mindset or Magic? (B1).
English, German, Spanish.

What translates (HOUSE-STYLE §8): the chrome, titles, eyebrows, every rule
bullet, the vocabulary meanings, every explanation, the task instructions,
the sort bins. What does not: stems, options, gap sentences, the order
pieces, the match items, the English examples, the survey answers and the
speech-bubble prompts — those are the English being practised.

Grammar words in CAPS, cited words in double quotes, as in the other decks.
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
    coverTitle='Money <em>Affirmations</em>',
    coverSub='Mindset or magic? The words people use about money, the verb patterns inside affirmations (DESERVE TO, AFFORD TO, WORTHY OF), and how to turn a wish into a plan with GOING TO, WILL and BY.',
    chipLevel='B1', chipFocus='money words · verb patterns · wish or plan', chipCount='25 slides',

    eW='Warm-up', eT='Let’s talk', eR='The rule', eV='Vocabulary',
    e1='Money words', e2='Verb patterns', e3='Wish or plan?',

    svT='Top five', svHint='Guess the five answers we expect most as a class, then click a card to check.',
    tk1T='Let’s talk!', tk2T='Let’s talk!',
    svQ='Ask people what they would do with more money. What are the top five answers?',

    vAt='Money words (1)',
    vA1='A source of money: a job, rent from a flat, sales from an online shop.',
    vA2='The money you earn or charge for one hour of work.',
    vA3='Money you keep and do not spend, often in a bank.',
    vBt='Money words (2)',
    vB1='Money you owe to a bank, a shop or a person.',
    vB2='Having enough money that you never have to worry about it.',
    vB3='The feeling that there is never enough, even when there is. Its opposite is an ABUNDANCE MINDSET.',

    matchT='Money verbs and nouns', matchHint='Click a verb, then the words that go with it.',
    matchW='These pairs are collocations: words that are normally used together. You PAY OFF a loan (all of it, until it is finished), SET a budget, OPEN an account, CHARGE a fee, GET a pay rise and GO INTO debt.',

    mcT='Choose the best answer',
    q1w='Three different sources of money = three INCOME STREAMS. An HOURLY RATE is the price of one hour; it is not where the money comes from.',
    q2w='PAY OFF = pay all of a loan or debt until nothing is left. You GO INTO debt and SET UP an account; you do not "charge for" a loan you owe.',
    q3w='Always feeling there is not enough money = a SCARCITY MINDSET. An ABUNDANCE MINDSET is the opposite feeling.',

    rBt='The verb patterns inside affirmations',
    rB1='After DESERVE and AFFORD: TO + the base verb.',
    rB2='They can also take a noun: DESERVE A REST, AFFORD A HOLIDAY.',
    rB3='WORTHY OF + a noun or -ING. After a preposition, a verb always takes -ING.',
    rB4='Not "worthy to earn", and never OF + the base verb.',
    rB5='ATTRACT takes its object directly: no TO, no FOR.',
    rB6='Money verbs and their prepositions: SPEND ON, SAVE FOR, INVEST IN, PAY FOR.',

    q4w='CAN’T AFFORD + TO + base verb: "can’t afford to buy". AFFORD does not take -ING, and it has no FOR.',
    q5w='WORTHY OF + -ING: "worthy of earning". After the preposition OF, the verb takes -ING.',
    q6w='You SPEND money ON something. FOR is for SAVE FOR and PAY FOR; IN is for INVEST IN.',

    gapT='Write the missing words',
    gHintB='Write a preposition, or TO + the verb in brackets.',
    g1w='SAVE FOR = keep money for something you want to buy later. SAVE UP FOR is also correct.',
    g2w='DESERVE + TO + base verb: "deserve to have".',
    g3w='INVEST IN: you put money IN something.',

    rCt='A wish or a plan?',
    rC1='It speaks as if the wish is already true, now.',
    rC2='PRESENT SIMPLE for a state, PRESENT CONTINUOUS for something happening now.',
    rC3='It has no action and no date, so nobody can check it.',
    rC4='GOING TO for a decision you have already made.',
    rC5='WILL for a promise or a decision you make as you speak.',
    rC6='BY + a date = at the latest. Now you can check it.',

    sortT='Affirmation or plan?', sortHint='Put each sentence in the right box.',
    binA='Affirmation', binP='Plan',
    sortW='An affirmation is in the present and says the wish is already true. A plan uses GOING TO, WILL or the PRESENT CONTINUOUS for an arrangement, and usually has a date or an action you can check.',

    q7w='"I’ve decided" = a plan made before now: AM GOING TO SAVE. WAS GOING TO says the plan did not happen; HAVE BEEN SAVING and WOULD HAVE SAVED do not fit a future plan.',
    q8w='BY + a date = at the latest. PAY OFF is one finished action, so UNTIL (which needs an action that continues) does not work. SINCE and FOR look back from now.',
    s9='Which sentence is a plan you can check?',
    q9w='Only one sentence has an action (SAVE), an amount and a date (BY JUNE). The others say the wish is already true, so nothing can be checked.',

    orderT='Build the sentence', orderHint='Click the pieces in order. One piece is left over.',
    o1w='PAY OFF is one finished action, so it takes BY + a date: "by July". "Until July" is left over.',
    o2w='DESERVE + TO + base verb: "deserve to take". "Taking" is left over.',

    gHintC='Turn each affirmation into a plan. Use the verb in brackets.',
    g4w='A decision about the future: AM GOING TO ASK (or WILL ASK).',
    g5w='BY + a date = at the latest: the loan will be finished by December.',
    g6w='A plan: AM GOING TO APPLY, WILL APPLY, or AM APPLYING if it is already arranged.',

    actTitle='From wish to plan',
    actUse='Use at least three:',
    actSpeakBrief='In pairs. One of you believes in money affirmations. The other only believes in plans.',
    actSpeak1='Believer: say three affirmations you repeat every morning and explain why they help you.',
    actSpeak2='Planner: turn each one into a plan with GOING TO or WILL and BY + a date.',
    actSpeak3='Together: agree on one affirmation and one plan you would both keep. Use DESERVE TO or CAN AFFORD TO.',
    actWriteKind='Writing',
    actWriteBrief='A friend has just paid £300 for an online course called "Manifest a Million". Write them a message (150–200 words): what could be useful in it, what worries you, and a real money plan with GOING TO, WILL and BY.',
    actPlaceholder='Hi Sam, …',
)

# ══════════════════════════════════════════════════════════════════════
#  GERMAN
# ══════════════════════════════════════════════════════════════════════
T['de'] = dict(
    coverTitle='Money <em>Affirmations</em>',
    coverSub='Denkweise oder Magie? Wörter rund ums Geld, die Verbmuster in Affirmationen (DESERVE TO, AFFORD TO, WORTHY OF) und wie aus einem Wunsch ein Plan mit GOING TO, WILL und BY wird.',
    chipLevel='B1', chipFocus='Geldwörter · Verbmuster · Wunsch oder Plan', chipCount='25 Folien',

    eW='Zum Einstieg', eT='Sprechen wir!', eR='Die Regel', eV='Wortschatz',
    e1='Geldwörter', e2='Verbmuster', e3='Wunsch oder Plan?',

    svT='Die Top fünf', svHint='Ratet gemeinsam die fünf Antworten, die wir am häufigsten erwarten, dann klickt auf eine Karte zum Prüfen.',
    tk1T='Sprechen wir!', tk2T='Sprechen wir!',
    svQ='Frag Leute, was sie mit mehr Geld machen würden. Was sind die fünf häufigsten Antworten?',

    vAt='Geldwörter (1)',
    vA1='Eine Geldquelle: ein Job, Miete aus einer Wohnung, Verkäufe aus einem Onlineshop.',
    vA2='Das Geld, das man für eine Stunde Arbeit verdient oder verlangt.',
    vA3='Geld, das man behält und nicht ausgibt, oft auf der Bank.',
    vBt='Geldwörter (2)',
    vB1='Geld, das man einer Bank, einem Geschäft oder einer Person schuldet.',
    vB2='So viel Geld haben, dass man sich nie Sorgen darum machen muss.',
    vB3='Das Gefühl, dass es nie genug gibt, auch wenn genug da ist. Das Gegenteil ist ein ABUNDANCE MINDSET.',

    matchT='Geldverben und -nomen', matchHint='Klicke auf ein Verb, dann auf die Wörter, die dazu passen.',
    matchW='Diese Paare sind Kollokationen: Wörter, die normalerweise zusammen stehen. Man sagt PAY OFF a loan (ganz abbezahlen), SET a budget, OPEN an account, CHARGE a fee, GET a pay rise und GO INTO debt.',

    mcT='Wähle die beste Antwort',
    q1w='Drei verschiedene Geldquellen = drei INCOME STREAMS. Eine HOURLY RATE ist der Preis für eine Stunde, nicht die Quelle des Geldes.',
    q2w='PAY OFF = einen Kredit oder eine Schuld ganz abbezahlen. In Schulden gerät man mit GO INTO, ein Konto eröffnet man mit SET UP; "charge for" passt nicht zu einem Kredit, den man schuldet.',
    q3w='Immer das Gefühl, dass das Geld nicht reicht = ein SCARCITY MINDSET. Ein ABUNDANCE MINDSET ist das Gegenteil.',

    rBt='Die Verbmuster in Affirmationen',
    rB1='Nach DESERVE und AFFORD: TO + Grundform des Verbs.',
    rB2='Sie können auch ein Nomen haben: DESERVE A REST, AFFORD A HOLIDAY.',
    rB3='WORTHY OF + Nomen oder -ING. Nach einer Präposition steht ein Verb immer mit -ING.',
    rB4='Nicht "worthy to earn" und nie OF + Grundform.',
    rB5='ATTRACT hat ein direktes Objekt: kein TO, kein FOR.',
    rB6='Geldverben und ihre Präpositionen: SPEND ON, SAVE FOR, INVEST IN, PAY FOR.',

    q4w='CAN’T AFFORD + TO + Grundform: "can’t afford to buy". AFFORD steht nicht mit -ING und hat kein FOR.',
    q5w='WORTHY OF + -ING: "worthy of earning". Nach der Präposition OF steht das Verb mit -ING.',
    q6w='Man gibt Geld für etwas aus: SPEND ON. FOR gehört zu SAVE FOR und PAY FOR, IN zu INVEST IN.',

    gapT='Ergänze die fehlenden Wörter',
    gHintB='Schreib eine Präposition oder TO + das Verb in Klammern.',
    g1w='SAVE FOR = Geld für etwas zurücklegen, das man später kaufen will. SAVE UP FOR ist auch richtig.',
    g2w='DESERVE + TO + Grundform: "deserve to have".',
    g3w='INVEST IN: Man steckt Geld IN etwas.',

    rCt='Ein Wunsch oder ein Plan?',
    rC1='Sie spricht so, als wäre der Wunsch schon jetzt wahr.',
    rC2='PRESENT SIMPLE für einen Zustand, PRESENT CONTINUOUS für etwas, das gerade passiert.',
    rC3='Sie hat keine Handlung und kein Datum, also kann niemand sie überprüfen.',
    rC4='GOING TO für eine Entscheidung, die schon getroffen ist.',
    rC5='WILL für ein Versprechen oder eine Entscheidung im Moment des Sprechens.',
    rC6='BY + Datum = spätestens dann. Jetzt kann man es überprüfen.',

    sortT='Affirmation oder Plan?', sortHint='Ordne jeden Satz der richtigen Box zu.',
    binA='Affirmation', binP='Plan',
    sortW='Eine Affirmation steht in der Gegenwart und sagt, dass der Wunsch schon wahr ist. Ein Plan benutzt GOING TO, WILL oder das PRESENT CONTINUOUS für eine Verabredung und hat meist ein Datum oder eine Handlung, die man überprüfen kann.',

    q7w='"I’ve decided" = ein schon gefasster Plan: AM GOING TO SAVE. WAS GOING TO heißt, dass der Plan nicht umgesetzt wurde; HAVE BEEN SAVING und WOULD HAVE SAVED passen nicht zu einem Zukunftsplan.',
    q8w='BY + Datum = spätestens dann. PAY OFF ist eine abgeschlossene Handlung, also passt UNTIL (das eine andauernde Handlung braucht) nicht. SINCE und FOR blicken von jetzt zurück.',
    s9='Welcher Satz ist ein Plan, den man überprüfen kann?',
    q9w='Nur ein Satz hat eine Handlung (SAVE), einen Betrag und ein Datum (BY JUNE). Die anderen sagen, dass der Wunsch schon wahr ist, also kann man nichts überprüfen.',

    orderT='Bilde den Satz', orderHint='Klicke die Teile in der richtigen Reihenfolge an. Ein Teil bleibt übrig.',
    o1w='PAY OFF ist eine abgeschlossene Handlung, also BY + Datum: "by July". "Until July" bleibt übrig.',
    o2w='DESERVE + TO + Grundform: "deserve to take". "Taking" bleibt übrig.',

    gHintC='Mach aus jeder Affirmation einen Plan. Benutze das Verb in Klammern.',
    g4w='Eine Entscheidung über die Zukunft: AM GOING TO ASK (oder WILL ASK).',
    g5w='BY + Datum = spätestens dann: Bis Dezember ist der Kredit abbezahlt.',
    g6w='Ein Plan: AM GOING TO APPLY, WILL APPLY oder AM APPLYING, wenn es schon verabredet ist.',

    actTitle='Vom Wunsch zum Plan',
    actUse='Benutze mindestens drei:',
    actSpeakBrief='Zu zweit. Eine Person glaubt an Geld-Affirmationen, die andere glaubt nur an Pläne.',
    actSpeak1='Gläubige Person: Nenne drei Affirmationen, die du jeden Morgen sagst, und erkläre, warum sie dir helfen.',
    actSpeak2='Planende Person: Mach aus jeder einen Plan mit GOING TO oder WILL und BY + Datum.',
    actSpeak3='Gemeinsam: Einigt euch auf eine Affirmation und einen Plan, die ihr beide behalten würdet. Benutzt DESERVE TO oder CAN AFFORD TO.',
    actWriteKind='Schreiben',
    actWriteBrief='Ein Freund hat gerade 300 £ für einen Onlinekurs namens "Manifest a Million" bezahlt. Schreib ihm eine Nachricht (150–200 Wörter): was daran nützlich sein könnte, was dir Sorgen macht und einen echten Geldplan mit GOING TO, WILL und BY.',
    actPlaceholder='Hi Sam, …',
)

# ══════════════════════════════════════════════════════════════════════
#  SPANISH
# ══════════════════════════════════════════════════════════════════════
T['es'] = dict(
    coverTitle='Money <em>Affirmations</em>',
    coverSub='¿Mentalidad o magia? Las palabras que usamos para hablar de dinero, los patrones verbales de las afirmaciones (DESERVE TO, AFFORD TO, WORTHY OF) y cómo convertir un deseo en un plan con GOING TO, WILL y BY.',
    chipLevel='B1', chipFocus='palabras de dinero · patrones verbales · deseo o plan', chipCount='25 diapositivas',

    eW='Para empezar', eT='¡Hablemos!', eR='La regla', eV='Vocabulario',
    e1='Palabras de dinero', e2='Patrones verbales', e3='¿Deseo o plan?',

    svT='Las cinco primeras', svHint='Adivinad en clase las cinco respuestas que más esperamos y luego haced clic en una tarjeta para comprobarla.',
    tk1T='¡Hablemos!', tk2T='¡Hablemos!',
    svQ='Pregunta a la gente qué haría con más dinero. ¿Cuáles son las cinco respuestas más comunes?',

    vAt='Palabras de dinero (1)',
    vA1='Una fuente de dinero: un trabajo, el alquiler de un piso, las ventas de una tienda online.',
    vA2='El dinero que ganas o cobras por una hora de trabajo.',
    vA3='Dinero que guardas y no gastas, a menudo en el banco.',
    vBt='Palabras de dinero (2)',
    vB1='Dinero que debes a un banco, a una tienda o a una persona.',
    vB2='Tener tanto dinero que nunca tienes que preocuparte por él.',
    vB3='La sensación de que nunca hay suficiente, aunque lo haya. Lo contrario es un ABUNDANCE MINDSET.',

    matchT='Verbos y sustantivos de dinero', matchHint='Haz clic en un verbo y luego en las palabras que van con él.',
    matchW='Estos pares son colocaciones: palabras que normalmente van juntas. Se dice PAY OFF a loan (pagarlo entero), SET a budget, OPEN an account, CHARGE a fee, GET a pay rise y GO INTO debt.',

    mcT='Elige la mejor respuesta',
    q1w='Tres fuentes de dinero distintas = tres INCOME STREAMS. Una HOURLY RATE es el precio de una hora, no el origen del dinero.',
    q2w='PAY OFF = pagar un préstamo o una deuda hasta que no quede nada. Te endeudas con GO INTO y abres una cuenta con SET UP; "charge for" no sirve para un préstamo que debes.',
    q3w='Sentir siempre que no hay dinero suficiente = un SCARCITY MINDSET. Un ABUNDANCE MINDSET es lo contrario.',

    rBt='Los patrones verbales de las afirmaciones',
    rB1='Después de DESERVE y AFFORD: TO + el verbo en forma base.',
    rB2='También pueden llevar un sustantivo: DESERVE A REST, AFFORD A HOLIDAY.',
    rB3='WORTHY OF + sustantivo o -ING. Después de una preposición, el verbo siempre va en -ING.',
    rB4='No "worthy to earn", y nunca OF + forma base.',
    rB5='ATTRACT lleva el objeto directamente: sin TO, sin FOR.',
    rB6='Verbos de dinero y sus preposiciones: SPEND ON, SAVE FOR, INVEST IN, PAY FOR.',

    q4w='CAN’T AFFORD + TO + forma base: "can’t afford to buy". AFFORD no va con -ING y no lleva FOR.',
    q5w='WORTHY OF + -ING: "worthy of earning". Después de la preposición OF, el verbo va en -ING.',
    q6w='El dinero se gasta EN algo: SPEND ON. FOR va con SAVE FOR y PAY FOR; IN va con INVEST IN.',

    gapT='Escribe las palabras que faltan',
    gHintB='Escribe una preposición, o TO + el verbo entre paréntesis.',
    g1w='SAVE FOR = guardar dinero para algo que quieres comprar más tarde. SAVE UP FOR también es correcto.',
    g2w='DESERVE + TO + forma base: "deserve to have".',
    g3w='INVEST IN: pones dinero EN algo.',

    rCt='¿Un deseo o un plan?',
    rC1='Habla como si el deseo ya fuera verdad, ahora.',
    rC2='PRESENT SIMPLE para un estado, PRESENT CONTINUOUS para algo que está pasando ahora.',
    rC3='No tiene acción ni fecha, así que nadie puede comprobarla.',
    rC4='GOING TO para una decisión que ya has tomado.',
    rC5='WILL para una promesa o una decisión que tomas mientras hablas.',
    rC6='BY + una fecha = como muy tarde. Ahora sí se puede comprobar.',

    sortT='¿Afirmación o plan?', sortHint='Pon cada frase en la caja correcta.',
    binA='Afirmación', binP='Plan',
    sortW='Una afirmación está en presente y dice que el deseo ya es verdad. Un plan usa GOING TO, WILL o el PRESENT CONTINUOUS para algo acordado, y suele tener una fecha o una acción que se puede comprobar.',

    q7w='"I’ve decided" = un plan ya tomado: AM GOING TO SAVE. WAS GOING TO dice que el plan no se cumplió; HAVE BEEN SAVING y WOULD HAVE SAVED no encajan con un plan de futuro.',
    q8w='BY + una fecha = como muy tarde. PAY OFF es una acción terminada, así que UNTIL (que necesita una acción que continúa) no funciona. SINCE y FOR miran hacia atrás desde ahora.',
    s9='¿Qué frase es un plan que se puede comprobar?',
    q9w='Solo una frase tiene una acción (SAVE), una cantidad y una fecha (BY JUNE). Las otras dicen que el deseo ya es verdad, así que no hay nada que comprobar.',

    orderT='Construye la frase', orderHint='Haz clic en las piezas en orden. Sobra una pieza.',
    o1w='PAY OFF es una acción terminada, así que lleva BY + fecha: "by July". Sobra "until July".',
    o2w='DESERVE + TO + forma base: "deserve to take". Sobra "taking".',

    gHintC='Convierte cada afirmación en un plan. Usa el verbo entre paréntesis.',
    g4w='Una decisión sobre el futuro: AM GOING TO ASK (o WILL ASK).',
    g5w='BY + una fecha = como muy tarde: en diciembre el préstamo estará pagado.',
    g6w='Un plan: AM GOING TO APPLY, WILL APPLY, o AM APPLYING si ya está acordado.',

    actTitle='Del deseo al plan',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas. Una persona cree en las afirmaciones sobre el dinero; la otra solo cree en los planes.',
    actSpeak1='Creyente: di tres afirmaciones que repites cada mañana y explica por qué te ayudan.',
    actSpeak2='Planificador: convierte cada una en un plan con GOING TO o WILL y BY + una fecha.',
    actSpeak3='Juntos: poneos de acuerdo en una afirmación y un plan que los dos mantendríais. Usad DESERVE TO o CAN AFFORD TO.',
    actWriteKind='Escritura',
    actWriteBrief='Un amigo acaba de pagar 300 £ por un curso online llamado "Manifest a Million". Escríbele un mensaje (150–200 palabras): qué podría ser útil, qué te preocupa y un plan real de dinero con GOING TO, WILL y BY.',
    actPlaceholder='Hola, Sam: …',
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
