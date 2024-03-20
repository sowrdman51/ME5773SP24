# =====================================================================================
# This file defines a system of Finite Element Equations for a simple spring system.
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
import scipy as sp # Install scipy using "conda install scipy"
import time
# =====================================================================================


def assemble(e,Ke,fe,Kg,fg):
	"""
	DESCRIPTION: Assemble an element's system matrix and rhs into a global 
	             system of equations for 1D Finite Element problem.
	             
	             This assembly function only supports linear elastic problems
	             of springs assembled in the form:
				
	        x-^^-x-^^-x-^^-x...x-^^-x-^^-x-^^-x

	
	INPUTS:
		-e: (integer) Element index.
		-Ke: (Float array, Shape: (2,2) ) Elemental stiffness matrix.
		-fe: (Float array, Shape: (2,) )  Elemental force vector.
		-Kg: (Float array, Shape: (2,2) ) Global stiffness matrix.
		-fg: (Float array, Shape: (2,) )  Global force vector.
	
	OUTPUTS:
		Nothing, global inputs are modified.

	"""
	
	for i in range(2):
		for j in range(2):
			Kg[e+i,e+j] = Kg[e+i,e+j] + Ke[i,j]
		# end for 
	# end for 

# end function


def elasticElement(e,k_list):
	"""
	DESCRIPTION: Assemble an element's system of equation into a global 
	             system of equations for 1D Finite Element problem.
	             
	             This assembly function only supports linear elastic problems
	             of springs assembled in the form:
				
	        x-^^-x-^^-x-^^-x...x-^^-x-^^-x-^^-x
	        
	
	INPUTS:
		-e: (integer) Element index.
		-k_list: (List of floats, len: Ne ) Element stiffness values. Ne: Number of elements.
		
	OUTPUTS:
		- Ke: Elemental stifness matrix
		- fe: Elemental force vector.

	"""
	
	Ke = k_list[e] * np.array([[ 1,-1],
		                       [-1, 1]])

	fe = np.array([0.0,
		           0.0])
	
	return Ke,fe

# end function


def elasticFEProblem( Ndof, Ne1, Ne2, k_list ):
	"""
	DESCRIPTION: This function assembles the global stiffness matrix for a sequence 
	             of spring elements, aranged in the following manner:
				
	        x-^^-x-^^-x-^^-x...x-^^-x-^^-x-^^-x

	INPUTS:
		-Ndof: Total number of degrees of freedom.
		-k_list: (List of floats, len: Ne ) Element stiffness values. Ne: Number of elements.
		-Ne1: Starting element to be evaluated.
        -Ne2: Final element to be evaluated.
	
	OUTPUTS:
		-Kg: (Float array, Shape: (2,2) ) Global stiffness matrix.
        -fg: (Float array, Shape: (2,) )  Global force vector.

	"""
	# Create the global matrix.
	Kg = np.zeros((Ndof,Ndof))
	fg = np.zeros((Ndof,))

	Ne = len(k_list) # Number of elements.
	Nu = Ne+1        # Number of nodes.

	for e in range( Ne1, Ne2):
		
		# Compute element stiffness matrix and load vector.
		Ke, fe = elasticElement(e,k_list)

		# Assemble the elemental values into the global components.
		assemble(e,Ke,fe,Kg,fg)
		
	# end for

	return Kg, fg

# end function


if __name__ == '__main__':

	t_start = time.time()
	
	# Total number of degrees of freedom to be generated
	Ndof = 50000
	Ne   = Ndof-1 # number of elements.

	print('Number of Degrees of freedom: {0}'.format(Ndof))
	

	# List of elemental stiffness values.
	#
	# This should be created such that each element 
	# may have a different stiffness value.

	k_list  = [1]*Ne
	
	
	t_start = time.time()
	
	# Create the global system
	Kg, fg = elasticFEProblem( Ndof, 0, Ne, k_list ) 

	t_end   = time.time()
	
	# print(Kg)

	print('Total time to assemble:',t_end-t_start)

# end if __main__