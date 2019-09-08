#!/usr/bin/env bash

cd `dirname $0`

SENTRY_POD=$(kubectl -n sentry get pods -l role=web -o name | grep -m 1 -o "sentry-web.*$")
kubectl -n sentry exec "$SENTRY_POD" -- bash -c "sentry export --silent --indent=2 --exclude migrationhistory,permission,savedsearch,contenttype > /home/sentry/dump.json"
kubectl -n sentry cp "$SENTRY_POD":home/sentry/dump.json dump.json