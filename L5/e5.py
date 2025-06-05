import numpy as np
import matplotlib.pyplot as plt

k = 1.0
n_lado = 4  # cargas por lado
L = 0.8     # lado del cuadrado
epsilon = 1e-4

x_cargas = []
y_cargas = []

x_cargas.extend(np.linspace(0, L, (n_lado-1), endpoint=False))
y_cargas.extend([0] * (n_lado-1))

x_cargas.extend([L] * (n_lado-1))
y_cargas.extend(np.linspace(0, L, (n_lado-1), endpoint=False))

x_cargas.extend(np.linspace(L, 0, (n_lado-1), endpoint=False))
y_cargas.extend([L] * (n_lado-1))

x_cargas.extend([0] * (n_lado-1))
y_cargas.extend(np.linspace(L, 0, (n_lado-1), endpoint=False))

x_cargas = np.array(x_cargas)
y_cargas = np.array(y_cargas)

xa = np.linspace(-0.5, 1.5, 100)
ya = np.linspace(-0.5, 1.5, 100)
x, y = np.meshgrid(xa, ya)

import random

charges = np.array([1 if random.randint(0,2) == 0 else -1 for i in range(len(x_cargas))])

z = np.zeros_like(x)
for i in range(len(charges)):
    z += k * charges[i] / np.sqrt((x - x_cargas[i])**2 + (y - y_cargas[i])**2 + epsilon)

plt.figure()
zmax = np.max(z)
zmin = np.min(z)
dz = (zmax - zmin) / 40
niveles = np.arange(zmin, zmax, dz)

contours = plt.contour(x, y, z, levels=niveles, cmap='cividis')
plt.clabel(contours, inline=True, fontsize=8)
plt.scatter(x_cargas, y_cargas, color='red', s=50)
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.title('Potencial eléctrico - Espira cuadrada (cargas intercaladas)')
plt.axis('equal')
plt.grid(True)
plt.show()
