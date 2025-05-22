import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

k = 0.1          # sin resorte
m = 0.2        # masa en kg
c = 0.5        # fricción viscosa
h = 0.01       # paso de tiempo
tfin = 60     # duración de la simulación

t = 0
x = 0
v = -2

pt = [t]
px = [x]
pv = [v]

while t <= tfin:
    a = -(k * x + c * v) / m
    v += h * a
    x += h * v
    t += h
    pt.append(t)
    px.append(x)
    pv.append(v)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

omega_0 = math.sqrt(k / m)

gamma = c / (2 * m)

print(f"w_0 = {omega_0:.4f}")
print(f"Y  = {gamma:.4f}")

# Evaluación del régimen
if gamma**2 < omega_0**2:
    print("Sistema subamortiguado (oscilatorio)")
elif gamma**2 == omega_0**2:
    print("Sistema críticamente amortiguado")
else:
    print("Sistema sobreamortiguado (no oscilatorio)")

ax.plot(pt, px, pv, color='orange', label='Trayectoria (t, x, v)')

ax.set_xlabel('Tiempo (t)')
ax.set_ylabel('Posición (x)')
ax.set_zlabel('Velocidad (v)')
ax.set_title('Gráfico 3D: v, x, t')
ax.legend()

plt.tight_layout()
plt.show()

