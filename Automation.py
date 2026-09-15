
import os
import shutil

source_folder = "myfolder"
destination_folder = "jpg_files"
os.makedirs(source_folder, exist_ok=True)
os.makedirs(destination_folder, exist_ok=True)

for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

print("All JPG files moved successfully!")
