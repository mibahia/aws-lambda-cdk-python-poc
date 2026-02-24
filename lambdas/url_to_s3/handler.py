import logging
import os
from typing import Any

<<<<<<<< HEAD:lambdas/url_to_s3/handler.py
from aws_helpers import upload_file_to_s3
from get_data_from_url import get_data_from_url
========
from src.aws_helpers import upload_file_to_s3
from src.get_data_from_url import get_data_from_url
>>>>>>>> origin/main:src/handler.py

logger = logging.getLogger()
logger.setLevel("INFO")


def handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    print("🔍 Event received:", event)
    try:
        bucket = os.environ["BUCKET_NAME"]

        url = event.pop("url")
        file_key = event.pop("file_key")

        response = get_data_from_url(url=url, **event)

        upload_file_to_s3(bucket=bucket, file_key=file_key, response=response)

        logger.info(
            f"File {file_key} from '{url}' sucessfully uploaded to S3 bucket {bucket}"
        )
        return {
            "statusCode": 200,
            "message": f"File {file_key} sucessfully uploaded to S3 bucket {bucket}",
        }
    except Exception as e:
        logger.error(f"Error uploading file: {e}")
        raise


# if __name__ == "__main__":
#     os.environ["BUCKET_NAME"] = "gla-demography"
#     handler(
#         event={
#             "url": "https://fingertips.phe.org.uk/api/all_data/csv/by_indicator_id?",
#             "file_key": "fingertips2.csv",
#             "indicator_ids": "20601",
#             "area_type_id": "6",
#         },
#         context=None,
#     )
