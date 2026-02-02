#!/bin/sh
# Wait for Postgres to be available
set -e

host="${DB_HOST:-db}"
port="${DB_PORT:-5432}"

# Use nc if available, otherwise use bash tcp check fallback
until (nc -z "$host" "$port" 2>/dev/null) || (echo > /dev/tcp/$host/$port 2>/dev/null); do
  echo "Waiting for postgres at $host:$port..."
  sleep 1
done

# Run migrations / create DB tables
python -c "from app.models.base import init_db; init_db()"

# Start gunicorn
exec gunicorn --bind 0.0.0.0:5000 --workers 4 "app.main:create_app()"
