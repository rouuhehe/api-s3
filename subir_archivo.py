import boto3
import base64

def lambda_handler(event, context):
    s3 = boto3.resource('s3')

    # Parámetros desde el evento
    bucket_name = "baldecito-tarea"
    folder_name =  "nuevacarpeta/"
    file_name = "gatitos.png"
    base64_str = event.get("base64_str")

    if not base64_str:
        return {
            'statusCode': 400,
            'body': "Falta el parámetro 'base64_str' con la imagen codificada."
        }

    try:
        s3_file_name = f"{folder_name}{file_name}"

        s3.Object(bucket_name, s3_file_name).put(Body=base64.b64decode(base64_str))

        return {
            'statusCode': 200,
            'body': f"Imagen subida exitosamente en s3://{bucket_name}/{s3_file_name}"
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error subiendo imagen: {str(e)}"
        }
