# -*- coding: utf-8 -*-
"""Question Words (A0, German support). House style 2, 27 slides.

Rebuilt 2026-11-06 from `Forbes_English_A0_Question_Words.html`, an intro
with the six question words and their German meanings, then eighteen
one-at-a-time items in three kinds: meaning, fill the gap, match the answer.

Changed:
  * The six "meaning" items asked "What does 'Who' mean in German?" with
    German options, which a deck that ships Spanish cannot ask. They now ask
    which word asks about a person, a thing, a place … — the same six
    meanings, in English, with the German AND Spanish words on the rule
    cards beside the English.
  * "___ is your birthday?" accepted WHAT ("What is your birthday?" is
    good English), and "___ is your teacher?" accepted WHERE and HOW. The
    first lost its WHAT; the second says it is asking about a person.
  * "Why are you learning English? — To learn English." was circular. The
    explanation's model answer is now "For my job."
Added: two sentence builds, two speaking fields and the activation.

Run from the repo root:  py lesson-template/build/build_question_words_a0.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='Forbes_English_A0_Question_Words.html',
    title='Question Words (A0)',
    folder='QuestionWordsA0',
    scheme='cool',
    art={
        'hero': ('quiz', 'a big question mark made of six coloured pieces, one for each question word'),
        'talk': ('people', 'two figures meeting for the first time, one speech bubble with a question mark'),
        'a': ('idea', 'a lamp switching on above an open notebook'),
        'b': ('words', 'a stack of index cards with a magnifying glass'),
        'c': ('talk', 'a speech bubble with a question mark answered by a second bubble'),
        'act': ('pair', 'two chairs facing each other with name badges on the table'),
    },
)


def q(stem, options, n, gl=None):
    d = dict(stem=stem, options=options, correct=0, why='w%d' % n)
    if gl:
        d['gl'] = gl
    return d


MEAN = [
    q('Which question word asks about a <strong>person</strong>?', ['Who', 'What', 'Where', 'When'], 1, 'gM1'),
    q('Which question word asks about a <strong>thing</strong>?', ['What', 'Who', 'How', 'Why'], 2, 'gM2'),
    q('Which question word asks about a <strong>place</strong>?', ['Where', 'When', 'Who', 'How'], 3, 'gM3'),
    q('Which question word asks about a <strong>time</strong>?', ['When', 'Where', 'What', 'Why'], 4, 'gM4'),
    q('Which question word asks for a <strong>reason</strong>?', ['Why', 'How', 'Who', 'When'], 5, 'gM5'),
    q('Which question word asks how you <strong>feel</strong>, or the <strong>way</strong> to do something?',
      ['How', 'Why', 'What', 'Where'], 6, 'gM6'),
]
GAP = [
    q('____ are you? (asking about feelings)', ['How', 'Where', 'What', 'Who'], 7, 'g7'),
    q('____ do you live?', ['Where', 'When', 'Why', 'Who'], 8, 'g8'),
    q('____ is your name?', ['What', 'How', 'Why', 'When'], 9, 'g9'),
    q('____ is your birthday?', ['When', 'Who', 'Where', 'Why'], 10, 'g10'),
    q('____ are you learning English?', ['Why', 'Who', 'Where', 'What'], 11, 'g11'),
    q('____ is your teacher? (asking about a person)', ['Who', 'What', 'When', 'Why'], 12, 'g12'),
]
MATCH = [
    q('Who are you?', ['I’m Maria.', 'In Munich.', 'A phone.', 'I’m good.'], 13, 'g13'),
    q('Where do you live?', ['In Munich.', 'I’m Maria.', 'A phone.', 'At 10 o’clock.'], 14, 'g14'),
    q('What is this?', ['A phone.', 'I’m Maria.', 'In Munich.', 'I’m good.'], 15, 'g15'),
    q('How are you?', ['I’m good.', 'In Munich.', 'A phone.', 'To study.'], 16, 'g16'),
    q('When is the lesson?', ['At 10 o’clock.', 'I’m Maria.', 'A phone.', 'To study English.'], 17, 'g17'),
    q('Why are you here?', ['To study English.', 'I’m Maria.', 'In Munich.', 'At 10 o’clock.'], 18, 'g18'),
]

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'What is your name?', 'Where are you from?', 'How are you today?',
        'When is your birthday?', 'Who is your best friend?', 'Why are you here?',
    ], 'talk', 3),
    ('rules', 'eR', 'rT1', [
        ('Who', ['rWho'], '<strong>Who</strong> is she? — My sister.'),
        ('What', ['rWhat'], '<strong>What</strong> is this? — A phone.'),
        ('Where', ['rWhere'], '<strong>Where</strong> do you live? — In Berlin.'),
    ], None),
    ('rules', 'eR', 'rT2', [
        ('When', ['rWhen'], '<strong>When</strong> is your birthday? — In May.'),
        ('Why', ['rWhy'], '<strong>Why</strong> are you happy? — Because it’s Friday!'),
        ('How', ['rHow'], '<strong>How</strong> are you? — I’m fine, thanks.'),
    ], None),
    ('mc', 'e1', 'mcT', MEAN, 'a', None),
    ('mc', 'e2', 'mcT', GAP, 'b', 'left'),
    ('mc', 'e3', 'mcT3', MATCH, 'c', None),
    ('order', 'e4', 'orderT', 'orderHint', [
        (['Where', 'do', 'you', 'live?'], ['are'], 'o1w'),
        (['What', 'is', 'your', 'name?'], ['do'], 'o2w'),
    ], 'c', 'left'),
    ('talk', 'eT', 'tk2T', [
        '<strong>Who</strong> do you live with?', '<strong>What</strong> is your favourite food?',
        '<strong>Where</strong> do you work or study?', '<strong>When</strong> do you get up?',
        '<strong>Why</strong> do you like your city?', '<strong>How</strong> do you go to work?',
    ], None, 3),
]
SPEC['chips'] = ['How', 'Who', 'When', 'What', 'Why', 'Where']

W = {
    'en': [
        'WHO asks about a person: Who is she? — My sister.',
        'WHAT asks about a thing: What is this? — A phone.',
        'WHERE asks about a place: Where do you live? — In Berlin.',
        'WHEN asks about a time: When is your birthday? — In May.',
        'WHY asks for a reason: Why are you happy? — Because it’s Friday!',
        'HOW asks about a feeling or a way: How are you? — I’m fine.',
        '“How are you?” asks how you feel. Answer: I’m fine, thanks.',
        '“Where do you live?” asks about a place. Answer: I live in Berlin.',
        '“What is your name?” Answer: I’m Anna.',
        '“When is your birthday?” asks about a time. Answer: It’s in May.',
        '“Why are you learning English?” asks for a reason. Answer: For my job.',
        'A person → WHO. Answer: Mrs Schmidt.',
        'WHO asks about a person, so the answer names a person: I’m Maria.',
        'WHERE asks about a place, so the answer is a place: In Munich.',
        'WHAT asks about a thing, so the answer is a thing: A phone.',
        '“How are you?” asks how you feel: I’m good.',
        'WHEN asks about a time, so the answer is a time: At 10 o’clock.',
        'WHY asks for a reason, so the answer is a reason: To study English.',
    ],
    'de': [
        'WHO (wer) fragt nach einer Person: Who is she? — My sister.',
        'WHAT (was) fragt nach einer Sache: What is this? — A phone.',
        'WHERE (wo) fragt nach einem Ort: Where do you live? — In Berlin.',
        'WHEN (wann) fragt nach einer Zeit: When is your birthday? — In May.',
        'WHY (warum) fragt nach einem Grund: Why are you happy? — Because it’s Friday!',
        'HOW (wie) fragt nach einem Gefühl oder einer Art und Weise: How are you? — I’m fine.',
        '„How are you?“ fragt, wie es dir geht. Antwort: I’m fine, thanks.',
        '„Where do you live?“ fragt nach einem Ort. Antwort: I live in Berlin.',
        '„What is your name?“ Antwort: I’m Anna.',
        '„When is your birthday?“ fragt nach einer Zeit. Antwort: It’s in May.',
        '„Why are you learning English?“ fragt nach einem Grund. Antwort: For my job.',
        'Eine Person → WHO. Antwort: Mrs Schmidt.',
        'WHO fragt nach einer Person, also nennt die Antwort eine Person: I’m Maria.',
        'WHERE fragt nach einem Ort, also ist die Antwort ein Ort: In Munich.',
        'WHAT fragt nach einer Sache, also ist die Antwort eine Sache: A phone.',
        '„How are you?“ fragt, wie es dir geht: I’m good.',
        'WHEN fragt nach einer Zeit, also ist die Antwort eine Zeit: At 10 o’clock.',
        'WHY fragt nach einem Grund, also ist die Antwort ein Grund: To study English.',
    ],
    'es': [
        'WHO (quién) pregunta por una persona: Who is she? — My sister.',
        'WHAT (qué) pregunta por una cosa: What is this? — A phone.',
        'WHERE (dónde) pregunta por un lugar: Where do you live? — In Berlin.',
        'WHEN (cuándo) pregunta por un momento: When is your birthday? — In May.',
        'WHY (por qué) pregunta por una razón: Why are you happy? — Because it’s Friday!',
        'HOW (cómo) pregunta por un sentimiento o una manera: How are you? — I’m fine.',
        '«How are you?» pregunta cómo estás. Respuesta: I’m fine, thanks.',
        '«Where do you live?» pregunta por un lugar. Respuesta: I live in Berlin.',
        '«What is your name?» Respuesta: I’m Anna.',
        '«When is your birthday?» pregunta por un momento. Respuesta: It’s in May.',
        '«Why are you learning English?» pregunta por una razón. Respuesta: For my job.',
        'Una persona → WHO. Respuesta: Mrs Schmidt.',
        'WHO pregunta por una persona, así que la respuesta nombra a una persona: I’m Maria.',
        'WHERE pregunta por un lugar, así que la respuesta es un lugar: In Munich.',
        'WHAT pregunta por una cosa, así que la respuesta es una cosa: A phone.',
        '«How are you?» pregunta cómo estás: I’m good.',
        'WHEN pregunta por un momento, así que la respuesta es un momento: At 10 o’clock.',
        'WHY pregunta por una razón, así que la respuesta es una razón: To study English.',
    ],
}

T = {
    'en': dict(
        coverTitle='Question <em>Words</em>',
        coverSub='Who, what, where, when, why and how: six words that start most questions, what each one asks about, and the answers that go with them.',
        chipLevel='A0', chipFocus='who · what · where · when · why · how', chipCount='27 slides',
        eW='Warm-up', eT='Let’s talk', eR='The rule', e1='What does it ask?', e2='Fill the gap',
        e3='Find the answer', e4='Your turn', tk1T='Let’s talk!', tk2T='Let’s talk!',
        mcT='Choose the right word', mcT3='Choose the right answer',
        rT1='Six question words (1)', rT2='Six question words (2)',
        rWho='a person', rWhat='a thing', rWhere='a place', rWhen='a time', rWhy='a reason', rHow='a feeling, a way',
        orderT='Build the question', orderHint='Click the pieces in order. One piece is left over.',
        o1w='Question word + DO + you + verb: Where do you live? ARE is left over.',
        o2w='Question word + IS + the subject: What is your name? DO is left over.',
        actTitle='Getting to know you', actUse='Use all six:',
        actSpeakBrief='In pairs. Meet your partner.',
        actSpeak1='Ask your partner six questions, one with each question word.',
        actSpeak2='Answer your partner’s questions. Then change roles.',
        actSpeak3='Tell the class two things about your partner.',
        actWriteKind='Writing',
        actWriteBrief='Write six questions for a new classmate, one with each question word, and your own answers (40–60 words).',
        actPlaceholder='What is your name? My name is …',
    ),
    'de': dict(
        coverTitle='Question <em>Words</em>',
        coverSub='Who, what, where, when, why und how: sechs Wörter, mit denen die meisten Fragen beginnen, wonach jedes fragt und welche Antworten dazu passen.',
        chipLevel='A0', chipFocus='who · what · where · when · why · how', chipCount='27 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Die Regel', e1='Wonach fragt es?', e2='Füll die Lücke',
        e3='Finde die Antwort', e4='Du bist dran', tk1T='Sprechen wir!', tk2T='Sprechen wir!',
        mcT='Wähle das richtige Wort', mcT3='Wähle die richtige Antwort',
        rT1='Sechs Fragewörter (1)', rT2='Sechs Fragewörter (2)',
        rWho='wer — eine Person', rWhat='was — eine Sache', rWhere='wo — ein Ort', rWhen='wann — eine Zeit',
        rWhy='warum — ein Grund', rHow='wie — ein Gefühl, eine Art',
        orderT='Bilde die Frage', orderHint='Klicke die Teile der Reihe nach an. Ein Teil bleibt übrig.',
        o1w='Fragewort + DO + you + Verb: Where do you live? ARE bleibt übrig.',
        o2w='Fragewort + IS + Subjekt: What is your name? DO bleibt übrig.',
        actTitle='Kennenlernen', actUse='Verwende alle sechs:',
        actSpeakBrief='Zu zweit. Lerne deinen Partner kennen.',
        actSpeak1='Stell deinem Partner sechs Fragen, eine mit jedem Fragewort.',
        actSpeak2='Beantworte die Fragen deines Partners. Dann tauscht die Rollen.',
        actSpeak3='Erzähl der Klasse zwei Dinge über deinen Partner.',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib sechs Fragen für eine neue Mitschülerin, eine mit jedem Fragewort, und deine eigenen Antworten (40–60 Wörter).',
        actPlaceholder='What is your name? My name is …',
    ),
    'es': dict(
        coverTitle='Question <em>Words</em>',
        coverSub='Who, what, where, when, why y how: seis palabras con las que empiezan casi todas las preguntas, qué pregunta cada una y las respuestas que les corresponden.',
        chipLevel='A0', chipFocus='who · what · where · when · why · how', chipCount='27 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='La regla', e1='¿Qué pregunta?', e2='Completa el hueco',
        e3='Encuentra la respuesta', e4='Tu turno', tk1T='¡A conversar!', tk2T='¡A conversar!',
        mcT='Elige la palabra correcta', mcT3='Elige la respuesta correcta',
        rT1='Seis palabras interrogativas (1)', rT2='Seis palabras interrogativas (2)',
        rWho='quién — una persona', rWhat='qué — una cosa', rWhere='dónde — un lugar', rWhen='cuándo — un momento',
        rWhy='por qué — una razón', rHow='cómo — un sentimiento, una manera',
        orderT='Construye la pregunta', orderHint='Haz clic en las piezas en orden. Sobra una pieza.',
        o1w='Palabra interrogativa + DO + you + verbo: Where do you live? Sobra ARE.',
        o2w='Palabra interrogativa + IS + sujeto: What is your name? Sobra DO.',
        actTitle='Para conocernos', actUse='Usa las seis:',
        actSpeakBrief='En parejas. Conoce a tu compañero.',
        actSpeak1='Hazle a tu compañero seis preguntas, una con cada palabra interrogativa.',
        actSpeak2='Responde a las preguntas de tu compañero. Después cambien los papeles.',
        actSpeak3='Cuéntale a la clase dos cosas sobre tu compañero.',
        actWriteKind='Escritura',
        actWriteBrief='Escribe seis preguntas para una compañera nueva, una con cada palabra interrogativa, y tus propias respuestas (40–60 palabras).',
        actPlaceholder='What is your name? My name is …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w

GLOSS = {
    'de': dict(
        gM1='Welches Fragewort fragt nach einer Person?', gM2='Welches Fragewort fragt nach einer Sache?',
        gM3='Welches Fragewort fragt nach einem Ort?', gM4='Welches Fragewort fragt nach einer Zeit?',
        gM5='Welches Fragewort fragt nach einem Grund?', gM6='Welches Fragewort fragt, wie es dir geht, oder nach der Art und Weise?',
        g7='Wie geht es dir?', g8='Wo wohnst du?', g9='Wie heißt du?', g10='Wann hast du Geburtstag?',
        g11='Warum lernst du Englisch?', g12='Wer ist dein Lehrer?', g13='Wer bist du?', g14='Wo wohnst du?',
        g15='Was ist das?', g16='Wie geht es dir?', g17='Wann ist der Unterricht?', g18='Warum bist du hier?',
    ),
    'es': dict(
        gM1='¿Qué palabra pregunta por una persona?', gM2='¿Qué palabra pregunta por una cosa?',
        gM3='¿Qué palabra pregunta por un lugar?', gM4='¿Qué palabra pregunta por un momento?',
        gM5='¿Qué palabra pregunta por una razón?', gM6='¿Qué palabra pregunta cómo te sientes, o la manera de hacer algo?',
        g7='¿Cómo estás?', g8='¿Dónde vives?', g9='¿Cómo te llamas?', g10='¿Cuándo es tu cumpleaños?',
        g11='¿Por qué estudias inglés?', g12='¿Quién es tu profesor?', g13='¿Quién eres?', g14='¿Dónde vives?',
        g15='¿Qué es esto?', g16='¿Cómo estás?', g17='¿Cuándo es la clase?', g18='¿Por qué estás aquí?',
    ),
}

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T, GLOSS)
