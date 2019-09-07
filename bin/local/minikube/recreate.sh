#!/usr/bin/env bash

cd `dirname $0`
# cd into root dir
cd ../../../

minikube --profile=shangren delete
minikube --profile=shangren start --cpus 5 --memory 15000 --vm-driver=kvm2
source envs/local/activate.sh
minikube --profile=shangren addons enable dashboard
minikube --profile=shangren addons enable ingress

helm init --wait

MINIKUBE_IP=$(minikube --profile=shangren ip)
sudo hostess add shangren.dashboard.local "$MINIKUBE_IP"
kubectl apply -f bin/local/k8s/dashboard_ingress.yaml

bash bin/deploy.sh

bash bin/local/skaffold.sh
