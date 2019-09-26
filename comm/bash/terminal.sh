#!/usr/bin/env bash

. "$SHANGREN_ROOT"/shangren.sh

export POD=$(kubectl -n $1 get pods -l role=$2 -o name | grep -m 1 -o "$2.*$")
[ -z "$POD" ] && echo "Pod \"$2\" can't be find in namespace \"$1\"." && exit

kubectl exec -n $1 -it "$POD" /bin/bash
