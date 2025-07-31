import matplotlib.pyplot as plt

# Define cube vertices (3D coordinates)
cube_vertices = [
    [-1, -1, -1],
    [-1, -1,  1],
    [-1,  1, -1],
    [-1,  1,  1],
    [ 1, -1, -1],
    [ 1, -1,  1],
    [ 1,  1, -1],
    [ 1,  1,  1],
]

# Perspective projection function
def project_point(x, y, z, d=5):
    # Simple perspective projection onto 2D plane
    factor = d / (d + z)
    x_proj = x * factor
    y_proj = y * factor
    return x_proj, y_proj

# Define edges of the cube (by index of vertices)
edges = [
    (0, 1), (0, 2), (0, 4),
    (1, 3), (1, 5),
    (2, 3), (2, 6),
    (3, 7),
    (4, 5), (4, 6),
    (5, 7),
    (6, 7)
]

# Project all 3D points to 2D
projected_points = [project_point(x, y, z) for x, y, z in cube_vertices]

# Separate X and Y for plotting
x_vals, y_vals = zip(*projected_points)

# Plot
plt.figure(figsize=(6,6))
for edge in edges:
    x0, y0 = projected_points[edge[0]]
    x1, y1 = projected_points[edge[1]]
    plt.plot([x0, x1], [y0, y1], 'bo-')  # blue line with dots

plt.title("3D Wireframe Cube (2D Projection)")
plt.axis('equal')
plt.grid(True)
plt.show()
