#!/bin/bash
# A partial credit gose to ChatGPT 3.5(10%) and full grade goes to P & J!!!!
#----------------------------------------------------
# Sample Slurm job script for Arc nodes
#SBATCH -J myjob # Job Name
#SBATCH -o myjob.o%j # Name of the stdout output file
#SBATCH -e myjob.e%j # Name of stderr error file
#SBATCH -p compute1 # Queue (partition) name
#SBATCH -N 1 # Total # of nodes (must be 1 for serial)
#SBATCH -n 40 # Total # of mpi tasks (should be 1 for serial)i
#SBATCH -t 00:59:00 # Run time (hh:mm:ss)
#SBATCH --ntasks=2 #Number of Tasks
#SBATCH --mail-type=ALL
#SBATCH --mail-user=pratik.mitra@my.utsa.edu

# Load necessary modules (if needed)
# module load ...

# Execute six instances of twice.sh with different inputs
# Each instance runs in the background
srun ./twice.sh 5 &
srun ./twice.sh 2 &
srun ./twice.sh 7 &
srun ./twice.sh 6 &
srun ./twice.sh 1 &
srun ./twice.sh 3 &

# Wait for all background processes to finish
wait

# Print execution time in seconds
echo "All tasks have finished. Execution time: $SECONDS seconds."

