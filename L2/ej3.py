import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# === Función de simulación orbital ===
def orbita(x0, y0, vx0, vy0, h=0.01, t_max=50000, radio_planeta=3):
    x, y = x0, y0
    vx, vy = vx0, vy0
    px, py = [], []

    for _ in range(t_max):
        r2 = x**2 + y**2
        r = np.sqrt(r2)
        
        # Aceleración gravitacional
        ax = -x / r2**(3/2)
        ay = -y / r2**(3/2)
        
        # Actualizar velocidades
        vx += h * ax
        vy += h * ay
        
        # Actualizar posiciones
        x += h * vx
        y += h * vy

        if r > radio_planeta:
            px.append(x)
            py.append(y)
        else:
            break  # colisión, deja de guardar datos

    return px, py

# === Condiciones iniciales ===
x0 = 4
y0 = 0
vx0 = 0.0
vy0 = -0.6  # negativa para dirección hacia abajo

# Simular una trayectoria
px, py = orbita(x0, y0, vx0, vy0)

# === Preparar la animación ===
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-10, 10)
ax.set_ylim(0, 15)
ax.set_aspect('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Animación de la órbita con colisión')

# Planeta
circle = plt.Circle((0, 0), 3, color='gray', fill=True, alpha=0.3)
ax.add_patch(circle)
ax.plot(0, 0, 'ro', label='Centro de atracción')

# Línea de trayectoria y punto actual
line, = ax.plot([], [], 'b-', label='Trayectoria')
point, = ax.plot([], [], 'bo')  # punto en movimiento

# === Función de actualización de la animación ===
def update(frame):
    line.set_data(px[:frame], py[:frame])
    point.set_data(px[frame-1], py[frame-1])
    return line, point

# Crear la animación
ani = FuncAnimation(fig, update, frames=len(px), interval=1, blit=True)

plt.legend()
plt.grid(True)
plt.show()
