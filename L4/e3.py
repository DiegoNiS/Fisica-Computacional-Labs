import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

k = 1
m = 2
h = 0.1
tfin = 30

t = 0
x = 1
v = 0

pt = [t]
px = [x]
pv = [v]

while t <= tfin:
    a = -k * x / m
    v += h * a
    x += h * v
    t += h
    pt.append(t)
    px.append(x)
    pv.append(v)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot(pt, px, pv, color='purple', label='Trayectoria 3D')

ax.set_xlabel('Tiempo (t)')
ax.set_ylabel('Posición (x)')
ax.set_zlabel('Velocidad (v)')
ax.set_title('Gráfico 3D: posición y velocidad en función del tiempo')
ax.legend()

plt.tight_layout()
plt.show()
