#!/bin/bash

FIND=$1
REPLACE=$2
FILES_INPUT=$3

# Split the comma-separated string into an array
IFS=',' read -ra FILES <<< "$FILES_INPUT"

for i in "${FILES[@]}"; do
    # Remove any accidental spaces (like " README.md")
    FILE=$(echo $i | xargs)
    
    echo "Processing file: $FILE"
    
    # Check if the file exists before trying to update it
    if [ -f "$FILE" ]; then
        # This is where your actual replacement command (likely 'sed') lives
        # Make sure to use "$FILE" (the variable) here!
        sed -i "s/$FIND/$REPLACE/g" "$FILE"
    else
        echo "Warning: $FILE not found, skipping."
    fi
done
