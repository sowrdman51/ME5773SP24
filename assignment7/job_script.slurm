#!/bin/bash
#----------------------------------------------------
# Sample Slurm job script for Arc nodes 
#SBATCH -J myjob # Job Name
#SBATCH -o myjob.o%j # Name of the stdout output file
#SBATCH -e myjob.e%j # Name of stderr error file
#SBATCH -p compute1 # Queue (partition) name
#SBATCH -N 1 # Total # of nodes (must be 1 for serial)
#SBATCH -n 21 # Total # of mpi tasks (should be 1 for serial)
#SBATCH -t 00:05:00 # Run time (hh:mm:ss)
#SBATCH --mail-type=ALL
#SBATCH --mail-user=pratik.mitra@my.utsa.edu  

# Load module
module load openmpi
module swap openmpi intel/oneapi/2021.2.0
#module load libctl/4.5.0
#module load gcc
#module swap intel/oneapi gcc/11.2.0

cd /work/gug303/sources/ME5773SP24/assignment7

#mpirun -np 21 Homework7.py 
#mpiexec -n 21 python Homework7.py
mpiexec -n 21 python part1.py

