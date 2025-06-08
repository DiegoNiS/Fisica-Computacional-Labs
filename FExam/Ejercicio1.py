import numpy as np
import matplotlib.pyplot as plt

def show_points(t, x, n):
    indexes = np.linspace(0, len(x)-1, n, dtype=int)
    x_points = [round(x[i], 2) for i in indexes]
    t_points = [round(t[i], 2) for i in indexes]

    print('-' * 25)

    for t_val, x_val in zip(t_points, x_points):
        print(f'| {t_val:8.2f} | {x_val:10.2f} |')
    print('\n')

def show_multi_points(t, x_list, labels, n):
    indexes = np.linspace(0, len(t)-1, n, dtype=int)
    t_points = [t[i] for i in indexes]

    # Cabecera
    header = f'| {"t":>8} ' + ''.join([f'| {label:>10} ' for label in labels]) + '|'
    print(header)
    print('-' * len(header))

    # Filas
    for i in indexes:
        row = f'| {t[i]:8.2f} '
        for x in x_list:
            row += f'| {x[i]:10.2f} '
        row += '|'
        print(row)
    print('\n')

# Datos iniciales
x0 = -2.0  # posición inicial (m)
v0 = 0.5   # velocidad inicial (m/s)
a = 2.0    # aceleración constante (m/s^2)
t0 = 0.0   # tiempo inicial (s)
t_final = 10.0  # tiempo final (s)
h_inf_lim = 0.01
h_sup_lim = 2
h_values = np.linspace(h_inf_lim, h_sup_lim, 5)  # diferentes tamaños de paso para el método de Euler

# Solución analítica
t = np.linspace(t0, t_final, 500)
x_analytical = x0 + v0 * t + 0.5 * a * t**2

# Mostrar algunos puntos:
n = 10
print(f'Mustra de {n} puntos de la funcion analítica:\n')

print(f'| {"t":>8} | {"x(t)":>10} |')
show_points(t, x_analytical, 10)

# Método de Euler
def euler_method(x0, v0, a, h, t_final):
    t_values = np.arange(t0, t_final + h, h)
    x_values = [x0]
    v = v0
    for i in range(1, len(t_values)):
        x_new = x_values[-1] + v * h
        v += a * h
        x_values.append(x_new)
    return t_values, x_values

# Gráfica
plt.figure(figsize=(10, 6))
plt.plot(t, x_analytical, label='Solución analítica', color='black', linewidth=2)

x_all = [x_analytical]
labels = ['Analítica']

# Comparación para diferentes h
for h in h_values:
    t_euler, x_euler = euler_method(x0, v0, a, h, t_final)
    plt.plot(t_euler, x_euler, label=f'Método de Euler (h={h})', linestyle='--')
    if h == h_inf_lim:
        n = 10
        print(f'Mustra de {n} puntos de la funcion de Euler:\n')

        print(f'| {"t":>8} | {"x(t)":>10} |')
        show_points(t_euler, x_euler, 10)
    # Interpolamos a los mismos t que la solución analítica para la tabla final
    x_euler_interp = np.interp(t, t_euler, x_euler)
    x_all.append(x_euler_interp)
    labels.append(f'Euler h={h:.2f}')

# Tabla comparativa final
print(f'Tabla comparativa de {n} puntos:\n')
show_multi_points(t, x_all, labels, n)
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.title('Movimiento lineal con aceleración constante')
plt.legend()
plt.grid(True)
plt.show()