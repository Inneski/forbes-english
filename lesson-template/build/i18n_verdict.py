# -*- coding: utf-8 -*-
"""Interface strings for Anatomy of a Verdict (C1). See build_verdict.py.

English, German and Spanish (DE and ES written in-session, no native check).
The narrative glosses (the Translate button) live in N in the DE and ES
modules; this file is the chrome: cover, rules, ledger, decisions, endings'
labels, activation. NOT translated, deliberately (HOUSE-STYLE §8): the
question stems, every option, the lock sentences and the concession cards'
headwords and examples. Grammar tokens in CAPS.
"""
import importlib, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount',
        'actSpeakWord', 'actWriteWord']

LANGS = ('en', 'de', 'es')

T = {}

T['en'] = dict(
    coverTitle='Anatomy of a <em>Verdict</em>',
    coverSub='Eleven jurors say she pushed him. You are juror twelve, and you are not sure.',
    chipLevel='C1 · Advanced', chipFocus='Concession · the language of argument',
    chipCount='60–75 minutes',
    btnContinue='Continue →',
    actBefore='Before you begin',

    howEyebrow='How the deliberation works',
    howTitle='Every argument has a price.',
    howDp='Points', howDpBody='A correct argument earns <strong>+1 point</strong>.',
    howTime='Patience',
    howTimeBody='The room starts with four. A wrong argument costs one. At zero, nobody is listening.',
    howClues='Votes',
    howCluesBody='Four jurors can be turned. You need all four for the best verdict.',
    ledDp='Points', ledTime='Patience', ledClues='Votes',

    labEyebrow='Before you deliberate', labTitle='How to concede a point.',
    voteTurned='A vote turns', voteHeld='The vote holds',
    chooseA='Replay the recording', chooseB='Study the stairwell',
    chooseC='Question the witness', chooseD='Run the clock',
    explainFirst='Explain your choice in English before you click.',

    boardEyebrow='Your closing speech · speaking round', boardTitle='Make the case aloud.',
    lockEyebrow='The final argument', lockTitle='Complete both sentences.',

    ledgerEyebrow='The last ballot is in', ledgerTitle='Your ledger decides the verdict.',
    gold='Unanimous', goldBody='Every vote turned, and the room still listening.',
    silver='Majority', silverBody='Enough arguments held for a majority verdict.',
    shadow='No verdict', shadowBody='The room never settles.',
    ledgerNote='Endings you did not earn are locked.',
    branchLocked='Your ledger does not support this verdict',
    endGold='Unanimous verdict', endSilver='Majority verdict', endShadow='Hung jury',
    revealKick='What the evidence could prove',
    resRoute='Scored only on the questions your route actually met.',

    glossShow='Translate', glossHide='Hide translation',
    resPerfect='Flawless. Every argument held.',
    resStrong='Strong work. The room listened to you.',
    resMid='A fair case, with gaps a barrister would find.',
    resLow='The doubt was right. The arguments were not.',

    actTitle='Now argue it yourself.',
    actUse='Use at least three of these',
    actSpeakBrief='In pairs or threes. Concede first, then turn the point.',
    actSpeak1='You are Victor. Argue that Ruth is guilty. Your partner concedes each point, then turns it.',
    actSpeak2='You are Ruth’s barrister. Admit three facts against her, and show why none of them proves a push.',
    actSpeak3='Think of a time you changed your mind. Explain what you still believe, and what changed it.',
    actWriteKind='Writing · 150–250 words',
    actWriteBrief='Write the note the foreman sends the judge, explaining how the jury reached its verdict. '
                  'Concede three points against Ruth and turn each one.',
    actPlaceholder='Dear Judge …',
)

for _c in LANGS[1:]:
    try:
        T[_c] = importlib.import_module('i18n_verdict_%s' % _c).T
    except ImportError:
        pass


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    rows = ['    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
            for k in sorted(d)]
    return '{\n' + ',\n'.join(rows) + '\n  }'
