import numpy as np
import matplotlib.pyplot as plt

# Parámetros
v = 1.0
t = 0  # instante de tiempo fijo
x_resolution = 1
num_periodos = 1
segment_length = 2.0  # medio periodo

# Crear figura
plt.figure(figsize=(12, 4))
plt.title("Onda triangular continua tipo /\\/\\/\\/\\")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Rango de x (10 periodos)
x_vals = np.arange(0, num_periodos * 2 * segment_length, x_resolution)

# Cálculo de la onda triangular alternada
y_vals = []
for x in x_vals:
    fase = (x - v * t) % (2 * segment_length)
    if fase < segment_length:
        y = fase
    else:
        y = 2 * segment_length - fase
    y_vals.append(y)

# Centrar verticalmente la onda
y_vals = np.array(y_vals) - segment_length / 2

# Dibujar
plt.plot(x_vals, y_vals, 'b', linewidth=2)
plt.ylim([-segment_length, segment_length])
plt.xlim([0, num_periodos * 2 * segment_length])
plt.show()
