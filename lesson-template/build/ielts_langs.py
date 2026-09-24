# -*- coding: utf-8 -*-
"""The ten languages of the IELTS route, and what its i18n modules need for the
seven added on 2026-09-24.

Innes, 2026-09-24: add French, Italian, Portuguese, Russian, Arabic, Chinese
and Japanese "to all IELTS". The route had gone out in English, German and
Spanish, the house minimum, while the candidates come from everywhere.

Conventions, taken from chrome_i18n.CHROME so that a deck's own text and its
buttons speak with one voice: French and Russian address the learner as
vous / вы, Italian and Portuguese as tu (Portuguese is European: "Seguinte",
"Carrega", "diapositivo"), Japanese is です/ます, Chinese is Simplified with
full-width punctuation, Arabic is Modern Standard Arabic with Western digits.
The English under test (passages, statements, options, examples in <em>) stays
English in every language, as in German and Spanish.

TAIL: the IELTS i18n modules carry six labels the template reads that are not
in every language of CHROME. The ledger three come from CHROME, so they cannot
drift; the gloss button and the branch lock are here.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

MORE = ('fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja')
LANGS = ('en', 'de', 'es') + MORE

_LABELS = {
    #      glossShow    glossHide   branchLocked
    'fr': ('Traduire', 'Masquer', 'Votre registre ne permet pas cette fin'),
    'it': ('Traduci', 'Nascondi', 'Il tuo registro non consente questo finale'),
    'pt': ('Traduzir', 'Ocultar', 'O teu registo não permite este final'),
    'ru': ('Перевести', 'Скрыть', 'Ваш журнал не допускает этот финал'),
    'ar': ('ترجمة', 'إخفاء', 'سجلّك لا يسمح بهذه النهاية'),
    'zh': ('翻译', '隐藏', '你的记录不支持这个结局'),
    'ja': ('翻訳', '隠す', 'この記録ではこの結末に進めません'),
}

TAIL_MORE = {
    c: {'branchLocked': "'%s'" % lock, 'glossHide': "'%s'" % hide,
        'glossShow': "'%s'" % show, 'ledClues': CHROME[c]['ledClues'],
        'ledDp': CHROME[c]['ledDp'], 'ledTime': CHROME[c]['ledTime']}
    for c, (show, hide, lock) in _LABELS.items()
}
