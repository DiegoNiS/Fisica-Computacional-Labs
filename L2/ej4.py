import numpy as np
import matplotlib.pyplot as plt

def orbita(x0, y0, vx0, vy0, h=0.01, t_max=50000, radio_planeta=3):
    x, y = x0, y0
    vx, vy = vx0, vy0
    
    px, py = [], []
    
    for _ in range(t_max):
        r2 = x**2 + y**2
        r = np.sqrt(r2)
        
        # Aceleración gravitacional
        ax = -x / r2**(3/2)
        ay = -y / r2**(3/2)
        
        # Actualizar velocidades
        vx += h * ax
        vy += h * ay
        
        # Actualizar posiciones
        x += h * vx
        y += h * vy
        
        # Si está fuera del planeta, guardar para graficar
        if r > radio_planeta:
            px.append(x)
            py.append(y)
        else:
            break
        # Si colisiona, NO se guarda, pero la simulación sigue

    return px, py

# Puedes modificar aquí tus condiciones iniciales:
x0 = 4
y0 = 0
vx0 = 0.0
vy0 = 0.2  # prueba también valores menores o mayores

# Simular trayectoria
px1, py1 = orbita(x0, y0, vx0, -vy0)
px2, py2 = orbita(x0, y0, vx0, -vy0 * 1.5)  # Otra trayectoria para comparar

px3, py3 = orbita(x0, y0, vx0, -vy0 * 3)  # Otra trayectoria para comparar
px4, py4 = orbita(x0, y0, vx0, -vy0 * 3.3)  # Otra trayectoria para comparar

px5, py5 = orbita(x0, y0, vx0, -vy0 * 4.5)  # Otra trayectoria para comparar
px6, py6 = orbita(x0, y0, vx0, -vy0 * 5.5)  # Otra trayectoria para comparar


# Graficar resultado
plt.figure(figsize=(8, 8))
plt.plot(px1, py1, label='Trayectoria orbital')
plt.plot(px2, py2, label='Trayectoria orbital (v0 * 1.5)')
plt.plot(px3, py3, label='Trayectoria orbital (v0 * 2.5)')
plt.plot(px4, py4, label='Trayectoria orbital (v0 * 3.5)')
plt.plot(px5, py5, label='Trayectoria orbital (v0 * 4.5)')
plt.plot(px6, py6, label='Trayectoria orbital (v0 * 5.5)')
circle = plt.Circle((0, 0), 3, color='gray', fill=True, alpha=0.3, label='Planeta (radio=3)')
plt.gca().add_patch(circle)
plt.plot(0, 0, 'ro', label='Centro de atracción')
# ver solo en el grafico y de 0 a 15
plt.ylim(0, 15)
plt.gca().set_ylim(0, 15)  # fuerza el límite duro

plt.axis('equal')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Órbita con colisión: trayectoria se detiene si entra en la esfera')
plt.legend()
plt.show()
