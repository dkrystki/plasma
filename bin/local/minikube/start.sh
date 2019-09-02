#!/usr/bin/env bash

minikube start --profile=shangren
minikube -p shangren dashboard &
