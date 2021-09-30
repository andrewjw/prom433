#!/bin/bash

set -e

pip3 install -r requirements.txt

./code_style.sh
./run_tests.sh

BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Building branch $BRANCH"
if [[ "$BRANCH" == "master" ]]; then
  echo coverage
  COVERALLS_REPO_TOKEN=$PROM433_COVERALLS_REPO_TOKEN coveralls
  echo $?
  semantic-release publish
fi
if [[ ${BRANCH:0:7} == "heads/v" ]]; then
    ./docker_push.sh
fi
