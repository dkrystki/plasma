#!/usr/bin/env bash

. "$SHANGREN_ROOT"/header.sh

telepresence --method inject-tcp --namespace "$1" --swap-deployment "$2" \
             --run bash dump_envs_and_wait.sh "$3"
