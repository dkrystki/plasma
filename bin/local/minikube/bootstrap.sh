#!/usr/bin/env bash

set -xeuo pipefail

cd "$(dirname "$0")" || exit

source "$SHANGREN_ROOT/.settings"

printf "Bootstraping Minikube\n"

source stage local

sudo snap remove microk8s
sudo snap install microk8s --classic --channel=1.15/stable

sudo microk8s.start
sleep 10

mkdir -p "$(dirname "$KUBECONFIG")"
microk8s.config > "$KUBECONFIG"

microk8s.enable dns
microk8s.enable rbac
sudo microk8s.enable storage
microk8s.enable ingress
microk8s.kubectl apply -f k8s/ingress-rbac.yaml

sudo sh -c 'echo "--allow-privileged=true" >> /var/snap/microk8s/current/args/kube-apiserver'
sudo systemctl restart snap.microk8s.daemon-apiserver.service

if [ ! -f /usr/local/bin/helm ]; then
  HELM_NAME="helm-$HELM_VERSION-linux-386"
  wget "https://get.helm.sh/$HELM_NAME.tar.gz"
  tar -zxvf "$HELM_NAME.tar.gz"
  sudo mv linux-386/helm /usr/local/bin/helm
  rm "$HELM_NAME.tar.gz"
  rm -r linux-386
fi
sleep 15
helm init
microk8s.kubectl create serviceaccount -n kube-system tiller
microk8s.kubectl create clusterrolebinding tiller-cluster-admin --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
microk8s.kubectl --namespace kube-system patch deploy tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'

tee -a "/var/snap/microk8s/current/args/containerd-template.toml" << END
  [plugins.cri.registry.mirrors."shangren.registry.local"]
          endpoint = ["http://shangren.registry.local"]
END

wget https://github.com/cbednarski/hostess/releases/download/v0.3.0/hostess_linux_386
sudo chmod u+x hostess_linux_386
sudo mv hostess_linux_386 /usr/local/bin/hostess

sudo hostess add shangren.registry.local 127.0.0.1

printf "Bootstraped Minikube\n\n"
