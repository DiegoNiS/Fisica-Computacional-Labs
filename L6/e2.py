import numpy as np
import matplotlib.pyplot as plt

# Crear la grilla donde se calculará el campo
xa = np.arange(-5, 5.4, 0.2)
ya = np.arange(-5, 5.4, 0.2)
x, y = np.meshgrid(xa, ya)

# Corriente unitaria
I = 1.0
coefHelp = 0.1

# --- Sentido de la corriente ---
sentido = +1  # Inciso (a): corriente hacia +z
# sentido = -1  # Inciso (b): corriente hacia -z ← descomenta esta línea para inciso (b)

# --- Coordenadas de los n vértices del triángulo equilátero centrado en el origen ---
n = 4
radio = 3  # puedes ajustar este radio si quieres un triángulo más grande
angulos = np.linspace(0, 2*np.pi, n, endpoint=False)
x_v = radio * np.cos(angulos)
y_v = radio * np.sin(angulos)

# Inicializar campo magnético (simplificado usando modelo de alambres infinitos)
Bx = np.zeros_like(x)
By = np.zeros_like(y)

# Sumar el campo de cada hilo con corriente perpendicular al plano
for xv, yv in zip(x_v, y_v):
    dx = x - xv
    dy = y - yv
    r2 = dx**2 + dy**2 + coefHelp  # evitar división por cero
    Bx += -sentido * dy / r2
    By +=  sentido * dx / r2

# Graficar campo magnético con quiver
plt.figure(figsize=(8, 8))
plt.quiver(x, y, Bx, By, color='r', scale=60)
#plt.plot(np.append(x_v, x_v[0]), np.append(y_v, y_v[0]), 'b-', lw=2)  # triángulo
#plt.scatter(x_v, y_v, color='k')  # vértices
plt.title(f"Campo magnético en triángulo equilátero (corriente en {'+z' if sentido == 1 else '-z'})")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.grid(True)
plt.show()
