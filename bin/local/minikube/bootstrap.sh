#!/usr/bin/env bash

set -xeuo pipefail

cd "$(dirname "$0")" || exit

printf "Bootstraping Minikube\n"

unset KUBECONFIG
KUBERNETES_VERSION=v1.16.0

sudo minikube delete
sudo rm /home/shangren-local/.kube -rf
sudo minikube start --vm-driver=none --kubernetes-version="$KUBERNETES_VERSION"

sudo minikube addons enable dashboard
sudo minikube addons enable registry
sudo minikube addons enable ingress

sudo minikube start --vm-driver=none --embed-certs --kubernetes-version="$KUBERNETES_VERSION"

sudo chown -R $USER /home/shangren-local/.kube

sudo snap install kubectl --classic

sudo snap install helm --classic
sudo apt install socat -y
helm init --wait

kubectl apply -f k8s/dashboard_ingress.yaml

wget https://github.com/cbednarski/hostess/releases/download/v0.3.0/hostess_linux_386
sudo chmod u+x hostess_linux_386
sudo mv hostess_linux_386 /usr/local/bin/hostess

sudo hostess add shangren.registry.local 127.0.0.1

printf "Bootstraped Minikube\n\n"
