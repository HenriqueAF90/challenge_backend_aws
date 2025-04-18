#arquivo para configuraçao do localstack
import os
import boto3
#configs para o localstack
AWS_ENDPOINT_URL = os.getenv("AWS_ENDPOINT_URL", "http://localhost:4566")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")


dynamodb_client = boto3.resource(
    "dynamodb",
    region_name=AWS_REGION,
    endpoint_url=AWS_ENDPOINT_URL,
)

sqs_client = boto3.client(
    "sqs",
    region_name=AWS_REGION,
    endpoint_url=AWS_ENDPOINT_URL,
)

s2_client = boto3.client(
"s3"),
region_name=AWS_REGION,
endpoint_url=AWS_ENDPOINT_URL,

