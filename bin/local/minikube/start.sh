#!/usr/bin/env bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

minikube start

SHANGREN_DASHBOARD_IP=$(kubectl -n kube-system get service kubernetes-dashboard -o yaml | grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}")
hostess add shangren.dashboard.local "$SHANGREN_DASHBOARD_IP"
