#!/usr/bin/env bash
set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python3 manage.py migrate
if [ $LOAD_INITIAL_DATA == true ]; then
    python3 manage.py loaddata initial_data.json
fi
python3 manage.py collectstatic --noinput --verbosity 0
echo "Run gunicorn..."
gunicorn --bind :8000 --workers 3 rest_api.wsgi:application

