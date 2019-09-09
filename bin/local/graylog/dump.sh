#!/usr/bin/env bash

printf "♻️Dumping graylog♻️\n"

cd "$(dirname $0)" || exit

MONGO_POD=$(kubectl -n graylog get pods -l app=mongodb-replicaset -o name | grep -m 1 -o "mongodb.*$")

kubectl -n graylog exec "$MONGO_POD" -- bash -c "mongodump --quiet -d graylog -o /home/dumps"
kubectl -n graylog cp "$MONGO_POD":home/dumps/graylog dump
printf "👌Done👌\n\n"
