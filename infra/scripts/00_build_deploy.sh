#!/bin/bash

### Set variables

platform="arm64"
# platform="amd64"
appName="newsanalyzer"

### Build and push image

# Create image
docker build \
  --platform "linux/${platform}" \
  --tag "${DOCKERHUB_NAME}/${appName}" \
  "../../app"

# docker run --name test "${DOCKERHUB_NAME}/${appName}"

# docker push "${DOCKERHUB_NAME}/${httpserver[imageName]}"
