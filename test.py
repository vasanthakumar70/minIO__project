import os
folder_path = "Assessment_Data"  


for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        file_path = os.path.join(root, file_name)  # Full file path
        object_name = os.path.relpath(file_path, folder_path).replace("\\", "/")  # Preserve folder structure in MinIO
            # client.fput_object(bucket_name, object_name, file_path)
        print(f"Uploaded: {file_path} as {object_name}")

