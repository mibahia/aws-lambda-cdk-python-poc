from aws_cdk import (
    Stack,
)
from aws_cdk import aws_s3 as s3
from constructs import Construct

from construct.url_to_s3 import UrlToS3Lambda


class UploadRawData(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket.from_bucket_name(self, "demography_bucket", "gla-demography")

        UrlToS3Lambda(self, "UrlToS3Lambda", bucket=bucket)
