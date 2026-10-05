/* Block Camp: full screen on a phone, and the way to it on an iPhone.

   Innes, 2026-10-02: "make block camp easier to use on mobile phones (full
   screen pop out ideally)".

   What a web page can do about the browser's bars depends on the phone:

   - Android (Chrome, Samsung Internet, Firefox), iPads and laptops have the
     Fullscreen API. It needs a tap to start, and it ENDS AT EVERY PAGE
     NAVIGATION: the next camp, the map, an adventure are all new pages. So
     the choice is remembered for the tab (sessionStorage 'camp-full') and the
     learner's first tap on the next page puts it back. A tap is the only
     thing a browser accepts for that; nothing can do it on load.
   - iPhones have no Fullscreen API for anything but a <video> (iOS 26 still
     reports document.fullscreenEnabled false). The one way to lose Safari's
     bars is to add the site to the Home Screen: since iOS 26 every such icon
     opens as a web app with no browser UI. So on an iPhone the same button
     opens a short how-to, in the page's language, instead of doing nothing
     (the RPGs' FULLSCREEN button did nothing on an iPhone until today).
   - Opened from the Home Screen (display-mode standalone / fullscreen, or
     navigator.standalone) the page already has the whole screen: the button
     hides itself.

   "Pop out": on a phone the deck's Begin and the adventures' first button
   call CampFull.popOut() from inside their own tap, which enters full screen
   where the phone can. Leaving full screen (the button, the back gesture)
   is a choice the learner made, so nothing pops out again in that tab.

   Loaded with <script src="…/camp-full.js" defer></script>. Where the button
   goes, like camp-music.js:
     deck  - the grammar decks' .deck-bar, after the language controls (on a
             phone camp-phone.css sizes it for the thumb bar);
     rpg   - the RPG engine's own #fullscreen utility button is taken over;
     other - any element marked data-camp-full becomes a toggle.
   Pages with chrome of their own (the site's nav band over the village or a
   map) hide it under html.camp-fs, which is on while the page is full screen.

   Window API: CampFull.toggle(), .popOut(), .isOn(), .can, .installed,
   .bind(el), .howTo(). */
(function () {
  'use strict';
  if (window.CampFull) return;
  var d = document, html = d.documentElement, ua = navigator.userAgent || '';

  function fsEl() { return d.fullscreenElement || d.webkitFullscreenElement || null; }
  var req = html.requestFullscreen || html.webkitRequestFullscreen;
  var can = !!(req && (d.fullscreenEnabled || d.webkitFullscreenEnabled));
  function mq(q) { try { return !!(window.matchMedia && matchMedia(q).matches); } catch (_) { return false; } }
  var installed = navigator.standalone === true ||
    mq('(display-mode: standalone)') || mq('(display-mode: fullscreen)') || mq('(display-mode: minimal-ui)');
  // iPadOS asks for desktop pages and reports itself as a Mac; touch gives it away.
  var ios = /iP(hone|od|ad)/.test(ua) || (/Macintosh/.test(ua) && navigator.maxTouchPoints > 1);
  // In-app browsers (Instagram, Facebook, LINE…) cannot add to the Home Screen.
  var inApp = /FBAN|FBAV|Instagram|Line\/|MicroMessenger|GSA\//.test(ua);
  var safari26 = /Version\/(2[6-9]|[3-9]\d)\./.test(ua) && /Safari/.test(ua) && !/CriOS|FxiOS|EdgiOS/.test(ua);
  function phone() {
    return Math.min(screen.width || innerWidth, screen.height || innerHeight) < 600 && mq('(pointer: coarse)');
  }
  if (installed) html.classList.add('camp-app');

  /* ── one app for the whole of Block Camp ───────────────────────────── */
  // The Quest's manifest (written by block-camp-quest/build.py) has scope
  // '/block': a plain string prefix in both WebKit and Chromium, so it holds
  // /block-camp.html, both maps, /block-camp/* and every /blockcamp-* deck,
  // and nothing else on the site. Every Block Camp page links it, so the
  // Home Screen icon is the same app wherever it was added from, and moving
  // between camps stays inside it. iOS 17/18 also want the apple meta.
  (function () {
    var me = d.currentScript && d.currentScript.src;
    if (!me || !d.head) return;
    var base = me.replace(/[^\/]*$/, '');
    function add(tag, attrs) {
      var el = d.createElement(tag);
      for (var k in attrs) el.setAttribute(k, attrs[k]);
      d.head.appendChild(el);
    }
    if (!d.querySelector('link[rel="manifest"]')) add('link', { rel: 'manifest', href: base + 'manifest.webmanifest' });
    if (!d.querySelector('link[rel="apple-touch-icon"]')) add('link', { rel: 'apple-touch-icon', href: base + 'quest-icons/icon-192.png' });
    if (!d.querySelector('meta[name="apple-mobile-web-app-capable"]')) add('meta', { name: 'apple-mobile-web-app-capable', content: 'yes' });
    if (!d.querySelector('meta[name="mobile-web-app-capable"]')) add('meta', { name: 'mobile-web-app-capable', content: 'yes' });
    if (!d.querySelector('meta[name="apple-mobile-web-app-title"]')) add('meta', { name: 'apple-mobile-web-app-title', content: 'Block Camp' });
  })();

  /* ── the words ─────────────────────────────────────────────────────── */
  var T = {
    en: { on: 'Full screen', off: 'Leave full screen',
          title: 'Full screen on an iPhone',
          lede: 'An iPhone will not let a web page hide Safari’s bars. Put Block Camp on your Home Screen instead: it then opens full screen, like an app.',
          s1: 'Tap Share {share}', s1b: 'In Safari 26, it is in the ••• menu.',
          s2: 'Tap Add to Home Screen {add}',
          s3: 'Tap Add. If you see Open as Web App, leave it on.',
          s4: 'Open Block Camp from the new icon.',
          inApp: 'Open this page in Safari first: this app’s browser cannot add it.',
          other: 'Open your browser’s menu {dots} and choose Add to Home screen or Install app. Block Camp then opens full screen.',
          note: 'On an iPhone the new icon keeps its own progress and sign-in, apart from Safari. To take your progress with you, copy your save code on the Quest page (Passport) first.',
          ok: 'Got it' },
    de: { on: 'Vollbild', off: 'Vollbild beenden',
          title: 'Vollbild auf dem iPhone',
          lede: 'Auf dem iPhone darf eine Webseite die Leisten von Safari nicht ausblenden. Leg Block Camp stattdessen auf den Home-Bildschirm: Dann öffnet es sich im Vollbild, wie eine App.',
          s1: 'Tippe auf Teilen {share}', s1b: 'In Safari 26 steckt es im Menü •••.',
          s2: 'Tippe auf Zum Home-Bildschirm {add}',
          s3: 'Tippe auf Hinzufügen. Wenn du Als Web-App öffnen siehst, lass es eingeschaltet.',
          s4: 'Öffne Block Camp über das neue Symbol.',
          inApp: 'Öffne diese Seite zuerst in Safari: Der Browser dieser App kann sie nicht hinzufügen.',
          other: 'Öffne das Menü deines Browsers {dots} und wähle Zum Startbildschirm hinzufügen oder App installieren. Dann öffnet sich Block Camp im Vollbild.',
          note: 'Auf dem iPhone hat das neue Symbol seinen eigenen Fortschritt und seine eigene Anmeldung, getrennt von Safari. Um deinen Fortschritt mitzunehmen, kopiere zuerst deinen Speichercode auf der Quest-Seite (Passport).',
          ok: 'Verstanden' },
    es: { on: 'Pantalla completa', off: 'Salir de pantalla completa',
          title: 'Pantalla completa en el iPhone',
          lede: 'En el iPhone, una página web no puede ocultar las barras de Safari. Añade Block Camp a tu pantalla de inicio: así se abre a pantalla completa, como una app.',
          s1: 'Toca Compartir {share}', s1b: 'En Safari 26 está en el menú •••.',
          s2: 'Toca Añadir a pantalla de inicio {add}',
          s3: 'Toca Añadir. Si ves Abrir como app web, déjalo activado.',
          s4: 'Abre Block Camp desde el nuevo icono.',
          inApp: 'Abre primero esta página en Safari: el navegador de esta app no puede añadirla.',
          other: 'Abre el menú del navegador {dots} y elige Añadir a pantalla de inicio o Instalar aplicación. Block Camp se abrirá a pantalla completa.',
          note: 'En el iPhone, el nuevo icono guarda su propio progreso e inicio de sesión, aparte de Safari. Para llevarte tu progreso, copia antes tu código de guardado en la página de la Quest (Passport).',
          ok: 'Entendido' },
    fr: { on: 'Plein écran', off: 'Quitter le plein écran',
          title: 'Plein écran sur iPhone',
          lede: 'Sur iPhone, une page web ne peut pas masquer les barres de Safari. Ajoutez Block Camp à l’écran d’accueil : il s’ouvrira alors en plein écran, comme une app.',
          s1: 'Touchez Partager {share}', s1b: 'Dans Safari 26, il se trouve dans le menu •••.',
          s2: 'Touchez Sur l’écran d’accueil {add}',
          s3: 'Touchez Ajouter. Si vous voyez Ouvrir en tant qu’app web, laissez-le activé.',
          s4: 'Ouvrez Block Camp depuis la nouvelle icône.',
          inApp: 'Ouvrez d’abord cette page dans Safari : le navigateur de cette app ne peut pas l’ajouter.',
          other: 'Ouvrez le menu du navigateur {dots} et choisissez Ajouter à l’écran d’accueil ou Installer l’application. Block Camp s’ouvrira en plein écran.',
          note: 'Sur iPhone, la nouvelle icône garde sa propre progression et sa propre connexion, à part de Safari. Pour garder votre progression, copiez d’abord votre code de sauvegarde sur la page Quest (Passport).',
          ok: 'Compris' },
    it: { on: 'Schermo intero', off: 'Esci dallo schermo intero',
          title: 'Schermo intero su iPhone',
          lede: 'Su iPhone una pagina web non può nascondere le barre di Safari. Aggiungi Block Camp alla schermata Home: si aprirà a schermo intero, come un’app.',
          s1: 'Tocca Condividi {share}', s1b: 'In Safari 26 si trova nel menu •••.',
          s2: 'Tocca Aggiungi alla schermata Home {add}',
          s3: 'Tocca Aggiungi. Se vedi Apri come app web, lascialo attivo.',
          s4: 'Apri Block Camp dalla nuova icona.',
          inApp: 'Apri prima questa pagina in Safari: il browser di questa app non può aggiungerla.',
          other: 'Apri il menu del browser {dots} e scegli Aggiungi a schermata Home o Installa app. Block Camp si aprirà a schermo intero.',
          note: 'Su iPhone la nuova icona ha i propri progressi e il proprio accesso, separati da Safari. Per portare con te i progressi, copia prima il codice di salvataggio nella pagina della Quest (Passport).',
          ok: 'Ho capito' },
    pt: { on: 'Tela cheia', off: 'Sair da tela cheia',
          title: 'Tela cheia no iPhone',
          lede: 'No iPhone, uma página da web não pode esconder as barras do Safari. Adicione o Block Camp à Tela de Início: ele passa a abrir em tela cheia, como um app.',
          s1: 'Toque em Compartilhar {share}', s1b: 'No Safari 26, fica no menu •••.',
          s2: 'Toque em Adicionar à Tela de Início {add}',
          s3: 'Toque em Adicionar. Se aparecer Abrir como App Web, deixe ativado.',
          s4: 'Abra o Block Camp pelo novo ícone.',
          inApp: 'Abra esta página no Safari primeiro: o navegador deste app não consegue adicioná-la.',
          other: 'Abra o menu do navegador {dots} e escolha Adicionar à tela inicial ou Instalar app. O Block Camp vai abrir em tela cheia.',
          note: 'No iPhone, o novo ícone guarda o próprio progresso e o próprio login, separados do Safari. Para levar seu progresso, copie antes o código de salvamento na página da Quest (Passport).',
          ok: 'Entendi' },
    ru: { on: 'Во весь экран', off: 'Выйти из полноэкранного режима',
          title: 'Во весь экран на iPhone',
          lede: 'На iPhone веб-страница не может скрыть панели Safari. Добавьте Block Camp на экран «Домой» — тогда он будет открываться во весь экран, как приложение.',
          s1: 'Нажмите «Поделиться» {share}', s1b: 'В Safari 26 эта кнопка в меню •••.',
          s2: 'Нажмите «На экран „Домой“» {add}',
          s3: 'Нажмите «Добавить». Если видите «Открыть как веб-приложение», оставьте включённым.',
          s4: 'Откройте Block Camp через новый значок.',
          inApp: 'Сначала откройте эту страницу в Safari: браузер этого приложения не может её добавить.',
          other: 'Откройте меню браузера {dots} и выберите «Добавить на главный экран» или «Установить приложение». Block Camp будет открываться во весь экран.',
          note: 'На iPhone у нового значка свой прогресс и свой вход, отдельно от Safari. Чтобы перенести прогресс, сначала скопируйте код сохранения на странице Quest (Passport).',
          ok: 'Понятно' },
    ar: { on: 'ملء الشاشة', off: 'الخروج من ملء الشاشة',
          title: 'ملء الشاشة على iPhone',
          lede: 'لا يسمح iPhone لصفحة ويب بإخفاء أشرطة Safari. أضف Block Camp إلى الشاشة الرئيسية بدلًا من ذلك، فيفتح بملء الشاشة مثل التطبيق.',
          s1: 'اضغط على مشاركة {share}', s1b: 'في Safari 26 تجده في قائمة •••.',
          s2: 'اضغط على إضافة إلى الشاشة الرئيسية {add}',
          s3: 'اضغط على إضافة. إذا ظهر خيار الفتح كتطبيق ويب، فأبقِه مفعّلًا.',
          s4: 'افتح Block Camp من الأيقونة الجديدة.',
          inApp: 'افتح هذه الصفحة في Safari أولًا: متصفح هذا التطبيق لا يستطيع إضافتها.',
          other: 'افتح قائمة المتصفح {dots} واختر الإضافة إلى الشاشة الرئيسية أو تثبيت التطبيق. سيفتح Block Camp بعدها بملء الشاشة.',
          note: 'على iPhone تحتفظ الأيقونة الجديدة بتقدّمها وتسجيل دخولها بعيدًا عن Safari. لتنقل تقدّمك، انسخ أولًا رمز الحفظ من صفحة Quest (Passport).',
          ok: 'فهمت' },
    zh: { on: '全屏', off: '退出全屏',
          title: '在 iPhone 上全屏',
          lede: 'iPhone 不允许网页隐藏 Safari 的工具栏。把 Block Camp 添加到主屏幕，它就会像 App 一样全屏打开。',
          s1: '轻点“共享” {share}', s1b: '在 Safari 26 中，它在 ••• 菜单里。',
          s2: '轻点“添加到主屏幕” {add}',
          s3: '轻点“添加”。如果看到“作为网页 App 打开”，请保持开启。',
          s4: '从新图标打开 Block Camp。',
          inApp: '请先在 Safari 中打开此页面：这个 App 的内置浏览器无法添加。',
          other: '打开浏览器菜单 {dots}，选择“添加到主屏幕”或“安装应用”。之后 Block Camp 会全屏打开。',
          note: '在 iPhone 上，新图标有自己的进度和登录，与 Safari 分开。想带上进度，请先在 Quest 页面（Passport）复制你的存档码。',
          ok: '知道了' },
    ja: { on: '全画面', off: '全画面を終了',
          title: 'iPhoneで全画面にする',
          lede: 'iPhoneでは、WebページがSafariのバーを隠すことはできません。Block Campをホーム画面に追加すると、アプリのように全画面で開きます。',
          s1: '共有 {share} をタップ', s1b: 'Safari 26では ••• メニューの中にあります。',
          s2: '「ホーム画面に追加」{add} をタップ',
          s3: '「追加」をタップ。「Webアプリとして開く」が表示されたら、オンのままにします。',
          s4: '新しいアイコンからBlock Campを開きます。',
          inApp: 'まずこのページをSafariで開いてください。このアプリ内のブラウザでは追加できません。',
          other: 'ブラウザのメニュー {dots} を開き、「ホーム画面に追加」または「アプリをインストール」を選びます。Block Campが全画面で開くようになります。',
          note: 'iPhoneでは、新しいアイコンの進み具合とログインはSafariとは別になります。進み具合を引き継ぐには、先にQuestページ（Passport）でセーブコードをコピーしてください。',
          ok: 'OK' }
  };
  function lang() { return (html.getAttribute('lang') || 'en').toLowerCase().slice(0, 2); }
  function w(k) { var L = T[lang()] || T.en; return L[k] != null ? L[k] : T.en[k]; }

  /* ── the pictures ──────────────────────────────────────────────────── */
  // Four corners out = go full screen; four corners in = leave it.
  var ICON_ON = '<svg class="cf-i" viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" ' +
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/></svg>';
  var ICON_OFF = '<svg class="cf-i" viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" ' +
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 4v5H4M15 4v5h5M9 20v-5H4M15 20v-5h5"/></svg>';
  // iOS's own Share and Add glyphs, drawn to sit in a line of text.
  var SHARE = '<svg class="cf-g" viewBox="0 0 20 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" ' +
    'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M10 2v13M5.5 6.5 10 2l4.5 4.5"/>' +
    '<path d="M6.5 10H4.5a1.5 1.5 0 0 0-1.5 1.5v9A1.5 1.5 0 0 0 4.5 22h11a1.5 1.5 0 0 0 1.5-1.5v-9a1.5 1.5 0 0 0-1.5-1.5h-2"/></svg>';
  var ADD = '<svg class="cf-g" viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" ' +
    'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="4"/>' +
    '<path d="M12 8v8M8 12h8"/></svg>';
  var DOTS = '<svg class="cf-g" viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="currentColor">' +
    '<circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/></svg>';

  /* ── the look ──────────────────────────────────────────────────────── */
  // Theme tokens with Block Camp's own greens behind them, so the sheet sits
  // in each page's palette and still reads on a page that has none.
  var css = d.createElement('style');
  css.id = 'camp-full-css';
  css.textContent =
    '.camp-full{display:inline-flex;align-items:center;justify-content:center;gap:7px;flex:none;box-sizing:border-box;' +
    'height:34px;min-width:34px;padding:0 9px;border-radius:6px;cursor:pointer;white-space:nowrap;' +
    'font-family:var(--font-mono,inherit);font-size:12px;letter-spacing:.06em;text-transform:uppercase;' +
    'background:var(--scrim);color:var(--text);border:1px solid color-mix(in srgb,var(--border) 70%,transparent);' +
    'transition:border-color .15s,color .15s}' +
    '.camp-full:hover,.camp-full:focus-visible{border-color:var(--accent);color:var(--accent-bright,var(--accent))}' +
    '.camp-full .cf-i{width:17px;height:17px;flex:none}' +
    '.camp-full[aria-pressed="true"]{color:var(--accent-bright,var(--accent));border-color:var(--accent)}' +
    '.camp-app .camp-full,.camp-app [data-camp-full],.camp-app #fullscreen.utility{display:none!important}' +
    '.cf-sheet{position:fixed;inset:0;z-index:2147483000;display:grid;place-items:end center;' +
    'padding:16px 12px calc(16px + env(safe-area-inset-bottom,0px));box-sizing:border-box;' +
    'background:color-mix(in srgb,var(--void,#0b1a12) 62%,transparent);animation:cf-fade .18s ease both}' +
    '.cf-sheet[hidden]{display:none}' +
    '.cf-card{width:min(440px,100%);max-height:calc(100% - 8px);overflow:auto;box-sizing:border-box;padding:20px 20px 16px;' +
    'border-radius:16px;background:var(--surface2,#14301f);color:var(--text,#f2f7f3);' +
    'border:1px solid color-mix(in srgb,var(--accent,#e8c04a) 55%,transparent);' +
    'box-shadow:0 18px 50px color-mix(in srgb,var(--void,#0b1a12) 80%,transparent);' +
    'font-family:var(--font-read,var(--font-ui,system-ui,-apple-system,sans-serif));font-size:16px;line-height:1.45;' +
    'text-align:start;animation:cf-up .22s cubic-bezier(.2,.8,.3,1) both}' +
    '.cf-card h2{margin:0 0 8px;font:inherit;font-size:20px;font-weight:700;line-height:1.2;color:var(--accent-bright,var(--accent,#e8c04a))}' +
    '.cf-card p{margin:0 0 12px}' +
    '.cf-card ol{margin:0 0 12px;padding-inline-start:1.4em}' +
    '.cf-card li{margin:0 0 8px;padding-inline-start:.2em}' +
    '.cf-card li small{display:block;font-size:14px;opacity:.78}' +
    '.cf-card .cf-g{display:inline-block;width:1.2em;height:1.2em;vertical-align:-.25em;margin:0 .1em;color:var(--accent-bright,var(--accent,#e8c04a))}' +
    '.cf-card .cf-note{font-size:14px;opacity:.82}' +
    '.cf-card .cf-ok{display:block;width:100%;min-height:48px;margin-top:6px;border:0;border-radius:10px;cursor:pointer;' +
    'font:inherit;font-weight:700;text-transform:none;letter-spacing:normal;background:var(--accent,#e8c04a);color:var(--void,#0b1a12)}' +
    '.cf-card,.cf-card *{text-transform:none;letter-spacing:normal}' +
    // A landscape phone is ~340px tall: the card scrolls, Got it stays in reach.
    '.cf-card .cf-ok{position:sticky;bottom:0;box-shadow:0 -10px 14px var(--surface2,#14301f)}' +
    '@media (max-height:480px){.cf-sheet{place-items:center;padding-top:8px;padding-bottom:8px}' +
    '.cf-card{width:min(640px,100%);padding:14px 18px 12px;font-size:15px}.cf-card h2{font-size:18px;margin-bottom:4px}' +
    '.cf-card p,.cf-card ol{margin-bottom:8px}.cf-card li{margin-bottom:4px}.cf-card .cf-ok{min-height:44px}}' +
    '@keyframes cf-fade{from{opacity:0}}@keyframes cf-up{from{transform:translateY(24px);opacity:0}}' +
    '@media (prefers-reduced-motion:reduce){.cf-sheet,.cf-card{animation:none}}' +
    '@media print{.camp-full,.cf-sheet{display:none!important}}';
  (d.head || html).appendChild(css);

  /* ── remembering the choice across pages ───────────────────────────── */
  var KEY = 'camp-full';                  // '1' wants full screen, '0' left it
  function want(v) {
    try { if (v == null) return sessionStorage.getItem(KEY); sessionStorage.setItem(KEY, v); } catch (_) {}
    return null;
  }
  // A navigation ends full screen too, and that must not count as leaving it.
  // The exit is written only if the page is still here a moment later; a page
  // that is being replaced never runs the timer.
  var leaving = false;
  addEventListener('pagehide', function () { leaving = true; });
  addEventListener('beforeunload', function () { leaving = true; });
  d.addEventListener('click', function (e) {
    var a = e.target && e.target.closest && e.target.closest('a[href]');
    if (a && !a.target && !a.hasAttribute('download') && a.getAttribute('href').charAt(0) !== '#') leaving = true;
  }, true);
  addEventListener('pageshow', function () { leaving = false; });

  /* ── doing it ──────────────────────────────────────────────────────── */
  function isOn() { return !!fsEl(); }
  function enter() {
    if (!can || fsEl()) return;
    try { var p = req.call(html, { navigationUI: 'hide' }); if (p && p.then) p.then(null, function () {}); } catch (_) {}
  }
  function exit() {
    var x = d.exitFullscreen || d.webkitExitFullscreen;
    try { var p = x && x.call(d); if (p && p.then) p.then(null, function () {}); } catch (_) {}
  }
  function toggle() {
    if (fsEl()) { want('0'); exit(); return; }
    if (can) { want('1'); enter(); return; }
    if (!installed) howTo();
  }
  // From inside the page's own start tap, on a phone only, unless the
  // learner has already said no in this tab.
  function popOut() {
    if (!can || fsEl() || !phone() || want() === '0') return;
    want('1'); enter();
  }

  var bound = [];
  function paint() {
    var on = isOn();
    html.classList.toggle('camp-fs', on);
    bound.forEach(function (b) {
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
      var label = on ? w('off') : w('on');
      b.setAttribute('aria-label', label);
      b.title = label;
      var i = b.querySelector('.cf-i');
      if (i) i.outerHTML = on ? ICON_OFF : ICON_ON;
      var l = b.querySelector('.cf-l');
      if (l) l.textContent = b.classList.contains('utility') ? label.toUpperCase() : label;
    });
  }
  function bind(b) {
    if (!b || b._campFull) return b;
    b._campFull = true;
    bound.push(b);
    b.addEventListener('click', function (e) { e.preventDefault(); e.stopImmediatePropagation(); toggle(); }, true);
    if (installed) b.hidden = true;
    paint();
    return b;
  }
  ['fullscreenchange', 'webkitfullscreenchange'].forEach(function (ev) {
    d.addEventListener(ev, function () {
      paint();
      if (fsEl()) { want('1'); return; }
      setTimeout(function () { if (!leaving && !fsEl()) want('0'); }, 700);
    });
  });

  // Back in full screen on the first tap of the next page.
  if (can && !installed && want() === '1' && !fsEl()) {
    var again = function (e) {
      var a = e.target && e.target.closest && e.target.closest('a[href]');
      if (a && a.getAttribute('href').charAt(0) !== '#') return;   // that tap is leaving anyway
      d.removeEventListener('click', again, true);
      enter();
    };
    d.addEventListener('click', again, true);
  }

  /* ── the iPhone how-to ─────────────────────────────────────────────── */
  var sheet = null, before = null;
  function howTo() {
    if (!sheet) {
      sheet = d.createElement('div');
      sheet.className = 'cf-sheet';
      sheet.hidden = true;
      sheet.setAttribute('role', 'dialog');
      sheet.setAttribute('aria-modal', 'true');
      sheet.addEventListener('click', function (e) { if (e.target === sheet || e.target.closest('.cf-ok')) close(); });
      sheet.addEventListener('keydown', function (e) { if (e.key === 'Escape') { e.stopPropagation(); close(); } });
      d.body.appendChild(sheet);
    }
    var steps = ios
      ? '<ol><li>' + w('s1').replace('{share}', SHARE) + (safari26 ? '<small>' + w('s1b') + '</small>' : '') + '</li>' +
        '<li>' + w('s2').replace('{add}', ADD) + '</li><li>' + w('s3') + '</li><li>' + w('s4') + '</li></ol>'
      : '<p>' + w('other').replace('{dots}', DOTS) + '</p>';
    sheet.innerHTML = '<div class="cf-card" dir="auto" aria-labelledby="cf-t"><h2 id="cf-t">' +
      (ios ? w('title') : w('on')) + '</h2>' +
      (ios ? '<p>' + w('lede') + '</p>' : '') +
      (ios && inApp ? '<p><b>' + w('inApp') + '</b></p>' : '') +
      steps + (ios ? '<p class="cf-note">' + w('note') + '</p>' : '') +
      '<button type="button" class="cf-ok">' + w('ok') + '</button></div>';
    sheet.dir = lang() === 'ar' ? 'rtl' : 'ltr';
    before = d.activeElement;
    sheet.hidden = false;
    var ok = sheet.querySelector('.cf-ok');
    try { ok.focus({ preventScroll: true }); } catch (_) {}
  }
  function close() {
    if (!sheet) return;
    sheet.hidden = true;
    if (before && before.focus) try { before.focus({ preventScroll: true }); } catch (_) {}
  }

  /* ── where the button goes ─────────────────────────────────────────── */
  function place() {
    var bar = d.querySelector('.deck-bar');
    if (bar && !bar.querySelector('.camp-full')) {
      var b = d.createElement('button');
      b.type = 'button';
      b.className = 'camp-full';
      b.innerHTML = ICON_ON;
      // After the language controls and the part chip, before the arrows:
      // on a phone those controls move into the menu, which leaves it
      // beside the menu button, away from Next.
      var prev = bar.querySelector('.nav-btn[data-action="prev"]');
      var anchor = bar.querySelector('.ledger') || prev;
      bar.insertBefore(b, anchor && anchor.parentNode === bar ? anchor : null);
      bind(b);
    }
    var rpg = d.getElementById('fullscreen');
    if (rpg) bind(rpg);
    [].slice.call(d.querySelectorAll('[data-camp-full]')).forEach(bind);
  }
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', place); else place();
  if (window.MutationObserver) new MutationObserver(paint).observe(html, { attributes: true, attributeFilter: ['lang'] });

  window.CampFull = { toggle: toggle, popOut: popOut, isOn: isOn, can: can, installed: installed, ios: ios,
                      bind: bind, howTo: howTo, enter: enter, exit: exit };
})();

/* Block Camp's weekly clock (pricing go-live, 2026-10-04).

   A subscriber's Block Camp missions open one a week, counted from their
   first Block Camp visit. The Worker can only see that visit with the
   fe_at cookie, which sb-client.js keeps for about an hour (the life of the
   access token). Block Camp pages do not load sign-in, so a subscriber who
   comes back to Mission 1 from a bookmark or an email a day later arrives
   signed in (supabase-js keeps the session in localStorage) but without the
   cookie, and the visit would not count.

   This lives here because camp-full.js is the one script every Block Camp
   page loads. Only when a stored session exists and the cookie does not
   does it load sign-in (from our own origin, like every other page), let
   sb-client.js refresh the session and write the cookie, and then ask the
   Worker for this page again with a HEAD: the gate notes the visit. A
   signed-out reader, or one whose cookie is fresh, costs nothing. */
(function () {
  'use strict';
  var has = function () { return /(?:^|;\s*)fe_at=/.test(document.cookie); };
  try {
    if (has()) return;
    var signedIn = false;
    for (var i = 0; i < localStorage.length; i++) {
      if (/^sb-[a-z0-9]+-auth-token$/.test(localStorage.key(i) || '')) { signedIn = true; break; }
    }
    if (!signedIn) return;
  } catch (e) { return; }

  function load(src) {
    return new Promise(function (ok, no) {
      var s = document.createElement('script');
      s.src = src; s.onload = ok; s.onerror = no;
      document.head.appendChild(s);
    });
  }
  var tries = 0;
  function ping() {
    if (has()) {
      fetch(location.pathname, { method: 'HEAD', credentials: 'same-origin', cache: 'no-store' })
        .catch(function () {});
    } else if (++tries < 40) {
      setTimeout(ping, 250);
    }
  }
  function start() {
    if (window.supabase && window.sbGetSession) { ping(); return; }
    (window.supabase ? Promise.resolve() : load('/vendor/supabase-js-2.116.0.min.js'))
      .then(function () { return window.sbGetSession ? null : load('/sb-client.js'); })
      .then(ping)
      .catch(function () {});
  }
  if (document.readyState === 'complete') start(); else window.addEventListener('load', start);
})();
