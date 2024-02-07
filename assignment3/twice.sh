#!/bin/bash

# All credit for this code goes to ChatGPT 3.5. The grade will go to Pratik and James! :)

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

