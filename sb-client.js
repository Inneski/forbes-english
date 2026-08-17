// Shared Supabase client for Forbes English.
// Loaded via <script> tag (no bundler in this project), exposes `window.sb`.
//
// The anon key is safe to expose in browser code by design — Supabase's
// Row Level Security (see deploy/schema.sql) is what actually protects data,
// not secrecy of this key.

const SUPABASE_URL = "https://tusioporxpjtegjlqkkb.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR1c2lvcG9yeHBqdGVnamxxa2tiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODYxMjk2NjksImV4cCI6MjEwMTcwNTY2OX0.9jPi4_Y6IfcUdzqfPzPJ8XsBCSXPuLvtCN8wWFMiLe4";

window.sb = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

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
window.sb.auth.onAuthStateChange((_event, session) => writeSessionCookie(session));
window.sb.auth.getSession().then(({ data }) => writeSessionCookie(data.session));

// --- small helpers used by account.html ---

async function sbSignUp(email, password) {
  return window.sb.auth.signUp({ email, password });
}

async function sbSignIn(email, password) {
  return window.sb.auth.signInWithPassword({ email, password });
}

async function sbSignOut() {
  return window.sb.auth.signOut();
}

// Sends the reset email. redirectTo must be an allowed URL in the Supabase
// dashboard (Authentication -> URL Configuration -> Redirect URLs).
async function sbSendPasswordReset(email) {
  return window.sb.auth.resetPasswordForEmail(email, {
    redirectTo: `${location.origin}/account.html`,
  });
}

// Called after the user returns from that email with a recovery session.
async function sbUpdatePassword(password) {
  return window.sb.auth.updateUser({ password });
}

async function sbGetUser() {
  const { data } = await window.sb.auth.getUser();
  return data.user;
}

async function sbGetProfile(userId) {
  const { data } = await window.sb
    .from("profiles")
    .select("*")
    .eq("id", userId)
    .single();
  return data;
}

// --- lesson library helpers used by library.html ---

// Grid order is sort_order first, then id. sort_order is NULL on almost every
// row: those are unpinned and keep their historical id order, which is what
// the library has always shown. Give a row a low sort_order to pin it to the
// front without renumbering ids -- the ids are referenced by lesson-meta.json,
// the sitemap and the gate pages, so renumbering them is not a safe reorder.
// nullsFirst: false is what keeps the unpinned rows behind the pinned ones;
// Postgres sorts NULLs first by default on ascending, which would invert this.
async function sbGetLessons() {
  const { data, error } = await window.sb
    .from("lessons")
    .select("file, title, level, video, deck, access, sort_order")
    .order("sort_order", { ascending: true, nullsFirst: false })
    .order("id", { ascending: true });
  if (error) {
    console.error("Failed to load lessons from Supabase:", error);
    return [];
  }
  return data;
}
