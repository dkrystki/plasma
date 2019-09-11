#!/usr/bin/env bash

. "$ROOT"/shangren.sh

MINIKUBE_IP=$(minikube --profile=shangren ip)

printf "🚀Deploying graylog🚀\n"
helm repo add elastic https://helm.elastic.co
helm upgrade --install --namespace graylog elasticsearch \
 -f values/local/elasticsearch.yaml \
    --force --wait=true \
    --timeout=25000 \
    elastic/elasticsearch

helm upgrade --install --namespace graylog mongodb \
 -f values/local/mongodb.yaml \
    --force --wait=true \
    --timeout=25000 \
    stable/mongodb-replicaset

helm upgrade --install --namespace graylog graylog \
    -f values/local/graylog.yaml \
    --force --wait=true \
    --timeout=25000 \
    stable/graylog
sudo hostess add shangren.graylog.local "$MINIKUBE_IP"

helm upgrade --install --namespace graylog \
    -f values/local/fluentbit.yaml --force --wait=true \
     fluentbit stable/fluent-bit
bash seed.sh
printf "👌Deployed graylog👌\n\n"
