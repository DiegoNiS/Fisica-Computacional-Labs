import numpy as np
import matplotlib.pyplot as plt

# Datos iniciales
x0 = -2.0  # posición inicial (m)
v0 = 0.5   # velocidad inicial (m/s)
a = 2.0    # aceleración constante (m/s^2)
t0 = 0.0   # tiempo inicial (s)
t_final = 10.0  # tiempo final (s)
h_values = np.linspace(2, 0.01, 5)  # diferentes tamaños de paso para el método de Euler

# Solución analítica
t = np.linspace(t0, t_final, 500)
x_analytical = x0 + v0 * t + 0.5 * a * t**2

# Método de Euler
def euler_method(x0, v0, a, h, t_final):
    t_values = np.arange(t0, t_final + h, h)
    x_values = [x0]
    v = v0
    for i in range(1, len(t_values)):
        x_new = x_values[-1] + v * h
        v += a * h
        x_values.append(x_new)
    return t_values, x_values

# Gráfica
plt.figure(figsize=(10, 6))
plt.plot(t, x_analytical, label='Solución analítica', color='black', linewidth=2)

# Comparación para diferentes h
for h in h_values:
    t_euler, x_euler = euler_method(x0, v0, a, h, t_final)
    plt.plot(t_euler, x_euler, label=f'Método de Euler (h={h})', linestyle='--')

plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.title('Movimiento lineal con aceleración constante')
plt.legend()
plt.grid(True)
plt.show()