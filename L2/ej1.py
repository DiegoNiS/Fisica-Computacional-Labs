import matplotlib.pyplot as plt
import numpy as np

r = 3
n = 1000
theta = np.linspace(0, 2 * np.pi, n)
x = r * np.cos(theta)
y = r * np.sin(theta)
plt.figure(figsize=(8, 8))
plt.plot(x, y, color='blue')
plt.title('Circunferencia de radio 3')
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
