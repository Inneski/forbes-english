-- Forbes English — Supabase schema
-- Run this once in the Supabase SQL Editor (Step 4).

-- One row per user, mirroring auth.users, tracking subscription state.
create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text,
  stripe_customer_id text,
  stripe_subscription_id text,
  subscription_status text not null default 'inactive', -- 'active' | 'trialing' | 'past_due' | 'canceled' | 'inactive'
  plan text, -- 'monthly' | 'semiannual' | 'annual'
  current_period_end timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- Keep updated_at current on every change.
create or replace function public.set_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

drop trigger if exists profiles_set_updated_at on public.profiles;
create trigger profiles_set_updated_at
  before update on public.profiles
  for each row execute function public.set_updated_at();

-- Auto-create a profile row the moment someone signs up.
create or replace function public.handle_new_user()
returns trigger as $$
begin
  insert into public.profiles (id, email)
  values (new.id, new.email);
  return new;
end;
$$ language plpgsql security definer;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- Row Level Security: users can only ever see/edit their own row.
-- Writes from the Stripe webhook go through the service_role key, which
-- bypasses RLS entirely, so this stays locked down for browser clients.
alter table public.profiles enable row level security;

create policy "Users can view their own profile"
  on public.profiles for select
  using (auth.uid() = id);

create policy "Users can update their own profile"
  on public.profiles for update
  using (auth.uid() = id);


-- ─────────────────────────────────────────────────────────────────────
-- Lesson catalogue and the access tier the paywall reads.
--
-- The `lessons` table was created outside this file originally; this block
-- records the part that matters for access control so the repo is the record.
-- ─────────────────────────────────────────────────────────────────────

alter table public.lessons
  add column if not exists access text not null default 'pro'
  check (access in ('free', 'pro'));

comment on column public.lessons.access is
  'free = served to anyone; pro = the Worker requires an active subscription.';

-- The catalogue itself is public — library.html is a shop window and has to
-- list everything. Only the CONTENT of pro lessons is gated, and that gate
-- lives in the Cloudflare Worker (src/index.js), because lessons are static
-- .html files that never pass through Postgres. No RLS policy can protect
-- them; do not add one here and assume it did.
alter table public.lessons enable row level security;

drop policy if exists "Lesson catalogue is public" on public.lessons;
create policy "Lesson catalogue is public"
  on public.lessons for select
  using (true);

-- The free set: the whole Sherpa Tensing tense reference, two complete
-- lessons at each of A1-C1 and one at C2.
-- update public.lessons set access = 'free' where file in (...);
