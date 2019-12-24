#!/usr/bin/env bash

CURRENT_DIR=$(pwd)

source "$PLASMA_COMM_ROOT"/bash/utils.sh

export PROMPT_COMMAND_BEFORE

case $1 in
  start)
    if ! test -f "$PROJECT_DIR/.telepresence.sh"; then
      function cleanup {
        rm "$APP_ROOT/.telepresence.env" > /dev/null
        rm "$APP_ROOT/.telepresence.sh" > /dev/null
        unset TELE_ON
      }

      trap cleanup EXIT

      telepresence --method inject-tcp --namespace "$NAMESPACE" --swap-deployment "$APP_NAME" \
                   --run bash "$PLASMA_COMM_ROOT/bash/tele/command.sh"
    else
      printf "Already started\n"
      exit 1
    fi
    ;;
  shell)
    cleanup() {
      export PROMPT_COMMAND=$PROMPT_COMMAND_BEFORE
    }
    check_tele() {
      if ! test -f "$APP_ROOT/.telepresence.sh"; then
        print_style "Telepresence is down.\n" "error"
        direnv reload
        cleanup
      fi
    }
    if test -f "$APP_ROOT/.telepresence.sh"; then
      export APP_VIRTUAL_ENV
      APP_VIRTUAL_ENV=$(dirname "$(which python)")

      source "$APP_ROOT/.telepresence.sh"
      export CUSTOM_PS1="$STAGE_EMOJI📻($APP_NAME)"

      export PATH="$APP_VIRTUAL_ENV:$PATH"

      if [[ $PROMPT_COMMAND != *"check_tele"* ]]; then
        export PROMPT_COMMAND_BEFORE=$PROMPT_COMMAND
        export PROMPT_COMMAND="check_tele;$PROMPT_COMMAND"
      fi
    else
      print_style "run \"tele start\" first.\n" "error"
    fi
    ;;
  *)
    print_style "Provide arguments. (start, shell)\n" "info"
    ;;
esac

cd "$CURRENT_DIR"
