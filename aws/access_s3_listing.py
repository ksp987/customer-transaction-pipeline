# Note: Ensure that you have the necessary AWS credentials configured
# and the boto3 library installed in your Python environment.
# This script lists all objects in a specified S3 bucket and prefix

import boto3

s3 = boto3.client('s3')
bucket = 'rawdatatecron'
prefix = 'raw/finance/txn_payments/'

response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
for obj in response.get('Contents', []):
    print(obj['Key'], obj['Size'])
