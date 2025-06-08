import numpy as np
import matplotlib.pyplot as plt

v0 = 5  # m/s
alpha0_deg = 60  # grados
alpha0 = np.radians(alpha0_deg)
g = 9.81  # m/s^2

vx0 = v0 * np.cos(alpha0)
vy0 = v0 * np.sin(alpha0)

def trayectoria_analitica(x):
    return x * np.tan(alpha0) - (g / (2 * v0**2 * np.cos(alpha0)**2)) * x**2

alcance_teorico = (v0**2 * np.sin(2 * alpha0)) / g

def euler_trayectoria(h):
    x, y = 0.0, 0.0
    vx, vy = vx0, vy0
    t = 0.0

    x_list = [x]
    y_list = [y]

    while y >= 0:
        x += vx * h
        y += vy * h
        vy -= g * h
        t += h

        x_list.append(x)
        y_list.append(y)

    return x_list, y_list

h_values = [0.5, 0.1, 0.05, 0.01, 0.005]
alcances_euler = []

plt.figure(figsize=(10, 6))

x_analitico = np.linspace(0, alcance_teorico, 300)
y_analitico = trayectoria_analitica(x_analitico)
plt.plot(x_analitico, y_analitico, 'k-', label='Analítica', linewidth=2)

for h in h_values:
    x_euler, y_euler = euler_trayectoria(h)
    alcance = x_euler[-1]
    alcances_euler.append(alcance)
    plt.plot(x_euler, y_euler, '--', label=f'Euler (h={h})')
    print(f"h = {h:<6} → Alcance (Euler) ≈ {alcance:.4f} m, Error = {abs(alcance - alcance_teorico):.4f} m")

plt.title('Comparación de trayectorias (Analítica vs Euler)')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid(True)
plt.axvline(alcance_teorico, color='gray', linestyle=':', label=f'Alcance Teórico ≈ {alcance_teorico:.2f} m')
plt.legend()
plt.show()

print("\nTabla de comparación de alcances:")
print(f'| {"h":>8} | {"Alcance Euler (m)":>18} | {"Error (m)":>10} |')
print('-' * 45)
for h, alcance in zip(h_values, alcances_euler):
    error = abs(alcance - alcance_teorico)
    print(f'| {h:8.4f} | {alcance:18.4f} | {error:10.4f} |')

# Mostrar alcance teórico
print(f"\nAlcance teórico: {alcance_teorico:.4f} m")
