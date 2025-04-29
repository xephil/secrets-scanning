import requests

# WARNING: Hardcoded secrets are a BAD practice!
API_KEY = "sk_test_51N3FJEXAMPLEh6gW4Vd7jkfa0f4lJmz"
DB_PASSWORD = "P@ssw0rd123!"
aws_access_key_id = "AKIA6KJQR5EG25KTYHEV"
aws_secret_access_key = "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"

def call_external_service():
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get("https://api.example.com/data", headers=headers)
    return response.json()

def connect_to_database():
    connection_string = f"mongodb://admin:{DB_PASSWORD}@localhost:27017/"
    # Simulate database connection
    print(f"Connecting to database with: {connection_string}")

def upload_to_aws():
    # Simulate uploading to AWS S3
    print(f"Uploading file with AWS Secret Key: {aws_secret_access_key}")

if __name__ == "__main__":
    call_external_service()
    connect_to_database()
    upload_to_aws()
