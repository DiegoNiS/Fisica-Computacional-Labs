import numpy as np
import matplotlib.pyplot as plt

# Parámetros
xa = np.arange(-0.1, 1.12, 0.02)
ya = np.arange(-0.1, 1.12, 0.02)
k = 1.0
x1, y1 = 0.2, 0.2
x2, y2 = 0.5, 0.2
x3, y3 = 0.5, 0.5
x4, y4 = 0.2, 0.5

# Crear malla
x, y = np.meshgrid(xa, ya)

# Calcular potencial eléctrico
q1, q2, q3, q4 = 1, 1, 1, 1

# Evitar división por cero agregando una pequeña constante al denominador
epsilon = 1e-6
z = (k*q1 / np.sqrt((x - x1)**2 + (y - y1)**2 + epsilon) +
     k*q2 / np.sqrt((x - x2)**2 + (y - y2)**2 + epsilon) +
     k*q3 / np.sqrt((x - x3)**2 + (y - y3)**2 + epsilon) +
     k*q4 / np.sqrt((x - x4)**2 + (y - y4)**2 + epsilon))

# Limitar el valor máximo del potencial para que no se dispare visualmente
z = np.clip(z, a_min=None, a_max=100)

# Definir niveles de contorno
zmax = np.max(z)
zmin = np.min(z)
dz = (zmax - zmin) / 40  # menos niveles = más claro
nivel = np.arange(zmin, zmax, dz)

# Graficar equipotenciales
plt.figure()
contours = plt.contour(x, y, z, levels=nivel, cmap='viridis')
plt.clabel(contours, inline=True, fontsize=8)
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.title('Líneas equipotenciales - 4 cargas positivas')
plt.axis('equal')
plt.grid(True)
plt.scatter([x1, x2, x3, x4], [y1, y2, y3, y4], color='red', s=100)
plt.show()
