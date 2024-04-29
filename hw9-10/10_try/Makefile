FC = ifort
FCFLAGS = -O2 -L. -qopenmp  

MODSRCS = searchutils.f90
MAINSRC = main_program.f90

all: searchutils.mod main_program.exe

searchutils.mod: $(MODSRCS)
	$(FC) -c $(MODSRCS) $(FCFLAGS)  
	ar rc libsearchutils.a searchutils.o  # Use a tab here as well
	ranlib libsearchutils.a  # And a tab here

main_program.exe: $(MAINSRC) searchutils.mod
	$(FC) $(MAINSRC) -o $@ $(FCFLAGS) -lsearchutils  # Tab before this command

.PHONY: clean

clean:
	rm -f *.exe *.o *.mod *.a  # Tab before this command
