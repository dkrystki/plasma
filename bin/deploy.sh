#!/usr/bin/env bash

echo "Deploying static services (not debuggable)"

cd "$(dirname $0)" || exit
# cd into root dir
cd ../

MINIKUBE_IP=$(minikube --profile=shangren ip)

bash dataprovs/bin/deploy.sh

printf "\n🚀Deploying graylog🚀\n"
helm repo add elastic https://helm.elastic.co
helm upgrade --install --namespace graylog elasticsearch \
 -f bin/local/values/elasticsearch.yaml \
    --force --wait=true \
    --timeout=25000 \
    elastic/elasticsearch

helm upgrade --install --namespace graylog mongodb \
 -f bin/local/values/mongodb.yaml \
    --force --wait=true \
    --timeout=25000 \
    stable/mongodb-replicaset

helm upgrade --install --namespace graylog graylog \
    -f bin/local/values/graylog.yaml \
    --force --wait=true \
    --timeout=25000 \
    stable/graylog
sudo hostess add shangren.graylog.local "$MINIKUBE_IP"

helm upgrade --install --namespace graylog -f bin/local/values/fluentbit.yaml --force --wait=true \
     fluentbit stable/fluent-bit
bash bin/local/graylog/seed.sh
printf "👌Deployed graylog👌\n"


printf "\n🚀Deploying sentry🚀\n"
helm upgrade --install --namespace sentry sentry \
    -f bin/local/values/sentry.yaml \
    --force --wait=true \
    --timeout=25000 \
    stable/sentry

sudo hostess add shangren.sentry.local "$MINIKUBE_IP"
bash dataprovs/bitstamp/bin/sentry/seed.sh
printf "👌Deployed sentry👌\"
