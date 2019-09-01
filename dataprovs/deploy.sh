#!/usr/bin/env bash

helm install --namespace=$DATAPROVS_NAMESPACE --name=influxdb stable/influxdb
