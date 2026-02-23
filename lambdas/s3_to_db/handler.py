import logging
import os
from typing import Any

import pandas as pd
from src.aws_helpers import read_file_from_s3
from src.life_expectancy import LifeExpectancy

logger = logging.getLogger()
logger.setLevel("INFO")


def handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    print("🔍 Event received:", event)
    try:
        bucket = os.environ["BUCKET_NAME"]
        logger.info(
            f"Lambda time remaining in ms: {context.get_remaining_time_in_millis()}"
        )

        file_key = event.pop("file_key")

        response = read_file_from_s3(bucket=bucket, file_path=file_key)
        obj = LifeExpectancy(response=response)

        excel = obj.parse()
        data = obj.clean(excel=excel)
        print(data.head())

        logger.info(
            f"Lambda time remaining in ms: {context.get_remaining_time_in_millis()}"
        )

        return {
            "statusCode": 200,
        }
    except Exception as e:
        logger.error(f"Error uploading file: {e}")
        raise


# if __name__ == "__main__":
#     os.environ["BUCKET_NAME"] = "gla-demography"
#     handler(
#         event={
#             "url": "https://fingertips.phe.org.uk/api/all_data/csv/by_indicator_id?",
#             "file_key": "lifeexpectancylocalareas.xlsx",
#             "indicator_ids": "20601",
#             "area_type_id": "6",
#         },
#         context=None,
#     )
