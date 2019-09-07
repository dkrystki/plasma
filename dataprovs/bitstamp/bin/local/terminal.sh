#!/usr/bin/env bash

SENTRY_POD=$(kubectl -n dataprovs get pods -l role=bitstamp -o name | grep -m 1 -o "bitstamp.*$")

kubectl exec -n "$DATAPROVS_NAMESPACE" -it "$SENTRY_POD" /bin/bash
