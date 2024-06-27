import os
import shutil

# Get working directory and code.json file
project_type = '{{cookiecutter.project_type}}'
current_dir = os.getcwd()
repometrics_file = "code.json"
source_file = os.path.join(current_dir, repometrics_file)

# Get parent directory, one level up from the current directory
parent_dir = os.path.normpath(os.path.join(current_dir, '..'))
# Construct the destination path in the parent directory
destination_file = os.path.join(parent_dir, repometrics_file)

# Attempt to move code.json to parent directory
try:
    shutil.move(source_file, destination_file)
except FileNotFoundError:
    print(f"The file {source_file} does not exist.")
except PermissionError:
    print(f"Permission denied: Unable to move the file {source_file}.")
except Exception as e:
    print(f"An error occurred: {e}")


# Remove directories once code.json file was successfully moved
dir_name = "repometrics"
repometrics_dir = os.path.join(parent_dir, dir_name)
project_type_dir = os.path.join(parent_dir, project_type)

try:
    if os.path.isdir(repometrics_dir):
        shutil.rmtree(repometrics_dir)

    if os.path.isdir(project_type_dir):
        shutil.rmtree(project_type_dir)
except Exception as e:
    print(f"An error occurred: {e}")