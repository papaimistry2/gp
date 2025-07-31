import matplotlib.pyplot as plt

def plot_circle_points(xc, yc, x, y, points):
    # Use 8-way symmetry to plot points
    points.extend([
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x),
    ])

def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r
    points = []

    plot_circle_points(xc, yc, x, y, points)

    while x <= y:
        x += 1
        if d < 0:
            d += 4 * x + 6
        else:
            y -= 1
            d += 4 * (x - y) + 10
        plot_circle_points(xc, yc, x, y, points)

    return points

# -------- Parameters --------
xc, yc = 150, 150   # Center of circle
radius = 80         # Radius

# -------- Get Circle Points --------
circle_points = bresenham_circle(xc, yc, radius)

# -------- Plot --------
x_vals, y_vals = zip(*circle_points)

plt.figure(figsize=(6, 6))
plt.scatter(x_vals, y_vals, color='blue', s=4)
plt.title("Circle using Bresenham's Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
