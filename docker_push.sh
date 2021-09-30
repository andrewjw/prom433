#!/bin/bash

set -e

docker login --username andrewjw --password $DOCKER_TOKEN

docker build --build-arg VERSION=$TAG -t andrewjw/prom433:$TAG .

docker push andrewjw/prom433:$TAG
