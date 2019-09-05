#!/usr/bin/env bash

cd `dirname $0`
cd ../../../..

./bin/local/sentry/seed.sh dataprovs/bitstamp/bin/sentry/dump.json
