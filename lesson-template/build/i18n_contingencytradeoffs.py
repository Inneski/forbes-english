# -*- coding: utf-8 -*-
"""Interface strings for Contingency Plans & Trade-offs (C1).

English, German and Spanish (DE and ES written in-session, no native check). The lesson is a C1 vocabulary list of 58 items taught
through English definitions, so a language pass is 58 definitions plus 28
explanations per language — not cheap, and not asked for. Every string the
learner reads is keyed here, so adding a language later is one module per
language (i18n_contingencytradeoffs_<code>.py exporting T), exactly as
The Writer's Nightmare does, plus the code in LANGS.

NOT translated, deliberately (HOUSE-STYLE §8): the headwords, the quiz stems
and every option. Cited words in explanations are in double quotes.
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
    coverTitle='Contingency Plans &amp; <em>Trade-offs</em>',
    coverSub='The vocabulary of planning, risk and materials',
    chipLevel='C1 · Advanced', chipFocus='Vocabulary · 58 words',
    chipCount='54 slides',

    d1t='Plans and Outcomes', d1n='Part 1 · eighteen words',
    d2t='On Site', d2n='Part 2 · eighteen words',
    d3t='People and Pressure', d3n='Part 3 · twenty-two words',
    d4t='The Test', d4n='Part 4 · twenty-eight questions',

    e1='Plans and outcomes', e2='On site', e3='People and pressure', e4='Test',

    p1t='Plan A, plan B',
    p1a='Every project runs on an <strong>assumption</strong> or two. When one fails, '
        'you either reach for the <strong>contingency plan</strong> you wrote in advance, '
        'or you improvise something <strong>ad hoc</strong> — and explain it '
        '<strong>post hoc</strong>.',
    p1b='The gap between what you planned and what you got is the '
        '<strong>shortfall</strong>. What you give up to close it is the '
        '<strong>trade-off</strong>.',
    p2t='What the building is made of',
    p2a='On site the vocabulary turns physical: <strong>moisture</strong> in the walls, '
        'the <strong>firmness</strong> of a membrane, a <strong>dense</strong> and '
        '<strong>homogeneous</strong> concrete mix, a <strong>fire-retardant</strong> coating.',
    p2b='And when an old building lacks something, you do not rebuild it. You '
        '<strong>retrofit</strong>.',
    p3t='The human side',
    p3a='Projects are run by people, and people get tired. An <strong>arduous</strong> '
        'week ends in <strong>exhaustion</strong>; a <strong>monotonous</strong> one in '
        'boredom. A client who is <strong>agitated</strong> needs a '
        '<strong>persuasive</strong> answer, not an <strong>exaggerated</strong> one.',
    p3b='Some of these words have two meanings. Watch "concern" and "concerns", and '
        '"compromised".',

    vt1='Planning ahead', vt2='Facts and checks', vt3='Limits and safety',
    vt4='Materials', vt5='Condition and repair', vt6='Around the site',
    vt7='Reading people', vt8='Effort', vt9='Reactions and argument',
    vt10='Money, deals and leading',

    # definitions (the old page's glossary, audited)
    g_contingency='A plan that can be followed if the original plan is not possible.',
    g_adhoc='Arranged specifically as needed, not planned in advance.',
    g_posthoc='After the event; done or reasoned after the fact.',
    g_parallel='Happening at the same time and connected.',
    g_tradeoff='Verb: give up one thing to gain another, as part of a compromise. '
               'The noun is "a trade-off".',
    g_shortfall='A deficit of something required or expected.',
    g_unintended='Not planned or meant.',
    g_actual='Existing in fact, as opposed to what was intended, expected or believed.',
    g_current='Happening or existing now.',
    g_requirement='Something that is necessary.',
    g_assumption='Something accepted as true or certain to happen, without proof.',
    g_reassess='Consider or assess again, especially in the light of new information.',
    g_threshold='The level that must be exceeded for a reaction or effect to occur.',
    g_precaution='A measure taken in advance to prevent something unpleasant.',
    g_reliable='Able to be trusted to work well, consistently.',
    g_primarily='For the most part; mainly.',
    g_delay='A period by which something is late or postponed.',
    g_trial='A test of the performance, quality or suitability of someone or something.',
    g_moisture='Water or other liquid present in small amounts in a solid or on a surface.',
    g_firmness='The quality of having a solid, almost unyielding surface or structure.',
    g_dense='Closely compacted in substance.',
    g_homogeneous='Of the same kind all the way through; alike.',
    g_resilient='Able to withstand difficult conditions or recover quickly from them.',
    g_fireretardant='A substance or treatment that slows or stops the spread of fire.',
    g_mouldy='Covered in or affected by mould.',
    g_hazardous='Risky; dangerous.',
    g_width='How wide something is.',
    g_retrofit='Add a component to something that did not have it when it was built.',
    g_remove='Take something away from where it was.',
    g_takeoff='Deduct part of an amount: "take 10% off the price".',
    g_chain='A connected, flexible series of metal links for fastening or pulling loads.',
    g_carpet='A floor or stair covering made of thick woven fabric.',
    g_stuck='Past of "stick": pushed something sharp into something. Also: unable to move.',
    g_locate='Find the exact place or position of something.',
    g_audible='Able to be heard.',
    g_appropriate='Suitable for the situation.',
    g_deserve='Have earned a reward or punishment by your actions or qualities.',
    g_tell='In poker: an unconscious action that gives away an attempt to deceive.',
    g_granted='Fail to appreciate someone or something because you are so used to it.',
    g_concern='Noun: anxiety; worry.',
    g_concerns='Verb: relates to; is about. "This email concerns the delay."',
    g_competitor='Another business offering a similar product or service.',
    g_exhaustion='A state of extreme physical or mental tiredness.',
    g_arduous='Needing a lot of effort; difficult and tiring.',
    g_monotonous='Boring and repetitive.',
    g_manageable='Able to be organised or completed without too much difficulty.',
    g_agitated='Troubled or nervous, and showing it.',
    g_nightmare='A frightening dream — or, informally, a very difficult situation.',
    g_startle='Give a person or animal a sudden shock or fright.',
    g_provoke='Cause a reaction, often a strong or angry one.',
    g_exaggerate='Describe something as bigger, better or worse than it really is.',
    g_persuade='Convince someone to do or believe something.',
    g_persuasive='Good at persuading people, through reasons or temptation.',
    g_opinion='A view or judgement, not necessarily based on fact.',
    g_compromised='1. Settled a dispute by each side giving something up. '
                  '2. Weakened or put at risk: "a compromised structure".',
    g_affordable='Reasonably priced.',
    g_advert='An advertisement.',
    g_conduct='1. Organise and carry out: "conduct a survey". 2. Lead or guide someone.',

    mt='Match the meaning',
    matchHint='Click a word, then the meaning that goes with it.',
    matchWhy='Each word is matched to its definition from this part.',

    qt1='Meaning → word', qt2='Word → meaning', qt3='Complete the sentence',
    q1i='Twelve definitions. Choose the word or phrase each one describes.',
    q2i='Eight words. Choose the meaning that fits.',
    q3i='Eight sentences from site and office. Choose the word that completes each one.',
    qInfo='Every word in the test is taught in Parts 1 to 3.',

    q1w='"Deserve" means to have earned something, good or bad, through your actions or qualities.',
    q2w='"In parallel" describes connected processes happening at the same time: '
        'testing two components in parallel.',
    q3w='A "contingency plan" is your backup — what you do if plan A fails.',
    q4w='"Unintended" describes an outcome that happened by accident, not by design.',
    q5w='A "tell" is a small, often involuntary sign that gives away what someone is '
        'really thinking.',
    q6w='To "trade off" is to give up one thing to gain another. The noun is '
        '"a trade-off": a compromise between two priorities.',
    q7w='A "shortfall" is the gap between what you needed and what you actually got.',
    q8w='"Post hoc" (Latin) describes something done or reasoned after the event.',
    q9w='"Ad hoc" describes something arranged for a specific purpose as it comes up, '
        'rather than planned in advance.',
    q10w='"Actual" contrasts the real situation with what was planned or assumed: '
         '"actual sales" against "projected sales".',
    q11w='"Retrofit" means fitting something new to an existing structure — retrofitting '
         'insulation to an old building, for example.',
    q12w='To "take something for granted" is to stop noticing its value because it has '
         'always been there.',
    q13w='"Moisture" is water held within a material or condensed on its surface.',
    q14w='"Firmness" describes how solid and resistant to pressure something is.',
    q15w='"Resilient" describes the ability to withstand stress or damage, or to bounce '
         'back from it.',
    q16w='A "threshold" is the tipping point — the level something must reach before an '
         'effect begins.',
    q17w='"Homogeneous" means uniform: made up of parts that are all of the same kind.',
    q18w='"Exhaustion" is the state of being completely worn out, physically or mentally.',
    q19w='"Arduous" describes a task that demands a lot of effort and is tiring to complete.',
    q20w='"Persuasive" is the adjective: it describes someone or something good at '
         'changing minds. "Persuade" is the verb.',
    q21w='A "contingency plan" is a backup for when the adhesive does not perform as expected.',
    q22w='"Unintended" describes a result nobody planned — here, the discolouration.',
    q23w='A "shortfall" names the gap between what was needed and what was delivered.',
    q24w='"Firmness" is the quality of resisting deformation — what you want from a '
         'structural membrane.',
    q25w='"Retrofit" means adding something to an existing structure that did not '
         'originally have it.',
    q26w='"Remove" means take something away from where it was — the old tape, here.',
    q27w='"In parallel" fits two connected processes happening at the same time.',
    q28w='"Take for granted" means stop appreciating something because it is familiar; '
         'the warning is not to let that happen.',

    actTitle='Your turn: plan B',
    actUse='Use at least four:',
    actSpeakBrief='In pairs or small groups. Give real examples, not one-word answers.',
    actSpeak1='Describe a project — at work, at home or in your studies — where the '
              'original plan failed. Was there a contingency plan, or was the fix ad hoc?',
    actSpeak2='What trade-offs does your job or course force on you? Time against '
              'quality, cost against safety? Which one would you reassess?',
    actSpeak3='What do people in your field take for granted — a tool, a colleague, a '
              'material — that would be a nightmare to lose?',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='You manage a building project. A supplier has delivered 30% less '
                  'fire-retardant board than ordered. Write an email to the client: '
                  'explain the shortfall, the precautions you are taking, and your '
                  'contingency plan.',
    actPlaceholder='Dear …',
)

for _c in LANGS[1:]:
    try:
        T[_c] = importlib.import_module('i18n_contingencytradeoffs_%s' % _c).T
    except ImportError:
        pass


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    rows = ['    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
            for k in sorted(d)]
    return '{\n' + ',\n'.join(rows) + '\n  }'
