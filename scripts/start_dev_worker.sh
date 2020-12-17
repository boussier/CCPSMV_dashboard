#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

pip3 install watchdog argh
watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- \
          celery worker --loglevel info --app bop:celeryapp
