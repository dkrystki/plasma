#!/usr/bin/env bash

. "$ROOT"/shangren.sh

POD=$(kubectl -n dataprovs get pods -l role=bitstamp -o name | grep -m 1 -o "bitstamp.*$")

kubectl exec -n dataprovs -it "$POD" /bin/bash
