import numpy as np
import matplotlib.pyplot as plt

# Constantes
mu0 = 4 * np.pi * 1e-7  # permeabilidad del vacío
I = 1.0                 # corriente en cada anillo
R = 1.0                 # radio de cada anillo
d = 0.4             # distancia entre anillos
N = 30                   # número de anillos (ímpares para que haya uno centrado)

# Posiciones de los centros de los anillos
centros = np.linspace(-d*(N//2), d*(N//2), N)

# Rango de x sobre el cual calcular el campo
x = np.linspace(-10, 10, 1000)

# Inicializar campo total
B_total = np.zeros_like(x)

# Sumar campos de cada anillo
for xc in centros:
    B_total += (mu0 * I * R**2) / (2 * ((x - xc)**2 + R**2)**(1.5))

# Graficar
plt.figure(figsize=(10, 5))
plt.plot(x, B_total, label='B total', color='blue')
for xc in centros:
    plt.axvline(xc, color='gray', linestyle='--', alpha=0.3)  # marcar los anillos
plt.title("Campo magnético B(x) de varios anillos alineados")
plt.xlabel("x (m)")
plt.ylabel("B (T)")
plt.grid(True)
plt.legend()
plt.show()
