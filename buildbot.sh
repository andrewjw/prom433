#!/bin/bash

set -e

pip3 install -r requirements.txt

COVERAGE=coverage-3.8 ./run_tests.sh

pip3.9 install -r requirements.txt

COVERAGE=coverage-3.9 ./run_tests.sh

pip3.10 install -r requirements.txt

COVERAGE=coverage-3.10 ./run_tests.sh

pip3.11 install -r requirements.txt

COVERAGE=coverage-3.11 ./run_tests.sh

./code_style.sh

BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Building branch $BRANCH"
if [[ "$BRANCH" == "main" ]]; then
  COVERALLS_REPO_TOKEN=$PROM433_COVERALLS_REPO_TOKEN coveralls
  semantic-release publish
fi
if [[ ${BRANCH:0:7} == "heads/v" ]]; then
    TAG=${BRANCH:7} ./docker_push.sh
fi
