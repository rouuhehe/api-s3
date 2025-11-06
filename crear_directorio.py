import boto3

bucket_name = "baldecito-tarea"
folder_name = "nuevacarpeta/"

s3 = boto3.client('s3')

s3.put_object(Bucket=bucket_name, Key=folder_name)
print(f"Folder '{folder_name}' created successfully in bucket '{bucket_name}'.")