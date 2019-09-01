#!/usr/bin/env bash

cd `dirname $0`
cd ../../../

minikube delete --profile=shangren
minikube start --profile=shangren --memory 8192

source envs/local/activate.sh

helm init
minikube --profile=shangren dashboard &
