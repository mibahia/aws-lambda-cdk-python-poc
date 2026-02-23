#!/bin/bash

docker rm core-pipeline-dev

docker build -t core-pipeline-dev .

docker run --name core-pipeline-dev \
    -p 9000:8080 \
    -v ~/.aws:/root/.aws \
    -v $PWD:/var/task \
    -e AWS_PROFILE=cdk-user \
    core-pipeline-dev 