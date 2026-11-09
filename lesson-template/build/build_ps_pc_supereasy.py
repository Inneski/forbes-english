# -*- coding: utf-8 -*-
"""Present Simple vs Present Continuous — Supereasy (A1, German support).
House style 1, 18 slides.

Rebuilt 2026-11-06 from `present_simple_continuous_de.html`, a ten-item
two-button test (simple or continuous) with a German translation and a
signal word under each sentence. All ten sentences are kept; the German
line is the click-to-reveal gloss, with Spanish added.

Changed:
  * Two options made every continuous key the conspicuously longer answer
    ("is writing" against "writes"), which the ANSWERS gate exists to stop.
    Each item now offers four forms of the same verb.
  * Item 8's explanation said LIKE is stative "so we never use it in the
    continuous form". Memory and practice disagree ("I'm liking this new
    job"); the test is whether IS LIKING works in THIS sentence, and a
    general taste for chocolate is not happening now.
Added: the rule as two pill-tab cards, a sort of the signal words, a gap
slide, the speaking fields and the activation.

Run from the repo root:  py lesson-template/build/build_ps_pc_supereasy.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H
import deck as D

SPEC = dict(
    out='present_simple_continuous_de.html',
    title='Present Simple vs Present Continuous — Supereasy (A1)',
    folder='PSPCSupereasy',
    scheme='warm',
    style='hs1',
    # House style 1 (HOUSE-STYLE §000, 2026-11-09): Midjourney plates, his style
    # images at --stylize 200, one per slide, briefs here.
    plates={
        'hero': 'a girl writing a letter at a sunny window',
        'talk': 'a busy family breakfast table in the morning',
        'r-daily': 'a big kitchen clock above a mug of coffee in the morning sun',
        's1': 'a girl writing a letter at her desk',
        's2': 'a man drinking coffee by a window in the morning',
        's3': 'a mother cooking dinner in a warm kitchen',
        's4': 'a baby crying in a cot',
        's5': 'students studying English in a classroom',
        't1': 'a boy playing football in a park',
        't2': 'a family watching a film together on the sofa',
        't3': 'a girl happily eating a bar of chocolate',
        't4': 'a dog running in a garden',
        't5': 'a child with a school bag walking to school',
        'talk2': 'two children chatting on a bench in the playground',
        'results': 'a school desk with an open exercise book and coloured pencils',
    },
    pop={'hero': (None, 'square'), 't4': (None, 'free'), 'talk2': (None, 'blob')},
    results='results',
)


def q(stem, options, n):
    return dict(stem=stem, options=options, correct=0, why='w%d' % n, gl='g%d' % n)


A = [
    q('Look! She ____ (write) a letter right now.', ['is writing', 'writes', 'is write', 'writing'], 1),
    q('I always ____ (drink) coffee in the morning.', ['drink', 'am drinking', 'drinks', 'drinking'], 2),
    q('My mum ____ (cook) dinner every day.', ['cooks', 'is cooking', 'cook', 'is cook'], 3),
    q('Listen! The baby ____ (cry) in the next room.', ['is crying', 'cries', 'is cry', 'crying'], 4),
    q('We ____ (study) English at the moment.', ['are studying', 'study', 'are study', 'is studying'], 5),
]
B = [
    q('He usually ____ (play) football on Saturdays.', ['plays', 'is playing', 'play', 'playing'], 6),
    q('Right now, they ____ (watch) a film together.', ['are watching', 'watch', 'is watching', 'are watch'], 7),
    q('She ____ (like) chocolate very much.', ['likes', 'is liking', 'like', 'liking'], 8),
    q('Look! The dog ____ (run) in the garden.', ['is running', 'runs', 'is runing', 'running'], 9),
    q('I ____ (go) to school every day.', ['go', 'am going', 'goes', 'going'], 10),
]

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'What do you do every morning?',
        'What are you doing right now?',
        'What do you usually eat for breakfast?',
        'Who do you live with?',
        'What do you do on Saturdays?',
        'What is your family doing at the moment?',
    ], 'talk', 3),
    ('stage',),
    ('rules', 'eR', 'rT', [
        ('Present simple', ['rS1', 'rS2'], 'I <strong>drink</strong> coffee every morning. She <strong>cooks</strong> every day.'),
        ('Present continuous', ['rC1', 'rC2'], 'Look! She <strong>is writing</strong> a letter. We <strong>are studying</strong> now.'),
    ], 'r-daily'),
    ('mc', 'e1', 'mcT', A, ['s1', 's2', 's3', 's4', 's5'], None),
    ('stage',),
    ('mc', 'e2', 'mcT', B, ['t1', 't2', 't3', 't4', 't5'], None),
    ('raw', None),  # the sort, filled in below once T exists
    ('gap', 'e3', 'gapT', 'gHint', [
        ('Shh! The children ______ (sleep).', ['are sleeping|’re sleeping|\'re sleeping'], 'gw1'),
        ('My brother ______ (work) in a bank.', ['works'], 'gw2'),
        ('I ______ (not / watch) TV right now.', ['am not watching|’m not watching|\'m not watching'], 'gw3'),
    ]),
    ('talk', 'eT', 'tk2T', [
        'What <strong>do</strong> you <strong>do</strong> every weekend?',
        'What <strong>are</strong> you <strong>wearing</strong> today?',
        'What <strong>is</strong> your best friend <strong>doing</strong> now, do you think?',
        'How <strong>do</strong> you usually <strong>go</strong> to work or school?',
        'What music <strong>do</strong> you <strong>like</strong>?',
        'What <strong>are</strong> you <strong>learning</strong> at the moment?',
    ], 'talk2', 3),
]
SPEC['chips'] = ['right now', 'usually', 'is', 'every day', 'are', 'at the moment', 'always']

W = {
    'en': [
        'RIGHT NOW and LOOK!: it is happening at this moment, so IS WRITING.',
        'ALWAYS: a habit, so the present simple. I DRINK (no -S with I).',
        'EVERY DAY: a routine, so the present simple. My mum = she → COOKS.',
        'LISTEN!: you can hear it now, so IS CRYING.',
        'AT THE MOMENT: happening now, so ARE STUDYING (we → ARE).',
        'USUALLY: a habit, so the present simple. He → PLAYS.',
        'RIGHT NOW: happening at this moment. They → ARE WATCHING.',
        'Liking chocolate is how she is in general, not something happening now: IS LIKING does not work here. She → LIKES.',
        'LOOK!: you can see it now, so IS RUNNING (run → runNing).',
        'EVERY DAY: a routine. I → GO.',
    ],
    'de': [
        'RIGHT NOW und LOOK!: Es passiert genau jetzt, also IS WRITING.',
        'ALWAYS: eine Gewohnheit, also Present Simple. I DRINK (kein -S bei I).',
        'EVERY DAY: eine Routine, also Present Simple. My mum = she → COOKS.',
        'LISTEN!: Man hört es jetzt, also IS CRYING.',
        'AT THE MOMENT: passiert gerade, also ARE STUDYING (we → ARE).',
        'USUALLY: eine Gewohnheit, also Present Simple. He → PLAYS.',
        'RIGHT NOW: passiert genau in diesem Moment. They → ARE WATCHING.',
        'Schokolade mögen ist, wie sie allgemein ist, nicht etwas, das gerade passiert: IS LIKING passt hier nicht. She → LIKES.',
        'LOOK!: Man sieht es jetzt, also IS RUNNING (run → runNing).',
        'EVERY DAY: eine Routine. I → GO.',
    ],
    'es': [
        'RIGHT NOW y LOOK!: está pasando en este momento, así que IS WRITING.',
        'ALWAYS: un hábito, así que present simple. I DRINK (sin -S con I).',
        'EVERY DAY: una rutina, así que present simple. My mum = she → COOKS.',
        'LISTEN!: lo oyes ahora, así que IS CRYING.',
        'AT THE MOMENT: está pasando ahora, así que ARE STUDYING (we → ARE).',
        'USUALLY: un hábito, así que present simple. He → PLAYS.',
        'RIGHT NOW: está pasando en este momento. They → ARE WATCHING.',
        'Que le guste el chocolate es algo general, no algo que pasa ahora: IS LIKING no funciona aquí. She → LIKES.',
        'LOOK!: lo ves ahora, así que IS RUNNING (run → runNing).',
        'EVERY DAY: una rutina. I → GO.',
    ],
}

T = {
    'en': dict(
        coverTitle='Present Simple <br><em>or Continuous?</em>',
        coverSub='Supereasy: every day or right now? Ten sentences, the signal words that decide them, and a few of your own.',
        chipLevel='A1', chipFocus='I drink · I’m drinking', chipCount='18 slides',
        eW='Warm-up', eT='Let’s talk', eR='The rule', e1='Every day or right now?', e2='Every day or right now?',
        e3='Signal words', tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the right form',
        rT='Every day, or right now?',
        rS1='Habits and routines: every day, always, usually.', rS2='He / she / it + -S: she COOKS.',
        rC1='Happening now: now, right now, at the moment, Look!, Listen!', rC2='AM / IS / ARE + verb-ING.',
        sortT='Sort the signal words', sortHint='Click a word, then the box it belongs in.',
        sortWhy='Habits and routines take the present simple; what is happening now takes the present continuous.',
        binA='Present simple', binB='Present continuous',
        gapT='Write the verb', gHint='Present simple or present continuous? Use the verb in brackets.',
        gw1='SHH!: they are asleep now → ARE SLEEPING.',
        gw2='A job is a general fact, not just now: he → WORKS.',
        gw3='RIGHT NOW → present continuous. The negative: AM NOT WATCHING.',
        actTitle='My day, right now', actUse='Use at least three:',
        actSpeakBrief='In pairs. Talk about your days and about now.',
        actSpeak1='Tell your partner three things you do every day.',
        actSpeak2='Look around the room. Say three things people are doing right now.',
        actSpeak3='Ask your partner: What do you usually do on Sundays? What are you doing this week?',
        actWriteKind='Writing',
        actWriteBrief='Write a short message to a friend (50–70 words): what you usually do on Saturdays, and what you are doing right now.',
        actPlaceholder='Hi Mia! On Saturdays I usually …',
    ),
    'de': dict(
        coverTitle='Present Simple <br><em>or Continuous?</em>',
        coverSub='Supereinfach: jeden Tag oder genau jetzt? Zehn Sätze, die Signalwörter, die entscheiden, und ein paar eigene Sätze.',
        chipLevel='A1', chipFocus='I drink · I’m drinking', chipCount='18 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Die Regel', e1='Jeden Tag oder genau jetzt?', e2='Jeden Tag oder genau jetzt?',
        e3='Signalwörter', tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle die richtige Form',
        rT='Jeden Tag oder genau jetzt?',
        rS1='Gewohnheiten und Routinen: every day, always, usually.', rS2='He / she / it + -S: she COOKS.',
        rC1='Passiert gerade: now, right now, at the moment, Look!, Listen!', rC2='AM / IS / ARE + Verb-ING.',
        sortT='Sortiere die Signalwörter', sortHint='Klicke ein Wort an, dann den passenden Kasten.',
        sortWhy='Gewohnheiten und Routinen nehmen Present Simple; was gerade passiert, nimmt Present Continuous.',
        binA='Present Simple', binB='Present Continuous',
        gapT='Schreib das Verb', gHint='Present Simple oder Present Continuous? Verwende das Verb in Klammern.',
        gw1='SHH!: Sie schlafen jetzt → ARE SLEEPING.',
        gw2='Ein Beruf ist eine allgemeine Tatsache, nicht nur jetzt: he → WORKS.',
        gw3='RIGHT NOW → Present Continuous. Die Verneinung: AM NOT WATCHING.',
        actTitle='Mein Tag, genau jetzt', actUse='Verwende mindestens drei:',
        actSpeakBrief='Zu zweit. Sprecht über euren Alltag und über jetzt.',
        actSpeak1='Erzähl deinem Partner drei Dinge, die du jeden Tag machst.',
        actSpeak2='Schau dich im Raum um. Sag drei Dinge, die Leute gerade machen.',
        actSpeak3='Frag deinen Partner: What do you usually do on Sundays? What are you doing this week?',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib einer Freundin eine kurze Nachricht (50–70 Wörter): was du samstags normalerweise machst und was du gerade machst.',
        actPlaceholder='Hi Mia! On Saturdays I usually …',
    ),
    'es': dict(
        coverTitle='Present Simple <br><em>or Continuous?</em>',
        coverSub='Superfácil: ¿todos los días o ahora mismo? Diez oraciones, las palabras clave que deciden y algunas oraciones tuyas.',
        chipLevel='A1', chipFocus='I drink · I’m drinking', chipCount='18 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='La regla', e1='¿Todos los días o ahora mismo?', e2='¿Todos los días o ahora mismo?',
        e3='Palabras clave', tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige la forma correcta',
        rT='¿Todos los días o ahora mismo?',
        rS1='Hábitos y rutinas: every day, always, usually.', rS2='He / she / it + -S: she COOKS.',
        rC1='Pasa ahora: now, right now, at the moment, Look!, Listen!', rC2='AM / IS / ARE + verbo-ING.',
        sortT='Clasifica las palabras clave', sortHint='Haz clic en una palabra y después en su caja.',
        sortWhy='Los hábitos y las rutinas llevan present simple; lo que pasa ahora lleva present continuous.',
        binA='Present simple', binB='Present continuous',
        gapT='Escribe el verbo', gHint='¿Present simple o present continuous? Usa el verbo entre paréntesis.',
        gw1='SHH!: están dormidos ahora → ARE SLEEPING.',
        gw2='Un trabajo es un hecho general, no solo ahora: he → WORKS.',
        gw3='RIGHT NOW → present continuous. La negación: AM NOT WATCHING.',
        actTitle='Mi día, ahora mismo', actUse='Usa al menos tres:',
        actSpeakBrief='En parejas. Hablen de su día a día y de ahora.',
        actSpeak1='Cuéntale a tu compañero tres cosas que haces todos los días.',
        actSpeak2='Mira a tu alrededor. Di tres cosas que la gente está haciendo ahora mismo.',
        actSpeak3='Pregúntale a tu compañero: What do you usually do on Sundays? What are you doing this week?',
        actWriteKind='Escritura',
        actWriteBrief='Escribe un mensaje corto a una amiga (50–70 palabras): qué haces normalmente los sábados y qué estás haciendo ahora mismo.',
        actPlaceholder='Hi Mia! On Saturdays I usually …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w

GLOSS = {
    'de': dict(
        g1='Schau! Sie schreibt gerade einen Brief.', g2='Ich trinke morgens immer Kaffee.',
        g3='Meine Mutter kocht jeden Tag das Abendessen.', g4='Hör mal! Das Baby weint im Zimmer nebenan.',
        g5='Wir lernen gerade Englisch.', g6='Er spielt samstags normalerweise Fußball.',
        g7='Gerade jetzt schauen sie zusammen einen Film.', g8='Sie mag Schokolade sehr gern.',
        g9='Schau! Der Hund rennt im Garten.', g10='Ich gehe jeden Tag zur Schule.',
    ),
    'es': dict(
        g1='¡Mira! Está escribiendo una carta ahora mismo.', g2='Siempre tomo café por la mañana.',
        g3='Mi madre cocina la cena todos los días.', g4='¡Escucha! El bebé está llorando en la habitación de al lado.',
        g5='Estamos estudiando inglés en este momento.', g6='Normalmente juega al fútbol los sábados.',
        g7='Ahora mismo están viendo una película juntos.', g8='Le gusta mucho el chocolate.',
        g9='¡Mira! El perro está corriendo en el jardín.', g10='Voy a la escuela todos los días.',
    ),
}

E = T['en']
SORT = D.sort_slide(
    [E['binA'], E['binB']],
    [('always', 0), ('every day', 0), ('usually', 0), ('on Saturdays', 0), ('never', 0),
     ('now', 1), ('right now', 1), ('at the moment', 1), ('Look!', 1), ('Listen!', 1)],
    'e3', E['e3'], 'sortT', E['sortT'], 'sortHint', E['sortHint'], 'sortWhy',
    bin_keys=['binA', 'binB'])
SPEC['flow'] = [st if st != ('raw', None) else ('raw', SORT) for st in SPEC['flow']]

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T, GLOSS)
