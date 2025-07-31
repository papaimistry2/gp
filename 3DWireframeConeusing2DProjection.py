import matplotlib.pyplot as plt
import numpy as np

def project_point(x, y, z):
    """Simple orthographic projection with depth adjustment."""
    return x, y - z * 0.5  # simulate 3D depth on 2D plane

def draw_wireframe_cone(center=(200, 200, 0), radius=80, height=120, base_segments=36):
    cx, cy, cz = center
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_title("3D Wireframe Cone (2D Projection)")

    # Generate base circle points
    base_points = []
    for angle in np.linspace(0, 2 * np.pi, base_segments, endpoint=False):
        x = cx + radius * np.cos(angle)
        y = cy + radius * np.sin(angle)
        z = cz
        x2d, y2d = project_point(x, y, z)
        base_points.append((x2d, y2d))

    # Project apex
    apex_3d = (cx, cy, cz + height)
    apex_2d = project_point(*apex_3d)

    # Draw base circle
    for i in range(len(base_points)):
        x1, y1 = base_points[i]
        x2, y2 = base_points[(i + 1) % len(base_points)]
        ax.plot([x1, x2], [y1, y2], 'blue')  # base edge

    # Draw side edges from base to apex
    for bp in base_points:
        ax.plot([bp[0], apex_2d[0]], [bp[1], apex_2d[1]], 'red')  # side edges

    ax.set_aspect('equal')
    ax.grid(True)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis (with depth)")
    plt.xlim(cx - radius*1.5, cx + radius*1.5)
    plt.ylim(cy - radius*1.5, cy + height)
    plt.show()

# Run with default values
draw_wireframe_cone(center=(200, 200, 0), radius=80, height=120, base_segments=36)
