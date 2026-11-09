# -*- coding: utf-8 -*-
"""Past Simple vs Present Perfect — Golf Edition (B1). House style 1, 24 slides.

Rebuilt 2026-11-06 from `forbes-english-golf-lesson.html` (free), a tabbed
page: theory (the difference, time signals, side-by-side pairs), eight
multiple-choice items, six gap-fills and six "correct the error" items.
All twenty items are kept. The page's only picture is a 1200x671 library
card, so the deck is on stand-ins and the card stays its thumbnail.

Fixed:
  * Every MC hint named the tense ("Clue: 'yesterday' = finished, specific
    time"). The hints now point at the clue without naming the answer.
  * MC2: McIlroy has won the Open once, not "four times". Real players now
    carry only facts that will not date (Woods won the 2005 Masters and the
    2019 Masters); the career counts are a fictional player's.
  * MC8: the blank before "already" built "has achieved already three
    top-ten finishes". The adverb is now in the right place.
  * Gap 4 ("The tournament ___ just ___") and gap 5 ("How many majors ___
    Nicklaus ___") had two blanks and ONE answer string ("has just
    started", "did nicklaus win"): no learner could ever be marked right.
    Each blank now has its own answer.
  * "Correct the error" had two options each, and two "errors" are good
    English: "Did you ever play Augusta?" (US usage) and "The committee
    already decided the layout". Those items now test the FORM, and every
    item has three options, so the key is no longer simply the longer one.
  * "Since always triggers present perfect" was attached to "How long have
    you played golf since you started?", which no one says. Rewritten.

Run from the repo root:  py lesson-template/build/build_golf_ps_pp.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='forbes-english-golf-lesson.html',
    title='Past Simple vs Present Perfect — Golf Edition (B1)',
    folder='Golf',
    scheme='sage',
    style='hs1',
    # House style 1 (HOUSE-STYLE §000, 2026-11-09): hero = the fairway plate
    # that was the library card; one Midjourney plate per slide besides,
    # his style images at --stylize 200, briefs here.
    plates={
        'hero': 'a golf fairway at dusk',
        'talk': 'a golf buggy parked beside a green, two bags on the back',
        'r-trophy': 'a golfer lifting a silver trophy on the eighteenth green',
        'q1': 'a golfer punching the air as her putt drops into the hole',
        'q2': 'a young woman golfer standing in front of a shelf with three trophies',
        'q3': 'a twelve-year-old girl swinging a golf club on a driving range',
        'q4': 'an old stone golf clubhouse with flags flying and a white marquee',
        'q5': 'a golf bag left alone in the open boot of a car in a car park',
        'q6': 'a caddie handing a golfer a club from the bag on a fairway',
        'q7': 'a golf ball rolling into the hole on a green, the tee far away',
        'q8': 'a woman golfer walking up the final fairway as a crowd applauds',
        'e1': 'a green blazer on a hanger in a wooden locker room',
        'e2': 'pink azaleas in bloom beside a golf hole with a small white stone bridge',
        'e3': 'three golf balls lying under the water of a pond, a golfer peering in',
        'e4': 'an older grey-haired woman golfer in mid-swing on a fairway',
        'e5': 'club committee members around a table studying a golf course map',
        'e6': 'a worn leather golf glove and an old battered golf club on a bench',
        'talk2': 'two friends talking over coffee on a golf clubhouse terrace',
        'results': 'a golf flag on the last green at sunset, one ball beside the hole',
    },
    pop={'hero': (None, 'square'), 'q5': (None, 'free'), 'e6': (None, 'blob')},
    results='results',
    # the hint line under each stem (ctx) costs a row: tighter options and
    # gap rows keep the answered state inside the slide (answered-overflow)
    css='html[data-style="editorial"] .slide:has(.q-ctx) .opt { padding-top: 7px; padding-bottom: 7px; }',
    gap_size=20,
)


def q(stem, options, n, ctx=None):
    d = dict(stem=stem, options=options, correct=0, why='w%d' % n)
    if ctx:
        d['ctx'] = ctx
    return d


MC = [
    q('The player ____ a fantastic birdie on the 15th hole yesterday.', ['scored', 'has scored', 'has been scoring', 'was scoring'], 1, 'hTime'),
    q('Ella Ross ____ three major championships so far in her career, and she is only 26.', ['has won', 'won', 'was winning', 'had won'], 2, 'hNow'),
    q('She ____ golf since she was twelve years old, and she is still improving.', ['has played', 'played', 'plays', 'was playing'], 3, 'hSince'),
    q('The club ____ the championship in 1895, 1921 and 1946.', ['hosted', 'has hosted', 'is hosting', 'had hosted'], 4, 'hTime'),
    q('He can’t start the round — he ____ his golf bag in the car park!', ['has left', 'left', 'was leaving', 'had left'], 5, 'hNow'),
    q('The caddie ____ her the wrong club during the final round last Sunday.', ['gave', 'has given', 'gives', 'has been giving'], 6, 'hTime'),
    q('Have you ever ____ a hole-in-one?', ['scored', 'scoring', 'to score', 'score'], 7, 'hForm'),
    q('This season Ella ____ already ____ three top-ten finishes.', ['has / achieved', 'did / achieve', 'is / achieving', 'was / achieved'], 8, 'hSeason'),
]
ERR = [
    q('Which sentence is correct?', ['He won the Masters in 2005.', 'He has won the Masters in 2005.', 'He has win the Masters in 2005.'], 15, 'hTime'),
    q('Which question is correct?', ['Have you ever played Augusta National?', 'Have you ever play Augusta National?',
                                    'Did you ever played Augusta National?'], 16, 'hForm'),
    q('Which sentence is correct?', ['I lost three balls yesterday.', 'I have lost three balls yesterday.',
                                    'I have losed three balls yesterday.'], 17, 'hTime'),
    q('Which sentence is correct?', ['She has played golf for 20 years, and she is still competing.',
                                    'She played golf for 20 years, and she is still competing.',
                                    'She is playing golf for 20 years, and she is still competing.'], 18, 'hNow'),
    q('Which sentence is correct?', ['The committee has already decided the layout, so we can print the maps.',
                                    'The committee already decides the layout, so we can print the maps.',
                                    'The committee has already decide the layout, so we can print the maps.'], 19, 'hForm'),
    q('You want to know how many years someone has been a golfer. Which question is correct?',
      ['How long have you played golf?', 'How long do you play golf?', 'How long are you playing golf?'], 20, 'hSince'),
]
APOS = lambda *xs: '|'.join(sorted({v for x in xs for v in (x, x.replace('’', "'"), x.replace("'", '’'))}))

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'Have you ever played golf?',
        'What sport did you play as a child?',
        'Which sports star do you admire?',
        'What is the best match you have ever watched?',
        'Where did you go last weekend?',
        'What have you done this week that you are proud of?',
    ], 'talk', 3),
    ('stage',),
    ('rules', 'eR', 'rDT', [
        ('Past simple', ['rP1', 'rP2'], 'Tiger Woods <strong>won</strong> the Masters in 2005. She <strong>played</strong> her best round yesterday.'),
        ('Present perfect', ['rQ1', 'rQ2'], 'She <strong>has won</strong> three majors. She <strong>has lost</strong> her 7-iron — she can’t find it!'),
    ], 'r-trophy'),
    ('rules', 'eR', 'rST', [
        ('Past simple', [(None, 'yesterday · last week · in 1997'), (None, 'two years ago · when I was …'),
                         (None, 'in the 2000s · at the Open')], None),
        ('Present perfect', [(None, 'already · yet · just'), (None, 'ever · never · so far'),
                             (None, 'this season · recently · since · for')], None),
        ('pWatch', ['rW1'], 'This season she <strong>has played</strong> well. (Still going.) · Last season she <strong>played</strong> well.'),
    ], None),
    ('rules', 'eR', 'rPT', [
        ('pPair', [(None, 'He <strong>scored</strong> a hole-in-one in 2019.')], 'He <strong>has scored</strong> a hole-in-one. (at some point in his life)'),
        ('pPair', [(None, 'The caddie <strong>gave</strong> her the wrong club on the 18th.')], 'The caddie <strong>has given</strong> her the wrong club — she’s furious!'),
        ('pPair', [(None, 'The club <strong>hosted</strong> the Open last summer.')], 'The club <strong>has hosted</strong> the Open three times.'),
    ], None),
    ('mc', 'e1', 'mcT', MC, ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'], None),
    ('gap', 'e2', 'gapT', 'gHint', [
        ('The ball ______ (fall) into the water on hole 12. We never found it.', ['fell'], 'w9'),
        ('She ______ (not / play) this course before. It’s her first time here.',
         [APOS('hasn’t played', 'has not played', 'has never played')], 'w10'),
        ('Tiger Woods ______ (complete) his comeback in 2019, when he won the Masters.', ['completed'], 'w11'),
    ]),
    ('gap', 'e2', 'gapT', 'gHint', [
        ('The tournament ______ just ______ (start), and the scores are coming in.', ['has', 'started'], 'w12'),
        ('How many majors ______ Jack Nicklaus ______ (win) in his career?', ['did', 'win'], 'w13'),
        ('She ______ (practise) for six hours, and now she is exhausted.',
         [APOS('has practised', 'has practiced', 'has been practising', 'has been practicing', '’s practised', '’s been practising')], 'w14'),
    ]),
    ('stage',),
    ('mc', 'e3', 'mcT', ERR, ['e1', 'e2', 'e3', 'e4', 'e5', 'e6'], None),
    ('talk', 'eT', 'tk2T', [
        'What sport <strong>have you</strong> never <strong>tried</strong>?',
        'When <strong>did you</strong> last <strong>play</strong> a sport?',
        'What <strong>have you</strong> already <strong>done</strong> today?',
        'Which famous match <strong>did you watch</strong> as a child?',
        'How long <strong>have you known</strong> your best friend?',
        'What <strong>has changed</strong> in your town since 2020?',
    ], 'talk2', 3),
]
SPEC['chips'] = ['won', 'have you ever', 'last season', 'has already', 'since', 'yesterday', 'has played']

W = {
    'en': [
        'YESTERDAY is a finished time, so the past simple: SCORED.',
        'SO FAR IN HER CAREER, and she is still playing: the present perfect, HAS WON.',
        'SINCE SHE WAS TWELVE, and still improving: from then until now, HAS PLAYED.',
        'Three dates, all finished: the past simple, HOSTED.',
        'The bag is still missing NOW: the present perfect, HAS LEFT.',
        'LAST SUNDAY is a finished time: the past simple, GAVE.',
        'HAVE YOU EVER + the past participle: SCORED.',
        'THIS SEASON is still going, and ALREADY sits between HAS and the participle: HAS ALREADY ACHIEVED.',
        'A finished event in a story: the past simple, FELL (fall – fell – fallen).',
        'BEFORE + a first time now: the present perfect, HASN’T PLAYED.',
        'IN 2019 is a finished time: the past simple, COMPLETED.',
        'JUST + very recent and relevant now: HAS JUST STARTED.',
        'Nicklaus has retired; his career is finished: the past simple question DID … WIN?',
        'The practice is over and the result is visible now: HAS PRACTISED (or HAS BEEN PRACTISING).',
        '2005 is a finished year: no present perfect with a past date. HE WON.',
        'EVER + HAVE + the past participle: HAVE you ever PLAYED?',
        'YESTERDAY is a finished time: I LOST. And LOSE is irregular: lose – lost – lost.',
        'She is STILL competing: from then until now, HAS PLAYED … FOR 20 YEARS.',
        'HAS ALREADY DECIDED: done, and the result matters now — we can print. HAS + participle, not the base form.',
        'From then until now: HOW LONG HAVE YOU PLAYED? German and Spanish use the present here; English does not.',
    ],
    'de': [
        'YESTERDAY ist ein abgeschlossener Zeitpunkt, also Past Simple: SCORED.',
        'SO FAR IN HER CAREER, und sie spielt noch: Present Perfect, HAS WON.',
        'SINCE SHE WAS TWELVE, und sie wird immer besser: von damals bis jetzt, HAS PLAYED.',
        'Drei Jahreszahlen, alle vorbei: Past Simple, HOSTED.',
        'Die Tasche fehlt JETZT noch: Present Perfect, HAS LEFT.',
        'LAST SUNDAY ist ein abgeschlossener Zeitpunkt: Past Simple, GAVE.',
        'HAVE YOU EVER + Partizip: SCORED.',
        'THIS SEASON läuft noch, und ALREADY steht zwischen HAS und dem Partizip: HAS ALREADY ACHIEVED.',
        'Ein abgeschlossenes Ereignis in einer Geschichte: Past Simple, FELL (fall – fell – fallen).',
        'BEFORE + zum ersten Mal jetzt: Present Perfect, HASN’T PLAYED.',
        'IN 2019 ist ein abgeschlossener Zeitpunkt: Past Simple, COMPLETED.',
        'JUST + ganz kürzlich und jetzt wichtig: HAS JUST STARTED.',
        'Nicklaus hat aufgehört; seine Karriere ist vorbei: die Frage im Past Simple, DID … WIN?',
        'Das Training ist vorbei, das Ergebnis sieht man jetzt: HAS PRACTISED (oder HAS BEEN PRACTISING).',
        '2005 ist ein abgeschlossenes Jahr: kein Present Perfect mit einer Jahreszahl. HE WON.',
        'EVER + HAVE + Partizip: HAVE you ever PLAYED?',
        'YESTERDAY ist vorbei: I LOST. LOSE ist unregelmäßig: lose – lost – lost.',
        'Sie spielt NOCH: von damals bis jetzt, HAS PLAYED … FOR 20 YEARS.',
        'HAS ALREADY DECIDED: erledigt, und das zählt jetzt — wir können drucken. HAS + Partizip, nicht die Grundform.',
        'Von damals bis jetzt: HOW LONG HAVE YOU PLAYED? Im Deutschen steht hier das Präsens („Wie lange spielst du schon?“), im Englischen nicht.',
    ],
    'es': [
        'YESTERDAY es un momento terminado, así que past simple: SCORED.',
        'SO FAR IN HER CAREER, y sigue jugando: present perfect, HAS WON.',
        'SINCE SHE WAS TWELVE, y sigue mejorando: desde entonces hasta ahora, HAS PLAYED.',
        'Tres fechas, todas terminadas: past simple, HOSTED.',
        'La bolsa todavía falta AHORA: present perfect, HAS LEFT.',
        'LAST SUNDAY es un momento terminado: past simple, GAVE.',
        'HAVE YOU EVER + participio: SCORED.',
        'THIS SEASON sigue, y ALREADY va entre HAS y el participio: HAS ALREADY ACHIEVED.',
        'Un hecho terminado en una historia: past simple, FELL (fall – fell – fallen).',
        'BEFORE + es la primera vez ahora: present perfect, HASN’T PLAYED.',
        'IN 2019 es un momento terminado: past simple, COMPLETED.',
        'JUST + muy reciente: HAS JUST STARTED.',
        'Nicklaus ya se retiró: carrera terminada, pregunta en past simple: DID … WIN?',
        'Terminó de entrenar y se nota ahora: HAS PRACTISED (o HAS BEEN PRACTISING).',
        '2005 es un año terminado: nada de present perfect con una fecha pasada. HE WON.',
        'EVER + HAVE + participio: HAVE you ever PLAYED?',
        'YESTERDAY ya pasó: I LOST. LOSE es irregular: lose – lost – lost.',
        'Todavía compite: desde entonces hasta ahora, HAS PLAYED … FOR 20 YEARS.',
        'HAS ALREADY DECIDED: hecho, y eso importa ahora — podemos imprimir. HAS + participio, no la forma base.',
        'Desde entonces hasta ahora: HOW LONG HAVE YOU PLAYED? En español se usa el presente («¿Cuánto tiempo hace que juegas?»); en inglés, no.',
    ],
}

T = {
    'en': dict(
        coverTitle='Past Simple <br><em>vs Present Perfect</em>',
        coverSub='Golf edition: finished times and the present perfect’s link to now, the signal words, and twenty questions from the fairway.',
        chipLevel='B1', chipFocus='won · has won', chipCount='24 slides',
        eW='Warm-up', eT='Let’s talk', eR='The rule', e1='Which tense?', e2='Write the verb', e3='Correct the error',
        tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the right form',
        hTime='Look for the time word.', hNow='Does it connect to now?', hSince='From when until when?',
        hForm='Look at the form of the verb.', hSeason='Is the season over?',
        rDT='The key difference',
        rP1='A finished action at a time that is stated or clear.', rP2='The link to now is not important.',
        rQ1='A past action connected to NOW: no time given, or the result matters today.',
        rQ2='Experience, change, unfinished time.',
        rST='Signal words', pWatch='Watch out',
        rW1='THIS SEASON takes the present perfect while the season is still going, the past simple once it is over.',
        rPT='Side by side', pPair='Past simple → present perfect',
        gapT='Write the verb', gHint='Past simple or present perfect? Use the verb in brackets.',
        actTitle='The clubhouse', actUse='Use at least three:',
        actSpeakBrief='In pairs. Talk about sport, then and now.',
        actSpeak1='Ask your partner three HAVE YOU EVER …? questions. For every “yes”, ask WHEN DID YOU …?',
        actSpeak2='Tell your partner about a sport you PLAYED as a child, and one you HAVE NEVER TRIED.',
        actSpeak3='What HAVE you ALREADY done this week, and what did you do LAST weekend?',
        actWriteKind='Writing',
        actWriteBrief='Write a short profile of a sports person you admire (120–150 words): what they DID early in their career, and what they HAVE ACHIEVED so far.',
        actPlaceholder='She started playing when she was …',
    ),
    'de': dict(
        coverTitle='Past Simple <br><em>vs Present Perfect</em>',
        coverSub='Golf-Ausgabe: abgeschlossene Zeitpunkte und die Verbindung des Present Perfect zum Jetzt, die Signalwörter und zwanzig Fragen vom Fairway.',
        chipLevel='B1', chipFocus='won · has won', chipCount='24 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Die Regel', e1='Welche Zeitform?', e2='Schreib das Verb', e3='Korrigiere den Fehler',
        tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle die richtige Form',
        hTime='Achte auf die Zeitangabe.', hNow='Gibt es eine Verbindung zum Jetzt?', hSince='Von wann bis wann?',
        hForm='Achte auf die Form des Verbs.', hSeason='Ist die Saison vorbei?',
        rDT='Der entscheidende Unterschied',
        rP1='Eine abgeschlossene Handlung zu einem genannten oder klaren Zeitpunkt.', rP2='Die Verbindung zum Jetzt ist nicht wichtig.',
        rQ1='Eine vergangene Handlung mit Verbindung zum JETZT: keine Zeitangabe, oder das Ergebnis zählt heute.',
        rQ2='Erfahrung, Veränderung, nicht abgeschlossene Zeit.',
        rST='Signalwörter', pWatch='Achtung',
        rW1='THIS SEASON nimmt Present Perfect, solange die Saison läuft, und Past Simple, wenn sie vorbei ist.',
        rPT='Im Vergleich', pPair='Past Simple → Present Perfect',
        gapT='Schreib das Verb', gHint='Past Simple oder Present Perfect? Verwende das Verb in Klammern.',
        actTitle='Im Clubhaus', actUse='Verwende mindestens drei:',
        actSpeakBrief='Zu zweit. Sprecht über Sport, damals und heute.',
        actSpeak1='Stell deinem Partner drei Fragen mit HAVE YOU EVER …? Frag bei jedem „Ja“: WHEN DID YOU …?',
        actSpeak2='Erzähl von einer Sportart, die du als Kind gemacht hast (PLAYED), und einer, die du noch nie probiert hast (HAVE NEVER TRIED).',
        actSpeak3='Was hast du diese Woche schon gemacht (HAVE ALREADY), und was hast du letztes Wochenende gemacht (LAST)?',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib ein kurzes Porträt einer Sportlerin oder eines Sportlers, die du bewunderst (120–150 Wörter): was sie früh in ihrer Karriere gemacht hat (DID) und was sie bis jetzt erreicht hat (HAVE ACHIEVED).',
        actPlaceholder='She started playing when she was …',
    ),
    'es': dict(
        coverTitle='Past Simple <br><em>vs Present Perfect</em>',
        coverSub='Edición golf: momentos terminados y el vínculo del present perfect con el ahora, las palabras clave y veinte preguntas desde la calle.',
        chipLevel='B1', chipFocus='won · has won', chipCount='24 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='La regla', e1='¿Qué tiempo?', e2='Escribe el verbo', e3='Corrige el error',
        tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige la forma correcta',
        hTime='Busca la expresión de tiempo.', hNow='¿Tiene relación con el ahora?', hSince='¿Desde cuándo hasta cuándo?',
        hForm='Mira la forma del verbo.', hSeason='¿Ha terminado la temporada?',
        rDT='La diferencia clave',
        rP1='Una acción terminada en un momento dicho o claro.', rP2='La relación con el ahora no importa.',
        rQ1='Una acción pasada relacionada con el AHORA: sin fecha, o el resultado importa hoy.',
        rQ2='Experiencia, cambio, tiempo no terminado.',
        rST='Palabras clave', pWatch='Cuidado',
        rW1='THIS SEASON lleva present perfect mientras la temporada sigue, y past simple cuando ha terminado.',
        rPT='Lado a lado', pPair='Past simple → present perfect',
        gapT='Escribe el verbo', gHint='¿Past simple o present perfect? Usa el verbo entre paréntesis.',
        actTitle='En el club', actUse='Usa al menos tres:',
        actSpeakBrief='En parejas. Hablen de deporte, antes y ahora.',
        actSpeak1='Hazle a tu compañero tres preguntas con HAVE YOU EVER …? Por cada «sí», pregunta WHEN DID YOU …?',
        actSpeak2='Cuéntale un deporte que practicabas de niño (PLAYED) y uno que nunca has probado (HAVE NEVER TRIED).',
        actSpeak3='¿Qué has hecho ya esta semana (HAVE ALREADY) y qué hiciste el fin de semana pasado (LAST)?',
        actWriteKind='Escritura',
        actWriteBrief='Escribe un perfil corto de una deportista que admires (120–150 palabras): qué hizo al principio de su carrera (DID) y qué ha conseguido hasta ahora (HAVE ACHIEVED).',
        actPlaceholder='She started playing when she was …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T)
