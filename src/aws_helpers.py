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


def read_file_from_s3(session: boto3.Session, bucket: str, file_path: str):
    s3_client = session.client("s3")

    try:
        response = s3_client.get_object(Bucket=bucket, Key=file_path)
        return response["Body"].read()
    except ClientError as e:
        print(f"Client error: {e}")


# if __name__ == "__main__":
# session = boto3.Session(profile_name="cdk-user")
# data = read_file_from_s3(
#     session=session,
#     bucket="gla-demography",
#     file_path="lifeexpectancylocalareas.xlsx",
# )

# with BytesIO(data) as file:
#     excel = pd.read_excel(
#         file,
#         sheet_name="1",
#         header=5,
#         skiprows=None,
#         skipfooter=0,
#         parse_dates=False,
#     )
#     pd.ExcelWriter
