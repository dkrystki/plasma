#!/usr/bin/env bash

CURRENT_DIR=$(pwd)

PROJECT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
PROJECT_ROOT=$(dirname "$PROJECT_ROOT")

cd "$PROJECT_ROOT" || exit
#source ../../envs/activate.sh
source bin/telepresence.dec
# command above activates shangren core virtualenv so we have to exit it
#deactivate

cd flesh || exit

VENV_DIR=$(dirname "$(pipenv run which python)")
source "$VENV_DIR"/activate

cd "$CURRENT_DIR" || exit
