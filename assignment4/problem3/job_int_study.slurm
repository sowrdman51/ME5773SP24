#!/bin/bash

#SBATCH -J myjob # Job Name
#SBATCH -o myjob.o%j # Name of the stdout output file
#SBATCH -e myjob.e%j # Name of stderr error file
#SBATCH -p compute1 # Queue (partition) name
#SBATCH -N 1 # Total # of nodes (must be 1 for serial)
#SBATCH -n 80 # Total # of mpi tasks (CPUs per task)
#SBATCH -t 00:59:00 # Run time (hh:mm:ss)
#SBATCH --ntasks=1 #Number of Tasks
#SBATCH --mail-type=ALL
#SBATCH --mail-user=james.smith3@my.utsa.edu

module load Anaconda3

conda activate envTeam6

echo " 1 Thread "
export OMP_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
python3 integral.py

echo " 2 Threads "
export OPM_NUM_THREADS=2 
export NUMEXPR_NUM_THREADS=2
python3 integral.py 

echo " 4 Threads "
export OPM_NUM_THREADS=4 
export NUMEXPR_NUM_THREADS=4
python3 integral.py 	

echo " 8 Threads "
export OPM_NUM_THREADS=8
export NUMEXPR_NUM_THREADS=8
python3 integral.py 
