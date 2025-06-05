import numpy as np
import matplotlib.pyplot as plt

# Parámetros
k = 1.0
n = 6  # número de cargas (hexágono regular)
radio = 0.7  # distancia desde el centro (cm)
epsilon = 1e-3  # para evitar división por cero

# Posiciones de las cargas en el hexágono
angulos = np.linspace(0, 2*np.pi, n, endpoint=False)
x_cargas = radio * np.cos(angulos)
y_cargas = radio * np.sin(angulos)

# Malla de puntos
xa = np.arange(-1.5, 1.52, 0.05)
ya = np.arange(-1.5, 1.52, 0.05)
x, y = np.meshgrid(xa, ya)

cargas = [1, -1, 1, -1, 1, -1]
z = np.zeros_like(x)
for i in range(n):
    z += k * cargas[i] / np.sqrt((x - x_cargas[i])**2 + (y - y_cargas[i])**2 + epsilon)

plt.figure()
zmax = np.max(z)
zmin = np.min(z)
dz = (zmax - zmin) / 40
niveles = np.arange(zmin, zmax, dz)

contours = plt.contour(x, y, z, levels=niveles, cmap='cividis')
plt.clabel(contours, inline=True, fontsize=8)
plt.scatter(x_cargas, y_cargas, s=100)
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.title('Potencial eléctrico - cargas intercaladas en hexágono')
plt.axis('equal')
plt.grid(True)
plt.show()
