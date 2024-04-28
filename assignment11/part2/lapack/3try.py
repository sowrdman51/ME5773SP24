import module as md
import numpy as np
import time

def solve_dense_system(N):
    print("N:", N)

    start_time_creation = time.time()

    # Create the matrix K
    K = np.zeros((N, N))
    for i in range(N):
        K[i, i] = 2
        if i > 0:
            K[i, i - 1] = -1
        if i < N - 1:
            K[i, i + 1] = -1
    K[-1, -1] = 1

    # Create the vector f
    f = np.zeros((N, 1))
    f[-1] = 1 / N

    end_time_creation = time.time()
    print("Time elapsed for creating K and f:", format(end_time_creation - start_time_creation, ".9f"), "seconds")

    start_time_solve = time.time()

    # Assume md.mkl_solver or a similar function is used to solve the system
    try:
        u = md.mkl_solver(K, f)
        if u is None:
            raise ValueError("Solver returned None, which indicates a failure.")
    except Exception as e:
        print("An error occurred while solving Ku = f:", e)
        u = None

    end_time_solve = time.time()
    print("Time elapsed for solving Ku = f:", format(end_time_solve - start_time_solve, ".9f"), "seconds")

    if u is not None:
        print("Solution vector u:", u.flatten())
        print("u_N:", u[-1, 0])
    else:
        print("No solution was computed, or an error was encountered.")

# Assuming module is imported correctly
# import module as md
solve_dense_system(10000)

