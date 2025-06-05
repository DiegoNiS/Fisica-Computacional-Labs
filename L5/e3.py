import numpy as np
import matplotlib.pyplot as plt

# Parámetros
k = 1.0
q = 1  # todas las cargas iguales
n = 6  # número de cargas (hexágono regular)
radio = 1.0  # distancia desde el centro (cm)

# Posiciones de las cargas en el hexágono
angulos = np.linspace(0, 2*np.pi, n, endpoint=False)
x_cargas = radio * np.cos(angulos)
y_cargas = radio * np.sin(angulos)

# Malla de puntos
xa = np.arange(-1.5, 1.52, 0.1)
ya = np.arange(-1.5, 1.52, 0.1)
x, y = np.meshgrid(xa, ya)

# Calcular el campo eléctrico
epsilon = 1e-6  # para evitar división por cero

cargas = [1, -1, 1, 1, 1, 1]  # intercaladas

Ex = np.zeros_like(x)
Ey = np.zeros_like(y)
for i in range(n):
    dx = x - x_cargas[i]
    dy = y - y_cargas[i]
    r2 = dx**2 + dy**2 + epsilon
    r3 = r2**1.5
    Ex += k * cargas[i] * dx / r3
    Ey += k * cargas[i] * dy / r3


# Graficar el campo con flechas
plt.figure()
plt.quiver(x, y, Ex, Ey)
plt.scatter(x_cargas, y_cargas, s=100)
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.title('Campo eléctrico - 6 cargas positivas en hexágono')
plt.axis('equal')
plt.grid(True)
plt.show()
