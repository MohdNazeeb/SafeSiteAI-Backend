# app/s3_client.py
import os
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")

def get_s3_client():
    if not AWS_ACCESS_KEY or not AWS_SECRET_KEY:
        # credentials not set; return None (upload endpoints should handle this)
        return None
    return boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )

def upload_fileobj_to_s3(file_obj, bucket: str, key: str):
    s3 = get_s3_client()
    if s3 is None:
        raise RuntimeError("AWS credentials not configured")
    try:
        s3.upload_fileobj(file_obj, bucket, key)
    except ClientError as e:
        raise
