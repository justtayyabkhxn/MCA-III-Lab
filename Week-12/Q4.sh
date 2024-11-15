#!/bin/bash

# Pattern search in file
echo "Enter the filename to search in:"
read filename
echo "Enter the pattern to search for:"
read pattern

# Search for the pattern and display results
if grep -q "$pattern" "$filename"; then
    echo "Pattern '$pattern' found in '$filename':"
    grep "$pattern" "$filename"
else
    echo "Pattern '$pattern' not found in '$filename'."
fi
