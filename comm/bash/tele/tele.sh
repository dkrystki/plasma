#!/usr/bin/env bash

CURRENT_DIR=$(pwd)

source "$SHANGREN_ROOT"/comm/bash/utils.sh

export PROMPT_COMMAND_BEFORE

case $1 in
  start)
    if ! test -f "$PROJECT_DIR/.telepresence.sh"; then
      "$SHANGREN_ROOT"/comm/bash/tele/start.sh "$NAMESPACE" "$PROJECT_NAME" "$PROJECT_DIR"
    else
      printf "Already started\n"
      exit 1
    fi
    ;;
  shell)
    if [ "$0" = "$BASH_SOURCE" ]; then
        print_style "Error: Script must be sourced\n" "error"
        exit 1
    fi

    cleanup() {
      export PROMPT_COMMAND=$PROMPT_COMMAND_BEFORE
    }
    check_tele() {
      if ! test -f "$PROJECT_DIR/.telepresence.sh"; then
        print_style "Telepresence is down.\n" "error"
        direnv reload
        cleanup
      fi
    }
    if test -f "$PROJECT_DIR/.telepresence.sh"; then
      source "$PROJECT_DIR"/.telepresence.sh
      export CUSTOM_PS1="$STAGE_EMOJI📻($PROJECT_NAME)"

      export VIRTUAL_ENV
      VIRTUAL_ENV=$( dirname "$(dirname "$(cd "$PROJECT_DIR/flesh" && poetry run which python)")")
      export PATH="$VIRTUAL_ENV/bin:$PATH"

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
