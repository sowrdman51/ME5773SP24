from mpi4py import MPI
import time

# Start timer
start = time.perf_counter()

# Start the MPI process
comm = MPI.COMM_WORLD

# Determine total number of tasks
size = comm.Get_size()

# Determine id of "this" task
rank = comm.Get_rank()

# Function to integrate
def f(x):
    return x * x

# Integrates f(x) from a to b with n trapezoids
def compute_integral(a, b, n):
    h = (b - a) / n
    x = a
    integral = 0
    for i in range(n):
        integral += ((f(x) + f(x + h)) / 2.0) * h
        x += h
    return integral

# Set parameters (integrate from a to b using n trapezoids)
a = 0
b = 100
n = 100000000
h = (b - a) / n  # size of 1 trapezoid

# --- Master ---
if rank == 0:
    partial = 0.  # partial integral result returned by a Worker
    integral = 0.  # running total of the integral

    # Loop over all tasks waiting for result
    for i in range(1, size):
        partial = comm.recv(source=i)  # receive result from Worker i
        integral += partial  # accumulate integral
        print(f"Master received value {partial} from process {i}")  # report who sent results

    # Integral complete - write results
    finish = time.perf_counter()
    print(f'The integral is {integral}')
    print(f'Finish in {round(finish - start, 3)} seconds')

# --- Worker ---
else:
    # Print notification including process id
    print(f"Process {rank} starts")

    # Determine the number of trapezoids
    n1 = n // (size - 1)

    # Rank determines the integration range
    a1 = a + (rank - 1) * n1 * h
    b1 = a + rank * n1 * h
    partial = compute_integral(a1, b1, n1)

    # Send results back to Master (rank = 0)
    comm.send(partial, dest=0)

