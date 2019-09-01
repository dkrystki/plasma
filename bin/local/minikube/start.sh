#!/usr/bin/env bash

minikube start --profile=shangren --cpus 4 --memory 8192
minikube -p shangren dashboard &
