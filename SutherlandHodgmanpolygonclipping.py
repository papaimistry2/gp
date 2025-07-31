import matplotlib.pyplot as plt

# Define the clipping window (rectangle)
clip_window = [(150, 150), (300, 150), (300, 200), (150, 200)]

# Define the polygon to be clipped
polygon = [(100, 150), (200, 250), (350, 150), (250, 100)]

# Helper function to check if a point is inside an edge
def inside(p, edge_start, edge_end):
    x, y = p
    x1, y1 = edge_start
    x2, y2 = edge_end
    return (x2 - x1) * (y - y1) >= (y2 - y1) * (x - x1)

# Helper function to compute intersection point
def intersection(p1, p2, cp1, cp2):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = cp1
    x4, y4 = cp2

    denom = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
    if denom == 0:
        return None  # Lines are parallel
    px = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denom
    py = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denom
    return (px, py)

# Sutherland-Hodgman polygon clipping
def sutherland_hodgman(subject_polygon, clip_polygon):
    output_list = subject_polygon
    cp1 = clip_polygon[-1]

    for cp2 in clip_polygon:
        input_list = output_list
        output_list = []
        if not input_list:
            break
        s = input_list[-1]

        for e in input_list:
            if inside(e, cp1, cp2):
                if not inside(s, cp1, cp2):
                    output_list.append(intersection(s, e, cp1, cp2))
                output_list.append(e)
            elif inside(s, cp1, cp2):
                output_list.append(intersection(s, e, cp1, cp2))
            s = e
        cp1 = cp2
    return output_list

# Perform clipping
clipped_polygon = sutherland_hodgman(polygon, clip_window)

# Plotting
plt.figure(figsize=(8, 6))
plt.title("Sutherland-Hodgman Polygon Clipping")

# Original polygon
polygon_plot = polygon + [polygon[0]]
px, py = zip(*polygon_plot)
plt.plot(px, py, 'b--', label="Original Polygon")

# Clipping window
clip_plot = clip_window + [clip_window[0]]
cx, cy = zip(*clip_plot)
plt.plot(cx, cy, 'k-', label="Clipping Window")

# Clipped polygon
if clipped_polygon:
    clipped_polygon.append(clipped_polygon[0])  # close the polygon
    clx, cly = zip(*clipped_polygon)
    plt.plot(clx, cly, 'g-', linewidth=2, label="Clipped Polygon")

plt.legend()
plt.grid(True)
plt.xlim(50, 400)
plt.ylim(50, 300)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
