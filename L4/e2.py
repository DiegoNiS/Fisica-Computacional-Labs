import matplotlib.pyplot as plt

k = 0.1
m = 0.2
h = 0.01  
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
    a = -k * x / m  
    v = v + h * a
    x = x + h * v
    t = t + h
    n += 1
    pt.append(t)
    px.append(x)
    pv.append(v)
    pa.append(a)

def EU(k, x):
    return 0.5 * k * x**2

def EK(m, v):
    return 0.5 * m * v**2

def ET(EK, EU):
    return EK + EU

energia_potencial = [EU(k, xi) for xi in px]
energia_cinetica = [EK(m, vi) for vi in pv]
energia_total = [ET(EK(m, vi), EU(k, xi)) for xi, vi in zip(px, pv)]

plt.figure(figsize=(10, 6))
plt.plot(px, energia_potencial, label='Energía Potencial (U)', color='blue')
plt.plot(px, energia_cinetica, label='Energía Cinética (K)', color='red')
plt.plot(px, energia_total, label='Energía Total (E)', color='green')
plt.xlabel('Desplazamiento (x)')
plt.ylabel('Energía')
plt.title('Energías del sistema en función de la posición')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
