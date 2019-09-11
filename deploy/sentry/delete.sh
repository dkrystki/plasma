#!/usr/bin/env bash

. "$ROOT"/shangren.sh

printf "☠️Deleting sentry☠️\n"
helm delete --purge sentry
printf "👌️Deleting Sentry Done👌\n\n"
