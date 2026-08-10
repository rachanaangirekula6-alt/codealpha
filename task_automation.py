import os
import shutil

source_folder = input("Enter the source folder path: ")
destination_folder = input("Enter the destination folder path: ")

if not os.path.exists(source_folder):
    print("Source folder does not exist.")
else:
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    count = 0

    for file in os.listdir(source_folder):
        if file.lower().endswith(".jpg"):
            source_file = os.path.join(source_folder, file)
            destination_file = os.path.join(destination_folder, file)

            shutil.move(source_file, destination_file)
            count += 1

    print(count, "JPG file(s) moved successfully.")