#!/bin/bash

# Directory backup script
echo "Enter the directory to back up:"
read source_dir
echo "Enter the backup destination directory:"
read backup_dir

# Create the backup directory if it doesn't exist
mkdir -p "$backup_dir"

# Copy the directory recursively
cp -r "$source_dir" "$backup_dir"

echo "Backup of '$source_dir' completed in '$backup_dir'."
