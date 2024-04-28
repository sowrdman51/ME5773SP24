import module as md
import numpy as np
import time

def solve_dense_system(N):
    print("N:", N)

    # Start measuring time for creating matrix K and vector f
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
    f = np.zeros(N)
    f[-1] = 1 / N
    f = f.reshape(-1, 1)  # Correctly reshape f to (N, 1)

    # End measuring time for creating matrix K and vector f
    end_time_creation = time.time()

    # Print the time elapsed for creating matrix K and vector f
    print("Time elapsed for creating K and f:", format(end_time_creation - start_time_creation, ".9f"), "seconds")

    # Start measuring time for solving Ku = f
    start_time_solve = time.time()

    # Solve the system using numpy.linalg.solve
    #u = np.linalg.solve(K, f)
    u = md.mkl_solver(K, f)
   
    # End measuring time for solving Ku = f
    end_time_solve = time.time()
    print("Time elapsed for solving Ku = f:", format(end_time_solve - start_time_solve, ".9f"), "seconds")

    # Print the solution vector u
    print("Solution vector u:", u.flatten())
    print("u_N:", u[-1, 0])

solve_dense_system(10000)

