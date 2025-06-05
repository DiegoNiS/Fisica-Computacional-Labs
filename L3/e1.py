import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches

r1 = 1.5
r2 = 1.5
b = 2
c = 3
center1 = (-b, c)
center2 = (b, -c)
n_points = 100
theta = np.linspace(0, 2 * np.pi, n_points)
x1 = center1[0] + r1 * np.cos(theta)
y1 = center1[1] + r1 * np.sin(theta)
x2 = center2[0] + r2 * np.cos(theta)
y2 = center2[1] + r2 * np.sin(theta)

def ax(x, y):
    x1 = x - center1[0]
    y1 = y - center1[1]
    r1 = math.sqrt(x1**2 + y1**2)
    x2 = x - center2[0]
    y2 = y - center2[1]
    r2 = math.sqrt(x2**2 + y2**2)
    cos_theta1 = x1 / r1
    cos_theta2 = x2 / r2
    return -1 / r1**2 * cos_theta1 - 1 / r2**2 * cos_theta2
def ay(x, y):
    x1 = x - center1[0]
    y1 = y - center1[1]
    r1 = math.sqrt(x1**2 + y1**2)
    x2 = x - center2[0]
    y2 = y - center2[1]
    r2 = math.sqrt(x2**2 + y2**2)
    sin_theta1 = y1 / r1
    sin_theta2 = y2 / r2
    return -1 / r1**2 * sin_theta1 - 1 / r2**2 * sin_theta2

def simulate_trajectory(x, y, vx, vy, dt, t_max):
    positions = []
    for t in np.arange(0, t_max, dt):
        positions.append((x, y))
        ax_val = ax(x, y)
        ay_val = ay(x, y)
        vx += ax_val * dt
        vy += ay_val * dt
        x += vx * dt
        y += vy * dt
        if esta_dentro_circulo(x, y, center1, r1) or esta_dentro_circulo2(x, y, center2, r2):
            break
    return positions

def esta_dentro_circulo(x, y, center1, radius):
    return (x - center1[0])**2 + (y - center1[1])**2 < radius**2
def esta_dentro_circulo2(x, y, center2, radius):
    return (x - center2[0])**2 + (y - center2[1])**2 < radius**2

dt = 0.01
t_max = 200

x = 1
y = 5
vx = 0.3
vy = -0.3
positions = simulate_trajectory(x, y, vx, vy, dt, t_max)
x = 3.5
y = -2
vx = -0.38
vy = 0.8
positions2 = simulate_trajectory(x, y, vx, vy, dt, t_max)
x = -3
y = 1
vx = 0.5
vy = -0.4
positions3 = simulate_trajectory(x, y, vx, vy, dt, t_max)
x = 4
y = 4
vx = -0.1
vy = -0.1
positions4 = simulate_trajectory(x, y, vx, vy, dt, t_max)

x = 1
y = 5
vx = 0.3
vy = -0.3
positions = simulate_trajectory(x, y, vx, vy, dt, t_max)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.plot(x1, y1, color='blue', label='C1')
ax.plot(x2, y2, color='red', label='C2')
ax.plot(x, y, color='green', label='nose que')
for pos in positions:
    ax.plot(pos[0], pos[1], 'go', markersize=1)

for pos in positions2:
    ax.plot(pos[0], pos[1], 'ro', markersize=1)

for pos in positions3:
    ax.plot(pos[0], pos[1], 'bo', markersize=1)

for pos in positions4:
    ax.plot(pos[0], pos[1], 'yo', markersize=1)

ax.add_patch(patches.Circle(center1, r1, color='blue', alpha=0.5))
ax.add_patch(patches.Circle(center2, r2, color='red', alpha=0.5))
plt.show()