import math
import time
from mpi4py import MPI
import numpy as np

def f(x):
    return x * math.exp(x)

def gauleg(x1, x2, x, w, n):
    EPS = 3.0e-16
    m = (n + 1) // 2
    xm = 0.5 * (x2 + x1)
    xl = 0.5 * (x2 - x1)
    
    for i in range(1, m + 1):
        z = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        while True:
            p1, p2 = 1.0, 0.0
            for j in range(1, n + 1):
                p3 = p2
                p2 = p1
                p1 = ((2.0 * j - 1.0) * z * p2 - (j - 1.0) * p3) / j
            
            pp = n * (z * p1 - p2) / (z * z - 1.0)
            z1 = z
            z = z1 - p1 / pp
            if abs(z - z1) <= EPS:
                break
        
        x[i - 1] = xm - xl * z
        x[n - i] = xm + xl * z
        w[i - 1] = 2.0 * xl / ((1.0 - z * z) * pp * pp)
        w[n - i] = w[i - 1]

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    results = []
    for n in range(1, 21):
        x = [0.0] * n
        w = [0.0] * n
        gauleg(-1.0, 1.0, x, w, n)
        
        start_time = time.time()
        comm.send((x, w), dest=n, tag=n)
        
        result = comm.recv(source=n, tag=n)
        end_time = time.time()
        
        exact = 2 / math.exp(1)
        error = abs(result - exact) / exact * 100
        run_time = end_time - start_time
        results.append((n, result, error, run_time))

    # Print the table header
    print(f"{'Quadrature no.':<15}{'Integration Result':<20}{'Percent Error':<15}{'Run time (s)':<15}")
    print("-" * 65)

    # Print each row of results
    for n, result, error, run_time in results:
        print(f"{n:<15}{result:<20.10f}{error:<15.2f}{run_time:<15.6f}")

    # Save results to part1.txt
    with open('part1.txt', 'w') as f:
        for n, result, error, run_time in results:
            f.write(f"{n} {result} {error} {run_time}\n")

else:
    x, w = comm.recv(source=0, tag=rank)
    integral = sum(w[i] * f(x[i]) for i in range(len(x)))
    comm.send(integral, dest=0, tag=rank)

