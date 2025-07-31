import matplotlib.pyplot as plt
import numpy as np

def project_point(x, y, z):
    """Simple orthographic projection with depth effect."""
    return x, y - z * 0.5  # simulate depth on Y-axis

def draw_wireframe_pyramid(center=(200, 200, 0), base_side=120, height=150):
    cx, cy, cz = center
    half = base_side / 2

    # Define base vertices (square)
    base_vertices_3d = [
        (cx - half, cy - half, cz),  # Bottom-left
        (cx + half, cy - half, cz),  # Bottom-right
        (cx + half, cy + half, cz),  # Top-right
        (cx - half, cy + half, cz),  # Top-left
    ]

    # Define apex (top point)
    apex_3d = (cx, cy, cz + height)

    # Project all points to 2D
    base_2d = [project_point(x, y, z) for (x, y, z) in base_vertices_3d]
    apex_2d = project_point(*apex_3d)

    # Plotting
    plt.figure(figsize=(6, 6))
    plt.title("3D Wireframe Pyramid (2D Projection)")

    # Draw base square
    for i in range(4):
        x1, y1 = base_2d[i]
        x2, y2 = base_2d[(i + 1) % 4]
        plt.plot([x1, x2], [y1, y2], 'blue')

    # Draw sides (apex connections)
    for x, y in base_2d:
        plt.plot([x, apex_2d[0]], [y, apex_2d[1]], 'red')

    # Display
    plt.xlabel("X")
    plt.ylabel("Y (with depth)")
    plt.grid(True)
    plt.gca().set_aspect('equal')
    plt.xlim(cx - base_side, cx + base_side)
    plt.ylim(cy - base_side, cy + height)
    plt.show()

# Run the function with default input
draw_wireframe_pyramid(center=(200, 200, 0), base_side=120, height=150)
