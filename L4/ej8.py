import numpy as np
import matplotlib.pyplot as plt

# Parámetros
m = 0.2
k = 0.1
c = 0.05
F_v = 0.01
omega = 0.3
h = 0.01  # paso de tiempo
tfin = 60  # tiempo total para ver varias oscilaciones

# Condiciones iniciales
t = 0
x = -1
v = 1

# Listas para almacenar datos
pt = [t]
px = [x]
pv = [v]
pa = []

# a_x = -kx/m -fv/m + F_vcos(omega*t)/m

while t <= tfin:
    F_ext = F_v * np.cos(omega * t)
    a = (F_ext - c * v - k * x) / m
    v += h * a
    x += h * v
    t += h
    
    pt.append(t)
    px.append(x)
    pv.append(v)
    pa.append(a)

# Ajustar pa para igualar tamaño de listas
pa.append(pa[-1])

# Graficar
plt.figure(figsize=(12, 9))

# x vs t
plt.subplot(2, 2, 1)
plt.plot(pt, px, color='blue')
plt.title('Posición (x) vs Tiempo (t)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.grid(True)

# v vs t
plt.subplot(2, 2, 2)
plt.plot(pt, pv, color='red')
plt.title('Velocidad (v) vs Tiempo (t)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)

# a vs t
plt.subplot(2, 2, 3)
plt.plot(pt, pa, color='green')
plt.title('Aceleración (a) vs Tiempo (t)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Aceleración (m/s²)')
plt.grid(True)

# v vs x
plt.subplot(2, 2, 4)
plt.plot(px, pv, color='purple')
plt.title('Velocidad (v) vs Posición (x)')
plt.xlabel('Posición (m)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)

plt.tight_layout()
plt.show()
