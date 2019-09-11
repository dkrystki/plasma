#!/usr/bin/env bash

. "$ROOT"/shangren.sh

printf "🧹Clearing the cluster🧹\n"

bash graylog/delete.sh
🧹bash sentry/delete.sh
bash dataprovs/delete.sh

printf "👌Cleared the cluster👌\n\n"
