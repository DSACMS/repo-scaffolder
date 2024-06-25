import os
import shutil
import time 

# Get working directory and repometrics file
current_dir = os.getcwd()
repometrics_file = "repometrics.json"
source_file = os.path.join(current_dir, repometrics_file)

# Get parent directory, one level up from the current directory
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

# Construct the destination path in the parent directory
destination_file = os.path.join(parent_dir, repometrics_file)

# Attempt to move repometrics to parent directory
try:
    shutil.move(source_file, destination_file)
except FileNotFoundError:
    print(f"The file {source_file} does not exist.")
except PermissionError:
    print(f"Permission denied: Unable to move the file {source_file}.")
except Exception as e:
    print(f"An error occurred: {e}")


# Remove directory once repometrics file was successfully moved
os.chdir("..")
dir_name = "{{cookiecutter.project_type}}"

try:
    # Check if the directory exists
    if os.path.exists(dir_name):
        # Attempt to remove the directory
        shutil.rmtree(dir_name)
    else:
        print(f"Directory '{dir_name}' does not exist.")
except FileNotFoundError:
    print(f"File not found: The directory '{dir_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")