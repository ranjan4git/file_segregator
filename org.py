import os
import shutil

def classify_files_by_extension(base_folder):
    # Change directory to the base folder
    os.chdir(base_folder)
    
    # Get all files and directories in the base folder
    items = os.listdir(base_folder)
    
    # Process each item
    for item in items:
        item_path = os.path.join(base_folder, item)
        
        # If the item is a file, process it
        if os.path.isfile(item_path):
            # Get the file extension
            _, ext = os.path.splitext(item)
            
            # Remove the dot from the extension
            ext = ext[1:] if ext.startswith('.') else ext
            
            # Create a folder with the extension name if it doesn't exist
            ext_folder = os.path.join(base_folder, ext)
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)
            
            # Move the file into the extension folder
            shutil.move(item_path, os.path.join(ext_folder, item))
        
        # If the item is a directory, process it recursively
        elif os.path.isdir(item_path):
            classify_files_by_extension(item_path)

# Usage
base_folder = "path-to-directory"
classify_files_by_extension(base_folder)



