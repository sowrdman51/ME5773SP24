#James Smith & Pratik Mitra , HPC Course Spring 2024

import time 
import numpy as np
import h5py

#Matrix A
 
A = np.matrix(np.random.randint(2,10,size=(5000,5000),dtype=int64,order='F'))
B = np.matrix(np.random.randint(100,128,size=(5000,5000),dtype=int8,order='C'))
C = np.matrix(np.ones(5000,5000,dtype=float64) * 0.33, order='C')
D = np.arange(1001, 1101, dtype=int16).reshape((10, 10), order='F'))
E = np.arange(350,350.4,0.1,dtype=float32).reshape((2,2),order='C'))

Start_Time = time.time()
np.savetxt("A.csv", A, delimiter=",", fmt='%d')
End_Time = time.time()
A_Time = End_Time - Start_Time
print(f" A CSV Time is {A_Time:.4f} ")

Start_Time = time.time()
np.savetxt("B.csv", B, delimiter=",", fmt='%d')
End_Time = time.time() 
B_Time = End_Time - Start_Time
print(f" B CSV Time is {B_Time:.4f} ")

Start_Time = time.time()
np.savetxt("C.csv", C, delimiter=",", fmt='%.18e')
End_Time = time.time() 
C_Time = End_Time - Start_Time
print(f" C CSV Time is {C_Time:.4f} ")

Start_Time = time.time()
np.savetxt("D.csv", D, delimiter=",", fmt='%d')
End_Time = time.time() 
D_Time = End_Time - Start_Time
print(f" D CSV Time is {D_Time:.4f} ")

Start_Time = time.time()
np.savetxt("E.csv", E, delimiter=",", fmt='%.7e')
End_Time = time.time() 
E_Time = End_Time - Start_Time
print(f" E CSV Time is {E_Time:.4f} ")

Start_Time = time.time()
np.save("A.npy", A)
End_Time = time.time()
A_Numpy_Time = End_Time - Start_Time
print(f" A Numpy Time is {A_Numpy_Time:.4f} "

Start_Time = time.time()
np.save("B.npy", B)
End_Time = time.time()
B_Numpy_Time = End_Time - Start_Time
print(f" B Numpy Time is {B_Numpy_Time:.4f} "))

Start_Time = time.time()
np.save("C.npy", C)
End_Time = time.time()
C_Numpy_Time = End_Time - Start_Time
print(f" C Numpy Time is {C_Numpy_Time:.4f} "))

Start_Time = time.time()
np.save("D.npy", D)
End_Time = time.time()
D_Numpy_Time = End_Time - Start_Time
print(f" D Numpy Time is {D_Numpy_Time:.4f} "))

Start_Time = time.time()
np.save("E.npy", E)
End_Time = time.time()
E_Numpy_Time = End_Time - Start_Time
print(f" E Numpy Time is {E_Numpy_Time:.4f} "))

Start_Time = time.time()
with h5py.File("matrix_db.hdf5", "w") as file:

	integer_group = file.create_group("integer_group")
	integer_group.attrs["description"] = "A one phrase description of how stinky all of these elements are."

	Database_Time = time.time()
	integer_group.create_dataset("A", data=A, compression="gzip", chunks=(500, 500))
	A_Database_Time = time.time() - Database_Time

	Database_Time =	time.time()
	integer_group.create_dataset("B", data=B, compression="gzip", chunks=(1000, 1000))
        B_Database_Time	= time.time() -	Database_Time

        Database_Time =	time.time()
	integer_group.create_dataset("D", data=D)
        D_Database_Time	= time.time() -	Database_Time

	float_group = file.create_group("float_group")

        Database_Time =	time.time()
	float_group.create_dataset("C", data=C, compression="gzip")
        C_Database_Time	= time.time() -	Database_Time

        Database_Time =	time.time()
	float_group.create_dataset("E", data=E)
        E_Database_Time	= time.time() -	Database_Time

End_Time = time.time()
HDF5_Time = End_Time - Start_Time

print(f" HDF5 Time is {HDF5_Time:.4f} ")
print(f" A Database Time is {A_Database_Time:.4f} ")
print(f" B Database Time is {B_Database_Time:.4f} ")
print(f" D Database Time is {D_Database_Time:.4f} ")
print(f" C Database Time is {C_Database_Time:.4f} ")
print(f" E Database Time is {E_Database_Time:.4f} ")
