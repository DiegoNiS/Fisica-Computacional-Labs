import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Encuentra el punto de intersección entre sin(x) y x^2
def interseccion(x):
    return np.sin(x) - x**2

x0 = fsolve(interseccion, 0.8)[0]  # Punto de corte aproximado
N = 100000

# Generar puntos aleatorios dentro del rectángulo
x_rand = np.random.uniform(0, x0, N)
y_rand = np.random.uniform(0, 1, N)

# Condición: punto está entre las dos curvas
inside = (y_rand >= x_rand**2) & (y_rand <= np.sin(x_rand))

# Estimar el área
area_rect = x0 * 1.0  # ancho * alto del rectángulo
area_estimada = area_rect * np.sum(inside) / N

print(f"Área estimada: {area_estimada:.6f}")

# Graficar puntos Montecarlo
fig, ax = plt.subplots(figsize=(8,5))
ax.scatter(x_rand[inside], y_rand[inside], color='blue', s=0.5, label='Dentro')

# También se dibujan las curvas
x_plot = np.linspace(0, x0, 300)
ax.plot(x_plot, np.sin(x_plot), color='black', linestyle='--', label=r'$y = \sin x$')
ax.plot(x_plot, x_plot**2, color='black', linestyle='-.', label=r'$y = x^2$')

ax.set_title('Método de Montecarlo para área entre curvas')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig('images/mc3.png')
plt.show()
