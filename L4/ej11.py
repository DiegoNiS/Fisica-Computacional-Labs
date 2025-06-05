import numpy as np
import matplotlib.pyplot as plt

m1 = 1
m2 = 1
l = 1
n = 2

k1 = m1 * l**2  
k2 = m2 * n**2  

x0 = 1
vx0 = 2.3
y0 = 1
vy0 = 0

h = 0.001  
tfin = 20
t = np.arange(0, tfin, h)

x = [x0]
vx = [vx0]
y = [y0]
vy = [vy0]

for i in range(len(t)-1):
    ax = -k1/m1 * x[-1]
    ay = -k2/m2 * y[-1]
    
    vx_new = vx[-1] + h * ax
    x_new = x[-1] + h * vx[-1]
    
    vy_new = vy[-1] + h * ay
    y_new = y[-1] + h * vy[-1]
    
    vx.append(vx_new)
    x.append(x_new)
    
    vy.append(vy_new)
    y.append(y_new)

plt.figure(figsize=(8,8))
plt.plot(x, y, color='purple')
plt.title(f'Figura de Lissajous para l={l}, n={n}')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')
plt.show()
