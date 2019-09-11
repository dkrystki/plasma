#!/usr/bin/env bash

. "$ROOT"/shangren.sh

MINIKUBE_IP=$(minikube --profile=shangren ip)

printf "🚀Deploying sentry🚀\n"
helm upgrade --install --namespace sentry sentry \
    -f values/local/sentry.yaml \
    --force --wait=true \
    --timeout=25000 \
    stable/sentry

sudo hostess add shangren.sentry.local "$MINIKUBE_IP"
bash seed.sh
printf "👌Deployed sentry👌\n\n"
