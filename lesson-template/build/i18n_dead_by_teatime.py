# -*- coding: utf-8 -*-
"""Interface strings for Dead by Teatime (B1). See build_dead_by_teatime.py.

English, German and Spanish (the house minimum). This file is the English
chrome and the machinery; each other language's module carries T (its
chrome), N (the narrative glosses behind the Translate button) and QT (each
question slide's eyebrow, title, instruction and explanation).
NOT translated, deliberately (HOUSE-STYLE §8): gap stems, every option, the
toolkit's headwords and examples, the activation chips. Grammar tokens in CAPS.
"""
import importlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME  # noqa: E402

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount',
        'actSpeakWord', 'actWriteWord']

LANGS = ('en', 'de', 'es')

T = {}

T['en'] = dict(
    coverTitle='Dead by <em>Teatime</em>',
    coverSub='Monday in Lowfield. The neighbours are not well, and you have the only keys to the bowling alley.',
    chipLevel='B1 · Intermediate', chipFocus='Must · have to · should · relative clauses',
    chipCount='60–80 minutes',
    btnContinue='Continue →', btnChoose='Choose this', btnHead='Head for Lowfield Lanes →',
    btnRevisit='Change your mind',
    actBefore='Before you begin',

    howEyebrow='How the game works', howTitle='Keep your nerve.',
    howDp='Points', howDpBody='A correct answer earns <strong>+1 point</strong>.',
    howTime='Nerve',
    howTimeBody='You start with five. A wrong answer costs one. At zero, the group stops trusting your plans.',
    howClues='Stops',
    howCluesBody='Three stops before the bowling alley, in any order. Lowfield Lanes opens when all three are done.',
    howAloud='Read each scene aloud and explain your choice in English before you click.',
    ledDp='Points', ledTime='Nerve', ledClues='Stops',

    briefEyebrow='Prologue · Monday, 7:40 a.m.', briefTitle='Lowfield is not well.',
    castEyebrow='Before you leave · your people', castTitle='Who is who.',
    cast1='You', cast1Body='The one who has the keys to Lowfield Lanes.',
    cast2='Gaz', cast2Body='Your flatmate, who has never been awake before ten.',
    cast3='Nan', cast3Body='Your grandmother, whose cricket bat has a name.',
    cast4='Priya', cast4Body='The paramedic who still has your best hoodie.',
    cast5='Colin', cast5Body='Priya’s new boyfriend, who has read every survival manual.',
    cast6='Mr Bell', cast6Body='The man whose corner shop never closes.',

    labEyebrow1='Before you leave · your toolkit · 1 of 2', labTitle1='Rules and advice.',
    labEyebrow2='Before you leave · your toolkit · 2 of 2', labTitle2='Who, which, where, whose.',
    lab1='A rule, or something you feel is necessary. MUSTN’T: it is forbidden.',
    lab2='An obligation from outside: a rule, a timetable, the situation.',
    lab3='It isn’t necessary, so you can choose. Not the same as MUSTN’T.',
    lab4='Advice: a good idea, or a bad one.',
    lab5='People: WHO. Things: WHICH. Both: THAT.',
    lab6='A place where something happens: WHERE. Possession: WHOSE + noun.',
    lab7='The pronoun can go when a new subject follows it.',
    lab8='Extra information: between commas, and never THAT.',

    hubEyebrow='Act II · three stops', hubTitle='Who do you get first?',
    stopA='Stop A · Nan’s house', stopABody='Nan isn’t answering her phone.',
    stopB='Stop B · the ambulance station', stopBBody='Priya’s last message came from here.',
    stopC='Stop C · Bell’s corner shop', stopCBody='Supplies, and the only shop still open.',

    lanesEyebrow='Act III · Lowfield Lanes', lanesTitle='Eight lanes and a glass front.',
    sayLanes='Say it aloud: three rules for the bowling alley. One MUST, one MUSTN’T, one SHOULD.',
    forkEyebrow='Act IV · midnight', forkTitle='The lights go out.',
    routeBack='Restart the generator in the back yard', routeFront='Barricade the glass doors',
    explainFirst='Explain your choice in English before you click.',
    dawnEyebrow='Act V · morning', dawnTitle='Daylight.',
    sayDawn='Say it aloud: describe one person in the group in one sentence, with WHO or WHOSE.',

    decisionEyebrow='The decision', decisionTitle='How do you get out?',
    voteBus='Everyone on the bus', voteBusBody='Nan drives. Nobody argues.',
    voteWait='Wait for the army', voteWaitBody='Stay behind the barricade.',
    voteSolo='Run for it alone', voteSoloBody='You are faster on your own.',
    branchLocked='Nobody trusts your plans any more',
    endBus='Ending I · the slow getaway', endBusTitle='Nine miles an hour.',
    endWait='Ending II · the long wait', endWaitTitle='Behind the fridge.',
    endSolo='Ending III · on your own', endSoloTitle='Nobody to hold the door.',
    sayBus='Tell the story of the night in 60 seconds. Use one WHO, one WHERE and one WHOSE.',
    sayWait='Write three house rules for Thursday: one MUST, one MUSTN’T, one DON’T HAVE TO.',
    saySolo='What advice would you give yourself? Begin: “You shouldn’t …”. Then change your mind.',
    resRoute='Scored only on the questions your route actually met.',

    glossShow='Translate', glossHide='Hide translation',
    resPerfect='Flawless. Everyone made it out.',
    resStrong='Strong work. Only a few close calls.',
    resMid='You survived, with some near misses.',
    resLow='Alive, just. Read the toolkit again.',

    actTitle='Now plan your own survival.',
    actUse='Use at least three of these',
    actSpeakBrief='In pairs or threes. Agree on a plan, then explain it to the class.',
    actSpeak1='Your town has an emergency alert. Agree on five rules for your group: two with MUST or MUSTN’T, '
              'two with HAVE TO or DON’T HAVE TO, one with SHOULD.',
    actSpeak2='Choose your refuge: a place you know well. Describe it with WHERE, WHO and WHICH: the room where '
              'you would sleep, the person who would cook.',
    actSpeak3='Pick three people you know for your team. Describe each one in a sentence without the name: '
              '“the one whose …”, “the friend who …”. Your partner guesses.',
    actWriteKind='Writing · 120–180 words',
    actWriteBrief='Write the notice for the door of your refuge. Say who can come in, what people must and '
                  'mustn’t do, what they don’t have to worry about, and give one piece of advice. Use at least '
                  'two relative clauses.',
    actPlaceholder='WELCOME TO …',
)

# The deck bar's act label: data-act is English, these are its keys
ACTS = {'en': {'Before you begin': 'Before you begin', 'Act I': 'Act I', 'Act II': 'Act II', 'Stop A': 'Stop A',
               'Stop B': 'Stop B', 'Stop C': 'Stop C', 'Act III': 'Act III', 'Act IV': 'Act IV',
               'Act V': 'Act V', 'Ending': 'Ending', 'Activation': 'Activation'}}

# "1 of 4" on a question's eyebrow, per language
OF = {'en': '%d of %d'}

QT = {}

for _c in LANGS[1:]:
    try:
        _m = importlib.import_module('i18n_dead_by_teatime_%s' % _c)
    except ImportError:
        continue
    T[_c], QT[_c], ACTS[_c], OF[_c] = _m.T, _m.QT, _m.ACTS, _m.OF

for _code, _labels in ACTS.items():
    if _code in T:
        T[_code].update(('act' + re.sub('[^A-Za-z]', '', k), v) for k, v in _labels.items())


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    rows = ['    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
            for k in sorted(d)]
    return '{\n' + ',\n'.join(rows) + '\n  }'
