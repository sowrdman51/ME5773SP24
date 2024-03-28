import math
from mpi4py import MPI
import numpy as np
import warnings

# This code was written by James Smith to perform Gaussian Integration 

# Suppress Leggauss warning about dividing by Zero
warnings.filterwarnings("ignore", category=RuntimeWarning)

# Start the MPI Process
comm = MPI.COMM_WORLD

# Determine the Total Number of Tasks
size = comm.Get_size()

# Determine the rank (ID) of this task
rank = comm.Get_rank()

# Function to integrate
def f(x):
    return x*math.exp(x)


N = list(range(1,21))


## --- Master ---
if rank == 0:
    
    # Generate Quadrature Number 
    N = list(range(1,21))
    
    # Integration Bounds 
    x1 = -1
    x2 = 1
    
    # Weights(w) and Integration Points(x)
    w=[]
    x=[]
    for i in N:
        x_temp,w_temp  = np.polynomial.legendre.leggauss(i)
        w.append(w_temp)
        x.append(x_temp)

    ### Compute the Quadrature ###

    # Send Data to Workers
    comm.bcast(N, root=0)
    comm.bcast(x, root=0)
    comm.bcast(w, root=0)
 
    # Collect the results from each worker
    int_results=[]
    for i in range(1,size):
         temp=comm.recv(source=i)
         int_results.append(temp)
    # Compute the table 
    print(int_results)

## --- Worker --- 
else:
    print(f"Process {rank} starts") #Displays worker ID

    # Receive Data
    N_local = comm.bcast(None, root=0)
    x_local = comm.bcast(None, root=0)
    w_local = comm.bcast(None, root=0) 

    # Takes 3 arrays and isolates data list specific to this worker
    data_local=[N_local[rank-1],x_local[rank-1],w_local[rank-1]]

    # Takes Data and separates list into 3 arrays for weights, x, and N
    w_worker = data_local[2]
    x_worker = data_local[1]
    N_worker = data_local[0]

    # Performs Integration
    sum = 0.0
    for i in range (0,N_worker):
        sum = sum + w_worker[i]*f(x_worker[i])
    result=sum

    # Send Results to Main
    comm.send(result, dest=0)



