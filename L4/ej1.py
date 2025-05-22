import matplotlib.pyplot as plt

k = 1
m = 2
h = 0.1  # paso de tiempo
tfin = 30

t = 0
x = 1
v = 0
n = 0

pt = [t]
px = [x]
pv = [v]
pa = []



while t <= tfin:
    a = -k * x / m #armonico(x, k, m)
    v = v + h * a
    x = x + h * v
    t = t + h
    n += 1
    pt.append(t)
    px.append(x)
    pv.append(v)
    pa.append(a)

def armonico(x, k, m):
    return -k * x / m

pa.append(armonico(x, k, m))

plt.figure(figsize=(10, 8))



plt.subplot(2, 2, 1)
plt.plot(pt, pa)
plt.grid(True)
plt.xlabel('Tiempo (s)')
plt.ylabel('Aceleración (m/s²)')
plt.axis('equal')

plt.subplot(2, 2, 2)
plt.plot(pt, pv)
plt.grid(True)
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.axis('equal')

plt.subplot(2, 2, 3)
plt.plot(pt, px)
plt.grid(True)
plt.xlabel('Tiempo (s)')
plt.ylabel('Desplazamiento (m)')
plt.axis('equal')

plt.subplot(2, 2, 4)
plt.plot(px, pv)
plt.grid(True)
plt.xlabel('Desplazamiento (m)')
plt.ylabel('Velocidad (m/s)')
plt.axis('equal')

plt.tight_layout()
plt.show()
