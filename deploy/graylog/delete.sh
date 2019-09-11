#!/usr/bin/env bash

. "$ROOT"/shangren.sh

printf "Deleting graylog🧹\n"

printf "☠️Deleting elasticsearch☠️\n"
helm delete --purge elasticsearch

printf "☠️Deleting mongodb☠️\n"
helm delete --purge mongodb

printf "☠️Deleting graylog☠️\n"
helm delete --purge graylog

printf "☠️Deleting fluentbit☠️\n"
helm delete --purge fluentbit

printf "👌Deleting graylog done👌\n\n"
