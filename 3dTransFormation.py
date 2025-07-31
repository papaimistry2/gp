import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import math

# ------------ Transformation Functions ------------

def translate(points, tx, ty, tz):
    translation_matrix = np.array([tx, ty, tz])
    return points + translation_matrix

def scale(points, sx, sy, sz):
    scaling_matrix = np.array([sx, sy, sz])
    return points * scaling_matrix

def rotate_x(points, angle_deg):
    angle_rad = math.radians(angle_deg)
    rx = np.array([
        [1, 0, 0],
        [0, math.cos(angle_rad), -math.sin(angle_rad)],
        [0, math.sin(angle_rad), math.cos(angle_rad)]
    ])
    return points @ rx.T

def rotate_y(points, angle_deg):
    angle_rad = math.radians(angle_deg)
    ry = np.array([
        [math.cos(angle_rad), 0, math.sin(angle_rad)],
        [0, 1, 0],
        [-math.sin(angle_rad), 0, math.cos(angle_rad)]
    ])
    return points @ ry.T

def rotate_z(points, angle_deg):
    angle_rad = math.radians(angle_deg)
    rz = np.array([
        [math.cos(angle_rad), -math.sin(angle_rad), 0],
        [math.sin(angle_rad), math.cos(angle_rad), 0],
        [0, 0, 1]
    ])
    return points @ rz.T

# ------------ Visualization Function ------------

def draw_object(points, title, ax, color='skyblue'):
    faces = [
        [points[0], points[1], points[2], points[3]],
        [points[4], points[5], points[6], points[7]],
        [points[0], points[1], points[5], points[4]],
        [points[2], points[3], points[7], points[6]],
        [points[1], points[2], points[6], points[5]],
        [points[4], points[7], points[3], points[0]],
    ]
    ax.add_collection3d(Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='black', alpha=0.7))
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_box_aspect([1,1,1])

# ------------ Define Object (Cube) ------------

cube = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1],
])

# ------------ Transformation Parameters ------------

# Translation
tx, ty, tz = 2, 1, 0

# Scaling
sx, sy, sz = 1.5, 1, 2

# Rotation (degrees)
rx, ry, rz = 30, 45, 60

# ------------ Apply Transformations ------------

transformed = translate(cube, tx, ty, tz)
transformed = scale(transformed, sx, sy, sz)
transformed = rotate_x(transformed, rx)
transformed = rotate_y(transformed, ry)
transformed = rotate_z(transformed, rz)

# ------------ Plot Original and Transformed Object ------------

fig = plt.figure(figsize=(12, 6))

# Original Cube
ax1 = fig.add_subplot(121, projection='3d')
draw_object(cube, "Original Cube", ax1)

# Transformed Cube
ax2 = fig.add_subplot(122, projection='3d')
draw_object(transformed, "Transformed Cube", ax2, color='lightgreen')

plt.tight_layout()
plt.show()
