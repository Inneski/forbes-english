// Forbes English — account.html in a real browser against a fake Supabase:
// what each kind of reader sees (term buyer back from checkout, subscriber,
// IELTS only, owner, nothing bought + the EUR 49 marking button).
//
//   node deploy/test-account.cjs          (from the repo root; needs playwright)
//
const { chromium } = require('playwright');
const fs = require('fs');
const ROOT = process.cwd() + '/';
const OUT = process.argv[2] || require('os').tmpdir();
const page0 = fs.readFileSync(ROOT + 'account.html', 'utf8');
const sbClient = fs.readFileSync(ROOT + 'sb-client.js', 'utf8');
const DAY = 86400000;

const TERM1 = [];
const names = ['Present Simple 1a', 'Present Simple 1b', 'Present Continuous 1a', 'Present Continuous 1b', 'Past Simple 1a',
  'Past Simple 1b', 'Past Continuous 1a', 'Past Continuous 1b', 'Going To 1a', 'Going To 1b', 'Future Simple 1a', 'Future Simple 1b'];
names.forEach((n, i) => {
  TERM1.push({ file: `blockcamp-m${i + 1}.html`, title: `Block Camp \u2014 ${n}`, term: 1, mission: i + 1, access: i ? 'pro' : 'free' });
  if (![3, 7, 11].includes(i)) TERM1.push({ file: `block-camp/quest-${i + 1}.html`, title: `Quest ${i + 1}`, term: 1, mission: i + 1, access: i ? 'pro' : 'free' });
});

// The fake client: profiles / user_plans / lessons, per scenario. `plansAfter`
// lets a purchase appear only on a later read (the webhook landing late).
function fake(sc) {
  return `
  (function(){
    const SC = ${JSON.stringify(sc)};
    let planReads = 0;
    function q(table){
      const data = () => table === 'profiles' ? [SC.profile]
        : table === 'user_plans' ? (++planReads > (SC.plansAfter || 0) ? SC.plans : (SC.plansBefore || []))
        : SC.lessons;
      const o = { select(){return o;}, eq(){return o;}, order(){return o;},
        single(){ return Promise.resolve({ data: data()[0], error: null }); },
        then(res, rej){ return Promise.resolve({ data: data(), error: null }).then(res, rej); } };
      return o;
    }
    const client = { from: q, auth: {
      onAuthStateChange(){ return { data: { subscription: { unsubscribe(){} } } }; },
      getSession: async () => ({ data: { session: { access_token: 'tok-' + SC.name, expires_at: Date.now()/1000 + 3600 } } }),
      getUser: async () => ({ data: { user: { id: 'u', email: SC.email } } }),
    } };
    window.supabase = { createClient: () => client };
  })();`;
}

async function scenario(b, sc, path = '/account.html') {
  const page = await b.newPage({ viewport: { width: 420, height: 900 } });
  const posts = [];
  await page.route('https://x.test/**', (route) => {
    const req = route.request();
    const u = new URL(req.url());
    if (u.pathname === '/account.html') return route.fulfill({ contentType: 'text/html', body: page0 });
    if (u.pathname.startsWith('/vendor/supabase-js')) return route.fulfill({ contentType: 'text/javascript', body: fake(sc) });
    if (u.pathname === '/sb-client.js') return route.fulfill({ contentType: 'text/javascript', body: sbClient });
    if (u.pathname === '/api/create-checkout-session') {
      posts.push({ body: req.postData(), auth: req.headers()['authorization'] });
      return route.fulfill({ status: 500, contentType: 'application/json', body: '{"error":"x"}' });
    }
    return route.fulfill({ status: 404, body: '' });
  });
  await page.goto('https://x.test' + path);
  await page.waitForTimeout(sc.wait || 1200);
  const view = await page.evaluate(() => {
    const vis = (id) => { const e = document.getElementById(id); return e && !e.hidden && !e.closest('[hidden]'); };
    const txt = (id) => (document.getElementById(id) || {}).textContent;
    return {
      badge: txt('sub-badge'), period: txt('sub-period'), cancel: vis('cancel-note'), subscribe: vis('subscribe-btn'),
      bc: vis('bc-card'), bcTitle: txt('bc-title'), term: vis('bc-term-row') ? txt('bc-term') : null, week: txt('bc-week'),
      openLinks: [...document.querySelectorAll('.mission.open a')].length,
      locked: [...document.querySelectorAll('.mission.locked')].length,
      firstLockedWhen: (document.querySelector('.mission.locked .mission-when') || {}).textContent || null,
      specials: vis('bc-specials'), ielts: vis('ielts-card'), credits: txt('marking-credits'), how: vis('marking-how'),
      notice: vis('checkout-notice') ? txt('checkout-notice') : null,
    };
  });
  if (sc.click) {
    await page.click('#marking-buy');
    await page.waitForTimeout(600);
    view.marked = await page.evaluate(() => ({ err: document.getElementById('marking-error').textContent,
      label: document.getElementById('marking-buy').textContent, disabled: document.getElementById('marking-buy').disabled }));
  }
  if (sc.shot) await page.screenshot({ path: `${OUT}/account-${sc.name}.png`, fullPage: true });
  await page.close();
  return { view, posts };
}

const ago = (d) => new Date(Date.now() - d * DAY).toISOString();
(async () => {
  const b = await chromium.launch();
  const results = [];
  const run = async (sc, path, test) => {
    const r = await scenario(b, sc, path);
    const ok = test(r.view, r.posts);
    results.push(ok);
    console.log(`${ok ? 'PASS' : 'FAIL'} ${sc.name}: ${JSON.stringify(r.view)}${r.posts.length ? ' posts=' + JSON.stringify(r.posts) : ''}`);
  };

  const term = { product: 'blockcamp', status: 'active', term: 1, starts_at: ago(8), ends_at: null, marking_credits: 0, stripe_checkout_session_id: 'cs_bc' };
  const im = { product: 'ielts', status: 'active', term: null, starts_at: ago(1), ends_at: null, marking_credits: 2, stripe_checkout_session_id: 'cs_new' };
  await run({ name: 'term-buyer-back-from-checkout', email: 'parent@example.com', profile: { subscription_status: 'inactive', owner: false },
      plansBefore: [term], plans: [term, im], plansAfter: 1, lessons: TERM1, wait: 4200, shot: true },
    '/account.html?checkout=success&cs=cs_new',
    (v) => v.badge === 'Not subscribed' && v.bc && v.bcTitle === 'Block Camp Term 1' && v.term === 'Term 1' &&
      v.week === 'Week 2 of 12' && v.openLinks === 4 && v.locked === 10 && /^Opens /.test(v.firstLockedWhen) &&
      v.specials && v.ielts && v.credits === '2' && v.how && v.notice === 'Thank you \u2014 your purchase is ready.');
  await run({ name: 'subscriber', email: 's@example.com', profile: { subscription_status: 'active', owner: false,
      current_period_end: new Date(Date.now() + 9 * DAY).toISOString(), blockcamp_first_open: ago(20) }, plans: [], lessons: TERM1 },
    '/account.html',
    (v) => v.badge === 'Active' && v.cancel && !v.subscribe && v.bc && v.bcTitle === 'Block Camp' && v.term === null &&
      v.week === 'Week 3 of 12' && !v.specials && !v.ielts && v.credits === '0' && !v.how && v.notice === null);
  await run({ name: 'ielts-only', email: 'i@example.com', profile: { subscription_status: 'inactive', owner: false },
      plans: [{ product: 'ielts', status: 'active', term: null, starts_at: ago(3), ends_at: null, marking_credits: 0 }], lessons: TERM1 },
    '/account.html',
    (v) => !v.bc && v.ielts && v.subscribe && v.credits === '0');
  await run({ name: 'owner', email: 'o@example.com', profile: { subscription_status: 'inactive', owner: true }, plans: [], lessons: TERM1, shot: true },
    '/account.html',
    (v) => v.badge === 'Owner \u2014 full access' && v.bc && v.week === 'Every mission open' && v.openLinks === 21 && v.locked === 0);
  await run({ name: 'nothing-yet', email: 'n@example.com', profile: { subscription_status: 'inactive', owner: false }, plans: [], lessons: TERM1, click: true },
    '/account.html',
    (v, posts) => v.badge === 'Not subscribed' && v.subscribe && !v.bc && !v.ielts && v.credits === '0' &&
      posts.length === 1 && posts[0].auth === 'Bearer tok-nothing-yet' && posts[0].body === '{"product":"marking"}' &&
      /went wrong/.test(v.marked.err) && !v.marked.disabled && /\u20ac49/.test(v.marked.label));
  await b.close();
  process.exit(results.every(Boolean) ? 0 : 1);
})();
