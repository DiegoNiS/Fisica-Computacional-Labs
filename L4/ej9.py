import numpy as np
import matplotlib.pyplot as plt

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
    

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')

# Sin fuerza externa
ax.plot(pt, x_sin, v_sin, label='Sin fuerza externa', color='blue')

# Con fuerza externa
ax.plot(pt, x_con, v_con, label='Con fuerza externa', color='red', alpha=0.7)

ax.set_xlabel('Tiempo (t)')
ax.set_ylabel('Posición (x)')
ax.set_zlabel('Velocidad (v)')
ax.set_title('Gráfico 3D: v, x, t')
ax.legend()
plt.show()