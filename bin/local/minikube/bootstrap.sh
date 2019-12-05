#!/usr/bin/env bash

set -xeuo pipefail

cd "$(dirname "$0")" || exit

source "$SHANGREN_ROOT/.settings"

printf "Bootstraping Minikube\n"

unset KUBECONFIG

microk8s.reset

sudo microk8s.start
microk8s.enable dns
microk8s.enable rbac
microk8s.enable dashboard
microk8s.enable helm
sudo microk8s.enable storage
microk8s.enable ingress

wget https://github.com/cbednarski/hostess/releases/download/v0.3.0/hostess_linux_386
sudo chmod u+x hostess_linux_386
sudo mv hostess_linux_386 /usr/local/bin/hostess

sudo hostess add shangren.registry.local 127.0.0.1

printf "Bootstraped Minikube\n\n"
