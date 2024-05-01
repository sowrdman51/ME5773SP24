import cupy as cp
import time as time
import numpy as np


defI_kernel = cp.RawKernel(r'''
extern "C" __global__
void defI( double* I_p, int ncols, int nrows) {
    /*
    This function defines an identity matrix Eye (in row-major format)
    with all elements in the diagonal as 1 and all other elements 0. 

    INPUTS: 
    - I_p: Pointer to the memory in Eye.
    - nrows: Number of rows of the matrix
    - ncols: Number of columns of the matrix
    */
    
    // FYI: This is a comment
    
    /* and this is also a comment */

    // Define global indices of the threads along each direction.
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    int j = blockDim.y * blockIdx.y + threadIdx.y;   
    
    // Check that the i, j location lies within the matrix dimensions.
    if ( ( i < nrows) && ( j < ncols ) ){
        
        // Define the contiguous global index of the matrix.
        // i.e the index to access a single data point from the main 
        // pointer in K 
        // Consider the global indices as follows
        //
        // I_local = [[(0,0),(0,1),(0,2)],  // i,j indices for K.
        //            [(1,0),(1,1),(1,2)],
        //            [(2,0),(2,1),(2,2)]]
        //
        // I_g = [[ 0, 1, 2],  // global contiguous indices for K.
        //        [ 3, 4, 5],
        //        [ 6, 7, 8]]
        //
        // we use long long type (int64) because the 
        // integer value gets very large.
        //

        long long g_indx = i * ncols + j ;    
        
        if (i==j){

            // Diagonal element
            I_p[g_indx] = 1.0;
        
        } else {
        
            I_p[g_indx] = 0.0;
        
        }
        
    }

}
''', 'defI')

# Create the inputs. Must be defined with corresponding 
# types as in the raw kernel.

t_start = time.time()
N = 10

I = cp.empty((N,N),dtype = cp.float64)

# Define the execution grid.
block_dim = 16
grid_dim  = N//block_dim+1 # Guarantee we send at least 1 grid.

# We are required to create the holder of the result.
# print("-")
defI_kernel((grid_dim,grid_dim,1), (block_dim,block_dim,1), ( I, I.shape[0],I.shape[1]))  # grid, block and arguments

t_end = time.time()

# Check the values in the matrix:
print(I)

print(f"Time spent creating the matrix: {t_end-t_start:.6f} s")
