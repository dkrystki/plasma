#!/usr/bin/env bash

cd "$(dirname $0)" || exit
cd ../../

printf "Bootstraping\n"

export PIPENV_VENV_IN_PROJECT=true
pipenv install
printf "👌Done👌\n\n"
