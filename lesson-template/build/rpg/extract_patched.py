#!/usr/bin/env python3
"""Pull the text and pictures out of a *patched-stack* standalone RPG export.

    python3 lesson-template/build/rpg/extract_patched.py <export.html> <slug>

README.md §2 names two export kinds and says "a third kind means: read its
script first". This is the third kind, and Frankenstein: The Green Prometheus
(V32) is the first of it. It is neither the Oz shape (one
`window.*_GAME_DATA` JSON object) nor the Wonderland shape (`EMBEDDED_SCENES`
plus `q(...)` tables). It is a **stack of successive patch scripts**: a base
`const DATA={...}` followed by twenty-two more `<script>` blocks — kids-patch,
v4-refined, v5-unobtrusive, … v30, final-user-fixes, v32-definitive — each one
reassigning scenes, rewriting story text, swapping images and wrapping the
render functions. Regexing any one of them gives you a superseded draft: the
Frankenstein export's `03_arctic_rescue.story.en` is rewritten three times,
and the last rewrite is 21 words where the first was 52.

So there is no parsing this file. The only way to the *final* text is to run
it the way a browser does — every block in order, in one shared scope — and
read `DATA` afterwards. That is what this script does:

  * splits the export into its `<script>` blocks and strips the inlined
    base64 payloads out of the code (they are extracted separately, and
    an 18 MB string literal makes node's parser crawl);
  * rewrites top-level `const`/`let` to `var`. `vm.runInContext` gives each
    `runInContext` call its own lexical scope, so a top-level `const DATA`
    is invisible to the next block — the browser's `var`-like global is what
    the export is written against;
  * runs each block in one shared context behind a small DOM shim, catching
    per block exactly as a browser does (a throw kills its own `<script>`
    and nothing else) and reporting which blocks threw;
  * fires DOMContentLoaded and load, because late patches register there;
  * writes the pictures and `data.json` in the same places and the same
    shape `extract_standalone.py` uses, so the rest of the pipeline is
    unchanged.

Every learner-facing string comes out **English-only**. The export carries
`de`/`es` keys, but on Frankenstein they gloss the *pre-patch* English and
were never redone — 71 of them are off by more than a length ratio of 1.7
against the text they sit under. Trust the translations directory, not the
export's own glosses; `apply_translations()` fills all nine.

Needs node on PATH (no packages). Prints the scene list README.md §3 wants.
"""
import base64, json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..'))

DATA_URI = re.compile(r"""(['"])data:(image|font)/[a-z0-9.+-]+;base64,[A-Za-z0-9+/=]+\1""")
TOP_DECL = re.compile(r'(?m)^(?:const|let)\s')

SHIM = r"""
// A DOM small enough to let a patch script run and big enough that none of
// them throws on the way to mutating DATA. Elements answer every call the
// export makes; `value` mirrors innerHTML because the exports decode HTML
// entities through a detached <textarea>, and an undefined .value there is
// what makes a v15-and-later block die halfway.
function makeEl(tag){
  const el = {
    tagName:(tag||'div').toUpperCase(), dataset:{}, children:[], className:'', id:'',
    textContent:'', _html:'', value:'', hidden:false,
    style:new Proxy({},{get:(t,k)=>t[k]||'',set:(t,k,v)=>{t[k]=v;return true}}),
    classList:{add(){},remove(){},toggle(){},contains(){return false}},
    get innerHTML(){return this._html},
    set innerHTML(v){ this._html=String(v);
      this.value=String(v).replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&quot;/g,'"')
        .replace(/&#39;/g,String.fromCharCode(39)).replace(/&nbsp;/g,' ').replace(/&amp;/g,'&'); },
    appendChild(c){this.children.push(c);return c}, append(){}, prepend(){},
    insertBefore(c){this.children.push(c);return c}, removeChild(){}, remove(){},
    setAttribute(k,v){this[k]=v}, getAttribute(k){return this[k]==null?null:this[k]},
    hasAttribute(){return false}, removeAttribute(){}, replaceWith(){},
    addEventListener(){}, removeEventListener(){},
    querySelector(){return null}, querySelectorAll(){return []}, closest(){return null},
    focus(){}, click(){}, scrollTo(){}, scrollIntoView(){}, cloneNode(){return makeEl(tag)},
    getBoundingClientRect(){return {top:0,left:0,width:100,height:100,bottom:100,right:100}},
    get firstChild(){return this.children[0]||null},
    get firstElementChild(){return this.children[0]||null},
    get parentNode(){return null},
  };
  return el;
}
const listeners = {};
const document = {
  readyState:'loading', head:makeEl('head'), body:makeEl('body'), documentElement:makeEl('html'),
  createElement:makeEl, createTextNode:(t)=>({textContent:t}),
  createDocumentFragment:()=>makeEl('frag'),
  getElementById:(id)=>{const e=makeEl('div'); e.id=id; return e;},
  querySelector:()=>makeEl('div'), querySelectorAll:()=>[],
  addEventListener:(t,f)=>{(listeners[t]=listeners[t]||[]).push(f)}, removeEventListener(){},
};
const storage = {_d:{}, getItem(k){return k in this._d?this._d[k]:null},
                 setItem(k,v){this._d[k]=String(v)}, removeItem(k){delete this._d[k]}};
const ctx = {
  console, document, localStorage:storage, sessionStorage:storage,
  setTimeout:(f)=>{try{f()}catch(e){} return 0}, clearTimeout(){},
  setInterval(){return 0}, clearInterval(){},
  requestAnimationFrame:(f)=>{try{f()}catch(e){} return 0}, cancelAnimationFrame(){},
  navigator:{userAgent:'node', language:'en'}, location:{href:'file:///x.html', search:''},
  matchMedia:()=>({matches:false, addEventListener(){}, addListener(){}}),
  getComputedStyle:()=>new Proxy({},{get:()=>''}),
  AudioContext:function(){return {state:'running', resume(){}, currentTime:0, destination:{},
    createOscillator:()=>({connect:()=>({connect(){}}), start(){}, stop(){}, frequency:{value:0}}),
    createGain:()=>({connect:()=>({connect(){}}),
      gain:{value:0, setValueAtTime(){}, exponentialRampToValueAtTime(){}}})}},
  Image:function(){return makeEl('img')}, fetch:()=>Promise.resolve({}),
  ResizeObserver:function(){return {observe(){},disconnect(){}}},
  MutationObserver:function(){return {observe(){},disconnect(){}}},
  IntersectionObserver:function(){return {observe(){},disconnect(){}}},
  alert(){}, scrollTo(){}, innerWidth:1536, innerHeight:864, devicePixelRatio:1,
  addEventListener:(t,f)=>{(listeners[t]=listeners[t]||[]).push(f)}, removeEventListener(){},
};
ctx.window = ctx; ctx.globalThis = ctx; ctx.self = ctx;
"""

RUNNER = r"""
const fs = require('fs'), vm = require('vm');
const blocks = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
__SHIM__
vm.createContext(ctx);
const errs = [];
blocks.forEach((b, i) => {
  try { vm.runInContext(b, ctx, {filename: 'block' + i + '.js'}); }
  catch (e) { errs.push([i, String(e)]); }
});
document.readyState = 'complete';
for (const t of ['DOMContentLoaded', 'load'])
  (listeners[t] || []).forEach(f => { try { f({type: t}) } catch (e) { errs.push(['event ' + t, String(e)]) } });
if (!ctx.DATA) { console.error('no DATA in the export after running every block'); process.exit(1); }
const out = {scenes: ctx.DATA.scenes, endings: ctx.DATA.endings};
for (const k of Object.keys(ctx.DATA))
  if (!['scenes', 'endings', 'images'].includes(k)) out[k] = ctx.DATA[k];
fs.writeFileSync(process.argv[3], JSON.stringify({data: out, errors: errs}, null, 1));
"""


def english_only(o):
    """Drop every non-`en` key from a language bundle: see the docstring."""
    if isinstance(o, dict):
        if 'en' in o and isinstance(o['en'], str):
            for k in [k for k in o if k != 'en']:
                del o[k]
        else:
            for v in o.values():
                english_only(v)
    elif isinstance(o, list):
        for v in o:
            english_only(v)


def main(src, slug):
    html = open(src, encoding='utf-8').read()
    blocks = re.findall(r'<script\b[^>]*>(.*?)</script>', html, re.S)
    if len(blocks) < 2:
        raise SystemExit('%s has %d script block(s) — not a patched-stack export' % (src, len(blocks)))
    code = [TOP_DECL.sub('var ', DATA_URI.sub(r"\1STRIPPED\1", b)) for b in blocks]
    print('%d script blocks, %d KB of code once the base64 is out'
          % (len(code), sum(map(len, code)) // 1024))

    tmp = tempfile.mkdtemp(prefix='rpg-extract-')
    json.dump(code, open(os.path.join(tmp, 'blocks.json'), 'w', encoding='utf-8'))
    open(os.path.join(tmp, 'run.js'), 'w', encoding='utf-8').write(RUNNER.replace('__SHIM__', SHIM))
    r = subprocess.run(['node', os.path.join(tmp, 'run.js'),
                        os.path.join(tmp, 'blocks.json'), os.path.join(tmp, 'out.json')])
    if r.returncode:
        raise SystemExit('node run failed — read the shim in this file and widen it')
    got = json.load(open(os.path.join(tmp, 'out.json'), encoding='utf-8'))
    if got['errors']:
        print('\n! %d block(s) threw — every DATA change AFTER the throw in that block is\n'
              '  lost, so widen the shim until this list is empty:' % len(got['errors']))
        for i, e in got['errors']:
            print('    block %-3s %s' % (i, e[:160]))

    data = got['data']
    english_only(data)

    # the pictures: name.ext, the extension taken from the data URI's own type
    img_dir = os.path.join(REPO, 'block-camp', slug)
    os.makedirs(img_dir, exist_ok=True)
    # Two forms, and both matter: the base DATA object holds its pictures as
    # JSON pairs ("05_lightning_oak":"data:image/png;base64,…") while every
    # later patch assigns them (DATA.images['v32_cover'] = 'data:…'). Reading
    # only the assignments gets you 31 of Frankenstein's 82. Document order is
    # patch order, so a later write of the same name wins.
    pics = {}
    for m in re.finditer(r"""(?:images\s*\[\s*)?(['"])([A-Za-z0-9_]+)\1\s*(?:\]\s*=|:)\s*(['"])data:image/([a-z]+);base64,([A-Za-z0-9+/=]+)\3""", html):
        pics[m.group(2)] = (m.group(4), m.group(5))
    kinds = set()
    for name, (ext, b64) in pics.items():
        open(os.path.join(img_dir, '%s.%s' % (name, ext)), 'wb').write(base64.b64decode(b64))
        kinds.add(ext)
    print('\n%d pictures -> block-camp/%s/  (%s)' % (len(pics), slug, ', '.join(sorted(kinds)) or 'none found'))
    if kinds - {'webp'}:
        print('  ! not all webp — run tools/prep-artwork.py over the folder before building')

    out_dir = os.path.join(HERE, slug)
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, 'data.json')
    json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('text -> %s  (%d scenes, %d endings, English only)'
          % (os.path.relpath(out, REPO), len(data['scenes']), len(data.get('endings', {}))))

    print('\nscenes (fill HOT from a gridded contact sheet — README.md §3):')
    for sid, sc in data['scenes'].items():
        print('  %-26s %-9s %-22s %s' % (sid, sc.get('kind', ''), sc.get('image', ''), sc.get('pos', '')))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__.strip().splitlines()[2].strip())
    main(sys.argv[1], sys.argv[2])
