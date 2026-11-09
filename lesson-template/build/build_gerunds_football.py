# -*- coding: utf-8 -*-
"""Verbs + Gerunds — English for Graphic Designers (B1). House style 2, 17 slides.

Rebuilt 2026-11-06 from `lesson1_gerunds_football.html` (Module 1 · Lesson
1), a verb list, four corrected mistakes ("red card / goal") and seven
football-themed items, EN + DE. All of it is kept; Spanish added. Cover:
the page's own hero, FootballGerunds/retro-runner.jpg.

Fixed: the page said these verbs "always" take -ING and "never" an
infinitive, and listed "I have stopped to drink alcohol" as a red card.
STOP + TO is good English with a different meaning (stop in order to do
something), so the card now teaches the difference instead of calling it
wrong; the rule says "take -ING", not "always".
Added: a gap slide, two sentence builds with a decoy, the speaking fields
and the activation.

Run from the repo root:  py lesson-template/build/build_gerunds_football.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='lesson1_gerunds_football.html',
    title='Verbs + Gerunds — English for Graphic Designers (B1)',
    folder='FootballGerunds',
    hero='retro-runner',
    scheme='sage',
    style='hs1',
    # House style 1 (HOUSE-STYLE §000, 2026-11-09): the live runner plate is
    # the cover; Midjourney renders besides (his style images, --stylize
    # 200), the runner's navy / cream / orange named in the prompt.
    plates={
        'retro-runner': 'a footballer running after the ball past floodlights',
        'talk': 'a design studio with two desks, big monitors and a football on the floor',
        'r-studio': 'a designer at a desk, a football poster pinned on the wall behind',
        'g1': 'a designer trying out different page layouts on a big screen',
        'g2': 'a designer comparing font sample cards beside a football kit on a hanger',
        'g3': 'a video editor cutting football highlights across two monitors',
        'g4': 'a client on the phone pacing beside a wall of trophy logo drafts',
        'g5': 'a motion designer animating a bouncing football on a drawing tablet',
        'g6': 'a calm designer planning ahead at a wall covered in sticky notes',
        'g7': 'a designer sketching a new football crest from scratch at a drawing board',
        'o1': 'a young man looking at laptops in a shop window',
        'o2': 'two designers pinning a finished football poster to the studio wall',
        'talk2': 'two colleagues chatting over drinks after work, a football match on the bar television',
        'results': 'a football resting on a desk beside an open laptop and a coffee cup',
    },
    pop={'retro-runner': (None, 'square')},
    results='results',
)


def q(stem, options, n):
    return dict(stem=stem, options=options, correct=0, why='w%d' % n)


ITEMS = [
    q('I really enjoy ____ with new layout styles in Figma.', ['experimenting', 'to experiment', 'experiment'], 1),
    q('The FIFA brand guidelines recommend ____ a consistent typeface across all platforms.', ['using', 'to use', 'use'], 2),
    q('Once you finish ____ the 120 highlight clips, export them as H.264.', ['editing', 'to edit', 'edit'], 3),
    q('The client kept ____ for more versions of the World Cup logo.', ['asking', 'to ask', 'asks'], 4),
    q('I spend a lot of time ____ with new motion design modules.', ['experimenting', 'to experiment', 'experiment'], 5),
    q('I avoid ____ tight deadlines by planning well in advance.', ['missing', 'to miss', 'miss'], 6),
    q('Can you imagine ____ the whole FIFA visual identity from scratch?', ['redesigning', 'to redesign', 'redesign'], 7),
]

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'What do you enjoy most about your job?',
        'What do you spend most of your time doing at work?',
        'Which design tool do you keep using, and why?',
        'Is there anything you avoid doing on a project?',
        'What would you recommend to a new designer?',
        'Do you mind working late before a deadline?',
    ], 'talk', 3),
    ('stage',),
    ('rules', 'eR', 'rT', [
        ('verb + -ing', ['rL1', (None, 'enjoy · avoid · consider · finish · keep · miss'),
                         (None, 'practise · recommend · suggest · mind · imagine · risk'),
                         (None, 'can’t stand · spend time')], None),
        ('pStop', ['rL2', 'rL3'], 'I’ve <strong>stopped drinking</strong> coffee. · We <strong>stopped to have</strong> a coffee.'),
    ], 'r-studio'),
    ('rules', 'eR', 'rMT', [
        ('pCard', [(None, '<s>Once you finish to do 120 clips …</s>')], 'Once you finish <strong>doing</strong> 120 clips …'),
        ('pCard', [(None, '<s>I’m thinking about to buy a Mercedes.</s>')], 'I’m thinking about <strong>buying</strong> a Mercedes.'),
        ('pCard', [(None, '<s>I spend a lot of time experiment with modules.</s>')], 'I spend a lot of time <strong>experimenting</strong> with modules.'),
    ], None),
    ('mc', 'e1', 'mcT', ITEMS, ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7'], None),
    ('gap', 'e2', 'gapT', 'gHint', [
        ('Would you mind ______ (send) me the files tonight?', ['sending'], 'gw1'),
        ('She suggested ______ (start) with the logo.', ['starting'], 'gw2'),
        ('We can’t risk ______ (lose) this client.', ['losing'], 'gw3'),
    ]),
    ('order', 'e2', 'orderT', 'orderHint', [
        (['I’m thinking about', 'buying', 'a new', 'laptop.'], ['to buy'], 'o1w'),
        (['We finished', 'designing', 'the poster', 'on Friday.'], ['to design'], 'o2w'),
    ], ['o1', 'o2'], None),
    ('talk', 'eT', 'tk2T', [
        'What do you <strong>enjoy doing</strong> after work?',
        'What do you <strong>miss doing</strong> from your first job?',
        'Which task do you always <strong>put off doing</strong>?',
        'What are you <strong>thinking about learning</strong> next?',
        'What do you <strong>avoid saying</strong> to a client?',
        'Can you <strong>imagine working</strong> in another country?',
    ], 'talk2', 3),
]
SPEC['chips'] = ['enjoy designing', 'avoid missing', 'keep asking', 'finish editing', 'spend time', 'recommend using']

W = {
    'en': [
        'ENJOY + -ING: enjoy experimenting, enjoy designing.',
        'RECOMMEND + -ING: recommend using. (Or RECOMMEND THAT we use.)',
        'FINISH + -ING: finish editing, finish doing — the exact mistake from your notes.',
        'KEEP + -ING: kept asking = asked again and again.',
        'SPEND TIME + -ING: spend time experimenting.',
        'AVOID + -ING: avoid missing.',
        'IMAGINE + -ING: imagine redesigning.',
    ],
    'de': [
        'ENJOY + -ING: enjoy experimenting, enjoy designing.',
        'RECOMMEND + -ING: recommend using. (Oder: RECOMMEND THAT we use.)',
        'FINISH + -ING: finish editing, finish doing — genau der Fehler aus deinen Notizen.',
        'KEEP + -ING: kept asking = fragte immer wieder.',
        'SPEND TIME + -ING: spend time experimenting.',
        'AVOID + -ING: avoid missing.',
        'IMAGINE + -ING: imagine redesigning.',
    ],
    'es': [
        'ENJOY + -ING: enjoy experimenting, enjoy designing.',
        'RECOMMEND + -ING: recommend using. (O bien: RECOMMEND THAT we use.)',
        'FINISH + -ING: finish editing, finish doing — justo el error de tus apuntes.',
        'KEEP + -ING: kept asking = preguntaba una y otra vez.',
        'SPEND TIME + -ING: spend time experimenting.',
        'AVOID + -ING: avoid missing.',
        'IMAGINE + -ING: imagine redesigning.',
    ],
}

T = {
    'en': dict(
        coverTitle='Verbs <br><em>+ Gerunds</em>',
        coverSub='English for graphic designers: the verbs that take the -ING form, your own corrected mistakes, and seven match-day questions.',
        chipLevel='B1', chipFocus='enjoy doing · finish editing', chipCount='17 slides',
        eW='Warm-up', eT='Let’s talk', eR='The rule', e1='Match day', e2='Your turn',
        tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the right form',
        rT='Verbs that take -ing',
        rL1='After these verbs, use the -ING form, not TO + verb.',
        pStop='Careful: stop',
        rL2='STOP + -ING: you don’t do it any more.',
        rL3='STOP + TO: you stop in order to do something else.',
        rMT='Your mistakes, corrected', pCard='Red card → goal',
        gapT='Write the -ing form', gHint='Use the verb in brackets.',
        gw1='MIND + -ING: “Would you mind sending …?”', gw2='SUGGEST + -ING: suggested starting.', gw3='RISK + -ING: risk losing.',
        orderT='Build the sentence', orderHint='Click the pieces in order. One piece is left over.',
        o1w='THINK ABOUT + -ING: after a preposition the verb takes -ING. TO BUY is left over.',
        o2w='FINISH + -ING: finished designing. TO DESIGN is left over.',
        actTitle='The design brief', actUse='Use at least three:',
        actSpeakBrief='In pairs: one of you is a designer, the other a client.',
        actSpeak1='Client: say what you ENJOY and what you want to AVOID in the new logo.',
        actSpeak2='Designer: RECOMMEND doing two things, and say when you will FINISH designing.',
        actSpeak3='Swap roles. Talk about a project you KEPT changing.',
        actWriteKind='Writing',
        actWriteBrief='Write an email to a client (100–120 words) about a new poster: what you RECOMMEND doing, what you SUGGEST avoiding, and when you expect to FINISH designing it.',
        actPlaceholder='Dear Ms Weber, …',
    ),
    'de': dict(
        coverTitle='Verbs <br><em>+ Gerunds</em>',
        coverSub='Englisch für Grafikdesigner: die Verben, die die -ING-Form nehmen, deine eigenen korrigierten Fehler und sieben Fragen am Spieltag.',
        chipLevel='B1', chipFocus='enjoy doing · finish editing', chipCount='17 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Die Regel', e1='Spieltag', e2='Du bist dran',
        tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle die richtige Form',
        rT='Verben mit -ing',
        rL1='Nach diesen Verben steht die -ING-Form, nicht TO + Verb.',
        pStop='Vorsicht: stop',
        rL2='STOP + -ING: Du machst es nicht mehr.',
        rL3='STOP + TO: Du hörst auf, um etwas anderes zu tun.',
        rMT='Deine Fehler, korrigiert', pCard='Rote Karte → Tor',
        gapT='Schreib die -ing-Form', gHint='Verwende das Verb in Klammern.',
        gw1='MIND + -ING: „Would you mind sending …?“', gw2='SUGGEST + -ING: suggested starting.', gw3='RISK + -ING: risk losing.',
        orderT='Bilde den Satz', orderHint='Klicke die Teile der Reihe nach an. Ein Teil bleibt übrig.',
        o1w='THINK ABOUT + -ING: Nach einer Präposition nimmt das Verb -ING. TO BUY bleibt übrig.',
        o2w='FINISH + -ING: finished designing. TO DESIGN bleibt übrig.',
        actTitle='Das Designbriefing', actUse='Verwende mindestens drei:',
        actSpeakBrief='Zu zweit: Eine Person ist Designerin, die andere Kundin.',
        actSpeak1='Kundin: Sag, was du magst (ENJOY) und was du im neuen Logo vermeiden willst (AVOID).',
        actSpeak2='Designerin: Empfiehl zwei Dinge (RECOMMEND + -ING) und sag, wann du fertig bist (FINISH DESIGNING).',
        actSpeak3='Tauscht die Rollen. Sprecht über ein Projekt, das ihr immer wieder geändert habt (KEPT CHANGING).',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib einer Kundin eine E-Mail (100–120 Wörter) über ein neues Plakat: was du empfiehlst (RECOMMEND doing), was du vermeiden würdest (SUGGEST avoiding) und wann du fertig sein wirst (FINISH designing).',
        actPlaceholder='Dear Ms Weber, …',
    ),
    'es': dict(
        coverTitle='Verbs <br><em>+ Gerunds</em>',
        coverSub='Inglés para diseñadores gráficos: los verbos que llevan la forma -ING, tus propios errores corregidos y siete preguntas de día de partido.',
        chipLevel='B1', chipFocus='enjoy doing · finish editing', chipCount='17 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='La regla', e1='Día de partido', e2='Tu turno',
        tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige la forma correcta',
        rT='Verbos que llevan -ing',
        rL1='Después de estos verbos va la forma -ING, no TO + verbo.',
        pStop='Cuidado: stop',
        rL2='STOP + -ING: ya no lo haces.',
        rL3='STOP + TO: paras para hacer otra cosa.',
        rMT='Tus errores, corregidos', pCard='Tarjeta roja → gol',
        gapT='Escribe la forma -ing', gHint='Usa el verbo entre paréntesis.',
        gw1='MIND + -ING: «Would you mind sending …?»', gw2='SUGGEST + -ING: suggested starting.', gw3='RISK + -ING: risk losing.',
        orderT='Construye la oración', orderHint='Haz clic en las piezas en orden. Sobra una pieza.',
        o1w='THINK ABOUT + -ING: después de una preposición el verbo lleva -ING. Sobra TO BUY.',
        o2w='FINISH + -ING: finished designing. Sobra TO DESIGN.',
        actTitle='El encargo de diseño', actUse='Usa al menos tres:',
        actSpeakBrief='En parejas: uno es diseñador y el otro cliente.',
        actSpeak1='Cliente: di qué te gusta (ENJOY) y qué quieres evitar (AVOID) en el nuevo logo.',
        actSpeak2='Diseñador: recomienda dos cosas (RECOMMEND + -ING) y di cuándo terminarás (FINISH DESIGNING).',
        actSpeak3='Cambien los papeles. Hablen de un proyecto que cambiaban una y otra vez (KEPT CHANGING).',
        actWriteKind='Escritura',
        actWriteBrief='Escribe un correo a una clienta (100–120 palabras) sobre un cartel nuevo: qué recomiendas hacer (RECOMMEND doing), qué sugieres evitar (SUGGEST avoiding) y cuándo esperas terminar de diseñarlo (FINISH designing).',
        actPlaceholder='Dear Ms Weber, …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T)
