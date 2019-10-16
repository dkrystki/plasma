#!/usr/bin/env bash

. "$SHANGREN_ROOT"/header.sh

export TELE_ON
TELE_ON="True"

ENVS_DIR=$3

function cleanup {
  rm "$ENVS_DIR"/telepresence.env
  rm "$ENVS_DIR"/telepresence.sh
  unset TELE_ON
}

trap cleanup EXIT

telepresence --method inject-tcp --namespace "$1" --swap-deployment "$2" \
             --run bash telepresence_command.sh "$3"
