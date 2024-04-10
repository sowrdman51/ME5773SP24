import numpy as np
import time
import multiprocessing as mp
import os
import scipy as sp
import sys
import scipy.sparse as spr

def assemble_worker(args):
    e, k_list, Ne1, Ne2 = args
    Ke, fe = elasticElement(e, k_list)
    Kg_local = np.zeros((2, 2))
    fg_local = np.zeros(2)
    assemble(e, Ke, fe, Kg_local, fg_local)
    return Kg_local, fg_local

def assemble(e, Ke, fe, Kg, fg):
    """
    DESCRIPTION: Assemble an element's system matrix and rhs into a global
                 system of equations for 1D Finite Element problem.
    """

    for i in range(2):
        for j in range(2):
            #Kg[e+i, e+j] += Ke[i, j]
            Kg[e+i,e+j] = Kg[e+i,e+j] + Ke[i,j]

def elasticElement(e, k_list):
    """
    DESCRIPTION: Assemble an element's system of equation into a global
                 system of equations for 1D Finite Element problem.
    """

    Ke = k_list[e] * np.array([[1, -1], [-1, 1]])
    fe = np.array([0.0, 0.0])

    return Ke, fe

def elasticFEProblem(Ndof, Ne1, Ne2, k_list):
    """
    DESCRIPTION: This function assembles the global stiffness matrix for a sequence
                 of spring elements, arranged in the following manner:
                 x-^^-x-^^-x-^^-x...x-^^-x-^^-x-^^-x
    """

    Kg = spr.csc_array((Ndof, Ndof)) # Generates Sparse Array for Kg
    fg = np.zeros(Ndof)

    for e in range(Ne1, Ne2):
        Ke, fe = elasticElement(e, k_list)
        assemble(e, Ke, fe, Kg, fg)

    Kg =spr.csr_array(Kg) # Compresses Sparse Array for Kg 

    return Kg, fg

def TestJames(bingus):
    return elasticFEProblem(*bingus)

if __name__ == '__main__':

    t_start = time.time()

    Ndof = 50000
    Ne = Ndof - 1

    print('Number of Degrees of freedom: {0}'.format(Ndof))

    k_list = [1] * Ne

    pool_size = 2  # Set the pool size


    pool = mp.Pool(processes=pool_size) # Creates Pool of size = pool_size

    chunk_size = Ne + pool_size//pool_size  # Define the chunk size for domain decomposition

    chunks = [(Ndof, i*chunk_size, min((i+1)*chunk_size, Ne),k_list) for i in range(pool_size)]
    
    #results = assemble_worker(Ndof)
    #print(len(chunks))
    results = pool.map(TestJames, chunks)

    Kg = spr.csr_array((Ndof, Ndof))
    fg = np.zeros(Ndof)

    #for Kg_local, fg_local in results:
    #    for i in range(2):
    #        for j in range(2):
    #            Kg[i:i + 2, i:i + 2] += Kg_local
    #        fg[i:i + 2] += fg_local

    for Kg_local, fg_local in results:
        # Update the global sparse matrix Kg directly
        for i in range(Kg_local.shape[0]):
            for j in range(Kg_local.shape[1]):
                Kg[i, j] += Kg_local[i, j]

        # Update the global array fg
        fg += fg_local
    print('does anything work')
    pool.close()
    print('testing holy hell')
    t_end = time.time()
    print(time.time())

    print('Total time to assemble:', t_end - t_start)

