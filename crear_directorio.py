import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    bucket_name = "baldecito-tarea"
    folder_name = "nuevacarpeta/"

    try:
        s3.put_object(Bucket=bucket_name, Key=folder_name)
        return {
            'statusCode': 200,
            'body': f"Carpeta '{folder_name}' creada correctamente en el bucket '{bucket_name}'."
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error creando carpeta: {str(e)}"
        }
