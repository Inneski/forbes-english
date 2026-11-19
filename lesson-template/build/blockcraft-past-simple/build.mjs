// Builds ../../../blockcraft-past-simple.html from App.tsx (Innes's React lesson).
// One self-contained page: React bundled, Tailwind compiled, nothing loaded from a CDN.
//   cd lesson-template/build/blockcraft-past-simple && npm install && node build.mjs
// Then run tools/build_hubs.py and tools/seo.py from the repo root.
import { build } from 'esbuild';
import { execFileSync } from 'node:child_process';
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);

import { transform } from './i18n-transform.mjs';
import { readdirSync, mkdirSync } from 'node:fs';
import { createHash } from 'node:crypto';

const OUT = '../../../blockcraft-past-simple.html';

// 1. Wrap every German string of App.tsx in t(); the German text is the key.
const { code, keys } = transform(readFileSync('App.tsx', 'utf8'));
writeFileSync('App.i18n.jsx', code);
mkdirSync('i18n', { recursive: true });
writeFileSync('i18n/_keys.json', JSON.stringify(keys, null, 1) + '\n');
const SOURCE = createHash('sha256').update(JSON.stringify(keys)).digest('hex').slice(0, 12);

// 2. A language ships only when every key is translated (HOUSE-STYLE rule 5).
const data = {};
for (const f of readdirSync('i18n').filter((f) => /^[a-z]{2}\.json$/.test(f)).sort()) {
  // Each file is {"source": <hash of _keys.json>, "t": [one string per key, same order]}.
  const lang = f.slice(0, 2), file = JSON.parse(readFileSync('i18n/' + f, 'utf8'));
  if (file.source !== SOURCE || !Array.isArray(file.t) || file.t.length !== keys.length) {
    console.log(`  ${lang}: LEFT OUT — written for source ${file.source} with ${file.t && file.t.length} strings; now ${SOURCE} with ${keys.length}. Re-translate the changed lines.`);
    continue;
  }
  const tr = Object.fromEntries(keys.map((k, i) => [k, file.t[i]]));
  const missing = keys.filter((k) => typeof tr[k] !== 'string' || !tr[k].trim());
  const edge = keys.filter((k) => tr[k] && ((k[0] === ' ') !== (tr[k][0] === ' ') || (k.at(-1) === ' ') !== (tr[k].at(-1) === ' ')));
  const stale = [];
  if (missing.length || edge.length) {
    console.log(`  ${lang}: LEFT OUT — ${missing.length} missing, ${edge.length} with wrong edge spaces`);
    missing.concat(edge).slice(0, 5).forEach((k) => console.log('      ' + JSON.stringify(k).slice(0, 90)));
    continue;
  }
  if (stale.length) console.log(`  ${lang}: ${stale.length} unused key(s) — App.tsx text changed?`);
  data[lang] = Object.fromEntries(keys.map((k) => [k, tr[k]]));
}
writeFileSync('i18n-data.js', 'export default ' + JSON.stringify(data) + ';\n');
console.log(`  ${keys.length} strings · languages: de, ${Object.keys(data).join(', ')}`);
const js = (await build({
  entryPoints: ['main.jsx'], bundle: true, minify: true, write: false,
  format: 'iife', target: 'es2019', define: { 'process.env.NODE_ENV': '"production"' },
  jsx: 'automatic', loader: { '.tsx': 'tsx' },
})).outputFiles[0].text.replace(/<\/script/gi, '<\/script');

execFileSync(process.execPath, [require.resolve('tailwindcss/lib/cli.js'),
  '-c', 'tailwind.config.cjs', '-i', 'input.css', '-o', 'out.css', '--minify'], { stdio: 'inherit' });
const css = readFileSync('out.css', 'utf8');

// Keep the SEO block seo.py wrote last time, so a rebuild does not strip it before seo.py runs.
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
${seo}<title>BlockCraft: Past Simple (A2-B1)</title>
<style>${css}
body{background:#090b10;margin:0}
.fe-home{position:fixed;left:12px;bottom:12px;z-index:60;font:600 13px/1 system-ui,sans-serif;color:#e2e8f0;background:#111318cc;border:1px solid #334155;border-radius:8px;padding:8px 12px;text-decoration:none}
.fe-home:hover{border-color:#94a3b8}
.fe-lang{position:fixed;right:12px;top:12px;z-index:60;display:flex;align-items:center;gap:6px;font:600 13px/1 system-ui,sans-serif;color:#e2e8f0;background:#111318e6;border:1px solid #334155;border-radius:8px;padding:6px 8px}
.fe-lang select{background:transparent;color:inherit;border:0;font:inherit;cursor:pointer;outline:none}
.fe-lang option{background:#111318;color:#e2e8f0}
.helper-rtl #root *{unicode-bidi:plaintext}
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
