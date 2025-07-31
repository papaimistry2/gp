import matplotlib.pyplot as plt
import numpy as np

def project_point(x, y, z):
    """Orthographic 2D projection with depth shading."""
    return x, y - z * 0.5  # Simulates 3D depth on Y-axis

def draw_wireframe_sphere(center=(200, 200, 0), radius=100, lat_lines=10, lon_lines=10):
    cx, cy, cz = center
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_title("3D Wireframe Sphere (2D Projection)")

    # Draw latitude lines (horizontal circles)
    for i in range(1, lat_lines):
        theta = np.pi * i / lat_lines
        r = radius * np.sin(theta)
        z = radius * np.cos(theta)

        circle = []
        for j in range(0, 361, 10):
            phi = np.radians(j)
            x = cx + r * np.cos(phi)
            y = cy + r * np.sin(phi)
            xp, yp = project_point(x, y, cz + z)
            circle.append((xp, yp))
        xs, ys = zip(*circle)
        ax.plot(xs, ys, color='blue')

    # Draw longitude lines (vertical half-circles)
    for j in range(0, 360, int(360 / lon_lines)):
        phi = np.radians(j)
        arc = []
        for i in range(0, 181, 5):
            theta = np.radians(i)
            x = cx + radius * np.sin(theta) * np.cos(phi)
            y = cy + radius * np.sin(theta) * np.sin(phi)
            z = radius * np.cos(theta)
            xp, yp = project_point(x, y, cz + z)
            arc.append((xp, yp))
        xs, ys = zip(*arc)
        ax.plot(xs, ys, color='red')

    ax.set_aspect('equal')
    ax.grid(True)
    plt.xlim(cx - radius*1.5, cx + radius*1.5)
    plt.ylim(cy - radius*1.5, cy + radius*1.5)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis (with depth)")
    plt.show()

# Run with default values
draw_wireframe_sphere(center=(200, 200, 0), radius=100, lat_lines=10, lon_lines=12)
