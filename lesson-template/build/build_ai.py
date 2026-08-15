# -*- coding: utf-8 -*-
import re, json
D = json.load(open('/tmp/ai.json'))

HERO = 'AILearning/retro-desk-sunset.jpg'
ALT  = 'AILearning/vr-goggles-surveillance.jpg'

ORDER_CHUNKS = [
    "She founds a social enterprise",
    "UK literacy figures shock her",
    "She names two systemic failures",
    "A survey exposes AI homework",
    "She sets out four techniques",
    "Effort: a feature, not a flaw",
]
ORDER_EX = ("The talk is built as a narrowing argument: a global philanthropic project, "
            "a domestic statistic that undermines it, the two failures behind that statistic, "
            "the evidence that AI is deepening rather than solving them, the four techniques "
            "that do work, and finally the reframe &mdash; effort is the mechanism, not the obstacle.")

s = open('lesson-template/lesson-template.html', encoding='utf-8').read()
s = s.replace('<title>Lesson Title | Forbes English</title>',
              '<title>AI, Learning &amp; the Productive Struggle (C1) | Forbes English</title>')
s = s.replace("  --hero: url('sample-hero.jpg');   /* real lessons: url('<folder>/hero.jpg') */",
              f"  --hero: url('{HERO}');")
pal = {'--void':'#090e09','--surface':'#121c12','--surface2':'#1a291a','--border':'#a44948',
       '--text':'#f5f2f2','--text-dim':'#bfa3a3','--accent':'#e46f6e','--accent-bright':'#f2a8a7',
       '--accent-dim':'#c92e2d','--secondary':'#144b6f','--contrast':'#1ded8b'}
for k,v in pal.items():
    s = re.sub(r'(\n  '+re.escape(k)+r'\s*: )#[0-9a-fA-F]{3,8};', lambda m,v=v: m.group(1)+v+';', s, count=1)
s = s.replace('  --bg-opacity: 0.34;', '  --bg-opacity: 0.40;')

def esc(x): return x.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')
def keep(x): return x.replace('&','&amp;').replace('"','&quot;')

def smart(x):
    """Straight quotes in source data -> typographic entities."""
    x = x.replace('&','&amp;')
    out, open_d, open_s = [], True, True
    for ch in x:
        if ch == '"':
            out.append('&ldquo;' if open_d else '&rdquo;'); open_d = not open_d
        elif ch == "'":
            out.append('&rsquo;')
        else:
            out.append(ch)
    return ''.join(out)

body = ''

# ── TEACH 1 : the argument ────────────────────────────────────────────
body += '''
    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="t1e">The claim</div>
        <h2 class="slide-title" data-i18n="t1t">Fluency is not learning</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols">
          <div class="card">
            <p class="prose" data-i18n="t1a">
              Reading something that is <strong>smoothly written</strong> feels like
              understanding it. That feeling is the <em>illusion of competence</em> &mdash;
              the ease of processing mistaken for mastery. AI writes fluently by design,
              so it manufactures that feeling on demand.
            </p>
          </div>
          <div class="card">
            <p class="prose" data-i18n="t1b">
              Durable learning comes from the opposite experience: <strong>effortful
              retrieval</strong>. If it felt hard to get back out of your memory, it is
              more likely to still be there next week. The struggle is the mechanism,
              not the obstacle.
            </p>
          </div>
        </div>
        <div class="card" style="margin-top:16px">
          <p class="prose dim" data-i18n="t1n">
            The question the talk poses is not whether AI is good or bad, but whether
            you are using it to <strong>complement</strong> your thinking or to
            <strong>replace</strong> it.
          </p>
        </div>
      </div>
    </section>
'''

# ── TEACH 2 : four techniques ─────────────────────────────────────────
body += f'''
    <section class="slide" data-type="teach" data-bg="{ALT}">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="t2e">The evidence</div>
        <h2 class="slide-title" data-i18n="t2t">Four things that actually work</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols">
          <div class="card">
            <p class="prose" data-i18n="t2a">
              <strong>Retrieval</strong> &mdash; close the book and reconstruct it from
              memory. <strong>Spacing</strong> &mdash; return to it days apart rather
              than in one sitting.
            </p>
          </div>
          <div class="card">
            <p class="prose" data-i18n="t2b">
              <strong>Generation</strong> &mdash; attempt the answer before you are told
              it, even badly. <strong>Reflection</strong> &mdash; ask what you now know
              that you did not an hour ago.
            </p>
          </div>
        </div>
        <div class="card" style="margin-top:16px">
          <p class="prose dim" data-i18n="t2n">
            Every one of the four feels <em>worse</em> in the moment than re-reading
            does &mdash; and every one of the four outperforms it. Comfort is a poor
            signal of progress.
          </p>
        </div>
      </div>
    </section>
'''

# ── MC : comprehension ────────────────────────────────────────────────
def mc_slide(q, n, total, ekey, tkey):
    opts = []
    for i, o in enumerate(q['opts']):
        mark = ' data-correct' if i == q['ans'] else ''
        opts.append(f'          <button class="opt"{mark}>{smart(o)}</button>')
    return f'''
    <section class="slide" data-type="mc">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="{ekey}{n}">{tkey[1]} &middot; {n}/{total}</div>
        <h2 class="slide-title" data-i18n="{tkey[0]}">{tkey[2]}</h2>
      </div></div>
      <div class="slide-body">
        <p class="q-ctx">{smart(q['ctx'])}</p>
        <p class="q-stem">{smart(q['q'])}</p>
        <div class="opts two-up">
{chr(10).join(opts)}
        </div>
        <p class="feedback" data-explain="{esc(q['why'])}"></p>
      </div>
    </section>
'''

for i, q in enumerate(D['mc']):
    body += mc_slide(q, i+1, 6, 'a1e', ('a1t', 'The argument', 'What the speaker is claiming'))
for i, q in enumerate(D['vocab']):
    body += mc_slide(q, i+1, 6, 'a2e', ('a2t', 'Precision vocabulary', 'What the word is doing here'))

# ── MATCH ─────────────────────────────────────────────────────────────
pairs = [f'          <div class="match-pair" data-term="{esc(m["term"])}" data-def="{esc(m["def"])}"></div>'
         for m in D['match']]
body += f'''
    <section class="slide" data-type="match" data-bg="{ALT}">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="a3e">The vocabulary of learning science &middot; 6 pairs</div>
        <h2 class="slide-title" data-i18n="a3t">Match the term to its definition</h2>
      </div></div>
      <div class="slide-body">
        <div class="match-grid">
{chr(10).join(pairs)}
        </div>
        <p class="feedback" data-explain="These six terms are the working vocabulary of the talk. Four name things that help learning; two name the thing that only feels like it."></p>
      </div>
    </section>
'''

# ── ORDER ─────────────────────────────────────────────────────────────
body += f'''
    <section class="slide" data-type="order">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="a4e">The shape of the argument &middot; 6 stages</div>
        <h2 class="slide-title" data-i18n="a4t">Put the talk back in order</h2>
      </div></div>
      <div class="slide-body">
        <div class="order-hint" data-i18n="orderHint">Click the parts in order &middot; click one again to take it back</div>
        <div class="order" data-answer="{esc('|'.join(ORDER_CHUNKS))}"></div>
        <div style="margin-top:18px">
          <button class="btn" data-action="check-order" data-i18n="btnCheck">Check</button>
        </div>
        <p class="feedback" data-explain="{esc(ORDER_EX)}"></p>
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
'''          <span class="bank-chip">productive struggle</span>
          <span class="bank-chip">retrieval practice</span>
          <span class="bank-chip">the illusion of competence</span>
          <span class="bank-chip">durable learning</span>
          <span class="bank-chip">to confabulate</span>
          <span class="bank-chip">complement rather than replace</span>''')

s = s.replace('.q-stem {',
  '.q-ctx { font-size: 17px; line-height: 1.5; font-style: italic; color: var(--text-dim); '
  'border-left: 2px solid var(--accent-dim); padding-left: 14px; margin-bottom: 14px; max-width: 62ch; }\n.q-stem {', 1)

open('/tmp/ai_stage1.html','w',encoding='utf-8').write(s)
print('slides:', body.count('<section'))
