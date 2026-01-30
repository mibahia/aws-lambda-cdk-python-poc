#!/bin/bash

export AWS_REGION=eu-west-2

aws lambda invoke \
  --function-name UrlToS3Lambda \
  --cli-binary-format raw-in-base64-out \
  --payload '{"url": "https://www.ons.gov.uk/file?uri=/peoplepopulationandcommunity/birthsdeathsandmarriages/conceptionandfertilityrates/adhocs/2609livebirthsbyageofmotherbylocalauthoritiesenglandandwales2022to2023/finalfileage.xlsx", "file_key": "finalfileage.xlsx"}' \
  response.json \
  --profile cdk-user
