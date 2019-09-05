#!/usr/bin/env bash

echo "Deploying static services (not debuggable)"

cd `dirname $0`
# cd into root dir
cd ../

bash dataprovs/bin/deploy.sh

printf "\n🚀Deploying graylog🚀\n"
helm upgrade --install --namespace graylog graylog \
    --set graylog.replicas=1 \
    --set graylog.password.rootPassword=password \
    --set graylog.service.port=80 \
    --set elasticsearch.replicas=1 \
    --set elasticsearch.minimumMasterNodes=1 \
    --set mongodb-replicaset.replicas=1 \
    --force --wait=true \
    --timeout=15000 \
    stable/graylog

export SHANGREN_GRAYLOG_IP
SHANGREN_GRAYLOG_IP=$(kubectl -n graylog get service graylog-web -o yaml | grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}")
hostess add shangren.graylog.local "$SHANGREN_GRAYLOG_IP"
printf "👌Deployed graylog👌\n"

printf "\n🚀Deploying sentry🚀\n"
helm upgrade --install --namespace sentry sentry \
    -f helm_values/local/sentry.yaml \
    --force --wait=true \
    --timeout=15000 \
    stable/sentry
export SHANGREN_SENTRY_IP
SHANGREN_SENTRY_IP=$(kubectl -n sentry get service sentry -o yaml | grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}")
hostess add shangren.sentry.local "$SHANGREN_SENTRY_IP"
bash dataprovs/bitstamp/bin/sentry/seed.sh
printf "👌Deployed sentry👌\n"
