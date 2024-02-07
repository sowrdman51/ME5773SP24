#!/bin/bash

#All credit for this code goes to ChatGPT version 3.5, but the grade will go to James and Pratik

# Function to calculate factorial
factorial() {
    if (( $1 <= 1 )); then
        echo 1
    else
        echo $(( $1 * $(factorial $(( $1 - 1 ))) ))
    fi
}

# Input number
read -p "Enter a number: " N

# Output factorials from 1 to N
for (( i = 1; i <= N; i++ )); do
    echo "Factorial of $i: $(factorial $i)"
done

