import requests

# WARNING: Hardcoded secrets are a BAD practice!
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def upload_to_aws():
    # Simulate uploading to AWS S3
    print(f"Uploading file with AWS Secret Key: {AWS_SECRET_ACCESS_KEY}")

if __name__ == "__main__":
    upload_to_aws()
