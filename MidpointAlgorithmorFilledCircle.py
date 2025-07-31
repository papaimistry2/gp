import matplotlib.pyplot as plt

def plot_filled_circle_points(xc, yc, x, y, pixels):
    # For each horizontal pair, fill between symmetrical points
    for dy in [-y, y]:
        for dx in range(-x, x + 1):
            pixels.append((xc + dx, yc + dy))

    for dx in [-x, x]:
        for dy in range(-y + 1, y):
            pixels.append((xc + dx, yc + dy))

def midpoint_filled_circle(xc, yc, r):
    x = 0
    y = r
    d = 1 - r

    pixels = []
    plot_filled_circle_points(xc, yc, x, y, pixels)

    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1
        plot_filled_circle_points(xc, yc, x, y, pixels)

    return pixels

# -------- Parameters --------
xc, yc = 150, 150   # Center
radius = 60         # Radius

# -------- Get filled points --------
filled_pixels = midpoint_filled_circle(xc, yc, radius)

# -------- Plot --------
x_vals, y_vals = zip(*filled_pixels)

plt.figure(figsize=(6, 6))
plt.scatter(x_vals, y_vals, color='purple', s=5)
plt.title("Filled Circle using Midpoint Algorithm")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
