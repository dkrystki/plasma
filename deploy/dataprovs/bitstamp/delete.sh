#!/usr/bin/env bash

. "$ROOT"/shangren.sh

printf "🧹Deleting bitstamp\n"

bash bitstamp/delete.sh

printf "👌Clearing Done👌\n\n"
