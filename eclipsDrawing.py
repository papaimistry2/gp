import matplotlib.pyplot as plt

def plot_ellipse_points(xc, yc, x, y, points):
    # Using symmetry of ellipse to plot 4 points at once
    points.extend([
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
    ])

def midpoint_ellipse(xc, yc, a, b):
    x = 0
    y = b

    a2 = a * a
    b2 = b * b

    points = []

    # Region 1
    d1 = b2 - a2 * b + 0.25 * a2
    dx = 2 * b2 * x
    dy = 2 * a2 * y
    while dx < dy:
        plot_ellipse_points(xc, yc, x, y, points)
        x += 1
        dx = 2 * b2 * x
        if d1 < 0:
            d1 += b2 * (2 * x + 1)
        else:
            y -= 1
            dy = 2 * a2 * y
            d1 += b2 * (2 * x + 1) - dy

    # Region 2
    d2 = b2 * (x + 0.5)**2 + a2 * (y - 1)**2 - a2 * b2
    while y >= 0:
        plot_ellipse_points(xc, yc, x, y, points)
        y -= 1
        dy = 2 * a2 * y
        if d2 > 0:
            d2 += a2 * (1 - 2 * y)
        else:
            x += 1
            dx = 2 * b2 * x
            d2 += a2 * (1 - 2 * y) + dx

    return points

# --------- Default Input (you can modify here) ---------
xc = 50   # center x
yc = 50   # center y
a = 300    # semi-major axis
b = 200   # semi-minor axis

points = midpoint_ellipse(xc, yc, a, b)
x_vals, y_vals = zip(*points)

# --------- Plot the Ellipse ---------
plt.figure()
plt.plot(x_vals, y_vals, 'bo', markersize=1.5)
plt.title("Midpoint Ellipse Drawing")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
