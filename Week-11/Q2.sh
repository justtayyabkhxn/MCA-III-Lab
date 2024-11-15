#!/bin/bash

# Factorial calculation
echo "Enter a number to find its factorial:"
read num

factorial=1

for (( i=1; i<=num; i++ ))
do
    factorial=$((factorial * i))
done

echo "Factorial of $num is $factorial"
