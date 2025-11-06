import boto3
#https://i.pinimg.com/736x/ff/dd/86/ffdd8691730d5ca5688450e93cd8d60e.jpg
import requests
import json

s3 = boto3.client('s3')
BUCKET = "baldecito-tarea"

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        image_url = body["image_url"]
        file_name = body["file_name"]
        folder_name = body["folder_name"]
        key = f"{folder_name}{file_name}"

        # Descargar la imagen desde el enlace
        response = requests.get(image_url)
        if response.status_code != 200:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No se pudo descargar la imagen"})
            }

        # Subir a S3
        s3.put_object(Bucket=BUCKET, Key=key, Body=response.content)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Imagen subida correctamente",
                "s3_path": f"s3://{BUCKET}/{key}"
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
