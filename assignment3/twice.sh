#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <N>"
    exit 1
fi

# Get the input value N
N=$1

# Sleep for 2N seconds
sleep $((2 * N))

# Output the termination message
echo "Terminated a task that takes $((2 * N)) seconds."

