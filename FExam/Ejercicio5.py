import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parámetros
A, B, C = 1.0, 1.0, 1.0
a, b, c = 3.0, 2.0, 5.0
delta, epsilon = np.pi / 2, np.pi / 3
h, t_max = 0.01, 2 * np.pi
steps = int(t_max / h)

# Funciones lambda
x_func = lambda t: A * np.sin(a * t + delta)
y_func = lambda t: B * np.sin(b * t)
z_func = lambda t: C * np.sin(c * t + epsilon)

# Trazo acumulado
x_vals, y_vals, z_vals = [], [], []
t = 0
for _ in range(steps):
    x_vals.append(x_func(t))
    y_vals.append(y_func(t))
    z_vals.append(z_func(t))
    t+=h

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
line, = ax.plot([], [], [], lw=2, color='mediumseagreen')
point, = ax.plot([], [], [], 'o', color='crimson')  # Partícula

ax.set_xlim(-A, A)
ax.set_ylim(-B, B)
ax.set_zlim(-C, C)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Animación Lissajous 3 Dimensiones")

def init():
    line.set_data([], [])
    line.set_3d_properties([])
    point.set_data([], [])
    point.set_3d_properties([])
    return line, point

def update(frame):
    line.set_data(x_vals[:frame], y_vals[:frame])
    line.set_3d_properties(z_vals[:frame])
    point.set_data([x_vals[frame]], [y_vals[frame]])
    point.set_3d_properties([z_vals[frame]])
    return line, point

ani = FuncAnimation(fig, update, frames=steps, init_func=init, interval=10, blit=True, repeat=False)
plt.show()