# -*- coding: utf-8 -*-
"""Full Grammar Test — 45 questions, one file, nine support languages.

**This replaces a one-shot migration script.** The previous version of this
file read the pre-migration HTML, patched a logo, a hero, a language switcher
and a set of runtime i18n hooks into it, and wrote the result back over the
source. It could only ever run once: on a second run its very first
`assert intro_prefix_old in src` fails, because the intro it is looking for has
already been replaced by the intro it writes. It also loaded all three of its
data files from `/tmp`, which no longer exist. So the lesson was not
reproducible from source at all — editing a translation meant editing 112 KB of
generated HTML by hand.

What this version does instead is idempotent, and safe to run repeatedly:

  * the three i18n tables are re-injected from JSON committed beside this
    script, recovered out of the shipped HTML. Edit a translation there and
    re-run; that is now the supported way to change one.
  * the language switcher's buttons are regenerated from `LANGS`, so adding a
    language is a one-line change here rather than hand-edited markup.
  * every patch checks whether it has already been applied and skips it, but
    fails loudly if it finds *neither* the old form nor the new one — a genuine
    breakage still stops the build instead of passing silently.

**The merge.** `full_grammar_test.html` (DE) and `full_grammar_test_italian.html`
(IT) were the same lesson twice: 1242 of 1253 strings identical, and the only
differences were eleven pieces of page chrome — the title, the section
headings, the button labels, "Dein Ergebnis" against "Il tuo risultato".

Those eleven were never a real difference. `updateStaticUI()` rewrites every
one of them from `UI_I18N[currentLang]` on load, so the two files rendered
identically the moment their JavaScript ran; the hardcoded strings were only
what the server sent before that. The actual difference between the two files
was one line: `let currentLang = "de"` against `"it"`.

So the merge costs nothing. One file now reads its starting language from
`?lang=`, falling back to `de` so existing links keep behaving as they did.
`full_grammar_test_italian.html` becomes a redirect to `…?lang=it`, which keeps
every bookmark and every link from the catalogue working.

**English is now selectable.** `UI_I18N` and `SECTION_GLOSS` always carried an
`en` entry, but `LANGS` never offered it, so there was no way to see the test
without an L1 gloss over it. `QUESTION_I18N` has no `en` — correctly, since the
questions are already English — so the per-question gloss is now guarded and
simply renders empty for English rather than throwing.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, 'full_grammar_test.html')
OLD_IT = os.path.join(ROOT, 'full_grammar_test_italian.html')

UI_I18N = json.load(open(os.path.join(HERE, 'ui_i18n.json'), encoding='utf-8'))
SECTION_GLOSS = json.load(open(os.path.join(HERE, 'sections_i18n.json'), encoding='utf-8'))
QUESTION_I18N = json.load(open(os.path.join(HERE, 'all_questions_i18n.json'), encoding='utf-8'))

# English first: it is the no-gloss view, and it is the one that was missing.
LANGS = [
    {"code": "en", "flag": "\U0001F1EC\U0001F1E7", "name": "English"},
    {"code": "de", "flag": "\U0001F1E9\U0001F1EA", "name": "Deutsch"},
    {"code": "it", "flag": "\U0001F1EE\U0001F1F9", "name": "Italiano"},
    {"code": "es", "flag": "\U0001F1EA\U0001F1F8", "name": "Español"},
    {"code": "fr", "flag": "\U0001F1EB\U0001F1F7", "name": "Français"},
    {"code": "ja", "flag": "\U0001F1EF\U0001F1F5", "name": "日本語"},
    {"code": "zh", "flag": "\U0001F1E8\U0001F1F3", "name": "中文"},
    {"code": "ar", "flag": "\U0001F1F8\U0001F1E6", "name": "العربية"},
    {"code": "ru", "flag": "\U0001F1F7\U0001F1FA", "name": "Русский"},
    {"code": "pt", "flag": "\U0001F1F5\U0001F1F9", "name": "Português"},
]
DEFAULT_LANG = 'de'


def patch(src, old, new, what):
    """Apply a replacement, or confirm it is already applied. Never silent."""
    # Check the NEW form first. Two of these replacements embed their own
    # search string inside their replacement, so an old-first check re-wraps
    # them on every run — which is exactly how the previous script's output
    # would have drifted had it ever been runnable twice.
    if new in src:
        return src                      # already done on a previous run
    if old in src:
        return src.replace(old, new)
    raise AssertionError('%s: found neither the old form nor the new one — the '
                         'page has changed underneath this builder' % what)


def build():
    src = open(OUT, encoding='utf-8').read()

    # ── the i18n tables, re-injected from the committed JSON ──────────
    for name, data in (('LANGS', LANGS), ('UI_I18N', UI_I18N),
                       ('SECTION_GLOSS', SECTION_GLOSS), ('QUESTION_I18N', QUESTION_I18N)):
        pat = re.compile(r'const %s = (?:\{.*?\}|\[.*?\]);\n' % name, re.S)
        assert pat.search(src), 'could not find const %s in the page' % name
        src = pat.sub('const %s = %s;\n' % (name, json.dumps(data, ensure_ascii=False)), src, count=1)

    # ── the switcher buttons, regenerated from LANGS ──────────────────
    buttons = "\n".join(
        '      <button class="lang-btn" data-lang="%s"><span class="flag">%s</span>%s</button>'
        % (l['code'], l['flag'], l['name']) for l in LANGS)
    src = re.sub(r'(<div class="lang-grid" id="langGrid">\n).*?(\n\s*</div>)',
                 lambda m: m.group(1) + buttons + m.group(2), src, count=1, flags=re.S)

    # ── the merge: starting language comes from ?lang=, not the filename ──
    src = patch(
        src,
        'let currentLang = "%s";' % DEFAULT_LANG,
        '''let currentLang = (function(){
  // The two files this lesson used to ship as differed in exactly this line.
  // Now the language is a parameter, so one file serves every reader and
  // full_grammar_test_italian.html redirects here with ?lang=it.
  var want = new URLSearchParams(location.search).get('lang');
  return LANGS.some(function(l){ return l.code === want; }) ? want : "%s";
})();''' % DEFAULT_LANG,
        'currentLang initialiser')

    # ── English has no per-question gloss, and does not need one ──────
    src = patch(src, '${QUESTION_I18N[currentLang][qi][0]}',
                '${(QUESTION_I18N[currentLang]||{})[qi] ? QUESTION_I18N[currentLang][qi][0] : ""}',
                'question gloss')
    src = patch(src, 'QUESTION_I18N[currentLang][qi][1]',
                '((QUESTION_I18N[currentLang]||{})[qi] ? QUESTION_I18N[currentLang][qi][1] : "")',
                'feedback gloss')

    # ── keep the URL honest as the reader switches ────────────────────
    src = patch(
        src,
        """  currentLang = btn.dataset.lang;
  updateStaticUI();""",
        """  currentLang = btn.dataset.lang;
  // So a chosen language survives a reload or a shared link.
  try {
    var u = new URL(location.href);
    u.searchParams.set('lang', currentLang);
    history.replaceState(null, '', u);
  } catch (e) { /* file:// — nothing to keep */ }
  updateStaticUI();""",
        'switcher URL sync')

    open(OUT, 'w', encoding='utf-8').write(src)

    # ── the Italian filename keeps working ────────────────────────────
    redirect = '''<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<title>Full Grammar Test — Forbes English</title>
<link rel="canonical" href="full_grammar_test.html">
<meta http-equiv="refresh" content="0; url=full_grammar_test.html?lang=it">
<script>location.replace('full_grammar_test.html?lang=it');</script>
</head>
<body>
<p>Questa lezione ora vive in un unico file con tutte le lingue.
<a href="full_grammar_test.html?lang=it">Continua qui</a>.</p>
</body>
</html>
'''
    open(OLD_IT, 'w', encoding='utf-8').write(redirect)

    print('wrote %s (%d bytes, %d languages, default %s)'
          % (os.path.basename(OUT), len(src), len(LANGS), DEFAULT_LANG))
    print('wrote %s (%d bytes, redirect -> ?lang=it)'
          % (os.path.basename(OLD_IT), len(redirect)))


if __name__ == '__main__':
    build()
