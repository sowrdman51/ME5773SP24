import numpy as np
import time
from multiprocessing import Pool

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

    Kg = np.zeros((Ndof, Ndof))
    fg = np.zeros(Ndof)

    for e in range(Ne1, Ne2):
        Ke, fe = elasticElement(e, k_list)
        assemble(e, Ke, fe, Kg, fg)

    return Kg, fg

if __name__ == '__main__':
    t_start = time.time()

    Ndof = 50000
    Ne = Ndof - 1

    print('Number of Degrees of freedom: {0}'.format(Ndof))

    k_list = [1] * Ne

    pool_size = 40  # Set the pool size

    pool = Pool(processes=pool_size)

    chunk_size = 50000  # Define the chunk size for domain decomposition
    chunks = [(i, k_list, i * chunk_size, min((i + 1) * chunk_size, Ne)) for i in range(Ne // chunk_size + 1)]

    results = pool.map(assemble_worker, chunks)

    Kg = np.zeros((Ndof, Ndof))
    fg = np.zeros(Ndof)
    for Kg_local, fg_local in results:
        for i in range(2):
            for j in range(2):
                Kg[i:i + 2, i:i + 2] += Kg_local
            fg[i:i + 2] += fg_local

    t_end = time.time()

    print('Total time to assemble:', t_end - t_start)

