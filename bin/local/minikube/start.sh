#!/usr/bin/env bash

. "$SHANGREN_ROOT"/shangren.sh

minikube --profile=shangren start --vm-driver=none
