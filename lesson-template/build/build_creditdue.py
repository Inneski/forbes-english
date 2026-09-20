# -*- coding: utf-8 -*-
"""Credit Where It's Due (C1) - claiming your work without grandstanding.

The sibling of Holding the Line, and deliberately its mirror. That deck
teaches the agentless passive as a shield: "the lead tasks WERE NOT allocated
to me" states a fact and accuses nobody. This one teaches when the same
structure is the enemy - "the proposal WAS PUT TOGETHER over three weeks"
erases the person who put it together, and on this topic the person is the
point. Same grammar, opposite job, and knowing which is which is the C1 skill.

THE LANGUAGE SPINE:

  * **the cleft** - WHAT + clause + WAS/IS. "WHAT I proposed on Tuesday WAS a
    two-week pilot." A cleft front-loads the author and asks the room to
    remember a date; "that was my idea" front-loads the argument and asks the
    room to pick a winner. That difference is the whole lesson.
  * **active over passive for authorship**, and the contrast that makes it
    work: passives around the parts that were not yours make the two actives
    the two sentences anybody reads.
  * **quantifying** - a number replaces an opinion about a contribution.

The distractors run on one taxonomy, so every wrong answer is wrong for a
reason a teacher can name rather than for taste: TOO SHARP (it accuses),
TOO SOFT (it signs the work away), TOO LOUD (it grandstands, or stops the
meeting to litigate). See HOUSE-STYLE and the synonym-ban note - a pragmatics
item is only defensible when the failure has a name.

SOURCES. Innes supplied two trade articles on the subject. Nothing in them is
reproduced: the situations, the wording, the items and the tasks are written
here, and no publication, employer or product is named anywhere in the deck.

EDITORIAL STYLE (HOUSE-STYLE §15), like its sibling. `data-bg` is the framed
picture, a slide without one takes the full width, a slide with one has two
columns at most, and the palette is fixed rather than derived.

ARTWORK. The commissioned set landed 2026-09-20, to the brief in
`docs/ARTWORK-credit-where-its-due.md`, and 16:9 again rather than the 7:6
the frame wants - twice now, so it is the Midjourney default rather than a
slip, and the brief has been rewritten to ask for what that pipeline actually
produces. The hero needed no crop; the other six were cut to 7:6 here at a
chosen centre, and the crop centres are in docs/HANDOFF.md.

One slot changed name. `nameplate` came back as a hand holding nothing and
was unusable; the second hero candidate - the sheet of paper lying on the
table - took its place and the slot is `paper`, which is what the two screens
using it are about anyway.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-credit-where-its-due-c1.html'
F = 'CreditWhereDue'

ART = {
    'hero':      'hero.jpg',       # cover, the only 16:9 plate
    'room':      'room.jpg',       # the meeting, and who holds the floor
    'trail':     'trail.jpg',      # the dated record
    'tally':     'tally.jpg',      # the number that ends the argument
    'paper':     'paper.jpg',      # the sheet on the table: the record
    'folder':    'folder.jpg',     # the timestamp you can hand round
    'spotlight': 'spotlight.jpg',  # the moment, and who is standing in it
    'cups':      'cups.jpg',       # the check-in
}


def art(slide, side=None, shape=None):
    extra = (' data-art-side="left"' if side == 'left' else '') \
          + (' data-art="arch"' if shape == 'arch' else '')
    return slide.replace('<section class="slide"',
                         '<section class="slide"' + extra, 1)


def assert_key_is_middle(mc, label='MC'):
    """Both halves of check-lesson.js's ANSWERS gate, at its own thresholds.

    deck.assert_no_key_is_longest guards the long case only, and on a deck
    whose options are whole spoken sentences the SHORT case is the easy one
    to walk into: the line a professional would actually say is tighter than
    the two clumsy ones written around it.
    """
    D.assert_no_key_is_longest(mc, label)
    for n, q in enumerate(mc, 1):
        L = [len(re.sub(r'<[^>]+>', '', o)
                 .replace('&ldquo;', '"').replace('&rdquo;', '"')
                 .replace('&rsquo;', "'").replace('&mdash;', '-')) for o in q['options']]
        k, lo = L[q['correct']], min(x for i, x in enumerate(L) if i != q['correct'])
        assert not (lo > k * 1.50 and lo - k >= 10), (
            '%s Q%d: the key is conspicuously the shortest (%d vs %d).' % (label, n, k, lo))


def deal(mc, slots):
    """Rotate each item so the key lands on the slot named, moving `ex` with
    it. Authoring puts the sensible answer second every time; the KEYS gate
    reads source order. Idempotent."""
    assert len(mc) == len(slots), 'deal: one slot per question'
    for q, t in zip(mc, slots):
        n = len(q['options'])
        k = (t - q['correct']) % n
        rot = lambda L: L[-k:] + L[:-k] if k else L
        q['options'], q['ex'], q['correct'] = rot(q['options']), rot(q['ex']), t


# ── stage one: what happened, and the sentence that fixes it ───────────
CASE = [
    ('caseH1', 'What you did', 'case1',
     'You proposed it in a Tuesday stand-up, in one sentence, and nobody '
     'picked it up.',
     'caseN1', 'One sentence in a stand-up is still a proposal.'),
    ('caseH2', 'What he did', 'case2',
     'On Thursday he put the same idea to the director, in more detail, as '
     'his own.',
     'caseN2', 'More detail is not more authorship.'),
    ('caseH3', 'What the room believes', 'case3',
     'The room believes what it heard last, from whoever had the floor '
     'longest.',
     'caseN3', 'You are not correcting a lie. You are correcting a record.'),
]

CLEFT = [
    (None, 'FORM &middot; WHAT + CLAUSE + WAS / IS', None,
     '&ldquo;WHAT I proposed on Tuesday WAS a two-week pilot.&rdquo; The '
     'clause names you before the idea arrives.',
     'cleftN1', 'Front-loads the author, not the argument.'),
    ('cleftH2', 'Why not just say it was yours', 'cleft2',
     '&ldquo;That was mine&rdquo; asks the room to judge two people. A cleft '
     'asks it to remember a date.',
     'cleftN2', 'You want the record corrected, not a winner declared.'),
]

TERMS_TAKE = [
    ('take credit for', 'Present the work as your own'),
    ('give credit to', 'Name the person the work came from'),
    ('acknowledge', 'Say in public that a contribution happened'),
    ('claim', 'State that something is yours, expecting it to be checked'),
]

TERMS_SHOW = [
    ('contribution', 'The part of the work that was yours'),
    ('instrumental', 'Without this person it would not have happened'),
    ('flag', 'Raise it early, so it is on the record'),
    ('quantify', 'Put a number on it so it cannot be argued with'),
]

TERM_GLOSS = {
    'de': {
        'take credit for': 'Die Arbeit als die eigene darstellen',
        'give credit to': 'Die Person nennen, von der die Arbeit stammt',
        'acknowledge': '&Ouml;ffentlich sagen, dass ein Beitrag geleistet wurde',
        'claim': 'Etwas f&uuml;r sich beanspruchen und Pr&uuml;fung aushalten',
        'contribution': 'Der Teil der Arbeit, der von Ihnen stammt',
        'instrumental': 'Ohne diese Person w&auml;re es nicht zustande gekommen',
        'flag': 'Fr&uuml;h ansprechen, damit es aktenkundig ist',
        'quantify': 'Mit einer Zahl belegen, die niemand bestreiten kann',
    },
    'es': {
        'take credit for': 'Presentar el trabajo como propio',
        'give credit to': 'Nombrar a la persona de quien viene el trabajo',
        'acknowledge': 'Decir en p&uacute;blico que hubo una aportaci&oacute;n',
        'claim': 'Afirmar que algo es tuyo, sabiendo que se comprobar&aacute;',
        'contribution': 'La parte del trabajo que fue tuya',
        'instrumental': 'Sin esta persona no habr&iacute;a salido adelante',
        'flag': 'Plantearlo pronto, para que quede registrado',
        'quantify': 'Ponerle un n&uacute;mero para que no se discuta',
    },
    'ru': {
        'take credit for': 'Представить работу как свою',
        'give credit to': 'Назвать того, от кого исходит работа',
        'acknowledge': 'Публично признать чей-то вклад',
        'claim': 'Заявить права, готовясь к проверке',
        'contribution': 'Та часть работы, которая была вашей',
        'instrumental': 'Без этого человека ничего бы не вышло',
        'flag': 'Поднять вопрос заранее, чтобы это зафиксировали',
        'quantify': 'Подкрепить цифрой, с которой не поспоришь',
    },
}

RECLAIM_BANK = ['building', 'credit', 'glad', 'proposed', 'record']
RECLAIM_A = [
    ('I am ______ we agree &mdash; when I ______ this on Tuesday, the plan was '
     'two weeks.', ['glad', 'proposed'],
     'GLAD first. The concession buys the sentence that follows it, and the '
     'date does the claiming.'),
    ('I am ______ on what I suggested in the stand-up.', ['building'],
     'BUILD ON + something already said. It reclaims the idea and hands the '
     'floor back in one move.'),
]
RECLAIM_B = [
    ('Could we get that on the ______ before the board pack goes out?',
     ['record'],
     'ON THE RECORD asks for the correction without naming the person who '
     'made it necessary.'),
    ('She gave me full ______ for the analysis in front of the director.',
     ['credit'],
     'GIVE somebody CREDIT FOR something. TAKE credit for it is the other '
     'half of the pair, and the other person.'),
]

ROOM = [
    dict(stem='Which reply corrects the record without putting him on trial?',
         options=[
             'Actually, that was my idea &mdash; I said it in Tuesday&rsquo;s stand-up.',
             'Glad that landed. What I proposed on Tuesday was a two-week pilot.',
             'Right, well, I suppose it does not really matter whose idea it was.',
         ],
         correct=1,
         why='WHAT + clause + WAS names the author and the date in one breath, '
             'and asks nobody in the room to lose.',
         ex=['TOO SHARP. &ldquo;Actually&rdquo; makes it a dispute between two '
             'people, and the room now has to pick one.',
             None,
             'TOO SOFT. It is yours, you have just signed it over, and nobody '
             'in that room will hand it back.']),
    dict(stem='Which reply keeps your name on it and the meeting moving?',
         options=[
             'I said that five minutes ago, more or less word for word, if '
             'anybody was listening.',
             'Yes &mdash; that is the point I made earlier. To build on it, the '
             'next step is a pilot.',
             'Sorry, I think you will find I raised exactly this point at the '
             'start of the meeting.',
         ],
         correct=1,
         why='Name it once, then move. A correction that stops the meeting '
             'costs you more than the credit is worth.',
         ex=['TOO SHARP, and the last clause is a complaint about the room '
             'rather than a claim on the idea.',
             None,
             'TOO LOUD. &ldquo;You will find&rdquo; turns a meeting into a '
             'hearing, and you will be the one who called it.']),
    dict(stem='Which reply gets you into the record without sounding wounded?',
         options=[
             'It would be nice if my name turned up in one of these team '
             'summaries every now and again.',
             'Thanks &mdash; the final proposal came together on my side, with '
             'Deepak&rsquo;s research behind it.',
             'No thanks needed on my side, I was only ever doing the job I was '
             'actually asked to do.',
         ],
         correct=1,
         why='Give one name, then take one. A sentence that thanks somebody is '
             'very hard to read as a complaint.',
         ex=['TOO SHARP, and it asks for a favour rather than stating a fact. '
             'The director now owes you something.',
             None,
             'TOO SOFT. &ldquo;Only doing what I was asked&rdquo; is a '
             'description of somebody with no contribution to name.']),
]

# ── stage two: the record, and the number ──────────────────────────────
MOVES = [
    ('movesH1', 'Reclaim in the room', 'moves1',
     'Same meeting, one sentence, with a date in it. Then hand the floor '
     'straight back.',
     'movesN1', 'Later is a complaint. Now is a correction.'),
    ('movesH2', 'Build the trail', 'moves2',
     'Put the idea in writing before the meeting, to more than one person. A '
     'dated line beats a good memory.',
     'movesN2', 'Not suspicious. Legible.'),
    ('movesH3', 'Give first, then take', 'moves3',
     'Name two people, then name what you did. Generous first makes the claim '
     'sound like a fact.',
     'movesN3', 'The order is the whole trick.'),
]

SORT_BINS = ['Puts your name on it', 'Signs it over to somebody else']
SORT_ITEMS = [
    ('What I proposed on Tuesday was a two-week pilot.', 0),
    ('The proposal was put together over three weeks.', 1),
    ('I ran the analysis and brought the numbers in.', 0),
    ('We all chipped in, really. It was a team thing.', 1),
    ('I drafted the section on risk.', 0),
    ('Somehow it all got finished in time.', 1),
    ('The deck was pulled together at the last minute.', 1),
    ('I cut four days off the review cycle.', 0),
]

ORDER_ITEMS = ['What I suggested', 'in the stand-up', 'was a two-week pilot,',
               'and the numbers behind it', 'are in my Monday email.']

VOICE = [
    (None, 'FORM &middot; I + PAST SIMPLE, not IT + WAS + DONE', None,
     '&ldquo;I DRAFTED the risk section.&rdquo; Not &ldquo;The risk section '
     'WAS DRAFTED.&rdquo;',
     'voiceN1', 'The passive hides the agent. Here the agent is the point.'),
    ('voiceH2', 'Where the passive still earns its place', 'voice2',
     'Use it for the parts that were not yours, so the parts that were stand '
     'out by contrast.',
     'voiceN2', 'Two actives in a paragraph of passives are the two anybody reads.'),
]

NUM_BANK = ['audits', 'cycle', 'hours', 'per cent', 'weeks']
# One line each in the 58% column the framed picture leaves. Three rows at
# two lines ran 61px over; §6 says split or shorten the line, never the type,
# and these sentences lost nothing that was being taught.
NUM_A = [
    ('I delivered it two ______ ahead of the agreed date.', ['weeks'],
     'A date beaten by a measured amount. &ldquo;Ahead of schedule&rdquo; is '
     'the same claim with nothing in it.'),
    ('I ran twenty-one ______ of the figures in six months.', ['audits'],
     'Countable and dull, which is exactly why it works. Nobody argues with '
     'twenty-one.'),
    ('Returns fell by nine ______ after the change.', ['per cent'],
     'PER CENT is two words in British English. The fall is the evidence; the '
     'change is the claim.'),
]
NUM_B = [
    ('I cut four days off the review ______.', ['cycle'],
     'A CYCLE is the repeating process. Cutting days off one is a permanent '
     'saving, not a one-off.'),
    ('That saved the team roughly eleven ______ a week.', ['hours'],
     'ROUGHLY is doing useful work: an estimate you can defend beats a precise '
     'figure you cannot.'),
]

EMAIL = [
    dict(stem='Which email puts your name on it without looking defensive?',
         options=[
             'Just so there is no confusion later, this idea is mine and I want that noted.',
             'Ahead of Thursday: here is the two-week pilot I suggested, with the numbers.',
             'I have attached some thoughts, in case any of them turn out to be useful.',
         ],
         correct=1,
         why='A dated attachment does the claiming for you, so the sentence '
             'around it only has to be ordinary.',
         ex=['TOO LOUD. It announces a dispute that has not happened yet, and '
             'dates the suspicion rather than the idea.',
             None,
             'TOO SOFT. &ldquo;Some thoughts&rdquo; is not a proposal, and '
             'nobody can steal what was never claimed.']),
]

FUNCTIONS = [
    ('What I proposed on Tuesday was&hellip;',
     'Names the author and the date in one breath'),
    ('Building on what I suggested&hellip;',
     'Reclaims it and hands the floor back'),
    ('Ahead of Thursday, here is&hellip;',
     'Puts it in writing before it can be repeated'),
    ('Yasmin crunched the numbers; I wrote the proposal.',
     'Gives first, so the claim reads as a fact'),
    ('I cut four days off the cycle.',
     'Replaces an opinion with a number'),
    ('Could we get that on the record?',
     'Asks for the correction without naming anyone'),
]

FUNC_GLOSS = {
    'de': {
        'What I proposed on Tuesday was&hellip;': 'Nennt Urheber und Datum in einem Zug',
        'Building on what I suggested&hellip;': 'Holt es zur&uuml;ck und gibt das Wort zur&uuml;ck',
        'Ahead of Thursday, here is&hellip;': 'Schriftlich, bevor es wiederholt werden kann',
        'Yasmin crunched the numbers; I wrote the proposal.': 'Gibt zuerst, dadurch klingt der Anspruch wie eine Tatsache',
        'I cut four days off the cycle.': 'Ersetzt eine Meinung durch eine Zahl',
        'Could we get that on the record?': 'Bittet um die Korrektur, ohne jemanden zu nennen',
    },
    'es': {
        'What I proposed on Tuesday was&hellip;': 'Nombra al autor y la fecha de una vez',
        'Building on what I suggested&hellip;': 'Lo recupera y devuelve la palabra',
        'Ahead of Thursday, here is&hellip;': 'Por escrito, antes de que puedan repetirlo',
        'Yasmin crunched the numbers; I wrote the proposal.': 'Da primero, y as&iacute; el m&eacute;rito suena a hecho',
        'I cut four days off the cycle.': 'Cambia una opini&oacute;n por un n&uacute;mero',
        'Could we get that on the record?': 'Pide la correcci&oacute;n sin se&ntilde;alar a nadie',
    },
    'ru': {
        'What I proposed on Tuesday was&hellip;': 'Называет автора и дату сразу',
        'Building on what I suggested&hellip;': 'Возвращает идею и отдаёт слово',
        'Ahead of Thursday, here is&hellip;': 'Письменно — до того, как повторят',
        'Yasmin crunched the numbers; I wrote the proposal.': 'Сначала отдаёт — и притязание звучит как факт',
        'I cut four days off the cycle.': 'Меняет мнение на цифру',
        'Could we get that on the record?': 'Просит поправку, никого не называя',
    },
}

# Eight. Ten of these wrapped the row to a third line and the row comes
# straight out of the activation panel's height — check-lesson.js's new
# ACTIVATION gate reported the write panel 27px past the canvas. The two
# multi-word phrases stay, because a phrase is the harder thing to produce.
CHIPS = ['take credit for', 'give credit to', 'contribution', 'instrumental',
         'quantify', 'on the record', 'building on', 'what I proposed was']


def build(style='editorial', out=None):
    deal(ROOM, [0, 2, 1])
    deal(EMAIL, [2])
    assert_key_is_middle(ROOM, 'ROOM')
    assert_key_is_middle(EMAIL, 'EMAIL')
    D.assert_bank_is_not_a_key(
        RECLAIM_BANK, [a for _, ans, _ in RECLAIM_A + RECLAIM_B for a in ans])
    D.assert_bank_is_not_a_key(
        NUM_BANK, [a for _, ans, _ in NUM_A + NUM_B for a in ans])

    logo = D.logo_from(TPL)
    A = lambda k: ART[k]

    slides = (
        D.cover(logo, 'Credit Where It&rsquo;s <em>Due</em>',
                'You said it on Tuesday. He said it on Thursday. The room '
                'heard it on Thursday.',
                [('Level', 'C1 &middot; Recognition at work'),
                 ('Focus', 'Claiming work without grandstanding'),
                 ('Count', 'COUNT slides')])

        + D.teach('caseEyebrow', 'The situation', 'caseTitle',
                  'Said on Tuesday, heard on Thursday', CASE)

        + art(D.teach('cleftEyebrow', 'The first move', 'cleftTitle',
                      'Put your name in the sentence', CLEFT,
                      cols='1fr 1fr', folder=F, bg=A('room')), shape='arch')

        + D.match(TERMS_TAKE, 'termsEyebrow', 'The vocabulary', 'termsTitleA',
                  'Taking it, and giving it', 'termsHint',
                  'Click a term, then the line that defines it.',
                  'TAKE credit FOR something; GIVE credit TO somebody. '
                  'ACKNOWLEDGE is said out loud; CLAIM expects to be checked.',
                  glosses=TERM_GLOSS)

        + D.match(TERMS_SHOW, 'termsEyebrow', 'The vocabulary', 'termsTitleB',
                  'Showing what was yours', 'termsHint',
                  'Click a term, then the line that defines it.',
                  'INSTRUMENTAL is the strongest of these and the easiest to '
                  'overuse. QUANTIFY is the one that ends arguments.',
                  glosses=TERM_GLOSS)

        + art(D.gap(1, 2, RECLAIM_A, RECLAIM_BANK, 'reclaimEyebrow',
                    'Say it in the room', 'reclaimTitle', 'Complete the line',
                    folder=F, bg=A('paper'), hint_key='reclaimHint',
                    hint='One word per gap; each is used once across both '
                         'screens.'), side='left')

        + art(D.gap(2, 2, RECLAIM_B, RECLAIM_BANK, 'reclaimEyebrow',
                    'Say it in the room', 'reclaimTitle', 'Complete the line',
                    folder=F, bg=A('folder'), hint_key='reclaimHint',
                    hint='One word per gap; each is used once across both '
                         'screens.'))

        + "".join(art(D.mc(i + 1, len(ROOM), q, 'roomEyebrow', 'In the room',
                           'roomTitle', 'What do you actually say?', folder=F,
                           explains=q['ex'], ctx_key='roomCtx%d' % (i + 1),
                           ctx=['He has just put your Tuesday idea to the '
                                'director as his own.',
                                'A colleague restates your point five minutes '
                                'after you made it.',
                                'The director thanks the team and names '
                                'everyone but you.'][i],
                           bg=A(['room', 'spotlight', 'spotlight'][i])),
                      side='left' if i % 2 else None,
                      shape='arch' if i == 2 else None)
                  for i, q in enumerate(ROOM))

        + D.teach('movesEyebrow', 'Three moves', 'movesTitle',
                  'How credit actually gets recorded', MOVES)

        + D.sort_slide(SORT_BINS, SORT_ITEMS, 'sortEyebrow', 'Before you say it',
                       'sortTitle', 'Claims it, or gives it away?', 'sortHint',
                       'Click a line, then the box it belongs in.',
                       'Every line in the right-hand box is grammatical, polite '
                       'and true. That is what makes it expensive.',
                       bin_keys=['sortBin1', 'sortBin2'])

        + art(D.order(ORDER_ITEMS, 'ordEyebrow', 'Say it cleanly', 'ordTitle',
                      'Build the sentence', 'ordHint',
                      'Click the parts in order.',
                      'The cleft carries the author; the last clause carries '
                      'the proof. Nobody has to take your word for it.',
                      folder=F, bg=A('paper')), shape='arch')

        + art(D.teach('voiceEyebrow', 'Active or passive', 'voiceTitle',
                      'Which voice puts you in it', VOICE,
                      cols='1fr 1fr', folder=F, bg=A('trail')))

        + art(D.gap(1, 2, NUM_A, NUM_BANK, 'numEyebrow', 'Put a number on it',
                    'numTitle', 'Complete the line', folder=F, bg=A('tally'),
                    hint_key='numHint',
                    hint='One word per gap; each is used once across both '
                         'screens.'), side='left')

        + art(D.gap(2, 2, NUM_B, NUM_BANK, 'numEyebrow', 'Put a number on it',
                    'numTitle', 'Complete the line', folder=F, bg=A('tally'),
                    hint_key='numHint',
                    hint='One word per gap; each is used once across both '
                         'screens.'))

        + art(D.mc(1, 1, EMAIL[0], 'mailEyebrow', 'Before the meeting',
                   'mailTitle', 'Put it in writing first', folder=F,
                   explains=EMAIL[0]['ex'], ctx_key='mailCtx',
                   ctx='You want the idea on the record before Thursday.',
                   bg=A('folder')), side='left')

        + D.match(FUNCTIONS, 'funcEyebrow', 'The phrase bank', 'funcTitle',
                  'What each line actually does', 'funcHint',
                  'Click a line, then the job it does in the room.',
                  'Not one of these says a word about the other person. That '
                  'is what makes them usable twice.', glosses=FUNC_GLOSS)

        + D.results(next_key='resNext', next_text='Now claim it out loud &rarr;')

        + D.activate(
            'Now claim it out loud', 'Use at least four:', CHIPS,
            'Speaking',
            'In pairs. Three minutes each, then swap roles and run it again.',
            ['He has just presented your idea. Reclaim it in one sentence.',
             'Swap. The director thanks everyone but you. Get into the record.',
             'Same meeting, and he is a friend. What changes, and what must not?',
             'The other side: when is claiming credit the wrong move?'],
            'Writing &middot; 180&ndash;220 words',
            'The email that puts your idea on the record before Thursday: one '
            'date, two numbers, one name that is not yours.',
            'Ahead of Thursday &mdash; the two-week pilot I suggested in '
            'Tuesday&rsquo;s stand-up, with the numbers behind it&hellip;',
            folder=F, bg=A('cups'))
    )

    import i18n_creditdue as I
    out_path = out or OUT
    s = D.assemble(TPL, out_path, slides,
                   D.editorial_palette('%s/%s' % (F, ART['hero'])),
                   'Credit Where It’s Due — Forbes English',
                   I, langs=('en', 'de', 'es', 'ru'), style=style)

    n = len(re.findall(r'<section class="slide[^>]*\bdata-type=', s))
    s = s.replace('COUNT slides', '%d slides' % n)
    s = s.replace('COUNT Folien', '%d Folien' % n)
    s = s.replace('COUNT diapositivas', '%d diapositivas' % n)
    ten, hun = n % 10, n % 100
    ru = ('слайдов' if 11 <= hun <= 14 else
          'слайд' if ten == 1 else
          'слайда' if ten in (2, 3, 4) else
          'слайдов')
    s = s.replace('COUNT слайдов', '%d %s' % (n, ru))
    open(out_path, 'w', encoding='utf-8', newline='').write(s)
    print('%s - %d slides (editorial)' % (out_path, n))


if __name__ == '__main__':
    build()
