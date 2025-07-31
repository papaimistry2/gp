import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ---------- 3D Transformation Matrices ----------
def translate(points, tx, ty, tz):
    T = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])
    return apply_transform(points, T)

def scale(points, sx, sy, sz):
    S = np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])
    return apply_transform(points, S)

def rotate_y(points, angle_deg):
    angle = np.radians(angle_deg)
    R = np.array([
        [np.cos(angle), 0, np.sin(angle), 0],
        [0, 1, 0, 0],
        [-np.sin(angle), 0, np.cos(angle), 0],
        [0, 0, 0, 1]
    ])
    return apply_transform(points, R)

def apply_transform(points, matrix):
    homogeneous = np.hstack((points, np.ones((points.shape[0], 1))))
    transformed = homogeneous @ matrix.T
    return transformed[:, :3]

# ---------- Projection Functions ----------
def parallel_projection(points):
    # Orthographic: simply drop Z
    return points[:, :2]

def perspective_projection(points, d=2):
    # Project 3D to 2D using perspective formula
    projected = []
    for x, y, z in points:
        factor = d / (d + z) if d + z != 0 else 1
        xp = x * factor
        yp = y * factor
        projected.append((xp, yp))
    return np.array(projected)

# ---------- Draw 2D Wireframe ----------
def draw_wireframe(ax, projected_points, title, color='blue'):
    faces = [
        [0, 1, 2, 3],  # Bottom
        [4, 5, 6, 7],  # Top
        [0, 1, 5, 4],  # Front
        [2, 3, 7, 6],  # Back
        [1, 2, 6, 5],  # Right
        [0, 3, 7, 4]   # Left
    ]
    for face in faces:
        x = [projected_points[i][0] for i in face + [face[0]]]
        y = [projected_points[i][1] for i in face + [face[0]]]
        ax.plot(x, y, color=color)

    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    ax.set_aspect('equal')

# ---------- Main ----------
# Define a cube centered at origin (size = 2 units)
cube = np.array([
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1],
])

# Apply transformations
cube = scale(cube, 1, 1.5, 1)
cube = rotate_y(cube, 30)
cube = translate(cube, 2, 1, 3)

# Project using parallel and perspective
parallel = parallel_projection(cube)
perspective = perspective_projection(cube, d=5)

# ---------- Plotting ----------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
draw_wireframe(ax1, parallel, "Parallel Projection", color='green')
draw_wireframe(ax2, perspective, "Perspective Projection", color='purple')
plt.tight_layout()
plt.show()
