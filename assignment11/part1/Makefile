
all: f2py

f2py: searchutils.f90
	# This comand runs f2py to compile a fortran function/subroutine into a python module.
	# -L, -l, -I flags used as in compiler commands.
	
	python3.11 -m numpy.f2py --fcompiler=intelem -c searchutils.f90 -m searchUtilsTeam06 
