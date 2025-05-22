import matplotlib.pyplot as plt
import numpy as np
# Graficar una circunferencia con radio r = 3 cuyo centro esta en el origen
# condiciones iniciales 
r = 3

# Definir el número de puntos
n = 1000
# Crear un array de ángulos
theta = np.linspace(0, 2 * np.pi, n)
# Calcular las coordenadas x e y
x = r * np.cos(theta)
y = r * np.sin(theta)
# Graficar
plt.figure(figsize=(8, 8))
plt.plot(x, y, color='blue')
plt.title('Circunferencia de radio 3')
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
