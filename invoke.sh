#!/bin/bash

aws lambda invoke \
  --function-name lambda_function \
  --cli-binary-format raw-in-base64-out \
  --payload '{"bucket": "gla-demography", "url": "https://www.ons.gov.uk/file?uri=/peoplepopulationandcommunity/birthsdeathsandmarriages/conceptionandfertilityrates/adhocs/2609livebirthsbyageofmotherbylocalauthoritiesenglandandwales2022to2023/finalfileage.xlsx", "file_key": "fertility/raw/fertility_data.xlsx"}' \
  response.json \
  --profile cdk-user
