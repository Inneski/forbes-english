# -*- coding: utf-8 -*-
s = open('/tmp/pp_stage1.html', encoding='utf-8').read()

def swap(start_marker, end_marker, new):
    global s
    a = s.index(start_marker); b = s.index(end_marker, a)
    s = s[:a] + new + s[b:]

# ── HERO COPY ─────────────────────────────────────────────────────────
swap('<span class="eyebrow">', '<svg class="hero-diagram"',
'''<span class="eyebrow">Camp four &middot; present perfect simple</span>
      <h1>The rope still attached</h1>
      <p>Camp three was the ground you crossed and left. Camp four is the ground still roped to you. The present perfect describes a past that has not been cut loose &mdash; a period still running, an experience with no date on it, or something that happened moments ago and is still showing.</p>
    </div>
    ''')

# ── WHEN TO USE IT ────────────────────────────────────────────────────
swap('      <h2>When to use it</h2>', '    <div class="camp" id="form">',
'''      <h2>When to use it</h2>
      <div class="rule-grid">
        <div class="rule-card">
          <h3>An unfinished time period</h3>
          <p>The period started in the past and is still running now.</p>
          <div class="ex">"I have lived here for ten years." <em>&mdash; and I still do</em></div>
        </div>
        <div class="rule-card">
          <h3>An unspecified time</h3>
          <p>It happened, but when is not stated and does not matter.</p>
          <div class="ex">"Have you ever been to Scotland?"</div>
        </div>
        <div class="rule-card">
          <h3>A very recent action</h3>
          <p>Finished moments ago, with the result still in front of you.</p>
          <div class="ex">"Doris has just made coffee." <em>&mdash; it is still hot</em></div>
        </div>
        <div class="rule-card">
          <h3>Life experience, so far</h3>
          <p>A running total, counted up to the present moment.</p>
          <div class="ex">"I have been there a few times."</div>
        </div>
        <div class="rule-card">
          <h3>A change up to now</h3>
          <p>The situation is different from how it was.</p>
          <div class="ex">"The village has grown since the road opened."</div>
        </div>
        <div class="rule-card">
          <h3>Something still outstanding</h3>
          <p>Expected, not done yet &mdash; and the door is still open.</p>
          <div class="ex">"She hasn't sent the report yet."</div>
        </div>
      </div>
      <div class="chart-wrap">
        <h3>The line that decides it</h3>
        <p class="chart-note">Give the sentence a finished, stated time and it falls back to camp three. This is the single test that settles almost every case.</p>
        <table class="conj">
          <thead><tr><th>Time is&hellip;</th><th>Tense</th><th>Example</th></tr></thead>
          <tbody>
            <tr><td class="subj">Finished and stated</td><td>Past simple</td><td>I <em>moved</em> here ten years ago.</td></tr>
            <tr><td class="subj">Still running</td><td>Present perfect</td><td>I <em>have lived</em> here for ten years.</td></tr>
            <tr><td class="subj">Not stated at all</td><td>Present perfect</td><td>I <em>have been</em> to Scotland.</td></tr>
            <tr><td class="subj">Stated, once you ask</td><td>Past simple</td><td>I <em>went</em> in 2019.</td></tr>
          </tbody>
        </table>
      </div>
    </div>

''')

# ── HOW IT'S BUILT ────────────────────────────────────────────────────
swap("      <h2>How it's built</h2>", '    <div class="camp" id="signals">',
'''      <h2>How it's built</h2>
      <div class="form-grid">
        <div class="rule-card">
          <h3>Affirmative</h3>
          <p>subject + have / has + past participle</p>
          <div class="ex">"She has worked here for years."</div>
        </div>
        <div class="rule-card">
          <h3>Negative</h3>
          <p>subject + have not (haven't) / has not (hasn't) + past participle</p>
          <div class="ex">"They haven't finished yet."</div>
        </div>
        <div class="rule-card">
          <h3>Yes / No questions</h3>
          <p>Have / Has + subject + past participle?</p>
          <div class="ex">"Have you called her?"</div>
        </div>
        <div class="rule-card">
          <h3>Wh- questions</h3>
          <p>question word + have / has + subject + past participle?</p>
          <div class="ex">"How long have you known her?"</div>
        </div>
      </div>
      <div class="chart-wrap">
        <h3>Conjugation chart</h3>
        <p class="chart-note">Only the auxiliary changes &mdash; <em>has</em> for he, she and it, <em>have</em> for everyone else. The participle never moves. Using the verb "to work" as the model.</p>
        <table class="conj">
          <thead>
            <tr><th>Subject</th><th>Affirmative</th><th>Negative</th><th>Question</th></tr>
          </thead>
          <tbody>
            <tr><td class="subj">I</td><td>I have worked</td><td>I have not worked <em>(haven't)</em></td><td>Have I worked?</td></tr>
            <tr><td class="subj">You</td><td>You have worked</td><td>You have not worked <em>(haven't)</em></td><td>Have you worked?</td></tr>
            <tr><td class="subj">He</td><td>He has worked</td><td>He has not worked <em>(hasn't)</em></td><td>Has he worked?</td></tr>
            <tr><td class="subj">She</td><td>She has worked</td><td>She has not worked <em>(hasn't)</em></td><td>Has she worked?</td></tr>
            <tr><td class="subj">It</td><td>It has worked</td><td>It has not worked <em>(hasn't)</em></td><td>Has it worked?</td></tr>
            <tr><td class="subj">We</td><td>We have worked</td><td>We have not worked <em>(haven't)</em></td><td>Have we worked?</td></tr>
            <tr><td class="subj">They</td><td>They have worked</td><td>They have not worked <em>(haven't)</em></td><td>Have they worked?</td></tr>
          </tbody>
        </table>
      </div>
      <div class="chart-wrap">
        <h3>Irregular past participles worth carrying</h3>
        <p class="chart-note">The participle is the third form, and it is not always the past simple. Getting <em>went</em> and <em>been</em> the wrong way round is the most common slip at this camp.</p>
        <table class="conj">
          <thead><tr><th>Base</th><th>Past simple</th><th>Past participle</th></tr></thead>
          <tbody>
            <tr><td class="subj">be</td><td>was / were</td><td>been</td></tr>
            <tr><td class="subj">go</td><td>went</td><td>gone / been</td></tr>
            <tr><td class="subj">see</td><td>saw</td><td>seen</td></tr>
            <tr><td class="subj">eat</td><td>ate</td><td>eaten</td></tr>
            <tr><td class="subj">write</td><td>wrote</td><td>written</td></tr>
            <tr><td class="subj">take</td><td>took</td><td>taken</td></tr>
            <tr><td class="subj">do</td><td>did</td><td>done</td></tr>
          </tbody>
        </table>
      </div>
    </div>

''')

# ── SIGNAL WORDS ──────────────────────────────────────────────────────
swap('      <h2>Signal words</h2>', '    <div class="camp" id="past-now">',
'''      <h2>Signal words</h2>
      <div class="signal-groups">
        <div class="signal-box">
          <h3>Time still running</h3>
          <ul>
            <li>for &mdash; for ten years, for a while</li>
            <li>since &mdash; since 2019, since I moved</li>
            <li>so far, up to now</li>
            <li>today, this week, this year</li>
            <li>all my life</li>
          </ul>
        </div>
        <div class="signal-box">
          <h3>No time given</h3>
          <ul>
            <li>ever &mdash; Have you ever&hellip;?</li>
            <li>never</li>
            <li>before</li>
            <li>once, twice, a few times</li>
            <li>already</li>
          </ul>
        </div>
        <div class="signal-box">
          <h3>Only moments ago</h3>
          <ul>
            <li>just</li>
            <li>recently, lately</li>
            <li>yet &mdash; in questions and negatives</li>
            <li>still &mdash; still hasn't arrived</li>
          </ul>
        </div>
      </div>
      <div class="chart-wrap">
        <h3>The words that send you back to camp three</h3>
        <p class="chart-note">These name a finished time, so they take the past simple &mdash; never the present perfect.</p>
        <p style="font-size:14px;margin:0;">yesterday &middot; last night &middot; last week &middot; two days ago &middot; in 1990 &middot; when I was a child &middot; at six o'clock</p>
      </div>
    </div>

''')

open('/tmp/pp_stage2.html', 'w', encoding='utf-8').write(s)
print('content in')
