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
    tasks = list(range(1, 21))
    results = [None] * 20
    workers = size - 1
    active_workers = 0

    while tasks or active_workers:
        if tasks and active_workers < workers:
            n = tasks.pop(0)
            x = [0.0] * n
            w = [0.0] * n
            gauleg(-1.0, 1.0, x, w, n)
            comm.send((n, x, w), dest=active_workers + 1, tag=1)
            active_workers += 1
        else:
            n, result = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG)
            active_workers -= 1
            results[n-1] = result

            if tasks:
                n_next = tasks.pop(0)
                x_next = [0.0] * n_next
                w_next = [0.0] * n_next
                gauleg(-1.0, 1.0, x_next, w_next, n_next)
                comm.send((n_next, x_next, w_next), dest=MPI.ANY_SOURCE, tag=1)
                active_workers += 1

    # Terminate workers
    for i in range(1, size):
        comm.send(None, dest=i, tag=2)

    # Save results to part2.txt
    with open('part2.txt', 'w') as f:
        for n, result in enumerate(results, start=1):
            exact = 2 / math.exp(1)
            error = abs(result - exact) / exact * 100
            f.write(f"{n} {result} {error}\n")

else:
    while True:
        task = comm.recv(source=0, tag=MPI.ANY_TAG)
        if task is None:
            break
        n, x, w = task
        integral = sum(w[i] * f(x[i]) for i in range(len(x)))
        comm.send((n, integral), dest=0, tag=1)

