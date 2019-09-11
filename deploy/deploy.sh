#!/usr/bin/env bash

. "$ROOT"/shangren.sh

printf "Deploying services\n"

bash graylog/deploy.sh
bash sentry/deploy.sh
bash dataprovs/deploy.sh

printf "👌Deployed services👌\n\n"
