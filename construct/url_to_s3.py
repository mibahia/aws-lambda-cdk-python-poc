from aws_cdk import BundlingOptions, DockerImage, Duration
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class UrlToS3Lambda(Construct):
    def __init__(self, scope: Construct, id: str, bucket: str) -> None:
        super().__init__(scope, id)

        lambda_fn = _lambda.Function(
            self,
            "LambdaFunction",
            function_name=id,
            runtime=_lambda.Runtime.PYTHON_3_13,
            code=_lambda.Code.from_asset(
                "lambda/",
                bundling=BundlingOptions(
                    image=DockerImage.from_registry("python:3.13-slim-bookworm"),
                    command=[
                        "bash",
                        "-c",
                        "cp -r url_to_s3/* /asset-output && "
                        "cp -r core_functions /asset-output",
                    ],
                ),
            ),
            handler="handler.handler",
            timeout=Duration.minutes(5),
            architecture=_lambda.Architecture.ARM_64,
            environment={"BUCKET_NAME": bucket.bucket_name},
        )

        bucket.grant_write(lambda_fn)
