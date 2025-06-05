import matplotlib.pyplot as plt
import numpy as np

x, y = 5, 0
vx, vy = 0, 1.2
h = 0.01
t_max = 1000
px, py = [], []

for _ in range(t_max):
    r = np.sqrt(x**2 + y**2)
    ax = -x / r**3
    ay = -y / r**3
    vx += h * ax
    vy += h * ay
    x += h * vx
    y += h * vy

    if np.sqrt(x**2 + y**2) > 3:
        px.append(x)
        py.append(y)

plt.figure()
plt.plot(px, py, label='Órbita fuera de r=3')
circle = plt.Circle((0, 0), 3, color='gray', fill=False, linestyle='--', label='r=3')
plt.gca().add_patch(circle)
plt.axis('equal')
plt.grid(True)
plt.title('Simulación: No graficar dentro de r=3')
plt.legend()
plt.show()
