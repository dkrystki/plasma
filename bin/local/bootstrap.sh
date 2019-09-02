#!/usr/bin/env bash

cd `dirname $0`
cd ../../

export PIPENV_VENV_IN_PROJECT=true
pipenv install
