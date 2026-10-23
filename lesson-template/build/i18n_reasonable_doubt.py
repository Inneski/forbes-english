# -*- coding: utf-8 -*-
"""Interface strings for Reasonable Doubt (B2–C1). See build_reasonable_doubt.py.

English, German and Spanish. The narrative glosses (the Translate button)
live in N in the DE and ES modules, taken from the ChatGPT export where the
English is unchanged and written in-session where it is not; no native
check. This file is the chrome: cover, rules, cast, toolkit meanings, the
evidence table, the fork, the verdict, the endings' labels, activation.
NOT translated, deliberately (HOUSE-STYLE §8): the question stems, every
option, the toolkit's headwords and examples, the activation chips.
Grammar tokens in CAPS.
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
    coverTitle='Reasonable <em>Doubt</em>',
    coverSub='Twelve voices. One room. Eleven are ready to convict, and you are not convinced.',
    chipLevel='B2–C1 · Upper intermediate', chipFocus='Past modals · concession · reported speech',
    chipCount='75–100 minutes',
    btnContinue='Continue →', btnChoose='Choose this', btnReconvene='Reconvene the jury →',
    btnRevisit='Revisit your vote',
    actBefore='Before you begin',

    howEyebrow='How the deliberation works',
    howTitle='Every word you say has a price.',
    howDp='Points', howDpBody='A careful answer earns <strong>+1 point</strong>.',
    howTime='Patience',
    howTimeBody='The room starts with five. A careless answer costs one. At zero, nobody will follow your vote.',
    howClues='Files',
    howCluesBody='Three pieces of evidence, in any order. The jury reconvenes when all three are closed.',
    howAloud='Read each scene aloud and explain your choice in English before you click.',
    ledDp='Points', ledTime='Patience', ledClues='Files',

    briefEyebrow='Prologue · your role', briefTitle='You are Juror 8.',
    castEyebrow='Before the first vote · the room', castTitle='Meet the twelve jurors.',
    cast1='The foreman', cast1Body='Keeps the discussion moving.',
    cast2='The hesitant voice', cast2Body='Needs space to contribute.',
    cast3='The forceful dissenter', cast3Body='Carries a personal grievance.',
    cast4='The analytical juror', cast4Body='Trusts orderly evidence.',
    cast5='The experienced observer', cast5Body='Questions easy assumptions.',
    cast6='The fair listener', cast6Body='Protects respectful treatment.',
    cast7='The impatient juror', cast7Body='Wants to leave.',
    cast8='You', cast8Body='Ask what can really be known.',
    cast9='The older ally', cast9Body='Notices people and small details.',
    cast10='The prejudiced voice', cast10Body='Confuses stereotypes with evidence.',
    cast11='The principled juror', cast11Body='Takes the responsibility seriously.',
    cast12='The wavering juror', cast12Body='Can be influenced by the room.',

    labEyebrow='Before the first vote · your toolkit', labTitle='The language of doubt.',
    lab1='A possibility in the past.', lab2='A strong negative deduction.',
    lab3='Concede a point, then challenge it.', lab4='An unreal past condition.',
    lab5='Report what someone said.', lab6='Propose, or set a condition.',

    hubEyebrow='Act II · the evidence table', hubTitle='Where does doubt begin?',
    fileA='File A · the knife', fileABody='The unusual knife.',
    fileB='File B · the man downstairs', fileBBody='What could he hear?',
    fileC='File C · across the tracks', fileCBody='What could she see?',
    hubNote='Opens when all three files are closed.',

    shiftEyebrow='Act III · doubt is spreading', shiftTitle='The room begins to shift.',
    forkEyebrow='Act IV · a choice of approach', forkTitle='How will you lead?',
    routeListen='Invite the quieter juror to speak', routeCalm='Interrupt the confrontation',
    explainFirst='Explain your choice in English before you click.',
    photoEyebrow='Act V · a moment to listen', photoTitle='A photograph on the table.',

    verdictEyebrow='The verdict', verdictTitle='Your final vote.',
    voteDoubt='Not guilty', voteDoubtBody='The evidence leaves reasonable doubt.',
    voteOpen='More discussion', voteOpenBody='You cannot agree yet.',
    voteHaste='Guilty', voteHasteBody='Simply to end the discussion.',
    verdictNote='A room that has lost its patience will not follow you to not guilty.',
    branchLocked='The room has stopped listening to you',
    endDoubt='Ending I · the reasoned verdict', endDoubtTitle='A doubt worth defending.',
    endOpen='Ending II · the unresolved room', endOpenTitle='The discussion continues.',
    endHaste='Ending III · the abandoned argument', endHasteTitle='The cost of hurrying.',
    resRoute='Scored only on the questions your route actually met.',

    glossShow='Translate', glossHide='Hide translation',
    resPerfect='Flawless. Every word was careful.',
    resStrong='Strong work. Most of your arguments held.',
    resMid='A fair case, with gaps the room noticed.',
    resLow='The doubt was right. The wording was not.',

    actTitle='Now argue it yourself.',
    actUse='Use at least three of these',
    actSpeakBrief='In pairs or threes. Claim, reason, and an honest limit.',
    actSpeak1='Change roles: one of you defends the reliability of a witness, the other questions it. '
              'Ninety seconds each, then swap.',
    actSpeak2='Give a 60-second closing statement to the jury: two pieces of evidence, one concession, '
              'and what you still do not know.',
    actSpeak3='Think of something you are sure about. What would make you reconsider? '
              'Begin: “I would reconsider if …”.',
    actWriteKind='Writing · 150–250 words',
    actWriteBrief='Write the foreman’s note to the judge explaining the verdict. Concede one point against '
                  'the defendant, explain two doubts, and say what the jury still does not know.',
    actPlaceholder='Your Honour, …',
)

for _c in LANGS[1:]:
    try:
        T[_c] = importlib.import_module('i18n_reasonable_doubt_%s' % _c).T
    except ImportError:
        pass


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    rows = ['    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
            for k in sorted(d)]
    return '{\n' + ',\n'.join(rows) + '\n  }'
