import numpy as np
import searchUtilsTeam06 as search
import time

x = np.linspace(-10, 10, 10_000_000, dtype=np.float64)

Start = time.time()

resultLinearFortran = search.searchutils.linearsearch(x,x[-2])
TimeLinear = time.time() - Start
resultBinaryFortran = search.searchutils.binarysearch(x,x[-2])
TimeBinary = time.time() - Start
resultNumpySearchSorted = np.searchsorted(x,x[-2])
TimeNumpySorted = time.time() - Start
resultNumpySearchNative = np.where(x == x[-2])
TimeNumpyNative = time.time() - Start

print("The Linear Fortran CPU Time is: ",TimeLinear)
print("The Binary Fortran CPU Time is: ",TimeBinary)
print("The Numpy Sorted CPU Time is: ",TimeNumpySorted)
print("The Numpy Native CPU Time is: ",TimeNumpyNative)

