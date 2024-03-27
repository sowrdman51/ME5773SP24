#----------------------------------------------------------------#
#
# This code was generate by Pratik, Smith, and ChatGPT.
# Date: 02-27-2024
# 2. Reading information from files
#
#----------------------------------------------------------------#
#
# a. Create a python script file named ‘loadFiles.py’.
# b. Import the libraries time, numpy and h5py.
#
#----------------------------------------------------------------#
#
import time
import numpy as np
import h5py
#
#----------------------------------------------------------------#
# Load CSV files
start_time = time.time()
A_csv = np.loadtxt('A.csv', delimiter=',')
print("Time taken to load A.csv:", time.time() - start_time, "seconds")

start_time = time.time()
B_csv = np.loadtxt('B.csv', delimiter=',')
print("Time taken to load B.csv:", time.time() - start_time, "seconds")

start_time = time.time()
C_csv = np.loadtxt('C.csv', delimiter=',')
print("Time taken to load C.csv:", time.time() - start_time, "seconds")

start_time = time.time()
D_csv = np.loadtxt('D.csv', delimiter=',')
print("Time taken to load D.csv:", time.time() - start_time, "seconds")

start_time = time.time()
E_csv = np.loadtxt('E.csv', delimiter=',')
print("Time taken to load E.csv:", time.time() - start_time, "seconds")

# Load NPY files
start_time = time.time()
A_npy = np.load('A.npy')
print("Time taken to load A.npy:", time.time() - start_time, "seconds")

start_time = time.time()
B_npy = np.load('B.npy')
print("Time taken to load B.npy:", time.time() - start_time, "seconds")

start_time = time.time()
C_npy = np.load('C.npy')
print("Time taken to load C.npy:", time.time() - start_time, "seconds")

start_time = time.time()
D_npy = np.load('D.npy')
print("Time taken to load D.npy:", time.time() - start_time, "seconds")

start_time = time.time()
E_npy = np.load('E.npy')
print("Time taken to load E.npy:", time.time() - start_time, "seconds")

# Load HDF5 file
start_time = time.time()
with h5py.File('matrix_db.hdf5', 'r') as f:
    A_hdf5 = f['integer_group/A'][...]
    print("Time taken to load A from HDF5:", time.time() - start_time, "seconds")

    start_time = time.time()
    B_hdf5 = f['integer_group/B'][...]
    print("Time taken to load B from HDF5:", time.time() - start_time, "seconds")

    start_time = time.time()
    D_hdf5 = f['integer_group/D'][...]
    print("Time taken to load D from HDF5:", time.time() - start_time, "seconds")

    start_time = time.time()
    C_hdf5 = f['float_group/C'][...]
    print("Time taken to load C from HDF5:", time.time() - start_time, "seconds")

    start_time = time.time()
    E_hdf5 = f['float_group/E'][...]
    print("Time taken to load E from HDF5:", time.time() - start_time, "seconds")

