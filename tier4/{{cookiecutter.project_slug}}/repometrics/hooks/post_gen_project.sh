#!/bin/bash

# Change to the parent directory
cd ..

# Define the repometrics directory to remove
dir_name="repometrics"

# Check if repometrics directory exists and remove it
if [ -d "$dir_name" ]; then
  rm -rf "$dir_name"
fi

project_type="{{cookiecutter.project_type}}"
sub_project_dir="${project_type}"
repometrics_file="code.json"
parent_dir="./"

if [ -f "${sub_project_dir}/${repometrics_file}" ]; then  
  # Move code.json file to parent directory
  mv "${sub_project_dir}/${repometrics_file}" "${parent_dir}"
  
  # Check if the move was successful
  if [ $? -eq 0 ]; then    
    # Remove the source directory
    rm -rf "${sub_project_dir}"
    
    # Check if the deletion was successful
    if [ $? -eq 0 ]; then
      echo "Successfully generated code.json file."
    fi
  fi
fi