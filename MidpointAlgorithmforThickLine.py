import matplotlib.pyplot as plt

def midpoint_thick_line(x1, y1, x2, y2, thickness=3):
    points = []

    dx = x2 - x1
    dy = y2 - y1

    steep = abs(dy) > abs(dx)

    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = y2 - y1
    d = dy * 2 - dx
    y_step = 1 if dy >= 0 else -1
    y = y1

    for x in range(x1, x2 + 1):
        # Draw vertical thickness if steep, horizontal if not
        for t in range(-thickness // 2, thickness // 2 + 1):
            if steep:
                points.append((y + t, x))
            else:
                points.append((x, y + t))

        if d > 0:
            y += y_step
            d -= 2 * dx
        d += 2 * dy

    return points

# Default input
x1, y1 = 50, 50
x2, y2 = 200, 120
thickness = 7  # can be 1, 3, 5, 7...

# Get thick line points
line_points = midpoint_thick_line(x1, y1, x2, y2, thickness)

# Plotting
plt.figure(figsize=(6, 6))
for x, y in line_points:
    plt.plot(x, y, 'ko', markersize=2)  # black pixels
plt.title(f"Thick Line (Midpoint Algorithm) - Thickness {thickness}")
plt.gca().set_aspect('equal')
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(0, 250)
plt.ylim(0, 250)
plt.show()
import matplotlib.pyplot as plt

def midpoint_thick_line(x1, y1, x2, y2, thickness=3):
    points = []

    dx = x2 - x1
    dy = y2 - y1

    steep = abs(dy) > abs(dx)

    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = y2 - y1
    d = dy * 2 - dx
    y_step = 1 if dy >= 0 else -1
    y = y1

    for x in range(x1, x2 + 1):
        # Draw vertical thickness if steep, horizontal if not
        for t in range(-thickness // 2, thickness // 2 + 1):
            if steep:
                points.append((y + t, x))
            else:
                points.append((x, y + t))

        if d > 0:
            y += y_step
            d -= 2 * dx
        d += 2 * dy

    return points

# Default input
x1, y1 = 50, 50
x2, y2 = 200, 120
thickness = 7  # can be 1, 3, 5, 7...

# Get thick line points
line_points = midpoint_thick_line(x1, y1, x2, y2, thickness)

# Plotting
plt.figure(figsize=(6, 6))
for x, y in line_points:
    plt.plot(x, y, 'ko', markersize=2)  # black pixels
plt.title(f"Thick Line (Midpoint Algorithm) - Thickness {thickness}")
plt.gca().set_aspect('equal')
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(0, 250)
plt.ylim(0, 250)
plt.show()
