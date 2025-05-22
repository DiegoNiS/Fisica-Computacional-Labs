import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parámetros
k = 0.1
m = 0.2
c = 0.05
F_v = 0.01
omega = 0.3
h = 0.01
tfin = 100  # tiempo suficiente para ver el comportamiento

# Condiciones iniciales
x0 = -1
v0 = 1

# Listas para ambos casos
pt = np.arange(0, tfin + h, h)

# Sin fuerza externa
x_sin = [x0]
v_sin = [v0]

# Con fuerza externa
x_con = [x0]
v_con = [v0]

# Simulación sin y con fuerza externa
for i in range(len(pt)-1):
    t = pt[i]
    a_1 = -(c * v_sin[-1] + k * x_sin[-1]) / m
    v_new = v_sin[-1] + h * a_1
    x_new = x_sin[-1] + h * v_sin[-1]
    v_sin.append(v_new)
    x_sin.append(x_new)
    t = pt[i]
    a_2 = (F_v * np.cos(omega * t) - c * v_con[-1] - k * x_con[-1]) / m
    v_new = v_con[-1] + h * a_2
    x_new = x_con[-1] + h * v_con[-1]
    v_con.append(v_new)
    x_con.append(x_new)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(np.min(pt), np.max(pt))
ax.set_ylim(min(min(x_sin), min(x_con)), max(max(x_sin), max(x_con)))
ax.set_zlim(min(min(v_sin), min(v_con)), max(max(v_sin), max(v_con)))

ax.set_xlabel('Tiempo (t)')
ax.set_ylabel('Posición (x)')
ax.set_zlabel('Velocidad (v)')
ax.set_title('Animación 3D: v, x, t')

line_sin, = ax.plot([], [], [], color='blue', label='Sin fuerza externa')
line_con, = ax.plot([], [], [], color='red', label='Con fuerza externa', alpha=0.7)
ax.legend()

def init():
    line_sin.set_data([], [])
    line_sin.set_3d_properties([])
    line_con.set_data([], [])
    line_con.set_3d_properties([])
    return line_sin, line_con

def update(frame):
    line_sin.set_data(pt[:frame], x_sin[:frame])
    line_sin.set_3d_properties(v_sin[:frame])
    
    line_con.set_data(pt[:frame], x_con[:frame])
    line_con.set_3d_properties(v_con[:frame])
    return line_sin, line_con

ani = FuncAnimation(fig, update, frames=len(pt), init_func=init, blit=True, interval=1)

plt.show()