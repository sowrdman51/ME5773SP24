#!/bin/bash
#SBATCH --partition=compute1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=80
#SBATCH --time=5:00  # 5 minutes
#SBATCH --output=output_%j.txt

# Load required modules
module load anaconda3

# Define the size N
N=10000

# Loop over different values of OMP_NUM_THREADS
for threads in 1 2 4 8 16 20 40; do
    export OMP_NUM_THREADS=$threads

    # Run the Python script
    python linalg.py
done

