import numpy as np
import matplotlib.pyplot as plt

# ----- Basic transformation functions -----

def translate(points, tx, ty):
    t_matrix = np.array([[1, 0, tx],
                         [0, 1, ty],
                         [0, 0, 1]])
    return apply_transform(points, t_matrix)

def scale(points, sx, sy):
    s_matrix = np.array([[sx, 0, 0],
                         [0, sy, 0],
                         [0, 0, 1]])
    return apply_transform(points, s_matrix)

def rotate(points, angle_deg):
    angle_rad = np.radians(angle_deg)
    r_matrix = np.array([[np.cos(angle_rad), -np.sin(angle_rad), 0],
                         [np.sin(angle_rad),  np.cos(angle_rad), 0],
                         [0, 0, 1]])
    return apply_transform(points, r_matrix)

def shear(points, shx=0, shy=0):
    sh_matrix = np.array([[1, shx, 0],
                          [shy, 1, 0],
                          [0, 0, 1]])
    return apply_transform(points, sh_matrix)

def reflect_x(points):
    r_matrix = np.array([[1, 0, 0],
                         [0, -1, 0],
                         [0, 0, 1]])
    return apply_transform(points, r_matrix)

def reflect_y(points):
    r_matrix = np.array([[-1, 0, 0],
                         [0, 1, 0],
                         [0, 0, 1]])
    return apply_transform(points, r_matrix)

# ----- Utility to apply a matrix transformation -----

def apply_transform(points, matrix):
    homogeneous = np.hstack((points, np.ones((points.shape[0], 1))))
    transformed = homogeneous @ matrix.T
    return transformed[:, :2]

# ----- Main Function -----

def plot_transformation(original, transformed, title):
    # Close the shape for plotting
    original = np.vstack([original, original[0]])
    transformed = np.vstack([transformed, transformed[0]])

    plt.figure()
    plt.plot(original[:, 0], original[:, 1], 'bo--', label='Original')
    plt.plot(transformed[:, 0], transformed[:, 1], 'r-', linewidth=2, label='Transformed')
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal')
    plt.show()

# ----- Define a 2D object (square) -----
square = np.array([
    [1, 1],
    [4, 1],
    [4, 4],
    [1, 4]
])

# ----- Apply different transformations -----
translated = translate(square, tx=3, ty=2)
scaled = scale(square, sx=2, sy=0.5)
rotated = rotate(square, angle_deg=45)
sheared = shear(square, shx=1)
reflected_x = reflect_x(square)
reflected_y = reflect_y(square)

# ----- Plot results -----
plot_transformation(square, translated, "Translation (tx=3, ty=2)")
plot_transformation(square, scaled, "Scaling (sx=2, sy=0.5)")
plot_transformation(square, rotated, "Rotation (45°)")
plot_transformation(square, sheared, "Shearing (shx=1)")
plot_transformation(square, reflected_x, "Reflection in X-axis")
plot_transformation(square, reflected_y, "Reflection in Y-axis")
