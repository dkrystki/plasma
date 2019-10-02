#!/usr/bin/env bash
printf "Bootstraping Minikube\n"

sudo minikube delete
bash start.sh
sudo minikube addons enable dashboard
sudo minikube addons enable ingress

sudo mv /home/shangren-local/.kube /home/shangren-local/.minikube
sudo chown -R $USER /home/shangren-local/.minikube

helm init --wait

kubectl apply -f k8s/dashboard_ingress.yaml

printf "Bootstraped Minikube\n\n"
