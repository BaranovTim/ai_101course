#!/bin/zsh
# Stop the bundled PostgreSQL server.
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PGBIN="$PROJECT_DIR/.venv/lib/python3.9/site-packages/pgserver/pginstall/bin"
"$PGBIN/pg_ctl" -D "$PROJECT_DIR/pgdata" stop
