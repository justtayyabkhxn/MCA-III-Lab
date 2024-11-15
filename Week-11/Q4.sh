#!/bin/bash

# Defining a simple function
greet_user() {
    echo "Hello, $1! Welcome to the shell scripting tutorial."
}

# Calling the function with an argument
echo "Enter your name:"
read name
greet_user "$name"
