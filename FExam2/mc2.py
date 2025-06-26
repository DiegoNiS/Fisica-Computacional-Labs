import numpy as np
import matplotlib.pyplot as plt

# Número de puntos
N = 100000

# Rango en x y z
x_min, x_max = 0, 2
z_min_func = lambda x: 0
z_max_func = lambda x: 2 - x

# Generar x y z aleatorios
x_rand = np.random.uniform(x_min, x_max, N)
z_rand = np.random.uniform(0, z_max_func(x_rand))

# Rango en y depende de x y z: y^2 <= x(2 - z)/4
y_max = np.sqrt(x_rand * (2 - z_rand) / 4)
y_rand = np.random.uniform(-y_max, y_max)

# Verificamos si están dentro de la superficie
inside = 4 * y_rand**2 <= x_rand * (2 - z_rand)

# Volumen de la caja contenedora
vol_caja = (x_max - x_min) * 2 * np.max(y_max) * np.max(z_max_func(np.array([x_min, x_max])))
vol_estimado = vol_caja * np.sum(inside) / N

print(f"Volumen estimado: {vol_estimado:.6f}")

# Graficar una muestra
sample = 5000
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_rand[:sample], y_rand[:sample], z_rand[:sample], c=inside[:sample], cmap='coolwarm', s=1)
ax.set_title('Montecarlo: Volumen bajo superficie cónica')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.tight_layout()
plt.savefig('images/mc2.png')
plt.show()
