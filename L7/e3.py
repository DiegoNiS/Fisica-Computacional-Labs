import numpy as np
import matplotlib.pyplot as plt

# Parámetros
v = 1.0
t = 0  # Solo una onda en un instante de tiempo
h = 1
x_resolution = 0.01
num_periodos = 5
x_vals = np.arange(0, num_periodos * 2 * np.pi, x_resolution)

# Segmentos del ciclo
segment_length = (2 * np.pi) / 6

# Crear figura
plt.figure(figsize=(12, 4))
plt.title("Onda Trapezoidal Periódica (5 periodos)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Colores para cada periodo
colores = ['r', 'g', 'b', 'm', 'c']

# Construcción de la onda para un solo instante t
for i in range(num_periodos):
    px = []
    py = []
    for ix in np.arange(0, 2 * np.pi, x_resolution):
        x = ix + i * 2 * np.pi
        ciclo = ix

        if 0 <= ciclo < segment_length:
            y = (3 * h / np.pi) * ciclo
        elif segment_length <= ciclo < 2 * segment_length:
            y = h
        elif 2 * segment_length <= ciclo < 3 * segment_length:
            y = - (3 * h / np.pi) * (ciclo - 2 * segment_length) + h
        elif 3 * segment_length <= ciclo < 4 * segment_length:
            y = - (3 * h / np.pi) * (ciclo - 3 * segment_length)
        elif 4 * segment_length <= ciclo < 5 * segment_length:
            y = -h
        elif 5 * segment_length <= ciclo < 2 * np.pi:
            y = (3 * h / np.pi) * (ciclo - 5 * segment_length) - h
        else:
            y = np.nan

        px.append(x)
        py.append(y)

    plt.plot(px, py, color=colores[i % len(colores)], linewidth=2, label=f"Periodo {i+1}")

plt.ylim([-2.5, 2.5])
plt.xlim([0, num_periodos * 2 * np.pi])
plt.legend()
plt.show()
