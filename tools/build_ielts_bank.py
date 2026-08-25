# -*- coding: utf-8 -*-
"""Build ielts-question-bank.html from tools/ielts_bank_data.py.

    python3 tools/build_ielts_bank.py

Everything countable on the page — the lede, the meta descriptions, the topic
chips — is derived from the data, so adding a topic or a prompt needs no edit
here. Run `tools/seo.py` afterwards: it owns the fenced SEO block and will
otherwise overwrite the description this writes.
"""
import sys, html, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from ielts_bank_data import TOPICS, TYPES

def esc(s): return html.escape(s, quote=True)

chips_topic = '\n'.join(
    f'        <button class="chip" data-filter="topic" data-value="{t["id"]}">{esc(t["name"])}</button>'
    for t in TOPICS)
chips_type = '\n'.join(
    f'        <button class="chip" data-filter="type" data-value="{k}">{esc(v[0])}</button>'
    for k,v in TYPES.items())

sections=[]
for t in TOPICS:
    rows=[]
    for i,(p,ty) in enumerate(t['prompts']):
        rows.append(f'''        <li class="q" data-topic="{t['id']}" data-type="{ty}">
          <p class="q-text">{esc(p)}</p>
          <div class="q-foot">
            <span class="tag tag-{ty}">{esc(TYPES[ty][0])}</span>
            <span class="tag tag-topic">{esc(t['name'])}</span>
            <button class="copy" type="button" data-copy="{esc(p)}">Copy</button>
          </div>
        </li>''')
    fors='\n'.join(f'            <li>{esc(x)}</li>' for x in t['for'])
    ags='\n'.join(f'            <li>{esc(x)}</li>' for x in t['against'])
    sections.append(f'''    <section class="topic" id="{t['id']}" data-topic="{t['id']}">
      <div class="topic-head">
        <h2>{esc(t['name'])}</h2>
        <span class="topic-blurb">{esc(t['blurb'])}</span>
      </div>
      <ul class="qs">
{chr(10).join(rows)}
      </ul>
      <div class="ideas">
        <div class="idea-col">
          <h3>{esc(t['for_h'])}</h3>
          <ul>
{fors}
          </ul>
        </div>
        <div class="idea-col">
          <h3>{esc(t['against_h'])}</h3>
          <ul>
{ags}
          </ul>
        </div>
      </div>
    </section>''')

TOTAL=sum(len(t['prompts']) for t in TOPICS)

page=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IELTS Task 2 Question Bank | Forbes English</title>
<!-- SEO:start -->
<meta name="description" content="{TOTAL} IELTS Writing Task 2 questions sorted by topic and by essay type, each topic with arguments for both sides.">
<link rel="canonical" href="https://forbesenglish.com/ielts-question-bank.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Forbes English">
<meta property="og:title" content="IELTS Task 2 Question Bank | Forbes English">
<meta property="og:description" content="{TOTAL} Task 2 questions by topic and essay type, each topic with arguments for both sides.">
<meta property="og:url" content="https://forbesenglish.com/ielts-question-bank.html">
<meta property="og:image" content="https://forbesenglish.com/ielts-question-bank/hero.jpg">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="IELTS Task 2 Question Bank | Forbes English">
<meta name="twitter:description" content="{TOTAL} Task 2 questions by topic and essay type, each topic with arguments for both sides.">
<meta name="twitter:image" content="https://forbesenglish.com/ielts-question-bank/hero.jpg">
<!-- SEO:end -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Barlow+Condensed:wght@600;700;800&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
<style>
:root {{
  --green-deep:#14301f; --green-lift:#234a33;
  --gold:#b8962e; --gold-bright:#e8c04a; --gold-pale:#f2dc9e; --gold-deep:#9c7818;
  --pink-mid:#8f2856; --cream:#faf8f3; --ink:#182a1f; --muted:#5d6f64; --radius:12px;
}}
* {{ box-sizing:border-box; }}
body {{
  margin:0; font-family:'Lato',sans-serif; color:var(--ink);
  background:
    radial-gradient(1100px 620px at 72% 42%, rgba(35,74,51,0.05), transparent 62%),
    radial-gradient(900px 500px at 10% 0%, rgba(35,74,51,0.05), transparent 60%),
    linear-gradient(165deg,#ffffff 0%,#f6f8f5 55%,#eef3ef 100%);
  -webkit-font-smoothing:antialiased;
}}
.topband {{ background:var(--green-deep); border-bottom:1px solid rgba(232,192,74,0.25); }}
.tb-inner {{ max-width:1180px; margin:0 auto; padding:10px clamp(20px,4vw,40px);
  display:flex; align-items:center; justify-content:space-between; gap:20px; }}
.tb-logo {{ display:block; width:160px; height:32px; background-image:url('logo-forbes-english_1.png');
  background-size:contain; background-repeat:no-repeat; background-position:left center;
  text-indent:-9999px; overflow:hidden; text-decoration:none; }}
.tb-links {{ display:flex; align-items:center; gap:clamp(12px,2vw,26px); flex-wrap:wrap; }}
.tb-links a {{ font-family:'Barlow Condensed',sans-serif; font-weight:600; letter-spacing:.06em;
  font-size:.78rem; text-transform:uppercase; color:var(--cream); text-decoration:none;
  opacity:.85; transition:opacity .15s ease; }}
.tb-links a:hover, .tb-links a[aria-current] {{ opacity:1; }}
.tb-links a[aria-current] {{ color:var(--gold-bright); }}
.tb-cta {{ background:var(--green-lift); color:var(--cream)!important; padding:6px 14px; border-radius:20px;
  opacity:1!important; border:1px solid rgba(232,192,74,.4); }}
.tb-cta-gold {{ background:var(--gold-bright); color:var(--green-deep)!important; padding:6px 14px;
  border-radius:20px; opacity:1!important; font-weight:700; }}
@media (max-width:620px) {{ .tb-links a:not(.tb-cta):not(.tb-cta-gold) {{ display:none; }} }}

.wrap {{ max-width:1180px; margin:0 auto; padding:clamp(26px,5vw,54px) clamp(20px,4vw,40px) clamp(50px,8vw,90px); }}
.hero {{ display:grid; grid-template-columns:1.15fr 1fr; gap:clamp(24px,4vw,48px); align-items:center;
  margin-bottom:clamp(28px,4vw,44px); }}
@media (max-width:820px) {{ .hero {{ grid-template-columns:1fr; }} }}
.eyebrow {{ font-family:'Barlow Condensed',sans-serif; font-weight:700; letter-spacing:.14em;
  text-transform:uppercase; font-size:.82rem; color:var(--gold-deep); margin-bottom:10px; }}
h1 {{ font-family:'Playfair Display',serif; font-weight:900; font-size:clamp(2.1rem,5vw,3.3rem);
  line-height:1.06; margin:0 0 16px; }}
h1 em {{ font-style:normal; color:var(--pink-mid); }}
.lede {{ font-size:1.08rem; line-height:1.62; color:var(--muted); max-width:46ch; margin:0 0 16px; }}
.lede strong {{ color:var(--ink); font-weight:700; }}
.hero-art {{ border-radius:var(--radius); overflow:hidden; box-shadow:0 18px 44px rgba(20,48,31,.22); margin:0; }}
.hero-art img {{ display:block; width:100%; height:auto; }}

/* filters */
/* Opaque, not a fade. The old gradient went transparent at 72% of its own
   height, which was invisible while the bar was one line tall and became a
   band of overlapping text the moment the chips wrapped. */
.controls {{ position:sticky; top:0; z-index:5; padding:14px 0 12px;
  background:#f7faf7; box-shadow:0 6px 14px -8px rgba(20,48,31,.35); }}
.topicbar {{ padding:4px 0 2px; }}
.search {{ width:100%; font-family:'Lato',sans-serif; font-size:1rem; padding:12px 16px;
  border:1px solid rgba(20,48,31,.18); border-radius:var(--radius); background:#fff; color:var(--ink); }}
.search:focus {{ outline:2px solid var(--gold); outline-offset:1px; }}
.chiprow {{ display:flex; gap:8px; flex-wrap:wrap; margin-top:10px; align-items:center; }}
.chiprow-label {{ font-family:'Barlow Condensed',sans-serif; font-weight:700; text-transform:uppercase;
  letter-spacing:.09em; font-size:.72rem; color:var(--muted); margin-right:4px; }}
.chip {{ font-family:'Barlow Condensed',sans-serif; font-weight:700; text-transform:uppercase;
  letter-spacing:.06em; font-size:.75rem; padding:6px 13px; border-radius:20px; cursor:pointer;
  border:1px solid rgba(20,48,31,.16); background:#fff; color:var(--muted); }}
.chip:hover {{ border-color:var(--gold); }}
.chip.on {{ background:var(--green-deep); color:var(--cream); border-color:var(--green-deep); }}
.count {{ font-family:'Barlow Condensed',sans-serif; font-weight:700; letter-spacing:.07em;
  text-transform:uppercase; font-size:.78rem; color:var(--muted); margin-top:12px; }}

/* topics */
.topic {{ margin-top:clamp(30px,5vw,50px); }}
.topic-head {{ display:flex; align-items:baseline; gap:14px; flex-wrap:wrap;
  padding-bottom:10px; border-bottom:2px solid rgba(20,48,31,.12); margin-bottom:18px; }}
.topic-head h2 {{ font-family:'Playfair Display',serif; font-weight:700;
  font-size:clamp(1.4rem,3vw,1.85rem); margin:0; }}
.topic-blurb {{ font-size:.95rem; color:var(--muted); }}
.qs {{ list-style:none; margin:0; padding:0; display:grid; gap:12px; }}
.q {{ background:#fff; border:1px solid rgba(20,48,31,.10); border-radius:var(--radius);
  padding:16px 18px; box-shadow:0 2px 10px rgba(20,48,31,.05); }}
.q-text {{ margin:0; font-size:1rem; line-height:1.55; }}
.q-foot {{ display:flex; gap:8px; align-items:center; flex-wrap:wrap; margin-top:10px; }}
.tag {{ font-family:'Barlow Condensed',sans-serif; font-weight:700; text-transform:uppercase;
  letter-spacing:.07em; font-size:.68rem; padding:3px 9px; border-radius:20px;
  background:rgba(20,48,31,.06); color:var(--muted); }}
.tag-opinion    {{ background:#e8c04a; color:var(--green-deep); }}
.tag-discussion {{ background:#7fa3b8; color:#0b2029; }}
.tag-outweigh   {{ background:#c98a5e; color:#2a1408; }}
.tag-measure    {{ background:#8fae86; color:#12240d; }}
.tag-direct     {{ background:#b98198; color:#2a0c1a; }}
.copy {{ margin-left:auto; font-family:'Barlow Condensed',sans-serif; font-weight:700;
  text-transform:uppercase; letter-spacing:.07em; font-size:.72rem; padding:5px 12px;
  border-radius:20px; cursor:pointer; border:1px solid rgba(20,48,31,.16);
  background:#fff; color:var(--green-lift); }}
.copy:hover {{ border-color:var(--gold); }}
.copy.done {{ background:var(--green-deep); color:var(--cream); border-color:var(--green-deep); }}

.ideas {{ display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px; }}
@media (max-width:780px) {{ .ideas {{ grid-template-columns:1fr; }} }}
.idea-col {{ background:var(--green-deep); color:var(--cream); border-radius:var(--radius); padding:18px 20px; }}
.idea-col h3 {{ font-family:'Barlow Condensed',sans-serif; font-weight:700; text-transform:uppercase;
  letter-spacing:.08em; font-size:.8rem; color:var(--gold-bright); margin:0 0 10px; }}
.idea-col ul {{ margin:0; padding:0; list-style:none; display:grid; gap:10px; }}
.idea-col li {{ font-size:.95rem; line-height:1.55; opacity:.9; padding-left:14px; position:relative; }}
.idea-col li::before {{ content:''; position:absolute; left:0; top:.62em; width:6px; height:6px;
  border-radius:50%; background:var(--gold-bright); }}

.empty {{ display:none; text-align:center; color:var(--muted); padding:40px 0; font-size:1.05rem; }}
.note {{ margin-top:clamp(34px,5vw,56px); background:var(--green-deep); color:var(--cream);
  border-radius:var(--radius); padding:clamp(22px,3.4vw,32px) clamp(22px,3.6vw,38px);
  display:grid; grid-template-columns:1fr auto; gap:22px; align-items:center; }}
@media (max-width:700px) {{ .note {{ grid-template-columns:1fr; }} }}
.note h3 {{ font-family:'Playfair Display',serif; font-weight:700; font-size:1.3rem; margin:0 0 8px; }}
.note p {{ margin:0; line-height:1.6; opacity:.86; font-size:.98rem; max-width:62ch; }}
.note a {{ font-family:'Barlow Condensed',sans-serif; font-weight:700; text-transform:uppercase;
  letter-spacing:.07em; font-size:.82rem; text-decoration:none; white-space:nowrap;
  background:var(--gold-bright); color:var(--green-deep); padding:10px 20px; border-radius:22px; }}
</style>
</head>
<body>

<nav class="topband">
  <div class="tb-inner">
    <a class="tb-logo" href="index.html">Forbes English</a>
    <div class="tb-links">
      <a href="library.html">Lessons</a>
      <a href="ielts.html" aria-current="page">IELTS</a>
      <a href="library.html#cat=Grammar+activity">Grammar</a>
      <a href="library.html#cat=Speaking+activity">Speaking</a>
      <a href="pricing.html" class="tb-cta-gold">Go Pro</a>
      <a href="mailto:forbes@goodtimebook.com" class="tb-cta">Work With Me</a>
    </div>
  </div>
</nav>

<div class="wrap">

  <div class="hero">
    <div>
      <div class="eyebrow">IELTS Writing Task 2 · Free</div>
      <h1>Question Bank <em>&amp; Ideas</em></h1>
      <p class="lede"><strong>{TOTAL} questions, sorted by topic and by essay type.</strong> Filter to the type you are practising, or search for a word.</p>
      <p class="lede">Under each topic sit arguments for <em>both</em> sides — written as reasons rather than slogans, because the thing that stops most candidates is not the shape of the essay. It is having nothing to say.</p>
    </div>
    <figure class="hero-art">
      <img src="ielts-question-bank/hero.jpg" alt="Illustration of a curving road cresting a hill at sunset, a lone figure walking">
    </figure>
  </div>

  <!-- The topic row sits ABOVE the sticky bar and scrolls away with the page.
       With seventeen topics it wraps to three lines on a laptop and eight on a
       phone; left inside the sticky bar it took 72% of a phone screen and the
       page underneath was unreadable. Topic is a once-per-visit choice, so it
       does not need to follow you down. Search and essay type do. -->
  <div class="topicbar">
    <div class="chiprow">
      <span class="chiprow-label">Topic</span>
{chips_topic}
    </div>
  </div>

  <div class="controls">
    <input class="search" id="q" type="search" placeholder="Search the questions — try &quot;children&quot;, &quot;government&quot;, &quot;cost&quot;…" aria-label="Search questions">
    <div class="chiprow">
      <span class="chiprow-label">Type</span>
{chips_type}
    </div>
    <div class="count" id="count"></div>
  </div>

{chr(10).join(sections)}

  <p class="empty" id="empty">Nothing matches those filters. Clear one and try again.</p>

  <div class="note">
    <div>
      <h3>Have the ideas, not sure of the shape?</h3>
      <p>Each essay type on this page is taught in the course — what the instruction obliges you to produce, a band 9 model, and the band 6 answer that got the shape right and the question wrong.</p>
    </div>
    <a href="ielts.html">The IELTS route &rarr;</a>
  </div>

</div>

<script>
(function(){{
  var active = {{topic:null, type:null}};
  var qEl = document.getElementById('q');
  var countEl = document.getElementById('count');
  var emptyEl = document.getElementById('empty');
  var questions = [].slice.call(document.querySelectorAll('.q'));
  var topics = [].slice.call(document.querySelectorAll('.topic'));

  document.querySelectorAll('.chip').forEach(function(c){{
    c.addEventListener('click', function(){{
      var k = c.dataset.filter, v = c.dataset.value;
      var on = active[k] === v;
      document.querySelectorAll('.chip[data-filter="'+k+'"]').forEach(function(x){{ x.classList.remove('on'); }});
      active[k] = on ? null : v;
      if (!on) c.classList.add('on');
      apply();
    }});
  }});
  qEl.addEventListener('input', apply);

  function apply(){{
    var term = qEl.value.trim().toLowerCase();
    var shown = 0;
    questions.forEach(function(el){{
      var ok = (!active.topic || el.dataset.topic === active.topic)
            && (!active.type  || el.dataset.type  === active.type)
            && (!term || el.textContent.toLowerCase().indexOf(term) !== -1);
      el.style.display = ok ? '' : 'none';
      if (ok) shown++;
    }});
    topics.forEach(function(sec){{
      var any = sec.querySelectorAll('.q:not([style*="none"])').length > 0;
      sec.style.display = any ? '' : 'none';
    }});
    countEl.textContent = shown + (shown === 1 ? ' question' : ' questions');
    emptyEl.style.display = shown ? 'none' : 'block';
  }}

  document.querySelectorAll('.copy').forEach(function(b){{
    b.addEventListener('click', function(){{
      var t = b.dataset.copy;
      var done = function(){{ b.classList.add('done'); b.textContent = 'Copied';
        setTimeout(function(){{ b.classList.remove('done'); b.textContent = 'Copy'; }}, 1400); }};
      if (navigator.clipboard && navigator.clipboard.writeText) {{
        navigator.clipboard.writeText(t).then(done, fallback);
      }} else {{ fallback(); }}
      function fallback(){{
        var ta = document.createElement('textarea');
        ta.value = t; ta.setAttribute('readonly','');
        ta.style.position='absolute'; ta.style.left='-9999px';
        document.body.appendChild(ta); ta.select();
        try {{ document.execCommand('copy'); done(); }} catch(e) {{}}
        document.body.removeChild(ta);
      }}
    }});
  }});

  apply();
}})();
</script>
</body>
</html>
'''
open(os.path.join(ROOT, 'ielts-question-bank.html'), 'w', encoding='utf-8').write(page)
print('written', round(len(page)/1024), 'KB ·', TOTAL, 'prompts')
