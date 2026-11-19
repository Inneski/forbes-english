// Chooses the helper language and translates the German source strings into it.
import DATA from './i18n-data.js';
export const NAMES = { de: 'Deutsch', en: 'English', es: 'Español', fr: 'Français', it: 'Italiano',
  pt: 'Português', ru: 'Русский', ar: 'العربية', zh: '中文', ja: '日本語', hr: 'Hrvatski' };
export const LANGS = ['de', ...Object.keys(DATA)];
function pick() {
  const ok = (l) => l && LANGS.includes(l) ? l : null;
  let q = null, saved = null;
  try { q = new URLSearchParams(location.search).get('lang'); } catch (e) {}
  try { saved = localStorage.getItem('blockcraft-lang'); } catch (e) {}
  const nav = (navigator.languages || [navigator.language || '']).map((l) => String(l).slice(0, 2).toLowerCase());
  return ok(q) || ok(saved) || nav.map(ok).find(Boolean) || 'de';
}
export const LANG = pick();
export function setLang(l) {
  try { localStorage.setItem('blockcraft-lang', l); } catch (e) {}
  const u = new URL(location.href); u.searchParams.set('lang', l); location.href = u.toString();
}
export function t(s) {
  if (LANG === 'de') return s;
  const d = DATA[LANG];
  return d && d[s] != null ? d[s] : s;
}
