-- Bunny Reading persistent storage
-- Run once in Supabase SQL Editor.
-- Recommended: keep RLS enabled and use a server-side service-role/secret key
-- only inside Streamlit Secrets (never commit it to GitHub).

create table if not exists public.bunny_books (
    owner text not null,
    book_id text not null,
    book_data jsonb not null,
    created_at timestamptz not null default now(),
    primary key (owner, book_id)
);

create table if not exists public.bunny_progress (
    owner text not null,
    book_id text not null,
    chapter_index integer not null default 0 check (chapter_index >= 0),
    updated_at timestamptz not null default now(),
    primary key (owner, book_id)
);

create table if not exists public.bunny_bookmarks (
    owner text not null,
    book_id text not null,
    chapter_id text not null,
    bookmark_data jsonb not null,
    created_at timestamptz not null default now(),
    primary key (owner, book_id, chapter_id)
);

alter table public.bunny_books enable row level security;
alter table public.bunny_progress enable row level security;
alter table public.bunny_bookmarks enable row level security;

-- No anonymous policies are created intentionally.
-- A server-side service-role/secret key in Streamlit Secrets can access these tables.
