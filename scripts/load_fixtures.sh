ROOT_DIR=$(dirname "$0")/../

python3 "${ROOT_DIR}/manage.py" loaddata "${ROOT_DIR}"/bop/*/fixtures/*
