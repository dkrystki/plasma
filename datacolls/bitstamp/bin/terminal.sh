#!/usr/bin/env bash

set -euo pipefail

. "$SHANGREN_ROOT"/shangren.sh

POD=$(kubectl -n datacolls get pods -l role=bitstamp -o name | grep -m 1 -o "bitstamp.*$")
kubectl exec -n datacolls -it "$POD" /bin/bash
