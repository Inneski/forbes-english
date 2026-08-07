// Shared Supabase client for Forbes English.
// Loaded via <script> tag (no bundler in this project), exposes `window.sb`.
//
// The anon key is safe to expose in browser code by design — Supabase's
// Row Level Security (see deploy/schema.sql) is what actually protects data,
// not secrecy of this key.

const SUPABASE_URL = "https://tusioporxpjtegjlqkkb.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR1c2lvcG9yeHBqdGVnamxxa2tiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODYxMjk2NjksImV4cCI6MjEwMTcwNTY2OX0.9jPi4_Y6IfcUdzqfPzPJ8XsBCSXPuLvtCN8wWFMiLe4";

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

// --- lesson library helpers used by library.html ---

async function sbGetLessons() {
  const { data, error } = await window.sb
    .from("lessons")
    .select("file, title, level, video, deck")
    .order("id", { ascending: true });
  if (error) {
    console.error("Failed to load lessons from Supabase:", error);
    return [];
  }
  return data;
}
