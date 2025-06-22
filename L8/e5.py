import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- PARTE 1: Superficies con meshgrid ---
x_vals = np.linspace(-3, 4, 100)
y_vals = np.linspace(-3, 2, 100)
X, Y = np.meshgrid(x_vals, y_vals)

Z_top = 4 - Y**2
Z_bottom = Y**2 + 2

# --- PARTE 2: Monte Carlo para puntos dentro ---
m = 10000
ax, bx = -1, 2
ay, by = -1, 1
az, bz = 2, 4

x_mc = ax + (bx - ax) * np.random.rand(m)
y_mc = ay + (by - ay) * np.random.rand(m)
z_mc = az + (bz - az) * np.random.rand(m)

# Condición: estar entre las dos superficies
inside = (z_mc >= y_mc**2 + 2) & (z_mc <= 4 - y_mc**2)

# Guardamos los puntos válidos
px = x_mc[inside]
py = y_mc[inside]
pz = z_mc[inside]

# --- PARTE 3: Gráfico combinado ---
fig = plt.figure(figsize=(12, 7))
ax3d = fig.add_subplot(111, projection='3d')

# Superficies
ax3d.plot_surface(X, Y, Z_top, alpha=0.6)
ax3d.plot_surface(X, Y, Z_bottom, alpha=0.6)

# Puntos Monte Carlo
ax3d.scatter(px, py, pz, c='green', s=4, alpha=0.3)

# Estética
ax3d.set_title('Volumen entre z = 4 - y² y z = y² + 2 (con puntos Monte Carlo)')
ax3d.set_xlabel('x')
ax3d.set_ylabel('y')
ax3d.set_zlabel('z')
ax3d.view_init(elev=25, azim=30)
ax3d.set_box_aspect([1, 1, 1])
plt.tight_layout()
plt.show()

#ax3d.scatter(px, py, pz, c='blue', s=3)