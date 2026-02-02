#!/bin/sh
# Wait for Postgres to be available
set -e

host="${DB_HOST:-db}"
port="${DB_PORT:-5432}"

# Use Python to check TCP connectivity (portable across images)
echo "Waiting for postgres at $host:$port..."
python - <<'PY'
import socket, time, os
host = os.environ.get('DB_HOST', 'db')
port = int(os.environ.get('DB_PORT', '5432'))
while True:
    try:
        s = socket.create_connection((host, port), timeout=1)
        s.close()
        break
    except Exception:
        print(f"Waiting for postgres at {host}:{port}...")
        time.sleep(1)
PY

# Run migrations / create DB tables
python -c "from app.models.base import init_db; init_db()"

# Start gunicorn
exec gunicorn --bind 0.0.0.0:5000 --workers 4 "app.main:create_app()"
