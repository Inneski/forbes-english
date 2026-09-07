#!/usr/bin/env node
/*
 * Exhaustively walk every path through fireshield-pitch.html and report which
 * ending each one reaches.
 *
 * This exists because the first merge of the three FireShield parts shipped a
 * scoring bug that was invisible by eye and obvious by measurement: 84% of
 * playthroughs landed on the best ending and the worst ending could not be
 * reached at all. A defect class needs a measurement, not just a fix
 * (CLAUDE.md, "things that have bitten us").
 *
 * Run it after changing ANY trust value, tier threshold, or scene link:
 *
 *     node tools/simulate_fireshield.js
 *
 * It exits non-zero if an ending is unreachable or if any single ending takes
 * more than 60% of complete playthroughs.
 */

const fs = require("fs");
const path = require("path");

const file = path.join(__dirname, "..", "fireshield-pitch.html");
const src = fs.readFileSync(file, "utf8");
const S = JSON.parse(src.match(/const SCENES = (\{[\s\S]*?\n\});/)[1]);

const endings = {};
let complete = 0, meterLo = 999, meterHi = -999;

const PRIOR = 20;   // keep in step with the page

function totals(log, act) {
  const rows = act ? log.filter(r => r.act === act) : log;
  let got = 0, max = 0;
  for (const r of rows) { got += r.delta; max += r.max; }
  return { got, max };
}
function ratio(log, act) {
  const t = totals(log, act);
  return t.max <= 0 ? 0 : Math.max(0, Math.min(1, t.got / t.max));
}
function meter(log) {
  const t = totals(log, null);
  const v = (t.got + PRIOR / 2) / (t.max + PRIOR);
  return Math.round(100 * Math.max(0, Math.min(1, v)));
}

function tally(key) { endings[key] = (endings[key] || 0) + 1; }

function walk(k, log, depth) {
  if (depth > 60) return;
  const v = S[k];

  if (v.type === "story") {
    const best = Math.max.apply(null, v.choices.map(x => x.trust));
    for (const c of v.choices) {
      walk(c.next, log.concat([{ act: v.act, delta: c.trust, max: best }]), depth + 1);
    }
    return;
  }

  if (v.type === "checkpoint") {
    // first try right, and first try wrong (explanation, no trust)
    walk(v.next, log.concat([{ act: v.act, delta: v.trustOnCorrect, max: v.trustOnCorrect }]), depth + 1);
    walk(v.next, log.concat([{ act: v.act, delta: 0, max: v.trustOnCorrect }]), depth + 1);
    return;
  }

  if (v.type === "interlude") {
    const r = v.final ? ratio(log, null) : ratio(log, v.act);
    const tier = v.tiers.find(t => r >= t.min) || v.tiers[v.tiers.length - 1];
    if (v.final) {
      tally(tier.title.replace(/&[a-z]+;/g, "'").slice(0, 52));
      complete++;
      const m = meter(log);
      if (m < meterLo) meterLo = m;
      if (m > meterHi) meterHi = m;
      return;
    }
    walk(v.next, log, depth + 1);
    return;
  }

  if (v.type === "ending") {
    tally("FAIL — " + v.tag.replace("Ending — ", ""));
    return;
  }
}

walk("a1_open", [], 0);

const rows = Object.entries(endings).sort((a, b) => b[1] - a[1]);
const total = rows.reduce((n, r) => n + r[1], 0);

console.log(`paths: ${total}   complete playthroughs: ${complete}`);
console.log(`meter at the close: ${meterLo}–${meterHi}\n`);
for (const [k, n] of rows) {
  const pct = (n / total * 100).toFixed(1).padStart(5);
  console.log(`  ${String(n).padStart(8)}  ${pct}%  ${k}`);
}

// Every authored ending must be reachable.
const authored = [];
for (const v of Object.values(S)) {
  if (v.type === "ending") authored.push("FAIL — " + v.tag.replace("Ending — ", ""));
  if (v.type === "interlude" && v.final) {
    for (const t of v.tiers) authored.push(t.title.replace(/&[a-z]+;/g, "'").slice(0, 52));
  }
}
const missing = authored.filter(a => !endings[a]);
const dominant = rows.filter(([, n]) => n / total > 0.6);

// How the lesson behaves for plausible learners. Uniform path-counting weights
// "got every checkpoint wrong" the same as "got every one right"; a B2 learner
// paying attention does not play that way.
function archetype(pick, cpRate) {
  let k = "a1_open", log = [];
  for (let i = 0; i < 60; i++) {
    const v = S[k];
    if (v.type === "story") {
      const safe = v.choices.filter(c => c.trust > -30);   // never the fatal one
      const best = Math.max.apply(null, v.choices.map(x => x.trust));
      const c = pick === "best" ? safe.reduce((a, b) => (b.trust > a.trust ? b : a))
              : pick === "worst" ? safe.reduce((a, b) => (b.trust < a.trust ? b : a))
              : safe[Math.floor(safe.length / 2)];
      log.push({ act: v.act, delta: c.trust, max: best });
      k = c.next; continue;
    }
    if (v.type === "checkpoint") {
      log.push({ act: v.act, delta: cpRate * v.trustOnCorrect, max: v.trustOnCorrect });
      k = v.next; continue;
    }
    if (v.type === "interlude") {
      const r = v.final ? ratio(log, null) : ratio(log, v.act);
      const t = v.tiers.find(x => r >= x.min) || v.tiers[v.tiers.length - 1];
      if (v.final) return { r, m: meter(log), end: t.title.replace(/&[a-z]+;/g, "'") };
      k = v.next; continue;
    }
    if (v.type === "ending") return { r: 0, m: meter(log), end: "FAIL " + v.tag };
  }
}

console.log("\nplausible learners:");
const CASES = [
  ["ideal     — best choices, every checkpoint first try", "best", 1],
  ["strong    — best choices, 70% first try", "best", 0.7],
  ["mixed     — middling choices, 70% first try", "mid", 0.7],
  ["weak      — poorest safe choices, 50% first try", "worst", 0.5],
  ["careless  — poorest safe choices, none first try", "worst", 0],
];
const seen = new Set();
for (const [name, pick, rate] of CASES) {
  const o = archetype(pick, rate);
  seen.add(o.end);
  console.log(`  ${name.padEnd(52)} meter ${String(o.m).padStart(3)}  ` +
              `ratio ${o.r.toFixed(2)}  -> ${o.end.slice(0, 46)}`);
}

let bad = false;
if (seen.size < 4) {
  console.log(`\nARCHETYPES COLLAPSE: five learner profiles reach only ${seen.size} distinct outcomes.`);
  bad = true;
}
if (missing.length) {
  console.log("\nUNREACHABLE:"); missing.forEach(m => console.log("  " + m)); bad = true;
}
if (dominant.length) {
  console.log("\nDOMINANT (>60% of paths):");
  dominant.forEach(([k, n]) => console.log(`  ${(n / total * 100).toFixed(1)}%  ${k}`));
  bad = true;
}
if (!bad) console.log("\nPASS — every ending reachable, none dominant.");
process.exit(bad ? 1 : 0);
