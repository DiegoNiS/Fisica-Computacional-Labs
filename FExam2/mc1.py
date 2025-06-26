import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Punto:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0  

    def __str__(self):
        return f"Punto({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

    def random(self, x_min, x_max, y_min, y_max, z_min, z_max):
        self.x = np.random.uniform(x_min, x_max)
        self.y = np.random.uniform(y_min, y_max)
        self.z = np.random.uniform(z_min, z_max)

    def is_inside(self, condition):
        return condition(self.x, self.y, self.z)
    
N = 10000
inside =  []

def condition(x, y, z):
    if x <= 2 :
        if x + y <= 2 and x - y <= 2:
            if np.log(x + 2) >= z >= 0:
                return True    
    else:
        if x + y >= 2 and x - y >= 2:
            if np.log(6 - x) >= z >= 0:
                return True
    return False

for _ in range(N):
    p = Punto()
    p.random(-1, 5, -3, 3, 0, 2*np.log(2))
    if p.is_inside(lambda x, y, z: condition(x, y, z)):
        inside.append(p)

# -----------------------------
# GRAFICAR PUNTOS + SUPERFICIES
# -----------------------------
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Puntos Montecarlo
x_inside = [p.x for p in inside]
y_inside = [p.y for p in inside]
z_inside = [p.z for p in inside]
ax.scatter(x_inside, y_inside, z_inside, color='blue', s=3, label='Puntos dentro')

# # Superficie 1: ln(x+2)
# x1 = np.linspace(-2, 6, 10)
# y1 = np.linspace(-4, 4, 10)
# X1, Y1 = np.meshgrid(x1, y1)
# Z1 = np.log(X1 + 2)
# ax.plot_surface(X1, Y1, Z1, alpha=0.4, color='green', edgecolor='none')

# # Superficie 2: ln(6-x)
# x2 = np.linspace(-2, 6, 10)
# y2 = np.linspace(-4, 4, 10)
# X2, Y2 = np.meshgrid(x2, y2)
# Z2 = np.log(6 - X2)
# ax.plot_surface(X2, Y2, Z2, alpha=0.4, color='orange', edgecolor='none')

# # Superficie 3: plano ZY1
# y3 = np.linspace(-4, 4, 10)
# z3 = np.linspace(-1, 2*np.log(2)+1, 10)
# Y3, Z3 = np.meshgrid(y3, z3)
# X3 = -Y3 + 2
# ax.plot_surface(X3, Y3, Z3, alpha=0.4, color='purple', edgecolor='none')

# # Superficie 4: plano ZY2
# Y4 = np.linspace(-4, 4, 10)
# Z4 = np.linspace(-1, 2*np.log(2)+1, 10)
# Y4, Z4 = np.meshgrid(Y4, Z4)
# X4 = Y4 + 2
# ax.plot_surface(X4, Y4, Z4, alpha=0.4, color='red', edgecolor='none')

# # Superficie 5: plano Z = 0
# Y5 = np.linspace(-4, 4, 10)
# X5 = np.linspace(-2, 6, 10)
# Y5, X5 = np.meshgrid(Y5, X5)
# Z5 = X5 * 0 + 0
# ax.plot_surface(X5, Y5, Z5, alpha=0.4, color='yellow', edgecolor='none')

# Ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Método de Montecarlo — Puntos dentro de la región definida')

ax.legend()
plt.tight_layout()
plt.show()