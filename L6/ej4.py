import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n = 3
radio = 3
I = 1.0
mu0_4pi = 1e-7

angulos = np.linspace(0, 2*np.pi, n, endpoint=False)
x_cargas = radio * np.cos(angulos)
y_cargas = radio * np.sin(angulos)
z_cargas = np.zeros_like(x_cargas)

x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)
z = np.linspace(-5, 5, 10)

X, Y, Z = np.meshgrid(x, y, z)

Bx = np.zeros_like(X)
By = np.zeros_like(Y)
Bz = np.zeros_like(Z)

for (x0, y0, z0) in zip(x_cargas, y_cargas, z_cargas):
    dx = X - x0
    dy = Y - y0
    dz = Z - z0
    r2 = dx**2 + dy**2 + dz**2 + 0.1
    r = np.sqrt(r2)

    Bx += -mu0_4pi * I * dy / r2
    By +=  mu0_4pi * I * dx / r2

# Escalar para que se vean los vectores
factor_escala = 5e7
Bx_scaled = Bx * factor_escala
By_scaled = By * factor_escala
Bz_scaled = Bz * factor_escala

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')


step = 2
ax.quiver(X[::step, ::step, ::step], Y[::step, ::step, ::step], Z[::step, ::step, ::step],
          Bx_scaled[::step, ::step, ::step], By_scaled[::step, ::step, ::step], Bz_scaled[::step, ::step, ::step],
          length=0.5, normalize=False, color='r')

ax.scatter(x_cargas, y_cargas, z_cargas, color='b', s=60)

ax.set_xlim([-6, 6])
ax.set_ylim([-6, 6])
ax.set_zlim([-6, 6])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Campo magnético 3D con tamaño proporcional a intensidad')

plt.show()


# step = 1
# ax.quiver(X[::step, ::step, ::step], Y[::step, ::step, ::step], Z[::step, ::step, ::step],
#           Bx_scaled[::step, ::step, ::step], By_scaled[::step, ::step, ::step], Bz_scaled[::step, ::step, ::step],
#           length=0.5, normalize=False, color='r')

# ax.scatter(x_cargas, y_cargas, z_cargas, color='b', s=60)

# ax.set_xlim([-6, 6])
# ax.set_ylim([-6, 6])
# ax.set_zlim([-6, 6])

# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('Campo magnético 3D con tamaño proporcional a intensidad')

# plt.show()
