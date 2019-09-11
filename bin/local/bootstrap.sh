#!/usr/bin/env bash

. "$ROOT"/shangren.sh

cd ../../

printf "Bootstraping\n"

export PIPENV_VENV_IN_PROJECT=true
pipenv install
printf "👌Done👌\n\n"
