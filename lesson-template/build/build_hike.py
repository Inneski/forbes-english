# -*- coding: utf-8 -*-
import json, re
d = json.load(open('/tmp/hike.json'))

TPL = open('lesson-template/lesson-template.html', encoding='utf-8').read()
s = TPL
s = s.replace('<title>Lesson Title | Forbes English</title>',
              '<title>Solo Hiking Safety (C1) | Forbes English</title>')
s = s.replace("  --hero: url('sample-hero.jpg');   /* real lessons: url('<folder>/hero.jpg') */",
              "  --hero: url('Hiking/hero.jpg');")
pal = {'--void':'#0c1112','--surface':'#141e20','--surface2':'#1c2a2d','--border':'#9c424a',
       '--text':'#f5f2f2','--text-dim':'#bfa3a6','--accent':'#e4606c','--accent-bright':'#f29aa2',
       '--accent-dim':'#c12835','--secondary':'#517288','--contrast':'#1ded76'}
for k, v in pal.items():
    s = re.sub(r'(\n  ' + re.escape(k) + r'\s*: )#[0-9a-fA-F]{3,8};', lambda m: m.group(1)+v+';', s, count=1)
s = s.replace('  --bg-opacity: 0.34;', '  --bg-opacity: 0.46;')

def esc(x): return x.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')
def keep(x): return x.replace('&nbsp;',' ')          # stems already carry safe markup

body = ''

# ── ACTIVITY 1 · multiple choice ──────────────────────────────────────
for q in d['mc']:
    opts = []
    for o in q['opts']:
        mark = ' data-correct' if o['l'] == q['key'] else ''
        opts.append(f'          <button class="opt"{mark}>{keep(o["t"])}</button>')
    body += f'''
    <section class="slide" data-type="mc">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="a1e{q['n']}">Comprehension &amp; inference &middot; {q['n']}/5</div>
        <h2 class="slide-title" data-i18n="a1t">Choose the best answer</h2>
      </div></div>
      <div class="slide-body">
        <p class="q-stem">{keep(q['stem'])}</p>
        <div class="opts">
{chr(10).join(opts)}
        </div>
        <p class="feedback" data-explain="{esc(q['explain'])}"></p>
      </div>
    </section>
'''

# ── ACTIVITY 2 · gap fill ─────────────────────────────────────────────
for q in d['fitb']:
    sent = q['sentence']
    ans = '|'.join(dict.fromkeys(q['answers']))
    size = max(10, len(q['answers'][0]) + 2)
    sent = re.sub(r'<input[^>]*>',
                  f'<input class="gap" data-answer="{esc(ans)}" size="{size}" aria-label="gap">', sent)
    body += f'''
    <section class="slide" data-type="gap">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="a2e{q['n']}">Collocations &amp; vocabulary &middot; {q['n']}/5</div>
        <h2 class="slide-title" data-i18n="a2t">Complete the sentence</h2>
      </div></div>
      <div class="slide-body">
        <p class="q-stem">{keep(sent)}</p>
        <p class="cue">{keep(q['hint'])}</p>
        <div style="margin-top:20px">
          <button class="btn" data-action="check" data-i18n="btnCheck">Check</button>
        </div>
        <p class="feedback" data-explain="{esc(q['explain'])}"></p>
      </div>
    </section>
'''

# ── ACTIVITY 3 · matching ─────────────────────────────────────────────
TERMS = {1:'animal track', 2:'wash', 3:'cache', 4:'rabbit hole', 5:'dorsiflexion'}
pairs = []
for p in d['match']:
    pairs.append(f'          <div class="match-pair" data-term="{esc(TERMS[p["n"]])}" data-def="{esc(p["def"].strip(chr(34)))}"></div>')
body += f'''
    <section class="slide" data-type="match">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="a3e">Definitions to terms &middot; 5 pairs</div>
        <h2 class="slide-title" data-i18n="a3t">Match each term to its definition</h2>
      </div></div>
      <div class="slide-body">
        <div class="match-grid">
{chr(10).join(pairs)}
        </div>
        <p class="feedback" data-explain="All five are technical terms a hiker meets on the trail: two describe the ground underfoot, one a hazard, one a stored file, and one a movement of the foot."></p>
      </div>
    </section>
'''

# ── ACTIVITY 4 · word order ───────────────────────────────────────────
RO_EXPLAIN = {
 1:'A perfect gerund — <em>having pushed</em> — puts the cause before the consequence it explains.',
 2:'The adverb sits next to the verb it modifies, and the concessive <em>even without</em> closes the clause.',
 3:'Adverb of frequency, then verb, then the adjectives in their natural order before the noun.',
 4:'A verb + noun + prepositional phrase: what is reassessed, and towards what.',
 5:'The comparative frame is <em>N times safer than</em> + gerund.',
}
for q in d['reorder']:
    chunks = q['answer'].split()
    body += f'''
    <section class="slide" data-type="order">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="a4e{q['n']}">Word order &middot; {q['n']}/5</div>
        <h2 class="slide-title" data-i18n="a4t">Build the clause</h2>
      </div></div>
      <div class="slide-body">
        <p class="q-stem">{keep(q['stem'])}</p>
        <div class="order-hint" data-i18n="orderHint">Click the parts in order &middot; click one again to take it back</div>
        <div class="order" data-answer="{esc('|'.join(chunks))}"></div>
        <div style="margin-top:16px">
          <button class="btn" data-action="check-order" data-i18n="btnCheck">Check</button>
        </div>
        <p class="feedback" data-explain="{esc(RO_EXPLAIN[q['n']])}"></p>
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
'''          <span class="bank-chip">impassable</span>
          <span class="bank-chip">provoke</span>
          <span class="bank-chip">robust</span>
          <span class="bank-chip">an animal track</span>
          <span class="bank-chip">reassess</span>
          <span class="bank-chip">push past exhaustion</span>''')

# the hint line under a gap
s = s.replace('.q-stem {', '''.cue {
  font-family: var(--font-mono); font-size: 12.5px; line-height: 1.45;
  color: var(--text-dim); margin-top: 14px;
}
.q-stem {''', 1)

open('/tmp/hike_stage1.html', 'w', encoding='utf-8').write(s)
print('slides:', body.count('<section'))
