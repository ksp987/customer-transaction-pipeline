# GetS3TransactionData_lambda.py
# This Lambda function retrieves a CSV file from an S3 bucket, parses it, and returns
# the data in JSON format. It also handles CORS by allowing all origins.

import boto3
import json
import csv

def lambda_handler(event, context):
    # Initialize the S3 client
    s3 = boto3.client('s3')
    bucket = 'rawdatatecron'
    key = 'raw/finance/txn_payments/year=2024/month=06/PS_20174392719_1491204439457_log.csv'

    try: 
        response = s3.get_object(Bucket=bucket, Key=key)
        lines = response['Body'].read().decode('utf-8').splitlines()
        reader = csv.DictReader(lines)
        data = list(reader)

        return {
            'statusCode': 200,
            'body': json.dumps(data),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})    
        }
    