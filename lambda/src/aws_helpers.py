import logging

import boto3

logger = logging.getLogger(__name__)


def upload_file_to_s3(bucket: str, file_key: str, response: bytes) -> None:
    s3_client = boto3.client("s3")

    s3_client.put_object(
        Bucket=bucket,
        Key=file_key,
        Body=response,
        IfNoneMatch="*",
    )
