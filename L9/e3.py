import numpy as np
import matplotlib.pyplot as plt

# Inicialización de variables
xi = 0
xf = 60
h = 0.001
n = int((xf - xi) / h) # Convertir a entero para el rango

# Inicialización de arrays (Python usa índices base 0)
x = np.zeros(n + 1)
y1 = np.zeros(n + 1)
y2 = np.zeros(n + 1)
y3 = np.zeros(n + 1)

x[0] = xi
y1[0] = 5
y2[0] = 5
y3[0] = 5

# Definición de las funciones derivadas (Lorenz system-like)
def f1(x_val, y1_val, y2_val, y3_val):
    """Función 1 derivada: dy1/dx"""
    return 10 * (y2_val - y1_val)

def f2(x_val, y1_val, y2_val, y3_val):
    """Función 2 derivada: dy2/dx"""
    return y1_val * (28 - y3_val) - y2_val

def f3(x_val, y1_val, y2_val, y3_val):
    """Función 3 derivada: dy3/dx"""
    return y1_val * y2_val - (8/3) * y3_val

# Reutilizamos funciones f1, f2, f3 y valores h, n, xi ya definidos arriba

# --------- Primera simulación (x = 5) ---------
y1_a = np.zeros(n + 1)
y2_a = np.zeros(n + 1)
y3_a = np.zeros(n + 1)
x_vals = np.zeros(n + 1)

y1_a[0] = 5
y2_a[0] = 5
y3_a[0] = 5
x_vals[0] = xi

for i in range(n):
    x_vals[i+1] = x_vals[i] + h

    # RK4 para y1
    k11 = f1(x_vals[i], y1_a[i], y2_a[i], y3_a[i])
    k21 = f1(x_vals[i] + 0.5 * h, y1_a[i] + 0.5 * k11 * h, y2_a[i], y3_a[i])
    k31 = f1(x_vals[i] + 0.5 * h, y1_a[i] + 0.5 * k21 * h, y2_a[i], y3_a[i])
    k41 = f1(x_vals[i] + h, y1_a[i] + k31 * h, y2_a[i], y3_a[i])
    y1_a[i+1] = y1_a[i] + h * (k11 + 2*k21 + 2*k31 + k41) / 6

    # RK4 para y2
    k12 = f2(x_vals[i], y1_a[i], y2_a[i], y3_a[i])
    k22 = f2(x_vals[i] + 0.5 * h, y1_a[i], y2_a[i] + 0.5 * k12 * h, y3_a[i])
    k32 = f2(x_vals[i] + 0.5 * h, y1_a[i], y2_a[i] + 0.5 * k22 * h, y3_a[i])
    k42 = f2(x_vals[i] + h, y1_a[i], y2_a[i] + k32 * h, y3_a[i])
    y2_a[i+1] = y2_a[i] + h * (k12 + 2*k22 + 2*k32 + k42) / 6

    # RK4 para y3
    k13 = f3(x_vals[i], y1_a[i], y2_a[i], y3_a[i])
    k23 = f3(x_vals[i] + 0.5 * h, y1_a[i], y2_a[i], y3_a[i] + 0.5 * k13 * h)
    k33 = f3(x_vals[i] + 0.5 * h, y1_a[i], y2_a[i], y3_a[i] + 0.5 * k23 * h)
    k43 = f3(x_vals[i] + h, y1_a[i], y2_a[i], y3_a[i] + k33 * h)
    y3_a[i+1] = y3_a[i] + h * (k13 + 2*k23 + 2*k33 + k43) / 6

# --------- Segunda simulación (x = 5.00000001) ---------
y1_b = np.zeros(n + 1)
y2_b = np.zeros(n + 1)
y3_b = np.zeros(n + 1)

y1_b[0] = 5.00000001
y2_b[0] = 5
y3_b[0] = 5

for i in range(n):
    # RK4 para y1
    k11 = f1(x_vals[i], y1_b[i], y2_b[i], y3_b[i])
    k21 = f1(x_vals[i] + 0.5 * h, y1_b[i] + 0.5 * k11 * h, y2_b[i], y3_b[i])
    k31 = f1(x_vals[i] + 0.5 * h, y1_b[i] + 0.5 * k21 * h, y2_b[i], y3_b[i])
    k41 = f1(x_vals[i] + h, y1_b[i] + k31 * h, y2_b[i], y3_b[i])
    y1_b[i+1] = y1_b[i] + h * (k11 + 2*k21 + 2*k31 + k41) / 6

    # RK4 para y2
    k12 = f2(x_vals[i], y1_b[i], y2_b[i], y3_b[i])
    k22 = f2(x_vals[i] + 0.5 * h, y1_b[i], y2_b[i] + 0.5 * k12 * h, y3_b[i])
    k32 = f2(x_vals[i] + 0.5 * h, y1_b[i], y2_b[i] + 0.5 * k22 * h, y3_b[i])
    k42 = f2(x_vals[i] + h, y1_b[i], y2_b[i] + k32 * h, y3_b[i])
    y2_b[i+1] = y2_b[i] + h * (k12 + 2*k22 + 2*k32 + k42) / 6

    # RK4 para y3
    k13 = f3(x_vals[i], y1_b[i], y2_b[i], y3_b[i])
    k23 = f3(x_vals[i] + 0.5 * h, y1_b[i], y2_b[i], y3_b[i] + 0.5 * k13 * h)
    k33 = f3(x_vals[i] + 0.5 * h, y1_b[i], y2_b[i], y3_b[i] + 0.5 * k23 * h)
    k43 = f3(x_vals[i] + h, y1_b[i], y2_b[i], y3_b[i] + k33 * h)
    y3_b[i+1] = y3_b[i] + h * (k13 + 2*k23 + 2*k33 + k43) / 6

# --------- Graficar comparación ---------
plt.figure(figsize=(10, 5))
plt.plot(x_vals, y1_a, label='x₀ = 5', linewidth=1)
plt.plot(x_vals, y1_b, label='x₀ = 5.00000001', linewidth=1, linestyle='--')
plt.title('Sensibilidad a las Condiciones Iniciales: x(t)')
plt.xlabel('Tiempo (t)')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
