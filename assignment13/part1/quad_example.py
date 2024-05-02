import numpy as np
import pyvista as pv
# Create two quad elements, as follows:
#
# Coordinates:                
# y ^                   
#   |                   
# 2 *----*----*         
#   |    |    |         
#   |    |    |         
#   *----*----*--->     
#   0    1    2   x     
#

# This will have a total of 6 vertices (points), with the coordinates as follows:
# y ^                   
#   |                   
#  (3)--(4)--(5)         
#   |    |    |         
#   |    |    |         
#  (0)--(1)--(2)-->     
#                 x     
#
points = np.array([[0, 0, 0],
                   [1, 0, 0],
                   [2, 0, 0],
                   [0, 2, 0],
                   [1, 2, 0],
                   [2, 2, 0]], dtype=np.float64 )

npoints = points.shape[0]

# Each quad element is formed by 4 nodes, with the following order
# (see Figure 2 under 
# https://docs.vtk.org/en/latest/design_documents/VTKFileFormats.html#legacy-file-examples )
#
# Quad element:                  
#  (3)--(2)
#   |    |
#   |    |
#  (0)--(1)
# 
# The connectivity of a cell is determined by supplying the indices of the points
# that form the correspoinding quad (in the order described above). 
#
# For example, the first quad is formed by the points 0, 1, 4 and 3. 
# y ^                   
#   |                   
#  (3)--(4)--(5)         
#   |    |    |         
#   |    |    |         
#  (0)--(1)--(2)-->     
#                 x 
#
# The  second quad is formed by the nodes 1, 2, 4 and 5. 
# 
# The cells array is a 1d-array that contains the connectivity of the cells:
# First, the number of indices that corresponds to this type is supplied, and then
# the cell's connectivity:
# [nInd, id_0, id_1, ...,id_(nInd-1) ]
#
cells = np.array([4, 0, 1, 4, 3, # First  quad
                  4, 1, 2, 5, 4  # Second quad.
                  ])
# Number of cells
ncells = 2

# All cells are type quad, thus we only define for each
# cell, its correspondign type:
cell_type = pv.CellType.QUAD * np.ones(ncells,dtype=np.int8)

# The grid is created using all the cells
grid = pv.UnstructuredGrid(cells, cell_type, points)

# Adding Point data (e.g temperature field, velocity field)
# For scalar fields:
# --> grid[ point_data_name ] = f1
#          -> point_data_name: any string that defines your field.
#          -> f1 is a 1d array of size equal to the number of points.
#
# To assign the values corresponding to the distance from the 
# origin, use the following
#  
x = points[:,0]
y = points[:,1]
grid['Distance'] = (x**2 + y**2)**0.5

# Vector fields can also be added for point data. 
# --> grid[ point_data_name ] = f2
#          -> point_data_name: any string that defines your field.
#          -> f2 is a 2d array of shape(npoints, ndim) with the vector field data.
#             where ndim is the number of dimensions of the vector field.
#
# For this example, the following is the generated field
#
grid['Locations'] = points**2

grid.save("quadExample.vtk")

grid.plot(show_edges=True)
