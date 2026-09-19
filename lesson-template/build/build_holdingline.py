# -*- coding: utf-8 -*-
"""Holding the Line (C1) - answering an unreasonable manager.

Written from a live class: a junior who completed the junior tasks he was
assigned, inside the time allowance for them, and who is now being told his
"time efficiency is concerning" and handed lead work that was never formally
allocated to him. The summary of that class named three stages, and they are
this deck's three stages: explain the role and its limits, answer the
criticism, ask for the reassignment before taking the work.

THE LANGUAGE SPINE, because a phrase list is not a lesson:

  * **the agentless passive** - "The lead tasks WERE NOT allocated to me"
    against "You never gave me the lead tasks". Same fact; one of them is a
    record and the other is a charge, and only one survives being forwarded.
  * **ONCE / AS SOON AS + PRESENT SIMPLE** - "I CAN pick that up ONCE
    ownership IS reassigned." A refusal with a condition attached is not a
    refusal, and the tense is the thing learners get wrong (*once it will be).
  * the vocabulary of allocation: remit, scope, ownership, accountability,
    authority, sign-off, allocate, capacity.

BUILT ON THE EDITORIAL STYLE (HOUSE-STYLE §15), which is what Innes asked
for. Three consequences a later session should not undo:

  * `data-bg` is the FRAMED PICTURE here, not a background wash, and a slide
    with no `data-bg` shows no picture and takes the full width. The four
    wide slides below (the case, the eight-term match, the three moves, the
    fact/verdict sort) omit it deliberately: they need the 1280px.
  * a slide WITH a picture has 58% of the width, so two columns maximum.
    Every teach slide that carries art has two cards; the three-card ones
    carry none.
  * the palette is NOT derived from the hero. `extract-palette.py` is not run
    for this deck; `tools/check-editorial-palette.py` is what guards it.

ARTWORK. The eight plates arrived 2026-09-19, to the brief in
`docs/ARTWORK-holding-the-line.md` - except for the aspect, which came back
16:9 on all eleven candidates rather than 7:6. The hero wanted 16:9 anyway
(the cover is the one full-bleed slide); the other seven were cut to the
frame's 7:6 before prep, at a chosen centre rather than the blind middle,
because the middle bisects the door and the clock. The crop centres are in
docs/HANDOFF.md. Sources are in `incoming/` and are gitignored, so a re-cut
means going back to Midjourney.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-holding-the-line-c1.html'
F = 'HoldingTheLine'

# ── the art slots ──────────────────────────────────────────────────────
# The commissioned set, dropped 2026-09-19. One line per slot; nothing else
# in this file knows a filename.
ART = {
    'hero':     'hero.jpg',      # cover, and the only 16:9 plate
    'remit':    'remit.jpg',     # scope, and what sits outside it
    'ledger':   'ledger.jpg',    # the dated record of what was done
    'facts':    'facts.jpg',     # time, measured rather than asserted
    'door':     'door.jpg',      # the room this conversation belongs in
    'handover': 'handover.jpg',  # ownership changing hands
    'keys':     'keys.jpg',      # access
    'talk':     'talk.jpg',      # two chairs, the same size
}


def art(slide, side=None, shape=None):
    """Tag a slide with how the editorial style places its picture.

    Inert under the default style - nothing outside the editorial block
    reads either attribute - so this deck could be rebuilt either way.
    """
    extra = ''
    if side == 'left':
        extra += ' data-art-side="left"'
    if shape == 'arch':
        extra += ' data-art="arch"'
    return slide.replace('<section class="slide"',
                         '<section class="slide"' + extra, 1)


def assert_key_is_middle(mc, label='MC'):
    """check-lesson.js fails a key that is conspicuously the longest option
    AND one that is conspicuously the shortest. deck.assert_no_key_is_longest
    only guards the first, and this deck's options are whole sentences, where
    the short case is the easy one to walk into: a clean professional line is
    naturally shorter than the two clumsy ones around it.

    Same thresholds as the checker, so a pass here is a pass there.
    """
    D.assert_no_key_is_longest(mc, label)
    for n, q in enumerate(mc, 1):
        L = [len(re.sub(r'<[^>]+>', '', o)
                 .replace('&ldquo;', '"').replace('&rdquo;', '"')
                 .replace('&rsquo;', "'").replace('&mdash;', '-'))
             for o in q['options']]
        k = L[q['correct']]
        lo = min(x for i, x in enumerate(L) if i != q['correct'])
        assert not (lo > k * 1.50 and lo - k >= 10), (
            '%s Q%d: the key is conspicuously the shortest option (%d vs %d). '
            'Tighten the distractors - never pad the key.' % (label, n, k, lo))


def deal(mc, slots):
    """Rotate each item's options so the key lands on the slot named.

    check-lesson.js's KEYS gate reads the SOURCE order, and every item here
    was authored with the true answer second, because that is how a sensible
    reply reads when you are writing a wrong one either side of it. Six of
    the seven keys came out on B.

    Rotating is safer than re-typing the options in a new order: `ex` has to
    move with them, and a hand-reorder that forgets one line hangs the wrong
    explanation on the wrong distractor, which is invisible until a learner
    picks it. Idempotent - the slot is absolute, so a second call is a no-op.
    """
    assert len(mc) == len(slots), 'deal: one slot per question'
    for q, t in zip(mc, slots):
        n = len(q['options'])
        k = (t - q['correct']) % n
        rot = lambda L: L[-k:] + L[:-k] if k else L
        q['options'] = rot(q['options'])
        q['ex'] = rot(q['ex'])
        q['correct'] = t


# ── stage one: the role, and what was never in it ──────────────────────
CASE = [
    ('caseH1', 'What you did', 'case1',
     'You completed the three junior tasks you were assigned, inside the time '
     'allowance set for them.',
     'caseN1', 'Not in dispute. Say it once, with the dates.'),
    ('caseH2', 'What was never issued', 'case2',
     'The lead tasks were not allocated to you, and no authority, sign-off or '
     'system access came with them.',
     'caseN2', 'A task you were never given is not a task you failed.'),
    ('caseH3', 'What is being said', 'case3',
     'Your time efficiency is called concerning, and a fourth task arrives that '
     'nobody has put in writing.',
     'caseN3', 'Two separate claims. Answer them separately.'),
]

PASSIVE = [
    (None, 'FORM &middot; WAS / WERE + PAST PARTICIPLE', None,
     '&ldquo;The lead tasks WERE NOT allocated to me.&rdquo; &mdash; '
     '&ldquo;Sign-off WAS NEVER given.&rdquo;',
     'passN1', 'No agent. Nobody in the room is named.'),
    ('passH2', 'Why it is the safer sentence', 'pass2',
     '&ldquo;You never gave me authority&rdquo; is a charge against your manager. '
     'The passive states the same fact and charges nobody.',
     'passN2', 'A fact survives being forwarded to him. An accusation does not.'),
]

TERMS_OWN = [
    ('remit', 'The area of work your role answers for'),
    ('scope', 'The agreed limits of one task or project'),
    ('ownership', 'Being the person the work belongs to'),
    ('accountability', 'Being answerable for the result'),
]

TERMS_DO = [
    ('authority', 'The right to decide or approve'),
    ('sign-off', 'The formal approval that finishes the work'),
    ('allocate', 'To give a task to one named person'),
    ('capacity', 'The hours you have left to give'),
]

TERM_GLOSS = {
    'de': {
        'remit': 'Der Aufgabenbereich, f&uuml;r den Ihre Rolle zust&auml;ndig ist',
        'scope': 'Der vereinbarte Umfang einer Aufgabe oder eines Projekts',
        'ownership': 'Die Person sein, der die Arbeit geh&ouml;rt',
        'accountability': 'Für das Ergebnis geradestehen',
        'authority': 'Das Recht zu entscheiden oder freizugeben',
        'sign-off': 'Die formale Freigabe, die eine Arbeit abschlie&szlig;t',
        'allocate': 'Eine Aufgabe einer namentlich genannten Person zuweisen',
        'capacity': 'Die Arbeitsstunden, die Ihnen noch bleiben',
    },
    'ru': {
        'remit': 'Область работы, за которую отвечает ваша должность',
        'scope': 'Согласованные границы одной задачи или проекта',
        'ownership': 'Быть тем, кому принадлежит работа',
        'accountability': 'Отвечать за результат',
        'authority': 'Право решать или утверждать',
        'sign-off': 'Формальное утверждение, завершающее работу',
        'allocate': 'Поручить задачу конкретному человеку',
        'capacity': 'Часы, которые у вас ещё остались',
    },
    'es': {
        'remit': 'El &aacute;mbito de trabajo del que responde tu puesto',
        'scope': 'Los l&iacute;mites acordados de una tarea o un proyecto',
        'ownership': 'Ser la persona a quien pertenece el trabajo',
        'accountability': 'Responder del resultado',
        'authority': 'El derecho a decidir o aprobar algo',
        'sign-off': 'La aprobaci&oacute;n formal que cierra un trabajo',
        'allocate': 'Asignar una tarea a una persona concreta',
        'capacity': 'Las horas de trabajo que te quedan disponibles',
    },
}

LIMIT_BANK = ['allocated', 'authority', 'capacity', 'remit', 'scope']
LIMIT_ROWS_A = [
    ('All three tasks were ______ to me on 4 March.', ['allocated'],
     'ALLOCATE is the verb a system uses. It puts a named person on a task.'),
    ('The lead deliverable falls outside my ______.', ['remit'],
     'Your REMIT is the area your role answers for. A SCOPE belongs to a task, '
     'not to a person.'),
    ('I do not have the ______ to approve that.', ['authority'],
     'AUTHORITY is the right to decide. ACCOUNTABILITY is being answerable '
     'afterwards, which is not the same thing.'),
]

LIMIT_ROWS_B = [
    ('That sits outside the ______ we agreed at the kick-off.', ['scope'],
     'SCOPE + of + a task. It is what was agreed, so it can be quoted back.'),
    ('I do not have the ______ to take that on without dropping something.',
     ['capacity'],
     'CAPACITY is hours. Say what would have to drop, or the answer sounds '
     'like an excuse.'),
]

LIMIT = [
    dict(stem='Which reply states the record without putting it on a person?',
         options=[
             'You never gave me that task, and you never gave me the access for it.',
             'That task was never allocated to me, and I have no access to it.',
             'Sorry &mdash; I will stay late tonight and see how far I get with it.',
         ],
         correct=1,
         why='The passive names the decision, not the person: WAS / WERE + '
             'PAST PARTICIPLE.',
         ex=['Same fact, aimed at a person. &ldquo;You never&rdquo; turns a '
             'record into a charge, and he will answer the charge.',
             None,
             'You have just accepted a task nobody gave you. By tomorrow the '
             'record says it was always yours.']),
    dict(stem='Which reply answers a request that never officially arrived?',
         options=[
             'I did not see any ticket for that, so I assumed it was not mine.',
             'I have not had that request through the system. Could you send it?',
             'Nothing came to me about that, and honestly nobody tells me anything.',
         ],
         correct=1,
         why='Report what did not arrive, then name the route it should arrive '
             'by. One sentence of fact, one of process.',
         ex=['&ldquo;I assumed&rdquo; makes the gap your judgement call, and a '
             'judgement call is something you can be wrong about.',
             None,
             'The second half is a complaint about everyone. It answers nothing '
             'and gives him something easier to argue with.']),
    dict(stem='Which reply keeps the finished work and the missing work apart?',
         options=[
             'Everything I was actually given is finished, and the rest was '
             'never mine to begin with.',
             'The three tasks I was allocated are done. The lead work was not '
             'allocated to anyone.',
             'I have done everything that anybody could reasonably expect from '
             'me in this role.',
         ],
         correct=1,
         why='Two clauses, two facts, both checkable. &ldquo;Everything I could '
             'reasonably be expected to do&rdquo; is a verdict on yourself.',
         ex=['&ldquo;Actually&rdquo; is doing the arguing, and &ldquo;never mine '
             'to begin with&rdquo; is a claim with no record behind it.',
             None,
             '&ldquo;Reasonably expect&rdquo; invites the obvious reply: who '
             'decides what is reasonable, and on what evidence?']),
]

# ── stage two: answering the criticism ─────────────────────────────────
MOVES = [
    ('movesH1', 'Ask for the instance', 'moves1',
     '&ldquo;Could you give me a specific example?&rdquo; A judgement with no '
     'instance behind it cannot be answered &mdash; and does not have to be '
     'accepted.',
     'movesN1', 'You are not arguing. You are asking what the claim is about.'),
    ('movesH2', 'Stick to the facts', 'moves2',
     '&ldquo;Can we stick to the facts, please?&rdquo; Then give the dates, the '
     'tickets, the hours &mdash; things a third person could check.',
     'movesN2', 'Say it once. Twice and it is a slogan.'),
    ('movesH3', 'Move the conversation', 'moves3',
     '&ldquo;I would like to discuss the limits of my role at a convenient '
     'time.&rdquo; Ask for a length and a purpose.',
     'movesN3', 'A corridor is not a room. Fifteen minutes and a door.'),
]

SORT_BINS = ['A fact anyone could check', 'A verdict about a person']
SORT_ITEMS = [
    ('Three tasks were allocated to me on 4 March.', 0),
    ('You are setting me up to fail.', 1),
    ('I do not have access to that system.', 0),
    ('You are being completely unreasonable.', 1),
    ('The lead task has never appeared in my queue.', 0),
    ('Nobody here has any respect for my time.', 1),
    ('All three were finished inside the eight hours allowed.', 0),
    ('You clearly do not trust me with anything.', 1),
]

CRIT = [
    dict(stem='Which reply asks for evidence without conceding the point?',
         options=[
             'Could you give me a specific example, with the date?',
             'I am doing my best with what I was given.',
             'That is not fair. I finished everything you asked me for.',
         ],
         correct=0,
         why='A vague judgement becomes a conversation the moment you ask what '
             'it is measured against.',
         ex=[None,
             '&ldquo;Doing my best&rdquo; accepts the judgement and argues about '
             'effort instead. Nothing in it can be checked.',
             '&ldquo;Not fair&rdquo; is a verdict, and it invites a second one '
             'straight back.']),
    dict(stem='Which reply moves it somewhere you can actually answer it?',
         options=[
             'Can we talk about this later, please? Not right now.',
             'I would like to go through this properly. Could we book fifteen '
             'minutes?',
             'I would rather not discuss my performance while the whole team is '
             'listening.',
         ],
         correct=1,
         why='Name a length and a purpose. An ask with a number attached is hard '
             'to refuse and easy to diarise.',
         ex=['It asks for less and gives no reason, so the easiest answer is '
             '&ldquo;no, now&rdquo;.',
             None,
             'True &mdash; and it makes the audience the subject. Ask for the '
             'meeting, not for privacy.']),
    dict(stem='Which reply answers &ldquo;your time efficiency is concerning&rdquo; '
              'with a measurement?',
         options=[
             'I work as fast as anybody else on this team does, honestly.',
             'The three tasks took eleven hours against a twelve-hour allowance.',
             'Concerning compared with what, exactly? Nobody has ever told me.',
         ],
         correct=1,
         why='Hours against an allowance is a number he has to argue with. '
             'Everything else is one opinion against another.',
         ex=['A comparison with colleagues invites a comparison with '
             'colleagues, and you will not win that one in public.',
             None,
             'The question is the right one; &ldquo;nobody has ever told '
             'me&rdquo; turns it into a grievance.']),
]

ORDER_ITEMS = ['I would like to go through', 'what was allocated to me',
               'and when,', 'before we discuss', 'efficiency.']

# ── stage three: the boundary, and the ask ─────────────────────────────
COND = [
    (None, 'FORM &middot; CAN + VERB &hellip; ONCE + PRESENT SIMPLE', None,
     '&ldquo;I CAN pick that up ONCE ownership IS reassigned.&rdquo; '
     'Never ONCE ownership WILL BE reassigned.',
     'condN1', 'ONCE, WHEN and AS SOON AS take the present for future time.'),
    ('condH2', 'Name both conditions', 'cond2',
     'Ownership, and access. Work with neither is work you can be blamed for '
     'and cannot actually do.',
     'condN2', '&ldquo;Formally allocated&rdquo; is what makes it a record.'),
]

ASK_BANK = ['access', 'formally', 'once', 'ownership', 'writing']
ASK_ROWS_A = [
    ('I can take the lead tasks on ______ ownership is reassigned to me.',
     ['once'],
     'ONCE + PRESENT SIMPLE. The condition is stated, so this is not a refusal.'),
    ('I would need ______ to the deployment system before I could start.',
     ['access'],
     'ACCESS + to. Name the system, or the sentence sounds like reluctance.'),
]

ASK_ROWS_B = [
    ('Happy to help, as soon as it is ______ allocated.', ['formally'],
     'FORMALLY is the word that separates a corridor instruction from a record.'),
    ('Could you confirm the change of ______ in ______?', ['ownership', 'writing'],
     'IN WRITING. Said aloud it is a favour; written down it is the allocation.'),
]

CORRIDOR = [
    dict(stem='Which reply keeps the task off your record until it is real?',
         options=[
             'Fine, send it over and I will see what I can do with it.',
             'I can take it on once it is allocated to me in the system.',
             'No, that is not in my job description and I am not going to do it.',
         ],
         correct=1,
         why='ONCE + PRESENT SIMPLE turns a refusal into a condition. You are '
             'not saying no; you are saying what has to be true first.',
         ex=['&ldquo;Send it over&rdquo; is acceptance. The system will show '
             'you owning it by lunchtime.',
             None,
             'True, and final. A refusal with no route back leaves him one '
             'move, which is to escalate it above you.']),
]

FUNCTIONS = [
    ('Could you give me a specific example?',
     'Turns a judgement into something answerable'),
    ('Can we stick to the facts, please?',
     'Stops the conversation moving to character'),
    ('That was never allocated to me.',
     'States the record without naming anyone'),
    ('I can take it on once ownership is reassigned.',
     'Accepts the work and names the condition'),
    ('Could you confirm that in writing?',
     'Turns an instruction into a record'),
    ('I would like to discuss this at a convenient time.',
     'Moves it to a room with a door'),
]

FUNC_GLOSS = {
    'de': {
        'Could you give me a specific example?':
            'Macht aus einem Urteil etwas Beantwortbares',
        'Can we stick to the facts, please?':
            'Verhindert, dass das Gespräch auf den Charakter kippt',
        'That was never allocated to me.':
            'Nennt den Sachstand, ohne jemanden zu benennen',
        'I can take it on once ownership is reassigned.':
            'Nimmt die Arbeit an und nennt die Bedingung',
        'Could you confirm that in writing?':
            'Macht aus einer Anweisung einen Nachweis',
        'I would like to discuss this at a convenient time.':
            'Verlegt es in einen Raum mit einer Tür',
    },
    'ru': {
        'Could you give me a specific example?':
            'Превращает оценку в то, на что можно ответить',
        'Can we stick to the facts, please?':
            'Не даёт разговору перейти на личности',
        'That was never allocated to me.':
            'Сообщает факт, не называя никого',
        'I can take it on once ownership is reassigned.':
            'Принимает работу и называет условие',
        'Could you confirm that in writing?':
            'Превращает указание в запись',
        'I would like to discuss this at a convenient time.':
            'Переносит разговор в комнату с дверью',
    },
    'es': {
        'Could you give me a specific example?':
            'Convierte un juicio en algo que se puede responder',
        'Can we stick to the facts, please?':
            'Impide que la conversación pase al terreno personal',
        'That was never allocated to me.':
            'Expone el registro sin señalar a nadie',
        'I can take it on once ownership is reassigned.':
            'Acepta el trabajo y nombra la condición',
        'Could you confirm that in writing?':
            'Convierte una instrucción en un registro',
        'I would like to discuss this at a convenient time.':
            'Lo traslada a una sala con puerta',
    },
}

CHIPS = ['remit', 'scope', 'ownership', 'accountability', 'authority',
         'sign-off', 'allocated', 'capacity', 'access', 'in writing',
         'a specific example', 'once ownership is reassigned']


def build(style='editorial', out=None):
    deal(LIMIT, [0, 1, 2])
    deal(CRIT, [0, 2, 1])
    deal(CORRIDOR, [2])
    assert_key_is_middle(LIMIT, 'LIMIT')
    assert_key_is_middle(CRIT, 'CRIT')
    assert_key_is_middle(CORRIDOR, 'CORRIDOR')
    # The bank is shown whole on both screens of a split round and every word
    # is used exactly once across the pair, so the gate has to see the pair.
    D.assert_bank_is_not_a_key(
        LIMIT_BANK, [a for _, ans, _ in LIMIT_ROWS_A + LIMIT_ROWS_B for a in ans])
    D.assert_bank_is_not_a_key(
        ASK_BANK, [a for _, ans, _ in ASK_ROWS_A + ASK_ROWS_B for a in ans])

    logo = D.logo_from(TPL)
    A = lambda k: ART[k]

    slides = (
        D.cover(logo, 'Holding the <em>Line</em>',
                'What to say when work nobody gave you becomes work you are '
                'being blamed for',
                [('Level', 'C1 &middot; Workplace pressure'),
                 ('Focus', 'Scope, facts and the ask'),
                 ('Count', 'COUNT slides')])

        # ── stage one ──────────────────────────────────────────────────
        # No picture: three cards need the full 1280px under this style.
        + D.teach('caseEyebrow', 'The situation', 'caseTitle',
                  'Three tasks given, one never allocated', CASE)

        + art(D.teach('passEyebrow', 'The first move', 'passTitle',
                      'Name the decision, not the person', PASSIVE,
                      cols='1fr 1fr', folder=F, bg=A('remit')),
              shape='arch')

        + D.match(TERMS_OWN, 'termsEyebrow', 'The vocabulary', 'termsTitle',
                  'The words for what you own', 'termsHint',
                  'Click a term, then the line that defines it.',
                  'REMIT is a person&rsquo;s area; SCOPE is a task&rsquo;s '
                  'limits. OWNERSHIP is holding the work; ACCOUNTABILITY is '
                  'answering for it afterwards.', glosses=TERM_GLOSS)

        + D.match(TERMS_DO, 'termsEyebrow', 'The vocabulary', 'termsTitle2',
                  'The words for what you can do', 'termsHint',
                  'Click a term, then the line that defines it.',
                  'AUTHORITY is the right to decide; SIGN-OFF is the approval '
                  'itself. ALLOCATE puts a named person on a task.',
                  glosses=TERM_GLOSS)

        # Split, not shrunk (§6). Five rows in the 58% column the framed
        # picture leaves ran 129px over; three and two both fit, and the
        # round keeps its picture.
        + art(D.gap(1, 2, LIMIT_ROWS_A, LIMIT_BANK, 'limitEyebrow',
                    'Say the limit', 'limitTitle', 'Complete the line',
                    folder=F, bg=A('ledger'), hint_key='limitHint',
                    hint='One word per gap; each is used once across both '
                         'screens.'),
              side='left')

        + art(D.gap(2, 2, LIMIT_ROWS_B, LIMIT_BANK, 'limitEyebrow',
                    'Say the limit', 'limitTitle', 'Complete the line',
                    folder=F, bg=A('remit'), hint_key='limitHint',
                    hint='One word per gap; each is used once across both '
                         'screens.'))

        + "".join(art(D.mc(i + 1, len(LIMIT), q, 'roleEyebrow', 'Your remit',
                           'roleTitle', 'Which sentence would you send?',
                           folder=F, explains=q['ex'], ctx_key='roleCtx%d' % (i + 1),
                           ctx=['Your manager, in front of the team: &ldquo;Why '
                                'isn&rsquo;t the lead deliverable ready?&rdquo;',
                                'He refers to a task you have never seen in the '
                                'system.',
                                'He asks you to account for the week.'][i],
                           bg=A(['remit', 'ledger', 'door'][i])),
                      side='left' if i % 2 else None,
                      shape='arch' if i == 2 else None)
                  for i, q in enumerate(LIMIT))

        # ── stage two ──────────────────────────────────────────────────
        + D.teach('movesEyebrow', 'Under criticism', 'movesTitle',
                  'Three moves that lower the temperature', MOVES)

        + D.sort_slide(SORT_BINS, SORT_ITEMS, 'sortEyebrow', 'Before you say it',
                       'sortTitle', 'Fact, or verdict?', 'sortHint',
                       'Click a line, then the box it belongs in.',
                       'A fact survives being repeated to somebody else. A '
                       'verdict invites a second verdict.',
                       bin_keys=['sortBin1', 'sortBin2'])

        + "".join(art(D.mc(i + 1, len(CRIT), q, 'critEyebrow', 'The criticism',
                           'critTitle', 'Answer it without agreeing to it',
                           folder=F, explains=q['ex'], ctx_key='critCtx%d' % (i + 1),
                           ctx=['&ldquo;Your time efficiency is concerning.&rdquo;',
                                'The same conversation, still at your desk, still '
                                'audible.',
                                'He repeats the word &ldquo;concerning&rdquo;.'][i],
                           bg=A(['facts', 'door', 'facts'][i])),
                      side='left' if i % 2 else None,
                      shape='arch' if i == 1 else None)
                  for i, q in enumerate(CRIT))

        + art(D.order(ORDER_ITEMS, 'ordEyebrow', 'Say it cleanly', 'ordTitle',
                      'Put the request in order', 'ordHint',
                      'Click the parts in order.',
                      'The dated record comes first. Once it is on the table, '
                      '&ldquo;concerning&rdquo; has to be measured against '
                      'something.', folder=F, bg=A('facts')),
              shape='arch')

        # ── stage three ────────────────────────────────────────────────
        + art(D.teach('condEyebrow', 'The boundary', 'condTitle',
                      'Yes &mdash; once two things happen', COND,
                      cols='1fr 1fr', folder=F, bg=A('handover')))

        + art(D.gap(1, 2, ASK_ROWS_A, ASK_BANK, 'askEyebrow', 'The ask',
                    'askTitle', 'Ask for the two things', folder=F,
                    bg=A('keys'), hint_key='askHint',
                    hint='One word per gap; each is used once across both '
                         'screens.'),
              side='left')

        + art(D.gap(2, 2, ASK_ROWS_B, ASK_BANK, 'askEyebrow', 'The ask',
                    'askTitle', 'Ask for the two things', folder=F,
                    bg=A('handover'), hint_key='askHint2',
                    hint='One word per gap &mdash; and the last line takes two.'))

        + art(D.mc(1, 1, CORRIDOR[0], 'corrEyebrow', 'The corridor',
                   'corrTitle', 'A fourth task, on the way to lunch',
                   folder=F, explains=CORRIDOR[0]['ex'], ctx_key='corrCtx',
                   ctx='He tells you about it walking past your desk, and keeps '
                       'walking.', bg=A('door')))

        + D.match(FUNCTIONS, 'funcEyebrow', 'The phrase bank', 'funcTitle',
                  'What each line actually does', 'funcHint',
                  'Click a line, then the job it does in the room.',
                  'Every one of these does something to the conversation. None '
                  'of them says anything about the other person.',
                  glosses=FUNC_GLOSS)

        + D.results(next_key='resNext', next_text='Now run the meeting &rarr;')

        + D.activate(
            'Now run the meeting', 'Use at least four:', CHIPS,
            'Speaking',
            'In pairs. Three minutes each, then swap roles and run it again.',
            ['You are the junior. Your manager opens with &ldquo;Your time '
             'efficiency is concerning.&rdquo; Answer without accepting it and '
             'without attacking him.',
             'Swap. This time the manager hands over a fourth task in the '
             'corridor. Get it allocated, or get it off your list.',
             'Same meeting, with HR in the room. What changes in how you say it '
             '&mdash; and what must not change?',
             'Argue the other side: when is a manager right to hand somebody work '
             'outside their remit?'],
            'Writing &middot; 180&ndash;220 words',
            'Write the email asking for your role to be clarified. Three dated '
            'facts, one concession, one specific ask, and nothing at all about '
            'anybody&rsquo;s character.',
            'Dear Ana, following this morning&rsquo;s conversation, I would like '
            'to set out what was allocated to me and when&hellip;',
            folder=F, bg=A('talk'))
    )

    import i18n_holdingline as I
    out_path = out or OUT
    palette = (D.editorial_palette('%s/%s' % (F, ART['hero']))
               if style == 'editorial' else None)
    assert palette, 'this deck is written for the editorial style'
    s = D.assemble(TPL, out_path, slides, palette,
                   'Holding the Line — Forbes English',
                   I, langs=('en', 'de', 'es', 'ru'), style=style)

    # The count chip is written once the deck knows how long it is. Counting
    # `<section class="slide` returns N+1 - the template keeps one of its own
    # that never ships - so count the ones that carry a data-type, which is
    # the set check-lesson.js reports in its header line.
    n = len(re.findall(r'<section class="slide[^>]*\bdata-type=', s))
    s = s.replace('COUNT slides', '%d slides' % n)
    s = s.replace('COUNT Folien', '%d Folien' % n)
    s = s.replace('COUNT diapositivas', '%d diapositivas' % n)
    # Russian counts the noun, not the digit: 21 слайд, 23 слайда, 25 слайдов.
    # The chip is generated, so the form has to be as well - a hard-coded
    # '%d слайдов' is wrong for two thirds of the numbers a deck can be.
    ten, hun = n % 10, n % 100
    ru = ('слайдов' if 11 <= hun <= 14 else
          'слайд' if ten == 1 else
          'слайда' if ten in (2, 3, 4) else 'слайдов')
    s = s.replace('COUNT слайдов', '%d %s' % (n, ru))
    open(out_path, 'w', encoding='utf-8', newline='').write(s)
    print('%s - %d slides (editorial)' % (out_path, n))


if __name__ == '__main__':
    build()
