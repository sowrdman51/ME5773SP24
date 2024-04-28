import module as md 
import numpy as np
import time

N = 10000
print("N:", N)

start_time_creation = time.time()

K = np.zeros((N, N))
for i in range(N):
    K[i, i] = 2
    if i > 0:
        K[i, i - 1] = -1
    if i < N - 1:
        K[i, i + 1] = -1

K[-1, -1] = 1

f = np.zeros(N)
f[-1] = 1 / N
f = f.reshape(-1, 1)  # Reshape f to be a two-dimensional array

end_time_creation = time.time()
print("Time elapsed for creating K and f:", format(end_time_creation - start_time_creation, ".9f"), "seconds")

start_time_solve = time.time()

try:
    u = md.mkl_solver(K, f)
except ValueError as e:
    print("Failed to solve the system:", e)
    u = None

end_time_solve = time.time()
print("Time elapsed for solving Ku = f:", format(end_time_solve - start_time_solve, ".9f"), "seconds")

if u is not None:
    print("Solution vector u:", u.flatten())  # Flatten u for easier viewing if it's 2D
    print("u_N:", u[-1, 0])  # Access the last element appropriately if u is 2D
else:
    print("No solution computed.")

