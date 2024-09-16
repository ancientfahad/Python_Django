import csv
import os
import shutil

file_path = '/Users/u75530/Desktop/ID.csv'
folder_path = '/Users/u75530/Desktop/Photopath'
destination_folder = '/Users/u75530/Desktop/MatchedFiles'  # Folder where matching files will be copied

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

badgeID = set()  # Use a set for badgeID to easily remove found ones
fileID = []

# Get badgeID from the CSV
with open(file_path, 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)

    for row in reader:
        # Remove any leading or trailing whitespace characters and add to badgeID set
        badgeID.add(int(row[0].strip()))

# Keep a copy of the original badgeID set for tracking unmatched IDs
unmatched_badgeID = badgeID.copy()

# Get a list of files in the folder
file_names = os.listdir(folder_path)

# Compare and copy files that match badgeID
for file in file_names:
    try:
        # Attempt to extract the first 5 characters and convert them to an integer
        file_id = int(file[0:5])  # Extract first 5 characters as file ID
        if file_id in badgeID:  # Check if the fileID matches badgeID
            # Source file path
            source_file = os.path.join(folder_path, file)
            # Destination file path
            destination_file = os.path.join(destination_folder, file)
            # Copy the file
            shutil.copy(source_file, destination_file)

            print(f"Copied {file} to {destination_folder}")
            
            # Remove the matched badgeID from unmatched_badgeID set
            unmatched_badgeID.discard(file_id)

    except ValueError:
        # Skip the file if it cannot be converted to an integer
        print(f"Skipping file: {file}, not a valid ID.")

# Print unmatched badge IDs
if unmatched_badgeID:
    print("Badge IDs not matched with any files:")
    for badge in unmatched_badgeID:
        print(badge)
else:
    print("All badge IDs were matched with files.")

# Optional: Print summary of copied files
print(f"Total files copied: {len(os.listdir(destination_folder))}")
