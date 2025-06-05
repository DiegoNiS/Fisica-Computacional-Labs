import numpy as np
import matplotlib.pyplot as plt

# Parámetros
xa = np.arange(-2.1, 2.12, 0.12)
ya = np.arange(-2.1, 2.12, 0.12)
k = 1.0
q1 = 1
q2 = 1
x1 = 1
x2 = -1

# Crear la malla de puntos
x, y = np.meshgrid(xa, ya)

# Calcular el potencial eléctrico
z = k*q1 / np.sqrt((x - x1)**2 + y**2) + k*q2 / np.sqrt((x - x2)**2 + y**2)

# Definir niveles de contorno
zmax = np.max(z)
zmin = np.min(z)
dz = (zmax - zmin) / 400
nivel = np.arange(zmin, zmax, dz)

# Graficar líneas de contorno (equipotenciales)
plt.figure()
contours = plt.contour(x, y, z, levels=nivel, cmap='viridis')
plt.clabel(contours, inline=True, fontsize=8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Líneas equipotenciales de dos cargas positivas')
plt.axis('equal')
plt.grid(True)
plt.show()
