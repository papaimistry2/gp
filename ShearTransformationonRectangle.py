import numpy as np
import matplotlib.pyplot as plt

def shear(points, shx=0, shy=0):
    """Apply 2D shear transformation to points."""
    shear_matrix = np.array([
        [1, shx],
        [shy, 1]
    ])
    return points @ shear_matrix.T

def plot_rectangle(original, transformed, title):
    # Close the rectangles for plotting
    original = np.vstack([original, original[0]])
    transformed = np.vstack([transformed, transformed[0]])

    plt.figure()
    plt.plot(original[:, 0], original[:, 1], 'bo--', label='Original')
    plt.plot(transformed[:, 0], transformed[:, 1], 'r-', linewidth=2, label='Sheared')
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.gca().set_aspect('equal')
    plt.legend()
    plt.show()

# ----- Define Rectangle (square) -----
# Rectangle from (1, 1) to (4, 3)
rectangle = np.array([
    [1, 1],
    [4, 1],
    [4, 3],
    [1, 3]
])

# ----- Apply Shear -----
sheared_x = shear(rectangle, shx=1.0, shy=0.0)  # Shear in X direction
sheared_y = shear(rectangle, shx=0.0, shy=0.5)  # Shear in Y direction
sheared_xy = shear(rectangle, shx=1.0, shy=0.5) # Shear in both directions

# ----- Plot -----
plot_rectangle(rectangle, sheared_x, "Shear Transformation (X-axis, shx = 1.0)")
plot_rectangle(rectangle, sheared_y, "Shear Transformation (Y-axis, shy = 0.5)")
plot_rectangle(rectangle, sheared_xy, "Shear Transformation (X & Y-axis)")
