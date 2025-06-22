import numpy as np
import matplotlib.pyplot as plt

# Parámetros
v = 1.0
tfin = 8.0
dt = np.pi
x_resolution = 0.001
segment_width = 3  # cada segmento va de -1 a 1

# Preparar figura
plt.figure(figsize=(10, 4))
plt.title("Onda triangular alternada (tramos reflejados)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Simulación en distintos tiempos
for t in np.arange(0, tfin + dt, dt):
    px = []
    py = []

    for ix in np.arange(0, np.pi, x_resolution):
        x = ix + v * t
        tramo = int(np.floor((x - v * t) / segment_width))  # número de segmento
        signo = (-1) ** tramo  # alterna positivo-negativo
        y = signo * (x - v * t)
        px.append(x)
        py.append(y)

    plt.plot(px, py, linewidth=2)

#plt.xlim([0, v * (tfin + 1)])
#plt.ylim([-1.2, 1.2])
plt.show()
