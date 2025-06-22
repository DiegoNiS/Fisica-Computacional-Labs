import numpy as np
import matplotlib.pyplot as plt

# Parámetros
m = 50000        # número de puntos por iteración
veces = 50       # número de repeticiones del experimento
ax, bx = 0, 8/3   # intervalo en x
ay, by = -3, 5   # intervalo en y

sa = 0.0         # suma de áreas
saa = 0.0        # suma de áreas al cuadrado
px_total = []    # para graficar puntos al final
py_total = []

# Simulación Monte Carlo
for k in range(veces):
    n = 0
    px = []
    py = []

    for i in range(m):
        x = ax + (bx - ax) * np.random.rand()
        y = ay + (by - ay) * np.random.rand()

        f1 = -x**2 + 4 * x
        f2 = x**2/2

        if f1 >= y >= f2:  # Elipse: x²/4 + y²/9 < 1
            n += 1
            px.append(x)
            py.append(y)

    area = n * (by - ay) * (bx - ax) / m
    sa += area
    saa += area**2

    if k == 0:
        px_total = px
        py_total = py

# Cálculo de resultados
prom = sa / veces
desv = np.sqrt(veces * saa - sa**2) / veces

# Gráfica
plt.figure(figsize=(8, 6))
plt.plot(px_total, py_total, '.', markersize=1)
plt.title('Áreas por el método de Monte Carlo')
plt.xlabel('x')
plt.ylabel('y')
#plt.axis([-3, 3, -4, 4])
plt.text(0.5, 3.5, f"{prom:.4f}")
plt.text(1.5, 3.5, "+/-")
plt.text(2.0, 3.5, f"{desv:.4f}")
plt.grid(True)
plt.show()
