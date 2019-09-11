#!/usr/bin/env bash

. "$ROOT"/shangren.sh

telepresence --method inject-tcp --namespace dataprovs --swap-deployment bitstamp  --context shangren --run bash dump_envs_and_wait.sh
