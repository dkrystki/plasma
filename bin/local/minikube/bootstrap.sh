#!/usr/bin/env bash

set -xeuo pipefail

printf "Bootstraping Minikube\n"

sudo microk8s.start
microk8s.enable dns
microk8s.enable dashboard
microk8s.enable helm
microk8s.enable ingress
microk8s.enable rbac
microk8s.kubectl apply -f k8s/dashboard_ingress.yaml
microk8s.helm init --wait

#kubectl delete clusterrolebindings.rbac.authorization.k8s.io -n kube-system kubernetes-dashboard
#kubectl create clusterrolebinding kubernetes-dashboard --clusterrole=cluster-admin --serviceaccount=kube-system:kubernetes-dashboard

#kubectl create serviceaccount -n kube-system tiller
#kubectl create clusterrolebinding tiller-cluster-admin --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
#kubectl --namespace kube-system patch deploy tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'

# this one is a hack. Has already been fixed but waiting for a merge
# https://github.com/helm/helm/issues/6374
microk8s.helm init --output yaml | sed 's@apiVersion: extensions/v1beta1@apiVersion: apps/v1@' | sed 's@  replicas: 1@  replicas: 1\n  selector: {"matchLabels": {"app": "helm", "name": "tiller"}}@' | microk8s.kubectl apply -f -
# install cert manager
# Install the CustomResourceDefinition resources separately
#kubectl apply -f https://raw.githubusercontent.com/jetstack/cert-manager/release-0.10/deploy/manifests/00-crds.yaml
# Create the namespace for cert-manager
#kubectl create namespace cert-manager
# Label the cert-manager namespace to disable resource validation
#kubectl label namespace cert-manager certmanager.k8s.io/disable-validation=true
# Add the Jetstack Helm repository
#helm repo add jetstack https://charts.jetstack.io
# Update your local Helm chart repository cache
#helm repo update
## Install the cert-manager Helm chart
#helm install \
#  --name cert-manager \
#  --namespace cert-manager \
#  --version v0.10.1 \
#  jetstack/cert-manager
#
#
#CLUSTER_SERVER="$(microk8s.kubectl config view -o jsonpath='{.clusters[?(@.name == "microk8s-cluster")].cluster.server}')"
#CONTEXT_USER="$(microk8s.kubectl config view -o jsonpath='{.contexts[?(@.context.cluster == "microk8s-cluster")].context.user}')"
#USERNAME="$(microk8s.kubectl config view -o jsonpath="{.users[?(@.name == '$CONTEXT_USER')].user.username}")"
#microk8s.kubectl config set-cluster "$CLUSTER_SERVER" --insecure-skip-tls-verify=true --server="$CLUSTER_SERVER"
#
#
#microk8s.kubectl config set-cluster ${KUBE_CONTEXT} --insecure-skip-tls-verify=true \
#--server=${KUBE_CONTEXT}
#
#bash start.sh
#sudo minikube addons enable dashboard
#sudo minikube addons enable ingress
#
#sudo mv /home/shangren-local/.kube /home/shangren-local/.minikube
#sudo chown -R $USER /home/shangren-local/.minikube
#
#helm init --wait
#

printf "Bootstraped Minikube\n\n"
