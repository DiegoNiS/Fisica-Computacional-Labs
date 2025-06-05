import numpy as np
import matplotlib.pyplot as plt

# Constantes
k = 1.0
n_lado = 10  # 4 cargas por lado, incluyendo esquinas
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

# Todas las cargas positivas
charges = np.ones(len(x_cargas))

# Malla para calcular el potencial
xa = np.linspace(-0.5, 1.5, 100)
ya = np.linspace(-0.5, 1.5, 100)
x, y = np.meshgrid(xa, ya)

# Calcular el potencial eléctrico
z = np.zeros_like(x)
for i in range(len(charges)):
    z += k * charges[i] / np.sqrt((x - x_cargas[i])**2 + (y - y_cargas[i])**2 + epsilon)

# Calcular el campo eléctrico (E = -grad V)
Ey, Ex = np.gradient(-z, ya[1] - ya[0], xa[1] - xa[0])

# Graficar el potencial
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
plt.title('Potencial eléctrico - Espira cuadrada (10 cargas positivas)')
plt.axis('equal')
plt.grid(True)
plt.show()

# Graficar el campo eléctrico
plt.figure()
plt.streamplot(x, y, Ex, Ey, color='black', density=1.0)
plt.scatter(x_cargas, y_cargas, color='red', s=50)
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.title('Campo eléctrico - Espira cuadrada (10 cargas positivas)')
plt.axis('equal')
plt.grid(True)
plt.show()
