# -*- coding: utf-8 -*-
import re, json
MC = json.load(open('/tmp/ua_mc.json'))

GAP = [
 ("To put these staggering figures into ", "perspective", ", the World Bank now estimates total recovery needs at well over half a trillion dollars.",
  "<strong>Put figures into perspective</strong> — the phrase that makes a huge number mean something to an audience."),
 ("I'll keep my remarks ", "concise", ", so we leave ample room for questions at the end.",
  "<strong>Keep my remarks concise</strong> — brief and to the point. The only adjective that fits the frame."),
 ("Allow me to ", "outline", " the three pillars on which our proposal rests, before we examine each in detail.",
  "<strong>Outline</strong> previews structure. &ldquo;Before we examine each in detail&rdquo; signals an overview, not a summary."),
 ("This timeline, I must ", "stress", ", is contingent on a stable security environment throughout.",
  "A parenthetical <strong>I must stress</strong> puts weight on a caveat without breaking the sentence."),
 ("Having dealt with the costs, let me ", "turn", " to the equally pressing issue of oversight.",
  "<strong>Let me turn to</strong> is the standard signpost for moving to a new topic."),
 ("I'd be glad to ", "explore", " any of these themes in greater depth once I've finished.",
  "<strong>Explore in greater depth</strong> invites fuller discussion — the polite close before questions."),
]
BANK = ["perspective","concise","outline","stress","turn","explore","digress","recap","gloss"]

MATCH = [
 ('Testing your own argument by voicing the opposing view', '&ldquo;Let me play devil&rsquo;s advocate for a moment&hellip;&rdquo;'),
 ('Making an abstract figure relatable', '&ldquo;To give you a sense of scale, that&rsquo;s roughly the GDP of a mid-sized nation.&rdquo;'),
 ('Deferring a question politely', '&ldquo;That&rsquo;s a fair question — I&rsquo;ll come back to it, if I may, in just a moment.&rdquo;'),
 ('Introducing a qualifying point', '&ldquo;That said, the picture is not uniformly bleak.&rdquo;'),
 ('Flagging the single key message', '&ldquo;If you take one thing away today, let it be this.&rdquo;'),
 ('Hedging a claim, inviting correction', '&ldquo;Correct me if I&rsquo;m wrong, but my understanding is that funds are ring-fenced.&rdquo;'),
]

ORDER = [
 (["Before I outline our proposal,","let me briefly summarise","the scale of the damage."],
  "A subordinate clause of time first, then the main clause it frames."),
 (["While the costs are daunting,","we cannot afford","the cost of inaction."],
  "A concessive <em>while</em> clause sets up the reversal that follows."),
 (["Public funds will get us started,","but to finish the job,","the private sector will be essential."],
  "Two clauses joined by <em>but</em>, with a purpose phrase in the middle."),
 (["Before we move on,","let me address the elephant in the room:","the risk of corruption."],
  "Signpost, then the move, then the colon that names it."),
 (["And before I hand over,","I'd like to leave you with one thought:","recovery is not a cost but an investment."],
  "The classic closing frame: time clause, intention, then the thought itself."),
]

s = open('lesson-template/lesson-template.html', encoding='utf-8').read()
s = s.replace('<title>Lesson Title | Forbes English</title>',
              '<title>Presenting on the Reconstruction of Ukraine (C1) | Forbes English</title>')
s = s.replace("  --hero: url('sample-hero.jpg');   /* real lessons: url('<folder>/hero.jpg') */",
              "  --hero: url('Ukraine/reconstruction-hero.jpg');")
pal = {'--void':'#0c0b0b','--surface':'#191515','--surface2':'#231f1f','--border':'#aea495',
       '--text':'#f5f4f2','--text-dim':'#bfb4a3','--accent':'#e7d8c2','--accent-bright':'#fdbb5a',
       '--accent-dim':'#c9ad85','--secondary':'#c9a997','--contrast':'#31c5d8'}
for k,v in pal.items():
    s = re.sub(r'(\n  '+re.escape(k)+r'\s*: )#[0-9a-fA-F]{3,8};', lambda m: m.group(1)+v+';', s, count=1)
s = s.replace('  --bg-opacity: 0.34;', '  --bg-opacity: 0.44;')

def esc(x): return x.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')
def keep(x): return x.replace('&','&amp;')
def strip(x): return re.sub(r'<[^>]+>', lambda m: '', x)

body = ''
for i, q in enumerate(MC):
    n = i + 1
    opts = []
    for o in q['opts']:
        mark = ' data-correct' if o == q['answer'] else ''
        opts.append(f'          <button class="opt"{mark}>{keep(o)}</button>')
    fb = q['fb'].replace('<b>','<strong>').replace('</b>','</strong>')
    body += f'''
    <section class="slide" data-type="mc">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="a1e{n}">Precision vocabulary &middot; {n}/6</div>
        <h2 class="slide-title" data-i18n="a1t">Choose the exact word</h2>
      </div></div>
      <div class="slide-body">
        <p class="q-stem">{keep(q['q']).replace('___','<em>_______</em>')}</p>
        <div class="opts two-up">
{chr(10).join(opts)}
        </div>
        <p class="feedback" data-explain="{esc(fb)}"></p>
      </div>
    </section>
'''

BANKHTML = ' '.join(f'<span class="bank-chip">{w}</span>' for w in BANK)
PAIRS = [GAP[i:i+2] for i in range(0, len(GAP), 2)]
for pi, pair in enumerate(PAIRS):
    n = pi + 1
    rows = []
    for before, ans, after, ex in pair:
        rows.append(f'''        <div class="gap-row">
          <p class="q-stem">{keep(before)}<input class="gap" data-answer="{esc(ans)}" size="{len(ans)+3}" aria-label="gap">{keep(after)}</p>
          <p class="feedback" data-explain="{esc(ex)}"></p>
        </div>''')
    body += f'''
    <section class="slide" data-type="gap">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="a2e{n}">Signposting the talk &middot; {n}/3</div>
        <h2 class="slide-title" data-i18n="a2t">Complete the sentence</h2>
      </div></div>
      <div class="slide-body">
        <div class="bank">{BANKHTML}</div>
{chr(10).join(rows)}
        <div style="margin-top:16px">
          <button class="btn" data-action="check" data-i18n="btnCheck">Check</button>
        </div>
      </div>
    </section>
'''

pairs = [f'          <div class="match-pair" data-term="{esc(t)}" data-def="{d}"></div>' for t, d in MATCH]
body += f'''
    <section class="slide" data-type="match" data-bg="Ukraine/reconstruction-hero.jpg">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="a3e">What the phrase is doing &middot; 6 pairs</div>
        <h2 class="slide-title" data-i18n="a3t">Match the move to the words</h2>
      </div></div>
      <div class="slide-body">
        <div class="match-grid">
{chr(10).join(pairs)}
        </div>
        <p class="feedback" data-explain="Every one of these is a rhetorical move, not just a phrase: conceding, deferring, scaling, hedging. Naming the move is what lets you use it deliberately."></p>
      </div>
    </section>
'''

for i, (chunks, ex) in enumerate(ORDER):
    n = i + 1
    body += f'''
    <section class="slide" data-type="order">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="a4e{n}">Building the sentence &middot; {n}/5</div>
        <h2 class="slide-title" data-i18n="a4t">Put the presenter&rsquo;s line together</h2>
      </div></div>
      <div class="slide-body">
        <div class="order-hint" data-i18n="orderHint">Click the parts in order &middot; click one again to take it back</div>
        <div class="order" data-answer="{esc('|'.join(chunks))}"></div>
        <div style="margin-top:18px">
          <button class="btn" data-action="check-order" data-i18n="btnCheck">Check</button>
        </div>
        <p class="feedback" data-explain="{esc(ex)}"></p>
      </div>
    </section>
'''

start = s.index('    <!-- ── TEACHING SLIDE ───────────────────────────────────── -->')
end   = s.index('    <!-- ── RESULTS ──────────────────────────────────────────── -->')
s = s[:start] + body + '\n' + s[end:]

s = s.replace('''          <span class="bank-chip">target phrase</span>
          <span class="bank-chip">target phrase</span>
          <span class="bank-chip">target phrase</span>
          <span class="bank-chip">target phrase</span>''',
'''          <span class="bank-chip">to put it into perspective</span>
          <span class="bank-chip">contingent on</span>
          <span class="bank-chip">let me turn to</span>
          <span class="bank-chip">I must stress</span>
          <span class="bank-chip">that said</span>
          <span class="bank-chip">if you take one thing away</span>''')

s = s.replace('.q-stem {', '.bank { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 18px; }\n.gap-row + .gap-row { margin-top: 22px; }\n.q-stem {', 1)
open('/tmp/ua_stage1.html','w',encoding='utf-8').write(s)
print('slides:', body.count('<section'))
