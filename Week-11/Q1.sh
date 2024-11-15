#!/bin/bash

# File existence check
echo "Enter the file name (with path if not in the current directory):"
read filename

if [ -e "$filename" ]; then
    echo "File '$filename' exists."
else
    echo "File '$filename' does not exist."
fi
