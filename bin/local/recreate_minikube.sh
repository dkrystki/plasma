#!/usr/bin/env bash

minikube delete -p shangren
minikube start --insecure-registry=192.168.99.102:2376 --profile=shangren
helm init
minikube -p shangren dashboard &
#export DOCKER_HOST="tcp://192.168.99.102:2376"
