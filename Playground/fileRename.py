### Elementary

# import os
# import shutil

# def organize_photos(base_directory):
#     # Loop through each homeroom directory in the specified path
#     for root, dirs, files in os.walk(base_directory):
#         # Check if the current folder is a homeroom folder
#         if any(folder in root for folder in ["PrekB", "PrekF", "KGB", "KGR", "1C", "1G", "2B", "2L", "3M", "3P", "4K", "4R", "5C", "5J"]):
#             front_faced_dir = os.path.join(root, "Front Faced")
#             side_faced_dir = os.path.join(root, "Side Faced")
            
#             # Create folders for organizing photos
#             os.makedirs(front_faced_dir, exist_ok=True)
#             os.makedirs(side_faced_dir, exist_ok=True)
            
#             for file_name in files:
#                 if file_name.lower().endswith(".jpg"):
#                     # Separate files based on naming pattern
#                     if ".." in file_name or " .." in file_name:
#                         target_dir = front_faced_dir
#                     else:
#                         target_dir = side_faced_dir
                    
#                     # Rename the file to 12345.jpg format
#                     new_name = file_name.split("..")[0].strip() + ".jpg"
#                     new_name = new_name.split(".")[0].strip() + ".jpg"  # Extra safeguard
                    
#                     # Move the file to the appropriate folder
#                     src_path = os.path.join(root, file_name)
#                     dst_path = os.path.join(target_dir, new_name)
#                     shutil.move(src_path, dst_path)
#                     print(f"Moved: {src_path} -> {dst_path}")

# if __name__ == "__main__":
#     base_directory = "/Users/u75530/Desktop/Yearbook Photos/Elementary/By ID"
#     organize_photos(base_directory)

# import os
# import shutil
# import pandas as pd

# def create_folder_structure(base_directory, homeroom_folders):
#     """Creates the By Name folder structure for elementary grades."""
#     by_name_base = os.path.join(base_directory, "By Name")
#     for homeroom in homeroom_folders:
#         front_faced_dir = os.path.join(by_name_base, homeroom, "Front Faced")
#         side_faced_dir = os.path.join(by_name_base, homeroom, "Side Faced")
#         os.makedirs(front_faced_dir, exist_ok=True)
#         os.makedirs(side_faced_dir, exist_ok=True)
#     return by_name_base

# def copy_and_rename_photos(source_base, destination_base, homeroom_folders, id_to_name_mapping):
#     """Copies and renames photos based on ID-to-name mapping."""
#     for homeroom in homeroom_folders:
#         for folder_type in ["Front Faced", "Side Faced"]:
#             src_folder = os.path.join(source_base, homeroom, folder_type)
#             dest_folder = os.path.join(destination_base, homeroom, folder_type)
#             if not os.path.exists(src_folder):
#                 continue

#             for file_name in os.listdir(src_folder):
#                 if file_name.lower().endswith(".jpg"):
#                     # Extract ID from the filename
#                     student_id = os.path.splitext(file_name)[0]  # Get filename without extension
#                     if student_id in id_to_name_mapping:
#                         student_name = id_to_name_mapping[student_id]
#                         new_file_name = f"{student_name}.jpg"
#                         src_path = os.path.join(src_folder, file_name)
#                         dest_path = os.path.join(dest_folder, new_file_name)
#                         shutil.copy(src_path, dest_path)
#                         print(f"Copied and renamed: {src_path} -> {dest_path}")
#                     else:
#                         print(f"ID {student_id} not found in mapping. Skipping {file_name}.")

# if __name__ == "__main__":
#     # Directory paths
#     base_directory = "/Users/u75530/Desktop/Yearbook Photos/Elementary"
#     source_base = os.path.join(base_directory, "By ID")
#     homeroom_folders = ["PrekB", "PrekF", "KGB", "KGR", "1C", "1G", "2B", "2L", "3M", "3P", "4K", "4R", "5C", "5J"]
#     destination_base = create_folder_structure(base_directory, homeroom_folders)
    
#     # Load the Excel file with student information
#     excel_path = "/Users/u75530/Desktop/Yearbook Photos/Students.xlsx"
#     student_data = pd.read_excel(excel_path)
    
#     # Create a dictionary mapping ID to Name
#     id_to_name_mapping = dict(zip(student_data["ID"].astype(str), student_data["Name"]))
    
#     # Process the folders
#     copy_and_rename_photos(source_base, destination_base, homeroom_folders, id_to_name_mapping)

######################################################################################################################################################################################
######################################################################################################################################################################################
######################################################################################################################################################################################

### Secondary
# import os
# import shutil

# def organize_photos(base_directory, grade_folders, front_identifier, side_identifier):
#     # Loop through each grade folder in the specified path
#     for root, dirs, files in os.walk(base_directory):
#         # Check if the current folder is a grade folder
#         if any(folder in root for folder in grade_folders):
#             front_faced_dir = os.path.join(root, "Front Faced")
#             side_faced_dir = os.path.join(root, "Side Faced")
            
#             # Create folders for organizing photos
#             os.makedirs(front_faced_dir, exist_ok=True)
#             os.makedirs(side_faced_dir, exist_ok=True)
            
#             for file_name in files:
#                 if file_name.lower().endswith(".jpg"):
#                     # Separate files based on the identifier
#                     if front_identifier in file_name:
#                         target_dir = front_faced_dir
#                     elif side_identifier in file_name:
#                         target_dir = side_faced_dir
#                     else:
#                         continue  # Skip files that don't match either identifier
                    
#                     # Rename the file to 12345.jpg format
#                     new_name = file_name.split(front_identifier)[0].strip() + ".jpg"
#                     new_name = new_name.split(side_identifier)[0].strip() + ".jpg"  # Handle both cases
                    
#                     # Move the file to the appropriate folder
#                     src_path = os.path.join(root, file_name)
#                     dst_path = os.path.join(target_dir, new_name)
#                     shutil.move(src_path, dst_path)
#                     print(f"Moved: {src_path} -> {dst_path}")

# if __name__ == "__main__":
#     base_directory = "/Users/u75530/Desktop/Yearbook Photos/Secondary/By ID"
#     grade_folders = ["6", "7", "8", "9", "10", "11", "12"]
#     front_identifier = "(1)"  # Identifier for front faced photos
#     side_identifier = "(2)"   # Identifier for side faced photos
    
#     organize_photos(base_directory, grade_folders, front_identifier, side_identifier)

# import os
# import shutil
# import pandas as pd

# def create_folder_structure(base_directory, grade_folders):
#     """Creates the By Name folder structure."""
#     by_name_base = os.path.join(base_directory, "By Name")
#     for grade in grade_folders:
#         front_faced_dir = os.path.join(by_name_base, grade, "Front Faced")
#         side_faced_dir = os.path.join(by_name_base, grade, "Side Faced")
#         os.makedirs(front_faced_dir, exist_ok=True)
#         os.makedirs(side_faced_dir, exist_ok=True)
#     return by_name_base

# def copy_and_rename_photos(source_base, destination_base, grade_folders, id_to_name_mapping):
#     """Copies and renames photos based on ID-to-name mapping."""
#     for grade in grade_folders:
#         for folder_type in ["Front Faced", "Side Faced"]:
#             src_folder = os.path.join(source_base, grade, folder_type)
#             dest_folder = os.path.join(destination_base, grade, folder_type)
#             if not os.path.exists(src_folder):
#                 continue

#             for file_name in os.listdir(src_folder):
#                 if file_name.lower().endswith(".jpg"):
#                     # Extract ID from the filename
#                     student_id = os.path.splitext(file_name)[0]  # Get filename without extension
#                     if student_id in id_to_name_mapping:
#                         student_name = id_to_name_mapping[student_id]
#                         new_file_name = f"{student_name}.jpg"
#                         src_path = os.path.join(src_folder, file_name)
#                         dest_path = os.path.join(dest_folder, new_file_name)
#                         shutil.copy(src_path, dest_path)
#                         print(f"Copied and renamed: {src_path} -> {dest_path}")
#                     else:
#                         print(f"ID {student_id} not found in mapping. Skipping {file_name}.")

# if __name__ == "__main__":
#     # Directory paths
#     base_directory = "/Users/u75530/Desktop/Yearbook Photos/Secondary"
#     source_base = os.path.join(base_directory, "By ID")
#     destination_base = create_folder_structure(base_directory, ["6", "7", "8", "9", "10", "11", "12"])
    
#     # Load the Excel file with student information
#     excel_path = "/Users/u75530/Desktop/Yearbook Photos/Students.xlsx"
#     student_data = pd.read_excel(excel_path)
    
#     # Create a dictionary mapping ID to Name
#     id_to_name_mapping = dict(zip(student_data["ID"].astype(str), student_data["Name"]))
    
#     # Process the folders
#     copy_and_rename_photos(source_base, destination_base, ["6", "7", "8", "9", "10", "11", "12"], id_to_name_mapping)

import os
import shutil

def copy_front_faced_photos(source_base, homeroom_folders, destination_folder):
    """Copies all front-faced photos from source folders to a single destination."""
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)
    
    for homeroom in homeroom_folders:
        front_faced_folder = os.path.join(source_base, homeroom, "Front Faced")
        
        if not os.path.exists(front_faced_folder):
            print(f"Folder does not exist: {front_faced_folder}. Skipping...")
            continue
        
        for file_name in os.listdir(front_faced_folder):
            if file_name.lower().endswith(".jpg"):
                src_path = os.path.join(front_faced_folder, file_name)
                dest_path = os.path.join(destination_folder, file_name)
                
                # Ensure no overwriting by renaming duplicates
                if os.path.exists(dest_path):
                    name, ext = os.path.splitext(file_name)
                    count = 1
                    while os.path.exists(dest_path):
                        dest_path = os.path.join(destination_folder, f"{name}_{count}{ext}")
                        count += 1
                
                shutil.copy(src_path, dest_path)
                print(f"Copied: {src_path} -> {dest_path}")

if __name__ == "__main__":
    # Directory paths
    # source_base = "/Users/u75530/Desktop/Yearbook Photos/Elementary/By ID"
    source_base = "/Users/u75530/Desktop/Yearbook Photos/Secondary/By ID"
    # homeroom_folders = ["PrekB", "PrekF", "KGB", "KGR", "1C", "1G", "2B", "2L", "3M", "3P", "4K", "4R", "5C", "5J"]
    homeroom_folders = ["6", "7", "8", "9", "10", "11", "12"]
    destination_folder = "/Users/u75530/Desktop/Yearbook Photos/PowerSchool"
    
    # Copy photos
    copy_front_faced_photos(source_base, homeroom_folders, destination_folder)