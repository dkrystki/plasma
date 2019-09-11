#!/usr/bin/env bash

. "$ROOT"/shangren.sh

eval $(minikube -p shangren docker-env)
skaffold dev -p local &
