from aws_cdk import (
    Duration,
    Stack,
)
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_s3 as s3
from constructs import Construct


class UploadRawData(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        gla_demography_bucket = s3.Bucket.from_bucket_name(
            self, "demography_bucket", "gla-demography"
        )

        # Define Lambda Function
        lambda_fn = _lambda.Function(
            self,
            "LambdaFunction",
            function_name="lambda_function",  # Set the name of the Lambda function
            runtime=_lambda.Runtime.PYTHON_3_13,
            handler="handler.handler",
            code=_lambda.Code.from_asset("lambda/"),  # Getting the necessary code
            timeout=Duration.minutes(5),  # Set the timeout
            architecture=_lambda.Architecture.ARM_64,  # Lighter, cheaper version - getting errors without param
        )

        # Need to give lambda access to s3 to write files.
        gla_demography_bucket.grant_write(lambda_fn)
