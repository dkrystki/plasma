#!/usr/bin/env bash

printf "🌱Seeding graylog🌱\n"

cd "$(dirname $0)" || exit

MONGO_POD=$(kubectl -n graylog get pods -l app=mongodb-replicaset -o name | grep -m 1 -o "mongodb.*$")

kubectl -n graylog exec "$MONGO_POD" -- bash -c "mkdir -p /home/restore"
kubectl -n graylog cp dump "$MONGO_POD":home/restore/graylog
kubectl -n graylog exec "$MONGO_POD" -- bash -c "mongorestore --quiet /home/restore"
printf "👌Done👌\n\n"
