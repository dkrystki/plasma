#!/usr/bin/env bash

. "$ROOT"/shangren.sh

printf "Bootstraping Minikube\n"

minikube --profile=shangren delete
minikube --profile=shangren start --cpus=5 --memory=15000 --disk-size="40000mb"
minikube --profile=shangren addons enable dashboard
minikube --profile=shangren addons enable ingress

helm init --wait

MINIKUBE_IP=$(minikube --profile=shangren ip)

beep 1500 0.1
sudo hostess add shangren.dashboard.local "$MINIKUBE_IP"
sudo hostess add shangren.graylog.local "$MINIKUBE_IP"
sudo hostess add shangren.sentry.local "$MINIKUBE_IP"
kubectl apply -f k8s/dashboard_ingress.yaml

printf "Bootstraped Minikube\n\n"
