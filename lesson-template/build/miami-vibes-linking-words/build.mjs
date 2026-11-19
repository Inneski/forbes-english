// Builds ../../../miami-vibes-linking-words.html from App.tsx (Innes's Gemini Canvas quiz).
// One self-contained page: React bundled, Tailwind compiled, nothing loaded from a CDN
// except the two Google Fonts the app imports itself.
//   cd lesson-template/build/miami-vibes-linking-words && npm install && node build.mjs
// Then run tools/build_hubs.py and tools/seo.py from the repo root.
//
// App.tsx is Innes's file unchanged. The build applies a few exact patches (each must match
// once, or the build stops) and writes App.build.jsx:
//   - the Spanish helper line and the two feedback words go through t(), so the 🌐 menu
//     switches them; the Spanish text is the key. English shows no helper line (it would be
//     the answer sentence again).
//   - the 4.5-second auto-advance is removed: it moved on before a B1 learner could read the
//     explanation, and a teacher projecting it could not stop to discuss. "Next Question" stays.
import { build } from 'esbuild';
import { execFileSync } from 'node:child_process';
import { readFileSync, writeFileSync, existsSync, readdirSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);

const OUT = '../../../miami-vibes-linking-words.html';
let src = readFileSync('App.tsx', 'utf8').replace(/\r\n/g, '\n');

const PATCHES = [
  [`import React, { useState, useEffect } from 'react';`,
   `import React, { useState, useEffect } from 'react';\nimport { t } from './i18n-runtime.js';`],
  [`      timer = setTimeout(() => {\n        handleNext();\n      }, 4500);\n`, ``],
  [/<p className="text-md text-gray-400 italic">\s*\{q\.spanish\}\s*<\/p>/,
   `{t(q.spanish) && <p className="text-md text-gray-400 italic">{t(q.spanish)}</p>}`],
  [`<span className="text-[#00ff88]">¡Correcto! 😎</span>`, `<span className="text-[#00ff88]">{t("¡Correcto! 😎")}</span>`],
  [`<span className="text-[#ff2a85]">Incorrecto 🚫</span>`, `<span className="text-[#ff2a85]">{t("Incorrecto 🚫")}</span>`],
];
for (const [from, to] of PATCHES) {
  const n = typeof from === 'string' ? src.split(from).length - 1 : (src.match(new RegExp(from, 'g')) || []).length;
  if (n !== 1) throw new Error(`patch matched ${n} times, expected 1: ${String(from).slice(0, 70)}`);
  src = src.replace(from, () => to);
}
writeFileSync('App.build.jsx', src);

// Keys: every helper line in question order, then the two feedback words.
const keys = [...src.matchAll(/spanish: "((?:[^"\\]|\\.)*)"/g)].map((m) => JSON.parse(`"${m[1]}"`));
keys.push('¡Correcto! 😎', 'Incorrecto 🚫');
writeFileSync('i18n/_keys.json', JSON.stringify(keys, null, 1) + '\n');
const SOURCE = createHash('sha256').update(JSON.stringify(keys)).digest('hex').slice(0, 12);

// A language ships only when every key is translated (HOUSE-STYLE rule 5).
// Each file is {"source": <hash of the keys>, "t": [one string per key, same order]}.
// "" is allowed for a helper line only in en.json (English hides the line).
const data = {};
for (const f of readdirSync('i18n').filter((f) => /^[a-z]{2}\.json$/.test(f)).sort()) {
  const lang = f.slice(0, 2), file = JSON.parse(readFileSync('i18n/' + f, 'utf8'));
  if (file.source !== SOURCE || !Array.isArray(file.t) || file.t.length !== keys.length) {
    console.log(`  ${lang}: LEFT OUT — written for source ${file.source} with ${file.t && file.t.length} strings; now ${SOURCE} with ${keys.length}. Re-translate the changed lines.`);
    continue;
  }
  const bad = file.t.map((s, i) => (typeof s !== 'string' || (!s.trim() && !(lang === 'en' && i < keys.length - 2)) || s !== s.trim()) ? i : -1).filter((i) => i >= 0);
  if (bad.length) { console.log(`  ${lang}: LEFT OUT — bad lines ${bad.join(', ')}`); continue; }
  data[lang] = Object.fromEntries(keys.map((k, i) => [k, file.t[i]]));
}
writeFileSync('i18n-data.js', 'export default ' + JSON.stringify(data) + ';\n');
console.log(`  ${keys.length} strings · languages: es, ${Object.keys(data).join(', ')}`);

const js = (await build({
  entryPoints: ['main.jsx'], bundle: true, minify: true, write: false,
  format: 'iife', target: 'es2019', define: { 'process.env.NODE_ENV': '"production"' },
  jsx: 'automatic',
})).outputFiles[0].text.replace(/<\/script/gi, '<\\/script');

execFileSync(process.execPath, [require.resolve('tailwindcss/lib/cli.js'),
  '-c', 'tailwind.config.cjs', '-i', 'input.css', '-o', 'out.css', '--minify'], { stdio: 'inherit' });
const css = readFileSync('out.css', 'utf8');

let seo = '';
if (existsSync(OUT)) {
  const m = readFileSync(OUT, 'utf8').match(/<!-- SEO:start -->[\s\S]*?<!-- SEO:end -->/);
  if (m) seo = m[0] + '\n';
}

writeFileSync(OUT, `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
${seo}<title>Miami Vibes: Linking Words Quiz (B1)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Righteous&family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
<style>${css}
html,body{background:linear-gradient(135deg,#1a0b2e 0%,#0b1a30 100%);background-attachment:fixed;margin:0;color:#fff}
.fe-home{position:fixed;left:12px;bottom:12px;z-index:60;font:600 13px/1 system-ui,sans-serif;color:#e2e8f0;background:#1a0b2ecc;border:1px solid #00f3ff55;border-radius:8px;padding:8px 12px;text-decoration:none}
.fe-home:hover{border-color:#00f3ff}
.fe-lang{position:fixed;right:12px;top:12px;z-index:60;display:flex;align-items:center;gap:6px;font:600 13px/1 system-ui,sans-serif;color:#e2e8f0;background:#1a0b2ee6;border:1px solid #00f3ff55;border-radius:8px;padding:6px 8px}
.fe-lang select{background:transparent;color:inherit;border:0;font:inherit;cursor:pointer;outline:none}
.fe-lang option{background:#1a0b2e;color:#e2e8f0}
.helper-rtl #root p.italic{direction:rtl;unicode-bidi:plaintext}
@media (max-width:640px){#root>div{padding-top:56px;padding-bottom:64px}}
</style>
</head>
<body>
<div id="root"></div>
<a class="fe-home" href="/library">&larr; Forbes English</a>
<script>${js}</script>
</body>
</html>
`);
console.log('wrote', OUT, Math.round(readFileSync(OUT).length / 1024) + ' KB');
