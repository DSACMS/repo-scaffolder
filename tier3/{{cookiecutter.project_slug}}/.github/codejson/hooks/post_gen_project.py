import subprocess
import shutil
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

def get_scc_labor_hours():
    if shutil.which('scc') is not None:
        try:
            #Run scc and load results into a dictionary
            #assuming we are in the .git directory of the repo
            cmd = ['scc', '..', '--format', 'json2', '--exclude-file']

            # Currently only supports specific files
            files_to_exclude = [
                "checks.yml,auto-changelog.yml,contributors.yml,repoStructure.yml,code.json,checklist.md,checklist.pdf,README.md,CONTIRBUTING.md,LICENSE,MAINTAINERS.md,repolinter.json,SECURITY.md,CODE_OF_CONDUCT.md,CODEOWNERS.md,COMMUNITY_GUIDELINES.md,GOVERANCE.md"
            ]

            cmd.extend(files_to_exclude)

            d = json.loads(subprocess.run(cmd,check=True, capture_output=True).stdout)
            
            l_hours = d['estimatedScheduleMonths'] * 730.001

            return round(l_hours,2)
            
        except (subprocess.CalledProcessError, KeyError) as e:
            print(e)
            return None
    else:
        print("scc (https://github.com/boyter/scc) not found on system")

        #Otherwise just use previous value as a default value.
        return None

def prompt_exemption_text(exemptionType):
    print(f"You have selected {exemptionType} for your Usage Type.")
    return input("Please provide a one or two sentence justification for the exemption used: ")

def format_multi_select_fields(text):
    new_text = text.split(",")

    new_text = [text.strip() for text in new_text]

    return new_text

def update_code_json(json_file_path):
    # Read the JSON 
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Add date_information and labor hours to the JSON
    data['date'] = get_date_fields()

    # Calculate labor hours
    hours = get_scc_labor_hours()
    if hours:
        data['laborHours'] = hours
    else:
        data['laborHours'] = None

    # Check if usageType is an exemption
    if data['permissions']['usageType'].startswith('exempt'):
        exemption_text = prompt_exemption_text(data['permissions']['usageType'])
        data['permissions']['exemptionText'] = exemption_text
    else:
        del data['permissions']['exemptionText']

    # Format multi-select options
    data['categories'] = format_multi_select_fields(data['categories'][0])
    data['languages'] = format_multi_select_fields(data['languages'][0])
    data['tags'] = format_multi_select_fields(data['tags'][0])

    # Update the JSON 
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent = 2)

def main():
    try:
        # Change to the parent directory
        os.chdir('..')

        # Define the codejson directory to remove
        dir_name = "codejson"

        # Check if codejson directory exists and remove it
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)

        # Get the project name from cookiecutter
        sub_project_dir = "{{cookiecutter.project_name}}"
        codejson_file = "code.json"
        project_root_dir = os.path.abspath('..')

        json_file_path = os.path.join(sub_project_dir, codejson_file)
    
        if os.path.exists(json_file_path):
            # Move code.json file to parent directory
            new_json_path = os.path.join(project_root_dir, codejson_file)
            shutil.move(json_file_path, new_json_path)
        
            # Remove the source directory
            shutil.rmtree(sub_project_dir)

            # Update the json with date and scc information
            update_code_json(new_json_path)
            print("Succesfully generated code.json file!")

        else:
            print(f"Error: {codejson_file} not found in {sub_project_dir}")

    except OSError as error:
        print(f"Error during OS operations: {error}")
    except shutil.Error as error:
        print(f"Error during shutil operations: {error}")

if __name__ == "__main__":
    main()
