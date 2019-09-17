#!/usr/bin/env bash

. "$ROOT"/shangren.sh

minikube --profile=shangren start --cpus=5 --memory=15000 --disk-size="40000mb"
