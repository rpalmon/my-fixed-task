#!/bin/bash
# pytest + pytest-json-ctrf are baked into environment/Dockerfile (no verify-time installs).

pytest /tests/test_outputs.py -rA --ctrf /app/ctrf.json
rc=$?

if [ "$rc" -eq 0 ]; then
  echo 1 > /app/reward.txt
else
  echo 0 > /app/reward.txt
fi