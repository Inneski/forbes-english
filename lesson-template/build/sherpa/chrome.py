# -*- coding: utf-8 -*-
"""Sherpa-only interface strings, in every language a Sherpa deck can offer.

SH_CHROME is the family's own chrome: the route-map and voice links in the
deck bar, the example-translation picker, and camp two's frequency slider.
They are the same on every page, so they live here rather than in 25
translation files.

PL_CHROME is the deck engine's shared chrome (chrome_i18n.CHROME) for Polish,
which that module has never needed. Camps one and two offered Polish on their
scrolling pages, and the decks keep it.
"""

SH_CHROME = {
    'en': dict(navMap='Route map', navToPassive='Passive &#8646;', navToActive='Active &#8646;',
               navExOff='Examples: off', navExHint='Pick a language, then tap an example',
               ftKicker='Adverb of frequency', ftControl='Change the frequency',
               ftStart='Beginning', ftTime='Time', ftEnd='End',
               ftNone='Not once', ftDensity='{n} times in {m} chances'),
    'de': dict(navMap='Routenkarte', navToPassive='Passiv &#8646;', navToActive='Aktiv &#8646;',
               navExOff='Beispiele: aus', navExHint='Sprache wählen, dann auf ein Beispiel tippen',
               ftKicker='Häufigkeitsadverb', ftControl='Ändere die Häufigkeit',
               ftStart='Anfang', ftTime='Zeit', ftEnd='Ende',
               ftNone='Kein einziges Mal', ftDensity='{n}-mal bei {m} Gelegenheiten'),
    'es': dict(navMap='Mapa de la ruta', navToPassive='Pasiva &#8646;', navToActive='Activa &#8646;',
               navExOff='Ejemplos: no', navExHint='Elige un idioma y toca un ejemplo',
               ftKicker='Adverbio de frecuencia', ftControl='Cambia la frecuencia',
               ftStart='Inicio', ftTime='Tiempo', ftEnd='Fin',
               ftNone='Ni una vez', ftDensity='{n} veces de {m} ocasiones'),
    'fr': dict(navMap="Carte de l'itinéraire", navToPassive='Passif &#8646;', navToActive='Actif &#8646;',
               navExOff='Exemples : non', navExHint='Choisis une langue, puis touche un exemple',
               ftKicker='Adverbe de fréquence', ftControl='Change la fréquence',
               ftStart='Début', ftTime='Temps', ftEnd='Fin',
               ftNone='Pas une seule fois', ftDensity='{n} fois sur {m} occasions'),
    'it': dict(navMap='Mappa del percorso', navToPassive='Passivo &#8646;', navToActive='Attivo &#8646;',
               navExOff='Esempi: no', navExHint='Scegli una lingua, poi tocca un esempio',
               ftKicker='Avverbio di frequenza', ftControl='Cambia la frequenza',
               ftStart='Inizio', ftTime='Tempo', ftEnd='Fine',
               ftNone='Nemmeno una volta', ftDensity='{n} volte su {m} occasioni'),
    'pl': dict(navMap='Mapa trasy', navToPassive='Strona bierna &#8646;', navToActive='Strona czynna &#8646;',
               navExOff='Przykłady: nie', navExHint='Wybierz język, potem dotknij przykładu',
               ftKicker='Przysłówek częstotliwości', ftControl='Zmień częstotliwość',
               ftStart='Początek', ftTime='Czas', ftEnd='Koniec',
               ftNone='Ani razu', ftDensity='{n} razy na {m} okazji'),
    'ru': dict(navMap='Карта маршрута', navToPassive='Пассив &#8646;', navToActive='Актив &#8646;',
               navExOff='Примеры: нет', navExHint='Выбери язык и нажми на пример',
               ftKicker='Наречие частотности', ftControl='Измени частоту',
               ftStart='Начало', ftTime='Время', ftEnd='Конец',
               ftNone='Ни разу', ftDensity='{n} раз из {m} возможностей'),
    'zh': dict(navMap='路线图', navToPassive='被动语态 &#8646;', navToActive='主动语态 &#8646;',
               navExOff='例句：关', navExHint='先选语言，再点一个例句',
               ftKicker='频率副词', ftControl='调整频率',
               ftStart='开始', ftTime='时间', ftEnd='结束',
               ftNone='一次也没有', ftDensity='{m} 次机会中有 {n} 次'),
}

# Values are JS source, exactly as chrome_i18n.CHROME stores them.
PL_CHROME = {
    'btnStart': "'Zaczynamy →'", 'btnCheck': "'Sprawdź'", 'btnNext': "'Dalej →'",
    'btnRestart': "'Od nowa'", 'btnFull': "'Pełny ekran'", 'scoreLabel': "'Wynik'",
    'slideOf': '(a,b)=>`${a} / ${b}`', 'fbCorrect': "'Dobrze.'", 'fbWrong': "'Nie całkiem.'",
    'fbAnswer': "'Odpowiedź:'",
    'resNext': "'Rozpoznać język to połowa sukcesu. Teraz go użyj →'",
    'actEyebrow': "'Aktywacja'", 'actSpeakKind': "'Dyskusja · w parach'",
    'actSpeakWord': "'Dyskusja'", 'actWriteWord': "'Pisanie'",
    'btnCopy': "'Kopiuj'", 'btnCopied': "'Skopiowano'",
    'wordCount': "(n)=>`${n} ${n===1?'słowo':(n%10>=2&&n%10<=4&&(n%100<10||n%100>=20))?'słowa':'słów'}`",
    'btnOpen': "'Otwórz'", 'ledDp': "'DP'", 'ledTime': "'Czas'", 'ledClues': "'Wskazówki'",
}

# Where the switcher lists Polish; the template's LANGS never had it.
LANG_LABELS = {'pl': 'Polski'}
