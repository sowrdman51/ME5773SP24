#!/bin/bash
#SBATCH --partition=compute1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=80
#SBATCH --time=5:00
#SBATCH --output=output_%j.txt

# Load Anaconda3 module
module load anaconda3

# Activate the envTeamX environment
conda activate envTeam6

# Set the environment variable MKL_NUM_THREADS to 1
export MKL_NUM_THREADS=1

# Define the size N
N=10000

# Run the Python script with different values of OMP_NUM_THREADS
for threads in 1 2 4 8 16 20 40; do
    export OMP_NUM_THREADS=$threads
    python linalg.py
done

