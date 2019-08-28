#!/usr/bin/env bash

minikube start --insecure-registry
minikube profile=shangren
minikube -p shangren dashboard &
