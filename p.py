import boto3
import os

# Set configerations
session = boto3.Session(
  region_name = 'ap-southeast-1',
  aws_access_key_id = 'AKIA3JLEB3ZSUBTIXSUL',
  aws_secret_access_key= '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'
)

# Create s3 service client
s3 = session.client('s3')

# Upload file to a selected bucket
def upload():
  response = s3.upload_file(
    Filename="photo.jpg",
    Bucket="infini-test-bucket",
    Key="photo.jpg",
  )

upload()
