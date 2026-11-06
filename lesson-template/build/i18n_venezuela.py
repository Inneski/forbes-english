# -*- coding: utf-8 -*-
"""Interface strings for Used To & Be Used To — Venezuela Edition (B1).
English, German, Spanish.

What translates (HOUSE-STYLE §8): the chrome, titles, eyebrows, every rule
bullet, the example notes and labels, every explanation, the task
instructions. What does not: stems, options, gap sentences, the order
pieces, the English example sentences, the survey answers and the
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
    coverTitle='Used To &amp; <em>Be Used To</em>',
    coverSub='Venezuela edition: USED TO for past habits and states, BE USED TO + -ING for what feels normal, and GET USED TO for the change between them.',
    chipLevel='B1', chipFocus='used to · be used to · get used to', chipCount='28 slides',

    eW='Warm-up', eT='Let’s talk', eR='The rule', eX='In context',
    e1='Used to', e2='Be used to', e3='Used to or be used to?',

    svT='Top five', svHint='Guess the five most common answers as a class, then click a card to check.',
    tk1T='Let’s talk!', tk2T='Let’s talk!',

    rAt='Used to: past habits and states',
    rA1='A past habit: it happened again and again, and it has stopped.',
    rA2='A past state: true before, not true now.',
    rA3='Not for something that is still true today.',
    rA4='The negative takes DIDN’T, and then USE, with no D.',
    rA5='The question starts with DID, and again USE, with no D.',

    xAt='Used to in Venezuela',
    xA1l='History', xA1n='A past state: it is no longer true in the same way.',
    xA2l='Nature', xA2n='"Flock" = travel in large numbers. Far fewer tourists go today.',
    xA3l='Daily life', xA3n='A repeated past habit: something done regularly.',
    xA4l='Industry', xA4n='A past state that has changed dramatically.',
    xA5l='Childhood', xA5n='Negative: something that did NOT happen regularly.',
    xA6l='Music', xA6n='A past situation: the radio culture of a whole country.',

    mcT='Choose the right form', gapT='Write the missing words',
    gHintA='Use the verb in brackets with USED TO.',
    gHintB='Use BE USED TO or GET USED TO.',

    rBt='Be used to: it feels normal',
    rB1='It feels normal and familiar: you are accustomed to it.',
    rB2='BE shows the time (AM / IS / ARE, WAS / WERE); the -ING form stays.',
    rB3='Negative: ISN’T / WASN’T USED TO. Question: ARE YOU USED TO …?',
    rB4='A noun or a pronoun can follow too: USED TO THE NOISE, USED TO IT.',
    rB5='GET USED TO is the change: slowly, it becomes normal.',

    xBt='Be used to in context',
    xB1l='Climate', xB1n='Present: it feels normal and comfortable now.',
    xB2l='Work', xB2n='Past: it was normal for them at that time.',
    xB3l='Food', xB3n='Negative: it does NOT feel normal (yet).',
    xB4l='Travel', xB4n='Question: ARE + subject + USED TO + -ING.',
    xB5l='Weather', xB5n='GOT USED TO = the change: slowly it became normal.',
    xB6l='Noise', xB6n='Present: something that feels routine.',

    rCt='Two structures, side by side',
    rC1='A past habit or state that has stopped.',
    rC2='Only about the past.',
    rC3='Always + the base verb.',
    rC4='Something that feels normal or familiar.',
    rC5='Past, present or future: BE shows the time.',
    rC6='Always + -ING, or a noun.',

    orderT='Build the sentence', orderHint='Click the pieces in order. One piece is left over.',
    o1w='DID + subject + USE TO + base verb. With DID it is USE TO, so "used to" is left over.',
    o2w='BE USED TO + -ING: "isn’t used to DRIVING". "Drive" is left over.',

    q1w='The fact is STILL true, so it is not USED TO: USED TO says something is over. HAS ALWAYS BEEN = true then, and true now.',
    q2w='A past habit that has stopped: USED TO + base verb. USE TO with no D only comes after DID, and ARE USED TO means "it feels normal".',
    q3w='USED TO + the base verb (EMPLOY) for a past state that has changed.',
    q4w='A question: DID + subject + USE TO. DID already shows the past, so it is USE, not USED.',
    q5w='Negative: DIDN’T USE TO + base verb. It did not happen then, and it happens now. "Used to not" is informal; "hasn’t used to" does not exist.',
    q6w='It feels normal NOW: ARE USED TO + -ING. USED TO on its own is a past habit and cannot take LIVING.',
    q7w='Then, it did not feel normal: WASN’T USED TO + a noun (THE NOISE). DIDN’T USE TO would need a base verb, and ISN’T is the present.',
    q8w='Normal for them in the past: WERE USED TO + -ING. "Had been their routine" puts it in the past, so not ARE.',
    q9w='FINALLY shows a change over time: GET USED TO = become used to. WAS USED TO describes the state, not the change.',
    q10w='A question about NOW: ARE + subject + USED TO + -ING. "Do … use to" is not English.',
    q11w='USED TO SWIM = a childhood habit that stopped. IS USED TO LIVING = it feels normal to her now.',
    q12w='TODAY: ARE USED TO + -ING, it is normal for them. In the 1960s, a past state that has changed: DIDN’T USE TO HAVE.',
    q13w='AREN’T USED TO + a noun (SUCH HUMIDITY): it does not feel normal. USED TO COME = a past pattern that has changed, because now they come all year.',

    g1w='A past habit or state that has stopped: USED TO + base verb.',
    g2w='Negative: DIDN’T USE TO + base verb. No D on USE after DIDN’T.',
    g3w='A question: DID + subject + USE TO + base verb.',
    g4w='It is normal for her now: IS USED TO + -ING.',
    g5w='It did not feel normal then: WASN’T USED TO + a noun.',
    g6w='The change, in the past: GOT USED TO.',

    actTitle='Then and now',
    actUse='Use at least three:',
    actSpeakBrief='In pairs. Tell your partner about a big change in your life: a new city, a new job, a new school.',
    actSpeak1='Say what you USED TO do before the change, and one thing you DIDN’T USE TO do.',
    actSpeak2='Say what you ARE USED TO now that felt strange at first. How long did it take to GET USED TO it?',
    actSpeak3='Ask your partner three questions: one with DID … USE TO and two with ARE YOU USED TO …?',
    actWriteKind='Writing',
    actWriteBrief='A friend from Venezuela is moving to your city. Email them (150–200 words): what life here USED TO be like, what people ARE USED TO, and what takes time to GET USED TO.',
    actPlaceholder='Hi Daniela, …',
)

# ══════════════════════════════════════════════════════════════════════
#  GERMAN
# ══════════════════════════════════════════════════════════════════════
T['de'] = dict(
    coverTitle='Used To &amp; <em>Be Used To</em>',
    coverSub='Venezuela-Ausgabe: USED TO für frühere Gewohnheiten und Zustände, BE USED TO + -ING für das, was sich normal anfühlt, und GET USED TO für den Wandel dazwischen.',
    chipLevel='B1', chipFocus='used to · be used to · get used to', chipCount='28 Folien',

    eW='Zum Einstieg', eT='Sprechen wir!', eR='Die Regel', eX='Im Kontext',
    e1='Used to', e2='Be used to', e3='Used to oder be used to?',

    svT='Die Top fünf', svHint='Ratet gemeinsam die fünf häufigsten Antworten, dann klickt auf eine Karte zum Prüfen.',
    tk1T='Sprechen wir!', tk2T='Sprechen wir!',

    rAt='Used to: frühere Gewohnheiten und Zustände',
    rA1='Eine frühere Gewohnheit: Sie kam immer wieder vor und hat aufgehört.',
    rA2='Ein früherer Zustand: Früher wahr, heute nicht mehr.',
    rA3='Nicht für etwas, das heute noch stimmt.',
    rA4='Die Verneinung bildet man mit DIDN’T, danach USE ohne D.',
    rA5='Die Frage beginnt mit DID, und auch hier USE ohne D.',

    xAt='Used to in Venezuela',
    xA1l='Geschichte', xA1n='Ein früherer Zustand: Heute stimmt das so nicht mehr.',
    xA2l='Natur', xA2n='"Flock" = in großen Scharen reisen. Heute kommen viel weniger Touristen.',
    xA3l='Alltag', xA3n='Eine wiederholte frühere Gewohnheit: etwas, das man regelmäßig tat.',
    xA4l='Industrie', xA4n='Ein früherer Zustand, der sich stark verändert hat.',
    xA5l='Kindheit', xA5n='Verneinung: etwas, das NICHT regelmäßig geschah.',
    xA6l='Musik', xA6n='Eine frühere Situation: die Radiokultur eines ganzen Landes.',

    mcT='Wähle die richtige Form', gapT='Ergänze die fehlenden Wörter',
    gHintA='Verwende das Verb in Klammern mit USED TO.',
    gHintB='Verwende BE USED TO oder GET USED TO.',

    rBt='Be used to: Es fühlt sich normal an',
    rB1='Es fühlt sich normal und vertraut an: Man ist daran gewöhnt.',
    rB2='BE zeigt die Zeit (AM / IS / ARE, WAS / WERE); die -ING-Form bleibt.',
    rB3='Verneinung: ISN’T / WASN’T USED TO. Frage: ARE YOU USED TO …?',
    rB4='Auch ein Nomen oder Pronomen kann folgen: USED TO THE NOISE, USED TO IT.',
    rB5='GET USED TO ist der Wandel: Nach und nach wird es normal.',

    xBt='Be used to im Kontext',
    xB1l='Klima', xB1n='Gegenwart: Es fühlt sich jetzt normal und angenehm an.',
    xB2l='Arbeit', xB2n='Vergangenheit: Damals war es für sie normal.',
    xB3l='Essen', xB3n='Verneinung: Es fühlt sich (noch) NICHT normal an.',
    xB4l='Reisen', xB4n='Frage: ARE + Subjekt + USED TO + -ING.',
    xB5l='Wetter', xB5n='GOT USED TO = der Wandel: Nach und nach wurde es normal.',
    xB6l='Lärm', xB6n='Gegenwart: etwas, das sich wie Routine anfühlt.',

    rCt='Zwei Strukturen im Vergleich',
    rC1='Eine frühere Gewohnheit oder ein Zustand, der aufgehört hat.',
    rC2='Nur über die Vergangenheit.',
    rC3='Immer + Grundform des Verbs.',
    rC4='Etwas, das sich normal oder vertraut anfühlt.',
    rC5='Vergangenheit, Gegenwart oder Zukunft: BE zeigt die Zeit.',
    rC6='Immer + -ING oder ein Nomen.',

    orderT='Bilde den Satz', orderHint='Klicke die Teile der Reihe nach an. Ein Teil bleibt übrig.',
    o1w='DID + Subjekt + USE TO + Grundform. Nach DID heißt es USE TO, also bleibt "used to" übrig.',
    o2w='BE USED TO + -ING: "isn’t used to DRIVING". "Drive" bleibt übrig.',

    q1w='Die Tatsache stimmt NOCH immer, also kein USED TO: USED TO sagt, dass etwas vorbei ist. HAS ALWAYS BEEN = damals wahr und heute wahr.',
    q2w='Eine frühere Gewohnheit, die aufgehört hat: USED TO + Grundform. USE TO ohne D steht nur nach DID, und ARE USED TO bedeutet "es fühlt sich normal an".',
    q3w='USED TO + Grundform (EMPLOY) für einen früheren Zustand, der sich verändert hat.',
    q4w='Eine Frage: DID + Subjekt + USE TO. DID zeigt schon die Vergangenheit, also USE und nicht USED.',
    q5w='Verneinung: DIDN’T USE TO + Grundform. Damals geschah es nicht, heute schon. "Used to not" ist umgangssprachlich; "hasn’t used to" gibt es nicht.',
    q6w='Es fühlt sich JETZT normal an: ARE USED TO + -ING. USED TO allein ist eine frühere Gewohnheit und kann nicht mit LIVING stehen.',
    q7w='Damals fühlte es sich nicht normal an: WASN’T USED TO + Nomen (THE NOISE). DIDN’T USE TO bräuchte eine Grundform, und ISN’T ist Gegenwart.',
    q8w='Damals für sie normal: WERE USED TO + -ING. "Had been their routine" legt es in die Vergangenheit, also nicht ARE.',
    q9w='FINALLY zeigt einen Wandel über die Zeit: GET USED TO = sich daran gewöhnen. WAS USED TO beschreibt den Zustand, nicht den Wandel.',
    q10w='Eine Frage über JETZT: ARE + Subjekt + USED TO + -ING. "Do … use to" ist kein Englisch.',
    q11w='USED TO SWIM = eine Gewohnheit aus der Kindheit, die aufgehört hat. IS USED TO LIVING = es fühlt sich jetzt für sie normal an.',
    q12w='TODAY: ARE USED TO + -ING, es ist für sie normal. In den 1960ern ein früherer Zustand, der sich verändert hat: DIDN’T USE TO HAVE.',
    q13w='AREN’T USED TO + Nomen (SUCH HUMIDITY): Es fühlt sich nicht normal an. USED TO COME = ein früheres Muster, das sich verändert hat, denn jetzt kommen sie das ganze Jahr.',

    g1w='Eine frühere Gewohnheit oder ein Zustand, der aufgehört hat: USED TO + Grundform.',
    g2w='Verneinung: DIDN’T USE TO + Grundform. Nach DIDN’T kein D bei USE.',
    g3w='Eine Frage: DID + Subjekt + USE TO + Grundform.',
    g4w='Für sie ist es jetzt normal: IS USED TO + -ING.',
    g5w='Damals fühlte es sich nicht normal an: WASN’T USED TO + Nomen.',
    g6w='Der Wandel, in der Vergangenheit: GOT USED TO.',

    actTitle='Damals und heute',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu zweit. Erzähle deinem Partner von einer großen Veränderung in deinem Leben: eine neue Stadt, ein neuer Job, eine neue Schule.',
    actSpeak1='Sag, was du vor der Veränderung gemacht hast (USED TO) und eine Sache, die du nicht gemacht hast (DIDN’T USE TO).',
    actSpeak2='Sag, woran du jetzt gewöhnt bist (ARE USED TO), das sich am Anfang seltsam anfühlte. Wie lange hat es gedauert (GET USED TO)?',
    actSpeak3='Stell deinem Partner drei Fragen: eine mit DID … USE TO und zwei mit ARE YOU USED TO …?',
    actWriteKind='Schreiben',
    actWriteBrief='Eine Freundin aus Venezuela zieht in deine Stadt. Schreib ihr (150–200 Wörter): wie das Leben hier früher war (USED TO), woran man hier gewöhnt ist (ARE USED TO) und woran sie sich erst gewöhnen muss (GET USED TO).',
    actPlaceholder='Hi Daniela, …',
)

# ══════════════════════════════════════════════════════════════════════
#  SPANISH
# ══════════════════════════════════════════════════════════════════════
T['es'] = dict(
    coverTitle='Used To &amp; <em>Be Used To</em>',
    coverSub='Edición Venezuela: USED TO para hábitos y estados del pasado, BE USED TO + -ING para lo que resulta normal, y GET USED TO para el cambio entre los dos.',
    chipLevel='B1', chipFocus='used to · be used to · get used to', chipCount='28 diapositivas',

    eW='Para empezar', eT='¡A conversar!', eR='La regla', eX='En contexto',
    e1='Used to', e2='Be used to', e3='¿Used to o be used to?',

    svT='Las cinco más comunes', svHint='Adivinen en clase las cinco respuestas más comunes y hagan clic en una tarjeta para comprobar.',
    tk1T='¡A conversar!', tk2T='¡A conversar!',

    rAt='Used to: hábitos y estados del pasado',
    rA1='Un hábito del pasado: ocurría una y otra vez, y ya terminó.',
    rA2='Un estado del pasado: era verdad antes y ya no lo es.',
    rA3='No se usa para algo que sigue siendo verdad hoy.',
    rA4='La negación lleva DIDN’T y después USE, sin D.',
    rA5='La pregunta empieza con DID, y otra vez USE, sin D.',

    xAt='Used to en Venezuela',
    xA1l='Historia', xA1n='Un estado del pasado: hoy ya no es verdad de la misma manera.',
    xA2l='Naturaleza', xA2n='"Flock" = viajar en grandes grupos. Hoy van muchos menos turistas.',
    xA3l='Vida diaria', xA3n='Un hábito repetido del pasado: algo que se hacía con regularidad.',
    xA4l='Industria', xA4n='Un estado del pasado que ha cambiado muchísimo.',
    xA5l='Infancia', xA5n='Negación: algo que NO ocurría con regularidad.',
    xA6l='Música', xA6n='Una situación del pasado: la cultura de radio de todo un país.',

    mcT='Elige la forma correcta', gapT='Escribe las palabras que faltan',
    gHintA='Usa el verbo entre paréntesis con USED TO.',
    gHintB='Usa BE USED TO o GET USED TO.',

    rBt='Be used to: resulta normal',
    rB1='Resulta normal y familiar: estás acostumbrado.',
    rB2='BE marca el tiempo (AM / IS / ARE, WAS / WERE); la forma -ING no cambia.',
    rB3='Negación: ISN’T / WASN’T USED TO. Pregunta: ARE YOU USED TO …?',
    rB4='También puede seguir un sustantivo o un pronombre: USED TO THE NOISE, USED TO IT.',
    rB5='GET USED TO es el cambio: poco a poco, se vuelve normal.',

    xBt='Be used to en contexto',
    xB1l='Clima', xB1n='Presente: ahora resulta normal y cómodo.',
    xB2l='Trabajo', xB2n='Pasado: en aquella época era normal para ellos.',
    xB3l='Comida', xB3n='Negación: (todavía) NO resulta normal.',
    xB4l='Viajes', xB4n='Pregunta: ARE + sujeto + USED TO + -ING.',
    xB5l='Tiempo', xB5n='GOT USED TO = el cambio: poco a poco se volvió normal.',
    xB6l='Ruido', xB6n='Presente: algo que ya es rutina.',

    rCt='Dos estructuras, lado a lado',
    rC1='Un hábito o estado del pasado que ya terminó.',
    rC2='Solo habla del pasado.',
    rC3='Siempre + el verbo en forma base.',
    rC4='Algo que resulta normal o familiar.',
    rC5='Pasado, presente o futuro: BE marca el tiempo.',
    rC6='Siempre + -ING, o un sustantivo.',

    orderT='Construye la oración', orderHint='Haz clic en las piezas en orden. Sobra una pieza.',
    o1w='DID + sujeto + USE TO + verbo en forma base. Con DID es USE TO, así que sobra "used to".',
    o2w='BE USED TO + -ING: "isn’t used to DRIVING". Sobra "drive".',

    q1w='El hecho SIGUE siendo verdad, así que no es USED TO: USED TO dice que algo terminó. HAS ALWAYS BEEN = verdad antes y verdad ahora.',
    q2w='Un hábito del pasado que terminó: USED TO + verbo base. USE TO sin D solo va después de DID, y ARE USED TO significa "resulta normal".',
    q3w='USED TO + el verbo base (EMPLOY) para un estado del pasado que ha cambiado.',
    q4w='Una pregunta: DID + sujeto + USE TO. DID ya marca el pasado, así que es USE, no USED.',
    q5w='Negación: DIDN’T USE TO + verbo base. Antes no ocurría y ahora sí. "Used to not" es informal; "hasn’t used to" no existe.',
    q6w='Resulta normal AHORA: ARE USED TO + -ING. USED TO solo es un hábito del pasado y no puede llevar LIVING.',
    q7w='Entonces no le resultaba normal: WASN’T USED TO + sustantivo (THE NOISE). DIDN’T USE TO necesitaría un verbo base, e ISN’T es presente.',
    q8w='Normal para ellos en el pasado: WERE USED TO + -ING. "Had been their routine" lo sitúa en el pasado, así que no es ARE.',
    q9w='FINALLY muestra un cambio con el tiempo: GET USED TO = acostumbrarse. WAS USED TO describe el estado, no el cambio.',
    q10w='Una pregunta sobre AHORA: ARE + sujeto + USED TO + -ING. "Do … use to" no es inglés.',
    q11w='USED TO SWIM = un hábito de la infancia que terminó. IS USED TO LIVING = ahora le resulta normal.',
    q12w='TODAY: ARE USED TO + -ING, para ellos es normal. En los años 60, un estado del pasado que ha cambiado: DIDN’T USE TO HAVE.',
    q13w='AREN’T USED TO + sustantivo (SUCH HUMIDITY): no les resulta normal. USED TO COME = un patrón del pasado que ha cambiado, porque ahora vienen todo el año.',

    g1w='Un hábito o estado del pasado que terminó: USED TO + verbo base.',
    g2w='Negación: DIDN’T USE TO + verbo base. Después de DIDN’T, USE va sin D.',
    g3w='Una pregunta: DID + sujeto + USE TO + verbo base.',
    g4w='Ahora para ella es normal: IS USED TO + -ING.',
    g5w='Entonces no le resultaba normal: WASN’T USED TO + sustantivo.',
    g6w='El cambio, en pasado: GOT USED TO.',

    actTitle='Antes y ahora',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas. Cuéntale a tu compañero un gran cambio en tu vida: una ciudad nueva, un trabajo nuevo, una escuela nueva.',
    actSpeak1='Di qué hacías antes del cambio (USED TO) y una cosa que no hacías (DIDN’T USE TO).',
    actSpeak2='Di a qué estás acostumbrado ahora (ARE USED TO) que al principio te parecía raro. ¿Cuánto tardaste en acostumbrarte (GET USED TO)?',
    actSpeak3='Hazle a tu compañero tres preguntas: una con DID … USE TO y dos con ARE YOU USED TO …?',
    actWriteKind='Escritura',
    actWriteBrief='Una amiga de Venezuela se muda a tu ciudad. Escríbele (150–200 palabras): cómo era antes la vida aquí (USED TO), a qué está acostumbrada la gente (ARE USED TO) y a qué le costará acostumbrarse (GET USED TO).',
    actPlaceholder='Hola, Daniela: …',
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
