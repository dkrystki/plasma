#!/usr/bin/env bash

. "$SHANGREN_ROOT"/header.sh

cd $SHANGREN_ROOT

printf "Bootstraping\n"

poetry install

sudo apt install direnv

DIRENV_SETUP="
render_ps1() {
  echo \$CUSTOM_PS1
}
export -f render_ps1
export DIRENV_LOG_FORMAT=
PS1='\$(render_ps1)'\$PS1
"

grep -qxF 'render_ps1() {' ~/.bashrc || echo "$DIRENV_SETUP" >> ~/.bashrc

printf "👌Done👌\n\n"
