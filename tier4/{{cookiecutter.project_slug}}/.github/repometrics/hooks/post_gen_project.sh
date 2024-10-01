#!/bin/bash

# Change to the parent directory
cd ..

# Define the repometrics directory to remove
dir_name="repometrics"

# Check if repometrics directory exists and remove it
if [ -d "$dir_name" ]; then
  rm -rf "$dir_name"
fi

project_name="{{cookiecutter.project_name}}"
sub_project_dir="${project_name}"
repometrics_file="code.json"
project_root_dir="../"

if [ -f "${sub_project_dir}/${repometrics_file}" ]; then  
  # Move code.json file to parent directory
  mv "${sub_project_dir}/${repometrics_file}" "${project_root_dir}"
  
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