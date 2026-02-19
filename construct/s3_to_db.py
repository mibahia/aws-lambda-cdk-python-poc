from aws_cdk import BundlingOptions, DockerImage, Duration
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class S3ToDBLambda(Construct):
    def __init__(self, scope: Construct, id: str, bucket: str) -> None:
        super().__init__(scope, id)

        dependencies_layer = _lambda.LayerVersion(
            self,
            "DependenciesLayer",
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_11],
            compatible_architectures=[_lambda.Architecture.ARM_64],
            code=_lambda.Code.from_asset(
                "src/lib",
            ),
        )

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
                        "cp aws_helpers.py /asset-output && cp -r s3_to_db/* /asset-output",
                    ],
                ),
            ),
            handler="handler.handler",
            timeout=Duration.minutes(5),
            architecture=_lambda.Architecture.ARM_64,
            environment={"BUCKET_NAME": bucket.bucket_name},
            layers=[dependencies_layer],
        )

        bucket.grant_write(lambda_fn)
