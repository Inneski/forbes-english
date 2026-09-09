# -*- coding: utf-8 -*-
"""Interface strings for Between Two Worlds — Advanced Prepositions (C1).

English, German and Spanish. Teach cards use the six-item form, so the rule
text travels with its heading — the standing rule since 2026-09-04.

What is NOT translated, deliberately: every example sentence, every option,
every gap sentence and every collocation pair. Those ARE the English being
taught. A C1 learner reading "absorbed in" needs to see it in English; what
they may want in their own language is the *rule* around it, which is what
the card bodies carry.

The builder reads its English from T['en'] rather than repeating it as
literals. Two copies of the same sentence drift, and when they drift the
symptom is bizarre: the slide renders correctly until the learner picks
English in the switcher, at which point the text changes.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

# The template's RPG ledger chrome. This deck has no ledger, but the markup
# that reads these keys ships in every page, and the I18N gate fails a page
# whose data-i18n has no English behind it.
TAIL = {
    'en': {'ledClues': "'Clues'", 'ledDp': "'DP'", 'ledTime': "'Time'"},
    'de': {'ledClues': "'Hinweise'", 'ledDp': "'DP'", 'ledTime': "'Zeit'"},
    'es': {'ledClues': "'Pistas'", 'ledDp': "'DP'", 'ledTime': "'Tiempo'"},
}

T = {}

# ══════════════════════════════════════════════════════════════════════
#  ENGLISH
# ══════════════════════════════════════════════════════════════════════
T['en'] = dict(
    coverTitle='Between <em>Two Worlds</em>',
    coverSub='What a preposition does to a sentence — not what it means',
    chipLevel='C1 · Advanced', chipFocus='Prepositions', chipCount='50 slides',
    bankLabel='Word bank:',

    # ── stage dividers ────────────────────────────────────────────────
    d1t='Advanced Theory', d1n='Stage 1 · form and function',
    d2t='Multi-word Forms', d2n='Stage 2 · compound and complex',
    d3t='Lexical Patterns', d3n='Stage 3 · fixed collocations',
    d4t='The Double Agents', d4n='Stage 4 · preposition or conjunction',
    d5t='The Investigation', d5n='Stage 5 · ten questions',
    d6t='The Black Lodge', d6n='Stage 6 · complete the case files',
    d7t='Crime Scene Analysis', d7n='Stage 7 · spot the error',
    d8t='Red Room Connections', d8n='Stage 8 · match the pair',

    # ── stage eyebrows ────────────────────────────────────────────────
    e1='Advanced theory', e2='Multi-word forms', e3='Lexical patterns',
    e4='The double agents', e5='The investigation', e6='The Black Lodge',
    e7='Crime scene analysis', e8='Red Room connections',

    # ── 1. what a prepositional phrase is ─────────────────────────────
    s1t='The hinge, not the joint',
    s1a='A preposition is not a small joining word. It is the <strong>hinge</strong> '
        'between a noun phrase and the job that phrase does in the sentence.',
    s1b='<em>in</em> + <em>the Black Lodge</em> → <em>in the Black Lodge</em>. The '
        'object is always a noun, a pronoun or an <em>-ing</em> form — never a '
        'finite verb.',

    # ── 2. the three functions ────────────────────────────────────────
    s2t='Three jobs, and only three',
    s2ah='1 · Adverbial',
    s2ab='Modifies a verb, an adjective, or the whole sentence. Answers '
         '<em>where</em>, <em>when</em>, <em>how</em>, <em>why</em>.',
    s2an='Cooper sat <strong>in the diner</strong>.',
    s2bh='2 · Adjectival',
    s2bb='Modifies a noun. Answers <em>which one?</em> Usually called a '
         'post-modifier.',
    s2bn='The woman <strong>in the red room</strong> spoke backwards.',
    s2ch='3 · Nominal',
    s2cb='Acts as a noun itself — subject or object. Rare, and formal.',
    s2cn='<strong>Between the trees</strong> is where he vanished.',

    # ── 3. post-modifiers ─────────────────────────────────────────────
    s3t='Which one?',
    s3a='Inside a noun phrase, a prepositional phrase follows the noun it '
        'modifies and does exactly one job: it tells you <strong>which one</strong>.',
    s3b='<em>The owls [in the forest] are not what they seem.</em> — which owls? '
        'Remove the bracket and the sentence stops identifying anything.',

    # ── 4-5. the six adverbial sub-types ──────────────────────────────
    s4t='Adverbials · where, when, where to',
    s4ah='Place — <em>where?</em>',
    s4ab='The position of the action. The commonest and the least noticed.',
    s4an='Cooper sat <strong>at the Double R</strong>.',
    s4bh='Time — <em>when? how long?</em>',
    s4bb='Locates the action on a timeline, or measures it.',
    s4bn='She vanished <strong>before sunrise</strong>.',
    s4ch='Direction — <em>where to, where from?</em>',
    s4cb='Movement with a goal or a source. Contrast this with Place: direction '
         'needs a verb of motion.',
    s4cn='He walked <strong>into the Red Room</strong>.',

    s5t='Adverbials · how, why, despite what',
    s5ah='Manner — <em>how?</em>',
    s5ab='The way the action is done. Often replaces an adverb.',
    s5an='He spoke <strong>in a low whisper</strong>.',
    s5bh='Reason — <em>why? what for?</em>',
    s5bb='The cause or the purpose behind the action.',
    s5bn='She went back <strong>for the ring</strong>.',
    s5ch='Concession — <em>despite what?</em>',
    s5cb='Something that should have stopped the action and did not.',
    s5cn='<strong>Despite the danger</strong>, he entered.',

    # ── 6. stranded prepositions ──────────────────────────────────────
    s6t='The rule that was never a rule',
    s6a='A preposition can sit at the end of a clause — in questions and in '
        'relative clauses. This is called <strong>stranding</strong>, and it is '
        'ordinary, correct English.',
    s6b='<em>The lodge he came from. Who did she talk to?</em> Only very formal '
        'academic writing prefers <em>the lodge from which he came</em>. Never '
        'avoid it in speech.',

    # ── 7. two-word prepositions ──────────────────────────────────────
    s7t='Two words, one preposition',
    s7ah='except for — <em>excluding</em>',
    s7ab='Removes one thing from an otherwise complete set.',
    s7an='<strong>Except for</strong> the owls, the forest was silent.',
    s7bh='due to — <em>because of</em>',
    s7bb='States a cause. The most formal of the four.',
    s7bn='<strong>Due to</strong> the fog, the road was invisible.',
    s7ch='along with — <em>together with</em>',
    s7cb='Adds a second item without making it a second subject.',
    s7cn='<strong>Along with</strong> the ring, she left a warning.',
    s7dh='apart from — <em>besides / except</em>',
    s7db='Two opposite meanings, and only context separates them.',
    s7dn='<strong>Apart from</strong> Cooper, no one knew the truth.',

    # ── 8-9. three-word prepositions ──────────────────────────────────
    s8t='Three words, one preposition',
    s8ah='in front of',
    s8ab='Directly before, in space. Not <em>before</em>, which is time.',
    s8an='He stood <strong>in front of</strong> the curtain.',
    s8bh='in spite of',
    s8bb='Concession. Identical in meaning to <em>despite</em> — and note that '
         '<em>despite of</em> does not exist.',
    s8bn='<strong>In spite of</strong> the warning, she entered.',
    s8ch='on behalf of',
    s8cb='Representing someone, speaking in their place.',
    s8cn='He spoke <strong>on behalf of</strong> the dead.',
    s8dh='on top of',
    s8db='Literally above, or figuratively <em>in addition to</em>.',
    s8dn='<strong>On top of</strong> everything, the lights went out.',

    s9t='Three words, formal register',
    s9ah='by means of',
    s9ab='The instrument or method. A formal <em>using</em>.',
    s9an='She communicated <strong>by means of</strong> the log.',
    s9bh='with regard to',
    s9bb='Introduces a topic. Common in written business and academic English.',
    s9bn='<strong>With regard to</strong> the case, nothing added up.',
    s9ch='as a result of',
    s9cb='Consequence. Points backwards to the cause.',
    s9cn='<strong>As a result of</strong> the vision, he changed course.',
    s9dh='at the expense of',
    s9db='Something gained, and the price paid for it.',
    s9dn='He solved the case <strong>at the expense of</strong> his sanity.',

    # ── 10. due to vs because of ──────────────────────────────────────
    s10t='<em>Due to</em> and <em>because of</em>',
    s10a='Both give a cause. <strong>Due to</strong> is more formal and '
         'traditionally follows a form of <em>be</em> — <em>the delay was due to '
         'fog</em>.',
    s10b='In modern English they are often interchangeable, but do not open a '
         'sentence with <em>Due to…</em> in academic writing. Use <em>Because '
         'of…</em> there.',

    # ── 11. complex with "of" ─────────────────────────────────────────
    s11t='The <em>of</em> pattern',
    s11ah='in the absence of',
    s11ab='A formal <em>without</em>. Common in reports and legal English.',
    s11an='<strong>In the absence of</strong> evidence, the case was closed.',
    s11bh='by virtue of',
    s11bb='Gives the reason something is permitted or true.',
    s11bn='<strong>By virtue of</strong> his badge, Cooper was allowed through.',
    s11ch='in the wake of',
    s11cb='Immediately following an event, usually a bad one.',
    s11cn='<strong>In the wake of</strong> the tragedy, the town fell silent.',

    # ── 12-14. verb + preposition ─────────────────────────────────────
    s12t='Verbs that demand a preposition',
    s12ah='depend on',
    s12ab='Rely on. Never <em>depend of</em>.',
    s12an='The truth <strong>depends on</strong> who is asking.',
    s12bh='insist on',
    s12bb='Demand firmly. Takes <em>-ing</em>, not an infinitive.',
    s12bn='She <strong>insisted on</strong> seeing the body.',
    s12ch='consist of',
    s12cb='Be made up of. No passive — never <em>is consisted of</em>.',
    s12cn='The Lodge <strong>consists of</strong> endless corridors.',
    s12dh='specialise in',
    s12db='Focus professionally on one area.',
    s12dn='She <strong>specialised in</strong> unsolved disappearances.',

    s13t='<em>Result in</em> and <em>result from</em>',
    s13a='The direction of the arrow is the whole difference. The <strong>event '
         'results in</strong> the consequence. The <strong>consequence results '
         'from</strong> the event.',
    s13b='<em>The investigation resulted in an arrest</em> (cause → effect). '
         '<em>The arrest resulted from the investigation</em> (effect ← cause).',

    s14t='More fixed verb pairs',
    s14ah='respond to',
    s14ab='React to. The noun is <em>reaction to</em>, never <em>reaction on</em>.',
    s14an='He did not <strong>respond to</strong> the knock.',
    s14bh='apologise for',
    s14bb='Express regret for the thing; apologise <em>to</em> the person.',
    s14bn='She <strong>apologised for</strong> the delay.',
    s14ch='suffer from',
    s14cb='Be affected by an illness or a lasting problem.',
    s14cn='The sheriff <strong>suffered from</strong> nightmares.',
    s14dh='believe in',
    s14db='Have faith in — or think a thing exists. <em>Believe</em> alone means '
          'only "accept as true".',
    s14dn='Cooper <strong>believed in</strong> the power of dreams.',

    # ── 15-16. adjective + preposition ────────────────────────────────
    s15t='Adjectives that demand a preposition',
    s15ah='afraid of / aware of',
    s15ab='Both take <em>of</em>. <em>Aware</em> never takes <em>about</em>.',
    s15an='He was <strong>aware of</strong> being watched.',
    s15bh='capable of',
    s15bb='Followed by <em>-ing</em>, never by an infinitive.',
    s15bn='BOB was <strong>capable of</strong> anything.',
    s15ch='responsible for',
    s15cb='The thing, or the person you answer to — both take <em>for</em>.',
    s15cn='Who was <strong>responsible for</strong> the killing?',
    s15dh='guilty of / innocent of',
    s15db='Both take <em>of</em> before the crime. <em>Guilty for</em> is wrong.',
    s15dn='He was found <strong>guilty of</strong> deception.',

    s16t='Interest, habit and fatigue',
    s16ah='interested in',
    s16ab='Never <em>interested about</em> — the commonest single error here.',
    s16an='She was intensely <strong>interested in</strong> the past.',
    s16bh='familiar with',
    s16bb='You are familiar <em>with</em> a thing; a thing is familiar <em>to</em> you.',
    s16bn='Are you <strong>familiar with</strong> the Black Lodge?',
    s16ch='obsessed with',
    s16cb='Takes <em>with</em>, not <em>by</em>, when it describes a person.',
    s16cn='He was <strong>obsessed with</strong> the case for years.',
    s16dh='tired of',
    s16db='<em>Tired of</em> = bored by. <em>Tired from</em> = exhausted by effort.',
    s16dn='She was <strong>tired of</strong> the lies.',

    # ── 17. noun + preposition ────────────────────────────────────────
    s17t='Nouns that demand a preposition',
    s17ah='effect on',
    s17ab='An effect is always <em>on</em> something, never <em>to</em>.',
    s17an='The vision had a lasting <strong>effect on</strong> him.',
    s17bh='solution to / reason for',
    s17bb='Two of the most-missed pairs at C1. Not <em>solution of</em>.',
    s17bn='There was no obvious <strong>solution to</strong> the case.',
    s17ch='increase in',
    s17cb='The thing that grows takes <em>in</em>; the amount takes <em>of</em>.',
    s17cn='An <strong>increase in</strong> strange events was reported.',
    s17dh='connection between',
    s17db='Between two things; <em>connection with</em> one thing.',
    s17dn='The <strong>connection between</strong> the two crimes was clear.',

    # ── 18. the key rule ──────────────────────────────────────────────
    s18t='One word, two grammars',
    s18a='Several words work as both. What follows them decides which. '
         '<strong>Preposition + noun phrase</strong> — no subject, no verb. '
         '<strong>Conjunction + clause</strong> — subject and verb.',
    s18b='<em>She left before dawn</em> (preposition). <em>She left before the owl '
         'appeared</em> (conjunction). Same word, different grammar.',

    s19t='Before, after, until',
    s19ah='before / after',
    s19ab='Both work either way. Test what follows: a noun, or a subject and verb?',
    s19an='He arrived <strong>after midnight</strong>. / He arrived '
          '<strong>after the lights went out</strong>.',
    s19bh='until',
    s19bb='Also both. Note it marks the end of a period, not a point in it.',
    s19bn='They waited <strong>until nightfall</strong>. / …<strong>until the fire '
          'truck appeared</strong>.',
    s19ch='since',
    s19cb='Both, and it carries a third meaning as well — see the next slide.',
    s19cn='Silent <strong>since Tuesday</strong>. / Silent <strong>since she saw '
          'the Red Room</strong>.',

    s20t='The two that will not swap',
    s20ah='despite — preposition only',
    s20ab='It cannot take a clause. For a clause use <em>although</em> or '
          '<em>even though</em>. <em>Despite of</em> is not English.',
    s20an='<strong>Despite the danger</strong>, he went in. / '
          '<strong>Although it was dangerous</strong>, he went in.',
    s20bh='except — needs help',
    s20bb='A preposition on its own; it only becomes a conjunction with '
          '<em>that</em> after it.',
    s20bn='Everyone stayed, <strong>except Cooper</strong>. / …<strong>except that '
          'Cooper left a note</strong>.',

    # ── 21. since ─────────────────────────────────────────────────────
    s21t='The tricky <em>since</em>',
    s21a='<strong>Since</strong> does three jobs. Preposition of time, conjunction '
         'of time, and conjunction of reason — where it simply means '
         '<em>because</em>.',
    s21b='<em>Since last winter</em> (preposition). <em>Since Laura died</em> '
         '(time). <em>Since you know the truth, you must know the danger</em> '
         '(reason). Context decides, and sometimes nothing does.',

    # ── 22. particle vs preposition ───────────────────────────────────
    s22t='Particle or preposition?',
    s22a='A <strong>particle</strong> belongs to the verb and changes its meaning. '
         'A <strong>preposition</strong> belongs to the noun phrase after it.',
    s22b='<em>She looked up the case file</em> — particle, = researched. <em>She '
         'looked up the hill</em> — preposition, and you can ask "up where?" Only '
         'the particle can move: <em>looked it up</em>.',

    # ── the investigation ─────────────────────────────────────────────
    q1t='Concession', q2t='Verb collocation', q3t='Preposition or conjunction',
    q4t='Adjective collocation', q5t='Formal register', q6t='Which function?',
    q7t='Cause and effect', q8t='Register', q9t='Adjective collocation',
    q10t='Compound preposition',

    # ── the black lodge (gap) ─────────────────────────────────────────
    g1t='Cause, concession, method', g2t='Collocations under pressure',
    g3t='Representing and reacting', g4t='The last four blanks',
    gapHint='One word per blank, unless the bracket says otherwise.',

    # ── crime scene ───────────────────────────────────────────────────
    sortT='Correct, or not?',
    sortHint='Drag each sentence into a box. Four of the eight are wrong.',
    sortWhy='The four wrong ones: <em>interested about</em> → <em>interested in</em>; '
            '<em>Despite of</em> → <em>Despite</em>; <em>since twenty years</em> → '
            '<em>for twenty years</em>; <em>resulted of</em> → <em>resulted from</em>.',

    # ── red room ──────────────────────────────────────────────────────
    matchT='Fixed pairs · verbs and adjectives',
    matchT2='Fixed pairs · nouns and outcomes',
    matchHint='Click a fragment, then its ending.',
    matchWhy='Every one of these is fixed. There is no rule to derive them from — '
             'they are learned as pairs, which is why they are tested as pairs.',

    # ── activation ────────────────────────────────────────────────────
    actTitle='Now use it',
    actUse='Use at least three:',
    actSpeakBrief='Describe a place that changed how you saw something. Where it '
                  'was, what stood near it, and why it mattered.',
    actSpeak1='Where was it, and what was around it?',
    actSpeak2='What happened there, and what did it result in?',
    actSpeak3='What are you still aware of, years later?',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Write an account of an investigation — real or invented. Use at '
                  'least two three-word prepositions, one stranded preposition, and '
                  'one pair from the collocation slides.',
    actPlaceholder='In the absence of any real evidence, we…',

    resPerfect='Full marks. Compound forms, collocations and the double agents — all held.',
    resStrong='Strong. Look again at the collocation slides; that is where the last point usually goes.',
    resMid='Solid on the theory. The fixed pairs are the part to drill — they have no rule behind them.',
    resLow='Go back to Stage 4. The preposition/conjunction test is one question: noun, or clause?',
)

# ══════════════════════════════════════════════════════════════════════
#  GERMAN
# ══════════════════════════════════════════════════════════════════════
T['de'] = dict(
    coverTitle='Between <em>Two Worlds</em>',
    coverSub='Was eine Präposition mit einem Satz macht — nicht, was sie bedeutet',
    chipLevel='C1 · Fortgeschritten', chipFocus='Präpositionen', chipCount='50 Folien',
    bankLabel='Wortspeicher:',

    d1t='Fortgeschrittene Theorie', d1n='Stufe 1 · Form und Funktion',
    d2t='Mehrwortformen', d2n='Stufe 2 · zusammengesetzt und komplex',
    d3t='Lexikalische Muster', d3n='Stufe 3 · feste Verbindungen',
    d4t='Die Doppelagenten', d4n='Stufe 4 · Präposition oder Konjunktion',
    d5t='Die Ermittlung', d5n='Stufe 5 · zehn Fragen',
    d6t='The Black Lodge', d6n='Stufe 6 · Akten vervollständigen',
    d7t='Tatortanalyse', d7n='Stufe 7 · Fehler finden',
    d8t='Red Room Connections', d8n='Stufe 8 · Paare zuordnen',

    e1='Fortgeschrittene Theorie', e2='Mehrwortformen', e3='Lexikalische Muster',
    e4='Die Doppelagenten', e5='Die Ermittlung', e6='The Black Lodge',
    e7='Tatortanalyse', e8='Red Room Connections',

    s1t='Das Scharnier, nicht die Fuge',
    s1a='Eine Präposition ist kein kleines Verbindungswort. Sie ist das '
        '<strong>Scharnier</strong> zwischen einer Nominalphrase und der Aufgabe, '
        'die diese Phrase im Satz übernimmt.',
    s1b='<em>in</em> + <em>the Black Lodge</em> → <em>in the Black Lodge</em>. Das '
        'Objekt ist immer ein Nomen, ein Pronomen oder eine <em>-ing</em>-Form — '
        'nie ein finites Verb.',

    s2t='Drei Aufgaben, und nur drei',
    s2ah='1 · Adverbial',
    s2ab='Bestimmt ein Verb, ein Adjektiv oder den ganzen Satz. Antwortet auf '
         '<em>wo</em>, <em>wann</em>, <em>wie</em>, <em>warum</em>.',
    s2an='Cooper sat <strong>in the diner</strong>.',
    s2bh='2 · Adjektivisch',
    s2bb='Bestimmt ein Nomen. Antwortet auf <em>welches?</em> Meist Postmodifikator '
         'genannt.',
    s2bn='The woman <strong>in the red room</strong> spoke backwards.',
    s2ch='3 · Nominal',
    s2cb='Steht selbst als Nomen — Subjekt oder Objekt. Selten und formell.',
    s2cn='<strong>Between the trees</strong> is where he vanished.',

    s3t='Welches denn?',
    s3a='In einer Nominalphrase folgt die Präpositionalphrase dem Nomen, das sie '
        'bestimmt, und hat genau eine Aufgabe: sie sagt, <strong>welches</strong>.',
    s3b='<em>The owls [in the forest] are not what they seem.</em> — welche Eulen? '
        'Ohne die Klammer identifiziert der Satz nichts mehr.',

    s4t='Adverbiale · wo, wann, wohin',
    s4ah='Ort — <em>wo?</em>',
    s4ab='Die Position der Handlung. Am häufigsten und am wenigsten bemerkt.',
    s4an='Cooper sat <strong>at the Double R</strong>.',
    s4bh='Zeit — <em>wann? wie lange?</em>',
    s4bb='Verortet die Handlung auf einer Zeitachse oder misst sie.',
    s4bn='She vanished <strong>before sunrise</strong>.',
    s4ch='Richtung — <em>wohin, woher?</em>',
    s4cb='Bewegung mit Ziel oder Ausgangspunkt. Anders als Ort: Richtung braucht '
         'ein Bewegungsverb.',
    s4cn='He walked <strong>into the Red Room</strong>.',

    s5t='Adverbiale · wie, warum, trotz was',
    s5ah='Art und Weise — <em>wie?</em>',
    s5ab='Wie die Handlung ausgeführt wird. Ersetzt oft ein Adverb.',
    s5an='He spoke <strong>in a low whisper</strong>.',
    s5bh='Grund — <em>warum? wozu?</em>',
    s5bb='Die Ursache oder der Zweck hinter der Handlung.',
    s5bn='She went back <strong>for the ring</strong>.',
    s5ch='Einräumung — <em>trotz was?</em>',
    s5cb='Etwas, das die Handlung hätte verhindern sollen und es nicht tat.',
    s5cn='<strong>Despite the danger</strong>, he entered.',

    s6t='Die Regel, die nie eine war',
    s6a='Eine Präposition kann am Ende eines Teilsatzes stehen — in Fragen und in '
        'Relativsätzen. Das heißt <strong>stranding</strong> und ist ganz normales, '
        'korrektes Englisch.',
    s6b='<em>The lodge he came from. Who did she talk to?</em> Nur sehr formelles '
        'akademisches Schreiben zieht <em>the lodge from which he came</em> vor. '
        'Im Gespräch nie vermeiden.',

    s7t='Zwei Wörter, eine Präposition',
    s7ah='except for — <em>ausgenommen</em>',
    s7ab='Nimmt eine Sache aus einer sonst vollständigen Menge heraus.',
    s7an='<strong>Except for</strong> the owls, the forest was silent.',
    s7bh='due to — <em>wegen</em>',
    s7bb='Nennt eine Ursache. Die formellste der vier.',
    s7bn='<strong>Due to</strong> the fog, the road was invisible.',
    s7ch='along with — <em>zusammen mit</em>',
    s7cb='Fügt ein zweites Element hinzu, ohne es zum zweiten Subjekt zu machen.',
    s7cn='<strong>Along with</strong> the ring, she left a warning.',
    s7dh='apart from — <em>außer / abgesehen von</em>',
    s7db='Zwei gegensätzliche Bedeutungen; nur der Kontext trennt sie.',
    s7dn='<strong>Apart from</strong> Cooper, no one knew the truth.',

    s8t='Drei Wörter, eine Präposition',
    s8ah='in front of',
    s8ab='Räumlich direkt vor. Nicht <em>before</em> — das ist zeitlich.',
    s8an='He stood <strong>in front of</strong> the curtain.',
    s8bh='in spite of',
    s8bb='Einräumung. Bedeutungsgleich mit <em>despite</em> — und <em>despite of</em> '
         'gibt es nicht.',
    s8bn='<strong>In spite of</strong> the warning, she entered.',
    s8ch='on behalf of',
    s8cb='Jemanden vertreten, an seiner Stelle sprechen.',
    s8cn='He spoke <strong>on behalf of</strong> the dead.',
    s8dh='on top of',
    s8db='Wörtlich oben auf, oder übertragen <em>zusätzlich zu</em>.',
    s8dn='<strong>On top of</strong> everything, the lights went out.',

    s9t='Drei Wörter, formelles Register',
    s9ah='by means of',
    s9ab='Das Mittel oder die Methode. Ein formelles <em>using</em>.',
    s9an='She communicated <strong>by means of</strong> the log.',
    s9bh='with regard to',
    s9bb='Führt ein Thema ein. Häufig im geschäftlichen und akademischen Englisch.',
    s9bn='<strong>With regard to</strong> the case, nothing added up.',
    s9ch='as a result of',
    s9cb='Folge. Verweist zurück auf die Ursache.',
    s9cn='<strong>As a result of</strong> the vision, he changed course.',
    s9dh='at the expense of',
    s9db='Etwas gewonnen — und der Preis, der dafür gezahlt wurde.',
    s9dn='He solved the case <strong>at the expense of</strong> his sanity.',

    s10t='<em>Due to</em> und <em>because of</em>',
    s10a='Beide nennen eine Ursache. <strong>Due to</strong> ist formeller und folgt '
         'traditionell einer Form von <em>be</em> — <em>the delay was due to fog</em>.',
    s10b='Im heutigen Englisch sind sie oft austauschbar, aber beginne im '
         'akademischen Schreiben keinen Satz mit <em>Due to…</em>. Dort gehört '
         '<em>Because of…</em> hin.',

    s11t='Das <em>of</em>-Muster',
    s11ah='in the absence of',
    s11ab='Ein formelles <em>without</em>. Häufig in Berichten und Rechtsenglisch.',
    s11an='<strong>In the absence of</strong> evidence, the case was closed.',
    s11bh='by virtue of',
    s11bb='Nennt den Grund, warum etwas erlaubt oder wahr ist.',
    s11bn='<strong>By virtue of</strong> his badge, Cooper was allowed through.',
    s11ch='in the wake of',
    s11cb='Unmittelbar nach einem Ereignis, meist einem schlimmen.',
    s11cn='<strong>In the wake of</strong> the tragedy, the town fell silent.',

    s12t='Verben, die eine Präposition verlangen',
    s12ah='depend on',
    s12ab='Sich verlassen auf. Nie <em>depend of</em>.',
    s12an='The truth <strong>depends on</strong> who is asking.',
    s12bh='insist on',
    s12bb='Nachdrücklich verlangen. Mit <em>-ing</em>, nicht mit Infinitiv.',
    s12bn='She <strong>insisted on</strong> seeing the body.',
    s12ch='consist of',
    s12cb='Bestehen aus. Kein Passiv — nie <em>is consisted of</em>.',
    s12cn='The Lodge <strong>consists of</strong> endless corridors.',
    s12dh='specialise in',
    s12db='Sich beruflich auf ein Gebiet spezialisieren.',
    s12dn='She <strong>specialised in</strong> unsolved disappearances.',

    s13t='<em>Result in</em> und <em>result from</em>',
    s13a='Die Pfeilrichtung ist der ganze Unterschied. Das <strong>Ereignis results '
         'in</strong> der Folge. Die <strong>Folge results from</strong> dem Ereignis.',
    s13b='<em>The investigation resulted in an arrest</em> (Ursache → Wirkung). '
         '<em>The arrest resulted from the investigation</em> (Wirkung ← Ursache).',

    s14t='Weitere feste Verbverbindungen',
    s14ah='respond to',
    s14ab='Reagieren auf. Das Nomen ist <em>reaction to</em>, nie <em>reaction on</em>.',
    s14an='He did not <strong>respond to</strong> the knock.',
    s14bh='apologise for',
    s14bb='Sich für die Sache entschuldigen; bei der Person heißt es <em>to</em>.',
    s14bn='She <strong>apologised for</strong> the delay.',
    s14ch='suffer from',
    s14cb='Von einer Krankheit oder einem dauerhaften Problem betroffen sein.',
    s14cn='The sheriff <strong>suffered from</strong> nightmares.',
    s14dh='believe in',
    s14db='An etwas glauben — oder es für existent halten. <em>Believe</em> allein '
          'heißt nur „für wahr halten“.',
    s14dn='Cooper <strong>believed in</strong> the power of dreams.',

    s15t='Adjektive, die eine Präposition verlangen',
    s15ah='afraid of / aware of',
    s15ab='Beide mit <em>of</em>. <em>Aware</em> nie mit <em>about</em>.',
    s15an='He was <strong>aware of</strong> being watched.',
    s15bh='capable of',
    s15bb='Mit <em>-ing</em>, nie mit Infinitiv.',
    s15bn='BOB was <strong>capable of</strong> anything.',
    s15ch='responsible for',
    s15cb='Die Sache oder die Person, der man Rechenschaft schuldet — beide mit '
          '<em>for</em>.',
    s15cn='Who was <strong>responsible for</strong> the killing?',
    s15dh='guilty of / innocent of',
    s15db='Beide mit <em>of</em> vor der Tat. <em>Guilty for</em> ist falsch.',
    s15dn='He was found <strong>guilty of</strong> deception.',

    s16t='Interesse, Gewohnheit und Müdigkeit',
    s16ah='interested in',
    s16ab='Nie <em>interested about</em> — der häufigste Einzelfehler hier.',
    s16an='She was intensely <strong>interested in</strong> the past.',
    s16bh='familiar with',
    s16bb='Man ist mit einer Sache <em>familiar with</em>; eine Sache ist einem '
          '<em>familiar to</em>.',
    s16bn='Are you <strong>familiar with</strong> the Black Lodge?',
    s16ch='obsessed with',
    s16cb='Bei Personen mit <em>with</em>, nicht mit <em>by</em>.',
    s16cn='He was <strong>obsessed with</strong> the case for years.',
    s16dh='tired of',
    s16db='<em>Tired of</em> = überdrüssig. <em>Tired from</em> = erschöpft von.',
    s16dn='She was <strong>tired of</strong> the lies.',

    s17t='Nomen, die eine Präposition verlangen',
    s17ah='effect on',
    s17ab='Eine Wirkung ist immer <em>on</em> etwas, nie <em>to</em>.',
    s17an='The vision had a lasting <strong>effect on</strong> him.',
    s17bh='solution to / reason for',
    s17bb='Zwei der am häufigsten verfehlten Paare auf C1. Nicht <em>solution of</em>.',
    s17bn='There was no obvious <strong>solution to</strong> the case.',
    s17ch='increase in',
    s17cb='Das Wachsende mit <em>in</em>, die Menge mit <em>of</em>.',
    s17cn='An <strong>increase in</strong> strange events was reported.',
    s17dh='connection between',
    s17db='Zwischen zwei Dingen; bei einem heißt es <em>connection with</em>.',
    s17dn='The <strong>connection between</strong> the two crimes was clear.',

    s18t='Ein Wort, zwei Grammatiken',
    s18a='Mehrere Wörter können beides. Was folgt, entscheidet. '
         '<strong>Präposition + Nominalphrase</strong> — kein Subjekt, kein Verb. '
         '<strong>Konjunktion + Teilsatz</strong> — Subjekt und Verb.',
    s18b='<em>She left before dawn</em> (Präposition). <em>She left before the owl '
         'appeared</em> (Konjunktion). Gleiches Wort, andere Grammatik.',

    s19t='Before, after, until',
    s19ah='before / after',
    s19ab='Beide gehen beides. Prüfe, was folgt: ein Nomen, oder Subjekt und Verb?',
    s19an='He arrived <strong>after midnight</strong>. / He arrived '
          '<strong>after the lights went out</strong>.',
    s19bh='until',
    s19bb='Ebenfalls beides. Es markiert das Ende eines Zeitraums, keinen Punkt darin.',
    s19bn='They waited <strong>until nightfall</strong>. / …<strong>until the fire '
          'truck appeared</strong>.',
    s19ch='since',
    s19cb='Beides — und dazu eine dritte Bedeutung, siehe nächste Folie.',
    s19cn='Silent <strong>since Tuesday</strong>. / Silent <strong>since she saw '
          'the Red Room</strong>.',

    s20t='Die zwei, die nicht tauschen',
    s20ah='despite — nur Präposition',
    s20ab='Kann keinen Teilsatz nehmen. Dafür <em>although</em> oder <em>even '
          'though</em>. <em>Despite of</em> gibt es im Englischen nicht.',
    s20an='<strong>Despite the danger</strong>, he went in. / '
          '<strong>Although it was dangerous</strong>, he went in.',
    s20bh='except — braucht Hilfe',
    s20bb='Allein eine Präposition; zur Konjunktion wird es erst mit <em>that</em>.',
    s20bn='Everyone stayed, <strong>except Cooper</strong>. / …<strong>except that '
          'Cooper left a note</strong>.',

    s21t='Das knifflige <em>since</em>',
    s21a='<strong>Since</strong> hat drei Aufgaben: temporale Präposition, temporale '
         'Konjunktion und kausale Konjunktion — dort heißt es schlicht '
         '<em>because</em>.',
    s21b='<em>Since last winter</em> (Präposition). <em>Since Laura died</em> (Zeit). '
         '<em>Since you know the truth, you must know the danger</em> (Grund). Der '
         'Kontext entscheidet — und manchmal entscheidet nichts.',

    s22t='Partikel oder Präposition?',
    s22a='Eine <strong>Partikel</strong> gehört zum Verb und ändert dessen Bedeutung. '
         'Eine <strong>Präposition</strong> gehört zur folgenden Nominalphrase.',
    s22b='<em>She looked up the case file</em> — Partikel, = nachgeschlagen. <em>She '
         'looked up the hill</em> — Präposition, und man kann „up where?“ fragen. Nur '
         'die Partikel lässt sich versetzen: <em>looked it up</em>.',

    q1t='Einräumung', q2t='Verbverbindung', q3t='Präposition oder Konjunktion',
    q4t='Adjektivverbindung', q5t='Formelles Register', q6t='Welche Funktion?',
    q7t='Ursache und Wirkung', q8t='Register', q9t='Adjektivverbindung',
    q10t='Zusammengesetzte Präposition',

    g1t='Ursache, Einräumung, Methode', g2t='Verbindungen unter Druck',
    g3t='Vertreten und reagieren', g4t='Die letzten vier Lücken',
    gapHint='Ein Wort pro Lücke, sofern die Klammer nichts anderes sagt.',

    sortT='Richtig oder nicht?',
    sortHint='Ziehe jeden Satz in ein Feld. Vier der acht sind falsch.',
    sortWhy='Die vier falschen: <em>interested about</em> → <em>interested in</em>; '
            '<em>Despite of</em> → <em>Despite</em>; <em>since twenty years</em> → '
            '<em>for twenty years</em>; <em>resulted of</em> → <em>resulted from</em>.',

    matchT='Feste Paare · Verben und Adjektive',
    matchT2='Feste Paare · Nomen und Folgen',
    matchHint='Klicke ein Fragment an, dann seine Ergänzung.',
    matchWhy='Alle diese Verbindungen sind fest. Es gibt keine Regel, aus der man sie '
             'ableiten könnte — man lernt sie als Paare, und darum werden sie als '
             'Paare geprüft.',

    actTitle='Jetzt anwenden',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Beschreibe einen Ort, der deinen Blick auf etwas verändert hat. Wo '
                  'er lag, was in der Nähe stand und warum er wichtig war.',
    actSpeak1='Wo war es, und was war ringsum?',
    actSpeak2='Was ist dort passiert, und was hat es bewirkt?',
    actSpeak3='Was ist dir Jahre später noch bewusst?',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Schreibe den Bericht einer Ermittlung — echt oder erfunden. Verwende '
                  'mindestens zwei dreiteilige Präpositionen, eine nachgestellte '
                  'Präposition und ein Paar aus den Kollokationsfolien.',
    actPlaceholder='In the absence of any real evidence, we…',

    resPerfect='Volle Punktzahl. Mehrwortformen, Kollokationen und die Doppelagenten — alles gehalten.',
    resStrong='Stark. Sieh dir die Kollokationsfolien noch einmal an; dort geht der letzte Punkt meist verloren.',
    resMid='Die Theorie sitzt. Üben musst du die festen Paare — hinter ihnen steht keine Regel.',
    resLow='Zurück zu Stufe 4. Der Test für Präposition oder Konjunktion ist eine Frage: Nomen oder Teilsatz?',
)

# ══════════════════════════════════════════════════════════════════════
#  SPANISH
# ══════════════════════════════════════════════════════════════════════
T['es'] = dict(
    coverTitle='Between <em>Two Worlds</em>',
    coverSub='Qué le hace una preposición a una oración — no qué significa',
    chipLevel='C1 · Avanzado', chipFocus='Preposiciones', chipCount='50 diapositivas',
    bankLabel='Banco de palabras:',

    d1t='Teoría avanzada', d1n='Etapa 1 · forma y función',
    d2t='Formas pluriverbales', d2n='Etapa 2 · compuestas y complejas',
    d3t='Patrones léxicos', d3n='Etapa 3 · colocaciones fijas',
    d4t='Los agentes dobles', d4n='Etapa 4 · preposición o conjunción',
    d5t='La investigación', d5n='Etapa 5 · diez preguntas',
    d6t='The Black Lodge', d6n='Etapa 6 · completa los expedientes',
    d7t='Análisis de la escena', d7n='Etapa 7 · encuentra el error',
    d8t='Red Room Connections', d8n='Etapa 8 · empareja',

    e1='Teoría avanzada', e2='Formas pluriverbales', e3='Patrones léxicos',
    e4='Los agentes dobles', e5='La investigación', e6='The Black Lodge',
    e7='Análisis de la escena', e8='Red Room Connections',

    s1t='La bisagra, no la junta',
    s1a='Una preposición no es una palabrita de enlace. Es la <strong>bisagra</strong> '
        'entre un sintagma nominal y la función que ese sintagma cumple en la oración.',
    s1b='<em>in</em> + <em>the Black Lodge</em> → <em>in the Black Lodge</em>. El '
        'objeto es siempre un sustantivo, un pronombre o una forma en <em>-ing</em> — '
        'nunca un verbo conjugado.',

    s2t='Tres funciones, y solo tres',
    s2ah='1 · Adverbial',
    s2ab='Modifica un verbo, un adjetivo o toda la oración. Responde a <em>dónde</em>, '
         '<em>cuándo</em>, <em>cómo</em>, <em>por qué</em>.',
    s2an='Cooper sat <strong>in the diner</strong>.',
    s2bh='2 · Adjetival',
    s2bb='Modifica un sustantivo. Responde a <em>¿cuál?</em> Suele llamarse '
         'posmodificador.',
    s2bn='The woman <strong>in the red room</strong> spoke backwards.',
    s2ch='3 · Nominal',
    s2cb='Funciona como sustantivo — sujeto u objeto. Poco frecuente y formal.',
    s2cn='<strong>Between the trees</strong> is where he vanished.',

    s3t='¿Cuál exactamente?',
    s3a='Dentro de un sintagma nominal, el sintagma preposicional sigue al sustantivo '
        'que modifica y cumple una sola función: decir <strong>cuál</strong>.',
    s3b='<em>The owls [in the forest] are not what they seem.</em> — ¿qué búhos? Quita '
        'el corchete y la oración deja de identificar nada.',

    s4t='Adverbiales · dónde, cuándo, adónde',
    s4ah='Lugar — <em>¿dónde?</em>',
    s4ab='La posición de la acción. El más frecuente y el menos advertido.',
    s4an='Cooper sat <strong>at the Double R</strong>.',
    s4bh='Tiempo — <em>¿cuándo? ¿cuánto?</em>',
    s4bb='Sitúa la acción en una línea temporal, o la mide.',
    s4bn='She vanished <strong>before sunrise</strong>.',
    s4ch='Dirección — <em>¿adónde, de dónde?</em>',
    s4cb='Movimiento con meta u origen. A diferencia del lugar, la dirección exige un '
         'verbo de movimiento.',
    s4cn='He walked <strong>into the Red Room</strong>.',

    s5t='Adverbiales · cómo, por qué, pese a qué',
    s5ah='Modo — <em>¿cómo?</em>',
    s5ab='La manera en que se hace la acción. A menudo sustituye a un adverbio.',
    s5an='He spoke <strong>in a low whisper</strong>.',
    s5bh='Causa — <em>¿por qué? ¿para qué?</em>',
    s5bb='El motivo o el propósito detrás de la acción.',
    s5bn='She went back <strong>for the ring</strong>.',
    s5ch='Concesión — <em>¿pese a qué?</em>',
    s5cb='Algo que debería haber impedido la acción y no lo hizo.',
    s5cn='<strong>Despite the danger</strong>, he entered.',

    s6t='La regla que nunca fue regla',
    s6a='Una preposición puede ir al final de una cláusula — en preguntas y en '
        'relativas. Se llama <strong>stranding</strong> y es inglés corriente y '
        'correcto.',
    s6b='<em>The lodge he came from. Who did she talk to?</em> Solo la escritura '
        'académica muy formal prefiere <em>the lodge from which he came</em>. Al '
        'hablar, nunca lo evites.',

    s7t='Dos palabras, una preposición',
    s7ah='except for — <em>excepto</em>',
    s7ab='Saca un elemento de un conjunto por lo demás completo.',
    s7an='<strong>Except for</strong> the owls, the forest was silent.',
    s7bh='due to — <em>debido a</em>',
    s7bb='Expresa causa. La más formal de las cuatro.',
    s7bn='<strong>Due to</strong> the fog, the road was invisible.',
    s7ch='along with — <em>junto con</em>',
    s7cb='Añade un segundo elemento sin convertirlo en segundo sujeto.',
    s7cn='<strong>Along with</strong> the ring, she left a warning.',
    s7dh='apart from — <em>aparte de / salvo</em>',
    s7db='Dos sentidos opuestos; solo el contexto los separa.',
    s7dn='<strong>Apart from</strong> Cooper, no one knew the truth.',

    s8t='Tres palabras, una preposición',
    s8ah='in front of',
    s8ab='Delante de, en el espacio. No <em>before</em>, que es temporal.',
    s8an='He stood <strong>in front of</strong> the curtain.',
    s8bh='in spite of',
    s8bb='Concesión. Idéntica a <em>despite</em> — y ojo: <em>despite of</em> no existe.',
    s8bn='<strong>In spite of</strong> the warning, she entered.',
    s8ch='on behalf of',
    s8cb='Representar a alguien, hablar en su nombre.',
    s8cn='He spoke <strong>on behalf of</strong> the dead.',
    s8dh='on top of',
    s8db='Literalmente encima, o en sentido figurado <em>además de</em>.',
    s8dn='<strong>On top of</strong> everything, the lights went out.',

    s9t='Tres palabras, registro formal',
    s9ah='by means of',
    s9ab='El instrumento o el método. Un <em>using</em> formal.',
    s9an='She communicated <strong>by means of</strong> the log.',
    s9bh='with regard to',
    s9bb='Introduce un tema. Frecuente en inglés académico y de negocios.',
    s9bn='<strong>With regard to</strong> the case, nothing added up.',
    s9ch='as a result of',
    s9cb='Consecuencia. Apunta hacia atrás, a la causa.',
    s9cn='<strong>As a result of</strong> the vision, he changed course.',
    s9dh='at the expense of',
    s9db='Algo ganado, y el precio pagado por ello.',
    s9dn='He solved the case <strong>at the expense of</strong> his sanity.',

    s10t='<em>Due to</em> y <em>because of</em>',
    s10a='Ambas dan una causa. <strong>Due to</strong> es más formal y sigue por '
         'tradición a una forma de <em>be</em> — <em>the delay was due to fog</em>.',
    s10b='En inglés moderno suelen ser intercambiables, pero no empieces una oración '
         'con <em>Due to…</em> en un texto académico. Ahí va <em>Because of…</em>.',

    s11t='El patrón con <em>of</em>',
    s11ah='in the absence of',
    s11ab='Un <em>without</em> formal. Habitual en informes y en inglés jurídico.',
    s11an='<strong>In the absence of</strong> evidence, the case was closed.',
    s11bh='by virtue of',
    s11bb='Da la razón por la que algo se permite o es cierto.',
    s11bn='<strong>By virtue of</strong> his badge, Cooper was allowed through.',
    s11ch='in the wake of',
    s11cb='Inmediatamente después de un suceso, normalmente malo.',
    s11cn='<strong>In the wake of</strong> the tragedy, the town fell silent.',

    s12t='Verbos que exigen preposición',
    s12ah='depend on',
    s12ab='Depender de. Nunca <em>depend of</em>.',
    s12an='The truth <strong>depends on</strong> who is asking.',
    s12bh='insist on',
    s12bb='Exigir con firmeza. Con <em>-ing</em>, no con infinitivo.',
    s12bn='She <strong>insisted on</strong> seeing the body.',
    s12ch='consist of',
    s12cb='Estar compuesto de. Sin pasiva — nunca <em>is consisted of</em>.',
    s12cn='The Lodge <strong>consists of</strong> endless corridors.',
    s12dh='specialise in',
    s12db='Especializarse profesionalmente en un área.',
    s12dn='She <strong>specialised in</strong> unsolved disappearances.',

    s13t='<em>Result in</em> y <em>result from</em>',
    s13a='La dirección de la flecha es toda la diferencia. El <strong>suceso results '
         'in</strong> la consecuencia. La <strong>consecuencia results from</strong> '
         'el suceso.',
    s13b='<em>The investigation resulted in an arrest</em> (causa → efecto). <em>The '
         'arrest resulted from the investigation</em> (efecto ← causa).',

    s14t='Más pares verbales fijos',
    s14ah='respond to',
    s14ab='Reaccionar a. El sustantivo es <em>reaction to</em>, nunca <em>reaction on</em>.',
    s14an='He did not <strong>respond to</strong> the knock.',
    s14bh='apologise for',
    s14bb='Disculparse <em>for</em> la cosa; ante la persona, <em>to</em>.',
    s14bn='She <strong>apologised for</strong> the delay.',
    s14ch='suffer from',
    s14cb='Padecer una enfermedad o un problema duradero.',
    s14cn='The sheriff <strong>suffered from</strong> nightmares.',
    s14dh='believe in',
    s14db='Creer en algo — o pensar que existe. <em>Believe</em> a secas solo significa '
          '«dar por cierto».',
    s14dn='Cooper <strong>believed in</strong> the power of dreams.',

    s15t='Adjetivos que exigen preposición',
    s15ah='afraid of / aware of',
    s15ab='Ambos con <em>of</em>. <em>Aware</em> nunca con <em>about</em>.',
    s15an='He was <strong>aware of</strong> being watched.',
    s15bh='capable of',
    s15bb='Seguido de <em>-ing</em>, nunca de infinitivo.',
    s15bn='BOB was <strong>capable of</strong> anything.',
    s15ch='responsible for',
    s15cb='La cosa, o la persona ante quien respondes — ambas con <em>for</em>.',
    s15cn='Who was <strong>responsible for</strong> the killing?',
    s15dh='guilty of / innocent of',
    s15db='Ambos con <em>of</em> ante el delito. <em>Guilty for</em> es incorrecto.',
    s15dn='He was found <strong>guilty of</strong> deception.',

    s16t='Interés, costumbre y hartazgo',
    s16ah='interested in',
    s16ab='Nunca <em>interested about</em> — el error más común de todo el bloque.',
    s16an='She was intensely <strong>interested in</strong> the past.',
    s16bh='familiar with',
    s16bb='Uno está <em>familiar with</em> una cosa; una cosa te resulta '
          '<em>familiar to</em>.',
    s16bn='Are you <strong>familiar with</strong> the Black Lodge?',
    s16ch='obsessed with',
    s16cb='Con <em>with</em>, no con <em>by</em>, cuando describe a una persona.',
    s16cn='He was <strong>obsessed with</strong> the case for years.',
    s16dh='tired of',
    s16db='<em>Tired of</em> = harto de. <em>Tired from</em> = agotado por el esfuerzo.',
    s16dn='She was <strong>tired of</strong> the lies.',

    s17t='Sustantivos que exigen preposición',
    s17ah='effect on',
    s17ab='Un efecto siempre es <em>on</em> algo, nunca <em>to</em>.',
    s17an='The vision had a lasting <strong>effect on</strong> him.',
    s17bh='solution to / reason for',
    s17bb='Dos de los pares más fallados en C1. No <em>solution of</em>.',
    s17bn='There was no obvious <strong>solution to</strong> the case.',
    s17ch='increase in',
    s17cb='Lo que crece lleva <em>in</em>; la cantidad lleva <em>of</em>.',
    s17cn='An <strong>increase in</strong> strange events was reported.',
    s17dh='connection between',
    s17db='Entre dos cosas; con una sola, <em>connection with</em>.',
    s17dn='The <strong>connection between</strong> the two crimes was clear.',

    s18t='Una palabra, dos gramáticas',
    s18a='Varias palabras hacen las dos cosas. Lo que las sigue decide cuál. '
         '<strong>Preposición + sintagma nominal</strong> — sin sujeto ni verbo. '
         '<strong>Conjunción + cláusula</strong> — con sujeto y verbo.',
    s18b='<em>She left before dawn</em> (preposición). <em>She left before the owl '
         'appeared</em> (conjunción). Misma palabra, gramática distinta.',

    s19t='Before, after, until',
    s19ah='before / after',
    s19ab='Ambas valen para las dos. Mira lo que sigue: ¿sustantivo, o sujeto y verbo?',
    s19an='He arrived <strong>after midnight</strong>. / He arrived '
          '<strong>after the lights went out</strong>.',
    s19bh='until',
    s19bb='También las dos. Marca el final de un periodo, no un punto dentro de él.',
    s19bn='They waited <strong>until nightfall</strong>. / …<strong>until the fire '
          'truck appeared</strong>.',
    s19ch='since',
    s19cb='Las dos — y además un tercer sentido; mira la diapositiva siguiente.',
    s19cn='Silent <strong>since Tuesday</strong>. / Silent <strong>since she saw '
          'the Red Room</strong>.',

    s20t='Las dos que no se cambian',
    s20ah='despite — solo preposición',
    s20ab='No admite cláusula. Para eso, <em>although</em> o <em>even though</em>. '
          '<em>Despite of</em> no existe en inglés.',
    s20an='<strong>Despite the danger</strong>, he went in. / '
          '<strong>Although it was dangerous</strong>, he went in.',
    s20bh='except — necesita ayuda',
    s20bb='Sola es preposición; solo se vuelve conjunción con <em>that</em> detrás.',
    s20bn='Everyone stayed, <strong>except Cooper</strong>. / …<strong>except that '
          'Cooper left a note</strong>.',

    s21t='El <em>since</em> difícil',
    s21a='<strong>Since</strong> hace tres trabajos: preposición temporal, conjunción '
         'temporal y conjunción causal — donde equivale simplemente a '
         '<em>because</em>.',
    s21b='<em>Since last winter</em> (preposición). <em>Since Laura died</em> (tiempo). '
         '<em>Since you know the truth, you must know the danger</em> (causa). Decide '
         'el contexto, y a veces no decide nada.',

    s22t='¿Partícula o preposición?',
    s22a='Una <strong>partícula</strong> pertenece al verbo y le cambia el significado. '
         'Una <strong>preposición</strong> pertenece al sintagma nominal que la sigue.',
    s22b='<em>She looked up the case file</em> — partícula, = consultó. <em>She looked '
         'up the hill</em> — preposición, y puedes preguntar «up where?». Solo la '
         'partícula se mueve: <em>looked it up</em>.',

    q1t='Concesión', q2t='Colocación verbal', q3t='Preposición o conjunción',
    q4t='Colocación adjetival', q5t='Registro formal', q6t='¿Qué función?',
    q7t='Causa y efecto', q8t='Registro', q9t='Colocación adjetival',
    q10t='Preposición compuesta',

    g1t='Causa, concesión, método', g2t='Colocaciones bajo presión',
    g3t='Representar y reaccionar', g4t='Los últimos cuatro huecos',
    gapHint='Una palabra por hueco, salvo que el paréntesis diga otra cosa.',

    sortT='¿Correcta o no?',
    sortHint='Arrastra cada oración a una caja. Cuatro de las ocho están mal.',
    sortWhy='Las cuatro incorrectas: <em>interested about</em> → <em>interested in</em>; '
            '<em>Despite of</em> → <em>Despite</em>; <em>since twenty years</em> → '
            '<em>for twenty years</em>; <em>resulted of</em> → <em>resulted from</em>.',

    matchT='Pares fijos · verbos y adjetivos',
    matchT2='Pares fijos · sustantivos y resultados',
    matchHint='Haz clic en un fragmento y luego en su final.',
    matchWhy='Todas estas combinaciones son fijas. No hay regla de la que deducirlas — '
             'se aprenden como pares, y por eso se evalúan como pares.',

    actTitle='Ahora úsalo',
    actUse='Usa al menos tres:',
    actSpeakBrief='Describe un lugar que cambió tu manera de ver algo. Dónde estaba, qué '
                  'había cerca y por qué importó.',
    actSpeak1='¿Dónde estaba y qué había alrededor?',
    actSpeak2='¿Qué pasó allí y en qué acabó?',
    actSpeak3='¿De qué sigues siendo consciente años después?',
    actWriteKind='Escritura · 150–200 palabras',
    actWriteBrief='Escribe el relato de una investigación — real o inventada. Usa al '
                  'menos dos preposiciones de tres palabras, una preposición al final '
                  'de cláusula y un par de las diapositivas de colocaciones.',
    actPlaceholder='In the absence of any real evidence, we…',

    resPerfect='Puntuación perfecta. Formas compuestas, colocaciones y agentes dobles: todo controlado.',
    resStrong='Muy bien. Vuelve a las diapositivas de colocaciones; ahí suele irse el último punto.',
    resMid='La teoría está. Lo que hay que practicar son los pares fijos — detrás de ellos no hay regla.',
    resLow='Vuelve a la Etapa 4. La prueba de preposición o conjunción es una sola pregunta: ¿sustantivo o cláusula?',
)


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    rows = ['    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
            for k in sorted(d)]
    rows += ['    %s: %s' % (k, TAIL[code][k]) for k in sorted(TAIL[code])]
    return '{\n' + ',\n'.join(rows) + '\n  }'


if __name__ == '__main__':
    base = set(T['en'])
    for c, d in T.items():
        m, x = base - set(d), set(d) - base
        print('%-3s %3d keys' % (c, len(d)),
              ('MISSING %s' % sorted(m)) if m else 'ok',
              ('EXTRA %s' % sorted(x)) if x else '')
