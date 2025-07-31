import matplotlib.pyplot as plt

# Region codes
INSIDE = 0  # 0000
LEFT   = 1  # 0001
RIGHT  = 2  # 0010
BOTTOM = 4  # 0100
TOP    = 8  # 1000

# Function to compute region code
def compute_code(x, y, xmin, xmax, ymin, ymax):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

# Cohen-Sutherland Line Clipping Function
def cohen_sutherland_clip(x1, y1, x2, y2, xmin, xmax, ymin, ymax):
    code1 = compute_code(x1, y1, xmin, xmax, ymin, ymax)
    code2 = compute_code(x2, y2, xmin, xmax, ymin, ymax)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            # Trivially accepted
            accept = True
            break
        elif code1 & code2 != 0:
            # Trivially rejected
            break
        else:
            # Clipping needed
            code_out = code1 if code1 != 0 else code2
            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, xmin, xmax, ymin, ymax)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2, xmin, xmax, ymin, ymax)

    if accept:
        return x1, y1, x2, y2
    else:
        return None  # Line rejected

# ------------ Example Input ------------
# Clipping window
xmin, ymin = 100, 100
xmax, ymax = 300, 300

# Line endpoints
x1, y1 = 50, 250
x2, y2 = 350, 150

# ------------ Perform Clipping ------------
clipped_line = cohen_sutherland_clip(x1, y1, x2, y2, xmin, xmax, ymin, ymax)

# ------------ Plotting ------------
plt.figure(figsize=(6, 6))
plt.title("Cohen-Sutherland Line Clipping")

# Draw clipping rectangle
plt.plot([xmin, xmax, xmax, xmin, xmin],
         [ymin, ymin, ymax, ymax, ymin], 'k-', label="Clipping Window")

# Draw original line
plt.plot([x1, x2], [y1, y2], 'r--', label="Original Line")

# Draw clipped line (if any)
if clipped_line:
    cx1, cy1, cx2, cy2 = clipped_line
    plt.plot([cx1, cx2], [cy1, cy2], 'g-', linewidth=2, label="Clipped Line")
else:
    print("Line is outside and rejected.")

# Display
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.xlim(0, 400)
plt.ylim(0, 400)
plt.show()
