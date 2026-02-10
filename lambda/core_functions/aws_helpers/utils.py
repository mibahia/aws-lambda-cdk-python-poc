import os

import boto3
from botocore.exceptions import ClientError


def upload_file_to_s3(bucket: str, file_key: str, response: bytes) -> None:
    s3_client = boto3.client("s3")

    s3_client.put_object(
        Bucket=bucket,
        Key=file_key,
        Body=response,
        IfNoneMatch="*",
    )


def read_file_from_s3(bucket: str, file_path: str):
    s3_client = boto3.client("s3")

    try:
        response = s3_client.get_object(Bucket=bucket, Key=file_path)
        return response["Body"].read()
    except ClientError as e:
        print(f"Client error: {e}")
