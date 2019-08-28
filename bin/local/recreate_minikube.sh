#!/usr/bin/env bash

minikube delete -p shangren
minikube start -p shangren
helm init
minikube -p shangren dashboard &
