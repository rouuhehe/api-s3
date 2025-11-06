import boto3

s3 = boto3.client('s3')

bucket_name = "baldecito-tarea"
region = "us-east-1"

try:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created successfully in region '{region}'.")
except Exception as e:
    print(f"Error creating bucket: {e}")
