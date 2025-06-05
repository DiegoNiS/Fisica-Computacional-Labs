import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Necesario para 3D plots

# Parámetros
xa = np.arange(-2.1, 2.12, 0.12)
ya = np.arange(-2.1, 2.12, 0.12)
k = 1.0
q1 = 1
q2 = -1
x1 = 1
x2 = -1

# Crear la malla de puntos
x, y = np.meshgrid(xa, ya)

# Calcular el potencial eléctrico
z = k*q1 / np.sqrt((x - x1)**2 + y**2) + k*q2 / np.sqrt((x - x2)**2 + y**2)

# Crear figura y graficar superficie
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis', edgecolor='k')

# Etiquetas y ajustes
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Potencial eléctrico (V)')
ax.set_title('Potencial eléctrico de dos cargas')
plt.show()
