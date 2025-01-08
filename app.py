from minio import Minio
from minio.error import S3Error
from dotenv import load_dotenv
import os
load_dotenv()


sceret_key=os.getenv("secret_key")
access_key=os.getenv("access_key")

client = Minio(
    "localhost:32775",  
    access_key=access_key, 
    secret_key=sceret_key, 
    secure=False 
)


bucket_name = "onedata"

objects = client.list_objects(bucket_name, prefix="raw/", recursive=True)
for obj in objects:
    print(obj)