#Created by James Smith with the assistance of Pratik Mitra and Google for Dr. Cano & Dr. Millwater's HPC course

######Initialize 

#Import Libraries

import numpy as np 
import math
import numexpr
import time

#Initialize Variables 
N = 10**9
deltax = 2/N

##### Code 

# For Loop

#Init
F1 = 0
xi = 0
Fxi = 0

Start = time.time()

for i in range(N):
	xi = (2/N)*i - 1
	Fxi = math.sqrt(4-4*(xi**2))
	F1 = F1 + Fxi*deltax

Stop = time.time()

Elapsed = Stop-Start

print(f"{Elapsed:.6f}")
print(f"{F1:.16f}")

#### Vectorized Function 

vec_Start = time.time()

i_vec = np.arange(N)

x_vec = (2*i_vec/N) - 1
F_vec = np.sqrt(4-4*(x_vec**2))
F2 = np.sum(F_vec)

vec_Stop = time.time()
vec_Elapsed = vec_Stop - vec_Start

print(f"{vec_Elapsed:.6f}")

##### Numexpr Evaluations 

NumexprStart = time.time()

i_vec = np.arange(N)

x_vec = numexpr.evaluate('(2 * i_vec / N) - 1')

F_vec = numexpr.evaluate('sqrt(4-(4 * (x_vec**2)))')

F3 = numexpr.evaluate('sum(F_vec)')

NumexprStop = time.time()

NumexprElapsed = NumexprStop - NumexprStart

print(f"{NumexprElapsed:.6f}")
