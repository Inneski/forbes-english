// Builds ../../../blockcraft-past-simple.html from App.tsx (Innes's React lesson).
// One self-contained page: React bundled, Tailwind compiled, nothing loaded from a CDN.
//   cd lesson-template/build/blockcraft-past-simple && npm install && node build.mjs
// Then run tools/build_hubs.py and tools/seo.py from the repo root.
import { build } from 'esbuild';
import { execFileSync } from 'node:child_process';
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);

const OUT = '../../../blockcraft-past-simple.html';
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
