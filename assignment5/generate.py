#James Smith & Pratik Mitra , HPC Course Spring 2024

import time 
import numpy as np
import h5py

#Matrix A
 
A = np.matrix(np.random.randint(2,9,size=(5000,5000),dtype=int64,order='F'))
B = np.matrix(np.random.randint(100,127,size=(5000,5000),dtype=int8,order='C'))
