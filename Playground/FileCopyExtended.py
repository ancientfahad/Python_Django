import os
import shutil

def copy_folders(src, dest):
    """
    Copy all folders, subfolders, and files from src to dest, excluding .exe files.

    Parameters:
    src (str): Source directory path
    dest (str): Destination directory path
    """

    # Verify the source path
    if not os.path.isdir(src):
        print(f"Source directory does not exist: {src}")
        return
    else:
        print(src)

    try:
        found_content = False  # To track if any content is found

        # Walk through the source directory
        for root, dirs, files in os.walk(src, topdown=True):
            found_content = True
            # Calculate destination path
            rel_path = os.path.relpath(root, src)
            dest_path = os.path.join(dest, rel_path)
            os.makedirs(dest_path, exist_ok=True)

            print(f"Copying from {root} to {dest_path}")

            # Copy each file
            for file in files:
                if not file.endswith('.exe'):
                    src_file = os.path.join(root, file)
                    dest_file = os.path.join(dest_path, file)

                    shutil.copy2(src_file, dest_file)  # Copy file with metadata
                    print(f"Copied: {src_file} -> {dest_file}")
                else:
                    print(f"Skipped: {os.path.join(root, file)} (ignored .exe file)")

        if not found_content:
            print("No files or directories found in the source path.")
        else:
            print("Copy process completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
source_directory = '/Volumes/Untitled/USB Drive/7th Semester'  # Explicitly use the hidden folder path
destination_directory = '/Users/u75530/Desktop/untitled folder'

copy_folders(source_directory, destination_directory)
