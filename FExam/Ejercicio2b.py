import numpy as np
import matplotlib.pyplot as plt

# Datos iniciales
v0 = 5  # m/s
alpha0_deg = 60  # grados
alpha0 = np.radians(alpha0_deg)
g = 9.81  # m/s^2

# Componentes iniciales de la velocidad
vx0 = v0 * np.cos(alpha0)
vy0 = v0 * np.sin(alpha0)

# Condiciones iniciales
x = 0.0
y = 0.0
vx = vx0
vy = vy0
t = 0.0

# Paso de tiempo y arrays para guardar resultados
h = 0.01  # s
x_list = [x]
y_list = [y]
t_list = [t]

# Integración con Euler
while y >= 0:
    # Actualizar posición y velocidad
    x += vx * h
    y += vy * h
    vy += -g * h
    t += h

    # Guardar resultados
    x_list.append(x)
    y_list.append(y)
    t_list.append(t)

# Alcance aproximado (última x antes de que y caiga)
alcance_euler = x_list[-1]

# Gráfica de la trayectoria
plt.figure(figsize=(8,5))
plt.plot(x_list, y_list, label='Trayectoria (Euler)')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Trayectoria de una partícula (Euler)')
plt.axhline(0, color='k', linestyle='--')
plt.axvline(alcance_euler, color='r', linestyle='--', label=f'Alcance ≈ {alcance_euler:.2f} m')
plt.grid(True)
plt.legend()
plt.show()

# Mostrar el alcance
print(f"El alcance aproximado usando Euler es: {alcance_euler:.2f} metros")
