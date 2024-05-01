import cupy as cp
import time as time
import numpy as np


defK_kernel = cp.RawKernel(r'''
extern "C" __global__
void defK( double* K, int ncols, int nrows) {
    
    /*
    This function defines an identity matrix K (in row-major format)
    with all elements in the diagonal as 4 and all elements next to 
    the diagonal as 2. The last element of the diagonal set to 2. 
    All other elements are set to zero.

    INPUTS: 
    - K: Pointer to the memory in K.
    - nrows: Number of rows of the matrix
    - ncols: Number of columns of the matrix
    */

    // Define global indices of the threads along each direction.
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    int j = blockDim.y * blockIdx.y + threadIdx.y;   
    
    // Check that the i, j location lies within the matrix dimensions.
    if ( ( i < nrows) && ( j < ncols ) ){
        
        long long g_indx = i * ncols + j ;    
        
        if (i==j){
            
            K[g_indx] = 4.0;

            if (i == nrows-1 && j == ncols-1 ) {

            K[g_indx] = 2.0;
            
            }
        } else if (i==j+1 || i==j-1) {

            //Near-Diagonal Element
            K[g_indx] = -2.0;
        
        }
        else {

        //All other elements
        K[g_indx] = 0.0;
        }
        
    }

}
''', 'defK')

# Create the inputs. Must be defined with corresponding 
# types as in the raw kernel.

t_start = time.time()
N = 30000
print(f"N is :",N)

K = cp.empty((N,N),dtype = cp.float64)

# Define the execution grid.
block_dim = 16
grid_dim  = N//block_dim+1 # Guarantee we send at least 1 grid.

# We are required to create the holder of the result.
# print("-")
defK_kernel((grid_dim,grid_dim,1), (block_dim,block_dim,1), ( K, K.shape[0],K.shape[1]))  # grid, block and arguments

t_end = time.time()

# Check the values in the matrix:
#print(K)

print(f"Time spent creating the matrix: {t_end-t_start:.6f} s")

f = cp.empty((N,1),dtype = cp.float64)
f[N-1] = 1/N

print(f"Time spent creating f vector: {time.time() - t_end:.6f} s")

u = cp.linalg.solve(K,f)

print(f"Last value of u is : ", u[-1])

print(f"Total Time: {time.time() - t_start:.6f} s")

# NUMPY COMPARISON STUFF YAY!
t_Numpy = time.time()

K_Numpy = np.zeros((N,N))
f_Numpy = np.zeros((N,1))
f_Numpy[-1] = 1/N

for i in range(N):
    for j in range(N):
        if i == j:
            K_Numpy[i][j] = 4.0
            if i == N-1 and j == N-1:
                K_Numpy[i][j] = 2
        elif i == j+1 or i == j-1:
            K_Numpy[i][j] = -2.0


u_Numpy = np.linalg.solve(K_Numpy,f_Numpy)

print(f"The last value for the Numpy solution vector is : ", u_Numpy[-1])
print(f"Total Time (Numpy): {time.time() - t_Numpy:.6f} s")



