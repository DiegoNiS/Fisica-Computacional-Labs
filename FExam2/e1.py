import numpy as np
import matplotlib.pyplot as plt

# Derivada dx/dt = x * cos(t)
def v(t, x):
    return x * np.cos(t)

# Solución exacta: x(t) = x0 * exp(sin(t))
def exact_solution(t, x0):
    return x0 * np.exp(np.sin(t))

# Parámetros
x0 = 1.0
t0 = 0.0
tf = 10.0
h = 0.1
n = int((tf - t0)/h) + 1

# Inicialización
t = np.linspace(t0, tf, n)
x = np.zeros(n)
x[0] = x0

# Euler: forma 1 (x_{i+1} = x_i + h * v_i)
for i in range(n - 1):
    x[i+1] = x[i] + h * v(t[i], x[i])

# Solución exacta
x_exact = exact_solution(t, x0)

# Gráfica
plt.figure(figsize=(8,5))
plt.plot(t, x, label='Euler', marker='o', markersize=3)
plt.plot(t, x_exact, label='Exacta', linestyle='--', color='black')
plt.title('Comparación entre método de Euler y solución exacta')
plt.xlabel('Tiempo t')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('images/e1.png')
plt.show()
