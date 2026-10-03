#!/usr/bin/env node
// The Climb, played in a real browser.
//
//   node lesson-template/build/sherpa-climb/test_climb.js                 # the game, at 1280x800 and 390x844,
//                                                                          # plus the no-scroll gate at five sizes
//   node lesson-template/build/sherpa-climb/test_climb.js --canon         # the typed-answer canon, unit tests only
//   node lesson-template/build/sherpa-climb/test_climb.js --content <f>   # read the expected content from another
//                                                                          # content file (as build.py --content)
//   node lesson-template/build/sherpa-climb/test_climb.js --page <f.html> # test a variant built with build.py --out
//                                                                          # (served at the page's own URL)
//   node lesson-template/build/sherpa-climb/test_climb.js --no-gate       # skip the five-size no-scroll gate (quick)
//   node lesson-template/build/sherpa-climb/test_climb.js --shots <dir>   # where the screenshots go (default:
//                                                                          # $CLIMB_SHOTS, else <temp>/sherpa-climb-shots)
//   node lesson-template/build/sherpa-climb/test_climb.js --lang de       # the gate in a learner's language: a gloss
//                                                                          # under every line, or the card's toggle
//   node lesson-template/build/sherpa-climb/test_climb.js --gate-only     # the gate alone (the play-through is in
//                                                                          # English whatever --lang says)
//
// Serves the repo (as tools/sherpa_type_check.js does) and plays camp one with one line
// deliberately wrong first time (it must come back, and the score must be n-1 of n), then
// camp two all right, checking the save, the route map's store left alone, no console
// errors, no sideways scroll, a double-click on "Next", and on a phone that the card and its
// buttons stay on screen. Then the no-scroll gate (Innes: "NO scrolling" in a game panel):
// at 1366x768, 1280x720, 1024x768, 844x390 and 360x740, every camp's arrival card, every
// line asked and answered (wrong first: the tallest state), every camp-complete card and,
// with a SUMMIT, both steps of the summit screen (the second with 25+ lines to look at
// again): the card must not scroll. With --lang, wherever a card shows its "Translation"
// toggle (the glosses did not fit beneath the English), the gate also presses it and
// measures the card with the translation in place of the English, then presses it again.
// If the page offers more than one language, a switch in the middle of a line must keep it.
// The canon tests run the canon() that ships: they read it out of the built page.
const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');
const HERE = __dirname;
const ROOT = path.resolve(HERE, '..', '..', '..');
const PAGE = 'sherpa-tensing-the-climb.html';
const argv = process.argv.slice(2);
const opt = k => { const i = argv.indexOf(k); return i >= 0 ? argv[i + 1] : null; };
const PAGE_FILE = opt('--page') ? path.resolve(opt('--page')) : path.join(ROOT, PAGE);
const SHOTS = opt('--shots') || process.env.CLIMB_SHOTS || path.join(require('os').tmpdir(), 'sherpa-climb-shots');
const GATE_SIZES = [[1366, 768], [1280, 720], [1024, 768], [844, 390], [360, 740]];
const SHOT_SIZES = ['1280x720', '844x390', '360x740'];   // the gate photographs its key states at these
const LANG = opt('--lang') || 'en';
const GAP = 420;   // ms: the page ignores a click or Enter within 350ms of a line appearing or being answered
const TYPES = { '.html': 'text/html', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.jpg': 'image/jpeg',
  '.png': 'image/png', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json',
  '.webp': 'image/webp', '.m4a': 'audio/mp4' };

const results = [];
let fails = 0;
function ok(cond, what, detail) {
  results.push(`${cond ? 'PASS' : 'FAIL'} ${what}${detail ? ' (' + detail + ')' : ''}`);
  if (!cond) fails++;
  return cond;
}
const notes = [];

// ── canon ────────────────────────────────────────────────────────────────────────
function loadCanon() {
  const src = fs.readFileSync(PAGE_FILE, 'utf8');
  const m = src.match(/\/\*CANON:start\*\/([\s\S]*?)\/\*CANON:end\*\//);
  if (!m) throw new Error('no /*CANON:start*/ block in ' + PAGE_FILE);
  return new Function(m[1] + '\nreturn { flat: flat, variants: variants, accepts: accepts };')();
}
function canonTests() {
  const C = loadCanon();
  const yes = [
    ["'m tying", ['am tying'], 'contraction typed, full form accepted'],
    ['am tying', ["'m tying"], 'full form typed, contraction accepted'],
    ["don't like", ['do not like'], "n't to not"],
    ['do not like', ["don't like"], 'not to n\'t'],
    ['dont like', ["don't like"], 'apostrophe-less dont'],
    ['doesnt work', ['does not work'], 'apostrophe-less doesnt'],
    ['didnt see', ["didn't see"], 'apostrophe-less didnt'],
    ["isn't", ['is not'], "isn't"],
    ['wont go', ['will not go'], 'apostrophe-less wont = will not'],
    ["won't go", ['will not go'], "won't = will not"],
    ["can't", ['cannot'], "can't = cannot"],
    ['cannot', ['can not'], 'cannot = can not'],
    ['cant swim', ["can't swim"], 'apostrophe-less cant'],
    ["shan't", ['shall not'], "shan't"],
    ["shan't leave", ["won't leave"], "shan't = won't (BrE I / we)"],
    ['shall be sleeping', ['will be sleeping'], 'shall = will (BrE I / we)'],
    ['I shall have walked', ['I will have walked'], 'shall have = will have'],
    ["he's gone", ['he has gone'], "'s = has"],
    ["he's going", ['he is going'], "'s = is"],
    ["she'd left", ['she had left'], "'d = had"],
    ["she'd leave", ['she would leave'], "'d = would"],
    ["they're", ['they are'], "'re"],
    ["we've been", ['we have been'], "'ve"],
    ["'ll be sweating", ['will be sweating'], "'ll"],
    ['is sleeping.', ['is sleeping'], 'final full stop'],
    ['is sleeping!', ['is sleeping'], 'final !'],
    ['is sleeping?', ['is sleeping'], 'final ?'],
    ['don’t like', ["don't like"], 'curly apostrophe'],
    ['is  sleeping', ['is sleeping'], 'double spaces'],
    ['  is sleeping  ', ['is sleeping'], 'outer spaces'],
    ['Is Sleeping', ['is sleeping'], 'case'],
    ['IS SLEEPING', ['is sleeping'], 'all capitals'],
    ['checks', ['checks'], 'plain'],
    ['have‐been', ['have-been'], 'unicode hyphen'],
    ['ｉｓ sleeping', ['is sleeping'], 'NFKC full-width letters'],
    ['are using', ['Are ... using'], '"..." in an accept entry'],
  ];
  const no = [
    ['is sleep', ['is sleeping'], 'wrong form'],
    ['sleeping', ['is sleeping'], 'missing IS'],
    ['was sleeping', ['is sleeping'], 'wrong tense'],
    ["he's gone", ['he was gone'], "'s is not was"],
    ["she'd left", ['she has left'], "'d is not has"],
    ['', ['is sleeping'], 'empty'],
    ['   ', ['is sleeping'], 'spaces only'],
    ['is sleeping.', ['is sleepings'], 'near miss'],
    ['do like', ["don't like"], 'lost negative'],
  ];
  for (const [inp, acc, why] of yes) ok(C.accepts(inp, acc), `canon accepts ${JSON.stringify(inp)} for ${JSON.stringify(acc)}: ${why}`);
  for (const [inp, acc, why] of no) ok(!C.accepts(inp, acc), `canon refuses ${JSON.stringify(inp)} for ${JSON.stringify(acc)}: ${why}`);
  ok(JSON.stringify(C.variants("he's")) === JSON.stringify(['he is', 'he has']), "variants(\"he's\") = he is | he has", JSON.stringify(C.variants("he's")));
  ok(C.variants("he'd said she's").length === 4, "two ambiguous contractions give four readings", JSON.stringify(C.variants("he'd said she's")));
  ok(C.flat('  Don’t  LIKE. ') === "don't like", 'flat() folds case, quotes, spaces and the stop');
  return C;
}

/* A typed answer the canon must accept that is not the accept entry as written: a
   contraction where one is possible ("am writing" -> "'m writing", "don't" -> "dont"),
   else the entry with a capital and a full stop. Worked out from the content, so the test
   does not break when a line is rewritten. */
function variantOf(acc) {
  const rules = [
    [/^am (.+)$/, "'m $1"], [/^is not (.+)$/, "isn't $1"], [/^are not (.+)$/, "aren't $1"], [/^is (.+)$/, "'s $1"],
    [/^are (.+)$/, "'re $1"], [/^will not (.+)$/, "won't $1"], [/^will (.+)$/, "'ll $1"], [/^have (.+)$/, "'ve $1"],
    [/^has (.+)$/, "'s $1"], [/^had (.+)$/, "'d $1"],
    [/\b(do|does|did|is|are|was|were|have|has|had)n't\b/, '$1nt'], [/\bwon't\b/, 'wont'], [/\bcan't\b/, 'cant'],
    [/\b(do|does|did|is|are|was|were|have|has|had) not\b/, "$1n't"],
  ];
  for (const [re, to] of rules) if (re.test(acc)) return { v: acc.replace(re, to), contracted: true };
  return { v: acc.charAt(0).toUpperCase() + acc.slice(1) + '.', contracted: false };
}

// ── the browser ──────────────────────────────────────────────────────────────────
function serve() {
  return new Promise(res => {
    const srv = http.createServer((req, rsp) => {
      const u = decodeURIComponent(req.url.split('?')[0].split('#')[0]);
      const f = u === '/' + PAGE ? PAGE_FILE : path.join(ROOT, u);
      if (!(f === PAGE_FILE || f.startsWith(ROOT)) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { rsp.writeHead(404); return rsp.end(); }
      rsp.writeHead(200, { 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream' });
      rsp.end(fs.readFileSync(f));
    });
    srv.listen(0, 'localhost', () => res(srv));
  });
}

function content() {
  const args = [path.join(HERE, 'build.py'), '--dump'];
  if (opt('--content')) args.push('--content', opt('--content'));
  const r = spawnSync(process.platform === 'win32' ? 'py' : 'python3', args, { encoding: 'utf8' });
  if (r.status !== 0) return { refused: (r.stderr || r.stdout).trim() };
  const out = r.stdout.trim().split('\n');
  return JSON.parse(out[out.length - 1]);
}

const SENTINEL = '{"camp-one-present-continuous":{"face":"ascent","best":3,"total":10},"test":"sentinel"}';

async function boxOf(p) {
  return p.evaluate(() => {
    const c = document.querySelector('#card');
    const r = c.getBoundingClientRect();
    const btns = [...c.querySelectorAll('button, input, a')].filter(b => b.offsetParent !== null && getComputedStyle(b).display !== 'none' && getComputedStyle(b).visibility !== 'hidden')
      .map(b => { const q = b.getBoundingClientRect(); return { t: (b.textContent || b.placeholder || '').trim().slice(0, 24), top: q.top, bottom: q.bottom, left: q.left, right: q.right }; });
    return { card: { top: r.top, bottom: r.bottom, left: r.left, right: r.right }, vw: innerWidth, vh: innerHeight,
             scroll: c.scrollHeight - c.clientHeight, btns, over: document.documentElement.scrollWidth - innerWidth };
  });
}
function boxProblems(box) {
  const inView = q => q.top >= -0.5 && q.left >= -0.5 && q.bottom <= box.vh + 0.5 && q.right <= box.vw + 0.5;
  const inCard = q => q.top >= box.card.top - 0.5 && q.bottom <= box.card.bottom + 0.5;
  const bad = [];
  if (box.scroll > 1) bad.push(`the card scrolls by ${Math.round(box.scroll)}px`);
  if (!inView(box.card)) bad.push(`card ${Math.round(box.card.top)}-${Math.round(box.card.bottom)} outside the ${box.vw}x${box.vh} screen`);
  for (const b of box.btns) if (!inView(b) || !inCard(b)) bad.push(`"${b.t}" ${Math.round(b.top)}-${Math.round(b.bottom)} cut off`);
  if (box.over > 1) bad.push(`sideways scroll ${box.over}px`);
  return bad;
}
async function layoutCheck(p, dev, where) {
  const box = await boxOf(p);
  const bad = boxProblems(box);
  return ok(!bad.length, `${dev} ${where}: card and its ${box.btns.length} control(s) inside the ${box.vw}x${box.vh} screen, no scroll`, bad.join('; '));
}

const cur = p => p.evaluate(() => {
  const st = window.SherpaClimb.state(), r = st.run;
  if (!r || !r.cur) return { view: st.view, id: null };
  const it = r.items[r.cur.idx];
  return { view: st.view, id: it.id, kind: it.kind, answered: r.cur.answered, back: r.cur.back };
});

async function answerItem(p, it, wrong, typed, keys) {
  if (it.kind === 'type') {
    await p.fill('#typed', wrong ? it.accept[0] + ' xyz' : typed);
    await p.press('#typed', 'Enter');
  } else {
    const want = wrong ? it.options.find(o => String(o) !== String(it.answer)) : it.answer;
    if (keys) {
      const idx = await p.evaluate(v => [...document.querySelectorAll('#view .opt')].findIndex(b => b.getAttribute('data-v') === String(v)), want);
      await p.keyboard.press(String(idx + 1));
    } else {
      await p.click(`#view .opt[data-v="${String(want).replace(/"/g, '\\"')}"]`);
    }
  }
  await p.waitForSelector('#fb .verdict');
}

async function playCamp(p, dev, camp, C, shot, opts) {
  const n = camp.n;
  const items = Object.fromEntries(camp.items.map(it => [it.id, it]));
  const seq = [];
  const wrongId = opts.wrongId;
  let shotChoose = false, shotSpot = false;
  for (let step = 0; step < camp.items.length * 3; step++) {
    const state = await p.evaluate(() => {
      const q = document.querySelector('#view .v-q'), d = document.querySelector('#view .v-done, #view .v-top');
      return { id: q && q.getAttribute('data-id'), done: !!d };
    });
    if (state.done) break;
    if (!ok(!!state.id, `${dev} camp ${n}: a question is showing at step ${step + 1}`)) return null;
    const it = items[state.id];
    if (!ok(!!it, `${dev} camp ${n}: item ${state.id} is in the content`)) return null;
    const firstTime = !seq.includes(it.id);
    seq.push(it.id);
    const wrong = firstTime && it.id === wrongId;
    if (dev === 'phone') await layoutCheck(p, dev, `${it.id} (${it.kind}) asked`);
    if (it.kind === 'choose' && !shotChoose) { await shot('choose'); shotChoose = true; }
    if (it.kind === 'spot' && !shotSpot) { await shot('spot'); shotSpot = true; }
    let typed = null;
    if (it.kind === 'type') {
      const vo = variantOf(it.accept[0]);
      typed = firstTime ? vo.v : it.accept[0];
      if (!wrong && firstTime && vo.contracted) opts.contracted.push(`${it.id}: "${vo.v}" for "${it.accept[0]}"`);
    }
    await answerItem(p, it, wrong, typed, opts.keys);
    const fb = await p.evaluate(() => ({
      verdict: document.querySelector('#fb .verdict .vt').textContent.trim(),
      more: (document.querySelector('#fb .more') || {}).textContent || '',
      fixed: document.querySelector('#view .q-line').innerHTML,
      sr: (document.querySelector('#fb .sr-only') || {}).innerHTML || '',
      why: document.querySelector('#fb .why').textContent,
      out: [...document.querySelectorAll('#view .opt.out')].filter(b => getComputedStyle(b).display !== 'none').length,
      mine: [...document.querySelectorAll('#view .opt.wrong')].filter(b => getComputedStyle(b).display !== 'none').length,
    }));
    if (wrong) {
      ok(fb.verdict === 'Not quite. The rope holds.' && fb.more === 'This line comes back before you leave the camp.',
        `${dev} ${it.id}: a miss says "Not quite. The rope holds." and that the line comes back`, fb.verdict + ' / ' + fb.more);
    } else {
      ok(fb.verdict === 'Right. Up you go.', `${dev} ${it.id}: "${it.kind === 'type' ? typed : it.answer}" is marked right`, fb.verdict);
    }
    const want = it.kind === 'spot' ? [it.text.match(/\[([^\]]+)\]/)[1]] : String(it.answer).split('...').map(s => s.trim());
    ok(want.every(w => fb.fixed.includes('<b>' + w.replace(/&/g, '&amp;') + '</b>')) && !/_|\[|\]|class="gap"|class="cue"/.test(fb.fixed) && fb.sr === fb.fixed,
      `${dev} ${it.id}: the line is put right in place, the answer in bold (and read out in the live region)`, fb.fixed);
    ok(fb.why.trim() === it.fb.replace(/\*\*/g, ''), `${dev} ${it.id}: the explanation line is shown`);
    if (it.kind !== 'type') ok(fb.out === 0 && fb.mine === (wrong ? 1 : 0), `${dev} ${it.id}: answered, the options not chosen go; a wrong choice stays, marked`, JSON.stringify(fb));
    if (it.kind === 'type' && wrong) await shot('type-wrong');
    if (dev === 'phone') await layoutCheck(p, dev, `${it.id} answered`);
    await p.waitForTimeout(GAP);
    if (opts.keys) await p.keyboard.press('Enter'); else await p.click('#next');
    await p.waitForTimeout(GAP);
  }
  return seq;
}

async function newPage(b, base, vp, errors, dev) {
  const ctx = await b.newContext({ viewport: vp, reducedMotion: 'no-preference' });
  await ctx.addInitScript(s => { try { if (!localStorage.getItem('sherpa.progress.v1')) localStorage.setItem('sherpa.progress.v1', s); } catch (e) {} }, SENTINEL);
  const p = await ctx.newPage();
  p.on('pageerror', e => errors.push('pageerror: ' + e.message));
  p.on('console', m => {
    if (m.type() !== 'error') return;
    const url = (m.location() || {}).url || '';
    if (/Failed to load resource/.test(m.text()) && url && !url.startsWith(base)) { notes.push(`${dev}: offline? ${m.text()} ${url}`); return; }
    errors.push(m.text() + (url ? ' @ ' + url : ''));
  });
  return { ctx, p };
}

async function run(b, base, C, dev, vp) {
  const errors = [];
  const { ctx, p } = await newPage(b, base, vp, errors, dev);
  fs.mkdirSync(SHOTS, { recursive: true });
  const shot = async (name, full) => { await p.waitForTimeout(450); await p.screenshot({ path: path.join(SHOTS, `${dev}-${name}.png`), fullPage: !!full }); };

  await p.goto(base + PAGE, { waitUntil: 'load' });
  await p.waitForTimeout(1300);
  const start = await p.evaluate(() => ({
    over: document.documentElement.scrollWidth - innerWidth,
    picks: [...document.querySelectorAll('.pick[data-camp]')].map(b => [b.getAttribute('data-camp'), b.querySelector('.pick-name').textContent.trim()]),
    go: document.querySelector('#go').textContent.trim(),
    playing: document.body.classList.contains('playing'),
    lang: document.documentElement.lang,
    radius: getComputedStyle(document.querySelector('.member')).borderTopLeftRadius,
    choose: document.querySelector('#choose').getBoundingClientRect().top + scrollY,
  }));
  ok(start.over <= 1, `${dev} start: no sideways scroll`, start.over > 1 ? start.over + 'px' : '');
  const want = C.camps.map(c => [String(c.n), C.tenses[String(c.n)]]).concat(C.summit ? [['summit', 'Summit push · all thirteen tenses']] : []);
  ok(JSON.stringify(start.picks) === JSON.stringify(want), `${dev} start: lists every camp in the content (${C.camps.length})`, JSON.stringify(start.picks));
  ok(/^Start at camp one/.test(start.go), `${dev} start: a first visit offers "Start at camp one"`, start.go);
  ok(!start.playing && start.lang === 'en', `${dev} start: the start screen, in English`);
  ok(start.radius === '14px', `${dev} start: the team cards have the route map's --radius`, start.radius);
  if (dev === 'phone') ok(start.choose < 2 * vp.height, `${dev} start: "Choose a camp" starts within two screens`, Math.round(start.choose) + 'px');
  await shot('start', true);

  // camp one
  await p.click('#go');
  await p.waitForSelector('#view .v-arrive');
  const arrive = await p.evaluate(() => ({
    k: document.querySelector('.v-arrive .k').textContent, tense: document.querySelector('.v-arrive .tense').textContent,
    tip: document.querySelector('.v-arrive .tip').textContent, lines: document.querySelectorAll('.v-arrive .line').length,
    read: document.querySelector('.v-arrive .read').getAttribute('href'), bold: document.querySelectorAll('.v-arrive .en b').length,
    readH: document.querySelector('.v-arrive .read').getBoundingClientRect().height,
    over: document.documentElement.scrollWidth - innerWidth, chip: document.querySelector('#chip').textContent,
    alt: document.querySelector('#alt').textContent, scene: document.querySelector('#scene').getAttribute('src'),
  }));
  const c1 = C.camps[0];
  ok(arrive.k === `Camp ${c1.n} · ${c1.alt.toLocaleString('en-GB')} m`, `${dev} arrival: "Camp ${c1.n} · ${c1.alt.toLocaleString('en-GB')} m"`, arrive.k);
  ok(arrive.tense === C.tenses[String(c1.n)], `${dev} arrival: the tense name, ${C.tenses[String(c1.n)]}`, arrive.tense);
  ok(arrive.tip === c1.tip && arrive.lines === c1.arrive.length && arrive.bold > 0, `${dev} arrival: the tip and ${c1.arrive.length} arrival lines, **bold** as <b>`);
  ok(/^sherpa-tensing-camp-/.test(arrive.read) && arrive.readH >= 44, `${dev} arrival: "Read camp ${c1.n} first" links the camp page, a 44px target`, arrive.read + ' ' + arrive.readH);
  ok(arrive.chip === `Camp ${c1.n} · ${C.tenses[String(c1.n)]}` && arrive.alt === c1.alt.toLocaleString('en-GB'), `${dev} arrival: the camp chip and the altitude`, arrive.chip + ' / ' + arrive.alt);
  ok(arrive.scene === `SherpaClimb/camp-${String(c1.n).padStart(2, '0')}${vp.width < 900 ? '-sm' : ''}.jpg`, `${dev} arrival: the camp's scene (${vp.width < 900 ? '-sm' : 'full'})`, arrive.scene);
  if (dev === 'phone') await layoutCheck(p, dev, 'arrival card');
  await shot('arrive');
  const keys = dev === 'desktop';
  if (keys) await p.keyboard.press('Enter'); else await p.click('#begin');
  await p.waitForTimeout(GAP);
  const wrongItem = c1.items.find(it => it.kind === 'type') || c1.items[0];
  const contracted = [];
  const seq1 = await playCamp(p, dev, c1, C, shot, { keys, wrongId: wrongItem.id, contracted });
  if (seq1) {
    ok(seq1.filter(x => x === wrongItem.id).length === 2 && seq1[seq1.length - 1] === wrongItem.id,
      `${dev} camp ${c1.n}: the missed line ${wrongItem.id} came back, after every other line`, seq1.join(' '));
  }
  await p.waitForSelector('#view .v-done');
  const done1 = await p.evaluate(() => document.querySelector('#view .v-done').innerText);
  ok(done1.includes(`Camp ${c1.n} reached`) && done1.includes(`First try: ${c1.items.length - 1} of ${c1.items.length}`),
    `${dev} camp ${c1.n}: complete card says "First try: ${c1.items.length - 1} of ${c1.items.length}"`, done1.replace(/\s+/g, ' ').slice(0, 120));
  if (dev === 'phone') await layoutCheck(p, dev, 'complete card');
  await shot('complete');
  const store = await p.evaluate(() => ({ climb: localStorage.getItem('sherpa.climb.v1'), prog: localStorage.getItem('sherpa.progress.v1') }));
  const save = JSON.parse(store.climb || '{}');
  ok(save.v === 1 && save.camps && save.camps[String(c1.n)] && save.camps[String(c1.n)].best === c1.items.length - 1 &&
     save.camps[String(c1.n)].total === c1.items.length && save.camps[String(c1.n)].plays === 1,
    `${dev} save: camps["${c1.n}"].best == ${c1.items.length - 1} of ${c1.items.length}`, store.climb);
  ok(save.misses && save.misses[wrongItem.id] === true && Object.keys(save.misses).length === 1,
    `${dev} save: misses["${wrongItem.id}"] is true, and nothing else`, JSON.stringify(save.misses));
  ok(store.prog === SENTINEL, `${dev} save: sherpa.progress.v1 untouched`);
  const gold7 = (c1.items.length - 1) / c1.items.length >= .75;
  ok(save.camps[String(c1.n)].gold === gold7, `${dev} save: gold flag ${gold7}`);

  // camp two: by "Continue" after a reload on the computer, by "On to camp 2" on the phone
  const c2 = C.camps[1];
  if (c2) {
    if (dev === 'desktop') {
      await p.reload({ waitUntil: 'load' });
      await p.waitForTimeout(900);
      const go = await p.evaluate(() => ({ go: document.querySelector('#go').textContent.trim(),
        best: document.querySelector(`.pick[data-camp="1"] .pick-best`).textContent }));
      ok(go.go.startsWith(`Continue: camp ${c2.n}`), `${dev} start: progress turns the button into "Continue: camp ${c2.n}"`, go.go);
      ok(go.best.startsWith(`${c1.items.length - 1}/${c1.items.length}`), `${dev} start: camp ${c1.n} shows its best, ${c1.items.length - 1}/${c1.items.length}`, go.best);
      await p.click('#go');
    } else {
      const onward = await p.evaluate(() => (document.querySelector('#onward') || {}).textContent || '');
      ok(onward.startsWith(`On to camp ${c2.n}`), `${dev} complete card: "On to camp ${c2.n}"`, onward);
      await p.click('#onward');
    }
    await p.waitForSelector('#view .v-arrive');
    await p.click('#begin');
    await p.waitForTimeout(GAP);
    if (dev === 'desktop') {
      // a double-click on "Next": the second click must not answer the next line
      const first = c2.items.find(it => it.kind === 'choose');
      const c = await cur(p);
      const it = c2.items.find(x => x.id === c.id);
      await answerItem(p, it, false, it.kind === 'type' ? it.accept[0] : null, false);
      await p.waitForTimeout(GAP);
      await p.dblclick('#next');
      await p.waitForTimeout(150);
      const after = await cur(p);
      const sv = await p.evaluate(() => JSON.parse(localStorage.getItem('sherpa.climb.v1')).misses);
      ok(after.id && after.id !== c.id && !after.answered && Object.keys(sv).length === 1,
        `${dev} a double-click on "Next" shows the next line and answers nothing`, JSON.stringify({ was: c.id, now: after.id, answered: after.answered, misses: Object.keys(sv) }));
      void first;
      await p.waitForTimeout(GAP);
      const seq2 = await playCamp(p, dev, c2, C, shot, { keys: false, contracted });
      if (seq2) ok(seq2.length === c2.items.length - 1, `${dev} camp ${c2.n}: all right first time, no line repeated`, seq2.join(' '));
    } else {
      const seq2 = await playCamp(p, dev, c2, C, shot, { keys: false, contracted });
      if (seq2) ok(seq2.length === c2.items.length, `${dev} camp ${c2.n}: all right first time, no line repeated`, seq2.join(' '));
    }
    ok(contracted.length > 0 || ![...c1.items, ...c2.items].some(it => it.kind === 'type' && variantOf(it.accept[0]).contracted),
      `${dev} canon in the page: a contracted typed answer is marked right`, contracted.join('; '));
    await p.waitForSelector('#view .v-done');
    const done2 = await p.evaluate(() => ({ text: document.querySelector('#view .v-done').innerText,
      onward: !!document.querySelector('#onward'), gold: !!document.querySelector('#view .reached .flag-ico.gold') }));
    ok(done2.text.includes(`First try: ${c2.items.length} of ${c2.items.length}`) && done2.gold, `${dev} camp ${c2.n}: ${c2.items.length} of ${c2.items.length}, a gold flag`);
    const nextExists = C.camps[2] || (c2.n === 13 && C.summit);
    ok(done2.onward === !!nextExists, `${dev} camp ${c2.n}: ${nextExists ? 'an onward button' : 'no next camp yet, so just "Camps"'}`);
    await p.click('#tocamps');
    await p.waitForTimeout(500);
    const back = await p.evaluate(() => ({ playing: document.body.classList.contains('playing'),
      bests: [...document.querySelectorAll('.pick[data-camp] .pick-best')].map(e => e.textContent),
      flags: [...document.querySelectorAll('.pick[data-camp] .pick-flag .flag-ico')].map(e => e.classList.contains('gold')),
      dflags: [...document.querySelectorAll('.mtn:not(.mtn-mini) .dflag')].map(e => e.getAttribute('class')).filter(c => c !== 'dflag'),
      over: document.documentElement.scrollWidth - innerWidth }));
    ok(!back.playing && back.bests[0].startsWith(`${c1.items.length - 1}/`) && back.bests[1].startsWith(`${c2.items.length}/`),
      `${dev} back at the camps: bests ${back.bests.map(s => s.split(' ')[0]).join(', ')}`);
    ok(back.flags[0] === gold7 && back.flags[1] === true && back.dflags.length === 2, `${dev} back at the camps: flags on the list and on the mountain`, JSON.stringify(back));
    ok(back.over <= 1, `${dev} back at the camps: no sideways scroll`);
    await shot('start-after', true);
  }

  if (C.summit) {
    // the summit push, from the last row of the list: its first line missed on purpose
    const S = C.summit;
    await p.click('.pick[data-camp="summit"]');
    await p.waitForSelector('#view .v-arrive');
    const k = await p.evaluate(() => document.querySelector('.v-arrive .k').textContent);
    ok(k === `Summit push · ${S.alt.toLocaleString('en-GB')} m`, `${dev} summit push: "Summit push · ${S.alt.toLocaleString('en-GB')} m"`, k);
    await p.click('#begin');
    await p.waitForTimeout(GAP);
    const leak = await p.evaluate(() => ({ chip: !!document.querySelector('#view .v-q .tchip'),
      mark: (document.querySelector('#view mark.spot') && getComputedStyle(document.querySelector('#view mark.spot')).backgroundImage) || '' }));
    ok(!leak.chip, `${dev} summit push: no tense name on a line before it is answered`);
    const seqS = await playCamp(p, dev, Object.assign({}, S, { n: 'summit' }), C, async () => {}, { keys: false, wrongId: S.items[0].id, contracted: [] });
    if (seqS) ok(seqS[seqS.length - 1] === S.items[0].id, `${dev} summit push: the missed line came back last`, seqS.join(' '));
    // step one: the end of the story, and one button on
    await p.waitForSelector('#view .v-top.s1');
    const top1 = await p.evaluate(() => ({
      h: document.querySelector('.v-top .tense').textContent, lines: document.querySelectorAll('.v-top .lines .line').length,
      btns: [...document.querySelectorAll('#view button, #view a')].map(b => b.textContent.trim()),
      stats: !!document.querySelector('.v-top .stats'), focus: document.activeElement && document.activeElement.id }));
    const wantLines = (S.done ? 1 : 0) + (C.outro || []).length;
    ok(top1.h === 'The summit' && top1.lines === wantLines && !top1.stats,
      `${dev} summit, step one: "The summit", the push's last line and ${(C.outro || []).length} closing line(s), no scores yet`, top1.h + ' ' + top1.lines);
    ok(top1.btns.length === 1 && /^See your climb/.test(top1.btns[0]) && top1.focus === 'seeclimb',
      `${dev} summit, step one: one button, "See your climb", with the focus on it`, JSON.stringify(top1));
    if (dev === 'phone') await layoutCheck(p, dev, 'summit step one');
    await shot('summit-1');
    if (keys) {
      // Enter, held: the first press goes on, the repeats must not reach "Climb again"
      await p.waitForTimeout(GAP);
      await p.keyboard.down('Enter');
      await p.waitForSelector('#view .v-top.s2');
      await p.waitForTimeout(GAP);            // past the page's 350ms guard: only the repeat check stops these
      await p.keyboard.down('Enter');
      await p.keyboard.down('Enter');
      await p.keyboard.up('Enter');
      await p.waitForTimeout(150);
      const held = await p.evaluate(() => ({ view: window.SherpaClimb.state().view, s2: !!document.querySelector('#view .v-top.s2'),
        misses: Object.keys(JSON.parse(localStorage.getItem('sherpa.climb.v1')).misses).length }));
      ok(held.view === 'summit' && held.s2 && held.misses > 0, `${dev} summit: Enter goes to step two, and Enter held down does not climb again`, JSON.stringify(held));
    } else {
      await p.waitForTimeout(GAP);
      await p.click('#seeclimb');
    }
    // step two: the climb
    await p.waitForSelector('#view .v-top.s2');
    const top = await p.evaluate(() => ({
      h: document.querySelector('.v-top .tense').textContent, lines: document.querySelectorAll('.v-top .lines .line').length,
      stats: document.querySelector('.v-top .stats').textContent, chips: document.querySelectorAll('.v-top .rv-chips li:not(.rv-more)').length,
      more: (document.querySelector('.v-top .rv-more') || {}).textContent || '',
      scene: document.querySelector('#scene').getAttribute('src'), focus: document.activeElement && document.activeElement.id,
      links: [...document.querySelectorAll('.v-top a')].map(a => a.getAttribute('href')),
      save: JSON.parse(localStorage.getItem('sherpa.climb.v1')) }));
    ok(top.h === 'Your climb' && top.lines === 0 && top.focus === 'again', `${dev} summit, step two: "Your climb", the focus on "Climb again"`, JSON.stringify({ h: top.h, lines: top.lines, focus: top.focus }));
    ok(/Gold flags: \d+ of \d+/.test(top.stats) && /First try overall: \d+%/.test(top.stats), `${dev} summit, step two: the stats`, top.stats);
    const missed = Object.keys(top.save.misses);
    const camps = new Set(missed.map(id => id.startsWith('s-') ? String(S.items.find(x => x.id === id).camp) : id.split('-')[0].slice(1)));
    ok(top.chips === Math.min(4, camps.size) && top.more === (camps.size > 4 ? '+' + (camps.size - 4) : '') && missed.includes(S.items[0].id),
      `${dev} summit screen: a count for each camp with lines to look at again (${camps.size}; four shown at most)`, missed.join(' '));
    await p.click('#rv-open');
    await p.waitForTimeout(300);
    const dlg = await p.evaluate(() => ({ open: document.querySelector('#rv').open, review: [...document.querySelectorAll('#rv-list .rv-g p[lang]')].map(e => e.innerHTML) }));
    ok(dlg.open && dlg.review.length === missed.length && dlg.review.every(h => /<b>/.test(h)),
      `${dev} summit screen: "Read them again" opens the ${missed.length} line(s) in full, form in bold`, String(dlg.review.length));
    await p.keyboard.press('Escape');
    await p.waitForTimeout(200);
    const still = await p.evaluate(() => ({ open: document.querySelector('#rv').open, playing: document.body.classList.contains('playing') }));
    ok(!still.open && still.playing, `${dev} summit screen: Esc closes the list, not the game`);
    ok(/(sherpa-day|summit-top)\.jpg$/.test(top.scene) &&   // Innes's team-on-top art once it exists
       top.links.includes('sherpa-tensing-route-map.html#the-map'),
      `${dev} summit screen: the sherpa's picture, and the way down to the passive`, top.scene);
    ok(top.save.summit && top.save.summit.total === S.items.length && top.save.summit.best === S.items.length - 1, `${dev} save: summit best`, JSON.stringify(top.save.summit));
    if (dev === 'phone') await layoutCheck(p, dev, 'summit step two');
    await shot('summit-2');
    await p.click('#again');
    await p.waitForSelector('#view .v-arrive');
    const again = await p.evaluate(() => ({ s: JSON.parse(localStorage.getItem('sherpa.climb.v1')), k: document.querySelector('.v-arrive .k').textContent }));
    ok(Object.keys(again.s.misses).length === 0 && again.s.camps['1'] && again.k.startsWith('Camp ' + C.camps[0].n),
      `${dev} "Climb again": back to camp ${C.camps[0].n}, the review cleared, the bests kept`);
    await p.click('#back');
    await p.waitForTimeout(300);
  }

  if (dev === 'desktop') {
    // keyboard: a camp from the list, Enter, a number key, Escape back to the camps
    await p.focus('.pick[data-camp="1"]');
    await p.keyboard.press('Enter');
    await p.waitForSelector('#view .v-arrive');
    await p.keyboard.press('Enter');
    await p.waitForSelector('#view .v-q');
    const focusOnCard = await p.evaluate(() => document.activeElement && (document.activeElement.id === 'card' || document.activeElement.id === 'typed'));
    ok(focusOnCard, `${dev} keyboard: focus moves to the card on a new line`);
    await p.keyboard.press('s');
    const snd = await p.evaluate(() => ({ pressed: document.querySelector('#snd').getAttribute('aria-pressed'), store: localStorage.getItem('sherpa-climb-sound') }));
    ok(snd.pressed === 'true' && snd.store === '1', `${dev} keyboard: S turns the sound on and remembers it`, JSON.stringify(snd));
    await p.keyboard.press('s');
    await p.keyboard.press('Escape');
    await p.waitForTimeout(300);
    const esc = await p.evaluate(() => ({ playing: document.body.classList.contains('playing'), util: !!document.querySelector('.wm-right #util') }));
    ok(!esc.playing && esc.util, `${dev} keyboard: Esc goes back to the camps (the sound and music buttons go back to the wordmark)`);
    if (C.summit) {
      // after a summit run with the camps not played, "Continue" sends you back down to them
      await p.evaluate(() => localStorage.setItem('sherpa.climb.v1', JSON.stringify({ v: 1, camps: {}, summit: { best: 1, total: 3, plays: 1 }, last: 'summit', misses: {} })));
      await p.reload({ waitUntil: 'load' });
      await p.waitForTimeout(500);
      const go = await p.evaluate(() => document.querySelector('#go').textContent.trim());
      ok(go.startsWith('Continue: camp ' + C.camps[0].n), `${dev} after a summit run with no camps played: "Continue: camp ${C.camps[0].n}"`, go);
    }
    // a language that is not complete is not offered, and ?lang= falls back to English
    await p.goto(base + PAGE + '?lang=de', { waitUntil: 'load' });
    await p.waitForTimeout(700);
    const de = await p.evaluate(() => ({ lang: document.documentElement.lang, opts: [...document.querySelectorAll('#lang option')].map(o => o.value),
      shown: getComputedStyle(document.querySelector('#lang')).display !== 'none' }));
    ok(de.lang === (de.opts.includes('de') ? 'de' : 'en'), `${dev} ?lang=de: ${de.opts.includes('de') ? 'German' : 'not complete, so English'}`, JSON.stringify(de));
    ok(de.shown === de.opts.length > 1, `${dev} the language menu shows only when there is a choice (${de.opts.join(' ')})`);
    if (de.opts.length > 1) await langSwitch(p, base, C, dev, de.opts.find(l => l !== 'en'));
    else notes.push(`${dev}: one language only, so the switch in the middle of a line was not tried (test a variant: build.py --i18n <dir> --out <f>, then --page <f>)`);
  }
  ok(!errors.length, `${dev}: no console errors or page errors`, errors.slice(0, 5).join(' | '));
  await ctx.close();
}

// a language switch in the middle of a line keeps the line: its options in the same order,
// no "Again" tag, what was typed, and the answer if one was given (shown in the new language)
async function langSwitch(p, base, C, dev, other) {
  await p.goto(base + PAGE + '?lang=en', { waitUntil: 'load' });
  await p.evaluate(() => { localStorage.removeItem('sherpa.climb.v1'); });
  await p.goto(base + PAGE + '?lang=en&switch=1#camp-' + C.camps[0].n, { waitUntil: 'load' });
  await p.waitForSelector('#view .v-arrive');
  await p.click('#begin');
  await p.waitForTimeout(GAP);
  const items = Object.fromEntries(C.camps[0].items.map(it => [it.id, it]));
  let didChoose = false, didType = false;
  for (let i = 0; i < C.camps[0].items.length && !(didChoose && didType); i++) {
    const c = await cur(p);
    const it = items[c.id];
    if (it.kind !== 'type' && !didChoose) {
      const before = await p.evaluate(() => [...document.querySelectorAll('#view .opt')].map(b => b.getAttribute('data-v')));
      await p.selectOption('#lang', other);
      await p.waitForTimeout(200);
      const mid = await p.evaluate(() => ({ order: [...document.querySelectorAll('#view .opt')].map(b => b.getAttribute('data-v')),
        again: !!document.querySelector('#view .again'), id: document.querySelector('#view .v-q').getAttribute('data-id'), lang: document.documentElement.lang }));
      ok(mid.id === c.id && JSON.stringify(mid.order) === JSON.stringify(before) && !mid.again && mid.lang === other,
        `${dev} language switch on an open line: same line, same option order, no "Again"`, JSON.stringify({ before, mid }));
      await answerItem(p, it, false, null, false);
      await p.waitForTimeout(1000);
      await p.selectOption('#lang', 'en');
      await p.waitForTimeout(200);
      const fb = await p.evaluate(() => ({ verdict: document.querySelector('#fb .verdict .vt').textContent, alt: document.querySelector('#alt').textContent,
        state: window.SherpaClimb.state().run.cur.answered }));
      ok(fb.verdict === 'Right. Up you go.' && fb.state && /^\d{1,3}(,\d{3})*$/.test(fb.alt),
        `${dev} language switch on an answered line: the feedback follows the language, the altitude is whole`, JSON.stringify(fb));
      didChoose = true;
    } else if (it.kind === 'type' && !didType) {
      await p.fill('#typed', 'half typed');
      await p.selectOption('#lang', other);
      await p.waitForTimeout(200);
      const v = await p.evaluate(() => document.querySelector('#typed').value);
      ok(v === 'half typed', `${dev} language switch while typing: the typed words stay`, v);
      await p.selectOption('#lang', 'en');
      await p.fill('#typed', it.accept[0]);
      await p.press('#typed', 'Enter');
      await p.waitForSelector('#fb .verdict');
      didType = true;
    } else {
      await answerItem(p, it, false, it.kind === 'type' ? it.accept[0] : null, false);
    }
    await p.waitForTimeout(GAP);
    await p.click('#next');
    await p.waitForTimeout(GAP);
  }
}

// ── the glosses and the card's "Translation" toggle ─────────────────────────────
/* Where the glosses are on the card, and whether the toggle should be showing: hidden
   glosses must not have fitted (fitG is measured against the tightest step with them
   beneath), and each gloss must share its English's box, RTL per element in Arabic. */
function glossState(p) {
  return p.evaluate(() => {
    const c = document.querySelector('#card');
    const shown = el => !!el && el.getClientRects().length > 0 && getComputedStyle(el).visibility !== 'hidden';
    const gl = [...c.querySelectorAll('.gl')].filter(g => g.textContent.trim());
    const tx = [...c.querySelectorAll('.tx')];
    const tog = c.querySelector('#gtog');
    let fitsTight = null;
    if (c.classList.contains('fitG')) {
      const keep = c.className, top = c.scrollTop;
      c.classList.remove('fitG', 'gsw'); c.classList.add('fit1', 'fit2', 'fit3');
      fitsTight = c.scrollHeight <= c.clientHeight + 1;
      c.className = keep; c.scrollTop = top;
    }
    const lang = document.documentElement.lang, rtl = window.CLIMB_I18N.rtl.indexOf(lang) >= 0;
    return { g: c.classList.contains('fitG'), sw: c.classList.contains('gsw'), n: gl.length, glShown: gl.filter(shown).length,
      tx: tx.length, txShown: tx.filter(shown).length, tog: shown(tog), pressed: tog ? tog.getAttribute('aria-pressed') : null,
      label: tog ? tog.textContent.trim() : null, want: lang === 'en' ? null : (window.CLIMB_I18N.t[lang] || {})['Translation'],
      togLang: tog ? tog.getAttribute('lang') : null, lang, fitsTight,
      dirOk: gl.every(g => (g.getAttribute('dir') === 'rtl') === rtl),
      inBox: gl.every(g => g.previousElementSibling && g.previousElementSibling.classList.contains('tx')),
      txEn: tx.every(x => x.getAttribute('lang') === 'en') };
  });
}
function glossProblems(s, on) {
  const bad = [];
  if (!s.dirOk) bad.push('a gloss without dir="rtl" (or with it in a left-to-right language)');
  if (!s.inBox || !s.txEn || s.tx !== s.n) bad.push(`${s.n} gloss(es) for ${s.tx} English line(s) in the same box`);
  if (!s.g) {
    if (s.glShown !== s.n) bad.push(`${s.n - s.glShown} gloss(es) hidden though they fit`);
    if (s.tog) bad.push('the toggle shows though the glosses fit');
    if (s.txShown !== s.tx) bad.push('English hidden with no toggle');
    return bad;
  }
  if (s.fitsTight !== false) bad.push('the glosses were hidden though they fit beneath at the tightest step');
  if (!s.tog) bad.push('the glosses are hidden and no toggle shows');
  if (s.label !== s.want || s.togLang !== s.lang) bad.push(`the toggle reads "${s.label}" (${s.togLang}), not "${s.want}" (${s.lang})`);
  if (s.pressed !== String(!!on)) bad.push(`aria-pressed="${s.pressed}", the card shows ${on ? 'the translation' : 'the English'}`);
  if (on ? s.glShown !== s.n || s.txShown !== 0 : s.glShown !== 0 || s.txShown !== s.tx)
    bad.push(on ? `pressed: ${s.glShown} of ${s.n} gloss(es) in place, ${s.txShown} English line(s) still showing`
      : `${s.txShown} of ${s.tx} English line(s) showing, ${s.glShown} gloss(es) beneath`);
  return bad;
}

// ── the no-scroll gate ───────────────────────────────────────────────────────────
async function gateSize(b, base, C, w, h) {
  const errors = [];
  const dev = `${w}x${h}`;
  const { ctx, p } = await newPage(b, base, { width: w, height: h }, errors, dev);
  const bad = [];
  let states = 0, toggled = 0;
  const shots = SHOT_SIZES.includes(dev);
  const taken = new Set();
  const slug = s => s.replace(/[^a-z0-9-]+/gi, '-').replace(/^-|-$/g, '').toLowerCase();
  const snap = async (key, where) => {
    if (!shots || taken.has(key)) return;
    taken.add(key);
    await p.screenshot({ path: path.join(SHOTS, `gate-${LANG}-${dev}-${key}${where ? '-' + slug(where) : ''}.png`) });
  };
  /* one state of a card: no scroll, every control on screen, and the glosses beneath the
     English or, where they do not fit, the toggle; pressed, the card must still fit with
     the translation in place of the English, and pressed again, be as it was. `kind` names
     the screenshots: the first card of each kind, and the first with the toggle */
  const check = async (where, kind) => {
    states++;
    const box = await boxOf(p);
    const pr = boxProblems(box);
    const s = await glossState(p);
    pr.push(...glossProblems(s, false));
    if (LANG === 'en' && (s.n || s.tog)) pr.push('glosses or a toggle in English');
    if (kind) await snap(kind, where);
    if (s.tog) {
      toggled++;
      if (kind) await snap(`${kind}-toggle-off`, where);
      await p.click('#gtog');
      await p.waitForTimeout(60);
      const on = await glossState(p);
      const onPr = [...boxProblems(await boxOf(p)), ...glossProblems(on, true)];
      if (onPr.length) pr.push('translation in place: ' + onPr.join(', '));
      if (kind) await snap(`${kind}-toggle-on`, where);
      await p.click('#gtog');
      await p.waitForTimeout(60);
      const off = await glossState(p);
      const offBox = await boxOf(p);
      const offPr = [...boxProblems(offBox), ...glossProblems(off, false)];
      if (Math.abs(offBox.card.bottom - box.card.bottom) > 0.5 || Math.abs(offBox.card.top - box.card.top) > 0.5)
        offPr.push(`the card moved from ${Math.round(box.card.top)}-${Math.round(box.card.bottom)} to ${Math.round(offBox.card.top)}-${Math.round(offBox.card.bottom)}`);
      if (offPr.length) pr.push('pressed again: ' + offPr.join(', '));
    }
    if (pr.length) bad.push(`${where}: ${pr.join(', ')}`);
    return s;
  };
  let keysTried = false;
  const stages = C.camps.map(c => ({ hash: 'camp-' + c.n, stage: c })).concat(C.summit ? [{ hash: 'summit', stage: C.summit }] : []);
  for (const { hash, stage } of stages) {
    if (hash === 'summit') {
      // 25 or more lines to look at again by the end of the push
      const ids = C.camps.flatMap(c => c.items.map(it => it.id)).slice(0, 25);
      await p.evaluate(ids => { const s = JSON.parse(localStorage.getItem('sherpa.climb.v1') || '{"v":1,"camps":{},"summit":null,"last":null,"misses":{}}');
        ids.forEach(id => { s.misses[id] = true; }); localStorage.setItem('sherpa.climb.v1', JSON.stringify(s)); }, ids);
    }
    await p.goto(base + PAGE + '?gate=' + hash + (LANG !== 'en' ? '&lang=' + LANG : '') + '#' + hash, { waitUntil: 'load' });   // a new query: a real load, not a hash change
    await p.waitForSelector('#view .v-arrive');
    await p.waitForTimeout(150);
    if (hash === stages[0].hash) {
      // a language the page does not offer falls back to English: that would be a gate run
      // in English under another name
      const docLang = await p.evaluate(() => document.documentElement.lang);
      if (!ok(docLang === LANG, `${dev} the gate runs in ${LANG}`, docLang)) break;
    }
    const arr = await check(`${hash} arrival`, 'arrive');
    if (arr.tog && !keysTried) {
      // the first card with a toggle: it works from the keyboard (Enter on it is not
      // "Start"), and its position belongs to this card only: the next card starts in English
      keysTried = true;
      await p.focus('#gtog');
      await p.keyboard.press('Enter');
      const k1 = await p.evaluate(() => ({ view: window.SherpaClimb.state().view, pressed: document.querySelector('#gtog').getAttribute('aria-pressed') }));
      await p.setViewportSize({ width: w, height: h - 1 });          // a redraw of the same card keeps it
      await p.waitForTimeout(300);
      await p.setViewportSize({ width: w, height: h });
      await p.waitForTimeout(300);
      const k2 = await glossState(p);
      await p.click('#begin');
      await p.waitForTimeout(GAP);
      const k3 = await glossState(p);
      ok(k1.view === 'arrive' && k1.pressed === 'true' && k2.sw && k2.pressed === 'true' && !k3.sw && (k3.pressed === null || k3.pressed === 'false'),
        `${dev} ${LANG} the toggle: Enter on it shows the translation and does not start; a resize keeps it; the next card starts in English`,
        JSON.stringify({ k1, k2: { sw: k2.sw, pressed: k2.pressed }, k3: { sw: k3.sw, pressed: k3.pressed } }));
    } else {
      await p.click('#begin');
      await p.waitForTimeout(GAP);
    }
    const items = Object.fromEntries(stage.items.map(it => [it.id, it]));
    const seen = new Set();
    for (let step = 0; step < stage.items.length * 3; step++) {
      const c = await cur(p);
      if (!c.id) break;
      const it = items[c.id];
      const first = !seen.has(it.id);
      seen.add(it.id);
      if (first) await check(`${it.id} asked`);
      await answerItem(p, it, first, it.kind === 'type' ? it.accept[0] : null, false);
      if (first) await check(`${it.id} answered wrong`, 'answered-wrong');
      await p.waitForTimeout(GAP);
      await p.click('#next');
      await p.waitForTimeout(GAP);
    }
    if (hash === 'summit') {
      // the summit in two steps, each measured on its own
      await p.waitForSelector('#view .v-top.s1');
      await p.waitForTimeout(150);
      await check('summit step one', 'summit-1');
      await p.waitForTimeout(GAP);
      await p.click('#seeclimb');
      await p.waitForSelector('#view .v-top.s2');
      await p.waitForTimeout(150);
      await check('summit step two', 'summit-2');
      const n = await p.evaluate(() => document.querySelector('.rv-n') && +document.querySelector('.rv-n').textContent);
      ok(n >= 25, `${dev} ${LANG} summit step two was measured with ${n} lines to look at again`);
    } else {
      await p.waitForSelector('#view .v-done');
      await p.waitForTimeout(150);
      await check(`${hash} complete`, 'complete');
    }
  }
  ok(!bad.length, `${dev} ${LANG} no-scroll gate: ${states} states across ${stages.length} stage(s)${toggled ? `, ${toggled} with the translation toggle pressed and released` : ''}, the card never scrolls and every control is on screen`,
    bad.slice(0, 6).join(' | ') + (bad.length > 6 ? ` | and ${bad.length - 6} more` : ''));
  ok(!errors.length, `${dev} ${LANG} gate: no console errors or page errors`, errors.slice(0, 3).join(' | '));
  await ctx.close();
}

(async () => {
  canonTests();
  if (!argv.includes('--canon')) {
    const C = content();
    if (C.refused) {
      ok(false, 'the content builds', C.refused.split('\n').slice(0, 4).join(' / '));
    } else {
      const srv = await serve();
      const base = `http://localhost:${srv.address().port}/`;
      const { chromium } = require(path.join(ROOT, 'node_modules', 'playwright'));
      const b = await chromium.launch();
      try {
        if (argv.includes('--gate-only')) notes.push('--gate-only: the play-through (in English) was skipped');
        else await Promise.all([
          run(b, base, C, 'desktop', { width: 1280, height: 800 }),
          run(b, base, C, 'phone', { width: 390, height: 844 }),
        ]);
        if (argv.includes('--no-gate')) notes.push('--no-gate: the no-scroll gate was skipped');
        else await Promise.all(GATE_SIZES.map(([w, h]) => gateSize(b, base, C, w, h)));
      } catch (e) {
        ok(false, 'the run finished', String(e && e.stack || e).split('\n').slice(0, 4).join(' / '));
      }
      await b.close();
      srv.close();
    }
  }
  results.forEach(r => console.log(r));
  if (notes.length) { console.log('\nnotes:'); [...new Set(notes)].forEach(n => console.log('  ' + n)); }
  const passed = results.length - fails;
  console.log(`\n${fails ? 'FAIL' : 'PASS'}: ${passed} of ${results.length} checks passed` + (argv.includes('--canon') ? ' (canon only)' : `; screenshots in ${SHOTS}`));
  process.exit(fails ? 1 : 0);
})();
