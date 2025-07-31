import matplotlib.pyplot as plt
import numpy as np

def flood_fill(image, x, y, target_color, replacement_color):
    # Check bounds
    if x < 0 or x >= image.shape[0] or y < 0 or y >= image.shape[1]:
        return
    # Stop if color doesn't match target
    if image[x][y] != target_color or image[x][y] == replacement_color:
        return

    # Replace color
    image[x][y] = replacement_color

    # Recursively fill in 4 directions (you can also do 8 directions)
    flood_fill(image, x+1, y, target_color, replacement_color)
    flood_fill(image, x-1, y, target_color, replacement_color)
    flood_fill(image, x, y+1, target_color, replacement_color)
    flood_fill(image, x, y-1, target_color, replacement_color)

# ----------- Example grid (0 = background, 1 = boundary) -------------
image = np.array([
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
])

# ------------ Default Seed Point and Fill Color ----------------------
seed_x, seed_y = 3, 3
fill_color = 2
target_color = image[seed_x][seed_y]

# ------------ Perform Flood Fill -------------------------------------
flood_fill(image, seed_x, seed_y, target_color, fill_color)

# ------------ Display Result ------------------------------------------
plt.imshow(image, cmap='Accent')
plt.title("Flood Fill Result")
plt.axis('off')
plt.show()
