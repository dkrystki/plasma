#!/usr/bin/env bash

cd `dirname $0`
# cd into root dir
cd ../../../

minikube delete --profile=shangren
minikube start --profile=shangren --cpus 5 --memory 12288 --vm-driver=none
source envs/local/activate.sh

helm init --wait
#suod minikube --profile=shangren dashboard &

SHANGREN_DASHBOARD_IP=$(kubectl -n kube-system get service kubernetes-dashboard -o yaml | grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}")
hostess add shangren.dashboard.local "$SHANGREN_DASHBOARD_IP"

bash bin/deploy.sh

bash bin/local/skaffold.sh
