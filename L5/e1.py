import numpy as np
import matplotlib.pyplot as plt

def campo_electrico(charges, x_cargas, y_cargas, x, y):
    Ex = 0
    Ey = 0
    k = 1.0  # constante de Coulomb
    for i in range(len(charges)):
        dx = x - x_cargas[i]
        dy = y - y_cargas[i]
        r2 = dx**2 + dy**2
        r3 = r2**1.5
        r3[r3 == 0] = 1e-10  # evitar división por cero
        Ex += k * charges[i] * dx / r3
        Ey += k * charges[i] * dy / r3
    return Ex, Ey


# Posiciones de las cargas (vértices del cuadrado)
x_cargas = [0, 1, 1, 0]
y_cargas = [0, 0, 1, 1]

# Todas las cargas positivas
charges = [1, -1, 1, 1]

# Crear malla
xa = np.linspace(-0.5, 1.5, 25)
ya = np.linspace(-0.5, 1.5, 25)
x, y = np.meshgrid(xa, ya)

# Calcular el campo
Ex, Ey = campo_electrico(charges, x_cargas, y_cargas, x, y)

# Dibujar el campo
plt.figure()
plt.quiver(x, y, Ex, Ey)
plt.scatter(x_cargas, y_cargas, s=100)
plt.axis('square')
plt.title('Campo eléctrico - 4 cargas positivas')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.grid(True)
plt.show()