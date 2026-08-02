// Shared Supabase client for Forbes English.
// Loaded via <script> tag (no bundler in this project), exposes `window.sb`.
//
// Fill in the two values below once you have them (deploy/04-supabase-setup.md).
// The anon key is safe to expose in browser code by design — Supabase's
// Row Level Security (see deploy/schema.sql) is what actually protects data,
// not secrecy of this key.

const SUPABASE_URL = "https://YOUR-PROJECT.supabase.co";
const SUPABASE_ANON_KEY = "YOUR-ANON-KEY";

window.sb = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

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
