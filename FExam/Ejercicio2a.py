import numpy as np
import matplotlib.pyplot as plt

# Datos iniciales
v0 = 5  # m/s
alpha0_deg = 60  # grados
alpha0 = np.radians(alpha0_deg)
g = 9.81  # m/s^2

# Ecuación de la trayectoria
def trayectoria(x):
    return x * np.tan(alpha0) - (g / (2 * v0**2 * np.cos(alpha0)**2)) * x**2

# Calcular el alcance teórico (cuando y = 0)
alcance_teorico = (v0**2 * np.sin(2 * alpha0)) / g

# Generar datos para la gráfica
x = np.linspace(0, alcance_teorico, 100)
y = trayectoria(x)

# Graficar la trayectoria
plt.figure(figsize=(8,5))
plt.plot(x, y, label='Trayectoria')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Trayectoria de una partícula (v0=5m/s, alpha0=60°)')
plt.grid(True)
plt.axhline(0, color='k', linestyle='--')
plt.axvline(alcance_teorico, color='r', linestyle='--', label=f'Alcance ≈ {alcance_teorico:.2f} m')
plt.legend()
plt.show()

# Mostrar el alcance
print(f"El alcance teórico es: {alcance_teorico:.2f} metros")
