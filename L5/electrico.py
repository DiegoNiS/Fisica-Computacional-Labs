import numpy as np
import matplotlib.pyplot as plt

# Parámetros
xa = np.arange(-2, 2.5, 0.5)
ya = np.arange(-2, 2.5, 0.5)
k = 1.0
q1 = 1
q2 = -1
x1 = 1
x2 = -1

# Crear la malla de puntos
x, y = np.meshgrid(xa, ya)

# Calcular componentes del campo eléctrico
Ex = k*q1*(x - x1) / ((x - x1)**2 + y**2)**1.5 + k*q2*(x - x2) / ((x - x2)**2 + y**2)**1.5
Ey = k*q1*y / ((x - x1)**2 + y**2)**1.5 + k*q2*y / ((x - x2)**2 + y**2)**1.5

# Graficar el campo eléctrico
plt.figure()
plt.quiver(x, y, Ex, Ey)
plt.axis('square')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Campo eléctrico de dos cargas')
plt.grid(True)
plt.show()