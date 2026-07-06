#!/bin/zsh
# Start PostgreSQL (bundled) and the Django dev server.
set -e
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PGBIN="$PROJECT_DIR/.venv/lib/python3.9/site-packages/pgserver/pginstall/bin"

cd "$PROJECT_DIR"

if ! "$PGBIN/pg_isready" -h 127.0.0.1 -p 5432 -q; then
  echo "Starting PostgreSQL on 127.0.0.1:5432 …"
  "$PGBIN/pg_ctl" -D ./pgdata -o "-p 5432 -c listen_addresses=127.0.0.1" -l ./pgdata/server.log start
else
  echo "PostgreSQL already running."
fi

echo "Starting Django at http://127.0.0.1:8000 …"
exec .venv/bin/python manage.py runserver 127.0.0.1:8000
