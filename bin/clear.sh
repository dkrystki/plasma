#!/usr/bin/env bash

printf "🧹Clearing the cluster🧹\n"

cd "$(dirname $0)" || exit
🧹
printf "\n☠️Deleting elasticsearch☠️\n"
helm delete --purge elasticsearch

printf "\n☠️Deleting mongodb☠️\n"
helm delete --purge mongodb

printf "\n☠️Deleting graylog☠️\n"
helm delete --purge graylog

printf "\n☠️Deleting fluentbit☠️\n"
helm delete --purge fluentbit

printf "\n☠️Deleting sentry☠️\n"
helm delete --purge sentry
