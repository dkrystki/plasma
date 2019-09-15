#!/usr/bin/env bash

. "$ROOT"/shangren.sh

printf "🚀Deploying influxdby🚀\n"
helm upgrade --install --namespace=$DATAPROVS_NAMESPACE influxdb \
    --force --wait=true \
    --timeout=15000 \
    stable/influxdb
printf "👌Deployed influxdby👌\n\n"

