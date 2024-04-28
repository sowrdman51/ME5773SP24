
all: cython

cython: module.pyx setup.py
	# This comand runs python to execute the cython file.
	CC=icc LINKCC=icc python setup.py build_ext --inplace

clean:
	rm -rf *.so module.html module.c build/