# AI 101 Academy 🧠

An interactive AI education platform for the Cayman Islands community.
Django + PostgreSQL backend, Tailwind-styled frontend with React components
(quiz player and AI tutor chat), Stripe payments, and PDF certificates.

## Quick start

```bash
./scripts/start.sh
```

Then open **http://127.0.0.1:8000**.

The script starts the bundled PostgreSQL server (if not already running) and the
Django dev server. Stop the database later with `./scripts/stop_db.sh`.

### First-time setup (already done on this machine)

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python manage.py migrate
.venv/bin/python manage.py seed_course        # loads all 5 modules / 21 lessons / 61 quiz questions
.venv/bin/python manage.py createsuperuser
```

## What's included

| Feature | Where |
|---|---|
| Landing, pricing, industry hub, curriculum pages | public site |
| Signup / login with occupation profile | `/accounts/…` |
| $100 one-time purchase via **Stripe Checkout** | `/payments/…` |
| Local **payment simulator** when Stripe keys are absent | automatic in dev |
| 5 modules · 21 lessons · 61 quiz questions (seeded) | `manage.py seed_course` |
| Interactive **React quiz player** with explanations | lesson pages |
| **AI Tutor chat** (Anthropic API `claude-opus-4-8`, offline fallback without a key) | `/tutor/` |
| Progress tracking + dashboard | `/dashboard/` |
| **PDF certificate** with verification ID on completion | `/certificates/` |
| Django admin for editing content, users, payments | `/admin/` (user `admin` / `admin12345` — change this!) |

## Database (PostgreSQL + DBeaver)

PostgreSQL runs locally from the pip-installed `pgserver` package — real Postgres
binaries, data stored in `./pgdata`, listening on TCP so DBeaver connects normally.

**DBeaver connection settings** (Database → New Connection → PostgreSQL):

| Setting | Value |
|---|---|
| Host | `127.0.0.1` |
| Port | `5432` |
| Database | `ai101db` |
| Username | `ai101` |
| Password | `ai101pass` |

(A `postgres` superuser also exists with password `postgres`.)

Interesting tables: `courses_course`, `courses_module`, `courses_lesson`,
`courses_quiz`, `courses_question`, `courses_choice`, `courses_enrollment`,
`courses_lessonprogress`, `courses_quizattempt`, `courses_certificate`,
`payments_payment`, `tutor_tutormessage`, `accounts_profile`, `auth_user`.

## Configuration (`.env`)

```
STRIPE_PUBLISHABLE_KEY=   # from https://dashboard.stripe.com/test/apikeys
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=    # optional locally; payment is verified on the success page too
ANTHROPIC_API_KEY=        # enables the live AI tutor (otherwise a helpful offline tutor runs)
COURSE_PRICE_CENTS=10000  # $100
```

- **Without Stripe keys** the checkout shows a clearly-labeled *simulated* payment
  page so you can test the whole flow locally.
- **With Stripe test keys** the enroll button redirects to real Stripe Checkout
  (test card `4242 4242 4242 4242`). For webhooks run:
  `stripe listen --forward-to 127.0.0.1:8000/payments/webhook/` and put the
  printed `whsec_…` into `.env`.

## Editing course content

- Quick edits: Django admin → Courses / Modules / Lessons / Quizzes.
- Bulk edits: change `courses/course_content_part1.py` / `_part2.py`
  and re-run `.venv/bin/python manage.py seed_course` (idempotent).

## Project layout

```
ai101_academy/   Django settings & root urls
accounts/        signup, profile, settings
courses/         course/module/lesson/quiz models, views, seed command, PDF certificates
payments/        Stripe checkout, webhook, dev simulator
tutor/           AI tutor chat (Anthropic API + offline fallback)
templates/       Tailwind pages (Lumina Learning design system from /Planning)
static/js/       React components: quiz.js, tutor.js (+ helpers.js)
pgdata/          PostgreSQL data directory (gitignored)
```

## Tech stack

Python 3.9 · Django 4.2 LTS · PostgreSQL 16 (pgserver) · Tailwind CSS (CDN) ·
React 18 (CDN, no build step) · Stripe · ReportLab · Anthropic API
