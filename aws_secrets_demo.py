aws_secrets_demo.py

import boto3

# WARNING: Hardcoded secrets are insecure! This is for DEMO PURPOSES ONLY.
aws_access_key_id = "AKIA3MTWN5MBGU6LVPP2"
aws_secret_access_key = "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"

def list_s3_buckets():
    # Create a session with hardcoded credentials
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name="us-east-1"
    )
    s3 = session.client('s3')

    try:
        response = s3.list_buckets()
        print("Buckets:")
        for bucket in response.get('Buckets', []):
            print(f" - {bucket['Name']}")
    except Exception as e:
        print(f"Error listing S3 buckets: {e}")

if __name__ == "__main__":
    list_s3_buckets()
