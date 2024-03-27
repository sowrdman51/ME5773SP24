import math
import mpi 

# This code was written by James Smith to perform Gaussian Integration 

# Start the MPI Process
comm = MPI.COMM_WORLD

# Determine the Total Number of Tasks
size = comm.Get_size()

# Determine the rank (ID) of this task
rank = comm.Get_rank()

# Function to integrate
def f(x):
    return x*math.exp(x)

# Function takes input x points and weights w and returns them from -1 to 1 scale
def gauleg(x1, x2, x, w, n):
    #Input x1, x2 (Integration Bounds) 
    # x = an array of integration points 
    # w = an array of the weights
    # n = the number of points (quadrature number) 


    EPS = 3.0e-16
    m = (n + 1) // 2
    xm = 0.50 * (x2 + x1)
    xl = 0.50 * (x2 - x1)
    
    for i in range(1, m + 1):
        z = math.cos(math.pi * (i - 0.25) / (n + 0.50))
        while True:
            p1 = 1.0
            p2 = 0.0
            for j in range(1, n + 1):
                p3 = p2
                p2 = p1
                p1 = ((2.0 * j - 1.0) * z * p2 - (j - 1.0) * p3) / j
            
            pp = n * (z * p1 - p2) / (z * z - 1.0)
            z1 = z
            z = z1 - p1 / pp
            
            if abs(z - z1) > EPS:
                continue
            
            x[i - 1] = xm - xl * z
            x[n - i] = xm + xl * z
            w[i - 1] = 2.0 * xl / ((1.0 - z * z) * pp * pp)
            w[n - i] = w[i - 1]
            break


## --- Master ---
if rank == 0:
    N = list(range(1,21))
    # Compute the Quadrature
    # Send the Quadrature to the Workers 
    # Collect the results from each worker
    # Compute the table 
    sum = 0.0

## --- Worker --- 
else:

    sum = 0.0
    for i in range (0,n)
        sum = sum + w[i]*f(x[i])
    print(f"sum = ",{sum})
:
