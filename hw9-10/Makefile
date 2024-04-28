
FC = ifort


# Define the general flags.
FCFLAGS = -O0 -L.

MODSRCS = searchutils.f90
MAINSRC = main_program.f90

all: searchutils.mod  main_program.exe

searchutils.mod: searchutils.f90

	$(FC) -c searchutils.f90 $(FCFLAGS)
	ar rc libsearchutils.a searchutils.o
	ranlib libsearchutils.a


main_program.exe: main_program.f90

	$(FC) $^ -o  $@ $(FCFLAGS) -lsearchutils

.PHONY: clean


clean:
	rm -f *.exe *.o *.mod
