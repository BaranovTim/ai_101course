# Setting up AI 101 Academy on a new computer

A complete guide: from a bare machine (nothing installed) to a running site,
using only the GitHub link. Written for Mac, with Windows differences noted.

## Step 0. Know this first

Two things are **not stored** on GitHub (they're in `.gitignore`), so you'll
need to recreate them on the new computer:

- **`.env`** — the file with secret keys (API keys, passwords). Template below.
- **`pgdata/`** — the PostgreSQL database itself, with all courses and users.
  On a new computer the database starts empty, and the AI 101 course is loaded
  with the `seed_course` command.

## Step 1. Install Git and Python

**Mac:** open Terminal and run:

```bash
xcode-select --install        # installs Git (and developer tools)
```

For Python, use the official site **python.org/downloads** — download
Python 3.11 or 3.12 and install it like a normal app.

**Windows:** download Git from **git-scm.com** and Python from **python.org**
(during installation, make sure to check **"Add Python to PATH"**).
Run the commands below in "Git Bash" or PowerShell.

VS Code is not needed to *run* the project — only for editing code.
If you want it, it installs in a minute from code.visualstudio.com.

## Step 2. Download the project

```bash
cd ~/Desktop
git clone https://github.com/BaranovTim/ai_101course.git
cd ai_101course
```

## Step 3. Create a virtual environment and install libraries

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

This installs Django, Stripe, Pillow, openai, anthropic, and `pgserver` —
a package that contains a real PostgreSQL inside it (so you don't need to
install Postgres separately). Takes a few minutes.

## Step 4. Create the `.env` file

In the project root, create a file named `.env` (e.g. with `nano .env`) and paste:

```
SECRET_KEY=django-insecure-ai101-local-dev-key
DEBUG=True

DB_NAME=ai101db
DB_USER=ai101
DB_PASSWORD=ai101pass
DB_HOST=127.0.0.1
DB_PORT=5432

STRIPE_PUBLISHABLE_KEY=
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=
COURSE_PRICE_CENTS=10000

ANTHROPIC_API_KEY=
OPENAI_API_KEY=
```

All keys can stay empty — the site will work with the payment simulator and
the offline tutor. Add your OpenAI key to `OPENAI_API_KEY` whenever you want
the live bot. **Never paste real keys into code files or commit them to git —
they live in `.env` only.**

## Step 5. Create and start the database (one time)

Run from the project folder, with `.venv` activated:

```bash
# path to the PostgreSQL binaries inside pgserver (works with any Python version)
PGBIN=$(.venv/bin/python -c "import pgserver, os; print(os.path.join(os.path.dirname(pgserver.__file__), 'pginstall', 'bin'))")

# 1) create the database cluster (superuser password comes from a temp file)
echo "postgres" > /tmp/pgpw.txt
"$PGBIN/initdb" -D ./pgdata -U postgres --auth=scram-sha-256 --pwfile=/tmp/pgpw.txt -E UTF8

# 2) start the database server
"$PGBIN/pg_ctl" -D ./pgdata -o "-p 5432 -c listen_addresses=127.0.0.1" -l ./pgdata/server.log start

# 3) create the site's database user and database
PGPASSWORD=postgres "$PGBIN/psql" -h 127.0.0.1 -U postgres \
  -c "CREATE ROLE ai101 LOGIN PASSWORD 'ai101pass' CREATEDB;" \
  -c "CREATE DATABASE ai101db OWNER ai101;"
```

## Step 6. Create tables, load the course, create an admin

```bash
python manage.py migrate         # creates all the tables
python manage.py seed_course     # loads the General track + AI 101 course (21 lessons)
python manage.py createsuperuser # choose your admin username/password
```

## Step 7. Run it

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000** — the site is live. Admin panel at `/admin/`,
course Studio at `/studio/` (with the admin account).

## Everyday startup (after a reboot)

```bash
cd ~/Desktop/ai_101course
./scripts/start.sh
```

> ⚠️ In `scripts/start.sh` the PostgreSQL path is hardcoded with `python3.9`
> (the version on the original Mac). If the new computer has Python 3.11/3.12,
> open the script and replace `python3.9` with your version
> (check with `ls .venv/lib/`).

## Troubleshooting

| Symptom | Cause & fix |
|---|---|
| `command not found: python` | Use `python3`, or the venv isn't activated — run `source .venv/bin/activate` |
| `No module named django` | The venv isn't activated, or `pip install -r requirements.txt` wasn't run |
| `connection refused ... port 5432` | The database isn't running — repeat step 5's `pg_ctl ... start` command (or use `./scripts/start.sh`) |
| `That port is already in use` | Another server is on port 8000 — `pkill -f runserver`, or run `python manage.py runserver 8001` |
| `NotOpenSSLWarning` lines | Harmless noise from an old system library — ignore |

## Optional but useful

**DBeaver** (dbeaver.io) to browse the database visually — PostgreSQL
connection, host `127.0.0.1`, port `5432`, database `ai101db`, user `ai101`,
password `ai101pass`.
