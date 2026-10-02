# -*- coding: utf-8 -*-
"""Spanish strings for The School Visit: Correction Test. See i18n_schoolvisit.py.

Written in-session, "tú" as the course chrome; no native check yet. Every
cited English form stays in English. The four "ask the author" prompts are
the original Spanish prompts from the test sheet."""
T = dict(
    coverTitle='La visita al colegio: <em>test de corrección</em>',
    coverSub='Invitan a una autora a hablar de su libro en una clase — veintisiete cosas que corregir antes de ir',
    chipLevel='A2–B1 · Preintermedio', chipFocus='Corrección de errores',
    chipCount='32 diapositivas',

    d1t='Corrige los errores', d1n='Parte 1 · diez frases, un error en cada una',
    d2t='Completa las frases', d2n='Parte 2 · ocho huecos',
    d3t='Pregunta a la autora', d3n='Parte 3 · cuatro preguntas de los niños',
    d4t='Elige la expresión correcta', d4n='Parte 4 · cinco decisiones rápidas',

    e1='Corrige los errores', e2='Completa las frases',
    e3='Pregunta a la autora', e4='Elige la expresión correcta',

    s1t='Un error en cada frase',
    s1a='La historia: mi vecina me ha pedido que hable de mi libro en su colegio. Cada frase de abajo es algo que dije sobre eso, y cada una tiene exactamente un error — del tipo que un hispanohablante comete por una razón.',
    s1b='Escribe la frase entera, corregida. Las mayúsculas no importan, un punto o una coma que falte no es un error, y donde el inglés permite más de una corrección, se aceptan todas.',

    s2t='Rellena el hueco',
    s2a='Ocho frases de la misma historia, a cada una le falta una palabra o una forma verbal. Si hay un verbo entre paréntesis, ponlo en la forma que la frase necesita.',
    s2b='Lee primero la frase entera. La pista suele estar al lado del hueco: “when I was young”, “when she … up”, “don’t … TV”.',

    s3t='Los niños tienen preguntas',
    s3a='Una clase de niños va a preguntar sobre el libro. Cada enunciado te dice, en tu idioma, lo que un niño quiere saber. Escríbelo como una pregunta natural en inglés.',
    s3b='Corto y directo está bien: los niños no preguntan con frases largas. El signo de interrogación al final da igual que esté o no.',

    s4t='Dos formas de decirlo — una es inglés',
    s4a='Cinco decisiones rápidas sobre los puntos a los que el test vuelve una y otra vez: SAY y TELL, TO y FOR, y dónde va el sujeto de una frase.',
    s4b='Elige la que es inglés correcto. La otra es lo que suele decir un estudiante.',

    aHint='Escribe la frase corregida.',
    a1t='La invitación', a2t='Un aviso', a3t='La sinopsis',
    a4t='Un libro difícil', a5t='Una página dura', a6t='El párrafo',
    a7t='El apagón', a8t='Las tardes en casa', a9t='El generador',
    a10t='El tiempo de ayer',

    a1w='WANT lleva una persona y el infinitivo con TO: “wants me to give”. En inglés no existe “wants that I”.',
    a2w='TELL lleva la persona directamente: “told me that”. SAY necesita TO antes de la persona: “said to me that”. “Said me” nunca es posible.',
    a3w='“The synopsis” es singular, así que DOESN’T. Más natural todavía: “There’s no problem with the synopsis of my book.”',
    a4w='Una negación en pasado es DIDN’T + verbo base: “didn’t understand”. “No understand” es orden de palabras español.',
    a5w='Otra vez DIDN’T + verbo base. Si el problema sigue hoy, también vale DOESN’T understand — “no understand”, nunca.',
    a6w='Una finalidad es TO + verbo (“to explain”) o FOR + -ING (“for explaining”). FOR + verbo base no existe.',
    a7w='El inglés usa una sola negación. DON’T … ANYTHING, o KNOW NOTHING — nunca “don’t … nothing”.',
    a8w='Un hábito va en Present Simple: “I don’t watch”. Y solo una negación: “don’t watch anything” o simplemente “don’t watch TV”.',
    a9w='Una frase en inglés necesita sujeto. “We have a generator in our house”, o “There is a generator in my house”. Un lugar no puede ser el sujeto de HAVE.',
    a10w='RAIN es un verbo: “it was raining” (en curso todo el día) o “it rained”. “Was rain” mezcla las dos.',

    bHint='Una respuesta por hueco. Se aceptan las contracciones habituales.',
    b1t='Preguntas desde la clase', b2t='Hacerse mayor', b3t='La televisión',
    b4t='La tormenta',

    b11w='Un momento en el futuro: WILL + verbo, “I will sweat”. WILL BE + -ING, “I will be sweating”, lo muestra en curso en ese momento — las dos son correctas.',
    b12w='“When I was young” pone la frase en pasado: HAD. “Used to have” también vale.',
    b13w='Después de WHEN en una oración temporal usamos una forma de presente para el futuro: “when she grows up”, o “when she is grown up” (GROWN-UP es un adjetivo: adulta). Nunca “will grow”.',
    b14w='Una pregunta indirecta: ASKED + persona + WHETHER (o IF). “Asked” va en pasado porque la pregunta ya se hizo.',
    b15w='Después de una negación, ANY: “don’t watch any TV”. MUCH también es correcto — “don’t watch much TV”.',
    b16w='Después de una negación, ANYTHING. “I don’t watch anything on TV” — o “much”, que también se acepta.',
    b17w='Un power CUT (británico) o un power OUTAGE (americano): se va la luz.',
    b18w='TOLD + persona: “told me she wanted”. Con SAY sería “said she wanted”, sin “me”.',

    cHint='Escribe la pregunta en inglés natural.',
    c1t='Lo que preguntan los niños', c2t='Más manos levantadas',
    c1x='¿Qué te inspiró a escribir tu libro?',
    c2x='¿De qué trata tu libro?',
    c3x='¿Los niños también pueden leer tu libro?',
    c4x='Has dicho que no. ¿Por qué no?',
    c1w='WHAT + Past Simple: “What inspired you to write your book?” INSPIRE lleva una persona y el infinitivo con TO.',
    c2w='La preposición va al final: “What’s your book about?” — nunca “About what is your book?”',
    c3w='CAN + sujeto + verbo: “Can kids read your book too?” “Too” o “as well” al final, o “also” antes del verbo.',
    c4w='“Why not?” — dos palabras. La pregunta completa, “Why can’t they?”, es la misma idea.',

    m1t='La presentación', m2t='El libro interesante', m3t='Una imagen',
    m4t='El diagrama', m5t='En casa',
    m5x='¿Cuál significa “Tenemos un generador en nuestra casa”, dicho correctamente?',
    m5s='Elige la frase correcta.',
    m1w='TELL + persona: “told me about the presentation”. SAY no puede llevar “me” directamente.',
    m2w='SAY + THAT: “said that the book was interesting”. TELL necesitaría primero una persona: “told me that”.',
    m3w='Finalidad con un verbo: TO + forma base, “to explain”. FOR + verbo base no es inglés.',
    m4w='Después de un adjetivo como USEFUL, la finalidad es FOR + -ING: “useful for explaining”. “For explain” nunca es correcto.',
    m5w='El sujeto es la gente a la que pertenece: “We have a generator in our house”. “In our house” es un lugar, no un sujeto.',

    actTitle='Tu turno: la visita al colegio',
    actUse='Usa al menos cuatro:',
    actSpeakBrief='En parejas. Uno es la autora, el otro un niño de la clase; cambiad después de tres preguntas.',
    actSpeak1='El niño pregunta de qué trata el libro, qué lo inspiró y si los niños pueden leerlo. La autora responde con frases completas.',
    actSpeak2='La autora cuenta a la clase el día en que se fue la luz en casa — qué estaba pasando, qué hizo, cómo se sintió.',
    actSpeak3='Cuenta la conversación a una tercera persona: “She asked me whether …”, “I told her that …”.',
    actWriteKind='Escritura · 80–120 palabras',
    actWriteBrief='Escribe el comienzo de tu charla a la clase: quién te pidió que fueras, de qué trata tu libro, qué te inspiró a escribirlo y si los niños pueden leerlo. Usa al menos cuatro chips.',
    actPlaceholder='Good morning, everyone. My neighbour asked me to …',
)
