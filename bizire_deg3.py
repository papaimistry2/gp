import matplotlib.pyplot as plt

def bezier_cubic(p0, p1, p2, p3, num_points=100):
    curve_x = []
    curve_y = []

    for t in [i / num_points for i in range(num_points + 1)]:
        x = (1 - t)**3 * p0[0] + 3 * (1 - t)**2 * t * p1[0] + 3 * (1 - t) * t**2 * p2[0] + t**3 * p3[0]
        y = (1 - t)**3 * p0[1] + 3 * (1 - t)**2 * t * p1[1] + 3 * (1 - t) * t**2 * p2[1] + t**3 * p3[1]
        curve_x.append(x)
        curve_y.append(y)

    return curve_x, curve_y

# -------- Input 4 control points --------
print("Enter 4 control points for the cubic Bézier curve:")
p0 = tuple(map(float, input("P0 (x y): ").split()))
p1 = tuple(map(float, input("P1 (x y): ").split()))
p2 = tuple(map(float, input("P2 (x y): ").split()))
p3 = tuple(map(float, input("P3 (x y): ").split()))

# -------- Generate Bézier Curve --------
x_vals, y_vals = bezier_cubic(p0, p1, p2, p3)

# -------- Plotting --------
plt.figure()
# Bézier curve
plt.plot(x_vals, y_vals, 'b-', label='Bezier Curve')
# Control points and polygon
control_x, control_y = zip(p0, p1, p2, p3)
plt.plot(control_x, control_y, 'ro--', label='Control Polygon')
plt.title("Cubic Bézier Curve")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()


## 00 13 33 40