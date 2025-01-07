from minio import Minio
from minio.error import S3Error
from dotenv import load_dotenv
import os
load_dotenv()


sceret_key=os.getenv("secret_key")
access_key=os.getenv("access_key")


# Initialize MinIO client
client = Minio(
    "localhost:32776",  
    access_key=access_key, 
    secret_key=sceret_key, 
    secure=False 
)


bucket_name = "onedata"
folder_path = "Assessment_Data"  



try:
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)  # Full file path
            object_name = os.path.relpath(file_path, folder_path).replace("\\", "/")  # Preserve folder structure in MinIO
            client.fput_object(bucket_name, object_name, file_path)
            print(f"Uploaded: {file_path} as {object_name}")
except S3Error as err:
    print(f"Error uploading files: {err}")
