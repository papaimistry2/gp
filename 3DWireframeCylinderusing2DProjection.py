import matplotlib.pyplot as plt
import numpy as np

def project_point(x, y, z):
    """Simple orthographic projection with a depth effect."""
    return x, y - z * 0.5  # simulate Z-depth effect in Y-axis

def draw_wireframe_cylinder(center=(200, 200, 0), radius=80, height=150, segments=36):
    cx, cy, cz = center

    # Generate base and top circle points
    base_points = []
    top_points = []

    for angle in np.linspace(0, 2 * np.pi, segments, endpoint=False):
        x = cx + radius * np.cos(angle)
        y = cy + radius * np.sin(angle)
        z_base = cz
        z_top = cz + height

        base_points.append(project_point(x, y, z_base))
        top_points.append(project_point(x, y, z_top))

    # Plotting
    plt.figure(figsize=(6, 6))
    plt.title("3D Wireframe Cylinder (2D Projection)")

    # Draw base circle
    for i in range(len(base_points)):
        x1, y1 = base_points[i]
        x2, y2 = base_points[(i + 1) % len(base_points)]
        plt.plot([x1, x2], [y1, y2], 'blue')

    # Draw top circle
    for i in range(len(top_points)):
        x1, y1 = top_points[i]
        x2, y2 = top_points[(i + 1) % len(top_points)]
        plt.plot([x1, x2], [y1, y2], 'blue')

    # Draw vertical edges
    for b, t in zip(base_points, top_points):
        plt.plot([b[0], t[0]], [b[1], t[1]], 'red')

    # Final plot settings
    plt.xlabel("X")
    plt.ylabel("Y (with depth)")
    plt.grid(True)
    plt.gca().set_aspect('equal')
    plt.xlim(cx - radius * 1.5, cx + radius * 1.5)
    plt.ylim(cy - radius * 1.5, cy + height)
    plt.show()

# Run the function with default values
draw_wireframe_cylinder(center=(200, 200, 0), radius=80, height=150, segments=36)
