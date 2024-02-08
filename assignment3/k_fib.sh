#!/bin/bash

# A partial credit gose to ChatGPT 3.5 and full grade goes to P & J!!!!

# Function to calculate K-Fibonacci series 
k_fibonacci() {
    N=$1
    K=$2

    # Initialize array to store K-Fibonacci series
    fib[0]=0
    fib[1]=1

    # Calculate K-Fibonacci series
    for ((i=2; i<N; i++)); do
        fib[$i]=0
        for ((j=1; j<=K && i-j>=0; j++)); do
            fib[$i]=$((fib[$i] + fib[$((i-j))]))
        done
    done

    # Output K-Fibonacci series
    for ((i=0; i<N; i++)); do
        echo -n "${fib[$i]} "
    done
    echo
}

# Check if correct number of arguments are provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <N>"
    exit 1
fi

# Read input N from command line
N=$1

# Check if N is a positive integer
if ! [[ "$N" =~ ^[1-9][0-9]*$ ]]; then
    echo "N must be a positive integer."
    exit 1
fi

# Call k_fibonacci function with N=5 and K=2 by default
k_fibonacci $N 2

