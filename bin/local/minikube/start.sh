#!/usr/bin/env bash

. "$ROOT"/shangren.sh

minikube start

SHANGREN_DASHBOARD_IP=$(kubectl -n kube-system get service kubernetes-dashboard -o yaml | grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}")
