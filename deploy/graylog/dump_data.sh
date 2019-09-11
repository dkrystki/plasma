#!/usr/bin/env bash

. "$ROOT"/shangren.sh

printf "♻️Dumping graylog♻️\n"

MONGO_POD=$(kubectl -n graylog get pods -l app=mongodb-replicaset -o name | grep -m 1 -o "mongodb.*$")

kubectl -n graylog exec "$MONGO_POD" -- bash -c "mongodump --quiet -d graylog -o /home/dumps"
kubectl -n graylog cp "$MONGO_POD":home/dumps/graylog dump
printf "👌Dumping graylog done👌\n\n"
