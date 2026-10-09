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
// The specials (no term) come back from the same read; a Term 2 row is in
// the fake's answer too, to prove the page lists it nowhere (the fake ignores
// the query's filters).
const SPECIALS = [
  { file: 'block-camp/grand-hotel-rpg.html', title: 'The Last Night at the Grand Hotel', term: null, mission: null, access: 'pro' },
  { file: 'blockcamp-passive-trial.html', title: 'Block Camp II — Passive 16: The Trial', term: null, mission: null, access: 'pro' },
];
const TERM2 = { file: 'blockcamp-present-perfect.html', title: 'Block Camp — Present Perfect 1a', term: 2, mission: null, access: 'pro' };
TERM1.push(...SPECIALS, TERM2);

// The fake client: profiles / user_plans / lessons, per scenario. `plansAfter`
// lets a purchase appear only on a later read (the webhook landing late).
function fake(sc) {
  return `
  (function(){
    const SC = ${JSON.stringify(sc)};
    let planReads = 0, profileReads = 0;
    function q(table){
      const data = () => table === 'profiles' ? [++profileReads > (SC.profileAfter || 1e9) ? SC.profileLater : SC.profile]
        : table === 'user_plans' ? (++planReads > (SC.plansAfter || 0) ? SC.plans : (SC.plansBefore || []))
        : SC.lessons;
      const o = { select(){return o;}, eq(){return o;}, or(){return o;}, is(){return o;}, order(){return o;},
        single(){ return Promise.resolve({ data: data()[0], error: null }); },
        then(res, rej){
          if (SC.plansError && table === 'user_plans') return Promise.resolve({ data: null, error: { message: 'boom' } }).then(res, rej);
          return Promise.resolve({ data: data(), error: null }).then(res, rej); } };
      return o;
    }
    // Signed out until verifyOtp trades a claim's token for a session.
    let signedIn = !SC.signedOut;
    const client = { from: q, auth: {
      onAuthStateChange(){ return { data: { subscription: { unsubscribe(){} } } }; },
      getSession: async () => ({ data: { session: !signedIn ? null : { access_token: 'tok-' + SC.name, expires_at: Date.now()/1000 + 3600 } } }),
      getUser: async () => ({ data: { user: !signedIn ? null : { id: 'u', email: SC.email, user_metadata: SC.meta || {} } } }),
      verifyOtp: async (a) => { window.__verify = a; signedIn = true; return { data: { session: {} }, error: null }; },
      updateUser: async (a) => { window.__update = a; return { data: {}, error: null }; },
      signUp: async (args) => { window.__signup = args;
        return { data: { user: { id: 'n', identities: [{}] }, session: null }, error: null }; },
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
    if (u.pathname === '/api/claim-checkout') {
      posts.push({ claim: req.postData() });
      return route.fulfill({ status: sc.claimStatus || 200, contentType: 'application/json', body: JSON.stringify(sc.claim || {}) });
    }
    return route.fulfill({ status: 404, body: '' });
  });
  await page.goto('https://x.test' + path);
  await page.waitForTimeout(sc.wait || 1200);
  if (sc.signup) {
    await page.click('#switch-link');
    await page.fill('#email', 'new@example.com');
    await page.fill('#password', 'secret123');
    await page.click('#auth-submit');
    await page.waitForTimeout(400);
  }
  const view = await page.evaluate(() => {
    if (location.pathname !== '/account.html') return { path: location.pathname };
    const vis = (id) => { const e = document.getElementById(id); return e && !e.hidden && !e.closest('[hidden]'); };
    const txt = (id) => (document.getElementById(id) || {}).textContent;
    return {
      badge: txt('sub-badge'), period: txt('sub-period'), cancel: vis('cancel-note'), subscribe: vis('subscribe-btn'),
      bc: vis('bc-card'), bcTitle: txt('bc-title'), term: vis('bc-term-row') ? txt('bc-term') : null, week: txt('bc-week'),
      openLinks: [...document.querySelectorAll('.mission.open a')].length,
      locked: [...document.querySelectorAll('.mission.locked')].length,
      firstLockedWhen: (document.querySelector('.mission.locked .mission-when') || {}).textContent || null,
      specials: vis('bc-specials'), ielts: vis('ielts-card'), credits: txt('marking-credits'), how: vis('marking-how'),
      specialsLinks: [...document.querySelectorAll('#bc-specials a')].map((a) => a.getAttribute('href') + ' ' + a.textContent),
      listed: [...document.querySelectorAll('#bc-card a')].map((a) => a.getAttribute('href')),
      authMsg: vis('auth-section') ? txt('auth-error') : null,
      authGood: document.getElementById('auth-error').classList.contains('good'),
      authEmail: document.getElementById('email').value,
      account: vis('account-section'),
      passwordCard: vis('password-card'),
      verify: window.__verify || null,
      signupRedirect: window.__signup ? window.__signup.options.emailRedirectTo : null,
      notice: vis('checkout-notice') ? txt('checkout-notice') : null,
      plansError: vis('plans-error'),
      fullFirst: (() => { const f = document.getElementById('full-card'), b = document.getElementById('bc-card');
        return Boolean(f.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING); })(),
    };
  });
  if (sc.setPassword) {
    await page.fill('#set-password', 'secret123');
    await page.click('#password-form button');
    await page.waitForTimeout(500);
    view.afterPassword = await page.evaluate(() => ({ update: window.__update,
      card: !document.getElementById('password-card').hidden, note: document.getElementById('checkout-notice').textContent }));
  }
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
      v.specials && v.ielts && v.credits === '2' && v.how && v.notice === 'Thank you \u2014 your purchase is ready.' &&
      // The specials by name, linked straight to the lessons; Term 2 nowhere.
      v.specialsLinks.length === 2 && v.specialsLinks[0] === 'block-camp/grand-hotel-rpg.html Adventure: The Last Night at the Grand Hotel' &&
      v.specialsLinks[1] === 'blockcamp-passive-trial.html Deck: Passive 16: The Trial' &&
      !v.listed.includes('blockcamp-present-perfect.html'));
  await run({ name: 'subscriber', email: 's@example.com', profile: { subscription_status: 'active', owner: false,
      current_period_end: new Date(Date.now() + 9 * DAY).toISOString(), blockcamp_first_open: ago(20) }, plans: [], lessons: TERM1 },
    '/account.html',
    (v) => v.badge === 'Active' && v.cancel && !v.subscribe && v.bc && v.bcTitle === 'Block Camp' && v.term === null &&
      v.week === 'Week 3 of 12' && v.specials && v.specialsLinks.length === 2 && !v.ielts && v.credits === '0' && !v.how && v.notice === null);
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
  // Owns Term 1, buys the full plan: no ?cs=, so it waits for the
  // subscription itself, then puts the full plan's card back on top.
  const t1 = { product: 'blockcamp', status: 'active', term: 1, starts_at: ago(8), ends_at: null, marking_credits: 0, stripe_checkout_session_id: 'cs_bc' };
  await run({ name: 'one-off-owner-buys-full-plan', email: 'f@example.com', profile: { subscription_status: 'inactive', owner: false },
      profileAfter: 1, profileLater: { subscription_status: 'active', owner: false, blockcamp_first_open: null,
        current_period_end: new Date(Date.now() + 30 * DAY).toISOString() },
      plans: [t1], lessons: TERM1, wait: 4200 },
    '/account.html?checkout=success',
    (v) => v.badge === 'Active' && v.notice === 'Thank you \u2014 your purchase is ready.' && v.fullFirst);
  // The purchases read fails: say so, rather than showing nothing owned.
  await run({ name: 'plans-read-fails', email: 'e@example.com', profile: { subscription_status: 'inactive', owner: false },
      plans: [t1], plansError: true, lessons: TERM1 },
    '/account.html',
    (v) => v.plansError && v.credits === '\u2014' && !v.bc);
  // A device clock a little behind: never 'Week 0', Mission 1 open.
  await run({ name: 'clock-behind', email: 'c@example.com', profile: { subscription_status: 'inactive', owner: false },
      plans: [{ ...t1, starts_at: new Date(Date.now() + 3600000).toISOString() }], lessons: TERM1 },
    '/account.html',
    (v) => v.week === 'Week 1 of 12' && v.openLinks === 2);
  // On the way to checkout and signed in (a confirmation link, or a pricing
  // page that timed out): straight back to the plans.
  await run({ name: 'signed-in-back-to-pricing', email: 'p@example.com', profile: { subscription_status: 'inactive', owner: false },
      plans: [], lessons: TERM1 },
    '/account.html?redirect=pricing',
    (v) => v.path === '/pricing.html');
  // A new buyer signing up from pricing: the confirmation link comes back
  // through the account page to the plans, and the page says so.
  await run({ name: 'sign-up-from-pricing', email: 'x', signedOut: true, signup: true, profile: null, plans: [], lessons: TERM1 },
    '/account.html?redirect=pricing',
    (v) => v.signupRedirect === 'https://x.test/account.html?redirect=pricing' && /back to the plans/.test(v.authMsg));
  await run({ name: 'sign-up-plain', email: 'x', signedOut: true, signup: true, profile: null, plans: [], lessons: TERM1 },
    '/account.html',
    (v) => v.signupRedirect === 'https://x.test/account.html' && /then log in/.test(v.authMsg));
  // Paid without an account (guest checkout): the success page claims the
  // purchase, trades the one-time token for a session, and shows the
  // account with the purchase and a "set a password" card.
  const guestRow = { ...t1, starts_at: ago(0.01), stripe_checkout_session_id: 'cs_live_g1' };
  await run({ name: 'guest-new-account', email: 'new.parent@example.com', signedOut: true, meta: { via: 'checkout', needs_password: true },
      claim: { state: 'new_account', token_hash: 'th-1', email: 'new.parent@example.com' },
      profile: { subscription_status: 'inactive', owner: false }, plans: [guestRow], lessons: TERM1, setPassword: true, shot: true },
    '/account.html?checkout=success&cs=cs_live_g1&claim=cs_live_g1',
    (v, posts) => v.account && v.verify && v.verify.token_hash === 'th-1' && v.verify.type === 'email' &&
      v.bcTitle === 'Block Camp Term 1' && v.notice === 'Thank you — your purchase is ready.' && v.passwordCard &&
      posts.some((p) => p.claim === '{"cs":"cs_live_g1"}') &&
      v.afterPassword.update.password === 'secret123' && v.afterPassword.update.data.needs_password === false &&
      !v.afterPassword.card && /Password saved/.test(v.afterPassword.note));
  await run({ name: 'guest-existing-account', email: 'x', signedOut: true,
      claim: { state: 'existing_account', email: 'old.parent@example.com' }, profile: null, plans: [], lessons: TERM1 },
    '/account.html?checkout=success&cs=cs_live_g2&claim=cs_live_g2',
    (v) => !v.account && v.authEmail === 'old.parent@example.com' && /on the account for old\.parent@example\.com/.test(v.authMsg) &&
      v.authGood && !v.verify);
  await run({ name: 'guest-processing', email: 'x', signedOut: true, claim: { state: 'processing' }, profile: null, plans: [], lessons: TERM1 },
    '/account.html?checkout=success&cs=cs_live_g3&claim=cs_live_g3',
    (v) => !v.account && /still confirming/.test(v.authMsg) && v.authGood);
  await run({ name: 'guest-not-paid', email: 'x', signedOut: true, claim: { state: 'not_paid' }, profile: null, plans: [], lessons: TERM1 },
    '/account.html?checkout=success&claim=cs_live_g4',
    (v) => /not completed/.test(v.authMsg) && !v.authGood);
  // An answer that cannot change: shown at once, not retried.
  await run({ name: 'guest-final-error', email: 'x', signedOut: true, claimStatus: 409,
      claim: { error: 'This payment is not for anything sold on this site. Write to info@forbesenglish.com.' }, profile: null, plans: [], lessons: TERM1 },
    '/account.html?checkout=success&claim=cs_live_g5',
    (v, posts) => /not for anything sold on this site/.test(v.authMsg) && !v.authGood && posts.filter((p) => p.claim).length === 1);
  // Signed in already: a claim parameter is ignored, nothing is posted.
  await run({ name: 'signed-in-ignores-claim', email: 'p@example.com', profile: { subscription_status: 'inactive', owner: false },
      plans: [t1], lessons: TERM1 },
    '/account.html?checkout=success&cs=cs_bc&claim=cs_bc',
    (v, posts) => v.account && !posts.some((p) => p.claim) && !v.passwordCard);
  await b.close();
  process.exit(results.every(Boolean) ? 0 : 1);
})();
