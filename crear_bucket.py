import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = "baldecito-tarea"
    region = event.get("region", "us-east-1")

    try:
        s3.create_bucket(Bucket=bucket_name)
        return {
            'statusCode': 200,
            'body': f"Bucket '{bucket_name}' creado exitosamente en '{region}'."
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error creando bucket: {str(e)}"
        }
