#!/bin/bash

export AWS_REGION=eu-west-2

aws lambda invoke \
  --function-name UrlToS3Lambda \
  --cli-binary-format raw-in-base64-out \
  --payload '{"url": "https://fingertips.phe.org.uk/api/all_data/csv/by_indicator_id?", "file_key": "fingertips2.csv" ,"indicator_ids":"20601", "area_type_id": "6"}' \
  response.json \
  --profile cdk-user
