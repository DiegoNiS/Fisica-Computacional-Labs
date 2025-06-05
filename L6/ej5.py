import numpy as np
import matplotlib.pyplot as plt

# Crear una grilla densa pero observar solo zona -2 a 2
xa = np.arange(-2, 2.1, 0.2)
ya = np.arange(-2, 2.1, 0.2)
x, y = np.meshgrid(xa, ya)

# Parámetros
I = 1.0
coefHelp = 0.05
sentido = +1  # Corriente hacia +z
# sentido = -1  # Corriente hacia -z ← descomenta para inciso b

# Alambres muy densos (lámina "más infinita")
num_alambres = 200
x_alambres = np.linspace(-10, 10, num_alambres)
y_alambres = np.zeros_like(x_alambres)

# Inicializar campo
Bx = np.zeros_like(x)
By = np.zeros_like(y)

# Superponer campo de cada alambre
for x0 in x_alambres:
    dx = x - x0
    dy = y
    r2 = dx**2 + dy**2 + coefHelp
    Bx += -sentido * dy / r2
    By +=  sentido * dx / r2

# Magnitud para normalizar visualmente
magnitud = np.sqrt(Bx**2 + By**2)

# Gráfica
plt.figure(figsize=(8, 6))
plt.quiver(x, y, Bx, By, magnitud, cmap='plasma', scale=40)
plt.title("Campo magnético en región central de una lámina infinita")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis('equal')
plt.colorbar(label='Intensidad del campo')
plt.show()
