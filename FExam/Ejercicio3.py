import numpy as np
import matplotlib.pyplot as plt

G=6.67430e-11  # Constante gravitacional (m^3/kg*s^2)
M=5.972e24    # Masa de la Tierra (kg)
R=6.371e6     # Radio de la Tierra (metros)

h=0.1
tfin=20000 # Tiempo final de la simulación (segundos)

def ax(x, y):
    r = x**2 + y**2
    r = r * np.sqrt(r) # r ^ (3/2)
    return -G * M * x / r

def ay(x, y):
    r = x**2 + y**2
    r = r * np.sqrt(r) # r ^ (3/2)
    return -G * M * y / r

# Dibujar circulo
theta = np.linspace(0, 2*np.pi, 1000)
x_earth = R * np.cos(theta)
y_earth = R * np.sin(theta)

plt.figure(figsize=(8, 8))
plt.plot(x_earth, y_earth, 'k', linewidth=3)
plt.axis('equal')

# Posición inicial en el borde del círculo
x0 = 0.0
y0 = R + 1000e3  # Altura de 1000 km sobre la superficie de la Tierra

vel_iniciales = np.linspace(5000, 9000, 5)
vel_iniciales = np.append(vel_iniciales, 11500)  # Velocidad de escape aproximada
for vx_init in vel_iniciales:
    x = x0
    y = y0
    vx = vx_init
    vy = 0
    px = [x]
    py = [y]
    t = 0.0
    while t < tfin:
        x += vx * h
        y += vy * h
        if x**2 + y**2 < R**2:
            break
        vx += ax(x, y) * h
        vy += ay(x, y) * h
        px.append(x)
        py.append(y)
        t += h
    plt.plot(px, py, label=f'vx = {vx_init/1000:.1f} km/s')

plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Trayectorias de cuerpos en movimiento alrededor de la Tierra')
plt.legend()
plt.grid(True)
plt.show()