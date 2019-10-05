#!/usr/bin/env bash

set -xeuo pipefail

cd "$(dirname "$0")" || exit

printf "Bootstraping Minikube\n"

unset KUBECONFIG

sudo minikube delete
sudo rm /home/shangren-local/.kube -rf
sudo minikube start --vm-driver=none --kubernetes-version=v1.15.0

sudo minikube addons enable dashboard
sudo minikube addons enable ingress

sudo minikube start --vm-driver=none --embed-certs --kubernetes-version=v1.15.0

sudo chown -R $USER /home/shangren-local/.kube

sudo snap install kubectl --classic

sudo snap install helm --classic
sudo apt install socat -y
helm init --wait

kubectl apply -f k8s/dashboard_ingress.yaml

printf "Bootstraped Minikube\n\n"
