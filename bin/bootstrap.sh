#!/usr/bin/env bash

. "$SHANGREN_ROOT"/header.sh

cd ../../

printf "Bootstraping\n"

pipenv install

sudo apt install direnv

curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

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
