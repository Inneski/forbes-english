// Forbes English — pricing.html in a real browser against a fake Supabase and
// a fake Worker: what a Buy press does, signed out and signed in.
//
//   node deploy/test-pricing.cjs        (from the repo root; needs playwright)
//
// A signed-out buyer goes straight to checkout (guest checkout, 2026-10-09):
// no account page, no stored intent, no token sent. A signed-in buyer sends
// their token. The Worker's "already have it" (409) is shown as it says it.
const { chromium } = require('playwright');
const fs = require('fs');
const ROOT = process.cwd() + '/';
const page0 = fs.readFileSync(ROOT + 'pricing.html', 'utf8');
const sbClient = fs.readFileSync(ROOT + 'sb-client.js', 'utf8');

const fake = (signedIn) => `(function(){
  let inside = ${signedIn};
  const client = { from(){ const o={select(){return o;},eq(){return o;},then(r){return Promise.resolve({data:[],error:null}).then(r);}}; return o; },
    auth: { onAuthStateChange(){ return { data: { subscription: { unsubscribe(){} } } }; },
      getSession: async () => ({ data: { session: inside ? { access_token: 'tok-1', expires_at: Date.now()/1000 + 3600 } : null } }),
      getUser: async () => ({ data: { user: inside ? { id: 'u', email: 'p@example.com' } : null } }),
      signOut: async (o) => { window.__signOut = o; inside = false; return { error: null }; } } };
  window.supabase = { createClient: () => client };
})();`;

async function scenario(b, { signedIn, answer, click }) {
  const page = await b.newPage({ viewport: { width: 390, height: 844 } });
  const posts = [];
  await page.route('https://x.test/**', (route) => {
    const req = route.request();
    const u = new URL(req.url());
    if (u.pathname === '/pricing.html') return route.fulfill({ contentType: 'text/html', body: page0 });
    if (u.pathname.startsWith('/vendor/supabase-js')) return route.fulfill({ contentType: 'text/javascript', body: fake(signedIn) });
    if (u.pathname === '/sb-client.js') return route.fulfill({ contentType: 'text/javascript', body: sbClient });
    if (u.pathname === '/api/founder-status') return route.fulfill({ contentType: 'application/json', body: '{"limit":50,"remaining":40}' });
    if (u.pathname === '/api/create-checkout-session') {
      posts.push({ body: req.postData(), auth: req.headers()['authorization'] || null });
      const a = typeof answer === 'function' ? answer(posts.length) : answer;
      return route.fulfill({ status: a.status, contentType: 'application/json', body: JSON.stringify(a.body) });
    }
    if (u.pathname === '/stripe-checkout') return route.fulfill({ contentType: 'text/html', body: '<p>STRIPE</p>' });
    return route.fulfill({ status: 404, body: '' });
  });
  await page.goto('https://x.test/pricing.html');
  await page.waitForTimeout(900);
  await page.click(click);
  await page.waitForTimeout(1200);
  const v = await page.evaluate(() => ({
    path: location.pathname,
    banner: (document.getElementById('status-banner') || {}).textContent || '',
    intent: (() => { try { return localStorage.getItem('fe_intended_plan'); } catch (e) { return 'x'; } })(),
  }));
  await page.close();
  return { v, posts };
}

(async () => {
  const b = await chromium.launch();
  let ok = true;
  const check = (pass, what, extra) => { ok = ok && pass; console.log(`${pass ? 'PASS' : 'FAIL'} ${what}${pass ? '' : ' ' + JSON.stringify(extra)}`); };

  const toStripe = { status: 200, body: { url: 'https://x.test/stripe-checkout' } };
  let r = await scenario(b, { signedIn: false, answer: toStripe, click: '.plan-btn[data-product="blockcamp"]' });
  check(r.v.path === '/stripe-checkout' && r.posts.length === 1 && r.posts[0].auth === null &&
    r.posts[0].body === '{"product":"blockcamp"}' && !r.v.intent,
    'signed out, Buy Term 1: straight to checkout, no account page, no token, no stored intent', r);

  r = await scenario(b, { signedIn: false, answer: toStripe, click: '.plan-btn[data-plan="monthly"]' });
  check(r.v.path === '/stripe-checkout' && r.posts[0].body === '{"plan":"monthly"}' && r.posts[0].auth === null,
    'signed out, Forbes English Pro: straight to checkout too', r);

  r = await scenario(b, { signedIn: true, answer: toStripe, click: '.plan-btn[data-product="ielts"]' });
  check(r.v.path === '/stripe-checkout' && r.posts[0].auth === 'Bearer tok-1', 'signed in: the token goes with it', r);

  r = await scenario(b, { signedIn: true, click: '.plan-btn[data-product="blockcamp"]',
    answer: { status: 409, body: { error: 'You already have Block Camp Term 1. It is on your account page.', owned: true } } });
  check(r.v.path === '/pricing.html' && /already have Block Camp Term 1/.test(r.v.banner), 'already bought: the Worker\'s sentence, no checkout', r);

  r = await scenario(b, { signedIn: false, click: '.plan-btn[data-product="blockcamp"]', answer: { status: 502, body: { error: 'Stripe error' } } });
  check(r.v.path === '/pricing.html' && /went wrong/.test(r.v.banner), 'checkout fails: the page says so and stays', r);

  // A sign-in this browser holds but Supabase no longer accepts: signed out
  // here (locally), and the same purchase goes ahead as a guest.
  r = await scenario(b, { signedIn: true, click: '.plan-btn[data-product="blockcamp"]',
    answer: (n) => n === 1 ? { status: 401, body: { error: 'Your sign-in has expired.', stale: true } } : toStripe });
  check(r.v.path === '/stripe-checkout' && r.posts.length === 2 && r.posts[0].auth === 'Bearer tok-1' && r.posts[1].auth === null,
    'an expired sign-in: signed out locally, then straight to checkout as a guest', r);

  check(/No account needed to buy/.test(page0) && /Do I need an account\?<\/summary>\s*<p>No\./.test(page0),
    'the page says no account is needed to buy');
  await b.close();
  process.exit(ok ? 0 : 1);
})();
