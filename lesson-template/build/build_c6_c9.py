# -*- coding: utf-8 -*-
"""Camps six and nine: the two continuous tenses.

Both are built from camp seven, which is now the model for a camp: same
engine, same furniture, its own colour and its own diagram. What they share
with each other is the shape of the idea — a tense that spreads around a
moment instead of occupying a block — so both take the ripple rather than the
rectangle, and the diagrams are deliberately siblings.
"""
import re, sys, shutil
sys.path.insert(0, 'lesson-template')
shutil.copy('/tmp/camp_diagrams.py', 'camp_diagrams.py')
import camp_diagrams as D

BASE = open('sherpa-tensing-camp-seven-future-simple.html', encoding='utf-8').read()


def assemble(hero_section, camps, diagram_js, questions, palette, title,
             extra_replacements, out):
    s = BASE
    A = s.index('<section class="hero" id="hero">')
    B = s.index('</section>', A) + len('</section>')
    C = s.index('<div class="camp" id="rules">')
    Dq = s.index('<div class="camp" id="quiz">')
    E = s.index('var willExamples = [')
    F = s.index('// ── QUIZ ──')
    G = s.index('var questions = [')
    H = s.index('\nvar current = 0;')
    out_s = (s[:A] + hero_section + s[B:C] + camps + s[Dq:E] + diagram_js +
             s[F:G] + questions + s[H:])
    out_s = re.sub(r'  :root\{.*?\n  \}', palette, out_s, count=1, flags=re.S)
    out_s = out_s.replace(
        "<title>Sherpa Tensing - Camp Seven: The Weather You Can't See Yet (Future Simple)</title>",
        title, 1)
    for a, b in extra_replacements:
        out_s = out_s.replace(a, b)
    open(out, 'w', encoding='utf-8').write(out_s)
    return out_s


def hero(eyebrow, h1, para, svg):
    return ('<section class="hero" id="hero">\n    <div>\n'
            '      <span class="eyebrow">%s</span>\n'
            '      <h1>%s</h1>\n      <p>%s</p>\n    </div>\n    %s\n  </section>'
            % (eyebrow, h1, para, svg))


def rule_grid(cards, cls='rule-grid'):
    return '<div class="%s">\n%s\n      </div>' % (cls, "\n".join(
        '        <div class="rule-card">\n          <h3>%s</h3>\n'
        '          <p>%s</p>\n          <div class="ex">%s</div>\n        </div>' % c
        for c in cards))


MARK_FLAG = ('<div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" '
             'stroke-width="2"><path d="M5 3v18M5 4h11l-3 4 3 4H5"/></svg></div>')
MARK_TABLE = ('<div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" '
              'stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"/>'
              '<path d="M3 10h18M9 4v16"/></svg></div>')
MARK_FORK = ('<div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" '
             'stroke-width="2"><path d="M12 3v18"/><path d="M7 8l-4 4 4 4M17 8l4 4-4 4"/></svg></div>')
MARK_CLOCK = ('<div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" '
              'stroke-width="2"><circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/></svg></div>')
MARK_PANES = ('<div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" '
              'stroke-width="2"><rect x="3" y="4" width="8" height="16"/>'
              '<rect x="13" y="4" width="8" height="16"/></svg></div>')

# ═════════════════════════════════════════════════════════════════════
# CAMP SIX · PAST CONTINUOUS
# ═════════════════════════════════════════════════════════════════════
SIX_HERO = hero(
    'Camp six &middot; past continuous',
    'The weather you were already in',
    'Camp three struck the tent and walked away. Camp six goes back and stands inside the day itself &mdash; '
    'the rain that was already falling, the argument that was already running, the thing that was going on '
    'when something else cut across it.',
    D.camp_six('pc'))

SIX_CAMPS = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Basecamp briefing</div>
      <h2>When to use it</h2>
      ''' + rule_grid([
        ('The action that got interrupted',
         'Something was already running when a shorter, finished action cut in.',
         '"I <em>was driving</em> home when the call came."'),
        ('Two things at once',
         'Both were in progress, usually joined by <em>while</em>.',
         '"She <em>was cooking</em> while he <em>was unpacking</em>."'),
        ('Setting a scene',
         'The background of a story, before anything happens in it.',
         '"It <em>was raining</em>. Nobody <em>was speaking</em>."'),
        ('A temporary past situation',
         'True for a while, and not any more.',
         '"That year we <em>were living</em> above the bakery."'),
        ('An irritating past habit',
         'always, forever or constantly + -ing carries the complaint.',
         '"He <em>was always losing</em> his keys."'),
        ('Softening what you want',
         'The past continuous makes a request sound less blunt.',
         '"I <em>was wondering</em> whether you had a moment."'),
    ]) + '''
    </div>

    <div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Building the tense</div>
      <h2>How it's built</h2>
      ''' + rule_grid([
        ('Affirmative', 'subject + was / were + <strong>-ing</strong>', '"They <em>were waiting</em> outside."'),
        ('Negative', 'subject + was / were + not + -ing', '"I <em>wasn\'t listening</em>."'),
        ('Yes / No questions', 'Was / Were + subject + -ing?', '"<em>Were you sleeping</em>?"'),
        ('Wh- questions', 'question word + was / were + subject + -ing?', '"What <em>were they doing</em>?"'),
    ], 'form-grid') + '''
      <div class="chart-wrap">
        <h3>Conjugation chart</h3>
        <p class="chart-note">Only <em>be</em> changes, and it changes exactly as it does in camp three &mdash; <em>was</em> for I, he, she and it; <em>were</em> for the rest. The <em>-ing</em> form never moves.</p>
        <table class="conj">
          <thead><tr><th>Subject</th><th>Affirmative</th><th>Negative</th><th>Question</th></tr></thead>
          <tbody>
            <tr><td class="subj">I</td><td>I was working</td><td>I wasn't working</td><td>Was I working?</td></tr>
            <tr><td class="subj">You</td><td>You were working</td><td>You weren't working</td><td>Were you working?</td></tr>
            <tr><td class="subj">He / She / It</td><td>She was working</td><td>She wasn't working</td><td>Was she working?</td></tr>
            <tr><td class="subj">We</td><td>We were working</td><td>We weren't working</td><td>Were we working?</td></tr>
            <tr><td class="subj">They</td><td>They were working</td><td>They weren't working</td><td>Were they working?</td></tr>
          </tbody>
        </table>
      </div>
      <div class="chart-wrap">
        <h3>The verbs that refuse the -ing</h3>
        <p class="chart-note">State verbs describe a condition rather than an activity, and English does not put a condition in the continuous. These take the past simple even when everything around them is continuous.</p>
        <table class="conj">
          <thead><tr><th>Group</th><th>Verbs</th><th>Say this instead</th></tr></thead>
          <tbody>
            <tr><td class="subj">Thinking</td><td>know, believe, understand, remember</td><td>"I <em>knew</em> the answer." not "I was knowing"</td></tr>
            <tr><td class="subj">Feeling</td><td>like, love, hate, want, need</td><td>"She <em>wanted</em> to leave."</td></tr>
            <tr><td class="subj">Senses</td><td>see, hear, smell, seem</td><td>"It <em>seemed</em> quiet."</td></tr>
            <tr><td class="subj">Having</td><td>own, belong, have (= possess)</td><td>"We <em>had</em> two cars then."</td></tr>
          </tbody>
        </table>
      </div>
      <div class="chart-wrap">
        <h3>Three mistakes worth naming</h3>
        <p class="chart-note">Almost every error with this tense is one of these three.</p>
        <table class="conj">
          <thead><tr><th>Not this</th><th>This</th><th>Why</th></tr></thead>
          <tbody>
            <tr><td class="subj">They was waiting.</td><td>They were waiting.</td><td><em>They</em> is plural, so it takes <em>were</em>.</td></tr>
            <tr><td class="subj">I was knowing him.</td><td>I knew him.</td><td>State verbs do not take the continuous.</td></tr>
            <tr><td class="subj">While I was walking, it was starting to rain.</td><td>While I was walking, it started to rain.</td><td>The thing that cuts in is short and finished: past simple.</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="camp" id="vs-simple">
      ''' + MARK_FORK + '''
      <div class="camp-label">The fork in the path</div>
      <h2>Past continuous or past simple?</h2>
      <div class="chart-wrap" style="margin-top:18px">
        <p class="chart-note" style="margin-bottom:16px">Camp three and camp six describe the same night. The difference is whether you are standing <em>inside</em> the action or looking back at it as one finished event.</p>
        <table class="conj">
          <thead><tr><th>Question</th><th>Past continuous</th><th>Past simple</th></tr></thead>
          <tbody>
            <tr><td class="subj">What is it?</td><td>The background, still running.<br>"I <em>was reading</em>."</td><td>The event, complete.<br>"I <em>read</em> it."</td></tr>
            <tr><td class="subj">Which one interrupts?</td><td>Gets interrupted.</td><td>Does the interrupting.<br>"I was reading when the lights <em>went out</em>."</td></tr>
            <tr><td class="subj">A sequence?</td><td>Never.</td><td>Always.<br>"She stood up, paid and left."</td></tr>
            <tr><td class="subj">Which word introduces it?</td><td><em>while</em>, <em>as</em></td><td><em>when</em></td></tr>
          </tbody>
        </table>
        <p class="example" style="margin-top:14px">The reliable test: <em>while</em> takes the long action, <em>when</em> takes the short one. "While I was cooking, the phone rang" and "When the phone rang, I was cooking" are the same night told from opposite ends.</p>
      </div>
      <div class="btnrow" style="margin-top:16px">
        <a class="route-link" href="sherpa-tensing-camp-three-past-simple.html">&larr; Camp three &middot; past simple</a>
      </div>
    </div>

    <div class="camp" id="signals">
      ''' + MARK_CLOCK + '''
      <div class="camp-label">Trail markers</div>
      <h2>Signal words</h2>
      <div class="signal-groups">
        <div class="signal-box">
          <h3>The long action</h3>
          <ul>
            <li>while &middot; as</li>
            <li>all morning / all day / all night</li>
            <li>at eight o'clock last night</li>
            <li>at that moment</li>
            <li>this time last week</li>
            <li>the whole time</li>
          </ul>
        </div>
        <div class="signal-box">
          <h3>The thing that cuts in</h3>
          <ul>
            <li>when</li>
            <li>suddenly</li>
            <li>just then</li>
            <li>at that point</li>
            <li>until</li>
            <li>and then</li>
          </ul>
        </div>
      </div>
      <p class="example" style="margin-top:14px">If a sentence has both, they almost always split the same way: <em>while</em> + was/were doing, <em>when</em> + past simple.</p>
    </div>

    <div class="camp" id="past-now">
      ''' + MARK_PANES + '''
      <div class="camp-label">Interactive</div>
      <h2>The long action and the short one</h2>
      <div class="diagram-card">
        <p class="diagram-intro">The yellow spreads through past time with no edge you can point at &mdash; that is the past continuous, and it is why the picture is a glow and not a block. The brown bar dropping into it is camp three: one short, finished action, cutting in. Click either to name it and see it in a sentence.</p>
        <div class="diagram-stage">
          ''' + D.camp_six('pcb').replace('<svg class="hero-diagram"', '<svg') + '''
        </div>
        <div class="diagram-panels">
          <div class="diagram-panel" id="panel-long">
            <h4>Past continuous &mdash; the long action</h4>
            <ul id="panel-long-list"></ul>
          </div>
          <div class="diagram-panel is-now" id="panel-short">
            <h4>Past simple &mdash; the interruption</h4>
            <ul id="panel-short-list"></ul>
          </div>
        </div>
      </div>
    </div>

    '''

SIX_JS = '''var longExamples = [
  "I <em>was driving</em> home in the dark.",
  "It <em>was raining</em> and nobody <em>was speaking</em>.",
  "That year we <em>were living</em> above the bakery."
];
var shortExamples = [
  "&hellip; when the call <em>came</em>.",
  "&hellip; when the lights <em>went out</em>.",
  "&hellip; then the door <em>opened</em>."
];

function renderList(id, items){
  var ul = document.getElementById(id);
  ul.innerHTML = "";
  items.forEach(function(txt){
    var li = document.createElement("li");
    li.innerHTML = txt;
    ul.appendChild(li);
  });
}
renderList("panel-long-list", longExamples);
renderList("panel-short-list", shortExamples);

'''

SIX_Q = '''var questions = [
  {
    prompt: "I _____ home when the call came. (drive)",
    hint: "The long action that got interrupted.",
    correct: "was driving",
    options: ["was driving", "drove", "were driving", "was drive"],
    explain: "The action already running takes the past continuous: was driving. The short thing that cut in — the call — takes the past simple."
  },
  {
    prompt: "While she _____ , the doorbell rang. (cook)",
    hint: "\\"While\\" almost always takes the long action.",
    correct: "was cooking",
    options: ["was cooking", "cooked", "were cooking", "is cooking"],
    explain: "While introduces the background action, so it takes the past continuous: while she was cooking."
  },
  {
    prompt: "When the lights went out, we _____ dinner. (have)",
    hint: "Which half is the background here?",
    correct: "were having",
    options: ["were having", "had", "was having", "were had"],
    explain: "The dinner was already in progress when the lights went out, so it takes the past continuous with the plural were."
  },
  {
    prompt: "They _____ ready when the taxi arrived. (not / be)",
    hint: "Careful \\u2014 be is a state verb.",
    correct: "weren't",
    options: ["weren't", "weren't being", "wasn't", "didn't be"],
    explain: "Be describes a state, so it stays in the past simple: they weren't ready. \\"Weren't being ready\\" is not English."
  },
  {
    prompt: "I _____ the answer at the time. (know)",
    hint: "A state verb again.",
    correct: "knew",
    options: ["knew", "was knowing", "were knowing", "knowed"],
    explain: "Know is a state verb and refuses the continuous. Past simple: I knew."
  },
  {
    prompt: "_____ you _____ when I called? (sleep)",
    hint: "Question order for the past continuous.",
    correct: "Were ... sleeping",
    options: ["Were ... sleeping", "Did ... sleeping", "Was ... sleeping", "Were ... slept"],
    explain: "Questions invert be: Were you sleeping? You is plural in form, so it takes were."
  },
  {
    prompt: "He _____ his keys that summer. (always / lose)",
    hint: "A complaint, not a neutral fact.",
    correct: "was always losing",
    options: ["was always losing", "always lost", "was losing always", "always was lose"],
    explain: "Always + the past continuous carries irritation: he was always losing his keys. Always lost would just be a habit."
  },
  {
    prompt: "She stood up, _____ the bill and left. (pay)",
    hint: "Three finished actions in order.",
    correct: "paid",
    options: ["paid", "was paying", "were paying", "pays"],
    explain: "A sequence of completed actions stays in the past simple throughout. The past continuous never tells a sequence."
  },
  {
    prompt: "At eight o'clock last night I _____ on a train. (sit)",
    hint: "A clock time in the past, mid-action.",
    correct: "was sitting",
    options: ["was sitting", "sat", "were sitting", "have sat"],
    explain: "A precise past moment with the action already under way takes the past continuous: I was sitting."
  },
  {
    prompt: "I _____ whether you had a moment. (wonder)",
    hint: "A softened request.",
    correct: "was wondering",
    options: ["was wondering", "wondered", "am wondering", "were wondering"],
    explain: "The past continuous makes a request less blunt: I was wondering whether… It is politeness, not past time."
  },
  {
    prompt: "While we _____ , they _____ the whole flat. (talk / repaint)",
    hint: "Two long actions at the same time.",
    correct: "were talking ... were repainting",
    options: ["were talking ... were repainting", "talked ... repainted",
              "were talking ... repainted", "talked ... were repainting"],
    explain: "Two actions running side by side both take the past continuous, joined by while."
  },
  {
    prompt: "The car _____ when I turned the key. (not / start)",
    hint: "A single finished attempt.",
    correct: "didn't start",
    options: ["didn't start", "wasn't starting", "weren't starting", "not started"],
    explain: "One completed attempt at a moment in the past is the past simple: it didn't start."
  },
  {
    prompt: "It _____ hard, so we stayed in. (rain)",
    hint: "The weather as background.",
    correct: "was raining",
    options: ["was raining", "rained", "were raining", "is raining"],
    explain: "Weather setting the scene takes the past continuous: it was raining. \\"It rained\\" would report the whole day as one finished event."
  },
  {
    prompt: "What _____ you _____ at midnight? (do)",
    hint: "Asking about a moment, not a whole night.",
    correct: "were ... doing",
    options: ["were ... doing", "did ... do", "was ... doing", "were ... did"],
    explain: "Asking what was in progress at a precise past time takes the past continuous: What were you doing?"
  }
];
'''

SIX_PALETTE = '''  :root{
    --ink:#2A2208;
    --ink-soft:#6E6231;
    --paper:#FDFBF0;
    --card:#FFFFFF;
    --accent:#A8860B;
    --accent-dark:#6B5200;
    --accent-light:#F0E0A6;
    --accent-lighter:#FBF4DA;
    --good:#1E7A4C;
    --good-bg:#E5F5EC;
    --bad:#B23A3A;
    --bad-bg:#FBEAEA;
    --radius:14px;
  }'''

assemble(SIX_HERO, SIX_CAMPS, SIX_JS, SIX_Q, SIX_PALETTE,
         '<title>Sherpa Tensing - Camp Six: The Weather You Were Already In (Past Continuous)</title>',
         [('shape-will', 'shape-long'), ('panel-will', 'panel-long'),
          ('"#E8632A"', '"#C79A00"'),
          ('/* ── NOW vs WILL DIAGRAM CAMP ── */', '/* ── LONG vs SHORT DIAGRAM CAMP ── */'),
          ('// ── NOW vs WILL diagram interactivity ──', '// ── the long action and the interruption ──'),
          ('"Clean run. You can tell a decision from a plan, and a belief from a forecast."',
           '"Clean run. You can hear which action is the background and which one cuts in."'),
          ('"Solid progress. Worth a look back at camp five before camp eight."',
           '"Solid progress. Worth a look back at camp three before camp seven."'),
          ('"Good first attempt. The will/going to fork is the part to read again."',
           '"Good first attempt. The while/when fork is the part to read again."')],
         'sherpa-tensing-camp-six-past-continuous.html')
print('camp six written')

# ═════════════════════════════════════════════════════════════════════
# CAMP NINE · FUTURE CONTINUOUS
# ═════════════════════════════════════════════════════════════════════
NINE_HERO = hero(
    'Camp nine &middot; future continuous',
    'This time tomorrow',
    'Camp seven told you what will happen. Camp nine tells you what will already be happening &mdash; '
    'the thing that starts before you arrive and is still going when you do. It is the tense of the '
    'appointed hour, and of asking for something without appearing to ask.',
    D.camp_nine('fc'))

NINE_CAMPS = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Basecamp briefing</div>
      <h2>When to use it</h2>
      ''' + rule_grid([
        ('In progress at a future moment',
         'It starts before the moment and is still running at it.',
         '"This time tomorrow I <em>\'ll be flying</em> over the Alps."'),
        ('Already arranged, running its course',
         'Nobody has to decide anything; it is simply going to be happening.',
         '"I <em>\'ll be seeing</em> her at the meeting anyway."'),
        ('Asking without asking',
         'The politest way in English to find out someone\'s plans.',
         '"<em>Will you be using</em> the car tonight?"'),
        ('Two futures side by side',
         'Both in progress at the same future time.',
         '"While you <em>\'re unpacking</em>, I <em>\'ll be cooking</em>."'),
        ('Guessing what is going on now',
         'A confident assumption about this very moment.',
         '"Don\'t call &mdash; he <em>\'ll be driving</em>."'),
        ('Softening a plain future',
         'Less pushy than <em>will do</em>, because nobody chose it.',
         '"I <em>\'ll be sending</em> the invoice on Friday."'),
    ]) + '''
    </div>

    <div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Building the tense</div>
      <h2>How it's built</h2>
      ''' + rule_grid([
        ('Affirmative', 'subject + will be + <strong>-ing</strong>', '"They <em>\'ll be waiting</em> at arrivals."'),
        ('Negative', 'subject + will not (won\'t) be + -ing', '"I <em>won\'t be working</em> on Friday."'),
        ('Yes / No questions', 'Will + subject + be + -ing?', '"<em>Will you be joining</em> us?"'),
        ('Wh- questions', 'question word + will + subject + be + -ing?', '"Where <em>will you be staying</em>?"'),
    ], 'form-grid') + '''
      <div class="chart-wrap">
        <h3>Conjugation chart</h3>
        <p class="chart-note">Nothing agrees with anything. <em>Will</em> is a modal, <em>be</em> stays in its base form, and only the main verb takes <em>-ing</em> &mdash; which makes this one of the easiest tenses in English to build and one of the hardest to know when to use.</p>
        <table class="conj">
          <thead><tr><th>Subject</th><th>Affirmative</th><th>Negative</th><th>Question</th></tr></thead>
          <tbody>
            <tr><td class="subj">I</td><td>I will be working <em>(I'll)</em></td><td>I won't be working</td><td>Will I be working?</td></tr>
            <tr><td class="subj">You</td><td>You will be working</td><td>You won't be working</td><td>Will you be working?</td></tr>
            <tr><td class="subj">He / She / It</td><td>She will be working</td><td>She won't be working</td><td>Will she be working?</td></tr>
            <tr><td class="subj">We</td><td>We will be working</td><td>We won't be working</td><td>Will we be working?</td></tr>
            <tr><td class="subj">They</td><td>They will be working</td><td>They won't be working</td><td>Will they be working?</td></tr>
          </tbody>
        </table>
      </div>
      <div class="chart-wrap">
        <h3>Three mistakes worth naming</h3>
        <p class="chart-note">The form is simple, so the errors are nearly always the same three.</p>
        <table class="conj">
          <thead><tr><th>Not this</th><th>This</th><th>Why</th></tr></thead>
          <tbody>
            <tr><td class="subj">I will being working.</td><td>I will be working.</td><td>After a modal, <em>be</em> keeps its base form.</td></tr>
            <tr><td class="subj">I will be know the answer.</td><td>I will know the answer.</td><td>State verbs take the plain future, not the continuous.</td></tr>
            <tr><td class="subj">When I will be arriving, call me.</td><td>When I arrive, call me.</td><td>After <em>when</em> and <em>if</em>, use the present &mdash; the same rule as camp seven.</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="camp" id="vs-will">
      ''' + MARK_FORK + '''
      <div class="camp-label">The fork in the path</div>
      <h2>Will do or will be doing?</h2>
      <div class="chart-wrap" style="margin-top:18px">
        <p class="chart-note" style="margin-bottom:16px">Both are true about the same future. What changes is whether you are naming the whole event or standing in the middle of it &mdash; and, more often than learners expect, how much you are asking of the other person.</p>
        <table class="conj">
          <thead><tr><th>Situation</th><th>Will be doing</th><th>Will do</th></tr></thead>
          <tbody>
            <tr><td class="subj">The shape</td><td>In progress around a moment.<br>"At six I <em>'ll be cooking</em>."</td><td>The whole event.<br>"At six I <em>'ll cook</em>."</td></tr>
            <tr><td class="subj">Who decided</td><td>Nobody &mdash; it is simply the way the day runs.</td><td>You, and often just now.</td></tr>
            <tr><td class="subj">Asking a favour</td><td>Neutral. "<em>Will you be going</em> past the post office?"</td><td>A request. "<em>Will you go</em> past the post office?"</td></tr>
            <tr><td class="subj">Promises and offers</td><td>Not used.</td><td>The natural choice.<br>"I <em>'ll help</em> you."</td></tr>
          </tbody>
        </table>
        <p class="example" style="margin-top:14px">This is why "Will you be using the car?" is polite and "Will you use the car?" sounds like an instruction: the continuous asks about the world, the simple asks about you.</p>
      </div>
      <div class="btnrow" style="margin-top:16px">
        <a class="route-link" href="sherpa-tensing-camp-seven-future-simple.html">&larr; Camp seven &middot; future simple</a>
      </div>
    </div>

    <div class="camp" id="signals">
      ''' + MARK_CLOCK + '''
      <div class="camp-label">Trail markers</div>
      <h2>Signal words</h2>
      <div class="signal-groups">
        <div class="signal-box">
          <h3>The appointed moment</h3>
          <ul>
            <li>this time tomorrow / next week</li>
            <li>at eight o'clock on Friday</li>
            <li>when you arrive</li>
            <li>by then</li>
            <li>during the flight</li>
            <li>at that point</li>
          </ul>
        </div>
        <div class="signal-box">
          <h3>The stretch of time</h3>
          <ul>
            <li>all day tomorrow</li>
            <li>all next week</li>
            <li>between two and four</li>
            <li>from Monday to Thursday</li>
            <li>for the next few hours</li>
            <li>while you&hellip;</li>
          </ul>
        </div>
      </div>
      <p class="example" style="margin-top:14px">If the time marker names a <em>point</em> and the action was under way before it, you are in camp nine.</p>
    </div>

    <div class="camp" id="past-now">
      ''' + MARK_PANES + '''
      <div class="camp-label">Interactive</div>
      <h2>Now vs. what will be under way</h2>
      <div class="diagram-card">
        <p class="diagram-intro">The amber spreads through future time the way camp six's yellow spreads through past time &mdash; same idea, other side of the line. The dashed marker is the appointed moment, and the point of the tense is that the action does not start there. It is already running when you arrive. Click either to name it and see it in a sentence.</p>
        <div class="diagram-stage">
          ''' + D.camp_nine('fcb').replace('<svg class="hero-diagram"', '<svg') + '''
        </div>
        <div class="diagram-panels">
          <div class="diagram-panel is-now" id="panel-now">
            <h4>Now &mdash; where you're speaking from</h4>
            <ul id="panel-now-list"></ul>
          </div>
          <div class="diagram-panel" id="panel-fc">
            <h4>Future continuous &mdash; already under way</h4>
            <ul id="panel-fc-list"></ul>
          </div>
        </div>
      </div>
    </div>

    '''

NINE_JS = '''var fcExamples = [
  "This time tomorrow I <em>'ll be flying</em> over the Alps.",
  "<em>Will you be using</em> the car tonight?",
  "Don't call him &mdash; he <em>'ll be driving</em>."
];
var nowExamples = [
  "We <em>are</em> at base camp.",
  "It <em>is</em> raining hard.",
  "She <em>works</em> here."
];

function renderList(id, items){
  var ul = document.getElementById(id);
  ul.innerHTML = "";
  items.forEach(function(txt){
    var li = document.createElement("li");
    li.innerHTML = txt;
    ul.appendChild(li);
  });
}
renderList("panel-fc-list", fcExamples);
renderList("panel-now-list", nowExamples);

'''

NINE_Q = '''var questions = [
  {
    prompt: "This time tomorrow I _____ over the Alps. (fly)",
    hint: "In progress at a named future moment.",
    correct: "'ll be flying",
    options: ["'ll be flying", "'ll fly", "'ll been flying", "am flying"],
    explain: "The flight starts before that moment and is still going at it, so it takes will be + -ing."
  },
  {
    prompt: "_____ you _____ the car this evening?",
    hint: "The polite way to ask about someone's plans.",
    correct: "Will ... be using",
    options: ["Will ... be using", "Will ... use", "Do ... be using", "Will ... using"],
    explain: "Will you be using…? asks about the world rather than making a request. \\"Will you use the car?\\" sounds like an instruction."
  },
  {
    prompt: "Don't ring him now \\u2014 he _____ . (drive)",
    hint: "A confident guess about this very moment.",
    correct: "'ll be driving",
    options: ["'ll be driving", "drives", "'ll drive", "was driving"],
    explain: "The future continuous is often used for what is almost certainly happening right now: he'll be driving."
  },
  {
    prompt: "I _____ on Friday, so send it Monday. (not / work)",
    hint: "Negative form.",
    correct: "won't be working",
    options: ["won't be working", "don't be working", "won't working", "am not work"],
    explain: "The negative puts not on will: won't be working. Be keeps its base form."
  },
  {
    prompt: "At three o'clock we _____ halfway up the ridge. (climb)",
    hint: "Mid-action at a clock time.",
    correct: "will be climbing",
    options: ["will be climbing", "will climb", "will been climbing", "are climbing"],
    explain: "The climb is already under way at three, so it takes the future continuous."
  },
  {
    prompt: "While you _____ the tents, I _____ supper. (pitch / cook)",
    hint: "Two future actions side by side.",
    correct: "'re pitching ... 'll be cooking",
    options: ["'re pitching ... 'll be cooking", "'ll be pitching ... 'll be cooking",
              "pitch ... 'll cook", "'ll pitch ... cook"],
    explain: "After while we use a present form for the first half, and the second takes the future continuous."
  },
  {
    prompt: "I _____ the answer by then. (know)",
    hint: "Careful \\u2014 which verbs refuse the continuous?",
    correct: "'ll know",
    options: ["'ll know", "'ll be knowing", "'ll been knowing", "know"],
    explain: "Know is a state verb, so it takes the plain future: I'll know. \\"Will be knowing\\" is not English."
  },
  {
    prompt: "Give me a ring when you _____ at the station. (arrive)",
    hint: "What follows \\"when\\"?",
    correct: "arrive",
    options: ["arrive", "will arrive", "will be arriving", "arrived"],
    explain: "After when, if and as soon as we use the present even about the future — the same rule as camp seven."
  },
  {
    prompt: "This time next year she _____ in Lisbon. (live)",
    hint: "A situation running at a distant future moment.",
    correct: "will be living",
    options: ["will be living", "will live", "lives", "is living"],
    explain: "Both are possible, but \\"will be living\\" is the natural choice with this time next year, because it describes the situation as ongoing."
  },
  {
    prompt: "The phone's ringing \\u2014 I _____ it. (get)",
    hint: "A decision taken this second.",
    correct: "'ll get",
    options: ["'ll get", "'ll be getting", "get", "am getting"],
    explain: "An offer or a spontaneous decision takes the plain future. The continuous would be odd here — nobody has arranged to answer a phone."
  },
  {
    prompt: "We _____ the results all afternoon. (discuss)",
    hint: "A stretch of future time.",
    correct: "'ll be discussing",
    options: ["'ll be discussing", "'ll discuss", "discuss", "'ll been discussing"],
    explain: "All afternoon describes a stretch the action fills, so the future continuous is the natural fit."
  },
  {
    prompt: "Where _____ you _____ while the flat is being painted? (stay)",
    hint: "Wh- question order.",
    correct: "will ... be staying",
    options: ["will ... be staying", "do ... be staying", "will ... staying", "will ... stay"],
    explain: "Wh- questions keep the same order: question word + will + subject + be + -ing."
  },
  {
    prompt: "I _____ her at the meeting anyway, so I'll pass it on. (see)",
    hint: "Something already going to happen \\u2014 nobody arranged it for this.",
    correct: "'ll be seeing",
    options: ["'ll be seeing", "'ll see", "see", "am seeing"],
    explain: "\\"I'll be seeing her anyway\\" says the meeting is happening regardless of your errand. That is exactly what this tense is for."
  },
  {
    prompt: "By this time on Sunday the race _____ . (still / run)",
    hint: "Still in progress at a future point.",
    correct: "will still be running",
    options: ["will still be running", "will still run", "is still running", "will be still run"],
    explain: "Still sits between will and be: will still be running."
  }
];
'''

NINE_PALETTE = '''  :root{
    --ink:#2C2004;
    --ink-soft:#725B24;
    --paper:#FDFAF2;
    --card:#FFFFFF;
    --accent:#C2860A;
    --accent-dark:#7A5200;
    --accent-light:#F5DCA8;
    --accent-lighter:#FCF2DE;
    --good:#1E7A4C;
    --good-bg:#E5F5EC;
    --bad:#B23A3A;
    --bad-bg:#FBEAEA;
    --radius:14px;
  }'''

assemble(NINE_HERO, NINE_CAMPS, NINE_JS, NINE_Q, NINE_PALETTE,
         '<title>Sherpa Tensing - Camp Nine: This Time Tomorrow (Future Continuous)</title>',
         [('shape-will', 'shape-fc'), ('panel-will', 'panel-fc'),
          ('"#E8632A"', '"#C98A00"'),
          ('/* ── NOW vs WILL DIAGRAM CAMP ── */', '/* ── NOW vs FUTURE CONTINUOUS DIAGRAM CAMP ── */'),
          ('// ── NOW vs WILL diagram interactivity ──', '// ── NOW vs FUTURE CONTINUOUS diagram interactivity ──'),
          ('"Clean run. You can tell a decision from a plan, and a belief from a forecast."',
           '"Clean run. You can hear the difference between doing and already doing."'),
          ('"Solid progress. Worth a look back at camp five before camp eight."',
           '"Solid progress. Worth a look back at camp seven before camp ten."'),
          ('"Good first attempt. The will do / will be doing fork is the part to read again."',
           '"Good first attempt. The will do / will be doing fork is the part to read again."'),
          ('"Good first attempt. The will/going to fork is the part to read again."',
           '"Good first attempt. The will do / will be doing fork is the part to read again."')],
         'sherpa-tensing-camp-nine-future-continuous.html')
print('camp nine written')

import os
os.remove('camp_diagrams.py')
