from aws_cdk import Duration
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class S3ToDBLambda(Construct):
    def __init__(self, scope: Construct, id: str, bucket: str) -> None:
        super().__init__(scope, id)

        lambda_fn = _lambda.DockerImageFunction(
            self,
            "S3ToDBLambda",
            function_name=id,
            code=_lambda.DockerImageCode.from_image_asset("./lambdas/s3_to_db"),
            timeout=Duration.minutes(10),
            memory_size=1200,
            architecture=_lambda.Architecture.X86_64,
            environment={"BUCKET_NAME": bucket.bucket_name},
        )

        bucket.grant_read(lambda_fn)
