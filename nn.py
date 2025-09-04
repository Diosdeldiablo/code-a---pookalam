import cv2
import numpy as np

# Canvas settings
size = 800
canvas = np.ones((size, size, 3), dtype=np.uint8) * 30  # dark background
center = (size // 2, size // 2)

# Color palette (BGR)
marigold = (0, 140, 255)
orange = (0, 180, 255)
red = (0, 0, 255)
dark_red = (0, 0, 150)
yellow = (0, 255, 255)
green = (0, 128, 0)
white = (255, 255, 255)
brown = (42, 42, 42)

# Draw concentric filled circles (outer to inner)
cv2.circle(canvas, center, 390, brown, -1)          # background ring
cv2.circle(canvas, center, 370, marigold, -1)       # outermost marigold
cv2.circle(canvas, center, 340, green, -1)          # green ring
cv2.circle(canvas, center, 280, dark_red, -1)       # red pattern background
cv2.circle(canvas, center, 240, green, -1)          # green ring
cv2.circle(canvas, center, 200, orange, -1)         # orange ring
cv2.circle(canvas, center, 170, yellow, -1)         # yellow inner ring
cv2.circle(canvas, center, 140, white, -1)          # flower petal background

# Add central flower circle
cv2.circle(canvas, center, 30, orange, -1)
cv2.circle(canvas, center, 15, yellow, -1)

# Draw petals (red + white combo) using triangles
def draw_petals(n_petals, radius1, radius2, color1, color2):
    angle_step = 360 / n_petals
    for i in range(n_petals):
        angle = np.deg2rad(i * angle_step)
        next_angle = np.deg2rad((i + 1) * angle_step)
        p1 = (int(center[0] + radius1 * np.cos(angle)), int(center[1] + radius1 * np.sin(angle)))
        p2 = (int(center[0] + radius1 * np.cos(next_angle)), int(center[1] + radius1 * np.sin(next_angle)))
        tip = (int(center[0] + radius2 * np.cos((angle + next_angle) / 2)),
               int(center[1] + radius2 * np.sin((angle + next_angle) / 2)))
        petal_color = color1 if i % 2 == 0 else color2
        cv2.fillPoly(canvas, [np.array([p1, tip, p2])], petal_color)

# Inner red-white petals
draw_petals(16, 130, 80, red, white)

# Mid-orange petals
draw_petals(16, 230, 180, orange, orange)

# Outer triangle spikes in red and yellow
def draw_outer_spikes(n, r1, r2, color1, color2):
    for i in range(n):
        theta = 2 * np.pi * i / n
        mid_theta = theta + np.pi / n
        pt1 = (int(center[0] + r1 * np.cos(theta)), int(center[1] + r1 * np.sin(theta)))
        pt2 = (int(center[0] + r1 * np.cos(theta + 2*np.pi / n)), int(center[1] + r1 * np.sin(theta + 2*np.pi / n)))
        tip = (int(center[0] + r2 * np.cos(mid_theta)), int(center[1] + r2 * np.sin(mid_theta)))
        color = color1 if i % 2 == 0 else color2
        cv2.fillPoly(canvas, [np.array([pt1, tip, pt2])], color)

draw_outer_spikes(24, 300, 340, red, yellow)

# Flower circles on outer orange ring
for i in range(12):
    theta = 2 * np.pi * i / 12
    x = int(center[0] + 260 * np.cos(theta))
    y = int(center[1] + 260 * np.sin(theta))
    cv2.circle(canvas, (x, y), 15, orange, -1)
    cv2.circle(canvas, (x, y), 5, yellow, -1)

# Final display
cv2.imshow("Pookalam Recreated", canvas)
cv2.imwrite("pookalam_generated.png", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
