# -*- coding: utf-8 -*-
"""Reasonable Doubt (B2–C1) — a jury-room RPG, built like The Scarlet Star.

Innes, 2026-10-23: a ChatGPT export, `Forbes_English_12_Angry_Men_RPG_V1.html`
(41 illustrated scenes, one scrolling page, pictures inlined as WebP), with
"You need to rename this and fix it up forbes style". Renamed after the
export's own subtitle: the film's title is off every page, and so is every
mention of "the film". Built as a branch-flow deck on the house template,
the same machine as `sherlock-scarlet-star.html` and `build_verdict.py`
(an adult story RPG is a Scarlet deck, not Block Camp).

The game. You are Juror 8 in a New York jury room in 1957, the one hand
that stays down in an eleven-to-one vote. Every question is something you
say to the room. The language: past modals of possibility and deduction
(MIGHT / MAY / COULD HAVE, CAN'T HAVE), concession (EVEN IF, ALTHOUGH,
DESPITE), the unreal past, reported speech with backshift, CLAIM TO HAVE,
WOULD RATHER + past simple, UNLESS, HEAR SOMEONE OUT.

  trunk     q04 q05
  hub       evidence: files A (q07–q11), B (q12–q16), C (q17–q21) in any
            order; each checkpoint carries a file (data-clue), and the jury
            reconvenes only with all three (clues>=3)
  trunk     shift q23–q26
  fork      quiet: q28 (HEAR HIM OUT)  |  q29 (UNLESS)
  trunk     q30–q33 photograph q35
  verdict   not guilty (needs Patience left) | more discussion | guilty to leave
  27 MC on every route (the export's 28 counts both arms of the fork).

What changed from the export, and why (none of it is on a slide):
  - Ten keys were the only longest option, by up to 33 characters; their
    distractors are lengthened, never the key shortened.
  - Every explanation rewritten with the grammar in CAPS and cited words in
    double quotes (the house rule), and kept English (HOUSE-STYLE §8). The
    export translated the stems and options too; those are English here.
  - The scene selector, answer key and teacher notes are dropped (the
    results slide keeps every miss); the twelve-juror cast is its own slide;
    the toolkit grew from four forms to six so it covers what is asked.
  - The two "speak before you move on" prompts on question slides ride in
    the feedback; the rest are on the bridges, and the closing statement and
    the role-swap debrief are the activation stage.
  - The three endings were a free choice. The reasoned verdict now needs
    Patience left: lose the room five times and it will not follow you.

Pictures: the export's own 41 plates (1536×1024, a painted mid-century
look), through prep-artwork.py into ReasonableDoubt/. The palette is
extract-palette.py ReasonableDoubt/hero.jpg --light.

Run from the repo root:  py lesson-template/build/build_reasonable_doubt.py
"""
import importlib
import itertools
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_reasonable_doubt as I
from chrome_i18n import CHROME

TPL = 'lesson-template/lesson-template.html'
OUT = 'reasonable-doubt-rpg.html'
F = 'ReasonableDoubt'
TITLE = 'Reasonable Doubt (B2–C1) | Forbes English'
E = dict(CHROME['en'], **I.T['en'])
PATIENCE = 5

PALETTE = '''  --hero: url('ReasonableDoubt/hero.jpg');

  --void          : #d8c9ac;
  --surface       : #e1d7c4;
  --surface2      : #dccfb8;
  --border        : #967b4a;
  --text          : #2a2111;
  --text-dim      : #5e4d2e;
  --accent        : #764c00;
  --accent-bright : #654711;
  --accent-dim    : #e09611;
  --secondary     : #334a4d;
  --contrast      : #0d5968;'''

# ── the narrative, glossed. key -> English; DE/ES in i18n_reasonable_doubt_<code>.N ──
N = {
    'brief': 'New York, 1957. A young man is accused of killing his father. Eleven jurors seem ready to '
             'convict. You are not convinced the evidence is reliable. Your task: make room for doubt, '
             'without pretending to know what happened.',
    'toolkit': 'You can question an argument without attacking the person making it. '
               'Choose the strength of your language carefully.',
    'evidence': 'Three claims hold the case together. Choose which one to investigate first. '
                'Complete all three files to return to the full jury.',
    'shift': 'The knife is no longer unique. The timing is uncertain. The view may have been obstructed. '
             'Several jurors are reconsidering. Now you must protect a fair discussion as well as a careful argument.',
    'shift-say': 'Say it aloud: a 30-second summary of the three files, with MIGHT HAVE, EVEN IF and ALTHOUGH.',
    'quiet': 'A quiet juror tries to speak while two louder men argue. You can create space gently '
             'or interrupt the confrontation directly.',
    'photograph': 'Juror 3 takes out a worn photograph of himself and his son. The argument stops. You give him time. '
                  'A fair discussion sometimes needs silence more than another clever sentence.',
    'photograph-say': 'Say it aloud, in your own words, without diagnosing him. Begin: “Take your time. We can …”',
    'verdict': 'You have heard the arguments and tested the claims. Choose the vote you can defend.',
    'end-doubt': 'The jury agrees on not guilty. You leave the courthouse knowing that you have not solved every '
                 'mystery. You have insisted that a serious decision requires more than confidence, pressure or prejudice.',
    'end-doubt-say': 'What is the difference between “not proven guilty” and “proven innocent”?',
    'end-open': 'The jurors remain divided. The foreman tells the court they have not reached agreement. '
                'This is an unresolved outcome, not a victory or a defeat.',
    'end-open-say': 'What would you need to reconsider your position? Use “I would reconsider if …”.',
    'end-haste': 'You agree to a guilty verdict for the sake of leaving. Your choice ends the discussion, '
                 'but it does not answer the doubts. Nobody in the room can say whether the decision is right.',
    'end-haste-say': 'Complete: “We should not have … because …”. Then revisit your vote.',
}

# ── the questions. (node, eyebrow, title, story, stem, [key, wrong, wrong], why, picture[, say]) ──
Q = [
    ('q04', 'Act I · the first vote', 'Eleven hands rise.',
     'Eleven votes for guilty. Your hand stays down. Juror 3 leans in: “Are you saying you know he is innocent?”',
     'Which reply expresses uncertainty accurately?',
     ['I don’t know. I think we should examine the evidence.',
      'He must be innocent. I can feel it, so we don’t need evidence.',
      'He can’t be guilty, because he looks far too nervous.'],
     'I DON’T KNOW admits uncertainty; SHOULD proposes a next step. MUST and CAN’T claim a certainty that a feeling can’t give.',
     'hands', 'Say one reason a confident person might still be wrong.'),
    ('q05', 'Act I · disagreeing politely', 'Hold your ground.',
     'Juror 3 calls the case obvious. The room waits for your reply. You need a question that keeps the discussion open.',
     'Which reply challenges the claim respectfully?',
     ['I see your point, but how can we be sure?',
      'You clearly haven’t thought about any of this.',
      'I agree, so there’s nothing left to discuss.'],
     'I SEE YOUR POINT, BUT … grants the point before the challenge, so you disagree without attacking. '
     'A question keeps the discussion open.',
     'ground'),

    ('q07', 'File A · the knife', 'An unusual object.',
     'The prosecution links an unusual knife to the defendant. But a link is not the same as proof that he used it.',
     'The knife ___ to him, but we cannot be certain.',
     ['might have belonged', 'must have belong', 'might belonged'],
     'A possibility in the past: MIGHT HAVE + past participle, “might have belonged”. MUST HAVE claims '
     'certainty, and after HAVE the verb is always the past participle.',
     'knife'),
    ('q08', 'File A · testing a claim', 'A second knife.',
     'You place a second knife on the table. It is the same model. The claim that this design is unique can no longer stand.',
     'Which sentence draws a strong negative deduction about the past?',
     ['The design can’t have been unique.', 'The design might have unique.', 'The design can’t has been unique.'],
     'A strong negative deduction about the past: CAN’T HAVE BEEN. After a modal, HAVE never becomes HAS. '
     'A second knife disproves “unique”, not the whole accusation.',
     'twoknives'),
    ('q09', 'File A · limiting your claim', 'What does that prove?',
     'Juror 4 examines both knives. “So another person could have owned one. What follows from that?”',
     'Choose the most careful conclusion.',
     ['It weakens one claim; it doesn’t identify the killer.',
      'This proves that somebody else committed the crime.',
      'Every part of the prosecution’s case is false now.'],
     'WEAKENS keeps the conclusion inside what the evidence supports. PROVES and EVERY PART turn one doubt '
     'into a claim that everything is false.',
     'juror4'),
    ('q10', 'File A · even if', 'Concede. Then challenge.',
     'Juror 3 insists that the defendant bought a similar knife. Accept that point for the sake of argument, '
     'then question the conclusion.',
     '___ he owned one, that does not prove he used it.',
     ['Even if', 'Despite of', 'In spite'],
     'EVEN IF + clause accepts the point, not the conclusion. DESPITE never takes “of”; IN SPITE needs OF.',
     'concede', 'Make another “Even if …” argument about the case.'),
    ('q11', 'File A · evidence checkpoint', 'File the first doubt.',
     'Write one sentence for the jury’s evidence file. It must tell a reasonable doubt apart from a claim of innocence.',
     'Which note belongs in the file?',
     ['The knife’s design does not uniquely link it to the defendant.',
      'A second knife proves that the defendant was somewhere else that night.',
      'Anyone who owns a knife like this one must be guilty of the crime.'],
     'File A is complete. The note challenges one claim, that the knife was unique, and stays inside the '
     'evidence. PROVES and MUST claim far more.',
     'filea'),

    ('q12', 'File B · what could he hear?', 'A voice beneath a train.',
     'The downstairs witness says he heard a threat. An elevated train was passing at the time. Its noise '
     'matters, but you have not measured it.',
     'Which sentence questions the testimony without overstating certainty?',
     ['The noise might have made the words difficult to hear.',
      'He definitely heard nothing at all, not a single word.',
      'The train proves that he invented the whole story.'],
     'MIGHT HAVE MADE offers a possible obstacle. It doesn’t call the witness a liar, and it doesn’t claim '
     'the words were impossible to hear.',
     'train'),
    ('q13', 'File B · reported speech', 'What the witness said.',
     'In court, the witness said: “I heard the argument.” Now you report his statement to the jury, with the usual backshift.',
     'Choose the correctly backshifted report.',
     ['He said that he had heard the argument.', 'He told that he had heard the argument.',
      'He said us he has heard the argument.'],
     'Backshift: HEARD becomes HAD HEARD. SAY something, but TELL someone something: “He told us that he '
     'had heard …” also works.',
     'oldman'),
    ('q14', 'File B · putting events in order', 'The length of a hallway.',
     'The witness walked slowly with a limp. First the person on the stairs disappeared; then the witness '
     'reached his doorway.',
     'By the time he reached the door, the person ___.',
     ['had already disappeared', 'has already disappeared', 'had already disappear'],
     'The earlier of two past events takes the past perfect, HAD + past participle: “had disappeared”. '
     'The later one, “reached”, is past simple.',
     'hallway'),
    ('q15', 'File B · the unreal past', 'Test the timing.',
     'In your reconstruction, the walk takes longer than the witness’s estimate. It is a reconstruction, '
     'not an exact measurement.',
     'If he had moved that slowly, he ___ the door in time.',
     ['couldn’t have reached', 'couldn’t have reach', 'couldn’t had reached'],
     'IF + HAD + past participle pairs with COULDN’T HAVE + past participle for an unreal past. After '
     'HAVE, always the past participle: “reached”.',
     'stopwatch'),
    ('q16', 'File B · evidence checkpoint', 'Mistaken is not dishonest.',
     'Juror 9 reminds the room that wanting to be helpful does not make someone’s memory perfect. Record the '
     'strongest doubt you can defend.',
     'Choose a careful statement about the witness.',
     ['He may have misjudged the timing without intending to deceive us.',
      'An elderly witness like him is always unreliable, whatever he says.',
      'He must have lied to the court, because our timing was so different.'],
     'File B is complete. MAY HAVE MISJUDGED allows an honest mistake. MUST HAVE LIED claims a deliberate '
     'lie, and ALWAYS turns one witness into everyone.',
     'juror9'),

    ('q17', 'File C · a claim of sight', 'Across the tracks.',
     'A woman says she saw the attack from her apartment across the railway tracks. Report her claim '
     'without presenting it as a fact.',
     'She claims ___ the attack.',
     ['to have seen', 'to have saw', 'having saw'],
     'CLAIM + TO HAVE + past participle reports a claim about an earlier event. The past participle of '
     '“see” is “seen”, not “saw”.',
     'tracks'),
    ('q18', 'File C · possibility, not proof', 'A moving obstruction.',
     'A passing train lay between the two buildings. You can question the view without claiming that every '
     'glimpse was impossible.',
     'Choose the accurate past-possibility form.',
     ['The train could have blocked her view.', 'The train could has blocked her view.',
      'The train could have block her view.'],
     'COULD HAVE + past participle: a past possibility. After a modal, HAVE never becomes HAS, and the verb '
     'is the past participle, “blocked”.',
     'sightline'),
    ('q19', 'File C · a small observation', 'The marks of spectacles.',
     'Juror 9 remembers marks on the woman’s nose, like those left by spectacles. Nobody knows whether she '
     'wore glasses when she looked out of bed.',
     'Which sentence avoids turning an inference into certainty?',
     ['She may not have been wearing her glasses at the time.',
      'Those marks on her nose prove that she could never see anything.',
      'She was definitely wearing her glasses in bed.'],
     'MAY NOT HAVE BEEN + -ING: a possible ongoing state in the past. The marks raise a question without '
     'answering it, so PROVE and DEFINITELY go too far.',
     'spectacles'),
    ('q20', 'File C · although', 'Confidence and accuracy.',
     'The witness sounded certain. Acknowledge her confidence, and question whether confidence guarantees accuracy.',
     '___ she sounded certain, she could still have been mistaken.',
     ['Although', 'Despite', 'Despite of'],
     'ALTHOUGH takes a clause, “she sounded certain”. DESPITE takes a noun or -ING, “despite sounding '
     'certain”, and never takes OF.',
     'window'),
    ('q21', 'File C · evidence checkpoint', 'File the final doubt.',
     'The distance, the passing train and the missing glasses all deserve consideration. Make a conditional '
     'statement, not an accusation.',
     'If she hadn’t been wearing her glasses, she ___ him clearly.',
     ['might not have seen', 'might not saw', 'might not has seen'],
     'File C is complete. MIGHT NOT HAVE + past participle: a possible result of an unreal past condition. '
     'You don’t claim to know what she saw.',
     'filec'),

    ('q23', 'Act III · making a proposal', 'A private change of mind.',
     'Some jurors worry about looking weak if they change their vote. You propose a secret ballot to reduce the pressure.',
     'I’d rather we ___ in secret this time.',
     ['voted', 'to vote', 'voting'],
     'WOULD RATHER + a new subject + past simple, for a present or future preference: “I’d rather we voted”. '
     'The past form doesn’t mean past time here.',
     'ballots'),
    ('q24', 'Act III · listening for meaning', 'The first ally.',
     'Juror 9 supports continuing the discussion. He does not claim the defendant is innocent; he respects '
     'the courage it takes to stand alone.',
     'Which sentence paraphrases his position accurately?',
     ['He believes the doubts deserve a fair hearing.', 'He knows the defendant did nothing wrong.',
      'He agrees because all the other jurors agree.'],
     'DESERVE A FAIR HEARING means the doubts should be listened to seriously. It doesn’t mean he knows the '
     'young man is innocent.',
     'ally'),
    ('q25', 'Act III · challenging a motive', 'A ticket is not an argument.',
     'Juror 7 checks his watch. He will vote either way if it gets him out of the room. Challenge the reason, '
     'not his intelligence.',
     'Which reply keeps the verdict connected to the evidence?',
     ['Your vote should depend on the evidence, not your evening plans.',
      'Any quick decision is better than another hour of this discussion.',
      'You must agree with me, because I have stayed in this room longer.'],
     'DEPEND ON names the right basis for a vote. You challenge his reason, not his intelligence.',
     'ticket'),
    ('q26', 'Act III · challenging a generalisation', 'When prejudice speaks.',
     'Juror 10 makes a sweeping claim about people from the defendant’s neighbourhood. The room goes still. '
     'Bring the discussion back to this person and this case.',
     'Which reply challenges the faulty reasoning directly?',
     ['That’s a generalisation, not evidence about this defendant.',
      'We should vote against him because you sound so certain.',
      'Everyone from your neighbourhood is wrong about everything too.'],
     'Name the reasoning error, then return to the evidence. Answering one stereotype with another repeats '
     'the same mistake.',
     'prejudice'),

    ('q28', 'Act IV · the listening route', 'Make room for a voice.',
     'You turn towards the quieter juror. He begins, but Juror 3 cuts across him. Ask the room to listen before judging.',
     'Could we ___ before responding?',
     ['hear him out', 'listen him out', 'hear out him'],
     'HEAR SOMEONE OUT: listen until they finish. A pronoun goes between the two words: “hear him out”, '
     'never “hear out him”.',
     'listen'),
    ('q29', 'Act IV · the direct route', 'Lower the temperature.',
     'Your interruption stops the argument, but the room is tense. Make calm a condition for making progress.',
     'We won’t make progress ___ we let each other finish.',
     ['unless', 'despite', 'even'],
     'UNLESS means IF … NOT: we won’t make progress if we don’t let each other finish. It states the condition.',
     'calm'),
    ('q30', 'Act IV · despite + noun', 'Rain against the window.',
     'Rain cools the city, but the discussion stays heated. The foreman turns on the fan and asks everyone to continue.',
     '___ the tension, the jury kept discussing the evidence.',
     ['Despite', 'Although', 'Even though'],
     'DESPITE + noun: “despite the tension”. ALTHOUGH and EVEN THOUGH need a clause: “although the room was tense”.',
     'fan'),
    ('q31', 'Act IV · explaining an alternative', 'A memory under pressure.',
     'The defendant struggled to recall details of his evening at the cinema. Juror 4 treats that as '
     'suspicious. Offer another explanation.',
     'Which explanation is cautious and relevant?',
     ['Stress may have affected his ability to remember details.',
      'Only guilty people forget the details of an evening like that.',
      'Forgetting a title proves his entire story was true.'],
     'A memory gap has more than one explanation. MAY HAVE AFFECTED offers one without claiming it is proved.',
     'cinema'),
    ('q32', 'Act IV · reporting a decision', 'Changing a vote.',
     'One juror says: “I will reconsider my vote.” Later, you report this promise to the foreman, with the usual backshift.',
     'Choose the correct report.',
     ['He said he would reconsider his vote.', 'He said he will reconsider my vote.',
      'He told he would reconsider his vote.'],
     'Backshift: WILL becomes WOULD, and MY becomes HIS, because you report another person’s words. TELL '
     'needs a person: “He told us …”.',
     'ballot'),
    ('q33', 'Act V · evidence and emotion', 'The last resistance.',
     'Juror 3 is increasingly isolated. He speaks about ungrateful sons, then falls silent. His anger may '
     'come from somewhere beyond this case.',
     'Which question combines empathy with a return to the evidence?',
     ['Could your own experience be influencing how you see this case?',
      'Why are you always so unreasonable with everyone in this room?',
      'If you are this upset, then everything you say must be false.'],
     'COULD … BE INFLUENCING raises a possibility instead of making an accusation. Strong feeling doesn’t '
     'make a claim false.',
     'isolated'),
    ('q35', 'Act V · claim, reason, limit', 'Make the final argument.',
     'The foreman asks you to summarise. Connect the evidence to your conclusion, and make clear what you still do not know.',
     'Which summary is the most defensible?',
     ['These weaknesses leave reasonable doubt; they don’t prove what happened.',
      'He looks innocent to me, and by now most of you in this room agree with me.',
      'Every single witness lied to the court, so now I know exactly what happened.'],
     'A strong argument states its limit. The jury decides whether guilt has been proved, not what really happened.',
     'summary'),
]

# where each question leads
ORDER = ['q04', 'q05', 'evidence',
         'q07', 'q08', 'q09', 'q10', 'q11', 'evidence',
         'q12', 'q13', 'q14', 'q15', 'q16', 'evidence',
         'q17', 'q18', 'q19', 'q20', 'q21', 'evidence',
         'shift', 'q23', 'q24', 'q25', 'q26', 'quiet',
         'q28', 'q30', 'q29', 'q30', 'q31', 'q32', 'q33', 'photograph', 'q35', 'verdict']
NEXT = {a: b for a, b in zip(ORDER, ORDER[1:]) if a.startswith('q')}
FILES = {'q11': 'fileA', 'q16': 'fileB', 'q21': 'fileC'}   # a checkpoint closes its file
SECTIONS = [['q04', 'q05'], ['q07', 'q08', 'q09', 'q10', 'q11'], ['q12', 'q13', 'q14', 'q15', 'q16'],
            ['q17', 'q18', 'q19', 'q20', 'q21'], ['q23', 'q24', 'q25', 'q26'], ['q28'], ['q29'],
            ['q30', 'q31', 'q32', 'q33'], ['q35']]
GOLD = 'time>=1'
SLOTS = [1, 2, 0, 2, 0, 1, 0, 1, 2]


def bg(pic):
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


def section(node, kind, act, body, pic=None, extra=''):
    return ('\n    <section class="slide" data-type="%s" data-node="%s" data-act="%s"%s%s>\n%s'
            '    </section>\n' % (kind, node, act, bg(pic) if pic else '', extra, body))


def gl(key, cls='prose'):
    return '<p class="%s gloss" data-tr="%s">%s</p>' % (cls, key, N[key])


def teach(node, act, eyebrow, title, inner, to, pic, extra='', ek=None, tk=None):
    body = (head(eyebrow, title, ek, tk) +
            '      <div class="slide-body" style="position:relative">\n        %s\n' % inner +
            (cont(to) if to else '') + '      </div>\n')
    return section(node, 'teach', act, body, pic, extra)


def say(key):
    """A speaking prompt under a story card: glossed, dim, marked as speech."""
    return gl(key, 'prose dim').replace('<p class="prose dim', '<p style="margin-top:12px" class="prose dim', 1)


def mc(q):
    node, eyebrow, title, story, stem, opts, why, pic = q[:8]
    speak = q[8] if len(q) > 8 else None
    key = opts[0]
    nxt = NEXT[node]
    clue = ' data-clue="%s"' % FILES[node] if node in FILES else ''
    sec = next(s for s in SECTIONS if node in s)
    n = sec.index(node) + 1
    # The engine shuffles, but check-lesson's KEYS gate reads the source, so
    # the key is dealt round the letters too: 1 2 0 2 0 1 …, never three alike.
    slot = SLOTS[[x[0] for x in Q].index(node) % len(SLOTS)]
    dealt = list(opts[1:])
    dealt.insert(slot, key)
    buttons = []
    for o in dealt:
        if o == key:
            buttons.append('<button class="opt" data-correct data-dp="1"%s data-goto="%s">%s</button>' % (clue, nxt, o))
        else:
            buttons.append('<button class="opt" data-time="-1"%s data-goto="%s">%s</button>' % (clue, nxt, o))
    N['q-' + node] = story
    if speak:
        why = '%s<br><strong>Say it aloud:</strong> %s' % (why, speak)
    count = ' · %d of %d' % (n, len(sec)) if len(sec) > 1 else ''
    body = (head(eyebrow + count, title) +
            '      <div class="slide-body">\n'
            '        <p class="q-ctx gloss" data-tr="q-%s" style="margin-bottom:10px">%s</p>\n' % (node, story) +
            '        <p class="q-stem">%s</p>\n' % stem +
            '        <div class="opts">\n          %s\n        </div>\n' % '\n          '.join(buttons) +
            # Continue sits beside the feedback, not under it: with the gloss open
            # and a two-line explanation, a button underneath met the deck bar.
            '        <div style="display:flex;gap:16px;align-items:flex-start">\n'
            '          <p class="feedback" style="flex:1" data-explain="%s"></p>\n' % D.esc(why) +
            '          <button class="btn btn-solid" style="flex:none;margin-top:10px" data-action="branch-continue" '
            'data-i18n="btnContinue" hidden>%s</button>\n'
            '        </div>\n      </div>\n' % E['btnContinue'])
    return section(node, 'mc', eyebrow.split(' · ')[0], body, pic)


def choices(rows, cols=''):
    """Choice cards: (label key, body key or None, goto, require)."""
    out = '        <div class="cols%s">\n' % cols
    for k, bk, to, req in rows:
        out += ('          <div class="card">\n'
                '            <p class="prose"><strong data-i18n="%s">%s</strong>%s</p>\n'
                '            <div style="margin-top:12px"><button class="btn btn-solid choice" data-goto="%s"%s '
                'data-i18n="btnChoose">%s</button></div>\n'
                '          </div>\n' % (k, E[k], '<br><span data-i18n="%s">%s</span>' % (bk, E[bk]) if bk else '',
                                       to, ' data-require="%s"' % req if req else '', E['btnChoose']))
    return out + '        </div>\n'


def build_slides():
    logo = D.logo_from(TPL)
    by = {q[0]: q for q in Q}

    def m(node):
        return mc(by[node])

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
                  '        </div>\n'
                  '        <p class="prose dim" style="margin-top:14px;text-align:center" data-i18n="howAloud">%s</p>\n'
                  % E['howAloud'] + cont('brief') + '      </div>\n', 'jurors')

    brief = teach('brief', E['actBefore'], E['briefEyebrow'], E['briefTitle'],
                  '<div class="card">%s</div>' % gl('brief'), 'cast', 'door', ek='briefEyebrow', tk='briefTitle')

    cast = section('cast', 'teach', E['actBefore'],
                   head(E['castEyebrow'], E['castTitle'], 'castEyebrow', 'castTitle') +
                   '      <div class="slide-body">\n        <div class="cols" style="grid-template-columns:repeat(4,1fr);gap:10px">\n' +
                   ''.join('          <div class="card" style="padding:10px 14px"><p class="prose" style="font-size:16px">'
                           '<strong>%02d · <span data-i18n="cast%d">%s</span></strong><br>'
                           '<span class="dim" data-i18n="cast%dBody">%s</span></p></div>\n'
                           % (i, i, E['cast%d' % i], i, E['cast%dBody' % i]) for i in range(1, 13)) +
                   '        </div>\n' + cont('toolkit') + '      </div>\n', 'cafe')

    toolkit = teach('toolkit', E['actBefore'], E['labEyebrow'], E['labTitle'],
                    '<p class="prose gloss" data-tr="toolkit" style="margin-bottom:12px">%s</p>' % N['toolkit'] +
                    '<div class="cols cols-3">%s</div>' % ''.join(
                        '<div class="card" style="padding:12px 16px"><p class="prose" style="font-size:17px">'
                        '<strong style="font-size:13px;letter-spacing:.04em">%s</strong><br>%s<br>'
                        '<span class="dim" data-i18n="lab%d">%s</span></p></div>'
                        % (h, ex, i, E['lab%d' % i]) for i, (h, ex) in enumerate(LAB, 1)),
                    'q04', 'toolkit', ek='labEyebrow', tk='labTitle')

    evidence = teach('evidence', 'Act II', E['hubEyebrow'], E['hubTitle'],
                     gl('evidence') + '\n' +
                     choices([('fileA', 'fileABody', 'q07', None), ('fileB', 'fileBBody', 'q12', None),
                              ('fileC', 'fileCBody', 'q17', None)], ' cols-3') +
                     '        <div style="margin-top:16px;display:flex;gap:14px;align-items:center">\n'
                     '          <button class="btn btn-solid" data-goto="shift" data-require="clues>=3" '
                     'data-i18n="btnReconvene">%s</button>\n'
                     '          <span class="prose dim" data-i18n="hubNote">%s</span>\n'
                     '        </div>\n' % (E['btnReconvene'], E['hubNote']),
                     None, 'evidence', ek='hubEyebrow', tk='hubTitle')

    shift = teach('shift', 'Act III', E['shiftEyebrow'], E['shiftTitle'],
                  '<div class="card">%s%s</div>' % (gl('shift'), say('shift-say')), 'q23', 'shift',
                  ek='shiftEyebrow', tk='shiftTitle')

    quiet = teach('quiet', 'Act IV', E['forkEyebrow'], E['forkTitle'],
                  gl('quiet') + '\n' +
                  choices([('routeListen', None, 'q28', None), ('routeCalm', None, 'q29', None)]) +
                  '        <p class="prose dim" style="margin-top:14px;text-align:center" '
                  'data-i18n="explainFirst">%s</p>\n' % E['explainFirst'],
                  None, 'quiet', ek='forkEyebrow', tk='forkTitle')

    photograph = teach('photograph', 'Act V', E['photoEyebrow'], E['photoTitle'],
                       '<div class="card">%s%s</div>' % (gl('photograph'), say('photograph-say')), 'q35',
                       'photograph', ek='photoEyebrow', tk='photoTitle')

    verdict = teach('verdict', 'Verdict', E['verdictEyebrow'], E['verdictTitle'],
                    gl('verdict') + '\n' +
                    choices([('voteDoubt', 'voteDoubtBody', 'end-doubt', GOLD),
                             ('voteOpen', 'voteOpenBody', 'end-open', None),
                             ('voteHaste', 'voteHasteBody', 'end-haste', None)], ' cols-3') +
                    '        <p class="prose dim" style="margin-top:14px;text-align:center" '
                    'data-i18n="verdictNote">%s</p>\n' % E['verdictNote'],
                    None, 'verdict', ek='verdictEyebrow', tk='verdictTitle')

    def ending(k, pic, revisit):
        K = k.capitalize()
        inner = '<div class="card">%s%s</div>' % (gl('end-' + k), say('end-%s-say' % k))
        body = (head(E['end' + K], E['end%sTitle' % K], 'end' + K, 'end%sTitle' % K) +
                '      <div class="slide-body" style="position:relative">\n        %s\n' % inner +
                '        <div style="margin-top:18px;display:flex;gap:10px">\n'
                '          <button class="btn btn-solid" data-goto="results" data-i18n="btnContinue">%s</button>\n'
                % E['btnContinue'] +
                ('          <button class="btn" data-goto="verdict" data-i18n="btnRevisit">%s</button>\n'
                 % E['btnRevisit'] if revisit else '') +
                '        </div>\n      </div>\n')
        return section('end-' + k, 'teach', 'Ending', body, pic)

    results = D.results(next_key='resRoute', next_text=E['resRoute'], folder=F, bg='hero.jpg')
    results = results.replace('data-type="results"', 'data-type="results" data-node="results" data-act="Verdict"', 1)
    i = results.rindex('      </div>\n    </section>')
    results = results[:i] + cont('activate', 'resNext') + results[i:]

    act = D.activate(E['actTitle'], E['actUse'], CHIPS, 'Speaking', E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder'],
                     folder=F, bg='cafe.jpg')
    act = act.replace('data-type="activate"', 'data-type="activate" data-node="activate" data-act="Activation"', 1)
    act = act.replace('data-action="restart"', 'data-action="restart" data-goto="how"', 1)

    return ''.join([
        cover, how, brief, cast, toolkit,
        m('q04'), m('q05'), evidence,
        m('q07'), m('q08'), m('q09'), m('q10'), m('q11'),
        m('q12'), m('q13'), m('q14'), m('q15'), m('q16'),
        m('q17'), m('q18'), m('q19'), m('q20'), m('q21'),
        shift, m('q23'), m('q24'), m('q25'), m('q26'),
        quiet, m('q28'), m('q29'),
        m('q30'), m('q31'), m('q32'), m('q33'), photograph, m('q35'),
        verdict,
        ending('doubt', 'handshake', False), ending('open', 'divided', True), ending('haste', 'emptychair', True),
        results, act,
    ])


# headword (English, never translated) and example; the meaning is lab<n> in T
LAB = [
    ('MIGHT / MAY / COULD HAVE + PP', 'He might have been mistaken.'),
    ('CAN’T HAVE + PP', 'The design can’t have been unique.'),
    ('EVEN IF / ALTHOUGH + CLAUSE · DESPITE + NOUN', 'Even if he owned one, it proves nothing.'),
    ('IF + HAD + PP, COULD(N’T) HAVE + PP', 'If he had left earlier, he could have arrived in time.'),
    ('SAID (THAT) + BACKSHIFT', '“I heard it.” → He said he had heard it.'),
    ('I’D RATHER WE + PAST · UNLESS', 'I’d rather we voted in secret.'),
]

CHIPS = ['might have', 'can’t have', 'could have', 'even if', 'although', 'despite',
         'he said that he had', 'unless', 'I see your point, but']

# every route: the three files in any order, either arm of the fork
FILE_RUNS = [['q07', 'q08', 'q09', 'q10', 'q11'], ['q12', 'q13', 'q14', 'q15', 'q16'],
             ['q17', 'q18', 'q19', 'q20', 'q21']]
PATHS = [['q04', 'q05'] + sum(order, []) + ['q23', 'q24', 'q25', 'q26', arm, 'q30', 'q31', 'q32', 'q33', 'q35']
         for order in itertools.permutations(FILE_RUNS) for arm in ('q28', 'q29')]


def gates(slides):
    """The checks a branching deck needs that check-lesson.js does not make."""
    D.assert_no_key_is_longest([dict(options=q[5], correct=0) for q in Q], 'MC')
    nodes = re.findall(r'data-node="([^"]+)"', slides)
    assert len(nodes) == len(set(nodes)), 'duplicate node'
    gotos = set(re.findall(r'data-goto="([^"]+)"', slides))
    missing = gotos - set(nodes)
    assert not missing, 'data-goto to no node: %s' % missing
    orphans = set(nodes) - gotos - {'cover'}
    assert not orphans, 'orphan nodes: %s' % orphans
    for p in PATHS:
        assert len(p) == 27, ('questions on a path', len(p))
    # each file's last question is the only one carrying its clue, on every option
    for node, clue in FILES.items():
        sec = re.search(r'data-node="%s".*?</section>' % node, slides, re.S).group(0)
        assert sec.count('data-clue="%s"' % clue) == 3, node
    assert slides.count('data-clue=') == 9
    # no two linked slides share a picture, and every plate is used once
    pic = dict(re.findall(r'data-node="([^"]+)"[^>]*?data-bg="([^"]+)"', slides))
    secs = re.findall(r'data-node="([^"]+)"(.*?)</section>', slides, flags=re.S)
    for node, body in secs:
        for to in set(re.findall(r'data-goto="([^"]+)"', body)):
            if node in pic and to in pic and pic[node] == pic[to]:
                raise AssertionError('%s and %s are neighbours on one picture (%s)' % (node, to, pic[node]))
    for p in set(re.findall(r'data-bg="([^"]+)"', slides)) | {F + '/hero.jpg'}:
        assert os.path.exists(p), 'missing plate %s' % p
    for k in N:
        assert '’' not in k


def narrative_tr(langs):
    out = {}
    for c in langs[1:]:
        mod = importlib.import_module('i18n_reasonable_doubt_%s' % c)
        nk = set(N) - set(mod.N)
        assert not nk, '%s glosses missing: %s' % (c, sorted(nk))
        extra = set(mod.N) - set(N)
        assert not extra, '%s glosses for nothing: %s' % (c, sorted(extra))
        out[c] = mod.N
    return 'const NARRATIVE_TR = ' + json.dumps(out, ensure_ascii=False, indent=1) + ';\n'


def build():
    slides = build_slides()
    gates(slides)
    n = slides.count('<section class="slide')
    langs = tuple(c for c in I.LANGS if c in I.T)
    s = D.assemble(TPL, OUT, slides, PALETTE, TITLE, I, langs=langs)
    s = s.replace('<body>', '<body data-flow="branch" data-start="cover" data-time="%d">' % PATIENCE, 1)
    s = s.replace('const UI_I18N = {', narrative_tr(langs) + 'const UI_I18N = {', 1)
    open(OUT, 'w', encoding='utf-8', newline='').write(s)
    print('wrote %s — %d slides, %s' % (OUT, n, ','.join(langs)))


if __name__ == '__main__':
    build()
