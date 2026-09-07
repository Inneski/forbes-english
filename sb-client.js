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

// emailRedirectTo must be an allowed URL in the Supabase dashboard
// (Authentication -> URL Configuration -> Redirect URLs), same as the reset
// link below. Without it the confirmation link falls back to the project's
// Site URL and drops a newly confirmed user on the library, with nothing
// telling them a plan is the next step.
async function sbSignUp(email, password) {
  return window.sb.auth.signUp({
    email,
    password,
    options: { emailRedirectTo: `${location.origin}/account.html` },
  });
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
  const { data, error } = await window.sb
    .from("lessons")
    .select("file, title, level, video, deck, access, sort_order, created_at")
    .order("sort_order", { ascending: true, nullsFirst: false })
    .order("id", { ascending: true });
  if (error) {
    console.error("Failed to load lessons from Supabase:", error);
    return [];
  }
  return data;
}
