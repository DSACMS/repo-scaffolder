import subprocess
import json
import os
import shutil

def get_date_fields():
    # Run git commands and capture as string
    output = subprocess.run(['git', 'log', '--date=iso', '--pretty=%cI', '--max-parents=0', '-n', '1'], capture_output=True, text=True)

    # Store string and strip of leading / trailing whitespace
    date =  output.stdout.strip()

    # Create a dictionary for date information to be pushed to JSON
    date_information = {"created": f"{date}", 
    "lastModified": "{% now 'utc', '%Y-%m-%dT%H:%M:%S%z' %}",
    "metadataLastUpdated": "{% now 'utc', '%Y-%m-%dT%H:%M:%S%z' %}"}

    return date_information

def update_code_json(json_file_path):
    # Read the JSON 
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Add date_information to the JSON
    data['date'] = get_date_fields()

    # Update the JSON 
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent = 2)

def main():
    try:
        # Change to the parent directory
        os.chdir('..')

        # Define the repometrics directory to remove
        dir_name = "repometrics"

        # Check if repometrics directory exists and remove it
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)

        # Get the project name from cookiecutter
        sub_project_dir = "{{cookiecutter.project_name}}"
        repometrics_file = "code.json"
        project_root_dir = os.path.abspath('..')

        json_file_path = os.path.join(sub_project_dir, repometrics_file)
    
        if os.path.exists(json_file_path):
            # Move code.json file to parent directory
            new_json_path = os.path.join(project_root_dir, repometrics_file)
            shutil.move(json_file_path, new_json_path)
        
            # Remove the source directory
            shutil.rmtree(sub_project_dir)

            # Update the json with date_information
            update_code_json(new_json_path)
            print("Succesfully generated code.json file!")

        else:
            print(f"Error: {repometrics_file} not found in {sub_project_dir}")

    except OSError as error:
        print(f"Error during OS operations: {error}")
    except shutil.Error as error:
        print(f"Error during shutil operations: {error}")

if __name__ == "__main__":
    main()
