# -*- coding: utf-8 -*-
"""The Truth About the Harry Quebert Affair (B2): narrative tenses and
thriller vocabulary. House style 1, 24 slides.

Rebuilt 2026-11-06 from `harry-quebert-b2.html`: an original case-file
synopsis (written for the lesson, not an excerpt), the three narrative
tenses, and sixteen items in three parts (vocabulary, tenses, reading).
All of it is kept; the reading questions now come straight after the case
file they ask about.

Fixed:
  * Four keys were the only long option: the definitions of REMAINS, ALIBI
    and ALLEGATIONS, and reading Q4. The distractors now match them.
  * Two tense items had a second right answer: "While Marcus READ the old
    letters, he found a name" and "because someone DUG UP the garden the
    week before" are both good English. Now the first offers wrong forms
    only, and the second asks for HAD … DUG with ALREADY.
  * "Marcus believed his mentor's innocence" — one believes IN someone's
    innocence. And the explanation no longer says BELIEVE "rarely takes a
    continuous form": the test is whether WAS BELIEVING works in this
    sentence, and a belief is a state, not an action in progress.
Added: a gap slide, speaking fields and the activation.

Run from the repo root:  py lesson-template/build/build_harry_quebert.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='harry-quebert-b2.html',
    title='The Truth About the Harry Quebert Affair (B2)',
    folder='HarryQuebert',
    scheme='slate',
    style='hs1',
    # House style 1 (HOUSE-STYLE §000, 2026-11-09): Midjourney plates, his style
    # images at --stylize 200, one per slide, briefs here.
    plates={
        'hero': 'a writer standing before a white clapboard house by the sea in a small New England town',
        'talk': 'a stack of crime novels and a magnifying glass on a café table',
        'case': 'police tape around a seaside garden, investigators digging under a white tent',
        'c1': 'an old writer on the porch of a white seaside house',
        'c2': 'a young writer staring at a blank typewriter page in a New York apartment',
        'c3': 'police officers digging in the garden of a seaside house',
        'c4': 'a young man driving along a coastal road towards a small town',
        'a1': 'two detectives opening a dusty box of old case files',
        'a2': 'forensic investigators kneeling over a dig in a garden',
        'a3': 'a detective in front of a wall of photographs linked by red string',
        'a4': 'a nervous man showing a cinema ticket to a detective',
        'a5': 'worried locals whispering over coffee in a small-town diner',
        'a6': 'a journalist going through archive boxes late at night by lamplight',
        'b1': 'an old man at the window of a white seaside house he has lived in for decades',
        'b2': 'a man reading a bundle of old letters by lamplight',
        'b3': 'an empty forest road at dusk in summer, a bicycle lying in the grass',
        'b4': 'workers arriving at a garden where a hole has already been dug',
        'b5': 'the peaceful main street of a small seaside town on a summer evening',
        'b6': 'a determined young man getting out of a car in a small seaside town',
        'talk2': 'two friends discussing a novel in a bookshop café',
        'results': 'a pile of handwritten manuscript pages on a desk by a window to the sea',
    },
    pop={'hero': (None, 'square'), 'talk2': (None, 'blob')},
    results='results',
)


def q(stem, options, n):
    return dict(stem=stem, options=options, correct=0, why='w%d' % n)


CASE = ('In the summer of 1975, a fifteen-year-old girl named Nola disappeared from the quiet town of Aurora. '
        'Thirty-three years later, the case reopened when workers found human remains buried in the garden of Harry '
        'Quebert, a celebrated novelist who had been living peacefully in the town ever since. Quebert’s former student, '
        'a young writer named Marcus Goldman, was struggling with a severe case of writer’s block when the scandal broke. '
        'Convinced that his mentor was innocent, Marcus travelled to Aurora to dig deeper into the affair himself. As he '
        'interviewed old neighbours and searched through forgotten letters, he slowly uncovered a web of lies that had '
        'protected the town for over three decades.')
CASE_SLIDE = '''
    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="eC">Case file</div>
        <h2 class="slide-title" data-i18n="cT">Aurora, New Hampshire</h2>
      </div></div>
      <div class="slide-body">
        <div class="card" style="padding:26px 32px">
          <p class="prose" style="font-size:19.5px;line-height:1.58">%s</p>
          <p class="prose dim" style="margin-top:12px;font-size:14.5px" data-i18n="cNote">A short original synopsis written for this lesson — not an excerpt from the novel.</p>
        </div>
      </div>
    </section>
''' % CASE

READ = [
    q('How long had Harry been living in Aurora before the case reopened?',
      ['Over three decades', 'About five years', 'Since the previous summer', 'Only a few months'], 13),
    q('What was Marcus struggling with when the scandal broke?',
      ['Severe writer’s block', 'A police investigation into himself', 'A lack of money', 'A disagreement with Harry'], 14),
    q('What was found in Harry Quebert’s garden?', ['Human remains', 'Old love letters', 'A missing manuscript', 'Nola’s diary'], 15),
    q('Why did Marcus decide to go to Aurora himself?',
      ['He believed his mentor was innocent', 'The police had ordered him to go there', 'He wanted to sell a news story', 'He was one of Nola’s relatives'], 16),
]
VOCAB = [
    q('Police decided to ____ the case after new evidence was found near Harry’s house.', ['reopen', 'rewrite', 'reorder', 'reclaim'], 1),
    q('In a police report, “remains” most likely refers to …',
      ['a body, or part of one, found after death', 'the food that was left behind at a crime scene', 'the documents that a suspect left behind', 'the money that someone leaves in a will'], 2),
    q('The idiom “a web of lies” describes …',
      ['a complicated network of connected lies', 'a single lie told to protect someone', 'a lie told over the internet', 'an accidental mistake'], 3),
    q('An “alibi” is …',
      ['proof that someone was somewhere else at the time', 'the lawyer who defends a suspect in court', 'a confession that a suspect has written down', 'the reason a person had for committing a crime'], 4),
    q('“Allegations” are …',
      ['accusations that have not been proven yet', 'facts that a court has already confirmed', 'the official records kept by the police', 'the people who saw a crime take place'], 5),
    q('If a journalist decides to “dig deeper” into a story, they …',
      ['investigate it more thoroughly', 'stop reporting on it for good', 'publish it straight away', 'hand it over to the police'], 6),
]
TENSE = [
    q('By the time Marcus arrived in Aurora, Harry ____ there for over thirty years.', ['had lived', 'was living', 'lived', 'has lived'], 7),
    q('While Marcus ____ the old letters, he found a name he didn’t recognise.', ['was reading', 'reads', 'had been read', 'were reading'], 8),
    q('Nola ____ from Aurora in the summer of 1975.', ['disappeared', 'was disappearing', 'had disappeared', 'disappears'], 9),
    q('When the workers arrived, someone ____ already ____ part of the garden.', ['had / dug up', 'has / dug up', 'was / digging up', 'did / dig up'], 10),
    q('The town ____ peacefully when the scandal suddenly broke.', ['was living', 'lived', 'had lived', 'lives'], 11),
    q('Marcus ____ in his mentor’s innocence and travelled to Aurora to prove it.', ['believed', 'was believing', 'had believed', 'believes'], 12),
]

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'Do you like crime novels or detective series?',
        'What makes a good mystery story?',
        'Have you ever read a book that surprised you at the end?',
        'Why do old crimes still interest people?',
        'Would you like to be a detective? Why, or why not?',
        'What was the last story you couldn’t stop reading?',
    ], 'talk', 3),
    ('stage',),
    ('raw', CASE_SLIDE, 'case'),
    ('mc', 'e3', 'mcT', READ, ['c1', 'c2', 'c3', 'c4'], None),
    ('stage',),
    ('mc', 'e1', 'mcT', VOCAB, ['a1', 'a2', 'a3', 'a4', 'a5', 'a6'], None),
    ('rules', 'eR', 'rT', [
        ('Past simple', ['rS1'], 'Nola <strong>disappeared</strong> in 1975. Marcus <strong>travelled</strong> to Aurora.'),
        ('Past continuous', ['rC1'], 'Marcus <strong>was struggling</strong> with writer’s block when the scandal <strong>broke</strong>.'),
        ('Past perfect', ['rP1'], 'Harry <strong>had lived</strong> there for thirty years before Marcus <strong>arrived</strong>.'),
    ], None),
    ('stage',),
    ('mc', 'e2', 'mcT', TENSE, ['b1', 'b2', 'b3', 'b4', 'b5', 'b6'], None),
    ('gap', 'e2', 'gapT', 'gHint', [
        ('When the police ______ (arrive), the journalists were already waiting outside.', ['arrived'], 'gw1'),
        ('Marcus ______ (write) his second novel when he heard the news.', ['was writing'], 'gw2'),
        ('Nobody knew that Harry ______ (meet) Nola years before.', ['had met'], 'gw3'),
    ]),
    ('talk', 'eT', 'tk2T', [
        'Tell the story of a strange day: what <strong>was</strong> everyone <strong>doing</strong> when it began?',
        'What <strong>had</strong> you <strong>done</strong> before you started learning English?',
        'Do you have an <strong>alibi</strong> for last Saturday night?',
        'Which news story would you like to <strong>dig deeper</strong> into?',
        'When should the police <strong>reopen</strong> an old case?',
        'Can <strong>allegations</strong> ruin an innocent person’s life?',
    ], 'talk2', 3),
]
SPEC['chips'] = ['had already', 'was struggling', 'dig deeper', 'alibi', 'a web of lies', 'reopened']

W = {
    'en': [
        'REOPEN a case: start investigating it again after it was closed.',
        'REMAINS: the formal word in crime reports for a dead body.',
        'A WEB OF LIES: many lies connected to and supporting each other, like a spider’s web.',
        'An ALIBI: evidence that a suspect was somewhere else when the crime happened.',
        'ALLEGATIONS: accusations without proof yet. They may or may not be true.',
        'DIG DEEPER: investigate more thoroughly.',
        'BY THE TIME + past simple: the earlier, longer state takes the past perfect, HAD LIVED.',
        'WHILE + a background action in progress: WAS READING. MARCUS is one person, so not WERE.',
        'One finished event that moves the story on: the past simple, DISAPPEARED.',
        'Earlier than the arrival, with ALREADY: HAD … DUG UP, the past perfect.',
        'The scene in progress, interrupted by an event: WAS LIVING … when the scandal BROKE.',
        'A belief is a state, not an action happening at one moment, so WAS BELIEVING does not work here. One believes IN someone’s innocence.',
        'He had lived there since 1975, and the case reopened 33 years later: over three decades.',
        'The text: “was struggling with a severe case of writer’s block”.',
        'Workers found human remains in the garden; that is what reopened the case.',
        'He was “convinced that his mentor was innocent” and went to dig deeper himself.',
    ],
    'de': [
        'REOPEN a case: einen Fall wieder aufnehmen, nachdem er abgeschlossen war.',
        'REMAINS: das formelle Wort im Polizeibericht für eine Leiche (sterbliche Überreste).',
        'A WEB OF LIES: viele Lügen, die zusammenhängen und sich stützen, wie ein Spinnennetz („ein Lügengeflecht“).',
        'An ALIBI: der Beweis, dass ein Verdächtiger zur Tatzeit woanders war.',
        'ALLEGATIONS: Vorwürfe, die noch nicht bewiesen sind. Sie können stimmen oder nicht.',
        'DIG DEEPER: gründlicher nachforschen.',
        'BY THE TIME + Past Simple: Der frühere, längere Zustand steht im Past Perfect, HAD LIVED.',
        'WHILE + eine Hintergrundhandlung im Verlauf: WAS READING. MARCUS ist eine Person, also nicht WERE.',
        'Ein abgeschlossenes Ereignis, das die Geschichte vorantreibt: Past Simple, DISAPPEARED.',
        'Früher als die Ankunft, mit ALREADY: HAD … DUG UP, Past Perfect.',
        'Die Szene im Verlauf, unterbrochen von einem Ereignis: WAS LIVING … when the scandal BROKE.',
        'Ein Glaube ist ein Zustand, keine Handlung in einem Moment, also passt WAS BELIEVING hier nicht. Man glaubt IN someone’s innocence.',
        'Er lebte seit 1975 dort, und der Fall wurde 33 Jahre später wieder aufgenommen: über drei Jahrzehnte.',
        'Im Text: „was struggling with a severe case of writer’s block“ (Schreibblockade).',
        'Arbeiter fanden menschliche Überreste im Garten; deshalb wurde der Fall wieder aufgenommen.',
        'Er war „convinced that his mentor was innocent“ und wollte selbst nachforschen.',
    ],
    'es': [
        'REOPEN a case: reabrir un caso que estaba cerrado.',
        'REMAINS: la palabra formal de los informes policiales para un cadáver (restos).',
        'A WEB OF LIES: muchas mentiras conectadas que se sostienen entre sí, como una telaraña («una red de mentiras»).',
        'An ALIBI: la prueba de que un sospechoso estaba en otro lugar cuando ocurrió el crimen (coartada).',
        'ALLEGATIONS: acusaciones todavía sin pruebas. Pueden ser ciertas o no.',
        'DIG DEEPER: investigar más a fondo.',
        'BY THE TIME + past simple: el estado anterior y más largo va en past perfect, HAD LIVED.',
        'WHILE + una acción de fondo en curso: WAS READING. MARCUS es una persona, así que no WERE.',
        'Un hecho terminado que hace avanzar la historia: past simple, DISAPPEARED.',
        'Antes de la llegada, con ALREADY: HAD … DUG UP, past perfect.',
        'La escena en curso, interrumpida por un hecho: WAS LIVING … when the scandal BROKE.',
        'Una creencia es un estado, no una acción en un momento, así que WAS BELIEVING no funciona aquí. Se cree IN someone’s innocence.',
        'Vivía allí desde 1975 y el caso se reabrió 33 años después: más de tres décadas.',
        'El texto: «was struggling with a severe case of writer’s block» (bloqueo del escritor).',
        'Unos obreros encontraron restos humanos en el jardín; por eso se reabrió el caso.',
        'Estaba «convinced that his mentor was innocent» y quiso investigar él mismo.',
    ],
}

T = {
    'en': dict(
        coverTitle='The Harry <br><em>Quebert Affair</em>',
        coverSub='A literary mystery: investigate a decades-old disappearance with narrative tenses and thriller vocabulary, one clue at a time.',
        chipLevel='B2', chipFocus='narrative tenses · crime vocabulary', chipCount='24 slides',
        eW='Warm-up', eT='Let’s talk', eR='The rule', eC='Case file', e1='Thriller vocabulary', e2='Narrative tenses', e3='Reading',
        cT='Aurora, New Hampshire', cNote='A short original synopsis written for this lesson — not an excerpt from the novel.',
        tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the best answer',
        rT='Three past tenses for a story',
        rS1='Moves the main story forward: one finished event after another.',
        rC1='Sets the scene, or is interrupted by an event.',
        rP1='Shows what had already happened before the main story.',
        gapT='Tell the story', gHint='Past simple, past continuous or past perfect? Use the verb in brackets.',
        gw1='The event that moves the story on: ARRIVED. The journalists were already there (past continuous).',
        gw2='The background, interrupted by the news: WAS WRITING.',
        gw3='Earlier than “nobody knew”: HAD MET.',
        actTitle='Reopen the case', actUse='Use at least four:',
        actSpeakBrief='In pairs: one of you is a journalist, the other a neighbour in Aurora in 1975.',
        actSpeak1='Journalist: ask what the neighbour WAS DOING on the evening Nola DISAPPEARED.',
        actSpeak2='Neighbour: say what you HAD SEEN earlier that week. Do you have an ALIBI?',
        actSpeak3='Swap roles and DIG DEEPER: find one lie in your partner’s story.',
        actWriteKind='Writing',
        actWriteBrief='Write the opening of a news article (150–180 words) about a case that has been reopened. Use all three narrative tenses: what HAPPENED, what people WERE DOING, and what HAD HAPPENED before.',
        actPlaceholder='Thirty-three years after a teenager vanished …',
    ),
    'de': dict(
        coverTitle='The Harry <br><em>Quebert Affair</em>',
        coverSub='Ein literarischer Krimi: Ermittle in einem jahrzehntealten Verschwinden — mit Erzählzeiten und Thriller-Vokabular, Hinweis für Hinweis.',
        chipLevel='B2', chipFocus='Erzählzeiten · Krimi-Vokabular', chipCount='24 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Die Regel', eC='Fallakte', e1='Thriller-Vokabular', e2='Erzählzeiten', e3='Lesen',
        cT='Aurora, New Hampshire', cNote='Eine kurze, eigens für diese Lektion geschriebene Zusammenfassung — kein Auszug aus dem Roman.',
        tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle die beste Antwort',
        rT='Drei Vergangenheitsformen zum Erzählen',
        rS1='Treibt die Haupthandlung voran: ein abgeschlossenes Ereignis nach dem anderen.',
        rC1='Beschreibt die Szene oder wird von einem Ereignis unterbrochen.',
        rP1='Zeigt, was vor der Haupthandlung schon passiert war.',
        gapT='Erzähl die Geschichte', gHint='Past Simple, Past Continuous oder Past Perfect? Verwende das Verb in Klammern.',
        gw1='Das Ereignis, das die Geschichte vorantreibt: ARRIVED. Die Journalisten waren schon da (Past Continuous).',
        gw2='Der Hintergrund, unterbrochen von der Nachricht: WAS WRITING.',
        gw3='Früher als „nobody knew“: HAD MET.',
        actTitle='Der Fall wird neu aufgerollt', actUse='Verwende mindestens vier:',
        actSpeakBrief='Zu zweit: Eine Person ist Journalistin, die andere eine Nachbarin in Aurora im Jahr 1975.',
        actSpeak1='Journalistin: Frag, was die Nachbarin an dem Abend tat (WAS DOING), als Nola verschwand (DISAPPEARED).',
        actSpeak2='Nachbarin: Sag, was du früher in der Woche gesehen hattest (HAD SEEN). Hast du ein ALIBI?',
        actSpeak3='Tauscht die Rollen und forscht nach (DIG DEEPER): Findet eine Lüge in der Geschichte des anderen.',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib den Anfang eines Zeitungsartikels (150–180 Wörter) über einen wieder aufgenommenen Fall. Verwende alle drei Erzählzeiten: was passierte, was die Leute gerade taten und was vorher passiert war.',
        actPlaceholder='Thirty-three years after a teenager vanished …',
    ),
    'es': dict(
        coverTitle='The Harry <br><em>Quebert Affair</em>',
        coverSub='Un misterio literario: investiga una desaparición de hace décadas con los tiempos narrativos y vocabulario de thriller, pista a pista.',
        chipLevel='B2', chipFocus='tiempos narrativos · vocabulario policiaco', chipCount='24 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='La regla', eC='Expediente', e1='Vocabulario de thriller', e2='Tiempos narrativos', e3='Lectura',
        cT='Aurora, New Hampshire', cNote='Un breve resumen original escrito para esta lección, no un fragmento de la novela.',
        tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige la mejor respuesta',
        rT='Tres pasados para contar una historia',
        rS1='Hace avanzar la historia principal: un hecho terminado tras otro.',
        rC1='Describe la escena, o se ve interrumpido por un hecho.',
        rP1='Muestra lo que ya había pasado antes de la historia principal.',
        gapT='Cuenta la historia', gHint='¿Past simple, past continuous o past perfect? Usa el verbo entre paréntesis.',
        gw1='El hecho que hace avanzar la historia: ARRIVED. Los periodistas ya estaban allí (past continuous).',
        gw2='El fondo, interrumpido por la noticia: WAS WRITING.',
        gw3='Antes de «nobody knew»: HAD MET.',
        actTitle='Reabrir el caso', actUse='Usa al menos cuatro:',
        actSpeakBrief='En parejas: uno es periodista y el otro un vecino de Aurora en 1975.',
        actSpeak1='Periodista: pregunta qué estaba haciendo el vecino (WAS DOING) la tarde en que Nola desapareció (DISAPPEARED).',
        actSpeak2='Vecino: di lo que habías visto antes esa semana (HAD SEEN). ¿Tienes una coartada (ALIBI)?',
        actSpeak3='Cambien los papeles e investiguen más a fondo (DIG DEEPER): encuentren una mentira en la historia del otro.',
        actWriteKind='Escritura',
        actWriteBrief='Escribe el comienzo de una noticia (150–180 palabras) sobre un caso reabierto. Usa los tres tiempos narrativos: lo que pasó, lo que la gente estaba haciendo y lo que había pasado antes.',
        actPlaceholder='Thirty-three years after a teenager vanished …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T)
