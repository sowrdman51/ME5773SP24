import numpy as np
import time
import numba
from numba import jit
from numba import prange

Threads = [1,2,4,8,16,20]
TimeResults = []
IntegralResults = []

for i in range(len(Threads)):

    numba.set_num_threads(Threads[i])

    @jit(nopython=True)
    def myfunct(x):
        """
        Defines the function to be integrated.

        INPUTS:
        - x: double, evaluation point.

        OUTPUTS:
        - double, evaluated function.
    
    """

        return np.sin(x*x)+x/2

    # end function

    @jit(nopython=True,parallel=True)
    def integral_riemann(a,b,N):
        """
        Implements the Riemann integration for the function
        myfunct(x).

        INPUTS:
        - a: double, Lower integration limit.
        - b: double, Upper integration limit.
        - N: Int, Number of integration regions.

        OUTPUTS:
        - double, evaluated integral.
        
        """
        dx = (b-a)/N
        F = 0
        
        for i in prange(N):
            x = a + i*dx
            F += myfunct(x)*dx
        # end for 

        return F

    # end function

    if __name__ == '__main__':

        # If needed, add dummy call to the integral_riemann
        # function here
        integral_riemann(0,2,100)
        # Evaluate the CPU time and integration here.

        t_start = time.time()
        a = 0
        b = 2
        N = 100_000_000 # 10**8 
        F = integral_riemann(a,b,N)
        t_end = time.time()
         
        IntegralResults.append(F)
        TimeResults.append(t_end-t_start)
        print('Threads: ', Threads[i])
        print('Integral {0:f}'.format(F))
        print('CPU time:{0:.6f}s'.format(t_end-t_start))

    # end if
print('Integral Results: ', IntegralResults)
print('CPU Time Results: ', TimeResults)
