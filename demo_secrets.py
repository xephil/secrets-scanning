import requests

# WARNING: Hardcoded secrets are a BAD practice!
API_KEY = "sk_test_51N3FJEXAMPLEh6gW4Vd7jkfa0f4lJmz"
DB_PASSWORD = "P@ssw0rd123!"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

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
    print(f"Uploading file with AWS Secret Key: {AWS_SECRET_ACCESS_KEY}")

if __name__ == "__main__":
    call_external_service()
    connect_to_database()
    upload_to_aws()
