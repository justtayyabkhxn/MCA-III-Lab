#!/bin/bash

# User account creation script
echo "Enter the username for the new account:"
read username
echo "Enter the default password for the new account:"
read -s password

# Check if the user already exists
if id "$username" &>/dev/null; then
    echo "User '$username' already exists."
else
    # Create the user and set the password
    sudo useradd -m "$username"
    echo "$username:$password" | sudo chpasswd

    echo "User '$username' has been created successfully."
fi
