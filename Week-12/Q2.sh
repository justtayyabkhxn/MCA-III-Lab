#!/bin/bash

# Disk usage monitoring script
threshold=80  # Set threshold percentage

# Get disk usage percentage of the root partition
usage=$(df / | grep / | awk '{ print $5 }' | sed 's/%//g')

if [ "$usage" -gt "$threshold" ]; then
    echo "Warning: Disk usage has exceeded ${threshold}%! Current usage is ${usage}%."
else
    echo "Disk usage is within the limit. Current usage: ${usage}%."
fi
