# Note: Ensure that you have the necessary AWS credentials configured
# and the boto3 library installed in your Python environment.
# This script lists all objects in a specified S3 bucket and prefix

import argparse
import boto3

def list_all_objects(bucket: str, prefix: str):
    """Yield all object keys and sizes under a prefix."""

    s3 = boto3.client("s3")
    paginator = s3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        for obj in page.get("Contents", []):
            yield obj["Key"], obj["Size"]


def main() -> None:
    """CLI entry point for listing S3 objects."""

    parser = argparse.ArgumentParser(description="List objects in an S3 prefix")
    parser.add_argument(
        "--bucket",
        default="rawdatatecron",
        help="Name of the S3 bucket"
    )
    parser.add_argument(
        "--prefix",
        default="raw/finance/txn_payments/",
        help="Prefix within the bucket to list"
    )

    args = parser.parse_args()

    for key, size in list_all_objects(args.bucket, args.prefix):
        print(key, size)


if __name__ == "__main__":
    main()