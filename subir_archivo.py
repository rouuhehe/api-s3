import boto3
import base64


bucket_name = "baldecito-tarea"
folder_name = "nuevacarpeta/"

def upload_base_64_to_s3(s3_bucket_name, s3_file_name, base_64_str):
    """
    Allows for the upload of a base64 string to a s3 object, may need fleshing out down the line, returns location
    of file in S3
    :param s3_bucket_name: S3 bucket name to push image to
    :param s3_file_name: File name
    :param base_64_str: base 64 string of the image to push to S3
    :return: Tuple of bucket_name and s3_file_name
    """
    s3 = boto3.resource('s3')
    s3.Object(s3_bucket_name, s3_file_name).put(Body=base64.b64decode(base_64_str))
    return (s3_bucket_name, s3_file_name)


with open("mi_imagen.png", "rb") as img_file:
    base64_str = base64.b64encode(img_file.read()).decode("utf-8")

bucket, key = upload_base_64_to_s3(bucket_name, f"{folder_name}gatitos.png", base64_str)
print(f"Imagen subida en s3://{bucket}/{key}")
