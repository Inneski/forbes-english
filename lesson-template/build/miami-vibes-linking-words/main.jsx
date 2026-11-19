import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App.build.jsx';
import { LANG, LANGS, NAMES, setLang } from './i18n-runtime.js';

document.documentElement.setAttribute('data-helper-lang', LANG);
if (LANG === 'ar') document.documentElement.classList.add('helper-rtl');

function LangSwitch() {
  if (LANGS.length < 2) return null;
  return (
    <label className="fe-lang">
      <span aria-hidden="true">🌐</span>
      <select aria-label="Language" value={LANG} onChange={(e) => setLang(e.target.value)}>
        {LANGS.map((l) => <option key={l} value={l}>{NAMES[l] || l}</option>)}
      </select>
    </label>
  );
}

createRoot(document.getElementById('root')).render(<><App /><LangSwitch /></>);
