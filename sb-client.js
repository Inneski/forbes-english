// Shared Supabase client for Forbes English.
// Loaded via <script> tag (no bundler in this project), exposes `window.sb`.
//
// The anon key is safe to expose in browser code by design — Supabase's
// Row Level Security (see deploy/schema.sql) is what actually protects data,
// not secrecy of this key.

const SUPABASE_URL = "https://tusioporxpjtegjlqkkb.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR1c2lvcG9yeHBqdGVnamxxa2tiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODYxMjk2NjksImV4cCI6MjEwMTcwNTY2OX0.9jPi4_Y6IfcUdzqfPzPJ8XsBCSXPuLvtCN8wWFMiLe4";

// --- creating the client, defensively ---
//
// Until 2026-09-10 this file opened with a bare
// `window.sb = supabase.createClient(...)`. Anything that stopped the library
// from loading threw a ReferenceError on that line, which aborted the rest of
// this file *and* the inline script on the page that follows it — including
// the call that draws the page. account.html was left showing "Loading…" with
// no form, no error and no way forward.
//
// Measured on a 390px iPhone viewport, three ordinary phone conditions each
// produced exactly that dead page: a blocked cdn.jsdelivr.net, a Supabase host
// that did not answer, and localStorage throwing. The library now comes from
// our own origin (see vendor/README.md), which removes the common cause; the
// guards below make the remainder visible instead of silent.

// A localStorage-shaped object that keeps the session in memory only. Used
// when the real one is unavailable: iOS Safari with "Block All Cookies", and
// some in-app browsers, throw a SecurityError on any localStorage access.
// Signing in still works, the session just is not remembered after the tab
// closes — far better than a page that cannot be used at all.
function memoryStorage() {
  const store = new Map();
  return {
    getItem: (k) => (store.has(k) ? store.get(k) : null),
    setItem: (k, v) => { store.set(k, String(v)); },
    removeItem: (k) => { store.delete(k); },
  };
}

function createSupabaseClient() {
  if (typeof supabase === "undefined" || !supabase || typeof supabase.createClient !== "function") {
    console.error("supabase-js did not load — sign-in is unavailable on this page.");
    return null;
  }
  try {
    return supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
  } catch (err) {
    console.warn("Supabase client failed with browser storage, retrying in memory:", err);
    try {
      return supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
        auth: { storage: memoryStorage(), persistSession: true },
      });
    } catch (err2) {
      console.error("Supabase client could not be created:", err2);
      return null;
    }
  }
}

window.sb = createSupabaseClient();

// Lets a page tell "signed out" apart from "sign-in cannot run here" — two
// states that otherwise look identical and need very different words.
window.sbUnavailable = !window.sb;

// What every helper returns when there is no client. Shaped like a Supabase
// reply so callers can keep handling one thing: `{ data, error }`.
const SB_NO_CLIENT = Object.freeze({
  data: null,
  error: {
    message:
      "Sign-in could not load in this browser. Reload the page; if it keeps " +
      "happening, turn off any ad or content blocker for this site, or open " +
      "it in Safari or Chrome rather than inside another app.",
  },
});

// Every call below goes over the network, and on a phone the network
// sometimes simply never answers. Without a deadline the caller waits for
// ever — which is how the account page came to sit on "Loading…" indefinitely.
// A timeout resolves with `fallback` rather than rejecting, so the caller has
// one path to handle, not two.
function sbWithTimeout(promise, ms, fallback) {
  let timer;
  return Promise.race([
    Promise.resolve(promise).catch((err) => {
      console.error("Supabase request failed:", err);
      return fallback;
    }),
    new Promise((resolve) => {
      timer = setTimeout(() => {
        console.warn(`Supabase request gave up after ${ms}ms.`);
        resolve(fallback);
      }, ms);
    }),
  ]).finally(() => clearTimeout(timer));
}

// --- session cookie, so the Worker can see who is asking ---
//
// supabase-js keeps the session in localStorage, which the server never sees.
// The paywall runs in the Cloudflare Worker (src/index.js) and has to decide
// before it serves a lesson file, so the access token is mirrored into a
// cookie that rides along with every request to the site.
//
// The token is not a secret being newly exposed here: it already lives in
// localStorage on this origin, it is short-lived, and it grants exactly what
// the row-level policies allow. The cookie is SameSite=Lax so it is not sent
// with cross-site requests, and Secure everywhere except local development.

const FE_COOKIE = "fe_at";

function writeSessionCookie(session) {
  const secure = location.protocol === "https:" ? "; Secure" : "";
  if (!session || !session.access_token) {
    document.cookie = `${FE_COOKIE}=; Path=/; Max-Age=0; SameSite=Lax${secure}`;
    return;
  }
  // Expire the cookie with the token, so a stale one is never presented.
  const maxAge = Math.max(
    60,
    (session.expires_at ? session.expires_at * 1000 - Date.now() : 3600e3) / 1000 | 0
  );
  document.cookie =
    `${FE_COOKIE}=${encodeURIComponent(session.access_token)}` +
    `; Path=/; Max-Age=${maxAge}; SameSite=Lax${secure}`;
}

// Fires on load with the restored session, and again on sign-in, sign-out and
// every silent token refresh — so the cookie tracks the real session state.
// Guarded, and the initial read is caught: an unhandled rejection here used to
// be one more way for a page to stop halfway through drawing itself.
if (window.sb) {
  try {
    window.sb.auth.onAuthStateChange((_event, session) => writeSessionCookie(session));
    window.sb.auth.getSession()
      .then(({ data }) => writeSessionCookie(data.session))
      .catch((err) => console.error("Could not read the stored session:", err));
  } catch (err) {
    console.error("Could not wire up the session cookie:", err);
  }
}

// --- small helpers used by account.html ---

// emailRedirectTo must be an allowed URL in the Supabase dashboard
// (Authentication -> URL Configuration -> Redirect URLs), same as the reset
// link below. Without it the confirmation link falls back to the project's
// Site URL and drops a newly confirmed user on the library, with nothing
// telling them a plan is the next step.
async function sbSignUp(email, password) {
  if (!window.sb) return SB_NO_CLIENT;
  return window.sb.auth.signUp({
    email,
    password,
    options: { emailRedirectTo: `${location.origin}/account.html` },
  });
}

async function sbSignIn(email, password) {
  if (!window.sb) return SB_NO_CLIENT;
  return window.sb.auth.signInWithPassword({ email, password });
}

async function sbSignOut() {
  if (!window.sb) return SB_NO_CLIENT;
  return window.sb.auth.signOut();
}

// Sends the reset email. redirectTo must be an allowed URL in the Supabase
// dashboard (Authentication -> URL Configuration -> Redirect URLs).
async function sbSendPasswordReset(email) {
  if (!window.sb) return SB_NO_CLIENT;
  return window.sb.auth.resetPasswordForEmail(email, {
    redirectTo: `${location.origin}/account.html`,
  });
}

// Called after the user returns from that email with a recovery session.
async function sbUpdatePassword(password) {
  if (!window.sb) return SB_NO_CLIENT;
  return window.sb.auth.updateUser({ password });
}

// Resolves to null rather than hanging or throwing. A visitor we cannot
// confirm is treated as signed out, which shows them the login form — the one
// state they can always act on.
async function sbGetUser() {
  if (!window.sb) return null;
  const res = await sbWithTimeout(window.sb.auth.getUser(), 8000, { data: { user: null } });
  return res && res.data ? res.data.user : null;
}

// Reads the session that is already stored in this browser. Local and
// instant in the ordinary case, so the first paint of a page never has to
// wait on the network to decide whether to show a login form or an account
// panel. (supabase-js may still go out to refresh an expired token, hence
// the short deadline.)
async function sbGetSession() {
  if (!window.sb) return null;
  const res = await sbWithTimeout(window.sb.auth.getSession(), 2500, { data: { session: null } });
  return res && res.data ? res.data.session : null;
}

async function sbGetProfile(userId) {
  if (!window.sb) return null;
  const res = await sbWithTimeout(
    window.sb.from("profiles").select("*").eq("id", userId).single(),
    8000,
    { data: null }
  );
  return res ? res.data : null;
}

// --- lesson library helpers used by library.html ---

// Fetch order is sort_order first, then id -- the same order tools/seo.py
// uses for the crawlable list, so the two never disagree. The shelf itself
// re-sorts in library.html's render(): a sort_order of zero or below pins a
// row to the front, and everything else runs newest first by created_at,
// which is why created_at is selected here. Positive sort_order values are
// left in the data but no longer move a card on the shelf. Renumbering ids
// is still not a safe reorder -- lesson-meta.json, the sitemap and the gate
// pages reference them.
// nullsFirst: false keeps the unpinned rows behind the pinned ones;
// Postgres sorts NULLs first by default on ascending, which would invert this.
async function sbGetLessons() {
  if (!window.sb) {
    console.error("Cannot load the lesson catalogue: no Supabase client.");
    return [];
  }
  const { data, error } = await sbWithTimeout(
    window.sb
      .from("lessons")
      .select("file, title, level, video, deck, access, sort_order, created_at")
      .order("sort_order", { ascending: true, nullsFirst: false })
      .order("id", { ascending: true }),
    8000,
    { data: null, error: { message: "timed out" } }
  );
  if (error) {
    console.error("Failed to load lessons from Supabase:", error);
    return [];
  }
  return data || [];
}
