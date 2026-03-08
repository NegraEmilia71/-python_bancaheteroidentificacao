import os
import shutil

def organize_files(pdf_files):

    base_folder = "output/pdf"

    os.makedirs(base_folder, exist_ok=True)

    for file in pdf_files:
        shutil.move(file, base_folder)
      
