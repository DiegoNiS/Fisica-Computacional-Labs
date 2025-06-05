import numpy as np
import matplotlib.pyplot as plt
import random

# Constantes
k = 1.0
n_lado = 4  # 4 cargas por lado, incluyendo esquinas
L = 0.8     # longitud del lado del cuadrado
epsilon = 1e-4

# Posiciones de las cargas
x_cargas = []
y_cargas = []

# Lado inferior (de izquierda a derecha)
x_cargas.extend(np.linspace(0, L, n_lado))
y_cargas.extend([0] * n_lado)

# Lado derecho (de abajo hacia arriba)
x_cargas.extend([L] * (n_lado - 1))  # Ya se colocó la esquina inferior derecha
y_cargas.extend(np.linspace(0, L, n_lado)[1:])

# Lado superior (de derecha a izquierda)
x_cargas.extend(np.linspace(L, 0, n_lado)[1:])  # Esquina superior derecha ya colocada
y_cargas.extend([L] * (n_lado - 1))

# Lado izquierdo (de arriba hacia abajo)
x_cargas.extend([0] * (n_lado - 2))  # Esquina superior izquierda ya colocada
y_cargas.extend(np.linspace(L, 0, n_lado)[1:-1])

x_cargas = np.array(x_cargas)
y_cargas = np.array(y_cargas)

# Asignar cargas distintas al azar en cada posición
charges = np.array([random.choice([-2, -1, 1, 2]) for _ in range(len(x_cargas))])

# Crear malla para calcular el potencial
xa = np.linspace(-0.5, 1.5, 200)
ya = np.linspace(-0.5, 1.5, 200)
x, y = np.meshgrid(xa, ya)

# Calcular el potencial eléctrico en cada punto de la malla
z = np.zeros_like(x)
for i in range(len(charges)):
    z += k * charges[i] / np.sqrt((x - x_cargas[i])**2 + (y - y_cargas[i])**2 + epsilon)

# Gráfica
plt.figure(figsize=(8, 6))
zmax = np.max(z)
zmin = np.min(z)
dz = (zmax - zmin) / 40
niveles = np.arange(zmin, zmax, dz)

contours = plt.contour(x, y, z, levels=niveles, cmap='plasma')
plt.clabel(contours, inline=True, fontsize=8)
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.title('Potencial eléctrico - Espira cuadrada (4 cargas por lado)')
plt.axis('equal')
plt.grid(True)
plt.show()
