#!/usr/bin/env bash

printf "🌱Seeding graylog🌱"

cd "$(dirname $0)" || exit
cd ../../../

SENTRY_POD=$(kubectl -n sentry get pods -l role=web -o name | grep -m 1 -o "sentry-web.*$")

kubectl -n sentry cp $1 "$SENTRY_POD":home/sentry/dump.json
kubectl -n sentry exec "$SENTRY_POD" -- bash -c "sentry django loaddata /home/sentry/dump.json"
printf "👌Done👌\n\n"
