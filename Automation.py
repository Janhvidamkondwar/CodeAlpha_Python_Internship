
# import os
# import shutil

# source_folder='myfolder'
# destination_folder='jpg_files'

# #to create new folder
# os.makedirs(destination_folder,exist_ok=True)

# for files in os.listdir(source_folder):
#     if files.endswith ('.jpg'):
#         source_path=os.path.join(source_folder,files)
#         destination_folder=os.path.join(destination_folder,files)
#         shutil.move(source_folder,destination_folder)
# print("All jpg files moved successfully.")
        
import os
import shutil

source_folder = "myfolder"
destination_folder = "jpg_files"

# Agar myfolder nahi hai to automatically bana dega
os.makedirs(source_folder, exist_ok=True)

# jpg_files nahi hai to automatically bana dega
os.makedirs(destination_folder, exist_ok=True)

for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

print("All JPG files moved successfully!")