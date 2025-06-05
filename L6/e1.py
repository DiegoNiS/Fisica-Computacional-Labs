import numpy as np
import matplotlib.pyplot as plt

# Crear la grilla
xa = np.arange(-10, 10.4, 0.4)
ya = np.arange(-10, 10.4, 0.4)
x, y = np.meshgrid(xa, ya)

# Constantes y posiciones de los hilos (con corriente en +z)
B1 = 1
B2 = 1
B3 = 1

x1, y1 = -2, -4/np.sqrt(3)
x2, y2 =  2, -4/np.sqrt(3)
x3, y3 =  0,  4/np.sqrt(3)

# Campo magnético en el plano XY (usando superposición de campos tipo alambre infinito)
Bx = -B1 * (y - y1) / ((x - x1)**2 + (y - y1)**2)
Bx += -B2 * (y - y2) / ((x - x2)**2 + (y - y2)**2)
Bx += -B3 * (y - y3) / ((x - x3)**2 + (y - y3)**2)

By = B1 * (x - x1) / ((x - x1)**2 + (y - y1)**2)
By += B2 * (x - x2) / ((x - x2)**2 + (y - y2)**2)
By += B3 * (x - x3) / ((x - x3)**2 + (y - y3)**2)

# Graficar campo magnético con quiver
plt.figure(figsize=(8, 8))
plt.quiver(x, y, Bx, By, scale=50)
plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], lw=2)  # Triángulo equilátero
plt.title("Campo magnético de tres hilos de corriente (modelo idealizado)")
plt.xlabel('x')
plt.ylabel('y')
plt.axis('square')
plt.grid(True)
plt.show()
