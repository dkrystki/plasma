#!/usr/bin/env bash

eval $(minikube -p shangren docker-env)
skaffold dev -p local
