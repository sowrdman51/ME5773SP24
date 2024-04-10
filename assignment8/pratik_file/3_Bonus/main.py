import numpy as np
from matrix_multiplication import matrix_multiply
import time

# Create random matrices
n = 1000
m = 1000
p = 1000
A = np.random.rand(n, m)
B = np.random.rand(m, p)

# Evaluate the performance
num_iterations = 100
start_time = time.time()
for _ in range(num_iterations):
    C_cython = matrix_multiply(A, B)
end_time = time.time()
cython_time = (end_time - start_time) / num_iterations

start_time = time.time()
for _ in range(num_iterations):
    C_numpy = np.dot(A, B)
end_time = time.time()
numpy_time = (end_time - start_time) / num_iterations

print(f"Cython execution time: {cython_time:.6f} seconds")
print(f"NumPy execution time: {numpy_time:.6f} seconds")

