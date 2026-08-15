# -*- coding: utf-8 -*-
"""Build Sherpa Tensing camp five (going to + infinitive) from camp three.

The engine, the CSS and the page furniture are camp three's, unchanged — the
route is meant to feel like one continuous climb. What changes:

  * the palette goes from the past-simple brown to the route map's olive
    (#639922, already reserved for camp five on the map);
  * the hero diagram is camp three's composition mirrored about the canvas
    centre, so the NOW column is untouched but the block now stands on the
    other side of it — ahead in time instead of behind;
  * new content: rules, form, a going-to vs will camp, signals, quiz.
"""
import re

s = open('sherpa-tensing-camp-three-past-simple.html', encoding='utf-8').read()

# ── the diagram, mirrored ────────────────────────────────────────────
# Every x becomes 640-x. The NOW column keeps its exact width and colours
# (17px coral behind 12px blue) and simply moves to the left; the block keeps
# its shape and its perspective and moves to the right, so time still reads
# left to right and the future sits after now instead of before it.
DEFS = '''      <defs>
        <linearGradient id="planFade" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0"    stop-color="#7FB52C"/>
          <stop offset="0.42" stop-color="#4A731A"/>
          <stop offset="0.78" stop-color="#1E2E0B"/>
          <stop offset="1"    stop-color="#0C1204"/>
        </linearGradient>
      </defs>
      <rect x="0" y="0" width="640" height="344" fill="var(--paper)"/>
      <line x1="28" y1="299" x2="349" y2="299" stroke="#171c0c" stroke-width="2"/>'''

BLOCK = '<path d="M518,38 L458,38 L458,299 L349,299 L416,326 L608,326 L608,264 L518,264 Z" fill="url(#planFade)"/>'
NOWCOL = ('<rect x="186.5" y="38" width="17.0" height="261" fill="#D98A72"/>\n'
          '      <rect x="189.0" y="40.5" width="12.0" height="256" fill="#5C7690"/>')

LABELS = '''      <text x="592" y="292" text-anchor="end" class="diagram-caption" fill="#EEF3E2" style="letter-spacing:.08em" pointer-events="none">GOING TO</text>
      <text x="195" y="26" text-anchor="middle" class="diagram-caption" fill="#3E6A85" pointer-events="none">NOW</text>
      <text x="592" y="311" text-anchor="end" class="dg-reveal" data-for="shape-going" font-family="Inter, sans-serif" font-size="11.5" fill="#C6CFB2" pointer-events="none">already decided &#183; already visible</text>
      <text x="195" y="317" text-anchor="middle" class="dg-reveal" data-for="shape-now" font-family="Inter, sans-serif" font-size="11.5" fill="#5F7C90" pointer-events="none">present simple</text>'''

HERO = '''<section class="hero" id="hero">
    <div>
      <span class="eyebrow">Camp five &middot; going to + infinitive</span>
      <h1>The route already chosen</h1>
      <p>Camp four kept a rope attached to now. Camp five turns you round to face the ridge above. <em>Going to</em> is the future you can already see from where you stand &mdash; a plan you've made, or evidence in front of you that makes the next step certain.</p>
    </div>
    <svg class="hero-diagram" viewBox="0 0 640 344" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Now as a narrow column, and going to as a block standing after it">
''' + DEFS + '''
      ''' + NOWCOL + '''
      ''' + BLOCK + '''
''' + LABELS + '''
    </svg>
  </section>'''

# ── camps: rules, form, will-vs-going-to, signals, the diagram ───────
CAMPS = '''<div class="camp" id="rules">
      <div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M5 3v18M5 4h11l-3 4 3 4H5"/></svg></div>
      <div class="camp-label">Basecamp briefing</div>
      <h2>When to use it</h2>
      <div class="rule-grid">
        <div class="rule-card">
          <h3>A plan made in advance</h3>
          <p>You decided before this conversation started.</p>
          <div class="ex">"We're going to renovate the kitchen in the spring."</div>
        </div>
        <div class="rule-card">
          <h3>An intention</h3>
          <p>What you mean to do, whether or not it's arranged.</p>
          <div class="ex">"I'm going to tell her tonight."</div>
        </div>
        <div class="rule-card">
          <h3>A prediction from evidence</h3>
          <p>Something you can see, hear or feel right now points to it.</p>
          <div class="ex">"Look at those clouds &mdash; it's going to rain."</div>
        </div>
        <div class="rule-card">
          <h3>Something on the point of happening</h3>
          <p>Already in motion, seconds away.</p>
          <div class="ex">"Careful &mdash; that shelf is going to fall."</div>
        </div>
        <div class="rule-card">
          <h3>Where things are heading</h3>
          <p>Reading the current trend forward.</p>
          <div class="ex">"At this rate, they're going to miss the deadline."</div>
        </div>
        <div class="rule-card">
          <h3>The plan that never happened</h3>
          <p>was / were going to &mdash; an intention overtaken by events.</p>
          <div class="ex">"I was going to call you, but the meeting overran."</div>
        </div>
      </div>
    </div>

    <div class="camp" id="form">
      <div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M9 4v16"/></svg></div>
      <div class="camp-label">Building the tense</div>
      <h2>How it's built</h2>
      <div class="form-grid">
        <div class="rule-card">
          <h3>Affirmative</h3>
          <p>subject + am / is / are + going to + <strong>base verb</strong></p>
          <div class="ex">"She's going to apply." &middot; "They're going to wait."</div>
        </div>
        <div class="rule-card">
          <h3>Negative</h3>
          <p>subject + am / is / are + not + going to + base verb</p>
          <div class="ex">"They aren't going to wait."</div>
        </div>
        <div class="rule-card">
          <h3>Yes / No questions</h3>
          <p>Am / Is / Are + subject + going to + base verb?</p>
          <div class="ex">"Are you going to accept the offer?"</div>
        </div>
        <div class="rule-card">
          <h3>Wh- questions</h3>
          <p>question word + am / is / are + subject + going to + base verb?</p>
          <div class="ex">"When are you going to tell him?"</div>
        </div>
      </div>
      <div class="chart-wrap">
        <h3>Conjugation chart</h3>
        <p class="chart-note">Only <em>be</em> changes. <em>Going to</em> never changes, and the verb after it is always the bare infinitive &mdash; using "to travel" as the model.</p>
        <table class="conj">
          <thead>
            <tr><th>Subject</th><th>Affirmative</th><th>Negative</th><th>Question</th></tr>
          </thead>
          <tbody>
            <tr><td class="subj">I</td><td>I am going to travel <em>(I'm)</em></td><td>I am not going to travel <em>(I'm not)</em></td><td>Am I going to travel?</td></tr>
            <tr><td class="subj">You</td><td>You are going to travel <em>(you're)</em></td><td>You are not going to travel <em>(aren't)</em></td><td>Are you going to travel?</td></tr>
            <tr><td class="subj">He</td><td>He is going to travel <em>(he's)</em></td><td>He is not going to travel <em>(isn't)</em></td><td>Is he going to travel?</td></tr>
            <tr><td class="subj">She</td><td>She is going to travel <em>(she's)</em></td><td>She is not going to travel <em>(isn't)</em></td><td>Is she going to travel?</td></tr>
            <tr><td class="subj">It</td><td>It is going to travel <em>(it's)</em></td><td>It is not going to travel <em>(isn't)</em></td><td>Is it going to travel?</td></tr>
            <tr><td class="subj">We</td><td>We are going to travel <em>(we're)</em></td><td>We are not going to travel <em>(aren't)</em></td><td>Are we going to travel?</td></tr>
            <tr><td class="subj">They</td><td>They are going to travel <em>(they're)</em></td><td>They are not going to travel <em>(aren't)</em></td><td>Are they going to travel?</td></tr>
          </tbody>
        </table>
      </div>
      <div class="chart-wrap">
        <h3>The plan that didn't happen: was / were going to</h3>
        <p class="chart-note">Put <em>be</em> into the past and the whole structure becomes an intention that something interrupted. The sentence usually needs a "but".</p>
        <table class="conj">
          <thead>
            <tr><th>Subject</th><th>Affirmative</th><th>Negative</th><th>Question</th></tr>
          </thead>
          <tbody>
            <tr><td class="subj">I / He / She / It</td><td>I was going to call</td><td>I wasn't going to call</td><td>Was I going to call?</td></tr>
            <tr><td class="subj">You / We / They</td><td>We were going to call</td><td>We weren't going to call</td><td>Were we going to call?</td></tr>
          </tbody>
        </table>
      </div>
      <div class="chart-wrap">
        <h3>Three mistakes worth naming</h3>
        <p class="chart-note">Almost every error with this structure is one of these three.</p>
        <table class="conj">
          <thead>
            <tr><th>Not this</th><th>This</th><th>Why</th></tr>
          </thead>
          <tbody>
            <tr><td class="subj">I going to leave.</td><td>I'm going to leave.</td><td><em>Be</em> is not optional &mdash; it carries the person and the tense.</td></tr>
            <tr><td class="subj">She's going to leaving.</td><td>She's going to leave.</td><td>What follows <em>going to</em> is always the bare infinitive.</td></tr>
            <tr><td class="subj">Do you going to come?</td><td>Are you going to come?</td><td>Questions invert <em>be</em>. <em>Do</em> has no job here.</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="camp" id="vs-will">
      <div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M12 3v18"/><path d="M7 8l-4 4 4 4M17 8l4 4-4 4"/></svg></div>
      <div class="camp-label">The fork in the path</div>
      <h2>Going to or will?</h2>
      <div class="chart-wrap" style="margin-top:18px">
        <p class="chart-note" style="margin-bottom:16px">Both talk about the future. The difference is <strong>when the decision was made</strong> and <strong>what the prediction rests on</strong>. Camp seven covers <em>will</em> properly; this is the part you need now.</p>
        <table class="conj">
          <thead>
            <tr><th>Situation</th><th>Going to</th><th>Will</th></tr>
          </thead>
          <tbody>
            <tr><td class="subj">The decision</td><td>Made <em>before</em> you spoke.<br>"I'm going to hand in my notice."</td><td>Made <em>as</em> you speak.<br>"Fine &mdash; I'll do it myself."</td></tr>
            <tr><td class="subj">The prediction</td><td>Based on evidence you can point at.<br>"She's going to win &mdash; she's two laps ahead."</td><td>Based on opinion or belief.<br>"I think she'll win."</td></tr>
            <tr><td class="subj">Offers and promises</td><td>Not used.</td><td>The natural choice.<br>"I'll carry that for you."</td></tr>
            <tr><td class="subj">The phone rings</td><td>&mdash;</td><td>"I'll get it."</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="camp" id="signals">
      <div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/></svg></div>
      <div class="camp-label">Trail markers</div>
      <h2>Signal words</h2>
      <div class="signal-groups">
        <div class="signal-box">
          <h3>Future time markers</h3>
          <ul>
            <li>tonight / tomorrow / tomorrow morning</li>
            <li>next week / month / summer / year</li>
            <li>in two days / in a fortnight</li>
            <li>this evening / at the weekend</li>
            <li>soon, shortly, later</li>
            <li>on Friday, after lunch</li>
          </ul>
        </div>
        <div class="signal-box">
          <h3>Evidence and intention cues</h3>
          <ul>
            <li>look!, watch out!, careful!</li>
            <li>at this rate, the way things are going</li>
            <li>judging by, by the look of it</li>
            <li>I've decided to&hellip;, the plan is to&hellip;</li>
            <li>any minute now, any moment</li>
            <li>&hellip;but (after was / were going to)</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="camp" id="past-now">
      <div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><rect x="3" y="4" width="8" height="16"/><rect x="13" y="4" width="8" height="16"/></svg></div>
      <div class="camp-label">Interactive</div>
      <h2>Now vs. what's already decided</h2>
      <div class="diagram-card">
        <p class="diagram-intro">Now is the narrow column you're standing in. <em>Going to</em> is the block on the other side of it &mdash; the same solid shape as camp three's past, but ahead of you instead of behind: decided, or already visible, and leaning into time you haven't reached yet. Click each block to name it and see it in a sentence.</p>
        <div class="diagram-stage">
          <svg viewBox="0 0 640 344" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Diagram: now as a narrow column, and going to as a block after it">
''' + DEFS + '''
      <g class="diagram-shape" id="shape-now" tabindex="0" role="button" aria-label="Show present simple examples">
      ''' + NOWCOL + '''
      </g>
      <g class="diagram-shape" id="shape-going" tabindex="0" role="button" aria-label="Show going to examples">
      ''' + BLOCK + '''
      </g>
''' + LABELS + '''
          </svg>
        </div>
        <div class="diagram-panels">
          <div class="diagram-panel is-now" id="panel-now">
            <h4>Now &mdash; where you're speaking from</h4>
            <ul id="panel-now-list"></ul>
          </div>
          <div class="diagram-panel" id="panel-going">
            <h4>Going to &mdash; decided, in motion</h4>
            <ul id="panel-going-list"></ul>
          </div>
        </div>
      </div>
    </div>

    '''

DIAGRAM_JS = '''var goingExamples = [
  "We <em>are going to</em> leave at dawn.",
  "It <em>'s going to</em> rain &mdash; look at that sky.",
  "I <em>'m going to</em> tell her tonight."
];
var nowExamples = [
  "We <em>are</em> at the col.",
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
renderList("panel-going-list", goingExamples);
renderList("panel-now-list", nowExamples);

function pulseShape(el){
  el.style.transformOrigin = "center";
  el.animate(
    [{ opacity: 1 }, { opacity: 0.6 }, { opacity: 1 }],
    { duration: 380, easing: "ease-out" }
  );
}
["shape-going", "shape-now"].forEach(function(id){
  var el = document.getElementById(id);
  var activate = function(){
    pulseShape(el);
    document.querySelectorAll(".dg-reveal").forEach(function(t){
      t.classList.toggle("is-shown", t.dataset.for === id);
    });
    var panelId = id === "shape-going" ? "panel-going" : "panel-now";
    document.querySelectorAll(".diagram-panel").forEach(function(p){ p.style.outline = "none"; });
    document.getElementById(panelId).style.outline = "2px solid " + (id === "shape-going" ? "#639922" : "#5C7690");
  };
  el.addEventListener("click", activate);
  el.addEventListener("keydown", function(e){ if (e.key === "Enter" || e.key === " "){ e.preventDefault(); activate(); } });
});

'''

QUESTIONS = '''var questions = [
  {
    prompt: "Look at those clouds \\u2014 it _____ rain.",
    hint: "The evidence is in front of you.",
    correct: "is going to",
    options: ["is going to", "is going", "goes to", "will going to"],
    explain: "A prediction based on evidence you can see takes be + going to + base verb: it is going to rain."
  },
  {
    prompt: "We _____ the kitchen next spring. (be going to / renovate)",
    hint: "A plan made well before now.",
    correct: "are going to renovate",
    options: ["are going to renovate", "are going to renovating", "is going to renovate", "are going renovate"],
    explain: "The subject is plural, so be is are; and what follows going to is always the bare infinitive: are going to renovate."
  },
  {
    prompt: "She _____ apply for the job \\u2014 she decided last night.",
    hint: "The decision came before the conversation.",
    correct: "is going to",
    options: ["is going to", "is going", "goes to", "will"],
    explain: "A decision already made before speaking takes going to. Will would suggest she decided at this moment."
  },
  {
    prompt: "He's going to _____ the report tomorrow. (finish)",
    hint: "What form follows \\"going to\\"?",
    correct: "finish",
    options: ["finish", "finishes", "finishing", "finished"],
    explain: "Going to is always followed by the bare infinitive: going to finish. Never going to finishing."
  },
  {
    prompt: "They _____ wait any longer. (not / be going to)",
    hint: "Negative: put not after be.",
    correct: "aren't going to",
    options: ["aren't going to", "don't going to", "aren't go to", "isn't going to"],
    explain: "The negative is formed on be, not with do: they aren't going to wait."
  },
  {
    prompt: "I _____ argue about it. (not / be going to)",
    hint: "First person singular.",
    correct: "am not going to",
    options: ["am not going to", "amn't going to", "don't going to", "am not go to"],
    explain: "I takes am, and the negative is am not (contracted as I'm not). \\"Amn't\\" is not standard English."
  },
  {
    prompt: "_____ you _____ tell him tonight?",
    hint: "Questions invert be \\u2014 no auxiliary do.",
    correct: "Are ... going to",
    options: ["Are ... going to", "Do ... going to", "Are ... go to", "Will ... going to"],
    explain: "Yes/No questions move be in front of the subject: Are you going to tell him?"
  },
  {
    prompt: "When _____ she _____ announce it?",
    hint: "Wh- word + be + subject + going to + base verb.",
    correct: "is ... going to",
    options: ["is ... going to", "does ... going to", "is ... go to", "will ... going to"],
    explain: "Wh- questions keep the same inversion: When is she going to announce it?"
  },
  {
    prompt: "I _____ call you, but the meeting overran.",
    hint: "An intention that something interrupted.",
    correct: "was going to",
    options: ["was going to", "am going to", "were going to", "have going to"],
    explain: "Put be into the past and going to describes a plan that never happened: I was going to call you, but\\u2026"
  },
  {
    prompt: "We _____ leave early, but the road was closed.",
    hint: "Same structure, plural subject.",
    correct: "were going to",
    options: ["were going to", "was going to", "are going to", "will be going to"],
    explain: "We takes were: we were going to leave. The \\"but\\" is what tells you the plan failed."
  },
  {
    prompt: "\\"The phone's ringing.\\" \\"Don't worry \\u2014 I _____ answer it.\\"",
    hint: "The decision is being made this second.",
    correct: "'ll",
    options: ["'ll", "'m going to", "was going to", "go to"],
    explain: "A decision made at the moment of speaking takes will. Going to would mean you had planned to answer the phone before it rang."
  },
  {
    prompt: "Careful! You _____ drop that.",
    hint: "You can see it happening.",
    correct: "'re going to",
    options: ["'re going to", "'ll", "were going to", "go to"],
    explain: "Visible evidence, something on the point of happening: you're going to drop that. Will here would sound like a distant prediction."
  },
  {
    prompt: "At this rate, the team _____ miss the deadline.",
    hint: "Reading the current trend forward.",
    correct: "is going to",
    options: ["is going to", "are going to", "is go to", "will going to"],
    explain: "\\"The team\\" is treated as singular here, so it takes is; and the trend in front of you calls for going to."
  },
  {
    prompt: "First we're going to check the ropes, then we _____ set off at dawn.",
    hint: "The second half of one agreed plan.",
    correct: "'re going to",
    options: ["'re going to", "going to", "'re go to", "are went to"],
    explain: "Both halves of the plan use the same structure: we're going to check\\u2026 then we're going to set off. Going to on its own, with no form of be, is the most common error of all."
  }
];
'''

# ── assemble ─────────────────────────────────────────────────────────
A = s.index('<section class="hero" id="hero">')
B = s.index('</section>', A) + len('</section>')
C = s.index('<div class="camp" id="rules">')
D = s.index('<div class="camp" id="quiz">')
E = s.index('var pastExamples = [')
F = s.index('// ── QUIZ ──')
G = s.index('var questions = [')
H = s.index('\nvar current = 0;')

out = s[:A] + HERO + s[B:C] + CAMPS + s[D:E] + DIAGRAM_JS + s[F:G] + QUESTIONS + s[H:]

# ── palette: brown -> olive ──────────────────────────────────────────
palette = '''  :root{
    --ink:#22260F;
    --ink-soft:#5C6440;
    --paper:#F8F8EF;
    --card:#FFFFFF;
    --accent:#639922;
    --accent-dark:#456A17;
    --accent-light:#D9E6C2;
    --accent-lighter:#EEF4E1;
    --good:#1E7A4C;
    --good-bg:#E5F5EC;
    --bad:#B23A3A;
    --bad-bg:#FBEAEA;
    --radius:14px;
  }'''
out = re.sub(r'  :root\{.*?\n  \}', palette, out, count=1, flags=re.S)

# ── chrome ───────────────────────────────────────────────────────────
out = out.replace(
  '<title>Sherpa Tensing - Camp Three: The Camp Behind You (Past Simple)</title>',
  '<title>Sherpa Tensing - Camp Five: The Route Already Chosen (Going to + Infinitive)</title>', 1)
out = out.replace('/* ── PAST vs NOW DIAGRAM CAMP ── */',
                  '/* ── NOW vs GOING TO DIAGRAM CAMP ── */', 1)

# Clicking a shape was leaving the browser's focus rectangle drawn round the
# whole group. Keyboard users still get a ring; mouse users don't.
out = out.replace('  .diagram-shape:hover{opacity:.86;}',
                  '  .diagram-shape:hover{opacity:.86;}\n'
                  '  .diagram-shape:focus{outline:none;}\n'
                  '  .diagram-shape:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:4px;}', 1)
out = out.replace('// ── PAST vs NOW diagram interactivity ──',
                  '// ── NOW vs GOING TO diagram interactivity ──', 1)

# ── summit log wording ───────────────────────────────────────────────
out = out.replace('"Camp struck. Every step behind you accounted for."',
                  '"Route set. Every plan and every prediction in the right form."', 1)
out = out.replace('"Solid progress. A couple of loose stones to check before camp four."',
                  '"Solid progress. A couple of loose stones to check before camp six."', 1)

# The hero and the interactive stage carry the same gradient, so the second
# copy is renamed — camp three shipped with a duplicate id, which is invalid
# and only works because the two definitions happen to be identical.
i = out.index('id="planFade"', out.index('id="planFade"') + 1)
tail = out[i:].replace('id="planFade"', 'id="planFadeB"', 1).replace('url(#planFade)', 'url(#planFadeB)', 1)
out = out[:i] + tail

open('sherpa-tensing-camp-five-going-to.html', 'w', encoding='utf-8').write(out)
print('written', len(out), 'bytes')
for probe in ['pastExamples', 'panel-past', 'shape-past', 'pastFade', 'B08968', 'Past simple', 'past simple']:
    print(f'  leftover {probe!r}:', out.count(probe))
print('  planFade:', out.count('planFade'), '| shape-going:', out.count('shape-going'),
      '| questions:', out.count('prompt:'))
