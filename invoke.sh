#!/bin/bash

aws lambda invoke \
  --function-name upload-raw-data-staging \
  --cli-binary-format raw-in-base64-out \
  --payload '{"url": "https://www.ons.gov.uk/file?uri=/peoplepopulationandcommunity/birthsdeathsandmarriages/conceptionandfertilityrates/adhocs/2609livebirthsbyageofmotherbylocalauthoritiesenglandandwales2022to2023/finalfileage.xlsx", "file_key": "fertility/finalfileage.xlsx"}' \
  response.json \
  --profile cdk-user
