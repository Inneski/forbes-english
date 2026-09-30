# -*- coding: utf-8 -*-
"""Interface strings for Reddit × French Market: Getting in the Door (C1).

English, German and Spanish (DE and ES written in-session, no native
check). Every string the learner reads is keyed here, so a further
language is one module (i18n_redditdoor_<code>.py exporting T) plus the
code in LANGS.

NOT translated, deliberately (HOUSE-STYLE §8): the phrase on each teach
card (the headword), its example line, every question option, the gap
sentences, the order chunks, the match terms and the sort items — they are
the English being taught. Situations (ctx) and stems with no blank in them
translate, as deck.mc allows. Cited phrases are in double quotes.
"""
import importlib, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount',
        'actSpeakWord', 'actWriteWord',
        'resPerfect', 'resStrong', 'resMid', 'resLow']

LANGS = ('en', 'de', 'es')

T = {}

T['en'] = dict(
    coverTitle='Reddit &times; French Market: <em>Getting in the Door</em>',
    coverSub='Cold outreach, gatekeepers and the follow-up, at C-suite level',
    chipLevel='C1 · Advanced', chipFocus='Business English · prospecting',
    chipCount='37 slides',

    d1t='The Cold Approach', d1n='Part 1 · the first email',
    d2t='Past the Gatekeeper', d2n='Part 2 · the phone call',
    d3t='Reading the Room', d3n='Part 3 · the first meeting, French style',
    d4t='The Follow-up', d4n='Part 4 · chasing without pestering',

    e1='The cold approach', e2='Past the gatekeeper', e3='Reading the room',
    e4='The follow-up',

    p1t='Ninety seconds of a CMO’s attention',
    p1a='A cold email to the CMO of Galeries Morel gets ninety seconds, on a phone, '
        'between meetings. It needs a <strong>hook</strong> that names her world, one '
        'line of <strong>credibility</strong>, and a <strong>soft ask</strong> she can '
        'say yes to without committing to anything.',
    p1b='The register is warm but not familiar. You are not "reaching out"; you are '
        '"writing because". You are not "excited"; you have "a reason to think".',
    p2t='The chief of staff is not an obstacle',
    p2a='In a French house the <strong>directeur de cabinet</strong> or executive '
        'assistant decides what reaches the top. Treat them as the first decision-maker, '
        'not a door. The language is <strong>indirect</strong>: you were hoping, you '
        'wondered whether, you would be guided by them.',
    p2b='Direct questions ("Is she free on Tuesday?") sound like demands. Hedged ones '
        '("Might there be a window later in the month?") sound like respect.',
    p3t='Logic first, warmth second',
    p3a='French senior management wants the <strong>argument</strong> before the '
        'relationship: the premise, the reasoning, then the proposal. A "non" at the '
        'start is often a <strong>position</strong>, not a decision. Silence after your '
        'pitch is thinking, not rejection.',
    p3b='Formality holds longer than in Dublin or London: surnames, "vous", and a lunch '
        'that is part of the meeting, not a break from it.',
    p4t='Persistent, never pushy',
    p4a='Most first approaches are answered by <strong>silence</strong>. The follow-up '
        'is where deals are actually opened: one nudge a fortnight apart, each adding '
        'something new, each giving the reader an <strong>easy out</strong>.',
    p4b='The skill is sounding relaxed while being relentless. "I’m conscious you’ll '
        'have a full inbox" does more work than "just checking in".',

    vt1='Opening lines', vt2='The ask', vt3='On the phone with the chief of staff',
    vt4='Before the pitch', vt5='In the room', vt6='The nudge',

    # teach-card bodies (the headword and the example stay in English)
    c1='The hook. Names the trigger: something she said, launched or published. '
       'Never "I hope this finds you well".',
    c2='A promise to respect her time. Then keep it: four sentences, no attachment.',
    c3='Credibility by association, in one line. Name a peer house, not a case study.',
    c4='The ask, without pressure. Softer than "I’d love to" and more adult than '
       '"I was wondering if maybe".',
    c5='Frames the meeting as her decision about value, not your request for time.',
    c6='The easy out. Paradoxically, it raises the reply rate: nobody feels cornered.',
    c7='The past continuous softens the request: it is what you were hoping, so '
       'nobody has to refuse you now.',
    c8='The most indirect question in English. It asks about the world, not about her.',
    c9='Hands the decision to the gatekeeper. It is the phrase that turns a gate into '
       'an ally.',
    c10='Closes the call with an action she owns, without asking her to promise anything.',
    c11='Acknowledge the pressure on the boss before you add to it.',
    c12='Offers work instead of demanding it: a one-pager, a French deck, a shorter slot.',
    c13='Start from the reasoning, not the offer. A French board hears the logic first '
        'and judges you on it.',
    c14='States an assumption so it can be corrected. Cartesian, and it lets the senior '
        'person be the expert.',
    c15='Signals that disagreement is coming, formally. Use it once. It carries weight '
        'precisely because it is rare.',
    c16='A "non" in a French meeting is often an opening position. Ask, lightly, which '
        'one you have heard.',
    c17='Lunch is part of the meeting. The hardest question is often answered at the '
        'table, not in the room.',
    c18='Silence after a proposal is thinking, not refusal. Say nothing, or name it, '
        'and wait.',
    c19='Acknowledges the silence without blaming anyone for it.',
    c20='Informal, light and honest about what you are doing. Use it with someone who '
        'has replied once already.',
    c21='Every follow-up adds something new: a number, a name, a date. Never just '
        '"checking in".',
    c22='Names the interpretation you will make, so she can correct it in one line.',
    c23='Finish the thread politely, either way. A closed loop is reopened more easily '
        'than an ignored one.',
    c24='Proposes a pause on your terms, with a date. It keeps control of the timeline.',

    mt1='The first email', mt2='The gatekeeper call', mt3='In the room', mt4='The nudge',
    gt1='The email, line by line', gt2='The follow-up, line by line',
    gh='Use the word bank. One word per gap.',
    bankLabel='Word bank:',
    gw1='"Keep this brief" is the promise; four sentences is keeping it.',
    gw2='"What prompted me to write" names the trigger: her interview.',
    gw3='"I’d welcome the chance to" is the soft ask.',
    gw4='"No need to reply if" is the easy out, and it raises the reply rate.',
    gw5='"I’m conscious" acknowledges her inbox without blaming her for it.',
    gw6='"Since I last wrote" introduces the one new thing this message adds.',
    gw7='"Close the loop" is to finish the thread politely, either way.',
    gw8='"Park this until" proposes a pause on your terms, with a date.',

    ot1='Build the hedged request', ot2='Build the hedged question',
    oh1='Build the hedged request. Every piece is used.',
    ow1='"I was hoping to" puts the request in the past continuous, so it is a hope, '
        'not a demand. The time phrase goes last.',
    oh2='Build the question. One piece is left over.',
    ow2='"Might there be" is the existential question: it asks whether a window exists. '
        '"Might it be a window" is not English.',

    mtt='Match the move to its meaning',
    matchHint='Click a phrase, then what it does in the room.',
    matchWhy='Each move is one of the six from this part.',

    x1='A cold email to the CMO of Galeries Morel. She has never heard of you.',
    s1='Which opening line earns the second sentence?',
    q1w='"What prompted me to write" is the hook: it names something she did, so the '
        'email is about her before it is about you. A pleasantry, a self-introduction '
        'and "reaching out" all spend the first line on nothing.',
    x2='The last line of the same email.',
    s2='Which line makes the ask?',
    q2w='"Would it be worth" frames the meeting as her judgement of value, and "no need '
        'to reply if not" gives her the easy out. "Jump on a quick call" is too casual '
        'for a first contact; "please let me know your availability" is an instruction; '
        '"at your earliest convenience" is a form letter.',
    x3='Subject lines are read on a phone, in a list of forty.',
    s3='Which subject line would you send?',
    q3w='A subject line is the hook in seven words. "What French buyers said" promises '
        'information she does not have. "Partnership opportunity" and "Introduction" '
        'promise a sales call; "Quick question" is the most deleted subject line in '
        'business English.',
    x4='The chief of staff says: "Madame Morel is not taking new meetings this quarter."',
    s4='What do you say?',
    q4w='Accept the no, hedge the next question ("might there be"), offer work ("would '
        'it help if I"). Going round the gatekeeper on LinkedIn, or asking for an '
        'exception, turns an ally into an obstacle. Asking for "someone else" tells her '
        'the boss was never the point.',
    x5='You want to end the call with something she owns.',
    s5='Which close keeps the door open?',
    q5w='"Could I leave it with you" gives her the action without extracting a promise, '
        'and "check back in a fortnight" sets a cadence she can veto. Dictating a '
        'deadline, calling again tomorrow, or bypassing her to a generic inbox all say '
        'you were not listening.',
    x6='Twenty minutes in, the Finance Director of Groupe Éclat says: "Non. We are not '
       'putting budget into a forum."',
    s6='What do you say?',
    q6w='A first "non" is often a position. "Is that a no, or a not yet?" asks which, '
        'lightly, and returning to the premise argues the logic rather than the person. '
        '"Your competitors have understood" is a threat; retreating to next year '
        'concedes; UK case studies answer a question he did not ask.',
    x7='The CEO of Maison Éclore has said nothing for ten seconds after your proposal.',
    s7='What do you do?',
    q7w='Silence after a proposal in a French boardroom is thinking. Filling it, '
        'discounting into it or moving past it all read as nerves, and a discount '
        'offered against silence sets the new price. Name it once if you must, then wait.',
    x8='The meeting is going well. The CMO stands and says: "On continue à table?"',
    s8='Which reply is right?',
    q8w='Lunch is part of the meeting: the hardest question is often settled at the '
        'table. Declining it for a train, or declaring it a business-free zone, both '
        'misread the invitation. Bringing the laptop misreads it the other way.',
    x9='Two weeks after your first email to the Head of Digital at Maison Lumière. '
       'No reply.',
    s9='Which follow-up do you send?',
    q9w='A follow-up acknowledges the silence without blame, then adds something new. '
        '"Just checking in" adds nothing; "my email of the 12th" scolds; taking her off '
        'your list is passive-aggressive and, worse, final.',
    x10='Fourth message, sixth week. Still nothing. You want to stop without burning '
        'the bridge.',
    s10='Which line closes the loop?',
    q10w='"I’ll take silence as" names the interpretation and gives her one line to '
         'correct it; a date keeps the thread alive. Counting your own emails, '
         'announcing a "last attempt" or asking to be released all make the silence '
         'her fault.',

    st='Too pushy, well pitched, or too apologetic?',
    sh='Drag each follow-up line into the column it belongs in.',
    sb1='Too pushy', sb2='Well pitched', sb3='Too apologetic',
    sw='Well pitched lines acknowledge, add something or propose a date. Pushy lines '
       'count, demand or set deadlines. Apologetic lines make the silence your fault.',

    actTitle='Your turn: get in the door',
    actUse='Use at least three:',
    actSpeakBrief='In pairs. One of you is the gatekeeper or the executive; swap after '
                  'each round.',
    actSpeak1='Phone the chief of staff of a CEO you have never met. Get a date, a name '
              'or a next step without asking a single direct question.',
    actSpeak2='Your pitch has just been met with "non" from a Finance Director. Find out '
              'whether it is a no or a not yet, using the premise, not the product.',
    actSpeak3='It is the fourth follow-up. Say, out loud, the message that closes the '
              'loop without closing the door.',
    actWriteKind='Writing · 150–250 words',
    actWriteBrief='Write the first email to the Head of Digital at a French luxury house '
                  'you have never contacted: a hook that names her world, one line of '
                  'credibility, a soft ask and an easy out. Then the follow-up you would '
                  'send two weeks later.',
    actPlaceholder='Subject: …',
)

for _c in LANGS[1:]:
    try:
        T[_c] = importlib.import_module('i18n_redditdoor_%s' % _c).T
    except ImportError:
        pass


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    rows = ['    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
            for k in sorted(d)]
    return '{\n' + ',\n'.join(rows) + '\n  }'
