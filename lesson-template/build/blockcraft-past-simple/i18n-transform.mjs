// Finds every German string in App.tsx (Innes's file, kept unchanged) and wraps it
// in t(...), so the page can show its explanations in any of the site's languages.
// The German text itself is the translation key: i18n/<lang>.json maps it to the
// target language. Strings in the English-teaching content (questions, options,
// example sentences) are never wrapped.
import * as acorn from 'acorn';
import jsx from 'acorn-jsx';

// Fields whose value is always learner-language text, wherever they appear in the data.
const ALWAYS = new Set(['germanHint', 'explanation', 'note', 'whenToUseDE', 'formulaNoteDE',
  'signalsDiffDE', 'de', 'title', 'badge', 'formula', 'labelDE', 'fullTitleDE', 'descDE',
  'nameDE', 'messageDE', 'subtitle']);
const UIKEYS = new Set(['label', 'aria-label', 'placeholder']);
// UI strings in the component are picked by these German markers.
const DE = /[äöüÄÖÜß„“]|\b(und|der|die|das|ist|nicht|mit|für|Wähle|Frage|Fragen|Alle|Sinn|Regel|Verb|Verben|Satz|Sätze|Fehler|Neuer|Tipp|Stark|Ergebnis|Beste|Gesammelte|Deine|Richtige|Rezept|Rezepte|Komplettes|Kein|Lernmodus|Klicken|Deutsch|Infinitiv|Kategorien|Fortschritt|Trefferquote|Spitzhacken|Zeitportal|Zum|Nur|Englisch|Meistere|Grammatik|Amboss|Hauptnavigation|Fenster|AN|AUS|Subjekt|Grundform|Konsonant|Vokal|Basis|Rechtschreibung|Verneinung|Signalwörter|Fragetyp|Lückentext|er Serie|XP gesammelt|Auto-Weiter|Holz|Stein|Eisen|Diamant|Netherit|Wann|Formel|Form|Beispiel)\b/;
const CLASSY = /^(bg-|text-|flex|grid|cursor|inline|hover)/;

export function transform(src) {
  const ast = acorn.Parser.extend(jsx()).parse(src, { ecmaVersion: 'latest', sourceType: 'module' });
  const appStart = src.indexOf('export default function App');
  const sites = [];
  (function walk(n, parent) {
    if (!n || typeof n.type !== 'string' || n.type === 'ImportDeclaration') return;
    let key = null;
    if (parent && parent.type === 'Property' && parent.value === n) key = parent.key.name || parent.key.value;
    if (parent && parent.type === 'JSXAttribute') key = parent.name.name;
    if (n.type === 'Literal' && typeof n.value === 'string') {
      const v = n.value, inApp = n.start > appStart;
      let take = false;
      if (!inApp && ALWAYS.has(key)) take = true;
      else if (!inApp && key === 'prompt' && !v.includes('_____')) take = true; // 4-sentence prompts are German
      else if ((inApp || UIKEYS.has(key)) && DE.test(v) && !CLASSY.test(v)) take = true;
      if (take) sites.push({ s: n.start, e: n.end, key: v,
        rep: (parent && parent.type === 'JSXAttribute' ? '{t(' + JSON.stringify(v) + ')}' : 't(' + src.slice(n.start, n.end) + ')') });
    } else if (n.type === 'JSXText' && n.value.trim()) {
      const v = n.value, lead = v.match(/^\s*/)[0], trail = v.match(/\s*$/)[0];
      const core = v.trim().replace(/\s*\n\s*/g, ' ');
      if (DE.test(core)) {
        const k = (lead && !lead.includes('\n') ? ' ' : '') + core + (trail && !trail.includes('\n') ? ' ' : '');
        sites.push({ s: n.start, e: n.end, key: k,
          rep: (lead.includes('\n') ? lead : '') + '{t(' + JSON.stringify(k) + ')}' + (trail.includes('\n') ? trail : '') });
      }
    }
    for (const f in n) {
      if (f === 'start' || f === 'end') continue;
      const c = n[f];
      if (Array.isArray(c)) c.forEach((x) => walk(x, n)); else if (c && typeof c.type === 'string') walk(c, n);
    }
  })(ast, null);
  sites.sort((a, b) => b.s - a.s);
  let out = src;
  for (const x of sites) out = out.slice(0, x.s) + x.rep + out.slice(x.e);
  out = "import { t } from './i18n-runtime.js';\n" + out;
  const keys = [...new Set(sites.sort((a, b) => a.s - b.s).map((x) => x.key))];
  return { code: out, keys };
}
