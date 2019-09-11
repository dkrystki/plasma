#!/usr/bin/env bash

. "$ROOT"/shangren.sh

printf "🌱Seeding sentry🌱\n"

SENTRY_POD=$(kubectl -n sentry get pods -l role=web -o name | grep -m 1 -o "sentry-web.*$")

kubectl -n sentry cp dump.json "$SENTRY_POD":home/sentry/dump.json
kubectl -n sentry exec "$SENTRY_POD" -- bash -c "sentry django loaddata /home/sentry/dump.json"
printf "👌Seeding sentry done👌\n\n"
