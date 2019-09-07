#!/usr/bin/env bash

cd "$(dirname $0)" || exit

telepresence --method inject-tcp --namespace dataprovs --swap-deployment bitstamp  --context shangren --run bash dump_envs_and_wait.sh
