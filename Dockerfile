FROM python:3.11-slim

WORKDIR /app

# Copy the Python script
COPY aws_secrets_demo.py .

# Set environment variables (BAD PRACTICE)
ENV AWS_ACCESS_KEY_ID="AKIA3MTWN5MBGU6LVPP2"
ENV AWS_SECRET_ACCESS_KEY="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"

# Install boto3
RUN pip install boto3

# Run the script
CMD ["python", "aws_secrets_demo.py"]
