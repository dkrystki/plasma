#!/usr/bin/env bash

. "$SHANGREN_ROOT"/shangren.sh

telepresence --method inject-tcp --namespace mockexchs --swap-deployment bitstamp  --context shangren --run bash dump_envs_and_wait.sh
