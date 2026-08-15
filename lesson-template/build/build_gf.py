# -*- coding: utf-8 -*-
import re, json

src = open('forbes-gap-fill.html', encoding='utf-8').read()
i = src.index('const sentences = ['); blk = src[i:src.index('\n];', i)]
sents = []
for chunk in re.split(r'\n  \{\n', blk)[1:]:
    def g(k):
        m = re.search(k + r':\s*"((?:[^"\\]|\\.)*)"', chunk)
        return m.group(1).replace('\\"','"').replace("\\'","'") if m else ''
    sents.append({'before': g('before'), 'after': g('after'),
                  'answer': g('answer'), 'hint': g('hint')})
print('sentences:', len(sents))

s = open('lesson-template/lesson-template.html', encoding='utf-8').read()
s = s.replace('<title>Lesson Title | Forbes English</title>',
              '<title>Talking with Clients | Forbes English</title>')
s = s.replace("  --hero: url('sample-hero.jpg');   /* real lessons: url('<folder>/hero.jpg') */",
              "  --hero: url('RedditFrench/cafe-hero.jpg');")
pal = {'--void':'#0c0e0a','--surface':'#171b14','--surface2':'#21271c','--border':'#744236',
       '--text':'#f5f2f2','--text-dim':'#bfa9a3','--accent':'#d75739','--accent-bright':'#e8866f',
       '--accent-dim':'#913823','--secondary':'#3a4d4d','--contrast':'#1dedb0'}
for k,v in pal.items():
    s = re.sub(r'(\n  '+re.escape(k)+r'\s*: )#[0-9a-fA-F]{3,8};', lambda m: m.group(1)+v+';', s, count=1)
s = s.replace('  --bg-opacity: 0.34;', '  --bg-opacity: 0.46;')

def esc(x): return x.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')
def keep(x): return x.replace('&','&amp;')

EXPLAIN = {
 'walk':'<strong>Walk someone through</strong> something means to guide them step by step. It is the standard phrase for taking a client through a proposal.',
 'schedule':'<strong>Schedule a meeting</strong> is the neutral, professional collocation. <em>Book</em> works too, but <em>schedule</em> is safer in writing.',
 'frustration':'<strong>Understand your frustration</strong> acknowledges the feeling without admitting fault — the standard opening of a professional apology.',
 'coming from':'<strong>I see where you are coming from</strong> concedes the other person’s position before you offer an alternative.',
 'free':'<strong>Feel free to</strong> is a fixed phrase inviting contact. It cannot be broken up or substituted.',
 'manage':'<strong>Manage expectations</strong> is a fixed business collocation: shaping what someone believes is possible, before they are disappointed.',
 'afraid':'<strong>I’m afraid</strong> softens a refusal. Without it, <em>we can’t offer a discount</em> reads as blunt.',
 'confirm':'<strong>Just to confirm</strong> opens a summary of what has been agreed — one of the most useful phrases in client email.',
 'raising':'<strong>Thank you for raising that</strong> treats a complaint as a contribution. <em>Bringing up</em> is the informal equivalent.',
 'draw':'<strong>Draw someone’s attention to</strong> something is the formal way to point at a detail in a document.',
 'focused':'<strong>Focused on</strong> takes the preposition <em>on</em>. <em>Focused in</em> and <em>focused at</em> are both wrong.',
 'introduce':'<strong>Allow me to introduce myself</strong> is the formal self-introduction, used on a first call or in a first email.',
 'trade':'<strong>Trade up</strong> means to choose a more expensive option. The opposite, <em>trade down</em>, is equally common in market talk.',
 'align':'<strong>Align on</strong> something means to reach a shared understanding. It has largely replaced <em>agree on</em> in project English.',
}

body = ''
PAIRS = [sents[i:i+2] for i in range(0, len(sents), 2)]
for pi, pair in enumerate(PAIRS):
    n = pi + 1
    rows = []
    for q in pair:
        size = max(9, len(q['answer']) + 3)
        rows.append(f'''        <div class="gap-row">
          <p class="q-stem">{keep(q['before'])} <input class="gap" data-answer="{esc(q['answer'])}" size="{size}" aria-label="gap"> {keep(q['after'])}</p>
          <p class="cue">{keep(q['hint'])}</p>
          <p class="feedback" data-explain="{esc(EXPLAIN.get(q['answer'], 'A fixed professional collocation — the words go together and cannot be swapped.'))}"></p>
        </div>''')
    body += f'''
    <section class="slide" data-type="gap">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="ge{n}">Client language &middot; {n}/{len(PAIRS)}</div>
        <h2 class="slide-title" data-i18n="gTitle">Complete the sentence</h2>
      </div></div>
      <div class="slide-body">
{chr(10).join(rows)}
        <div style="margin-top:16px">
          <button class="btn" data-action="check" data-i18n="btnCheck">Check</button>
        </div>
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
'''          <span class="bank-chip">walk you through</span>
          <span class="bank-chip">I&rsquo;m afraid</span>
          <span class="bank-chip">manage expectations</span>
          <span class="bank-chip">just to confirm</span>
          <span class="bank-chip">draw your attention to</span>
          <span class="bank-chip">align on</span>''')

s = s.replace('.q-stem {', '''.cue {
  font-family: var(--font-mono); font-size: 12px; line-height: 1.45;
  color: var(--text-dim); margin-top: 8px;
}
.gap-row + .gap-row { margin-top: 26px; }
.q-stem {''', 1)

open('/tmp/gf_stage1.html','w',encoding='utf-8').write(s)
print('slides:', body.count('<section'), '| gaps:', body.count('class="gap"'))
