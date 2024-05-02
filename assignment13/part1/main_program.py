import numpy as np
import pyvista as pv

# Define the points in a 3x3 grid
points = np.array([
    [-2, 0, 0],   # Point 0
    [0, 0, 0],    # Point 1
    [2, 0, 0],    # Point 2
    [-2, 2, 0],   # Point 3
    [0, 2, 0],    # Point 4
    [2, 2, 0],    # Point 5
    [-2, 4, 0],   # Point 6
    [0, 4, 0],    # Point 7
    [2, 4, 0]     # Point 8
], dtype=np.float64)

# Define the connectivity for 4 quad cells
cells = np.array([
    4, 0, 1, 4, 3,  # Quad 1
    4, 1, 2, 5, 4,  # Quad 2
    4, 3, 4, 7, 6,  # Quad 3
    4, 4, 5, 8, 7   # Quad 4
], dtype=np.int32)

# Define the cell types as quads
ncells = 4
cell_type = np.array([pv.CellType.QUAD] * ncells, dtype=np.int8)

# Create the unstructured grid
grid = pv.UnstructuredGrid(cells, cell_type, points)

# Define the scalar field 'dcenter' as the distance to the center point (0, 2)
center = np.array([0, 2, 0])
grid['dcenter'] = np.linalg.norm(points - center, axis=1)

# Define the vector field 'velocity'
x, y = points[:, 0], points[:, 1]
velocity = np.column_stack([y, -x, np.zeros_like(x)])
grid['velocity'] = velocity

# Save the grid to a VTK file
grid.save("quad_grid.vtk")

# Plot the grid with edges shown
grid.plot(show_edges=True)

