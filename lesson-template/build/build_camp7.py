# -*- coding: utf-8 -*-
"""Build Sherpa Tensing camp seven (future simple) from camp five.

Camp five is now the model for every future-facing camp: same engine, same
timeline diagram, same furniture. What changes here is the colour (the route
map already reserves #E8632A for camp seven), the block's caption, and all of
the content — because will and going to are the pair learners most often get
wrong, camp seven is written to point back at camp five constantly.
"""
import re, sys
sys.path.insert(0, 'lesson-template')
from sherpa_timeline import diagram, ramp

s = open('sherpa-tensing-camp-five-going-to.html', encoding='utf-8').read()

ORANGE = ramp('#F0813F', '#B44E17', '#4A1E06', '#1C0B02')
ARIA = ("A timeline running from past through now to the future. Now is a narrow "
        "column at the centre; will is a block standing in the future.")
HERO = diagram('willFade', ORANGE, None, 'WILL',
               'decided now &#183; predicted', 'will', aria=ARIA)
STAGE = diagram('willFadeB', ORANGE, None, 'WILL',
                'decided now &#183; predicted', 'will',
                aria=ARIA, classes='', groups=True).replace('<svg class=""', '<svg')

HERO_SECTION = '''<section class="hero" id="hero">
    <div>
      <span class="eyebrow">Camp seven &middot; future simple</span>
      <h1>The weather you can't see yet</h1>
      <p>Camp five was the route you'd already chosen. Camp seven is everything you haven't: the decision you make in the moment, the offer, the promise, and the prediction you can't point at any evidence for. <em>Will</em> is the future you believe in rather than the future you can see.</p>
    </div>
    ''' + HERO + '''
  </section>'''

CAMPS = '''<div class="camp" id="rules">
      <div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M5 3v18M5 4h11l-3 4 3 4H5"/></svg></div>
      <div class="camp-label">Basecamp briefing</div>
      <h2>When to use it</h2>
      <div class="rule-grid">
        <div class="rule-card">
          <h3>A decision made as you speak</h3>
          <p>You didn't plan it. You are deciding now, out loud.</p>
          <div class="ex">"That's the phone &mdash; I'll get it."</div>
        </div>
        <div class="rule-card">
          <h3>An offer</h3>
          <p>Volunteering to do something for someone.</p>
          <div class="ex">"I'll carry that for you."</div>
        </div>
        <div class="rule-card">
          <h3>A promise</h3>
          <p>Committing yourself, often with a time.</p>
          <div class="ex">"I'll have it finished by Friday."</div>
        </div>
        <div class="rule-card">
          <h3>A prediction or belief</h3>
          <p>What you think will happen, with no evidence to point at.</p>
          <div class="ex">"I think she'll get the job."</div>
        </div>
        <div class="rule-card">
          <h3>A refusal</h3>
          <p><em>Won't</em> is the strongest way to say no &mdash; even about objects.</p>
          <div class="ex">"He won't listen." &middot; "The car won't start."</div>
        </div>
        <div class="rule-card">
          <h3>A future fact</h3>
          <p>Something certain that nobody chose and nobody can change.</p>
          <div class="ex">"She'll be forty in March."</div>
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
          <p>subject + will + <strong>base verb</strong></p>
          <div class="ex">"I will call you." &middot; "I'll call you."</div>
        </div>
        <div class="rule-card">
          <h3>Negative</h3>
          <p>subject + will not (won't) + base verb</p>
          <div class="ex">"They won't agree to that."</div>
        </div>
        <div class="rule-card">
          <h3>Yes / No questions</h3>
          <p>Will + subject + base verb?</p>
          <div class="ex">"Will you be there?"</div>
        </div>
        <div class="rule-card">
          <h3>Wh- questions</h3>
          <p>question word + will + subject + base verb?</p>
          <div class="ex">"When will they announce it?"</div>
        </div>
      </div>
      <div class="chart-wrap">
        <h3>Conjugation chart</h3>
        <p class="chart-note"><em>Will</em> is a modal verb, and modals do not change for person &mdash; no <em>-s</em>, ever. The verb after it is always the bare infinitive.</p>
        <table class="conj">
          <thead>
            <tr><th>Subject</th><th>Affirmative</th><th>Negative</th><th>Question</th></tr>
          </thead>
          <tbody>
            <tr><td class="subj">I</td><td>I will arrive <em>(I'll)</em></td><td>I will not arrive <em>(won't)</em></td><td>Will I arrive?</td></tr>
            <tr><td class="subj">You</td><td>You will arrive <em>(you'll)</em></td><td>You will not arrive <em>(won't)</em></td><td>Will you arrive?</td></tr>
            <tr><td class="subj">He</td><td>He will arrive <em>(he'll)</em></td><td>He will not arrive <em>(won't)</em></td><td>Will he arrive?</td></tr>
            <tr><td class="subj">She</td><td>She will arrive <em>(she'll)</em></td><td>She will not arrive <em>(won't)</em></td><td>Will she arrive?</td></tr>
            <tr><td class="subj">It</td><td>It will arrive <em>(it'll)</em></td><td>It will not arrive <em>(won't)</em></td><td>Will it arrive?</td></tr>
            <tr><td class="subj">We</td><td>We will arrive <em>(we'll)</em></td><td>We will not arrive <em>(won't)</em></td><td>Will we arrive?</td></tr>
            <tr><td class="subj">They</td><td>They will arrive <em>(they'll)</em></td><td>They will not arrive <em>(won't)</em></td><td>Will they arrive?</td></tr>
          </tbody>
        </table>
      </div>
      <div class="chart-wrap">
        <h3>Shall &mdash; the one place it still lives</h3>
        <p class="chart-note">In modern English <em>shall</em> has almost vanished, except in questions with <em>I</em> and <em>we</em>, where it offers or suggests.</p>
        <table class="conj">
          <thead>
            <tr><th>Use</th><th>Example</th><th>Notes</th></tr>
          </thead>
          <tbody>
            <tr><td class="subj">Offering</td><td>Shall I open a window?</td><td>More natural than "Will I&hellip;?"</td></tr>
            <tr><td class="subj">Suggesting</td><td>Shall we start?</td><td>Invites the other person in.</td></tr>
            <tr><td class="subj">Formal writing</td><td>The tenant shall pay&hellip;</td><td>Contracts and law only.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="chart-wrap">
        <h3>Three mistakes worth naming</h3>
        <p class="chart-note">Nearly every error with <em>will</em> is one of these.</p>
        <table class="conj">
          <thead>
            <tr><th>Not this</th><th>This</th><th>Why</th></tr>
          </thead>
          <tbody>
            <tr><td class="subj">She wills come.</td><td>She will come.</td><td>Modals never take <em>-s</em>.</td></tr>
            <tr><td class="subj">I will to help you.</td><td>I will help you.</td><td>No <em>to</em> after a modal.</td></tr>
            <tr><td class="subj">When I will arrive, I'll call.</td><td>When I arrive, I'll call.</td><td>After <em>when</em>, <em>if</em>, <em>as soon as</em> and <em>until</em>, use the present.</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="camp" id="vs-going">
      <div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M12 3v18"/><path d="M7 8l-4 4 4 4M17 8l4 4-4 4"/></svg></div>
      <div class="camp-label">The fork in the path</div>
      <h2>Will or going to?</h2>
      <div class="chart-wrap" style="margin-top:18px">
        <p class="chart-note" style="margin-bottom:16px">Camp five and camp seven stand on the same square of the timeline. The question is never <em>when</em> &mdash; it is <strong>when the decision was made</strong> and <strong>what the prediction rests on</strong>.</p>
        <table class="conj">
          <thead>
            <tr><th>Situation</th><th>Will</th><th>Going to</th></tr>
          </thead>
          <tbody>
            <tr><td class="subj">The decision</td><td>Made <em>as</em> you speak.<br>"Fine &mdash; I'll do it myself."</td><td>Made <em>before</em> you spoke.<br>"I'm going to hand in my notice."</td></tr>
            <tr><td class="subj">The prediction</td><td>Opinion, belief, guess.<br>"I think it'll rain later."</td><td>Evidence you can point at.<br>"Look at those clouds &mdash; it's going to rain."</td></tr>
            <tr><td class="subj">Offers and promises</td><td>The natural choice.<br>"I'll help you move."</td><td>Not used.</td></tr>
            <tr><td class="subj">Refusals</td><td>"The engine won't start."</td><td>&mdash;</td></tr>
          </tbody>
        </table>
        <p class="example" style="margin-top:14px">Both are correct far more often than teachers admit. The test is whether the sentence would still be true if you had said nothing.</p>
      </div>
      <div class="btnrow" style="margin-top:16px">
        <a class="route-link" href="sherpa-tensing-camp-five-going-to.html">&larr; Camp five &middot; going to</a>
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
            <li>tomorrow / tonight</li>
            <li>next week / month / year</li>
            <li>in a moment / in an hour</li>
            <li>one day / some day</li>
            <li>by Friday / by then</li>
            <li>in 2050, in the future</li>
          </ul>
        </div>
        <div class="signal-box">
          <h3>Opinion and belief cues</h3>
          <ul>
            <li>I think&hellip; / I don't think&hellip;</li>
            <li>I'm sure&hellip; / I bet&hellip;</li>
            <li>probably, definitely, certainly</li>
            <li>I expect / I suppose / I hope</li>
            <li>perhaps, maybe</li>
            <li>I promise, don't worry</li>
          </ul>
        </div>
      </div>
      <p class="example" style="margin-top:14px">The opinion cues are the real giveaway: <em>I think</em>, <em>I'm sure</em> and <em>probably</em> almost always take <em>will</em>, because what follows is a belief and not a plan.</p>
    </div>

    <div class="camp" id="past-now">
      <div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><rect x="3" y="4" width="8" height="16"/><rect x="13" y="4" width="8" height="16"/></svg></div>
      <div class="camp-label">Interactive</div>
      <h2>Now vs. what you believe</h2>
      <div class="diagram-card">
        <p class="diagram-intro">The same line as camp five, in a different colour. <em>Will</em> stands in exactly the same place on it as <em>going to</em> &mdash; which is the point: the timeline cannot tell them apart, only the reason behind the sentence can. Click each block to name it and see it in a sentence.</p>
        <div class="diagram-stage">
          ''' + STAGE + '''
        </div>
        <div class="diagram-panels">
          <div class="diagram-panel is-now" id="panel-now">
            <h4>Now &mdash; where you're speaking from</h4>
            <ul id="panel-now-list"></ul>
          </div>
          <div class="diagram-panel" id="panel-will">
            <h4>Will &mdash; decided or believed</h4>
            <ul id="panel-will-list"></ul>
          </div>
        </div>
      </div>
    </div>

    '''

DIAGRAM_JS = '''var willExamples = [
  "I <em>'ll</em> get the door.",
  "I think it <em>will</em> rain later.",
  "The engine <em>won't</em> start."
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
renderList("panel-will-list", willExamples);
renderList("panel-now-list", nowExamples);

function pulseShape(el){
  el.style.transformOrigin = "center";
  el.animate(
    [{ opacity: 1 }, { opacity: 0.6 }, { opacity: 1 }],
    { duration: 380, easing: "ease-out" }
  );
}
["shape-will", "shape-now"].forEach(function(id){
  var el = document.getElementById(id);
  var activate = function(){
    pulseShape(el);
    document.querySelectorAll(".dg-reveal").forEach(function(t){
      t.classList.toggle("is-shown", t.dataset.for === id);
    });
    var panelId = id === "shape-will" ? "panel-will" : "panel-now";
    document.querySelectorAll(".diagram-panel").forEach(function(p){ p.style.outline = "none"; });
    document.getElementById(panelId).style.outline = "2px solid " + (id === "shape-will" ? "#E8632A" : "#5C7690");
  };
  el.addEventListener("click", activate);
  el.addEventListener("keydown", function(e){ if (e.key === "Enter" || e.key === " "){ e.preventDefault(); activate(); } });
});

'''

QUESTIONS = '''var questions = [
  {
    prompt: "\\"The phone's ringing.\\" \\"Don't get up \\u2014 I _____ answer it.\\"",
    hint: "You are deciding at this second.",
    correct: "'ll",
    options: ["'ll", "'m going to", "was going to", "am answering"],
    explain: "A decision taken at the moment of speaking takes will. Going to would mean you had planned to answer that call before it rang."
  },
  {
    prompt: "That bag looks heavy. _____ I carry it for you?",
    hint: "An offer, first person.",
    correct: "Shall",
    options: ["Shall", "Will", "Do", "Am"],
    explain: "Offers with I and we take shall in questions: Shall I carry it? \\"Will I carry it?\\" asks about the future, not about helping."
  },
  {
    prompt: "I promise I _____ tell anyone. (not / tell)",
    hint: "A promise, in the negative.",
    correct: "won't",
    options: ["won't", "don't", "am not going to", "will not to"],
    explain: "The negative of will is will not, contracted to won't. Promises are the natural home of will."
  },
  {
    prompt: "I think the meeting _____ longer than an hour. (last)",
    hint: "\\"I think\\" tells you which future this is.",
    correct: "will last",
    options: ["will last", "will lasts", "will to last", "is lasting"],
    explain: "Opinion cues like I think take will, and modals are followed by the bare infinitive: will last, never will lasts."
  },
  {
    prompt: "She _____ forty in March.",
    hint: "A future fact nobody decided.",
    correct: "will be",
    options: ["will be", "is going to be", "wills be", "will is"],
    explain: "Both will be and is going to be are heard, but a fixed future fact that nobody chose is the classic home of will."
  },
  {
    prompt: "_____ they _____ the results this week?",
    hint: "Question order with a modal.",
    correct: "Will ... publish",
    options: ["Will ... publish", "Will ... publishing", "Do ... will publish", "Will ... to publish"],
    explain: "Questions invert the modal: Will they publish? No do, no to, no -ing."
  },
  {
    prompt: "Careful with that shelf \\u2014 it _____ fall.",
    hint: "You can see it happening.",
    correct: "'s going to",
    options: ["'s going to", "'ll", "will be", "shall"],
    explain: "Visible evidence, seconds away: going to. Will here would sound like a distant prediction rather than a warning."
  },
  {
    prompt: "I've decided. I _____ apply for the transfer.",
    hint: "\\"I've decided\\" is the giveaway.",
    correct: "'m going to",
    options: ["'m going to", "'ll", "will have", "shall"],
    explain: "The decision was made before you spoke, so it takes going to. Will would contradict \\"I've decided\\"."
  },
  {
    prompt: "The lid _____ come off. I've tried three times. (not / come)",
    hint: "A refusal \\u2014 even from an object.",
    correct: "won't",
    options: ["won't", "doesn't", "isn't going to", "wouldn't"],
    explain: "Won't expresses refusal, and English extends that to things that will not cooperate: the lid won't come off."
  },
  {
    prompt: "Call me when you _____ at the station. (arrive)",
    hint: "What follows \\"when\\"?",
    correct: "arrive",
    options: ["arrive", "will arrive", "are arriving", "will have arrived"],
    explain: "After when, if, as soon as and until we use the present, even about the future: when you arrive, not when you will arrive."
  },
  {
    prompt: "If it rains tomorrow, we _____ the match. (cancel)",
    hint: "First conditional \\u2014 which half takes will?",
    correct: "will cancel",
    options: ["will cancel", "cancel", "are cancelling", "would cancel"],
    explain: "In a first conditional the if-half stays present and the result half takes will: If it rains, we will cancel."
  },
  {
    prompt: "Don't worry about the washing up \\u2014 I _____ it later.",
    hint: "An offer made on the spot.",
    correct: "'ll do",
    options: ["'ll do", "'m doing", "do", "will did"],
    explain: "An offer decided as you speak: I'll do it. \\"I'm doing it\\" would mean it was already arranged."
  },
  {
    prompt: "By 2050 most new cars _____ electric, experts say.",
    hint: "A long-range prediction.",
    correct: "will be",
    options: ["will be", "are", "are going to being", "will being"],
    explain: "A distant prediction with no visible evidence takes will + bare infinitive: will be."
  },
  {
    prompt: "He _____ listen to anyone about it. (not / listen)",
    hint: "Refusal again \\u2014 about a person this time.",
    correct: "won't",
    options: ["won't", "doesn't will", "isn't", "not will"],
    explain: "Won't listen means refuses to listen. It is stronger and more personal than \\"doesn't listen\\"."
  }
];
'''

# ── assemble ─────────────────────────────────────────────────────────
A = s.index('<section class="hero" id="hero">')
B = s.index('</section>', A) + len('</section>')
C = s.index('<div class="camp" id="rules">')
D = s.index('<div class="camp" id="quiz">')
E = s.index('var goingExamples = [')
F = s.index('// ── QUIZ ──')
G = s.index('var questions = [')
H = s.index('\nvar current = 0;')

out = s[:A] + HERO_SECTION + s[B:C] + CAMPS + s[D:E] + DIAGRAM_JS + s[F:G] + QUESTIONS + s[H:]

# ── palette: olive -> the route map's orange ─────────────────────────
palette = '''  :root{
    --ink:#2A1409;
    --ink-soft:#6E4a34;
    --paper:#FDF7F2;
    --card:#FFFFFF;
    --accent:#E8632A;
    --accent-dark:#A8410F;
    --accent-light:#F7D6C4;
    --accent-lighter:#FDEDE4;
    --good:#1E7A4C;
    --good-bg:#E5F5EC;
    --bad:#B23A3A;
    --bad-bg:#FBEAEA;
    --radius:14px;
  }'''
out = re.sub(r'  :root\{.*?\n  \}', palette, out, count=1, flags=re.S)

# a small link style for the pointer back to camp five
out = out.replace('  .quiz-card{',
  '''  .route-link{display:inline-flex;align-items:center;gap:7px;text-decoration:none;font-weight:600;font-size:14px;
    padding:9px 18px;border-radius:999px;border:1px solid var(--accent);color:var(--accent-dark);}
  .route-link:hover{background:var(--accent-lighter);}
  .quiz-card{''', 1)

out = out.replace(
  '<title>Sherpa Tensing - Camp Five: The Route Already Chosen (Going to + Infinitive)</title>',
  '<title>Sherpa Tensing - Camp Seven: The Weather You Can\'t See Yet (Future Simple)</title>', 1)
out = out.replace('/* ── NOW vs GOING TO DIAGRAM CAMP ── */', '/* ── NOW vs WILL DIAGRAM CAMP ── */', 1)
out = out.replace('// ── NOW vs GOING TO diagram interactivity ──', '// ── NOW vs WILL diagram interactivity ──', 1)
out = out.replace('"Route set. Every plan and every prediction in the right form."',
                  '"Clean run. You can tell a decision from a plan, and a belief from a forecast."', 1)
out = out.replace('"Solid progress. A couple of loose stones to check before camp six."',
                  '"Solid progress. Worth a look back at camp five before camp eight."', 1)
out = out.replace('"Good first attempt. Worth another pass before moving on."',
                  '"Good first attempt. The will/going to fork is the part to read again."', 1)

open('sherpa-tensing-camp-seven-future-simple.html', 'w', encoding='utf-8').write(out)
print('written', len(out), 'bytes')
for probe in ['goingExamples', 'panel-going', 'shape-going', 'planFade', '639922', 'GOING TO', 'going to + infinitive']:
    print('  leftover %-22r %d' % (probe, out.count(probe)))
print('  willFade:', out.count('willFade'), '| shape-will:', out.count('shape-will'), '| questions:', out.count('prompt:'))
