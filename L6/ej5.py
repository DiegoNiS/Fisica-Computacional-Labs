import numpy as np
import matplotlib.pyplot as plt


x_graph_max, x_graph_min = 20, -20
y_graph_max, y_graph_min = 20, -20
# Crear una grilla densa pero observar solo zona -2 a 2
xa = np.arange(x_graph_min-2, x_graph_max+2, 1.0)
ya = np.arange(y_graph_min-2, y_graph_max+2, 1.0)
x, y = np.meshgrid(xa, ya)

# Parámetros
I = 1.0
coefHelp = 0.1
sentido = +1  # Corriente hacia +z
# sentido = -1  # Corriente hacia -z ← descomenta para inciso b

# Alambres muy densos (lámina "más infinita")
num_alambres = 20
x_alambres = np.linspace(x_graph_min, x_graph_max, num_alambres)
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

# Gráfica
plt.figure(figsize=(8, 6))
plt.quiver(x, y, Bx, By)
plt.scatter(x_alambres, y_alambres, color='b', s=60)
plt.title("Campo magnético en región central de una lámina infinita")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis('equal')
plt.show()
