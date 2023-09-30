#!/bin/bash

### Set variables

platform="arm64"
appName="nltkanalyzer"

### Build and push image

# Create image
docker build \
  --platform "linux/${platform}" \
  --tag "${DOCKERHUB_NAME}/${appName}" \
  "."

# docker run --name test "${DOCKERHUB_NAME}/${appName}"

# docker push "${DOCKERHUB_NAME}/${httpserver[imageName]}"
