# ====================================================================================
#This file defines a system of Finite Element Equations for a simple spring system.
#
# The purpose of this is to provide a base file that ME5773 students can use to apply
# the concepts of parallelization with Python's multiprocessing module.
#
# Author: Mauricio Aristizabal, PhD
# Last modified: 03/19/2024
#
# =====================================================================================

# =====================================================================================
# Required Libraries
import numpy as np
import time
import multiprocessing as mp

# =====================================================================================


def assemble_worker(params):
    e, Ke, fe, Ndof = params
    Kg_local = np.zeros((Ndof, Ndof))
    fg_local = np.zeros(Ndof)

    for i in range(2):
        for j in range(2):
            Kg_local[e + i, e + j] += Ke[i, j]

    return Kg_local, fg_local


def elasticFEProblem_parallel(Ndof, Ne, k_list, num_workers):
    pool = mp.Pool(num_workers)

    # Split elements among workers
    chunk_size = Ne // num_workers
    chunks = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_workers)]
    if Ne % num_workers != 0:
        chunks[-1] = (chunks[-1][0], Ne)  # Adjust the last chunk size if Ne is not divisible by num_workers

    results = []
    for chunk in chunks:
        results.append(pool.apply_async(elasticFEProblem_chunk, args=(Ndof, chunk[0], chunk[1], k_list)))

    pool.close()
    pool.join()

    Kg = np.zeros((Ndof, Ndof))
    fg = np.zeros(Ndof)
    for result in results:
        Kg_chunk, fg_chunk = result.get()
        Kg += Kg_chunk
        fg += fg_chunk

    return Kg, fg


def elasticFEProblem_chunk(Ndof, start_element, end_element, k_list):
    Kg_chunk = np.zeros((Ndof, Ndof))
    fg_chunk = np.zeros(Ndof)

    for e in range(start_element, end_element):
        Ke, fe = elasticElement(e, k_list)
        Kg_local, fg_local = assemble_worker((e, Ke, fe, Ndof))
        Kg_chunk += Kg_local
        fg_chunk += fg_local

    return Kg_chunk, fg_chunk


def elasticElement(e, k_list):
    Ke = k_list[e] * np.array([[1, -1], [-1, 1]])
    fe = np.array([0.0, 0.0])
    return Ke, fe


if __name__ == '__main__':
    t_start = time.time()

    # Total number of degrees of freedom to be generated
    Ndof = 50000
    Ne = Ndof - 1  # number of elements.
    print('Number of Degrees of freedom: {0}'.format(Ndof))

    # List of elemental stiffness values.
    k_list = [1] * Ne

    num_workers_list = [1, 2, 4, 6, 8, 16, 20, 40]
    times = []

    for num_workers in num_workers_list:
        t_start = time.time()
        Kg, fg = elasticFEProblem_parallel(Ndof, Ne, k_list, num_workers)
        t_end = time.time()
        times.append(t_end - t_start)
        print(f'Time taken with {num_workers} workers: {times[-1]} seconds')
