import numpy as np
import matplotlib.pyplot as plt

# Inicialización de variables
xi = 0
xf = 20
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

# Método RK4 (Runge-Kutta de cuarto orden)
for i in range(n):
    x[i+1] = x[i] + h

    # RK4 para y1
    k11 = f1(x[i], y1[i], y2[i], y3[i])
    k21 = f1(x[i] + 0.5 * h, y1[i] + 0.5 * k11 * h, y2[i], y3[i])
    k31 = f1(x[i] + 0.5 * h, y1[i] + 0.5 * k21 * h, y2[i], y3[i])
    k41 = f1(x[i] + h, y1[i] + k31 * h, y2[i], y3[i])
    y1[i+1] = y1[i] + h * (k11 + 2 * k21 + 2 * k31 + k41) / 6

    # RK4 para y2
    k12 = f2(x[i], y1[i], y2[i], y3[i])
    k22 = f2(x[i] + 0.5 * h, y1[i], y2[i] + 0.5 * k12 * h, y3[i])
    k32 = f2(x[i] + 0.5 * h, y1[i], y2[i] + 0.5 * k22 * h, y3[i])
    k42 = f2(x[i] + h, y1[i], y2[i] + k32 * h, y3[i])
    y2[i+1] = y2[i] + h * (k12 + 2 * k22 + 2 * k32 + k42) / 6

    # RK4 para y3
    k13 = f3(x[i], y1[i], y2[i], y3[i])
    k23 = f3(x[i] + 0.5 * h, y1[i], y2[i], y3[i] + 0.5 * k13 * h)
    k33 = f3(x[i] + 0.5 * h, y1[i], y2[i], y3[i] + 0.5 * k23 * h)
    k43 = f3(x[i] + h, y1[i], y2[i], y3[i] + k33 * h)
    y3[i+1] = y3[i] + h * (k13 + 2 * k23 + 2 * k33 + k43) / 6

plt.figure(figsize=(12, 10))  # Figura más cuadrada para 2x2

# 1. Temperatura horizontal vs Velocidad del fluido (Y1 vs Y3)
plt.subplot(2, 2, 2)
plt.plot(y1, y3, 'b')
plt.title('Temperatura Horizontal vs Velocidad del Fluido')
plt.xlabel('Temperatura Horizontal (Y1)')
plt.ylabel('Velocidad del Fluido (Y3)')
plt.grid(True)

# 2. Temperatura vertical vs Velocidad del fluido (Y2 vs Y3)
plt.subplot(2, 2, 3)
plt.plot(y2, y3, 'g')
plt.title('Temperatura Vertical vs Velocidad del Fluido')
plt.xlabel('Temperatura Vertical (Y2)')
plt.ylabel('Velocidad del Fluido (Y3)')
plt.grid(True)

# 3. Temperatura vertical vs Temperatura horizontal (Y2 vs Y1)
plt.subplot(2, 2, 1)
plt.plot(y2, y1, 'r')
plt.title('Temperatura Vertical vs Temperatura Horizontal')
plt.xlabel('Temperatura Vertical (Y2)')
plt.ylabel('Temperatura Horizontal (Y1)')
plt.grid(True)

# 4. Velocidad del fluido vs Tiempo (Y3 vs X)
plt.subplot(2, 2, 4)
plt.plot(x, y3, 'm')
plt.title('Velocidad del Fluido vs Tiempo')
plt.xlabel('Tiempo (X)')
plt.ylabel('Velocidad del Fluido (Y3)')
plt.grid(True)

plt.tight_layout()
plt.show()