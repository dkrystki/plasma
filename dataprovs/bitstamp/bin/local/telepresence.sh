#!/usr/bin/env bash

DIR=`dirname $0`
telepresence --method inject-tcp --namespace dataprovs --swap-deployment bitstamp  --context shangren --run $DIR/dump_envs_and_wait.sh
