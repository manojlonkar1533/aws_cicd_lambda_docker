# Dockerfile.lambda — AWS Lambda container image
FROM public.ecr.aws/lambda/python:3.12

WORKDIR /var/task
# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Lambda handler
COPY lambda_handler.py .

# Lambda runtime interface (must use CMD)
CMD ["lambda_handler.lambda_handler"]