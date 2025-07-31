import matplotlib.pyplot as plt

def circle_points_plot(cx, cy, x, y, circle_points):
    circle_points.extend([
        (cx + x, cy + y),
        (cx - x, cy + y),
        (cx + x, cy - y),
        (cx - x, cy - y),
        (cx + y, cy + x),
        (cx - y, cy + x),
        (cx + y, cy - x),
        (cx - y, cy - x),
    ])

def midCircle(cx, cy, r):
    x = 0
    y = r
    d = 1 - r

    circle_points = []
    circle_points_plot(cx, cy, x, y, circle_points)

    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1
        circle_points_plot(cx, cy, x, y, circle_points)

    return circle_points

# Circle input
cx = 5
cy = 5
r = 300

points = midCircle(cx, cy, r)
x_val, y_val = zip(*points)

plt.figure()
plt.plot(x_val, y_val, marker='o', color="green", linestyle='None')
plt.title("Midpoint Circle Drawing")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
