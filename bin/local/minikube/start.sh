#!/usr/bin/env bash

. "$SHANGREN_ROOT"/shangren.sh

minikube --profile=shangren start --cpus=5 --memory=22000 --disk-size="40000mb" --vm-driver=kvm2
