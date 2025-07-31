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

def draw_rectangle(x1, y1, x2, y2):
    # Corner coordinates
    top_left = (x1, y1)
    top_right = (x2, y1)
    bottom_right = (x2, y2)
    bottom_left = (x1, y2)

    # Collect points for all four sides
    rectangle_points = []
    rectangle_points += bresenham_line(*top_left, *top_right)
    rectangle_points += bresenham_line(*top_right, *bottom_right)
    rectangle_points += bresenham_line(*bottom_right, *bottom_left)
    rectangle_points += bresenham_line(*bottom_left, *top_left)

    return rectangle_points

# -------- Input rectangle coordinates --------
x1, y1 = 50, 50       # Top-left
x2, y2 = 200, 150     # Bottom-right

# -------- Get rectangle points --------
rect_points = draw_rectangle(x1, y1, x2, y2)

# -------- Plot --------
x_vals, y_vals = zip(*rect_points)

plt.figure(figsize=(6, 6))
plt.scatter(x_vals, y_vals, c='green', s=5)
plt.title("Rectangle using Bresenham's Line Drawing Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.gca().set_aspect('equal')
plt.show()
