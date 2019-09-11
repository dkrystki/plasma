#!/usr/bin/env bash

. "$ROOT"/shangren.sh

printf "🌱Seeding graylog🌱\n"

MONGO_POD=$(kubectl -n graylog get pods -l app=mongodb-replicaset -o name | grep -m 1 -o "mongodb.*$")

kubectl -n graylog exec "$MONGO_POD" -- bash -c "mkdir -p /home/restore"
kubectl -n graylog cp dump "$MONGO_POD":home/restore/graylog
kubectl -n graylog exec "$MONGO_POD" -- bash -c "mongorestore --quiet /home/restore"
printf "👌Seeding graylog done👌\n\n"
