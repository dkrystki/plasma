#!/usr/bin/env bash

cd "$(dirname "$0")" || exit

# Args:
# 1 = namespace
# 2 = deployment name
# 3 = project directory

ENVS_DIR=$3

function cleanup {
  rm "$ENVS_DIR"/.telepresence.env
  rm "$ENVS_DIR"/.telepresence.sh
  unset TELE_ON
}

trap cleanup EXIT

telepresence --method inject-tcp --namespace "$1" --swap-deployment "$2" \
             --run bash command.sh "$3"
