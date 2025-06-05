import numpy as np
import matplotlib.pyplot as plt

# Constantes
k = 1.0
n_lado = 20  # 4 cargas por lado, incluyendo esquinas
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

# Crear figura con dos subplots (una fila, dos columnas)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# === Subplot 1: Potencial eléctrico (mesh) ===
mesh = axes[0].pcolormesh(x, y, z, shading='auto', cmap='cividis')
axes[0].scatter(x_cargas, y_cargas, color='red', s=50)
axes[0].set_xlabel('x (cm)')
axes[0].set_ylabel('y (cm)')
axes[0].set_title('Potencial eléctrico')
axes[0].axis('equal')
axes[0].grid(True)

# (opcional, pero útil si se desea)
# fig.colorbar(mesh, ax=axes[0], label='V')

# === Subplot 2: Campo eléctrico ===
axes[1].streamplot(x, y, Ex, Ey, color='black', density=1.0)
axes[1].scatter(x_cargas, y_cargas, color='red', s=50)
axes[1].set_xlabel('x (cm)')
axes[1].set_ylabel('y (cm)')
axes[1].set_title('Campo eléctrico')
axes[1].axis('equal')
axes[1].grid(True)

# Mostrar ambos subplots
plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Importar módulo 3D

# Constantes
k = 1.0
n_lado = 20
L = 0.8
epsilon = 1e-4

# Posiciones de cargas en espira cuadrada
x_cargas = []
y_cargas = []

x_cargas.extend(np.linspace(0, L, n_lado))
y_cargas.extend([0] * n_lado)

x_cargas.extend([L] * (n_lado - 1))
y_cargas.extend(np.linspace(0, L, n_lado)[1:])

x_cargas.extend(np.linspace(L, 0, n_lado)[1:])
y_cargas.extend([L] * (n_lado - 1))

x_cargas.extend([0] * (n_lado - 2))
y_cargas.extend(np.linspace(L, 0, n_lado)[1:-1])

x_cargas = np.array(x_cargas)
y_cargas = np.array(y_cargas)
charges = np.ones(len(x_cargas))

# Malla
xa = np.linspace(-0.5, 1.5, 100)
ya = np.linspace(-0.5, 1.5, 100)
x, y = np.meshgrid(xa, ya)

# Calcular potencial
z = np.zeros_like(x)
for i in range(len(charges)):
    z += k * charges[i] / np.sqrt((x - x_cargas[i])**2 + (y - y_cargas[i])**2 + epsilon)

# === Gráfico 3D ===
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='cividis', edgecolor='none')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
ax.set_zlabel('V (potencial)')
ax.set_title('Potencial eléctrico - Espira cuadrada (vista 3D)')
plt.show()
