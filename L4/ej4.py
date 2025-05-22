import matplotlib.pyplot as plt

# Parámetros del sistema
k = 0.1          # sin resorte
m = 0.2        # masa en kg
c = 0.05        # fricción viscosa
h = 0.01       # paso de tiempo
tfin = 60     # duración de la simulación

# Condiciones iniciales
t = 0
x = 0
v = -2

# Listas para almacenar los resultados
pt = [t]
px = [x]
pv = [v]
pa = []

# Simulación con integración de Euler
while t <= tfin:
    a = - (k * x + c * v) / m
    v = v + h * a
    x = x + h * v
    t = t + h
    pt.append(t)
    px.append(x)
    pv.append(v)
    pa.append(a)

# Ajustar longitud de pa (una iteración menos)
pa.append(pa[-1])  # repetir último valor

# === Graficar ===
plt.figure(figsize=(10, 8))

# x vs t
plt.subplot(2, 2, 1)
plt.plot(pt, px, color='blue')
plt.xlabel('Tiempo (t)')
plt.ylabel('Posición (x)')
plt.title('x vs t')
plt.grid(True)

# v vs t
plt.subplot(2, 2, 2)
plt.plot(pt, pv, color='red')
plt.xlabel('Tiempo (t)')
plt.ylabel('Velocidad (v)')
plt.title('v vs t')
plt.grid(True)

# a vs t
plt.subplot(2, 2, 3)
plt.plot(pt, pa, color='green')
plt.xlabel('Tiempo (t)')
plt.ylabel('Aceleración (a)')
plt.title('a vs t')
plt.grid(True)

# v vs x
plt.subplot(2, 2, 4)
plt.plot(px, pv, color='purple')
plt.xlabel('Posición (x)')
plt.ylabel('Velocidad (v)')
plt.title('v vs x')
plt.grid(True)

plt.tight_layout()
plt.show()
