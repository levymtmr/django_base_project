#!/bin/sh

set -e
set -u
set -o pipefail

DB_ready() {
python << END
import os
import sys
import psycopg2

try:
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_NAME'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_HOST'),
        port=int(os.getenv('POSTGRES_PORT')),
    )
except psycopg2.OperationalError:
    sys.exit(-1)
else:
    conn.close()
    sys.exit(0)
END
}

until DB_ready; do
  >&2 echo 'Waiting for Postgres to become available...'
  sleep 1
done
>&2 echo 'Postgres is available'

exec python src/manage.py $@