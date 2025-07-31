import matplotlib.pyplot as plt

# Liang-Barsky Algorithm
def liang_barsky(xmin, xmax, ymin, ymax, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

    u1 = 0.0
    u2 = 1.0

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None  # Line is parallel and outside the window
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                u1 = max(u1, t)
            else:
                u2 = min(u2, t)

    if u1 > u2:
        return None  # Line is outside
    else:
        x1_clip = x1 + u1 * dx
        y1_clip = y1 + u1 * dy
        x2_clip = x1 + u2 * dx
        y2_clip = y1 + u2 * dy
        return x1_clip, y1_clip, x2_clip, y2_clip

# ------------------------
# Default Input
# ------------------------

# Clipping window coordinates
xmin, ymin = 50, 50
xmax, ymax = 100, 100

# Line endpoints
x1, y1 = 20, 80
x2, y2 = 120, 60

# Perform clipping
clipped = liang_barsky(xmin, xmax, ymin, ymax, x1, y1, x2, y2)

# ------------------------
# Plotting
# ------------------------

plt.figure()
ax = plt.gca()

# Clipping window
rect = plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                     edgecolor='black', facecolor='none', linewidth=1.5)
ax.add_patch(rect)

# Original line
plt.plot([x1, x2], [y1, y2], 'r--', label='Original Line')

# Clipped line
if clipped:
    x1c, y1c, x2c, y2c = clipped
    plt.plot([x1c, x2c], [y1c, y2c], 'g-', linewidth=2.5, label='Clipped Line')
else:
    print("Line lies completely outside the clipping window.")

plt.title("Liang-Barsky Line Clipping")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.xlim(0, 150)
plt.ylim(0, 150)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
