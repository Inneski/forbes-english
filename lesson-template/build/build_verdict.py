# -*- coding: utf-8 -*-
"""Anatomy of a Verdict (C1) — a branching courtroom mystery, built like The Scarlet Star.

Innes, 2026-10-16: idea 30 of a list of adult RPGs whose titles, names and
plots are altered from modern films and series (here the shape of a juror
holding out against eleven, and a fall that may or may not have been a
push). First drafted as a Block Camp RPG; Innes: *"I dont want it to be
block camp, I want it like the Sherlock one Scarlet"*. So this is a
branch-flow deck on the house template, the same machine as
`sherlock-scarlet-star.html`: `<body data-flow="branch">`, nodes and
`data-goto` links, a ledger in the deck bar, gated endings.

The game. You are Mira Castell, a sound engineer and juror twelve, the one
"not guilty" in an eleven-to-one room. Ruth Adair is accused of pushing her
husband, Simon Hale, from the gallery of their mill. Every question is an
argument you make, and the language is CONCESSION: ALTHOUGH / EVEN THOUGH,
DESPITE / IN SPITE OF, EVEN SO / STILL / AND YET / THAT SAID, ADJECTIVE +
AS / THOUGH, MUCH AS / AS MUCH AS, MAY … BUT, HOWEVER / NO MATTER HOW,
WHATEVER, REGARDLESS OF, FOR ALL, TRY AS I MIGHT, EVEN IF vs EVEN THOUGH.
Every name, the case and the evidence are invented.

  trunk     room1–room4, room6   (room3 can turn Agnes: vote 1)
  fork 1    THE RECORDING rec1 rec2 rec4  |  THE STAIRWELL stair1 stair2 stair4
  trunk     after1–after3        (after3 can turn Priya: vote 2)
  fork 2    THE WITNESS wit1–wit3  |  THE CLOCK clock1–clock3 (both end on
            Gerald: vote 3)
  trunk     vote1 (Victor: vote 4), the closing speech, the final lock, vote2
  ledger    gold: every vote and Patience left; silver: enough points; shadow.

Sixteen MC and one two-row gap on every path. A correct answer pays +1
Point on the option itself; a wrong one costs one Patience (start 4). The
four vote questions route to a turned / held node, and only a turned node
carries the vote (`data-clue`). Glosses (Translate) on every narrative line
in DE and ES; stems and options stay English (HOUSE-STYLE §8).

**Art.** Noma Bar-style negative-space plates, like the Scarlet Star's,
briefed as Midjourney prompts in chat with --sref to the live
`Sherlock/hero.jpg`. Drop folder `incoming/verdict/`; plates go to
`Verdict/<name>.jpg`. Until every plate in PLATES is there, this writes the
gitignored preview `_forbes-anatomy-of-a-verdict-c1.html` on Scarlet Star
stand-ins with the Scarlet Star palette. With every plate in, it stops and
asks for PALETTE_LIVE from `extract-palette.py Verdict/hero.jpg`, then
writes `forbes-anatomy-of-a-verdict-c1.html`.

Run from the repo root:  py lesson-template/build/build_verdict.py
"""
import importlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_verdict as I
from chrome_i18n import CHROME

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-anatomy-of-a-verdict-c1.html'
PREVIEW = '_forbes-anatomy-of-a-verdict-c1.html'
F = 'Verdict'
TITLE = 'Anatomy of a Verdict (C1) | Forbes English'
E = dict(CHROME['en'], **I.T['en'])

# plate -> the Scarlet Star picture that stands in for it in the preview
PLATES = {
    'hero': 'hero', 'table': 'table', 'casefile': 'compass', 'rules': 'case',
    'danny': 'bar', 'agnes': 'faces', 'window': 'street', 'recording': 'teatin',
    'watch': 'study', 'trolley': 'door', 'headphones': 'celeste-eyes',
    'kitchen': 'body', 'stairs': 'stairs', 'bruise': 'celeste-face',
    'victor': 'moriarty-face', 'ballot': 'pov', 'witness': 'celeste-shadow',
    'van': 'carriage', 'hands': 'faces', 'dock': 'standoff', 'doors': 'platform',
    'box': 'chase-alley', 'act': 'pursued',
}

PALETTE_LIVE = None   # from: py lesson-template/extract-palette.py Verdict/hero.jpg

PALETTE_PREVIEW = '''  --hero: url('Sherlock/hero.jpg');

  --void          : #090c0e;
  --surface       : #12181c;
  --surface2      : #1c292d;
  --border        : #a84a3f;
  --text          : #f5f2f2;
  --text-dim      : #bfa6a3;
  --accent        : #e97264;
  --accent-bright : #f5a89f;
  --accent-dim    : #cd3624;
  --secondary     : #07466d;
  --contrast      : #1ded9f;'''

# ── the narrative, glossed. key -> English; DE/ES in i18n_verdict_<code>.N ──
N = {
    'casefile': '<strong>Tuesday</strong> Ruth and Simon argue. Simon records it on his phone.<br>'
                '<strong>Wednesday 14:25</strong> A doorbell camera shows Ruth’s van leaving the mill.<br>'
                '<strong>14:30</strong> Kit, the apprentice, says he heard a scream.<br>'
                '<strong>14:52</strong> Ruth calls 999. Simon lies at the foot of the iron stairs.',
    'casefile-note': 'Nobody saw the fall. The gallery rail is broken. Ruth says she was out buying clay.',
    'dec1-a': 'Your trade. Every second of Simon’s recording, every echo, every gap.',
    'dec1-b': 'Priya’s trade. The police photographs, the rail, the bruise.',
    'dec2-a': 'Kit Marlow, nineteen, the apprentice. He says he heard a scream.',
    'dec2-b': 'A doorbell camera, a white van, a 999 call. Twenty-seven minutes.',
    'agnes-yes': 'Agnes puts down her pencil. “All right. Not guilty, for now.” Her hand goes up with yours.',
    'agnes-no': 'Agnes frowns at the sentence and writes nothing down. “Try again later, dear.” Her vote stays where it was.',
    'priya-yes': 'Priya stands up and goes to the window. When she sits down again, she votes with you.',
    'priya-no': 'Priya shakes her head. “I can’t change my vote on a feeling.” The room grows impatient.',
    'gerald-yes': 'Gerald puts the watch back on and looks at the table. “Not guilty. Write it down.” The foreman has moved.',
    'gerald-no': 'Gerald looks at his watch again. “We’ve heard enough, I think.” His vote does not move.',
    'victor-yes': 'Victor opens his hands. For a long time he says nothing. Then: “Not guilty.” It is twelve to none.',
    'victor-no': 'Victor folds his arms again. “I’ve said my piece.” The room has to manage without him.',
    'board': 'Before the last vote, say three concessions aloud: admit one fact against Ruth each time, then turn it.',
    'end-gold': 'Twelve slips, one word. Ruth Adair grips the rail of the dock and does not cry. '
                'You will never know what happened on those stairs. That was the point: nobody in that room could know.',
    't-end-gold': 'Verdict · unanimous · not guilty',
    'end-silver': 'Eleven to one is enough after this long, the judge says. Victor would not move, and maybe he never could. '
                  'Ruth walks out into the rain, and you walk out behind her.',
    't-end-silver': 'Verdict · eleven to one · not guilty',
    'end-shadow': 'Four hours, three votes, and the room never settles. The judge discharges you. '
                  'There will be a retrial, a new twelve, the same recording.',
    't-end-shadow': 'No verdict · hung jury · retrial',
    'reveal-a': '<strong>What the evidence proved</strong><br>They argued the day before. Ruth lied about when she left. '
                'Simon fell from the gallery between two and three.',
    'reveal-b': '<strong>What it never proved</strong><br>A push. The crash was far from Ruth’s voice, the rail was rotten, '
                'the witness wore headphones, and the van was on the road.',
    'reveal-c': 'A jury does not decide what happened. It decides whether the evidence leaves a reasonable doubt.',
}

# ── the questions. (node, eyebrow, title, story, clue, stem, [key, wrong, wrong],
#    slot, why, picture). The slot is where the key is dealt: never a writer's habit.
Q = [
    ('room1', 'Chapter 1 · the first vote', 'Eleven to one.',
     'Gerald Pryce, the foreman, counts the slips. “Eleven guilty. One not guilty.” Every head turns towards you.',
     'Ruth was shouting at Simon the day before. You still have doubts.',
     'Which sentence states your position correctly?',
     ['Although she shouted, I’m not sure.', 'Although she shouted, but I’m not sure.',
      'Despite she shouted, I’m not sure.'], 0,
     'ALTHOUGH + a clause needs no BUT after it. DESPITE takes a noun or -ING, never a full clause like “she shouted”.',
     'table'),
    ('room2', 'Chapter 1 · the first vote', 'The cabbie.',
     'Danny Rourke drives a cab and has an opinion on everything. “She was angry. He’s dead. Job done.”',
     'You accept that she was angry. Anger alone proves nothing.',
     '___ her anger, it doesn’t prove she pushed him.',
     ['Despite', 'Although', 'Even though'], 1,
     'A noun phrase follows the gap, so you need DESPITE. ALTHOUGH and EVEN THOUGH need a clause: “although she was angry”.',
     'danny'),
    ('room3', 'Chapter 1 · the first vote', 'The headteacher.',
     'Agnes Bell, a retired headteacher, has filled four pages in pencil. She looks up. “Go on, then. Convince me.”',
     'Ruth lied to the police about when she left. You can’t deny it.',
     'Which sentence concedes the lie, then turns it?',
     ['She lied. Even so, a lie isn’t a push.', 'She lied. Even though, a lie isn’t a push.',
      'She lied. Despite, a lie isn’t a push.'], 2,
     'EVEN SO is an adverb that opens a new sentence. EVEN THOUGH and DESPITE are linkers and need something after them.',
     'agnes'),
    ('room4', 'Chapter 1 · the first vote', 'The recording plays.',
     'The usher brings in the laptop. Simon’s phone recording plays again: shouting, a crash, then Ruth crying.',
     'You are a sound engineer. The crash is very hard to place.',
     '___ hard I listen, I can’t tell what crashed.',
     ['However', 'Although', 'Even if'], 0,
     'HOWEVER + adjective or adverb + clause means “it makes no difference how”: however hard I listen. ALTHOUGH can’t take “hard” next.',
     'recording'),
    ('room6', 'Chapter 1 · the first vote', 'The foreman’s train.',
     'Gerald checks his watch. “Look, I respect you. But it’s eleven to one, and I’ve a train at six.”',
     'You respect Gerald too. You still want the evidence looked at again.',
     '___ I respect you, we have to look again.',
     ['Much as', 'Despite', 'Even'], 1,
     'MUCH AS + clause is a formal ALTHOUGH, often with like or respect. DESPITE needs a noun; EVEN alone isn’t a linker.',
     'watch'),

    ('rec1', 'Chapter 2 · the recording', 'The shouting.',
     'Headphones on. Ruth’s voice: “You never finish anything!” Then Simon, laughing. Danny leans in. “Hear that? Furious.”',
     'She sounds furious. Yet Simon is laughing, so he wasn’t afraid.',
     'She ___ furious, but Simon wasn’t afraid of her.',
     ['may have been', 'might had been', 'may has been'], 2,
     'MAY HAVE + past participle concedes a past possibility before BUT turns it. After a modal comes HAVE, never HAD or HAS.',
     'headphones'),
    ('rec2', 'Chapter 2 · the recording', 'The crash.',
     'You loop the crash five times. The echo is long: it happened far from the phone, near the kitchen.',
     'Ruth’s voice is close to the phone at the very moment of the crash.',
     'Which sentence makes your point correctly?',
     ['Loud though it is, she’s nowhere near it.', 'Though loud it is, she’s nowhere near it.',
      'Loud despite it is, she’s nowhere near it.'], 0,
     'ADJECTIVE + THOUGH + clause works like ADJECTIVE + AS: loud though it is. The adjective comes first, then THOUGH.',
     'kitchen'),
    ('rec4', 'Chapter 2 · the recording', 'Danny goes quiet.',
     'You play Danny the echo, then the gap in the file. He is quiet for once. “All right. It’s not as clear as I thought.”',
     'Danny still thinks she’s capable of it. But he admits there’s doubt.',
     'Danny: “___ she’s capable of it, I can’t be certain.”',
     ['While', 'Whereas', 'Nevertheless'], 1,
     'WHILE + clause can concede: while she’s capable of it = although. WHEREAS compares two facts; NEVERTHELESS opens a new clause.',
     'headphones'),

    ('stair1', 'Chapter 2 · the stairwell', 'The photographs.',
     'Priya Sandhu, an A&E nurse, spreads the police photos under the lamp. Iron stairs, a high gallery, a rail hanging from one bolt.',
     'The rail is broken. The prosecution says Ruth broke it in a struggle.',
     'Which sentence answers the prosecution correctly?',
     ['It’s broken. That said, nobody knows when.', 'It’s broken. Although, nobody knows when.',
      'It’s broken. That saying, nobody knows when.'], 1,
     'THAT SAID at the start of a sentence concedes the point before it. ALTHOUGH can’t stand alone before a comma.',
     'stairs'),
    ('stair2', 'Chapter 2 · the stairwell', 'The bruise.',
     'Priya grips her own arm. “A hand makes a mark like that. So does a rail, if you grab it as you fall.”',
     'You try every way to read the bruise as a grip. It still fits a fall.',
     '___ I might, I can’t make it a push.',
     ['Try as', 'As try', 'Trying as'], 2,
     'VERB + AS + subject + MIGHT concedes effort that failed: try as I might = although I try hard. Use the base verb.',
     'bruise'),
    ('stair4', 'Chapter 2 · the stairwell', 'The rusted bolt.',
     'In the photo the bolt is rusted through. In March Simon emailed a builder about the rail. He never booked him.',
     'Ruth may or may not have been on the stairs. The rail was dangerous anyway.',
     'Which sentence states the point correctly?',
     ['Even if she was there, it was unsafe.', 'Even though she was there, it was unsafe.',
      'Even she was there, it was unsafe.'], 0,
     'EVEN IF: we don’t know whether she was there. EVEN THOUGH would treat it as fact. EVEN alone isn’t a linker.',
     'stairs'),

    ('after1', 'Chapter 3 · after lunch', 'Arty types.',
     'Lunch arrives in plastic boxes. Victor Lane, a landlord, hasn’t touched his. “Arty types. They all lie.”',
     'Victor has judged her by her job, not the evidence. You keep calm.',
     '___ your feelings about artists, look at the facts.',
     ['Whatever', 'However', 'Whichever'], 0,
     'WHATEVER + noun concedes any possibility: whatever your feelings = it makes no difference what they are. HOWEVER needs an adjective.',
     'victor'),
    ('after2', 'Chapter 3 · after lunch', 'The second vote.',
     'Gerald calls a second vote. The hands go up more slowly this time. Victor slams the table. “This is ridiculous.”',
     'The vote has moved. Victor is just as certain as before.',
     'Victor: “___ the vote, she’s guilty.”',
     ['Regardless of', 'Regardless to', 'Irregardless of'], 1,
     'REGARDLESS OF + noun = it makes no difference: regardless of the vote. The preposition is OF, never TO.',
     'ballot'),
    ('after3', 'Chapter 3 · after lunch', 'At the window.',
     'You stand at the window with Agnes and Priya. Rain on the car park. “He’s not a bad man,” Agnes says. “Just tired.”',
     'Victor is rude. Agnes thinks he deserves a hearing anyway.',
     'Priya: “He’s rude. ___, he deserves a hearing.”',
     ['Still', 'Although', 'Despite'], 2,
     'STILL at the start of a sentence concedes the last point: still, he deserves a hearing. ALTHOUGH and DESPITE must join to something.',
     'window'),

    ('wit1', 'Chapter 4 · the witness', 'Kit’s statement.',
     'Kit Marlow, the apprentice, told the court he heard “a scream, then a thud” from the stairwell at half past two.',
     'Kit sounded honest. He was also wearing headphones at the potter’s wheel.',
     'Which sentence is fair to Kit?',
     ['He may be honest, but he had headphones on.', 'He may honest, but he had headphones on.',
      'He may is honest, but he had headphones on.'], 1,
     'MAY + base verb … BUT concedes, then turns: he may be honest, but. MAY never takes IS, and BE can’t be dropped.',
     'witness'),
    ('wit2', 'Chapter 4 · the witness', 'Exhibit fourteen.',
     'Exhibit 14: Kit’s headphones, found on the wheel. You know this model. It blocks out almost everything.',
     'Kit’s music was loud. A scream might still get through, just about.',
     '___ loud the music was, a scream might get through.',
     ['No matter how', 'No matter', 'No matter how much'], 2,
     'NO MATTER HOW + adjective + clause: no matter how loud the music was. Loud is an adjective, so there’s no MUCH.',
     'headphones'),
    ('wit3', 'Chapter 4 · the witness', 'Gerald listens.',
     'Gerald puts on the headphones himself and plays music. Agnes screams behind him. Gerald doesn’t turn round.',
     'Gerald heard almost nothing. He wanted to go home. Now he wants it right.',
     'Gerald: “___ to go home, I’m changing my vote.”',
     ['Despite wanting', 'Despite I want', 'Despite of wanting'], 0,
     'DESPITE + -ING: despite wanting to go home. Never DESPITE + subject and verb, and never DESPITE OF.',
     'table'),

    ('clock1', 'Chapter 4 · the clock', 'The white van.',
     'A neighbour’s doorbell camera shows Ruth’s van leaving the mill at 14:25. Her 999 call comes at 14:52.',
     'Simon died between two and three, so the times don’t clear her.',
     'Which sentence concedes the point correctly?',
     ['It isn’t proof. And yet it matters.', 'It isn’t proof. Although it matters.',
      'It isn’t proof. Despite it matters.'], 0,
     'AND YET can open a new sentence. “Although it matters” has no main clause, and DESPITE can’t take a subject and verb.',
     'van'),
    ('clock2', 'Chapter 4 · the clock', 'Twelve minutes.',
     'The van’s satnav was read out in court: twelve minutes to the clay merchant, twelve back, one stop on the way.',
     'She could have driven fast. The satnav says she kept to the limit.',
     '___ she could have driven fast, the satnav says not.',
     ['Though', 'Even', 'In spite of'], 1,
     'THOUGH + clause = although: though she could have driven fast. EVEN alone isn’t a linker; IN SPITE OF needs a noun.',
     'recording'),
    ('clock3', 'Chapter 4 · the clock', 'It doesn’t add up.',
     'Gerald takes off his watch and lays it on the table. “Twelve there, twelve back, and a stop. It doesn’t add up.”',
     'Gerald’s train matters to him. The timeline matters more now.',
     'Gerald: “___ my train, I’ll stay until we’re sure.”',
     ['In spite of', 'In spite', 'Even though'], 2,
     'IN SPITE OF + noun: in spite of my train. IN SPITE needs OF; EVEN THOUGH needs a subject and verb.',
     'watch'),

    ('vote1', 'Chapter 5 · the verdict', 'Eleven to one again.',
     'It is eleven to one again, the other way. Victor looks at his hands. “My son walked out too. Never said why.”',
     'Victor is hurting. You understand him, and you still need his vote.',
     '___ I understand, this isn’t about your son.',
     ['As much as', 'As much', 'So much as'], 0,
     'AS MUCH AS + clause concedes a feeling: as much as I understand. Both ASes are needed; SO MUCH AS means something else.',
     'victor'),
    ('vote2', 'Chapter 5 · the verdict', 'The last ballot.',
     'The usher knocks. Gerald holds out his hand for the slips. Victor’s is the last to go onto the pile.',
     'You’ll never know what happened on those stairs. The doubt is reasonable.',
     'Which sentence closes the case correctly?',
     ['Although we can’t know, we must decide.', 'Although we can’t know, but we must decide.',
      'Despite we can’t know, we must decide.'], 1,
     'ALTHOUGH + clause, then the main clause, with no BUT. DESPITE can’t take “we can’t know”: it needs a noun or -ING.',
     'ballot'),
]

# where each question leads; a vote question leads to its two outcome nodes
NEXT = {
    'room1': 'room2', 'room2': 'room3', 'room3': ('agnes-yes', 'agnes-no'),
    'room4': 'room6', 'room6': 'dec1',
    'rec1': 'rec2', 'rec2': 'rec4', 'rec4': 'after1',
    'stair1': 'stair2', 'stair2': 'stair4', 'stair4': 'after1',
    'after1': 'after2', 'after2': 'after3', 'after3': ('priya-yes', 'priya-no'),
    'wit1': 'wit2', 'wit2': 'wit3', 'wit3': ('gerald-yes', 'gerald-no'),
    'clock1': 'clock2', 'clock2': 'clock3', 'clock3': ('gerald-yes', 'gerald-no'),
    'vote1': ('victor-yes', 'victor-no'), 'vote2': 'ledger',
}
# outcome node -> (picture, vote it carries or None, where it leads)
OUTCOME = {
    'agnes-yes': ('window', 'v1', 'room4'), 'agnes-no': ('window', None, 'room4'),
    'priya-yes': ('ballot', 'v2', 'dec2'), 'priya-no': ('ballot', None, 'dec2'),
    'gerald-yes': ('hands', 'v3', 'vote1'), 'gerald-no': ('hands', None, 'vote1'),
    'victor-yes': ('hands', 'v4', 'board'), 'victor-no': ('box', None, 'board'),
}
GOLD = 'dp>=14 && time>=1 && clues>=4'
SILVER = 'dp>=9'
PATIENCE = 4


def bg(pic, preview):
    if preview:
        return ' data-bg="Sherlock/%s.jpg"' % PLATES[pic]
    return ' data-bg="%s/%s.jpg"' % (F, pic)


def cont(to, key='btnContinue'):
    return ('        <div style="margin-top:18px">\n'
            '          <button class="btn btn-solid" data-goto="%s" data-i18n="%s">%s</button>\n'
            '        </div>\n' % (to, key, E[key]))


def head(eyebrow, title, eyebrow_key=None, title_key=None):
    ek = ' data-i18n="%s"' % eyebrow_key if eyebrow_key else ''
    tk = ' data-i18n="%s"' % title_key if title_key else ''
    return ('      <div class="slide-head"><div>\n'
            '        <div class="eyebrow"%s>%s</div>\n'
            '        <h2 class="slide-title"%s>%s</h2>\n'
            '      </div></div>\n' % (ek, eyebrow, tk, title))


def section(node, kind, act, body, pic=None, preview=False, extra=''):
    return ('\n    <section class="slide" data-type="%s" data-node="%s" data-act="%s"%s%s>\n%s'
            '    </section>\n' % (kind, node, act, bg(pic, preview) if pic else '', extra, body))


def merged(story, clue):
    return '%s<br><span class="dim">%s</span>' % (story, clue)


def gl(key, cls='prose'):
    return '<p class="%s gloss" data-tr="%s">%s</p>' % (cls, key, N[key])


def teach(node, act, eyebrow, title, inner, to, pic, preview, extra='', ek=None, tk=None):
    body = (head(eyebrow, title, ek, tk) +
            '      <div class="slide-body" style="position:relative">\n        %s\n' % inner +
            cont(to) + '      </div>\n')
    return section(node, 'teach', act, body, pic, preview, extra)


def mc(n, q, preview):
    node, eyebrow, title, story, clue, stem, opts, slot, why, pic = q
    key, w1, w2 = opts
    dealt = [w1, w2]
    dealt.insert(slot, key)
    nxt = NEXT[node]
    yes, no = nxt if isinstance(nxt, tuple) else (nxt, nxt)
    buttons = []
    for o in dealt:
        if o == key:
            buttons.append('<button class="opt" data-correct data-dp="1" data-goto="%s">%s</button>' % (yes, o))
        else:
            buttons.append('<button class="opt" data-time="-1" data-goto="%s">%s</button>' % (no, o))
    N['s-' + node], N['c-' + node] = story, clue
    body = (head('%s · question %d' % (eyebrow, n), title) +
            '      <div class="slide-body">\n'
            '        <p class="q-ctx gloss" data-tr="q-%s" style="margin-bottom:16px">%s</p>\n'
            % (node, merged(story, clue)) +
            '        <p class="q-stem">%s</p>\n' % stem +
            '        <div class="opts two-up">\n          %s\n        </div>\n' % '\n          '.join(buttons) +
            '        <p class="feedback" data-explain="%s"></p>\n' % D.esc(why) +
            '        <div style="margin-top:14px">\n'
            '          <button class="btn btn-solid" data-action="branch-continue" data-i18n="btnContinue" hidden>%s</button>\n'
            '        </div>\n      </div>\n' % E['btnContinue'])
    return section(node, 'mc', eyebrow.split(' · ')[0], body, pic, preview)


def decision(node, act, eyebrow, title, a, b, pic, preview):
    def card(k, to, ck):
        return ('          <div class="card">\n'
                '            %s\n'
                '            <div style="margin-top:12px"><button class="btn btn-solid choice" '
                'data-goto="%s" data-i18n="%s">%s</button></div>\n'
                '          </div>\n' % (gl(k), to, ck, E[ck]))
    body = (head(eyebrow, title) +
            '      <div class="slide-body">\n        <div class="cols">\n' +
            card(*a) + card(*b) +
            '        </div>\n'
            '        <p class="prose dim" style="margin-top:14px;text-align:center" '
            'data-i18n="explainFirst">%s</p>\n      </div>\n' % E['explainFirst'])
    return section(node, 'teach', act, body, pic, preview)


def build_slides(preview):
    logo = D.logo_from(TPL)
    by = {q[0]: q for q in Q}
    num = {}

    def m(node):
        # numbered by position on its own path, so both arms read 6, 7, 8 …
        return mc(num.setdefault(node, POS[node]), by[node], preview)

    cover = D.cover(logo, E['coverTitle'], E['coverSub'],
                    [('Level', E['chipLevel']), ('Focus', E['chipFocus']), ('Count', E['chipCount'])])
    cover = cover.replace('data-type="cover"', 'data-type="cover" data-node="cover" data-act=""', 1)
    cover = cover.replace('data-action="next"', 'data-goto="how"', 1)
    how = section('how', 'teach', E['actBefore'],
                  head(E['howEyebrow'], E['howTitle'], 'howEyebrow', 'howTitle') +
                  '      <div class="slide-body">\n        <div class="cols cols-3">\n' +
                  ''.join('          <div class="card"><p class="prose"><strong data-i18n="%s">%s</strong><br>'
                          '<span data-i18n="%sBody">%s</span></p></div>\n'
                          % (k, E[k], k, E[k + 'Body']) for k in ('howDp', 'howTime', 'howClues')) +
                  '        </div>\n' + cont('casefile') + '      </div>\n', 'table', preview)

    casefile = teach('casefile', E['actBefore'], 'R v Adair · Kingsmere Crown Court', 'Simon Hale is dead.',
                     '<div class="cols" style="grid-template-columns:2fr 1fr"><div class="card">%s</div>'
                     '<div class="card">%s</div></div>'
                     % (gl('casefile'), gl('casefile-note', 'prose dim')), 'lab', 'casefile', preview)

    lab_cards = ''.join(
        '<div class="card"><p class="prose"><strong>%s</strong><br>%s</p></div>' % (h, ex)
        for h, ex in LAB)
    lab = teach('lab', E['actBefore'], E['labEyebrow'], E['labTitle'],
                '<div class="cols cols-3">%s</div>' % lab_cards, 'room1', 'rules', preview,
                ek='labEyebrow', tk='labTitle')

    def outcome(node, title):
        pic, vote, to = OUTCOME[node]
        extra = ' data-clue="%s"' % vote if vote else ''
        eyebrow = E['voteTurned'] if vote else E['voteHeld']
        return teach(node, 'Verdict', eyebrow, title, '<div class="card">%s</div>' % gl(node),
                     to, pic, preview, extra, ek='voteTurned' if vote else 'voteHeld')

    board = teach('board', 'Chapter 5', E['boardEyebrow'], E['boardTitle'],
                  '<div class="card">%s</div>' % gl('board'), 'lock', 'rules', preview,
                  ek='boardEyebrow', tk='boardTitle')

    lock_rows = ''.join(
        '          <div class="card gap-row">\n'
        '            <p class="q-stem" style="font-size:21px">%s</p>\n'
        '            <p class="prose dim" style="font-size:13px;margin-top:6px">%s</p>\n'
        '            <p class="feedback" data-explain="%s"></p>\n'
        '          </div>\n' % (s.replace('______', '<input class="gap" data-answer="%s" aria-label="gap" '
                                 'style="width:%dch">' % (a, max(5, max(len(x) for x in a.split('|')) + 3))),
                                 hint, D.esc(w))
        for s, a, hint, w in LOCK)
    lock = section('lock', 'gap', 'Chapter 5',
                   head(E['lockEyebrow'], E['lockTitle'], 'lockEyebrow', 'lockTitle') +
                   '      <div class="slide-body">\n' + lock_rows +
                   '        <div style="margin-top:14px;display:flex;gap:10px">\n'
                   '          <button class="btn" data-action="check" data-i18n="btnCheck">%s</button>\n'
                   '          <button class="btn btn-solid" data-goto="vote2" data-i18n="btnContinue">%s</button>\n'
                   '        </div>\n      </div>\n' % (E['btnCheck'], E['btnContinue']),
                   'hands', preview, ' data-dp="1"')

    ledger = section('ledger', 'teach', 'Verdict',
                     head(E['ledgerEyebrow'], E['ledgerTitle'], 'ledgerEyebrow', 'ledgerTitle') +
                     '      <div class="slide-body">\n        <div class="cols cols-3">\n' +
                     ''.join('          <div class="card">\n'
                             '            <p class="prose"><strong data-i18n="%s">%s</strong><br>'
                             '<span data-i18n="%sBody">%s</span></p>\n'
                             '            <div style="margin-top:12px"><button class="btn btn-solid choice" '
                             'data-goto="end-%s"%s data-i18n="%s">%s</button></div>\n'
                             '          </div>\n'
                             % (k, E[k], k, E[k + 'Body'], end,
                                ' data-require="%s"' % req if req else '', k, E[k])
                             for k, end, req in (('gold', 'gold', GOLD), ('silver', 'silver', SILVER),
                                                 ('shadow', 'shadow', None))) +
                     '        </div>\n'
                     '        <p class="prose dim" style="margin-top:14px;text-align:center" '
                     'data-i18n="ledgerNote">%s</p>\n      </div>\n' % E['ledgerNote'],
                     'table', preview)

    def ending(k, title, pic):
        return teach('end-' + k, 'Ending', E['end' + k.capitalize()], title,
                     '<div class="card">%s</div>\n        %s'
                     % (gl('end-' + k), gl('t-end-' + k, 'prose dim').replace(
                         '<p class="prose dim', '<p style="margin-top:14px;text-align:center;'
                         'text-transform:uppercase;letter-spacing:.1em;font-size:12px" class="prose dim', 1)),
                     'reveal', pic, preview, ek='end' + k.capitalize())

    reveal = teach('reveal', 'Solution', E['revealKick'], 'Nobody in that room could know.',
                   '<div class="cols cols-3"><div class="card">%s</div><div class="card">%s</div>'
                   '<div class="card">%s</div></div>'
                   % (gl('reveal-a'), gl('reveal-b'), gl('reveal-c', 'prose dim')),
                   'results', 'casefile', preview, ek='revealKick')

    results = D.results(next_key='resRoute', next_text=E['resRoute'], folder='Sherlock' if preview else F,
                        bg=(PLATES['hero'] if preview else 'hero') + '.jpg')
    results = results.replace('data-type="results"', 'data-type="results" data-node="results" data-act="Solution"', 1)
    i = results.rindex('      </div>\n    </section>')
    results = results[:i] + cont('activate', 'resNext') + results[i:]

    act = D.activate(E['actTitle'], E['actUse'], CHIPS, 'Speaking', E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder'],
                     folder='Sherlock' if preview else F,
                     bg=(PLATES['act'] if preview else 'act') + '.jpg')
    act = act.replace('data-type="activate"', 'data-type="activate" data-node="activate" data-act="Activation"', 1)
    act = act.replace('data-action="restart"', 'data-action="restart" data-goto="how"', 1)

    slides = ''.join([
        cover, how, casefile, lab,
        m('room1'), m('room2'), m('room3'),
        outcome('agnes-yes', 'Agnes changes her vote.'), outcome('agnes-no', 'Agnes isn’t convinced.'),
        m('room4'), m('room6'),
        decision('dec1', 'Chapter 2', 'Decision 1 · one piece of evidence', 'What do you reopen?',
                 ('dec1-a', 'rec1', 'chooseA'), ('dec1-b', 'stair1', 'chooseB'), 'trolley', preview),
        m('rec1'), m('rec2'), m('rec4'),
        m('stair1'), m('stair2'), m('stair4'),
        m('after1'), m('after2'), m('after3'),
        outcome('priya-yes', 'Priya changes her vote.'), outcome('priya-no', 'Priya holds her vote.'),
        decision('dec2', 'Chapter 4', 'Decision 2 · one reason for Victor', 'Where does the doubt lie?',
                 ('dec2-a', 'wit1', 'chooseC'), ('dec2-b', 'clock1', 'chooseD'), 'victor', preview),
        m('wit1'), m('wit2'), m('wit3'),
        m('clock1'), m('clock2'), m('clock3'),
        outcome('gerald-yes', 'The foreman moves.'), outcome('gerald-no', 'The foreman holds.'),
        m('vote1'),
        outcome('victor-yes', 'Victor changes his vote.'), outcome('victor-no', 'Victor holds out.'),
        board, lock, m('vote2'), ledger,
        ending('gold', 'Not guilty, twelve to none.', 'dock'),
        ending('silver', 'Not guilty, by majority.', 'doors'),
        ending('shadow', 'No verdict.', 'box'),
        reveal, results, act,
    ])
    return slides


LAB = [
    ('ALTHOUGH / EVEN THOUGH + CLAUSE', 'Although she was angry, nobody saw her push him.'),
    ('DESPITE / IN SPITE OF + NOUN OR -ING', 'Despite the shouting, the recording proves nothing.'),
    ('EVEN SO / STILL / AND YET', 'She lied about the time. Even so, that isn’t murder.'),
    ('ADJECTIVE + AS / THOUGH + CLAUSE', 'Strange as it sounds, the rail was already loose.'),
    ('MAY … BUT · MUCH AS + CLAUSE', 'She may have been furious, but furious isn’t guilty.'),
    ('EVEN IF ≠ EVEN THOUGH', 'Even if she was there, the rail was unsafe.'),
]

LOCK = [
    ('______ the shouting, nobody saw a push.', 'Despite|In spite of|despite|in spite of',
     'DESPITE / IN SPITE OF + noun',
     'A noun follows, so <strong>despite</strong> or <strong>in spite of</strong>, not although.'),
    ('She may ______ angry, but that doesn’t make her a killer.', 'have been',
     'MAY HAVE + past participle · be',
     'A past possibility, conceded: <strong>may have been</strong>.'),
]

CHIPS = ['although', 'even so', 'despite + -ing', 'much as', 'may have … but',
         'even if', 'that said', 'adjective + as']

# question number on its own path: trunk 1–5, arm 6–8, 9–11, arm 12–14, 15, 16
POS = {}
for _i, _n in enumerate(['room1', 'room2', 'room3', 'room4', 'room6'], 1):
    POS[_n] = _i
for _arm in (['rec1', 'rec2', 'rec4'], ['stair1', 'stair2', 'stair4']):
    for _i, _n in enumerate(_arm, 6):
        POS[_n] = _i
for _i, _n in enumerate(['after1', 'after2', 'after3'], 9):
    POS[_n] = _i
for _arm in (['wit1', 'wit2', 'wit3'], ['clock1', 'clock2', 'clock3']):
    for _i, _n in enumerate(_arm, 12):
        POS[_n] = _i
POS['vote1'], POS['vote2'] = 15, 16
PATHS = [['room1', 'room2', 'room3', 'room4', 'room6'] + a + ['after1', 'after2', 'after3'] + b + ['vote1', 'vote2']
         for a in (['rec1', 'rec2', 'rec4'], ['stair1', 'stair2', 'stair4'])
         for b in (['wit1', 'wit2', 'wit3'], ['clock1', 'clock2', 'clock3'])]


def gates(slides):
    """The checks a branching deck needs that check-lesson.js does not make."""
    D.assert_no_key_is_longest([dict(options=q[6], correct=0) for q in Q], 'MC')
    nodes = re.findall(r'data-node="([^"]+)"', slides)
    assert len(nodes) == len(set(nodes)), 'duplicate node'
    gotos = set(re.findall(r'data-goto="([^"]+)"', slides))
    missing = gotos - set(nodes)
    assert not missing, 'data-goto to no node: %s' % missing
    orphans = set(nodes) - gotos - {'cover'}
    assert not orphans, 'orphan nodes: %s' % orphans
    # every path: the key dealt evenly, never three running in one slot
    by = {q[0]: q for q in Q}
    for p in PATHS:
        t = [0, 0, 0]
        for n in p:
            t[by[n][7]] += 1
        assert max(t) <= 0.4 * len(p), ('key slots', p, t)
        for a, b, c in zip(p, p[1:], p[2:]):
            assert not (by[a][7] == by[b][7] == by[c][7]), ('three running', a, b, c)
        votes = sum(1 for n in p if isinstance(NEXT[n], tuple))
        assert votes == 4, ('votes on a path', p, votes)
    # Gold must be reachable: 16 MC + the lock = 17 points at most on a path
    assert 14 <= 17
    # no two linked slides share a picture
    pic = dict(re.findall(r'data-node="([^"]+)"[^>]*?data-bg="([^"]+)"', slides))
    secs = re.findall(r'data-node="([^"]+)"(.*?)</section>', slides, flags=re.S)
    for node, body in secs:
        for to in set(re.findall(r'data-goto="([^"]+)"', body)):
            if node in pic and to in pic and pic[node] == pic[to]:
                raise AssertionError('%s and %s are neighbours on one picture (%s)' % (node, to, pic[node]))
    for k in N:
        assert '’' not in k


def narrative_tr(langs):
    out = {}
    for c in langs[1:]:
        mod = importlib.import_module('i18n_verdict_%s' % c)
        nk = set(N) - set(mod.N)
        assert not nk, '%s glosses missing: %s' % (c, sorted(nk))
        extra = set(mod.N) - set(N)
        assert not extra, '%s glosses for nothing: %s' % (c, sorted(extra))
        # one Translate per question: the story and its evidence share it, or
        # two open glosses push the options off a 720px slide (DE, stair1)
        bank = {k: v for k, v in mod.N.items() if not k.startswith(('s-', 'c-'))}
        for q in Q:
            bank['q-' + q[0]] = merged(mod.N['s-' + q[0]], mod.N['c-' + q[0]])
        out[c] = bank
    return 'const NARRATIVE_TR = ' + json.dumps(out, ensure_ascii=False, indent=1) + ';\n'


def build():
    have = [p for p in PLATES if os.path.exists(os.path.join(F, p + '.jpg'))]
    preview = len(have) < len(PLATES)
    if not preview and PALETTE_LIVE is None:
        sys.exit('Every plate is in %s/. Run extract-palette.py %s/hero.jpg, paste its block '
                 'into PALETTE_LIVE, and run again.' % (F, F))
    slides = build_slides(preview)
    gates(slides)
    n = slides.count('<section class="slide')

    langs = tuple(c for c in I.LANGS if c in I.T)
    out = PREVIEW if preview else OUT
    s = D.assemble(TPL, out, slides, PALETTE_PREVIEW if preview else PALETTE_LIVE, TITLE, I, langs=langs)
    s = s.replace('<body>', '<body data-flow="branch" data-start="cover" data-time="%d">' % PATIENCE, 1)
    s = s.replace('const UI_I18N = {', narrative_tr(langs) + 'const UI_I18N = {', 1)
    open(out, 'w', encoding='utf-8', newline='').write(s)
    print('wrote %s — %d slides, %s%s' % (out, n, ','.join(langs),
                                          ' (PREVIEW: %d of %d plates in %s/)' % (len(have), len(PLATES), F)
                                          if preview else ''))


if __name__ == '__main__':
    build()
