import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros
m = 10000
veces = 30
ax, bx = 0, 1    # x > 0
ay, by = 0, 2    # y > 0
az, bz = -3, 3   # z completo

sa = 0.0
saa = 0.0

# Solo guardamos los puntos de la primera iteración para graficar
px, py, pz = [], [], []

for k in range(veces):
    count = 0

    x = ax + (bx - ax) * np.random.rand(m)
    y = ay + (by - ay) * np.random.rand(m)
    z = az + (bz - az) * np.random.rand(m)

    inside = (x**2 / 1 + y**2 / 4 + z**2 / 9) <= 1
    count = np.sum(inside)

    if k == 0:
        px = x[inside]
        py = y[inside]
        pz = z[inside]

    vol_prisma = (bx - ax) * (by - ay) * (bz - az)
    vol_estimado = count * vol_prisma / m

    sa += vol_estimado
    saa += vol_estimado**2

# Promedio y desviación
prom = sa / veces
desv = np.sqrt(veces * saa - sa**2) / veces

# Gráfica 3D
fig = plt.figure(figsize=(10, 7))
ax3d = fig.add_subplot(111, projection='3d')
ax3d.scatter(px, py, pz, c='blue', s=1, alpha=0.3)
ax3d.set_title(f'Puntos dentro del elipsoide\nVolumen estimado ≈ {prom:.4f} ± {desv:.4f}')
ax3d.set_xlabel('x')
ax3d.set_ylabel('y')
ax3d.set_zlabel('z')
ax3d.set_xlim(0, 1)
ax3d.set_ylim(0, 2)
ax3d.set_zlim(-3, 3)
plt.tight_layout()
plt.show()
