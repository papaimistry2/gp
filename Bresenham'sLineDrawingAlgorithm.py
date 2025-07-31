import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dy <= dx:
        err = 2 * dy - dx
        for _ in range(dx + 1):
            points.append((x, y))
            if err >= 0:
                y += sy
                err -= 2 * dx
            err += 2 * dy
            x += sx
    else:
        err = 2 * dx - dy
        for _ in range(dy + 1):
            points.append((x, y))
            if err >= 0:
                x += sx
                err -= 2 * dy
            err += 2 * dx
            y += sy

    return points

# ----------- Example Inputs -----------
x1, y1 = 10, 10
x2, y2 = 100, 50

# ----------- Get Line Points -----------
line_points = bresenham_line(x1, y1, x2, y2)

# ----------- Plotting -----------
x_vals, y_vals = zip(*line_points)

plt.figure(figsize=(6, 6))
plt.plot(x_vals, y_vals, 'ko', markersize=4)  # 'ko' = black circle marker
plt.title("Bresenham's Line Drawing Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.gca().set_aspect('equal')
plt.show()
