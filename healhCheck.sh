#!/bin/bash

# SLEEP_TIME=$(shuf -i 2-10 -n 1);
SLEEP_TIME=$(($RANDOM % 10 + 1))
sleep $SLEEP_TIME;
resp_code=$(curl -L --max-time 10 -o /dev/null -s -w "%{http_code}\n" nginx2.default.svc.cluster.local)
if [[ $resp_code == "200" ]]; then
  exit 0
else
  exit 1
fi