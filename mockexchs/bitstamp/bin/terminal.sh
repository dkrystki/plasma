#!/usr/bin/env bash

set -euo pipefail

. "$SHANGREN_ROOT"/shangren.sh

POD=$(kubectl -n mockexchs get pods -l role=bitstamp -o name | grep -m 1 -o "bitstamp.*$")
kubectl exec -n mockexchs -it "$POD" /bin/bash
