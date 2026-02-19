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
            runtime=_lambda.Runtime.PYTHON_3_11,
            code=_lambda.Code.from_asset(
                "src/",
                bundling=BundlingOptions(
                    image=DockerImage.from_registry(
                        "public.ecr.aws/sam/build-python3.11"
                    ),
                    command=[
                        "bash",
                        "-c",
                        "cp get_data_from_url.py aws_helpers.py handler.py /asset-output",
                    ],
                ),
            ),
            handler="handler.handler",
            timeout=Duration.minutes(5),
            architecture=_lambda.Architecture.ARM_64,
            environment={"BUCKET_NAME": bucket.bucket_name},
        )

        bucket.grant_write(lambda_fn)
