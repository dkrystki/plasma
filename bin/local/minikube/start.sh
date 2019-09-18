#!/usr/bin/env bash

. "$ROOT"/shangren.sh

minikube --profile=shangren start --cpus=5 --memory=18000 --disk-size="40000mb" --vm-driver=kvm2
