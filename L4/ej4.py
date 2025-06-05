import matplotlib.pyplot as plt

k = 0.1   
m = 0.2   
c = 0.05 
h = 0.01 
tfin = 60 

t = 0
x = 0
v = -2

pt = [t]
px = [x]
pv = [v]
pa = []

while t <= tfin:
    a = - (k * x + c * v) / m
    v = v + h * a
    x = x + h * v
    t = t + h
    pt.append(t)
    px.append(x)
    pv.append(v)
    pa.append(a)

pa.append(pa[-1]) 

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(pt, px, color='blue')
plt.xlabel('Tiempo (t)')
plt.ylabel('Posición (x)')
plt.title('x vs t')
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(pt, pv, color='red')
plt.xlabel('Tiempo (t)')
plt.ylabel('Velocidad (v)')
plt.title('v vs t')
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(pt, pa, color='green')
plt.xlabel('Tiempo (t)')
plt.ylabel('Aceleración (a)')
plt.title('a vs t')
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(px, pv, color='purple')
plt.xlabel('Posición (x)')
plt.ylabel('Velocidad (v)')
plt.title('v vs x')
plt.grid(True)

plt.tight_layout()
plt.show()
