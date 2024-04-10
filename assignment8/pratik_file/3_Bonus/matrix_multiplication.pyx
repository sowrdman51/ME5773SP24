import numpy as np
cimport numpy as np

# Define the matrix multiplication function
cpdef np.ndarray[np.float64_t, ndim=2] matrix_multiply(np.ndarray[np.float64_t, ndim=2] A,
                                                      np.ndarray[np.float64_t, ndim=2] B):
    cdef int n = A.shape[0]
    cdef int m = A.shape[1]
    cdef int p = B.shape[1]
    cdef np.ndarray[np.float64_t, ndim=2] C = np.zeros((n, p), dtype=np.float64)
    cdef int i, j, k

    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i, j] += A[i, k] * B[k, j]

    return C

